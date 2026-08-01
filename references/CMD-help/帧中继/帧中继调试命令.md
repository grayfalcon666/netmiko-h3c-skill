<!-- CMD-INDEX
  debugging fr                        | 用户视图             | L6
  debugging fr compression iphc       | 用户视图             | L706
-->

**帧中继 \-- 帧中继调试命令 \-- debugging fr**

------------------------------------------------------------------------

**[debugging** **fr**]命令用来打开帧中继调试信息开关。

**[undo** **debugging** **fr**]命令用来关闭帧中继调试信息开关。

【命令】

**[debugging fr** { **all** [ **interface** *interface-type* *interface-number*  \| **event** \| **inarp**  **interface** *interface-type* *interface-number* [ **dlci** *dlci-number*  ] \| **lmi**  **interface** *interface-type* *interface-number*  \| **packet**  **interface** *interface-type* *interface-number* [ **dlci** *dlci-number*  ] \| **packet-hex**  **interface** *interface-type* *interface-number*  }]]

**[undo debugging fr** { **all** [ **interface** *interface-type* *interface-number*  \| **event** \| **inarp**  **interface** *interface-type* *interface-number* [ **dlci** *dlci-number*  ] \| **lmi**  **interface** *interface-type* *interface-number*  \| **packet**  **interface** *interface-type* *interface-number* [ **dlci** *dlci-number* ] \| **packet-hex**  **interface** *interface-type* *interface-number*  }]]

【缺省情况】

帧中继所有调试信息开关均处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[event**]：表示事件调试信息开关。

**[inarp**]：表示逆向地址解析协议调试信息开关。

**[lmi**]：表示LMI协议调试信息开关。

**[packet**]：表示数据报文调试信息开关。

**[packet-hex**]：表示十六进制报文调试信息开关，包括数据报文和协商报文。

**[interface ***interface-type interface-number*]：表示指定接口的调试信息开关。如果不指定接口，则表示所有接口的调试信息开关。指定的接口只能是主接口，不能是子接口。指定主接口后，将打开主接口及其子接口的调试信息开关。

**[dlci ***dlci-number*]：表示指定虚电路的调试信息开关。*dlci-number*表示虚电路DLCI编号，取值范围为16～1007，范围0～15、1008～1023的虚电路为帧中继协议保留，供特殊使用。如果不指定本参数，则表示所有虚电路的调试信息开关。

【使用指导】

表1-1 debugging fr event命令输出信息描述表

字段

描述

Added IP address on interface *interface-name.*

接口*interface-name*添加IP地址

Deleted IP address on interface *interface-name.*

接口*interface-name*删除IP地址

Modified IP address on interface *interface-name.*

接口*interface-name*修改IP地址

Keepalive changed on interface *interface-name.*

接口*interface-name *keep alive变化

Failed to create a MAP for exceeding the MAP number limit on the DLCI.

创建MAP失败，超过了PVC上允许的最大MAP个数

Failed to create a MAP for exceeding the MAP number limit in the system.

创建MAP失败，超过了系统允许的最大MAP个数

Failed to create a MAP for exceeding the MAP number limit on the interface.

创建MAP失败，超过了接口允许的最大MAP个数

Failed to create a PVC for exceeding the PVC number limit in the system.

超出系统允许创建的PVC个数上限，创建PVC失败

Failed to send a packet on interface *interface-name*, because the PVC state is down.

PVC状态为DOWN，接口*interface-name*发送报文失败

Failed to send a packet on interface *interface-name*, because of the packet encapsulation error.

报文封装错误，接口*interface-name*发送报文失败

Failed to send a packet on interface *interface-name*, because the PVC does not exist.

PVC不存在，接口*interface-name*发送报文失败

Failed to send a packet on interface *interface-name*, because there is no matched MAP.

没有匹配的MAP，接口*interface-name*发送报文失败

Failed to send a packet on interface *interface-name*, because the packet type is unknown.

报文类型错误，接口*interface-name*发送报文失败

Failed to received a packet on interface *interface-name*, because the packet length error.

报文长度错误，接口*interface-name*接收报文失败

表1-2 debugging fr inarp命令输出信息描述表

字段

描述

Sent an InARP *packet-type* packet on interface *interface-name* DLCI *DLCI*:

  hard length=*hard length*, hard=*hard*

  protocol length=*protocol length*, protocol=*protocol*

  source IP=*source IP*, target IP=*target IP*

在接口*interface-name*下DCLI为*DLCI*上发送InARP *packet-type*报文：硬件地址长度为*hard length*，硬件地址类型为*hard*（*hard*值为0x000f，表示帧中继），协议地址长度为*protocol length*，协议地址类型为*protocol*（*protocol*值为0x0800，表示IP协议），源协议地址为*source IP*，目的协议地址为*target IP*，其中*packet-type*的类型如下：

·request：请求报文

·reply：应答报文

Received an InARP *packet-type* packet on interface *interface-name* DLCI *DLCI*:

  hard length=*hard length*, hard=*hard*

  protocol length=*protocol length*, protocol=*protocol*

  source *IP*=*source IP*, target *IP*=*target IP*

