<!-- CMD-INDEX
  ap-mode                             | SPBM视图           | L76
  area-authentication send-only       | SPBM视图           | L128
  area-authentication-mode            | SPBM视图           | L174
  b-vlan                              | VSI SPB视图        | L240
  bandwidth-reference                 | SPBM视图           | L290
  bridge-priority                     | SPBM视图           | L344
  circuit-cost                        | SPBM视图           | L390
  control-address                     | SPBM视图           | L446
  display l2vpn minm connection       | 任意视图             | L496
  display l2vpn minm forwarding       | 任意视图             | L598
  display l2vpn vsi                   | 任意视图             | L726
  display spbm agreement-protocol     | 任意视图             | L940
  display spbm b-vlan                 | 任意视图             | L1146
  display spbm bridge                 | 任意视图             | L1242
  display spbm bvlan-info             | 任意视图             | L1298
  display spbm bvlan-info statistics  | 任意视图             | L1380
  display spbm common statistics      | 任意视图             | L1498
  display spbm ect                    | 任意视图             | L1638
  display spbm ect-migration          | 任意视图             | L1822
  display spbm fast-channel statistics | 任意视图             | L1890
  display spbm graceful-restart event-log | 任意视图             | L2014
  display spbm graceful-restart status | 任意视图             | L2160
  display spbm interface              | 任意视图             | L2298
  display spbm lsdb                   | 任意视图             | L2438
  display spbm multicast-fdb          | 任意视图             | L2774
  display spbm multicast-fib          | 任意视图             | L2872
  display spbm multicast-fib statistics | 任意视图             | L3040
  display spbm multicast-pw           | 任意视图             | L3244
  display spbm non-stop-routing event-log | 任意视图             | L3322
  display spbm non-stop-routing status | 任意视图             | L3468
  display spbm peer                   | 任意视图             | L3532
  display spbm summary                | 任意视图             | L4072
  display spbm unicast-fdb            | 任意视图             | L4206
  display spbm unicast-fib            | 任意视图             | L4302
  display spbm unicast-fib statistics | 任意视图             | L4460
  display spbm unicast-pw             | 任意视图             | L4628
  display spbm unicast-tree           | 任意视图             | L4706
  ect                                 | SPBM视图           | L4824
  flash-flood                         | SPBM视图           | L4884
  graceful-restart                    | SPBM视图           | L4932
  graceful-restart suppress-sa        | SPBM视图           | L4978
  graceful-restart t2                 | SPBM视图           | L5020
  is-name                             | SPBM视图           | L5070
  l2vpn enable                        | 系统视图             | L5112
  log-peer-change                     | SPBM视图           | L5148
  multicast replicate-mode            | VSI SPB视图        | L5186
  multicast-bvlan enable              | SPBM视图           | L5232
  non-stop-routing                    | SPBM视图           | L5292
  reset spbm bvlan-info statistics    | 用户视图             | L5338
  reset spbm database                 | 用户视图             | L5400
  reset spbm graceful-restart event-log | 用户视图             | L5434
  reset spbm multicast-fib statistics | 用户视图             | L5494
  reset spbm non-stop-routing event-log | 用户视图             | L5556
  reset spbm unicast-fib statistics   | 用户视图             | L5616
  set-overload                        | SPBM视图           | L5678
  snmp context-name                   | SPBM视图           | L5740
  snmp-agent trap enable spbm         | 系统视图             | L5790
  spb i-sid                           | VSI视图            | L5870
  spbm                                | 系统视图             | L5922
  spbm authentication send-only       | 二层以太网接口视图/二层聚合接口视图 | L5966
  spbm authentication-mode            | 二层以太网接口视图/二层聚合接口视图 | L6012
  spbm cost                           | 二层以太网接口视图/二层聚合接口视图 | L6078
  spbm enable                         | 二层以太网接口视图/二层聚合接口视图 | L6126
  spbm timer hello                    | 二层以太网接口视图/二层聚合接口视图 | L6172
  spbm timer holding-multiplier       | 二层以太网接口视图/二层聚合接口视图 | L6226
  spbm timer lsp                      | 二层以太网接口视图/二层聚合接口视图 | L6280
  spsource                            | SPBM视图           | L6330
  timer lsp-generation                | SPBM视图           | L6376
  timer lsp-max-age                   | SPBM视图           | L6428
  timer lsp-refresh                   | SPBM视图           | L6480
  timer spf                           | SPBM视图           | L6532
  vsi                                 | 系统视图             | L6584
-->

**SPBM \-- SPBM配置命令 \-- ap-mode**

------------------------------------------------------------------------

**[ap-mode**]命令用来配置AP协议的运行模式。

**[undo ap-mode**]命令用来恢复缺省情况。

【命令】

**[ap-mode **[{ **both** \| **multicast** \| **off** }]]

**[undo ap-mode**]

【缺省情况】

AP协议运行在both模式。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[both**]：表示对单播表项、组播表项都进行AP检测。

**[multicast**]：表示仅对组播表项进行AP检测。

**[off**]：表示关闭AP检测。

【使用指导】

·SPBN整网各节点独立收集拓扑信息，并进行独立计算。网络拓扑震荡时，各节点收敛速度可能不一致，导致各节点计算的速度不一致，网络瞬间可能形成环路。可通过AP协议来保证不出现临时环路。

·配置AP模式后，对应的表项在生效前需进行AP检测，检测通过（即链路状态数据库同步完成）后，才能指导转发，检测不通过则表项不生效。

【举例】

\# 配置AP协议运行在multicast模式。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm ap-mode multicast

**SPBM \-- SPBM配置命令 \-- area-authentication send-only**

------------------------------------------------------------------------

**[area-authentication send-only**]命令用来配置不对收到的报文（包括LSP、CSNP、PSNP）进行验证密码检查。

**[undo area-authentication send-only**]命令用来恢复缺省情况。

【命令】

**[area-authentication send-only**]

**[undo area-authentication send-only**]

【缺省情况】

如果配置了区域验证方式和验证密码，则对收到的报文进行验证密码检查。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置区域验证方式和验证密码时如果没有配置本命令，则在发送的报文（包括LSP、CSNP、PSNP）中按照**area-authentication-mode**命令指定的方式携带验证密码，并对收到的报文进行验证密码的检查，只有通过检查后，该报文中的路由信息才会加入到本地LSDB中。当需要更改密码时，由于两台设备的密码更改操作不完全同步，导致瞬时的密码不一致、业务中断。此时，可以通过配置不对收到的报文进行验证密码检查，保证业务不会中断。

【举例】

\# 配置不对收到的报文进行验证密码检查。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm area-authentication send-only

【相关命令】

·**area-authentication-mode**

**SPBM \-- SPBM配置命令 \-- area-authentication-mode**

------------------------------------------------------------------------

**[area-authentication-mode**]命令用来配置区域验证方式和验证密码。

**[undo area-authentication-mode**]命令用来恢复缺省情况。

【命令】

**[area-authentication-mode **[{ **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* }]]

**[undo area-authentication-mode**]

【缺省情况】

没有配置区域验证方式和验证密码，不进行区域验证。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

**[cipher**]：表示以密文的形式输入密码。

*[cipher-string*]：表示密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示以明文的形式输入密码。

*[plain-string*]：表示明文密码，为1～16个字符的字符串，区分大小写。

【使用指导】

配置区域验证方式和验证密码后，将在发送的报文（包括LSP、CSNP、PSNP）中按照设定的方式携带验证密码，并对收到的报文进行验证密码的检查。

需要注意的是：

·同一区域内的SPBM设备必须配置相同的验证方式和验证密码。

·以明文或密文方式配置的验证密码，均以密文的方式保存在配置文件中。

【举例】

\# 配置区域采用简单验证模式，验证密码为123456，以明文形式输入密码。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm area-authentication-mode simple plain 123456

【相关命令】

·**area-authentication send-only**

**SPBM \-- SPBM配置命令 \-- b-vlan**

------------------------------------------------------------------------

**[b-vlan**]命令用来为SPB VSI实例指定B-VLAN。

**[undo b-vlan**]命令用来恢复缺省情况。

【命令】

**[b-vlan ***vlan-id*]

**[undo b-vlan**]

【缺省情况】

SPB VSI实例未指定B-VLAN。

【视图】

VSI SPB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：VLAN编号，取值范围为1～4094。

【使用指导】

配置SPB VSI实例时必须为其指定B-VLAN，只有I-SID和B-VLAN都相同的SPB VSI实例才能互通。

需要注意的是，一个SPB VSI实例只能指定一个B-VLAN，不同SPB VSI实例可以指定相同的B-VLAN。

【举例】

\# 为SPB VSI实例vpn1（I-SID 256）指定B-VLAN 100。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 spb i-sid 256

Sysname-vsi-vpn1-256 b-vlan 100

**SPBM \-- SPBM配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

**[bandwidth-reference**]命令用来配置SPBM自动计算链路开销值时依据的带宽参考值。

**[undo** **bandwidth-reference**]命令用来恢复缺省情况。

【命令】

**[bandwidth-reference** *value*]

**[undo bandwidth-reference**]

【缺省情况】

SPBM自动计算链路度量值时依据的带宽参考值为40000Mbps。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：带宽参考值，取值范围为1～2147483648，单位为Mbps。

【使用指导】

当接口链路开销值和全局链路开销值都为缺省值时，SPBM会自动计算接口链路的开销值。

链路开销值的计算公式为"链路开销值＝（带宽参考值÷带宽）×10"，链路开销值的取值范围为1～16777214。

【举例】

\# 配置SPBM进程的带宽参考值为200Mbps。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm bandwidth-reference 200

【相关命令】

·**circuit-cost**

·**spbm cost**

**SPBM \-- SPBM配置命令 \-- bridge-priority**

------------------------------------------------------------------------

**[bridge-priority**]命令用来配置SPBM的桥优先级。

**[undo bridge-priority**]命令用来恢复缺省情况。

【命令】

**[bridge-priority ***priority*]

**[undo bridge-priority**]

【缺省情况】

SPBM的桥优先级为32768。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：表示SPBM的桥优先级，该数值越小表示优先级越高。取值范围为0～61440之间4096的倍数，如0、4096、8192等。

【使用指导】

SPBM的桥优先级与设备的System ID共同组成设备的桥ID。桥ID与ECT掩码进行异或操作，计算后的数值越小，则越优先选择该设备所在的转发路径来承载流量。

【举例】

\# 配置SPBM的桥优先级为4096。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm bridge-priority 4096

**SPBM \-- SPBM配置命令 \-- circuit-cost**

------------------------------------------------------------------------

**[circuit-cost**]命令用来全局配置SPBM的链路开销值。

**[undo circuit-cost**]命令用来恢复缺省情况。

【命令】

**[circuit-cost** *value*]

**[undo circuit-cost**]

【缺省情况】

未全局配置SPBM的链路开销值。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路开销值，取值范围为1～16777215。

【使用指导】

·链路开销值参与SPT（Shortest Path Tree，最短路径树）的计算。

·全局配置的SPBM链路开销值将对所有SPBM接口生效。

·全局和接口同时配置了SPBM的链路开销值时，优先选择接口的配置值。

【举例】

\# 全局配置SPBM的链路开销值为11。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm circuit-cost 11

【相关命令】

·**bandwidth-reference**

·**spbm cost**

**SPBM \-- SPBM配置命令 \-- control-address**

------------------------------------------------------------------------

**[control-address**]命令用来配置SPB IS-IS协议报文的控制MAC地址。

**[undo control-address**]命令用来恢复缺省情况。

【命令】

**[control-address**[ { **all-cb** \| **all-is** \| **all-l1-is** \| **all-l2-is** \| **all-pb** }]]

**[undo control-address**]

【缺省情况】

SPB IS-IS协议报文的控制MAC地址为**all-pb**，对应MAC地址为0180-C200-002E。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all-cb**]：SPB IS-IS协议报文的控制MAC地址为0180-C200-002F。

**[all-is**]：SPB IS-IS协议报文的控制MAC地址为0900-2B00-0005。

**[all-l1-is**]：SPB IS-IS协议报文的控制MAC地址为0180-C200-0014。

**[all-l2-is**]：SPB IS-IS协议报文的控制MAC地址为0180-C200-0015。

**[all-pb**]：SPB IS-IS协议报文的控制MAC地址为0180-C200-002E。

【举例】

\# 配置SPB IS-IS协议报文的控制MAC地址为**all-is**，对应MAC地址为0900-2B00-0005。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm control-address all-is

**SPBM \-- SPBM配置命令 \-- display l2vpn minm connection**

------------------------------------------------------------------------

**[display l2vpn minm connection**]命令用来显示MAC-in-MAC连接信息。

【命令】

**[display l2vpn minm connection ** **vsi** *vsi-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi*** vsi-name*]：显示指定VSI的MAC-in-MAC连接信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定该参数，则显示所有VSI的MAC-in-MAC连接信息。

【举例】

\# 显示所有VSI的MAC-in-MAC连接信息。

\<Sysname\> display l2vpn minm connection

Total number of MinM connections: 6

Types: MC - multicast, UC - unicast

VSI name: 1

Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface

64       10001     9999-8888-7777  1234   SPB     UC    GE1/0/1

65       10001     9999-8988-7777  1234   SPB     UC    GE1/0/1

-        10001     0011-2222-3333  1234   SPB     MC    GE1/0/1

VSI name: 2

Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface

68       10002     9999-8888-7777  1234   SPB     UC    GE1/0/1

69       10002     9999-8988-7777  1234   SPB     UC    GE1/0/1

-        10002     9999-9088-7777  1234   SPB     MC    GE1/0/1

                                                        GE1/0/2

表1-1 display l2vpn minm connection命令显示信息描述表

字段

描述

VSI name

VSI名称

Link ID

MAC-in-MAC连接的链路标识符

I-SID

骨干网服务实例编号

BMAC

骨干网MAC地址

BVLAN

骨干网VLAN

Owner

表项生成者，取值为PBB或SPB

Type

MAC-in-MAC连接的属性标记，取值包括：

·MC：组播表项

·UC：单播表项

Interface

出接口

**SPBM \-- SPBM配置命令 \-- display l2vpn minm forwarding**

------------------------------------------------------------------------

**[display l2vpn minm forwarding**]命令用来显示MAC-in-MAC转发表项信息。

【命令】

集中式设备：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ]

分布式设备―独立运行模式/集中式IRF设备：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ] **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display l2vpn minm forwarding ** **vsi** *vsi-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsi*** vsi-name*]：显示指定VSI的MAC-in-MAC转发表项信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定该参数，则显示所有VSI的MAC-in-MAC转发表项信息。

**[slot*** slot-number*]：显示指定单板上的MAC-in-MAC转发表项信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示主控板上的MAC-in-MAC转发表项信息。（分布式设备―独立运行模式）

**[slot*** slot-number*]：显示指定成员设备上的MAC-in-MAC转发表项信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示Master设备上的MAC-in-MAC转发表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX上的MAC-in-MAC转发表项信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的MAC-in-MAC转发表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备上指定单板的MAC-in-MAC转发表项信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示Master设备上主控板的MAC-in-MAC转发表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的MAC-in-MAC转发表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示Master设备上主控板的MAC-in-MAC转发表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的MAC-in-MAC转发表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的MAC-in-MAC转发表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有的MAC-in-MAC转发表项信息。

