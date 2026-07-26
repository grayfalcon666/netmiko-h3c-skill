
**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta error**

------------------------------------------------------------------------

【命令】

**[debugging rta error**]

**[undo debugging rta error**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging rta error**]命令用来打开终端接入错误调试信息开关。**undo debugging rta error**命令关闭终端接入错误调试信息开关。

缺省情况下，终端接入错误调试信息开关处于关闭状态。

表1-1 debugging rta error命令输出信息描述表

字段

描述

Failed to activate listening port *port-id.*

指定监听端口*port-id*的转发组激活失败

Unknown mesh message.

消息处理函数为空

Invalid mesh message.

消息为空

Failed to send mesh message to all slots.

组播通道向所有节点同步数据失败

Mesh data is too long.

发送数据过长

Failed to get mesh channel.

Server根据LIP获取Client的单播通道失败

Failed to send mesh message to interface cards.

向指定接口板同步数据失败

Failed to send mesh message to server\'s MPU.

Client向Server的主控板发送数据失败

Failed to create mesh message.

创建mesh消息失败

Failed to allocate memory for RTC relay epoll of forward group *group-id.*

为指定转发组*group-id*分配Relay Epoll 数据内存失败

Failed to assign index to RTC relay client.

创建转发组内客户端索引失败

Failed to get index of RTC relay forward group.

获取转发组的索引失败

Failed to allocate memory for RTC relay forward group.

为转发组分配存储空间失败

Number of RTC relay clients for forward group *group-id* exceeded the maximum.

转发组group-id 的客户端已达最大支持数目

Failed to set socket option for RTC relay client.

设置RTC Relay客户端的socket属性失败

Failed to update RTC relay keepalive option (Server-ID: *server-id*, Client-ID: *client-id*).

更新指定RTC Relay客户端的keepalive属性失败

Failed to update RTC relay sendbuff option (Server-ID: *server-id*, Client-ID: *client-id*).

更新指定RTC Relay客户端的sendbuff的大小失败

Failed to update RTC relay recvbuff option (Server-ID: *server-id*, Client-ID: *client-id*).

更新指定RTC Relay客户端的recvbuff的大小失败

Failed to update RTC relay nodelay option (Server-ID: *server-id*, Client-ID: *client-id*).

更新指定RTC Relay客户端的nodelay属性失败

Server *server-id* Client *client-id* Failed to save data to other clients in the forward group..

将从指定client获取的报文保存到转发组内其他客户端失败

Invalid negotiation packet.

协商报文无效

RTC relay client accepted invalid socket for forward group *group-id.*

指定转发组接收的客户端连接的socket无效

Failed to add relay client socket to epoll.

添加客户端连接socket到epoll失败

Failed to allocate memory for updating client buffer.

更新客户端缓存时申请内存失败

Failed to add RTC relay data to epoll for listening port *port-id.*

添加指定端口port-id的relay数据到epoll失败

Failed to create RTC relay forward group.

创建转发组数据失败

Failed to create the backup terminal timer.

创建链路备份定时器失败

TTY*tty-number*:Failed to create the auto-close timer.

创建自动断链定时器失败

TTY*tty-number*:Failed to create the auto-link timer.

创建自动建链定时器失败

TTY*tty-number* IF*ifIndex*:Failed to create TTY.

指定接口ifIndex下的tty创建失败

TTY*tty-number* VTY*vty-number*:Transmitting VTY template failed.

根据tty模板填充运行数据失败

TTY*tty-number* VTY*vty-number*:Transmitting multipeer client failed.

传输一对多客户端阶段失败

TTY*tty-number*  IfIndex*ifIndex*: Activation failed.

激活阶段失败

Failed to get active VTY.

获取当前生效的app失败

Failed to send TCP *send-size* data to APP. Error Code:  *errno.*

向app发送TCP数据失败

Failed to send UDP *send-size* data for APP, Error code: *errno.*

向app发送UDP数据失败

TTY*tty-number* APP*app-number*:Failed to add epoll out event for socket *socket-fd.*

向epoll添加OUT事件失败