在接口*interface-name*下DCLI为*DLCI*上收到InARP *packet-type*报文：硬件地址长度为*hard length*，硬件地址类型为*hard*（*hard*值为0x000f，表示帧中继），协议地址长度为*protocol length*，协议地址类型为*protocol*（*protocol*值为0x0800，表示IP协议），源协议地址为*source IP*，目的协议地址为*target IP*，其中*packet-type*的类型如下：

·request：请求报文

·reply：应答报文

Received an InARP packet on interface *interface-name*: Protocol not supported.

接口*interface-name*收到InARP报文：协议类型不支持

Received an InARP packet on interface *interface-name*: Frame length error.

接口*interface-name*收到InARP报文：帧长度错误

Received an InARP packet on interface *interface-name*: Field length error.

接口*interface-name*收到InARP报文：域长度错误

Received an InARP packet on interface *interface-name*: Hardware type error.

接口*interface-name*收到InARP报文：硬件类型错误

Received an InARP packet on interface *interface-name*: IP address length error.

接口*interface-name*收到InARP报文：协议地址长度错误

Received an InARP packet on interface *interface-name*: Operation code error.

接口*interface-name*收到InARP报文：报文操作码不合法

Received an InARP packet on interface *interface-name*: Operation code not supported.

接口*interface-name*收到InARP报文：报文操作码不支持

Create dynamic MAP failed on interface *interface-name* : No IP address.

接口*interface-name*创建动态MAP失败：没有IP地址

Create dynamic MAP failed on interface *interface-name* : Cannot create MAP on P2P interface.

接口*interface-name*创建动态MAP失败：P2P子接口不能创建MAP

Create dynamic MAP failed on interface *interface-name* : Static or default MAP exist.

接口*interface-name*创建动态MAP失败：已经存在静态或缺省MAP

Interface *interface-name*: Failed to send a packet.

接口*interface-name*：报文发送失败

Interface *interface-name*: Unknown error.

接口*interface-name*：未知错误

表1-3 debugging fr lmi命令输出信息描述表

字段

描述

Sent a LMI *packet-type message-type* packet on interface *interface-name*:

  ssn=*ssn*, rsn=*rsn*

在接口*interface-name*上发送LMI *packet-type message-type*报文：发送报文序列号为*ssn*，接收报文序列号为*rsn*，其中*packet-type*的类型如下：

·full：全状态报文

·LIV：链路完整性验证报文

·asyn：异步PVC状态报文

*[message-type*]的类型如下：

·status：状态消息

·status enquiry：状态请求消息

Received a LMI *packet-type message-type* packet on interface *interface-name*:

  ssn=*ssn*, rsn=*rsn*

在接口*interface-name*上收到LMI *packet-type message-type*报文：发送报文序列号为*ssn*，接收报文序列号为*rsn*，其中*packet-type*的类型如下：

·full：全状态报文

·LIV：链路完整性验证报文

·asyn：异步PVC状态报文

*[message-type*]的类型如下：

·status：状态消息

·status enquiry：状态请求消息

Sent a LMI *packet-type message-type* packet on interface *interface-name*:

  ssn=*ssn*, rsn=*rsn*

**[PVCs=*num*]

**[DLCI=*DLCI*, *active*, new=*new*]

在接口*interface-name*上发送LMI *packet-type message-type*报文：发送报文序列号为*ssn*，接收报文序列号为*rsn*，虚链路号为*DLCI*，PVC的状态为*act*，是否新建标志为*new*，PVC个数为*num*，其中*packet-type*的 类型如下：

·full：全状态报文

·LIV：链路完整性验证报文

·asyn：异步PVC状态报文

*[message-type*]的类型如下：

·status：状态消息

·status enquiry：状态请求消息

*[active*]的类型如下：

·inactive：表示PVC处于非激活状态

·active：表示PVC处于激活状态

*[new*]的类型如下：

·0：表示不是新创建的PVC

·1：表示新创建的PVC

Received a LMI *packet-type message-type* packet on interface *interface-name*:

  ssn=*ssn*, rsn=*rsn*

**[PVCs=*num*]

  DLCI=*DLCI*, *active*, new=*new*

在接口*interface-name*上收到LMI *packet-type message-type*报文：发送报文序列号为*ssn*，接收报文序列号为*rsn*，虚链路号为*DLCI*，PVC的状态为*act*，是否新建标志为*new*，PVC个数为*num*，其中*packet-type*的 类型如下：

·full：全状态报文

·LIV：链路完整性验证报文

·asyn：异步PVC状态报文

*[message-type*]的类型如下：

·status：状态消息

·status enquiry：状态请求消息

*[active*]的类型如下：

·inactive：表示PVC处于非激活状态

·active：表示PVC处于激活状态

*[new*]的类型如下：

·0：表示不是新创建的PVC

·1：表示新创建的PVC

Timeout on interface *interface-name* (interface type=*interface type*, state=*state*).

在接口*interface-name*上超时，此接口类型为*interface type*，状态为*state*，其中*interface type*的类型如下：

·DTE：数据终端设备

·DCE：数据电路终接设备

*[state*]的类型如下：

·up：链路连接

