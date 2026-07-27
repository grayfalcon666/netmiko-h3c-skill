<!-- CMD-INDEX
  debugging mac-forwarding            | 用户视图             | L6
  debugging bridge                    | 用户视图             | L172
-->

**二层转发调试命令 \-- 普通二层转发 \-- debugging mac-forwarding**

------------------------------------------------------------------------

【命令】

**[debugging mac-forwarding**[ { **error** \| **packet** }]]

**[undo debugging mac-forwarding**[ { **error** \| **packet** }]]

【视图】

用户视图

【参数】

**[error**]：表示二层转发错误调试信息开关。

**[packet**]：表示二层转发报文调试信息开关。

【描述】

**[debugging mac-forwarding**]命令用来打开MAC转发调试开关。**undo debugging mac-forwarding**命令用来关闭MAC转发调试开关。

缺省情况下，调试信息开关处于关闭状态。

表1-1 debugging mac-forwarding命令输出信息描述表

字段

描述

Receiving

接收报文

Sending

发送报文

Deliver

将报文上送到上层

vlan

接收/发送报文的VLAN ID

interface

接收/发送报文的接口

payload

报文信息，以16进制格式打印前64字节

Discarding

报文被丢弃

Sending interface STP status is not forwarding. Packet discarded.

发送接口的STP状态不为forwarding。丢弃报文

The output interface is down. Packet discarded.

发送接口物理状态为down。丢弃报文

Unknown unicast, broadcast or multicast packet discarded by frame action.

当目的MAC为未知、广播、组播时丢弃报文

Frame discarded for Destination MAC is Drop.

目的MAC为丢弃类型，丢弃报文

Frame discarded for VLAN tag is invalid.

VLAN tag无效丢弃报文

Frame discarded by invalid MAC address.

MAC地址无效丢弃报文

**

【举例】

\# 打开转发报文调试开关。

\<Sysname\> debugging mac-forwarding packet

\*Aug  3 05:12:33:619 2013 Sysname MACFW/7/MACFW_PACKET:

Sending, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01

08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01

00 00 00 00 00 00 C0 A8 28 CA 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00

prompt : Sending an ethernet frame.

*// 本地接口GigabitEthernet1/0/1发送报文*

\*Aug  3 05:12:33:621 2013 Sysname MACFW/7/MACFW_PACKET:

Receiving, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 1C BD B9 E3 BD BB 00 26 E0 E0

03 FF FF 00 22 00 00 00 00 00 00 FF FF FF FF FF

FF 04 52 00 00 00 00 1C BD B9 E3 BD BB 40 00 00

03 00 04 00 00 00 00 00 00 00 00 00

prompt : Receiving an ethernet frame.

*// 从接口GigabitEthernet1/0/1接收到报文*

\*Aug  3 05:12:33:622 2013 Sysname MACFW/7/MACFW_PACKET:

Delivering, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01

08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01

00 00 00 00 00 00 C0 A8 28 66 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00

prompt: Deliver packet to layer2.

*// 将接收的报文送到上层处理*

\*Aug  3 05:12:33:623 2013 Sysname MACFW/7/MACFW_PACKET:

Discarding, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01

08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01

00 00 00 00 00 00 C0 A8 28 66 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00

prompt: Sending interface STP status is not forwarding. Packet discarded.

*// 发送接口的STP状态为discarding将报文丢弃*

\# 打开转发报文调试开关。

\<Sysname\>debugging mac-forwarding error

\*Aug  3 05:12:34:619 2013 Sysname MACFW/7/MACFW_ERROR:

prompt: Frame discarded by invalid MAC address.

*[// MAC*]*地址无效*

**二层转发调试命令 \-- Bridge转发 \-- debugging bridge**

------------------------------------------------------------------------

![说明](二层转发Debug.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

【命令】

**[debugging bridge **[{ **all** \| **error** \| **packet** }]]

**[undo debugging bridge **[{ **all** \| **error** \| **packet** }]]

【视图】

用户视图

【参数】

**[all**]：表示Bridge转发所有调试信息开关。

**[error**]：表示Bridge转发错误调试信息开关。

**[packet**]：表示Bridge转发报文调试信息开关。

【描述】

**[debugging bridge**]命令用来打开或关闭bridge转发调试开关。

缺省情况下，调试信息开关处于关闭状态。

表1-2 debugging bridge命令输出信息描述表

字段

描述

Receiving

接收报文

Sending

发送报文

vlan

接收/发送报文的VLAN ID

interface

接收/发送报文的接口

payload

报文信息，以16进制格式打印前64字节

Discarding

报文被丢弃

The packet is handling or discarded by service process!

报文被业务进程处理或丢弃

Frame discarded for Bridge is not found!

根据VLAN未找到Bridge的帧被丢弃

Frame discarded by invalid MAC address!

MAC地址无效的帧被丢弃

Frame discarded because of incorrect encapsulation type for the POS interface.

POS口丢弃收到的链路层封装类型不正确的帧

Invalid frame was discarded.

丢弃非法链路层报文

Sending an ethernet frame.

发送一个以太帧

Receiving an ethernet frame.

接收一个以太帧

Sending a PPP frame.

发送一个PPP帧

Receiving a PPP frame.

接收一个PPP帧

Sending an HDLC frame.

发送一个HDLC帧

Receiving an HDLC frame.

接收一个HDLC帧

【举例】

\# 打开所有调试信息开关。

\<Sysname\> debugging bridge all

\*Aug  3 05:12:33:619 2013 Sysname BRIDGE/7/BRIDGE_PACKET:

Sending, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01

08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01

00 00 00 00 00 00 C0 A8 28 CA 00 00 00 00 00 00

00 00 00 00 00 00 00 00 00 00 00 00

prompt : Sending an ethernet frame

*// 本地接口GigabitEthernet1/0/1发送报文*

\*Aug  3 05:12:33:621 2013 Sysname BRIDGE/7/BRIDGE_PACKET:

Receiving, vlan = 2, interface = GigabitEthernet1/0/1, payload =

FF FF FF FF FF FF 1C BD B9 E3 BD BB 00 26 E0 E0

03 FF FF 00 22 00 00 00 00 00 00 FF FF FF FF FF

FF 04 52 00 00 00 00 1C BD B9 E3 BD BB 40 00 00

03 00 04 00 00 00 00 00 00 00 00 00

prompt : Receiving an ethernet frame

*// 从接口GigabitEthernet1/0/1接收到报文*

\*Aug  3 05:12:34:619 2013 Sysname BRIDGE/7/ BRIDGE_ERROR:

Frame discarded for Bridge is not found!

*// 根据VLAN未找到Bridge的帧被丢弃*
