<!-- CMD-INDEX
  debugging ancp                      | 用户视图             | L5
-->

**ANCP调试命令 \-- ANCP调试命令 \-- debugging ancp**

------------------------------------------------------------------------

**[debugging ancp**]命令用来打开ANCP的调试信息开关。

**[undo debugging ancp**]命令用来关闭ANCP的调试信息开关。

【命令】

**[debugging ancp**[ { **all** \| **error** \| **event** \| **packet** }]]

**[undo debugging ancp**[ { **all** \| **error** \| **event** \| **packet** }]]

【缺省情况】

ANCP的所有调试信息开关均处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

**[packet**]：表示报文调试信息开关。

【使用指导】

表1-1 debugging ancp error命令输出信息描述表

字段

描述

Failed to send a(an) *type* message to neighbor *neighbor-name*.

向邻居*neighbor-name*发送*type*类型的报文失败。其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

·OAM Port Management：线路检测管理报文

·Line Config Port Management：线路配置管理报文

·Generic Response：一般应答报文

Failed to send a SYN message.

发送SYN报文失败

Capability not supported(*CapType*).

不支持的能力集，其中*CapType*为当前能力集字段的取值

Interface *interfaceName* with socket *sock* discarded the received data: Invalid encapsulating header.

接口名为*interfaceName*，Socket为*sock*的通信接口丢弃包含有不合法的封装头的接收数据

Discarded a message: Invalid version.

收到报文中*version*（版本号）不合法，丢弃

Discarded a message: Unknown message type.

收到未知类型的报文，丢弃

Discarded a message: Insufficient length.

报文长度不够，丢弃

Discarded a message from neighbor *neighbor-name*: Invalid version.

丢弃来自邻居*neighbor-name*的一个报文，因为其中的version（版本号）不合法

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Result field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Result（结果域）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

·Adjacency Update：邻接更新报文

·Generic Response：一般应答报文

Discarded a *type* message from neighbor *neighbor-name*: Invalid ResultCode field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的ResultCode（结果代码域）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Generic Response：一般应答报文

·Port Management：线路管理报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Partition ID field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Partition ID（分区ID）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Generic Response：一般应答报文

·Port Management：线路管理报文

·Adjacency Update：邻接更新报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid I Flag and SubMessage Number field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的I Flag和SubMessage Number（分片标记和分片序列号）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Generic Response：一般应答报文

·Port Management：线路管理报文

·Adjacency Update：邻接更新报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid length value in the message header.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为报文头中的length（长度）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Generic Response：一般应答报文

·Port Management：线路管理报文

·Adjacency Update：邻接更新报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Transaction ID field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Transaction ID（业务ID）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

·Adjacency Update：邻接更新报文

Discarded a *type* message from neighbor *neighbor-name*: Invalid Message Type field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Message Type（消息类型）不合法，与报文头中的不一致。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Tech Type field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Tech Type（线路类型）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACk：RSTACK报文

Discarded a *type* message from neighbor *neighbor-name*: Invalid \# of TLVs field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的\# of TlVs（扩展数据域中的TLV个数）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

Discarded a *type* message from neighbor *neighbor-name*: Invalid Extension Block length field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Extension Block length（扩展数据域长度）不合法。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

Discarded a Port Management message from neighbor *neighbor-name*: Invalid Function field.

丢弃来自邻居*neighbor-name*的线路管理报文，因为其中的Function（线路检测与线路配置标示）不合法

Discarded a Port Management message from neighbor *neighbor-name*: Invalid X-Function field.

丢弃来自邻居*neighbor-name*的线路管理报文，因为其中的X-Function（对Function的补充说明）不合法

Discarded a *type* message from neighbor *neighbor-name*: Insufficient length.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为报文长度不够。其中*type*的类型可以为：

·Port Up：线路上线报文

·Port Down：线路下线报文

·Port Management：线路管理报文

Discarded a Port Management message from neighbor *neighbor-name*: The neighbor does not support Line Config Capability.

丢弃来自邻居*neighbor-name*的线路管理报文，因为该邻居不支持线路配置能力

Discarded a Port Management message from neighbor *neighbor-name*: The neighbor does not support OAM Capability.