·down：链路断开

Received a LMI packet on interface *interface-name*: Packet length error.

接口*interface-name*收到LMI报文：报文长度错误

Interface *interface-name*: DTE received illegal LMI status enquiry packet.

接口*interface-name*：DTE端收到非法状态请求报文

Interface *interface-name*: DCE received illegal LMI status packet.

接口*interface-name*：DCE端收到非法状态应答报文

Interface *interface-name*: Received LMI type different from the configured type.

接口*interface-name*：接收LMI报文封装类型与端口配置类型不一致

Received a LMI packet on interface *interface-name*: Packet format error.

接口*interface-name*收到LMI报文：报文格式错误

Received a LMI packet on interface *interface-name*: Call reference information unit content error.

接口*interface-name*收到LMI报文：Call reference信息单元内容错误

Received a LMI packet on interface *interface-name*: Message type value is illegal.

接口*interface-name*收到LMI报文：Message type取值非法

Received a LMI packet on interface *interface-name*: Locking Shift information unit value is illegal.

接口*interface-name*收到LMI报文：ANSI类型Locking Shift信息单元内容取值非法

Received a LMI packet on interface *interface-name*: ANSI message type is illegal.

接口*interface-name*收到LMI报文：异步状态报文的消息类型非法

Received a LMI packet on interface *interface-name*: Report type ID error.

接口*interface-name*收到LMI报文：Report type信息单元标识取值非法

Received a LMI packet on interface *interface-name*: Report type length error.

接口*interface-name*收到LMI报文：Report type信息单元长度取值非法

Received a LMI packet on interface *interface-name*: Report type error.

接口*interface-name*收到LMI报文：Report类型不合法

Received a LMI packet on interface *interface-name*: LIV ID error.

接口*interface-name*收到LMI报文：Link integrity verification信息单元标识取值非法

Received a LMI packet on interface *interface-name*: LIV length error.

接口*interface-name*收到LMI报文：Link integrity verification信息单元长度取值非法

Received a LMI packet on interface *interface-name*: PVC status error in LIV.

接口*interface-name*收到LMI报文：PVC状态字段取值非法

Received a LMI packet on interface *interface-name*: PVC status unit length error.

接口*interface-name*收到LMI报文：PVC状态信息单元长度取值非法

Received a LMI packet on interface *interface-name*: PVC ID error.

接口*interface-name*收到LMI报文：PVC状态信息单元标识取值非法

Received a LMI packet on interface *interface-name*: PVC length error.

接口*interface-name*收到LMI报文：PVC状态信息单元长度取值非法

Received a LMI packet on interface *interface-name*: Exceeding the upper limit for the PVC count.

接口*interface-name*收到LMI报文：PVC个数超出最大限制

Received a LMI packet on interface *interface-name*: Illegal DLCI.

接口*interface-name*收到LMI报文：PVC状态信息单元DLCI取值非法

Interface *interface-name*: Failed to send a packet.

接口*interface-name*：报文发送失败

Interface *interface-name*: Unknown error.

接口*interface-name*：未知错误

表1-4 debugging fr packet命令输出信息描述表

字段

描述

Sent a *packet-type* packet on interface *interface-name* DLCI *DLCI*, packet length is *length.*

在接口*interface-name*下虚电路号为*DLCI*上发送*packet-type*报文，长度为*length*，其中*packet type*的类型有：IP、ISIS、MPLS

Received a *packet-type* packet on interface *interface-name* DLCI *DLCI*, packet length is *length.*

在接口*interface-name*下虚电路号为*DLCI*上收到*packet-type*报文，长度为*length*，其中*packet type*的类型有：IP、ISIS、MPLS

Interface *interface-name* DLCI *DLCI*: DLCI reserved

接口*interface-name* DLCI *DLCI*：保留虚链路号

Interface *interface-name* DLCI *DLCI*: Type unrecognized

接口*interface-name* DLCI *DLCI*：非法协议类型

Interface *interface-name* DLCI *DLCI*: PVC unavailable

接口*interface-name* DLCI *DLCI*：PVC没有配置或非激活

Interface *interface-name* DLCI *DLCI*: MAP unavailable

接口*interface-name* DLCI *DLCI*：MAP无效

Interface *interface-name* DLCI *DLCI*: Unknown reason

接口*interface-name* DLCI *DLCI*：未知的原因

表1-5 debugging fr packet-hex命令输出信息描述表

字段

描述

Sent a packet on interface *interface-name*, packet length is *length.*

The packet content in hex format:

*[  hex sequence*.]

在接口*interface-name*上发送报文，长度为*length。*十六进制显示报文内容：*十六进制序列*

Received a packet on interface *interface-name*, packet length is *length.*

The packet content in hex format:

*[  hex sequence*.]

在接口*interface-name*上收到报文，长度为*length。*十六进制显示报文内容：*十六进制序列*

【举例】

\# Router A与Router B通过串口连接，链路层协议配置为FR，两端配置好IP地址，Router A的DTE接口关闭InARP功能，Router B的DCE接口使能InARP功能，具体配置如下：

·Router A

\<RouterA\> system-view

RouterA interface serial 2/1/0

