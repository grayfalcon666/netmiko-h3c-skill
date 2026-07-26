
**多机备份 \-- IPoE支持多机备份Probe功能 \-- display system internal ip subscriber cache statistics**

------------------------------------------------------------------------

**[display system internal ip subscriber cache statistics**]命令用来显示多机备份环境下缓存的IPv4 IPoE用户统计信息。

【命令】

**[display system internal ip subscriber cache statistics** [ **vsrp-instance** *instance-name* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsrp-instance*** instance-name*]：表示多机备份实例名，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有多机备份实例的IPv4 IPoE用户统计信息。

**多机备份 \-- IPoE支持多机备份Probe功能 \-- display system internal ipv6 subscriber cache statistics**

------------------------------------------------------------------------

**[display system internal ip subscriber cache statistics**]命令用来显示多机备份环境下缓存的IPv6 IPoE用户统计信息。

【命令】

**[display system internal ipv6 subscriber cache statistics** [ **vsrp-instance** *instance-name* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsrp-instance*** instance-name*]：表示多机备份实例名，为1～31个字符的字符串，区分大小写。如果未指定本参数，将显示所有多机备份实例的IPv6 IPoE用户统计信息。

**多机备份 \-- PPPoE支持多机备份Probe命令 \-- display system internal ppp sync-session**

------------------------------------------------------------------------

**[display system internal ppp sync-session**]命令用来显示设备上PPP记录的未关联的会话信息。

【命令】

**[display system internal ppp sync-session** [ **vsrp-instance** *vsrp-instance-name* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vsrp-instance***vsrp-instance-name*]：显示PPP记录的指定多机备份实例的未关联会话信息。*vsrp-instance-name*表示多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，将显示PPP记录的所有多机备份实例的未关联会话信息。

【使用指导】

PPPoE会话和PPP会话独立进行同步。当PPP会话和PPPoE会话数据同步到备用设备上以后，由PPP完成PPPoE同步会话与PPP同步会话的关联。

·如果PPPoE会话先于PPP会话同步到备用设备上，PPP就把PPPoE会话信息先保存起来（此时PPPoE会话就是未关联的会话），等待PPP会话同步数据到达以后再进行会话的关联。

·如果PPP会话先于PPPoE会话同步到备用设备上，PPP就把PPP会话先保存起来（此时PPP会话就是未关联的会话），等待PPPoE会话同步数据到达以后再进行会话的关联。

本命令用于显示未关联的会话信息。
