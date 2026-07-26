
**RSVP \-- RSVP调试命令 \-- debugging rsvp all**

------------------------------------------------------------------------

【命令】

**[debugging rsvp all**]

**[undo debugging rsvp all**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp all**]命令用来打开RSVP所有调试信息开关。**undo debugging rsvp authentication**命令用来关闭RSVP所有调试信息开关。

缺省情况下，RSVP所有的调试信息开关均处于关闭状态。

【举例】

\# 打开RSVP的所有调试信息开关。

\<Sysname\> debugging rsvp all

**RSVP \-- RSVP调试命令 \-- debugging rsvp authentication**

------------------------------------------------------------------------

【命令】

**[debugging rsvp authentication**]

**[undo debugging rsvp authentication**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp authentication**]命令用来打开RSVP认证调试信息开关。**undo debugging rsvp authentication**命令用来关闭RSVP认证调试信息开关。

缺省情况下，RSVP认证调试信息开关处于关闭状态。

表1-1 debugging rsvp authentication命令输出信息描述表

字段

描述

Looking up SA for the incoming *message-type* message: from *start-address* to *end-address*.

为接收的*message-type*报文查找认证关联：起点地址*start-address*，终点地址*end-address*

Looking up SA for the outgoing *message-type* message: from *start-address* to *end-address*.

为发送的*message-type*报文查找认证关联：起点地址*start-address*，终点地址*end-address*

Created a receive mode SA: from *start-address* to *end-address*.

创建接收认证关联：起点地址*start-address*，终点地址*end-address*

Created a send mode SA: from *start-address* to *end-address*.

创建发送认证关联：起点地址*start-address*，终点地址*end-address*

Sent an integrity challenge message.

发送integrity challenge消息

Sent an integrity response message.

发送integrity response消息

Received an integrity challenge message, from *start-address* to *end-address.*

收到integrity challenge消息，起点地址*start-address*，终点地址*end-address*

Received an integrity response message, from *start-address* to *end-address*.

收到integrity response消息，起点地址*start-address*，终点地址*end-address*

Challenge state is not in progress.

Challenge状态不是正在协商

Challenge object is valid.

Challenge对象有效

Challenge object is invalid.

Challenge对象无效

No integrity object.

没有integrity对象

No challenge object.

没有challenge对象

Sequence *sequence* is out of the receiving window.

序列号*sequence*超出接收窗口

Replayed sequence *sequence*.

序列号*sequence*重复

Sequence *sequence* is valid.

序列号*sequence*有效

MD5 digest is valid.

MD5摘要有效

MD5 digest is invalid.

MD5摘要无效

【举例】

\# 在接口视图下配置RSVP认证密钥，打开RSVP认证调试信息开关，从接口接收到RSVP消息后打印如下调试信息。

\<Sysname\> debugging rsvp authentication

\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; Looking up SA for the incoming path message: from 12.11.110.11 to 10.33.33.33.                             

*// 为接收到的Path消息查找认证关联，认证起点地址为12.11.110.11，目的地址为10.33.33.33。*

\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; MD5 digest is valid.       

