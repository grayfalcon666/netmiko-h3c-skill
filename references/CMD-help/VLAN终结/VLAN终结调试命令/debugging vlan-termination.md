<!-- CMD-INDEX
  debugging vlan-termination          | 用户视图             | L5
-->

**VLAN终结 \-- VLAN终结调试命令 \-- debugging vlan-termination**

------------------------------------------------------------------------

【命令】

**[debugging **]**vlan-termination**[{ **all** \| **error** \| **event** \| **packet** } [ **interface** *interface-type interface-number* ]]

**[undo debugging **]**vlan-termination**[{ **all** \| **error** \| **event** \| **packet** } [ **interface** *interface-type interface-number* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示VLAN终结的所有调试开关。

**[error**]：表示VLAN终结的错误调试开关。

**[event**]：表示VLAN终结的事件调试开关。

**[packet**]：表示VLAN终结的报文调试开关。

**[interface**]* interface-type interface-number*：指定的接口类型和编号。

【描述】

**[debugging vlan-termination**]命令用来打开VLAN终结的调试开关。**undo debugging  vlan-termination**命令用来关闭VLAN终结的调试开关。

缺省情况下，VLAN终结的所有调试开关处于关闭状态。

表1-1 debugging vlan-termination命令输出信息描述表

字段

描述

*[interface-name*:]

*[state1 *to unique dot1q, DRV modify interface, VLAN ID *VID* ]

创建*interface-name*接口，接口状态从*state1*切换到unique dot1q，modify下驱动，下驱动时使用的*VID*

·interface-name表示接口名，形如：GigabitEthernet1/0/1.0

·state1接口原来的终结类型

·VID表示当前子接口的VLAN的编号

*[interface-name*:]

*[state1* to *unique qinq*, DRV modify interface, the first VLAN ID is *VID1*, and the second VLAN ID is *VID2*]

创建*interface-name*接口，接口状态从*state1*切换到unique qinq，modify下驱动

·*interface-name*表示接口名，形如：GigabitEthernet1/0/1.0

·*state1*接口原来的终结类型

·*VID1*表示当前子接口的外层VLAN的编号

·*VID2*表示当前子接口的内层VLAN的编号

*[interface-name*:]

*[state1* to ambiguous dot1q (ambiguous qinq), DRV modify interface, the number of nodes is *NUM*]

*[interface-name*]接口状态从*state1*切换到ambiguous dot1q或者ambiguous qinq，接口生成一个*NUM个*节点的链表

*[interface-name*:]

*[state1* to untagged (default/none), DRV modify interface]

*[interface-name*]接口状态从*state1*切换到untagged、default或者none

DRV create interface *interface-name*, which is not bound

*[interface-name*]接口被创建时不是绑定的

DRV create interface *interface-name,* which is bound to first is VLAN ID *VID*

*[interface-name*]接口被创建时是绑定的，VID表示绑定的VLAN ID

DRV destroy interface *interface-name,* whose config is none（default/untagged）

删除*interface-name*接口，删除之前的配置为none（default/untagged）

DRV destroy interface *interface-name,* whose config is unique dot1q, VLAN ID *VID*

删除*interface-name*接口，删除之前的配置为unique dot1q，VLAN ID为*VID*

DRV destroy interface *interface-name,* whose config is ambiguous dot1q: the number of nodes is *NUM*

删除*interface-name*接口，删除之前的配置为ambiguous dot1q，模糊终结节点的个数*NUM*

DRV destroy interface *interface-name*, whose config is unique qinq: the first VLAN ID is *VID1*, and the second VLAN ID is *VID2*

删除*interface-name*接口，删除之前的配置为*unique qinq*，*VID1*表示unique qinq的第一层VLAN ID, *VID2*表示*unique qinq*的第二层的VLAN ID

DRV destroy interface *interface-name,* whose config is ambiguous qinq: the first VLAN ID is *VID,* and the number of nodes is *NUM*

删除*interface-name*接口，删除之前的配置为ambiguous qinq，*VID*表示ambiguous qinq的第一层VLAN ID, 模糊终结节点的个数*NUM*

*interface-name*{.TableTextChar}:

OUT packet, len *length*{.TableTextChar}

*[context*]

*[interface-name*]接口发送一个报文，报文长度为*length*，报文内容为*context*

*interface-name*{.TableTextChar}:

IN packet, len *length*{.TableTextChar}

*[context*]

*[interface-name*]接口接收一个报文，报文长度为length，报文内容为*context*

![说明](VLAN终结Debug.files/image001.png)

接口有7种状态none、default、untagged、unique dot1q、unique qinq、ambiguous dot1q和ambiguous qinq，默认状态为none。

【举例】

\# 打开debug开关，创建子接口GigabitEthernet1/0/1.1，配置VLAN终结功能。

\<Sysname\> debugging vlan-termination all

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.1

\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:

DRV create interface GigabitEthernet1/0/1.1, which is not bound

*[//*]*创建子接口*

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q untagged

\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:

 GigabitEthernet1/0/1.1:

    none  to untagged, DRV modify interface

*[//*]*配置子接口为untagged，控制平面利用modify下驱动*

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 1

\*Feb 24 10:34:57:804 2023 Sysname ETH/7/EVENT:

 GigabitEthernet1/0/1.1:

    untagged to unique dot1q, DRV modify interface, VLAN ID 0x1

*// 配置子接口的VLAN ID为1，控制平面利用modify下驱动*

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 1 second-dot1q 3

\*Mar 26 17:07:25:156 2008 Sysname ETH/7/EVENT:

 GigabitEthernet1/0/1.1:

    unique dot1q to unique qinq, DRV modify interface, the first VLAN ID is 0x1， and the second VLAN ID is 0x3

*// 配置接口的明确QinQ，控制平面利用modify下驱动*

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 1 second-dot1q 10 12

\*Mar 26 17:07:25:156 2008 Sysname ETH/7/EVENT:

 GigabitEthernet1/0/1.1:

    unique qinq to ambiguous qinq, DRV modify interface, the number of nodes is 3

*// 配置接口的模糊QinQ，控制平面利用modify下驱动*

Sysname-GigabitEthernet1/0/1.1 undo vlan-type dot1q vid 1 second-dot1q 3 10 12

\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:

 GigabitEthernet1/0/1.1:

    ambiguous qinq  to none, DRV modify interface

*[//*]*配置子接口为none，控制平面利用modify下驱动*

Sysname-GigabitEthernet1/0/1.1 vlan-type dot1q vid 1 second-dot1q 13

Sysname-GigabitEthernet1/0/1.1 ip address 12.1.1.2 255.255.255.0

Sysname-GigabitEthernet1/0/1.1 ping -c 1 12.1.1.1

\*Mar 26 17:27:52:609 2008 Sysname ETH/7/PACKET:

 GigabitEthernet1/0/1.1:

     OUT packet,len 50

    ff ff ff ff ff ff 00 e0 14 03 32 00 81 00 00 01

    81 00 00 0d 08 06 00 01 08 00 06 04 00 01 00 e0

    14 03 32 00 0c 01 01 02 00 00 00 00 00 00 0c 01

    01 01

*// 从接口GigabitEthernet1/0/1.1发送一个长度为50的广播报文，报文的内层VLAN ID为13，外层VLAN ID为1*

\*Mar 26 17:27:52:671 2008 Sysname ETH/7/PACKET:

 GigabitEthernet1/0/1:

     IN packet,len 50

    00 e0 14 03 32 00 00 e0 14 03 28 00 81 00 00 01

    81 00 00 0d 08 06 00 01 08 00 06 04 00 02 00 e0

    14 03 28 00 0c 01 01 01 00 e0 14 03 32 00 0c 01

    01 02

*// 从接口GigabitEthernet1/0/1收到的一个长度为50的单播报文，报文带有双层VLAN TAG，内层为13，外层为1*

\*Mar 26 17:27:52:671 2008 Sysname ETH/7/PACKET:

 GigabitEthernet1/0/1.1:

     IN packet,len 42

    00 e0 14 03 32 00 00 e0 14 03 28 00 08 06 00 01

    08 00 06 04 00 02 00 e0 14 03 28 00 0c 01 01 01

    00 e0 14 03 32 00 0c 01 01 02

*// 从接口GigabitEthernet1/0/1.1收到一个长度为42的单播报文，此时报文的VLAN TAG已经被去掉*

Sysname-GigabitEthernet1/0/1.1 quit

Sysname undo interface gigabitethernet 1/0/1.1

\*Mar 26 17:07:25:156 2008 Sysname SIFVLAN/7/EVENT:

DRV destroy interface GigabitEthernet1/0/1.1, whose config is unique qinq: the first VLAN ID is 0x1, and the second VLAN ID is 0xd

*// 删除子接口*