RouterA-Serial2/1/0 link-protocol fr

RouterA-Serial2/1/0 fr interface-type dte

RouterA-Serial2/1/0 fr dlci 200

RouterA-Serial2/1/0-fr-dlci-200 quit

RouterA-Serial2/1/0 undo fr inarp ip 200

RouterA-Serial2/1/0 ip address 2.2.2.1 255.255.255.0

·Router B

\<RouterB\> system-view

RouterB interface serial 2/1/0

RouterB-Serial2/1/0 link-protocol fr

RouterB-Serial2/1/0 fr interface-type dce

RouterB-Serial2/1/0 fr dlci 200

RouterB-Serial2/1/0-fr-dlci-200 quit

RouterB-Serial2/1/0 fr inarp ip 200

RouterB-Serial2/1/0 ip address 2.2.2.2 255.255.255.0

\# 打开Router A的帧中继事件调试信息开关。将Router A的Serial2/1/0接口进行**undo ip address**操作时，在Router A上可以看到如下调试信息：

\<RouterA\> debugging fr event

\*Sep 10 09:36:30:715 2013 RouterA FR/7/EVENT:

Deleted IP address on interface Serial2/1/0.

*// 在接口Serial2/1/0上删除IP地址*

\# Router A与Router B通过串口连接，链路层协议配置为FR，接口或虚链路使能InARP功能（缺省使能），两端配置好IP地址，具体配置如下：

·Router A

\<RouterA\> system-view

RouterA interface serial 2/1/0

RouterA-Serial2/1/0 link-protocol fr

RouterA-Serial2/1/0 fr interface-type dte

RouterA-Serial2/1/0 fr dlci 200

RouterA-Serial2/1/0-fr-dlci-200 quit

RouterA-Serial2/1/0 ip address 2.2.2.1 255.255.255.0

·Router B

\<RouterB\> system-view

RouterB interface serial 2/1/0

RouterB-Serial2/1/0 link-protocol fr

RouterB-Serial2/1/0 fr interface-type dce

RouterB-Serial2/1/0 fr dlci 200

RouterB-Serial2/1/0-fr-dlci-200 quit

RouterB-Serial2/1/0 ip address 2.2.2.2 255.255.255.0

\# 打开Router A的帧中继逆向地址解析协议调试信息开关。将Router A的Serial2/1/0接口进行**shutdown**、**undo shutdown**操作时，在Router A上可以看到如下调试信息：

\<RouterA\> debugging fr inarp

\*Sep 10 09:36:30:715 2013 RouterA FR/7/INARP:

Sent an InARP request packet on interface serial2/1/0 DLCI 200:

  hard length=2, hard=0x000F

  protocol length=4, protocol=0x0800

  source IP=2.2.2.1, target IP=0.0.0.0

*// 在接口Serial2/1/0的虚链路200上发送InARP请求报文。*

\*Sep 10 09:36:30:715 2013 RouterA FR/7/INARP:

Received an InARP reply packet on interface serial2/1/0 DLCI 200:

  hard length=2, hard=0x000F

  protocol length=4, protocol=0x0800

  source IP=2.2.2.2, target IP=0.0.0.0

*// 在接口Serial2/1/0的虚链路200上收到InARP响应报文。*

\# Router A与Router B通过串口相连，链路层协议配置为FR，接口或虚链路使能LMI（缺省使能）。两端配置好接口类型，具体配置如下：

·Router A

\<RouterA\> system-view

RouterA interface serial 2/1/0

RouterA-Serial2/1/0 link-protocol fr

RouterA-Serial2/1/0 fr interface-type dte

·Router B

\<RouterB\> system-view

RouterB interface serial 2/1/0

RouterB-Serial2/1/0 link-protocol fr

RouterB-Serial2/1/0 fr interface-type dce

\# 在Router A端打开帧中继LMI协议调试信息开关。将Router A的Serial2/1/0接口进行**shutdown**、**undo shutdown**操作时，在Router A上可以看到如下调试信息：

\<RouterA\> debugging fr lmi

\*Sep 10 09:36:30:715 2013 RouterA FR/7/LMI:

Sent a LMI full status enquiry packet on interface serial2/1/0:

  ssn=1, rsn=0

*// 在接口Serial2/1/0的虚链路上发送LMI全状态请求报文，包含收发序号。*

\*Sep 10 09:36:30:715 2013 RouterA FR/7/LMI:{.TerminalDisplayChar}

Received a LMI full status packet on interface serial2/1/0:

  ssn=1, rsn=1

  PVCs=2

  DLCI=100, active, new=1

  DLCI=200, active, new=1

*// 在接口Serial2/1/0的虚链路上收到LMI全状态响应报文，包含收发序号以及PVC信息。*

\# Router A与Router B通过串口连接，链路层协议配置为FR，接口或虚链路使能InARP功能（缺省使能），两端配置好IP地址，具体配置如下：

·Router A

\<RouterA\> system-view

RouterA interface serial 2/1/0

RouterA-Serial2/1/0 link-protocol fr

RouterA-Serial2/1/0 fr interface-type dte

RouterA-Serial2/1/0 fr dlci 200

