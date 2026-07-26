
**EVI \-- EVI配置命令 \-- display evi arp-suppression**

------------------------------------------------------------------------

**[display evi arp-suppression**]命令用来显示EVI ARP泛洪抑制表项。

【命令】

集中式设备：

**[display evi arp-suppression interface tunnel*** interface-number* [ **vlan** *vlan-id*   **count** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display evi arp-suppression interface tunnel*** interface-number* [ **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

分布式设备－IRF模式：

**[display evi arp-suppression interface tunnel*** interface-number* [ **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口下的EVI ARP泛洪抑制表项。

**[vlan ***vlan-id*]：显示指定VLAN的EVI ARP泛洪抑制表项。*vlan-id*表示VLAN编号，取值范围为1～4094。如果不指定本参数，将显示所有VLAN的EVI ARP泛洪抑制表项。

**[slot** *slot-number*]：显示指定单板的EVI ARP泛洪抑制表项。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的EVI ARP泛洪抑制表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的EVI ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示Master设备上的EVI ARP泛洪抑制表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的EVI ARP泛洪抑制表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示Master设备上的EVI ARP泛洪抑制表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的EVI ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的EVI ARP泛洪抑制表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的EVI ARP泛洪抑制表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的EVI ARP泛洪抑制表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的EVI ARP泛洪抑制表项。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示EVI ARP泛洪抑制表项的数目。

【举例】

\# 显示EVI隧道接口Tunnel101下的EVI ARP泛洪抑制表项。

\<Sysname\> display evi arp-suppression interface tunnel 101

IP Address      MAC Address    VLAN ID  Interface                Aging Status

1.1.1.2         000f-e201-0101 1        EVI-link1                14    Valid

1.1.1.3         000f-e201-0202 1        EVI-link1                18    Invalid

1.1.1.4         000f-e201-0203 1        EVI-link1                10    Collision

\# 显示EVI隧道接口Tunnel101下的EVI ARP泛洪抑制表项的数目。

\<Sysname\> display evi arp-suppression interface tunnel 101 count

Total entries: 3

表1-1 display evi arp-suppression命令显示信息描述表

字段

描述

IP Address

EVI ARP泛洪抑制表项的IP地址

MAC Address

EVI ARP泛洪抑制表项的MAC地址

VLAN ID

EVI ARP泛洪抑制表项所属的激活VLAN

Interface

EVI ARP泛洪抑制表项对应的入接口，也就是学习到EVI ARP泛洪抑制表项的接口

Aging

EVI ARP泛洪抑制表项的老化时间，单位为分钟

Status

EVI ARP泛洪抑制表项的表项状态：

·Valid：有效。表项建立的初始状态为有效，有效时可以根据该表项进行代答

·Invalid：无效。表项自最后一次更新后15分钟内没有收到ARP更新报文，变为无效状态，此时不能根据该表项代答。无效状态能保持10分钟，10分钟内无更新报文，则删除该表项

·Collision：冲突。如果收到ARP报文时发现相同IP地址的泛洪抑制表项已经存在，但是MAC地址发生变化，则认为发生攻击，此时泛洪抑制表项处于冲突状态，不能根据该表项代答，并在25分钟后删除此表项

Total entries

EVI ARP泛洪抑制表项的数目

【相关命令】

·**evi arp-suppression enable**

·**reset evi arp-suppression**

**EVI \-- EVI配置命令 \-- display evi isis brief**

------------------------------------------------------------------------

**[display evi isis brief**]命令用来显示EVI IS-IS进程的摘要信息。

【命令】

**[display evi isis brief** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定EVI IS-IS进程的摘要信息。*process-id*表示EVI IS-IS进程号，取值范围为0～65535。如果不指定本参数，将显示所有EVI IS-IS进程的摘要信息。

【举例】

\# 显示EVI IS-IS进程的摘要信息。

\<Sysname\> display evi isis brief

Site ID: 10

Isolation Count: 0

Process ID: 0

Network-entity: 00.0011.2200.0001.00

LSP-length receive: 16384

LSP-length originate: 1400

Timers:

  LSP-max-age: 1200s

  LSP-refresh: 900s

表1-2 display evi isis brief显示信息描述表

字段

描述

Site ID

本地站点ID

Isolation Count

本设备被多少其他站点所隔离。若该数目不为0，则表示本地站点ID仍与其他站点ID有冲突且本设备被隔离，则本设备不对外发布Hello报文；若该数目为0，则表示本设备未被隔离，此时对外发布Hello报文

Process ID

进程实例号

Network-entity

网络实体名称

LSP-length receive

可以接收LSP的最大长度

LSP-length originate

生成的LSP的最大长度

Timers

LSP-max-age

LSP的最大生存时间

LSP-refresh

LSP的刷新周期

**EVI \-- EVI配置命令 \-- display evi isis graceful-restart status**

------------------------------------------------------------------------

**[display evi isis graceful-restart status**]命令用来显示EVI IS-IS协议的GR状态。

【命令】

**[display evi isis graceful-restart status** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定EVI IS-IS进程的GR状态。*process-id*表示EVI IS-IS进程号，取值范围为0～65535。如果不指定本参数，将显示所有EVI IS-IS进程的GR状态。

【举例】

\# 显示EVI IS-IS协议的GR状态。

\<Sysname\> display evi isis graceful-restart status

Process ID: 0

Restart status: RESTARTING

Restart phase: LSDB synchronization

Restart interval: 300s

T3 remaining time: 65531s

Total number of interfaces: 1

Number of waiting LSPs: 0

T2 remaining time: 56s

  Interface: EVI-Link0

    T1 remaining time: 2

    RA received: N

    CSNP received: N

    T1 expired number: 3

表1-3 display evi isis graceful-restart status显示信息描述表

字段

描述

Process ID

进程实例号

Restart status

重启状态：

·COMPLETE：重启完成

·STARTING：重启开始

·RESTARTING：重启中

·UNKNOWN：未知状态

Restart phase

重启阶段：

·Initialization：初始阶段

·LSDB synchronization：LSDB同步阶段

·MAC receiving：接收本地MAC地址上报的阶段

·LSP stable：LSP生成的阶段

·LSP generation：LSP刷新和泛洪的阶段

·Finish：GR完成的阶段

·Unknown：未知阶段

Restart interval

重启间隔

T3 remaining time

定时器T3的剩余时间

Total number of interfaces

进程实例下的所有接口数

Number of waiting LSPs

等待的LSP报文数

T2 remaining time

定时器T2的剩余时间

Interface

接口名

T1 remaining time

定时器T1的剩余时间

RA received

RA接收标记位

CSNP received

CSNP接收标记位

T1 expired number

定时器T1的超时次数

**EVI \-- EVI配置命令 \-- display evi isis local-mac**

------------------------------------------------------------------------

**[display evi isis local-mac**]命令用来显示EVI IS-IS的本地MAC地址信息。

【命令】

**[display evi isis local-mac**[ { **dynamic** \| **static** } [ **interface** **tunnel** *interface-number* [ **vlan** *vlan-id*   **filtered** \| **passed** ]  **count**  ]]]

**[display evi isis local-mac** **nonadvertised** [ **interface** **tunnel** *interface-number* [ **vlan** *vlan-id*   **count**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[dynamic**]：显示本地动态MAC地址信息。

**[nonadvertised**]：显示本地非发布MAC地址信息。非发布MAC地址包括：泛洪MAC地址、黑洞MAC地址、多端口单播MAC地址、组播MAC地址。

**[static**]：显示本地静态MAC地址信息。

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口下的本地MAC地址信息。如果不指定本参数，将显示所有EVI隧道接口下的EVI IS-IS的本地MAC地址信息。

**[vlan ***vlan-id*]：显示指定VLAN的本地MAC地址信息。*vlan-id*表示VLAN编号，取值范围为1～4094。如果不指定本参数，将显示所有VLAN的本地MAC地址信息。

**[filtered**]：只显示本地存在，但是被路由策略过滤掉、不能发布的本地MAC地址信息。

**[passed**]：只显示没有被路由策略过滤掉、允许发布的本地MAC地址信息。

**[count**]：显示本地MAC地址的数目。

【举例】

\# 显示所有EVI隧道接口下的EVI IS-IS的本地动态MAC地址信息。

\<Sysname\> display evi isis local-mac dynamic

Process ID: 0

Tunnel interface: Tunnel0

  VLAN ID: 100

    MAC address: 00aa-00bb-00cc

    MAC address: 00aa-00cc-00bb (Filtered)

    MAC address: 00cc-00aa-00bb

  VLAN ID: 50

    MAC address: 00bb-00aa-00cc

    MAC address: 00bb-00cc-00aa

\# 显示EVI隧道接口Tunnel0下允许发布的EVI IS-IS的本地动态MAC地址信息。

\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 passed

Process ID: 0

Tunnel interface: Tunnel0

  VLAN ID: 100

    MAC address: 00aa-00bb-00cc

    MAC address: 00cc-00aa-00bb

  VLAN ID: 50

    MAC address: 00bb-00aa-00cc

    MAC address: 00bb-00cc-00aa

\# 显示所有EVI隧道接口下的EVI IS-IS的本地非发布MAC地址信息。

\<Sysname\> display evi isis local-mac nonadvertised

MAC Flags: F-Flooding, B-Blackhole, P-Multiport, M-Multicast

Process ID: 3

  Tunnel interface: Tunnel3

  VLAN ID: 111

    MAC address: 0005-0005-0005

          Flags: F

\# 显示所有EVI隧道接口下的EVI IS-IS的本地静态MAC地址信息。

\<Sysname\> display evi isis local-mac static

Process ID: 0

Tunnel interface: Tunnel0

  VLAN ID: 100

    MAC address: 00aa-00bb-00cc

    MAC address: 00aa-00cc-00bb (Filtered)

    MAC address: 00cc-00aa-00bb

  VLAN ID: 50

    MAC address: 00bb-00aa-00cc

    MAC address: 00bb-00cc-00aa

\# 显示EVI隧道接口Tunnel0下被路由策略过滤不允许发布的EVI IS-IS的本地静态MAC地址信息。

\<Sysname\> display evi isis local-mac static interface tunnel 0 filtered

Process ID: 0

Tunnel interface: Tunnel0

  VLAN ID: 100

    MAC address: 00aa-00cc-00bb (Filtered)

  VLAN ID: 50

\# 显示EVI隧道接口Tunnel0下的本地动态MAC地址的数目。

\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 count

5 MAC addresses found.

\# 显示EVI隧道接口Tunnel0下允许发布的本地动态MAC地址的数目。

\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 passed count

4 MAC addresses found.

\# 显示EVI隧道接口Tunnel0下被路由策略过滤不允许发布的本地静态MAC地址的数目。

\<Sysname\> display evi isis local-mac static interface tunnel 0 filtered count

1 MAC addresses found.

表1-4 display evi isis local-mac显示信息描述表

字段

描述

Process ID

进程实例号

Tunnel interface

进程实例对应的Tunnel接口

VLAN ID

进程实例下的VLAN

MAC address

MAC地址

(Filtered)

被路由策略过滤掉、不能发布的MAC地址

Flags

EVI IS-IS本地非发布MAC地址标记：

·F-Flooding：泛洪MAC地址（即通过**evi selective-flooding mac-address**命令配置的选择性泛洪的MAC地址）

·B-Blackhole：黑洞MAC地址

·P-Multiport：多端口单播MAC地址

·M-Multicast：组播MAC地址

5 MAC addresses found

本地MAC地址的数目，本例中本地MAC地址的数目为5

**EVI \-- EVI配置命令 \-- display evi isis lsdb**

------------------------------------------------------------------------

**[display evi isis lsdb**]命令用来显示EVI IS-IS的链路状态数据库。

【命令】

**[display evi isis lsdb**[ [ **local** \| **lsp-id** *lspid* \| **verbose** ] \*  *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[local**]：显示当前设备产生的LSP的信息。

**[lsp-id** *lspid*]：LSP标识，形式为SYSID*.*Pseudonode ID-fragment num，其中，SYSID是产生该LSP的结点或伪结点的SystemID，fragment num是该LSP的分片号。

**[verbose**]：显示链路状态数据库中的LSP的详细信息。如果不指定本参数，将显示链路状态数据库中的LSP的摘要信息。

*[process-id*]：显示指定EVI IS-IS进程的链路状态信息。*process-id*表示EVI IS-IS进程号，取值范围为0～65535。如果不指定本参数，将显示所有EVI IS-IS进程的链路状态信息。

【举例】

\# 显示链路状态数据库的摘要信息。

\<Sysname\> display evi isis lsdb

               Link state database information for EVI-ISIS(0)

LSP ID                 Seq num     Checksum  Holdtime  Length    Overload

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0011.2200.0001.00-00\*  0x000000f3  0xd95e    45        47        0

0011.2200.0101.00-00   0x00000017  0xbb6f    1139      85        0

0011.2200.0101.02-00   0x00000002  0x7973    805       54        0

Flags: \*-Self LSP, +-Self LSP(Extended)

\# 显示链路状态数据库的详细信息。

\<Sysname\> display evi isis lsdb verbose

                Link state database information for EVI-ISIS(1)

LSP ID: 3822.d69e.ee00.00-00\*

Sequence number: 0x00000001

Checksum: 0xe0b5

Holdtime: 820s

Length: 47

Overload: 0

Source: 3822.d69e.ee00.00

Neighbour

    ID: 3ce5.a600.7600.02, Cost: 16777214

LSP ID: 3ce5.a600.7600.00-00

Sequence number: 0x00000007

Checksum: 0xc98a

Holdtime: 1163s

Length: 72

Overload: 0

Source: 3ce5.a600.7600.00

Neighbour

    ID: 3ce5.a600.7600.02, Cost: 16777214

MAC addresses:

  VLAN ID: 1   Confidence: 1

    3822-d69e-ef68

    d485-64aa-7f23

    3408-0499-b44c

LSP ID: 3ce5.a600.7600.02-00

Sequence number: 0x00000001

Checksum: 0xe16d

Holdtime: 819s

Length: 54

Overload: 0

Source: 3ce5.a600.7600.02

Neighbour

    ID: 3822.d69e.ee00.00, Cost: 0

    ID: 3ce5.a600.7600.00, Cost: 0

Flags: \*-Self LSP, +-Self LSP(Extended)

表1-5 display evi isis lsdb命令显示信息描述表

字段

描述

Link state database information for EVI-ISIS(0)

EVI IS-IS进程0的链路状态数据库信息

LSP ID

链路状态报文ID

Seqence number

LSP序列号

Checksum

LSP校验和

Holdtime

LSP生存时间，随着时间推移递减

Length

LSP长度

Overload

LSP中Overload bit的置位情况。1表示置位，0表示没有置位

Source

LSP生成路由器的System ID

Neighbour ID

LSP生成路由器邻居的System ID

Cost

开销值

MAC address

LSP生成路由器的MAC地址信息

VLAN ID

LSP生成路由器的MAC地址所在的VLAN ID

Confidence

可信度

Flags: \*-Self LSP, +-Self LSP(Extended)

带\*号表示是本地生成的、原始系统LSP

带+号表示是本地生成的、虚拟系统LSP（LSP扩展分片）

**EVI \-- EVI配置命令 \-- display evi isis peer**

------------------------------------------------------------------------

**[display evi isis peer**]命令用来显示EVI IS-IS的邻居信息。

【命令】

**[display** **evi isis** **peer** [ *process-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定的EVI IS-IS进程下的邻居信息。*process-id*表示EVI IS-IS进程号，取值范围为0～65535。如果不指定本参数，将显示所有EVI IS-IS进程的邻居信息。

【举例】

\# 显示EVI IS-IS进程0的邻居信息。（此例为无冲突的站点内邻居）

\<Sysname\> display evi isis peer 0

Process ID: 0

System ID: 0011.2200.0101

Link interface: Tunnel0

Circuit ID: 0011.2200.0301.01

State: Up

Site ID: 1

Hold time: 29s

Neighbour DED priority: 64

Uptime: 00:10:56

Process ID: 0

System ID: 0011.2200.0101

Link interface: EVI-Link0

Circuit ID: \-\--

State: Init

Site ID: 1

Hold time: 29s

Neighbour DED priority: 64

Uptime: 00:00:58

\# 显示EVI IS-IS进程0的邻居信息（此例为有冲突的站点间邻居）。

\<Sysname\> display evi isis peer 0

Process ID: 0

System ID: 0011.2200.0301

Link interface: EVI-Link0

Circuit ID: \-\--

State: Init

Site ID: 1 (Conflict)

Hold time: 27s

Neighbor DED priority: 64

Uptime: 00:00:00

表1-6 display evi isis peer命令显示信息描述表

字段

描述

Process ID

进程实例号

System ID

邻居的系统ID

Link interface

·Tunnel：与对端相连的本地Tunnel接口

·EVI-link：与对端相连的本地EVI-Link接口

Circuit ID

链路ID

State

邻居状态：

·Init：邻居初始化

·Up：邻接关系建立

·Down：邻接关系断开

Site ID

邻居的站点ID。括号中的Conflict表示邻居的站点ID与本地站点ID有冲突。当站点间邻居的站点ID与本地站点ID一致、或者站点内邻居的站点ID与本地站点ID不一致，则认为邻居的站点ID与本地站点ID有冲突

Hold time

存活时间，随着时间推移递减，如果在存活时间内还没有收到邻居发送的Hello报文，则认为邻居已经失效，如果收到了Hello报文，则存活时间将重置为初始值

Neighbour DED Priority

邻居接口DED优先级

Uptime

邻居关系保持的时间

**EVI \-- EVI配置命令 \-- display evi isis remote-mac**

------------------------------------------------------------------------

**[display evi isis remote-mac**]命令用来显示EVI IS-IS的远端MAC地址信息。

【命令】

**[display** **evi isis** **remote-mac** [ **interface** **tunnel** *interface-number* [ **vlan** *vlan-id*   **count**  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口下的远端MAC地址信息。如果不指定本参数，将显示所有EVI隧道接口下的EVI IS-IS的远端MAC地址信息。

**[vlan ***vlan-id*]：显示指定VLAN的远端MAC地址信息。*vlan-id*表示VLAN编号，取值范围为1～4094。如果不指定本参数，将显示所有VLAN的远端MAC地址信息。

**[count**]：显示远端MAC地址的数目。

【举例】

\# 显示所有EVI隧道接口下的EVI IS-IS的远端MAC地址信息。

\<Sysname\> display evi isis remote-mac

Process ID: 0

  Tunnel interface: Tunnel0

  VLAN ID: 3

    MAC address: 0033-0011-0022

      Interface:  EVI-Link0

          Flags:  0x2

  VLAN ID: 2

    MAC address: 0022-0033-0011

      Interface:  EVI-Link0

    MAC address: 0033-0022-0011

      Interface:  EVI-Link0

          Flags:  0x2

\# 显示EVI隧道接口Tunnel0下的远端MAC地址的数目。

\<Sysname\> display evi isis remote-mac interface tunnel 0 count

3 mac address(es) found.

表1-7 display evi isis remote-mac显示信息描述表

字段

描述

Process ID

进程实例号

Tunnel interface

进程实例对应的Tunnel接口

VLAN ID

进程实例下的VLAN

MAC address

MAC地址

Interface

EVI链路索引

Flags

EVI IS-IS远端MAC地址标记：

·0x1：该MAC地址与EVI IS-IS本地动态MAC地址冲突

·0x2：该MAC地址已经下发到远端MAC地址表

·0x4：该MAC地址与EVI IS-IS本地的静态或泛洪MAC地址冲突

3 mac address(es) found

远端MAC地址的数目，本例中远端MAC地址的数目为3

**EVI \-- EVI配置命令 \-- display evi isis tunnel**

------------------------------------------------------------------------

**[display evi isis tunnel**]命令用来显示Tunnel接口的EVI IS-IS信息。

【命令】

**[display evi isis tunnel** [ *tunnel-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[tunnel-number*]：显示指定Tunnel接口的EVI IS-IS信息。如果不指定本参数，将显示所有Tunnel接口上的EVI IS-IS信息。

【举例】

\# 显示Tunnel接口101上的EVI IS-IS信息。

\<Sysname\> display evi isis tunnel 101

Tunnel101

MTU: 1400

DED: Yes

DED priority: 80

Hello timer: 10s

Hello multiplier: 3

CSNP timer: 10s

LSP timer: 100ms

LSP transmit-throttle count: 5

AEF: Yes

EVI-Link0    DED: Yes

LAV:

  1,50,100

表1-8 display evi isis tunnel显示信息描述表

字段

描述

Tunnel

EVI隧道接口编号

MTU

链路MTU值

DED

是否被选举为DED：Yes表示是；No表示否

DED priority

DED优先级

Hello timer

Hello报文发送时间间隔

Hello multiplier

Hello报文失效数目

CSNP timer

CSNP报文发送时间间隔

LSP timer

LSP的最小发送时间间隔

LSP transmit-throttle count

LSP的最大传输数量

AEF

本设备是否可以作为扩展VLAN的授权转发设备。如果双归属站点内某设备核心侧故障，其该属性显示为No，表示本设备不能作为任何VLAN的授权转发设备；如果某设备核心侧正常，其该属性显示为Yes，表示本设备可以作为扩展VLAN的授权转发设备

EVI-link

EVI虚拟链接

LAV

Tunnel接口下的激活VLAN

**EVI \-- EVI配置命令 \-- display evi link**

------------------------------------------------------------------------

**[display evi link**]命令用来显示指定EVI隧道创建的EVI-Link接口信息。

【命令】

**[display evi link interface tunnel*** interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口下的EVI-Link接口信息。

【举例】

\# 显示EVI隧道接口Tunnel0创建的EVI-Link接口信息。

\<Sysname\> display evi link interface tunnel 0

Interface     Status Source          Destination

EVI-Link0     UP     1.1.1.1         1.1.2.1

EVI-Link1     UP     1.1.1.1         1.1.3.1

表1-9 display evi link命令显示信息描述表

字段

描述

Interface

EVI-Link接口名

Status

EVI-Link接口的链路UP/DOWN状态

Source

EVI-Link接口的EVI隧道本端地址

Destination

EVI-Link接口的EVI隧道对端地址

**EVI \-- EVI配置命令 \-- display evi mac-address**

------------------------------------------------------------------------

**[display evi mac-address**]命令用来显示远端MAC地址信息。

【命令】

集中式设备：

**[display evi mac-address interface tunnel*** interface-number* [ **vlan** *vlan-id*   **count** ]]

**[display evi mac-address interface tunnel*** interface-number* **mac-address** *mac-address* **vlan** *vlan-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display evi mac-address interface tunnel*** interface-number* [ **vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display evi mac-address interface tunnel*** interface-number* **mac-address** *mac-address* **vlan** *vlan-id* [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display evi mac-address interface tunnel*** interface-number* [ **vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **count** ]]

**[display evi mac-address interface tunnel*** interface-number* **mac-address** *mac-address* **vlan** *vlan-id* [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口下的远端MAC地址信息。

**[mac-address ***mac-address*]：显示指定MAC地址的远端MAC地址信息。如果不指定本参数，将显示所有MAC地址的远端MAC地址信息。

**[vlan ***vlan-id*]：显示指定VLAN的远端MAC地址信息。*vlan-id*表示VLAN编号，取值范围为1～4094。如果不指定本参数，将显示所有VLAN的远端MAC地址信息。

**[slot** *slot-number*]：显示指定单板的远端MAC地址信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的远端MAC地址信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的远端MAC地址信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示Master设备上的远端MAC地址信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的远端MAC地址信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示Master设备上的远端MAC地址信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的远端MAC地址信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端MAC地址信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的远端MAC地址信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端MAC地址信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的远端MAC地址信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示远端MAC地址信息的数目。

【举例】

\# 显示EVI隧道接口Tunnel101下的远端MAC地址信息。

\<Sysname\> display evi mac-address interface tunnel 101

MAC Address      VLAN ID   Port

000f-e201-0101   1         EVI-link1

000f-e202-0101   2         EVI-link1, EVI-link2

\# 显示EVI隧道接口Tunnel101下的远端MAC地址信息的数目。

\<Sysname\> display evi mac-address interface tunnel 101 count

Total entries: 2

表1-10 display evi mac-address命令显示信息描述表

字段

描述

MAC Address

远端MAC地址

VLAN ID

远端MAC地址所属VLAN

Port

远端MAC地址对应的出端口（N/A表示出端口无效，已被删除）

Total entries

远端MAC地址信息的数目

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client member**

------------------------------------------------------------------------

**[display evi neighbor-discovery client member**]命令用来在ENDC上显示ENDC学到的邻居信息。

【命令】

**[display evi neighbor-discovery** [ **ipv6**  **client** **member** [ **interface tunnel** *interface-number* \| **local** *local-ip* ]]｜ **remote ***client-ip*[ \| **server** *server-ip* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：显示ENDC学到的IPv6邻居信息。不指定本参数，则显示ENDC学到的IPv4邻居信息。

**[interface tunnel*** interface-number*]：显示通过指定EVI隧道接口学到的邻居信息。

**[local ***local-ip*]：显示通过指定IPv4地址/IPv6地址对应的EVI隧道接口学到的邻居信息。*local-ip*表示本地ENDC的IPv4地址/IPv6地址。

**[remote ***client-ip*]：显示设备学到的指定邻居ENDC的信息。*client-ip*表示邻居ENDC的IPv4地址/IPv6地址。

**[server ***server-ip*]：显示通过指定ENDS学到的邻居信息。*server-ip*表示ENDS的IPv4地址/IPv6地址。

【使用指导】

通过本命令可以查看ENDC学到的邻居信息，包括邻居的IPv4地址/IPv6地址、桥MAC地址、创建时间、老化时间、邻居之间的EVI Link状态等信息。

如果不指定任何参数，将显示设备上本地ENDC学到的所有邻居信息。

【举例】

\# 显示设备上ENDC学到的所有IPv4邻居信息。

\<Sysname\> display evi neighbor-discovery client member

Interface: Tunnel0    Network ID: 1

Local Address: 20.0.0.2

Server Address: 20.0.1.1

Neighbor        System ID         Created Time           Expire    Status

20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    13        Up

20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    12        Up

Interface: Tunnel0    Network ID: 1

Local Address: 20.0.0.2

Server Address: 20.0.1.2

Neighbor        System ID         Created Time           Expire    Status

20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up

20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Up

Interface: Tunnel1    Network ID: 2

Local Address: 21.0.0.1

Server Address: 21.0.1.2

Neighbor        System ID         Created Time           Expire    Status

21.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up

21.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Down

Interface: Tunnel2    Network ID: 3

Local Address: 21.0.0.2

Server Address: NA

Neighbor        System ID         Created Time           Expire    Status

21.0.2.1        NA                2011/01/01 12:12:12    25        Up

21.0.3.1        NA                2011/01/01 12:12:12    19        Up

\# 显示设备上ENDC学到的所有IPv6邻居信息。

\<Sysname\> display evi neighbor-discovery ipv6 client member

Interface: Tunnel0    Network ID: 1                                   

Local Address: 2000::2                                                

Server Address: 2000::1:1                                             

Neighbor        System ID         Created Time           Expire    Status

2000::2:1       000F-0000-0A3E    2011/01/01 12:12:12    13        Up 

2000::3:1       000F-0000-0A3F    2011/01/01 12:12:12    12        Up 

Interface: Tunnel0    Network ID: 1                                   

Local Address: 2000::2                                                

Server Address: 2000::1:2                                             

Neighbor        System ID         Created Time           Expire    Status

2000::2:1       000F-0000-0A3E    2011/01/01 12:12:12    25        Up 

2000::3:1       000F-0000-0A3F    2011/01/01 12:12:12    19        Up 

Interface: Tunnel1    Network ID: 2                                   

Local Address: 2001::1                                                

Server Address: 2001::1:1                                             

Neighbor        System ID         Created Time           Expire    Status

2001::2:1       000F-0000-0A3E    2011/01/01 12:12:12    25        Up 

2001::3:1       000F-0000-0A3F    2011/01/01 12:12:12    19        Down

Interface: Tunnel1    Network ID: 2                                   

Local Address: 2002::2                                                

Server Address: NA                                                    

Neighbor        System ID         Created Time           Expire    Status

2002::1         NA                2011/01/01 12:12:12    25        Up 

2002::3:1       NA                2011/01/01 12:12:12    19        Up 

表1-11 display evi neighbor-discovery client member命令显示信息描述表

字段

描述

Interface

启动ENDC功能的接口名称

Network ID

配置的Network ID

Local Address

EVI隧道接口的源端地址

Server Address

ENDS的IPv4地址/IPv6地址，NA表示ENDS未知

Neighbor

通过ENDS学到的邻居IPv4地址/IPv6地址

System ID

邻居的桥MAC地址，NA表示桥MAC地址未知

Created Time

邻居创建的时间

Expire

邻居的老化时间，单位为秒

Status

与邻居之间EVI Link的状态：

·Up：表示可以通过EVI Link进行传输

·Down：表示不可以通过EVI Link进行传输

·NA：表示尚未创建EVI Link

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client statistics**

------------------------------------------------------------------------

**[display evi neighbor-discovery client statistics**]命令用来在ENDC上显示ENDC的统计信息。

【命令】

**[display evi neighbor-discovery client statistics interface tunnel*** interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口对应的ENDC的统计信息。

【使用指导】

通过本命令可以查看使能ENDC功能后，接口收到和发送ENDP报文的统计信息。

【举例】

\# 显示IPv4 EVI隧道接口Tunnel0对应的ENDC的统计信息。

\<Sysname\> display evi neighbor-discovery client statistics interface tunnel 0

Server Address: 10.0.0.1

Received packets:

  Reply:        170              Error:      1

Sent packets:

  Register:     170              Purge:      0

Server Address: 10.0.0.2

Received packets:

  Reply:        99               Error:      1

Sent packets:

  Register:     100              Purge:      0

\# 显示IPv6 EVI隧道接口Tunnel1对应的ENDC的统计信息。

\<Sysname\> display evi neighbor-discovery client statistics interface tunnel 1

Server Address: 2000::1:1

Received packets:

  Reply:        170              Error:      1

Sent packets:

  Register:     170              Purge:      13

Server Address: 2000::1:2

Received packets:

  Reply:        99               Error:      1

Sent packets:

  Register:     100              Purge:      0

表1-12 display evi neighbor-discovery client statistics命令显示信息描述表

字段

描述

Server Address

ENDC对应的ENDS的IP地址

Received packets

ENDC收到的报文统计信息：

·Reply：表示注册应答报文

·Error：表示错误指示报文

Sent packets

ENDC发送的报文统计信息：

·Register：表示注册报文

·Purge：表示注销报文

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client summary**

------------------------------------------------------------------------

**[display evi neighbor-discovery client summary**]命令用来在ENDC上显示ENDC的运行信息。

【命令】

**[display evi neighbor-discovery** [ **ipv6**  **client summary**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：显示IPv6 ENDC的运行信息。不指定本参数，则显示IPv4 ENDC的运行信息。

【使用指导】

通过本命令可以查看ENDC的运行信息，包括ENDC的配置信息、ENDC与ENDS的连接状态。

【举例】

\# 显示IPv4 ENDC的运行信息。

\<Sysname\> display evi neighbor-discovery client summary

                         Status: I-Init  E-Establish  P-Probe

Interface    Local Address   Server Address  Network ID  Reg  Auth      Status

Tunnel0      20.0.0.2        20.0.0.1        1           15   enabled   E     

Tunnel0      20.0.0.2        20.0.0.3        1           15   enabled   P     

Tunnel1      21.0.0.2        21.0.0.1        2           15   disabled  P  

\# 显示IPv6 ENDC的运行信息。

\<Sysname\> display evi neighbor-discovery ipv6 client summary

                         Status: I-Init  E-Establish  P-Probe

Interface    Local Address   Server Address  Network ID  Reg  Auth      Status

Tunnel0      2000::1:1       2000::2:1       1           15   enabled   E    

Tunnel0      2000::1:1       2000::3:1       1           15   enabled   P    

Tunnel1      2001::1:2       2001::1:1       2           15   disabled  P      

表1-13 display evi neighbor-discovery client summary命令显示信息描述表

字段

描述

Interface

启动ENDC功能的接口名称

Local Address

本地EVI隧道接口的源端地址，NA表示未配置

Server Address

配置的远端ENDS的IPv4地址/IPv6地址

Network ID

配置的Network ID，NA表示未配置

Reg

注册时间间隔

Auth

是否使能认证功能：

·enabled：表示已使能

·disabled：表示未使能

Status

ENDC与ENDS的连接状态：

·I：表示初始状态

·E：表示已建立连接

·P：表示未建立连接正在探测

【相关命令】

·**evi neighbor-discovery authentication**

·**evi neighbor-discovery client enable**

·**evi neighbor-discovery client register-interval**

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server member**

------------------------------------------------------------------------

**[display evi neighbor-discovery server member**]命令用来在ENDS上显示ENDS学到的成员信息。

【命令】

**[display evi neighbor-discovery **[ **ipv6**  **server member** [ **interface tunnel** *interface-number* \| **local** *local-ip* \| **remote** *client-ip* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：显示ENDS学到的IPv6成员信息。不指定本参数，则显示ENDS学到的IPv4成员信息。

**[interface tunnel*** interface-number*]：显示通过指定EVI隧道接口学到的成员信息。

**[local ***local-ip*]：显示通过指定ENDS学到的成员信息。*local-ip*表示本地ENDS的IPv4地址/IPv6地址。

**[remote ***client-ip*]：显示ENDS学到的指定IPv4地址/IPv6地址的成员信息。*client-ip*表示ENDC的IPv4地址/IPv6地址。

【使用指导】

通过本命令可以查看ENDS学到的成员信息，包括成员的IPv4地址/IPv6地址、桥MAC地址、创建时间、老化时间等信息。

如果不指定任何参数，将显示设备上ENDS学到的所有成员信息。

【举例】

\# 显示设备上ENDS学到的所有IPv4成员信息。

\<Sysname\> display evi neighbor-discovery server member

Interface: Tunnel0    Network ID: 1

IP Address: 11.0.0.1

Client Address  System ID         Expire    Created Time    

11.0.0.3        000F-0001-0001    25        2011/01/01 00:00:43

11.0.0.4        000F-0001-0002    15        2011/01/01 01:00:46

11.0.0.5        000F-0001-0003    20        2011/01/01 01:02:13

Interface: Tunnel1    Network ID: 2

IP Address: 11.0.1.2

Client Address  System ID         Expire    Created Time      

11.0.1.3        000F-0001-0011    19        2011/01/01 00:19:31

11.0.1.4        000F-0001-0012    30        2011/01/01 02:00:43

11.0.1.5        000F-0001-0013    20        2011/01/01 01:02:13

Interface: Tunnel2    Network ID: 3

IP Address: 12.0.0.1

Client Address  System ID         Expire    Created Time 

12.0.0.2        000F-0002-0001    30        2011/01/01 03:20:43

12.0.0.3        000F-0002-0002    37        2011/01/01 03:27:46

\# 显示设备上ENDS学到的所有IPv6成员信息。

\<Sysname\> display evi neighbor-discovery ipv6 server member

Interface: Tunnel0    Network ID: 1

IP Address: 2000::1

Client Address  System ID         Expire    Created Time    

2000::3         000F-0001-0001    25        2011/01/01 00:00:43

2000::4         000F-0001-0002    15        2011/01/01 01:00:46

2000::5         000F-0001-0003    20        2011/01/01 01:02:13

Interface: Tunnel1    Network ID: 2

IP Address: 2000::2

Client Address  System ID         Expire    Created Time        

2000::3         000F-0001-0001    19        2011/01/01 00:19:31

2000::4         000F-0001-0002    30        2011/01/01 02:00:43

2000::5         000F-0001-0003    20        2011/01/01 01:02:13

Interface: Tunnel2    Network ID: 3

IP Address: 3000::1

Client Address  System ID         Expire    Created Time      

3000::2         000F-0002-0001    30        2011/01/01 03:20:43

3000::3         000F-0002-0002    37        2011/01/01 03:27:46

表1-14 display evi neighbor-discovery server member命令显示信息描述表

字段

描述

Interface

启动ENDS功能的接口名称

Network ID

配置的Network ID

IP Address

ENDS的IPv4地址/IPv6地址

Client Address

学到的成员的IPv4地址/IPv6地址

System ID

学到的成员的桥MAC地址

Expire

成员的剩余老化时间

Created Time

成员的创建时间

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server statistics**

------------------------------------------------------------------------

**[display evi neighbor-discovery server statistics**]命令用来在ENDS上显示ENDS的统计信息。

【命令】

**[display evi neighbor-discovery server statistics interface tunnel*** interface-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface tunnel*** interface-number*]：显示指定EVI隧道接口对应的ENDS的统计信息。

【使用指导】

通过本命令可以查看使能ENDS功能后，接口收到和发送报文的统计信息。

【举例】

\# 显示IPv4 EVI隧道接口Tunnel0对应的ENDS的统计信息。

\<Sysname\> display evi neighbor-discovery server statistics interface tunnel 0

Received packets:

  Register:     170              Purge:      13  

Sent packets:

  Reply:        170              Error:      1   

\# 显示IPv6 EVI隧道接口Tunnel1对应的ENDS的统计信息。

\<Sysname\> display evi neighbor-discovery server statistics interface tunnel 1

Received packets:

  Register:     170              Purge:      13  

Sent packets:

  Reply:        170              Error:      1   

表1-15 display evi neighbor-discovery server statistics命令显示信息描述表

字段

描述

Received packets

ENDS收到的报文统计信息：

·Register：表示注册报文

·Purge：表示注销报文

Sent packets

ENDS发送的报文统计信息：

·Reply：表示注册应答报文

·Error：表示错误指示报文

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server summary**

------------------------------------------------------------------------

**[display evi neighbor-discovery server summary**]命令用来在ENDS上显示ENDS的运行信息。

【命令】

**[display evi neighbor-discovery** [ **ipv6**  **server summary**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv6**]：显示IPv6 ENDS的运行信息。不指定本参数，则显示IPv4 ENDS的运行信息。

【使用指导】

通过本命令可以查看ENDS的运行信息，包括ENDS的配置信息、通过该ENDS学习到的ENDC个数。

【举例】

\# 显示IPv4 ENDS的运行信息。

\<Sysname\> display evi neighbor-discovery server summary

Interface      Local Address   Network ID    Auth        Members

Tunnel0        20.0.0.1        1             enabled     10     

Tunnel2        21.0.0.1        2             disabled    20     

Tunnel3        22.0.0.1        NA            disabled    0       

\# 显示IPv6 ENDS的运行信息。

\<Sysname\> display evi neighbor-discovery ipv6 server summary

Interface      Local Address   Network ID    Auth        Members

Tunnel0        2000::1         1             enabled     10     

Tunnel2        2000::2         2             disabled    20     

Tunnel1        2000::3         NA            disabled    0      

表1-16 display evi neighbor-discovery server summary命令显示信息描述表

字段

描述

Interface

启动ENDS功能的接口名称

Local Address

接口的源端地址，NA表示未配置

Network ID

接口下配置的Network ID，NA表示未配置

Auth

是否使能认证功能：

·enabled：表示已使能

·disabled：表示未使能

Members

通过该ENDS学习到的ENDC个数

【相关命令】

·**evi neighbor-discovery authentication**

·**evi neighbor-discovery server enable**

**EVI \-- EVI配置命令 \-- display evi vlan-mapping**

------------------------------------------------------------------------

**[display evi vlan-mapping**]命令用来显示EVI IS-IS的VLAN映射信息。

【命令】

**[display evi vlan-mapping** [ *process-id* [ **vlan** *vlan-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[process-id*]：显示指定的EVI IS-IS进程下的VLAN映射信息。*process-id*表示EVI IS-IS进程号，取值范围为0～65535。如果不指定本参数，将显示所有EVI IS-IS进程的VLAN映射信息。

*[vlan-id*]：显示指定VLAN的映射信息，取值范围为1～4094。如果不指定本参数，将显示所有VLAN的映射信息。

【举例】

\# 显示所有EVI IS-IS进程下的所有VLAN的映射信息。

\<Sysname\> display evi vlan-mapping

                         VLAN mappings for EVI IS-IS(0)

Local-VID  Peer-ID          Remote-VID  Interface   Remote-site

120        c4ca.d9e0.b804   121         EVI-Link2   10

                         VLAN mappings for EVI IS-IS(1)

Local-VID  Peer-ID          Remote-VID  Interface   Remote-site

150        3822.d659.6204   180         EVI-Link1   2

300        3822.d659.6204   301         EVI-Link1   2

表1-17 display evi vlan-mapping显示信息描述表

字段

描述

VLAN mappings for EVI IS-IS(0)

EVI IS-IS进程0的VLAN映射信息

Local-VID

本设备上的VLAN号

Peer-ID

与本设备关于上述VLAN有映射关系的EVI IS-IS邻居的System ID

Remote-VID

邻居上与上述VLAN映射的VLAN号

Interface

邻居所属的EVI-Link接口

Remote-site

VLAN映射所对应的远端站点ID

**EVI \-- EVI配置命令 \-- display interface evi-link**

------------------------------------------------------------------------

**[display interface evi-link**]命令用来显示EVI-Link接口的相关信息。

【命令】

**[display interface** [ **evi-link** [ *interface-number*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-number*]：显示指定EVI-Link接口的信息。*interface-number*表示EVI-Link接口编号，取值为已创建的EVI-Link接口的编号。

**[brief**]：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

本命令可以显示EVI-Link接口的相关信息，包括缺省VLAN ID、链路类型、EVI隧道源端地址、EVI隧道目的端地址、Network ID等。

需要注意的是：

·如果不指定**evi-link**参数，将显示设备支持的所有接口的相关信息。

·如果指定**evi-link**参数，不指定*interface-number*参数，将显示所有已创建的EVI-Link接口的相关信息。

【举例】

\# 显示接口EVI-Link0的详细信息。

\<Sysname\> display interface evi-link 0

EVI-Link0

Current state: UP

Description: EVI-Link0 Interface

PVID: 1

Port link-type: trunk

 VLAN Passing:   none

 VLAN permitted: none

 Trunk port encapsulation:  IEEE 802.1q

This EVI-link belongs to Tunnel0

Source 1.1.1.1, Destination 1.1.2.1

Network ID 1

表1-18 display interface evi-link命令显示信息描述表

字段

描述

Current state

接口的物理状态，可能的取值及含义如下：

·DOWN：该接口的物理状态为关闭

·UP：该接口的物理状态为开启

Description

接口描述信息

PVID: 1

EVI-Link接口的缺省VLAN ID为1

Port link-type: trunk

EVI-Link接口的链路类型为trunk

VLAN Passing

Trunk口实际可以通过的VLAN（该VLAN已经创建，并且接口允许其通过），对于EVI-Link接口来说，始终显示none

VLAN permitted

Trunk口允许通过的VLAN（该VLAN不一定存在，可能没有创建），对于EVI-Link接口来说，始终显示none

Trunk port encapsulation

Trunk口上封装的协议类型

This EVI-link belongs to Tunnel0

EVI-Link接口所属的EVI隧道实例

Source

EVI-Link接口的EVI隧道本端地址

Destination

EVI-Link接口的EVI隧道对端地址

Network ID

EVI-Link接口所属的Network ID

\# 显示接口EVI-Link0的概要信息。

\<Sysname\> display interface evi-link 0 brief

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Speed or Duplex: (a)/A - auto; H - half; F - full

Type: A - access; T - trunk; H - hybrid

Interface            Link Speed   Duplex Type PVID Description

ELNK0                UP   \--      \--     T    1

\# 显示当前物理状态为down的EVI-Link接口的信息以及down的原因。

\<Sysname\> display interface evi-link brief down

Brief information on interface(s) under bridge mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

ELNK0                DOWN Not connected

表1-19 display interface evi-link brief命令显示信息描述表

字段

描述

Brief information on interface(s) under bridge mode

二层接口的概要信息

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·DOWN：表示接口物理上不通

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

·Stby：表示该接口是一个备份接口

Speed

接口的速率，单位为bps

Duplex

接口的双工模式，取值可能为：

·A：表示双工模式由自动协商结果决定

·F：表示全双工

·F(a)：表示自动协商的结果为全双工

·H：表示半双工

·H(a)：表示自动协商的结果为半双工

Type

链路类型，取值可能为：

·A：表示Access链路类型

·T：表示Trunk链路类型

·H：表示Hybrid链路类型

PVID

接口的缺省VLAN ID

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态；取值为Not connected时表示没有物理连接（可能没有插网线或者网线故障）

**EVI \-- EVI配置命令 \-- evi arp-suppression enable**

------------------------------------------------------------------------

**[evi arp-suppression enable**]命令用来开启EVI ARP泛洪抑制功能。

**[undo evi arp-suppression enable**]命令用来恢复缺省情况。

【命令】

**[evi arp-suppression enable**]

**[undo evi arp-suppression enable**]

【缺省情况】

EVI ARP泛洪抑制功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

边缘设备通过侦听EVI隧道终结的流量建立EVI ARP泛洪抑制表项，当侦听到本站点内主机请求其它站点主机的ARP请求时，优先根据EVI ARP泛洪抑制表项进行代答，没有表项的则将ARP请求泛洪到公网。该功能可以大大减少ARP泛洪的次数。

需要注意的是，如果在动态MAC地址表项老化时间内，远端站点的EVI边缘设备没有流量转发到本地站点，那么远端EVI边缘设备上的动态MAC地址表项就会老化删除，同时通过EVI IS-IS通告本地站点的EVI边缘设备也删除对应表项。此时，如果本地站点内其他主机向对端站点内主机发出ARP请求，本地EVI边缘设备会根据EVI ARP泛洪抑制表项对该ARP请求进行代答。但是，报文在转发时会因为在本地EVI边缘设备的MAC地址表中没有对应表项而被丢弃，造成流量黑洞。

为了避免EVI边缘设备错误地代答本地的ARP请求造成流量黑洞，用户需要配置MAC地址表项老化时间不小于EVI ARP泛洪抑制表项老化时间。EVI ARP泛洪抑制表项的缺省老化时间为15分钟，动态MAC地址表项的缺省老化时间与设备型号有关，请以设备实际情况为准。可以通过命令**display mac-address aging-time**和**mac-address timer**查看和配置动态MAC地址表项的老化时间。

【举例】

\# 在EVI隧道接口Tunnel101下开启EVI ARP泛洪抑制功能。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel 101 evi arp-suppression enable

【相关命令】

·**display evi arp-suppression**

·**mac-address timer**（二层技术-以太网交换命令参考/MAC地址表）

·**reset evi arp-suppression**

**EVI \-- EVI配置命令 \-- evi designated-vlan**

------------------------------------------------------------------------

**[evi designated-vlan**]命令用来配置指定VLAN。

**[undo evi designated-vlan**]命令用来恢复缺省情况。

【命令】

**[evi designated-vlan** *vlan-id*]

**[undo evi designated-vlan**]

【缺省情况】

指定VLAN为1。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：指定VLAN，取值范围为1～4094。

【使用指导】

指定VLAN用来进行站点内EVI IS-IS Hello报文的交互。

网络规划时，必须保证各边缘设备在其指定VLAN内可达。

【举例】

\# 配置指定VLAN为2。

\<Sysname\> system-view

Sysname evi designated-vlan 2

**EVI \-- EVI配置命令 \-- evi enable**

------------------------------------------------------------------------

![说明](EVI命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[evi enable**]命令用来开启接口的EVI功能。

**[undo evi enable**]命令用来恢复缺省情况。

【命令】

**[evi enable**]

**[undo evi enable**]

【缺省情况】

接口的EVI功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

用户需要在接入EVI网络的所有物理接口上开启EVI功能。

【举例】

\# 开启接口GigabitEthernet1/0/1的EVI功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 evi enable

**EVI \-- EVI配置命令 \-- evi extend-vlan**

------------------------------------------------------------------------

**[evi extend-vlan**]命令用来配置扩展VLAN。

**[undo evi extend-vlan**]命令用来取消配置的扩展VLAN。

【命令】

**[evi extend-vlan** *vlan-list*]

**[undo evi extend-vlan** *vlan-list*]

【缺省情况】

没有配置扩展VLAN。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：VLAN列表，指定了扩展VLAN的范围。表示方式为*vlan-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以输入10次。

【举例】

\# 配置扩展VLAN为1～10、15和100～200。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi extend-vlan 1 to 10 15 100 to 200

**EVI \-- EVI配置命令 \-- evi flooding enable**

------------------------------------------------------------------------

![说明](EVI命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[evi flooding enable**]命令用来开启EVI泛洪功能。

**[undo evi flooding enable**]命令用来恢复缺省情况。

【命令】

**[evi flooding enable**]

**[undo evi flooding enable**]

【缺省情况】

EVI泛洪功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

缺省情况下，边缘设备对于未知地址的帧（包括未知单播帧和未知组播帧）只在VLAN内的站点内部接口上进行泛洪，不会泛洪到其它站点。如果用户希望未知地址的帧可以泛洪到其它站点，可以开启EVI泛洪功能，当边缘设备收到未知地址的帧时，可以通过EVI隧道泛洪转发到其它站点。

**[evi flooding enable**]命令和**evi selective-flooding mac-address**命令的区别如下：

·**evi flooding enable**命令是将所有的未知单播帧和未知组播帧都向其它站点泛洪。

·**evi selective-flooding mac-address**命令是针对某业务的MAC地址放开限制，仅将配置的MAC地址在指定的VLAN范围内向其它站点泛洪。

上述两个命令的使用场景不同，建议用户不要同时配置。如果用户同时配置了这两条命令，系统实际执行的是**evi flooding enable**命令，无法实现**evi selective-flooding mac-address**命令的控制效果。

【举例】

\# 在EVI隧道接口Tunnel101下开启EVI泛洪功能。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel 101 evi flooding enable

【相关命令】

·**evi selective-flooding mac-address**

**EVI \-- EVI配置命令 \-- evi isis ded-priority**

------------------------------------------------------------------------

**[evi isis ded-priority**]命令用来配置DED优先级。

**[undo evi isis ded-priority**]命令用来恢复缺省情况。

【命令】

**[evi isis ded-priority ***value*]

**[undo evi isis ded-priority**]

【缺省情况】

DED优先级为64。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：配置DED优先级，取值范围为0～127。

【使用指导】

DED分为站点内DED和站点间DED，二者的选举方式和作用不同：

·站点内DED：站点内的各边缘设备通过交互EVI IS-IS Hello报文来选举站点内DED。由站点内DED来分配各边缘设备的激活VLAN。

·站点间DED：每个EVI Link两端的边缘设备通过交互EVI IS-IS Hello报文选举出一个站点间DED。站点间的边缘设备通过站点间DED周期性发布CSNP报文来进行LSDB同步。

DED优先级数值越高，被选中的可能性就越大；如果两台边缘设备的DED优先级相同，则MAC地址较大的边缘设备会被选中。

【举例】

\# 配置EVI隧道接口Tunnel101的DED优先级为2。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi isis ded-priority 2

【相关命令】

·**display** **evi isis** **tunnel**

**EVI \-- EVI配置命令 \-- evi isis preferred-vlan**

------------------------------------------------------------------------

**[evi isis preferred-vlan**]命令用来配置优先分配给本设备的扩展VLAN，本设备将优先作为这些扩展VLAN的授权转发设备。

**[undo evi isis preferred-vlan**]命令用来取消优先分配给本设备的扩展VLAN的配置。

【命令】

**[evi isis preferred-vlan** *vlan-list*]

**[undo evi isis preferred-vlan** *vlan-list*]

【缺省情况】

没有配置优先分配给本设备的扩展VLAN。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-list*]：VLAN列表，指定了优先分配给本设备的扩展VLAN的范围。表示方式为*vlan-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

边缘设备配置了优先作为扩展VLAN X的授权转发设备后，DED会优先将扩展VLAN X分配给该边缘设备作为激活VLAN。两台或多台站点内边缘设备都配置了同样的VLAN，则仍按照原来的平均和连续的原则分配激活VLAN。取消配置后，如果该扩展VLAN没有被其他边缘设备配置为优先分配的扩展VLAN，按稳定原则不改变其授权转发设备。

需要注意的是：

·多次配置本命令，其结果是多次配置VLAN的合集。

·配置的优先分配给本设备的扩展VLAN必须是所配置的扩展VLAN的子集，如果用户配置的VLAN本身就不是扩展VLAN，则不起作用。

【举例】

\# 配置本设备优先作为扩展VLAN1～10、15、100～200的授权转发设备。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 evi isis preferred-vlan 1 to 10 15 100 to 200

【相关命令】

·**evi extend-vlan**

**EVI \-- EVI配置命令 \-- evi isis timer csnp**

------------------------------------------------------------------------

**[evi isis timer csnp**]命令用来配置DED发送CSNP报文的时间间隔。

**[undo evi isis timer csnp**]命令用来恢复缺省情况。

【命令】

**[evi isis timer csnp** *seconds*]

**[undo evi isis timer csnp**]

【缺省情况】

DED发送CSNP报文的时间间隔为10秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：DED发送CSNP报文的时间间隔，取值范围为1～600，单位为秒。

【使用指导】

DED使用CSNP报文来进行LSDB同步，只有在被选举为DED的设备上进行该项配置才有效。

【举例】

\# 配置DED发送CSNP报文的时间间隔为15秒。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi isis timer csnp 15

【相关命令】

·**display** **evi isis** **tunnel**

**EVI \-- EVI配置命令 \-- evi isis timer hello**

------------------------------------------------------------------------

**[evi isis timer hello**]命令用来配置EVI IS-IS Hello报文的发送时间间隔。

**[undo evi isis timer hello**]命令用来恢复缺省情况。

【命令】

**[evi isis timer hello** *seconds*]

**[undo evi isis timer hello**]

【缺省情况】

EVI IS-IS Hello报文的发送时间间隔为10秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：配置EVI IS-IS Hello报文的发送时间间隔，取值范围为3～255，单位为秒。

【使用指导】

EVI IS-IS Hello报文的发送时间间隔越短，网络收敛越快，但也需要占用更多的系统资源；因此，需要根据实际情况指定EVI IS-IS Hello报文的发送时间间隔。

需要注意的是，DED发送EVI IS-IS Hello报文的时间间隔是**evi isis timer hello**命令设置的时间间隔的1/3。

【举例】

\# 配置EVI IS-IS Hello报文的发送时间间隔为6秒。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi isis timer hello 6

【相关命令】

·**display** **evi isis** **tunnel**

**EVI \-- EVI配置命令 \-- evi isis timer holding-multiplier**

------------------------------------------------------------------------

**[evi isis timer holding-multiplier**]命令用来配置EVI IS-IS Hello报文失效数目。

**[undo evi isis timer holding-multiplier**]命令用来恢复缺省情况。

【命令】

**[evi isis timer holding-multiplier** *value*]

**[undo evi isis timer holding-multiplier**]

【缺省情况】

EVI IS-IS Hello报文失效数目为3。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：配置邻居的EVI IS-IS Hello报文失效数目，取值范围为3～1000。

【使用指导】

当前边缘设备可以将邻接关系保持时间通过EVI IS-IS Hello报文通知邻居边缘设备，如果邻居边缘设备在邻接关系保持时间内没有收到来自当前边缘设备的EVI IS-IS Hello报文，将宣告邻接关系失效。

邻接关系保持时间＝EVI IS-IS Hello报文失效数目×EVI IS-IS Hello报文发送时间间隔。EVI IS-IS Hello报文失效数目，即宣告邻接关系失效前EVI IS-IS没有收到的邻居EVI IS-IS Hello报文的数目。通过设置EVI IS-IS Hello报文失效数目和EVI IS-IS Hello报文的发送时间间隔，可以调整邻接关系保持时间，即邻居边缘设备要花多长时间能够监测到链路已经失效并重新进行路由计算。

邻接关系保持时间最大不能超过65535秒，超过65535秒时，算作65535秒。

【举例】

\# 配置EVI IS-IS Hello报文失效数目为6。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi isis timer holding-multiplier 6

【相关命令】

·**display evi isis tunnel**

·**evi isis timer hello**

**EVI \-- EVI配置命令 \-- evi isis timer lsp**

------------------------------------------------------------------------

**[evi isis timer lsp**]命令用来配置EVI IS-IS在接口上发送LSP的最小时间间隔以及一次最多可以发送的LSP数目。

**[undo evi isis timer lsp**]命令用来恢复缺省情况。

【命令】

**[evi isis timer lsp***time * **count** *count* ]

**[undo evi isis timer lsp**]

【缺省情况】

发送LSP的最小时间间隔为100毫秒，一次最多可以发送的LSP数目为5。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：发送LSP的最小时间间隔，取值范围为100～1000，为100的整数倍，单位为毫秒。

**[count***count*]：一次最多可以发送的LSP数目，取值范围为1～1000，缺省值为5。

【使用指导】

当LSDB的内容发生变化时，EVI IS-IS将把发生变化的LSP扩散出去，用户可以对LSP的最小发送时间间隔进行调节。

【举例】

\# 配置发送LSP的最小时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel101 evi isis timer lsp 500

【相关命令】

·**display** **evi isis** **brief**

**EVI \-- EVI配置命令 \-- evi isis track**

------------------------------------------------------------------------

**[evi isis track**]命令用来配置EVI IS-IS关联的Track项。

**[undo evi isis track**]命令用来删除EVI IS-IS关联的Track项。

【命令】

**[evi isis track ***track-entry-number*]

**[undo evi isis track**]

【缺省情况】

EVI IS-IS不与任何Track项联动。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：指定Track项的序号，取值范围为1～1024。

【使用指导】

EVI IS-IS关联Track项后，可以通过Track项的状态来检测上行口的故障。

一个Tunnel接口下的EVI IS-IS实例最多关联一个Track项，当配置多次时，最后配置的Track项生效。关于Track的详细介绍请参见"可靠性"中的"Track"。

【举例】

\# 配置EVI隧道接口Tunnel101上运行的EVI IS-IS关联Track项1。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 evi isis track 1

**EVI \-- EVI配置命令 \-- evi neighbor-discovery authentication**

------------------------------------------------------------------------

**[evi neighbor-discovery authentication**]命令用来使能ENDP认证功能。

**[undo evi neighbor-discovery authentication**]命令用来关闭ENDP认证功能。

【命令】

**[evi neighbor-discovery authentication**[ { **cipher** \| **simple** } ]]*password*

**[undo evi neighbor-discovery authentication**]

【缺省情况】

ENDP认证功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文方式设置认证密码。

**[simple**]：表示以明文方式设置认证密码。

*[password*]：设置的明文认证密码或密文认证密码，区分大小写。明文认证密码为1～24个字符的字符串；密文认证密码为1～65个字符的字符串。

【使用指导】

为了安全起见，可以配置ENDP认证功能来防止恶意的节点注册到EVI网络。

使能ENDP认证功能后，发送ENDP报文的设备会使用配置的密码和MD5算法对报文进行摘要运算，然后把运算结果放到报文的认证字段。对端设备收到ENDP报文后，如果该设备未配置认证功能，则认为报文合法；如果设备配置了认证功能，则利用本端配置的密码和MD5算法对报文进行摘要运算，然后比较运算结果与报文认证字段携带的信息是否一致，如果一致则认为报文合法，如果不一致则认为报文非法。

在一个安全的网络中，可以不配置ENDP认证功能。

需要注意的是：

·同一个EVI网络实例中所有的ENDS与ENDC必须配置相同的认证密码。

·以明文或密文方式设置的认证密码，均以密文的方式保存在配置文件中。

【举例】

\# 使能ENDP认证功能，并以方式设置指定明文认证密码为web-evi。

\<Sysname\> system

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 evi neighbor-discovery authentication simple web-evi

【相关命令】

·**display evi neighbor-discovery client summary**

·**display evi neighbor-discovery ipv6 client summary**

·**display evi neighbor-discovery ipv6 server summary**

·**display evi neighbor-discovery server summary**

**EVI \-- EVI配置命令 \-- evi neighbor-discovery client enable**

------------------------------------------------------------------------

**[evi neighbor-discovery client enable**]命令用来使能接口的ENDC功能，同时指定对应的ENDS地址。

**[undo evi neighbor-discovery client enable**]命令用来关闭接口的ENDC功能。

【命令】

**[evi neighbor-discovery client enable ***server-ip*]

**[undo evi neighbor-discovery client enable ***server-ip*]

【缺省情况】

ENDC功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-ip*]：ENDC要连接的ENDS的IP地址或IPv6地址。

【使用指导】

为了防止ENDS异常导致ENDC不能加入EVI网络，用户可以为每个ENDC指定两个ENDS，这两个ENDS同时有效。

【举例】

\# 使能IPv4 ENDC功能，该ENDC对应的ENDS地址为11.0.0.1。

\<Sysname\> system

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 evi neighbor-discovery client enable 11.0.0.1

\# 使能IPv6 ENDC功能，该ENDC对应的ENDS地址为2000::1。

\<Sysname\> system

Sysname interface tunnel 0 mode evi ipv6

Sysname-Tunnel0 evi neighbor-discovery client enable 2000::1

【相关命令】

·**display evi neighbor-discovery client summary**

·**display evi neighbor-discovery ipv6 client summary**

**EVI \-- EVI配置命令 \-- evi neighbor-discovery client register-interval**

------------------------------------------------------------------------

**[evi neighbor-discovery client register-interval**]命令用来配置ENDC向ENDS注册的时间间隔。

**[undo evi neighbor-discovery client register-interval**]命令用来恢复缺省情况。

【命令】

**[evi neighbor-discovery client register-interval **]*time-value*

**[undo evi neighbor-discovery client register-interval**]

【缺省情况】

ENDC向ENDS注册的时间间隔为15秒。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-value*]：注册时间间隔，取值范围为5～120，单位为秒。

【使用指导】

ENDP协议中用到了3个定时器：探测定时器、注册定时器、老化定时器。

(1)探测定时器

ENDC请求加入EVI网络时会启用探测定时器，该定时器以5秒的时间间隔定时向ENDS发送注册报文，收到ENDS应答报文后会停止探测定时器。

(2)注册定时器

ENDC加入EVI网络后，为了通告自己工作正常，会定时向ENDS发送注册报文，该定时器的默认时间间隔为15秒，用户可以通过配置**evi neighbor-discovery client register-interval**命令来调整该时间间隔。

如果ENDC连续发送5个注册报文，都未能收到ENDS的应答报文，则认为网络故障，此时需要清除之前学到的邻居信息，同时重新启用探测定时器。

(3)老化定时器

ENDC向ENDS发送的注册报文中携带注册时间间隔，ENDS会记录该时间间隔。

ENDC加入EVI网络后，如果ENDS在5倍的注册时间内未收到ENDC的注册报文则认为ENDC出现故障，此时需要把ENDC从EVI网络中删除。

【举例】

\# 配置ENDC向ENDS注册的时间间隔为30秒。

\<Sysname\> system

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 evi neighbor-discovery client register-interval 30

【相关命令】

·**display evi neighbor-discovery client summary**

·**display evi neighbor-discovery ipv6 client summary**

**EVI \-- EVI配置命令 \-- evi neighbor-discovery server enable**

------------------------------------------------------------------------

**[evi neighbor-discovery server enable**]命令用来使能接口的ENDS功能。

**[undo evi neighbor-discovery server enable**]命令用来关闭接口的ENDS功能。

【命令】

**[evi neighbor-discovery server enable**]

**[undo evi neighbor-discovery server enable**]

【缺省情况】

ENDS功能处于关闭状态。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能接口的ENDS功能时，会同时使能该接口的ENDC功能（该ENDC对应的ENDS地址为该接口的源地址）。

【举例】

\# 使能IPv4 ENDS功能。

\<Sysname\> system

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 evi neighbor-discovery server enable

\# 使能IPv6 ENDS功能。

\<Sysname\> system

Sysname interface tunnel 0 mode evi ipv6

Sysname-Tunnel0 evi neighbor-discovery server enable

【相关命令】

·**display evi neighbor-discovery ipv6 server summary**

·**display evi neighbor-discovery server summary**

**EVI \-- EVI配置命令 \-- evi network-id**

------------------------------------------------------------------------

**[evi network-id**]命令用来配置Network ID。

**[undo evi network-id**]命令用来删除Network ID。

【命令】

**[evi network-id ***number*]

**[undo evi network-id**]

【缺省情况】

没有配置Network ID。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：Network ID值，取值范围为1～16777215。

【使用指导】

一个站点需要加入EVI网络时，必须指定加入的EVI网络实例的Network ID。

一个EVI隧道只能属于一个EVI网络实例，一个站点加入多个EVI网络实例时，需要创建多个EVI Tunnel接口，并使用该命令指定多个EVI Tunnel接口分别属于哪个EVI网络实例。

【举例】

\# 配置EVI隧道的Network ID为123。

\<Sysname\> system-view

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 evi network-id 123

【相关命令】

·**interface tunnel**

**EVI \-- EVI配置命令 \-- evi selective-flooding mac-address**

------------------------------------------------------------------------

**[evi selective-flooding mac-address**]命令用来配置选择性泛洪的MAC地址。

**[undo evi selective-flooding mac-address**]命令用来恢复缺省情况。

【命令】

**[evi selective-flooding mac-address ***mac-address ***vlan****]*vlan-id-list*

**[undo evi selective-flooding mac-address*** mac-address ***vlan****]*vlan-id-list*

【缺省情况】

未配置选择性泛洪的MAC地址。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：选择性泛洪的MAC地址。该MAC地址不能为全F。

**[vlan****]*vlan-id-list*：指定选择性泛洪MAC地址所属的VLAN范围，*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]，*vlan-id*的取值范围为1～4094，*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值，&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

缺省情况下，边缘设备对于未知地址的帧（包括未知单播帧和未知组播帧）只在VLAN内的站点内部接口上进行泛洪，不会泛洪到其它站点。如果用户希望某些MAC地址的帧可以泛洪到其它站点，可以通过本命令配置选择性泛洪的MAC地址，当报文的目的MAC地址匹配该MAC地址时，报文可以通过EVI隧道泛洪转发到其它站点。

需要注意的是：

·选择性泛洪MAC地址所属的VLAN范围受到EVI Tunnel接口下激活VLAN的范围影响，最终生效的VLAN范围为激活VLAN和配置指定的VLAN之交集。

·不要将可以学习到的单播MAC地址设置为选择性泛洪的MAC地址，否则可能会导致报文在远端设备被丢弃。

【举例】

\# 在EVI隧道接口Tunnel101下配置选择性泛洪的MAC地址。

\<Sysname\> system-view

Sysname interface tunnel 101 mode evi

Sysname-tunnel 101 evi selective-flooding mac-address 000f-e201-0101 vlan 1 to 10

**EVI \-- EVI配置命令 \-- evi site-id**

------------------------------------------------------------------------

**[evi site-id**]命令用来指定一个设备所属的站点ID。

**[undo evi site-id**]命令用来恢复缺省情况。

【命令】

**[evi site-id ***site-id*]

**[undo evi site-id**]

【缺省情况】

站点ID为0。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[site-id*]：站点ID，取值范围为1～65535。

【使用指导】

站点ID用来唯一标识边缘设备所处的站点。如果没有为边缘设备配置站点ID（采用缺省站点ID 0），则其他边缘设备认为该设备为站点间边缘设备。相同站点内的多台边缘设备必须配置相同的的站点ID，不同站点间的边缘设备必须配置不同的站点ID或者均采用缺省站点ID。

当两台设备均在本地站点时，如果为设备配置不同的站点ID或至少一台设备采用缺省站点ID，则会出现冲突，此时会将桥MAC地址较小的设备隔离；当两台设备分别为不同站点时，配置相同的站点ID时会出现冲突，此时同样会将桥MAC地址较小的设备隔离。此处的隔离是针对EVI IS-IS协议来说的，被隔离的设备对于EVI IS-IS Hello报文将进行只收不发的处理，对于其它EVI IS-IS协议报文将不会进行交互。设备被隔离的情况可以通过**display evi isis brief**命令和**display evi isis peer**命令查看。

【举例】

\# 配置设备所属的站点ID为201。

\<Sysname\> system-view

Sysname evi site-id 201

【相关命令】

·**display evi-isis brief**

·**display evi isis peer**

**EVI \-- EVI配置命令 \-- evi vlan-mapping**

------------------------------------------------------------------------

**[evi vlan-mapping**]命令用来配置本设备上某VLAN与其他站点的VLAN的映射关系。

**[undo evi vlan-mapping**]命令用来删除VLAN映射关系。

【命令】

**[evi vlan-mapping ***local-vlan-id* **translated** *remote-vlan-id* [ **site** *site-id* ]]

**[undo evi vlan-mapping** \*[local-vlan-id ***translated** *remote-vlan-id* [ **site** *site-id*  ]]]

【缺省情况】

未配置VLAN映射关系。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[local-vlan-id*]：本地VLAN号，取值范围为1～4094。

*[remote-vlan-id*]：远端站点的VLAN号，取值范围为1～4094。

*[site-id*]：远端站点的站点ID，取值范围为1～65535。不指定本参数时，表示到其它所有站点的映射关系。

【使用指导】

**[undo**]命令中不指定任何参数时，表示删除所有的VLAN映射关系。

【举例】

\# 配置Tunnel101的VLAN 100与站点2的VLAN 200进行映射。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 evi vlan-mapping 100 translated 200 site 2

\# 配置Tunnel101的VLAN 100与其它所有站点的VLAN 200进行映射。

\<Sysname\> system-view

Sysname interface tunnel 101

Sysname-tunnel101 evi vlan-mapping 100 translated 200

**EVI \-- EVI配置命令 \-- evi-isis**

------------------------------------------------------------------------

**[evi-isis**]命令用来创建EVI IS-IS进程，并进入EVI IS-IS视图。

**[undo evi-isis**]命令用来删除EVI IS-IS进程或者清除EVI IS-IS进程下的配置数据。

【命令】

**[evi-isis ***process-id*]

**[undo evi-isis ***process-id*]

【缺省情况】

不存在EVI IS-IS进程。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：EVI IS-IS的进程ID，取值范围为0～65535。

【使用指导】

一个EVI实例对应一个EVI IS-IS进程。

创建EVI IS-IS进程有如下两种方法：

·在EVI Tunnel接口下配置可以创建EVI IS-IS进程的配置项。此时会自动创建EVI IS-IS进程，其进程ID与EVI Tunnel接口号相同。

·执行**evi-isis**命令。此时该EVI IS-IS进程与相同编号的EVI Tunnel接口相对应。

创建EVI IS-IS进程后，用户可以通过**evi-isis**命令进入EVI IS-IS视图，配置EVI IS-IS进程的协议参数。

需要注意的是，如果没有配置扩展VLAN，对应的EVI IS-IS进程不生效。

删除EVI IS-IS进程的时机如下：

·如果没有执行过**evi-isis**命令，只是通过在EVI Tunnel接口下配置EVI IS-IS配置项而自动创建了EVI IS-IS进程，在此种情况下，删除EVI Tunnel接口下的EVI IS-IS配置项时会自动删除对应的EVI IS-IS进程。

·如果执行过**evi-isis**命令，那么删除EVI Tunnel接口下的EVI IS-IS配置项时不会自动删除对应的EVI IS-IS进程，只能通过**undo evi-isis**命令来删除EVI IS-IS进程。

·执行**undo evi-isis**命令时，如果EVI IS-IS进程对应的EVI Tunnel接口存在EVI IS-IS配置项，则不会删除进程，只会清除进程下的配置数据；如果EVI IS-IS进程对应的EVI Tunnel接口下不存在EVI IS-IS配置项，则会删除进程，并清除进程下的配置数据。

【举例】

\# 进入EVI IS-IS视图。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101

【相关命令】

·**display evi****isis brief**

**EVI \-- EVI配置命令 \-- filter-policy**

------------------------------------------------------------------------

**[filter-policy**]命令用来配置EVI IS-IS进程绑定的路由策略。

**[undo filter-policy**]命令用来删除EVI IS-IS进程绑定的路由策略。

【命令】

**[filter-policy** *policy-name*]

**[undo filter-policy**]

【缺省情况】

EVI IS-IS进程没有绑定路由策略。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：路由策略名称，为1～63个字符的字符串，区分大小写。

【使用指导】

绑定路由策略后，该EVI IS-IS进程只向其它站点通告路由策略允许的站点本地MAC地址信息。

EVI IS-IS进程绑定的路由策略的配置中仅有如下两类匹配条件生效：

·MAC地址列表过滤的匹配条件

·VLAN范围的匹配条件

关于路由策略的详细介绍请参见"三层技术-IP路由配置指导"中的"路由策略"。

【举例】

\# 配置EVI IS-IS进程绑定路由策略EVI-Filter。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101 filter-policy EVI-Filter

**EVI \-- EVI配置命令 \-- graceful-restart**

------------------------------------------------------------------------

**[graceful-restart**]命令用来使能EVI IS-IS的GR能力。

**[undo graceful-restart**]命令用来关闭EVI IS-IS的GR能力。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

EVI IS-IS的GR能力处于关闭状态。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能EVI IS-IS进程101的GR能力。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101 graceful-restart

【相关命令】

·**display evi isis graceful-restart status**

**EVI \-- EVI配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

**[graceful-restart interval**]命令用来配置EVI IS-IS协议的GR重启间隔时间。

**[undo graceful-restart interval**]命令用来恢复缺省情况。

【命令】

**[graceful-restart interval** *interval-value*]

**[undo graceful-restart interval**]

【缺省情况】

EVI IS-IS协议的GR重启间隔时间为300秒。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：指定EVI IS-IS协议的GR重启间隔时间（期望重启时间），取值范围为30～1800，单位为秒。

【举例】

\# 配置EVI IS-IS进程1的GR重启间隔时间为120秒。

\<Sysname\> system-view

Sysname evi-isis 1

Sysname-evi-isis-1 graceful-restart interval 120

【相关命令】

·**display evi isis graceful-restart status**

**EVI \-- EVI配置命令 \-- gre key vlan-id**

------------------------------------------------------------------------

**[gre key vlan-id**]命令用来设置EVI类型Tunnel接口为发送的报文中添加根据VLAN ID生成的GRE Key。

**[undo gre key**]命令用来取消EVI类型Tunnel接口的GRE Key。

【命令】

**[gre key** **vlan-id**]

**[undo gre key**]

【缺省情况】

EVI类型Tunnel接口发送的报文中不携带GRE Key。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过设置EVI类型Tunnel接口发送报文时携带GRE Key后，发送方会在其发送的报文中携带GRE Key信息。接收方收到报文后将报文中的GRE Key与接收方本地配置的GRE Key进行比较，如果一致则对报文进行进一步处理；否则丢弃该报文。这样就可以防止设备接收非法报文。因此为保证通信正常，隧道两端必须设置相同的GRE Key，或者都不设置GRE Key。

执行本命令后，边缘设备将根据报文中的VLAN ID自动生成EVI类型Tunnel接口的GRE Key，并封装到报文中。GRE Key的高12位为VLAN ID，低20位为0。

部分产品发送报文时，报文中的GRE Key字段携带了VLAN ID。设备在与这些产品通信时需要配置本命令，使发出报文中的GRE Key字段也携带VLAN ID。

【举例】

\# 设置EVI类型Tunnel接口为发送的报文添加根据VLAN ID生成的GRE Key。

\<Sysname\> system-view

Sysname interface tunnel 1 mode evi

Sysname-Tunnel2 gre key vlan-id

【相关命令】

·**display interface tunnel**

**EVI \-- EVI配置命令 \-- keepalive**

------------------------------------------------------------------------

**[keepalive**]命令用来配置EVI隧道探测对端状态的keepalive报文的发送周期和最大发送次数。

**[undo keepalive**]命令用来恢复缺省情况。

【命令】

**[keepalive** [ *seconds* [ *times*  ]]]

**[undo keepalive**]

【缺省情况】

keepalive报文的发送周期为5秒，最大发送次数为2次。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：keepalive报文发送周期，取值范围为1～32767，单位为秒，缺省值为5秒。

*[times*]：keepalive报文的最大发送次数，取值范围为1～255，缺省值为2次。

【使用指导】

EVI Tunnel接口配置的ENDP协议会学习邻居信息并建立EVI-Link接口。设备会从基于EVI Tunnel建立的各个EVI-Link接口周期性发送keepalive报文。如果超时时间（即配置的keepalive报文发送周期）内没有收到对端的回应，则本端重新发送keepalive报文。如果达到最大发送次数后仍然没有收到对端的回应，则把本端EVI-Link接口的状态置为down。如果EVI-Link接口为down状态，当收到对端回复的keepalive确认报文或收到对端发送的keepalive报文时，EVI-Link接口的状态将转换为up，否则保持down状态。

【举例】

\# 配置keepalive报文的发送周期为20秒，最大发送次数为5次。

\<Sysname\> system-view

Sysname interface tunnel 0 mode evi

Sysname-Tunnel0 keepalive 20 5

【相关命令】

·**interface tunnel**

**EVI \-- EVI配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

**[log-peer-change enable**]命令用来打开邻接状态变化的输出开关。

**[undo log-peer-change enable**]命令用来关闭邻接状态变化的输出开关。

【命令】

**[log-peer-change enable**]

**[undo log-peer-change enable**]

【缺省情况】

邻接状态变化的输出开关处于打开状态。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当打开邻接状态变化的输出开关后，EVI IS-IS邻接状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。

【举例】

\# 关闭邻接状态变化的输出开关。

\<Sysname\> system-view

Sysname evi-isis 1

Sysname-evi-isis-1 undo log-peer-change enable

**EVI \-- EVI配置命令 \-- reset evi arp-suppression**

------------------------------------------------------------------------

**[reset evi arp-suppression**]命令用来清除EVI ARP泛洪抑制表项。

【命令】

**[reset evi arp-suppression interface tunnel*** interface-number * **vlan** *vlan-id* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface tunnel*** interface-number*]：清除指定EVI隧道接口下的EVI ARP泛洪抑制表项。

**[vlan ***vlan-id*]：清除指定VLAN的EVI ARP泛洪抑制表项。*vlan-id*表示VLAN编号，取值范围为1～4094。如果不指定本参数，将清除所有VLAN的EVI ARP泛洪抑制表项。

【举例】

\# 清除EVI隧道接口Tunnel101下的EVI ARP泛洪抑制表项。

\<Sysname\> reset evi arp-suppression interface tunnel 101

This will delete all entries under the specified interface. Continue? [Y/N:y]

【相关命令】

·**display evi arp-suppression**

·**evi arp-suppression enable**

**EVI \-- EVI配置命令 \-- reset evi isis all**

------------------------------------------------------------------------

**[reset evi isis all**]命令用来清除EVI IS-IS进程下所有的动态数据。

【命令】

**[reset evi isis all ** *process-id*]**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：EVI IS-IS进程号，取值范围为1～65535。如果不指定本参数，将清除所有EVI IS-IS进程下所有的动态数据。

【举例】

\# 清除EVI IS-IS进程1下所有的动态数据。

\<Sysname\> reset evi isis all 1

**EVI \-- EVI配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp context-name**]命令用来配置管理EVI IS-IS协议的SNMP实体所使用的上下文名称。

**[undo snmp context-name**]命令用来恢复缺省情况。

【命令】

**[snmp context-name ***context-name*]

**[undo snmp context-name**]

【缺省情况】

没有配置管理EVI IS-IS的SNMP实体所使用的上下文名称。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：管理EVI IS-IS协议的SNMP实体所使用的上下文名称，为1～32个字符的字符串，区分大小写。

【使用指导】

与IS-IS相同部分的EVI IS-IS信息使用了IS-IS的标准MIB（Management Information Base，管理信息库）对NMS（Network Management System，网络管理系统）提供EVI IS-IS信息对象的管理，但标准IS-IS MIB中定义的MIB为单实例管理对象，无法同时对IS-IS和EVI IS-IS进行管理。因此，参考RFC 4750中对OSPF多实例的管理方法，需要为管理EVI IS-IS定义一个上下文名称，以区分来自NMS的SNMP请求是要对IS-IS还是EVI IS-IS进行管理。

需要注意的是：

·所有使用标准IS-IS MIB的协议，如EVI、TRILL、IS-IS等，都需要配置上下文名称以区分SNMP请求的管理对象。各协议（包括各协议中的每个进程）配置的上下文名称都不能相同。

·由于上下文名称只是SNMPv3独有的概念，因此对于SNMPv1/v2c，会将团体名映射为上下文名称以对不同协议进行区分。

【举例】

\# 配置管理EVI IS-IS进程100的SNMP实体所使用的上下文名称为eviisis100。

\<Sysname\> system-view

Sysname evi-isis 100

Sysname-evi-isis-100 snmp context-name eviisis100

**EVI \-- EVI配置命令 \-- snmp-agent trap enable evi-isis**

------------------------------------------------------------------------

**[snmp-agent trap enable evi-isis**]命令用来开启EVI IS-IS的告警功能。

**[undo snmp-agent trap enable evi-isis**]命令用来关闭EVI IS-IS的告警功能。

【命令】

**[snmp-agent trap enable evi-isis**[ [ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **link-disconnect** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]]**maxarea-mismatch**[ \| ]**new-ded**[ \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** ] \*]

**[undo snmp-agent trap enable evi-isis**[ [ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **link-disconnect** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]]**maxarea-mismatch**[ \| ]**new-ded**[ \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** ] \*]

【缺省情况】

EVI IS-IS的所有告警功能均处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjacency-state-change**]：表示EVI IS-IS邻接状态变化的告警信息。

**[area-mismatch**]：表示Hello报文区域地址不匹配的告警信息。

**[buffsize-mismatch**]：表示LSP长度与产生缓冲区大小不匹配的告警信息。

**[id-length-mismatch**]：表示EVI IS-IS报文中System ID长度不匹配的告警信息。

**[link-disconnect**]：表示ED的公网侧故障的告警信息。

**[lsp-parse-error**]：表示LSP解析错误的告警信息。

**[lsp-size-exceeded**]：表示超大LSP导致泛洪失败的告警信息。

**[max-seq-exceeded**]：表示LSP序列号超过最大序列号的告警信息。

**[maxarea-mismatch**]：表示Hello报文最大区域地址不匹配的告警信息。

**[new-ded**]：表示本设备成为新的DED的告警信息。

**[own-lsp-purge**]：表示尝试清除本地LSP的告警信息。

**[protocol-support**]：表示报文协议支持类型不匹配的告警信息。

**[rejected-adjacency**]：表示无法根据Hello报文建立邻接关系的告警信息。

**[skip-sequence-number**]：表示跳过已产生过的LSP序列号的告警信息。

**[topology-change**]：表示站点内ED拓扑变化的告警信息。但同一事件导致发送了new-ded，则不发送本告警信息。

**[version-skew**]：表示Hello报文版本号不匹配的告警信息。

【使用指导】

·如果未指定任何参数，将开启EVI IS-IS所有类型的告警功能。

·开启EVI IS-IS模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的SNMP模块，通过设置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 开启EVI IS-IS邻居状态变化的告警功能。

\<Sysname\> system-view

Sysname snmp-agent trap enable evi-isis adjacency-state-change

**EVI \-- EVI配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

**[timer lsp-max-age**]命令用来配置当前边缘设备生成的LSP在LSDB里的最大生存时间。

**[undo timer lsp-max-age**]命令用来恢复缺省情况。

【命令】

**[timer lsp-max-age ***second*s]

**[undo timer lsp-max-age**]

【缺省情况】

当前边缘设备生成的LSP在LSDB里的最大生存时间为1200秒。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：LSP在LSDB里的最大生存时间，取值范围是3～65535，单位为秒。

【使用指导】

每个LSP都有一个最大生存时间，随着时间的推移最大生存时间将逐渐减小，当LSP的最大生存时间为0时，EVI IS-IS将启动清除过期LSP的过程。用户可根据网络的实际情况调整LSP的最大生存时间。

【举例】

\# 配置生成的LSP的最大生存时间为25分钟，即1500秒。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101 timer lsp-max-age 1500

【相关命令】

·**display** **evi isis** **brief**

**EVI \-- EVI配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

**[timer lsp-refresh**]命令用来配置LSP刷新周期。

**[undo timer lsp-refresh**]命令用来恢复缺省情况。

【命令】

**[timer lsp-refresh**] *second*s

**[undo timer lsp-refresh**]

【缺省情况】

LSP刷新周期为900秒。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[second*]s：LSP刷新周期，取值范围为1～65534，单位为秒。

【使用指导】

**[timer lsp-refresh**]命令配置的时间必须小于**timer lsp-max-age**命令配置的时间，以保证在LSP失效前进行刷新。

【举例】

\# 配置LSP刷新周期为1500秒。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101 timer lsp-refresh 1500

【相关命令】

·**display evi isis brief**

·**timer lsp-max-age**

**EVI \-- EVI配置命令 \-- virtual-system**

------------------------------------------------------------------------

**[virtual-system**]命令用来为系统创建一个EVI IS-IS虚拟系统。

**[undo **]**virtual-system**命令用来删除一个系统中已经存在的EVI IS-IS虚拟系统。

【命令】

**[virtual-system **]*system-id*

**[undo **]**virtual-system ***system-id*

【缺省情况】

系统中没有创建EVI IS-IS虚拟系统。

【视图】

EVI IS-IS视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[system-id*]：虚拟系统的系统ID，用来标识虚拟系统，格式为XXXX.XXXX.XXXX，X表示十六进制数字。

【使用指导】

当本地MAC地址数超过系统的LSP分片集所能携带的MAC地址数时，可以配置EVI IS-IS虚拟系统来扩展LSP的分片数量，以增加系统所能发布的MAC地址数量。

创建虚拟系统前，系统最多可以发送约55×2^10^的MAC地址信息，每创建一个虚拟系统，最多可以多发送55×2^10^的MAC地址信息。用户可以根据本地MAC地址表的规模，来决定创建的虚拟系统的个数。

创建虚拟系统时，用户要保证所配置的虚拟系统的系统ID在网络中是唯一的，否则会出现不可预知的错误。

【举例】

\# 创建一个系统ID为0001.0001.0001的虚拟系统。

\<Sysname\> system-view

Sysname evi-isis 101

Sysname-evi-isis-101 virtual-system 0001.0001.0001