丢弃来自邻居*neighbor-name*的线路管理报文，因为该邻居不支持OAM（线路检测）能力

Discarded a *type* message from neighbor *neighbor-name*: The neighbor does not support Topology Discovery Capacity.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为该邻居不支持线路拓扑发现能力。其中，*type*的类型可以是*：*

·Port Up：线路上线报文

·Port Down：线路下线报文

Discarded a(an) Unknown message from neighbor *neighbor-name*: Invalid Code field.

丢弃来自邻居*neighbor-name*的未知类型的报文，因为其中的Code（邻接报文类型）不合法

Discarded a SYN message from neighbor *neighbor-name*: Invalid M flag.

丢弃来自邻居*neighbor-name*的SYN报文，因为其中的M flag（SYN报文发起标示）不合法

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid Capability Fields.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的Capability Fields（能力域）不合法。其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid PFlag.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的P Flag（邻接建立类型）不合法。其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

Discarded a(an) *type* message from neighbor *neighbor-name*: Invalid PType field.

丢弃来自邻居*neighbor-name*的*type*类型的报文，因为其中的P Type（分区使用标志及协商方式）不合法。其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

Not enough memory resources.

内存资源不足

Failed to add a circuit entry: Not enough memory resources.

由于内存资源不足，添加线路结点失败

Not enough TCP socket resources.

TCP socket资源不足

表1-2 debugging ancp event命令输出信息描述表

字段

描述

Established the adjacency with neighbor *neighbor-name*.

与邻居*neighbor-name*建立邻接关系

The FSM state for neighbor *neighbor-name* with peer ID *H-H-H* changed from *state1* to *state2.*

名为*neighbor-name*，Peer ID为*H-H-H*的邻居状态机状态从*state1*迁移到*state2*。其中，*state1、state2*的取值可以是：

·SYNSENT：SYNSENT状态

·SYNRCVD：SYNRECV状态

·ESTAB：ESTAB状态

Halted the adjacency relationship with neighbor *neighbor-name*, because the set of Capabilities is empty.

由于协商的能力集为空，断开与邻居*neighbor-name*的邻接关系

Interface *interfaceName* with socket *sock* stopped adjacency establishment, because it failed to receive a response from the peer after completing retransmission in *SYNSENT* state.

通信接口（源接口名为*interfaceName*，socket为*sock*）在SYNSENT状态下完成超时重传后，还未收到对端回应，中断邻接建立过程

Halted the adjacency relationship with neighbor *neighbor-name*, due to failure to receive a response from the peer after completing retransmission in *states* state.

在*states*状态下完成超时重传后，还未收到来自对端的回应，断开与邻居*neighbor-name*的邻接关系。其中*states*的取值为：

·SYNSENT：SYNSENT状态

·SYNRCVD：SYNRECV状态

Halted the adjacency relationship with neighbor *neighbor-name*, due to failure to receive ACK messages from the peer within three periods of the adjacency timer.

由于三个邻接定时器周期内未收到邻居*neighbor-name*对端回应ACK报文，断开邻接关系

Halted the adjacency relationship with neighbor *neighbor-name*, because the peer disconnected the TCP connection.

由于邻居*neighbor-name*对端关闭TCP连接，断开邻接关系

Interface *interfaceName* with socket *sock* halted the adjacency relationship, because the peer disconnected the TCP connection.

通信接口（接口名为*interfaceName*，socket为*sock*）的对端关闭TCP连接，断开邻接关系

Interface *interfaceName* with socket *sock* halted the adjacency relationship after receiving an EPOLLHUP/EPOLLERR signal.

通信接口（源接口名为*interfaceName*，socket为*sock*）由于收到EPOLLHUP/EPOLLERR（EPOLL挂起/EPOLL错误）信号，断开邻接关系

Halted the adjacency relationship with neighbor *neighbor-name* after receiving an EPOLLHUP/EPOLLERR signal.

由于收到EPOLLHUP/EPOLLERR（EPOLL挂起/EPOLL错误）信号，断开与邻居*neighbor-name*的邻接关系

表1-3 debugging ancp packet命令输出信息描述表

字段