RouterA-Serial2/1/0-fr-dlci-200 quit

RouterA-Serial2/1/0 ip address 2.2.2.1 255.255.255.0

·Router B

\<RouterB\> system-view

RouterB interface serial 2/1/0

RouterB-Serial2/1/0 link-protocol fr

RouterB-Serial2/1/0 fr interface-type dce

RouterB-Serial2/1/0 fr dlci 200

RouterB-Serial2/1/0-fr-dlci-200 quit

RouterB-Serial2/1/0 ip address 2.2.2.2 255.255.255.0

\# 打开Router A的帧中继数据报文调试信息开关和十六进制报文调试信息开关。将Router A的Serial2/1/0接口进行ping -c 1 2.2.2.2操作时，在Router A上可以看到如下调试信息：

\<RouterA\> debugging fr packet

\<RouterA\> debugging fr packet-hex

\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET:

Sent an IP packet on interface serial2/1/0 DLCI 200, packet length is 88.

\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET-HEX:

Sent a packet on interface serial2/1/0, packet length is 88.

The packet content in hex format:

  30 81 03 cc 45 00 00 54 06 35 00 00 ff 01 ad 6d

  02 02 02 01 02 02 02 02 08 00 2c 2a 19 01 00 00

  52 3f 25 33 00 08 50 57 08 09 0a 0b 0c 0d 0e 0f

  10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f

*// 在接口Serial2/1/0的DLCI 200上发送IP报文，长度为88。*

\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET:

Received an IP packet on interface serial2/1/0 DLCI 200, packet length is 88.

\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET-HEX:

Received a packet on interface serial2/1/0, packet length is 88.

The packet content in hex format:

  30 81 03 cc 45 00 00 54 00 10 00 00 ff 01 b3 92

  02 02 02 02 02 02 02 01 00 00 34 2a 19 01 00 00

  52 3f 25 33 00 08 50 57 08 09 0a 0b 0c 0d 0e 0f

  10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f

*// 在接口Serial2/1/0的DLCI 200上收到IP报文，长度为88。*

**帧中继 \-- 帧中继调试命令 \-- debugging fr compression iphc**

------------------------------------------------------------------------

**[debugging fr compression iphc**]命令用来打开帧中继IPHC压缩调试信息开关。

**[undo debugging fr compression iphc**]命令用来关闭帧中继IPHC压缩调试信息开关。

【命令】

**[debugging fr compression iphc**[ { **rtp** \| **tcp** }]]

**[undo debugging fr compression iphc**[ { **rtp** \| **tcp** }]]

【缺省情况】

帧中继IPHC压缩的所有调试信息开关均处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rtp**]：表示RTP头压缩调试信息开关。

**[tcp**]：表示TCP头压缩调试信息开关。

【使用指导】

帧中继IPHC压缩调试信息包括：IPHC协商信息和压缩/解压缩信息。

表1-6 debugging fr compression iphc命令输出信息描述表（IPHC协商信息）

字段

描述

Received IPHC negotiation info on interface *interface-name* DLCI *dlci-number*.

在接口*interface-name*，DLCI为*dlci-number*上收到IPHC协商信息

Received an active event in Disable state.

IPHC negotiation started.

Sent a config REQ (F = 1) packet, FSM state changed to I1.

IPHC状态机在去使能状态收到了激活事件

IPHC开始协商

发送REQ (F = 1)报文，状态机进入I1状态

Received a config REQ (F = \*) packet in Disable state.

Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.

IPHC状态机在去使能状态下收到REQ (F =\*)报文

发送ACK报文和REQ (F = 0)报文，状态机进去I3状态

Error: Received a config ACK packet in Disable state.

状态机收到错误事件：去使能状态下收到ACK报文

Error: Received a negotiation timer timeout event in Disable state.

状态机收到错误事件：去使能状态下收到协商定时器超时事件

Error: Received an illegal event in Disable state.

状态机收到错误事件：去使能状态下收到非法事件

Error: Received an active event in I1 state.

状态机收到错误事件：I1状态收到激活事件

Received a config REQ (F = \*) packet in I1 state.

Sent a config ACK packet, FSM state changed to I3.

状态机在I1阶段收到REQ (F = \*)报文，并发送ACK报文，状态机进入I3状态

Received a config ACK packet in I1 state.

FSM state changed to I2.

状态机在I1阶段收到ACK报文

进入I2状态

Received a negotiation timer timeout (+) event in I1 state.

Sent a config REQ (F = 1) packet.

状态机在I1状态收到协商定时器超时(+)事件，并发送REQ (F = 1)报文

Received a negotiation timer timeout (-) event in I1 state.

IPHC negotiation stopped.

状态机在I1状态收到协商定时器超时(-)事件

IPHC协商停止

Error: Received an illegal event in I1 state.

状态机收到错误事件：I1状态收到非法事件

Error: Received an active event in I2 state.

状态机收到错误事件：I2状态收到激活事件

Received a config REQ (F = 1) packet in I2 state.

Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.

状态机在I2状态下收到REQ (F = 1)报文，并发送ACK报文和REQ (F = 0)报文，状态机进入I3状态

