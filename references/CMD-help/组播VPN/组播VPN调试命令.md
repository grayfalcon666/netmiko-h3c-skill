<!-- CMD-INDEX
  debugging multicast-domain          | 用户视图             | L5
-->

**组播VPN \-- 组播VPN调试命令 \-- debugging multicast-domain**

------------------------------------------------------------------------

【命令】

**[debugging** **multicast-domain** [ **vpn-instance** *vpn-instance-name*  { **all** \| **event**  *advanced-acl-number*  \| **packet** \| **timer** }]]

**[undo** **debugging** **multicast-domain** [ **vpn-instance** *vpn-instance-name*  { **all** \| **event** \| **packet** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定VPN实例，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。

**[all**]：表示MD的所有调试信息开关。

**[event**]：表示MD事件调试信息开关。

*[advanced-acl-number*]：表示IPv4高级ACL的编号，取值范围为3000～3999。

**[packet**]：表示MD报文调试信息开关。

**[timer**]：表示MD定时器调试信息开关。

【描述】

**[debugging** **multicast-domain**]命令用来打开MD调试信息开关。**undo** **debugging** **multicast-domain**命令用来关闭MD调试信息开关。

缺省情况下，MD调试信息开关处于关闭状态。

表1-1 debugging multicast-domain event命令输出信息描述表

字段

描述

create msg

MTI接口创建消息

destroy msg

MTI接口删除消息

up msg

MTI接口生效消息

down msg

MTI接口失效消息

join

加入MD组消息

prune

离开MD组消息

smooth

MD数据平滑

表1-2 debugging multicast-domain packet命令输出信息描述表

字段

描述

send/receive

发送/接收MD报文

MDT-Join packet

MD切换报文（由切换消息"MDT Join-TLV"构成）

from/to

报文的源/目的地址

type

切换消息中的类型，具体请参见RFC 6037

(1.1.1.1, 225.1.1.1) -\> 239.1.1.1

切换消息中的私网（S，G）地址及公网Data-Group地址

ignoring the packet

忽略报文

ignoring this MDT-Join

忽略该MD切换报文

表1-3 debugging multicast-domain timer命令输出信息描述表

字段

描述

reconnect

重新连接定时器

smooth

平滑相关定时器

reflush

失败重刷定时器（如MTI接口创建失败等）

memory

内存门限恢复相关定时器

【举例】

\# 打开VPN实例mvpn的MD事件调试信息开关。

\<Sysname\> debugging multicast-domain vpn-instance mvpn event

\*Nov  6 14:03:00:840 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MTunnel0 create msg to IPv4 MBR. (D04211)

*// 向IPv4 MBR发送VPN实例mvpn内MTI0接口的创建消息*

\*Nov  6 14:03:11:286 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MTunnel0 up msg to IPv4 MBR. (D04224)

*// 向IPv4 MBR发送VPN实例mvpn内MTI0接口的生效消息*

\*Nov  6 14:03:11:286 2012 Sysname MD/7/EVENT: -MDC=1; (mvpn): Send MD join (\*, 239.1.1.1) on MTunnel0 to IPv4 MBR. (D04229)

*// 向IPv4 MBR发送VPN实例mvpn内MTI0接口上的加入MD组（\*, 239.1.1.1）的消息*

\# 打开VPN实例mvpn的MD报文调试信息开关。

\<Sysname\> debugging multicast-domain vpn-instance mvpn packet

\*Jan 21 12:42:03:480 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Send a packet from 1.1.0.1 to 224.0.0.13, length: 16. (D11511)

*// 从1.1.0.1向224.0.0.13发送了一个长度为16字节的MD切换报文*

\*Jan 21 13:12:49:026 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Receive a packet from 1.1.0.1 to 224.0.0.13, length: 16. (D111858)

*// 收到了一个从1.1.0.1发向224.0.0.13的、长度为16字节的MD切换报文*

\*Jan 21 12:42:03:480 2013 Sysname MD/7/PACKET: -MDC=1; (mvpn): Type 1, length 16, (7.11.0.7, 225.1.1.1) -\> 239.1.2.0 (D11409)

*// 切换消息的类型为1（表示IPv4，具体请参见RFC 6037），长度为16字节，私网数据流为(7.11.0.7, 225.1.1.1)，切换到公网的组地址为239.1.2.0*

\# 打开公网实例MD定时器调试信息开关。

\<Sysname\> debugging multicast-domain timer

\*Nov  6 14:25:11:171 2012 Sysname MD/7/TIMER: -MDC=1; Create reconnet IPv4 MBR timer success. (D08282)

*// 成功创建重新连接IPv4 MBR定时器*

\*Nov  6 14:25:14:684 2012 Sysname MD/7/TIMER: -MDC=1; Create smooth end timer (90s). (D021269)

*// 创建等待平滑结束定时器，超时时间为90秒*