描述

Received a(an) *type* message from neighbor *neighbor-name*.

收到邻居*neighbor-name*的一个*type*类型的报文

其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

·Port Management：线路管理报文

·Port Up：线路上线报文

·Port Down：线路下线报文

·Adjacency Update：邻接更新报文

·Generic Response：一般应答报文

·Provisioning：信息提供报文

·Unknown：未知报文

Sent a(an) *type* message to neighbor *neighbor-name*.

向邻居*neighbor-name*发送一个*type*类型的报文。

其中*type*的类型可以为：

·SYN：SYN报文

·SYNACK：SYNACK报文

·ACK：ACK报文

·RSTACK：RSTACK报文

·Port Management：线路管理报文

·Generic Response：一般应答报文

Identifier: *identifier*

标识符，用于标示GSMP协议或ANCP协议，必须为：0x880c

Length: *length*

ANCP消息的长度，不包括4字节的封装头长度

Version: *version*

ANCP协议版本域

Message Type: *message-type*

ANCP协议消息类型，总共有7种，取值为：

·0xa：Adjacency Protocol，邻接报文

·0x32：Port Management，线路管理报文

·0x80：Port Up，线路上线报文

·0x81：Port Down，线路下线报文

·0x85：Adjacency Update，邻接更新报文

·0x91：Generic Response，一般应答报文

·0x93：Provisioning，信息提供报文

M flag and Code: *m-code*

邻接报文中M Flag和Code，共8位，其中，M Flag为第一位，用于标识SYN报文发起者身份，0表示AN，1表示BRAS；其余7位为Code，表示邻接消息类型，取值为1、2、3、4，依次代表SYN、SYNACK、ACK、RSTACK报文。正常情况下取值为：

·0x81：BRAS端发出的SYN报文

·0x01：AN端发出的SYN报文

·0x02：SYNACK报文

·0x03：ACK报文

·0x04：RSTACK报文

Sender Name: *sender-name*

发送端的标示

Receiver Name: *receiver-name*

接收端的标示

Sender Port: *sender-port*

发送端端口号

Receiver Port: *receiver-port*

接收端端口号

PType: *ptype*

邻接报文中PType字段，用于确定是否使用分区及分区ID的协商方式，取值为：

·0x0：不支持分区

·0x1：固定的分区请求

·0x2：固定的分区分配

P Flag: *p-flag*

邻接建立类型，取值为：

·0x1：新建邻接

·0x2：恢复邻接

Sender Instance: *sender-instance*

发送端实例号

Partition ID: *partition-id*

分区ID

Receiver Instance: *receiver-instance*

接收端实例号

\# of Caps: *of-caps*

能力域个数

Total Length: *total-length*

邻接报文中能力域总字节长度

Result: *result*

业务报文中的结果域，具体取值和报文类型有关

Result Code: *code*

业务报文中的结果代码域，具体取值和Result（结果域）有关

Length: *length*

业务报文中的长度字段

Transaction ID: *transaction-id*

业务ID，发起一次请求时选择的随机数，用来标识一次业务请求过程

Function: *function*

Port Management报文中的Function字段取值为：

·0x8：Line Configuration（线路配置）

·0x9：OAM（线路检测）

Extension Block length: *extension-block-length*

扩展数据域长度

【举例】

\# 在BARS设备上配置全局源接口、创建邻居名为dslam1的邻居并设置peer-id为2-2-2，最后使能ANCP功能。打开ANCP的所有调试开关。DSLAM与BARS设备建立邻接过程后，DSLAM端开始上报线路信息。

\<Syaname\> terminal monitor

The current terminal is enabled to display logs.

\<Syaname\> terminal debugging

The current terminal is enabled to display debugging logs.

\<Syaname\> debugging ancp all

\<Syaname\>\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) SYN message.

    Identifier: 0x880c    Length: 0x30

    Version: 0x32     Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x81

    Sender Name: 00-11-22-00-00-01    Receiver Name: 00-00-00-00-00-00

    Sender Port: 0x0     Receiver Port: 0x0

    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5

    Partition ID: 0x0     Receiver Instance: 0x0

    \# of Caps: 0x3     Total Length: 0xc