Received a config REQ (F = 0) packet in I2 state.

Sent a config ACK packet, FSM state changed to Operational.

IPHC negotiation done.

状态机在I2阶段收到REQ (F = 0)报文，并发送ACK报文，状态机进入Operational状态

IPHC协商完成

Error: Received a config ACK packet in I2 state.

状态机收到错误事件：在I2状态收到ACK报文

Received a negotiation timer timeout (+) event in I2 state.

Sent a config REQ (F = 1) packet, FSM state changed to I1.

状态机在I2阶段收到协商定时器超时(+)事件，并发送REQ (F = 1)报文，状态机进入I1状态

Received a negotiation timer timeout (-) event in I2 state.

IPHC negotiation stopped.

状态机在I2状态收到协商定时器超时(-)事件

IPHC协商停止

Error: Received an illegal event in I2 state.

状态机收到错误事件：I2状态下收到非法事件

Error: Received an active event in I3 state.

状态机收到错误事件：I3状态下收到激活事件

Received a config REQ (F = 1) packet in I3 state.

Sent config ACK and config REQ (F = 0) packets, FSM state remains in I3.

状态机在I3状态下收到REQ (F = 1)报文，并发送ACK报文和REQ (F = 0)报文，状态机保持在I3状态

Received a config REQ (F = 0) packet in I3 state.

Sent a config ACK packet, FSM state remains in I3.

状态机在I3状态下收到REQ (F = 0)报文，并发送ACK报文，状态机保持在I3状态

Received a config ACK packet in I3 state.

FSM state changed to Operational.

IPHC negotiation done.

状态机在I3状态收到ACK报文，并进入Operational状态

IPHC协商完成

Received a negotiation timer timeout (+) event in I3 state.

Sent a config REQ (F = 0) packet, FSM state remains in I3.

状态机在I3状态收到协商定时器超时(+)事件，并发送REQ (F = 0)报文，状态机保持在I3状态

Received a negotiation timer timeout (-) event in I3 state.

IPHC negotiation stopped.

状态机在I3状态收到协商定时器超时(-)事件

IPHC协商停止

Error: Received an illegal event in I3 state.

状态机收到错误事件：I3状态收到非法事件

Error: Received an active event in Operational state.

状态机收到错误事件：Operational状态收到激活事件

Error: Received a negotiation timer timeout event in Operational state.

状态机收到错误事件：Operational状态收到协商定时器超时事件

Received a config REQ (F = 1) packet in Operational state.

Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.

状态机在Operational状态收到REQ (F = 1)报文，并发送ACK报文和REQ (F = 0)报文，状态机进入I3状态

Received a config REQ (F = 0) packet in Operational state.

Sent a config ACK packet, FSM state remains in Operational state.

状态机在Operational状态收到REQ (F = 0)报文，并发送ACK报文，状态机保持Operational状态

Received a config ACK packet in Operational state.

状态机收到错误事件：Operational状态收到ACK报文

Error: Received an illegal event in Operational state.

状态机收到错误事件：Operational状态收到非法事件

帧中继IPHC状态机相关说明：

·Active：协商激活事件，状态机只在Disable状态时收到该事件。收到该事件后开始协商。

·REQ (F = 1)：请求报文(F = 1)，表示收到此报文后需要回复ACK报文和REQ (F = 0)报文。在I1状态时只需回复ACK报文。

·REQ (F = 0)：请求报文(F = 0)，表示收到此报文后，需要回复ACK报文。在Disable状态时，需同时回复REQ (F = 0)报文。

·REQ (F = \*)：表示不区别F = 1还是F = 0。

·ACK：应答报文，接收到对端REQ (F = \*)报文后，回复此报文。

·timeout (+)：定时器超时(+)事件。发送REQ (F = \*)报文后，在规定时间内没有收到ACK报文且定时器超时次数没有超过最大值时收到此事件。

·timeout (-)：定时器超时(-)事件。发送REQ (F = \*)报文后，在规定时间内没有收到ACK报文且定时器超时次数超过了到最大值时收到此事件。

·Error：表示在某状态下收到某个事件是错误的，不作动作，状态不改变。

表1-7 debugging fr compression iphc命令输出信息描述表（IPHC压缩/解压缩信息）

字段

描述

RHC

RTP头压缩信息

THC

TCP头压缩信息

FULL_HEADER

未压缩的TCP或者RTP报文，解压端根据这个报文为解压后续的压缩报文创建或更新解压表项

CONTEXT_STATE

一种由解压端发送给压缩端的特殊报文，用来传输已经或者可能已经失去同步的压缩和解压表项的ID号来通知压缩端发送一个FULL_HEADER报文来同步压缩和解压缩表项

COMPRESSED_NON_TCP

压缩的RTP报文。接口下配置**fr compression iphc enable** **nonstandard**命令后，成功压缩时，压缩端会将RTP报文压缩成该格式的报文

COMPRESSED_TCP

压缩的TCP报文。成功压缩时，压缩端会将TCP报文压缩成该格式的报文

COMPRESSED_RTP_8

