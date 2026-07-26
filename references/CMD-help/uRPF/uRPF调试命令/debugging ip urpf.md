
**uRPF \-- uRPF调试命令 \-- debugging ip urpf**

------------------------------------------------------------------------

【命令】

**[debugging ip urpf ** **interface** *interface-type interface-number* ]

**[undo debugging ip urpf ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：指定的接口类型和编号。

【描述】

**[debugging ip urpf**]命令用来打开uRPF调试信息开关。**undo debugging ip urpf**命令用来关闭uRPF调试信息开关。

缺省情况下，uRPF调试信息开关处于关闭状态。

表1-1 debugging ip urpf命令输出信息描述表

字段

描述

uRPF  uRPF-Discard: Packet from *ip-address* via *interface-type interface-number*

从指定接口收到的源地址为*ip-address*的报文被丢弃

uRPF  uRPF-Discard-Suppress: Packet from *ip-address* via *interface-type interface-number*

从指定接口收到的源地址为*ip-address*的报文被uRPF抑制后，匹配ACL规则成功，然后被转发

【举例】

\# 在一台启动了uRPF调试信息开关的设备上，收到源地址不可识别的报文，则打印以下调试信息。

\<Sysname\> debugging ip urpf{.TerminalDisplayChar}

\*0.3933516 Sysname URPF/7/debug_info:

 uRPF uRPF-Discard: Packet from 2.2.2.5 via GigabitEthernet1/0/1

*// 从接口GigabitEthernet1/0/1收到的源地址为2.2.2.5的报文被丢弃*

*\
*

**IPv6 uRPF \-- IPv6 uRPF调试命令 \-- debugging ipv6 urpf**

------------------------------------------------------------------------

【命令】

**[debugging ipv6 urpf ** **interface** *interface-type interface-number* ]

**[undo debugging ipv6 urpf ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：指定的接口类型和编号。

【描述】

**[debugging ipv6 urpf**]命令用来打开IPv6 uRPF调试信息开关。**undo debugging ipv6 urpf**命令用来关闭IPv6 uRPF调试信息开关。

缺省情况下，IPv6 uRPF调试信息开关处于关闭状态。

表2-1 debugging ipv6 urpf命令输出信息描述表

字段

描述

uRPF6  uRPF6-Discard: Packet from *ipv6-address* via *interface-type interface-number*

从指定接口收到的源地址为*ipv6-address*的报文被丢弃

uRPF6  uRPF6-Discard-Suppress: Packet from *ipv6-address* via *interface-type interface-number*

从指定接口收到的源地址为*ipv6-address*的报文被IPv6 uRPF抑制后，匹配IPv6 ACL规则成功，然后被转发

【举例】

\# 在一台启动了IPv6 uRPF调试信息开关的设备上，收到源地址不可识别的报文，则打印以下调试信息。

\<Sysname\>debugging ipv6 urpf{.TerminalDisplayChar}

\*0.3933516 Sysname URPF6/7/debug_info:

 uRPF6 uRPF6-Discard: Packet from 2000::5 via GigabitEthernet1/0/1

*// 从接口GigabitEthernet1/0/1收到的源地址为2000::5的报文被丢弃*
