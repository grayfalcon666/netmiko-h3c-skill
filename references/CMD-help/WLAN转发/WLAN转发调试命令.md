<!-- CMD-INDEX
  debugging wlan forward              | 用户视图             | L5
-->

**WLAN转发 \-- WLAN转发调试命令 \-- debugging wlan forward**

------------------------------------------------------------------------

【命令】

**[debugging wlan forward**[ { **all** \| **error** \| **packet** }]]

**[undo debugging wlan forward**[ { **all** \| **error** \| **packet** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示WLAN转发的所有调试信息开关。

**[error**]：表示WLAN转发的错误调试信息开关。

**[packet**]：表示WLAN转发的报文调试信息开关。

【描述】

**[debugging wlan forward**]命令用来打开WLAN转发调试信息开关。**undo debugging wlan forward**命令用来关闭WLAN转发调试信息开关。

缺省情况下，WLAN转发的调试信息开关处于关闭状态。

表1-1 debugging wlan forward packet命令输出信息描述表

字段

描述

Received a frame from a radio.

从radio收到了帧

Forwarded the frame received from the radio locally.

从Radio口收到帧进行本地转发

Received a frame from the AC.

接收来自AC的帧

Received a frame from the AP.

接收来自AP的帧

Sent a deauthentication frame.

STA不存在，发送deauth帧

Sent a frame to the BSS.

BSS_SND：发送帧到bss

Sent a frame for IP or IPv6 forwarding.

发送帧到ip或ipv6进行转发

Sent a frame to a radio for transmission.

发送帧到radio进行发送

Received a frame from the WLAN management module to a radio..

接收来自WLAN 管理发往radio的帧

Received a frame from the WLAN management module to a BSS.

接收来自WLAN 管理发往BSS的帧

Sent a frame to another card.

发送一个帧到别的板

The radio-based service dropped a frame. Phase for the service is *phase*. Service ID is *sid*. Position for the service in the MAP is *bitmap*. Result is *result*.

进行基于Radio口的业务处理并释放帧

*[phase*]表示业务的阶段，*sid*表示业务的ID，*bitmap*表示业务在MAP中的位置，*result*表示业务处理结果

*[result*]取值如下：

·1：报文已经被业务丢弃

·2：报文已经被业务消费处理

·3：报文已经被业务放入队列

The BSS-based service dropped a frame. Phase for the service is *phase*. Service ID is *sid*. Position for the service in the MAP is *bitmap*. Result is *result*.

进行基于BSS的业务处理并释放帧

*[phase*]表示业务的阶段，*sid*表示业务的*ID*，*bitmap*表示业务在MAP中的位置，*result*表示业务处理结果。

*[result*]取值如下：

·1：报文已经被业务丢弃

·2：报文已经被业务消费处理

·3：报文已经被业务放入队列

Received a CAPWAP fragment. Fragments received are not complete.

收到一个CAPWAP分片报文，且分片报文没有收全

Received a CAPWAP control packet.

收到CAPWAP控制报文

BSS sent a packet it intercepted to the Packet Socket.

报文被BSS侦听上送到Packet Socket

Radio sent a packet it intercepted to the Packet Socket.

报文被Radio侦听上送到Packet Socket

表1-2 debugging wlan forward error命令输出信息描述表

字段

描述

Failed to get BSS *bssid* info from the CAPWAP frame.

Capwap帧处理过程中，根据*bssid*获取BSS信息失败

Failed to parse the DOT11 frame from the WLAN management module to a radio.

解析来自WLAN管理发往radio的dot11帧失败

Failed to parse the DOT11 frame from the WLAN management module to a BSS.

解析来自WLAN管理发往BSS的dot11帧失败

Failed to parse the frame from a tunnel.

解析来自tunnel的帧失败

Failed to send the data frame for Layer 2 forwarding.

发送数据帧给mac做二层转发失败

Failed to convert the format of the unicast frame.

单播数据帧格式转换失败

Failed to get BSS *bssid* info from the data frame.

数据帧处理过程中，获取BSS信息失败

Failed to get BSS *bssid* info from the management frame.

管理帧处理过程中，获取BSS信息失败

Failed to get radio info.

获取radio信息失败

Failed to get BSS *bssid* info.

获取*bssid*的BSS信息失败

Failed to send the data frame for IP or IPv6 forwarding.

发送数据帧做ip或ipv6转发失败

Dropped a management frame with a broadcast, multicast, or all-zero source MAC address.

收到DOT11管理帧，丢弃，因为源MAC是组播、广播或全零

Dropped a data frame with a wrong protocol version.

收到DOT11数据帧，丢弃，因为版本号错误

Dropped a data frame with an unsupported subtype *subtype*.

收到DOT11数据帧，丢弃，因为子类型不被支持

*[subtype*]目前我们只支持：

DOT11_FRAME_SUBTYPE_DATA：子类型为Data的数据帧

DOT11_FRAME_SUBTYPE_QOS_DATA：子类型为QOS的数据帧

Dropped a management frame with an unsupported subtype.

收到DOT11管理帧，丢弃，因为子类型不被支持

Dropped a data frame with a broadcast, multicast, or all-zero source MAC address.

收到DOT11数据帧，丢弃，因为源MAC是广播、组播或全零

Dropped a frame with the same source MAC address and BSSID.

收到DOT11帧，丢弃，因为源MAC和BSSID相同

Dropped a frame with different destination MAC address and BSSID.

收到DOT11管理帧，丢弃，因为目的MAC和BSSID不相同

The client doesn\'t belong to BSS *bssid* for the data frame.

STA用户不属于此数据帧的*bssid*对应的BSS

The client doesn\'t belong to BSS *bssid* for the management frame.

STA用户不属于此管理帧的*bssid*对应的BSS

The radio is not up.

Radio状态没有up

Failed to get the tunnel info..

Tunnel不存在

Failed to get the client info.

STA不存在

Failed to get the forwarding info from the BSS.

BSS中转发信息不存在

Invalid forwarding type.

获取到的转发类型非法

Invalid frame type.

非法的帧类型

The frame is too short.

帧长度过小

Failed to get radio info by the radio ID and the WLAN ID.

无法通过RID和WLAN ID获取Radio信息

WLAN forwarding dropped a frame because the BSS failed to process the frame.

BSS侦听处理失败，WLANFW丢弃了帧

BSS accepted a frame it intercepted.

BSS侦听接管了帧

The frame sent for Layer 2 forwarding is not a data frame.

发往MAC转发的DOT11帧不是一个数据帧

The radio ID in the data frame is different from the radio ID in the BSS.

数据帧的radio ID和BSS中radio成员的ID不一致

The radio ID in the management frame is different from the radio ID in the BSS.

管理帧的radio ID和BSS中radio成员的ID不一致

Invalid frame with multiple CAPWAP headers.

进行了多次CAPWAP头封装的非法帧

The CAPWAP frame is too short.

Capwap帧长度过短

The frame type doesn\'t match the forwarding policy.

帧类型和转发策略不匹配

Dropped a management frame with an unsupported subtype.

收到DOT11管理帧，丢弃，因为子类型不被支持

There is no client in BSS *bssid*.

*[bssid*]对应的BSS中没有用户

QoS frame discarded because it was sent by a non-QoS client.

收到非QoS类型的STA发送的QoS帧，丢弃该QoS帧

Radio received a mesh frame.

Radio收到一个mesh类型的帧

Received a frame with invalid format from the BSS.

从BSS中获取的帧格式非法

The frame is too large to be fragmented.

帧太大无法被分片

Received a duplicate fragment.

收到重复的分片报文

Number of received fragments reached the limit. There are more fragments to be sent.

接收的分片报文数已达到允许最大值，但是还有更多的分片

Fragments out of sequence.

分片报文的顺序不正确

Number of reassembly queues reached the limit. Can\'t add another reassembly queue.

重组队列达到了临界值，不能再增加重组队列了

Received an invalid CAPWAP fragment.

收到非法的CAPWAP分片报文

Dropped a CAPWAP frame with an invalid radio MAC address.

收到CAPWAP报文丢弃，因为Radio mac字段不合法

Dropped a CAPWAP frame with an invalid W field.

收到CAPWAP报文丢弃，因为W字段不合法

Dropped a CAPWAP frame with no wireless specific information.

丢弃CAPWAP帧，由于CAPWAP头中未携带无线信息选项

Dropped a CAPWAP frame with wrong header length.

收到Capwap报文丢弃，因为报文的头长度字段与实际的头长度不相等

Failed to create a fragment node.

创建分片节点失败

Failed to create a fragment management node.

创建分片管理节点失败

Failed to convert the format of the frame.

帧格式转换失败

Failed to encrypt the data frame.

数据帧加密失败

Failed to add the TKIP MIC into the frame.

向帧中添加TKIP MIC失败

Failed to decrypt the data frame.

数据帧解密失败

Invalid TKIP MIC.

TKIP MIC非法

Invalid W field in the CAPWAP frame.

CAPWAP帧中的W字段非法

Failed to get forwarding info from the tunnel.

从隧道中获取转发信息失败

Dropped the frame because of too many encapsulations.

帧封装次数过多，丢弃报文

Failed to decrypt the management frame.

管理帧解密失败

Failed to encrypt the management frame.

管理帧加密失败

【举例】

\# 在AC，AP上打开WLAN转发的所有调试开关，STA发送一个报文给 PC，将输出如下调试信息。

\*May  4 10:19:37:470 2015 H3C WLANFW/7/PACKET:

interface = WLAN-Radio1/0/1 payload =

08 01 2C 00 00 0F E2 00 12 81 9C D3 6D 9D EA 85

08 2E 5F 2B 22 FE 70 09 AA AA 03 00 00 00 08 00

45 00 00 3C C4 6F 00 00 80 01 F2 75 C0 A8 01 07

C0 A8 01 84 08 00 48 5C 04 00 01 00 61 62 63 64

65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74

75 76 77 61 62 63 64 65 66 67 68 69

prompt: Received a frame from a radio.

*[// AP*]*收到一个报文，接收接口为WLAN-Radio1/0/1*

\*May  4 10:19:37:470 2015 H3C WLANFW/7/PACKET:

payload =

45 00 00 88 71 B6 00 00 FF 11 00 00 C0 A8 01 0E

C0 A8 01 0D 6D 40 14 7F 00 74 00 00 00 20 43 20

00 00 00 00 04 00 00 00 00 00 00 00 08 01 2C 00

00 0F E2 00 12 81 9C D3 6D 9D EA 85 08 2E 5F 2B

22 FE 70 09 AA AA 03 00 00 00 08 00 45 00 00 3C

C4 6F 00 00 80 01 F2 75 C0 A8 01 07 C0 A8 01 84

08 00 48 5C 04 00 01 00 61 62 63 64 65 66 67 68

69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 61

prompt: Sent a frame for IP or IPv6 forwarding.

*[// AP*]*把报文通过IP或IPv6转发发送出去*

\*May 20 10:45:08:919 2014 H3C WLANFW/7/PACKET:

interface = Vlan-interface1 payload =

45 00 00 88 71 B8 00 00 FF 11 C6 40 C0 A8 01 0E

C0 A8 01 0D 6D 40 14 7F 00 74 00 00 00 20 43 20

00 00 00 00 04 00 00 00 00 00 00 00 08 01 2C 00

00 0F E2 00 12 81 9C D3 6D 9D EA 85 08 2E 5F 2B

22 FE 90 09 AA AA 03 00 00 00 08 00 45 00 00 3C

C4 A0 00 00 80 01 F2 44 C0 A8 01 07 C0 A8 01 84

08 00 46 5C 04 00 03 00 61 62 63 64 65 66 67 68

69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 61

prompt: Received a frame from AP.

*[// AC*]*收到一个来自AP的报文，接收接口为Vlan-interface1*
