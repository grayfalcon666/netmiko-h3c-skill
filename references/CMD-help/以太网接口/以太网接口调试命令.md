<!-- CMD-INDEX
  debugging ethernet                  | ]                | L7
  debugging ifmgr                     | 用户视图             | L215
  debugging system-event              | 用户视图             | L279
-->

**以太网接口 \-- 以太网接口调试命令 \-- debugging ethernet**

------------------------------------------------------------------------

【命令】

**[debugging ethernet**** packet**[ \| ]**event** } \**[interface** *interface-type interface-number* ]

**[undo debugging ethernet **** packet **[\| ]**event **}

【视图】]

用户视图]

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[packet**]：表示收发以太网报文的调试信息开关。

**[event**]：表示以太网事件的调试信息开关。

**[interface** *interface-type interface-number*]：表示指定接口的调试信息开关。*interface-type interface-number*表示接口类型和接口编号。

【描述】

**[debugging ethernet**]命令用来打开以太网接口模块报文调试信息开关。**undo debugging ethernet**命令用来关闭以太网接口模块报文调试信息开关。

缺省情况下，以太网接口模块报文调试信息开关处于关闭状态。

表1-1 debugging ethernet命令显示信息描述表

字段

描述

Eth_rcv: Received an ethernet packet

接收一个以太网报文

Eth_send: Sent an ethernet packet

发送一个以太网报文

interface

收发报文的接口

format: x

以太网帧的封装格式：0表示ETH_II封装，1表示SNAP封装

src_addr: x--x-x

源MAC地址

dst_addr: x--x-x

目的MAC地址

payload: x x x

源MAC之后的报文以太网头信息，以16进制格式打印

Eth_event: Received LINKUP message

接收到链路上行事件的消息

Eth_event: Received LINKDOWN message

接收到链路下行事件的消息

Eth_event: Received IF message

接收到接口事件消息

Eth_event: Notified LAGG line status change message

通知聚合链路状态变化的消息

Ifindex *x*

接口索引值为*x*

type *x*

事件子类型为*x*

status from *x* to *y*

状态从*x*变到*y*

process return *x*

处理返回值为*x*

【举例】

\# 打开收发以太网报文的调试信息开关，两台设备直连，进行**ping**操作。

\<Sysname\> debugging ethernet packet

\<Sysname\> ping 20.10.3.100

 PING 20.10.3.100: 56  data bytes, press CTRL_C to break

\*Dec  8 09:58:04:957 2006 Sysname ETH/7/Eth_send: Sent an ethernet packet, interface: Vlan-interface1, format: 0, src_addr: 000f-e249-8048, dst_addr: ffff-ffff-ffff, payload: 08 00

*// 发送一个以太网报文，发送接口为Vlan-interface1，以太帧格式为ETHII，发送者MAC地址为000f-e249-8048，目标MAC地址为ffff-ffff-ffff，以太头源MAC后面的数据为0800*

\*Dec  8 09:58:04:957 2006 Sysname ETH/7/Eth_rcv: Received an ethernet packet, interface: GigabitEthernet1/0/3, format: 0, src_addr: 0015-e944-a947, dst_addr: 000f-e249-8048, payload: 81 00 00 02 08 00

*// 接收一个以太网报文，接收接口为GigabitEthernet1/0/3，以太帧格式为ETHII，发送者MAC地址为0015-e944-a947，目标MAC地址为000f-e249-8048，以太头源MAC后面的数据为810000020800*

\# 打开以太网事件的调试信息开关。

\<Sysname\> debugging ethernet event

\*Oct 24 11:37:16:425 2012 Sysname ETH/7/Eth_event: -MDC=1; Received IF message, type 1073741888, ifindex 0, process return 0.

*[//*]*接收到接口事件信息，类型为1073741888，接口索引为0，处理返回值为0. *

\*Oct 24 11:37:16:426 2012 Sysname ETH/7/Eth_event: -MDC=1; Received LINKUP message, type 5, ifindex 2, process return 0.    

*[//*]*接收到链路上行事件信息，类型为5，接口索引为2，处理返回值为0*

\*Oct 24 11:37:16:426 2012 Sysname ETH/7/Eth_event: -MDC=1; Received LINKDOWN message, type 35, ifindex 2, process return 0.

*[//*]*接收到链路下行事件信息，类型为35，接口索引为2，处理返回值为0*

\*Oct 24 11:01:00:902 2012 Sysname ETH/7/Eth_event: -MDC=1; Notified LAGG line status change message, ifindex 2, status from 0 to 1.

*[//*]*通知LAGG线路状态更新，接口索引为2，状态从0变为1*

表1-2 debugging ethernet命令显示信息描述表

字段

描述

Eth_rcv: Received an ethernet packet

接收一个以太网报文

Eth_send: Sent an ethernet packet

发送一个以太网报文

interface

收发报文的接口

format: x

以太网帧的封装格式：0表示ETH_II封装，1表示SNAP封装

src_addr: x--x-x

源MAC地址

dst_addr: x--x-x

目的MAC地址

payload: x x x

源MAC之后的报文以太网头信息，以16进制格式打印

Eth_event: Received LINKUP message

接收到链路上行事件的消息（物理层通知链路层的事件为上行事件）

Eth_event: Received LINKDOWN message

接收到链路下行事件的消息（网络层通知链路层的事件为下行事件）

Eth_event: Received IF message

接收到接口事件消息

Eth_event: Notified LAGG line status change message

通知聚合链路状态变化的消息

Ifindex *x*

接口索引值为*x*

type *x*

事件子类型为*x*

status from *x* to *y*

状态从*x*变到*y*

process return *x*

处理返回值为*x*

**以太网接口 \-- 以太网接口调试命令 \-- debugging ifmgr**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging ifmgr**]

**[undo** **debugging ifmgr**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging ifmgr ** **slot** *slot-number*  **cpu** *cpu-number*  ]

**[undo** **debugging ifmgr** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging** **ifmgr** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **ifmgr** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设置所有单板的调试开关。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示设置所有单板的调试开关。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示设置所有单板的调试开关。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示IRF中的设置所有单板/PEX的调试开关。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示所有单板/PEX的调试开关。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【描述】

**[debugging ifmgr**]命令用来打开接口管理模块调试信息开关。**undo debugging ifmgr**命令用来关闭接口管理模块调试信息开关。

缺省情况下，接口管理模块调试信息开关处于关闭状态。

【举例】

\# 打开接口管理模块调试信息的开关。

\<Sysname\> debugging ifmgr

**以太网接口 \-- 以太网接口调试命令 \-- debugging system-event**

------------------------------------------------------------------------

【命令】

集中式设备：

**[debugging system-event**]

**[undo** **debugging system-event**]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system-event** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging system-event** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[debugging** **system-event** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

**[undo** **debugging** **system-event** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：表示单板所在的槽位号。不指定该参数时，表示设置所有单板的调试开关。（分布式设备－独立运行模式）

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示设置所有单板的调试开关。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，表示设置所有单板的调试开关。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，则表示设置所有单板的调试开关。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。不指定该参数时，则表示所有单板/PEX的调试开关。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【描述】

**[debugging system-event**]命令用来打开系统事件模块调试信息开关。**undo** **debugging system-event**命令用来关闭系统事件模块调试信息开关。

缺省情况下，系统事件模块调试信息开关处于关闭状态。

【举例】

\# 打开系统事件模块调试信息的开关。

\<Sysname\> debugging system-event
