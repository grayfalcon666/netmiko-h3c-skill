
**负载均衡 \-- 负载均衡配置命令 \-- ap radio**

------------------------------------------------------------------------

**[ap radio**]命令用来将指定的Radio加入到负载均衡组中。

**[undo ap**]命令用来删除负载均衡组中的Radio。

【命令】

**[ap ***ap-name*** radio** *radio-number*]

**[undo ap **{ *ap-name* [ **radio** *radio-number*  \| **all** }]]

【缺省情况】

负载均衡组中不存在任何AP的Radio。

【视图】

负载均衡组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ap-name*]：加入负载均衡组的AP名称。为1～32个字符的字符串，不区分大小写。加入负载均衡组的AP必须已经存在。

*[radio-number*]：将AP的radio编号加入负载均衡组。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：删除负载均衡组中所有的Radio。

【使用指导】

·一个Radio只能加入一个负载均衡组。

·删除负载均衡组中的Radio时，如果使用**undo ap** *ap-name*命令（即不指定**radio*** radio-number*参数时），表示删除负载均衡组中指定AP的所有Radio。

【举例】

\# 将ap1的第2个Radio加入到ID为10的负载均衡组中。

\<Sysname\> system-view

Sysname wlan load-balance group 10

Sysname-wlan-lb-group-10 ap ap1 radio 2

**负载均衡 \-- 负载均衡配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来配置负载均衡组的描述信息。

**[undo description**]命令用来删除负载均衡组的描述信息。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

负载均衡组没有描述信息。

【视图】

负载均衡组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：负载均衡组的描述信息，为1～64个字符的字符串，区分大小写。

【举例】

\# 配置负载均衡组10的描述信息为marketing。

\<Sysname\> system-view

Sysname wlan load-balance group 10

Sysname-wlan-lb-group10 description marketing

**负载均衡 \-- 负载均衡配置命令 \-- display wlan load-balance group**

------------------------------------------------------------------------

**[display wlan load-balance group**]命令用来显示负载均衡组的当前配置信息。

【命令】

**[display wlan load-balance group **[{ *group-id* \| **all** }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-id*]：负载均衡组的ID。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：显示所有负载均衡组的配置。

【举例】

\# 显示组号为1的负载均衡组配置信息。

\<Sysname\> display wlan load-balance group 1

                  WLAN load balance group information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Group ID                : 1

Description             :

Group members           : ap3-radio2,

                          ap2-radio1,

                          ap1-radio1,

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\# 显示所有负载均衡组配置信息。

\<Sysname\> display wlan load-balance group all

                  WLAN load balance group information

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Group ID                : 1

Description             :

Group members           : ap3-radio2,

                          ap2-radio1,

                          ap1-radio1,

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Group ID                : 2

Description             : marketing

Group members           : ap3-radio1,

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

表1-1 display wlan load-balance group命令显示信息描述表

字段

描述

Group ID

负载均衡组ID

Description

负载均衡组描述信息

Group members

负载均衡组内的Radio列表

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance access-denial**

------------------------------------------------------------------------

**[wlan load-balance access-denial**]命令用来配置拒绝客户端关联请求的最大次数。

**[undo wlan load-balance access-denial**]命令用来恢复缺省情况。

【命令】

**[wlan load-balance access-denial** *access-denial*]

**[undo wlan load-balance access-denial**]

【缺省情况】

拒绝客户端关联请求的最大次数为10。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[access-denial*]：拒绝客户端关联请求的最大次数，取值范围为2～10。

【使用指导】

如果客户端反复向某个Radio发起关联请求，且Radio拒绝客户端关联请求次数达到设定的最大拒绝关联请求次数，那么该Radio会认为此时该客户端不能连接到其它任何的Radio，在这种情况下， Radio会接受该客户端的关联请求。

【举例】

\# 配置设备拒绝客户端关联请求的最大次数为4。

\<Sysname\> system-view

Sysname wlan load-balance access-denial 4

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance enable**

------------------------------------------------------------------------

**[wlan load-balance enable**]命令用来开启负载均衡功能。

**[undo wlan load-balance enable**]命令用来关闭负载均衡功能。

【命令】

**[wlan load-balance enable**]

**[undo wlan load-balance enable**]

【缺省情况】

负载均衡功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启负载均衡功能。

\<Sysname\> system-view

Sysname wlan load-balance enable

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance group**

------------------------------------------------------------------------

**[wlan load-balance group**]命令用来创建负载均衡组。

**[undo wlan load-balance group**]命令用来删除指定或所有的负载均衡组。

【命令】

**[wlan load-balance group ***group-id*]

**[undo wlan load-balance group ***[group-id***[ \| all ]**}]

【缺省情况】]

不存在负载均衡组。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-id*]：负载均衡组的ID。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[all**]：删除所有的负载均衡组。

【使用指导】

