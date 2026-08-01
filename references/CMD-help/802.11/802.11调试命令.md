<!-- CMD-INDEX
  debugging dot11 packet              | 用户视图             | L5
-->

**802.11 \-- 802.11调试命令 \-- debugging dot11 packet**

------------------------------------------------------------------------

![说明](802.11%20Debug.files/image001.png)

本命令的支持情况与设备型号有关，请以设备的实际情况为准。

【命令】

**[debugging dot11 packet**]

**[undo debugging dot11** **packet**]

【视图】

用户视图

【参数】

无

【描述】

**[debugging dot11** **packet**]命令用来打开802.11协议报文监听的调试信息开关。**undo debugging dot11** **packet**命令用来关闭802.11协议报文监听的调试信息开关。

缺省情况下，802.11协议报文监听的调试信息开关处于关闭状态。

表1-1 debugging dot11 packet命令输出信息描述表

字段

描述

DOT11_moniter: Matched  a 802.11 protocol packet

特征匹配到一个802.11协议报文

Action: *action*

特征对报文的处理动作，有以下处理方式：

·Forward：继续转发

·Redirect：重定向

·Copy：复制

Characteristics flag: x

特征有效字段标记，用16进制格式打印

Priority: *priority*

特征的优先级，数值越大优先级越高

Phase: *phase*

特征的侦听阶段，有以下几个阶段：

·Radio_Recv：Radio入方向侦听阶段

·BSS_Recv：BSS入方向侦听阶段

·BSS_Send：BSS出方向侦听阶段

Context0

特征上下文

Context1

特征上下文

【举例】

\# 在设备上打开802.11协议报文监听的调试信息开关。

\<Sysname\> debugging dot11 packet

\*Dec 8 09:58:04:957 2013 Sysname DOT11/7/DOT11_moniter: Matched a 802.11 protocol packet, Action: Redirect, Characteristics flag: 0x8000, Priority: 64, Phase: BSS_Recv, Context[0: 0x0, Context1: 0x1]

*// 匹配到一个符合802.11特征的报文，特征序列号为1，优先级为64，报文特征地址有效字段为0x8000，对报文的处理动作为重定向。*
