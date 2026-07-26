
**MPLS TE \-- MPLS TE配置命令 \-- auto-bandwidth enable**

------------------------------------------------------------------------

![说明](MPLS%20TE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[auto-bandwidth enable**]命令用来全局开启自动带宽调整功能，并配置出口速率采样的时间间隔。

**[undo auto-bandwidth enable**]命令用来全局关闭自动带宽调整功能。

【命令】

**[auto-bandwidth**] **enable** [ **sample-interval** *seconds* ]

**[undo auto-bandwidth enable**]

【缺省情况】

全局自动带宽调整功能处于关闭状态。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sample-interval**] *seconds*：指定为配置了自动带宽调整功能的隧道进行出口速率采样的时间间隔。*seconds*的取值范围为1～604800，单位为秒，缺省值300秒。建议使用缺省值。

【使用指导】

自动带宽调整功能是指对隧道的平均出口速率进行测量，并周期性地根据测量结果调整隧道的带宽，以便根据用户的业务量自动调整为MPLS TE隧道分配的带宽。

出口速率采样功能是指设备根据在出口速率采样时间间隔内通过的流量大小，计算平均出口速率。

通过本命令全局开启自动带宽调整功能后，还需要在Tunnel接口视图下执行**mpls te auto-bandwidth adjustment**命令，才能实现对该隧道进行自动带宽调整。

【举例】

\# 全局开启自动带宽调整功能，配置对MPLS TE隧道的出口速率每隔10分钟（600秒）进行一次采样。

\<Sysname\> system-view

Sysname mpls te

Sysname-te auto-bandwidth enable sample-interval 600

【相关命令】

·**mpls te auto-bandwidth**

·**reset mpls te auto-bandwidth-adjustment timers**

**MPLS TE \-- MPLS TE配置命令 \-- auto-tunnel backup**

------------------------------------------------------------------------

**[auto-tunnel backup**]命令用来全局开启自动隧道备份功能，并进入MPLS TE自动隧道备份视图。

**[undo auto-tunnel backup**]命令用来全局关闭自动隧道备份功能。

【命令】

**[auto-tunnel backup**]

**[undo auto-tunnel backup**]

【缺省情况】

自动隧道备份功能处于全局关闭状态。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过本命令全局开启自动隧道备份功能，并通过**tunnel-number**命令配置自动创建的Bypass隧道的接口编号范围后，本地设备会自动为经过本设备、且开启了FRR功能的所有MPLS TE隧道建立两条Bypass隧道：一条链路保护的Bypass隧道和一条节点保护的Bypass隧道。

需要注意的是：

·执行**undo auto-tunnel backup**命令后，MPLS TE会删除所有已经自动建立的Bypass隧道。

·倒数第二跳节点作为PLR时，只自动创建链路保护类型的Bypass隧道，不会自动创建节点保护类型的Bypass隧道。

【举例】

\# 全局开启自动隧道备份功能，并进入MPLS TE自动隧道备份视图。

\<Sysname\> system-view

Sysname mpls te

Sysname-te auto-tunnel backup

Sysname-te-auto-bk

【相关命令】

·**mpls te auto-ba****ckup disable**

·**nhop-only**

·**timers removal unused**

·**tunnel-number**

**MPLS TE \-- MPLS TE配置命令 \-- destination**

------------------------------------------------------------------------

**[destination**]命令用来配置Tunnel-Bundle接口的隧道目的端地址。

**[undo destination**]命令用来恢复缺省情况。

【命令】

**[destination**]*ip-address*

**[undo destination**]

【缺省情况】

未指定Tunnel-Bundle接口的隧道目的端地址。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：隧道的目的端IPv4地址。

【使用指导】

MPLS L3VPN、MPLS L2VPN和VPLS根据本命令配置的隧道目的端地址，选择承载VPN业务的公网隧道。即：远端PE的地址与Tunnel-Bundle接口的隧道目的端地址相同时，该捆绑隧道可以作为MPLS L3VPN、MPLS L2VPN和VPLS的公网隧道。

建议为成员接口和Tunnel-Bundle接口配置相同的目的端地址。如果不同，则需要确保通过成员接口能够到达Tunnel-Bundle接口的目的端地址；否则，会导致流量转发不通。

【举例】

\# 设置隧道捆绑接口Tunnel-Bundle2的隧道目的端地址为2.2.2.2。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 destination 2.2.2.2

【相关命令】

·**display tunnel-bundle**

**MPLS TE \-- MPLS TE配置命令 \-- disable**

------------------------------------------------------------------------

**[disable**]命令用来禁用当前显式路径。

**[undo disable**]命令用来恢复缺省情况。

【命令】

**[disable**]

**[undo disable**]

【缺省情况】

显式路径可用。

【视图】

显式路径视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[disable**]命令用来防止显式路径在配置过程中错误地被隧道引用，错误地建立隧道。

【举例】

\# 禁用名为path1的显式路径。

\<Sysname\> system-view

Sysname explicit-path path1

Sysname-explicit-path-path1 disable

**MPLS TE \-- MPLS TE配置命令 \-- display explicit-path**

------------------------------------------------------------------------

**[display explicit-path**]命令用来显示显式路径的信息。

【命令】