压缩的RTP报文。当接口上允许进行RTP头压缩的最大连接数小于等于256时，成功压缩时，压缩端会将RTP报文压缩成该种格式的报文

COMPRESSED_RTP_16

压缩的RTP报文。当接口上允许进行RTP头压缩的最大连接数大于256时，成功压缩时，压缩端会将RTP报文压缩成该种格式的报文

ERROR

IPHC压缩/解压缩过程的错误信息

WARNING

IPHC压缩/解压缩过程的提示信息

received

接收报文

sent

发送报文

connect ID

报文流标识，表示压缩/解压缩的某条流。压缩端和解压端根据这个ID号来查找压缩和解压缩表项

checksum

校验和

seq

Sequence Number，报文的序列号

gen

Generation Number字段用来检测COMPRESSED_NON_TCP报文压缩和解压缩的一致性

Sent uncompressed packets

发送了没有压缩的报文。压缩过程中，当检测到压缩表项为空，不能对报文进行压缩，为保证报文传输，会发送没有经过压缩的报文，并打印该条信息

The compression context of TCP is invalid

压缩TCP报文过程中检测到压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

IP header mismatched

压缩TCP报文过程中检测到IP头与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

TCP header mismatched

压缩TCP报文过程中检测到TCP头与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_URG code error

压缩TCP报文过程中检测到Delta URG字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

th_URG mismatched

压缩TCP报文过程中检测到URG字段与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_win code error

压缩TCP报文过程中检测到Delta Window字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_ACK code error

压缩TCP报文过程中检测到Delta Acknowledgment Number字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta th_seq code error

压缩TCP报文过程中检测到Delta Sequence字段编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The flag bits of th_URG, th_seq, and th_win are set

压缩TCP报文过程中检测到URG字段、Sequence Number字段和Window字段的标识位被置为1时，压缩端会发送FULL_HEADER报文，同时更新压缩表项

Delta IP ID code error

压缩TCP报文过程中检测到Delta IP ID编码错误。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The compression context of NON_TCP is invalid

将RTP报文压缩成COMPRESSED_NON_TCP报文过程中检测到COMPRESSED_NON_TCP的压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

UDP checksum mismatched

压缩RTP报文过程中检测到UDP头的Checksum字段与压缩表项中的不匹配。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The number of compressed NON_TCP packets is out of range

将RTP报文压缩成COMPRESSED_NON_TCP过程中检测到在两个FULL_HEADER报文之间，发送的COMPRESSED_NON_TCP报文的数量超出了规定的范围

The time for compressing NON_TCP packet is lawless

将RTP报文压缩成COMPRESSED_NON_TCP报文的过程中检测到压缩的报文的时间段非法。这时压缩端会发送一个FULL_HEADER报文来同步压缩端和解压端（在每发送一个FULL_HEADER报文后的一段时间内压缩的COMPRESSED_NON_TCP压缩报文是合法的，不在这个时间段内对报文进行压缩是非法的）

The delta values of timestamp,sequence number, or IP ID are lawless

压缩RTP报文的过程中检测到时间戳的delta值、报文序列号的delta值或者IP ID的delta值非法。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The compression context of RTP is invalid

压缩RTP报文的过程中检测到RTP的压缩表项无效。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

The delta value of the IP ID is lawless

压缩RTP报文的过程中检测到IP头Delta ID值非法。这时压缩端会发送FULL_HEADER报文，同时更新压缩表项

Connect ID xx out of range

解压过程中检测到报文流标识号xx超出合法范围

the decompression context is null

解压过程中检测到解压缩表项为空。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the decompression context is  invalid

解压过程中检测到解压缩表项无效。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the TCP checksum is error

解压过程中检测到TCP Checksum字段错误。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the generation number is mismatched

解压缩过程中检测到Generation Number字段不匹配。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the time for receiving the packet is lawless

解压过程中检测到接收COMPRESSED_NON_TCP报文的时间非法。这时解压端会向压缩端发送一个CONTEXT_STATE报文

the sequence number is mismatched

解压过程中检测到Sequence Number字段与解压表想中的不匹配。这时解压端会向压缩端发送一个CONTEXT_STATE报文

【举例】

\# Router A与Router B通过串口连接，链路层协议配置为FR，两端都开启IPHC压缩功能，并配置了IP地址。打开Router A和Router B的帧中继IPHC TCP头压缩调试信息开关，在Router A接口执行**shutdown**/**undo shutdown**，在Router A和Router B上可以看到如下调试信息：

\<RouterA\> debugging fr compression iphc tcp

\<RouterB\> debugging fr compression iphc tcp

·Router A

\*Mar 25 02:15:54:481 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received an active event in Disable state.

  IPHC negotiation started.

  Sent a config REQ (F = 1) packet, FSM state changed to I1.

*// 串口Serial2/1/0，虚电路 100，IPHC协商状态机在Disable状态收到激活事件，IPHC开始协商，发送REQ (F = 1)报文，进入I1状态*

\*Mar 25 02:15:54:496 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received a config REQ (F = \*) packet in I1 state.

  Sent a config ACK packet, FSM state changed to I3.