*[// Path*]*消息的MD5摘要有效。*

\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; Sequence 5778030575734489139 is valid.

*[// Path*]*消息的序列号有效。*

\*Aug 19 08:33:15:278 2012 Sysname RSVP/7/AUTH: -MDC=1; Looking up SA for the outgoing resv message: from 12.11.110.12 to 12.11.110.11.

*// 为发送的Resv消息查找认证关联，认证起点地址为12.11.110.12，目的地址为12.11.110.11。*

\*Aug 19 08:33:22:434 2012 Sysname RSVP/7/AUTH: -MDC=1; MD5 digest is valid.

*[// Resv*]*消息的MD5摘要有效。*

\*Aug 19 08:33:22:434 2012 Sysname RSVP/7/AUTH: -MDC=1; Sequence 5778030575734489140 is valid.

*[// Resv*]*消息的序列号有效。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp error**

------------------------------------------------------------------------

【命令】

**[debugging rsvp error**]

**[undo debugging rsvp error**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp error**]命令用来打开RSVP错误调试信息开关。**undo debugging rsvp error**命令用来关闭RSVP错误调试信息开关。

缺省情况下，RSVP错误调试信息开关处于关闭状态。

表1-2 debugging rsvp error命令输出信息描述表

字段

描述

Failed to receive a packet from socket (*socket-fd*).

从socket（*socket-fd*）接收报文错误

IP TTL expired.

IP TTL超时

RSVP TTL expired.

RSVP TTL超时

Invalid RSVP message type: *message-type*.

无效的RSVP报文类型*message-type*

Invalid RSVP message length: *length*.

RSVP报文长度*length*错误

Invalid RSVP message checksum: *checksum*.

RSVP报文校验和*checksum*错误

Failed to decode object (class number *class-number*) in the *message-type* message.

解码*message-type*报文中类型值为*class-number*的对象失败

Failed to decode the *message-type* message.

解码*message-type*报文失败

Failed to encode *object-type* object in the *message-type* message.

编码*message-type*报文的*object-type*对象失败

Failed to encode the *message-type* message.

编码*message-type*报文失败

Failed to set socket (*socket-fd*) option.

设置socket（*socket-fd*）选项失败

Failed to send packet to socket (*socket-fd*), error code *error-code*.

向socket（*socket-fd*）发送报文失败，错误值为*error-code*

Memory alert (*alert-state*).

内存门限告警，*alert-state*代表内存不足的严重程度，取值范围为0～3，0代表内存状态正常，值越大内存不足越严重

Different service IDs in Tspec: *service-ID1 service-ID2.*

Tspec中服务ID不一致，分别为*service-ID1*和*service-ID2*

Invalid service ID *service-ID* in Tspec.

Tspec中服务ID（*service-ID*）无效

Failed to send HA message.

发送HA消息失败

RSVP is not enabled on interface *interface*

接口*interface*未使能RSVP

【举例】

\# 打开RSVP错误调试信息开关，收到IP TTL超时的RSVP消息后打印如下调试信息。

\<Sysname\> debugging rsvp error

\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; IP TTL expired.

*[// RSVP*]*消息的IP TTL超时。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp frr**

------------------------------------------------------------------------

【命令】

**[debugging rsvp frr**]

**[undo debugging rsvp frr**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp frr**]命令用来打开RSVP快速重路由调试信息开关。**undo debugging rsvp frr**命令用来关闭RSVP快速重路由调试信息开关。

缺省情况下，RSVP快速重路由调试信息开关处于关闭状态。

表1-3 debugging rsvp frr命令输出信息描述表

字段

描述

TC updated bypass *tunnel-name* info, backup bandwidth *bandwidth*, protection CT *class-type*.

TC更新旁路隧道*tunnel-name*信息，保护带宽为*bandwidth*，保护带宽类型为*class-type*.

TC deleted bypass *tunnel-name* info.

TC删除旁路隧道*tunnel-name*信息

Bound bypass *tunnel-name* to CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

旁路隧道*tunnel-name*绑定CR-LSP，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

其中，*direction*取值包括：

·0：表示单向隧道

·1：表示双向隧道的正向CRLSP

·2：表示双向隧道的反向CRLSP

Unbound bypass *tunnel-name* from CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

旁路隧道*tunnel-name*取消绑定CR-LSP，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

Got bypass *tunnel-name* info from TC: backup bandwidth *bandwidth*, protection CT *class-type*.

从TC获取旁路隧道*tunnel-name*信息：保护带宽为*bandwidth*，保护带宽类型为*class-type*.

Failed to get bypass *tunnel-name* info from TC.

从TC获取旁路隧道*tunnel-name*信息失败

Updated the used bandwidth of bypass *tunnel-name* from *bandwidth1* to *bandwidth2*.

旁路隧道*tunnel-name*的已用带宽从*bandwidth1*更新为*bandwidth2*

Looking up bypass tunnel for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

为CR-LSP查找旁路隧道，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

The unused bandwidth *bandwidth* of bypass *tunnel-name* is insufficient for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

旁路隧道*tunnel-name*的未用带宽为*bandwidth*，带宽不足以保护CR-LSP，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

Optimizing bypass tunnel for all CR-LSPs.

正在为所有CR-LSP优化旁路隧道

Finished smoothing FRR configurations.

FRR配置平滑结束

Reset bypass *tunnel-name* info.

重置旁路隧道*tunnel-name*信息

Set staled flag to the bypass *tunnel-name.*

设置旁路隧道*tunnel-name*的老化标记

TC disconnected.

TC和RSVP的连接断开

Finished smoothing all CR-LSPs.

CR-LSP平滑结束

Created CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*.

创建CR-LSP，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

Deleted CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction.*

删除CR-LSP，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

No tunnel available to protect CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

没有可用的Bypass隧道保护主CR-LSP，主CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

Tunnel *bypass-tunnel-id* is the best bypass tunnel for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).

旁路隧道*bypass-tunnel-id*是可以保护主CR-LSP的最佳隧道，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

Received FRR configurations on an interface from TC:

interface index: *if-index*; Bypass number: *bypass-number*;

Bypass tunnel ID: *tunnel-id1*, *tunnel-id2*, *tunnel-id3*;

Auto backup flag: *auto-backup-flag*.

从TC获取接口FRR的配置信息：接口索引为*if-index*；旁路隧道数目为*bypass-number*；旁路隧道ID为：* tunnel-id1*，*tunnel-id2*，*tunnel-id3*；自动备份隧道标记为*auto-backup-flag*

Updated CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*.

FRR处理CR-LSP更新，CR-LSP的目的地址为*dst-addr*，源地址为*src-addr*，tunnel ID为*tunnel-id*，LSP ID为*lsp-id*，方向为*direction*

TC updated FRR configurations. FRR reoptimization time *reoptimize time*; auto backup *auto backup enable flag*; auto backup nexthop only *nexthop only flag*; auto backup removal time *remove time*; auto backup max tunnel number *max-tnlid*; auto backup min tunnel number *min-tnlid*.

收到TC处的FRR配置，优化定时器时间为*reoptimize time*；AUTOFRR使能标记为*auto backup enable flag*；下一跳的使能标记为*nexthop only flag*；删除定时器时间为*removal time*；自动隧道最大值为*max-tnlid*；自动隧道最小值为*min-tnlid*.

Finished smoothing auto FRR configurations, protected path tables, and automatic bypass tunnels.

auto FRR配置平滑，被保护路径表平滑和自动备份隧道信息平滑结束

Finished smoothing all tunnels with process tunnel.

与tunnel进程的隧道平滑结束

Tunnel disconnected.

Tunnel进程和RSVP进程断开连接

Created an auto backup removal timer for the protected path. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;*  protected type *prot-type*; auto tunnel number *tunnel-id*.

为被保护路径表创建removal定时器。接口为*if-index*，目的地址为*dest-addr*，保护的地址为*prot-addr*，保护类型为*prot-type*，自动隧道编号为*tunnel-id*.

Deleted the auto backup removal timer for the protected path. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;*  protected type *prot-type*; auto tunnel number *tunnel-id*.

删除被保护路径表removal定时器。接口为*if-index*，目的地址为*dest-addr*，保护的地址为*prot-addr*，保护类型为*prot-type*，自动隧道编号为*tunnel-id*

Auto backup removal timer for the protected path expired. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;* protected type *prot-type*; auto tunnel number *tunnel-id*.

被保护路径表的删除定时器超时。接口为*if-index*，目的地址为*dest-addr*，保护的地址为*prot-addr*，保护类型为*prot-type*，自动隧道编号为*tunnel-id*.

Begin to recreate automatic bypass tunnels.

开始重新创建自动旁路隧道

Reference count of the protected path updated to *ref-counter*. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr*; protected type *prot-type*.

被保护路径表更新引用计数到*ref-counter**，*被保护接口为*if-index*，目的地址为*dest-addr*，被保护地址为*prot-addr*，保护类型为*prot-type*

Finished smoothing all tunnel interfaces with process IF.

与IF进程的隧道接口信息平滑结束

【举例】

\# 打开RSVP快速重路由调试信息开关。关闭MPLS TE隧道模式的Tunnel接口时，打印如下调试信息。

\<Sysname\> debugging rsvp frr

\<Sysname\> system-view

Sysname interface tunnel 1

Sysname-Tunnel1 display this

\#

interface Tunnel1 mode mpls-te

 mpls te backup bandwidth 1000

 destination 10.33.33.33

\#

return

Sysname-Tunnel1 shutdown

Sysname-Tunnel1

\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; TC deleted bypass tunnel1 info.

*// 删除旁路隧道Tunnel1的信息。*

\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; Deleted CR-LSP: dst 10.33.33.33, src 10.22.22.22, tunnel ID 1, LSP ID 51011, direction 0.

*// 删除CR-LSP，该CR-LSP的目的地址为10.33.33.33，源地址为10.22.22.22，隧道的Tunnel ID为1，LSP ID为51011，该隧道为单向隧道。*

Sysname-Tunnel1 undo shutdown

Sysname-Tunnel1

\*Aug 19 08:45:44:148 2012 Sysname RSVP/7/FRR: -MDC=1; Created CR-LSP: dst 10.33.33.33, src 10.22.22.22, tunnel ID 1, LSP ID 51012, direction 0.

*// 创建CR-LSP，该CR-LSP的目的地址为10.33.33.33，源地址为10.22.22.22，隧道的Tunnel ID为1，LSP ID为51011，该隧道为单向隧道。*

\*Aug 19 08:45:44:148 2012 Sysname RSVP/7/FRR: -MDC=1; TC updated bypass tunnel1 info, backup bandwidth 1000kbps, protection CT 4.

*// 更新旁路隧道Tunnel1的信息，保护带宽为1000kbps，保护带宽类型为CT 4。*

Sysname-Tunnel1 interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp fast-reroute bypass-tunnel tunnel1

Sysname-GigabitEthernet1/0/1

\*Aug 19 08:45:52:706 2012 Sysname RSVP/7/FRR: -MDC=1; Got bypass tunnel1 info from TC: backup bandwidth 1000kbps, protection CT 4.

*// 从TC获取旁路隧道的信息，保护带宽为1000kbps，保护带宽类型为CT 4。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp hello**

------------------------------------------------------------------------

【命令】

**[debugging rsvp hello**]

**[undo debugging rsvp hello**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp hello**]命令用来打开RSVP Hello调试信息开关。**undo debugging rsvp hello**命令用来关闭RSVP Hello调试信息开关。

缺省情况下，RSVP Hello调试信息开关处于关闭状态。

表1-4 debugging rsvp hello命令输出信息描述表

字段

描述

Handling GR ASM, interface *interface*, peer *peer-addr*, GR state *state*, GR event *event*.

GR状态处理，接口为*interface*，邻居地址为*peer-addr*，GR状态为*state*，GR事件为*event*

GR state changed from invalid to ready.

GR状态由invalid变更为ready

GR state changed from ready to invalid.

GR状态由ready变更为invalid

GR state changed from ready to restart.

GR状态由ready变更为restart

GR state changed from restart to recovery.

GR状态由restart变更为recovery

GR state changed from restart to invalid.

GR状态由restart变更为invalid

GR state changed from recovery to invalid.

GR状态由recovery变更为invalid

GR state changed from recovery to restart.

GR状态由recovery变更为restart

Sent a hello request message, src instance *src-instance*, dst instance *dst-instance*.

发送hello请求消息，src instance为*src-instance*，dst instance为*dst-instance*

Replied a hello ACK message, src instance *src-instance*, dst instance *dst-instance*.

回应hello应答消息，src instance为*src-instance*，dst instance为*dst-instance*

Handling hello ASM, interface *interface*, peer  *peer-addr*, hello state *state,* hello event *event.*

Hello状态处理，接口为*interface*，邻居地址为*peer-addr*，hello状态为*state*，hello事件为*event*

Hello state changed from idle to init.

Hello状态从idle变更为init

Hello state changed from init to up.

Hello状态从init变更为up

Hello state changed from init to idle.

Hello状态从init变更为idle

Hello state changed from up to idle.

Hello状态从up变更为idle

Hello state changed from up to init.

Hello状态从up变更为init

The peer *peer-addr* was lost. Hello state changed from up to init.

邻居*peer-addr*丢失，hello状态从up变更为init

The peer\'s hello function was disabled. Hello state changed from up to init.

邻居关闭hello功能，hello状态从up变更为init

Received a hello message in idle state.

在idle状态收到hello报文

Received a hello request message in init state, src instance *src-instance*, dst instance *dst-instance*.

在init状态收到hello请求报文，src instance为*src- instance*，dst instance为*dst-instance*

Receive a hello ACK message in init state, src instance *src-instance*, dst instance *dst-instance*.

在init状态收到hello应答报文，src instance为*src-instance*，dst instance为*dst-instance*

Received a hello request message in up state, src instance *src-instance*, dst instance *dst-instance*.

在up状态收到hello请求报文，src instance为*src-instance*，dst instance为*dst-instance*

Received a hello ACK message in up state, src instance *src-instance*, dst instance *dst-instance*.

在up状态收到hello应答报文，src instance为*src-instance*，dst instance为*dst-instance*

Hello src instance *src-instance* is different from old src instance *old-instance*.

Hello报文中的src instance（*src-instance*）与原来的src instance（*old-instance*）不一致

Hello dst instance *dst-instance* is different from old dst instance *old-instance*.

Hello报文中的dst instance（*dst-instance*）与原来的dst instance（*old-instance*）不一致

Received more than *max-num* erroneous hello messages.

接收错误的hello报文数大于*max-num*

Received an incorrect hello message. Src instance is 0.

接收错误的hello报文，src instance为0

Received an incorrect hello message. Src instance is different.

接收错误的hello报文，src instance不一致

Received an incorrect hello message. Dst instance is different.

接收错误的hello报文，dst instance不一致

Sent *message-type* message to BFD, interface *interface*, src address *src-address*, dst address *dst-address*.

发送*message-type*消息给BFD，接口为*interface*，源地址为*src-address*，目的地址为*dst-address*

Received BFD down message, interface *interface*, peer *peer-address*.

收到BFD down消息，接口为*interface*，邻居地址为*peer-address*

【举例】

\# 在接口视图下配置RSVP Hello扩展功能后，打开RSVP Hello调试信息开关，打印如下调试信息。

\<Sysname\> debugging rsvp hello

\*Aug 19 08:35:12:478 2012 Sysname RSVP/7/HELLO: -MDC=1; Sent a hello request message, src instance 728, dst instance 727.

*// 发送Hello request消息，source instance为728，destination instance为727。*

\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Handling hello ASM, interface GE1/0/1, peer 12.11.110.11, hello state up, hello event received message.

*[// Hello*]*状态处理，接口为GigabitEthernet1/0/1，邻居地址为12.11.110.11，hello状态为up，hello事件为接收到消息*

\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Received a hello ACK message in up state, src instance 727, dst instance 728.

*// 在up状态接收到Hello ACK消息，source instance为727，destination instance为728。*

\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Handling GR ASM, interface GE1/0/1, peer 12.11.110.11, GR state invalid, GR event without object.

*[// GR*]*状态处理，接口为GigabitEthernet1/0/1，邻居地址为12.11.110.11，GR状态为invalid，GR事件为不存在对象*

**RSVP \-- RSVP调试命令 \-- debugging rsvp packet**

------------------------------------------------------------------------

【命令】

**[debugging rsvp packet**]

**[undo debugging rsvp packet**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp packet**]命令用来打开RSVP报文调试信息开关。**undo debugging rsvp packet**命令用来关闭RSVP报文调试信息开关。

缺省情况下，RSVP报文调试信息开关处于关闭状态。

表1-5 debugging rsvp packet命令输出信息描述表

字段

描述

Received a packet from socket *socket-fd*, length *length*, content: *content*.

从socket（*socket-fd*）接收到报文，报文长度为*length*，内容为*content*

Sent a packet to socket *socket-fd*, length *length*, content: *content*.

向socket（*socket-fd*）发送报文，报文长度为*length*，内容为*content*

Received *message-type* message from interface *interface*.

从接口*interface*收到*message-type*消息

Sent *message-type* message to interface *interface*, nexthop *nexthop-addr*, result *result*.

向接口*interface*发送*message-type*消息，下一跳地址为*nexthop-addr*，返回值为*result  *

其中，result的取值包括：

·successful：发送*message-type*消息成功

·failed：发送*message-type*消息失败

【举例】

\# 打开RSVP报文调试信息开关，收到RSVP报文后打印如下调试信息。

\<Sysname\> debugging rsvp packet

\*Aug 19 08:37:47:978 2012 Sysname RSVP/7/PKT: -MDC=1; Sent a packet to socket 41, length 164, content: 45 C0 A4 00 00 00 00 00 FF 2E 9C F8 0C 0B 6E 0C 0C 0B 6E 0B 10 02 00 00 FF 00 00 90 00 24 04 01 01 00 00 01 02 00 00 00 50 30 A4 AC 00 00 00 38 0E EE AA E5 A9 AD 67 71 68 A8 AF A0 BD 8A 4E 91 00 10 01 07 0A 21 21 21 00 00 00 01 0A 0B 0B 0B 00 0C 03 01 0C 0B 6E 0C 00 00 00 02 00 08 05 01 00 00 27 10 00 08 08 01 00 00 00 12 00 24 09 02 00 00 00 07 05 00 00 06 7F 00 00 05 00 00 00 00 44 7A 00 00 00 00 00 00 00 00 00 00 00 00 05 DC 00 0C 0A 07 0A 0B 0B 0B 00 00 47 24 00 08 10 01 00 00 04 7B .

*// 向socket 41发送RSVP报文，报文长度为164字节，报文内容以十六进制形式打印。*

\*Aug 19 08:37:47:978 2012 Sysname RSVP/7/PKT: -MDC=1; Sent resv message to interface GE1/0/1, nexthop 12.11.110.11, result successful.

*// 成功向接口GigabitEthernet1/0/1发送Resv报文，下一跳地址为12.11.110.11。*

\*Aug 19 08:37:51:278 2012 Sysname RSVP/7/PKT: -MDC=1; Sent a packet to socket 41, length 188, content: 46 C0 BC 00 00 00 00 00 FD 2E FF FF 0A 0B 0B 0B 0A 21 21 21 94 04 00 00 10 01 5B 0F FD 00 00 A4 00 10 01 07 0A 21 21 21 00 00 00 01 0A 0B 0B 0B 00 0C 03 01 17 0B 6E 0B 00 00 00 04 00 08 05 01 00 00 27 10 00 08 13 01 00 00 08 00 00 10 CF 07 07 07 04 07 54 75 6E 6E 65 6C 31 00 00 0C 0B 07 0A 0B 0B 0B 00 00 47 24 00 24 0C 02 00 00 00 07 01 00 00 06 7F 00 00 05 00 00 00 00 44 7A 00 00 00 00 00 00 00 00 00 00 00 00 05 DC 00 30 0D 02 00 00 00 0A 01 00 00 08 04 00 00 01 00 00 00 01 06 00 00 01 49 98 96 80 08 00 00 01 00 00 00 00 0A 00 00 01 00 00 05 DC 05 00 00 00 .

*// 向socket 41发送RSVP报文，报文长度为188字节，报文内容以十六进制形式打印。*

\*Aug 19 08:37:51:279 2012 Sysname RSVP/7/PKT: -MDC=1; Sent path message to interface GE1/0/2, nexthop 23.11.110.12, result successful.

*// 成功向接口GigabitEthernet1/0/2发送Path报文，下一跳地址为*23.11.110.12*。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp path**

------------------------------------------------------------------------

【命令】

**[debugging rsvp path** [ **destination** *ip-address* **source** *ip-address* **tunnel-id** *tunnel-id* ]]

**[undo debugging rsvp path**]

【视图】

用户视图

【参数】

**[destination** *ip-address*]：指定隧道的目的地址。

**[source** *ip-address*]：指定隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：指定隧道的ID。*tunnel-id*为隧道ID，取值范围为0～65535。

【描述】

**[debugging rsvp path**]命令用来打开RSVP Path相关的调试信息开关。**undo debugging rsvp path**命令用来关闭RSVP Path相关的调试信息开关。

缺省情况下，RSVP Path相关的调试信息开关处于关闭状态。

表1-6 debugging rsvp path命令输出信息描述表

字段

描述

TC triggered to create ingress CR-LSP, LSP ID *lsp-id*, direction *direction*.

TC触发创建头节点CR-LSP，LSP ID为*lsp-id*，方向为*direction*

TC triggered to delete ingress CR-LSP, LSP ID *lsp-id*, direction *direction*.

TC触发删除头节点CR-LSP，LSP ID为*lsp-id*，方向为*direction*

TC triggered to create egress CR-LSP, ingress LSR ID *lsr-id*, tunnel ID *tunnel-id*.

TC触发创建尾节点CR-LSP，头节点LSR ID为*lsr-id*，tunnel ID为*tunnel-id*

TC triggered to delete egress CR-LSP, ingress LSR ID *lsr-id*, tunnel ID *tunnel-id*.

TC触发创建尾节点CR-LSP，头节点LSR ID为*lsr-id*，tunnel ID为*tunnel-id*

Received a path message. Created a new PSB.

收到path消息，新建PSB

Received a path message. Updated the old PSB.

收到path消息，更新PSB

PSB\'s PHOP changed from *phop-addr1* to *phop-addr2*.

PSB的PHOP从*phop-addr1*变为*phop-addr2*

PSB incoming label *label1* is different from the recovery label *label2* in the path message.

PSB的入标签*label1*与path消息中的recovery label *label2*不一致

Allocated resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.

从TRM分配资源：接口为*interface*，带宽为*bandwidth*，带宽类型为*class-type*，返回值为*result *

其中，result的取值包括：

·successful：资源分配成功

·failed：资源分配失败

Checked resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.

检查TRM资源：接口为*interface*，带宽为*bandwidth*，带宽类型为*class-type*，返回值为*result*

其中，*result*的取值包括：

·successful：资源分配成功

·bandwidth unavailable：带宽无效，资源分配失败

·no route：亲和属性检查不通过，资源分配失败

Freed resource to TRM.

释放TRM资源

Created a reverse CR-LSP, LSP ID *lsp-id*.

创建反向CR-LSP，LSP ID为*lsp-id*

Deleted the reverse CR-LSP, LSP ID *lsp-id*.

删除反向CR-LSP，LSP ID为*lsp-id*

Allocated incoming label *label* for reverse LSP.

为反向LSP分配入标签*label*

Allocated incoming label *label* for LSP.

为LSP分配入标签*label*

Deleted MP information. PHOP is *phop-addr*.

删除MP信息，PHOP是*phop-addr*

Failed to trigger CSPF.

触发CSPF失败

FRR bind.

FRR绑定

FRR unbind.

FRR取消绑定

FRR inuse.

已经进行FRR切换

Finished smoothing all egress CR-LSP configurations.

尾节点CR-LSP配置平滑结束

TC disconnected.

TC和RSVP的连接断开

TRM reconnected.

TRM和RSVP重新建立连接

Resource was preempted.

资源被抢占

Deleted the PSB.

删除PSB

Released the incoming label *label* for reverse LSP.

释放反向LSP的入标签*label*

Released the incoming label *label* for LSP.

释放LSP的入标签*label*

Sent a path message.

发送path消息

The path message length *length* is greater than interface MTU *mtu*.

Path消息的长度*length*大于接口的MTU值*mtu*

Started to smooth all PSBs.

PSB平滑开始

Smoothing the PSB.

PSB平滑

Finished smoothing all PSBs.

PSB平滑结束

Received interface *interface* change message.

收到接口*interface*状态变化消息

Processing interface change message.

处理接口状态变化消息

Interface change message processing completed.

接口状态变化消息结束

Received peer *peer-addr* lost message, interface *interface*.

收到邻居*peer-addr*丢失消息，邻居所在的接口为*interface*

Processing peer lost message.

处理邻居丢失

Peer lost message processing completed.

邻居丢失消息处理结束

GR started: Set the staled flag on the PSB.

GR开始，给PSB打上老化标记

GR disabled: Deleted the staled flag on the PSB.

GR去使能，清除PSB老化标记

GR ended: Deleted the staled PSB.

GR结束，删除带有老化标记的PSB

Received an error notification from LSM, LSP ID *lsp-id*.

收到LSM错误通知，LSP ID为*lsp-id*

Received a PathErr message: error code = *error-code*, error value = *error-value*, error description = *description*.

收到PathErr消息，错误码为error-code，错误值为error-value，错误描述信息为description

Received a PathErr message. Sent a path message.

收到PathErr消息，发送path消息

Received a PathErr message. Teared the CR-LSP.

收到PathErr消息，拆除CR-LSP

Forwarded the PathErr message.

转发PathErr消息

Sent a PathErr message: error code = *error-code*, error value = *error-value*, error description = *description*.

发送PathErr消息，错误码为*error-code*，错误值为*error-value*，错误描述信息为*description*

Received a PathTear message.

收到PathTear消息

Received a PathTear message. Deleted MP information for PHOP *phop-addr*.

收到PathTear消息，删除MP信息，PHOP为*phop-addr*

Received a PathTear message. Deleted the PSB.

收到PathTear消息，删除PSB

Forwarded the PathTear message.

转发PathTear消息

Sent a PathTear message.

发送PathTear消息

【举例】

\# 打开RSVP Path相关的调试信息开关，收到Path消息后打印如下调试信息。

\<Sysname\> debugging rsvp path

\*Aug 19 08:25:17:440 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a path message. Created a new PSB.

*// 接收到Path消息，创建新的PSB。消息的目的地址为10.33.33.33，源地址为10.11.11.11，隧道的Tunnel ID为1。*

\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Failed to trigger CSPF.

*// 触发CSPF计算失败。*

\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Checked resource from TRM: interface GE1/0/1, bandwidth 0kbps, CT 0, result  successful.

*// 检查TRM资源成功：接口为GigabitEthernet1/0/1，带宽为0kbps，带宽类型为CT 0。*

\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Allocated incoming label 1148 for LSP.

*// 为LSP分配入标签值1148。*

\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a path message.

*// 发送Path消息。*

\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a path message. Updated the old PSB.

*// 接收到Path消息，更新已有的PSB。*

\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Failed to trigger CSPF.

*// 触发CSPF计算失败。*

\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a path message.

*// 发送Path消息。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp reduction**

------------------------------------------------------------------------

【命令】

**[debugging rsvp reduction**]

**[undo debugging rsvp reduction**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp reduction**]命令用来打开RSVP摘要刷新和消息可靠传递调试信息开关。**undo debugging rsvp reduction**命令用来关闭RSVP摘要刷新和消息可靠传递调试信息开关。

缺省情况下，RSVP摘要刷新和消息可靠传递调试信息开关处于关闭状态。

表1-7 debugging rsvp reduction命令输出信息描述表

字段

描述

Created message ID *message-id* for retransmit message.

为重传报文分配message ID，值为*message-id*

Added message ID *message-id* to srefresh message.

为摘要刷新消息添加message ID（*message-id*）

Received a srefresh message.

收到摘要刷新消息

Received an ACK message.

收到ACK消息

Replied an ACK message.

回应ACK消息

Replied a NACK message.

回应NACK消息

Processing ACK message ID list from *peer-addr*.

处理来自*peer-addr*的ACK消息的message ID链

Reset PSB cleanup timer by message ID *message-id*.

根据message ID（*message-id*）重置PSB老化定时器

Reset RSB cleanup timer by message ID *message-id*.

根据message ID（*message-id*）重置RSB老化定时器

Invalid message ID *message-id*.

无效的message ID（*message-id*）

Processing NACK message ID list from *peer-addr*.

处理来自*peer-addr*的NACK消息的message ID链

Sent a path message for message ID *message-id*.

为message ID（*message-id*）发送path消息

Sent a resv message for message ID *message-id*.

为message ID（*message-id*）发送resv消息

Added message ID *message-id* to the retransmit buffer.

向重传缓冲区添加message ID（*message-id*）

Deleted message ID *message-id* from the retransmit buffer.

从重传缓冲区中删除message ID（*message-id*）

【举例】

\# 在接口视图下配置RSVP摘要刷新和消息可靠传递功能后，打开RSVP摘要刷新和消息可靠传递调试信息开关，打印如下调试信息。

\<Sysname\> debugging rsvp reduction

\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Created message ID 7 for retransmit message.

*// 为重传报文分配message ID，值为7。*

\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Added message ID 6 to srefresh message.

*// 为摘要刷新消息添加message ID（6）。*

\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Added message ID 7 to the retransmit buffer.

*// 向重传缓冲区添加message ID（6）。*

\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Received an ACK message.

*// 接收到ACK消息。*

\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Processing ACK message ID list from 12.11.110.11.

*// 处理来自12.11.110.11的ACK消息的message ID链。*

\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Deleted message ID 7 from the retransmit buffer.

*// 从重传缓冲区中删除message ID（7）。*

\*Aug 19 08:50:04:334 2012 Sysname RSVP/7/REDUC: -MDC=1; Replied an ACK message.

*// 应答ACK消息。*

\*Aug 19 08:50:14:134 2012 Sysname RSVP/7/REDUC: -MDC=1; Received a srefresh message.

*// 接收到Srefresh消息。*

\*Aug 19 08:50:14:134 2012 Sysname RSVP/7/REDUC: -MDC=1; Reset PSB cleanup timer by message ID 7.

*// 根据message ID（7）重置PSB老化定时器。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp resv**

------------------------------------------------------------------------

【命令】

**[debugging rsvp resv** [ **destination** *ip-address* **source** *ip-address* **tunnel-id** *tunnel-id* ]]

**[undo debugging rsvp resv**]

【视图】

用户视图

【参数】

**[destination** *ip-address*]：指定隧道的目的地址。

**[source** *ip-address*]：指定隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：指定隧道的ID。*tunnel-id*为隧道ID，取值范围为0～65535。

【描述】

**[debugging rsvp resv**]命令用来打开RSVP Resv调试信息开关。**undo debugging rsvp resv**命令用来关闭RSVP Resv调试信息开关。

缺省情况下，RSVP Resv调试信息开关处于关闭状态。

表1-8 debugging rsvp resv命令输出信息描述表

字段

描述

Received a resv message. Created a new RSB.

收到resv消息，新建RSB

Received a resv message. Updated the old RSB.

收到resv消息，更新RSB

Allocated resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.

从TRM分配资源：接口为*interface*，带宽为*bandwidth*，带宽类型为*class-type*，返回值为*result *

其中，result的取值包括：

·successful：资源分配成功

·failed：资源分配失败

Modified resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.

修改TRM资源：接口为*interface*，带宽为*bandwidth*，带宽类型为*class-type*，返回值为*result *

其中，result的取值包括：

·successful：资源修改成功

·failed：资源修改失败

Freed resource to TRM.

向TRM释放资源

Failed to get PSB.

获取PSB失败

Created a new TCSB.

新建TCSB

Updated the old TCSB.

更新旧的TCSB

Added filterspec to TCSB.

向TCSB添加filterspec

The TCSB is blockaded.

TCSB被阻塞

Merged flowdesc from TCSB. The merge flag is off.

根据TCSB合并流量描述，合并标记为off

Merged flowdesc from TCSB. The merge flag is on.

根据TCSB合并流量描述，合并标记为on

Merged flowspec with LUB.

用LUB算法合并流量描述

Merged flowspec with GLB.

用GLB算法合并流量描述

Updated TCSB: TC_B_Police_flag *flag1*, TC_E_Police_flag *flag2,* TC_M_Police_flag *flag3*.

更新TCSB，TC_B_Police_flag为*flag1*，TC_E_Police_flag为*flag2，*TC_M_Police_flag为*flag3*

Updated CR-LSP, LSP ID *lsp-id*, direction *direction*.

更新CR-LSP，LSP ID为*lsp-id*，方向为*direction*

Deleted CR-LSP, LSP ID *lsp-id*, direction *direction*.

删除CR-LSP，LSP ID为*lsp-id*，方向为*direction*

Created request info.

创建request信息

Updated request info.

更新request信息

Deleted filterspec in request info.

从request信息中删除filterspec

No filterspec in request info, deleted request info.

request信息中没有filterspec，删除request信息

Sent a resv message.

发送resv消息

Resource was preempted.

资源被抢占

GR started: Set the staled flag on the RSB.

GR开始：给RSB打上老化标记

GR recovered: Recovered the staled RSB.

GR恢复：恢复RSB

GR disabled: Deleted the staled flag on the RSB.

GR去使能：清除RSB中老化标记

GR ended: Deleted the staled RSB.

GR结束：删除带有老化标记的RSB

Received interface *interface* change message.

收到接口*interface*状态变化消息

Processing interface change message.

处理接口状态变化消息

Interface change message processing completed.

接口状态变化消息处理结束

Received peer *peer-addr* lost message, interface *interface*.

收到邻居*peer-addr*丢失消息，邻居所在的接口为*interface*

Processing peer lost message.

处理邻居丢失消息

Peer lost message processing completed.

处理邻居丢失消息结束

Started to smooth all RSBs.

RSB平滑开始

Smoothing the RSB.

RSB平滑

Finished smoothing all RSBs.

RSB平滑结束

TRM reconnected.

TRM和RSVP重新建立连接

Received a ResvErr message: error code = *error-code*, error value = *error-value*, error description = *description.*

收到ResvErr消息，错误码为error-code，错误值为*error-value*，错误描述信息为*description*

Forwarded the ResvErr message.

转发ResvErr消息

Created a new BSB.

新建BSB

Updated the old BSB.

更新旧的BSB

Sent a ResvErr message: error code = *error-code*, error value = *error-value*, error description = *description.*

发送ResvErr消息，错误码为error-code，错误值为*error-value*，错误描述信息为*description*

Received a ResvTear message.

收到ResvTear消息

Received a ResvTear message. Sent a PathTear message.

收到ResvTear消息，发送PathTear消息

Received a ResvTear message. Sent a resv message.

收到ResvTear消息，发送resv消息

Forwarded the ResvTear message.

转发ResvTear消息

Sent a ResvTear message.

发送ResvTear消息

Received a ResvConf message.

收到ResvConf消息

Sent a ResvConf message.

发送ResvConf消息

【举例】

\# 打开RSVP Resv调试信息开关，收到Resv消息后打印如下调试信息。

\<Sysname\> debugging rsvp resv

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a resv message. Created a new RSB.

*// 接收到Resv消息，创建新的RSB。消息的目的地址为10.33.33.33，源地址为10.11.11.11，隧道的Tunnel ID为1。*

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.1

1.11, tunnel ID 1: TCSB param: TC_B_Police_flag 0, TC_E_Police_flag 0, TC_M_Police_flag 0.

*[// TC_B_Police_flag*]*为0，TC_E_Police_flag为0，TC_M_Police_flag为0。*

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.1

1.11, tunnel ID 1: Created a new TCSB.

*// 新建TCSB。*

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Allocated resource from TRM: interface GE1/0/1, bandwidth 0kbps, CT 0, result successful.

*// 成功从TRM分配资源：接口为GigabitEthernet1/0/1，带宽为0kbps，带宽类型为CT0。*

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Updated CR-LSP, LSP ID 18212, direction 0.

*// 更新CR-LSP，LSP ID为18212，该隧道为单向隧道。*

\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Created request info.

*// 创建request信息。*

\*Aug 19 08:30:13:405 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Merged flowdesc from TCSB. The merge flag is off.

*// 根据TCSB合并流量描述，合并标记为off。*

\*Aug 19 08:30:13:405 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a resv message.

*// 发送Resv消息。*

\*Aug 19 08:30:23:967 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a resv message. Updated the old RSB.

*// 接收到Resv消息，更新已有的RSB。*

**RSVP \-- RSVP调试命令 \-- debugging rsvp timer**

------------------------------------------------------------------------

【命令】

**[debugging rsvp timer**]

**[undo debugging rsvp timer**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging rsvp timer**]命令用来打开定时器调试信息开关。**undo debugging rsvp timer**命令用来关闭定时器调试信息开关。

缺省情况下，RSVP定时器调试信息开关处于关闭状态。

表1-9 debugging rsvp timer命令输出信息描述表

字段

描述

Created cleanup timer for SA: from *start-address* to *end-address*.

创建认证老化定时器：起点地址*start-address*，终点地址*end-address*

Reset cleanup timer of SA: from *start-address* to *end-address*.

重置认证老化定时器：起点地址*start-address*，终点地址*end-address*

Cleanup timer of SA expired: from *start-address* to *end-address*.

认证老化定时器超时：起点地址*start-address*，终点地址*end-address*

Deleted cleanup timer of SA: from *start-address* to *end-address*.

删除认证老化定时器：起点地址*start-address*，终点地址*end-address*

Created challenge timer for SA: from *start-address* to *end-address*.

创建认证挑战定时器：起点地址*start-address*，终点地址*end-address*

Reset challenge timer for SA: from *start-address* to *end-address*.

重置认证挑战定时器：起点地址*start-address*，终点地址*end-address*

Challenge timer of SA expired: from *start-address* to *end-address*.

认证挑战定时器超时：起点地址*start-address*，终点地址*end-address*

Deleted challenge timer of SA: from *start-address* to *end-address*.

删除认证挑战定时器：起点地址*start-address*，终点地址*end-address*

FRR optimize timer expired.

FRR优化定时器超时

Created resend timer for HA message.

创建HA消息重发定时器

Resend timer of HA message expired.

HA消息重发定时器超时

Deleted the resend timer of HA message.

删除HA消息重发定时器

Created GR restart timer, peer *peer-addr,* interface *interface*.

创建GR重启定时器，邻居地址*peer-addr*，接口*interface*

GR restart timer expired, peer *peer-addr,* interface *interface*.

GR重启定时器超时，邻居地址*peer-addr*，接口*interface*

Created GR recovery timer, peer *peer-addr,* interface *interface*.

创建GR恢复定时器，邻居地址*peer-addr*，接口*interface*

GR recovery timer expired, peer *peer-addr,* interface *interface*.

GR恢复定时器超时，邻居地址*peer-addr*，接口*interface*

Created hello timer, peer *peer-addr,* interface *interface*.

创建hello定时器，邻居地址*peer-addr*，接口*interface*

Hello timer expired, peer *peer-addr,* interface *interface*.

Hello定时器超时，邻居地址*peer-addr*，接口*interface*

Reset hello timer.

重置hello定时器

Created local repair timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

创建PSB本地修复定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Local repair timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

PSB本地修复定时器超时，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Deleted local repair timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

删除PSB本地修复定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Created cleanup timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

创建PSB老化定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Reset cleanup timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

重置PSB老化定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Deleted cleanup timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

删除PSB老化定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Cleanup timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

PSB老化定时器超时，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Created path refresh timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

创建path刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Reset path refresh timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

重置path刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Deleted path refresh timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

删除path刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Path refresh timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

path刷新定时器超时，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Created srefresh timer, peer *peer-addr,* interface *interface*.

创建摘要刷新定时器，邻居地址*peer-addr*，接口*interface*

Deleted srefresh timer, peer *peer-addr,* interface *interface*.

删除摘要刷新定时器，邻居地址*peer-addr*，接口*interface*

Srefresh timer expired, peer *peer-addr,* interface *interface*.

摘要刷新定时器超时，邻居地址*peer-addr*，接口*interface*

Created retransmit timer for message ID *message-id*.

为message ID（*message-id*）创建重传定时器

Retransmit timer of message ID *message-id* expired.

message ID（*message-id*）的重传定时器超时

Reset the retransmit timer.

重置重传定时器

The message ID *message-id* has been retransmitted more than *max-num* times, so deleted the message ID.

message ID（*message-id*）重传次数超过*max-num*次，删除该message ID

Created cleanup timer for BSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

创建BSB老化定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Reset cleanup timer for BSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

重置BSB老化定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Cleanup timer of BSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

BSB老化定时器超时，目的地址*dst-addr*，源地址 *src-addr*，tunnel ID *tunnel-id*

Created cleanup timer for RSB: src *src-addr*, LSP ID *lsp-id.*

创建RSB老化定时器，源地址*dst-addr*，LSP ID为*lsp-id*

Reset cleanup timer of RSB: src *src-addr*, LSP ID *lsp-id.*

重置RSB老化定时器，源地址*dst-addr*，LSP ID为*lsp-id*

Deleted cleanup timer of RSB: src *src-addr*, LSP ID *lsp-id.*

删除RSB老化定时器，源地址*dst-addr*，LSP ID为*lsp-id*

Cleanup timer of RSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

RSB老化定时器超时，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Created resv refresh timer for RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*.

创建resv刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Reset resv refresh timer of RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

重置resv刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Deleted resv refresh timer of RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

删除resv刷新定时器，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

Resv refresh timer of RSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*

resv刷新定时器超时，目的地址*dst-addr*，源地址*src-addr*，tunnel ID为*tunnel-id*

****

【举例】

\# 打开RSVP定时器调试信息开关，第一次收到Path和Resv消息后打印如下调试信息。

\<Sysname\> debugging rsvp timer

\*Aug 19 08:40:42:119 2012 Sysname RSVP/7/TIMER: -MDC=1; Created path refresh timer for PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.

*// 为PSB创建路径刷新定时器，目的地址为10.33.33.33，源地址为10.11.11.11，tunnel ID为1。*

\*Aug 19 08:40:42:119 2012 Sysname RSVP/7/TIMER: -MDC=1; Created cleanup timer for PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.

*// 创建PSB老化定时器，目的地址为10.33.33.33，源地址为10.11.11.11，tunnel ID为1。*

\*Aug 19 08:40:42:120 2012 Sysname RSVP/7/TIMER: -MDC=1; Created cleanup timer for RSB: src 10.11.11.11, LSP ID 18213.

*// 创建RSB老化定时器，源地址为10.11.11.11，LSP ID为18213。*

\*Aug 19 08:40:42:120 2012 Sysname RSVP/7/TIMER: -MDC=1; Created resv refresh timer for RSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.

*// 为PSB创建Resv刷新定时器，目的地址为10.33.33.33，源地址为10.11.11.11，tunnel ID为1。*

\*Aug 19 08:40:52:378 2012 Sysname RSVP/7/TIMER: -MDC=1; Path refresh timer of PSB expired: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.

*[// PSB*]*的路径刷新定时器超时，目的地址为10.33.33.33，源地址为10.11.11.11，tunnel ID为1。*

\*Aug 19 08:40:52:734 2012 Sysname RSVP/7/TIMER: -MDC=1; Reset cleanup timer of PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.

*// 重置PSB老化定时器，目的地址为10.33.33.33，源地址为10.11.11.11，tunnel ID为1。*

\*Aug 19 08:40:52:767 2012 Sysname RSVP/7/TIMER: -MDC=1; Reset cleanup timer of RSB: src 10.11.11.11, LSP ID 18213.

*// 重置RSB老化定时器，源地址为10.11.11.11，LSP ID为18213。*

****