**[display explicit-path** [ *path-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[path-name*]：显示指定显式路径的信息。*path-name*表示显式路径名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有显式路径的信息。

【举例】

\# 显示所有显式路径的信息。

\<Sysname\> display explicit-path

Path Name: path1      Hop Count: 3     Path Status: Enabled

Index     IP Address             Hop Type    Hop Attribute

1         1.1.1.1                Strict      Include

101       2.2.2.2                Loose       Include

201       3.3.3.3                  -         Exclude

表1-1 display explicit-path命令显示信息描述表

字段

描述

Path Name

显式路径名称

Hop Count

显式路径中配置的节点数

Path Status

显式路径状态，取值包括：

·Enabled：表示显式路径可用

·Disabled：表示显式路径不可用

Index

显式路径中节点的索引

IP Address

显式路径中节点的IP地址

Hop Type

节点的类型，取值包括Strict和Loose

Hop Attribute

节点的属性，取值包括Include和Exclude

**MPLS TE \-- MPLS TE配置命令 \-- display isis mpls te advertisement**

------------------------------------------------------------------------

**[display isis mpls te advertisement**]命令用来显示IS-IS TEDB中的链路和节点信息。

【命令】

**[display isis mpls te**  **advertisement** [ [ **level-1** \| **level-2** ] \| [ **originate-system** *system-id* \| **local** ] \| **verbose** ] \*  *process-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：显示Level-1路由器的链路和节点信息。

**[level-2**]：显示Level-2路由器的链路和节点信息。

**[originate-system**] *system-id*：显示指定系统发布的链路和节点信息。*system-id*为系统ID，形式为XXXX.XXXX.XXXX。

**[local**]：显示本地发布的链路和节点信息。

**[verbose**]：显示详细信息。如果不指定本参数，则显示简要信息。

*[process-id*]：显示指定IS-IS进程的信息。*process-id*为IS-IS进程号，取值范围为1～65535。如果不指定本参数，则显示所有IS-IS进程的信息。

【使用指导】

执行本命令时，如果没有指定**level-1**和**level-2**参数，则同时显示Level-1路由器和Level-2路由器的信息；如果没有指定**originate-system** *system-id*和**local**参数，则显示所有系统发布的信息。

【举例】

\# 显示IS-IS TEDB中Level-1路由器的链路和节点简要信息。

\<Sysname\> display isis mpls te advertisement level-1

TE information for IS-IS(1)

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Level-1 TE node and link information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Node total count   : 2

Node index         : 0

  System ID        : 0000.0000.0004

  MPLS LSR ID      : 4.4.4.4

  Node flags       : -/-/R/-

  Link total count : 1

  Link information :

    Neighbour           Frag ID   Link Type   Local Address    Remote Address

    0000.0000.0004.04   0x00      Broadcast   1.1.1.3

Node index         : 1

  System ID        : 0000.0000.0001

  MPLS LSR ID      : 1.1.1.1

  Node flags       : -/-/R/-

  Link total count : 1

  Link information :

    Neighbour           Frag ID   Link Type   Local Address    Remote Address

    0000.0000.0004.04   0x00      Broadcast   1.1.1.1          \--

\# 显示IS-IS TEDB中Level-1路由器的链路和节点详细信息。

\<Sysname\> display isis mpls te advertisement level-1 local verbose

                           TE information for IS-IS(1)

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Level-1 TE node and link information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Node total count   : 2

Node index         : 0

  System ID        : 0000.0000.0004

  MPLS LSR ID      : 4.4.4.4

  Node flags       : -/-/R/-

  Link total count : 1

  Link information :

  Link index   : 0

    Neighbor   : 0000.0000.0004.04       Frag ID     : 0x00

    Link type  : Broadcast               Admin group : 0x00000000

    IGP metric : 10                      TE metric   : 10

    Link flags : -/-/-

    Physical bandwidth: 12500000 bytes/sec

    Reservable bandwidth: 0 bytes/sec

    Unreserved bandwidth for each TE class:

      TE class  0: 0 bytes/sec           TE class  1: 0 bytes/sec

      TE class  2: 0 bytes/sec           TE class  3: 0 bytes/sec

      TE class  4: 0 bytes/sec           TE class  5: 0 bytes/sec

      TE class  6: 0 bytes/sec           TE class  7: 0 bytes/sec

      TE class  8: 0 bytes/sec           TE class  9: 0 bytes/sec

      TE class 10: 0 bytes/sec           TE class 11: 0 bytes/sec

      TE class 12: 0 bytes/sec           TE class 13: 0 bytes/sec

      TE class 14: 0 bytes/sec           TE class 15: 0 bytes/sec

    Bandwidth constraint model: Prestandard DS-TE RDM

    Bandwidth constraints:

      BC[00: 0 bytes/sec                BC01: 0 bytes/sec]

    Local address: 1.1.1.3

Node index         : 1

  System ID        : 0000.0000.0001

  MPLS LSR ID      : 1.1.1.1

  Node flags       : -/-/-/-

  Link total count : 1

  Link information :

  Link index  : 0

    Neighbor  : 0000.0000.0004.04        Frag ID     : 0x00

    Link type : Broadcast                Admin group : 0x00000000

    IGP metric: 10                       TE metric   : 10

    Link flags: -/-/-

    Physical bandwidth: 12500000 bytes/sec

    Reservable bandwidth: 0 bytes/sec

    Unreserved bandwidth for each TE class:

      TE class  0: 0 bytes/sec           TE class  1: 0 bytes/sec

      TE class  2: 0 bytes/sec           TE class  3: 0 bytes/sec

      TE class  4: 0 bytes/sec           TE class  5: 0 bytes/sec

      TE class  6: 0 bytes/sec           TE class  7: 0 bytes/sec

      TE class  8: 0 bytes/sec           TE class  9: 0 bytes/sec

      TE class 10: 0 bytes/sec           TE class 11: 0 bytes/sec

      TE class 12: 0 bytes/sec           TE class 13: 0 bytes/sec

      TE class 14: 0 bytes/sec           TE class 15: 0 bytes/sec

    Bandwidth constraint model: Prestandard DS-TE RDM

    Bandwidth constraints:

      BC[00: 0 bytes/sec                BC01: 0 bytes/sec]

    Local address: 1.1.1.1

表1-2 display isis mpls te advertisement命令显示信息描述表

字段

描述

TE information for IS-IS(1)

指定IS-IS进程的TE信息

Level-1 TE node and link information

Level-1路由器的TE信息

Level-2 TE node and link information

Level-2路由器的TE信息

Node total count

发布TE信息的节点个数

Node index

发布TE信息的节点索引

System ID

节点的系统ID

MPLS LSR ID

节点的MPLS LSR ID

Node flags

节点信息的状态标记，取值包括：

·A：节点信息成功同步到CSPF

·S：向CSPF同步节点信息失败后，准备再次向CSPF同步

·R：表示到达该节点的路由可达

·O：节点处于overload状态

Link total count

节点发布的链路数目

Link information

节点发布的链路信息

Link index

链路索引

Neighbor

邻居系统ID

Frag ID

LSP分片号

Link type

该条链路的链路类型，取值包括：

·Broadcast：表示广播链路

·P2P：表示点对点链路

Admin group

链路管理组属性

IGP metric

IGP开销值

 

TE metric

TE开销值

Link flags

链路信息的状态标记，取值包括：

·A：链路信息成功同步到CSPF

·U：向CSPF同步更新链路信息失败后，准备再次向CSPF同步

·D：向CSPF同步删除链路信息失败后，准备再次向CSPF同步

Physical bandwidth

物理带宽

Reservable bandwidth

可预留带宽

 

Unreserved bandwidth for each TE class

每个TE class的未预留带宽

 

TE class 0-15

16个TE class各自的未预留带宽

 

Bandwidth constraint model

带宽约束模型，取值包括：

·Prestandard DS-TE RDM

·IETF DS-TE RDM

·IETF DS-TE MAM

 

Bandwidth constraints

带宽约束

 

BC

各个带宽约束值（Prestandard模式支持2个BC，IETF模式支持4个BC）

 

Local address

该条链路的本地IP地址

Remote address

该条链路的对端IP地址

**MPLS TE \-- MPLS TE配置命令 \-- display isis mpls te configured-sub-tlvs**

------------------------------------------------------------------------

**[display isis mpls te configured-sub-tlvs**]命令用来显示IS-IS TE配置的子TLV类型值信息。

【命令】

**[display isis mpls te** **configured-sub-tlvs** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定IS-IS进程的信息。*process-id*为IS-IS进程号，取值范围为1～65535。如果不指定本参数，则显示所有IS-IS进程的信息。

【举例】

\# 显示IS-IS TE配置的子TLV类型值信息。

\<Sysname\> display isis mpls te configured-sub-tlvs

TE sub-TLV information for IS-IS(1)

                      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

  Type value of the unreserved sub-pool bandwidth sub-TLV : 251

  Type value of the bandwidth constraint sub-TLV          : 252

表1-3 display isis mpls te configured-sub-tlvs命令显示信息描述表

字段

描述

TE Sub-TLV Information for IS-IS(1)

指定进程配置的DS-TE子TLV类型值E

Type value of the unreserved subpool bandwidth sub-TLV

可用子池带宽子TLV的类型值

Type value of the bandwidth constraint sub-TLV

带宽约束子TLV的类型值

**MPLS TE \-- MPLS TE配置命令 \-- display isis mpls te network**

------------------------------------------------------------------------

**[display isis mpls te network**]命令用来显示IS-IS TEDB中的网络信息。

【命令】

**[display isis mpls te**[ **network** [ [ **level-1** \| **level-2** ] \| **local** \| **lsp-id** *lsp-id* ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：显示Level-1路由器的网络信息。

**[level-2**]：显示Level-2路由器的网络信息。

**[local**]：显示本地发布的网络信息。

**[lsp-id*** lsp-id*]：显示指定LSP的网络信息。*lsp-id*为LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的节点或伪节点的SystemID，Pseudonode ID是伪节点ID，fragment num是该LSP的分片号。

*[process-id*]：显示指定IS-IS进程的信息。*process-id*为IS-IS进程号，取值范围为1～65535。如果不指定本参数，则显示所有IS-IS进程的信息。

【使用指导】

执行本命令时，如果没有指定**level-1**和**level-2**参数，则同时显示Level-1路由器和Level-2路由器的信息；如果没有指定**local**和**lsp-id*** lsp-id*参数，则显示所有网络的信息。

【举例】

\# 显示IS-IS TEDB中Level-1路由器和Level-2路由器的网络信息。

\<Sysname\> display isis mpls te network

TE information for IS-IS(1)

     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Level-1 network information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LAN ID             : 0000.0000.0004.04

Frag ID            : 0x00

Flags              : -/-/-

Attached routers   : 0000.0000.0001

                     0000.0000.0004

Level-2 Network Information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LAN ID             : 0000.0000.0004.04

Frag ID            : 0x00

Flags              : -/-/-

Attached routers   : 0000.0000.0001

                     0000.0000.0004

表1-4 display isis mpls te network命令显示信息描述表

字段

描述

TE information for IS-IS(1)

指定IS-IS进程的TE信息

Level-1 TE Network Information

Level-1的TE网络信息

Level-2 TE Network Information

Level-2的TE网络信息

LAN ID

广播网络ID，形式为System-ID.Pseudonode-ID

Frag ID

LSP分片号

Flags

网络信息的状态标记：

·A：网络信息已成功同步到CSPF

·U：向CSPF同步更新网络信息失败后，准备再次向CSPF同步

·D：向CSPF同步删除网络信息失败后，准备再次向CSPF同步

Attached routers

相连路由器列表

**MPLS TE \-- MPLS TE配置命令 \-- display isis mpls te tunnel**

------------------------------------------------------------------------

**[display isis mpls te tunnel**]命令用来显示IS-IS的Tunnel接口信息。

【命令】

**[display isis mpls te**[ **tunnel** [ **level-1** \| **level-2** ]  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level-1**]：显示Level-1路由器的Tunnel接口信息。

**[level-2**]：显示Level-2路由器的Tunnel接口信息。

*[process-id*]：显示指定IS-IS进程的信息。*process-id*为IS-IS进程号，取值范围为1～65535。如果不指定本参数，则显示所有IS-IS进程的信息。

【使用指导】

执行本命令时，如果没有指定**level-1**和**level-2**参数，则同时显示Level-1路由器和Level-2路由器的信息。

【举例】

\# 显示IS-IS的Tunnel接口信息。

\<Sysname\> display isis mpls te tunnel

                    MPLS-TE tunnel information for IS-IS(1)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

                           Level-1 Tunnel Statistics

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Tunnel Name      Auto Route       Destination      Metric

   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   Tun0             Advertise        2.2.2.2          Relative 0

                           Level-2 Tunnel Statistics

                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Tunnel Name      Auto Route       Destination      Metric

   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

   Tun0             Advertise        2.2.2.2          Relative 0

表1-5 display isis mpls te tunnel命令显示信息描述表

字段

描述

MPLS-TE tunnel information for IS-IS(1)

指定IS-IS进程的MPLS TE隧道接口信息

Level-1 Tunnel Statistics

Level-1的MPLS TE隧道接口信息

Level-2 Tunnel Statistics

Level-2的MPLS TE隧道接口信息

Tunnel Name

隧道接口名称

Auto Route

隧道接口上配置的自动路由发布类型，取值包括：

·Advertise：转发邻接

·Shortcut：IGP shortcut

Destination

隧道的目的端地址

Metric

隧道接口上配置的度量值，取值包括：

·Relative：相对度量值

·Absolute：绝对度量值

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te ds-te**

------------------------------------------------------------------------

**[display mpls te ds-te**]命令用来显示DS-TE相关信息，包括DS-TE的模式、带宽约束模型及TE class与服务类型、优先级的对应关系等。

【命令】

**[display mpls te ds-te**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示DS-TE相关信息。

\<Sysname\> display mpls te ds-te

MPLS LSR ID         : 0.0.0.0

MPLS DS-TE mode     : Prestandard

MPLS DS-TE BC model : RDM

TE Class       Class Type     Priority

0              0              0

1              0              1

2              0              2

3              0              3

4              0              4

5              0              5

6              0              6

7              0              7

8              1              0

9              1              1

10             1              2

11             1              3

12             1              4

13             1              5

14             1              6

15             1              7

表1-6 display mpls te ds-te命令显示信息描述表

字段

描述

MPLS LSR ID

设备的MPLS LSR ID

MPLS DS-TE mode

DS-TE模式，取值包括Prestandard和IETF

MPLS DS-TE BC model

DS-TE的带宽约束模型，取值包括

·RDM：俄罗斯套娃模型

·MAM：最大分配模型

TE Class

CT及优先级组合的编号

Class Type

服务类型

Priority

优先级

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te link-management bandwidth-allocation**

------------------------------------------------------------------------

**[display mpls te link-management bandwidth-allocation**]命令用来显示开启了MPLS TE的接口上的带宽相关信息。

【命令】

**[display mpls te link-management bandwidth-allocation** [ **interface** *interface-type interface-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口上的带宽相关信息。*interface-type interface-number*为接口类型和接口编号。如果不指定本参数，则显示所有开启了MPLS TE的接口上的带宽相关信息。

【举例】

\# 显示所有开启了MPLS TE的接口上的带宽相关信息。

\<Sysname\> display mpls te link-management bandwidth-allocation

Interface: GigabitEthernet1/0/1

  Max Link Bandwidth                          : 3200000 kbps

  Max Reservable Bandwidth of Prestandard RDM : 2000000 kbps

  Max Reservable Bandwidth of IETF RDM        : 200000 kbps

  Max Reservable Bandwidth of IETF MAM        : 300000 kbps

  Allocated Bandwidth-Item Count ：1

  Allocated Bandwidth            ：1000 kbps

  Physical Link Status           : Up

  BC  Prestandard RDM(kbps)  IETF RDM(kbps)       IETF MAM(kbps)

  0   2000000                200000               2000

  1   1000000                150000               2000

  2   0                      100000               2000

  3   0                      50000                2000

  TE Class    Class Type    Priority   BW Reserved(kbps)  BW Available(kbps)

      0           0             0            0            2000000

      1           0             1            0            2000000

      2           0             2            0            2000000

      3           0             3            0            2000000

      4           0             4            0            2000000

      5           0             5            0            2000000

      6           0             6            0            2000000

      7           0             7            1000         1999000

      8           1             0            0            1000000

      9           1             1            0            1000000

     10           1             2            0            1000000

     11           1             3            0            1000000

     12           1             4            0            1000000

     13           1             5            0            1000000

     14           1             6            0            1000000

     15           1             7            0            1000000

表1-7 display mpls te link-management bandwidth-allocation命令显示信息描述表

字段

描述

Interface

开启了MPLS TE的接口

Max Link Bandwidth

用于转发MPLS TE流量的最大链路带宽

Max Reservable Bandwidth of Prestandard RDM

Prestandard RDM模型的最大可预留带宽

Max Reservable Bandwidth of IETF RDM

IETF RDM模型的最大可预留带宽

Max Reservable Bandwidth of IETF MAM

IETF MAM模型的最大可预留带宽

Allocated Bandwidth-Item Count

已分配带宽条目的数量

Allocated Bandwidth

已分配的带宽，单位为kbps

Physical Link Status

接口的物理层链路状态，取值包括Up和Down

BC

带宽约束

Prestandard RDM

Prestandard模式RDM模型的带宽约束，单位为kbps

IETF RDM

IETF模式RDM模型的带宽约束，单位为kbps

IETF MAM

IETF模式MAM模型的带宽约束，单位为kbps

TE Class

CT及优先级组合的编号

Class Type

服务类型

Priority

优先级

BW Reserved

已经为该TE class预留的带宽，单位为kbps

BW Available

目前该TE class可预留的带宽，单位为kbps

【相关命令】

·**mpls te max-link-bandwidth**

·**mpls te max-reservable-bandwidth**

·**mpls te max-reservable-bandwidth mam**

·**mpls te max-reservable-bandwidth rdm**

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te pce discovery**

------------------------------------------------------------------------

**[display mpls te pce discovery**]命令用来显示设备已发现的PCE的信息。

【命令】

**[display mpls te pce discovery ** *ip-address* ]  **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示设备已发现的指定PCE的信息。*ip-address*为PCE的IP地址。如果不指定本参数，则显示所有已发现PCE的信息。

**[verbose**]：显示设备已发现的PCE的详细信息。如果不指定本参数，则显示已发现的PCE的简要信息。

【举例】

\# 显示设备已发现的指定PCE的简要信息。

\<Sysname\> display mpls te pce discovery 100.100.100.150

Total number of PCEs: 1

Peer address          Discovery methods

100.100.100.150       Static, OSPF

\# 显示所有已发现PCE的简要信息。

\<Sysname\> display mpls te pce discovery

Total number of PCEs: 3

Peer address          Discovery methods

100.100.100.10        OSPF

100.100.100.150       Static, OSPF

100.100.100.160       Static

表1-8 display mpls te pce discovery命令显示信息描述表

字段

描述

Total number of PCEs

PCE的总数

Peer address

PCE的IP地址

Discovery methods

发现本PCE的方式，取值包括：

·Static：静态配置

·OSPF：OSPF协议自动发现

\# 显示指定的PCE的详细信息。

\<Sysname\> display mpls te pce discovery 2.2.2.9 verbose

PCE address: 2.2.2.9

  Discovery methods: OSPF

  Path scopes:

    Path scope                                                  Preference

    Compute intra-area paths                                    7

    Act as PCE for inter-area TE LSP computation                6

    Act as a default PCE for inter-area TE LSP computation      6

  Capabilities:

    Bidirectional path computation

    Support for request prioritization

    Support for multiple requests per message

  Domains:

    OSPF 1 area 0.0.0.0

    OSPF 1 area 0.0.0.1

\# 显示所有已发现PCE的详细信息。

\<Sysname\> display mpls te pce discovery verbose

PCE address: 2.2.2.9

  Discovery methods: OSPF

  Path scopes:

    Path scope                                                  Preference

    Compute intra-area paths                                    7

    Act as PCE for inter-area TE LSP computation                6

    Act as a default PCE for inter-area TE LSP computation      6

  Capabilities:

    Bidirectional path computation

    Support for request prioritization

    Support for multiple requests per message

  Domains:

    OSPF 1 area 0.0.0.0

    OSPF 1 area 0.0.0.1

PCE address: 4.4.4.9

  Discovery methods: OSPF

  Path scopes:

    Path scope                                                  Preference

    Compute intra-area paths                                    7

    Act as PCE for inter-area TE LSP computation                6

  Capabilities:

    Bidirectional path computation

    Support for request prioritization

    Support for multiple requests per message

  Domains:

    OSPF 1 area 0.0.0.2

  Neighbor domains:

    OSPF 1 area 0.0.0.0

表1-9 display mpls te pce discovery verbose命令显示信息描述表

字段

描述

PCE address

PCE的IP地址

Discovery methods

发现本PCE的方式，取值包括：

·Static：静态配置

·OSPF：OSPF协议自动发现

Path scopes

PCE路径计算范围及优先级信息

Path scope，路径计算范围，取值包括：

·Compute intra-area paths：表示区域内路径计算

·Act as PCE for inter-area TE LSP computation：表示区域间路径计算

·Act as a default PCE for inter-area TE LSP computation：表示区域间路径计算缺省PCE

·Act as PCE for inter-AS TE LSP：表示自治系统间路径计算

·Act as a default PCE for inter-AS TE LSP：表示自治系统间路径计算缺省PCE

·Act as PCE for inter-layer TE LSP：表示层间路径计算

Preference，PCE路径计算范围的计算优先级，即处理该计算范围的优先级，取值为0～7，数值越大，优先级越高

Capabilities

PCE路径计算能力，取值包括：

·Path computation with GMPLS link constraints：表示带GMPLS 链路约束的路径计算

·Bidirectional path computation：表示双向路径计算

·Diverse path computation：表示多条不同路径计算

·Load-balanced path computation：表示负载分担路径计算

·Synchronized path computation：表示同步路径计算

·Support for multiple objective functions：表示支持多对象功能

·Support for additive path constraints：表示支持附加路径约束

·Support for request prioritization：表示支持请求优先级

·Support for multiple requests per message：表示支持一个PCReq消息携带多个计算请求

Domains

PCE路径计算域

Neighbor domains

PCE路径计算相邻域

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te pce peer**

------------------------------------------------------------------------

**[display mpls te pce peer**]命令用来在显示PCC或PCE对等体的信息。

【命令】

**[display mpls te pce peer** [ *ip-address*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定PCC或PCE对等体的信息。*ip-address*为PCC或PCE对等体的IP地址。如果不指定本参数，则显示所有对等体的信息。

**[verbose**]：显示PCC或PCE对等体的详细信息。如果不指定本参数，则显示对等体的简要信息。

【使用指导】

本命令用来显示与本地设备之间正在建立PCEP会话或已建立PCEP会话的对等体的相关信息。

【举例】

\# 显示所有对等体的简要信息。

\<Sysname\> display mpls te pce peer

Total number of peers: 1

Peer address      Peer type   State     Mastership      Role

100.100.100.100   PCE         up        Normal          Active

表1-10 display mpls te pce peer命令显示信息描述表

字段

描述

Total number of peers

对等体的总数

Peer address

对等体的IP地址

Peer type

对等体的类型，取值为PCC或PCE

State

对等体之间的PCEP会话状态，取值包括：

·Idle：初始状态

·TCPPending：等待TCP连接建立完成

·OpenWait：等待对等体的Open消息

·KeepWait：等待对等体的Keepalive消息

·Up：PCEP会话成功建立

Mastership

PCE对等体角色，取值包括：

·Normal：普通PCC或PCE

·Primary：托管CRLSP的主PCE（暂不支持）

·Backup：托管CRLSP的备PCE（暂不支持）

Role

PCEP会话角色，取值包括：

·Passive：表示会话被动端

·Active：表示会话主动端

\# 显示所有PCC或PCE对等体的详细信息。

\<Sysname\> display mpls te pce peer verbose

Peer address: 100.100.100.20

  TCP Connection          : 100.100.100.20:5696 -\> 100.100.100.10:4189

  Peer type               : PCC

  Session type            : Active stateful

  Session state           : Up

  Mastership              : Normal

  Role                    : active

  Session up time         : 0000 days 01 hours 03 minutes

  Session ID              : Local 1, Peer 1

  Keepalive interval      : Local 0 sec, Peer 0 sec

  Recommended DeadTimer   : Local 0 sec, Peer 0 sec

  Tolerance:

    Min keepalive interval: 10 sec

    Max unknown messages  : 10

  Request timeout         : 50 sec

  Delegation timeout      : 30 sec

表1-11 display mpls te pce peer verbose命令显示信息描述表

字段

描述

Peer address

对等体的IP地址

TCP Connection

TCP 连接地址

Peer type

对等体类型，取值为PCC或PCE

Session type

PCEP会话类型，取值包括：

·Stateless ：表示无状态的会话类型

·Passive stateful ：表示被动方式的有状态会话类型（暂不支持）

·Active stateful ：表示主动方式的有状态会话类型（暂不支持）

Session state

PCEP会话状态，取值包括：

·Idle：初始状态

·TCPPending：等待TCP连接建立完成

·OpenWait：等待对等体的Open消息

·KeepWait：等待对等体的Keepalive消息

·Up：PCEP会话成功建立

Mastership

对等体角色，取值包括：

·Normal：普通PCC或PCE

·Primary：托管CRLSP的主PCE（暂不支持）

·Backup：托管CRLSP的备PCE（暂不支持）

Role

PCEP会话角色，取值包括：

·Passive：表示会话被动端

·Active：表示会话主动端

Session up time

PCEP会话处于Up状态的时间长度

Session ID

PCEP会话标识符，包括本地标识符和远端标识符

Keepalive interval

协商后的Keepalive消息的发送时间间隔，单位为秒

Recommended DeadTimer

PCE对等体推荐给本地使用的PCEP会话的保持时间，单位为秒

Tolerance

PCEP会话容忍度

Min keepalive interval

能接受的最小Keepalive发送时间间隔，单位为秒

Max unknown messages

每分钟能接受的最大未知消息数

Request timeout

发送PCEP请求后，等待PCEP应答的超时时间，单位为秒

Delegation timeout

PCEP会话中断后，取消托管等待时间，单位为秒（暂不支持）

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te pce statistics**

------------------------------------------------------------------------

**[display mpls te pce statistics**]命令用来显示PCC或PCE的统计信息。

【命令】

**[display mpls te pce statistics** [ *ip-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ip-address*]：显示指定PCC或PCE的统计信息。*ip-address*为PCC或PCE的IP地址。如果不指定本参数，则显示所有PCE和PCC的统计信息。

【举例】

\# 显示所有PCC和PCE的统计信息。

\<Sysname\> display mpls te pce statistics

PCE address: 2.2.2.9

  Keepalive messages sent/received           : 70/75

  Open messages sent/received                : 1/1

  PCReq messages sent/received               : 0/0

  PCRep messages sent/received               : 0/0

  PCErr messages sent/received               : 0/0

  PCNtf messages sent/received               : 0/0

  Session setup failures                     : 0

  Unknown messages received                  : 0

  Unknown requests received                  : 0

  Unknown responses received                 : 0

  Requests sent                              : 0

    Response is pending                      : 0

    Response with ERO received               : 0

    Response with NO-PATH received           : 0

    Canceled by peer sending a PCNtf         : 0

    Canceled by peer sending a PCErr         : 0

    Canceled by local speaker sending a PCNtf: 0

    Implicitly canceled (session down)       : 0

    Timeout                                  : 0

  Requests received                          : 0

    Response is pending                      : 0

    Response with ERO sent                   : 0

    Response with NO-PATH sent               : 0

    Canceled by local speaker sending a PCNtf: 0

    Canceled by local speaker sending a PCErr: 0

    Canceled by peer sending a PCNtf         : 0

    Implicitly canceled (session down)       : 0

表1-12 display mpls te pce statistics命令显示信息描述表

字段

描述

PCE address

PCE的IP地址

PCC address

PCC的IP地址

Keepalive messages sent/received

发送/接收的Keepalive消息数量

Open messages sent/received

发送/接收的Open消息数量

PCReq messages sent/received

发送/接收的PCReq消息数量

PCRep messages sent/received

发送/接收的PCRep消息数量

PCErr messages sent/received

发送/接收的PCErr消息数量

PCNtf messages sent/received

发送/接收的PCNtf消息数量

Session setup failures

尝试建立PCEP会话的失败次数

Unknown messages received

收到的未知消息数量

Unknown requests received

收到的未知请求（RP对象的Request ID为0的请求）数量

Unknown responses received

收到的未知应答（RP对象的Request ID匹配不到请求的应答）数量

Requests sent

已发送所有请求消息的总数

Response is pending

等待应答的请求数量

Response with ERO received

收到携带ERO对象的应答的请求消息的数量

Response with NO-PATH received

收到携带NO-PATH对象的应答的请求消息的数量

Cancelled by peer sending a PCNtf

收到对等体发送的取消计算请求的PCNtf消息的数量

Canceled by peer sending a PCErr

收到对等体发送的取消计算请求的PCErr消息的数量

Canceled by local speaker sending a PCNtf

本地通过发送PCNtf取消的请求消息的数量

Implicitly canceled(session down)

因PCEP会话关闭导致请求失效的请求消息的数量

Timeout

因等待应答超时而失效的的请求消息的数量

Requests received

收到的所有请求消息的总数

Response is pending

还未发送应答的请求消息的数量

Response with ERO  sent

已发送携带ERO对象的应答消息的数量

Response with NO-PATH sent

已发送携带NO-PATH对象的应答消息的数量

Canceled by local speaker sending a PCNtf

本地发送的取消计算请求的PCNtf消息数量

Canceled by local speaker sending a PCErr

本地发送的取消计算请求的PCErr消息数量

Canceled by peer sending a PCNtf

对端发送的取消计算请求的PCNtf消息数量

Implicitly canceled(session down)

因PCEP会话关闭而失效的请求消息的数量

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te tedb**

------------------------------------------------------------------------

**[display mpls te tedb**]命令用来显示MPLS TEDB（TE DataBase，流量工程数据库）信息。

【命令】

**[display mpls te tedb**  { { **isis** { **level-1** \| **level-2** } \| **ospf area** *area-id* } \| **link** *ip-address* \| **network** \| **node** [ **local** \| *mpls-lsr-id* ] \| **summary** }]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[isis**]：显示指定IS-IS级别的TEDB信息。

**[level-1**]：显示level-1级别的TEDB信息。

**[level-2**]：显示level-2级别的TEDB信息。

**[ospf area*** area-id*]：显示指定OSPF区域的TEDB信息。*area-id*为OSPF区域的标识，取值范围为0～4294967295。

**[link*** ip-address*]：显示指定IP地址对应链路的TEDB信息。*ip-address*为接口的IP地址。

**[network**]：显示所有广播和NBMA网络的TEDB信息。

**[node**]：显示节点相关的TEDB信息。如果没有指定**local**和*mpls-lsr-id*参数，则显示所有节点相关的TEDB信息。

**[local**]：显示本地节点相关的TEDB信息。

*[mpls-lsr-id*]：显示指定节点相关的TEDB信息。*mpls-lsr-id*为节点的MPLS LSR ID。

**[summary**]：显示TEDB的摘要信息。

【举例】

\# 显示所有广播和NBMA网络的TEDB信息。

\<Sysname\> display mpls te tedb network

DR MPLS LSR-ID  DR-address      IGP   Process-ID Area/Level  Neighbors

8.1.1.2         3.0.0.2         OSPF  100        0           1.1.1.1

                                                             2.1.1.1

                                                             8.1.1.2

2.1.1.1         3.0.0.3         OSPF  100        0           2.1.1.1

                                                             3.1.1.1

                                                             2.1.1.2

3.1.1.2         3.0.0.4          OSPF  100       0           3.1.1.1

                                                             4.1.1.1

                                                             3.1.1.2

4.1.1.2        3.0.0.5          OSPF  100         0          4.1.1.1

                                                             5.1.1.1

                                                             4.1.1.2

5.1.1.2        3.0.0.6          OSPF  100         0          5.1.1.1

                                                             6.1.1.1

                                                             5.1.1.2

6.1.1.2        3.0.0.9          OSPF  100         0          6.1.1.1

                                                             7.1.1.1

                                                             6.1.1.2

7.1.1.1        12.0.0.7         OSPF  100         0          3.1.1.1

                                                             7.1.1.1

                                                             7.1.1.2

表1-13 display mpls te tedb network命令显示信息描述表

字段

描述

DR MPLS LSR-ID

DR（Designated Router，指定路由器）的MPLS LSR ID，点分十进制形式

DR-address

DR的接口地址

IGP

内部网关协议，取值为OSPF或IS-IS

Process-ID

IGP进程ID

Area/Level

路由器属于的区域（OSPF）或Level（IS-IS）

Neighbors

与DR形成了完全邻接关系的路由器的Router ID，也包括DR自身的Router ID

\# 显示TEDB的概要信息。

\<Sysname\> display mpls te tedb summary

MPLS LSR-ID     IGP     Process-ID    Area/Level    Links-Count

1.1.1.1         OSPF    100           1001          20

                                      1002          30

                                      1003          40

                                      1004          50

                                      1007          70

                                      1010          80

2.1.1.1         ISIS    100           Level-1       20

                                      Level-1       30

3.1.1.1         OSPF    100           0             4

表1-14 display mpls te tedb summary命令显示信息描述表

字段

描述

MPLS LSR-ID

MPLS LSR ID，点分十进制形式

IGP

内部网关协议，取值为OSPF或IS-IS

Process-ID

IGP进程ID

Area/Level

路由器属于的区域（OSPF）或Level（IS-IS）

Links-Count

Area或Level中的链路数

\# 显示指定OSPF区域的TEDB信息。

\<Sysname\> display mpls te tedb ospf area 1

Node information for OSPF area 1:

MPLS LSR-ID    IGP     Process-ID     Area            Links-Count

2.2.2.2        OSPF    100            1               1

3.3.3.3        OSPF    100            1               1

Network information for OSPF area 1:

DR MPLS LSR-ID  DR-address    IGP  Process-ID Area    Neighbors

3.3.3.3         20.1.1.2      OSPF 100        1       2.2.2.2

                                                      3.3.3.3

表1-15 display mpls te tedb ospf area命令显示信息描述表

字段

描述

MPLS LSR-ID

MPLS LSR ID，点分十进制形式

IGP

内部网关协议，取值为OSPF或IS-IS

Process-ID

IGP的进程号

Area

路由器所属的OSPF区域

Links-Count

Area或Level中的链路数

DR MPLS LSR-ID

DR的MPLS LSR ID

DR-address

DR的接口地址

Neighbors

与DR形成了完全邻接关系的路由器的Router ID，也包括DR自身的Router ID

\# Prestandard模式下显示本地节点相关的TEDB信息。

\<Sysname\> display mpls te tedb node local

MPLS LSR-ID: 1.1.1.1

  IGP Type: OSPF          Process ID: 100         Area: 1

  Link[1:]

    Local IP Address: 2.0.1.33

          Neighbor IP Address: 2.0.1.2

    Neighbor MPLS LSR-ID: 1.1.1.2

    Link Type: P2P  Link Status: Inactive

    IGP Metric: 100             TE Metric: 100         Link Attribute: 0xff

    Maximum Link Bandwidth: 100 kbps

    Maximum Reservable Bandwidth: 20 kbps

Bandwidth Constraint Model: Prestandard DS-TE RDM

Bandwidth Constraints:

         BC[0:  100        kbps]

         BC[1:  20         kbps]

    Unreserved Bandwidth for each TE class:

         TE class  0:    10         kbps

         TE class  1:    10         kbps

         TE class  2:    10         kbps

         TE class  3:    10         kbps

         TE class  4:    10         kbps

         TE class  5:    10         kbps

         TE class  6:    10         kbps

         TE class  7:    10         kbps

         TE class  8:    10         kbps

         TE class  9:    10         kbps

         TE class 10:    10         kbps

         TE class 11:    10         kbps

         TE class 12:    10         kbps

         TE class 13:    10         kbps

         TE class 14:    10         kbps

         TE class 15:    10         kbps

MPLS LSR-ID: 1.1.1.1

  IGP Type: ISIS   Process ID: 100   Level: Level-1

  Link[1:]

    Local IP Address: 2.0.1.33

    Neighbor IP Address: 2.0.1.2

    Neighbor MPLS LSR-ID: 1.1.1.2

    Link Type: P2P  Link Status: Active

    IGP Metric: 10              TE Metric: 10          Link Attribute: 0x11

    Maximum Bandwidth: 100 (kbps)

    Maximum Reservable Bandwidth: 100 (kbps)

Bandwidth Constraint Model: Prestandard DS-TE RDM

Bandwidth Constraints:

         BC[0:  100        kbps]

         BC[1:  20         kbps]

    Unreserved Bandwidth for each TE Class:

         TE class  0:    10         kbps

         TE class  1:    10         kbps

         TE class  2:    10         kbps

         TE class  3:    10         kbps

         TE class  4:    10         kbps

         TE class  5:    10         kbps

         TE class  6:    10         kbps

         TE class  7:    10         kbps

         TE class  8:    10         kbps

         TE class  9:    10         kbps

         TE class 10:    10         kbps

         TE class 11:    10         kbps

         TE class 12:    10         kbps

         TE class 13:    10         kbps

         TE class 14:    10         kbps

         TE class 15:    10         kbps

表1-16 display mpls te tedb node命令显示信息描述表

字段

描述

MPLS LSR-ID

MPLS LSR ID，点分十进制形式

IGP Type

IGP类型，取值为OSPF或ISIS

Process ID

IGP进程号

Area

路由器所属的OSPF区域

Level

路由器所属的IS-IS级别，取值为Level-1、Level-2

Linkn

第n条链路的信息

Local IP Address

本地接口地址

Neighbor IP Address

对于P2P、P2MP链路，表示对端接口地址

对于NBMA、Broadcast链路，本字段为空

Neighbor MPLS LSR-ID

对端的MPLS LSR ID

Link Type

链路类型，取值包括：

·P2P：点到点链路

·P2MP：点到多点链路

·NBMA：非广播多路访问链路

·Broadcast：广播链路

Link Status

链路状态，取值包括Active、Inactive

IGP Metric

IGP度量值

TE Metric

TE度量值

Link Attribute

链路的属性

Maximum Bandwidth

链路最大带宽

Maximum Reservable Bandwidth

链路最大可预留带宽

Bandwidth Constraint Model

带宽约束模型，取值包括：

·Prestandard DS-TE RDM

·IETF DS-TE RDM

·IETF DS-TE MAM

Bandwidth Constraints

带宽约束

Unreserved Bandwidth for each TE Class

每个TE class的可预留带宽

\# IETF DS-TE模式RDM带宽约束模型下显示接口地址20.1.1.1对应链路的TEDB信息。

\<Sysname\> display mpls te tedb link 20.1.1.1

MPLS LSR-ID: 2.2.2.2

  IGP Type: ISIS   Process ID: 100  Level: Level-1

    Local IP Address: 20.1.1.1

Neighbor MPLS LSR-ID: 20.1.1.2

Link Type: Broadcast  Link Status: Active

    IGP Metric: 10          TE Metric: 0             Link Attribute: 0x0

    Maximum Bandwidth: 0 kbps

    Maximum Reservable Bandwidth: 0 kbps

Bandwidth Constraint Model: IETF DS-TE RDM

Bandwidth Constraints:

         BC[0 :  0          kbps]

         BC[1 :  0          kbps]

         BC[2 :  0          kbps]

         BC[3 :  0          kbps]

    Unreserved Bandwidth for each TE class:

         TE class  0:    0          kbps

         TE class  1:    0          kbps

         TE class  2:    0          kbps

         TE class  3:    0          kbps

         TE class  4:    0          kbps

         TE class  5:    0          kbps

         TE class  6:    0          kbps

         TE class  7:    0          kbps

表1-17 display mpls te tedb link命令显示信息描述表

字段

描述

MPLS LSR-ID

MPLS LSR ID，点分十进制形式

IGP Type

IGP类型，取值为OSPF或ISIS

Process ID

IGP进程号

Area

路由器所属的OSPF区域

Level

路由器所属的IS-IS级别，取值为Level-1、Level-2

Local IP Address

本地接口地址

Neighbor IP Address

对于P2P、P2MP链路，表示对端接口地址

对于NBMA、Broadcast链路，不显示本字段

Neighbor MPLS LSR-ID:

对端MPLS LSR ID

Link Type

链路类型，取值包括：

·P2P：点到点链路

·P2MP：点到多点链路

·NBMA：非广播多路访问链路

·Broadcast：广播链路

Link Status

链路状态，取值包括Active、Inactive

IGP Metric

IGP度量值

TE Metric

TE度量值

Link Attribute

链路的属性

Maximum Bandwidth

链路最大带宽

Maximum Reservable Bandwidth

链路最大可预留带宽

Bandwidth Constraint Mode

带宽约束模型，取值包括：

·Prestandard DS-TE RDM

·IETF DS-TE RDM

·IETF DS-TE MAM

Bandwidth Constraints

带宽约束

Unreserved Bandwidth for each TE Class

每个TE class的可预留带宽

**MPLS TE \-- MPLS TE配置命令 \-- display mpls te tunnel-interface**

------------------------------------------------------------------------

**[display mpls te tunnel-interface**]命令用来显示MPLS TE隧道接口的信息。

【命令】

**[display mpls te tunnel-interface ** **tunnel** *number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[tunnel ***number*]：显示指定Tunnel接口的信息。*number*为Tunnel接口的编号，本参数的取值范围与设备的型号有关，请以设备的实际情况为准。如果不指定本参数，则显示所有MPLS TE隧道接口的信息。

【举例】

\# 显示所有MPLS TE隧道接口的信息。

\<Sysname\> display mpls te tunnel-interface

Tunnel Name            : Tunnel 0

Tunnel State            : Up (Main CRLSP up)

Tunnel Attributes      :

  LSP ID               : 1               Tunnel ID            : 0

  Admin State          : Normal

  Ingress LSR ID       : 1.1.1.1         Egress LSR ID        : 3.3.3.3

  Signaling            : Static          Static CRLSP Name    : static-cr-lsp-1

  Resv Style           : -

  Tunnel mode          : -

  Reverse-LSP name     : -

  Reverse-LSP LSR ID   : -               Reverse-LSP Tunnel ID: -

  Class Type           : -               Tunnel Bandwidth     : -

  Reserved Bandwidth   : -

  Setup Priority       : 0               Holding Priority     : 0

  Affinity Attr/Mask   : -/-

  Explicit Path        : -

  Backup Explicit Path : -

  Metric Type          : TE

  Record Route         : -               Record Label         : -

  FRR Flag             : -               Bandwidth Protection : Disabled

  Backup Bandwidth Flag: Disabled        Backup Bandwidth Type: -

  Backup Bandwidth     : -

  Bypass Tunnel        : No              Auto Created         : No

  Route Pinning        : -

  Retry Limit          : 10              Retry Interval       : 2 sec

  Reoptimization       : -               Reoptimization Freq  : -

  Backup Type          : -               Backup LSP ID        : -

  Auto Bandwidth       : -               Auto Bandwidth Freq  : -

  Min Bandwidth        : -               Max Bandwidth        : -

  Collected Bandwidth  : -

表1-18 display mpls te tunnel-interface命令显示信息描述表

字段

描述

Tunnel Name

隧道接口的名称

Tunnel State

隧道的运行状态，取值包括Down和Up

隧道状态描述信息的取值包括：

·Main CRLSP down：配置不全，主CRLSP未建立

·Main CRLSP up：主CRLSP已建立

·Main CRLSP being set up：主CRLSP正在建立中

·{.TableTextChar}Shared-resourceCRLSP down：存在Shared-resource CRLSP相关配置，但Shared-resource CRLSP未建立

·{.TableTextChar}Shared-resource CRLSP up：Shared-resource CRLSP已建立

·{.TableTextChar}Shared-resource CRLSP being set up：Shared-resource CRLSP正在建立中

·{.TableTextChar}Shared-resource CRLSP being activated：Shared-resource CRLSP激活中

·{.TableTextChar}Shared-resource CRLSP switching to Main CRLSP：Shared-resource CRLSP与主CRLSP切换中

·{.TableTextChar}Backup CRLSP down：存在备份CRLSP相关配置，但备份CRLSP未建立

·{.TableTextChar}Backup CRLSP up：备份CRLSP已建立

·{.TableTextChar}Backup CRLSP being set up：备份CRLSP正在建立中

·Reverse CRLSP down：配置了双向隧道，反向CRLSP未建立

·Reverse CRLSP up：双向隧道的反向CRLSP已建立

·Reverse CRLSP being set up：双向隧道的反向CRLSP正在建立中

LSP ID

LSP ID

Tunnel ID

会话ID

Admin State

隧道接口的管理状态，取值包括：

·{.TableTextChar}Normal：未{.TableTextChar}通过**shutdown**命令关闭隧道接口

·Shutdown：通过**shutdown**命令关闭隧道接口

Ingress LSR ID

入口标签交换路由器ID

Egress LSR ID

出口标签交换路由器ID

Signaling

建立隧道使用的信令协议，取值包括RSVP-TE和Static

Static CRLSP Name

隧道引用的静态CRLSP

Resv Style

实际生效的资源预留风格，对于动态建立CRLSP的MPLS TE隧道，本字段有意义，取值为FF和SE；对于静态建立CRLSP的MPLS TE隧道，本字段显示为"-"

Tunnel Mode

双向隧道的模式，取值包括：

·Co-routed, active：表示Co-routed方式双向隧道的Active端

·Co-routed, passive：表示Co-routed方式双向隧道的Passive端

·Associated：表示Associated方式的双向隧道

Reverse-LSP Name

Associated方式反向LSP的名称

Reverse-LSP LSR ID

反向LSP的LSR ID

显示Associated方式双向隧道信息或Co-routed方式双向隧道的Passive端信息时，本字段有意义；其他情况下，本字段显示为"-"

Reverse-LSP Tunnel ID

反向LSP的Tunnel ID

显示Associated方式双向隧道信息或Co-routed方式双向隧道的Passive端信息时，本字段有意义；其他情况下，本字段显示为"-"

Class Type

隧道流量所属的服务类型，取值包括CT0、CT1、CT2和CT3

Tunnel Bandwidth

隧道所需的带宽，单位为kbps

Reserved Bandwidth

为隧道预留的带宽，单位为kbps

Setup Priority

隧道的建立优先级

Holding Priority

隧道的保持优先级

Affinity Attr/Mask

隧道的亲和属性及掩码

Explicit Path Name

隧道引用的显式路径名称

存在显示路径时，本字段有意义，其他情况下，本字段显示为"-"

Backup Explicit Path

备份隧道引用的显式路径名称

存在显示路径时，本字段有意义，其他情况下，本字段显示为"-"

Metric Type

隧道选路时使用的链路度量值类型，取值包括：

·TE：使用TE度量值

·IGP：使用IGP度量值

Record Route

是否开启路由记录功能，取值包括：

·Enabled：开启了路由记录功能

·Disabled：未开启路由记录功能

Record Label

是否开启标签记录功能，取值包括：

·Enabled：开启了标签记录功能

·Disabled：未开启标签记录功能

FRR Flag

是否开启快速重路由功能，取值包括：

·Enabled：开启了快速重路由功能

·Disabled：未开启快速重路由功能

Bandwidth Protection

快速重路由功能是否要求带宽保护，取值包括：

·Enabled：要求带宽保护

·Disabled：不要求带宽保护

Backup Bandwidth Flag

是否通过**mpls te backup bandwidth**命令指定了Bypass隧道可以保护的带宽和CRLSP类型，取值包括：

·Enabled：指定了Bypass隧道可以保护的带宽和CRLSP类型

·Disabled：未指定Bypass隧道可以保护的带宽和CRLSP类型

Backup Bandwidth Type

Bypass隧道可以保护的主CRLSP流量的服务类型，取值包括CT0、CT1、CT2和CT3

Backup Bandwidth

Bypass隧道可以保护的带宽，单位为kbps

Bypass Tunnel

是否是Bypass隧道，取值包括：

·Yes：是Bypass隧道

·No：不是Bypass隧道

Auto Created

是否为自动创建的Bypass隧道，取值包括：

·Yes：是自动创建

·No：不是自动创建

Route Pinning

是否开启路由固定功能，取值包括：

·Enabled：开启了路由固定功能

·Disabled：未开启路由固定功能

Retry Limit

隧道的最大重建次数

Retry Interval

隧道重建的时间间隔，单位为秒

Reoptimization

是否开启隧道重优化功能，取值包括：

·Enabled：开启了隧道重优化功能

·Disabled：未开启隧道重优化功能

Reoptimization Freq

隧道重优化频率，单位为秒

Backup Type

隧道使用的备份模式，取值包括：

·None：未开启隧道备份功能

·Hot Standby：热备份

·Ordinary：普通备份

Backup LSP ID

备份隧道的LSP ID

Auto Bandwidth

是否开启自动带宽调整功能，取值包括：

·Enabled：开启了自动带宽调整功能

·Disabled：未开启自动带宽调整功能

Auto Bandwidth Freq

自动带宽调整的时间间隔，单位为秒

Min Bandwidth

允许调整到的最小带宽值，单位为kbps

Max Bandwidth

允许调整到的最大带宽值，单位为kbps

Collected Bandwidth

当前收集到的出口速率，单位为kbps

**MPLS TE \-- MPLS TE配置命令 \-- display ospf mpls te advertisement**

------------------------------------------------------------------------

**[display ospf mpls te advertisement**]命令用来显示OSPF TEDB中的链路和节点信息。

【命令】

**[display ospf** [ *process-id*   **area** *area-id*  **mpls te advertisement** [ **originate-router** *advertising-router-id* \| **self-originate** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPF进程的信息。*process-id*为OSPF进程号，取值范围为1～65535。如果未指定本参数，则显示所有OSPF进程的信息。

**[area*** area-id*]：显示指定区域的信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式。如果未指定本参数，则显示所有区域的信息。

**[originate-router ***advertising-router-id*]：显示指定路由器发布的信息。*advertising-router-id*为路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的信息。

【举例】

\# 显示OSPF TEDB中的链路和节点信息。

\<Sysname\> display ospf mpls te advertisement

          OSPF Process 1 with Router ID 2.2.2.2

                 Traffic Engineering Database

                          Area: 0.0.0.1

    Adv Router ID              : 1.1.1.1

    MPLS LSR ID                : 1.1.1.1

    Flags                      : A/S/R

    Router Address Count       : 1

      Router Address Index     : 0

      Instance ID              : 0.0.0.0

      MPLS LSR ID              : 1.1.1.1

    Link Count                 : 1

      Link Index               : 0

      Link Type                : Broadcast

      Instance ID              : 0.0.0.1

      Link Flags               : -/U/-

      Link ID                  : 197.168.1.1

      TE Metric                : 1000

      IGP Metric               : 1000

      Maximum Bandwidth        : 12500000 bytes/sec

      Maximum Reservable BW    : 0 bytes/sec

      Administrative Group     : 0x0

      Unreserved Bandwidth for each TE Class:

        TE class  0 = 0 bytes/sec

        TE class  1 = 0 bytes/sec

        TE class  2 = 0 bytes/sec

        TE class  3 = 0 bytes/sec

        TE class  4 = 0 bytes/sec

        TE class  5 = 0 bytes/sec

        TE class  6 = 0 bytes/sec

        TE class  7 = 0 bytes/sec

        TE class  8 = 0 bytes/sec

        TE class  9 = 0 bytes/sec

        TE class 10 = 0 bytes/sec

        TE class 11 = 0 bytes/sec

        TE class 12 = 0 bytes/sec

        TE class 13 = 0 bytes/sec

        TE class 14 = 0 bytes/sec

        TE class 15 = 0 bytes/sec

      Bandwidth Constraint Model: Prestandard DS-TE RDM

      Bandwidth Constraints:

        BC [ 0 = 0 bytes/sec]

        BC [ 1 = 0 bytes/sec]

      Local Interface Address  : 197.168.1.1

      Remote Interface Address : 197.168.1.11

表1-19  display ospf mpls te advertisement命令显示信息描述表

字段

描述

Adv Router ID

发布该信息的路由器的Router ID

MPLS LSR ID

发布该信息的路由器的MPLS LSR ID

Flags

TE信息相关标记，取值包括：

·A：表示已向CSPF同步该信息

·S：表示准备向CSPF同步该信息

·R：表示到达发布该信息的路由器的路由可达

Router Address Count

TEDB中RouterTLV信息的总数

Router Address Index

当前RouterTLV信息的索引

Instance ID

LSA的实例号

Link Count

TEDB中LinkTLV信息的总数

Link Index

当前LinkTLV信息的索引

Link Type

链路类型，取值包括：

·Point to Point：点到点链路{.TableTextChar}

·Point to Multi Point：点到多点链路{.TableTextChar}

·Broadcast：广播链路{.TableTextChar}

·NBMA：非广播多点可达链路{.TableTextChar}

 

Link Flags

Link信息相关标记，取值包括：

·A：已向CSPF同步该信息

·U：向CSPF同步更新该信息失败后，准备再次向CSPF同步

·D：向CSPF同步删除该信息失败后，准备再次向CSPF同步

 

Link ID

链路状态ID

 

TE Metric

TE度量值

 

IGP Metric

OSPF协议度量值

 

Maximum bandwidth

链路的最大带宽

 

Maximum reservable BW

链路的最大可预留带宽

 

Administrative Group

链路的管理组，即链路的属性

 

Unreserved Bandwidth for each TE Class

每个TE class的可预留带宽

 

TE class

16个TE class各自的可预留带宽

 

Bandwidth Constraint Model

带宽约束模型，取值包括：Prestandard DS-TE RDM、IETF DS-TE RDM、IETF DS-TE MAM

 

Bandwidth Constraints

带宽约束（仅对于DS-TE有意义）

 

BC

各个带宽约束值（Prestandard模式支持2个BC，IETF模式支持4个BC）

 

Local Interface Address

本地接口的主IP地址

 

Remote Interface Address

远端接口的地址

 

**MPLS TE \-- MPLS TE配置命令 \-- display ospf mpls te network**

------------------------------------------------------------------------

**[display ospf mpls te network**]命令用来显示OSPF TEDB中的Network信息。

【命令】

**[display ospf** [ *process-id*   **area** *area-id*  **mpls te network** [ **originate-router** *advertising-router-id* \| **self-originate** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPF进程的信息。*process-id*为OSPF进程号，取值范围为1～65535。如果未指定本参数，则显示所有OSPF进程的信息。

**[area*** area-id*]：显示指定区域的信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，则显示所有区域的信息。

**[originate-router ***advertising-router-id*]：显示指定路由器发布的信息。*advertising-router-id*为路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的信息。

【举例】

\# 显示OSPF TEDB中的Network信息。

\<Sysname\> display ospf mpls te network

         OSPF Process 1 with Router ID 12.1.1.1

                 Traffic Engineering Network

                          Area: 0.0.0.0

      Adv Router ID             :  1.1.1.1

      Designated Router         :  197.168.1.1

      Flags                     :  -/U/-

       Attached Router    2.2.2.2

       Attached Router    1.1.1.1

表1-20 display ospf mpls te network命令显示信息描述表

字段

描述

Adv Router ID

发布该信息的路由器的Router ID

Designated Router

DR的IP地址

Flag

Network信息相关标记，取值包括：

·A：已向CSPF同步该信息

·U：向CSPF同步更新该信息失败后，准备再次向CSPF同步

·D：向CSPF同步删除该信息失败后，准备再次向CSPF同步

Attached Router

相连路由器的Router ID

**MPLS TE \-- MPLS TE配置命令 \-- display ospf mpls te pce**

------------------------------------------------------------------------

**[display ospf mpls te pce**]命令用来显示OSPF发现的PCE信息**。**

【命令】

**[display ospf** [ *process-id*   **area** *area-id*  **mpls te pce** [ **originate-router** *advertising-router-id* \| **self-originate** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPF进程的信息。*process-id*为OSPF进程号，取值范围为1～65535。如果未指定本参数，则显示所有OSPF进程的信息。

**[area*** area-id*]：显示指定区域的信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式。如果未指定本参数，则显示所有区域的信息。

**[originate-router***advertising-router-id*]：显示指定路由器发布的信息。*advertising-router-id*为路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的信息。

【举例】

\# 显示OSPF发现的所有PCE的信息。

\<Sysname\> display ospf mpls te pce

          OSPF Process 1 with Router ID 2.1.1.1

                 Path Computation Element

                          Area: 0.0.0.1

    Adv Router ID                : 2.1.1.1

    PCE Address                  : 5.6.7.8

    Flags                        : A/-/R/E

    PCE Path Scopes:

        Path Scope                     Preference

        L (PCE for intra-area)         7

        R (PCE for inter-area)         6

    PCE Capabilities:

        Bidirectional path computation

        Support for request prioritization

        Support for multiple requests per message

    PCE Domain List:

        Area 0.0.0.1

        Area 0.0.0.3

    PCE Neighbor Domain List:

        Area 0.0.0.2

表1-21 display ospf mpls te pce命令显示信息描述表

字段

描述

Adv Router ID

发布路由器的Router ID

PCE Address

PCE的IP地址

Flags

PCE信息相关标记：

·A：已向PCEP同步该信息

·U：向PCEP同步更新失败后在等待重新同步

·D：向PCEP同步删除失败后在等待重新同步

·R：到达对应路由器的路由可达

·E：PCE信息有效

PCE Path Scopes

PCE的计算范围集合

Path Scope

PCE的计算范围，包括：

·L (PCE for intra-area)：区域内路径计算

·R (PCE for inter-area)：区域间路径计算

·Rd(Default PCE for inter-area)：区域间路径计算缺省PCE

·S (PCE for inter-AS)：自治系统间路径计算

·Sd(Default PCE for inter-AS)：自治系统间路径计算缺省PCE

·Y (PCE for inter-layer)：层间路径计算

Preference

PCE路径计算范围的计算优先级，即处理该计算范围的优先级，取值为0～7，数值越大，优先级越高

PCE Capabilities

PCE能力集，包括：

·Path computation with GMPLS link constraints：带GMPLS 链路约束的路径计算

·Bidirectional path computation：双向路径计算

·Diverse path computation：多条不同路径计算

·Load-balanced path computation：负载分担路径计算

·Synchronized path computation：同步路径计算

·Support for multiple objective functions：支持多对象功能

·Support for additive path constraints：支持附加路径约束

·Support for request prioritization：支持请求优先级

·Support for multiple requests per message：支持一个PCReq消息携带多个计算请求

PCE Domain List

PCE上支持TE功能的本地域集合

PCE Neighbor Domain List

PCE上支持TE功能的邻居域集合

Area

支持TE的区域

AS

支持TE的自治系统

**MPLS TE \-- MPLS TE配置命令 \-- display ospf mpls te tunnel**

------------------------------------------------------------------------

**[display ospf mpls te tunnel**]命令用来显示OSPF的Tunnel接口信息。

【命令】

**[display ospf** [ *process-id*   **area** *area-id*  **mpls te tunnel**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定OSPF进程的信息。*process-id*为OSPF进程号，取值范围为1～65535。如果未指定本参数，则显示所有OSPF进程的信息。

**[area*** area-id*]：显示指定区域的信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式。如果未指定本参数，则显示所有区域的信息。

【举例】

\# 显示OSPF的Tunnel接口信息。

\<Sysname\> display ospf mpls te tunnel

          OSPF Process 1 with Router ID 2.2.2.2

                   Traffic Engineering Tunnel

                          Area: 0.0.0.1

Interface: Tunnel1 (12.1.1.2)

    State: Inactive

    Neighbor ID: 0.0.0.0         Cost: 0

    Destination: 125.1.1.1

    Auto Route: IGP Shortcut

    Metric: Relative  10

表1-22 display ospf mpls te tunnel命令显示信息描述表

字段

描述

Interface

隧道类型接口的接口名称和接口地址

State

隧道接口的状态，取值包括：

·Inactive：表示该隧道接口对应的路由不是最优路由，不用于转发报文

·Active：表示该隧道接口对应的路由为最优路由，用于转发报文

Neighbor ID

隧道目的端的Router ID

Cost

隧道接口的路由开销

Destination

隧道目的端的LSR ID

Auto Route

隧道采用的自动路由发布方式，取值包括IGP Shortcut、IGP Advertise

Metric

MPLS TE隧道的度量值，取值包括：

·{.TableTextChar}Absolute：以绝对值的方式指定MPLS TE{.TableTextChar}隧道的度量值{.TableTextChar}

·Relative：以相对值的方式指定MPLS TE隧道的度量值

**MPLS TE \-- MPLS TE配置命令 \-- display tunnel-bundle**

------------------------------------------------------------------------

**[display tunnel-bundle**]命令用来显示Tunnel-Bundle接口及其成员接口的信息。

【命令】

**[display tunnel-bundle *** number*****]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[number*]：显示指定Tunnel-Bundle接口及其成员接口的信息。*number*为Tunnel-Bundle接口的编号。本参数的取值范围与设备的型号有关，请以设备的事件情况为准。如果不指定本参数，则显示所有Tunnel-Bundle接口及其成员接口的信息。

【举例】

\# 显示所有Tunnel-Bundle接口及其成员口的信息[。]

\<Sysname\> display tunnel-bundle

Total number of tunnel bundles: 1, 1 up, 0 down

Tunnel bundle name: Tunnel-Bundle 1

Bundle state           : Up

Bundle attributes      :

  Working mode         : Load Balancing

  Tunnel type          : CR-LSP

  Tunnel destination   : 2.2.2.2

Bundle members:

  Member         State        Load-share        

  Tunnel2        Up           2       

  Tunnel3        Down         3         

  Tunnel6        Down         3      

表1-23 display tunnel-bundle命令显示信息描述表

字段

描述

Total number of tunnel bundles

Tunnel-Bundle接口的总数，以及处于up、down状态的捆绑接口数目

Tunnel bundle name

Tunnel-Bundle接口的名称

Bundle state

Tunnel-Bundle接口的状态，取值包括up、down

Bundle attributes

Tunnel-Bundle接口的属性

Working mode

Tunnel-Bundle接口的模式，取值包括：

·Load Balancing：表示负载分担模式

·1+1：表示1+1保护倒换模式

·1:1：表示1:1保护倒换模式

1+1保护倒换模式和1:1保护倒换模式的详细介绍，请参见"MPLS配置指导"中的"MPLS保护倒换"

Tunnel type

隧道类型，目前取值仅支持CR-LSP

Tunnel destination

Tunnel-Bundle接口的隧道目的端地址

Bundle members

Tunnel-Bundle接口中的成员接口信息

Member

成员接口的名称

State

成员接口的状态

Load-share

负载分担权重

**MPLS TE \-- MPLS TE配置命令 \-- ds-te bc-model**

------------------------------------------------------------------------

**[ds-te bc-model**]命令用来配置IETF DS-TE模式下使用的带宽约束模型。

**[undo ds-te bc-model**]命令用来恢复缺省情况。

【命令】

**[ds-te bc-model mam**]

**[undo**] **ds-te bc-model**

【缺省情况】

IETF DS-TE模式的带宽约束模型为RDM（Russian Dolls Model，俄罗斯套娃模型）。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mam**]：指定带宽约束模型为MAM（Maximum Allocation Model，最大分配模型）。

【使用指导】

RDM模型可以限制多种服务类型流量（CT）的共用带宽，允许多种CT间共享使用带宽，而不是限制某一种CT的带宽。RDM与建立优先级/保持优先级配合，可以实现CT间的带宽隔离。RDM比较适用于属于CT的流量不平稳、可能存在突发流量的情况。

MAM模型可以限制某一CT在接口上占用的带宽总和，即隔离CT之间的带宽使用。MAM不需要与建立优先级/保持优先级配合，就可以实现CT间的带宽隔离。MAM的特点是比较直观，配置较为容易。MAM比较适用于属于CT的流量较为平稳、不存在突发流量的情况。

需要注意的是：

·本命令仅对IETF DS-TE模式有效。Prestandard DS-TE模式下，只能使用RDM带宽约束模型。

·在IETF DS-TE模式下修改带宽约束模型后，设备上所有预留带宽非零的CRLSP都将被拆除，并重新建立。

【举例】

\# 配置IETF模式下带宽约束模型为MAM。

\<Sysname\> system-view

Sysname mpls te

Sysname-te ds-te bc-model mam

【相关命令】

·**display mpls te ds-te**

·**ds-te mode**

**MPLS TE \-- MPLS TE配置命令 \-- ds-te te-class**

------------------------------------------------------------------------

**[ds-te te-class**]命令用来配置IETF DS-TE模式下TE class与服务类型、优先级的对应关系。

**[undo ds-te te-class**]命令用来恢复缺省的TE class。

【命令】

**[ds-te te-class **]*te-class-index ***class-type ***class-type-number ***priority ***priority-number*

**[undo ds-te te-class ***te-class-index*]

【缺省情况】

IETF模式的TE class如[表]1-24(?851583115#_Ref329865032)所示。

表1-24 IETF模式的缺省TE class

TE Class

CT

Priority

0

0

7

1

1

7

2

2

7

3

3

7

4

0

0

5

1

0

6

2

0

7

3

0

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[te-class-index*]：TE class编号，取值范围为0～7。

**[class-type*** class-type-number*]：指定TE class对应的CT。*class-type-number*为CT编号，取值范围为0～3，即系统支持四个CT（CT 0、CT 1、CT 2和CT 3）。

**[priority ***priority-number*]：指定TE class对应的优先级。*priority-number*为优先级，取值范围为0～7。

【使用指导】

如果流量属于某个CT，则传输该流量的LSP隧道的建立优先级或保持优先级必须是TE class中该CT对应的优先级。

需要注意的是：

·通过**ds-te te-class**命令配置TE class时，输入的CT和优先级不要与已有TE class的CT和优先级相同。

·通过**undo ds-te te-class**命令恢复缺省TE class时，恢复的TE class的CT和优先级不要与已有TE class的CT和优先级相同。

·修改任意的TE class后，设备都会通知IGP更新发布所有TE接口的带宽信息，拆除所有TE接口上此TE class对应的CRLSP，并重新建立。

【举例】

\# 配置IETF模式下TE class 7对应CT 2，优先级为3。

\<Sysname\> system-view

Sysname mpls te

Sysname-mpls ds-te te-class 7 class-type 2 priority 3

【相关命令】

·**display mpls te ds-te**

·**ds-te mode**

**MPLS TE \-- MPLS TE配置命令 \-- ds-te mode**

------------------------------------------------------------------------

**[ds-te mode**]命令用来配置DS-TE模式。

**[undo ds-te mode**]命令用来恢复缺省情况。

【命令】

**[ds-te mode ietf**]

**[undo ds-te mode**]

【缺省情况】

DS-TE模式为Prestandard模式。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ietf**]：指定DS-TE模式为IETF模式。

【使用指导】

Prestandard模式和IETF模式具有如下区别，请根据服务类型的数量、所需带宽约束模型等选择合适的DS-TE模式。

·Prestandard模式支持2个CT（CT 0和CT 1），8种优先级，最大支持16个TE class；IETF模式支持4个CT（CT 0、CT 1、CT 2和CT 3），8种优先级，最大支持8个TE class。

·Prestandard模式下不可以通过配置改变TE class；IETF模式下可以通过配置改变TE class。

·Prestandard模式只支持RDM模型；IETF模式支持RDM模型和MAM模型。

·Prestandard模式为自定义模式，无法与所有厂商设备互通；IETF模式为根据RFC标准实现的模式，可以与其他厂商设备互通。

需要注意的是，修改DS-TE模式后，设备上所有的CRLSP都将被拆除，并重新建立。

【举例】

\# 配置DS-TE模式为IETF模式。

\<Sysname\> system-view

Sysname mpls te

Sysname-te ds-te mode ietf

【相关命令】

·**display mpls te ds-te**

·**ds-te bc-model**

**MPLS TE \-- MPLS TE配置命令 \-- explicit-path**

------------------------------------------------------------------------

**[explicit-path**]命令用来创建隧道的显式路径，并进入显式路径视图。

**[undo explicit-path**]命令用来删除指定的显式路径。

【命令】

**[explicit-path ***path-name*]

**[undo explicit-path ***path-name*]

【缺省情况】

设备上不存在任何显式路径。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[path-name*]：显式路径名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在显式路径视图下通过**nexthop**命令可以显式地指定隧道必须经过哪些节点或链路、不能经过哪些节点或链路，以便根据网络实际情况人为地干预隧道的建立。

【举例】

\# 创建一条名为path1的显式路径，并进入显式路径视图。

\<Sysname\> system-view

Sysname explicit-path path1

Sysname-explicit-path-path1

【相关命令】

·**display explicit-path**

·**mpls te backup-path**

·**mpls te path**

·**nexthop**

**MPLS TE \-- MPLS TE配置命令 \-- fast-reroute timer**

------------------------------------------------------------------------

**[fast-reroute timer**]命令用来配置在多条Bypass隧道中进行优选的时间间隔。

**[undo fast-reroute timer**]命令用来恢复缺省情况。

【命令】

**[fast-reroute timer **]*interval*

**[undo fast-reroute timer**]

【缺省情况】

在多条Bypass隧道中进行优选的时间间隔为300秒。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：在多条Bypass隧道中进行优选的时间间隔，取值范围为0～604800，单位为秒。取值为0表示不会定期进行Bypass隧道优选。

【使用指导】

如果为一条主CRLSP指定了多条Bypass隧道，MPLS TE会从中选择一条最优的Bypass隧道，当主CRLSP出现故障时，将流量切换到该Bypass隧道转发。在某些情况下（如Bypass隧道的可预留带宽发生变化），当前的最优隧道可能不是之前选中的Bypass隧道。因此，MPLS TE需要周期性地选择最优的Bypass隧道。通过本命令可以调整Bypass隧道优选的周期。

需要注意的是，如果流量已经从主CRLSP切换到了Bypass隧道，则不再进行Bypass隧道优选。

【举例】

\# 配置在多条Bypass隧道中进行优选的时间间隔为120秒。

\<Sysname\> system-view

Sysname mpls te

Sysname-te fast-reroute timer 120

**MPLS TE \-- MPLS TE配置命令 \-- interface tunnel-bundle**

------------------------------------------------------------------------

**[interface tunnel-bundle**]命令用来创建负载分担模式的隧道捆绑接口（Tunnel-Bundle接口），并进入Tunnel-Bundle接口视图。

**[undo **]**interface tunnel-bundle**命令用来删除指定的Tunnel-Bundle接口。

【命令】

**[interface tunnel-bundle** *number*]

**[undo **]**interface tunnel-bundle** *number*

【缺省情况】

设备上不存在任何Tunnel-Bundle接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Tunnel-Bundle接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在负载分担模式的Tunnel-Bundle接口下重复执行**member interface**命令，可以为该Tunnel-Bundle接口指定多个成员接口------MPLS TE隧道接口，形成一个捆绑隧道，使得流量的出接口为Tunnel-Bundle接口时，该流量能够在多条MPLS TE隧道间进行负载分担。

【举例】

\# 创建负载分担模式的隧道捆绑接口Tunnel-Bundle2，并进入Tunnel-Bundle接口视图。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2

【相关命令】

·**destination**

·**display tunnel-bundle**

·**member interface**

**MPLS TE \-- MPLS TE配置命令 \-- link-management periodic-flooding timer**

------------------------------------------------------------------------

**[link-management periodic-flooding timer**]命令用来设置通过IGP周期性泛洪TE信息的时间间隔。

**[undo link-management periodic-flooding timer**]命令用来恢复缺省情况。

【命令】

**[link-management periodic-flooding timer ***interval*]

**[undo link-management periodic-flooding timer**]

【缺省情况】

通过IGP周期性泛洪TE信息的时间间隔为180秒。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：通过IGP周期性泛洪TE信息的时间间隔，取值范围为0～3600，单位为秒。

【使用指导】

链路的可预留带宽发生变化时，需要通过IGP泛洪链路的TE相关信息，以便将变化后的链路情况通知给网络中的设备。通过**mpls te bandwidth change thresholds**命令可以配置带宽变化达到一定程度时才进行IGP泛洪，而不是只要带宽变化就进行IGP泛洪，以减轻网络负担。此时，没有及时泛洪的链路带宽变化，就可以按照本命令配置的时间间隔周期性地通告给网络中的设备。

如果配置时间间隔为0，则表示关闭周期性泛洪功能。本命令配置的最小生效时间间隔为30秒，如果配置的时间间隔为1～29秒，则设备自动将时间间隔设置为30秒。

执行本命令后，配置的时间间隔立即生效。

【举例】

\# 配置通过IGP周期性泛洪TE信息的时间间隔为100秒。

\<Sysname\> system-view

Sysname mpls te

Sysname-te link-management periodic-flooding timer 100

【相关命令】

·**mpls te bandwidth change thresholds**

**MPLS TE \-- MPLS TE配置命令 \-- member interface**

------------------------------------------------------------------------

**[member interface**]命令用来为Tunnel-Bundle接口指定成员接口。

**[undo member interface**]命令用来从Tunnel-Bundle接口中删除指定的成员接口。

【命令】

**[member interface tunnel **]*tunnel-number* [ **load-share** *value* ]

**[undo member interface tunnel **]*tunnel-number*

【缺省情况】

Tunnel-Bundle接口下不存在任何成员接口。

【视图】

Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tunnel** *tunnel-number*]：指定成员接口。*tunnel-number*为Tunnel接口的编号，本参数的取值范围与设备的型号有关，请以设备的实际情况为准。

**[load-share **]*value*：指定成员接口的负载分担权重。设备根据权重确定成员接口转发流量的比例。例如，Tunnel-Bundle接口下存在三个成员接口：Tunnel1、Tunnel2和Tunnel3，负载分担权重分别为1、1和2，则成员接口承担的流量比重分别为1/4、1/4和1/2。*value*为负载分担权重，取值范围为1～65535，缺省值为1。

【使用指导】

成员接口的负载分担权重是相对的，即三个成员接口的负载分担权重分别配置为40、40、40，与分别配置为1、1、1相同。

【举例】

\# 指定隧道捆绑接口Tunnel-Bundle2的成员接口为Tunnel1和Tunnel2，并配置接口Tunnel1和Tunnel2的负载分担权重分别为1和3。

\<Sysname\> system-view

Sysname interface tunnel-bundle 2

Sysname-tunnel-bundle2 member interface tunnel 1

Sysname-tunnel-bundle2 member interface tunnel 2 load-share 3

【相关命令】

·**display tunnel-bundle**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te**

------------------------------------------------------------------------

**[mpls te**]命令用来开启本节点的MPLS TE能力，并进入MPLS TE视图。

**[undo mpls te**]命令用来关闭本节点的MPLS TE能力。

【命令】

**[mpls te**]

**[undo mpls te**]

【缺省情况】

MPLS TE能力处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**undo mpls te**命令后，将关闭本节点的MPLS TE能力，并拆除设备上所有CRLSP、删除所有接口下的MPLS TE相关配置。

【举例】

\# 开启本节点的MPLS TE能力，并进入MPLS TE视图。

\<Sysname\> system-view

Sysname mpls lsr-id 1.1.1.9

Sysname mpls te

Sysname-te

【相关命令】

·**mpls te enable**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te affinity-attribute**

------------------------------------------------------------------------

**[mpls te affinity**-**attribute**]命令用来配置隧道的亲和属性，即隧道使用的链路需要具有的链路属性。

**[undo mpls te affinity**-**attribute**]命令用来恢复缺省情况。

【命令】

**[mpls te affinity-attribute** *attribute-value* [ **mask** *mask-value* ]]

**[undo mpls te affinity-attribute**]

【缺省情况】

隧道的亲和属性为0x00000000，掩码为0x00000000，即隧道可以使用任意属性的链路。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[attribute-value*]：隧道的亲和属性，取值范围为0x00000000～0xFFFFFFFF，即为32位的二进制数。亲和属性中的每一位二进制数代表一种属性，属性值为0或1。

**[mask** *mask-value*]：指定亲和属性的掩码。*mask-value*为亲和属性掩码，取值范围为0x00000000～0xFFFFFFFF，即为32位的二进制数。掩码中的每一位二进制数都表示是否检查该位的链路属性。掩码为1，表示需要检查该位的链路属性，只有该位的链路属性满足一定条件时，才可以使用该链路；掩码为0，表示不检查该位的链路属性，不管该位的链路属性与隧道的亲和属性是否相同，都可以使用该链路。

【使用指导】

MPLS TE隧道的亲和属性和链路的属性配合，决定了该隧道可以使用哪些链路。

链路属性、亲和属性、亲和属性的掩码都是32位的二进制数。如果希望某条链路能够被隧道所用，则需要满足如下要求：

·对于掩码为1的位，亲和属性为1的位中链路属性至少有1位也为1，亲和属性为0的位对应的链路属性位不能为1。

·对于掩码为0的位，不对链路属性的相应位进行检查。

例如，亲和属性为0xFFFFFFF0，掩码为0x0000FFFF，则可用链路的链路属性高16位可以任意取0或1，17～28位中至少有1位为1，且低4位不能为1。

【举例】

\# 配置隧道的亲和属性为0x101，掩码为0x303，即只有链路属性的左数第23位为0、31位为0、24位和32位中至少有一位为1时，才可以使用该链路。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te affinity-attribute 101 mask 303

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te link-attribute**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te auto-bandwidth**

------------------------------------------------------------------------

**[mpls te auto-bandwidth**]命令用来开启隧道的自动带宽调整和/或出口速率收集功能。

**[undo mpls te auto-bandwidth**]命令用来关闭隧道的自动带宽调整和出口速率收集功能。

【命令】

**[mpls te auto-bandwidth** { **adjustment** [ **frequency** *seconds*  [ **max-bw** *max-bandwidth* \| **min-bw** *min-bandwidth* ] \* \| **collect-bw**  **frequency** *seconds*  }]]

**[undo mpls te auto-bandwidth**]

【缺省情况】

隧道的自动带宽调整和出口速率收集功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjustment**]：同时开启隧道的自动带宽调整和出口速率收集功能。

**[collect-bw**]：仅开启隧道的出口速率收集功能，不开启自动带宽调整功能。

**[frequency ***seconds*]：指定隧道的自动带宽调整时间间隔（指定**adjustment**参数时）或出口速率收集时间间隔（指定**collect-bw**参数时）。*seconds*取值范围为300～604800，单位为秒，缺省值为86400秒（24小时）。

**[max-bw ***max-bandwidth*]：指定允许调整到的最大带宽值。*max-bandwidth*取值范围为1～4294967295，单位为kbps。如果不指定本参数，则不限制带宽的最大值。

**[min-bw*** min-bandwidth*]：指定允许调整到的最小带宽值。*min-bandwidth*取值范围为1～4294967295，单位为kbps。如果不指定本参数，则不限制带宽的最小值。

【使用指导】

自动带宽调整功能是指设备定时地对隧道的出口速率进行采样，计算采样时间间隔内的平均出口速率；自动带宽调整时间间隔到达后，将隧道的带宽设置为该时间间隔内多次采样中的最大平均出口速率；根据调整后的隧道带宽建立新的CRLSP；CRLSP建立成功后，将流量从旧的CRLSP切换到新的CRLSP，并拆除旧的CRLSP。

出口速率收集功能是指以出口速率收集时间间隔为周期，定期收集隧道上的出口速率，收集的隧道出口速率为在出口速率时间间隔内，多次出口速率采样所获得的最大平均出口速率。

只有在MPLS TE视图下通过**auto-bandwidth enable**命令全局开启自动带宽调整功能，并通过本命令开启指定隧道的自动带宽调整功能或出口速率收集功能后，才能自动对该隧道进行带宽调整或出口速率收集。

需要注意的是：

·建议配置的自动带宽调整时间间隔大于等于采样时间间隔的3倍，以便获得准确的出口速率。

·在同一个Tunnel接口下，自动带宽调整特性与以下命令互斥：**mpls te reoptimization**，**mpls te route-pinning**和**mpls te backup**。

·如果同时配置了**mpls te auto-bandwidth**和**mpls te bidirectional**，则仅**mpls te bidirectional**生效。

【举例】

\# 开启接口Tunnel0对应MPLS TE隧道的自动带宽调整功能，并配置自动带宽调整的时间间隔为1小时（3600秒）。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te auto-bandwidth adjustment frequency 3600

【相关命令】

·**display mpls te tunnel-interface**

·**auto-bandwidth enable**

·**reset mpls te auto-bandwidth-adjustment timers**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te auto-tunnel backup disable**

------------------------------------------------------------------------

**[mpls te auto-tunnel backup disable**]命令用来关闭接口的自动隧道备份功能。

**[undo mpls te auto-tunnel backup disable**]命令用来开启接口的自动隧道备份功能。

【命令】

**[mpls te auto-tunnel backup disable**]

**[undo mpls te auto-tunnel backup disable**]

【缺省情况】

全局开启了自动隧道备份功能后，所有使能RSVP能力的接口都会开启自动隧道备份功能，允许自动创建Bypass隧道。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，全局开启了自动隧道备份功能后，所有使能RSVP能力的接口都会开启自动隧道备份功能，允许为采用该接口作为出接口的主隧道建立两条Bypass隧道（一条链路保护和一条节点保护的Bypass隧道）。由于Bypass隧道需要预先建立，占用额外的带宽。因此，为了节省网络带宽资源，应该只对关键的接口进行快速重路由保护，在非关键的接口上可以通过本命令关闭该接口的自动隧道备份功能，避免为该接口建立Bypass隧道。

需要注意的是，配置**mpls te auto-tunnel backup disable**命令后，已自动创建的保护该接口的Bypass隧道会被删除。

【举例】

·路由应用

\# 关闭接口GigabitEthernet1/0/1的自动隧道备份功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te auto-tunnel backup disable

·交换应用

\# 关闭接口Vlan-interface10的自动隧道备份功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te auto-tunnel backup disable

【相关命令】

·**auto-tunnel backup**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te backup**

------------------------------------------------------------------------

**[mpls te backup**]命令用来开启当前隧道的备份功能，并配置使用的备份模式。

**[undo mpls te backup**]命令用来恢复缺省情况。

【命令】

**[mpls te backup**[ { **hot-standby** \| **ordinary** }]]

**[undo mpls te backup**]

【缺省情况】

隧道不进行备份。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hot-standby**]：热备份，即创建主CRLSP后随即创建备份CRLSP。主CRLSP失效时，通过MPLS TE直接将业务切换至备份CRLSP。

**[ordinary**]：普通备份，即主CRLSP失效后再创建备份CRLSP。

【使用指导】

通过本命令开启了隧道的备份功能后，将自动启动该隧道的路由记录功能，而不管用户是否配置了**mpls te record-route**命令。

在同一个Tunnel接口视图下，本命令与以下命令互斥：**mpls te reoptimization**和**mpls te auto-bandwidth adjustment**。

如果同时配置了**mpls te backup**和**mpls te bidirectional**，则仅**mpls te bidirectional**生效。

【举例】

\# 开启隧道Tunnel0的备份功能，并配置使用的备份模式为热备份。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te backup hot-standby

【相关命令】

·**mpls te backup-path**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te backup bandwidth**

------------------------------------------------------------------------

**[mpls te backup bandwidth**]命令用来配置Bypass隧道可以保护的带宽和CT类型。

**[undo mpls te backup bandwidth**]命令用来恢复缺省情况。

【命令】

**[mpls te backup bandwidth**[ [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] { *bandwidth* \| **un-limited** }]]

**[undo mpls te backup bandwidth**]

【缺省情况】

未指定Bypass隧道可以保护的带宽和CT类型。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：Bypass隧道所能保护的带宽总量，取值范围为1～4294967295，单位为kbps。

**[ct0**]：只有CT 0的CRLSP可以使用Bypass隧道。

**[ct1**]：只有CT 1的CRLSP可以使用Bypass隧道。

**[ct2**]：只有CT 2的CRLSP可以使用Bypass隧道。

**[ct3**]：只有CT 3的CRLSP可以使用Bypass隧道。

**[un-limited**]：不对所能保护的带宽总量进行限制，即不能提供带宽保护。

【使用指导】

如果配置的保护带宽为**un-limited**，则该Bypass隧道不能提供带宽保护功能，即FRR保护时不保证被保护隧道的带宽。如果被保护的隧道流量总和超过Bypass隧道实际的带宽，会导致被保护隧道所承载的流量丢失。不要求带宽保护的主CRLSP优选此类Bypass隧道进行绑定。

如果为Bypass隧道配置了具体的保护带宽值，则该Bypass隧道能够提供带宽保护功能。要求带宽保护的主CRLSP优选此类Bypass隧道进行绑定。由于带宽为零的隧道意味着尽力转发，占用的带宽不固定，因此，此类Bypass隧道不能保护带宽为零的主CRLSP。此类Bypass隧道也不能保护带宽超过保护带宽的主CRLSP。

需要注意的是：

·如果不指定CT 0、CT 1、CT 2和CT 3，则该Bypass隧道可以为所有服务类型的CRLSP提供保护。

·通过本命令配置的保护带宽仅用于计算并确立带宽保护关系，在Bypass隧道上不会预留相应的带宽。

·配置的保护带宽数目要小于Bypass隧道实际的带宽。否则，FRR切换后，会导致被保护隧道所承载的流量丢失，并可能造成被保护隧道down。

·发生FRR切换后，如果修改Bypass隧道的保护带宽，使得保护带宽类型不同、保护带宽不够或者引起FRR保护类型（是否为主CRLSP提供带宽保护）变化，都将导致主CRLSP Down。

·在Tunnel接口视图下执行**mpls te backup bandwidth**命令后，将自动启动该隧道的路由记录功能，而不管用户是否配置了**mpls te record-route**命令。

【举例】

\# 配置隧道Tunnel0只用来保护属于CT 0的CRLSP，并且不对所保护带宽总量进行限制。配置隧道Tunnel1只用来保护属于CT 1的CRLSP，保护的带宽总量是1000kbps。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te backup bandwidth ct0 un-limited

Sysname-Tunnel0 quit

Sysname interface tunnel 1

Sysname-Tunnel1 mpls te backup bandwidth ct1 1000

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te fast-reroute**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te backup-path**

------------------------------------------------------------------------

**[mpls te backup-path**]命令用来配置备份CRLSP应用的路径及路径的优先级。

**[undo mpls te backup-path**]命令用来删除指定的备份路径。

【命令】

**[mpls te backup-path preference ***value*****{ **dynamic** [ **pce** [ *ip-address* &\<0-8\> ] \| **explicit-path** *path-name* }  **no-cspf** ]]

**[undo mpls te backup-path preference ***value*]

【缺省情况】

使用自动计算的路径建立备份CRLSP。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[preference** *value*]：指定路径的优先级。*value*的取值范围为1～10，数值越小，优先级越高。

**[dynamic**]：使用自动计算的路径建立备份CRLSP。

**[pce**]：使用PCE计算路径。如果不指定本参数，则本地LSR通过CSPF自动计算路径。

 *ip-address* &\<0-8\>：指定计算路径的PCE的IP地址，如果不指定本参数，则自动选择PCE。&\<0-8\>表示前面的参数最多可以输入8次。

**[explicit-path** *path-name*]：引用已经存在的显式路径，根据该显式路径的要求建立备份CRLSP。*path-name*为显式路径名称，为1～31个字符的字符串，区分大小写。

**[no-cspf**]：不使用CSPF算法计算路径，通过查找路由来计算路径。

【使用指导】

一个Tunnel接口下最多可以配置10条备份路径。不同备份路径的优先级不能相同。

建立备份CRLSP时，按照优先级从高到低的顺序，依次根据配置的路径进行CSPF计算，直到成功建立备份CRLSP。如果所有路径的CSPF计算都失败，则无法建立备份CRLSP。

只有通过**mpls te backup**命令开启当前隧道的备份功能后，本命令才会生效。

如果指定的PCE地址数目大于或等于2，则会按照配置的PCE地址的顺序发起BRPC计算，否则发起EPC计算。

如果使用该命令或**mpls te path**命令指定了PCE的IP地址，则仅与指定的PCE建立PCEP会话；否则与所有发现的PCE建立会话。

【举例】

\# 配置Tunnel0可以使用显式路径path1和PCE计算的路径建立备份CRLSP，且优先使用PCE计算路径。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te backup-path preference 2 explicit-path path1

Sysname-Tunnel0 mpls te backup-path preference 1 dynamic pce 1.1.1.9 2.2.2.9

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te backup**

·**mpls te path**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te bandwidth**

------------------------------------------------------------------------

**[mpls te bandwidth**]命令用来配置MPLS TE隧道所需的带宽，并指定隧道流量所属的服务类型。

**[undo mpls te bandwidth**]命令用来恢复缺省配置。

【命令】

**[mpls te bandwidth**[ [ **ct0** \| **ct1** \| **ct2** \| **ct3** ] *bandwidth*]]

**[undo mpls te bandwidth**]

【缺省情况】

未配置MPLS TE隧道所需的带宽，即带宽为0，隧道流量属于CT 0。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ct0**]：配置隧道流量属于CT 0。

**[ct1**]：配置隧道流量属于CT 1。

**[ct2**]：配置隧道流量属于CT 2。

**[ct3**]：配置隧道流量属于CT 3。

*[bandwidth*]：MPLS TE隧道所需的带宽，取值范围为1～4294967295，单位为kbps。

【使用指导】

执行本命令时，如果不指定**ct0**、**ct1**、**ct2**或**ct3**，则隧道流量属于CT 0。

当配置MPLS TE隧道所需的带宽大于1024kbps时，建议配置为1024kbps的整数倍。

本命令只用于采用RSVP-TE协议建立的MPLS TE隧道。使用静态CRLSP建立MPLS TE隧道时，隧道所需的带宽及隧道流量所属的服务类型由**static-cr-lsp ingress**命令决定。

【举例】

\# 配置MPLS TE隧道所需带宽为1000kbps，隧道流量所属的服务类型为CT 1。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te bandwidth ct1 1000

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te max-link-bandwidth**

·**mpls te max-reservable-bandwidth**

·**mpls te max-reservable-bandwidth mam**

·**mpls te max-reservable-bandwidth ****rdm**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te bandwidth change thresholds**

------------------------------------------------------------------------

**[mpls te bandwidth change thresholds**]命令用来配置通过IGP泛洪TE信息的带宽变化阈值。

**[undo mpls te bandwidth change thresholds**]命令用来恢复缺省情况。

【命令】

**[mpls te bandwidth change thresholds**[ { **down** \| **up** } *percent*]]

**[undo mpls te bandwidth change thresholds**[ { **down** \| **up** }]]

【缺省情况】

通过IGP泛洪TE信息的带宽变化阈值为10%，即可预留带宽增加或减少10%时进行IGP泛洪。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[down**]：配置可预留带宽减少时IGP进行泛洪的百分比阈值。当链路可预留带宽的减少值与链路原有可预留带宽的比值大于等于此百分比阈值时，IGP将进行泛洪，并更新流量工程数据库。

**[up**]：配置可预留带宽增加时IGP进行泛洪的百分比阈值。当链路可预留带宽的增加值与链路原有可预留带宽的比值大于等于此百分比阈值时，IGP将进行泛洪，并更新流量工程数据库。

*[percent*]：带宽变化的百分比阈值，取值范围为0～100。

【使用指导】

链路的可预留带宽发生变化时，需要通过IGP泛洪链路的TE相关信息，以便将变化后的链路情况通知给网络中的设备。但是，频繁地IGP泛洪会增加网络中的流量，加大网络中设备的处理负担，并导致Ingress节点上频繁进行CSPF计算，占用过多的系统资源。通过本命令可以配置带宽变化达到一定程度时才进行IGP泛洪，以减轻网络负担。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置链路带宽减少100%时进行IGP泛洪。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te bandwidth change thresholds down 100

·交换应用

\# 在接口Vlan-interface10上配置链路带宽减少100%时进行IGP泛洪。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te bandwidth change thresholds down 100

【相关命令】

·**link-management periodic-flooding timer**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te bidirectional**

------------------------------------------------------------------------

**[mpls te bidirectional**]命令用来在MPLS TE隧道接口上启用双向隧道功能。

**[undo mpls te bidirectional**]命令用来恢复缺省情况。

【命令】

**[mpls te bidirectional**[ { **associated reverse-lsp** { **lsp-name** *lsp-name* \| **lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* } \| **co-routed**  { **active** \| **passive** **reverse-lsp lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* } }]]

**[undo mpls te bidirectional**]

【缺省情况】

未启用MPLS TE隧道接口的双向隧道功能，MPLS TE隧道接口上建立的隧道为MPLS TE单向隧道。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[associated reverse-lsp lsp-name** *lsp-name*]：配置Associated方式的MPLS TE双向隧道，并指定关联的反向CRLSP。*lsp-name*为反向静态CRLSP的名称，为1～15个字符的字符串，区分大小写。

**[associated reverse-lsp lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id*]：配置Associated方式的MPLS TE双向隧道，并指定关联的反向CRLSP。*ingress-lsr-id*为反向CRLSP的入节点LSR ID；*tunnel-id*为反向CRLSP的Tunnel ID，取值范围为0～65535。

**[co-routed**]：配置Co-routed方式的MPLS TE双向隧道。

**[active**]：指定本端作为Co-routed方式MPLS TE双向隧道的主动方。

**[passive** **reverse-lsp lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id*]：指定本端作为Co-routed方式MPLS TE双向隧道的被动方，并指定关联的反向CRLSP。*ingress-lsr-id*为反向CRLSP的入节点LSR ID；*tunnel-id*为反向CRLSP的Tunnel ID，取值范围为0～65535。被动方上需要指定反向CRLSP，以便将正、反两个方向的单向CRLSP关联为MPLS TE双向隧道。

【使用指导】

MPLS TE双向隧道的建立有如下几种方式：

·Co-routed方式：通过RSVP-TE信令协议建立MPLS TE双向隧道。配置Co-routed方式MPLS TE双向隧道时，隧道的两端节点需要分别配置为主动方（Active）和被动方（Passive）。

·Associated方式：通过配置手工将两条单向的CRLSP绑定，从而形成MPLS TE双向隧道。绑定在一起的两条单向CRLSP可以通过不同的方式建立，例如一个方向上的CRLSP使用静态方式建立，而另一个方向上的CRLSP使用RSVP-TE信令建立。绑定在一起的两条单向CRLSP使用的路径可以不同。

需要注意的是：

·建立Co-routed方式MPLS TE双向隧道时，必须配置建立隧道使用的信令协议为RSVP-TE。

·配置MPLS TE双向隧道时，在隧道两端都需要关闭PHP功能，为倒数第二跳分配非空标签。

·如果**mpls te bidirectional**与**mpls te backup**、**mpls te auto-bandwidth**、**mpls te reoptimization**或**mpls te fast-reroute**同时配置，则仅**mpls te bidirectional**生效。

【举例】

·Co-routed方式

 # 在隧道本端接口Tunnel0上启用MPLS TE双向隧道功能，配置为Co-routed方式的主动方

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 10.0.0.2

Sysname-Tunnel0 mpls te bidirectional co-routed active

\# 在隧道对端接口Tunnel1上启用MPLS TE双向隧道功能，并配置为Co-routed方式双向隧道的被动方，关联的反向CRLSP的入节点LSR ID为10.0.0.1，反向CRLSP的Tunnel ID为0。

\<Sysname\> system-view

Sysname interface tunnel 1 mode mpls-te

Sysname-Tunnel1 destination 10.0.0.1

Sysname-Tunnel1 mpls te bidirectional co-routed passive reverse-lsp lsr-id 10.0.0.1 tunnel-id 0

·Associated方式

\# 在隧道本端接口Tunnel0上启用MPLS TE双向隧道功能，并配置双向隧道建立方式为Associated方式，关联的反向CRLSP的入节点LSR ID为10.0.0.2，反向CRLSP的Tunnel ID为1。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 destination 10.0.0.2

Sysname-Tunnel0 mpls te bidirectional associated reverse-lsp lsr-id 10.0.0.2 tunnel-id 1

\# 在隧道对端接口Tunnel1上启用MPLS TE双向隧道功能，并配置双向隧道建立方式为Associated方式，关联的反向CRLSP的入节点LSR ID为10.0.0.1，反向CRLSP的Tunnel ID为0。

\<Sysname\> system-view

Sysname interface tunnel 1 mode mpls-te

Sysname-Tunnel1 destination 10.0.0.1

Sysname-Tunnel1 mpls te bidirectional associated reverse-lsp lsr-id 10.0.0.1 tunnel-id 0

【相关命令】

·**display mpls te tunnel-interface**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te enable (Interface view)**

------------------------------------------------------------------------

**[mpls te enable**]命令用来开启接口的MPLS TE能力。

**[undo mpls te enable**]命令用来关闭接口的MPLS TE能力。

【命令】

**[mpls te enable**]

**[undo mpls te enable**]

【缺省情况】

接口上的MPLS TE能力处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过**mpls te enable**命令开启接口的MPLS TE能力后，该接口可以作为MPLS TE隧道的一部分。

在接口上执行**undo mpls te enable**命令后，将关闭接口的MPLS TE能力，并拆除接口上所有的CRLSP。

【举例】

·路由应用

\# 开启接口GigabitEthernet1/0/1的MPLS TE能力。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te enable

·交换应用

\# 开启接口Vlan-interface10的MPLS TE能力。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te enable

【相关命令】

·**display mpls te link-management bandwidth-allocation**

·**mpls te**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te enable (IS-IS view)**

------------------------------------------------------------------------

**[mpls te enable**]命令用来在当前IS-IS进程下使能MPLS TE能力。

**[undo mpls te enable**]命令用来恢复缺省情况。

【命令】

**[mpls te enable **[[ **level-1** \| **level-2** ]]]

**[undo mpls te enable **[[ **level-1** \| **level-2** ]]]

【缺省情况】

IS-IS进程的MPLS TE能力处于关闭状态。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level-1**]：在IS-IS Level-1使能MPLS TE能力。

**[level-2**]：在IS-IS Level-2使能MPLS TE能力。

【使用指导】

如果不指定级别，则同时使能Level-1和Level-2的MPLS TE能力。

IS-IS TE使用扩展IS可达性TLV（类型为22）的子TLV携带TE属性信息，扩展IS可达性TLV携带wide类型的开销值。因此，配置IS-IS TE时，必须配置IS-IS的开销值类型为**wide**、**compatible**或**wide-compatible**。有关IS-IS的介绍请参见"三层技术-IP路由配置指导"中的"IS-IS"。

在IS-IS视图下重复执行本命令，新的配置覆盖已有配置。例如，执行**mpls te enable**命令后执行**mpls te enable level-1**命令，则使能Level-1的MPLS TE能力，关闭Level-2的MPLS TE能力。

通过**mpls te enable**命令同时使能Level-1和Level-2的MPLS TE能力后，如果配置**undo mpls te enable level-1**命令，则仅关闭Level-1的MPLS TE能力，Level-2的MPLS TE能力仍然使能。配置**undo mpls te enable level-2**命令，与此类似。

【举例】

\# 为IS-IS进程1的Level-2使能MPLS TE能力。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 cost-style compatible

Sysname-isis-1 mpls te enable level-2

【相关命令】

·**cost-style**（三层技术-IP路由命令参考/IS-IS）

**MPLS TE \-- MPLS TE配置命令 \-- mpls te enable (OSPF area view)**

------------------------------------------------------------------------

**[mpls te enable**]命令用来在当前OSPF区域下使能MPLS TE能力。

**[undo mpls te enable**]命令用来恢复缺省情况。

【命令】

**[mpls te enable**]

**[undo mpls te enable**]

【缺省情况】

OSPF区域的MPLS TE能力处于关闭状态。

【视图】

OSPF区域视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

OSPF TE使用Opaque Type 10 LSA携带链路的TE属性信息，因此，配置OSPF TE时必须先通过**opaque-capability**命令使能OSPF的Opaque能力。有关OSPF Opaque能力的介绍请参见"三层技术-IP路由配置指导"中的"OSPF"。

【举例】

\# 在OSPF进程1区域1使能MPLS TE能力。

\<Sysname\> system-view

Sysname ospf 1

Sysname-ospf-1 area 1

Sysname-ospf-1-area-0.0.0.1 mpls te enable

【相关命令】

·**opaque-capability**（三层技术-IP路由命令参考/OSPF）

**MPLS TE \-- MPLS TE配置命令 \-- mpls te fast-reroute**

------------------------------------------------------------------------

**[mpls te fast-reroute**]命令用来开启快速重路由功能。

**[undo mpls te fast-reroute**]命令用来关闭快速重路由功能。

【命令】

**[mpls te fast-reroute ** **bandwidth** ]

**[undo mpls te fast-reroute**]

【缺省情况】

快速重路由功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bandwidth**]：指定主CRLSP需要进行带宽保护。如果不指定本参数，则表示主CRLSP不需要进行带宽保护。

【使用指导】

FRR（Fast Reroute，快速重路由）是MPLS TE中实现网络局部保护的技术。FRR的切换速度可以达到50ms，能够最大程度减少网络故障时数据的丢失。

开启隧道的FRR功能后，当主CRLSP上的某条链路或某个节点失效时，流量会被切换到Bypass隧道上。同时，隧道的Ingress节点尝试建立新的CRLSP。新的CRLSP建立成功后，流量将切换到新的CRLSP。

不需要进行带宽保护时，主CRLSP优选不提供保护带宽的Bypass隧道，表明FRR切换后不要求带宽保证；需要进行带宽保护时，主CRLSP优选具有足够保护带宽的Bypass隧道，以提供FRR切换后的带宽保证。

需要注意的是：

·通过本命令开启了隧道的快速重路由功能后，将自动启动该隧道的标签记录功能，而不管用户是否配置了**mpls te record-route label**命令。

·无论主CRLSP是否要求带宽保护，一旦主CRLSP和提供保护带宽的Bypass隧道绑定，就会占用保护带宽，在PLR节点的RRO信息中可以看到带宽保护标记。

·如果同时配置了**mpls te fast-reroute**和**mpls te bidirectional**，则仅**mpls te bidirectional**生效。

【举例】

\# 开启接口Tunnel0的快速重路由功能。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te fast-reroute

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te backup bandwidth**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te fast-reroute bypass-tunnel**

------------------------------------------------------------------------

**[mpls te fast-reroute bypass-tunnel**]命令用来为被保护的接口（当前接口）指定一条Bypass隧道。

**[undo mpls te fast-reroute bypass-tunnel**]命令用来删除指定的Bypass隧道。

【命令】

**[mpls te fast-reroute bypass-tunnel**]**tunnel** *tunnel-number*

**[undo **]**mpls te fast-reroute bypass-tunnel****tunnel** *tunnel-number*

【缺省情况】

接口上不存在任何Bypass隧道。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[tunnel**]* tunnel-number*：指定Bypass隧道对应的隧道接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

执行本命令后，如果主CRLSP的出接口（当前接口）Down、通过BFD或Hello机制检测到邻居故障，则会将主CRLSP的报文切换到Bypass隧道进行转发。

通过多次执行**mpls te fast-reroute bypass-tunnel**命令，可以为一个接口指定多条Bypass隧道。最多可以为一个被保护接口指定3条Bypass隧道。

一条隧道最多可以保护3个接口。

需要注意的是：

·Bypass隧道必须使用RSVP信令协议建立。

·被保护的接口不能是Bypass隧道的出接口。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上使用隧道接口Tunnel0作为Bypass隧道。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te fast-reroute bypass-tunnel tunnel 0

·交换应用

\# 在接口Vlan-interface10上使用隧道接口Tunnel0作为Bypass隧道。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te fast-reroute bypass-tunnel tunnel 0

【相关命令】

·**fast-reroute timer**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te igp advertise**

------------------------------------------------------------------------

**[mpls te igp advertise**]命令用来开启转发邻接功能，即将MPLS TE隧道/捆绑隧道作为一条链路发布到IGP路由中。

**[undo mpls te igp advertise**]命令用来恢复缺省情况。

【命令】

Tunnel接口视图：

**[mpls te igp advertise** [ **hold-time** *value* ]]

**[undo mpls te igp advertise**]

Tunnel-Bundle接口视图：

**[mpls te igp advertise**]

**[undo mpls te igp advertise**]

【缺省情况】

转发邻接功能处于关闭状态，即不会将MPLS TE隧道/捆绑隧道作为一条链路发布到IGP路由中。

【视图】

Tunnel接口视图/Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hold-time ***value*]：MPLS TE隧道状态发生变化，即由up状态变更为down状态或由down状态变更为up状态后，通过IGP发布该信息的等待时间。*value*取值范围为0～4294967295，单位为毫秒，缺省值为0毫秒，即MPLS TE隧道状态变化后，立即通过IGP发布该信息。

【使用指导】

转发邻接功能是将流量引入MPLS TE隧道/捆绑隧道的一种方式。该功能将MPLS TE隧道/捆绑隧道当作一条直接连接隧道Ingress节点和Egress节点的链路，通过IGP路由协议将该链路发布到网络中，以便网络中的节点在路由计算时使用MPLS TE隧道/捆绑隧道。

IGP Shortcut和转发邻接功能的区别在于：

·在隧道的Ingress节点上开启IGP Shortcut功能后，只有Ingress节点计算IGP路由时会考虑MPLS TE隧道/捆绑隧道。IGP Shortcut功能不会通过IGP路由协议将MPLS TE隧道/捆绑隧道作为一条链路发布出去。因此，其他设备在路由计算时不会考虑MPLS TE隧道/捆绑隧道。

·在隧道的Ingress节点上开启转发邻接功能后，Ingress节点会通过IGP路由协议将MPLS TE隧道/捆绑隧道作为一条链路发布出去。因此，IGP网络中的所有设备在路由计算时都会考虑MPLS TE隧道/捆绑隧道。

需要注意的是：

·使用转发邻接功能时，需要在隧道两端节点上都建立到达对方的MPLS TE隧道/捆绑隧道，并在两端节点上都开启转发邻接功能。

·如果在同一个Tunnel接口/Tunnel-Bundle接口下重复执行**mpls te igp advertise**命令和**mpls te igp shortcut**命令，则新的配置覆盖原有配置。

·Tunnel接口成为Tunnel-Bundle接口的成员接口后，该Tunnel接口下的**hold-time**配置仍然可以生效。建议在该Tunnel接口下使用**undo**命令取消hold-time配置，避免Tunnel-Bundle接口的状态受到影响。

【举例】

\# 开启转发邻接功能，并配置MPLS TE隧道状态变化后通过IGP发布该信息的等待时间为10000毫秒。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te igp advertise hold-time 10000

【相关命令】

·**mpls te igp metric**

·**mpls te igp shortcut**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te igp metric**

------------------------------------------------------------------------

**[mpls te igp metric**]命令用来配置MPLS TE隧道/捆绑隧道的度量值。

**[undo mpls te igp metric**]命令用来恢复缺省情况。

【命令】

**[mpls te igp metric**[ { **absolute** *value* \| **relative** *value* }]]

**[undo mpls te igp metric**]

【缺省情况】

MPLS TE隧道/捆绑隧道的度量值等于其IGP度量值。

【视图】

Tunnel接口视图/Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[absolute*** value*]：以绝对值的方式指定MPLS TE隧道/捆绑隧道的度量值，即MPLS TE隧道/捆绑隧道的度量值为配置的值*value*。*value*为正整数，取值范围为1～65535。

**[relative*** value*]：以相对值的方式指定MPLS TE隧道/捆绑隧道的度量值，即MPLS TE隧道/捆绑隧道的度量值为配置的值*value*+MPLS TE隧道/捆绑隧道的IGP度量值。*value*可以是正整数、负整数或0，取值范围为-10～10。

【使用指导】

使用IGP Shortcut功能时，MPLS TE隧道/捆绑隧道作为一条链路参与IGP路由的计算。MPLS TE隧道/捆绑隧道这条链路在路由计算过程中的度量值可以通过本命令来配置。

【举例】

\# 配置在IGP Shortcut功能中计算IGP路由时，MPLS TE隧道Tunnel0的度量值为该隧道的IGP度量值-1。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te igp metric relative -1

【相关命令】

·**mpls te igp shortcut**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te igp shortcut**

------------------------------------------------------------------------

**[mpls te igp shortcut**]命令用来开启IGP Shortcut功能，即在隧道的Ingress节点上将MPLS TE隧道/捆绑隧道当作一条链路参与IGP路由的计算。

**[undo mpls te igp shortcut**]命令用来恢复缺省情况。

【命令】

**[mpls te igp shortcut**[ [ **isis** \| **ospf** ]]]

**[undo mpls te igp shortcut**]

【缺省情况】

IGP Shortcut功能处于关闭状态，即在隧道的Ingress节点上进行IGP路由计算时不考虑MPLS TE隧道/捆绑隧道。

【视图】

Tunnel接口视图/Tunnel-Bundle接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[isis**]：指定在IS-IS协议的路由计算中考虑MPLS TE隧道/捆绑隧道。

**[ospf**]：指定在OSPF协议的路由计算中考虑MPLS TE隧道/捆绑隧道。

【使用指导】

IGP Shortcut功能是将流量引入MPLS TE隧道/捆绑隧道的一种方式。该功能将MPLS TE隧道/捆绑隧道当作一条直接连接隧道Ingress节点和Egress节点的链路，在隧道的Ingress节点上进行IGP路由计算时考虑该MPLS TE隧道/捆绑隧道。

IGP Shortcut和转发邻接功能的区别在于：

·在隧道的Ingress节点上开启IGP Shortcut功能后，只有Ingress节点计算IGP路由时会考虑MPLS TE隧道/捆绑隧道。IGP Shortcut功能不会通过IGP路由协议将MPLS TE隧道/捆绑隧道作为一条链路发布出去。因此，其他设备在路由计算时不会考虑MPLS TE隧道/捆绑隧道。

·在隧道的Ingress节点上开启转发邻接功能后，Ingress节点会通过IGP路由协议将MPLS TE隧道/捆绑隧道作为一条链路发布出去。因此，IGP网络中的所有设备在路由计算时都会考虑MPLS TE隧道/捆绑隧道。

需要注意的是：

·执行本命令时如果不指定IGP类型，则OSPF和IS-IS协议的路由计算中都考虑MPLS TE隧道/捆绑隧道。

·如果在同一个Tunnel接口/Tunnel-Bundle接口下重复执行**mpls te igp advertise**命令和**mpls te igp shortcut**命令，则新的配置覆盖原有配置。

【举例】

\# 开启IGP Shortcut功能，在MPLS TE隧道Tunnel0的Ingress节点上将该隧道当作一条链路参与OSPF和IS-IS路由的计算

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te igp shortcut

【相关命令】

·**mpls te igp advertise**

·**mpls te igp metric**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te link-attribute**

------------------------------------------------------------------------

**[mpls te link-attribute**]命令用来配置链路的属性。

**[undo mpls te link-attribute**]命令用来恢复缺省情况。

【命令】

**[mpls te link-attribute** *attribute-value*]

**[undo mpls te link-attribute**]

【缺省情况】

链路的属性值为0x00000000。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[attribute-value*]：链路的属性，取值范围为0x00000000到0xFFFFFFFF，即为32位的二进制数，每一位二进制数代表一个属性，属性值为0或1。

【使用指导】

设备通过IGP发布的链路TE相关信息中包括本命令配置的链路属性。隧道的Ingress节点获取到该信息后，根据Ingress节点上配置的隧道亲和属性，判断建立MPLS TE隧道时是否可以使用该链路。如果希望某条链路能够被隧道所用，则需要满足如下要求：

·对于掩码为1的位，亲和属性为1的位中链路属性至少有1位也为1，亲和属性为0的位对应的链路属性位不能为1。

·对于掩码为0的位，不对链路属性的相应位进行检查。

例如，亲和属性为0xFFFFFFF0，掩码为0x0000FFFF，则可用链路的链路属性高16位可以任意取0或1，17～28位中至少有1位为1，且低4位不能为1。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置该链路的属性为0x00000101。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te link-attribute 101

·交换应用

\# 在接口Vlan-interface10上配置该链路的属性为0x00000101。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te link-attribute 101

【相关命令】

·**mpls te affinity-attribute**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te loop-detection**

------------------------------------------------------------------------

**[mpls te loop-detection**]命令用来配置隧道建立时进行环路检测。

**[undo mpls te loop-detection**]命令用来取消环路检测功能。

【命令】

**[mpls te loop-detection**]

**[undo mpls te loop-detection**]

【缺省情况】

隧道建立时不进行环路检测。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过本命令配置隧道建立时进行环路检测后，将自动启动该隧道的路由记录功能，而不管用户是否配置了**mpls te record-route**命令。隧道经过的节点根据记录的路由信息，判断是否出现环路。

【举例】

\# 配置建立MPLS TE隧道Tunnel0时进行环路检测。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te loop-detection

**MPLS TE \-- MPLS TE配置命令 \-- mpls te max-link-bandwidth**

------------------------------------------------------------------------

**[mpls te max-link-bandwidth**]命令用来配置用于转发MPLS TE流量的链路最大带宽。

**[undo mpls te max-link-bandwidth**]命令用来恢复缺省情况。

【命令】

**[mpls te max-link-bandwidth*** bandwidth-value*]

**[undo mpls te max-link-bandwidth**]

【缺省情况】

用于转发MPLS TE流量的链路最大带宽为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：链路的最大带宽，取值范围为1～4294967295，单位为kbps。

【使用指导】

设备在发布的IGP路由中携带本命令配置的链路最大带宽值，以便隧道的Ingress节点获取到该信息，并根据该信息进行CSPF计算，选择符合隧道带宽要求的路径。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1用于转发MPLS TE流量的链路最大带宽为1158kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te max-link-bandwidth 1158

·交换应用

\# 配置接口Vlan-interface10用于转发MPLS TE流量的链路最大带宽为1158kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te max-link-bandwidth 1158

【相关命令】

·**display mpls te link-management bandwidth-allocation**

·**mpls te bandwidth**

·**mpls te max-reservable-bandwidth**

·**mpls te max-reservable-bandwidth mam**

·**mpls te max-reservable-bandwidth ****rdm**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te max-reservable-bandwidth**

------------------------------------------------------------------------

**[mpls te max-reservable-bandwidth**]命令用来配置Prestandard DS-TE模式下RDM带宽约束模型BC 0和BC 1的最大可预留带宽。

**[undo mpls te max-reservable-bandwidth**]命令用来恢复缺省情况。

【命令】

**[mpls te max-reservable-bandwidth ***bandwidth-value* [ **bc1** ]*bc1-bandwidth*]

**[undo mpls te max-reservable-bandwidth**]

【缺省情况】

最大可预留带宽为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：链路的最大可预留带宽，即BC 0的最大可预留带宽，取值范围为1～4294967295，单位为kbps。

**[bc1**]*bc1-bandwidth*：BC 1的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

【使用指导】

设备在发布的IGP路由中携带本命令配置的最大可预留带宽值，以便隧道的Ingress节点获取到该信息，并根据该信息进行CSPF计算，选择符合隧道带宽要求的路径。

需要注意的是：

·链路的最大可预留带宽*bandwidth-value*不能大于**mpls te max-link-bandwidth**命令配置的链路最大带宽，且BC 1的最大可预留带宽*bc1-bandwidth*不能大于链路的最大可预留带宽*bandwidth-value*。

·本命令配置的链路最大可预留带宽只能用于MPLS TE流量。

【举例】

·路由应用

\# Prestandard模式下配置链路上最多可以为MPLS TE流量预留1158kbps的带宽，BC 1的最大可预留带宽为200kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te max-reservable-bandwidth 1158 bc1 200

·交换应用

\# Prestandard模式下配置链路上最多可以为MPLS TE流量预留1158kbps的带宽，BC 1的最大可预留带宽为200kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te max-reservable-bandwidth 1158 bc1 200

【相关命令】

·**display mpls te link-management bandwidth-allocation**

·**mpls te bandwidth**

·**mpls te max-link-bandwidth**

·**mpls te max-reservable-bandwidth mam**

·**mpls te max-reservable-bandwidth ****rdm**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te max-reservable-bandwidth mam**

------------------------------------------------------------------------

**[mpls te max-reservable-bandwidth mam**]命令用来配置IETF DS-TE模式下MAM带宽约束模型的MPLS TE链路最大可预留带宽及各BC的最大可预留带宽。

**[undo mpls te max-reservable-bandwidth mam**]命令用来恢复缺省情况。

【命令】

**[mpls te max-reservable-bandwidth mam **]*bandwidth-value *[{ **bc0** *bc0-bandwidth* \| **bc1** *bc1-bandwidth* \| **bc2** *bc2-bandwidth* \| **bc3** *bc3-bandwidth* } \*]

**[undo mpls te max-reservable-bandwidth mam**]

【缺省情况】

最大可预留带宽均为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：链路的最大可预留带宽，取值范围为1～4294967295，单位为kbps。

**[bc0**]* bc0-bandwidth*：BC 0的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

**[bc1**] *bc1-bandwidth*：BC 1的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

**[bc2**] *bc2-bandwidth*：BC 2的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

**[bc3**] *bc3-bandwidth*：BC 3的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

【使用指导】

设备在发布的IGP路由中携带本命令配置的最大可预留带宽值，以便隧道的Ingress节点获取到该信息，并根据该信息进行CSPF计算，选择符合隧道带宽要求的路径。

需要注意的是：

·链路的最大可预留带宽*bandwidth-value*不能大于**mpls te max-link-bandwidth**命令配置的链路最大带宽；所有BC的最大可预留带宽均不能大于链路的最大可预留带宽，即*bc0-bandwidth*、*bc1-bandwidth*、*bc2-bandwidth*和*bc3-bandwidth*不能大于*bandwidth-value*。

·本命令配置的链路最大可预留带宽只能用于MPLS TE流量。

【举例】

·路由应用

\# 配置IETF模式MAM带宽约束模型下链路上最多可以为MPLS TE流量预留1158kbps的带宽，BC 0的最大可预留带宽为500kbps，BC 1的最大可预留带宽为300kbps，BC 2的最大可预留带宽为400kbps，BC 3的最大可预留带宽为100kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te max-reservable-bandwidth mam 1158 bc0 500 bc1 300 bc2 400 bc3 100

·交换应用

\# 配置IETF模式MAM带宽约束模型下链路上最多可以为MPLS TE流量预留1158kbps的带宽，BC 0的最大可预留带宽为500kbps，BC 1的最大可预留带宽为300kbps，BC 2的最大可预留带宽为400kbps，BC 3的最大可预留带宽为100kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te max-reservable-bandwidth mam 1158 bc0 500 bc1 300 bc2 400 bc3 100

【相关命令】

·**display mpls te link-management bandwidth-allocation**

·**mpls te bandwidth**

·**mpls te max-link-bandwidth**

·**mpls te max-reservable-bandwidth**

·**mpls te max-reservable-bandwidth ****rdm**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te max-reservable-bandwidth rdm**

------------------------------------------------------------------------

**[mpls te max-reservable-bandwidth rdm**]命令用来配置IETF DS-TE模式RDM带宽约束模型各BC的最大可预留带宽。

**[undo mpls te max-reservable-bandwidth rdm**]命令用来恢复缺省情况。

【命令】

**[mpls te max-reservable-bandwidth rdm **]*bandwidth-value***** **bc1** *bc1-bandwidth*   **bc2** *bc2-bandwidth*   **bc3** *bc3-bandwidth*

**[undo mpls te max-reservable-bandwidth rdm**]

【缺省情况】

BC 0、BC 1、BC 2和BC 3的最大可预留带宽均为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：链路的最大可预留带宽，即BC 0的最大可预留带宽，取值范围为1～4294967295，单位为kbps。

**[bc1**] *bc1-bandwidth*：BC 1的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

**[bc2**] *bc2-bandwidth*：BC 2的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

**[bc3**] *bc3-bandwidth*：BC 3的最大可预留带宽，取值范围为1～4294967295，单位为kbps，缺省值为0。

【使用指导】

设备在发布的IGP路由中携带本命令配置的最大可预留带宽值，以便隧道的Ingress节点获取到该信息，并根据该信息进行CSPF计算，选择符合隧道带宽要求的路径。

需要注意的是：

·BC 0的最大预留带宽*bandwidth-value*必须小于等于**mpls te max-link-bandwidth**命令配置的最大链路带宽；BC 0的最大预留带宽*bandwidth-value*必须大于等于BC 1的最大预留带宽*bc1-bandwidth*；BC 1的最大预留带宽*bc1-bandwidth*必须大于等于BC 2的最大预留带宽*bc2-bandwidth*；BC 2的最大预留带宽*bc2-bandwidth*必须大于等于BC 3的最大预留带宽*bc3-bandwidth*。

·本命令配置的链路最大可预留带宽只能用于MPLS TE流量。

【举例】

·路由应用

\# 配置IETF模式RDM带宽约束模型下BC 0的最大可预留带宽为500kbps，BC 1的最大可预留带宽为400kbps，BC 2的最大可预留带宽为300kbps，BC 3的最大可预留带宽为100kbps。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te max-reservable-bandwidth rdm 500 bc1 400 bc2 300 bc3 100

·交换应用

\# 配置IETF模式RDM带宽约束模型下BC 0的最大可预留带宽为500kbps，BC 1的最大可预留带宽为400kbps，BC 2的最大可预留带宽为300kbps，BC 3的最大可预留带宽为100kbps。

\<Sysname\> system-view

Sysname interface vlan-interface 1

Sysname-Vlan-interface1 mpls te max-reservable-bandwidth rdm 500 bc1 400 bc2 300 bc3 100

【相关命令】

·**display mpls te link-management bandwidth-allocation**

·**mpls te bandwidth**

·**mpls te max-link-bandwidth**

·**mpls te max-reservable-bandwidth**

·**mpls te max-reservable-bandwidth mam**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te metric**

------------------------------------------------------------------------

**[mpls te metric**]命令用来配置链路的TE度量值。

**[undo** **mpls te metric**]命令用来恢复缺省情况。

【命令】

**[mpls te metric**] *value*

**[undo mpls te metric**]

【缺省情况】

链路使用其IGP度量作为TE的度量值。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路的TE度量值，取值范围是1～4294967295。

【使用指导】

设备在发布的IGP路由中携带链路的两种度量值：IGP度量值和TE度量值。其中，链路的TE度量值可以通过本命令来配置。隧道的Ingress节点获取到链路的度量值后，根据Ingress节点设备上**mpls te path-metric-type**命令或**path-metric-type**命令的配置，决定选择路径时采用IGP度量值还是TE度量值。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置链路的TE度量值为20。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mpls te metric 20

·交换应用

\# 在接口Vlan-interface10上配置链路的TE度量值为20。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 mpls te metric 20

【相关命令】

·**mpls te path metric-type**

·**path metric-type**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te path**

------------------------------------------------------------------------

**[mpls te path**]命令用来配置CRLSP应用的路径及路径的优先级。

**[undo mpls te path**]命令用来删除指定的路径。

【命令】

**[mpls te path preference ***value *{ **dynamic** [ **pce** [ *ip-address* &\<0-8\> ] \| **explicit-path** *path-name* }  **no-cspf** ]]

**[undo mpls te path preference ***value*]

【缺省情况】

使用自动计算的路径建立CRLSP。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[preference** *value*]：指定路径的优先级。*value*的取值范围为1～10，数值越小，优先级越高。

**[dynamic**]：使用自动计算的路径建立CRLSP。

**[pce**]：使用PCE计算路径。如果不指定本参数，则本地LSR通过CSPF自动计算路径。

 *ip-address* &\<0-8\>：指定计算路径的PCE的IP地址，如果不指定本参数，则自动选择PCE。&\<0-8\>表示前面的参数最多可以输入8次。

**[explicit-path** *path-name*]：引用已经存在的显式路径，根据该显式路径的要求建立CRLSP。*path-name*为显式路径名称，为1～31个字符的字符串，区分大小写。

**[no-cspf**]：不使用CSPF算法计算路径，通过查找路由来计算路径。

【使用指导】

一个Tunnel接口下最多可以配置10条路径。不同路径的优先级不能相同。

建立CRLSP时，按照优先级从高到低的顺序，依次根据配置的路径进行CSPF计算，直到成功建立CRLSP。如果所有路径的CSPF计算都失败，则无法建立CRLSP。

如果指定的PCE地址数目大于或等于2，则会按照配置的PCE地址的顺序发起BRPC计算，否则发起EPC计算。

如果使用该命令或**mpls te backup-path**命令指定了PCE的IP地址，则仅与指定的PCE建立PCEP会话；否则与所有发现的PCE建立会话。

【举例】

\# 配置Tunnel0可以使用显式路径path1和PCE计算的路径建立CRLSP，且优先使用PCE计算路径。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te path preference 2 explicit-path path1

Sysname-Tunnel0 mpls te path preference 1 dynamic pce 1.1.1.9 2.2.2.9

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te backup-path**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te path-metric-type**

------------------------------------------------------------------------

**[mpls te path-metric-type**]命令用来配置为当前隧道选路时使用的链路度量值类型。

**[undo mpls te path-metric-type**]命令用来恢复缺省情况。

【命令】

**[mpls te path-metric-type**  { **igp** \| **te** }]

**[undo mpls te path-metric-type**]

【缺省情况】

没有指定当前隧道选路时使用的链路度量值类型。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[igp**]：使用IGP度量。

**[te**]：使用TE度量。

【使用指导】

在MPLS TE中每条链路都具有两种度量值：IGP度量值和TE度量值。通过合理地规划两种度量值，可以实现为不同种类的业务选择不同的隧道。例如，使用IGP度量值来表示链路延迟的大小（IGP度量值越小，链路的延迟越小），使用TE度量值来表示链路带宽的大小（TE度量值越小，链路的带宽越大）。建立两条MPLS TE隧道（Tunnel1和Tunnel2），分别用来承载语音业务和视频业务。Tunnel1选择路径时使用IGP度量值，可以实现为延迟要求较高的语音业务选择延迟小的路径；Tunnel2选择路径时使用TE度量值，可以实现为数据量较大的视频业务选择带宽大的路径。

如果在Tunnel接口视图下执行了本命令，则该隧道使用本接口下配置的度量值类型选择路径；否则，使用MPLS TE视图下**path-metric-type**命令配置的度量值类型选择路径。

【举例】

\# 配置为隧道Tunnel0选路时使用IGP度量。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te path-metric-type igp

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te metric**

·**path-metric-type**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te priority**

------------------------------------------------------------------------

**[mpls te** **priority**]命令用来配置MPLS TE隧道的建立优先级和保持优先级。

**[undo mpls te priority**]命令用来恢复缺省情况。

【命令】

**[mpls te priority** *setup-priority* [ *hold-priority* ]]

**[undo mpls te priority**]

【缺省情况】

建立优先级和保持优先级都为7。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[setup-priority*]：建立优先级，取值范围为0～7，数值越小优先级越高。

*[hold-priority*]：保持优先级，取值范围为0～7，数值越小优先级越高。如果不指定本参数，则保持优先级与建立优先级相同。

【使用指导】

建立优先级和保持优先级标识了MPLS TE隧道的重要程度。数值越小，优先级越高，MPLS TE隧道越重要。如果一条隧道的建立优先级数值小于另一条隧道的保持优先级，则该隧道可以抢占另一条隧道的资源。

建立优先级和保持优先级可以应用在以下场景：

·多条MPLS TE隧道经过相同的路径，而该路径上的带宽不足以满足所有隧道的带宽要求时，通过为不同的隧道配置不同的建立优先级和保持优先级，可以确保重要的隧道能够优先建立。

·在重要的隧道建立之前，网络中已经建立了多条MPLS TE隧道，占用了带宽资源，使得重要的隧道无法使用最优路径建立。此时，通过为重要的隧道配置更高的优先级，可以使得该隧道抢占已建立隧道的资源，采用最优路径建立重要隧道。

需要注意的是，隧道的建立优先级不能高于该隧道的保持优先级，即其在数值上应大于或等于保持优先级。

【举例】

\# 配置隧道Tunnel0的建立优先级和保持优先级都为1。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te priority 1 1

【相关命令】

·**display mpls te tunnel-interface**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te record-route**

------------------------------------------------------------------------

**[mpls te record-route**]命令用来开启隧道的路由记录或标签记录功能。

**[undo mpls te record-route**]命令用来恢复缺省情况。

【命令】

**[mpls te record-route**  **label** ]

**[undo mpls te record-route**]

【缺省情况】

隧道的路由记录和标签记录功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[label**]：同时开启路由记录和标签记录功能。如果不指定本参数，则仅开启路由记录功能，未开启标签记录功能。

【使用指导】

路由记录和标签记录功能用来记录MPLS TE隧道经过的各个节点及各个节点分配的标签值，以便用户根据记录的信息了解MPLS TE隧道经过的路径和标签分配情况。在MPLS TE隧道出现故障时，用户也可以根据记录的信息对故障进行定位。

【举例】

\# 开启MPLS TE隧道Tunnel0的路由记录功能。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te record-route

【相关命令】

·**display mpls te tunnel-interface**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te reoptimization (Tunnel Interface view)**

------------------------------------------------------------------------

**[mpls te reoptimization**]命令用来开启隧道重优化功能。

**[undo mpls te reoptimization**]命令用来关闭隧道重优化功能。

【命令】

**[mpls te reoptimization ** **frequency** *seconds* ]

**[undo mpls te reoptimization**]

【缺省情况】

隧道重优化功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[frequency** *seconds*]：指定隧道重优化频率。*seconds*取值范围为1～604800，单位为秒，缺省值为3600秒，即1小时。

【使用指导】

隧道重优化功能是指周期性地或通过在用户视图下执行**mpls te reoptimization**命令手工触发隧道Ingress节点重新选择路径，以便将MPLS TE隧道切换到当前的最优路径。例如，如果在MPLS TE隧道建立时，最优路径上的链路没有足够的可预留带宽，则会导致MPLS TE隧道未使用最优路径建立。通过隧道重优化功能，可以实现链路上具有足够的带宽时将MPLS TE隧道自动切换到最优路径。

在同一个Tunnel接口下，隧道重优化功能与以下命令互斥：**mpls te auto-bandwidth adjustment**，**mpls te route-pinning**和**mpls te backup**。

如果同时配置了**mpls te reoptimization**和**mpls te bidirectional**，则仅**mpls te bidirectional**生效。

【举例】

\# 开启隧道Tunnel0的重优化功能，并配置每隔43200秒（12小时）重新计算路由。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te reoptimization frequency 43200

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te reoptimization** (User view)

**MPLS TE \-- MPLS TE配置命令 \-- mpls te reoptimization (User view)**

------------------------------------------------------------------------

**[mpls te reoptimization**]命令用来立即对所有开启了重优化功能的MPLS TE隧道进行重优化。

【命令】

**[mpls te reoptimization**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在Tunnel接口视图下通过**mpls te reoptimization**命令开启了该隧道的重优化功能后，在用户视图下执行本命令可以手工触发隧道Ingress节点重新为该隧道选择路径，以便将MPLS TE隧道切换到当前的最优路径。

【举例】

\# 立即对所有开启了重优化功能的MPLS TE隧道进行重优化。

\<Sysname\> mpls te reoptimization

【相关命令】

·**mpls te reoptimization** (Tunnel Interface view)

**MPLS TE \-- MPLS TE配置命令 \-- mpls te resv-style**

------------------------------------------------------------------------

**[mpls te resv-style**]命令用来配置隧道的资源预留风格。

**[undo**] **mpls te resv-style**命令用来恢复缺省情况。

【命令】

**[mpls te resv-style**  { **ff** \| **se** }]

**[undo**] **mpls te resv-style**

【缺省情况】

隧道的资源预留风格为SE。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ff**]：使用FF（Fixed-Filter，固定过滤器）资源预留风格。

**[se**]：使用SE（Shared-Explicit，共享显式）资源预留风格。

【使用指导】

FF资源预留风格是指为每个发送者单独预留资源，同一会话中的不同发送者不能共享资源。

SE资源预留风格是指为同一个会话中的不同发送者预留同一个资源，不同发送者之间可以共享资源。

需要注意的是，只有采用RSVP-TE协议建立MPLS TE隧道时，本命令才会生效。

【举例】

\# 配置使用FF资源预留风格建立MPLS TE隧道Tunnel0。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te resv-style ff

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te signaling**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te retry**

------------------------------------------------------------------------

**[mpls te retry**]命令用来配置尝试建立隧道的最大次数。

**[undo mpls te retry**]命令用来恢复缺省情况。

【命令】

**[mpls te retry **]*times*

**[undo mpls te retry**]

【缺省情况】

尝试建立隧道的最大次数为3次。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：尝试建立隧道的最大次数，取值范围为1～4294967295。

【使用指导】

MPLS TE隧道建立失败后，隧道的Ingress节点等待**mpls te timer retry**命令配置的隧道重建时间间隔后，将尝试重新建立隧道，直到隧道建立成功或尝试建立隧道的次数达到本命令配置的值。如果尝试建立隧道的次数达到本命令配置的值时仍未成功建立隧道，则等待较长的一段时间后，重复上述过程。

【举例】

\# 配置尝试建立隧道Tunnel0的最大次数为20次。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te retry 20

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te timer retry**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te route-pinning**

------------------------------------------------------------------------

**[mpls te**] **route-pinning**命令用来开启路由固定功能。

**[undo mpls te route-pinning**]命令用来关闭路由固定功能。

【命令】

**[mpls te route-pinning**]

**[undo mpls te route-pinning**]

【缺省情况】

路由固定功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

路由固定功能是指CRLSP创建成功后，该CRLSP不随路由变化而变化。

在路由变化频繁的网络中，如果不希望CRLSP随着路由频繁变化，则可以通过本功能确保只要已建立的CRLSP可用就不重新创建CRLSP。

在同一个Tunnel接口视图下，本命令与以下命令互斥：**mpls te reoptimization**命令和**mpls te auto-bandwidth adjustment**命令。

【举例】

\# 开启隧道Tunnel0的路由固定功能。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te route-pinning

【相关命令】

·**display mpls te tunnel-interface**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te signaling**

------------------------------------------------------------------------

**[mpls te signaling**]命令用来配置建立MPLS TE隧道使用的信令协议。

**[undo mpls te signaling**]命令用来恢复缺省情况。

【命令】

**[mpls te signaling**  { **rsvp-te** \| **static** }]

**[undo mpls te signaling**]

【缺省情况】

MPLS TE使用RSVP-TE信令协议建立隧道。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rsvp-te**]：使用RSVP-TE信令协议建立隧道。

**[static**]：使用静态CRLSP建立隧道。

【使用指导】

如果使用RSVP-TE信令协议建立MPLS TE隧道，则必须在隧道经过的路径上，开启接口的MPLS TE能力和RSVP-TE能力。

如果使用静态CRLSP建立隧道，则必须通过**mpls te static-cr-lsp**命令指定引用的静态CRLSP。

【举例】

\# 配置使用RSVP-TE信令协议建立MPLS TE隧道Tunnel0。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te signaling rsvp-te

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te static-cr-lsp**

**MPLS TE \-- MPLS TE配置命令 \-- mpls te static-cr-lsp**

------------------------------------------------------------------------

**[mpls te static-cr-lsp**]命令用来指定隧道引用的静态CRLSP。

**[undo mpls te static-cr-lsp**]命令用来取消引用静态CRLSP。

【命令】

**[mpls te static-cr-lsp** *lsp-name*]

**[undo mpls te static-cr-lsp** *lsp-name*]

【缺省情况】

隧道没有引用任何静态CRLSP。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lsp-name*]：引用的静态CRLSP的名称，为1～15个字符的字符串，区分大小写。

【使用指导】

只有在Tunnel接口视图下配置了**mpls te signaling static**命令，本命令才会生效。

本命令需要在Ingress节点上执行，即本命令中引用的静态CRLSP，必须是通过**static-cr-lsp ingress**命令创建的。

【举例】

\# 配置隧道Tunnel0引用名称为static-te-3的静态CRLSP。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te static-cr-lsp static-te-3

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te signaling**

·**static-cr-lsp egress**（MPLS命令参考/静态CRLSP）

·**static-cr-lsp ingress**（MPLS命令参考/静态CRLSP）

·**static-cr-lsp transit**（MPLS命令参考/静态CRLSP）

**MPLS TE \-- MPLS TE配置命令 \-- mpls te timer retry**

------------------------------------------------------------------------

**[mpls te timer retry**]命令用来配置隧道重建的时间间隔。

**[undo mpls te timer retry**]命令用来恢复缺省情况。

【命令】

**[mpls te timer retry** *seconds*]

**[undo mpls te timer retry**]

【缺省情况】

隧道重建的时间间隔为2秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：隧道重建的时间间隔，取值范围为1～604800，单位为秒。

【使用指导】

MPLS TE隧道建立失败后，隧道的Ingress节点等待本命令配置的隧道重建时间间隔后，将尝试重新建立隧道，直到隧道建立成功或尝试建立隧道的次数达到**mpls te retry**命令配置的值。如果尝试建立隧道的次数达到最大值时仍未成功建立隧道，则等待较长的一段时间后，重复上述过程。

【举例】

\# 配置每隔20秒重建隧道Tunnel0。

\<Sysname\> system-view

Sysname interface tunnel 0 mode mpls-te

Sysname-Tunnel0 mpls te timer retry 20

【相关命令】

·**display mpls te tunnel-interface**

·**mpls te retry**

**MPLS TE \-- MPLS TE配置命令 \-- nexthop**

------------------------------------------------------------------------

**[nexthop**]命令用来在显式路径中添加或修改节点及其属性（显式路径中是否包括添加的节点；添加的节点是松散下一跳，还是严格下一跳）。

**[undo nexthop**]命令用来删除显式路径中的指定节点。

【命令】

**[nexthop** [ **index** *index-number*  *ip-address* [ **exclude** \| **include** [ **loose** \| **strict** ] ]]]

**[undo nexthop index ***index-number*]

【缺省情况】

显式路径中不存在任何节点。

【视图】

显式路径视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index-number*]：节点在显式路径中的索引，取值范围为1～65535。如果不指定本参数，则自动计算索引值，大小为当前最大索引值+100。

*[ip-address*]：显式路径中节点的IP地址，点分十进制格式。

**[exclude**]：在显式路径中不能包括此节点。

**[include**]：指定在显式路径中需要包含此节点。

**[loose**]：指定的节点为松散下一跳，即上一跳与本节点可以不是直接相连。

**[strict**]：指定的节点为严格下一跳，即上一跳与本节点必须直接相连。

【使用指导】

本命令中指定的节点地址可以是：

·链路的IP地址：即设备上接口的IP地址，代表该地址所属的设备。

·设备的LSR ID：代表该设备。

严格下一跳的地址只能是链路的IP地址。松散下一跳的地址可以是链路的IP地址和设备的LSR ID。

对于**exclude**的节点，在CSPF计算时排除该地址对应的链路或设备；对于**include**的节点，CSPF计算时按照索引从小到大的顺序，依次查找符合节点地址要求的链路，以便建立CRLSP。

需要注意的是：

·执行**nexthop**命令时，如果指定了索引，且该索引已经存在，则修改节点的地址或属性。

·如果没有指定**include**和**exclude**关键字，则缺省为**include**，即在显式路径中需要包含此节点。

·如果没有指定**loose**和**strict**关键字，则缺省为**strict**，即上一跳与本节点必须直接相连。

【举例】

\# 配置MPLS TE显式路径中不包括IP地址10.0.0.125。

\<Sysname\> system-view

Sysname explicit-path path1

Sysname-explicit-path-path1 next-hop 10.0.0.125 exclude

【相关命令】

·**display explicit-path**

**MPLS TE \-- MPLS TE配置命令 \-- nhop-only**

------------------------------------------------------------------------

**[nhop-only**]命令用来配置仅自动创建链路保护类型的Bypass隧道。

**[undo nhop-only**]命令用来恢复缺省情况。

【命令】

**[nhop-only**]

**[undo nhop-only**]

【缺省情况】

链路保护和节点保护的Bypass隧道都会自动创建。

【视图】

MPLS TE自动隧道备份视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行**nhop-only**命令后，如果设备已创建节点保护类型的Bypass隧道，则节点保护类型的Bypass隧道将被删除。

执行**undo nhop-only**命令后，设备将恢复创建节点保护类型的Bypass隧道。

【举例】

\# 配置仅自动创建链路保护类型的Bypass隧道。

\<Sysname\> system-view

Sysname mpls te

Sysname-te auto-tunnel backup

Sysname-te-auto-bk nhop-only

【相关命令】

·**auto-tunnel backup**

·**tunnel-number**

**MPLS TE \-- MPLS TE配置命令 \-- path-metric-type**

------------------------------------------------------------------------

**[path-metric-type**]命令用来配置未配置度量类型的隧道选路时使用的链路度量值类型。

**[undo path-metric-type**]命令用来恢复缺省情况。

【命令】

**[path-metric-type**  { **igp** \| **te** }]

**[undo path-metric-type**]

【缺省情况】

未配置度量类型的隧道选路时使用TE度量值。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[igp**]：使用IGP度量。

**[te**]：使用TE度量。

【使用指导】

在MPLS TE中每条链路都具有两种度量值：IGP度量值和TE度量值。通过合理地规划两种度量值，可以实现为不同种类的业务选择不同的隧道。例如，使用IGP度量值来表示链路延迟的大小（IGP度量值越小，链路的延迟越小），使用TE度量值来表示链路带宽的大小（TE度量值越小，链路的带宽越大）。建立两条MPLS TE隧道（Tunnel1和Tunnel2），分别用来承载语音业务和视频业务。Tunnel1选择路径时使用IGP度量值，可以实现为延迟要求较高的语音业务选择延迟小的路径；Tunnel2选择路径时使用TE度量值，可以实现为数据量较大的视频业务选择带宽大的路径。

如果在Tunnel接口视图下执行了**mpls te path-metric-type**命令，则该隧道使用接口下配置的度量值类型选择路径；否则，使用本命令配置的度量值类型选择路径。

【举例】

\# 对所有未指定度量类型的MPLS TE隧道，配置其在进行路径计算时使用IGP度量值。

\<Sysname\> system-view

Sysname mpls te

Sysname-te path-metric-type igp

【相关命令】

·**mpls te metric**

·**mpls te path-metric-type**

**MPLS TE \-- MPLS TE配置命令 \-- pce address**

------------------------------------------------------------------------

**[pce address**]命令用来配置PCE的IP地址。

**[undo pce address**]命令用来删除PCE的IP地址。

【命令】

**[pce address ***ip-address*]

**[undo pce address**]

【缺省情况】

未配置PCE的IP地址。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：PCE的IP地址。

【使用指导】

配置PCE的IP地址后，本设备即可作为PCE。

建议配置PCE的IP地址为Loopback接口的IP地址，可在该Loopback接口上使能OSPF TE来发布PCE的信息，使PCC或其他PCE自动发现本PCE；或在PCC设备上静态指定本PCE的IP地址，建立PCEP会话。

如果未配置PCE的IP地址，则本设备仅可作为PCC，并使用LSR ID与PCE通信。PCC只能向PCE发起PCEP连接请求，不接受PCE的PCEP连接请求。

【举例】

\# 配置PCE的IP地址为10.10.10.10。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce address 10.10.10.10

**MPLS TE \-- MPLS TE配置命令 \-- pce deadtimer**

------------------------------------------------------------------------

**[pce deadtimer**]命令用来配置PCEP会话的保持时间。

**[undo pce deadtimer**]命令用来恢复缺省情况。

【命令】

**[pce deadtimer ***value*]

**[undo pce deadtimer**]

【缺省情况】

PCEP会话的保持时间为120秒。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：对等体之间的PCEP会话保持时间，取值范围为0～255，单位为秒。取值为0表示与对等体之间的会话不会超时。

【使用指导】

配置的**deadtimer**值会通告给对等体，对等体使用该值作为PCEP会话的保持时间。如果PCC或PCE在**deadtimer**内没有收到对等体发送的任何PCEP消息，则断开PCEP会话。会话中断后，对等体之间会尝试重新建立PCEP会话。

配置的**deadtimer**值必须大于**keepalive**值，否则会导致会话中断。

【举例】

\# 配置对等体之间的PCEP会话保持时间为180秒。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce deadtimer 180

【相关命令】

·**display mpls te pce peer**

·**pce keepalive**

**MPLS TE \-- MPLS TE配置命令 \-- pce keepalive**

------------------------------------------------------------------------

**[pce keepalive**]命令用来配置PCEP会话的Keepalive消息的发送时间间隔。

**[undo pce keepalive**]命令用来恢复缺省情况。

【命令】

**[pce keepalive*** interval*]

**[undo pce keepalive**]

【缺省情况】

Keepalive消息的发送时间间隔为30秒。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：Keepalive消息的发送时间间隔，取值范围为0～255，单位为秒。取值为0表示PCEP会话建立后不再发送Keepalive消息。

【使用指导】

对等体之间建立PCEP会话时，如果本端配置的Keepalive消息的发送时间间隔小于对端的**min-keepalive**，则本端会将对端配置的**min-keepalive**作为Keepalive消息的发送时间间隔。

如果本端配置的Keepalive消息的发送时间间隔为0，则对端的**min-keepalive**也需要配置为0，否则会话建立失败。

【举例】

\# 配置Keepalive消息的发送时间间隔为60秒。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce keepalive 60

【相关命令】

·**display mpls te pce peer**

·**pce deadtimer**

**MPLS TE \-- MPLS TE配置命令 \-- pce request-timeout**

------------------------------------------------------------------------

**[pce request-timeout**]命令用来配置发送路径计算请求后等待应答的超时时间。

**[undo pce request-timeout**]命令用来恢复缺省情况。

【命令】

**[pce request-timeout ***value*]

**[undo pce request-timeout**]

【缺省情况】

发送路径计算请求后等待应答的超时时间为10秒。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送路径计算请求后等待应答的超时时间，取值范围为5～100，单位为秒。

【使用指导】

·在EPC方式下，PCC向PCE发送计算请求后，如果在本命令指定的时间内没有收到计算应答，则PCC重新向该PCE发送计算请求。如果仍然没有收到计算应答，则持续本过程直至收到为止。

·在BRPC方式下：

¡对于PCC设备，PCC向PCE发送计算请求后，如果在本命令指定的时间内没有收到计算应答，则PCC认为请求失败，放弃计算请求。

¡对于PCE设备，PCE向它的下游PCE发送计算请求后，如果在本命令指定的时间内没有收到计算应答，则直接向它的上游PCE应答本PCE的计算结果（如果是头节点PCE，则向PCC反馈计算结果），不再等待下游PCE的应答。

【举例】

\# 配置发送路径计算请求后等待应答的超时时间为20秒。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce request-timeout 20

【相关命令】

·**display mpls te pce peer**

**MPLS TE \-- MPLS TE配置命令 \-- pce static**

------------------------------------------------------------------------

**[pce static**]命令用来在PCC或PCE设备上静态指定PCE对等体。

**[undo pce static**]命令用来删除静态指定的PCE对等体。

【命令】

**[pce** **static** *ip-address*]

**[undo pce static ***ip-address*]

【缺省情况】

设备上不存在静态指定的PCE对等体。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：静态指定PCE对等体的IP地址。

【举例】

\# 静态指定IP地址为10.10.10.10的PCE对等体。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce static 10.10.10.10

【相关命令】

·**display mpls te pce discovery**

**MPLS TE \-- MPLS TE配置命令 \-- pce tolerance**

------------------------------------------------------------------------

**[pce tolerance**]命令用来配置本地设备对PCE对等体发送的消息的容忍度。

**[undo pce tolerance**]命令用来恢复缺省情况。

【命令】

**[pce tolerance **[*[ value \| ]***max-unknown-messages*** value* }]

**[undo pce tolerance ****[max-unknown-messages **}]

【缺省情况】]

能接受的对等体发送]Keepalive消息的最小时间间隔为10秒；能接受的对等体每分钟发送未知类型消息的最大个数为5。

【视图】

MPLS TE视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[min-keepalive*** value*]：指定能接受的对等体发送Keepalive消息的最小时间间隔，取值范围为0～255，单位为秒，取值为0表示能接受任意的Keepalive发送时间间隔。

**[max-unknown-messages*** value*]：指定能接受的对等体每分钟发送未知类型消息的最大个数，取值范围为0～16384，取值为0表示不限制对等体每分钟发送未知类型消息的最大个数。

【使用指导】

对等体之间建立PCEP会话时，如果对端配置的Keepalive发送时间间隔小于本地配置的**min-keepalive**的值，则将对端Keepalive消息的发送时间间隔协商为本端配置的**min-keepalive**的值。

如果本地设备一分钟内从对等体接收到的未知消息数目大于或等于本地配置的**max-unknown-messages**，则断开与对等体的PCEP会话。

【举例】

\# 配置能接受的对等体的最小Keepalive消息发送时间间隔为20秒，每分钟发送未知类型消息的最大个数为10。

\<Sysname\> system-view

Sysname mpls te

Sysname-te pce tolerance min-keepalive 20

Sysname-te pce tolerance max-unknown-messages 10

【相关命令】

·**display mpls te pce peer**

·**pce keepalive**

**MPLS TE \-- MPLS TE配置命令 \-- reset mpls te auto-bandwidth-adjustment timers**

------------------------------------------------------------------------

![说明](MPLS%20TE命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset mpls te auto-bandwidth-adjustment timers**]命令用来重启自动带宽调整功能。

【命令】

**[reset** **mpls te auto-bandwidth-adjustment timers**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

执行本命令后，会清除出口速率采样信息，并清除距下一次带宽调整的剩余时间，以便重新进行出口速率采样和带宽调整。

【举例】

\# 重启自动带宽调整功能。

\<Sysname\> reset mpls te auto-bandwidth-adjustment timers

【相关命令】

·**mpls te auto-bandwidth**

·**auto-bandwidth enable**

**MPLS TE \-- MPLS TE配置命令 \-- reset mpls te pce statistics**

------------------------------------------------------------------------

**[reset mpls te pce statistics**]命令用来清除PCC或PCE统计信息。

【命令】

**[reset** **mpls te pce statistics** [ *ip-address* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：清除指定PCC或PCE的统计信息。*ip-address*为PCC或PCE的IP地址。如果不指定本参数，则清除所有PCC或PCE的统计信息。

【举例】

\# 清除IP地址为10.10.10.10的PCE统计信息。

\<Sysname\> reset mpls te pce statistics 10.10.10.10

【相关命令】

·**display mpls te pce statistics**

**MPLS TE \-- MPLS TE配置命令 \-- snmp-agent trap enable te**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable te**]命令用来开启MPLS TE模块的告警功能。

**[undo** **snmp-agent** **trap** **enable te**]命令用来关闭MPLS TE模块的告警功能。

【命令】

**[snmp-agent** **trap** **enable** **te**]

**[undo** **snmp-agent** **trap** **enable** **te**]

【缺省情况】

MPLS TE模块的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启MPLS TE模块的告警功能后，当MPLS TE隧道状态发生变化时会产生RFC 3812中规定的告警信息。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。

有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启MPLS TE模块的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable te

**MPLS TE \-- MPLS TE配置命令 \-- te-subtlv**

------------------------------------------------------------------------

**[te-subtlv**]命令用来配置携带DS-TE参数的各种子TLV的TLV类型值。

**[undo te-subtlv**]命令用来恢复缺省情况。

【命令】

**[te-subtlv**[ { **bw-constraint** *value* \| **unreserved-subpool-bw** *value* } \*]]

**[undo te-subtlv**[ { **bw-constraint** \| **unreserved-subpool-bw** } \*]]

【缺省情况】

带宽约束**bw-constraint**的子TLV类型值为252；子池未预订带宽**unreserved-subpool-bw**的子TLV类型值为251。

【视图】

IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bw-constraint*** value*]：指定带宽约束的子TLV类型值，*value*取值范围为23～254。

**[unreserved-subpool-bw*** value*]：指定子池未预订带宽的子TLV类型值，*value*取值范围为23～254。

【使用指导】

在Prestandard模式下，携带DS-TE参数的子TLV类型值未形成标准，不同厂商可能使用不同的类型值。为了实现不同厂商设备的互通，需要通过本命令手工配置这些子TLV的类型值。

需要注意的是，DS-TE模式为Prestandard时，本命令生效；模式为IETF时，本命令不生效。

【举例】

\# 配置IS-IS进程1携带DS-TE参数的各种子TLV的TLV类型值：

·带宽约束**bw-constraint**的子TLV类型值为200；

·子池未预订带宽**unreserved-subpool-bw**的子TLV类型值为202。

\<Sysname\> system-view

Sysname isis 1

Sysname-isis-1 te-subtlv bw-constraint 200 unreserved-subpool-bw 202

【相关命令】

·**display isis mpls te configured-sub-tlvs**

**MPLS TE \-- MPLS TE配置命令 \-- timers removal unused**

------------------------------------------------------------------------

**[timers removal unused**]命令用来配置空闲Bypass隧道的自动清除时间。

**[undo timers removal unused**]命令用来恢复缺省情况。

【命令】

**[timers removal unused **]*seconds*

**[undo timers removal unused**]

【缺省情况】

空闲Bypass隧道的自动清除时间为3600秒。

【视图】

MPLS TE自动隧道备份视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：空闲Bypass隧道的自动清除时间，取值范围为0、300～604800，单位为秒。取值为0表示禁止清除空闲的Bypass隧道。

【使用指导】

一条自动创建的Bypass隧道可以与多条主隧道绑定。当Bypass隧道没有与任何主隧道绑定时，该Bypass隧道称为空闲Bypass隧道。自动创建的Bypass隧道的空闲时间到达本命令配置的值时，自动清除该隧道，以释放该隧道占用的带宽资源和接口编号。

本命令配置的值如果过大，则会导致Bypass隧道长时间占用带宽资源和接口编号；本命令配置的值如果过小，则可能会导致Bypass隧道频繁建立和拆除。

【举例】

\# 配置空闲Bypass隧道的自动清除时间为100分钟。

\<Sysname\> system-view

Sysname mpls te

Sysname-te auto-tunnel backup

Sysname-te-auto-bk timers removal unused 60000

【相关命令】

·**auto-tunnel backup**

·**tunnel-number**

**MPLS TE \-- MPLS TE配置命令 \-- tunnel-number**

------------------------------------------------------------------------

**[tunnel-number**]命令用来配置自动创建的Bypass隧道的接口编号范围。

**[undo tunnel-number**]命令用来恢复缺省情况。

【命令】

**[tunnel-number min**]* min-number*** max ***max-number*

**[undo tunnel-number**]

【缺省情况】

未指定自动创建Bypass隧道的接口编号范围，不能自动创建Bypass隧道。

【视图】

MPLS TE自动隧道备份视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[min**]*min-number*：指定自动创建Bypass隧道的接口编号的最小值。本参数的取值范围与设备型号有关，请以设备实际情况为准。

**[max ***max-number*]：指定自动创建Bypass隧道的接口编号的最大值。本参数的取值范围与设备型号有关，请以设备实际情况为准。

【使用指导】

通过**auto-tunnel backup**命令全局开启自动隧道备份功能后，还需执行本命令，才能自动建立Bypass隧道；否则，无法自动建立Bypass隧道。自动建立Bypass隧道时，设备按照由小到大的顺序从本命令指定的范围内依次为Bypass隧道选择接口编号。

需要注意的是：

·配置的*min-number*必须小于等于*max-number*。

·配置的接口编号范围不能大于1000，否则命令无法成功执行。

·重复执行本命令，新的配置将覆盖原有配置。

·重复执行本命令修改接口编号范围时，修改后的编号范围需要包含已经自动创建的Bypass隧道的接口编号，否则命令无法成功执行。即：如果在修改编号范围前已经自动创建了Bypass隧道，则*min-number*不能大于这些Bypass隧道中的接口编号的最小值；*max-number*不能小于这些Bypass隧道中的接口编号的最大值。

·通过**interface tunnel**命令手工创建隧道接口时，指定的隧道接口编号可以在本命令配置的范围内，该编号不会再用于自动创建的Bypass隧道；通过**undo interface tunnel**命令删除该隧道接口后，该接口编号仍然可以用于自动创建的Bypass隧道。

【举例】

\# 配置自动创建的Bypass隧道的接口编号范围为800到900。

\<Sysname\> system-view

Sysname mpls te

Sysname-te auto-tunnel backup

Sysname-te-auto-bk tunnel-number min 800 max 900

【相关命令】

·**auto-tunnel backup**
