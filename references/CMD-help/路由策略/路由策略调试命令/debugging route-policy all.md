
**路由策略 \-- 路由策略调试命令 \-- debugging route-policy all**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **all**]

**[undo debugging route-policy** **all**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy all**]命令打开路由策略所有调试信息开关。**undo debugging route-policy all**命令用来关闭路由策略所有调试信息开关。

缺省情况下，路由策略所有调试开关处于关闭状态。

【举例】

\# 打开路由策略所有调试信息调试开关。

\<Sysname\> debugging route-policy all

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy as-path**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **as-path**]

**[undo debugging route-policy** **as-path**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy as-path**]命令用来打开路由策略中AS路径过滤列表相关的调试信息开关。**undo debugging route-policy as-path**用来关闭路由策略中AS路径过滤列表相关的调试信息开关。

缺省情况下，路由策略中AS路径过滤列表相关的调试信息开关处于关闭状态。

表1-1 debugging route-policy as-path命令输出信息描述表

字段

描述

Check aspath

检查AS路径过滤列表

result

匹配结果

Aspath

进行匹配的AS路径属性

【举例】

\# 打开路由策略中AS路径过滤列表相关的调试信息开关。

\<Sysname\> debugging route-policy as-path

\*Feb  1 14:07:58:645 2012 Sysname RPM/7/BGP-DEBUG: -MDC=1;

Check aspath 20, result:permit, Aspath:1 20 30 40 44 158 280

*// 检查编号为20的AS路径过滤列表，匹配asapth路径属性：1 20 30 40 44 158 280，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy community**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **community**]

**[undo debugging route-policy** **community**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy community**]命令用来打开路由策略中团体属性列表相关的调试信息开关。**undo debugging route-policy community**用来关闭路由策略中团体属性列表相关的调试信息开关。

缺省情况下，路由策略中团体属性列表相关的调试信息开关处于关闭状态。

表1-2 debugging route-policy community命令输出信息描述表

字段

描述

Check community

检查团体属性，团体属性名或者为数字型或者为名字型，输出形式为：数字型名字型，数字值为0时不支持路由过滤，数字值为1时支持路由过滤

ucFlag

表示是否进行确切匹配，对应if-match命令中的whole-match关键字，为1表示非确切匹配，为2表示确切匹配

result

匹配结果

Community

进行匹配的community属性

【举例】

\# 打开路由策略中团体属性列表相关的调试信息开关。

\<Sysname\> debugging route-policy community

\*Feb  1 13:38:09:737 2012 Sysname RPM/7/BGP-DEBUG: -MDC=1;

Check community 1[NULL, ucFlag:2, result:permit, Community:0 1 3 4 5 6 7 8 9 10]

 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 4294967041 4294967043

*// 检查序号为1的团体属性列表，匹配community路径属性:0 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 // 20 21 22 23 24 25 26 27 28 29 4294967041 4294967043，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy ext-community**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **ext-community**]

**[undo debugging route-policy** **ext-community**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy ext-community**]命令用来打开路由策略中扩展团体属性列表相关的调试信息开关。**undo debugging route-policy ext-community**用来关闭路由策略中扩展团体属性列表相关的调试信息开关。

缺省情况下，路由策略中扩展团体属性列表相关的调试信息开关处于关闭状态。

表1-3 debugging route-policy ext-community命令输出信息描述表

字段

描述

Check extcommunity

检查扩展团体属性列表

result

匹配结果

ExtComms

进行匹配的扩展团体属性

【举例】

\# 打开路由策略中扩展团体属性列表相关的调试信息开关。

\<Sysname\> debugging route-policy ext-community

\*Feb  1 13:25:34:023 2012 Sysname RPM/7/BGP-DEBUG: -MDC=1;

Check extcommunity 1, result:permit, ExtComms:

rt 65535:65535 rt 0.0.0.0:0

*// 检查序号为1的扩展团体属性列表，匹配扩展团体属性：rt 65535:65535 rt 0.0.0.0:0，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy ip-prefix4**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **ip-prefix4**]

**[undo debugging route-policy** **ip-prefix4**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy ip-prefix4**]命令用来打开路由策略中IPv4前缀列表相关的调试信息开关。**undo debugging route-policy ip-prefix4**用来关闭路由策略中IPv4前缀列表相关的调试信息开关。

缺省情况下，路由策略中IPv4前缀列表相关的调试信息开关处于关闭状态。

表1-4 debugging route-policy ip-prefix4命令输出信息描述表

字段

描述

Check addr/len *x.x.x.x/xx* in prefix-list

检查IPv4前缀列表，*x.x.x.x/xx*表示IPv4地址前缀和掩码

result

匹配结果

【举例】

\# 打开路由策略中IPv4前缀列表相关的调试信息开关。