The VRF *VpnName* is not found.

获取vrf索引失败

TTY*tty-number* APP*app-number*:Failed to send synchronization data to Multi-UDP APP.

向UDP一对多组网各RTC Client发送报文失败

TTY*tty-number* APP*app-number*:Failed to send *IfName* data to Single-UDP APP.

UDP发送数据失败

TTY*tty-number*:Failed to get active APP.

获取当前生效的app失败

Failed to encrtypt by MD5.

对验证字符串以及密码进行MD5加密失败

Failed to decrypt authentication password.

对密码进行解密失败

TTY*tty-number*: Failed to send authentication message due to invalid APP state\< *state* \>.

APP状态错误导致发送验证信息到APP失败

Failed to send negotiation packet from client to server.

TCP连接建立后Client端向Server端发送协商报文失败

UDP server remote IP or port is different, remote IP: *ip* vs *ip*; remote port: *port-id* vs *port-id.*

UDP SERVER接收数据时的remote IP或端口不一致

TTY*tty-number*APP*app-number*:Reached the APP buffer threshould.

达到APP缓冲区的阈值

The TTY*tty-number* is not found.

没有找到指定的TTY

The APP*app-number* is not found.

没有找到指定的APP

TTY*tty-number* APP*app-number*:Failed to create TCP client socket for epoll out.

将描述符从epoll中移出时创建客户端的TCP连接失败

TTY*tty-number*:Failed to create the idle timer.

指定TTY *tty-number* 创建TCP连接空闲超时定时器失败

Failed to set TCP server socketoption.

设置server端与client端通信的Socket属性失败

TTY*tty-number* APP*app-number*:Failed to allocate epoll data for APP.

指定TTY的app创建epoll数据失败

TTY*tty-number* APP*app-number*:Failed to add epoll data for APP.

将指定TTY的app的epoll数据加入epoll失败

TTY*tty-number* APP*app-number*:Failed to create TCP client socket.

创建tcp client 端socket失败

TTY*tty-number* APP*app-number*:Failed to create UDP socket.

创建UDP socket失败

Failed to get the TCP client IP address.

获取client端IP地址失败

Failed to find APP by the TCP client IP address.

通过client端IP查找app失败

Failed to check VPN  by the TCP client.

TCP client检验VPN失败

The negotiated APP is not  the current APP.

协商的APP不是当前APP

Failed to check negotiation data by the TCP server.

TCP server端检查协商数据失败

TTY*tty-number* APP*app-number*:Failed to add the TCP server socket *socket-fd* to epoll.

向epoll中添加TCP server的socket文件描述符*socket-fd *失败

Failed to check TCP client terminal number.

TCP server验证client端终端索引号失败

Failed to negotiate by the TCP server socket *socket-fd.*

指定socket的TCP server端接收协商报文后协商失败

Failed to receive the TCP client negotiation data by the TCP server socket *socket-fd.*

指定socket的TCP server端接收客户端的协商报文失败

Failed to spawn TCP server socket by listening socket *socket-fd.*

通过监听socket创建TCP server socket失败

Failed to add TCP server socket *socket-fd* to epoll.

向epoll中添加TCP server 的socket文件描述符失败

Failed to create TCP listening socket by port *port-id.*

创建指定端口*port-id*的TCP监听socket失败

Failed to add TCP listening socket *socket-fd* to epoll.

向epoll中添加TCP监听socket文件描述符失败

Failed to allocate temporary receive-buffer for APP.

申请临时接受数据缓冲区失败

TTY*tty-number*:Failed to find the TTY for  asynchronization interface.

没有找到异步接口上的TTY

TTY*tty-number*:Failed to receive the data from

asynchronization interface.

从异步接口上接收数据失败

IfIndex*ifIndex*:Failed to open asynchronization

 interface device.

打开指定异步接口ifIndex设备失败

IfIndex*ifIndex*:Failed to allocate epoll data for

 asynchronization interface.

为指定的异步接口*ifIndex*分配epoll 数据失败

IfIndex*ifIndex*:Failed to add epoll data for

