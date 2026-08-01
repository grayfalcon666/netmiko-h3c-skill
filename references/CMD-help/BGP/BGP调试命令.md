<!-- CMD-INDEX
  debugging bgp                       | 用户视图             | L19
  debugging bgp acl                   | 用户视图             | L373
  debugging bgp all                   | 用户视图             | L447
  debugging bgp calc                  | 用户视图             | L705
  debugging bgp event                 | 用户视图             | L819
  debugging bgp graceful-restart      | 用户视图             | L941
  debugging bgp ha                    | 用户视图             | L1149
  debugging bgp ipc                   | 用户视图             | L1403
  debugging bgp non-stop-routing      | 用户视图             | L1585
  debugging bgp prefix-list           | 用户视图             | L1823
  debugging bgp rely                  | 用户视图             | L1887
  debugging bgp timer                 | 用户视图             | L1963
  debugging bgp update                | 用户视图             | L2043
  debugging bgp update-group          | 用户视图             | L2233
  debugging bgp urt                   | 用户视图             | L2375
-->

**BGP \-- BGP调试命令 \-- debugging bgp**

------------------------------------------------------------------------

【命令】

**[debugging bgp**[ { **keepalive** \| **open** \| **packet** \| **raw-packet** \| **route-refresh** } [ *ipv4-address* [ *mask-length* ] *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  }   **receive** \| **send** ]]]