创建负载均衡组后，AC将以负载均衡组为单位，在各个组内的Radio间进行会话模式、流量模式或带宽模式的负载均衡，没有加入到任何负载均衡组的Radio不会参与负载均衡。

【举例】

\# 创建ID为10的负载均衡组。

\<Sysname\> system-view

Sysname wlan load-balance group 10

Sysname-wlan-lb-group-10

【相关命令】

·**ap radio**

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode bandwidth**

------------------------------------------------------------------------

**[wlan load-balance mode bandwidth**]命令用来配置负载均衡模式为带宽模式。

**[undo wlan load-balance mode**]命令用来恢复缺省情况。

【命令】

**[wlan load-balance mode bandwidth ***value* [ **gap** *gap-value* ]]

**[undo wlan load-balance mode**]

【视图】

系统视图

【缺省情况】

负载均衡模式为会话模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：带宽门限值，取值范围为1～500，单位为Mbps，缺省值为40Mbps。

*[gap-value*]：带宽差值门限值，取值范围为1～200，单位为Mbps，缺省值为20Mbps。带宽差值即当前Radio上的带宽与同一AC内其他Radio上的带宽最小者的差值。

【使用指导】

当Radio上的带宽达到/超过带宽门限值并且与同一AC内其他Radio上的带宽最小者的差值达到/超过带宽差值门限值，Radio开始运行负载均衡。

【举例】

\# 配置负载均衡模式为带宽模式，带宽门限值为100Mbps，带宽差值门限值为20Mbps。

\<Sysname\> system-view

Sysname wlan load-balance mode bandwidth 100 gap 20

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode session**

------------------------------------------------------------------------

**[wlan load-balance mode session**]命令用来配置负载均衡模式为会话模式。

**[undo wlan load-balance mode**]命令用来恢复缺省情况。

【命令】

**[wlan load-balance mode session** *value* [ **gap** *gap-value* ]]

**[undo wlan load-balance mode**]

【缺省情况】

负载均衡模式为会话模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：会话门限值，取值范围为1～40，缺省值为20。

*[gap-value*]：会话差值门限值，取值范围为1～8，缺省值为4。会话差值即当前Radio上的在线客户端数量与同一AC内其他Radio上的在线客户端数量最小者的差值。

【使用指导】

当Radio上的在线客户端数量达到/超过会话门限值并且与同一AC内其他Radio上的在线客户端数量最小者的差值达到/超过会话差值门限值，Radio开始运行负载均衡。

【举例】

\# 配置负载均衡模式为会话模式，会话门限值为7，会话差值门限值为5。

\<Sysname\> system-view

Sysname wlan load-balance mode session 7 gap 5

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance mode traffic**

------------------------------------------------------------------------

**[wlan load-balance mode traffic**]命令用来配置负载均衡模式为流量模式。

**[undo wlan load-balance mode**]命令用来恢复缺省情况。

【命令】

**[wlan load-balance mode traffic** *value* [ **gap** *gap-value* ]]

**[undo wlan load-balance mode**]

【缺省情况】

负载均衡模式为会话模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：流量门限值，该参数表示Radio上的数据流量占Radio最大支持带宽的百分比数值，取值范围为1～80，缺省值为30。

*[gap-value*]：流量差值门限值，该参数表示流量差值占Radio最大支持带宽的百分比数值，取值范围为10～40，缺省值为20。流量差值即当前Radio上的数据流量与同一AC内其他Radio上的流数据量最小者的差值。

【使用指导】

当Radio上的流量达到/超过流量门限值并且与同一AC内其他Radio上的流量最小者的差值达到/超过流量差值门限值，Radio开始运行负载均衡。

【举例】

\# 配置负载均衡模式为流量模式，流量门限值为占Radio最大支持带宽的25%，流量差值门限值为占Radio最大支持带宽的20%。

\<Sysname\> system-view

Sysname wlan load-balance mode traffic 25 gap 20

**负载均衡 \-- 负载均衡配置命令 \-- wlan load-balance rssi-threshold**

------------------------------------------------------------------------

**[wlan load-balance rssi-threshold**]命令用来配置负载均衡RSSI门限。

**[undo wlan load-balance rssi-threshold**]命令用来恢复缺省情况。

【命令】

**[wlan load-balance rssi-threshold** *rssi-threshold*]

**[undo wlan load-balance rssi-threshold**]

【缺省情况】

负载均衡RSSI门限值为25。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rssi-threshold*]：负载均衡RSSI门限值，取值范围为5～100。

【使用指导】

如果Radio检测到客户端的RSSI值低于设定值，则该Radio将判定该客户端没有被检测到。如果只有过载的Radio可以检测到某客户端，则即使该Radio已经过载，也会通过减少该客户端的最大拒绝关联请求次数，增大该客户端接入的概率。

【举例】

\# 配置负载均衡RSSI门限值为40。

\<Sysname\> system-view

Sysname wlan load-balance rssi-threshold 40