asynchronization interface.

向epoll中添加指定异步串口*ifIndex*的epoll数据失败

IfIndex*ifIndex*:Failed to put asynchronization interface authorization.

释放指定异步接口*ifIndex*的TTY使用权失败

TTY*tty-number* IfIndex*ifIndex*:Failed to create

asynchronization buffer.

创建异步处理数据buffer失败

TTY*tty-number* IfIndex*ifIndex*:Failed to get

asynchronization interface authorization.

和tty交互获取异步接口的使用权失败

TTY*tty-number*:Failed to send data to

asynchronization interface.

发送数据到异步接口上的tty失败

Failed to send *send-size*-byte asynchronization data. Error code: *errno.*

发送*send-size*字节异步数据失败,打印系统错误号*errno*

Failed to send *send-size*-byte asynchronization data.

发送*send-size*字节异步数据失败

Failed to receive *receive-size* data from

 asynchronization interface, errno is *errno.*

从异步接口接收数据失败，系统错误号*errno*

Failed to allocate memory for asynchronous

temporary receive-buffer.

申请临时的异步接受数据缓存失败

Invalid socket or empty send-buffer for

 synchronization interface.

同步接口向指定的发送packet socket时的socket无效或发送缓存为空

Failed to send *send-size*-byte synchronization data. Error code: *errno.*

发送数据失败，系统错误号*errno*

Invalid socket or empty receive-buffer for synchronization interface.

同步接口从指定的packet socket接收数据时socket无效或接收缓存为空

Failed to receive data  from synchronization interface. Error code: *errno.*

从同步接口接收数据失败，系统错误号*errno*

TTY*tty-number*:Failed to find the TTY for

synchronization interface.

同步接口上找不到指定的TTY *tty-number*

TTY*tty-number* IF*ifIndex*:Failed to receive the data from synchronization interface.

从指定应用接口ifIndex的TTY *tty-number*接收同步数据失败

IF*ifIndex*:Failed to creare socket for synchronization interface.

指定的同步接口ifIndex创建socket失败

IfIndex*ifIndex*:Failed to bind IP and set socket for synchronization interface.

指定的同步接口IfIndex绑定报文特征地址及设置socket属性失败

TTY*tty-number* IfIndex*ifIndex*:Failed to create

packet socket for synchronization interface.

为指定同步接口*ifIndex*上应用的TTY *tty-number*创建packet socket失败

TTY*tty-number* IfIndex*ifIndex*:Failed to add socket

 to epoll for synchronization interface.

向epoll中添加指定同步接口*ifIndex*上应用的TTY *tty-number*的socket文件描述符失败

TTY*tty-number* IfIndex*ifIndex*:Failed to allocate

 epoll data for synchronization interface.

向epoll中添加指定同步接口*ifIndex*上应用的TTY *tty-number*的epoll数据失败

TTY*tty-number* IfIndex*ifIndex*:Failed to create

 buffer for synchronization interface.

创建指定同步接口*ifIndex*上应用的TTY *tty-number*使用的buffer失败

TTY*tty-number* IfIndex*ifIndex*:Failed to create

 temporary buffer for synchronization interface.

创建指定同步接口*ifIndex*上应用的TTY *tty-number*使用的临时缓存buffer失败

TTY*tty-number* IfIndex*ifIndex*:Failed to send data to

synchronization interface.

取出socket缓冲区的数据发送到同步接口终端失败

Failed to allocate temporary receive-buffer for synchronization.

为同步接口上分配临时接收缓存失败

Protocol operation failed.

协议操作失败

Failed to copy protocol option.

拷贝协议选项失败

【举例】

\# 在设备上进行ERROR的相关配置，打开ERROR的调试信息开关。当用户登录设备时，设备上输出如下调试信息。

\<Sysname\> debugging rta error

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1; RTC relay client for forward group 1 has been used up.

*// 转发组1下已经有十个客户端，此时再次链接该转发组。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1; Failed to decrypt authentication password.

*// 对密码进行解密失败。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1;Failed to create the backup terminal timer.