*// 串口Serial2/1/0，虚电路100，IPHC协商状态机在I1状态收到REQ (F = \*)报文，并发送ACK报文，进入I3状态*

\*Mar 25 02:15:57:578 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received a negotiation timer timeout (+) event in I3 state.

  Sent a config REQ (F = 0) packet, FSM state remains in I3.

*// 串口Serial2/1/0，虚电路，IPHC协商状态机在I3状态收到协商定时器超时(+)事件，并发送REQ (F = 0)报文，保持I3状态*

\*Mar 25 02:15:57:580 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received a config ACK packet in I3 state.

  FSM state changed to Operational.

  IPHC negotiation done.

*// 串口Serial2/1/0，虚电路100，IPHC协商状态机在I3阶段收到ACK报文，进入Operational状态，协商完成*

·Router B

\*Mar 25 02:15:54:495 2014 RouterB FR/7/IPHC: -MDC=1;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received an active event in Disable state.

  IPHC negotiation started.

  Sent a config REQ (F = 1) packet, FSM state changed to I1.

*// 串口Serial2/1/0，虚电路100，IPHC协商状态机在Disable状态收到激活事件，IPHC开始协商，发送REQ (F = 1)，进入I1状态*

\*Mar 25 02:15:54:496 2014 RouterB FR/7/IPHC: -MDC=1;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received a config ACK packet in I1 state.

  FSM state changed to I2.

*// 串口Serial2/1/0，虚电路100，IPHC协商状态机在I1状态收到ACK报文，进入I2状态*

\*Mar 25 02:15:57:580 2014 RouterB FR/7/IPHC: -MDC=1;

Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:

  Received a config REQ (F = 0) packet in I2 state.

  Sent a config ACK packet, FSM state changed to Operational.

  IPHC negotiation done.

*// 串口Serial2/1/0，虚电路100，IPHC状态机在I2状态收到REQ (F = 0)报文，并发送ACK报文，进入Operational状态，协商完成*

\# Router A与Router B通过串口连接，链路层协议配置为FR，两端都开启IPHC压缩功能，并配置了IP地址。打开Router B的帧中继IPHC TCP头压缩调试信息开关。当Router A以Telnet方式登录Router B时，Router B上TCP头压缩解压缩调试信息如下：

\<RouterB\> debugging fr compression iphc tcp

\*Mar 14 05:51:29:849 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.

*// 串口Serial2/1/0，虚电路16接收到IPHC报文，报文长度为56*

\*Mar 14 05:51:29:851 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: received FULL_HEADER, connect ID 0, checksum 0xd572, seq 734446218

*[// TCP*]*报文压缩信息：报文流ID为0，接收到FULL_HEADER报文，校验和为0xd572，序列号为734446218*

\*Mar 14 05:51:29:852 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 38.

*// 串口Serial2/1/0，虚电路16接收到IPHC报文，报文长度为38*

\*Mar 14 05:51:29:853 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: received COMPRESSED_TCP, connect ID 0, checksum 0x9623, seq 734446218

*[// TCP*]*报文压缩信息：报文流ID为0，接收到COMPRESSED_TCP报文，校验和为0x9623，序列号为734446218*

\*Mar 14 05:51:29:854 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: sent FULL_HEADER, connect ID 0, checksum 0xd55a, seq 513970195

*[// TCP*]*报文压缩信息：报文流ID为0，发送FULL_HEADER报文，校验和为0xd55a，序列号为513970195*

\*Mar 14 05:51:29:854 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.

*[ // *]*串口Serial2/1/0，虚电路为16收到IPHC报文，报文长度为56*

\*Mar 14 05:51:29:872 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: sent COMPRESSED_TCP, connect ID 0, checksum 0x820e, seq 513970195

*[// TCP*]*报文压缩信息：报文流ID为0，发送COMPRESSED_TCP报文，校验和为0x820e，序列号为513970195*

\*Mar 14 05:51:29:872 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 41.

*// 串口Serial2/1/0，虚链路16，发送IPHC报文，报文长度41*

\*Mar 14 05:51:29:873 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 36.

*[//*]*串口Serial2/1/0，虚链路16收到IPHC报文，报文长度为56*

\*Mar 14 05:51:29:874 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: received COMPRESSED_TCP, connect ID 0, checksum 0xb78f, seq 734446200

*[// TCP*]*报文压缩信息：报文流ID为0，接收到COMPRESSED_TCP报文，校验和为0xb78f，序列号为734446200*

\*Mar 14 05:51:29:874 2014 RouterB IPHC/7/EVENT: -MDC=1-Slot=2;

 THC ERROR: Delta th_win code error, connect ID 0

*[// TCP*]*报文压缩错误信息：报文流ID为0，在压缩TCP报文过程中Delta Window字段编码错误*

\*Mar 14 05:51:29:875 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;

 THC: sent FULL_HEADER, connect ID 0, checksum 0xd4fa, seq 513970159

*[// TCP*]*报文压缩信息：报文流ID为0，发送FULL_HEADER报文，校验和为0xd4fa，序列号为513970159*

\*Mar 14 05:51:29:875 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;

Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.

*// 串口Serial2/1/0，虚电路16发送IPHC报文，报文长度为56*

