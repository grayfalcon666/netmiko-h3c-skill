<!-- CMD-INDEX
  auto-close                          | 终端模板视图           | L45
  auto-link                           | 终端模板视图           | L95
  bind vpn-instance                   | 终端模板视图           | L145
  display rta                         | 任意视图             | L193
  display rta relay statistics        | 任意视图             | L575
  display rta relay status            | 任意视图             | L657
  driverbuf save                      | 终端模板视图           | L737
  driverbuf size                      | 终端模板视图           | L783
  idle-timeout                        | 终端模板视图           | L833
  link-protocol stlp                  | 接口视图             | L879
  resetkey                            | 终端模板视图           | L921
  reset rta connection                | 用户视图             | L969
  reset rta relay statistics          | 用户视图             | L1007
  reset rta statistics                | 用户视图             | L1039
  rta relay buffer-size               | 系统视图             | L1075
  rta relay disconnect                | 系统视图             | L1123
  rta relay enable                    | 系统视图             | L1161
  rta relay listen-port               | 系统视图             | L1201
  rta relay tcp                       | 系统视图             | L1255
  rta relay tcp keepalive             | 系统视图             | L1309
  rta relay tcp nodelay               | 系统视图             | L1361
  rta rtc compatibility               | 系统视图             | L1407
  rta rtc-server listen-port          | 系统视图             | L1447
  rta server enable                   | 系统视图             | L1495
  rta source-ip                       | 系统视图             | L1535
  rta template                        | 系统视图             | L1583
  rta terminal                        | 异步串口视图           | L1629
  rta terminal backup                 | 接口视图             | L1679
  rtc-multipeer remote                | 终端模板视图           | L1727
  sendbuf bufsize                     | 终端模板视图           | L1793
  sendbuf threshold                   | 终端模板视图           | L1843
  tcp                                 | 终端模板视图           | L1893
  update changed-config               | 终端模板视图           | L1969
  vty description                     | 终端模板视图           | L2013
  vty hotkey                          | 终端模板视图           | L2061
  vty password                        | 终端模板视图           | L2111
  vty rtc-client remote               | 终端模板视图           | L2171
  vty rtc-client remote remote-port   | 终端模板视图           | L2229
  vty rtc-multipeer                   | 终端模板视图           | L2287
  vty rtc-server remote               | 终端模板视图           | L2343
  vty rtc-server remote udp           | 终端模板视图           | L2397
-->

**RTC终端接入 \-- RTC终端接入命令 \-- auto-close**

------------------------------------------------------------------------

**[auto-close**]命令用来配置自动断链时间。

**[undo auto-close**]命令用来恢复缺省情况。

【命令】

**[auto-close** *time*]

**[undo auto-close**]

【缺省情况】

自动断链时间为0，即不自动断链。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：自动断链时间，取值范围为5～240，单位为秒。

【使用指导】

终端接入具有终端自动断链功能，用户可以在终端模板视图下启用并配置该终端的自动断链时间。当用户终端设备和终端接入设备断开连接后，终端处于down状态，在经过设定的时间后，RTC Client自动与RTC Server断开TCP连接。如果不配置终端自动断链功能，该TCP连接将被一直保持。

【举例】

\# 配置自动断链时间为10秒。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc auto-close 10

【相关命令】

·**auto-link**

**RTC终端接入 \-- RTC终端接入命令 \-- auto-link**

------------------------------------------------------------------------

**[auto-link**]命令用来配置自动建链的时间。

**[undo auto-link**]命令用来恢复缺省配置。

【命令】

**[auto-link ***time*]

**[undo auto-link**]

【缺省情况】

自动建链时间为0，即需要手动建链。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：自动建链时间，取值范围为5～240，单位为秒*。*

【使用指导】

终端接入具有终端自动建链功能，用户可以在终端模板视图下启用并配置终端的自动建链时间。当终端的物理连接完好时，经过指定时间后，RTC Client将自动与远端的RTC Server建立TCP连接。如果没有配置终端自动建链时间，则终端需要通过手动方式建链，等待用户在终端上输入字符（除热键、终端的特殊字符外，特殊字符即终端直接处理的字符，如\<Shift+F2\>），RTC Client才会与RTC Server建立TCP连接。

【举例】

\# 配置自动建链时间为10秒。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc auto-link 10

【相关命令】

·**auto-close**

**RTC终端接入 \-- RTC终端接入命令 \-- bind vpn-instance**

------------------------------------------------------------------------

**[bind vpn-instance**]命令用来配置终端模板绑定的VPN实例。

**[undo bind vpn-instance**]命令用来取消绑定的VPN实例。

【命令】

**[bind vpn-instance** *vpn-name*]

**[undo bind vpn-instance**]

【缺省情况】

终端模板没有绑定VPN实例。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vpn-name*]：MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写*。*

【使用指导】

·该配置用于RTC Client同时做MPLS PE的情况。将配置了本命令的终端模板应用到异步串口下，则该异步串口所对应的终端也就绑定了该VPN实例，这样RTC Client就能将不同的终端划分到不同的VPN域里。RTC Server如果不配置本命令，它能够接受来自任何VPN的连接请求。

·一个模板只能绑定一个实例，如果多次使用该命令绑定实例，最新的配置有效。

【举例】

\# 配置终端模板绑定的VPN实例为vpn1。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc bind vpn-instance vpn1

**RTC终端接入 \-- RTC终端接入命令 \-- display rta**

------------------------------------------------------------------------

**[display rta**]命令用来显示终端接入相关的信息。

【命令】