*// 创建链路备份定时器失败。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1;TTY1:Failed to find the TTY for synchronization interface.

*// 找不到同步接口上指定的TTY 1。*

**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta event**

------------------------------------------------------------------------

【命令】

**[debugging rta event**]

**[undo debugging rta event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging rta event**]命令用来打开终端接入事件调试信息开关。**undo debugging rta event**命令关闭终端接入事件调试信息开关。

缺省情况下，终端接入事件调试信息开关处于关闭状态。

表1-2 debugging rta event命令输出信息列表

字段

描述

Responded to the interface deactive event caused by interface removal.

由删除引起的接口去激活事件已经响应

Responded to the interface up event.

接口UP事件已经响应

Responded to the interface down event.

接口DOWN事件已经响应

Responded to the interface deactive event.

接口DEACTIVE事件已经响应

Responded to the interface active event.

接口ACTIVE事件已经响应

Responded to the interface delete event.

接口DELETE事件已经响应

Responded to the interface aschange event.

接口ASCHANGE事件已经响应

Responded to the interface changeencap event.

接口CHANGEENCAP事件已经响应

The RemoteTermConn license active event is processed.

远程终端License事件已经激活

The RemoteTermConn license deactive event is processed.

远程终端License事件已经去激活

The mesh server is connected.

Mesh通道Server端连通

The mesh server is disconnected.

Mesh通道Server端断开

The mesh client is connected.

Mesh通道Client端连通

The mesh client is disconnected.

Mesh通道Client端断开

Updated RTC relay keepalive option. Server-ID: *server-id*, Client-ID: *client-id*.

更新Relay server的TCP配置的keepalive参数成功

Updated RTC relay sendbuff option. Server-ID: *server-id*, Client-ID: *client-id*.

更新Relay server的TCP配置的sendbuff参数成功

Updated RTC relay recvbuff option. Server-ID: *server-id*, Client-ID: *client-id*.

更新Relay server的TCP配置的recvbuff参数成功

Updated RTC relay nodelay option. Server-ID: *server-id*, Client-ID: *client-id*.

更新Relay server的TCP配置的nodelay参数成功

Received negotiation data. Server-ID: *server-id*, Client-ID : *client-id*.

收到Client和Relay server的协商数据

Updated RTC relay buffer-size. Server-ID: *server-id*, Client-ID: *client-id*.

更新Relay server的转发组缓存大小成功

RTC relay created socket for listening port *listen-port-id*.

Relay server创建监听端口成功

RTC relay deleted listening port *listen-port-id*.

Relay server删除监听端口成功

TTY*tty-number*:The primary and backup links deactived.

TTY的主链路和备份链路失效

TTY*tty-number*:The backup terminal timer timed out.

TTY备份链路定时器超时

TTY*tty-number*:The backup terminal timer is deleted.

TTY备份链路定时器删除

TTY*tty-number*:The backup terminal timer is created.

创建TTY备份链路定时器

TTY*tty-number*:The automatic link teardown timer timed out.

TTY自动断链定时器超时

TTY*tty-number*:The automatic link teardown timer is deleted.

删除TTY自动断链定时器

TTY*tty-number*:The automatic link teardown timer is created.

创建TTY自动断链定时器

TTY*tty-number*:The automatic link establishment timer timed out.

TTY自动建链定时器超时

TTY*tty-number*:The automatic link establishment timer is deleted.

删除TTY自动建链定时器

TTY*tty-number*:The automatic link establishment timer is created.

创建TTY自动建链定时器

TTY*tty-number* IfIndex*ifIndex*:The single link state is No Active.

TTY的单链路状态机为No Active状态

TTY*tty-number* IfIndex*ifIndex*:The single link state changed to Primary Active.

TTY的单链路状态机切换为Primary Active状态

TTY*tty-number* IfIndex*ifIndex*:The single link state changed to Backup Active.

TTY的单链路状态机切换为Backup Active状态

TTY*tty-number* IfIndex*ifIndex*:The single link state is Primary Active.

TTY的单链路状态机为Primary Active状态