\<Sysname\> debugging route-policy ip-prefix4

\*Apr 29 00:19:00:127 2012 Sysname RPM/7/OSPF-DEBUG: -MDC=1;

Check addr/len 1.1.1.1/32 in prefix-list prefix, result:permit

*// 检查IPv4前缀列表prefix，匹配前缀1.1.1.1/32，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy ip-prefix6**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **ip-prefix6**]

**[undo debugging route-policy** **ip-prefix6**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy** **ip-prefix6**]命令用来打开路由策略中IPv6前缀列表相关的调试信息开关。** undo debugging route-policy ip-prefix6**命令用来关闭路由策略中IPv6前缀列表相关的调试信息开关。

缺省情况下，路由策略中IPv6前缀列表相关的调试信息开关处于关闭状态。

表1-5 debugging route-policy ip-prefix6命令输出信息描述表

字段

描述

Check addr/len *x::x/xx* in prefix-list

检查IPv6前缀列表，*x::x/xx*表示IPv6地址前缀和前缀长度

result

匹配结果

【举例】

\# 打开路由策略中IPv6前缀列表相关的调试信息开关。

\<Sysname\> debugging route-policy ip-prefix6

\*Apr 29 00:20:43:976 2012 Sysname RPM/7/RIB-DEBUG: -MDC=1;

Check addr/len 1::1/64 in prefix-list prefix, result:permit

*// 检查IPv6前缀列表prefix，匹配前缀1::1/64，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy mac-list**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **mac-list**]

**[undo debugging route-policy** **mac-list**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy mac-list**]命令用来打开路由策略中MAC地址列表过滤器的调试信息开关。**undo debugging route-policy mac-list**用来关闭路由策略中MAC地址列表过滤器的调试信息开关。

缺省情况下，路由策略中MAC地址列表过滤器的调试信息开关处于关闭状态。

表1-6 debugging route-policy mac-list命令输出信息描述表

字段

描述

Check MAC addr H-H-H in mac-list

检查MAC地址，H-H-H表示MAX地址

result

匹配结果

【举例】

\# 打开路由策略中MAC地址列表过滤器的调试信息开关。

\<Sysname\> debugging route-policy mac-list

\*Nov 21 17:21:01:459 2012 Sysname RPM/7/STATIC-DEBUG: -MDC=1;

Check MAC address 0001-0001-0001 in mac-list policy, result: permit

*// 检查MAC地址列表policy，匹配MAC地址0001-0001-0001，匹配结果为通过*

**路由策略 \-- 路由策略调试命令 \-- debugging route-policy policy**

------------------------------------------------------------------------

【命令】

**[debugging route-policy** **policy**]

**[undo debugging route-policy** **policy**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

无

【描述】

**[debugging route-policy policy**]命令用来打开路由策略中policy过滤器的调试信息开关。**undo debugging route-policy policy**用来关闭路由策略中policy过滤器的调试信息开关。

缺省情况下，路由策略中policy过滤器的调试信息开关处于关闭状态。

表1-7 debugging route-policy policy命令输出信息描述表

字段

描述

Check  *xxx*  in policyName

检查路由策略

prefix/len

前缀/前缀长度信息

nexthop

下一跳

neighbour

邻居IP地址

Comm

团体属性

ExtComm

扩展团体属性

Aspath

AS路径过滤列表属性

Local-prefer

本地优先级

Metric

开销值

Tag

标签值

ProtoId

协议ID

SubprotoId

子协议ID

Label

MPLS Label

VrfIndex

VPN索引

ifIndex

接口索引

ProcId

进程ID

Flag

忽略标志

result

匹配结果

【举例】

\# 打开路由策略中policy过滤器的调试信息开关。

\<Sysname\> debugging route-policy policy

\*Apr 29 00:19:00:127 2012 Sysname RPM/7/OSPF-DEBUG: -MDC=1;

Check prefix/len 1.0.0.0/8, nexthop 0.0.0.0, neighbour 0.0.0.0, Comm:NULL, ExtComm:NULL, Aspath:NULL,  Local-prefer:0, Metric:0, Tag:0, ProtoId:2, SubprotoId:0, Label:4294967295, VrfIndex:0, ifIndex:2151f, ProcId:0, Flag:0x0 in policyName policy, result:deny

*// 使用路由策略policy匹配路由，匹配结果为不通过，路由属性为：prefix/len 1.0.0.0/8, nexthop 0.0.0.0, neighbour 0.0.0.0, Comm:NULL, ExtComm:NULL, Aspath:NULL,  Local-prefer:0, Metric:0, Tag:0, ProtoId:2, SubprotoId:0, Label:4294967295, VrfIndex:0, ifIndex:2151f, ProcId:0, Flag:0x0*

