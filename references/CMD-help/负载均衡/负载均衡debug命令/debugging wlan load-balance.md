
**负载均衡 \-- 负载均衡debug命令 \-- debugging wlan load-balance**

------------------------------------------------------------------------

【命令】

**[debugging wlan load-balance**[ { **all** \| **error** \| **event** \| **timer** }]]

**[undo debugging wlan load-balance**[ { **all** \| **error** \| **event** \| **timer** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示WLAN负载均衡所有调试信息开关。

**[error**]：表示WLAN负载均衡错误调试信息开关。

**[event**]：表示WLAN负载均衡事件调试信息开关。

**[timer**]：表示WLAN负载均衡定时器调试信息开关。

【描述】

**[debugging wlan load-balance**]命令用来打开WLAN负载均衡调试信息开关。

**[undo debugging wlan load-balance**]命令用来关闭WLAN负载均衡调试信息开关。

缺省情况下，WLAN负载均衡调试信息开关处于关闭状态。

表1-1 debugging wlan load-balance error命令输出信息描述表

字段

描述

Failed to get WLB radio information.

获取WLB模块radio数据失败

Failed to save WLB global configuration to DBM.

将WLB模块全局配置数据保存到DBM失败

Failed to save WLAN load balancing group configuration to DBM.

将WLB模块无线负载均衡组配置保存到DBM失败

APID: *apid*

AP ID信息

RADIOID: *radioid*

Radio ID信息

MAC: *mac-address*

station的MAC地址

APID: *apid* RADIOID: *radioid* MAC: *mac-address* Failed to reject the station when loads were not balanced.

负载不均衡时，拒绝station连接失败

Failed to change the load balancing mode from session mode to traffic or bandwidth mode.

无线负载均衡模式由会话模式改变为流量模式或者带宽模式初始化失败

Failed to enable WLB: Configuration thread initialization failure.

无线负载均衡开启时配置线程初始化失败

Failed to enable WLB: Service thread initialization failure.

无线负载均衡开启时业务线程初始化失败

Failed to update probe mask in WLB.

更新无线负载均衡probe mask失败

Global neighbor station hash table is empty.

全局邻居station的哈希表为空

MAC*: mac-address* Failed to identify whether valid neighbor radio existed for the station.

检查是否存在有效的邻居radio失败

表1-2 debugging wlan load-balance event命令输出信息描述表

描述

字段

Failed to add neighbor station to hash table: Not enough memory space.

内存不足，创建邻居station哈希表失败

APID: *apid*

AP的ID信息

RADIOID: *radioid*

Radio的ID信息

MAC: *mac-address*

station的MAC地址

MAC: *mac-address*  The station already existed in global neighbor station hash table.

邻居station哈希表中已经存在station

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio was added to neighbor radio list.

radio被添加到邻居radio链表中

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio was updated to neighbor radio list.

radio被更新到邻居radio链表

MAC: *mac-address* Created global neighbor station node.

创建全局邻居station节点

MAC: *mac-address* The station was added to global neighbor station hash table.

station被添加到全局邻居station哈希表中

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio was deleted from neighbor radio list: Aging time expired.

station达到老化时间，radio被从邻居radio链表中删除

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio was deleted from neighbor radio list: Radio went offline.

由于radio下线，radio被从邻居radio链表中删除

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio is in load balanced state.

radio当前为负载均衡状态

MAC: *mac-address* The station has no valid neighbor radios.

station无有效的邻居radio

APID: *apid* RADIOID: *radioid* The radio is in load balanced state: It is not in any load balancing group.

AC上存在负载均衡组，但是radio不在任何负载均衡组内，则本radio负载是均衡的

APID: *apid* RADIOID: *radioid* The radio is in load balanced state: Its load didn\'t exceed the gap value.

radio是负载均衡的，因为其负载未超过配置的差值门限

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The radio is in load unbalanced state.

radio当前为负载不均衡状态

APID: *apid* RADIOID: *radioid* The radio was added to global radio load hash table.

radio被添加到全局radio负载哈希表

APID: *apid* RADIOID: *radioid* The radio was deleted from global radio load hash table.

radio被从全局radio负载哈希表中删除

APID: *apid* RADIOID: *radioid*  MAC: *mac-address* The station was deleted from retry station hash table.

station的retry节点被从retry station哈希表中删除

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was added to retry station hash table.

station被添加到retry station哈希表中

MAC: *mac-address* The neighbor radio list is empty.

station的邻居radio链表为空

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was deleted from global neighbor station hash table.

station被从全局邻居station哈希表中删除

APID: *apid* RADIOID: *radioid* MAC: *mac-address* Successfully rejected the association request of the station when the radio was in load unbalanced state.

当radio负载不均衡时，拒绝station连接成功

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was permitted: Its association attempts reached the upper limit.

因为station连接达到最大次数，所以允许其连接radio

Changed the load balancing mode from session mode to traffic mode or bandwidth mode.

无线负载均衡模式由会话模式改变为流量模式或者带宽模式

Changed the load balancing mode from traffic or bandwidth mode to session mode.

无线负载均衡模式由流量模式或者带宽模式改变为会话模式

Changed the load balancing mode between traffic mode and bandwidth mode.

无线负载均衡在流量模式或者带宽模式间转变

Reset probe mask for all radios when the load balancing mode was changed.

当无线负载均衡模式改变时重置所有radio的probe mask标志位

MAC: *mac-address* Display the station\'sneighbor radio list:

显示station的邻居radio列表信息

APID: *apid* RADIOID: *radioid* The group ID and load of the radio are *GroupID* and *radio-load*.

radio所在无线负载均衡组ID为*GroupID*，当前负载信息为*radio-load*

MAC: *mac-address* The station is a roaming station.

station为漫游客户端

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was added to radio neighbor station hash table.

邻居station节点添加到radio下的邻居station哈希表

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was deleted from radio neighbor station hash table.

邻居station节点从radio下的邻居station哈希表中删除

MAC: *mac-address*The station\'s RSSI *RSSI-value* is lower than the RSSI threshold *RSSI-cfg*.

station的RSSI值*RSSI-value*小于RSSI门限值*RSSI-cfg*

APID: *apid* RADIOID: *radioid* MAC: *mac-address* The station was refused *refuse-times* times.

station被无线负载均衡功能拒绝连接次数达到* refuse-times*次

WLB was enabled.

无线负载均衡模块开启

WLB was disabled.

无线负载均衡模块关闭

APID: *apid* RADIOID: *radioid* The radio between the current traffic load and the max throughput of the radio is *load-value.*

radio当前负载的流量占radio支持的最大吞吐率的百分比为*load-value*

APID: *apid* RADIOID: *radioid* The current bandwidth of the radio is *load-value* Mbps.

radio的当前负载的带宽值为load-value Mbps

APID:*apid* RADIOID:*radioid* Successfully updated probe mask to hide probe response.

WLB模块成功更新probe mask至隐藏probe response状

APID:*apid* RADIOID:*radioid* Successfully updated probe mask to answer probe response.

WLB模块成功更新probe mask至应答probe response状态

表1-3 debugging wlan load-balance timer命令输出信息描述表

字段

描述

Successfully created traffic load balancing timer.

创建无线负载均衡流量定时器成功

Failed to create traffic load balancing timer.

创建无线负载均衡流量定时器失败

Failed to create retry station aging timer.

创建retry station老化定时器失败

MAC *mac-address* Failed to create global neighbor station aging timer.

创建全局邻居station老化定时器失败

MAC *mac-address* Successfully created global neighbor station aging timer.

创建全局邻居station老化定时器成功

【举例】

\# 打开WLAN负载均衡事件调试信息开关,使能WLAN负载均衡。

\<System\> debugging wlan load-balance event

\<Sysname\> system-view

Sysname wlan load-balance enable

\*Sep 11 09:33:10:120 2014 H3C STAMGR/7/Event: WLB was enabled.

*// 开启无线负载均衡成功*

\# 打开WLAN负载均衡错误调试信息开关，使能WLAN负载均衡，初始化失败。

\<System\> debugging wlan load-balance error

\<Sysname\> system-view

Sysname wlan load-balance enable

\*Sep 11 09:33:11:120 2014 H3C STAMGR/7/Event**:** Failed to enable WLB: Configuration thread initialization failure.

*// 配置线程初始化失败，故开启WLAN负载均衡失败*

\# 打开WLAN负载均衡定时器调试信息开关，切换模式到流量模式。

\<System\> debugging wlan load-balance timer

\<Sysname\> system-view

Sysname wlan load-balance mode traffic 20

\*Sep 11 09:33:11:120 2014 H3C STAMGR/7/Timer**:** Successfully created traffic-mode load balancing timer.

*// 切换WLAN负载均衡模式到流量模式，创建定时器成功*