TTY*tty-number* IfIndex*ifIndex*:The single link state is Backup Active.

TTY的单链路状态机为Backup Active状态

TTY*tty-number* IfIndex*ifIndex*:The single link state changed to No Active.

TTY的单链路状态机切换为No Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link state is No Active.

TTY的双链路状态机为No Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link state changed to Primary Active.

TTY的双链路状态机切换为Primary Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link state changed to Backup Active.

TTY的双链路状态机切换为Backup Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link state is Primate Active.

TTY的双链路状态机为Primate Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link current state is Backup Active.

TTY的双链路状态机为Backup Active状态

TTY*tty-number* Primary IfIndex*ifIndex* Backup IfIndex*ifIndex*:The double link state changed to No Active.

TTY的双链路状态机切换为No Active状态

TTY*tty-number* IfIndex*ifIndex*:The phase of TTY starting is incompleted.

TTY创建未完成

TTY*tty-number* IfIndex*ifIndex*:TTY created successfully.

TTY创建成功

TTY*tty-number* IfIndex*ifIndex*:Creating TTY.

TTY正在创建

TTY*tty-number*:Transmitting TTY template succeeded.

传输TTY配置模板成功

TTY*tty-number* VTY*vty-number*:Transmitting VTY template succeeded.

传输VTY配置模板创建成功

TTY*tty-number* VTY*vty-number*:Transmitting multipeer client succeeded.

传输multipeer client配置模板创建成功

TTY*tty-number* IfIndex*ifIndex*:TTY activated successfully.

初始化TTY各模块，激活TTY

TTY*tty-number* IfIndex*ifIndex*:TTY deactivated successfully.

去初始化TTY各模块，去激活TTY

TTY*tty-number* IfIndex*ifIndex*:TTY deleted successfully.

删除TTY各模块

All TTY deactived successfully.

去激活所有TTY业务

TTY*tty-number* IfIndex*ifIndex*:The TTY is processing interface up event.

TTY正在处理接口UP事件

TTY*tty-number* IfIndex*ifIndex*:The TTY is processing interface down event.

TTY正在处理接口DOWN事件

TTY*tty-number* APP*app-number*:Successfully added epoll out event for socket *socket-id*.

TTY成功添加EPOLL OUT事件

TTY*tty-number* APP*app-number*:Successfully sent synchronization data for Multi-UDP APP.

成功发送UDP同步数据到APP

TTY*tty-number* APP*app-number*:Successfully sent *data-len* data for Single-UDP APP.

成功发送Single-UDP数据到APP

TTY*tty-number* APP*app-number*:Successfully sent data-len data for Single-TCP APP.

成功发送Single-TCP数据到APP

TTY*tty-number* APP*app-number*:Block to send data-len data for Single-TCP APP.

停止发送Single-TCP数据到APP

TTY*tty-number*:Clear terminal buffer for APP.

清除APP的终端缓存

TTY*tty-number* APP*app-number*:Deal connectionless for APP.

处理处于无连接状态的APP

TTY*tty-number*:Failed to send data to APP.

TTY发送消息失败

Receive data *data-len* form UDP client APP, errno is *errno*.

从CLIENT APP收到UDP数据,recvfrom函数错误码为

Receive data data-len from UDP server APP, errno is data-len.

从SERVER APP收到UDP数据，recvfrom函数错误码为

Receive data data-len from TCP client APP, errno is data-len.

从CLIENT APP收到TCP数据，recv函数错误码为

Receive data data-len from TCP server APP, errno is data-len.

从SERVER APP收到TCP数据，recv函数错误码为

TTY*tty-number* APP*app-number*:TCP socket is closed at the other side.

TCP链接另一端的socket已经关闭

TTY*tty-number* APP*app-number*:Successfully created TCP client socket for epoll out.

成功创建CLIENT端的TCP socket用于处理epoll out事件

TTY*tty-number* APP*app-number*:Processed the epoll error event or epoll hup event for APP.

处理APP的epoll error事件和epoll hup事件

TTY*tty-number* APP*app-number*:Processed the epoll out event for APP.