**[undo debugging bgp**[ { **keepalive** \| **open** \| **packet** \| **raw-packet** \| **route-refresh** }  [ *ipv4-address* [ *mask-length* ] *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  }   **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[keepalive**]：BGP Keepalive报文的调试信息开关。

**[open**]：BGP Open报文的调试信息开关。

**[packet**]：所有BGP报文的调试信息开关，包括Open报文，Keepalive报文，Update报文和Route-Refresh报文。

**[raw-packet**]：BGP报文具体信息调试开关。

**[route-refresh**]：BGP Route-Refresh报文调试信息开关。

*[ipv4-address*]：对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP报文调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP报文调试信息开关。

**[receive**]：接收的BGP报文。

**[send**]：发送的BGP报文。

【描述】

**[debugging bgp**]命令用来打开BGP指定类型报文的调试信息开关。**undo debugging bgp**用来关闭BGP指定类型报文的调试信息开关。

缺省情况下，该调试信息开关处于关闭状态。

表1-1 debugging bgp keepalive命令输出信息描述表

字段

描述

BGP.*vpn-instance*

VPN实例*vpn-instance*的BGP报文

如果不携带*vpn-instance*参数，则表示公网的BGP报文

*[X.X.X.X*]

BGP邻居的IPv4地址

*[X:X::X:X*]

BGP邻居的IPv6地址

Recv

收到报文

Send

发送报文

Length: *LengthNumber*

报文长度

表1-2 debugging bgp open命令输出信息描述表

字段

描述

BGP.*vpn-instance*

VPN实例*vpn-instance*的BGP报文

如果不携带*vpn-instance*参数，则表示公网的BGP报文

*[X.X.X.X*]

BGP邻居的IPv4地址

*[X:X::X:X*]

BGP邻居的IPv6地址

Recv

收到报文

Send

发送报文

Version

BGP协议版本号

Local AS

本地自治域号

HoldTime

HoldTime值，单位：秒

Router ID

路由器ID号

BGP ID

BGP ID号

OPT Type:   2 (Capability)

能力协商内容

CAP Type:   1 (Multiprotocol)  CAP Len: 4

具有多协议能力

IPv4-UNC (1/1)

CAP Type:   2 (RouteRefresh)   CAP Len: 0

具有IPv4单播路由更新能力

IPv4-MLC (1/2)

CAP Type:   2 (RouteRefresh)   CAP Len: 0

具有IPv4组播路由更新能力

CAP Type:   65 (AS4)   CAP Len: 4 AS4：100

支持4字节AS号

Total CAPB Len

能力协商总长度值

Total OPT Len

可选参数总长度值

Total Message Len

整个报文长度

表1-3 debugging bgp route-refresh命令输出信息描述表

字段

描述

BGP.*vpn-instance*

VPN实例*vpn-instance*的BGP报文

如果不携带*vpn-instance*参数，则表示公网的BGP报文

*[X.X.X.X*]

BGP邻居的IPv4地址

*[X:X::X:X*]

BGP邻居的IPv6地址

Recv

收到报文

Send

发送报文

Length

报文长度

AFI: 1; SAFI: 1

地址族：1；子地址族：1

AFI/ SAFI

地址族/子地址族

WTR

发送刷新信息的延时（When to Refresh）

peer x.x.x.x

对端邻居地址的IPv4地址

peer x:x::x:x

对端邻居地址的IPv6地址

Update报文调试信息详见后面小节介绍。

【举例】

\# 在本地设备上打开BGP报文的调试信息开关，收发BGP报文时打印调试信息。

\<Sysname\> debugging bgp packet

\<Sysname\> system-view

Sysname bgp 100

Sysname-bgp peer 192.168.109.29 as-number 100

Sysname-bgp address-family ipv4 unicast

Sysname-bgp-ipv4 peer 192.168.109.29 enable

\*Apr 16 17:13:01:742 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Send OPEN, Version: 4

         Local AS: 100, HoldTime: 180, Router ID: 192.168.109.88

         OPT Type:   2 (Capability)

         CAP Type:   1 (Multiprotocol)   CAP Len: 4

                                         IPv4-UNC (1/1)

         CAP Type:   2 (RouteRefresh)    CAP Len: 0

         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100

         Total CAPB Len    : 14

         Total OPT Len     : 16

         Total Message Len : 45

*// 向192.168.109.29发送BGP open报文，协商BGP会话参数。*

\*Apr 16 17:13:01:761 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Recv OPEN Length: 37

         Version: 4, Local AS: 100, HoldTime : 180,

         BGP ID: 192.168.109.29, TotOptLen: 10

         OPT Type:   2 (Capability)     OPT Len: 8

CAP Type:   1 (Multiprotocol)  CAP Len: 4

IPv4-UNC (1/1)

         CAP Type:   2 (RouteRefresh)   CAP Len: 0

*// 从192.168.109.29接收到BGP open报文，建立BGP会话。*

\*Apr 16 17:13:01:771 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Send KEEPALIVE

         Length: 19

*// 向192.168.109.29发送BGP keepalive报文，报文长度为19字节。*

\*Apr 16 17:13:01:802 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Recv KEEPALIVE

         Length: 19

*// 从192.168.109.29接收到BGP keepalive报文，报文长度为19字节。*

Sysname-bgp-ipv4 import-route static

\*Apr 16 17:54:09:96 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Send UPDATE to peer 192.168.109.29 for following destinations:

         Origin       : Incomplete

         AS path      :

         Next hop     : 192.168.109.88

         Local pref   : 100

         111.1.1.1/32,

*// 引入静态路由后，向192.168.109.29发送BGP update报文，发布引入的静态路由信息。*

\*Apr 16 17:56:41:933 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Recv UPDATE from peer 192.168.109.29 with following destinations:

         Origin       : Incomplete

         AS path      :

         Next hop     : 192.168.109.29

         Local pref   : 100

         MED          : 0

         111.1.1.1/32,

*// 从192.168.109.29接收到BGP update报文。*

\# 在两台设备A、B之间建立BGP会话。A上打开接收BGP Route-Refresh报文的调试信息开关，B上打开发送BGP Route-Refresh报文的调试信息开关。在B上执行**refresh bgp ipv4 all import**命令后，A和B上将打印如下调试信息。

\<Sysname\> debugging bgp route-refresh send

\<Sysname\> refresh bgp ipv4 all import

\*Apr 16 18:01:11:53 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Send ROUTEREFRESH MSG to peer 9.9.9.9(IPv4-UNC).

*// 设备B发送Route-Refresh报文*，*长度为**23字节*，*地址族是**1*，*子地址族是**1。*

\<Sysname\> debugging bgp route-refresh receive

\*Apr 16 18:01:11:53 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.1 Recv ROUTEREFRESH MSG:

 Length: 23, AFI: 1, SAFI: 1, WTR: 4.

*// 设备A收到Route-Refresh报文*，*长度为**23字节*，*地址族是**1*，*子地址族是**1*，*发送刷新信息的延时时间是4。*

**BGP \-- BGP调试命令 \-- debugging bgp acl**

------------------------------------------------------------------------

【命令】

**[debugging bgp acl*** acl-number*]

**[undo debugging bgp acl**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[acl-number*]：用于匹配路由信息目的网络地址的访问列表号，取值范围为2000～3999。

【使用指导】

**[debugging bgp acl**]命令用来打开通过ACL过滤的BGP路由的调试信息开关。**undo debugging bgp acl**命令用来关闭通过ACL过滤的BGP路由的调试信息开关。

缺省情况下，BGP路由的调试信息开关处于关闭状态。

需要注意的是：

·如果同时配置了本命令和**debugging bgp prefix-list**命令，则只有BGP路由同时通过ACL和IP地址前缀列表过滤，才会打开该路由的调试信息开关。

·通过基本ACL（2000～2999）对BGP路由进行过滤时，如果配置了**rule** [ *rule-id*  { **deny** \| **permit** } **source** *source-address* *source-wildcard*]命令，则只要路由的目的网络地址与**rule**命令中的*source-address source-wildcard*匹配，则该路由与**rule**命令配置的规则匹配，不会再比较路由的目的网络地址掩码。

·通过高级ACL（3000～3999）对BGP路由进行过滤时，**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]命令配置的规则用来过滤指定目的网络地址的路由；**rule** [ *rule-id*  { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]命令配置的规则用来过滤指定目的网络地址和掩码的路由，其中**source ***sour-addr sour-wildcard*用来过滤路由目的网络地址，**destination ***dest-addr dest-wildcard*用来过滤路由掩码。**destination ***dest-addr dest-wildcard*指定的掩码应该是连续的。如果指定的掩码不连续，则该过滤掩码的条件不生效。

【举例】

\# 通过配置ACL过滤条件，打开BGP路由11.1.1.1/32的路由更新调试信息开关。设备接收到对端发布的11.1.1.1/32和11.1.1.2/32两条路由后，打印如下调试信息。

\<Sysname\> system-view

Sysname acl basic 2000

Sysname-acl-ipv4-basic-2000 rule permit source 11.1.1.1 0

Sysname-acl-ipv4-basic-2000 quit

Sysname quit

\<Sysname\> debugging bgp update

\<Sysname\> debugging bgp acl 2000

\*Dec 20 16:02:33:923 2011 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Recv UPDATE from peer 13.1.1.1 with following destinations:

         Update message length : 60

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 13.1.1.1

         MED          : 0

         11.1.1.1/32,

*// 对端发布两条路由11.1.1.1/32和11.1.1.2/32，只有11.1.1.1/32通过ACL过滤，因此，只打印11.1.1.1/32 的调试信息。*

**BGP \-- BGP调试命令 \-- debugging bgp all**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **all** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

**[undo debugging bgp** **all** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：表示与指定对等体之间的BGP所有调试信息开关。*ipv4-address*为对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：表示与指定对等体之间的BGP所有调试信息开关。*ipv6-address*为对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP所有调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP的所有调试信息开关。

【描述】

**debugging bgp all**命令打开BGP所有调试信息开关。**undo debugging bgp all**命令用来关闭BGP所有调试信息开关。

缺省情况下，BGP所有调试开关处于关闭状态。

需要注意的是：

·该命令会打开所有和BGP相关的调试信息开关，信息量会比较大，可能影响系统应用，请慎重使用。

·调试完毕后，请及时关闭调试信息开关。

【举例】

\# 在设备A上打开BGP所有调试信息开关。当设备A（IP地址为192.168.109.88）和设备B（IP地址为192.168.109.29）建立IBGP会话时，设备A上打印如下调试信息。

\<DeviceA\> debugging bgp all

\*Apr 16 16:19:10:54 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 CR Timer Expired.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in IDLE state.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive ManualStart event in IDLE state.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from IDLE to CONNECT.

*// 激活BGP对等体后，等待CONNECT定时器超时*，*主动发起连接。*

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 CR Timer Expired.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in CONNECT state.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from CONNECT to CONNECT.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 CR Timer Expired.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive FsmConnectRetryTimer_Expires event in CONNECT state.

\*Apr 16 16:19:10:55 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from CONNECT to CONNECT.

\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive Tcp_CR_Acked event in CONNECT state.

\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Connected to 192.168.109.29.

\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 CR Timer Deleted.

\*Apr 16 16:19:10:74 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 HD Timer Created.

\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Send OPEN, Version: 4

         Local AS: 100, HoldTime: 180, Router ID: 192.168.109.88

         OPT Type:   2 (Capability)

         CAP Type:   1 (Multiprotocol)   CAP Len: 4

                                         IPv4-UNC (1/1)

         CAP Type:   2 (RouteRefresh)    CAP Len: 0

         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100

         Total CAPB Len    : 14

         Total OPT Len     : 16

         Total Message Len : 45

\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP: Sent to 192.168.109.29 (AS Number: 100)

         (Displaying bytes from 1 to 45)

         Message Type: Open, Total number of bytes: 45

         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

00 2D 01 04 00 64 00 B4 C0 A8 6D 58 10 02 0E 01

         04 00 01 00 01 02 00 41 04 00 00 00 64

\*Apr 16 16:19:10:75 2010 Sysname BGP/7/DEBUG: -MDC=1;

BGP.: 192.168.109.29 State is changed from CONNECT to OPENSENT.

\*Apr 16 16:19:10:76 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION be sent SIGNAL: SIG_MAIN  .

*[// TCP*]*连接成功*，*主动发送**OPEN报文。*

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP: Received from 192.168.109.29 (AS Number: 100)

         (Displaying bytes from 1 to 45)

         Message Type: Open, Total number of bytes: 45

         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

00 2D 01 04 00 64 00 B4 83 01 01 01 10 02 0E 01

         04 00 01 00 01 02 00 41 04 00 00 00 64

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

BGP.: 192.168.109.29 Recv OPEN Length: 45

         Version: 4, Local AS: 100, HoldTime : 180,

         BGP ID: 131.1.1.1, TotOptLen: 16

         OPT Type:   2 (Capability)      OPT Len: 14

                                         IPv4-UNC (1/1)

         CAP Type:   1 (Multiprotocol)   CAP Len: 4

         CAP Type:   2 (RouteRefresh)    CAP Len: 0

         CAP Type:  65 (AS4)             CAP Len: 4 AS4: 100

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive ReceiveOpenMessage event in OPENSENT state.

*// 收到对端发送的OPEN报文。*

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 KA Timer Created.

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Send KEEPALIVE

         Length: 19

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP: Sent to 192.168.109.29 (AS Number: 100)

         (Displaying bytes from 1 to 19)

         Message Type: KeepAlive, Total number of bytes: 19

         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

         00 13 04

\*Apr 16 16:19:10:91 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from OPENSENT to OPENCONFIRM.

\*Apr 16 16:19:10:92 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION be sent SIGNAL: SIG_MAIN  .

\*Apr 16 16:19:10:99 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION be sent SIGNAL: SIG_MAIN  .

\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP: Received from 192.168.109.29 (AS Number: 100)

         (Displaying bytes from 1 to 19)

         Message Type: KeepAlive, Total number of bytes: 19

         FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

         00 13 04

\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: 192.168.109.29 Recv KEEPALIVE

         Length: 19

\*Apr 16 16:19:10:105 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive ReceiveKeepAliveMsg event in OPENCONFIRM state.

\*Apr 16 16:19:10:106 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from OPENCONFIRM to ESTABLISHED.

*[// BGP*]*会话建立成功。*

![说明](BGP%20Debug.files/image001.png)

以上是执行**debugging bgp all**命令后在设备A上得到的BGP会话建立过程的全部调试信息，当设备无法建立BGP会话时，可以初步对比此流程，观察是否缺少某个步骤的报文，进而定位问题。后续命令将逐一介绍这些调试信息，此处不再重复。

**BGP \-- BGP调试命令 \-- debugging bgp calc**

------------------------------------------------------------------------

【命令】

**[debugging bgp**[ **calc** [ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6**  **multicast**  \| **l2vpn** \| **vpn-instance** *vpn-instance-name* { **ipv4** \| **ipv6** \| **vpnv4** } \| **vpnv4** \| **vpnv6** ]]]

**[undo debugging bgp calc **[[ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6**  **multicast**  \| **l2vpn** \| **vpn-instance** *vpn-instance-name* { **ipv4** \| **ipv6** \| **vpnv4** } \| **vpnv4** \| **vpnv6** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示IPv4地址族的BGP路由选择调试信息开关。

**[ipv6**]：表示IPv6地址族的BGP路由选择调试信息开关。

**[mdt**]：表示BGP MDT地址族的BGP路由选择调试信息开关。

**[multicast**]：表示BGP组播地址族的BGP路由选择调试信息开关。

**[l2vpn**]：表示L2VPN地址族的BGP L2VPN信息选择调试信息开关。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP路由选择调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP路由选择调试信息开关。

**[vpnv4**]：表示VPNv4地址族的BGP路由选择调试信息开关。

**[vpnv6**]：表示VPNv6地址族的BGP路由选择调试信息开关。

【描述】

**[debugging bgp calc**]命令用来打开BGP路由选择调试信息开关。**undo debugging bgp calc**用来关闭BGP路由选择调试信息开关。

缺省情况下，BGP路由选择调试信息开关处于关闭状态。

执行本命令时，如果没有指定**multicast**和**mdt**参数，则表示单播地址族。

【举例】

\# 打开BGP路由选择调试信息开关。设备通过BGP对等体学习到路由129.1.1.0/24，在该设备上手工配置一条到达129.1.1.0/24的静态路由，并将其引入到BGP路由，触发BGP路由优选。此时，设备上将打印如下调试信息。

\<Sysname\> debugging bgp calc

\<Sysname\> system-view

Sysname ip route-static 129.1.1.0 24 null 0

Sysname display ip routing-table 129.1.1.0 24

Routing Table : Public

Summary Count : 1

Destination/Mask    Proto  Pre  Cost         NextHop         Interface

129.1.1.0/24         Static 60   0            0.0.0.0         NULL0

Sysname display bgp ipv4 routing-table 129.1.1.0

 BGP local router ID: 80.1.1.200

 Local AS number: 100

 Paths:   1 available, 1 best

 BGP routing table entry information of 129.1.1.0/24:

 From            : 192.168.136.1 (192.168.136.1)

 Rely Nexthop    : 0.0.0.0

 Original nexthop: 192.168.136.1

 OutLabel        : NULL

 AS-path         : 200

 Origin          : igp

 Attribute value : pref-val 0, pre 255

 State           : valid, external, best,

Sysname bgp 100

Sysname-bgp address-family ipv4 unicast

Sysname-bgp-ipv4 import-route static

\*May 31 21:50:59:773 2010 Sysname BGP/7/DEBUG: -MDC=1;

 CALC process result, Dest/Mask: 129.1.1.0/24 :

         InstKey         : IPv4-UNC/0

         First Rt        : 0xb320ef88

         Last Active Rt  : 0xb320ef88

         Table           : 0

         Flag            : 0x201

*// 到达目的网络129.1.1.0/24的BGP路由选择结束，打印优选结果。*

**BGP \-- BGP调试命令 \-- debugging bgp event**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **event** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

**[undo debugging bgp** **event** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：表示与指定对等体之间BGP会话的事件调试信息开关。*ipv4-address*为对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：表示与指定对等体之间BGP会话的事件调试信息开关。*ipv6-address*为对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP事件调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP事件调试信息开关。

【描述】

**[debugging bgp event**]命令用来打开BGP事件调试信息开关。**undo debugging bgp event**命令用来关闭BGP事件调试信息开关。

缺省情况下，BGP事件调试信息开关处于关闭状态。

打开此调试信息开关，会打印所有BGP状态机转变过程和触发状态机转变的事件，如果BGP邻居无法建立，从中可以定位是在哪个状态出现问题，是什么事件触发等。

表1-4 debugging bgp event命令输出信息描述表

字段

描述

BGP

数据包属于BGP协议

*[X.X.X.X*]

BGP邻居的IPv4地址

*[X:X::X:X*]

BGP邻居的IPv6地址

Receive *Eventname* event in state,

在某状态收到事件

State is changed from *old-state* to *new-state*.

状态转换报文，原始状态：*old-state ;*

新状态：*new-state*

【举例】

\# 打开BGP事件调试信息开关。与BGP对等体建立会话时，将打印如下调试信息。

\<Sysname\> debugging bgp event

\*Apr 16 16:44:13:52 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from IDLE to CONNECT.

*[// BGP*]*会话从IDLE状态转换为CONNECT状态。*

\*Apr 16 16:44:13:60 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive Tcp_CR_Acked event in CONNECT state.

*// 在CONNECT状态收到Tcp_CR_Acked事件。*

\*Apr 16 16:44:13:66 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Connected to 192.168.109.29.

*// 建立TCP连接。*

\*Apr 16 16:44:13:71 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from CONNECT to OPENSENT.

*[// BGP*]*会话从CONNECT状态转换为OPENSENT状态。*

\*Apr 16 16:44:13:79 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive ReceiveOpenMessage event in OPENSENT state.

*// 在OPENSENT状态收到Open报文事件。*

\*Apr 16 16:44:13:80 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from OPENSENT to OPENCONFIRM.

*[// BGP*]*会话从OPENSENT状态转换为OPENCONFIRM状态。*

\*Apr 16 16:44:13:87 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 Receive ReceiveKeepAliveMsg event in OPENCONFIRM state.

*// 在OPENCONFIRM状态收到Keepalive报文事件。*

\*Apr 16 16:44:13:87 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 192.168.109.29 State is changed from OPENCONFIRM to ESTABLISHED.

*[// BGP*]*会话从OPENCONFIRM状态转换为ESTABLISHED状态，成功建立BGP会话。*

**BGP \-- BGP调试命令 \-- debugging bgp graceful-restart**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **graceful-restart** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

**[undo debugging bgp graceful-restart **[ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：表示与指定对等体之间的GR调试信息开关。*ipv4-address*为对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：表示与指定对等体之间的GR调试信息开关。*ipv6-address*为对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的GR调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网的GR调试信息开关。

【描述】

**[debugging bgp** **graceful-restart**]命令用来打开BGP的GR调试信息开关。**undo debugging bgp** **graceful-restart**命令用来关闭BGP的GR事件调试信息开关。

缺省情况下，BGP的GR调试信息开关处于关闭状态。

打开此调试信息开关，会打印BGP GR过程的调试信息，包括GR开始、GR结束等信息。如果BGP在GR过程中发生问题，可以打开该调试信息开关定位问题。

表1-5 debugging bgp graceful-restart命令输出信息描述表

字段

描述

PrevNegGrSessCnt

重启前协商GR的邻居个数

Restarter GR Starts

GR Restarter开始GR过程

Restarter GR Ends

GR Restarter结束GR过程

Get GR State Over. Start FSM

获取GR状态结束，启动状态机

Received EOR from Peer *peer-address* (*address-family*)

从对等体*peer-address*接收到EOR（End of Routing-Information-Base，路由信息库结束）标识，该EOR的地址族为*address-family*

Recv ALL_PEERS_UP EVT, Get EOR wait Count

所有需要等待的邻居都UP了，还需要等待的IPv4和IPv6 EOR数目

Trigger Calc NULL Node

触发最后一条表项优选

Trigger Calc Result NULL Node

触发处理优选后的最后一条表项

Global GR Send Protect Timer Created

创建触发发送的超时保护定时器

Recv SMOOTH_END Event

接收到RM平滑结束消息，老化引入的路由

Trigger All Prefix Received Node

通知发送模块触发发送

Sent EOR to Peer *peer-address* (*address-family*)

向对等体*peer-address*发送EOR标识，该EOR的地址族为*address-family*

【举例】

\# 在Device A上打开BGP的GR调试信息开关。在Device A和Device B之间建立BGP会话，并且会话处于Established状态。Device A上重启BGP协议时，Device A上将打印如下调试信息。

\<Sysname\> debugging bgp graceful-restart

\*Aug  9 17:34:51:255 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: PrevNegGrSessCnt 3.

*// 重启前协商GR的邻居个数为3个。*

\*Aug  9 17:34:51:255 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: (IPv4) Restarter GR Starts.

*[// IPv4*]*地址族开始GR。*

\*Aug  9 17:34:52:209 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: Get GR State Over. Start FSM.

*// 启动状态机。*

\*Aug  9 17:35:23:421 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Received EOR from Peer 12.1.3.2 (IPv4-VPN).

*// 收到EOR。*

\*Aug  9 17:35:48:704 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Received EOR from Peer 12.1.4.2 (IPv4-VPN).

\*Aug  9 17:36:16:383 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: Recv ALL_PEERS_UP EVT, Get EOR wait Count:

          IPv4 Count: 1, IPv6 Count: 0, L2VPN Count: 0.

*// 所有需要等待的邻居都UP了，还需要等待一个IPv4的EOR。*

\*Aug  9 17:36:16:383 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Received EOR from Peer 12.1.2.2 (IPv4-VPN)

\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: (IPv4) Restarter GR Ends.

*[// IPv4*]*地址族GR结束。*

\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: Trigger Calc NULL Node(VerID=0x2). IPv4.

\*Aug  9 17:36:19:205 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR: Trigger Calc Result NULL Node(VerID=0x2). IPv4.

*// 所有路由迭代结束后触发优选。*

\*Jan  1 00:44:00:786 2000 Sysname BGP/7/DEBUG:

 BGP_TIMER: Global GR Send Protect Timer Created. IPv4.

\*Jan  1 00:44:00:847 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Recv SMOOTH_END Event. usFamily 2.

\*Jan  1 00:44:00:848 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Delete All IPv4 Redist Routes With Stale Flag.

*[// BGP*]*接收到RM平滑结束消息，老化引入的路由。*

\*Jan  1 00:44:00:849 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Trigger Calc NULL Node(VerID=0x2). IPv4.

\*Jan  1 00:44:00:850 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Trigger Calc Result NULL Node(VerID=0x2). IPv4.

*[// RM*]*平滑结束后再次触发迭代优选。*

\*Jan  1 00:44:02:783 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Check All Prefix Received Success. IPv4.

\*Jan  1 00:44:02:783 2000 Sysname BGP/7/DEBUG:

 BGP_GR: Trigger All Prefix Received Node. IPv4.

*[// BGP*]*路由已经稳定，触发发送。*

\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Sent EOR to Peer 12.1.3.2 (IPv4-VPN).

*// 发送EOR。*

\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Sent EOR to Peer 12.1.4.2 (IPv4-VPN).

*// 发送EOR。*

\*Aug  9 17:36:22:206 2011 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_GR.: Sent EOR to Peer 12.1.2.2 (IPv4-VPN).

*// 发送EOR。*

**BGP \-- BGP调试命令 \-- debugging bgp ha**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **ha**]

**[undo debugging bgp** **ha**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp ha**]命令用来打开BGP的HA调试信息开关。**undo debugging bgp ha**用来关闭BGP的HA调试信息开关。

缺省情况下，该调试开关处于关闭状态。

打开此调试信息开关，会打印BGP主备线程间的调试信息。如果BGP在主备过程中发生问题，可以打开该调试信息开关定位。

表1-6 debugging bgp ha命令输出信息描述表

字段

描述

BGP-HA

BGP的HA调试信息

The main process received an HA message. Type: *type*.

接收到类型为*type*的HA消息

The standby process received realtime backup data from the main process. Data type: *type*.

备进程从主进程接收实备数据，数据类型为*type*

The standby process finished processing the realtime backup data. Result: *result*.

备进程处理完实备数据

Begin to backup data in batches.

批备数据开始

Finished backing up data in batches.

批备数据完成

Started to process the received HA message. Message type: *type*.

开始处理接收到的HA消息，消息类型为*type*

The main process backed up the configuration data to the standby process through HA channel. Result: *result*.

主进程通过HA通道将配置数据备份到备进程，返回值为*result*

Received an unknown HA message. Message type: *type*,

收到未知类型的HA消息，消息类型为*type*

The main process sent data to the backup process in batches through the HA channel. Result: *result*.

主进程通过批备通道给备进程发送数据，返回值为* result*

BGP notified HA that the operation *type* completed.

通知HA操作完成，操作类型为*type*

The main process backed up the VRF data to the standby process through HA channel. Result: *result*.

主进程通过HA通道将VRF数据备份到备进程，返回值为*result*

The main process backed up the session reset event to the standby process through HA channel. Result: *result*.

主进程通过HA通道将会话reset事件备份到备进程，返回值为*result*

The session thread received a Stop messge from the main process.

SESSION线程收到主进程发送的Stop消息

The session thread received a Upgrade messge from the main process.

SESSION线程收到主进程发送的升级消息

The main process backed up the data of update-group *group-id* to the standby process through HA channel. Result: *result*.

主进程通过HA通道将打包组ID为*group-id*的打包组数据备份到备进程，返回值为*result*

The send thread received a Stop messge from the main process.

SEND线程收到主进程发送的Stop消息

The send thread received a Upgrade messge from the main process.

SEND线程收到主进程发送的升级消息

Triggered the main process to backup data to the standby processes in batches. Trigger type: *type*, result: *result*.

触发主进程向备进程通知批备数据，触发类型为*type*，返回值为*result*

Notified the main thread to decrease the HA_UPGRADE_Cnt to *number*.

通知主线程将HA_UPGRADE_Cnt减少为*number*

Notified the main thread to decrease the HA_STOP_Cnt to *number*.

通知主线程将HA_UPGRADE_Cnt减少为*number*

Notified the main thread to decrease the HA_BATCH_Cnt to *number*.

通知主线程将HA_BATCH_Cnt减少为*number*

The BRIB thread received a Upgrade messge from the main process.

BRIB线程收到主进程发送的升级消息

【举例】

\# 在Device B上打开BGP的HA调试信息开关。在Device A和Device B之间建立BGP会话，并且会话处于Established状态。Device B上配置NSR时，设备上将打印如下调试信息。

\<Sysname\> debugging bgp ha

\*May 19 20:33:54:844 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The main process received an HA message. Type: 0x00000001.

*[// BGP-HA*]*接收到类型为0x00000001的HA消息。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The standby process received realtime backup data from the main process. Data type: 0x0001.

*[// BGP-HA*]*备进程从主进程接收实备数据，数据类型为0x0001。*

 BGP-HA: The standby process finished processing the realtime backup data. Result: 0x01.

*[// BGP-HA*]*备进程从主进程接收实备数据，数据类型为0x01。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The standby process finished processing the realtime backup data. Result: 0x01.

*[// BGP-HA*]*实备数据完成，返回值为0x01。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Begin backing up data in batches.

*[// BGP-HA*]*批备数据开始。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Finished backing up data in batches.

*[// BGP-HA*]*批备数据完成。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Started to process the received HA message. Message type: 0x01.

*[// BGP-HA*]*开始处理接收到的HA消息，消息类型为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The main process backed up the configuration data to the standby process through HA channel. Result: 0x01.

*[// BGP-HA*]*主进程通过HA通道将配置数据备份到备进程，返回值为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Received an unknown HA message. Message type: 0x01.

*[// BGP-HA*]*收到未知类型的HA消息，消息类型为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The main process sent data to the backup process in batches through the HA channel. Result: 0x01.

*[// BGP-HA*]*主进程通过批备通道给备进程发送数据，返回值为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: BGP notified HA that the operation 0x01 completed.

*[// BGP-HA*]*通知HA操作完成，操作类型为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The main process backed up the VRF data to the standby process through HA channel. Result: 0x01.

*[// BGP-HA*]*主进程通过HA通道将VRF数据备份到备进程，返回值为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The main process backed up the session reset event to the standby process through HA channel. Result: 0x01.

*[// BGP-HA*]*主进程通过HA通道将会话reset事件备份到备进程，返回值为0x01。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The session thread received a Stop messge from the main process.

*[// BGP-HA SESSION*]*线程收到主进程发送的Stop消息。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: The session thread received a Upgrade messge from the main process.

*[// BGP-HA SESSION*]*线程收到主进程发送的升级消息。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Triggered the main process to backup data to the standby processes in batches. Trigger type: 0x01. result: 0x02.

*[// BGP-HA*]*触发主进程向备进程通知批备数据，触发类型为0x01，返回值为0x02。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Notified the main thread to decrease the HA_UPGRADE_Cnt to 1.

*[// BGP-HA*]*通知主线程将HA_UPGRADE_Cnt减少为1。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP-HA: Notified the main thread to decrease the HA_STOP_Cnt to 2.

*[// BGP-HA*]*通知主线程将HA_UPGRADE_Cnt减少为2。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

BGP-HA: Notified the main thread to decrease the HA_BATCH_Cnt to 3.

*[// BGP-HA*]*通知主线程将HA_BATCH_Cnt减少为 3。*

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

BGP-HA: The BRIB thread received a Upgrade messge from the main process.

*[// BGP-HA*]*的BRIB线程收到主进程发送的升级消息。*

**BGP \-- BGP调试命令 \-- debugging bgp ipc**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **ipc**]

**[undo debugging bgp** **ipc**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp ipc**]命令用来打开BGP的线程间通信调试信息开关。**undo debugging bgp ipc**用来关闭BGP的线程间通信调试信息开关。

缺省情况下，BGP线程间通信调试信息开关处于关闭状态。

打开此调试信息开关，会打印BGP各线程间的调试信息，信息中给出了当前触发的信号量。如果BGP在线程通信过程中发生问题，可以打开该调试信息开关定位。

表1-7 debugging bgp ipc命令输出信息描述表

字段

描述

BGP

数据包属于BGP协议

MAIN/SEND/BRIB/SESSION/CALC/RELY

BGP各线程

receive

接收事件

process

处理事件

sent

发送事件

Notify done

通知事件处理完成

0x00072005

信号量

【举例】

\# 在Device A上打开BGP的IPC调试信息开关。在Device A和Device B之间建立BGP会话，并且会话处于Established状态。Device A上配置一条命令时，设备上将打印如下调试信息。

\<Sysname\> debugging bgp ipc

 \*May 19 20:33:54:844 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    receive EVENT : 0x00072005.

\*May 19 20:33:54:845 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_SEND   to SEND.

*[// Send*]*线程收到给自己的发送信号。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    process EVENT : 0x00072005.

*[// Send*]*线程处理事件。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    notify  EVENT : 0x00072005 done.

*[// Send*]*线程通知事件完成。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_MAIN   to MAIN.

*[// Send*]*线程发送信号给MAIN线程。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    receive EVENT : 0x00072005.

*[// BRIB*]*线程接收到事件。*

\*May 19 20:33:54:846 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_BRIB   to BRIB.

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    process EVENT : 0x00072005.

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    notify  EVENT : 0x00072005 done.

\*May 19 20:33:54:847 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION receive EVENT : 0x00072005.

\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;

 MAIN    process EVENT : 0x00072005.

\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;

 MAIN    process EVENT : 0x00072005.

\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION process EVENT : 0x00072005.

\*May 19 20:33:54:848 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SESSION notify  EVENT : 0x00072005 done.

\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_MAIN   to MAIN.

\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;

 MAIN    process EVENT : 0x00072005.

\*May 19 20:33:54:849 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    receive EVENT : 0x00072005.

\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_SEND   to SEND.

\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    process EVENT : 0x00072005.

\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND    notify  EVENT : 0x00072005 done.

\*May 19 20:33:54:850 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_MAIN   to MAIN.

\*May 19 20:33:54:851 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    receive EVENT : 0x00072005.

\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;

 Send SIGNAL: SIG_BRIB   to BRIB.

\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    process EVENT : 0x00072005.

\*May 19 20:33:54:852 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BRIB    notify  EVENT : 0x00072005 done.

**BGP \-- BGP调试命令 \-- debugging bgp non-stop-routing**

------------------------------------------------------------------------

【命令】

**[debugging bgp non-stop-routing**]

**[undo debugging non-stop-routing**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging bgp** **non-stop-routing**]命令用来打开BGP NSR调试信息开关。**undo debugging bgp** **non-stop-routing**命令用来关闭BGP NSR事件调试信息开关。

缺省情况下，BGP NSR调试信息开关处于关闭状态。

打开此调试信息开关，会打印出BGP NSR过程的调试信息，包括NSR开始、NSR结束等信息。如果BGP在NSR过程中发生问题，可以打开该调试信息开关定位问题。打开调试信息开关会影响系统的性能，因此，请不要轻易打开调试信息开关，调试完毕后，请及时关闭调试信息开关。

表1-8 debugging bgp non-stop-routing命令输出信息描述表

字段

描述

BGP_NSR

BGP NSR相关信息

Received NSR batch backup start event, and notified *number* threads

收到NSR批备消息，已经通知*number*个线程开始批备NSR数据

Notified the standby process to start batch backup. Result: *result*

BGP通知备板开始批备，结果为*result*

Notified the BGP standby process that the memory of the BGP primary process had reached the critical state. Result: *result*

BGP主进程达到三级内存门限，通知备进程，返回值为*result*

Received ACK message from HA. Type: *type*, length: *length*

BGP接收到HA回复的ACK消息，类型值为*type*，消息长度为*length*字节

Received a BGP message from BGP peer *peer-address*, and backed up the information of the message to the standby process through HA. Information length: *length*, result: *result*

收到BGP对等体*peer-address*,发送的报文后通过HA将报文信息备份到备板，备份的信息长度为*length*字节，返回值为*result*

Backed up the *event-type* event to the standby process for BGP peer *peer-address* (*address-family*)

为地址族*address-family*的BGP对等体*peer-address*将*message-type*消息备份到备进程

*[address-family*]的取值包括：

·IPv4-UNC：IPv4单播地址族

·IPv4-VPN：VPNv4地址族

·IPv6-UNC：IPv6单播地址族

·IPv6-VPN：VPNv4地址族

*[event-type*]取值包括：

·refresh-in：入方向的软重启事件

·undo-keep-all-routes：取消保存所有路由事件

The batch backup of BRIB started. Result: *result*

BRIB开始批备，返回值为*result*

Backed up the send status *status*. Time stamp: *time-stamp*, result: *result*

BGP主进程备份send的状态*status*，时间戳为*time-stamp*，返回值是*result*

BGP.*vpn-instance-name*

VPN实例*vpn-instance-name*内的BGP相关信息

Enabled the TCP NSR option of socket *socket-id* for BGP peer *peer-address*. Result: *result*

为BGP对等体*peer-address*使能socket的TCP NSR选项，Socket ID为*socket-id*，返回值为*result*

Disabled the TCP NSR option of socket *socket-id* for BGP peer *peer-address*. Result: *result*

为BGP对等体*peer-address*关闭socket的TCP NSR选项，Socket ID为*socket-id*，返回值为*result*

Set the preferred standby process of socket *socket-id* to the process located on slot *slot-number* for BGP peer *peer-address*. Result: *result*

为BGP对等体*peer-address*设置socket优选的备板号是*slot-number*，返回值为*result*

Failed to delete the packet from the receive cache for BGP peer *peer-address* due to incorrect time-stamp

由于时间戳错误，为BGP对等体*peer-address*删除接收缓冲区中的报文失败

Deleted the packet from the cache of socket *socket-id* for BGP peer *peer-address*. Delete length: *delete-length*, remaining length: *remaining-length*

为BGP对等体*peer-address*删除socket缓冲区中的报文，Socket ID为*socket-id*，本次删除的报文长度为*delete-length*字节，剩余报文的长度为*remaining-length*字节

After processing the null message for BGP peer *peer-address*, BGP notified the standby process that backup finished. Result: *result*

为BGP对等体*peer-address*处理完空报文后通知备进程备份完成，返回值为*result*

After sending an Update message to BGP peer *peer-address*, BGP notified the standby process to delete the update message backed up previously. Result: *result*

向BGP对等体*peer-address*发送Update消息后，通知备进程删除之前备份的Update消息，返回值为*result*

When processing the refresh event for BGP peer *peer-address*, BGP backed up the refresh state to the standby process. Result: *result*

处理BGP对等体*peer-address*的Refresh事件时，将Refresh状态备份到备进程，返回值为*result*

The batch backup of BGP session started. Result: *result*

BGP session进程开始批备

【举例】

\# 配置BGP协议后，打开BGP NSR调试开关。

\<Sysname\> debugging bgp non-stop-routing

 \*May 19 20:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Received NSR batch backup start event, and notified 3 threads

*[// BGP*]*收到NSR批备消息，通知了3个线程开始批备。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Notified the standby process to start batch backup. Result: 0

*[// BGP*]*备份NSR批备开始消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Notified the BGP standby process that the memory of the BGP primary process had reached the critical state. Result: 0

*[// BGP*]*主进程内存门限时通知备进程删除数据消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Received ACK message from HA. Type: 1, length: 20

*[// BGP*]*接收到HA回复的ACK消息，类型值1，消息长度20。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Received a BGP message from BGP peer 1.1.1.1, and backed up the information of the message to the standby process through HA. Information length: 19, result: 0

*[// BGP*]*会话1.1.1.1接收到报文处理后向HA写入消息长度为19，返回值为0。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Backed up the refresh-in event to the standby process for BGP peer 1.1.1.1 (IPv4-UNC)

*[// BGP IPv4*]*单播邻居1.1.1.1备份refresh-in状态到备进程。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Backed up the undo-keep-all-routes event to the standby process for BGP peer 1.1.1.1 (IPv4-UNC)

*[// BGP IPv4*]*单播邻居1.1.1.1备份undo-keep-all-routes状态到备进程。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: The batch backup of BRIB started. Result: 0

*[// BGP*]*备份BRIB备份开始消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: Backed up the send status 1. Time stamp: 1, result: 0

*[// BGP SEND*]*备份状态消息，时间戳为1。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Enabled the TCP NSR option of socket 1 for BGP peer 1.1.1.1. Result: 0

*[// BGP *]*使能vpn1邻居1.1.1.1的tcp nsr选项。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Set the preferred standby process of socket 2 to the process located on slot 2 for BGP peer 1.1.1.1. Result: 0

*[// BGP *]*设置vpn1邻居1.1.1.1的优选备选项。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Failed to delete the packet from the receive cache for BGP peer 1.1.1.1 due to incorrect time-stamp

*// 时间戳错误，丢弃vpn1邻居1.1.1.1的报文。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: Deleted the packet from the cache of socket 2 for BGP peer peer-address. Deletelength: 20, remaining length: 30

*[// BGP*]*通知TCP  drop掉vpn1邻居1.1.1.1缓冲区。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: After processing the null message for BGP peer 1.1.1.1, BGP notified the standby process that backup finished. Result: 0.

*[// BGP  vpn1*]*邻居1.1.1.1处理完空报文向备进程备份消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: After sending an Update message to BGP peer 1.1.1.1, BGP notified the standby process to delete the update message backed up previously. Result: 0

*[// BGP  vpn1*]*邻居1.1.1.1发送完UPDATE报文后向备进程确认消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.vpn1: When processing the refresh event for BGP peer 1.1.1.1, BGP backed up the refresh state to the standby process. Result: 0

*[// BGP  vpn1*]*邻居1.1.1.1发送完除UPDATE外的其他报文后向备进程确认消息。*

\*May 19 21:33:54:844 2013 Sysname BGP/7/DEBUG: -MDC=1;

 BGP_NSR: The batch backup of BGP session started. Result: 0

*[// BGP SESSION*]*备份开始消息。*

**BGP \-- BGP调试命令 \-- debugging bgp prefix-list**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **prefix-list** *prefix-list-name*]

**[undo debugging bgp prefix-list**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[prefix-list-name*]：用于匹配路由信息目的网络地址的IP地址前缀列表，为1～63个字符的字符串，区分大小写。

【使用指导】

**[debugging bgp prefix-list**]命令用来打开通过IP地址前缀列表过滤的BGP路由的调试信息开关。**undo debugging bgpprefix-list**命令用来关闭通过IP地址前缀列表过滤的BGP路由的调试信息开关。

缺省情况下，BGP路由的调试信息开关处于关闭状态。

需要注意的是，如果同时配置了本命令和**debugging bgp acl**命令，则只有BGP路由同时通过ACL和IP地址前缀列表过滤，才会打开该路由的调试信息开关。

【举例】

\# 通过配置IP地址前缀列表过滤条件，打开BGP路由11.1.1.1/32的调试信息开关。设备接收到对端发布的11.1.1.1/32和11.1.1.2/32两条路由后，打印如下调试信息。

\<Sysname\> system-view

Sysname ip prefix-list p1 permit 11.1.1.1 32

Sysname quit

\<Sysname\> debugging bgp update

\<Sysname\> debugging bgp prefix-list p1

\*Dec 20 16:02:33:923 2011 H3C BGP/7/DEBUG: -MDC=1;

         BGP.: Recv UPDATE from peer 13.1.1.1 with following destinations:

         Update message length : 60

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 13.1.1.1

         MED          : 0

         11.1.1.1/32,

*// 对端发布两条路由11.1.1.1/32和11.1.1.2/32，只有11.1.1.1/32通过IP地址前缀列表过滤，因此，只打印11.1.1.1/32 的调试信息。*

**BGP \-- BGP调试命令 \-- debugging bgp rely**

------------------------------------------------------------------------

【命令】

**[debugging bgp rely**[[ **common** \| **tunnel** ]]]

**[undo debugging bgp rely **[[ **common** \| **tunnel** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[common**]：迭代到普通路由。

**[tunnel**]：迭代到隧道。

【描述】

**[debugging bgprely**]命令用来打开BGP路由迭代调试信息开关。**undo debugging bgprely**命令用来关闭BGP路由迭代调试信息开关。

缺省情况下，BGP rely调试开关处于关闭状态。

【举例】

\# 打开BGP路由迭代调试信息开关。设备上进行路由迭代时，打印如下调试信息。

\<Sysname\> debugging bgp rely

\*May 31 21:48:48:511 2010 Sysname BGP/7/DEBUG: -MDC=1;

 RELY add rely node, Dest/Mask: 129.1.1.0/24 :

          InstKey         : IPv4-UNC/0

         Original NextHop: 192.168.136.1

Rely     NextHop: NULL

         NbrType         : 4097

         VrfIndexNexthop: 0

         TnlPolicy       :

         IfIndexOrig     : 0

         TunnelID        : 0

         Action          : 1

\*May 31 21:48:48:526 2010 Sysname BGP/7/DEBUG: -MDC=1;

 RELY process result, Dest/Mask: 129.1.1.0/24 :

InstKey         : IPv4-UNC/0

         Original NextHop: 192.168.136.1

         Old Rely NextHop: NULL

         New Rely NextHop: 0.0.0.0

         Table           : 0

         Type            : SUCCEDED

**BGP \-- BGP调试命令 \-- debugging bgp timer**

------------------------------------------------------------------------

【命令】

**[debugging bgp** **timer** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

**[undo debugging bgp** **timer** [ *ipv4-address* [ *mask-length*  *\| ipv6-address*  *prefix-length*  \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  *\| ipv6-address*  *prefix-length*  } ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP定时器调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP定时器超时调试信息开关。

【描述】

**[debugging bgp timer**]命令用来打开BGP定时器调试信息开关。**undo debugging bgp timer**用来关闭BGP定时器调试信息开关。

缺省情况下，BGP定时器调试信息开关处于关闭状态。

表1-9 debugging bgp timer命令输出信息描述表

字段

描述

Peer X.X.X.X

对端邻居的IPv4地址

Peer *X:X::X:X*

对端邻居的IPv6地址

CR Timer

重新尝试连接（Connect Retry）定时器

KA Timer

KeepAlive超时定时器

HD Timer

连接超时定时器

BGP Timers debugging is on

BGP定时器调试信息开关处于打开状态

【举例】

**[\# **]在设备A上打开BGP定时器调试信息开关。在设备A上创建对等体2.2.2.2（设备B的地址），在设备B上不指定设备A为其对等体。此时，设备A上将打印如下调试信息。

\<Sysname\> debugging bgp timer

\*Apr 16 18:12:50:861 2010 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: 2.2.2.2 CR Timer Created.

*// 为BGP对等体2.2.2.2创建重新尝试连接定时器。*

**BGP \-- BGP调试命令 \-- debugging bgp update**

------------------------------------------------------------------------

【命令】

**[debugging bgp update **[ *ipv4-address* [ *mask-length*  [ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6** \| **vpnv4** \| **vpnv6** ] \| *ipv6-address*  *prefix-length*   **ipv6** [ **multicast**  ] \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  { **ipv4** \| **vpnv4** } \| *ipv6-address*  *prefix-length*  **ipv6** }   **receive** \| **send** ]]]

**[undo** **debugging bgp update** [ *ipv4-address* [ *mask-length*  [ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6** \| **vpnv4** \| **vpnv6** ] \| *ipv6-address*  *prefix-length*   **ipv6** [ **multicast**  ] \| **vpn-instance** *vpn-instance-name* { *ipv4-address*  *mask-length*  { **ipv4** \| **vpnv4** } *\| ipv6-address*  *prefix-length*  **ipv6** }   **receive** \| **send** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv4-address*]：对等体的IPv4地址。

*[mask-length*]：网络掩码，取值范围为0～32。如果指定本参数，则表示指定网段内的动态对等体。

*[ipv6-address*]：对等体的IPv6地址。

*[prefix-length*]：前缀长度，取值范围为0～128。如果指定本参数，则表示指定网段内的动态对等体。

**[ipv4**]：IPv4单播地址族。

**[mdt**]：表示BGP MDT地址族。

**[multicast**]：表示BGP组播地址族。

**[ipv6**]：IPv6单播地址族。

**[vpnv4**]：VPNv4地址族。

**[vpnv6**]：VPNv6地址族。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP更新报文调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP更新报文调试信息开关。

**[receive**]：接收的BGP报文。

**[send**]：发送的BGP报文。

【描述】

**[debugging bgp update**]命令用来打开BGP更新报文的调试信息开关。**undo debugging bgp update**命令用来关闭BGP更新报文的调试信息开关。

缺省情况下，BGP更新报文调试信息开关处于关闭状态。

执行本命令时，如果没有指定**mdt**和**multicast**参数，则表示单播地址族。

表1-10 debugging bgp update ipv4命令输出信息描述表

字段

描述

BGP.xxx

当前实例名

Recv UPDATE from x.x.x.x

从BGP邻居x.x.x.x收到更新路由

Recv UPDATE from x:x::x:x

从BGP邻居x:x::x:x收到更新路由

Recv UPDATE(Withdraw) from x.x.x.x

从BGP邻居x.x.x.x收到撤销路由

Recv UPDATE(Withdraw) from x:x::x:x

从BGP邻居x:x::x:x收到撤销路由

Send UPDATE to x.x.x.x

向BGP邻居x.x.x.x发送更新路由

Send UPDATE to x:x::x:x

向BGP邻居x:x::x:x发送更新路由

Send UPDATE(Withdraw) to peer x.x.x.x

向BGP邻居x.x.x.x发送撤销路由

Send UPDATE(Withdraw) to peer x:x::x:x

向BGP邻居x:x::x:x发送撤销路由

x.x.x.x/xx

目的地址/掩码

Update message length

Update报文长度

Origin

BGP的Origin属性

AS path

BGP的AS Path属性

Next hop

BGP的Next Hop属性

Local pref

BGP的Local Pref属性

MED

BGP的MED属性

Community

BGP的团体属性

Ext-Community

BGP的扩展团体属性

Send UPDATE MSG to peer *peer-address*(*address-family*) NextHop: *next-hop*

向地址族*address-family*的对等体*peer-address*发送Update消息，下一跳地址为*next-hop*

 

【举例】

\# 在两台设备A和B之间建立BGP会话。在设备A上打开BGP更新报文调试信息开关。A和B之间交互IPv4单播路由时，将打印如下调试信息。

\<Sysname\> debugging bgp update

\*Apr 16 21:06:16:48 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Send UPDATE to peer 192.168.109.1 for following destinations:

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 192.168.109.88

         111.1.1.1/32,

*// 向192.168.109.1发送Update报文，发布路由111.1.1.1/32。*

\*Apr 16 21:09:59:37 2010 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Recv UPDATE from peer 192.168.109.1 with following destinations:

         Origin       : Incomplete

         AS path      : 500 501

         Next hop     : 192.168.109.1

         MED          : 150

ADD route, Dest/Mask: 12.12.12.0/24.

         Origin       : Incomplete

         AS path      : 500 501

         Next hop     : 192.168.109.1

         MED          : 150

*// 从192.168.109.1接收到Update报文，该报文携带路由12.12.12.0/24。*

\*Apr 16 21:09:59:58 2010 2012 Sysname BGP/7/DEBUG: -MDC=1;

 BGP.: Send UPDATE MSG to peer 192.168.109.87(IPv4-UNC) NextHop: 192.168.109.88.

*// 向BGP对等体192.168.109.87发送Update报文，下一跳地址为192.168.109.88。*

**BGP \-- BGP调试命令 \-- debugging bgp update-group**

------------------------------------------------------------------------

【命令】

**[debugging bgp update-group **[ [ **vpn-instance** *vpn-instance-name*  { **ipv4** \| **ipv6** } \| **ipv4 mdt** \| { **ipv4** \| **ipv6** } **multicast** ]]]

**[undo debugging bgp update-group **[ [ **vpn-instance** *vpn-instance-name*  { **ipv4** \| **ipv6** } \| **ipv4 mdt** \| { **ipv4** \| **ipv6** } **multicast** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的打包组调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网打包组的调试信息开关。

**[ipv4**]：表示IPv4单播地址族。

**[ipv6**]：表示IPv6单播地址族。

**[ipv4 mdt**]：表示IPv4 MDT地址族。

**[multicast**]：表示BGP组播地址族。

【描述】

**[debugging bgp update-group**]命令用来打开BGP打包组调试信息开关。**undo debugging bgp update-group**命令用来关闭BGP打包组调试信息开关。

缺省情况下，BGP打包组调试信息开关处于关闭状态。

需要注意的是：

·执行本命令时，如果没有指定任何参数，则表示打开或关闭所有打包组的调试信息开关。

·执行本命令时，如果没有指定**multicast**和**mdt**参数，则表示单播地址族。

表1-11 debugging bgp update-group命令输出信息描述表

字段

描述

BGP.*vpn-instance-name*

VPN实例*vpn-instance-name*内的BGP打包组信息

Send UPDATE to update-group *group-id*

向BGP打包组*group-id*发送路由更新

Send UPDATE(Withdraw) to update-group *group-id*

向BGP打包组*group-id*发送路由撤销

*[destination-address*/*mask-length*]

发布的路由前缀的目的地址和掩码

Update message length

Update消息长度

Origin

BGP的Origin属性

AS path

BGP的AS Path属性

Next hop

BGP的Next Hop属性

Local pref

BGP的Local Pref属性

MED

BGP的MED属性

Community

BGP的团体属性

Ext-Community

BGP的扩展团体属性

update-group *group-id* *address-family* created

创建地址族*address-family*的打包组*group-id*

update-group *group-id* *address-family* deleted

删除地址族*address-family*的打包组*group-id*

【举例】

\# 打开BGP打包组调试信息开关，发布BGP路由时，设备上将打印如下信息。

\<Sysname\> debugging bgp update-group

\*Apr 16 21:06:16:48 2012 Sysname BGP/7/DEBUG: -MDC=1;

         BGP.: Send UPDATE to update-group 0 for following destinations:

         Origin       : Incomplete

         AS path      : 100

         Next hop     : 192.168.109.88

         111.1.1.1/32,

*// 向BGP打包组0发送路由更新，路由的Origin属性为Incomplete，AS path属性为100，下一跳地址为192.168.109.88，发布的路由前缀为111.1.1.1/32。*

\# 打开BGP打包组调试信息开关，创建和删除打包组时，打印如下调试信息。

\<Sysname\> debugging bgp update-group

\*Aug 16 10:24:34:132 2012 PE2 BGP/7/DEBUG: -MDC=1;

 BGP.: update-group 0 IPv6-UNC created.

*// 创建IPv6单播地址族的打包组0。*

\*Aug 16 10:24:02:896 2012 PE2 BGP/7/DEBUG: -MDC=1;

 BGP.: update-group 0 IPv6-UNC deleted.

*// 删除IPv6单播地址族的打包组0。*

**BGP \-- BGP调试命令 \-- debugging bgp urt**

------------------------------------------------------------------------

【命令】

**[debugging bgp**[ **urt** [ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6**  **multicast**  \| **l2vpn** \| **vpn-instance** *vpn-instance-name* [ **ipv4** \| **ipv6** \| **vpnv4** ] \| **vpnv4** \| **vpnv6** ]]]

**[undo debugging bgp**[ **urt** [ **ipv4** [ **mdt** \| **multicast** ] \| **ipv6**  **multicast**  \| **l2vpn** \| **vpn-instance** *vpn-instance-name* [ **ipv4** \| **ipv6** \| **vpnv4** ] \| **vpnv4** \| **vpnv6** ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：IPv4单播地址族。

**[mdt**]：表示IPv4 MDT地址族。

**[multicast**]：表示BGP组播地址族。

**[ipv6**]：IPv6单播地址族。

**[l2vpn**]：L2VPN地址族。

**[vpn-instance ***vpn-instance-name*]：表示指定VPN实例的BGP更新、添加、删除路由的调试信息开关。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则表示公网BGP更新、添加、删除路由的调试信息开关。

**[vpnv4**]：VPNv4地址族。

**[vpnv6**]：VPNv6地址族。

【描述】

**[debugging bgp urt**]命令用来打开BGP更新、添加、删除路由的调试信息开关。**undo debugging bgp urt**命令用来关闭BGP更新、添加、删除路由的调试信息开关。

缺省情况下，该调试开关处于关闭状态。

执行本命令时，如果没有指定**multicast**和**mdt**参数，则表示单播地址族。

表1-12 debugging bgp urt命令输出信息描述表

字段

描述

BGP.*vpn-instance*

VPN实例*vpn-instance*的调试信息

如果不携带*vpn-instance*参数，则表示公网的调试信息

MODIFY

修改路由信息

Dest/Mask

目的地址/掩码

Old attribute

原属性

New attribute

修改后的属性

Old real nexthop

修改前的真实下一跳

New real nexthop

修改后的真实下一跳

ADD

添加一条路由信息

DELETE

删除一条路由信息

Origin

BGP的Origin属性

AS path

BGP的AS Path属性

Next hop

BGP的Next Hop属性

Local pref

BGP的Local Pref属性

MED

BGP的MED属性

Community

BGP的团体属性

Ext-Community

BGP的扩展团体属性

NbrId

BGP的邻居ID

Outif

BGP路由的物理出接口

Logicif

BGP路由的逻辑出接口

Metric

BGP路由的MED值

Pref

BGP路由的路由优选值

ProtoID

BGP路由的协议ID

SubProto

BGP路由的子协议ID

Route common

BGP路由的通用信息

Tag

BGP路由信息的外部标记

Outlabel

BGP路由的出标签值

Weight

BGP路由信息的权重值

ProcessID

进程ID

IpPrec

IP优先级

QosLocID

Qos-Local-ID属性

OriRD

原始RD

VNID

引入路由的VNID

ProtoID

路由协议类型

SubProID

路由协议子类型

OrigProtoID

源路由协议类型

InstKey

路由所属实例的Key值

【举例】

\# 在设备A上打开BGP更新、添加、删除路由的调试信息开关。在两台设备A和B之间建立BGP会话，并在二者之间发布BGP路由。设备A上打印如下调试信息。

\<Sysname\> debugging bgp urt

\*Apr 16 22:24:11:24 2010 Sysname BGP/7/DEBUG: -MDC=1;

 ADD route, Dest/Mask: 14.14.14.14/32.

         Origin       : Incomplete

         AS path      : 500 501

         Next hop     : 192.168.109.1

         MED           : 100

\*Apr 16 22:24:11:84 2010 Sysname BGP/7/DEBUG: -MDC=1;

 ADD route common, Dest/Mask: 14.14.14.14/32, InstKey: IPv4-UNC/0.

       Tag      : 0         , Outlabel   : 4294967295

       Weight   : 0        , ProtoID     : 6

       SubProID : 1        , ProcessID  : 0

       IpPrec   : 65535    , QosLocID   : 65535

                                OrigProtoID: 6

       OriRD    : 0x0,

       VNID     : 0x0

*[// IPv4*]*地址族下收到Update报文，添加一条路由信息。*

\*Apr 16 22:24:11:104 2010 Sysname BGP/7/DEBUG: -MDC=1;

 MODIFY route common, Dest/Mask: 14.14.14.14/32, InstKey: IPv4-UNC/0.

 Old : Tag      : 0         , Outlabel   : 4294967295

       Weight   : 0         ,  ProtoID    : 6

       SubProID : 1         , ProcessID  : 0

       IpPrec   : 5         ,  QosLocID   : 5

                                 OrigProtoID: 6

       OriRD    : 0x0,

       VNID     : 0x0

 New : Tag      : 0         , Outlabel   : 4294967295

       Weight   : 0         ,  ProtoID    : 6

       SubProID : 1         , ProcessID  : 0

       IpPrec   : 65535     , QosLocID   : 65535

                                 OrigProtoID: 6

       OriRD    : 0x0

       VNID     : 0x0

\*Apr 16 22:24:11:123 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND Process Prefix. 14.14.14.14/32,  AttrId: 6, Op: ADD.

*// 修改路由的属性值。*

\*Apr 16 22:30:32:108 2010 Sysname BGP/7/DEBUG: -MDC=1;

 DELETE Route, Dest/Mask: 14.14.14.14/32.

\*Apr 16 22:30:32:110 2010 Sysname BGP/7/DEBUG: -MDC=1;

 SEND Process Prefix. 14.14.14.14/32,  AttrId: 0, Op: DELETE.

*[// IPv4*]*地址族下收到Update报文，删除一条路由信息。*