*[// TCP*]*连接建立，发送一个SYN报文*

\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) SYN message.

    Identifier: 0x880c     Length: 0x30

    Version: 0x32     Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x01

    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-00-00-00-00-00

    Sender Port: 0x0     Receiver Port: 0x0

    PType: 0x0, P Flag: 0x1     Sender Instance: 0x1

    Partition ID: 0x0     Receiver Instance: 0x0

    \# of Caps: 0x3     Total Length: 0xc

*// 收到一个SYN报文*

\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) SYNACK message to neighbor dslam1.

    Identifier: 0x880c     Length: 0x30

    Version: 0x32     Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x02

    Sender Name: 00-11-22-00-00-01     Receiver Name: 00-02-00-02-00-02

    Sender Port: 0x0     Receiver Port: 0x0

    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5

    Partition ID: 0x0     Receiver Instance: 0x1

    \# of Caps: 0x3     Total Length: 0xc

*// 向邻居dslam1发送一个SYNACK报文*

\*Jul 16 11:35:07:540 2013 Syaname ANCP/7/EVENT: -MDC=1; The FSM state for neighbor dslam1 with peer ID 0002-0002-0002 changed from SYNSENT to SYNRCVD.

*// 邻居名为dslam1，peer-id为2-2-2的邻居，状态机由SYNSENT状态迁移到SYNRCVD状态*

\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) SYNACK message from neighbor dslam1.

    Identifier: 0x880c     Length: 0x30

    Version: 0x32     Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x02

    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-11-22-00-00-01

    Sender Port: 0x0     Receiver Port: 0x0

    PType: 0x0, P Flag: 0x1     Sender Instance: 0x1

    Partition ID: 0x0     Receiver Instance: 0x5

    \# of Caps: 0x3     Total Length: 0xc

*// 收到邻居dslam1发送的一个SYNACK报文*

\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/PACKET: -MDC=1; Sent a(an) ACK message to neighbor dslam1.

    Version: 0x32     Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x03

    Sender Name: 00-11-22-00-00-01     Receiver Name: 00-02-00-02-00-02

    Sender Port: 0x0     Receiver Port: 0x0

    PType: 0x0  P Flag: 0x1     Sender Instance: 0x5

    Partition ID: 0x0     Receiver Instance: 0x1

    \# of Caps: 0x3     Total Length: 0xc

*// 向邻居dslam1发送一个ACK报文*

\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/EVENT: -MDC=1; The FSM state for neighbor dslam1 with peer ID 0002-0002-0002 changed from SYNRCVD to ESTAB.

*// 邻居名为dslam1，peer-id为2-2-2的邻居，状态机由SYNRCVD状态迁移到ESTAB状态*

\*Jul 16 11:35:07:541 2013 Syaname ANCP/7/EVENT: -MDC=1; Established the adjacency with neighbor dslam1.

*// 与邻居dslam1，建立邻接关系*

\*Jul 16 11:35:07:542 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) ACK message from neighbor dslam1.

    Identifier: 0x880c    Length: 0x30

    Version: 0x32    Message Type: 0xa

    Timer: 0xfa     M flag and Code: 0x03

    Sender Name: 00-02-00-02-00-02     Receiver Name: 00-11-22-00-00-01

    Sender Port: 0x0    Receiver Port: 0x0

    PType: 0x0 P Flag: 0x1     Sender Instance: 0x1

    Partition ID: 0x0     Receiver Instance: 0x5

    \# of Caps: 0x3     Total Length: 0xc

*// 收到邻居dslam1发送的一个ACK报文*

\*Jul 16 11:35:09:043 2013 Syaname ANCP/7/PACKET: -MDC=1; Received a(an) Port Up message from neighbor dslam1.

    Identifier: 0x880c     Length: 0xc0

    Version: 0x32     Message Type: 0x50

    Result: 0x0     Code: 0x0

    Partition ID: 0x0     Transaction ID: 0x0

    Length: 0xc0    \# of TLVs: 0x2     Extension Block length: 0x98

*[// DSLAM*]*端开始上报线路信息。BARS端邻居名为dslam1的邻居，收到一个Port Up报文*