处理APP的epoll out事件

TTY*tty-number* APP*app-number*:Processed the epoll in event for APP.

处理APP的epoll in事件

TTY*tty-number*:The idle timer timed out.

链接空闲定时器超时

TTY*tty-number*:The idle timer is deleted.

删除链接空闲定时器

TTY*tty-number*:The idle timer is created.

创建链接空闲定时器

TTY*tty-number*:The idle timer is refreshed.

刷新连接空闲定时器

TTY*tty-number* APP*app-number*:Successfully allocated epoll data for APP.

成功为APP分配epoll数据

TTY*tty-number* APP*app-number*:Successfully added epoll data for app.

成功为APP添加epoll数据

TTY*tty-number* APP*app-number*:Successfully created TCP client socket.

成功创建CLIENT端TCP socket

TTY*tty-number* APP*app-number*:Successfully created UDP socket.

成功创建UDP socket

TTY*tty-number* APP*app-number*:Successfully added the TCP server socket *socket-id* to epoll.

成功的把SERVER端TCP socket加入epoll

Successfully negotiated by the TCP server socket *socket-id*.

SERVER端TCP socket协商成功

Successfully spawned TCP listening socket by socket *socket-id*.

成功创建TCP监听socket通过其他socket

Successfully added TCP server socket *socket-id* to epoll.

成功的把SERVER端TCP socket加入epoll

Successfully created TCP listening socket by port *port-number*.

成功的通过端口port-number创建TCP 监听socket

Successfully added TCP listening socket *socket-id* to epoll.

成功的添加TCP 监听socket到epoll

Successfully deleted TCP listening socket *socket-id* from epoll and close.

成功的从epoll删除TCP 监听socket，并关闭

IfIndex*ifIndex*:Successfully allocated epoll data for asynchronization interface.

成功的为异步接口分派epoll数据

IfIndex*ifIndex*:Successfully added epoll data for asynchronization interface.

成功的为异步接口添加数据

IfIndex*ifIndex*:Successfully put asynchronization interface authorization.

释放指定异步接口的TTY使用权限成功

TTY*tty-number* IfIndex*ifIndex*:Successfully got asynchronization interface authorization.

成功的获取异步接口授权

TTY*tty-number*:Obtained data from APP buffer for asynchronization interface.

从APP缓存获取异步接口数据

TTY*tty-number*:Process the epoll in event for synchronization interface.

处理同步接口的epoll in事件

TTY*tty-number* IfIndex*ifIndex*:Successfully created packet socket for synchronization interface.

成功的创建同步接口的packet socket

TTY*tty-number*IfIndex*ifIndex*:Successfully allocated epoll data for synchronization interface.

成功的为同步接口分派epoll数据

TTY*tty-number* IfIndex*ifIndex*:Successfully added socket to epoll for synchronization interface.

成功的把同步接口socket加入epoll

TTY*tty-number* IF*ifIndex*:Obtained data from APP buffer for synchronization interface.

成功的从APP缓存获取同步接口数据

Obtained serial interface statistics(CRC error counts: *error-number*, input packets: *packets).*

下驱动获取串口统计信息

The serial interface checked for encapsulation.

内核态检查为封装状态

The serial interface checked for decapsulation.

内核态检查为去封装状态

Processed mdc init event.

处理mdc初始化事件

Processed mdc start event.

处理mdc start事件

Processed mdc stop event.

处理mdc stop事件

Processed protocol enable control message.

处理Rtc协议特征使能

Processed protocol disable control message.

处理Rtc协议特征去使能

【举例】

\# 打开EVENT的事件调试信息开关。用户通过串口登录设备的操作时，设备上输出如下调试信息。

\<Sysname\> debugging rta event

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1;The interface up event is responsed.

*// 接口UP事件已经响应。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY1:The primary and backup links deactived.

