<!-- CMD-INDEX
  debugging mac-forced-forwarding     | 用户视图             | L5
-->

**MFF \-- MFF调试命令 \-- debugging mac-forced-forwarding**

------------------------------------------------------------------------

【命令】

**[debugging mac-forced-forwarding**]

**[undo debugging mac-forced-forwarding**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging mac-forced-forwarding**]命令用来开启MFF调试信息开关。**undo debugging mac-forced-forwarding**命令用来关闭MFF调试信息开关。

缺省情况下，MFF调试开关处于关闭状态

表1-1 debugging mac-forced-forwarding命令显示信息描述表

字段

描述

SendType:*send-type*    VLAN ID :*vlan-id*

SrcMAC:*src-MAC-address*    SrcIP : *src-ip-address*

DstMAC:*dst-MAC-address*    DstIP: *dst-ip-address*

PacketType : *packet-type*

MFF发送报文的发送类型、接口所属VLAN ID、源IP、源MAC、目的IP、目的MAC以及报文类型

动作类型：

·MFF_SENDTYPE_VLAN：VLAN内广播

·MFF_SENDTYPE_VLAN_EX_SRCPORT：VLAN内排除源端口广播

·MFF_SENDTYPE_USER：遍历用户端口广播

·MFF_SENDTYPE_NETWORK：遍历网络端口广播

·MFF_SENDTYPE_NETWORK_EX_SRC：向下行网络端口广播

·MFF_SENDTYPE_UNICAST：单播

·MFF_RECPKT：收到报文开始处理

·报文类型：

·REPLY：应答ARP报文

·REQUEST：请求ARP报文

·GRATUITOUS：免费ARP报文

【举例】

\# 在设备上开启MFF调试信息开关。

\<Sysname\> debugging mac-forced-forwarding

\*Aug  7 11:55:26:906 2011 Sysname ARP/7/MFF: -MDC=1

SendType   :MFF_SENDTYPE_VLAN_EX_SRCPORT       VLAN ID :100

 SrcMAC     :000d-5619-f7bc                     SrcIP   :100.1.1.1

 DstMAC     :0000-0000-0000                     DstIP   :100.1.1.100

 PacketType :REQUEST

