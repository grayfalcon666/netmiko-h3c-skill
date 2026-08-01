<!-- CMD-INDEX
  debugging ip address event          | 用户视图             | L5
-->

**IP地址 \-- IP地址调试命令 \-- debugging ip address event**

------------------------------------------------------------------------

【命令】

**[debugging ip address event**]

**[undo debugging ip address event**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【描述】

**[debugging ip address event**]命令用来打开IP地址事件的调试开关。**undo debugging ip address event**命令用来关闭IP地址事件的调试开关。

缺省情况下，IP地址事件的调试信息开关处于关闭状态。

表1-1 debugging ip address event命令输出信息描述表

字段

描述

module

被通知的模块ID

IP

IP地址

Mask

掩码

Type

地址类型，取值如下：

·0x0：无

·0x1：手动配置的主地址

·0x8：通过DHCP分配

·0x10：通过BOOTP分配

·0x20：通过协商得到

·0x80：手动配置的从地址

·0x200：借用其他接口

·0x800：VRRP地址

·0x1000：MAD地址

·0x2000：SSLVPN虚接口的地址

·0x4000：集群地址

·0x40000：内部环回地址

·0x100000：mtunnel地址

·0x200000：本地NAT地址

·0x400000：本地NATPT地址

·0x800000：本地LB地址

·0x10000000：引入的主机地址

·0x20000000：引入的NAT主机地址

·0x40000000：引入的LB主机地址

State

地址状态，取值如下：

·0x1：可用

·0x2：不可用

【举例】

\# 在设备上配置IP地址事件的调试信息开关，配置接口GigabitEthernet 1/0/1的IP地址为2.1.1.1，掩码为24位。

[\<Sysname\> ]{.TerminalDisplayshading}[[debugging ip address event]]{.TerminalDisplayshading}

\<Sysname\> system-view{.TerminalDisplayshading}

[Sysname]{.TerminalDisplayshading}{.TerminalDisplayshading}interface {.TerminalDisplayshading}gigabite{.TerminalDisplayshading}thernet{.TerminalDisplayshading}1/{.TerminalDisplayshading}0/{.TerminalDisplayshading}1{.TerminalDisplayshading}

[Sysname-]{.TerminalDisplayshading}[[Gigabit]]{.TerminalDisplayshading}[[Ethernet]]{.TerminalDisplayshading}[[1/]]{.TerminalDisplayshading}[[0/]]{.TerminalDisplayshading}[[1]]{.TerminalDisplayshading}[[ip address 2.1.1.1 24]]{.TerminalDisplayshading}

[Sysname-]{.TerminalDisplayshading}[[Gigabit]]{.TerminalDisplayshading}[[Ethernet]]{.TerminalDisplayshading}[[1/]]{.TerminalDisplayshading}[[0/]]{.TerminalDisplayshading}[[1]]{.TerminalDisplayshading}[[]]{.TerminalDisplayshading}

\*{.TerminalDisplayshading}Dec{.TerminalDisplayshading}{.TerminalDisplayshading}3{.TerminalDisplayshading} 15:13:01:182 2012 Sysname {.TerminalDisplayshading}IPADDR{.TerminalDisplayshading}/7/{.TerminalDisplayshading}EVENT{.TerminalDisplayshading}: -MDC=1;{.TerminalDisplayshading}

IP address add event notified to module 0x04030000,{.TerminalDisplayshading}

IP: 2.1.1.1, Mask: 255.255.255.0, Type: 0x1, State: 0x1, {.TerminalDisplayshading}

V{.TerminalDisplayshading}PN Index: 0, Interface: {.TerminalDisplayshading}Gigabit{.TerminalDisplayshading}Ethernet{.TerminalDisplayshading}1/{.TerminalDisplayshading}0/{.TerminalDisplayshading}1{.TerminalDisplayshading}