*[// TTY 1*]*的主链路和备份链路失效。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY1:The phase of Transmitting TTY template is successful.

*// 传输TTY 1配置模板创建成功。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY1VTY0:The phase of transmitting VTY template is successful.

*// 传输TTY 1下的VTY 0配置模板创建成功。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; Process mdc start event.

*// 处理mdc start事件。*

**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta packet**

------------------------------------------------------------------------

【命令】

**[debugging rta packet**[ { **brief** \| **detail** } { **all** \| **recv-remote** \| **recv-terminal** \| **send-remote** \| **send-terminal** } *terminal-number*]]

**[undo debugging rta packet **[{ **brief** \| **detail** } { **all** \| **recv-remote** \| **recv-terminal** \| **send-remote** \| **send-terminal** } *terminal-number*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[brief**]：打开简要报文信息调试开关。

**[detail**]：打开详细报文信息调试开关。

**[all**]：显示所有报文信息。

**[recv-remote**]：显示设备从对端接收到的报文信息。

**[recv-terminal**]：显示设备从终端接收到的报文信息。

**[send-remote**]：显示设备向对端发送的报文信息。

**[send-terminal**]：显示设备向终端发送的报文信息。

*[terminal-number*]：需要显示信息的终端号。

【描述】

**[debugging rta packet**]命令用来打开终端接入报文调试信息开关。**undo debugging rta packet**命令关闭终端接入报文调试信息开关。

缺省情况下，终端接入报文调试信息开关处于关闭状态。

表1-3 debugging rta packet命令输出信息列表

字段

描述

TTY*tty-number* APP*app-number*: Sent *send-size* bytes synchronization data to remote Multi-UDP APP(IP=*ip*, Port=*port-id*).

UDP一对多组网时，指定*tty-number*号的TTY上的第*app-number*个APP发送*send-size*字节的UDP数据数据到多个对端

TTY*tty-number* APP*app-number*:Sent *send-size* bytes data of *ifname* to Single-UDP APP.

UDP一对一组网时，指定*tty-number*号的TTY上的第*app-number*个APP发送*send-size*个字节数据到对端

TTY*tty-number* APP*app-number*:Sent *send-size* bytes data of *ifname* to Single-TCP APP.

TCP一对一组网时，指定*tty-number*号的TTY上的第*app-number*个APP发送*send-size*个字节数据到对端

TTY*tty-number* APP*app-number*:Received *receive-size* bytes data from remote APP.

指定*tty-number*号的TTY上的第*app-number*个APP从对端接收*receive-size*个字节的数据

APP*app-number* sent MD5 challenge to client failed.

指定*app-number*的APP发送MD5加密信息到client端失败

APP*app-number* sent MD5 challenge to server failed.

指定*app-number*的APP发送MD5加密信息到server端失败

TTY*tty-number* IfIndex*ifindex*:Received *receive-size* bytes data from terminal in asynchronization interface.

指定终端号*tty-number*的TTY从异步接口上的终端接收*receive-size*字节的数据

TTY*tty-number* IfIndex*ifindex*:Sent *send-size* bytes data to terminal in asynchronization interface.

指定终端号*tty-number*的TTY发送*send-size*字节的数据到异步接口上的终端

TTY*tty-number* IfIndex*ifindex*:Received *receive-size* bytes data from terminal in synchronization interface.

指定终端号*tty-number*的TTY从同步接口上的终端接收*receive-size*字节的数据

TTY*tty-number* IfIndex*ifindex*:Sent *send-size* bytes data to terminal in synchronization interface.

指定终端号*tty-number*的TTY发送*send-size*字节的数据到同步接口上的终端

【举例】

\# 打开PACKET的事件调试信息开关，当用户使用串口登录设备时，设备上输出如下调试信息。

\<Sysname\> debugging rta packet brief all 1

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/PACKET: -MDC=1; TTY[1 APP1:Send 88 bytes data of async to Single-TCP APP.]

*[// TCP*]*一对一组网时，指定的TTY 1上的第1个APP发送88个字节数据到对端。*

\*Aug  7 18:20:48:047 2012 System RTERMCON/7/PACKET: -MDC=1; APP1 send MD5 challenge to client failed.

*// 指定app-number为1的APP发送MD5加密信息到client端失败。*