**[display rta **[{ **all** \| **statistics** \| *terminal-number* { *vty-number* \| **brief** \| **detail** \| **statistics** } }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有终端的信息。

**[statistics**]：显示终端的统计信息。

*[terminal-number*]：显示指定终端的信息。终端号，取值范围为1～255。

*[vty-number*]：显示指定虚终端的信息。虚终端号，取值范围为0～7。

**[brief**]：显示指定终端的简要信息。

**[detail**]：显示指定终端的详细信息。

【举例】

\# 显示终端号为1的VTY1的信息。

\<Sysname\> display rta 1 1

VTY 1

    APP index: 0

    APP type: RTC Client

    APP state: Unlinked

    Remote IP: 192.168.0.110

    Source IP: Not configured

    Actual source IP: \--

    Remote port: 9010

    Local port: Not configured

    Connection duration: 00:00:00

表1-1 display rta terminal-number vty-number命令显示信息描述表

字段

描述

APP index

应用的索引

APP type

应用的类型，取值包括RTC Client、RTC Server

APP state

应用的状态，取值为：

·Unlinked：表示连接未建立

·Linking：表示连接建立中（此状态只有TCP Client存在）

·Linked：表示连接已建立

·\--：表示当模板不存在APP

Remote IP

远端终端接入设备的IP地址

Source IP

源IP地址，即在终端模板下为VTY配置的源IP地址

Actual source IP

实际源IP地址，即建立连接时使用的源IP地址。"\--"表示连接还未建立。

Remote port

远端终端接入设备的监听端口

Local port

本端终端接入设备的监听端口

Connection duration

应用连接保持时间（时：分：秒）

\# 显示1号终端的简要信息。

\<Sysname\> display rta 1 brief

TTY 1

    Interface used         :  Async2/2/0

    Current state          :  Up

    Current APP            :  0

    APP type               :  RTC client

    APP name               :  Not configured

    APP state              :  Unlinked

    Socket recvBuf Size    :  2048 bytes

    Socket sendBuf Size    :  2048 bytes

    TTY auto-link          :  10 seconds

    TTY close-link         :  10 seconds

    TTY receive bytes      :  1371 bytes

    TTY send bytes         :  63696 bytes

    Last receive time      :  19:39:33

    Last send time         :  03:39:34

    Current APP recveive   :  55280 bytes

    Current APP send       :  1524 bytes

    Time from APP is linked: 00:00:00

    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

    VTY       APP       Type       State

    0         0         RTC client Unlinked

表1-2 表1-2 display rta terminal-number brief命令显示信息描述表

字段

描述

TTY 1

终端号为1的TTY终端

Interface used

终端1对应的物理接口

Current state

终端的当前状态，取值为：

·Down：物理Down

·Up：物理Up

Current APP

当前应用

APP type

应用类型

APP name

应用名称

APP state

应用状态

Socket recvBuf size

TCP接收缓存大小

Socket sendBuf size

TCP发送缓存大小

TTY auto-link

自动建链时间

TTY close-link

自动断链时间

TTY recieve bytes

接收数据的字节数

TTY send bytes

发送数据的字节数

Last receivev time

上一次接收数据的时间

Last send time

上一次发送数据的时间

Current APP receive

当前应用接收的数据字节数

Current APP send

当前应用发送的数据字节数

Time from APP is linked

应用连接保持时间

VTY       APP       Type       State

终端配置的虚终端列表，其中：

·VTY：表示虚终端号

·APP：表示应用

·Type：表示应用类型

·State：表示应用状态

\# 显示终端号为1的终端的统计信息。

\<Sysname\> display rta 1 statistics

TTY 1

  Received from terminal: 1231

  Send to terminal:       348

  Received from remote:   8342

  Send to remote:         7342

  VTY 0

    Receive from terminal: 1231            Last receive time: 03:08:29

    Send to terminal:      348             Last send time:    01:10:30

    Receive from remote:   8342            Last receive time: 17:21:25

    Send to remote:        7342            Last send time:    09:44:43

表1-3 display rta terminal-number statistics命令显示信息描述表

字段

描述

Receive from terminal

从终端接收的数据大小（单位为字节）

Send to terminal

发送到终端的数据大小（单位为字节）

Receive from remote

从远端接收的数据大小（单位为字节）

Send to remote

发送到远端的数据大小（单位为字节）

Last receive time

最近一次接收时间（时：分：秒），"\--"表示未收到过数据

Last send time

最近一次发送时间（时：分：秒），"\--"表示未发送过数据

\# 显示终端接入的所有信息。

\<Sysname\> display rta all

TTYID    TTY State     Current APP    APP Type    APP State

1        Up            0              RTC client  Unlinked

表1-4 display rta all命令显示信息描述表

字段

描述

TTYID

终端号

TTY State

终端状态

Current APP

当前应用

APP Type

应用类型

APP State

应用状态

\# 显示终端接入的统计信息。

\<Sysname\> display rta statistics

    RTA template number: 2

    RTA TTY number: 1

    RTA APP number: 1

    RTA listen port number: 0

表1-5 display rta statistics命令显示信息描述表

字段

描述

RTA template number

终端接入设备上配置的终端模板数

RTA TTY number

终端接入设备上配置的终端数

RTA APP number

配置终端后生成的应用数

RTA listen port number

终端接入设备正在侦听的端口数

【相关命令】

·**display rta relay statistics**

·**display rta relay status**

**RTC终端接入 \-- RTC终端接入命令 \-- display rta relay statistics**

------------------------------------------------------------------------

**[display rta relay statistics**]命令用来显示中继透传的数据转发统计信息。

【命令】

**[display rta relay statistics**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

中继服务器在向客户端转发数据时会实时统计转发的字节数和发送的报文数。

【举例】

\# 显示中继透传的数据转发统计信息。

\<Sysname\> display rta relay statistics

Server   Port    Client-IP    Recv-Packets Recv-Bytes Sent-Packets Sent-Bytes

0        1026    1.1.1.2      15           190        30           370

0        1026    1.1.1.3      15           110        35           421

1        1027    1.1.1.4      0            0          0            0

表1-6 display rta relay statistics命令显示信息描述表

字段

描述

Server

转发组ID

Port

转发组监听端口

Client-IP

客户端IP地址

Recv-Packets

从该客户端收到的报文数

Recv-Bytes

从该客户端收到的数据字节数

Sent-Packets

发向该客户端报文数

Sent-Bytes

发向该客户端数据字节数

【相关命令】

·**display rta**

·**display rta relay status**

**RTC终端接入 \-- RTC终端接入命令 \-- display rta relay status**

------------------------------------------------------------------------

**[display rta relay status**]命令用来显示中继服务接受的所有客户端的连接状态。

【命令】

**[display rta relay status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

对于每个转发组（以端口区分）最多可以接受10个客户端的连接。

【举例】

\# 显示中继服务接受的客户端的连接状态。

\<Sysname\> display rta relay status

Server-ID   Port   Client-ID    Client-IP        State

0           1026   0            1.1.1.2          Linked

0           1026   1            1.1.1.3          Linked

1           1027   0            1.1.1.4          Linking

1           1027   2            1.1.1.6          Linked

表1-7 display rta relay status命令显示信息描述表

字段

描述

Server-ID

转发组ID

Port

转发组监听端口

Client-ID

客户端在转发组内的标识

Client-IP

客户端IP地址

State

客户端协商状态：

·Linking：客户端还未发送协商字段

·Linked：客户端已完成协商过程

【相关命令】

·**display rta**

·**display rta relay statistics**

**RTC终端接入 \-- RTC终端接入命令 \-- driverbuf save**

------------------------------------------------------------------------

**[driverbuf save**]命令用来配置终端接入设备在TCP连接建立后不清空终端接收缓存。

**[undo driverbuf save**]命令用来恢复缺省情况。

【命令】

**[driverbuf save**]

**[undo driverbuf save**]

【缺省情况】

终端接入设备在TCP连接建立后清空终端接收缓存。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

终端接收缓存是指在终端接入设备上用于存放终端数据的缓存。

【举例】

\# 配置在TCP连接建立后不清空终端接收缓存。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc driverbuf save

【相关命令】

·**drive****rbuf size**

**RTC终端接入 \-- RTC终端接入命令 \-- driverbuf size**

------------------------------------------------------------------------

**[driverbuf size**]命令用来配置终端接收缓存的大小。

**[undo driverbuf size**]命令用来恢复缺省值。

【命令】

**[driverbuf size** *size*]

**[undo driverbuf size**]

【缺省情况】

终端接收缓存大小为8KB。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：缓存大小，取值范围为8～32，单位为KB*。*

【使用指导】

只有将模板重新应用到接口下，该命令配置才能生效。

【举例】

\# 配置终端缓存大小为8KB。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc driverbuf size 8

【相关命令】

·**drivebuf save**

**RTC终端接入 \-- RTC终端接入命令 \-- idle-timeout**

------------------------------------------------------------------------

**[idle-timeout**]命令用来设置终端接入TCP连接的空闲超时时间。

**[undo idle-timeout**]用来恢复缺省情况。

【命令】

**[idle-timeout ***seconds*]

**[undo idle-timeout**]

【缺省情况】

连接永不超时。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：空闲超时时间，取值范围为10～3600，单位为秒。

【使用指导】

如果设置了空闲超时时间，终端接入连接在设置的时间内没有接收到任何数据，则断开当前的连接。

【举例】

\# 配置终端接入的空闲超时时间为1000秒。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc idle-timeout 1000

**RTC终端接入 \-- RTC终端接入命令 \-- link-protocol stlp**

------------------------------------------------------------------------

**[link-protocol stlp**]命令用来配置接口封装的链路层协议为STLP。

**[undo link-protocol stlp**]命令用来恢复缺省情况。

【命令】

**[link-protocol stlp**]

**[undo link-protocol stlp**]

【缺省情况】

除以太网接口、VLAN接口外，其它接口封装的链路层协议均为PPP。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

STLP为链路层协议，用于远程终端连接同步透传功能。

【举例】

\# 配置接口Serial2/1/0封装STLP协议。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol stlp

**RTC终端接入 \-- RTC终端接入命令 \-- resetkey**

------------------------------------------------------------------------

**[resetkey**]命令用来设置终端复位的热键。

**[undo resetkey**]用来取消配置的热键。

【命令】

**[resetkey ***ascii-code&\<1-3\>*]

**[undo resetkey**]

【缺省情况】

没有设置终端复位热键。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ascii-code&\<1-3\>*]：热键的ASCII值，取值范围为1～255，&\<1-3\>表示前面的参数最多可以输入3次。

【使用指导】

·如果设置了终端复位热键，当终端出现异常时，在终端上按终端复位热键后，RTC Client断开并重新建立与RTC Server的TCP连接。

·需要注意的是，热键的ASCII值不能与设备上已设置的别的功能热键的ASCII值相同，否则，热键的功能将冲突。另外，在终端显示大量数据时使用热键，会影响热键的响应速度。

【举例】

\# 配置终端复位的热键为\<Ctrl+A\>，其对应的ASCII码为1。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc resetkey 1

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta connection**

------------------------------------------------------------------------

**[reset** **rta** **connection**]命令用来强制断开指定终端的虚终端对应的TCP连接。

【命令】

**[reset rta connection ***terminal-number vty-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[terminal-number*]：终端号，取值范围为1～255。

*[vty-number*]：虚终端号，取值范围为0～7。

【举例】

\# 断开终端号为1的虚终端1的TCP连接。

\<Sysname\> reset rta connection 1 1

【相关命令】

·**reset rta relay statistics**

·**reset rta statistics**

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta relay statistics**

------------------------------------------------------------------------

**[reset rta relay statistics**]命令用来清除连接到中继服务器的所有客户端的报文统计信息**。**

【命令】

**[reset rta relay statistics**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除客户端的报文统计信息。

\<Sysname\> reset rta relay statistics

【相关命令】

·**reset rta connection**

·**reset rta statistics**

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta statistics**

------------------------------------------------------------------------

**[reset rta statistics**]命令用来清除指定终端的统计信息*。*

【命令】

**[reset rta statistics ***terminal-number*]

【视图】

用户视图

【缺省用户角色】

network-admin

network-operator

【参数】

*[terminal-number*]：终端号，取值范围为1～255。

【举例】

\# 清除终端号为1的终端的所有统计信息。

\<Sysname\> reset rta statistics 1

【相关命令】

·**reset rta connection**

·**reset rta relay statistics**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay buffer-size**

------------------------------------------------------------------------

**[rta relay buffer-size**]命令用来配置中继透传服务客户端转发缓存大小。

**[undo rta relay buffer-size**]命令用来恢复缺省情况。

【命令】

**[rta relay buffer-size** *buffer-size*]

**[undo rta relay buffer-size**]

【缺省情况】

客户端转发缓存大小为8KB。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[buffer-size*]：客户端转发缓存大小，取值范围为1～64，单位为KB。

【使用指导】

如果客户端待发送报文数达到配置的缓存大小，则新增数据会覆盖旧的数据。该配置和**rta relay tcp sendbuf-size**不同之处在于后者设置的是传输层报文发送缓冲区的大小，如果后者设置的值过小，会影响发送效率但不会丢包。

【举例】

\# 配置中继透传服务客户端转发缓存大小为2KB。

\<Sysname\> system-view

Sysname rta relay buffer-size 2

【相关命令】

·**rta relay tcp sendbuf-size**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay disconnect**

------------------------------------------------------------------------

**[rta relay disconnect**]命令用来强制断开全部或者指定的客户端连接。

【命令】

**[rta relay disconnect **[{ *server-id client-id* \| **all** }]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[server-id*]：转发组ID，取值范围为0～63。

*[client-id*]：转发组内某一客户端的标识，取值范围为0～9。

【举例】

\# 断开所有客户端连接。

\<Sysname\> system-view

Sysname rta relay disconnect all

【相关命令】

·**display rta relay status**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay enable**

------------------------------------------------------------------------

**[rta relay enable**]命令用来开启中继服务器中继转发功能。

**[undo rta relay enable**]命令用来关闭中继服务器中继转发功能。

【命令】

**[rta relay enable**]

**[undo rta relay enable**]

【缺省情况】

中继转发功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

中继服务器仅应用于TCP的多（RTC Client）对一（中继服务器）方式透传。

【举例】

\# 开启中继服务器中继转发功能。

\<Sysname\> system-view

Sysname rta relay enable

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay listen-port**

------------------------------------------------------------------------

**[rta relay listen-port**]命令用来设置TCP监听端口。

**[undo rta relay listen-port**]命令用来删除TCP监听端口。

【命令】

**[rta relay listen-port** *port-number*]

**[undo rta relay** **listen-port** *port-number*]

【缺省情况】

不存在TCP监听端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：本端TCP监听端口，取值范围为1024～50000。

【使用指导】

·每个转发组最多可以接受10个客户端的连接。

·系统最多支持64个端口，每个端口上建立的连接会组成一个转发组，该群组内某终端数据会在组内广播转发。

·删除监听端口时如果此端口存在客户端连接，则断开连接到此端口的所有客户端连接。

【举例】

\# 设置TCP监听端口1026和1027。

\<Sysname\> system-view

Sysname rta relay listen-port 1026

Sysname rta relay listen-port 1027

【相关命令】

·**rta relay enable**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp**

------------------------------------------------------------------------

**[rta relay tcp**]命令用于配置中继透传服务器和客户端之间TCP连接的发送和接收缓冲区大小。

**[undo rta relay tcp**]命令用来恢复缺省情况。

【命令】

**[rta relay tcp**[ { **recvbuf-size** *recvbuff-size \|* **sendbuf-size** *sendbuff-size* }]]

**[undo rta relay tcp**[ { **recvbuf-size** \| **sendbuf-size** }]]

【缺省情况】

中继透传服务器和客户端之间TCP连接的发送和接收缓冲区大小为2048字节。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[recvbuff-size*]：socket接收缓冲区的大小，取值范围为512～16384，单位为字节。

*[sendbuff-size*]：socket发送缓冲区的大小，取值范围为512～16384，单位为字节。

【使用指导】

如果过大会影响数据转发的及时性，如果过小，会造成系统负担过大，不建议更改此值。

【举例】

\# 配置中继透传服务TCP连接的发送缓冲区和接受缓冲区大小分别为8194字节和2046字节。

\<Sysname\> system-view

Sysname rta relay tcp sendbuf-size 8194

Sysname rta relay tcp recvbuf-size 2046

【相关命令】

·**rta relay tcp keepalive**

·**rta relay tcp nodelay**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp keepalive**

------------------------------------------------------------------------

**[rta relay tcp keepalive**]命令用来配置中继服务器和客户端之间TCP连接的保活属性。

**[undo rta relay tcp keepalive**]命令用来恢复缺省情况。

【命令】

**[rta relay tcp keepalive ***time count*]

**[undo rta relay tcp keepalive**]

【缺省情况】

中继透传服务器和客户端之间TCP连接的保活报文发送间隔为50秒、发送次数为3。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：TCP连接保活报文发送间隔，取值范围为10～7200，单位为秒。

*[count*]：TCP连接保活报文发送次数，取值范围为1～100。

【使用指导】

这里使用TCP本身的保活功能探测客户端可达性，若探测失败则断开对应的客户端。

【举例】

\# 配置中继透传服务TCP连接的保活报文发送间隔为100秒、发送次数为3次。

\<Sysname\> system-view

Sysname rta relay tcp keepalive 100 3

【相关命令】

·**rta relay tcp**

·**rta relay tcp nodelay**

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp nodelay**

------------------------------------------------------------------------

**[rta relay tcp nodelay**]命令用来开启中继服务器的TCP无延时功能。

**[undo rta relay tcp nodelay**]命令用来恢复缺省情况。

【命令】

**[rta relay tcp nodelay**]

**[undo rta relay tcp nodelay**]

【缺省情况】

中继服务器的TCP无延时功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通过开启中继服务器的TCP 无延时功能来关闭TCP的Nagle算法，可减少Nagle算法对TCP报文收发造成的时延，以提高中继服务器转发性能。

【举例】

\# 开启中继服务器的TCP无延时功能。

\<Sysname\> system-view

Sysname rta relay tcp nodelay

【相关命令】

·**rta relay tcp**

·**rta relay tcp keepalive**

**RTC终端接入 \-- RTC终端接入命令 \-- rta rtc compatibility**

------------------------------------------------------------------------

**[rta rtc compatibility enable**]命令用来开启终端接入兼容模式。

**[undo rta rtc compatibility enable**]命令用来关闭终端接入兼容模式。

【命令】

**[rta rtc compatibility enable**]

**[undo rta rtc compatibility enable**]

【缺省情况】

终端接入兼容模式处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

对于Comware V3、Comware V5设备，有的版本上RTC数据传输机制工作在特性模式，有的版本工作在兼容模式。只有当RTC Client与RTC Server两端都工作在同一模式下时才能正常数据传输。Comware V7设备缺省工作在特性模式下，对于工作在兼容模式的Comware V3、Comware V5设备，需要开启兼容模式才能与之互通。

【举例】

\# 开启终端接入兼容模式。

\<Sysname\> system-view

Sysname rta rtc compatible enable

**RTC终端接入 \-- RTC终端接入命令 \-- rta rtc-server listen-port**

------------------------------------------------------------------------

**[rta rtc-server listen-port**]命令用来配置RTC Server的监听端口。

**[undo rta rtc-server listen-port**]命令用来取消配置的监听端口。

【命令】

**[rta rtc-server listen-port** *port-number*]

**[undo rta rtc-server listen-port** *port-number*]

【缺省情况】

没有指定专门的RTC Server监听端口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：RTC服务器端的TCP监听端口号，取值范围为1024～50000。

【使用指导】

只支持开启一个监听端口。

【举例】

\# 配置RTC-server监听端口号为9010。

\<Sysname\> system-view

Sysname rta rtc-server listen-port 9010

【相关命令】

·**rta server enable**

**RTC终端接入 \-- RTC终端接入命令 \-- rta server enable**

------------------------------------------------------------------------

**[rta server enable**]命令用来开启路由器的终端接入功能。

**[undo rta server enable**]命令用来关闭终端接入功能。

【命令】

**[rta server enable**]

**[undo rta server enable**]

【缺省情况】

路由器的终端接入功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

关闭终端接入功能后，对模板、终端及虚终端的设置将会被保留，不会自动取消。

【举例】

\# 开启终端接入功能。

\<Sysname\> system-view

Sysname rta server enable

**RTC终端接入 \-- RTC终端接入命令 \-- rta source-ip**

------------------------------------------------------------------------

**[rta source-ip**]命令用来配置全局的TCP连接源地址。

**[undo rta source-ip**]命令用来取消配置的源地址。

【命令】

**[rta source-ip** *ip-address*]

**[undo rta source-ip**]

【缺省情况】

全局范围内没有配置TCP连接的源地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：建立TCP连接使用的源地址，该地址不能是环回地址（如127.0.0.1）。

【使用指导】

·如果不采用发起方终端接入设备的出接口地址作为TCP连接源地址，可使用本命令另外指定源地址。一般借用终端接入设备Loopback口或Dialer口的IP地址作为TCP连接源地址，用于拨号备份和地址隐藏。

·如果在终端模板下也配置了源地址，则应用该终端模板的终端在建立TCP连接时，优先使用终端模板下配置的源地址作为TCP连接源地址。

·配置了全局的TCP连接源地址后，必须重新建立TCP连接，该地址才能生效。

【举例】

\# 设置全局的TCP连接源地址为1.1.1.1。

\<Sysname\> system-view

Sysname rta source-ip 1.1.1.1

**RTC终端接入 \-- RTC终端接入命令 \-- rta template**

------------------------------------------------------------------------

**[rta template**]命令用来创建终端模板，并进入终端模板视图。

**[undo rta template**]命令用来删除终端模板。

【命令】

**[rta template** *template-name*]

**[undo rta template** *template-name*]

【缺省情况】

没有配置终端模板。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：终端模板名称，为1～15个字符的字符串，不区分大小写。

【使用指导】

如果指定的模板已创建，则直接进入该终端模板视图。

【举例】

\# 创建终端模板abc，并进入该模板视图。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc

**RTC终端接入 \-- RTC终端接入命令 \-- rta terminal**

------------------------------------------------------------------------

**[rta terminal**]命令用来将模板应用到接口。

**[undo rta terminal**]命令用来取消该应用。

【命令】

**[rta terminal ***template-name terminal-number*]

**[undo rta terminal**]

【缺省情况】

接口下没有应用任何模板。

【视图】

异步串口视图

同/异步串口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：终端模板名，为1～15个字符的字符串。

*[terminal-number*]：终端号，取值范围为1～255。

【使用指导】

模板配置完成后需要应用到相应接口上才可以创建相应的终端，实现终端接入的功能，其终端号由配置的*terminal-number*决定。一个接口只能连接一个物理终端，不同的物理终端通过终端号来标识。

【举例】

\# 在接口应用终端模板abc，终端号为1。

\<Sysname\> system-view

Sysname interface async 2/2/1

Sysname-rta-async2/2/1 rta terminal abc 1

**RTC终端接入 \-- RTC终端接入命令 \-- rta terminal backup**

------------------------------------------------------------------------

**[rta terminal backup**]命令用来将终端模板应用到备份接口。

**[undo rta terminal backup**]命令用来在备份接口下取消终端模板应用。

【命令】

**[rta terminal ***template-name terminal-number* **backup**]

**[undo rta terminal backup**]

【缺省情况】

没有将终端模板应用到备份接口。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[template-name*]：终端模板名称，为1～15个字符的字符串。

*[terminal-number*]：终端号，取值范围为1～255。

【使用指导】

当主链路在恢复稳定后，备份链路重新切回到主链路上处理业务。

【举例】

\# 在接口应用终端模板abc，终端号为1，该接口为备份链路的接口。

\<Sysname\> system-view

Sysname interface async 2/2/1

Sysname-rta-async2/2/1 rta terminal abc 1 backup

**RTC终端接入 \-- RTC终端接入命令 \-- rtc-multipeer remote**

------------------------------------------------------------------------

**[rtc-multipeer remote**]命令用来在接收一对多连接的UDP RTC Server类型的虚终端上配置客户端列表。

**[undo rtc-multipeer remote**]命令用来删除指定虚终端的客户端列表。

【命令】

**[rtc-multipeer ***vty-number* **remote** *ip-address port-number*]

**[undo rtc-multipeer*** vty-number*** remote ***ip-address port-number*]

【缺省情况】

没有配置虚终端上客户端列表。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ip-address*]：客户端IP地址。

*[port-number*]：客户端UDP监听端口，取值范围为1024～50000。

【使用指导】

·需先创建UDP_1N_Server类型的虚终端才可以配置客户端列表，同一个虚终端下最多可以配置10个客户端。

·删除UDP_1N_Server类型的虚终端时，该虚终端下配置的客户端列表也会被删除。

·UDP_1N_Server类型的虚终端的配置可参考命令**vty rtc-multipeer**。

【举例】

\# 在接收一对多连接的UDP RTC Server类型的虚终端1上配置客户端列表。

客户端1：IP地址为1.1.1.2、UDP端口为1024

客户端2：IP地址为1.1.1.3、UDP端口为1025

\<Sysname\> system-view

Sysname rta template temp3

Sysname-rta-template-temp3 vty 1 rtc-multipeer 1.1.1.1 1024

Sysname-rta-template-temp3 rtc-multipeer 1 remote 1.1.1.2 1024

Sysname-rta-template-temp3 rtc-multipeer 1 remote 1.1.1.3 1025

【相关命令】

·**vty rtc-multipeer**

**RTC终端接入 \-- RTC终端接入命令 \-- sendbuf bufsize**

------------------------------------------------------------------------

**[sendbuf bufsize**]命令用来配置向终端一次性发送的最大数据包的大小。

**[undo sendbuf bufsize**]命令用来恢复缺省情况。

【命令】

**[sendbuf bufsize** *size*]

**[undo sendbuf bufsize**]

【缺省情况】

向终端一次性发送的最大数据包的大小为500字节。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：向终端一次性发送的最大包的大小，取值范围2～500，单位为字节。

【使用指导】

终端接入设备把数据打成包发给终端，根据实际情况，每次发送的包的大小可能不同。

【举例】

\# 配置一次性发送的最大数据包的大小为200字节。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc sendbuf bufsize 200

【相关命令】

·**sendbuf threshold**

**RTC终端接入 \-- RTC终端接入命令 \-- sendbuf threshold**

------------------------------------------------------------------------

**[sendbuf threshold**]命令用来配置终端发送缓存的阈值。

**[undo sendbuf threshold**]命令用来取消配置的发送缓存阈值。

【命令】

**[sendbuf threshold ***value*]

**[undo sendbuf threshold**]

【缺省情况】

没有设置终端发送缓存的阈值。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：终端发送缓存的阈值，取值范围为50～2048，单位为字节。

【使用指导】

该发送缓存用于存放路由器准备向终端发送的数据，该阈值是指该发送缓存的最多可存储的数据的字节数。

【举例】

\# 配置终端发送缓存阈值为1000字节。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc sendbuf threshold 1000

【相关命令】

·**sendbuf bufsize**

**RTC终端接入 \-- RTC终端接入命令 \-- tcp**

------------------------------------------------------------------------

**[tcp**]命令用来配置TCP的相关参数。

**[undo** **tcp**]命令用来恢复TCP的缺省值。

【命令】

**[tcp**[ { **keepalive** *time count* \| **nodelay** \| **recvbuf-size** *recvsize* \| **sendbuf-size** *sendsize* }]]

**[undo tcp**[ { **keepalive** \| **nodelay** \| **recvbuf-size** \| **sendbuf-size** }]]

【缺省情况】

接收缓存大小为2048字节，发送缓存大小为2048字节，有延迟，保活报文发送时间间隔为50秒，保活报文重发次数为3次。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[keepalive ***time count*]：设置TCP保活报文发送参数，*time*表示保活报文发送时间间隔，取值范围10～7200，单位为秒；*count*表示保活报文重发次数，取值范围1～100。

**[nodelay**]：不采用TCP的Nagle算法，即不延迟。

**[recvbuf-size***recvsize*]：TCP接收缓冲区大小，取值范围512～16384，单位为字节。

**[sendbuf-size***sendsize*]：TCP发送缓冲区大小，取值范围512～16384，单位为字节。

【使用指导】

TCP的相关参数需要重新建立连接才能生效。

【举例】

\# 配置TCP接收缓冲区大小为512字节。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc tcp recvbuf-size 512

\# 配置TCP发送缓冲区大小为512字节。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc tcp sendbuf-size 512

\# 配置TCP不延迟。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc tcp nodelay

\# 配置TCP保活报文的时间间隔为1800秒，发送次数为2次。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc tcp keepalive 1800 2

**RTC终端接入 \-- RTC终端接入命令 \-- update changed-config**

------------------------------------------------------------------------

**[update changed-config**]命令用来使模板下新修改的配置生效。

【命令】

**[update changed-config**]

【缺省情况】

模板下新修改的配置不会立即生效。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果模板已经被应用到相应接口，则在模板视图下修改配置后使用**update changed-config**命令进行更新即可使配置生效。

·更新配置会断开当前连接，然后进行重新连接，因此使用本命令前，请确认当前连接是否允许出现短暂中断。

·对于某些配置，如配置源IP，不仅要更新配置，而且要重新建立连接，才能生效。

【举例】

\# 在模板下增加自动断链的设置并且使新配置立即生效。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc auto-close 10

Sysname-rta-template-abc update changed-config

**RTC终端接入 \-- RTC终端接入命令 \-- vty description**

------------------------------------------------------------------------

**[vty description**]命令用来配置虚终端的描述信息。

**[undo vty description**]命令用来取消虚终端的描述信息。

【命令】

**[vty ***vty-number* **description** *string*]

**[undo vty** *vty-number* **description**]

【缺省情况】

没有配置虚终端的描述信息。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[string*]：虚终端的描述信息，为1～31个字符的字符串。

【使用指导】

当某个虚终端用于某种业务时，推荐直接用业务名描述这个虚终端，便于操作。

【举例】

\# 设置虚终端1的描述信息为"chuxu"。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc vty 1 description chuxu

**RTC终端接入 \-- RTC终端接入命令 \-- vty hotkey**

------------------------------------------------------------------------

**[vty hotkey**]命令用来设置虚终端快速切换的热键。

**[undo vty hotkey**]命令用来取消配置的热键。

【命令】

**[vty** *vty-number* **hotkey** *ascii-code&\<1-3\>*]

**[undo vty ***vty-number* **hotkey**]

【缺省情况】

没有配置虚终端快速切换的热键。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ascii-code&\<1-3\>*]：热键的ASCII值，取值范围为1～255，&\<1-3\>表示前面的参数最多可以输入3次。

【使用指导】

终端接入具有虚终端切换的功能，可以在各应用之间进行切换。终端接入把每个终端从逻辑上划分为8个虚终端，每个虚终端与一个应用相对应。当在某个终端上配置了多个虚终端和相应快速切换热键后，可以在终端上敲入对应不同虚终端的热键进入相应的应用界面，而不用通过菜单选择就可以完成虚终端之间的快速切换。切换前原来虚终端应用的连接状态将被保留，并不断开，从而实现了终端在不同的虚终端间动态切换，也就是在不同的应用间动态切换。

需要注意的是，热键的ASCII值不能与设备上已设置的别的功能热键的ASCII值相同，否则，热键的功能将冲突。比如，热键的值不能设置为17和19，因为这两个值对应了流量控制的快捷键。另外，在终端显示大量数据时使用热键，会影响热键的响应速度。

【举例】

\# 配置虚终端1的热键为\<Ctrl+A\>，即1。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc vty 1 hotkey 1

**RTC终端接入 \-- RTC终端接入命令 \-- vty password**

------------------------------------------------------------------------

**[vty password**]命令用来配置虚终端的认证密码。

**[undo vty password**]命令用来取消配置的密码。

【命令】

**[vty**[ *vty-number* **password** { **simple** \| **cipher** } *string*]]

**[undo vty***vty-number***password**]

【缺省情况】

没有配置虚终端的认证密码。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

**[simple**]：以明文方式设置认证密码。

**[cipher**]：以密文方式设置认证密码。

*[string*]：设置的明文密码或密文密码，区分大小写。明文密码为1～63个字符的字符串；密文密码为1～117个字符的字符串。

【使用指导】

·以明文或密文的方式设置的认证密码，均以密文的方式保存在配置文件中。

·如果需要支持认证功能，则服务端和客户端都必须配置密码，密码相同时认证才能通过；如果不需要支持认证功能，则服务端和客户端都不能配置密码。

【举例】

\# 配置虚终端1的密码为明文abc。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc vty 1 password simple abc

【相关命令】

·**vty rtc-client remote**

·**vty rtc-server remote**

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-client remote**

------------------------------------------------------------------------

**[vty rtc-client remote**]命令用来创建TCP RTC Client终端接入类型的虚终端。

**[undo vty**]用来删除指定的虚终端。

【命令】

**[vty** *vty-number* **rtc-client remote** *ip-address port-number* [ **source** *source-ip* ]]

**[undo vty** *vty-number*]

【缺省情况】

没有创建虚终端。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ip-address*]：RTC服务器端的IP地址。

*[port-number*]：RTC服务器端的监听端口号，取值范围1024～50000。

**[source ***source-ip*]：绑定的源IP地址。

【使用指导】

配置该功能后，该VTY所在的模板不能再配置其他类型的VTY。

【举例】

\# 创建RTC Client终端接入类型的虚终端1，它的RTC Server的IP地址为1.1.1.1，RTC Server侦听的端口为9010，建立TCP连接时是使用2.2.2.2作为源地址。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc vty 1 rtc-client remote 1.1.1.1 9010 source 2.2.2.2

【相关命令】

·**rta rtc-server listen-port**

·**vty rtc-server remote**

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-client remote remote-port**

------------------------------------------------------------------------

**[vty rtc-client remote remote-port**]命令用来创建UDP RTC Client终端接入类型的虚终端。

**[undo vty**]命令用来删除指定的虚终端。

【命令】

**[vty**]*****vty-number***rtc-client remote***ip-address***remote-port***remote-port-number ***udp ** **local-port*******local-port-number * \**source***source-ip-address*

**[undo vty** *vty-number*]

【缺省情况】

没有创建该类型的虚终端。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ip-address*]：RTC服务器IP地址。

*[remote-port-number*]：RTC服务器UDP端口，取值范围为1024～50000。

*[source-ip-address*]：本端IP地址。

*[local-port-number*]：本端UDP监听端口，取值范围为1024～50000。

【使用指导】

配置该功能后，该VTY所在的模板不能再配置其他类型的VTY。

【举例】

\# 创建UDP RTC Client终端接入类型的虚终端1，它的对端（RTC Server）地址为1.1.1.1、UDP端口为1024，本端地址为1.1.1.2、UDP监听端口为1025。

\<Sysname\> system-view

Sysname rta template temp2

Sysname-rta-template-temp2 vty 1 rtc-client remote 1.1.1.1 remote-port 1024 udp local-port 1025 source 1.1.1.2

【相关命令】

·**vty rtc-server remote udp**

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-multipeer**

------------------------------------------------------------------------

**[vty rtc-multipeer**]命令用来创建接收一对多连接的UDP RTC Server终端接入类型的虚终端。

**[undo vty**]命令用来删除指定的虚终端。

【命令】

**[vty ***vty-number* **rtc-multipeer** [ *ip-address*  *port-number*]]

**[undo vty*** vty-number*]

【缺省情况】

没有创建该类型的虚终端。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ip-address*]：本端IP地址。

*[port-number*]：本端UDP监听端口，取值范围为1024～50000。

【使用指导】

删除接收一对多连接的UDP RTC Server终端接入类型的虚终端后，会删除该虚终端下的客户端列表配置。

【举例】

\# 创建接收一对多连接的UDP RTC Server终端接入类型的虚终端1，它的本端监听端口为1024，本端地址为1.1.1.1。

\<Sysname\> system-view

Sysname rta template temp3

Sysname-rta-template-temp3 vty 1 rtc-multipeer 1.1.1.1 1024

【相关命令】

·**vty rtc-client remote remote-port**

·**rtc-multipeer remote**

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-server remote**

------------------------------------------------------------------------

**[vty rtc-server remote**]命令用来创建RTC Server终端接入类型的虚终端。

**[undo vty**]用来删除指定的虚终端。

【命令】

**[vty ***vty-number* **rtc-server remote** *ip-address terminal-number*]

**[undo vty ***vty-number*]

【缺省情况】

没有配置该类型的虚终端。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚终端号，取值范围为0～7。

*[ip-address*]：RTC客户端IP地址。

*[terminal-number*]：RTC客户端对应的终端号，取值范围为1～255。

【使用指导】

配置该功能后，该VTY所在的模板不能再配置其他类型的VTY。

【举例】

\# 添加RTC Server终端接入类型的虚终端，RTC Client端的IP地址为2.2.2.2，终端号为1。

\<Sysname\> system-view

Sysname rta template abc

Sysname-rta-template-abc vty 1 rtc-server remote 2.2.2.2 1

【相关命令】

·**vty rtc-client remote**

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-server remote udp**

------------------------------------------------------------------------

**[vty rtc-server remote udp**]命令用来创建UDP RTC Server终端接入类型的虚终端。

**[undo vty**]命令用来删除指定的虚终端。

【命令】

**[vty ***vty-number* **rtc-server remote** [ *ip-address* **remote-port** *remote-port-number*  **udp local-port** *local-port-number*  **source** *source-ip-address* ]]

**[undo vty ***vty-number*]

【缺省情况】

没有创建该类型的虚终端。

【视图】

终端模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vty-number*]：虚拟终端号，取值范围为0～7。

*[ip-address*]：RTC客户端IP地址。

*[remote-port-number*]：RTC客户端UDP端口，取值范围为1024～50000。

*[source-ip-address*]：本端IP地址。

*[local-port-number*]：本端UDP监听端口，取值范围为1024～50000。

【使用指导】

配置该功能后，该VTY所在的模板不能再配置其他类型的VTY。

【举例】

\# 创建UDP RTC Server终端接入类型的虚终端1，它的本端地址为1.1.1.1、UDP监听端口为1024，对端（RTC Client）地址为1.1.1.2、端口号为1025。

\<Sysname\> system-view

Sysname rta template temp1

Sysname-rta-template-temp1 vty 1 rtc-server remote 1.1.1.2 remote-port 1025 udp local-port 1024 source 1.1.1.1

【相关命令】

·**vty rtc-client remote remote-port**