\<Sysname\> display l2vpn minm forwarding

Total number of MinM connections: 6

Types: MC - multicast, UC - unicast

Status Flag: \* - inactive

VSI name: 1

Link ID I-SID     BMAC            BVLAN Owner Type Interface

64      10001     9999-8888-7777  1234  SPB   UC   GE1/0/1

65      10001     9999-8988-7777  1234  SPB   UC   GE1/0/1

-       10001     0011-2222-3333  1234  SPB   MC   GE1/0/1

VSI name: 2

Link ID I-SID     BMAC            BVLAN Owner Type Interface

68      10002     9999-8888-7777  1234  SPB   UC   GE1/0/1

69      10002     9999-8988-7777  1234  SPB   UC   GE1/0/1

-       10002     9999-9088-7777  1234  SPB   MC   GE1/0/1

                                                   GE1/0/2

表1-2 display l2vpn minm forwarding命令显示信息描述表

字段

描述

VSI name

VSI名称

Link ID

MAC-in-MAC连接的链路标识符

I-SID

骨干网服务实例编号

BMAC

骨干网MAC地址

BVLAN

骨干网VLAN

Owner

表项生成者，取值为PBB或SPB

Type

属性标记，取值包括：

·MC：组播表项

·UC：单播表项

Interface

出接口

如果接口后面带有"\*"，则表示该表项不生效

**SPBM \-- SPBM配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

**[display l2vpn vsi**]命令用来显示VSI的信息。

【命令】

**[display**]**l2vpn****vsi** \****[name*** vsi-name* \**verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[name**]* vsi-name*：显示指定VSI的信息。*vsi-name*表示VSI的名称，为1～31个字符的字符串，区分大小写。如果未指定该参数，则显示所有VSI的信息。

**[verbose**]：显示VSI的详细信息。如果未指定该参数，则显示VSI的简要信息。

【举例】

\# 显示所有VSI的详细信息。

\<Sysname\> display l2vpn vsi verbose

VSI Name: 0

  VSI Index               : 0

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : -

  Drop Unknown            : Disabled

  SPB I-SID               : 10000

VSI Name: 1

  VSI Index               : 1

  VSI State               : Up

  MTU                     : 1500

  Bandwidth               : 102400 kbps

  Broadcast Restrain      : 5%

  Multicast Restrain      : 100%

  Unknown Unicast Restrain: 100%

  MAC Learning            : Enabled

  MAC Table Limit         : -

  Drop Unknown            : Disabled

  SPB I-SID               : 10001

  SPB Connections:

    BMAC            BVLAN            Link ID    Type

    9999-8888-7777  1234             64         Unicast

    9999-8988-7777  1234             65         Unicast

  ACs:

    AC                               Link ID    State

    BAGG1 srv1                       0          Down

表1-3 display l2vpn vsi命令显示信息描述表

字段

描述

VSI Name

VSI名称

VSI Index

VSI索引

VSI Description

VSI的描述信息，如果不配置，则此行不显示

VSI State

VSI的状态，取值包括

·Up：up状态

·Down：down状态

·Administratively down：通过**shutdown**命令手工关闭VSI

MTU

VSI上配置的最大传输单元

Bandwidth

VSI的带宽限制值，单位为kbps

Broadcast Restrain

VSI的广播抑制百分比。当VSI的广播流量速率超出特定值（带宽限制值×广播抑制百分比）时，该VSI会丢弃广播报文

Multicast Restrain

VSI的组播抑制百分比。当VSI的组播流量速率超出特定值（带宽限制值×组播抑制百分比）时，该VSI会丢弃组播报文

Unknown Unicast Restrain

VSI的未知单播抑制百分比。当VSI的未知单播流量速率超出特定值（带宽限制值×未知单播抑制百分比）时，该VSI会丢弃未知单播流量报文

MAC Learning

是否使能了MAC地址学习功能，取值包括：

·Enabled：使能了MAC地址学习功能

·Disabled：未使能MAC地址学习功能

MAC Tabel Limit

VSI内MAC地址表项的最大数目

取值为Unlimited，表示不限制VSI内MAC地址表项的最大数目

Drop Unknown

当VSI内学习到的MAC地址数达到最大值后，是否禁止转发源MAC地址不在MAC地址表里的报文，取值包括：

·Enabled：表示禁止转发

·Disabled：表示允许转发

Hub-Spoke

是否使能了Hub-spoke能力。取值为Enabled，表示使能了Hub-spoke能力；如果未使能Hub-spoke能力，则不显示该字段

Hub-spoke不适用于SPBM，SPBM不关心该字段取值

SPB I-SID

SPB骨干网服务实例编号

SPB Connections

SPB连接

BMAC

骨干网MAC地址

BVLAN

骨干网VLAN

Type

属性标记，取值包括：

·Multicast：组播表项

·Unicast：单播表项

ACs

VSI的AC列表

AC

接入电路，取值为二层接口名称和以太网服务实例，如GE1/0/1 srv1

Link ID

AC或PW在VSI内的链路ID

State

AC的状态，取值包括Up和Down

**SPBM \-- SPBM配置命令 \-- display spbm agreement-protocol**

------------------------------------------------------------------------

**[display spbm agreement-protocol**]命令用来显示指定接口上指定ECT算法的AP信息。

【命令】

**[display spbm agreement-protocol status interface** *interface-type interface-number* **ect** *ect-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的AP信息。*interface-type interface-number*表示接口类型和接口编号。

**[ect** *ect-number*]：ECT算法编号，取值范围为1～16。

【举例】

\# 显示接口GigabitEthernet1/0/1上ECT 1的AP信息。

\<Sysname\> display spbm agreement-protocol status interface gigabitethernet 1/0/1 ect 1

Port AP information:

TxDigest : 00000000000000000000000000003f1f5e5270ce

RxDigest : 00000000000000000000000000003f1f5e5270ce

NBRAPMode: Both

TxAN     : 1                     TxDAN    : 0

RxAN     : 0                     RxDAN    : 0

TxValid  : No                    RxValid  : No

MisOrder : No                    TopoAgree: Yes

CalcEnd  : Yes                   AgreeSend: Normal

Port SPT AP information:

SystemID : 0011.2200.0001

Role     : ROOT             SelectedRole: ROOT

PSTState : 2                ReRoot      : No

Agree    : Yes              Agreed      : Yes

Sync     : No               Synced      : Yes

Forward  : Yes              Forwarding  : Yes

Port SPT AP information:

SystemID : 0011.2200.0101

Role     : DESI             SelectedRole: DESI

PSTState : 2                ReRoot      : No

Agree    : Yes              Agreed      : Yes

Sync     : No               Synced      : Yes

Forward  : Yes              Forwarding  : Yes

表1-4 display spbm agreement-protocol命令显示信息描述表

字段

描述

TxDigest

本地摘要

RxDigest

邻居摘要

NBRAPMode

邻居AP模式：

·Both：表示对单播表项、组播表项都进行AP检测

·Multicast：表示仅对组播表项进行AP检测

·Off：表示AP模式关闭

TxAN

本地的一致号

TxDAN

本地的丢弃一致号

RxAN

邻居的一致号

RxDAN

邻居的丢弃一致号

TxValid

本地摘要是否可用

RxValid

邻居摘要是否可用

MisOrder

摘要报文乱序标记

TopoAgree

拓扑一致标记

CalcEnd

拓扑计算是否结束标记

AgreeSend

发送摘要报文的状态：

·Normal：普通发送

·Fast：快速发送

SystemID

端口所在树的树根的System ID

Role

端口在树上当前的角色：

·ROOT：根端口

·ALTE：可选端口

·DESI：指定端口

SelectedRole

端口在树上新计算出的角色：

·ROOT：根端口

·ALTE：可选端口

·DESI：指定端口

PSTState

端口的PST状态

ReRoot

端口是否需要重启

Agree

端口是否需要发送一致标记

Agreed

端口是否已经发送一致标记

Sync

端口是否进行同步

Synced

端口是否已经同步

Forward

端口是否要迁移到转发状态

Forwarding

端口当前是否处于转发状态

**SPBM \-- SPBM配置命令 \-- display spbm b-vlan**

------------------------------------------------------------------------

**[display spbm b-vlan**]命令用来显示SPBM B-VLAN的ECT算法应用情况。

【命令】

**[display spbm b-vlan** [ *vlan-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vlan-id*]：显示指定B-VLAN的ECT算法应用情况，*vlan-id*取值范围为1～4094。如果未指定该参数，则显示所有B-VLAN的ECT算法应用情况。

【举例】

\# 显示所有B-VLAN的ECT算法应用情况。

\<Sysname\> display spbm b-vlan

B-VLAN 1:

  Mode: SPBM

  Local use: Yes      Remote use: No

  ECT-Index：1        Algorithm: 00-80-c2-01  Mask: 0x00

  I-SID list: 300-302, 305, 309

B-VLAN 2:

  Mode: SPBM

  Local use: Yes      Remote use: No

  ECT-Index：1        Algorithm: 00-80-c2-01  Mask: 0x00

  I-SID list: 400-402, 404

表1-5 display spbm b-vlan命令显示信息描述表

字段

描述

Mode

系统使用的模式

Local use

本地B-VLAN是否承载流量：

·Yes：表示本地B-VLAN承载流量

·No：表示本地B-VLAN不承载流量

Remote use

远端B-VLAN是否承载流量：

·Yes：表示远端B-VLAN承载流量

·No：表示远端B-VLAN不承载流量

ECT-Index

ECT索引

Algorithm

ECT算法

Mask

ECT算法对应的掩码

I-SID list

本地B-VLAN上承载的I-SID，N/A表示无承载I-SID

**SPBM \-- SPBM配置命令 \-- display spbm bridge**

------------------------------------------------------------------------

**[display spbm bridge**]命令用来显示SPBM的桥信息。

【命令】

**[display spbm bridge**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SPBM的桥信息。

\<Sysname\> display spbm bridge

System ID            Priority    SPSource ID    Host name

5555.1111.1111       32768       128            SPB-1

表1-6 display spbm bridge命令显示信息描述表

字段

描述

System ID

系统ID

Priority

桥优先级

SPSource ID

最短路径源ID

Host name

主机名，设备未配置主机名则显示对应的系统ID

**SPBM \-- SPBM配置命令 \-- display spbm bvlan-info**

------------------------------------------------------------------------

**[display** **spbm** **bvlan-info**]用来显示SPBM B-VLAN信息。

【命令】

集中式设备：

**[display** **spbm bvlan-info**]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **spbm bvlan-info** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display** **spbm** **bvlan-info** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的B-VLAN信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的B-VLAN信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的B-VLAN信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的B-VLAN信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的B-VLAN信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的B-VLAN信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的B-VLAN信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的B-VLAN信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的B-VLAN信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的B-VLAN信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的B-VLAN信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的B-VLAN信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示SPBM B-VLAN信息。

\<Sysname\> display spbm bvlan-info

Epoch: 0x1

Config B-VLAN list:

  1-7, 20

Driver B-VLAN list:

  1

表1-7 display spbm bvlan-info命令显示信息描述表

字段

描述

Epoch

B-VLAN时间戳

Config B-VLAN list

映射到MSTI 4092的B-VLAN列表（已通过激活MST域的配置使映射关系生效）

Driver B-VLAN list

下发驱动的B-VLAN列表

**SPBM \-- SPBM配置命令 \-- display spbm bvlan-info statistics**

------------------------------------------------------------------------

**[display spbm bvlan-info statistics**]命令用来显示SPBM B-VLAN统计信息。

【命令】

集中式设备：

**[display spbm bvlan-info** **statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm bvlan-info** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display spbm bvlan-info statistics** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的B-VLAN统计信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的B-VLAN统计信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的B-VLAN统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的B-VLAN统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的B-VLAN统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的B-VLAN统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的B-VLAN统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的B-VLAN统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的B-VLAN统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的B-VLAN统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的B-VLAN统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的B-VLAN统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示成员设备1上单板0的SPBM B-VLAN统计信息。

\<Sysname\> display spbm bvlan-info statistics chassis 1 slot 0

SPBM B-VLAN basic statistics:

RefreshMsg     : 1           AgeNumber        : 0

DrvAddNumber   : 1           DrvDeleteNumber  : 0

SPBM B-VLAN error statistics:

BVLANMsgError  : 0           BVLANCreatFail   : 0

DrvEnableFail  : 0           DrvDisableFail   : 0

AllocBVLANFail : 0

表1-8 display spbm bvlan-info statistics命令显示信息描述表

字段

描述

SPBM B-VLAN basic statistics

B-VLAN基础统计

RefreshMsg

刷新B-VLAN的消息计数

AgeNumber

B-VLAN老化计数

DrvAddNumber

通知驱动添加B-VLAN消息计数

DrvDeleteNumber

通知驱动删除B-VLAN消息计数

SPBM B-VLAN error statistics

B-VLAN错误统计

BVLANMsgError

收到B-VLAN错误消息计数

BVLANCreatFail

申请B-VLAN内存失败计数

DrvEnableFail

通知驱动B-VLAN生效失败计数

DrvDisableFail

通知驱动B-VLAN失效失败计数

AllocBVLANFail

分配B-VLAN失败计数

**SPBM \-- SPBM配置命令 \-- display spbm common statistics**

------------------------------------------------------------------------

**[display spbm common statistics**]命令用来显示SPBM公共统计信息。

【命令】

集中式设备：

**[display spbm common** **statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm common** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display spbm common statistics** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的SPBM公共统计信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的SPBM公共统计信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的SPBM公共统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的SPBM公共统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的SPBM公共统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的SPBM公共统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的SPBM公共统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的SPBM公共统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的SPBM公共统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的SPBM公共统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的SPBM公共统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的SPBM公共统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示SPBM公共统计信息。

\<Sysname\> display spbm common statistics

UMACReDRVCount    : 0           MMACReDRVCount      : 0

ActiveFail        : 0           AllocMsgFail        : 0

RTMsgTypeError    : 0           WriteQueFail        : 0

SyncRTMsgFail     : 0           CommMsgTypeError    : 0

ComQueMsgTypeError: 0           TimerQueMsgTypeError: 0

EpochNumber       : 0           GetBMACNumber       : 1

GetBMACFail       : 0           SetIfNumber         : 6

AgeIfNumber       : 0           SetIfErrNumber      : 0

表1-9 display spbm common statistics命令显示信息描述表

字段

描述

UMACReDRVCount

单播表项重新下发驱动计数

MMACReDRVCount

组播表项重新下发驱动计数

ActiveFail

备板变主板失败

AllocMsgFail

申请内存失败

RTMsgTypeError

错误的路由消息类型

WriteQueFail

外部消息写队列失败

SyncRTMsgFail

路由消息同步失败

CommMsgTypeError

错误的消息类型

ComQueMsgTypeError

错误的队列类型

TimerQueMsgTypeError

定时器队列消息类型错误

EpochNumber

全局老化计数，当表项的时间戳小于该值时，则表项需要老化

GetBMACNumber

获取驱动B-MAC计数

GetBMACFail

获取驱动B-MAC失败

SetIfNumber

接口下发驱动使能数目

AgeIfNumber

接口老化计数

SetIfErrNumber

接口下发驱动失败使能数目

**SPBM \-- SPBM配置命令 \-- display spbm ect**

------------------------------------------------------------------------

**[display spbm ect**]命令用来显示ECT算法信息以及使用对应ECT算法的B-VLAN。

【命令】

**[display spbm ect** [ *ect-index* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ect-index*]：ECT算法索引，取值范围为1～16。如果未指定该参数，则显示所有的ECT算法信息以及使用对应ECT算法的B-VLAN。

【举例】

\# 显示所有的ECT算法信息。

\<Sysname\> display spbm ect

ECT-1:

    Algorithm: 00-80-c2-01     Mask: 0x00

    Active B-VLANs: 1-10

    Inactive B-VLANs: 31-4094

ECT-2:

    Algorithm: 00-80-c2-02     Mask: 0xff

    Active B-VLANs: 11-20

    Inactive B-VLANs: 21-30

ECT-3:

    Algorithm: 00-80-c2-03     Mask: 0x88

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-4:

    Algorithm: 00-80-c2-04     Mask: 0x77

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-5:

    Algorithm: 00-80-c2-05     Mask: 0x44

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-6:

    Algorithm: 00-80-c2-06     Mask: 0x33

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-7:

    Algorithm: 00-80-c2-07     Mask: 0xcc

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-8:

    Algorithm: 00-80-c2-08     Mask: 0xbb

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-9:

    Algorithm: 00-80-c2-09     Mask: 0x22

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-10:

    Algorithm: 00-80-c2-0a     Mask: 0x11

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-11:

    Algorithm: 00-80-c2-0b     Mask: 0x66

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-12:

    Algorithm: 00-80-c2-0c     Mask: 0x55

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-13:

    Algorithm: 00-80-c2-0d     Mask: 0xaa

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-14:

    Algorithm: 00-80-c2-0e     Mask: 0x99

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-15:

    Algorithm: 00-80-c2-0f     Mask: 0xdd

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

ECT-16:

    Algorithm: 00-80-c2-10     Mask: 0xee

    Active B-VLANs: N/A

    Inactive B-VLANs: N/A

表1-10 display spbm ect命令显示信息描述表

字段

描述

Algorithm

ECT算法

Mask

ECT算法对应的掩码

Active B-VLANs

配置在该ECT算法下的生效B-VLAN，N/A表示该ECT算法下不存在生效B-VLAN

Inactive B-VLANs

配置在该ECT算法下无效B-VLAN，N/A表示该ECT算法下不存在无效B-VLAN

**SPBM \-- SPBM配置命令 \-- display spbm ect-migration**

------------------------------------------------------------------------

**[display spbm ect-migration**]命令用来显示指定I-SID的ECT迁移相关信息。

【命令】

**[display spbm ect-migration i-sid** *i-sid*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[i-sid*]：指定的I-SID值，取值范围为255～16777215。

【举例】

\# 显示I-SID 300的ECT迁移相关信息。

\<Sysname\> display spbm ect-migration i-sid 300

ECT            B-VLAN    T    R

00-80-c2-01    1         0    1

表1-11 display spbm ect-migration命令显示信息描述表

字段

描述

ECT

ECT算法

B-VLAN

该I-SID映射的B-VLAN

T

T标志是否置位定义了设备在I-SID对应组播组中的传输状态：

·1：置位，表示该设备是传输者。如果采用核心复制，BEB将T标志置位

·0：未置位，表示该设备不是传输者。如果采用头端复制，BEB不将T标志置位

R

R标志是否置位定义了设备在I-SID对应组播组中的接收状态：

·1：置位，表示该设备是接收者

·0：未置位，表示该设备不是接收者

**SPBM \-- SPBM配置命令 \-- display spbm fast-channel statistics**

------------------------------------------------------------------------

**[display spbm fast-channel statistics**]命令用来显示LSP快速泛洪通道的相关统计信息。

【命令】

**[display spbm fast-channel statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示LSP快速泛洪通道的相关统计信息。

\<Sysname\> display spbm fast-channel statistics

                   Fast channel information for SPBM

                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

VSI name              : 1

B-VLAN                : 1

I-SID                 : 255

State                 : Active

Replication mode      : tandem

ECT algorithm         : 00-80-c2-01

LSPs sent count       : 10

LSPs received count   : 20

LSP timer             : 10

LSPs transmitted count: 10

表1-12 display spbm fast-channel statistics命令显示信息描述表

字段

描述

VSI name

VSI名称

B-VLAN

骨干网VLAN

I-SID

骨干网服务实例编号

State

快速泛洪通道状态，取值为：

·Active：表示快速泛洪通道可用

·Inactive：表示快速泛洪通道不可用

Replication mode

组播复制模式，取值为：

·head-end：表示头端复制模式

·tandem：表示核心复制模式

ECT algorithm

B-VLAN对应的ECT算法

LSPs sent count

通过快速泛洪通道发送LSP的个数

当发生以下任意一种情况时，本字段清零：

·执行**reset spbm database**命令

·I-SID为255的SPB VSI实例down

·进行进程分布优化。有关进程分布优化的详细介绍，请参见"可靠性配置指导"中的"进程分布优化"

LSPs received count

通过快速泛洪通道接收的LSP个数

当发生以下任意一种情况时，本字段清零：

·执行**reset spbm database**命令

·I-SID为255的SPB VSI实例down

·进行进程分布优化

LSP timer

快速泛洪通道发送LSP的最小时间间隔，单位为毫秒。不可配

LSPs transmitted count

快速泛洪通道一次最多可以发送的LSP个数。不可配

**SPBM \-- SPBM配置命令 \-- display spbm graceful-restart event-log**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display spbm graceful-restart event-log**]命令用来显示SPBM GR日志信息。

【命令】

集中式设备：

**[display spbm graceful-restart event-log**]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm graceful-restart event-log** **slot** *slot-number*]

分布式设备－IRF模式：

**[display spbm graceful-restart event-log chassis** *chassis-number* **slot** *slot-number*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot**]* slot-number*：显示指定单板的SPBM GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的SPBM GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的SPBM GR日志信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定成员设备上指定单板的SPBM GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定单板的SPBM GR日志信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示成员设备0的SPBM GR日志信息。（集中式IRF设备）

\<Sysname\> display spbm graceful-restart event-log slot 0

SPBM log information:

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Initialization).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSDB synchronization).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSP stability).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSP generation).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (SPF computation).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Flush smooth).

Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Finish).

Aug 22 08:21:17 2013 -Slot=0 GR complete.

\# 显示单板1的SPBM GR日志信息。（分布式设备－独立运行模式）

\<Sysname\> display spbm graceful-restart event-log slot 1

SPBM log information:

Oct  5 12:54:53 2013 -Slot=1 HA backup channel was blocked.

Oct  5 12:54:56 2013 -Slot=1 HA backup channel was unblocked.

\# 显示单板2的SPBM GR日志信息。（分布式设备－独立运行模式）

\<Sysname\> display spbm graceful-restart event-log slot 2

SPBM log information:

Oct  6 15:50:56 2013 -Slot=2 Memory restore on the standby MPU triggered data batch backup.

表1-13 display spbm graceful-restart event-log命令显示信息描述表

字段

描述

Initialization

进入GR的初始化阶段

LSDB synchronization

进入GR的T2同步阶段

LSP stability

进入LSP稳定阶段

LSP generation

进入LSP生成阶段

SPF computation

进入路由计算阶段

Flush smooth

进入内核数据平滑阶段

Finish

进入GR的结束阶段

GR complete

完成GR

HA backup channel was blocked

降级（主进程变为备进程）过程中进入实时备份和批量备份通道阻塞状态

HA backup channel was unblocked

降级结束退出实时备份和批量备份通道阻塞状态

Memory restore on the standby MPU triggered data batch backup

备板内存恢复之后，会主动触发一次数据批量备份请求

【相关命令】

·**reset spbm graceful-restart event-log**

**SPBM \-- SPBM配置命令 \-- display spbm graceful-restart status**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display spbm graceful-restart status**]命令用来显示SPBM GR状态信息。

