
**WAAS \-- WAAS调试命令 \-- debugging waas**

------------------------------------------------------------------------

【命令】

**[debugging**[ **waas** { **all** \| **dre** \| **error** \| **event** \| **packet** }]]

**[undo**[ **debugging** **waas** { **all** \| **dre** \| **error** \| **event** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示WAAS所有调试信息开关。

**[dre**]：表示WAAS数据冗余消除调试信息开关。

**[error**]：表示WAAS错误调试信息开关。

**[event**]：表示WAAS事件调试信息开关。

**[packet**]：表示WAAS报文调试信息开关。

【描述】

**[debugging** **waas**]命令用来打开WAAS调试信息开关。**undo** **debugging** **waas**命令用来关闭WAAS调试信息开关。

缺省情况下，WAAS调试信息开关处于关闭状态。

表1-1 debugging waas dre命令输出信息描述表

字段

描述

The matching policy action is *ability*. The TFO global switch is *cfgswitch*. IPv4/IPv6 TCP packet: src=*ip*/*port*, dst=*ip*/*port*, payload length=*len.*

收到匹配WAAS策略的报文，其中策略引用的class的优化方式为*ability*，配置的WAAS全局优化开关为*cfgswitch*。基于TCP的IPv4/IPv6报文：源IPv4/IPv6地址和端口号为*ip*/*port*，目的IPv4/IPv6地址和端口号为*ip*/*port*，载荷长度为*len。ability*取值包括：

·NONE：无优化能力

·TFO：TFO传输优化

·DRE：数据冗余消除

·LZ：LZ压缩

不对报文进行优化，显示为NONE；对报文进行优化，TFO为必选，DRE和LZ可选，可取二者的组合。

*[cfgswitch*]的取值包括：

·DRE：打开WAAS消除数据冗余功能全局开关

·LZ：打开WAAS数据压缩功能全局开关

 

The original data was divided into *blocknum* blocks, of which *createdictnum* new dictionary entries were created and *matchdictnum* entries were matched.

原始数据进行DRE滑动分块处理。原始数据被切割成*blocknum*块，其中新创建的字典表项数为*createdictnum*，匹配的字典表项数为*matchdictnum*

 

DRE compressing, transmitted *orglen *bytes.

DRE压缩时，重传未确认的*orglen*字节数据

 

Fast compressing compressed *orglen* bytes to *cmplen* bytes.

快速压缩处理，将长度为*orglen*字节的数据压缩为*cmplen*字节。进行快速压缩的情况包括：

·报文过短，长度小于最小支持压缩数据大小（64字节）

·MSS（Maximum Segment Size，最大报文段长度）值小于能接受的最小MSS（285字节）

·LZ压缩失败

 

DRE compressed *orglen* bytes to *cmplen* bytes.

DRE压缩处理，将长度为*orglen*字节的数据压缩为*cmplen*字节

 

LZ was not performed: Insufficient compression buffer after DRE.

DRE压缩处理后，再进行LZ压缩处理时压缩缓冲区不足，放弃LZ压缩

 

DRE and LZ compressed *orglen* bytes to *cmplen* bytes.

DRE和LZ压缩处理，将长度为*orglen*字节的数据压缩为*cmplen*字节

 

DRE and LZ decompressed *orglen* bytes to *decmplen* bytes.

DRE和LZ解压处理，将长度为orglen字节的数据解压为*decmplen*字节

 

Performing fast compression after LZ failed: Insufficient compression buffer.

压缩缓冲区不足，导致LZ压缩失败，尝试进行快速压缩处理

 

LZ compressed *orglen* bytes to *cmplen* bytes.

LZ压缩处理，将长度为*orglen*字节的数据压缩为*cmplen*字节

 

LZ decompressed *orglen* bytes to *decmplen* bytes.

LZ解压缩处理，将长度为*orglen*字节的数据解压为decmplen字节

 

Compression was not performed: Data of *orglen* bytes is too short.

长度为*orglen*字节的数据太短，放弃压缩

 

DRE decompressed *orglen* bytes to *decmplen* bytes.

DRE解压缩处理，将长度为*orglen*字节的数据解压为*decmplen*字节

 

The peer has acknowledged *len* bytes of data, synchronizing and matching *ackdictnum* dictionary entries.

对端确认了*len*字节数据，这些数据匹配、创建*ackdictnum*个表项

 

表1-2 debugging waas error命令输出信息描述表

字段

描述

Failed to delete a matching rule of the class from kernel.

从内核删除class的match规则失败

 

Creating class *name* failed: Insufficient memory.

内存不足，导致创建名为*name*的class失败

 

Creating a matching rule for the class failed:Insufficient memory.

内存不足，导致创建class的match规则失败

 

Failed to create an instance for class* name*.

实例化名为*name*的class失败

 

Failed to add a matching rule of the class to kernel.

向内核添加class的match规则失败

 

Failed to add class *name* to kernel.

向内核添加名为*name*的class失败

 

Failed to delete class *name* from kernel.

从内核删除class *name*失败

 

Recovering class *name* from DBM failed: Insufficient memory.

内存不足，导致从DBM配置恢复class *name*失败

 

Recovering class a matching rule from DBM failed: Insufficient memory.

内存不足，导致从DBM配置恢复class的match规则失败

 

Failed to push the data of class to kernel.

class数据下内核失败

 

Failed to add session extension information to the session handle.

添加会话扩展信息到会话句柄上失败

 

Failed to set up a TCP listening handle.

创建监听TCP句柄失败

 

Failed to modify the IPv4/IPv6 option of *option*.

修改IPv4/IPv6连接选项*option*失败。*option*取值包括：

·base-congestion-window：设置/获取窗口大小

·receive-buffer：设置进入慢启动的拥塞窗口

·keepalive：设置保活定时器是否使能

 

Failed to enable WAAS forwarding.

使能WAAS业务转发点失败

 

Failed to get WAAS global status.

获取WAAS全局统计信息失败

 

Failed to add the application of the WAAS policy on interface *interface-name* to kernel.

向内核添加接口*interface-name*应用WAAS策略失败

 

Failed to apply the WAAS policy *name* to interface *interface-name*.

接口*interface-name*应用WAAS策略*name*失败

 

Failed to delete the application of the WAAS policy on interface *interface-name* from kernel.

从内核删除接口*interface-name*应用WAAS策略失败

 

Adding IPv4/IPv6 blacklist entries failed:Insufficient memory.

内存不足，导致添加IPv4/IPv6的黑名单表项失败

 

Failed to create a new IPv4/IPv6 blacklist.

创建新的IPv4/IPv6黑名单表失败

 

Processing the REQUESTFAIL event failed: Insufficient infomation.

获取信息不足，导致响应REQUESTFAIL事件失败

 

Failed to accept a new connection.

接受新连接失败

 

Creating local/peer dictionary entries failed: Insufficient memory.

内存不足，导致创建本端/对端数据字典表项失败

 

Adding meta data failed: Insufficient memory.

内存不足，导致添加本端/对端数据字典元数据失败

 

Failed to save local/peer dictionary entries.

保存本端/对端数据字典表项失败

 

Creating a link node for the unacknowledged dictionary entries failed: Insufficient memory.

内存不足，导致创建包含未确认数据字典表项信息的链表节点失败

 

DRE decompress failed: The dictionary has been deleted.

数据字典已被释放，导致DRE解压缩失败

 

DRE decompress failed: Insufficient decompression buffer.

DRE解压缩缓冲区不足，导致DRE解压缩失败

 

DRE decompress failed: The dictionary entry not found.

查找数据字典表项失败，导致DRE解压缩失败

 

DRE decompress failed: MD5 authentication failed.

MD5验证失败，导致DRE解压缩失败

 

Failed to add new dictionary entries during DRE decompression.

DRE解压缩时，添加新的字典表项失败

 

DRE compress failed: The peer was not found.

从DRE句柄获取peer节点失败，导致DRE压缩失败

 

DRE compress failed: The dictionary has been deleted.

数据字典已被释放，导致DRE压缩失败

 

Compress failed: The peer was not found.

获取peer节点失败，导致压缩失败

 

Decompress failed: The peer was not found.

获取peer节点失败，导致解压缩失败

 

Decompression failed: MD5 message error or empty package.

MD5信息错误或解压缩数据为空，导致解压缩失败。

 

Failed to add peer *peer-id.*

添加peer节点*peer-id*失败

 

LZ decompression failed.

LZ解压缩失败

 

Creating the peer dictionary failed: Insufficient memory.

内存不足，导致创建peer数据字典失败

 

Failed to create WAAS license reconnecting timer.

创建WAAS license重连定时器失败

 

Failed to create WAAS license checking timer.

创建WAAS license检查定时器失败

 

Failed to push the data of policy to kernel.

策略数据下内核失败

 

Failed to push the data of LocalID to kernel.

LocalID数据下内核失败

 

Failed to push the data of TFO to kernel.

TFO数据下内核失败

 

Failed to create blacklist aging timer.

创建黑名单老化定时器失败

 

Failed to reset the blacklist aging timer.

重置黑名单老化定时器失败

 

Failed to synchronize instance (type: *type*) message.

同步类型为*type*的实例化信息失败。*type*取值包括：

·1：设置debug调试开关状态

·2：添加class

·3：删除class

·4：添加match规则

·5：删除match规则

·6：添加策略

·7：删除策略

·8：修改策略

·9：策略添加match规则

·10：策略删除match规则

·11：设置接口应用策略

·12：设置全局优化开关状态

·13：修改策略优化方式

·14：设置TFO保活开关状态

·15：设置TFO拥塞窗口大小

·16：设置TFO接收缓冲区长度

·17：设置自动发现黑名单开关状态

·18：设置LocalID

·19：配置恢复，class下内核

·20：设置版本号

·21：设置黑名单老化时间

·22：添加黑名单

·23：删除黑名单

·24：清除DRE缓存

·25：清除DRE统计信息

·26：清除黑名单

 

Failed to modify policy *name* action on kernel.

修改内核策略*name*的优化方式失败

 

Creating an instance for policy *name* failed: Invalid ID.

无效的ID编号，导致实例化WAAS策略*name*失败

 

Failed to add policy *name* to kernel.

向内核添加策略*name*失败

 

Failed to delete policy *name* from kernel.

删除内核策略*name*失败

 

Failed to add/delete match *ID* on kernel.

添加/删除内核ID为*ID*的match规则失败

 

Adding a matching rule failed: Insufficient memory.

内存不足，导致class添加match规则失败

 

Adding policy *name* failed: Insufficient memory.

内存不足，导致添加策略*name*失败

 

Recovering policy *name* from DBM failed: Insufficient memory.

内存不足，导致从DBM恢复策略*name*数据失败

 

表1-3 debugging waas event命令输出信息描述表

字段

描述

State of Memory-alert-gate is minor.

内存门限一级告警

 

State of Memory-alert-gate is severe.

内存门限二级告警

 

State of Memory-alert-gate is critical.

内存门限三级告警

 

State of Memory-alert-gate changed to severe.

内存门限变为二级告警

 

State of Memory-alert-gate changed to minor.

内存门限变为一级告警

 

State of Memory-alert-gate changed to normal.

内存门限恢复正常

 

WAAS processes ifevent*ifevent*.

WAAS处理接口事件*ifevent。ifevent*取值包括：

·active：接口批量激活

·deactive：接口批量去激活

·delete：接口批量删除

 

The ifindex*index* ifevent*ifevent* failed.

接口索引为*index*的接口处理接口事件i*fevent*失败。*ifevent*取值包括：

·active：接口激活

·deactive：接口去激活

·delete：接口删除

 

Connection*info* received event *event* while the focusing event is e*vent*.

收到TCP连接事件，连接信息为*info。*TCP句柄收到事件*event*，监听事件是*event*。*info*形式为srcaddr/srcport -\> dstaddr/dstport*。event*取以下值或以下值的组合：

·DATAREADY，数据到达事件

·WRITESPACE，数据可写事件

·ERRORREPORT，连接关闭事件

·REQUESTFAIL，连接建立失败事件

 

Processing REQUESTFAIL event.

处理TCP连接建立失败事件

 

Processing ERRORREPORT event on connection*info*.

处理TCP连接关闭事件，连接信息为*info。info*形式为srcaddr/srcport -\> dstaddr/dstport

 

Accepted a new connection*info*.

接受一个TCP新连接，连接信息为*info。info*形式为srcaddr/srcport -\> dstaddr/dstport

 

Processing DATAREADY event on connection*info*.

处理TCP连接上的数据到达事件，连接信息为*info。inf*o形式为srcaddr/srcport -\> dstaddr/dstport

 

Processing WRITESPACE event on connection*info*.

处理TCP连接可写事件，连接信息为info*。info*形式为srcaddr/srcport -\> dstaddr/dstport

 

表1-4 debugging waas packet命令输出信息描述表

字段

描述

Failed to send *packetnum* packet(s) while processing DATAREADY event on connection*packet*.

处理TCP数据到达事件时，发送*packetnum*个数据包失败，报文信息为*packet。packet*形式为srcaddr/srcport -\> dstaddr/dstport

 

Sent *packetnum* packet(s) while processing DATAREADY event on connection*packet*.

处理TCP数据到达事件时，成功发送*packetnum*个数据包，报文信息为*packet。packet*形式为srcaddr/srcport -\> dstaddr/dstport

 

Failed to send *packetnum* packet(s) while processing WRITESPACE event on connection*packet*.

处理TCP连接可写事件，发送*packetnum*个数据包失败，报文信息为*packet。packet*形式为srcaddr/srcport -\> dstaddr/dstport

 

Sent *packetnum* packet(s) while processing WRITESPACE event on connection*packet*.

处理TCP连接可写事件，成功发送*packetnum*个数据包，报文信息为*packet。packet*形式为srcaddr/srcport -\> dstaddr/dstport

 

【举例】

\# 打开WAAS错误调试信息开关。添加peer字典表项，内存不足时，打印以下调试信息。

\<Sysname\> debugging waas error

\*Sep 19 09:55:52:338 2014 Sysname WAAS/7/ERROR: Adding peer dictionary entries failed : Insufficient memory

*// 添加peer字典表项失败*

\# 打开WAAS事件调试信息开关。内存进入二级门限时，打印以下调试信息。

\<Sysname\> debugging waas event

\*Aug 14 01:10:08:790 2014 Sysname WAAS/7/EVENT: -MDC=1; State of Memory-alert-gate is severe.

*// 达到内存门限二级告警*

\# 打开WAAS数据冗余消除调试信息开关。DRE解压缩处理时，打印以下调试信息。

\<Sysname\> debugging waas dre

\*Aug 14 01:10:08:790 2014 Sysname WAAS/7/DRE: -MDC=1; DRE decompressed 306 bytes to 280 bytes.

*[// DRE*]*解压缩时,将306字节解压成280字节*

\# 打开WAAS报文调试信息开关。TCP连接上收到TCP报文，打印以下调试信息。

\<Sysname\> debugging waas packet

\*Aug 14 01:10:08:660 2014 Sysname WAAS/7/PACKET: -MDC=1; Sent 1 packet(s) while processing DATAREADY event on connection[192.168.27.1/80 -\> 192.168.17.1/2900. ]

*// 收到DATAREADY事件，在源IPv4地址和端口号为192.168.27.1/80，目的IPv4地址和端口号为192.168.10.1/2900的连接上，成功发送一个报文*

\*Aug 14 01:10:08:792 2014 Sysname WAAS/7/PACKET: -MDC=1; Connection192.168.27.1/80 -\> 192.168.17.1/2901 received event DATAREADY while the focusing event is DATAREADYERRORREPORT.

*// 收到TCP监听事件，在源IPv4地址和端口号为192.168.27.1/80，目的IPv4地址和端口号为192.168.17.1/2901的连接上监听DATAREADY和ERRORREPORT事件时，收到DATAREADY事件*

