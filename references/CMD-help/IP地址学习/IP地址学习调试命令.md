<!-- CMD-INDEX
  debugging wlan wsnp                 | 用户视图             | L5
-->

**IP地址学习 \-- IP地址学习调试命令 \-- debugging wlan wsnp**

------------------------------------------------------------------------

【命令】

**[debugging wlan wsnp**[ { **all** \| **error** \| **event** }]]

**[undo debugging wlan wsnp**[ { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示IP地址学习模块所有的调试信息开关。

**[error**]：表示IP地址学习模块错误的调试信息开关。

**[event**]：表示IP地址学习模块事件的调试信息开关。

【描述】

**[debugging wlan wsnp**]命令用来打开IP地址学习调试信息开关。**undo debugging wlan wsnp**命令用来关闭IP地址学习调试信息开关。

缺省情况下，IP地址学习调试信息开关处于关闭状态。

表1-1 debugging wlan wsnp error命令输出信息描述表

字段

描述

No WSNP data in client.

STA结构下没有WSNP数据

No client *ClientMAC* in BSS or no WSNP data in client *ClientMAC*.

BSS下没有客户端*ClientMAC*，或者客户端*ClientMAC*下没有WSNP数据

Captured an invalid *MessageType* packet: Its length (*PacketLength*) is not greater than *Length*.

拦截到非法的*MessageType*类型报文，由于报文长度*PacketLength*必须比*Length*长

*[MessageType *]取值如下：

·uplink ARP：上行ARP报文

·uplink DHCP：上行DHCP报文

·downlink DHCP：下行DHCP报文

·uplink IPv6：上行ipv6报文

·downlink IPv6：下行ipv6报文

·uplink ICMPv6：上行ICMPv6报文

·uplink UDPv6：上行UDPv6报文

·uplink DHCPv6：上行DHCPv6报文

·downlink DHCPv6：下行DHCPv6报文

·downlink unicast ICMPv6：下行单播ICMPv6报文

·downlink unicast UDPv6：下行单播UDPv6报文

·downlink broadcast ICMPv6：下行广播ICMPv6报文

Captured an invalid *MessageType* packet: Its length (*PacketLength*) is not smaller than *Length*.

拦截到无效的*MessageType*类型报文，由于报文长度*PacketLength*必须比*Length*短

*[MessageType *]取值如下：

·uplink ARP：上行ARP报文

·uplink DHCP：上行DHCP报文

·downlink DHCP：下行DHCP报文

·uplink IPv6：上行ipv6报文

·downlink IPv6：下行ipv6报文

·uplink ICMPv6：上行ICMPv6报文

·uplink UDPv6：上行UDPv6报文

·uplink DHCPv6：上行DHCPv6报文

·downlink DHCPv6：下行DHCPv6报文

·downlink unicast ICMPv6：下行单播ICMPv6报文

·downlink unicast UDPv6：下行单播UDPv6报文

·downlink broadcast ICMPv6：下行广播ICMPv6报文

Invalid *PktSocketType* DHCP packet: Message Type option not found.

*[PktSocketType* DHCP]报文未携带Message Type option

·Uplink：上行

·Downlink：下行

Discarded packet: Invalid IPv4 address *IPv4Addr*.

丢弃报文，由于报文IPv4地址*IPv4Addr*无效

Discarded packet: Requested IP Address option not found.

丢弃报文，由于报文未携带Requested IP Address option

Discarded packet: Invalid IPv4 address length *IPLength*.

丢弃报文，由于报文IPv4地址长度*IPLength*非法

Discarded packet: Invalid packet length *PacketLength*.

丢弃报文，由于报文长度*PacketLength*非法

Discarded ND-NA packet: It is not the response to the ND-NS packet.

丢弃报文，由于ND-NA报文不是ND-NS报文的回应报文

Discarded packet: Option type *OptionType* or option length *Optionlength* is invalid.

丢弃报文，由于option类型*OptionType*无效或者option长度*Optionlength*无效

Discarded packet: MAC address *MACAddress* in the option is not the MAC address of the client.

丢弃报文，由于option中的MAC 地址*MACAddress*与客户端地址不匹配

Discarded packet: IP address is loopback IPv6 address *IPv6Addr*.

丢弃报文，由于IP地址是环路IPv6地址*IPv6Addr*

Discarded packet: IP address is multicast IPv6 address *IPv6Addr*.

丢弃报文，由于IP地址是组播IPv6地址*IPv6Addr*

Discarded packet: IP address is unspecified IPv6 address *IPv6Addr*.

丢弃报文，由于IP地址是未指定的IPv6地址*IPv6Addr*

Discarded packet: IP address is link local IPv6 address *IPv6Addr*.

丢弃报文，由于IP地址是本地链路IPv6地址*IPv6Addr*

Discarded packet: Incomplete DHCPv6 *OptionType* option.

丢弃报文，由于DHCPv6 option *OptionType*不完整

Discarded packet: Invalid header length *Length* of DHCPv6 *OptionType* option.

丢弃报文，由于DHCPv6 *OptionType* option头长度*Length*无效

*[OptionType*]取值如下：

·NA：Non-temporary Address非暂时地址

·TA：Temporary Address暂时地址

Discarded packet: Invalid length *Length* of DHCPv6 *OptionType* option.

丢弃报文，由于DHCPv6 *OptionType* option长度*Length*无效

*[OptionType*]取值如下：

·NA：Non-temporary Address非暂时地址

·TA：Temporary Address暂时地址

·IA：Identify Association认证关联

Discarded packet: Length of *OptionType* option is 0.

丢弃报文，由于Option[*OptionType*]中option长度0非法

Discarded packet: Incomplete packet.

丢弃报文，由于报文不完整

Discarded packet: Invalid prefix length *Length*.

丢弃报文，由于前缀长度*Length*无效

Failed to add the source *Source* for IPv4 address *IPv4Addr*: Memory allocation failure.

添加IPv4地址*IPv4Addr*来源*Source*失败，由于分配内存失败

*[Source*]取值如下：

·DHCP：DHCP方式

·ARP：ARP方式

Failed to delete the source *Source* for IPv4 address *IPv4Addr*: Memory allocation failure.

删除IPv4地址*IPv4Addr*来源*Source*失败，由于分配内存失败

*[Source*]取值如下：

·DHCP：DHCP方式

·ARP：ARP方式

Failed to add the source *Source* for IPv6 address *IPv6Addr*: Memory allocation failure.

添加IPv6地址*IPv6Addr*来源*Source*失败，由于分配内存失败

*[Source*]取值如下：

·DHCPv6：DHCPv6方式

·ND：ND方式

Failed to delete the source *Source* for IPv6 address *IPv6Addr*: Memory allocation failure.

删除IPv6地址*IPv6Addr*来源*Source*失败，由于分配内存失败

*[Source*]取值如下：

·DHCPv6：DHCPv6方式

·ND：ND方式

Failed to add the source *Source* for IPv6 prefix *IPv6Addr* whose length is *length*: Memory allocation failure.

添加IPv6前缀*IPv6Addr*前缀长度*length*来源*Source*失败，由于分配内存失败

*[MethodType*]取值如下：

·ND：ND方式

Failed to send *MessageType *message to the uplink device.

发送*MessageType*消息到上行设备失败

*[MessageType *]取值如下：

·IPv4 entry：IPv4表项

·IPv6 entry：IPv6表项

·IPv6 prefix entry：IPv6前缀选项

Failed to send WSNP data for roaming clients to AP: Data length=*DataLen*.

发送漫游用户迁移WSNP数据(长度：*DataLen*)给AP失败

Failed to send *MessageType *to HA.

发送*MessageType*消息到HA失败

*[MessageType*]取值如下：

·IPv4 entry：IPv4表项

·IPv6 entry：IPv6表项

·IPv6 Prefix：IPv6前缀表项

Unsupported message type.

不支持消息类型

Invalid message type.

要解析的消息类型无效

Length of message from FA is invalid: Length= *MessageLength.*

来自FA的消息长度*MessageLength*无效

Failed to process IP entry from FA.

处理来自FA的IP表项失败

Failed to get WSNP data for intra-AC roaming clients.

获取AC内漫游用户迁移WSNP数据失败

Failed to get WSNP data for inter-AC roaming clients.

获取AC间漫游用户迁移WSNP数据失败

Failed to recover WSNP data for roaming clients: Didn\'t get TLV data through TLV handle.

恢复漫游用户迁移WSNP数据失败：通过TLV handle 获取TLV数据失败

Failed to decode roam IPv4 entry: Invalid message length *Length*.

解析漫游IPv4表项失败：消息长度*Length*无效

Failed to decode roam IPv6 entry: Invalid message length *Length*.

解析漫游IPv6表项失败：消息长度*Length*无效

Failed to decode roam IPv6 prefix entry: Invalid message length *Length*.

解析漫游IPv6前缀表项失败：消息长度*Length*无效

Failed to notify module *moduleID* of IP event *event*.

通知其它模块*moduleID*IP事件*event*失败

Failed to initiate WSNP data in fake client: Memory allocation failure.

初始化fake STA结构中的WSNP数据失败：分配内存失败

Failed to initiate WSNP data in client: Memory allocation failure.

初始化STA结构中的WSNP数据失败：分配内存失败

表1-2 debugging wlan wsnp event命令输出信息描述表

字段

描述

Captured *MessageType* packet.

拦截到*MessageType*报文

*[MessageType*]取值如下：

·uplink ARP-REQUEST：上行ARP-REQUEST报文

·uplink ARP-REPLY：上行ARP-REPLY报文

·uplink DHCP-DECLINE：上行DHCP-DECLINE报文

·uplink DHCP-RELEASE：上行DHCP-RELEASE报文

·downlink DHCP-ACK：下行DHCP-ACK报文

·uplink ND-NS：上行ND-NS报文

·uplink ND-NA：上行ND-NA报文

·uplink DHCP6-DECLINE：上行DHCP6-DECLINE报文

·uplink DHCP6-RELEASE：上行DHCP6-RELEASE报文

·downlink unicast ND-RA：下行单播ND-RA报文

·downlink DHCP6-REPLY：下行DHCP6-REPLY报文

Captured a downlink broadcast ND-RA packet in BSS *BSSID*.

BSS*BSSID* 拦截到下行广播ND-RA报文

Added the source *Source* for IPv4 address *IPv4Addr*.

添加IPv4地址*IPv4Addr*的来源*Source*成功

*[Source*]取值如下：

·ARP：ARP方式

·DHCP：DHCP方式

Updated IPv4 address *IPv4Addr* successfully. Changed source from ARP to DHCP.

更新IPv4地址*IPv4Addr*成功，学习方式由ARP改为DHCP

Failed to add IPv4 address *IPv4Addr*: The address already existed.

添加IPv4地址*IPv4Addr*失败，由于地址已存在

Deleted IPv4 address *IPv4Addr*.

删除IPv4地址*IPv4Addr*成功

Failed to delete IPv4 address *IPv4Addr*: The address didn\'t exist.

删除IPv4地址失败，由于地址不存在

Added the source *Source* for IPv6 address *IPv6Addr*.

添加IPv6地址*IPv6Addr*来源*Source*成功

*[Source*]取值如下：

·DHCPv6：DHCPv6方式

·ND：ND方式

Updated IPv6 address *IPv6Addr* successfully. Changed source from ND to DHCPv6.

更新IPv6地址*IPv6Addr*成功，来源由ND改为DHCPv6

Failed to add the source *Source* for IPv6 address *IPv6Addr*: The source already existed.

要添加的IPv6地址*IPv6Addr*来源*Source*已经存在

*[Source*]取值如下：

·DHCPv6：DHCPv6方式

·ND：ND方式

Deleted IPv6 address *IPv6Addr*.

删除IPv6地址*IPv6Addr*成功

Failed to delete IPv6 address *IPv6Addr*: The address didn\'t exist.

要删除的IPv6地址*IPv6Addr*不存在

Added the source *Source* for IPv6 prefix *IPv6Addr* whose length is *length*.

添加IPv6前缀*IPv6Addr*前缀长度*length*来源*Source*成功

Failed to add IPv6 prefix *IPv6Addr* whose length is *length*: The prefix already exists.

添加IPv6前缀*IPv6Addr*前缀长度*length*失败：已存在

Sent *MessageType *message to the uplink device.

发送*MessageType*消息到上行设备成功

*[MessageType *]取值如下：

·IPv4 entry：IPv4表项

·IPv6 entry：IPv6表项

·IPv6 prefix entry：IPv6前缀选项

Sent WSNP data for roaming clients to AP: Data length=*DataLen*.

发送漫游用户迁移WSNP数据(长度：*DataLen*)给AP成功

Sent *MessageType *message to HA.

发送*MessageType*消息到HA成功

*[MessageType*]取值如下：

·IPv4 entry：IPv4表项

·IPv6 entry：IPv6表项

·IPv6 Prefix：IPv6前缀表项

Received *MessageType* message: APID=*APID*, CMD=*CMD*, length=*Length*.

接收到*MessageType*消息，APID=*APID*, CMD=*CMD*, length=*Length*.

*[MessageType *]取值如下：

·an up entry：上行表项

·a down entry：下行表项

Received a fake entry from FA: Entry length=*Length*.

接收到来自FA的fake表项（表项长度= *Length*)

Processed IP entry from FA successfully.

处理来自FA的IP表项成功

Got WSNP data for intra-AC roaming clients.

获取AC内漫游用户迁移WSNP数据成功

Got WSNP data for inter-AC roaming clients.

获取AC间漫游用户迁移WSNP数据成功

Recovered WSNP data for roaming clients: Data length=*DataLen*.

恢复漫游用户迁移WANP数据成功，数据长度= *DataLen*

Initialized WSNP data in fake STA successfully.

初始化fake STA结构中的WSNP数据成功

Destroyed WSNP data in fake STA.

销毁fake STA结构中的WSNP数据成功

Deleted WSNP information in the client.

删除WSNP信息成功

Initialized WSNP information in the client successfully.

初始化WSNP信息成功

【举例】

\# MAC地址为0023-8933-216b 静态IP地址为10.1.3.22的客户端成功上线后，其所在BSS的BSSID为000f-e212-ff01，在AC和AP端打开wlan wsnp event开关，客户端成功上线后，AP上会有如下调试信息：

\<H3C\>debugging wlan wsnp event

\*Sep 10 12:15:25:120 2014 H3C STAMGR/7/Event: Captured an uplink ARP-REQUEST packet.

*[//*]*抓到上行ARP-REQUEST报文。*

\*Sep 10 12:15:28:120 2014 H3C STAMGR/7/Event: MAC: 0023-8933-216b, BSSID: 000f-

e212-ff01Added the IPv4 address10.1.3.22 methodARP.

*[//*]*添加IP地址10.1.3.22学习方式ARP成功。*

AC上会有如下调试信息

\*Sep 10 12:15:28:818 2014 H3C STAMGR/7/Event: Received an up entry, APID=2, CMD=

318767106, length=17.

*[//*]*接收到上行表项消息。*

\*Sep 10 12:15:28:819 2014 H3C STAMGR/7/Event: MAC: 0023-8933-216b, BSSID: 000f-

e212-ff01Added the IPv4 address10.1.3.22 methodARP.

*[//*]*添加IP地址10.1.3.22学习方式ARP成功。*

\# MAC地址为0023-8933-216b 静态IP地址为10.1.3.22的客户端成功上线后，其所在BSS的BSSID为000f-e212-ff01，在AC和AP端打开wlan wsnp error开关，STA成功上线后，AP上会有如下调试信息：

\<H3C\> debugging wlan wsnp error

\*Sep 10 12:15:25:121 2014 H3C STAMGR/7/Error: [MAC: 0023-8933-216b, BSSID: 000f-

e212-ff01Discard packet]：Invalid IPv4 address[0.0.0.0.]

*[//*]*丢弃报文：无效的IPv4地址0.0.0.0*