【命令】

**[display spbm graceful-restart status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SPBM GR状态信息。

\<Sysname\> display spbm graceful-restart status

                         Restart information for SPBM

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Restart status             : Restarting

Restart phase              : LSDB synchronization

Restart interval           : 300

SA bit                     : Supported

Total number of interfaces : 2

Number of waiting LSPs     : 3

T2 remaining time          : 41

Interface      T1 remaining time  RA received  CSNP received  T1 expirations

GE1/0/1        2                  Y            N              2

GE1/0/2        2                  Y            N              2

![说明](SPBM命令.files/image003.png)

本命令的显示信息与设备的型号有关，请以设备的实际情况为准。

表1-14 display spbm graceful-restart status命令显示信息描述表

字段

描述

Restart status

当前设备的Restart状态：

·Restarting：主备倒换、保留FIB的过程。该状态下能保证进行转发

·Starting：对于不保留FIB的主备倒换或设备重启后进入的状态。该状态下不能保证转发

·Complete：完成GR

Restart phase

当前设备的Restart阶段：

·Initialization：GR初始

·LSDB synchronization：LSDB同步

·LSP stability：本地LSP稳定阶段

·LSP generation：LSP生成和泛洪

·First SPF computation：第一次拓扑计算

·Finish：完成

Restart Interval

设备预期完成重启的时间间隔，单位为秒，在该时间间隔内邻居不会断掉与重启设备的邻接关系

SA bit

设备是否支持SA：

·Supported：支持，SA位置位为1，重启设备的邻居不会发布与重启设备的邻接关系

·Not supported：不支持，SA位清空为0，重启设备的邻居会继续发布与重启设备的邻接关系

Total number of interfaces

当前使能SPBM的接口数

Number of waiting LSPs

GR Restarter从GR Helper进行LSDB同步时，未完成同步的LSP数目

T2 remaining time

T2定时器剩余的时间，单位为秒，T2定时器用来控制LSDB的同步时间

Interface

接口名称

T1 remaining time

接口上T1定时器剩余的时间，单位为秒，T1定时器用来控制带RR标志位的Hello报文的重传时间

RA received

接口上是否收到邻居发送的带RA标志位的Hello报文

CSNP received

接口上是否收到完整的CSNP报文，即是否完成与GR Helper的LSDB同步

T1 expirations

T1定时器的超时次数，超时达到10次后，不会再进行带RR标志位的Hello报文的重传

**SPBM \-- SPBM配置命令 \-- display spbm interface**

------------------------------------------------------------------------

**[display spbm interface**]命令用来显示使能SPBM功能接口的信息。

【命令】

**[display spbm interface** [ *interface-type interface-number*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[interface-type interface-number*]：显示指定接口的信息。*interface-type interface-number*表示接口类型和接口编号。如果未指定该参数，则显示所有使能SPBM功能接口的信息。

**[verbose**]：显示接口的详细信息。如果未指定该参数，则显示接口的简要信息。

【举例】

\# 显示使能SPBM功能的接口的简要信息。

\<Sysname\> display spbm interface

                        Interface information for SPBM

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface                   Circuit ID    State     MTU      Cost

GE1/0/1                     1             Up        1497     10

GE1/0/2                     2             Up        1497     100

\# 显示使能SPBM功能的接口的详细信息。

\<Sysname\> display spbm interface verbose

                        Interface information for SPBM

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface                   Circuit ID    State     MTU      Cost

GE1/0/1                     1             Up        1497     10

Hello timer           : 10

Hello multiplier      : 3

LSP timer             : 33

LSP transmitted count : 5

Interface                   Circuit ID    State     MTU      Cost

GE1/0/2                     2             Up        1497     100

Hello timer           : 10

Hello multiplier      : 3

LSP timer             : 33

LSP transmitted count : 5

\# 显示接口GigabitEthernet1/0/1的详细信息。

\<Sysname\> display spbm interface gigabitethernet 1/0/1 verbose

                        Interface information for SPBM

                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Interface                   Circuit ID    State     MTU      Cost

GE1/0/1                     1             Up        1497     10

Hello timer           : 10

Hello multiplier      : 3

LSP timer             : 33

LSP transmitted count : 5

表1-15 display spbm interface显示信息描述表

字段

描述

Interface

接口名

Circuit ID

电路ID

State

接口状态

MTU

接口MTU值

Cost

接口的链路开销值

Hello timer

Hello报文发送时间间隔，单位为秒

Hello multiplier

Hello报文失效数目

LSP timer

发送LSP的最小时间间隔，单位为毫秒

LSP transmitted count

发送LSP的数目

**SPBM \-- SPBM配置命令 \-- display spbm lsdb**

------------------------------------------------------------------------

**[display spbm lsdb**]命令用来显示SPBM链路状态数据库中的LSP信息。

【命令】

**[display spbm lsdb**[ [ [ **lsp-id** *lspid* \| **lsp-name** *lspname* ] \| **local** \| **verbose** ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[lsp-id*** lspid*]：LSP标识，形式为*SYSID.Pseudonode ID-fragment num*，其中，*SYSID*是产生该LSP的节点的System ID，*Pseudonode ID*是伪节点ID，*fragment num*是该LSP的分片号。如果未指定该参数，则显示链路状态数据库中所有LSP标识对应的LSP信息。

**[lsp-name*** lspname*]：LSP名称，形式为*Symbolic name-fragment num*，其中，*Symbolic name*是产生该LSP的节点名称，*fragment num*是该LSP的分片号。如果未指定该参数，则显示链路状态数据库中所有LSP名称对应的LSP信息。

**[local**]：显示本设备产生的所有LSP的信息。如果未指定该参数，则显示链路状态数据库中所有设备产生的LSP信息。

**[verbose**]：显示链路状态数据库中的LSP详细信息。如果未指定该参数，则显示链路状态数据库中的LSP摘要信息。

【使用指导】

如果未指定任何参数，则显示链路状态数据库中的所有LSP信息。

【举例】

\# 显示SPBM链路状态数据库中的LSP摘要信息。

\<Sysname\> display spbm lsdb

                         Database information for SPBM

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSP ID: \* - Local LSP

LSP ID                Seq Num      Checksum      Holdtime      Length  Overload

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

4455.6677.0001.00-00  0x00000fd2   0x1cea        1044          236     0

4455.6677.0001.00-01  0x00000fd2   0x1cea        1044          256     0

4455.6677.0003.00-00\* 0x00001448   0x3d27        683           323     0

4455.6677.0003.00-01\* 0x00001448   0xbd27        683           723     0

4455.6677.0004.00-00  0x00000ff8   0xd1d9        1090          323     0

4455.6677.0004.00-01  0x00000ff8   0xd7d9        1090          329     0

\# 显示SPBM链路状态数据库中的LSP详细信息。

\<Sysname\> display spbm lsdb verbose

                         Database information for SPBM

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

LSP ID: \* - Local LSP

LSP ID                Seq Num      Checksum      Holdtime      Length  Overload

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0011.2200.0001.00-00  0x0000000e   0x29ef        429           69      0

System ID           : 0011.2200.0001

NLPID               : SPBM

Area address        : 00.0000

MT capability TLV   :

 MT ID       : 00

 MT overload : 0

 SPB instance sub-TLV:

   CIST root identifier : 0000-0000-0000-0000

   CIST ERPC            : 0

   Bridge priority      : 32768

   SPSourceID           : 100

   Number of trees      : 1

     B-VLAN: 10      U-Bit: 1    ECT: 00-80-c2-01    SPVID: 0

0011.2200.0001.00-01  0x0000000f   0x209e        1190          66      0

System ID           : 0011.2200.0001

Hostname            : 0011.2200.0001.00

MT capability TLV   :

 MT ID       : 00

 MT overload : 0

 SPBM Service Identifier and Unicast Address sub-TLV:

   B-MAC     : 0011-2200-0001

   B-VLAN    : 10

     I-SID   : 300(R)

Extended neighbor reachability TLV:

 Hostname    : 0011.2200.0101.00

 Cost        : 11

 Port number : 1

0011.2200.0101.00-00\* 0x00000002   0x3846        1190          69      0

System ID           : 0011.2200.0101

NLPID               : SPBM

Area address        : 00.0000

MT capability TLV   :

 MT ID       : 00

 MT overload : 0

 SPB instance sub-TLV:

   CIST root identifier : 0000-0000-0000-0000

   CIST ERPC            : 0

   Bridge priority      : 32768

   SPSourceID           : 10

   Number of Trees      : 1

     B-VLAN: 10      U-Bit: 1    ECT: 00-80-c2-01    SPVID: 0

0011.2200.0101.00-01\* 0x00000002   0xfdcd        1190          66      0

System ID           : 0011.2200.0101

Hostname            : 0011.2200.0101.00

MT capability TLV   :

 MT ID       : 00

 MT overload : 0

 SPBM Service Identifier and Unicast Address sub-TLV:

   B-MAC     : 0011-2200-0101

   B-VLAN    : 10

     I-SID   : 300(R)

     I-SID   : 301(T&R)

Extended neighbor reachability TLV:

 Hostname    : 0011.2200.0001.00

 Cost        : 10

 Port number : 1

表1-16 display spbm lsdb命令显示信息描述表

字段

描述

LSP ID

链路状态报文ID，\*表示本地LSP

Seq Num

LSP序列号

Checksum

LSP校验和

Holdtime

LSP生存时间，单位为秒

Length

LSP长度

Overload

LSP中Overload的置位情况：

·1：表示置位

·0：表示没有置位

System ID

LSP生成设备的System ID

NLPID

LSP生成设备运行的协议

Area address

LSP生成设备的区域地址

MT capability TLV

多拓扑能力TLV

MT ID

多拓扑ID

MT overload

多拓扑能力TLV中overload的置位情况：

·1：表示置位

·0：表示没有置位

SPB instance sub-TLV

SPB实例子TLV

CIST root identifier

CIST根标识

CIST ERPC

CIST外部根路径开销

Bridge priority

桥优先级

SPSourceID

最短路径源ID

Number of trees

ECT算法与Base VID元组数目

B-VLAN

B-VLAN

U-Bit

该B-VLAN是否承载流量：

·1：表示承载

·0：表示不承载

ECT

ECT算法

SPVID

SPBV标记

SPBM Service Identifier and Unicast Address sub-TLV

SPBM服务实例和单播地址子TLV

B-MAC

骨干网MAC地址

B-VLAN

骨干网VLAN

I-SID

I-SID值及标记：

·T：Transmit位置位

·R：Receive位置位

Extended neighbor reachability TLV

扩展邻居可达TLV

Hostname

主机名，如果主机未配置则显示设备的System ID

Cost

链路开销

Port number

邻居建立的端口个数

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fdb**

------------------------------------------------------------------------

**[display spbm multicast-fdb**]命令用来显示SPBM的组播FDB表项信息。

【命令】

**[display spbm multicast-fdb****\**[b-vlan**[ *vlan-id* \| **i-sid** *i-sid* \| **system-id** *system-id* ]]]

**[display spbm multicast-fdb****\**[b-vlan** *vlan-id*  **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[b-vlan*** vlan-id*]：显示指定B-VLAN的组播FDB表项信息，*vlan-id*取值范围为1～4094。如果未指定该参数，则显示所有B-VLAN的组播FDB表项信息。

**[i-sid** *i-sid*]：显示指定I-SID的组播FDB表项信息，*i-sid*取值范围为255～16777215。如果未指定该参数，则显示所有I-SID的组播FDB表项信息。

**[system-id*** system-id*]：显示指定System ID的组播FDB表项信息，*system-id*的格式为XXXX.XXXX.XXXX。如果未指定该参数，则显示所有System ID的组播FDB表项信息。

**[count**]：显示组播FDB表项计数。

【使用指导】

如果**b-vlan*** vlan-id*、**i-sid** *i-sid*和**system-id*** system-id*三个参数都未指定，则显示所有的SPBM组播FDB表项信息。

【举例】

\# 显示所有的SPBM组播FDB表项信息。

\<Sysname\> display spbm multicast-fdb

Flags: E-Egress T-Transit

System ID            MAC address      B-VLAN   Flags Port

0011.2200.de01       9334-6900-03e8   7        T     GE1/0/2

0011.2200.de01       9334-6900-0190   4        T     GE1/0/2

0011.2200.de01       9334-6900-01f4   5        T     GE1/0/2

\# 显示所有的SPBM组播FDB表项计数。

\<Sysname\> display spbm multicast-fdb count

Total entries: 2

表1-17 display spbm multicast-fdb命令显示信息描述表

字段

描述

System ID

系统ID

MAC address

组播MAC地址

B-VLAN

组播MAC地址对应接口所属的B-VLAN

Flags

报文转发标志：

·E：表示出隧道

·T：表示转发

如果字段显示为两个转发标志的组合，如TE，则表示两个报文转发动作都有发生

Port

出端口，N/A表示没有出端口

Total entries

组播FDB表项计数

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fib**

------------------------------------------------------------------------

**[display spbm multicast-fib**]命令用来显示SPBM组播FIB表项信息。

【命令】

集中式设备：

**[display spbm multicast-fib** [ **mac-address** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **verbose** ]]

**[display spbm multicast-fib** [ **b-vlan** *vlan-id*  **count**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm multicast-fib** [ **mac-address** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

**[display spbm multicast-fib** [ **b-vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **count**]]

分布式设备－IRF模式：

**[display spbm multicast-fib** [ **mac-address** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

**[display spbm multicast-fib** [ **b-vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[mac-address*** mac-address*]：显示指定MAC地址的组播FIB表项信息，*mac-address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。如果未指定该参数，则显示所有B-MAC的组播FIB表项信息。

**[b-vlan*** vlan-id*]：显示指定B-VLAN的组播FIB表项信息，*vlan-id*取值范围为1～4094。如果未指定该参数，则显示所有B-VLAN的组播FIB表项信息。

**[mac-address*** mac-address* **b-vlan** *vlan-id*]：显示指定MAC地址及B-VLAN的组播FIB表项信息。如果未指定该参数，则显示所有组播FIB表项信息。

**[verbose**]：显示组播FIB表项的详细信息。如果未指定该参数，则显示组播FIB表项的简要信息。

**[slot*** slot-number*]：显示指定单板的组播FIB表项信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的组播FIB表项信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的组播FIB表项信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的组播FIB表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的组播FIB表项信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的组播FIB表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的组播FIB表项信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的组播FIB表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的组播FIB表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的组播FIB表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的组播FIB表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的组播FIB表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示所有的SPBM组播FIB表项信息。

\<Sysname\> display spbm multicast-fib

Flags: E-Egress T-Transit

MAC address    B-VLAN Flags Port

0300-0b00-0001 1      TE    GE1/0/2

\# 显示所有的SPBM组播FIB表项的详细信息。

\<Sysname\> display spbm multicast-fib verbose

Flags: E-Egress T-Transit

MAC address    B-VLAN Flags Epoch       Port                     Port flag

0300-0b00-0001 1      TE    0x1         GE1/0/2                  Done

\# 显示MAC地址为0300-0b00-0001、B-VLAN为1的SPBM组播FIB表项的详细信息。

\<Sysname\> display spbm multicast-fib mac-address 0300-0b00-0001 b-vlan 1 verbose

MAC address: 0300-0b00-0001    B-VLAN     : 1

Flags  : TE                 Driver flag: Done         Epoch: 0x1

Context: 0xffffffff 0xffffffff 0xffffffff 0xffffffff

Port                     Context                 Port flag

GE1/0/2                  0xffffaaaa  0xffffaaaa  Done

GE1/0/1                  0xffffaaaa  0xffffbbbb  Done

\# 显示B-VLAN 100的SPBM组播FIB表项计数。

\<Sysname\> display spbm multicast-fib b-vlan 100 count

Total entries: 3

表1-18 display spbm multicast-fib命令显示信息描述表

字段

描述

MAC address

SPBM组播转发的MAC地址

B-VLAN

SPBM组播转发的VLAN

Flags

报文转发标志：

·E：表示出隧道

·T：表示转发

如果字段显示为两个转发标志的组合，如TE，则表示两个报文转发动作都有发生

Driver flag

下发驱动标记：

·Nores：下发驱动资源不足，此时该表项不可用

·Done：下发驱动成功

Epoch

表项的时间戳

Context

保存SPBM FDB表项下发驱动后返回的驱动信息

Port

出端口，其中N/A表示无出端口

Context

出端口对应的驱动信息

Port flag

端口下发驱动标记：

·Nores：下发驱动资源不足

·Done：下发驱动成功

·N/A：端口未下发驱动

Total entries

SPBM组播FIB表项计数

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fib statistics**

------------------------------------------------------------------------

**[display spbm multicast-fib statistics**]命令用来显示SPBM组播FIB表项统计信息。

【命令】

集中式设备：

**[display spbm multicast-fib** **statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm multicast-fib** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display spbm multicast-fib statistics** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的组播FIB表项统计信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的组播FIB表项统计信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的组播FIB表项统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的组播FIB表项统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的组播FIB表项统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的组播FIB表项统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的组播FIB表项统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的组播FIB表项统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的组播FIB表项统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的组播FIB表项统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的组播FIB表项统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的组播FIB表项统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示成员设备1上单板0的SPBM组播FIB表项统计信息。

\<Sysname\> display spbm multicast-fib statistics chassis 1 slot 0

SPBM multicast FIB basic statistics:

RefreshMsg      : 0           DeleteMsg        : 0

AddIfMsg        : 1           DeleteIfMsg      : 0

AddMMACNumber   : 1           DeleteMMACNumber : 0

DeleteNotFound  : 0           AgeNumber        : 0

DrvAdd          : 1           DrvDelete        : 0

DrvAddIf        : 0           DrvDeleteIf      : 0

DrvModifyFlag   : 0

SPBM multicast FIB error statistics:

MMACMsgError    : 0           RefreshMsgFail   : 0

DeleteMsgFail   : 0           AddIfMsgFail     : 0

DeleteIfMsgFail : 0           AddMMACFail      : 0

DrvOtherFail    : 0           DrvDeleteFail    : 0

DrvNoResource   : 0           SynMsgFail       : 0

AllocEntryFail  : 0           AllocReDrvMsgFail: 0

AllocDrvMsgFail : 0

表1-19 display spbm multicast-fib statistics命令显示信息描述表

字段

描述

SPBM multicast FIB basic statistics

SPBM组播转发表基础统计信息

RefreshMsg

添加组播表项消息计数

DeleteMsg

组播组播表项删除消息计数

AddIfMsg

添加出接口消息计数

DeleteIfMsg

删除出接口消息计数

AddMMACNumber

创建组播MAC地址计数

DeleteMMACNumber

删除组播MAC地址计数

DeleteNotFound

删除时，查找不到合适的组播MAC地址计数

AgeNumber

当前启动老化状态时老化表项的个数

DrvAdd

添加驱动表项计数

DrvDelete

删除驱动表项计数

DrvAddIf

驱动表项增加出接口计数

DrvDeleteIf

驱动表项删除出接口计数

DrvModifyFlag

驱动表项修改转发标记计数

SPBM multicast FIB error statistics

SPBM组播转发表错误统计信息

MMACMsgError

无效的表项消息计数

RefreshMsgFail

组播MAC地址添加消息处理失败计数

DeleteMsgFail

组播MAC地址删除消息处理失败计数

AddIfMsgFail

组播MAC地址添加出接口消息处理失败计数

DeleteIfMsgFail

组播MAC地址删除出接口消息处理失败计数

AddUMACFail

创建组播MAC地址表项失败计数

DrvOtherFail

组播MAC地址修改转发标记消息处理失败计数

DrvDeleteFail

组播MAC地址下发驱动删除失败计数

DrvNoResource

组播MAC地址下发驱动资源不足计数

SynMsgFail

驱动信息同步失败计数

AllocEntryFail

组播MAC地址表项内存申请失败计数

AllocReDrvMsgFail

重刷组播MAC地址表项内存申请失败计数

AllocDrvMsgFail

组播MAC地址下发驱动内存申请失败计数

**SPBM \-- SPBM配置命令 \-- display spbm multicast-pw**

------------------------------------------------------------------------

**[display spbm multicast-pw**]命令用来显示SPBM的组播PW（BEB间建立的组播隧道）信息。

【命令】

**[display spbm multicast-pw**** **i-sid** ]*i-sid ***\**[count** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[i-sid ***i-sid*]：显示指定I-SID的组播PW信息。*i-sid*取值范围为255～16777215。如果未指定该参数，则显示所有I-SID的组播PW信息。

**[count**]：显示组播PW计数。如果未指定该参数，则显示组播PW信息。

【举例】

\# 显示所有的SPBM组播PW信息。

\<Sysname\> display spbm multicast-pw

System ID            I-SID      MAC address    B-VLAN Port

0011.2200.0101       300        0300-0a00-012c 10     GE1/0/1

                                                      GE1/0/2

\# 显示SPBM所有的组播PW计数。

\<Sysname\> display spbm multicast-pw count

Total entries: 2

表1-20 display spbm multicast-pw命令显示信息描述表

字段

描述

System ID

系统ID

I-SID

骨干网服务实例编号

MAC address

MAC地址

B-VLAN

MAC地址对应接口所属的B-VLAN

Port

出端口列表

Total entries

组播PW计数

**SPBM \-- SPBM配置命令 \-- display spbm non-stop-routing event-log**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display spbm non-stop-routing event-log**]命令用来显示SPBM NSR日志信息。

【命令】

集中式设备：

**[display spbm non-stop-routing**]** event-log**

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm non-stop-routing event-log** **slot** *slot-number*]

分布式设备－IRF模式：

**[display spbm non-stop-routing**]** event-log** **chassis***chassis-number***slot***slot-number*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot**]* slot-number*：显示指定单板的SPBM NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的SPBM NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的SPBM NSR日志信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定成员设备上指定单板的SPBM NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：显示指定单板的SPBM NSR日志信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 显示成员设备0的SPBM NSR日志信息。（集中式IRF设备）

\<Sysname\> display spbm non-stop-routing event-log slot 0

SPBM log information：

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Initialization).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Smooth).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (LSP stability).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (LSP generation).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (SPF computation).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Flush smooth).

Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Finish).

Aug 22 08:21:17 2013 -Slot=0 NSR complete.

\# 显示单板1的SPBM NSR日志信息。（分布式设备－独立运行模式）

\<Sysname\> display spbm non-stop-routing event-log slot 1

SPBM log information:

Oct  5 12:54:53 2013 -Slot=1 HA backup channel was blocked.

Oct  5 12:54:55 2013 -Slot=1 HA backup channel was unblocked.

\# 显示单板2的SPBM NSR日志信息。（分布式设备－独立运行模式）

\<Sysname\> display spbm non-stop-routing event-log slot 2

SPBM log information:

Oct  6 15:50:56 2013 -Slot=2 Memory restore on the standby MPU triggered data batch backup.

表1-21 display spbm non-stop-routing event-log命令显示信息描述表

字段

描述

Initialization

进入NSR的初始化阶段

Smooth

进入NSR的平滑阶段

LSP stability

进入LSP稳定阶段

LSP generation

进入LSP生成阶段

SPF computation

进入路由计算阶段

Flush smooth

进入内核数据平滑阶段

Finish

进入NSR的结束阶段

NSR complete

完成NSR

HA backup channel was blocked

降级（主进程变为备进程）过程中进入实时备份和批量备份通道阻塞状态

HA backup channel was unblocked

降级结束退出实时备份和批量备份通道阻塞状态

Memory restore on the standby MPU triggered data batch backup

备板内存恢复之后，会主动触发一次数据批量备份请求

【相关命令】

·**reset spbm ****non-stop-routing event-log**

**SPBM \-- SPBM配置命令 \-- display spbm non-stop-routing status**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display spbm non-stop-routing status**]命令用来显示SPBM NSR状态信息。

【命令】

**[display spbm non-stop-routing status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SPBM NSR状态信息。

\<Sysname\> display spbm non-stop-routing status

                     Nonstop Routing information for SPBM

                     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

NSR phase: Finish

表1-22 display spbm non-stop-routing status命令显示信息描述表

字段

描述

NSR phase

当前设备的NSR阶段：

·Initialization：进入NSR的初始化阶段

·Smooth：进入NSR的平滑阶段

·LSP stability：进入LSP稳定阶段

·LSP generation：进入LSP生成阶段

·SPF computation：进入路由计算阶段

·Flush smooth：进入内核数据平滑阶段

·Finish：进入NSR的结束阶段

**SPBM \-- SPBM配置命令 \-- display spbm peer**

------------------------------------------------------------------------

**[display spbm peer**]命令用来显示SPBM的邻居信息。

【命令】

**[display** **spbm** **peer** [ **system-id** *system-id*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[system-id ***system-id*]**：**显示指定邻居的信息，*system-id*的格式为XXXX.XXXX.XXXX。如果未指定该参数，则显示所有邻居的信息。

**[verbose**]：显示邻居的详细信息。如果未指定该参数，则显示邻居的简要信息。

【举例】

\# 显示所有邻居的简要信息。

\<Sysname\> display spbm peer

                          Peer information for SPBM

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

System ID         Port                        Circuit ID    State    Holdtime

5555.1111.1111    GE1/0/2                     1             Up       28s

5555.1111.2222    GE1/0/3                     1             Up\*      20s

\# 显示所有邻居的详细信息。

\<Sysname\> display spbm peer verbose

                          Peer information for SPBM

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

System ID         Port                        Circuit ID    State    Holdtime

5555.1111.1111    GE1/0/2                     1             Up       28s

Peer information:

  Host name: spbm-2

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

Local information:

  Host name: spbm-1

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format Selector      : 0

    Region Name          : spb

    Revision Level       : 0

    Configuration Digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

System ID         Port                        Circuit ID    State    Holdtime

5555.1111.2222    GE1/0/3                     1             Up       20s

Peer information:

  Host name: spbm-3

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

Local information:

  Host name: spbm-1

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

\# 显示System ID为5555.1111.1111的邻居的详细信息。

\<Sysname\> display spbm peer system-id 5555.1111.1111 verbose

                          Peer information for SPBM

                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

System ID         Port                        Circuit ID    State    Holdtime

5555.1111.1111    GE1/0/1                     1             Up       28s

Peer information:

  Host name: spbm-2

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

Local information:

  Host name: spbm-1

  Circuit ID: 1      Cost: 10

  MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  Aux MCID information:

    Format selector      : 0

    Region name          : spb

    Revision level       : 0

    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

  AP information:

    AN: 2    DAN: 0    Valid: 1

    Format identifier       : 0

    Format capabilities     : 0

    Convention identifier   : 0

    Convention capabilities : 0

    Edge count              : 2

    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000

表1-23 display spbm peer命令显示信息描述表

字段

描述

System ID

邻居的System ID

Port

与对端相连的本地SPBM接口

Circuit ID

邻居电路ID

State

邻居状态：

·Init：表示请求与邻居建立连接

·Up：表示邻居已建立，与邻居间的连接处于up状态，邻居可以承载流量

·Up\*：表示邻居已建立，与邻居间的连接处于up状态，但邻居不能承载流量

·Down：表示邻居已建立，与邻居间的连接处于down状态

Holdtime

抑制时间，如果在抑制时间内没有收到邻居发送的Hello报文，则认为邻居已经失效，如果收到了Hello报文，则抑制时间将重置为初始值

Peer information

邻居信息

Host name

邻居主机名，未配置主机名时显示邻居System ID

Circuit ID

邻居电路ID

Cost

邻居链路开销值

MCID information

邻居携带的主MCID信息

Aux MCID information

邻居携带的辅助MCID信息

Format selector

邻居生成树协议规定的选择因子，缺省值为0，不可配置

Region name

邻居MST域的域名

Revision level

邻居MST域的修订级别，可使用命令**revision-level**来配置，缺省为0级

Configuration digest

邻居配置摘要

AP information

邻居携带的AP信息，N/A表示未携带AP相关信息

AN

邻居携带的Agreement Number

DAN

邻居携带的Discarded Agreement Number

Valid

邻居携带的AP摘要是否有效：

·0：表示摘要无效

·1：表示摘要有效

Format identifier

邻居摘要类型标识

Format capabilities

邻居摘要格式类型

Convention identifier

邻居约定标识，发布环路避免的转发规则：

·1：表示无需匹配邻居的摘要信息

·2：表示发送者将继续进行无环路的组播和单播发送，即邻居之间严格Agreement之后才能转发流量

·3：表示发送者继续进行无环路的组播转发

Convention capabilities

邻居支持的摘要协商能力

Edge count

邻居AP协议计算摘要需要的参数

Topology digest

邻居拓朴摘要信息

Local information

本地信息

Hostname

本地主机名，未配置主机名时显示System ID

Circuit ID

本地电路ID

Cost

本地链路开销值

MCID information

本地携带的MCID

Aux MCID information

本地携带的辅助MCID

Format selector

本地生成树协议规定的选择因子，缺省值为0，不可配置

Region name

本地MST域的域名

Revision level

本地MST域的修订级别，可使用命令**revision-level**来配置，缺省为0级

Configuration digest

本地配置摘要

AP information

本地携带的AP信息，N/A表项未携带AP相关信息

AN

本地携带的Agreement Number

DAN

本地携带的Discarded Agreement Number

Valid

本地发送的AP摘要是否有效：

·0：表示摘要无效

·1：表示摘要有效

Format identifier

本地摘要类型标识

Format capabilities

本地摘要格式类型

Convention identifier

本地约定标识，发布环路避免的转发规则：

·1：表示无需匹配邻居的摘要信息

·2：表示发送者将继续进行无环路的组播和单播发送，即邻居之间严格Agreement之后才能转发流量

·3：表示发送者继续进行无环路的组播转发

Convention capabilities

本地支持的摘要协商能力

Edge count

本地AP摘要边数

Topology digest

本地拓朴摘要信息

**SPBM \-- SPBM配置命令 \-- display spbm summary**

------------------------------------------------------------------------

**[display spbm summary**]命令用来显示SPBM摘要信息。

【命令】

**[display spbm summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示SPBM摘要信息。

\<Sysname\> display spbm summary

                   Summary information for SPBM

                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Area address           : 00.0000

System ID              : 0011.2200.0001

System control address : 0180-c200-002e

System name            : spb-1

Bridge priority        : 32768

SPSource ID            : 200

SPSource mode          : Static

Agreement mode         : Both

MCID information:

  Format selector      : 0

  Region name          : spb

  Revision level       : 0

  Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7

B-VLANs                : 1-10, 100-200

表1-24 display spbm summary命令显示信息描述表

字段

描述

Area address

区域地址

System ID

系统ID

System control address

协议控制地址

System name

系统名

Bridge priority

桥优先级

SPSource ID

最短路径源ID

SPSource mode

最短路径源模式：

·Static：表明为静态配置

·Dynamic：表明为动态生成

Agreement mode

AP模式：

·Both：表示对单播表项、组播表项都进行AP检测

·Multicast：表示仅对组播表项进行AP检测

·Off：表示AP模式关闭

MCID information

本地MCID信息

Format selector

生成树协议规定的选择因子，缺省值为0，不可配置

Region name

MST域的域名

Revision level

MST域的修订级别，可使用命令**revision-level**来配置，缺省值为0

Configuration digest

配置摘要

B-VLANs

本地配置的B-VLAN

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fdb**

------------------------------------------------------------------------

**[display spbm unicast-fdb**]命令用来显示SPBM的单播FDB表项信息。

【命令】

**[display spbm unicast-fdb****\**[b-mac**[ *mac-address* \| **b-vlan** *vlan-id* \| **system-id** *system-id* ]  **count** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[b-mac*** mac-address*]：显示指定B-MAC的单播FDB表项信息，*mac-address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。如果未指定该参数，则显示所有B-MAC的单播FDB表项信息。

**[b-vlan*** vlan-id*]：显示指定B-VLAN的单播FDB表项信息。*vlan-id*为指定VLAN的编号，取值范围为1～4094。如果未指定该参数，则显示所有B-VLAN的单播FDB表项信息。

**[system-id** *system-id*]：显示指定System ID的单播FDB表项信息，*system-id*的格式为XXXX.XXXX.XXXX。如果未指定该参数，则显示所有System ID的单播FDB表项信息。

**[count**]：显示单播FDB表项计数。如果未指定本参数，则显示单播FDB表项信息。

【使用指导】

如果**b-mac*** mac-address*、**b-vlan*** vlan-id*和**system-id** *system-id*三个参数都未指定，则显示所有的SPBM单播FDB表项信息。

【举例】

\# 显示所有SPBM单播FDB表项信息。

\<Sysname\> display spbm unicast-fdb

Flags: E-Egress T-Transit

System ID            B-MAC            B-VLAN   Flags Port

0011.2200.0001       0011-2200-0001   9        T     GE1/0/2

0011.2200.0001       0011-2200-0001   4        T     GE1/0/2

0011.2200.0001       0011-2200-0001   5        T     GE1/0/2

\# 显示所有的SPBM单播FDB表项计数。

\<Sysname\> display spbm unicast-fdb count

Total entries: 2

表1-25 display spbm unicast-fdb命令显示信息描述表

字段

描述

System ID

系统ID

B-MAC

骨干网MAC地址

B-VLAN

B-MAC对应接口所属的B-VLAN

Flags

报文转发标志：

·E：表示出隧道

·T：表示转发

如果字段显示为两个转发标志的组合，如TE，则表示两个报文转发动作都有发生

Port

出端口

Total entries

SPBM单播FDB表项计数

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fib**

------------------------------------------------------------------------

**[display spbm unicast-fib**]命令用来显示SPBM单播FIB表项信息。

【命令】

集中式设备：

**[display spbm unicast-fib** [ **b-mac** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **verbose** ]]

**[display spbm unicast-fib** [ **b-vlan** *vlan-id*  **count**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm unicast-fib** [ **b-mac** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

**[display spbm unicast-fib** [ **b-vlan** *vlan-id*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **count**]]

分布式设备－IRF模式：

**[display spbm unicast-fib** [ **b-mac** *mac-address* [ **b-vlan** *vlan-id*  \| **b-vlan** *vlan-id* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]  **verbose** ]]

**[display spbm unicast-fib** [ **b-vlan** *vlan-id*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **count**]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[b-mac*** mac-address*]：显示指定B-MAC的单播FIB表项信息，*mac-address*的格式为H-H-H。在配置时，用户可以省去MAC地址中每段开头的"0"，例如输入"f-e2-1"即表示输入的MAC地址为"000f-00e2-0001"。如果未指定该参数，则显示所有B-MAC的单播FIB表项信息。

**[b-vlan*** vlan-id*]：显示指定B-VLAN的单播FIB表项信息，*vlan-id*取值范围为1～4094。如果未指定该参数，则显示所有B-VLAN的单播FIB表项信息。

**[b-mac*** mac-address* **b-vlan** *vlan-id*]：显示指定B-MAC及B-VLAN的单播FIB表项信息。如果未指定本参数，则显示所有的单播FIB表项信息。

**[verbose**]：显示单播FIB表项的详细信息。如果未指定本参数，则显示单播FIB表项的简要信息。

**[slot*** slot-number*]：显示指定单板的单播FIB表项信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的单播FIB表项信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的单播FIB表项信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的单播FIB表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的单播FIB表项信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的单播FIB表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的单播FIB表项信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的单播FIB表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的单播FIB表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的单播FIB表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的单播FIB表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的单播FIB表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[count**]：显示单播FIB表项计数。

【举例】

\# 显示SPBM单播FIB表的所有表项的简要信息。

\<Sysname\> display spbm unicast-fib

Flags: E-Egress T-Transit

B-MAC          B-VLAN Flags Port

0011-2200-0101 1      T     GE1/0/1

0011-2200-0101 2      T     GE1/0/2

\# 显示SPBM单播FIB表的所有表项的详细信息。

\<Sysname\> display spbm unicast-fib verbose

Flags: E-Egress T-Transit

B-MAC          B-VLAN Flags Driver flag Epoch       Port

0011-2200-0101 1      T     Done        0x1         GE1/0/2

0011-2200-0101 2      T     Done        0x1         GE1/0/2

\# 显示B-MAC为0011-2200-0101、B-VLAN为1的SPBM单播FIB表项的详细信息。

\<Sysname\> display spbm unicast-fib b-mac 0011-2200-0101 b-vlan 1 verbose

B-MAC  : 0011-2200-0101   B-VLAN     : 1

Port   : GE1/0/2

Flags  : T                Driver flag: Done

Epoch  : 0x1

Context: 0xffffffff 0xffffffff 0xffffffff 0xffffffff

\# 显示B-VLAN 100的SPBM单播FIB表项计数。

\<Sysname\> display spbm unicast-fib b-vlan 100 count

Total entries: 2

表1-26 display spbm unicast-fib命令显示信息描述表

字段

描述

B-MAC

SPBM单播转发表项的MAC地址

B-VLAN

SPBM单播转发表项的VLAN

Port

出端口

Flags

报文转发标志：

·E：表示出隧道

·T：表示转发

如果字段显示为两个转发标志的组合，如TE，则表示两个报文转发动作都有发生

Driver flag

下发驱动标记：

·Nores：表示下发驱动资源不足

·Done：表示下发驱动成功

Epoch

老化时间戳，用于表示表项是否需要老化

Context

保存SPBM FDB下刷驱动后返回的驱动信息

Total entries

SPBM单播FIB表项计数

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fib statistics**

------------------------------------------------------------------------

**[display spbm unicast-fib statistics**]命令用来显示SPBM单播FIB表项统计信息。

【命令】

集中式设备：

**[display spbm unicast-fib** **statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display spbm unicast-fib** **statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display spbm unicast-fib statistics** \**[chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot*** slot-number*]：显示指定单板的单播FIB表项统计信息。*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有单板的单播FIB表项统计信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的单播FIB表项统计信息。*slot-number*表示设备在IRF中的成员编号。如果未指定该参数，则显示所有成员设备的单播FIB表项统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的单播FIB表项统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定该参数，则显示所有成员设备/PEX的单播FIB表项统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的单播FIB表项统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的单播FIB表项统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的单播FIB表项统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定该参数，则显示所有单板的单播FIB表项统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的单播FIB表项统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。如果未指定该参数，则显示所有CPU的单播FIB表项统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示SPBM单播FIB表项统计信息。

\<Sysname\> display spbm unicast-fib statistics

SPBM unicast FIB basic statistics:

RefreshMsg     : 1           DeleteMsg        : 0

AddUMACNumber  : 1           DeleteUMACNumber : 0

DeleteNotFound : 0           AgeNumber        : 0

DrvAdd         : 1           DrvDelete        : 0

DrvDelRefresh  : 0

SPBM unicast FIB error statistics:

UMACMsgError   : 0           RefreshMsgFail   : 0

DeleteMsgFail  : 0           AddUMACFail      : 0

DrvOtherFail   : 0           DrvDeleteFail    : 0

DrvNoResource  : 0           SynMsgFail       : 0

AllocEntryFail : 0           AllocReDrvMsgFail: 0

表1-27 display spbm unicast-fib statistics命令显示信息描述表

字段

描述

SPBM unicast FIB basic statistics

SPBM单播转发表基础统计信息

RefreshMsg

单播MAC地址刷新消息

DeleteMsg

单播MAC地址删除消息

AddUMACNumber

创建单播MAC地址计数

DeleteUMACNumber

删除单播MAC地址计数

DeleteNotFound

删除时查找不到合适的单播MAC地址计数

AgeNumber

当前启动老化状态时老化表项的个数

DrvAdd

驱动表项添加

DrvDelete

驱动表项删除

DrvDelRefresh

驱动表项Modify时删除

UMACMsgError

无效的单播MAC地址消息

SPBM unicast FIB error statistics

SPBM单播转发表错误统计信息

RefreshMsgFail

单播MAC地址刷新消息处理失败

DeleteMsgFail

单播MAC地址删除消息处理失败

AddUMACFail

创建单播MAC地址表项失败

DrvOtherFail

单播MAC地址下发驱动添加或更新

DrvDeleteFail

单播MAC地址下发驱动删除

DrvNoResource

单播MAC地址下发驱动资源不足

SynMsgFail

信息同步失败

AllocEntryFail

单播MAC地址表项内存申请失败

AllocReDrvMsgFail

重刷单播MAC地址表项内存申请失败

**SPBM \-- SPBM配置命令 \-- display spbm unicast-pw**

------------------------------------------------------------------------

**[display spbm unicast-pw**]命令用来显示SPBM的单播PW（BEB间建立的单播隧道）信息。

【命令】

**[display spbm unicast-pw ** **i-sid** *i-sid* ]  **count**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[i-sid ***i-sid*]：显示指定I-SID的单播PW信息。*i-sid*取值范围为255～16777215。如果未指定该参数，则显示所有I-SID的单播PW信息。

**[count**]：显示单播PW计数。如果未指定该参数，则显示单播PW信息。

【举例】

\# 显示SPBM所有单播PW信息。

\<Sysname\> display spbm unicast-pw

System ID            I-SID      B-MAC          B-VLAN Port

000f.e201.0101       300        000f-e201-0101 100    GE1/0/1

000f.e201.0102       300        000f-e201-0102 100    GE1/0/2

\# 显示SPBM所有单播PW计数。

\<Sysname\> display spbm unicast-pw count

Total entries: 2

表1-28 display spbm unicast-pw命令显示信息描述表

字段

描述

System ID

系统ID

I-SID

I-SID

B-MAC

骨干网MAC地址

B-VLAN

B-MAC对应接口所属的B-VLAN

Port

B-MAC对应的接口

Total entries

单播PW计数

**SPBM \-- SPBM配置命令 \-- display spbm unicast-tree**

------------------------------------------------------------------------

**[display** **spbm unicast-tree**]用来显示单播树信息。

【命令】

**[display spbm unicast-tree**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示B-VLAN 100的SPBM单播树信息。

\<Sysname\> display spbm unicast-tree

                         SPF tree information for SPBM

                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    Flags: S-Node is on SPF tree       D-Node or Link is to be deleted

           O-Node is overload          I-Node is invalid

           T-Node is on tent list      P-Neighbor is parent node

           C-Neighbor is child node    L-Link is on changelist

           V-Link is involved          N-Link is a new path

SPF node: 0011.2200.0001

  LinkCount: 0x1    NodeFlags: T S

SPF link: \--\>0011.2200.0101

  Cost: 0xb      NewCost: 0xb      LinkFlags: P

SPF node: 0011.2200.0101

  LinkCount: 0x1    NodeFlags: S

SPF link: \--\>0011.2200.0001

  Cost: 0xa      NewCost: 0xb      LinkFlags: C

表1-29 display spbm unicast-tree命令显示信息描述表

字段

描述

Flags

节点或链路标志：

·S：表示节点在SPF树上

·D：表示节点或链路待删除

·O：表示节点置位OVERLOAD标记

·I：表示节点无效

·T：表示节点是候选节点

·P：表示节点是SPF树上指定链路的父节点

·C：表示节点是是SPF树上指定链路的子节点

·L：表示链路在链路变化链上

·V：表示链路置位INVOLVED标记

·N：表示链路是新增的

SPF node

SPF节点信息

LinkCount

以每个SPF节点为源的链路数

NodeFlags

SPF节点标志

SPF link

SPF链路信息

Cost

该链路源节点发布的度量值

NewCost

该链路源节点和目的节点协商后的度量值

LinkFlags

链路标志

**SPBM \-- SPBM配置命令 \-- ect**

------------------------------------------------------------------------

**[ect**]命令用来配置B-VLAN与ECT算法之间的映射关系。

**[undo ect**]命令用来取消B-VLAN与ECT算法之间的映射关系。

【命令】

**[ect ***ect-index*]**b-vlan** *vlan-id-list*

**[undo ect ***ect-index*]**b-vlan** [ *vlan-id-list* ]

【缺省情况】

所有B-VLAN都映射到ECT 1。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ect-index*]：ECT算法索引值，取值范围为1～16。

*[vlan-id-list*]：B-VLAN列表，表示方式为*vlan-id-list* = { *vlan-id1* [ **to** *vlan-id2*  }&\<1-10\>]。其中*vlan-id1*和*vlan-id2*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。*vlan*-*id2*的值要大于或等于*vlan*-*id1*的值。

【使用指导】

·在SPBN内通过不同ECT算法决策出不同的SPT，每个SPT对应一个转发路径，不同的SPT间形成流量的负载分担。ECT算法与B-VLAN之间有映射关系，一组B-VLAN可以映射到同一ECT算法，后续该组B-VLAN的流量都在该ECT算法决策的SPT内进行转发。通过调整B-VLAN与ECT算法的映射关系可以达到调整网络负载分担的目的。

·邻居间B-VLAN和ECT算法的映射关系不一致时，邻居间的链路不能承载流量。

·执行**undo ect**命令时，若指定的ECT算法索引值为1，则该配置无效。

【举例】

\# 配置B-VLAN 100～200映射到ECT 2上。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm ect 2 b-vlan 100 to 200

\# 取消所有B-VLAN与ECT 2的映射关系。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm undo ect 2 b-vlan

**SPBM \-- SPBM配置命令 \-- flash-flood**

------------------------------------------------------------------------

**[flash-flood**]命令用来配置LSP快速扩散功能。

**[undo flash-flood**]命令用来恢复缺省情况。

【命令】

**[flash-flood**[ [ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* ] \*]]

**[undo flash-flood**]

【缺省情况】

未配置LSP快速扩散功能。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[flood-count*** flooding-count*]：在SPF重新计算前快速扩散的LSP个数，取值范围为1～15，缺省值为5。

**[max-timer-interval*** flooding-interval*]：在LSP快速扩散之前的等待时间，取值范围为10～50000，单位为毫秒，缺省值为10毫秒。

【使用指导】

配置LSP快速扩散功能后，当LSP发生变化而导致SPF重新计算时，在SPF重新计算前，将把导致SPF重新计算的LSP快速扩散出去，扩散后，整网重新计算SPF。从而大大缩短设备之间由于进行LSP同步而导致LSDB不一致的时间，提高全网的快速收敛性能。

【举例】

\# 配置LSP快速扩散功能，在SPF重新计算前快速扩散的LSP个数为10，在LSP快速扩散之前的等待时间为100毫秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm flash-flood flood-count 10 max-timer-interval 100

**SPBM \-- SPBM配置命令 \-- graceful-restart**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart**]命令用来使能SPBM的GR功能。

**[undo graceful-restart**]命令用来恢复缺省情况。

【命令】

**[graceful-restart**]

**[undo graceful-restart**]

【缺省情况】

SPBM的GR功能处于关闭状态。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SPBM GR功能与SPBM NSR功能互斥，即**graceful-restart**和**non-stop-routing**命令互斥，不能同时配置。

【举例】

\# 使能SPBM的GR功能。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm graceful-restart

**SPBM \-- SPBM配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart suppress-sa**]命令用来配置GR时SA位置位。

**[undo graceful-restart suppress-sa**]命令用来配置GR时SA不置位。

【命令】

**[graceful-restart suppress-sa**]

**[undo graceful-restart suppress-sa**]

【缺省情况】

GR时SA位处于置位状态。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置GR时SA位置位。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm graceful-restart suppress-sa

**SPBM \-- SPBM配置命令 \-- graceful-restart t2**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[graceful-restart t2**]命令用来配置SPBM GR的T2定时器值。

**[undo graceful-restart t2**]命令用来恢复缺省情况。

【命令】

**[graceful-restart t2** *t2-value*]

**[undo graceful-restart t2**]

【缺省情况】

SPBM GR的T2定时器值为300秒。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[t2-value*]：指定SPBM GR的T2定时器值，取值范围为30～1800，单位为秒。

【使用指导】

T2定时器用来控制设备的GR时间间隔。T2定时器值在SPBM的Hello PDU中为保持时间，这样在该设备GR的时间内邻居不会断掉与其的邻接关系。如果T2定时器超时后，GR还没有完成，则GR失败。

【举例】

\# 配置SPBM GR的T2定时器值为120秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm graceful-restart t2 120

**SPBM \-- SPBM配置命令 \-- is-name**

------------------------------------------------------------------------

**[is-name**]命令用来使能动态主机名映射功能并为当前设备配置主机名称。

**[undo is-name**]命令用来恢复缺省情况。

【命令】

**[is-name** *is-name*]

**[undo is-name**]

【缺省情况】

动态主机名映射功能处于关闭状态且没有为当前设备配置主机名称。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[is-name*]：为当前设备配置的主机名称，为1～64个字符的字符串，区分大小写。

【举例】

\# 使能动态主机名映射功能，并为当前设备配置主机名称为spbm。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm is-name spbm

**SPBM \-- SPBM配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

**[l2vpn enable**]命令用来使能L2VPN功能。

**[undo l2vpn enable**]命令用来关闭L2VPN功能。

【命令】

**[l2vpn enable**]

**[undo l2vpn enable**]

【缺省情况】

L2VPN功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能L2VPN功能。

\<Sysname\> system-view

Sysname l2vpn enable

**SPBM \-- SPBM配置命令 \-- log-peer-change**

------------------------------------------------------------------------

**[log-peer-change**]命令用来配置邻接状态变化时生成日志信息。

**[undo log-peer-change**]命令用来配置邻接状态变化时不生成日志信息。

【命令】

**[log-peer-change**]

**[undo log-peer-change**]

【缺省情况】

邻接状态变化时生成日志信息。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置邻接状态变化时不生成日志信息。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm undo log-peer-change  

**SPBM \-- SPBM配置命令 \-- multicast replicate-mode**

------------------------------------------------------------------------

**[multicast replicate-mode**]命令用来配置SPBM组播转发模式。

**[undo multicast replicate-mode**]命令用来恢复缺省情况。

【命令】

**[multicast replicate-mode**[ { **head-end** \| **tandem** }]]

**[undo multicast replicate-mode**]

【缺省情况】

SPBM组播转发模式采用头端复制模式。

【视图】

VSI SPB视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[head-end**]：头端复制模式。

**[tandem**]：核心复制模式。

【举例】

\# 配置SPBM组播转发模式采用核心复制模式。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 spb i-sid 256

Sysname-vsi-vpn1-256 multicast replicate-mode tandem

**SPBM \-- SPBM配置命令 \-- multicast-bvlan enable**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[multicast-bvlan enable**]命令用来使能组播双B-VLAN功能。

**[undo multicast-bvlan enable**]命令用来恢复缺省情况。

【命令】

**[multicast-bvlan enable**]

**[undo multicast-bvlan enable**]

【缺省情况】

组播双B-VLAN处于关闭状态。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

支持组播核心复制模式的设备，缺省会使用同一B-VLAN来承载单播流量和组播流量。由于芯片限制会出现组播报文无法复制的问题，此时通过组播双B-VLAN功能可以解决该问题。

组播双B-VLAN功能使用奇数B-VLAN（B-VLAN值为奇数）来承载单播流量，使用偶数B-VLAN（B-VLAN值为偶数）来承载组播流量。SPB IS-IS协议报文中仅携带奇数B-VLAN，链路计算时会使用奇数B-VLAN来生成对应的单播转发表项，同时使用对应的偶数B-VLAN（奇数B-VLAN值＋1）来生成对应的组播转发表项。后续用户侧报文入SPBN时，会在奇数B-VLAN内进行单播发送，在偶数B-VLAN内进行组播发送。

需要注意的是：

·在SPBN中，只要有一台设备需使能组播双B-VLAN功能，则其他所有SPBM设备也必须使能组播双B-VLAN功能。

·在使能组播双B-VLAN模式与关闭组播双B-VLAN模式间进行切换时，会引起临时断流，所有对应B-MAC和PW表项都会删除重建。

·用户需要保证配置组播双B-VLAN时对应的奇数B-VLAN和偶数B-VLAN都与实例4092映射，且在这些B-VLAN流量经过的端口上都允许对应B-VLAN通过。若仅配置奇数B-VLAN或偶数B-VLAN，则SPB IS-IS协议报文无法携带该奇数B-VLAN。

·使能组播双B-VLAN功能后，SPB IS-IS协议报文只携带奇数B-VLAN，故对于I-SID与B-VLAN之间的映射关系，要求I-SID必须与奇数B-VLAN建立映射关系。

【举例】

\# 使能组播双B-VLAN功能。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm multicast-bvlan enable

**SPBM \-- SPBM配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[non-stop-routing**]命令用来使能SPBM的NSR功能。

**[undo non-stop-routing**]命令用来恢复缺省情况。

【命令】

**[non-stop-routing**]

**[undo non-stop-routing**]

【缺省情况】

SPBM的NSR功能处于关闭状态。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

SPBM NSR功能与SPBM GR功能互斥，即**non-stop-routing**和**graceful-restart**命令互斥，不能同时配置。

【举例】

\# 使能SPBM的NSR功能。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm non-stop-routing

**SPBM \-- SPBM配置命令 \-- reset spbm bvlan-info statistics**

------------------------------------------------------------------------

**[reset spbm bvlan-info statistics**]用来清除SPBM的B-VLAN统计信息。

【命令】

集中式设备：

**[reset spbm bvlan-info statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset spbm bvlan-info statistics** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset spbm bvlan-info statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：清除指定单板的B-VLAN统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot***slot-number*]：清除指定成员设备的B-VLAN统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：清除指定成员设备/PEX的B-VLAN统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的B-VLAN统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的B-VLAN统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的B-VLAN统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除SPBM的B-VLAN统计信息。（集中式设备）

\<Sysname\> reset spbm bvlan-info statistics

\# 清除单板1上SPBM的B-VLAN统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset spbm bvlan-info statistics slot 1

\# 清除成员设备1上SPBM的B-VLAN统计信息。（集中式IRF设备）

\<Sysname\> reset spbm bvlan-info statistics slot 1

【相关命令】

·**display spbm bvlan-info statistics**

**SPBM \-- SPBM配置命令 \-- reset spbm database**

------------------------------------------------------------------------

**[reset spbm database**]用来清除SPBM的数据库信息。

【命令】

**[reset spbm database** [ **graceful-restart** ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[graceful-restart**]：清除SPBM的数据库信息之后，可以通过GR方式来恢复数据。如果未指定本参数，则在清除SPBM的数据库信息后，只能以非GR方式来恢复数据。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除SPBM的数据库信息。

\<Sysname\> reset spbm database

【相关命令】

·**display spbm ****lsdb**

**SPBM \-- SPBM配置命令 \-- reset spbm graceful-restart event-log**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset spbm graceful-restart event-log**]命令用来清除SPBM GR日志信息。

【命令】

集中式设备：

**[reset spbm graceful-restart event-log**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset spbm graceful-restart event-log** **slot** *slot-number*]

分布式设备－IRF模式：

**[reset spbm graceful-restart event-log** **chassis** *chassis-number* **slot** *slot-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：清除指定单板的SPBM GR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：清除指定成员设备的SPBM GR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：清除指定成员设备/PEX的SPBM GR日志信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：清除指定成员设备上指定单板的SPBM GR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：清除指定单板的SPBM GR日志信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 清除单板1的SPBM GR日志信息。（分布式设备－独立运行模式）

\<Sysname\> reset spbm graceful-restart event-log slot 1

\# 清除成员设备1的SPBM GR日志信息。（集中式IRF设备）

\<Sysname\> reset spbm graceful-restart event-log slot 1

【相关命令】

·**display spbm graceful-restart event-log**

**SPBM \-- SPBM配置命令 \-- reset spbm multicast-fib statistics**

------------------------------------------------------------------------

**[reset spbm multicast-fib statistics**]用来清除SPBM的组播FIB表统计信息。

【命令】

集中式设备：

**[reset spbm multicast-fib statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset spbm multicast-fib statistics** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset spbm multicast-fib statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：清除指定单板的组播FIB表统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot***slot-number*]：清除指定成员设备的组播FIB表统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：清除指定成员设备/PEX的组播FIB表统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的组播FIB表统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的组播FIB表统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的组播FIB表统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除SPBM的组播FIB表统计信息。（集中式设备）

\<Sysname\> reset spbm multicast-fib statistics

\# 清除单板1上SPBM的组播FIB表统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset spbm multicast-fib statistics slot 1

\# 清除成员设备1上SPBM的组播FIB表统计信息。（集中式IRF设备）

\<Sysname\> reset spbm multicast-fib statistics slot 1

【相关命令】

·**display spbm multicast-fib statistics**

**SPBM \-- SPBM配置命令 \-- reset spbm non-stop-routing event-log**

------------------------------------------------------------------------

![说明](SPBM命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset spbm non-stop-routing event-log**]命令用来清除SPBM NSR日志信息。

【命令】

集中式设备：

**[reset spbm non-stop-routing event-log**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset spbm non-stop-routing event-log** **slot** *slot-number*]

分布式设备－IRF模式：

**[reset spbm non-stop-routing event-log** **chassis** *chassis-number* **slot** *slot-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]* slot-number*：清除指定单板的SPBM NSR日志信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：清除指定成员设备的SPBM NSR日志信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：清除指定成员设备/PEX的SPBM NSR日志信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：清除指定成员设备上指定单板的SPBM NSR日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number*** slot*** slot-number*：清除指定单板的SPBM NSR日志信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 清除单板1的SPBM NSR日志信息。（分布式设备－独立运行模式）

\<Sysname\> reset spbm non-stop-routing event-log slot 1

\# 清除成员设备1的SPBM NSR日志信息。（集中式IRF设备）

\<Sysname\> reset spbm non-stop-routing event-log slot 1

【相关命令】

·**display spbm non-stop-routing event-log**

**SPBM \-- SPBM配置命令 \-- reset spbm unicast-fib statistics**

------------------------------------------------------------------------

**[reset spbm unicast-fib statistics**]用来清除SPBM的单播FIB表统计信息。

【命令】

集中式设备：

**[reset spbm unicast-fib statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset spbm unicast-fib statistics** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[reset spbm unicast-fib statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：清除指定单板的单播FIB表统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot***slot-number*]：清除指定成员设备的单播FIB表统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：清除指定成员设备/PEX的单播FIB表统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的单播FIB表统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的单播FIB表统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的单播FIB表统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 清除SPBM的单播FIB表统计信息。（集中式设备）

\<Sysname\> reset spbm unicast-fib statistics

\# 清除单板1上SPBM的单播FIB表统计信息。（分布式设备－独立运行模式）

\<Sysname\> reset spbm unicast-fib statistics slot 1

\# 清除成员设备1上SPBM的单播FIB表统计信息。（集中式IRF设备）

\<Sysname\> reset spbm unicast-fib statistics slot 1

【相关命令】

·**display spbm unicast-fib statistics**

**SPBM \-- SPBM配置命令 \-- set-overload**

------------------------------------------------------------------------

**[set-overload**]命令用来配置LSDB过载标志位。

**[undo set-overload**]命令用来恢复缺省情况。

【命令】

**[set-overload** [ **on-startup** [ [ **start-from-nbr** *system-id* [ *timeout1* [ *nbr-timeout*  ] ] \| *timeout2* ]]]

**[undo set-overload**]

【缺省情况】]

未配置LSDB过载标志位。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[on-startup**]：系统启动时将过载标志位置位。

**[start-from-nbr** *system-id* [ *timeout1* [ *nbr-timeout*  ]]]：从系统启动时开始计算，如果在*nbr-timeout*参数指定的时长内仍未与指定邻居建立邻接关系，过载标志位将结束置位状态；如果在*nbr-timeout*参数指定的时长内与指定邻居建立了邻接关系，过载标志位将继续保持置位状态，且从与指定邻居建立邻接关系时重新计时，在*timeout1*参数配置的时长内保持置位状态。

*[system-id*]：指定邻居的System ID，*system-id*的格式为XXXX.XXXX.XXXX。

*[timeout1*]：取值范围为5～86400，单位为秒，缺省值为600秒（10分钟）。

*[nbr-timeout*]：取值范围为5～86400，单位为秒，缺省值为1200秒（20分钟）。

*[timeout2*]：从系统启动时开始计算，过载标志位保持置位状态的时间长度，取值范围为5～86400，单位为秒，缺省值为600秒（10分钟）。

【使用指导】

当SPBM设备因为内存不足或其他原因无法记录完整的LSDB时，将会导致区域路由的计算错误。在故障排除过程中，通过给怀疑有问题的设备配置LSDB过载标志位，SPBM将在该设备发送的LSP报文中把Overload位置位，以通知其他设备该设备发生了问题，无法正确的执行路由选择和报文转发，从而可以将其从SPBN中暂时隔离，便于进行故障定位。

需要注意的是：

·如果没有指定**on-startup**参数，SPBM将立即把过载标志位置位且一直保持置位状态，直到用户通过**undo** **set-overload**命令清除过载标志位。

·如果只指定**on-startup**参数，过载标志位将在系统启动时开始置位，并且在*timeout2*参数指定的时长内保持置位状态。

【举例】

\# 配置LSDB过载标志位。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm set-overload

**SPBM \-- SPBM配置命令 \-- snmp context-name**

------------------------------------------------------------------------

**[snmp context-name**]命令用来配置管理SPBM的SNMP实体所使用的上下文名称。

**[undo snmp context-name**]命令用来恢复缺省情况。

【命令】

**[snmp context-name ***context-name*]

**[undo snmp context-name**]

【缺省情况】

没有配置管理SPBM的SNMP实体所使用的上下文名称。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[context-name*]：管理SPBM的SNMP实体所使用的上下文名称，为1～32个字符的字符串，区分大小写。

【使用指导】

·SPBM使用IS-IS的MIB（Management Information Base，管理信息库）对NMS（Network Management System，网络管理系统）提供SPBM对象的管理，但标准IS-IS MIB中定义的MIB为单实例的管理对象，无法同时对IS-IS和SPBM进行管理。因此，参考RFC 4750中对OSPF多实例的管理方法，为管理SPBM定义一个上下文名称，以区分从NMS来的SNMP请求是要对IS-IS还是SPBM进行管理。

·由于上下文名称只是SNMPv3独有的概念，因此对于SNMPv1/v2c，会将团体名映射为上下文名称以对不同协议进行区分。

·所有使用IS-IS MIB的特性，如TRILL、EVI、SPBM、IS-IS等，都需要支持配置上下文名称以区分SNMP请求的管理对象。各特性实际配置的上下文名称是互斥的，即不允许不同的特性配置相同的上下文名称。

【举例】

\# 配置管理SPBM的SNMP实体所使用的上下文名称为spbm。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm snmp context-name spbm

**SPBM \-- SPBM配置命令 \-- snmp-agent trap enable spbm**

------------------------------------------------------------------------

**[snmp-agent trap enable spbm**]命令用来开启SPBM的告警功能。

**[undo snmp-agent trap enable spbm**]命令用来关闭SPBM的告警功能。

【命令】

**[snmp-agent trap enable spbm **[[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **b-mac-conflict** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]]**maxarea-mismatch**[ \| ]**own-lsp-purge**[ \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **spsource-conflict** \| **version-skew** ] **\***]

**[undo snmp-agent trap enable spbm **[[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **b-mac-conflict** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]]**maxarea-mismatch**[ \| ]**own-lsp-purge**[ \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **spsource-conflict** \| **version-skew** ] **\***]

【缺省情况】

SPBM的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[adjacency-state-change**]：表示SPBM邻居状态变化的告警信息。

**[area-mismatch**]：表示Hello报文区域地址不匹配的告警信息。

**[authentication**]：表示认证信息错误的告警信息。

**[authentication-type**]：表示认证信息类型错误的告警信息。

**[b-mac-conflict**]：表示远端B-MAC与本地B-MAC发生冲突的告警信息。

**[buffsize-mismatch**]：表示LSP报文长度和产生缓冲区大小不匹配的告警信息。

**[id-length-mismatch**]：表示SPBM报文中System ID长度不匹配的告警信息。

**[lsdboverload-state-change**]：表示LSDB过载状态变化的告警信息。

**[lsp-parse-error**]：表示LSP报文解析错误的告警信息。

**[lsp-size-exceeded**]：表示超大的LSP报文导致泛洪失败的告警信息。

**[max-seq-exceeded**]：表示LSP序列号超过最大序列号的告警信息。

**[maxarea-mismatch**]：表示Hello报文最大区域地址不匹配的告警信息。

**[own-lsp-purge**]：表示尝试清除本地LSP的告警信息。

**[protocol-support**]：表示报文协议支持类型不匹配的告警信息。

**[rejected-adjacency**]：表示Hello报文邻接不匹配丢弃的告警信息。

**[skip-sequence-number**]：表示跳过已经产生过的LSP序列号的告警信息。

**[spsource-conflict**]：表示远端SPSource ID与本地配置SPSource ID发生冲突的告警信息。

**[version-skew**]：表示Hello报文版本号不匹配的告警信息。

【使用指导】

如果未指定参数任何参数，表示开启或关闭SPBM的全部告警功能。

开启SPBM的告警功能后，SPBM会生成告警信息，用于报告本模块的重要事件。生成的告警信息将发送至SNMP模块，通过配置SNMP中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"SNMP"。

【举例】

\# 关闭SPBM的全部告警功能。

\<Sysname\> system-view

Sysname undo snmp-agent trap enable spbm

**SPBM \-- SPBM配置命令 \-- spb i-sid**

------------------------------------------------------------------------

**[spb i-sid**]命令用来创建SPB VSI实例，并进入VSI SPB视图。

**[undo spb i-sid**]命令用来恢复缺省情况。

【命令】

**[spb i-sid** *i-sid*]

**[undo spb i-sid**]

【缺省情况】

未创建SPB VSI实例。

【视图】

VSI视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[i-sid*]：指定SPB的骨干网服务实例编号，取值范围为255～16777215。

【使用指导】

创建SPB VSI实例就是创建一个SPB类型的VSI（Virtual Switch Instance，虚拟交换实例），并同时指定其I-SID。I-SID是SPB VSI实例的唯一编号，用来标识同一类型的服务，在同一个SPBN中必须指定相同的I-SID。有关VSI的详细介绍，请参见"MPLS配置指导"中的"VPLS"。

I-SID为255的SPB VSI实例专门提供给LSP快速泛洪通道，用于快速泛洪LSP。该SPB VSI实例在创建后即可开启LSP快速泛洪通道，无需与接口或以太网服务实例关联。

在同一个VSI视图下，PBB（Provider Backbone Bridge，运营商骨干网桥）和SPB的I-SID不能相同。有关PBB的详细介绍，请参见"二层技术-以太网交换配置指导"中的"PBB"。

【举例】

\# 为VSI实例vpn1指定SPB的I-SID为256，并进入VSI SPB视图。

\<Sysname\> system-view

Sysname vsi vpn1

Sysname-vsi-vpn1 spb i-sid 256

Sysname-vsi-vpn1-256

**SPBM \-- SPBM配置命令 \-- spbm**

------------------------------------------------------------------------

**[spbm**]命令用来全局使能SPBM功能，并进入SPBM视图。如果SPBM功能已全局使能，则直接进入SPBM视图。

**[undo spbm**]命令用来恢复缺省情况。

【命令】

**[spbm**]

**[undo spbm**]

【缺省情况】

全局的SPBM功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·全局使能SPBM功能后才可进行其他SPBM相关配置。

·全局关闭SPBM功能时会删除所有SPBM相关配置。

【举例】

\# 全局使能SPBM功能，并进入SPBM视图。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm

**SPBM \-- SPBM配置命令 \-- spbm authentication send-only**

------------------------------------------------------------------------

**[spbm authentication send-only**]命令用来配置不对收到的Hello报文进行验证密码检查。

**[undo spbm authentication send-only**]命令用来恢复缺省情况。

【命令】

**[spbm authentication send-only**]

**[undo spbm authentication send-only**]

【缺省情况】

如果配置了接口验证方式和验证密码，则对收到的Hello报文进行验证密码检查。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

配置邻居关系验证方式和验证密码时如果没有配置本命令，则在发送的Hello报文中按照**spbm authentication-mode**命令指定的方式携带验证密码，并对收到的Hello报文进行验证密码的检查，只有通过检查后，才会形成邻居关系。当需要更改密码时，由于两台设备的密码更改操作不完全同步，导致瞬时的密码不一致、邻居关系中断。此时，可以通过配置不对收到的报文进行验证密码检查，保证邻居关系不中断。

【举例】

\# 配置不对接口GigabitEthernet1/0/1收到的Hello报文进行验证密码检查。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm authentication send-only

【相关命令】

·**spbm authentication-mode**

**SPBM \-- SPBM配置命令 \-- spbm authentication-mode**

------------------------------------------------------------------------

**[spbm authentication-mode**]命令用来配置邻居关系验证方式和验证密码。

**[undo spbm authentication-mode**]命令用来恢复缺省情况。

【命令】

**[spbm authentication-mode****md5**[ \| ]**simple** } **[cipher ***cipher-string*[ \| ]**plain*** plain-string* }

**[undo spbm authentication-mode**]

【缺省情况】]

没有配置邻居关系验证方式和验证密码，不进行邻居关系验证。]

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md5**]：MD5验证模式。

**[simple**]：简单验证模式。

**[cipher**]：表示以密文的形式输入密码。

*[cipher-string*]：表示密文密码，为33～53个字符的字符串，区分大小写。

**[plain**]：表示以明文的形式输入密码。

*[plain-string*]：表示明文密码，为1～16个字符的字符串，区分大小写。

【使用指导】

配置邻居关系验证方式和验证密码后，将在发送的Hello报文中按照设定的方式携带验证密码，并对收到的报文进行验证密码的检查。

需要注意的是：

·两台SPBM设备要形成邻居关系必须在相应接口上配置相同的验证方式和验证密码。

·以明文或密文方式配置的验证密码，均以密文的方式保存在配置文件中。

【举例】

\# 在接口GigabitEthernet1/0/1上配置邻居关系采用简单验证模式，验证密码为123456，以明文形式输入密码。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm authentication-mode simple plain 123456

【相关命令】

·**spbm authentication send-only**

**SPBM \-- SPBM配置命令 \-- spbm cost**

------------------------------------------------------------------------

**[spbm cost**]命令用来配置SPBM的接口链路开销值。

**[undo spbm cost**]命令用来恢复缺省情况。

【命令】

**[spbm cost** *value*]

**[undo** **spbm cost**]

【缺省情况】

自动计算链路开销值。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：链路开销值，取值范围为1～16777215。

【使用指导】

·当接口链路开销值为16777215时，可以通过该接口与邻居建立连接关系，但邻居不能承载流量。

·当全局和接口同时配置链路开销值时，优先选择接口配置的链路开销值。

【举例】

\# 配置接口GigabitEthernet1/0/1的链路开销值为5。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm cost 5

**SPBM \-- SPBM配置命令 \-- spbm enable**

------------------------------------------------------------------------

**[spbm enable**]命令用来在当前接口上使能SPBM功能。

**[undo spbm enable**]命令用来恢复缺省情况。

【命令】

**[spbm enable**]

**[undo** **spbm enable**]

【缺省情况】

SPBM功能在接口上处于关闭状态。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·只需在BEB的上行口及BCB的接口上使能SPBM功能。

·使能接口上SPBM功能后才可进行接口上其他SPBM相关配置。

·关闭接口上SPBM功能时会删除该接口下所有SPBM相关配置。

【举例】

\# 在接口GigabitEthernet1/0/1上使能SPBM功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm enable

**SPBM \-- SPBM配置命令 \-- spbm timer hello**

------------------------------------------------------------------------

**[spbm timer hello**]命令用来配置Hello报文的发送时间间隔。

**[undo spbm timer hello**]命令用来恢复缺省情况。

【命令】

**[spbm timer hello** *seconds*]

**[undo spbm timer hello**]

【缺省情况】

Hello报文的发送时间间隔为10秒。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：配置Hello报文的发送时间间隔，取值范围为3～255，单位为秒。

【使用指导】

·如果设备在邻居关系保持时间内（邻居关系保持时间＝允许失效的Hello报文×Hello报文的发送时间间隔）一直没有收到来自邻居设备的Hello报文，将宣告邻居关系失效。通过配置允许失效的Hello报文数目和Hello报文的发送时间间隔，可以调整邻居关系保持时间，从而控制设备监测到邻居关系已经失效并重新进行路由计算所需的时长。

·发送时间间隔越短，网络收敛越快，但同时会占用更多的带宽资源和设备资源，请根据实际情况进行配置。

·邻居关系保持时间最大为65535秒。如果配置本命令后，计算出的邻居关系保持时间超过65535秒，则配置失败，配置前的Hello报文的发送时间间隔不做改变。

【举例】

\# 配置Hello报文在接口GigabitEthernet1/0/1上的发送时间间隔为20秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm timer hello 20

【相关命令】

·**spbm timer holding-multiplier**

**SPBM \-- SPBM配置命令 \-- spbm timer holding-multiplier**

------------------------------------------------------------------------

**[spbm timer holding-multiplier**]命令用来配置允许失效的Hello报文数目。

**[undo spbm timer holding-multiplier**]命令用来恢复缺省情况。

【命令】

**[spbm timer holding-multiplier** *value*]

**[undo spbm timer holding-multiplier**]

【缺省情况】

允许失效的Hello报文数目为3。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：允许失效的Hello报文数目，取值范围为3～1000。

【使用指导】

·失效的Hello报文数目，即宣告邻居失效前接口连续未收到的Hello报文数目（每当一个Hello报文的发送时间间隔内没有收到邻居Hello报文，就认为一个Hello报文失效）。

·如果设备在邻居关系保持时间内（邻居关系保持时间＝允许失效的Hello报文数目×Hello报文的发送时间间隔）一直没有收到来自邻居设备的Hello报文，将宣告邻居关系失效。通过配置允许失效的Hello报文数目和Hello报文的发送时间间隔，可以调整邻居关系保持时间，从而控制设备监测到邻居关系已经失效并重新进行路由计算所需的时长。

·邻居关系保持时间最大为65535秒。如果配置本命令后，计算出的邻居关系保持时间超过65535秒，则配置失败，配置前的允许失效的Hello报文数目不做改变。

【举例】

\# 指定接口GigabitEthernet1/0/1上允许失效的Hello报文数目为6。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm timer holding-multiplier 6

【相关命令】

·**spbm timer hello**

**SPBM \-- SPBM配置命令 \-- spbm timer lsp**

------------------------------------------------------------------------

**[spbm timer lsp**]命令用来配置发送LSP的最小时间间隔以及一次最多可以发送的LSP数目。

**[undo spbm timer lsp**]命令用来恢复缺省情况。

【命令】

**[spbm timer lsp** *time* [ **count** *count* ]]

**[undo** **spbm timer lsp**]

【缺省情况】

发送LSP的最小时间间隔为33毫秒，一次最多发送5个LSP报文。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：发送LSP的最小时间间隔，取值范围为1～1000，单位为毫秒。

*[count*]：一次最多可以发送的LSP数目，取值范围为1～1000。

【使用指导】

当LSDB的内容发生变化时，SPBM将把发生变化的LSP扩散出去，用户可以对LSP的最小发送时间间隔以及一次可以最多发送的LSP数目进行调节。

当存在大量SPBM接口或大量路由时，会发送大量的LSP报文，导致LSP风暴的出现。在这种情况下，建议将LSP的发送时间间隔配置得稍大一些。

【举例】

\# 配置接口GigabitEthernet1/0/1发送LSP的最小发送时间间隔为500毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 spbm timer lsp 500

**SPBM \-- SPBM配置命令 \-- spsource**

------------------------------------------------------------------------

**[spsource**]命令用来配置SPSource ID。

**[undo spsource**]命令用来恢复缺省情况。

【命令】

**[spsource** *spsource-id*]

**[undo spsource**]

【缺省情况】

SPSource ID由协议动态生成。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[spsource-id*]：最短路径源标记，取值范围为1～1048575。

【使用指导】

SPSource ID用来区分同一实例中不同的设备。静态配置时需保证配置的SPSource ID整网唯一。

【举例】

\# 配置SPSource ID为100。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm spsource 100

**SPBM \-- SPBM配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

**[timer** **lsp-generation**]命令用来配置LSP重新生成的时间间隔。

**[undo timer lsp-generation**]命令用来恢复缺省情况

【命令】

**[timer lsp-generation** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo timer lsp-generation**]

【缺省情况】

LSP重新生成的最大时间间隔为2秒，最小时间间隔为10毫秒，时间间隔惩罚增量为10毫秒。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：网络拓扑变化导致LSP重新生成时，LSP生成的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

·本命令在网络拓扑稳定的情况下将LSP重新生成的时间间隔缩小到*minimum-interval*，而在网络拓扑震荡的情况下进行相应惩罚（如连续触发路由计算n次时，时间间隔增加*incremental-interval*×2^n-2^），最终的时间间隔最大不超过*maximum-interval*。

·本命令中*minimum-interval*和*incremental-interva*l的配置值不允许大于*maximum-interval*的配置值。

【举例】

\# 配置LSP重新生成的最大时间间隔为10秒，最小时间间隔为100毫秒，时间间隔惩罚增量为200毫秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm timer lsp-generation 10 100 200

**SPBM \-- SPBM配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

**[timer lsp-max-age**]命令用来配置当前设备生成的LSP在LSDB里的最大生存时间。

**[undo timer lsp-max-age**]命令用来恢复缺省情况。

【命令】

**[timer lsp-max-age** *second*s]

**[undo timer lsp-max-age**]

【缺省情况】

当前设备生成的LSP在LSDB里的最大生存时间为1200秒。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：LSP在LSDB里的最大生存时间，取值范围是1～65535，单位为秒。

【使用指导】

·本命令仅对当前设备生效。

·每一个LSP都包含一个最大生存时间。当LSP驻留在LSDB中的时间达到最大生存时间时，SPBM将删除该LSP的内容，只保留该LSP的摘要信息（保留60秒），并将该LSP的剩余生存时间置0后，通知其他设备删除此LSP。网络管理员可根据网络规模对LSP的最大生存时间进行调整。

【举例】

\# 配置当前设备生成的LSP在LSDB里的最大生存时间为1500秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm timer lsp-max-age 1500

【相关命令】

·**timer lsp-refresh**

**SPBM \-- SPBM配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

**[timer lsp-refresh**]命令用来配置LSP刷新周期。

**[undo timer lsp-refresh**]命令用来恢复缺省情况。

【命令】

**[timer lsp-refresh** *second*s]

**[undo** **timer lsp-refresh**]

【缺省情况】

LSP刷新周期为900秒。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：LSP刷新周期，取值范围是1～65534，单位为秒。

【使用指导】

·每一个LSP都有一个最大生存时间，每个LSP都会随着时间的推移而被老化，因此每台设备必须定时刷新自己生成的LSP，以防止LSP被老化删除。另外，通过定时刷新LSP，还可以使整个区域中的LSP保持同步。用户可对LSP的刷新周期进行配置，提高LSP的刷新频率可以加快网络收敛速度，但是将占用更多的带宽。

·**timer lsp-refresh**命令配置的时间必须小于**timer lsp-max-age**命令配置的时间，以保证在LSP失效前进行刷新。

【举例】

\# 配置当前系统的LSP刷新周期为1200秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm timer lsp-refresh 1200

【相关命令】

·**timer lsp-max-age**

**SPBM \-- SPBM配置命令 \-- timer spf**

------------------------------------------------------------------------

**[timer spf**]命令用来配置SPBM路由计算[时间间隔。]

**[undo timer spf**]命令用来恢复缺省情况。

【命令】

**[timer spf** *maximum-interval* [ *minimum-interval* [ *incremental-interval*  ]]]

**[undo timer spf**]

【缺省情况】

SPBM路由计算的最大时间间隔为5秒，最小时间间隔为10毫秒，时间间隔惩罚增量为10毫秒。

【视图】

SPBM视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[maximum-interval*]：SPBM路由计算的最大时间间隔，取值范围为1～120，单位为秒。

*[minimum-interval*]：SPBM路由计算的最小时间间隔，取值范围为10～60000，单位为毫秒。

*[incremental-interval*]：SPBM路由计算的时间间隔惩罚增量，取值范围为10～60000，单位为毫秒。

【使用指导】

·本命令在网络拓扑稳定的情况下将连续路由计算的时间间隔缩小到*minimum-interval*，而在网络拓扑震荡的情况下进行相应惩罚（如连续触发路由计算n次时，时间间隔增加*incremental-interval*×2^n-2^），最终的时间间隔最大不超过*maximum-interval*。

·本命令中*minimum-interval*和*incremental-interval*的配置值不允许大于*maximum-interval*的配置值。

【举例】

\# 配置SPBM路由计算的最大时间间隔为10秒，最小时间间隔为100毫秒，时间间隔惩罚增量为300毫秒。

\<Sysname\> system-view

Sysname spbm

Sysname-spbm timer spf 10 100 300

**SPBM \-- SPBM配置命令 \-- vsi**

------------------------------------------------------------------------

**[vsi**]命令用来创建一个VSI，并进入VSI视图。如果指定的VSI已经存在，则直接进入VSI视图。

**[undo** **vsi**]命令用来删除指定的VSI。

【命令】

**[vsi**] *vsi-name*

**[undo**]**vsi** *vsi-name*

【缺省情况】

设备上不存在任何VSI。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsi-name*]：VSI的名称，为1～31个字符的字符串，区分大小写。

【举例】

\# 创建名为test的VSI，并进入VSI视图。

\<Sysname\> system-view

Sysname vsi test

Sysname-vsi-test

【相关命令】

·**display l2vpn vsi**

