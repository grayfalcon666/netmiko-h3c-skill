
**AP管理 \-- AP管理调试命令 \-- debugging wlan ap**

------------------------------------------------------------------------

【命令】

**[debugging wlan ap **[{ **all** \| **name** *ap-name* \| **serial-id** *serial-id* \| **mac-address** *mac-address* } { **all** \| **error** \| **event** }]]

**[undo debugging wlan ap **[{ **all \| name** *ap-name* \| **serial-id** *serial-id* \| **mac-address** *mac-address* \| { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示所有AP。

**[name ***ap-name*]：指定AP名称。*ap-name*为AP的名称，为1～63个字符的字符串，不区分大小写。

**[serial-id** *serial-id*]：指定AP的序列号。*serial-id*为AP的序列号，为1～127个字符的字符串，不区分大小写。

**[mac-address** *mac-address*]：指定AP的MAC地址。*mac-address*为AP的MAC地址，输入格式为H-H-H。

**[all**]：表示APMGR所有调试信息开关。

**[error**]：表示APMGR错误类型调试信息开关。

**[event**]：表示APMGR事件类型调试信息开关。

【描述】

**[debugging wlan ap**]命令用来打开AP上APMGR调试信息开关。**undo debugging wlan ap**命令用来关闭AP上APMGR调试信息开关。

缺省情况下，所有AP上APMGR调试信息开关处于关闭状态。

表1-1 debugging wlan ap all event命令输出信息描述表

字段

描述

Created AP *ap-name*.

成功创建名称为*ap-name*的AP

Deleted AP *ap-name*.

成功删除名称为*ap-name*的AP

Synchronized AP information

同步数据结束

Sent message to the kernel

下发消息至内核

表1-2 debugging wlan ap all error命令输出信息描述表

字段

描述

Failed to open APDB user script.

打开APDB用户脚本失败

Failed to decode APDB user script.

解析APDB用户脚本失败

【举例】

\# 打开所有AP上WLAN模块的事件调试信息开关，创建手工AP后，会有如下调试信息。

\<Sysname\> debugging wlan ap all event

\<Sysname\> system view

Sysname wlan ap ap1 model WA2100

\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Created AP ap1.

*// 成功创建一个手工AP，AP名称为ap1*

\# 打开所有AP上WLAN模块的事件调试信息开关，删除手工AP后，会有如下调试信息。

\<Sysname\> debugging wlan ap all event

\<Sysname\> system view

Sysname undo wlan ap ap1

\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Deleted AP ap1.

*// 成功删除一个手工AP，AP名称为ap1*

\# 打开所有AP上WLAN模块的所有调试信息开关，删除手工AP后，会有如下调试信息。

\<Sysname\> debugging wlan ap all all

\<Sysname\> system view

Sysname undo wlan ap ap1

\*Jul 25 14:20:35:749 2013 H3C APMGR/7/Event: -MDC=1; Deleted AP ap1.

*// 成功删除一个手工AP，AP名称为ap1*

**AP管理 \-- AP管理调试命令 \-- debugging wlan capwap**

------------------------------------------------------------------------

【命令】

**[debugging wlan capwap**[ { **all** \| **error** \| **event** \| **fsm** \| **packet** { **control** { **receive** \| **send** } [ **verbose** ] \| **data** } \| **timer** }]]

**[undo debugging wlan capwap **[{ **all** \| **error** \| **event** \| **fsm** \| **packet** { **control** { **receive** \| **send** } [ **verbose** ] \| **data** } \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示CAPWAP所有类型调试信息开关。

**[error**]：表示CAPWAP错误类型调试信息开关。

**[event**]：表示CAPWAP事件类型调试信息开关。

**[fsm**]：表示CAPWAP状态机调试信息开关。

**[packet**]：表示CAPWAP报文调试信息开关。

**[control**]：表示CAPWAP控制报文调试信息开关。

**[receive**]：表示CAPWAP报文接收调试信息开关。

**[send**]：表示CAPWAP报文发送调试信息开关。

**[verbose**]：表示CAPWAP详细调试信息开关。

**[data**]：表示CAPWAP数据报文调试信息开关。

**[timer**]：表示CAPWAP定时器调试信息开关。

【描述】

**[debugging wlan capwap**]命令用来打开CAPWAP调试信息开关。**undo debugging wlan capwap**命令用来关闭CAPWAP调试信息开关。

缺省情况下，所有CAPWAP调试信息开关处于关闭状态。

表1-3 debugging wlan capwap error命令输出信息描述表

字段

描述

 

Failed to verify CAPWAP header.

校验控制报文CAPWAP header失败

 

Failed to verify CAPWAP control header.

校验控制报文CAPWAP control header失败

 

Failed to send *MsgType* message.

发送*MsgType*类型报文失败。*MsgType*取值如下：

·unknown message：未知报文

·discovery request：发现请求报文

·discovery response：发现回复报文

·join request：加入请求报文

·join response：请求加入回复报文

·configuration request：配置请求报文

·configuration response：配置回复报文

·configuration update request：配置更新请求报文

·configuration update response：配置更新回复报文

·WTP event request：WTP事件请求报文

·WTP event response：WTP事件回复报文

·change state event request：状态事件改变请求报文

·change state event response：状态事件改变回复报文

·echo request：回声请求报文

·echo response：回声回复报文

·image data request：镜像数据请求报文

·image data response：镜像数据回复报文

·reset request：重启请求报文

·reset response：重启回复报文

·primary discovery request：优先发现请求报文

·primary discovery response：优先发现回复报文

·data transfer request：数据传输请求报文

·data transfer response：数据传输回复报文

·clear configuration request：清除配置请求报文

·clear configuration response：清除配置回复报文

·ctation configuration request：Station配置请求报文

·station configuration response：Station配置回复报文

·WLANconfiguration request：WLAN配置请求报文

·WLANconfiguration response：WLAN配置回复报文

 

Failed to match *MsgType* with SeqNum *SeqNum*.

匹配序列号为*SeqNum*类型为*MsgType*的报文失败*MsgType*取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Received duplicate *MsgType* with SeqNum *SeqNum*.

收到重复的序列号为*SeqNum*的*MsgType*类型报文*MsgType*取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Received old *MsgType* with SeqNum *SeqNum*.

收到序列号为*SeqNum*的旧的*MsgType*类型报文

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Number of packets in the retransmission queue exceeded the limit *MaxNum*.

重传队列中缓存的报文超过最大数量*MaxNum*

 

Failed to retransmit *MsgType* and tore down the tunnel: Number of retransmissions exceeded the limit *RetranCnt.*

*[MsgType*]类型报文重传次数达到*RetranCnt*次数导致重传失败，断开隧道

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Failed to retransmit *MsgType* *RetranCnt* times.

*[MsgType*]类型报文重传次数达到*RetranCnt*次数导致重传失败。

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Failed to send fragment *FragNum* of *MsgType* with SeqNum *SeqNum* to AP at address:*port.*

向地址为*address*端口号为*port *的AP发送*MsgType*类型报文的第*FragNum*个分片失败

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Failed to send all fragments of *MsgType* with SeqNum *SeqNum* to AP at address:*port.*

向地址为*address*端口号为*port *的AP发送*MsgType*类型报文的分片未全部成功

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

 

Received packet fragments exceeded the upper limit.

接收报文的分片个数超过上限

 

Discarded a duplicate fragment.

丢弃重复的分片

 

Failed to decode TLV: Invalid packet length.

报文长度非法，解析TLV失败

 

Failed to decode TLV: Type = *TlvType*, Length = *TlvLen*.

解析类型为*TlvType*，长度为*TlvLen*的TLV失败

 

Failed to decode Vendor TLV: Invalid packet length.

报文长度非法，解析Vendor TLV失败

 

Failed to decode Vendor TLV: Element ID=*ElementID*, element Length=*ElementLen*.

解析元素类型标识为*ElementID*，长度为*ElementLen*的Vendor TLV失败

 

Failed to process discovery request: WTP Model Number was not included in WTP BoardData.

WTP BoardData中不包含WTP Model Number，处理Discovery Reqeust失败

 

Failed to process discovery request: WTP Board Data has no serial ID and MAC address.

WTP BoardData中不包含SerialID和MAC地址，处理Discovery Reqeust失败

 

Failed to process discovery request from AP with serial ID *serial-id*: AP reported wrong radio numbers.

序列号为*serial-id*的AP上报错误的Radio个数，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported hardware version.

AC不支持序列号为*serial-id*的AP的硬件版本，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported boot version.

AC不支持序列号为*serial-id*的AP上的启动文件版本，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported AP.

AP不支持该序列号的AP，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unmatched model number.

AC不支持序列号为*serial-id*的AP的model，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unmatched model number.

序列号为*serial-id*的AP的型号名和AC上配置的不符，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported tunnel mode.

AC不支持序列号为*serial-id*的AP的隧道模式，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported MAC type.

AC不支持序列号为*serial-id*的AP的MAC类型，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unsupported discovery type.

不支持序列号为*serial-id*的AP的发现类型，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: No WTP Descriptor TLV.

序列号为*serial-id*的AP的Discovery Request报文中缺少WTP Descriptor TLV，处理Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: No WTP Board Data TLV.

Discovery Request报文中缺少WTP Board Data TLV，处理Discovery Request失败

 

Failed to process fast recovery: Unmatched model.

Model不匹配，处理快速恢复失败

 

Failed to process fast recovery: Unmatched Serial ID.

Serial ID不匹配，处理快速恢复失败

 

Failed to process fast recovery:Unmatched MAC address.

MAC Address不匹配，处理快速恢复失败

 

Failed to process discovery request from AP with serial ID *serial-id* in Run state: Invalid fast recovery.

由于快速回复不合法AC在Run状态时处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to process discovery request from AP with serial ID *serial-id*.

APMGR处理序列号为*serial-id*的AP的Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Invalid AP state.

当前AP的状态非法，处理序列号为*serial-id*的AP的Discovery Request失败

 

Failed to process discovery request from AP with serial ID *serial-id*: MAC address was already in use.

相同的Mac地址已经被使用,处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to process discovery request from AP with serial ID *serial-id*: AC has no available IP address.

AC没有可用的ip地址，处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to process discovery request from AP with serial ID *serial-id*: No available AP configurations.

没有可用的AP配置信息，处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Number of APs exceeded the limit.

超过了AC允许上线的AP最大个数，处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to process discovery request from AP with serial ID *serial-id*: Unknown error.

除已知错误码外的其它问题，处理序列号为*serial-id*的AP的Discovery Request报文失败

 

Failed to decode discovery request.

解析Discovery Request失败

 

Failed to decode join request.

解析Join Request失败

 

Failed to process join request: No WTP Board Data TLV in the request.

Join Request报文中缺少WTP Board Data TLV，处理Join Request失败

 

Failed to process join request from AP with serial ID *serial-id*: No WTP Descriptor TLV.

序列号为*serial-id*的AP的Join Request报文中缺少WTP Descriptor TLV，处理Join Request失败

 

Failed to process join request from AP with serial ID *serial-id*: No Session ID TLV.

序列号为*serial-id*的AP的Join Request报文中缺少SessionID TLV，处理Join Request失败

 

Failed to process join request: WTP Board Data TLV lacks necessary sub element.

WTP BoardData中缺少必要子元素，处理Join Request失败

 

Failed to process join request from AP with serial ID *serial-id*: Number of APs exceeded the limit.

AP个数超过限制，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Unsupported transport protocol.

Transport Protocol不支持，处理序列号为*serial-id*的AP的Join request失败

Failed to process join request from AP with serial ID *serial-id*: APMGR has no available license.

Apmgr进程没有可用的证书，处理序列号为*serial-id*的AP的Join Request报文失败

Failed to process join request from AP with serial ID *serial-id*: Not enough memory.

内存达到上限，处理序列号为*serial-id*的AP的Join Request报文失败

Failed to process join request from AP with serial ID *serial-id*: Invalid AP online info.

由于AC检查到AP上线信息不合法，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to add AP running info.

由于添加AP运行数据失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to apply AP group configurations.

由于应用AP组配置失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to create an auto AP.

创建自动AP失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to create a CTLAP.

创建CTLAP失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to add the AP to an AP group.

加入AP组失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to create AP private data.

创建AP私有数据失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: MAC authentication failed.

请求MAC地址认证失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Failed to create private data for CTLAP.

创建CTLAP私有数据失败，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Unknown error.

除已知错误码外的其他问题，处理序列号为*serial-id*的AP的Join Request报文失败

Failed to process process join request from AP with serial ID *serial-id*: Unsupported MAC type.

Mac Type不支持，处理序列号为*serial-id*的AP的Join request失败

Failed to process process join request from AP with serial ID *serial-id*: Unsupported tunnel mode.

Tunnel mode不匹配，处理序列号为*serial-id*的AP的Join request失败

Failed to process process join request from AP with serial ID *serial-id*: Session ID was already in use.

Session ID已被使用，处理序列号为*serial-id*的AP的Join request失败

Failed to process process join request from AP with serial ID *serial-id*: Unmatched model number.

序列号为*serial-id*的AP的型号名和AC上配置的不符，处理序列号为*serial-id*的AP的Join request失败

Failed to process process join request from AP with serial ID *serial-id*: Unmatched number of radios.

Radio个数错误，处理序列号为*serial-id*的AP的Join request失败

Failed to process join request from AP with serial ID *serial-id*: Unsupported boot version.

启动文件错误，处理序列号为*serial-id*的AP的Join request失败

Failed to process the second half of join request: Invalid AP ID.

AP ID无效，处理Join request后半部分失败

Failed to add an AP according to join request from AP with serial ID *serial-id*.

根据序列号为*serial-id*的AP的Join request报文信息来添加AP失败

Failed to process join request from AP with serial ID *serial-id* in Run state: Invalid fast recovery.

由于快速恢复不合法，在Run状态下处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: Invalid AP state.

当前AP的状态非法，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: MAC address was already in use.

相同的Mac地址已经被使用，处理序列号为*serial-id*的AP的Join Request失败

Received configuration update response with wrong error code *ResultCode* from AP *ap-name*.

AC接收到*ap-name*回复的错误的配置更新结果码为*ResultCode*的Configuration Update Response报文

Failed to decode configuration update response.

AC解析Configuration Update Response报文失败

Failed to process configuration status request.

AC处理Configuration Status Request报文失败

Failed to decode configuration status request.

AC解析Configuration Status Request报文失败

Failed to decode reset response.

AC解析Reset Response报文失败

Failed to create image file keep-alive timer.

创建image文件保活定时器失败

Failed to write message with type *type* and sub type *sub-type* to AP entity thread queue*.

子线程写主类型为*type*子类型为*sub-type*的消息到AP实体线程的消息队列失败。*type*取值为以下两种：

·6：AC端Image模块消息

·7：AP端Image模块消息

*[sub-type*]取值为以下几种：

·0：CAPWAP读镜像文件请求

·1：CAPWAP写镜像文件请求

·2：LWAPP读镜像文件请求

·3：LWAPP读镜像文件请求

·4：CAPWAP读镜像文件回复

·5：CAPWAP读镜像文件回复

·6：LWAPP读镜像文件回复

·7：LWAPP读镜像文件回复

·8：文件线程退出

Failed to write message with type *type* and sub type *sub-type to* file thread queue.

AP实体线程写主类型为*type*子类型为*sub-type*的消息到文件线程的消息队列失败

*[type*]、*sub-type*的取值请参见Failed to write entity-thread queue type *type* by sub-type *sub-type*中*type*、*sub-type*的取值

Failed to get current directory.

获取当前工作路径失败

Failed to allocate memory for image file *file-name*.

为文件名为的*file-name*的Image文件内存分配失败

Failed to read image file *file-name*.

读取文件名为*file-name*的Image文件失败

Failed to open image file *file-name*.

打开文件名为*file-name*的Image文件打开失败

Failed to exit file thread.

文件线程退出失败

Failed to create file thread.

文件线程创建失败

Failed to initiate file thread.

文件线程初始化失败

Failed to download image file *file-name* for AP *ap-name*.

Image文件下载失败

Failed to decode image data request.

Image Data Request解析失败

Received invalid image data request.

收到无效的Image Data Request报文

Number of images downloaded at the same time exceeded the limit.

超出Image下载上限

Failed to process image data request.

Image Data Request处理失败

Failed to decode image data response.

Image Data Response解析失败

Received invalid image data response.

收到无效的Image Data Response报文

Failed to process image data response.

Image Data Response处理失败

Failed to send data channel keep-alive message.

发送数据隧道保活报文失败

Failed to process data channel keep-alive message: Session ID TLV didn\'t exist.

处理数据隧道保活报文失败，Session ID TLV不存在

Failed to process data channel keep-alive message: Invalid session ID.

处理数据隧道保活报文失败，Session ID TLV无效

LWAPP: Failed to verify LWAPP transport header.

LWAPP：校验控制报文LWAPP transport header失败

LWAPP: Failed to verify LWAPP control header.

LWAPP：校验控制报文LWAPP control header失败

LWAPP: Failed to send *MsgType*.

LWAPP：发送*MsgType*类型报文失败

*[MsgType*]取值如下：

·unknown message：未知报文

·discovery request：发现请求报文

·discovery response：发现回复报文

·join request：加入请求报文

·join response：加入回复报文

·join ACK：加入确认报文

·join confirm：加入确认回复报文

·image data request：镜像数据请求报文

·image data response：镜像数据回复报文

LWAPP: Failed to match *MsgType* with SeqNum *SeqNum*.

LWAPP：匹配序列号为SeqNum类型为MsgType的报文失败*MsgType*取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

LWAPP: Received duplicate *MsgType* with SeqNum *SeqNum*.

LWAPP：接收到序列号为*SeqNum*的重复请求报文，即序列号等于上次接受的请求报文序列号。

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

LWAPP: Received old *MsgType* with SeqNum *SeqNum*.

LWAPP：接收到序列号为*SeqNum*的旧的请求报文，即序列号小于上次接收的请求报文序列号

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

LWAPP: Number of packets in the retransmission queue exceeded the limit *MaxNum*.

LWAPP：重传队列中缓存的报文超过最大数量*MaxNum*

LWAPP: Failed to retransmit *MsgType* and tore down the tunnel: Number of retransmissions exceeded the limit *RetranCnt*.

LWAPP：报文重传*RetranCnt*次后失败，断开隧道

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

LWAPP: Failed to retransmit *MsgType* *RetranCnt* times.

LWAPP：报文重传*RetranCnt*次后失败

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

LWAPP: Failed to process discovery request because WTP Descriptor TLV didn\'t exist.

LWAPP：Discovery Request没有携带Descriptor TLV

LWAPP: Failed to process discovery request because WTP Name TLV didn\'t exist.

LWAPP：Discovery Request没有携带WTP Name TLV

LWAPP: Failed to process discovery request because WTP Radio Information TLV didn\'t exist.

LWAPP：Discovery Request没有携带Radio Information TLV

LWAPP: Failed to process discovery request: Unsupported discovery type.

LWAPP：发现类型不支持

LWAPP: Failed to process discovery request: Unmatched number of radios.

LWAPP：Radio数量不匹配，处理Discovery Request失败

LWAPP: Failed to process discovery request: Unsupported hardware version.

LWAPP：硬件版本不支持，处理Discovery Request失败

LWAPP: Failed to process discovery request: Unsupported boot version.

LWAPP：AC不支持AP的启动版本，处理Discovery Request失败

LWAPP: Failed to process discovery request: Unsupported AP software version.

LWAPP：AC不支持AP的软件版本，处理Discovery Request报文失败

LWAPP: Failed to process Discovery Request because WTP name carried default serial-ID.

LWAPP：WTP Name中携带默认的序列号，处理Discovery Request报文失败

LWAPP: Failed to process Discovery Request because WTP name carried auto serial-ID.

LWAPP: WTP Name中携带自动序列号，处理Discovery Request报文失败

LWAPP: Failed to process discovery request: Serial-ID didn't match the AP name.

LWAPP：Discovery Request中的serial-id和AP的Name不匹配

LWAPP: Failed to process discovery request: WTP Board Data carried default model number.

LWAPP：WTP Board Data中携带默认的型号，处理Discovery Request报文失败

LWAPP: Received discovery request when AP was in non-idle state.

LWAPP：AC在AP处于非Idle状态收到Discovery Request报文

LWAPP: Failed to process discovery request: Unmatched model number.

LWAPP：型号不匹配，处理Discovery Request失败

LWAPP: APMGR Failed to process discovery request.

LWAPP：APMGR处理Discovery Request失败

LWAPP:Failed to process discovery request: MAC address was already in use.

LWAPP：WTP MAC地址重复，处理Discovery Request失败

LWAPP: Failed to decode discovery request.

LWAPP：解析Discovery Request报文失败

LWAPP: Failed to decode join request.

LWAPP：解析Join  Request报文失败

LWAPP: Failed to decode join ACK.

LWAPP：解析Join Ack报文失败

LWAPP: Failed to process join request: WTP Name TLV didn't exist.

LWAPP：WTP Name TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request: WTP Descriptor TLV didn't exist.

LWAPP：WTP Descriptor TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request: Session ID TLV didn't exist.

LWAPP：Session ID TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request: WTP ADDR TLV didn't exist.

LWAPP：WTP ADDR TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request: WTP Radio Information TLV didn't exist.

LWAPP：WTP Radio Information TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request: XNONCE TLV didn't exist.

LWAPP：XNONCE TLV不存在，处理Join Request报文失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*: Number of APs exceeded the limit.

LWAPP：AP个数超过限制，处理序列号为*serial-id*的AP的Join Request报文失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*: Unmatched number of radios.

LWAPP：Radio个数错误，处理序列号为*serial-id*的AP的Join Request失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*:Unsupported hardware version.

LWAPP：硬件版本错误，处理序列号为*serial-id*的AP的Join Request失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*: Unsupported boot version.

LWAPP：启动版本错误，处理序列号为*serial-id*的AP的Join Request失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*: Session ID was already in use.

LWAPP：SessionID已被使用，处理序列号为*serial-id*的AP的Join Request失败

LWAPP: Failed to process join request from AP with serial ID *serial-id*: Invalid AP state.

LWAPP：AP当前的状态不合法，处理序列号为*serial-id*的AP的Join Request失败

Failed to process join request from AP with serial ID *serial-id*: MAC address was already in use.

LWAPP：相同的Mac地址已经被使用，处理序列号为*serial-id*的AP的Join Request失败

LWAPP: Failed to add AP according to join request from AP with serial ID *serial-id*.

LWAPP：根据序列号为*serial-id*的AP的Join request报文信息来添加AP失败

LWAPP: Failed to process the second half of join request: Invalid AP ID.

LWAPP：AP ID无效，处理Join request后半部分失败

LWAPP: Failed to process join ACK from AP with serial ID *serial-id*: Wrong session ID.

LWAPP：SessionID错误，处理序列号为*serial-id*的AP的Join Ack失败

LWAPP: Failed to decode image data request message.

LWAPP：解析Image Data Request报文失败

LWAPP: Failed to process image data request message.

LWAPP：处理Image Data Request报文失败

LWAPP: Number of images downloaded at the same time exceeded the limit.

LWAPP：超出Image下载上限

LWAPP: Received invalid Image Data Request message.

LWAPP：收到无效的Image Data Request报文

表1-4 debugging wlan capwap event命令输出信息描述表

字段

描述

Received join request from AP with serial ID *serial-id* in Run state and tore down the tunnel.

Run状态下收到序列号为*serial-Id*的Join Request报文， 断开隧道

Cannot process join request from AP with serial ID *serial-id*: AP down event was being processed.

Apmgr正在处理down事件，接收到序列号为*serial-Id*的Join Request报文，丢弃报文

CAPWAP tunnel to AP *ap-name* went down:*.* R*eason*.

由于原因*reason*，AC端断开和*ap-name*间的隧道

*[reason*]取值如下：

·Neighbor dead timer expired：Neighbor Dead定时器超时

·Wait request timer expired：Wait Request定时器超时

·Data check timer expired：Data Check定时器超时

·Failed to process data channel keep-alive message：处理数据隧道保活报文失败

·Failed to process request：处理请求报文失败

·AP was reset：重启AP

·AP was deleted：删除AP

·Failed to go up：AP隧道UP失败

·Serial number changed：修改序列号

·Number of APs exceeded the limit：AP个数超过上限

·Processjoin request in Run state：Run状态下收到并处理Join Request报文

·Failed to create AP context：创建Context失败

·Failure result code：失败的错误码

·Failed to retransmit message ：重传失败

·Failed to download image file：下载image文件失败

·Image file downloaded successfully：下载image文件成功

·File operation timer expired：File operation定时器超时

LWAPP: LWAPP tunnel to AP *ap-name* went down: R*eason*.

LWAPP：AC端断开和*ap-name*间的LWAPP隧道

*[reason*]取值如下：

·Wait request timer expired：Wait Request定时器超时

·Number of APs exceeded the limit：AP个数超过上限

·Failed to process request：处理请求报文失败

·Failed to create AP context：创建Context失败

·AP was reset：重启AP

·AP was deleted：删除AP

·Failed to go up：AP隧道UP失败

·Serial number changed：修改序列号

·Failed to retransmit message：重传失败

·Failed to download image file：Image文件下载失败

·Image file downloaded successfully：Image文件下载成功

·File operation timer expired：File operation定时器超时

表1-5 debugging wlan capwap fsm命令输出信息描述表

字段

描述

Enter Join state.

AC进入Join 状态

Enter Config state.

AC进入Config状态

Enter Image Download state

AC进入Image Download状态

Enter Data Check state.

AC进入Data Check状态

Enter Run state.

AC进入Run状态

LWAPP: Enter Join state.

LWAPP：AC进入Join状态

LWAPP: Enter Join Confirm state.

LWAPP：AC进入Join Confirm状态

LWAPP: Enter Image Download state.

LWAPP：AC进入Image Download状态

表1-6 debugging wlan capwap packet control receive命令输出信息描述表

字段

描述

Received *MsgType* with SeqNum *SeqNum* from AP at *address:port.*

从地址为*address*端口号为*port*的AP接收序列号为*SeqNum*的 *MsgType*类型报文

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

Received a fragment from AP at *address:port.*

从地址为*address*端口号为*port*的AP接收到一个控制报文分片

Assembled *MsgType* with SeqNum *SeqNum* from AP at *address:port.*

从地址为*address*端口号为*port*的AP接收到完整的一组分片并成功重组为序列号为*SeqNum*的 *MsgType*类型报文

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

LWAPP: Received *MsgType* with SeqNum *SeqNum* from AP at *address:port.*

LWAPP：从地址为*address*端口号为*port*的AP接收序列号为*SeqNum*的*MsgType*类型报文

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

表1-7 debugging wlan capwap packet control receive verbose命令输出信息描述表

字段

描述

Received *MsgType* from AP at *address:port.* Length=*length*. *content*

从地址为*address*端口号为*port*的AP接收长度为*length*的* MsgType*类型报文，其详细信息为*content*

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

Received fragment from AP at *address:port.*, Length= *length*. *content*

从地址为*address*端口号为*port*的AP接收到一个控制报文分片，长度为*length*，详细信息为content。

LWAPP: Received *MsgType* from AP at *address:port.* Length= *length*. *content*

LWAPP：从地址为*address*端口号为*port*的AP接收长度为*length*的*MsgType*类型报文，其详细信息为*content*。

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

表1-8 debugging wlan capwap packet control send命令输出信息描述表

字段

描述

Sent *MsgType* with SeqNum *SeqNum* to AP at *address:port.*

发送序列号为*SeqNum*的*MsgType*类型报文到地址为*address*端口号为*port*的AP

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

Sent fragment *FragNum* of *MsgType* with SeqNum *SeqNum* to AP at *address:port.*

发送序列号为*SeqNum*的*MsgType*类型报文的第*FragNum*个分片到地址为*address*端口号为*port*的AP

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

Sent all fragments of *MsgType* with SeqNum *SeqNum* to AP at *address:port.*

发送序列号为*SeqNum*的*MsgType*类型报文的所有分片到地址为*address*端口号为*port*的AP

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

LWAPP: Sent *MsgType* with SeqNum *SeqNum* to AP at *address:port.*

LWAPP：发送序列号为*SeqNum*的*MsgType*类型报文到地址为*address*端口号为*port*的AP

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

表1-9 debugging wlan capwap packet control send verbose命令输出信息描述表

字段

描述

Sent *MsgType* sent to AP at *address*:*port*: Length=*length*. *content*

向地址为*address*端口号为*port*的AP发送长度为*length*的* MsgType*类型报文，其详细信息为*content*

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

Sent fragment *FragNum* of *MsgType* sent to AP at *address:port: Length=length. content*

向地址为*address*端口号为*port*的AP发送到第*FragNum*个控制报文分片，长度为*length*，详细信息为*content*

*[MsgType*]取值请参见Failed to send *MsgType* message中的*MsgType*取值

LWAPP: Sent *MsgType* sent to AP at *address:port: Length=length. content*

LWAPP：向地址为*address*端口号为*port*的AP发送长度为*length*的* MsgType*类型报文，其详细信息为*content*

*[MsgType*]取值请参见LWAPP: Failed to send *MsgType* message中*MsgType*的取值

表1-10 debugging wlan capwap data命令输出信息描述表

字段

描述

Sent data channel keep-alive message to AP.

向AP发送数据隧道保活报文成功

Received data channel keep-alive message from AP.

成功收到来自AP的数据隧道保活报文

表1-11 debugging wlan capwap timer命令输出信息描述表

字段

描述

Wait Request timer expired.

Wait Request定时器超时

File *file-name* operation timer expired.

*[file-name*]文件的操作定时器超时

Image file keep-alive timer expired. Freed the file *file-name* buffer.

*[file-name*]文件的文件保活定时器超时，释放文件缓存

Debug Wait timer of AP *ap-name* expired.

*[ap-name*]上的DataTransfer等待分片定时器超时

Debug Refresh timer of AP *ap-name* expired.

*[ap-name*]上的DataTransfer重启调试信息的刷新定时器

Retransmission timer of AP *ap-name* expired.

*[ap-name*]上的报文收发的重传定时器超时

Fragment timer of AP *ap-name* expired.

*[ap-name*]上的报文收发的分片定时器超时

Data Check timer expired.

Data Check定时器超时

LWAPP: Retransmission timer of AP *ap-name* expired.

LWAPP：*ap-name*上的报文收发的重传定时器超时

LWAPP: File *file-name* operation timer expired.

LWAPP：*file-name*文件操作定时器超时

【举例】

\# AP发现AC的过程中，在AC端打开capwap fsm调试开关，会有如下调试信息：

\<AC\> debugging wlan capwap fsm

\*Sep 10 10:59：17:404 2013 H3C.com CWS/7/FSM： -MDC = 1; Enter Join state.

*[// AC*]*进入Join状态*
