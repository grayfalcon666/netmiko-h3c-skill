
**业务环回组 \-- 业务环回组Probe命令 \-- display system internal service-loopback running**

------------------------------------------------------------------------

**[display system internal service-loopback running**]命令用来显示业务环回组的运行数据。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal service-loopback running**]** group ***group-number***slot***slot-number*

分布式设备－IRF模式：

**[display system internal service-loopback running **]**group ***group-number*** chassis***chassis-number***slot***slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[group ***group-number*]：显示指定环回组的信息，取值范围为1～1024。

**[slot**]*slot-mumber*：显示指定单板的业务环回组信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]*slot-mumber*：显示指定成员设备的业务环回组信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**]*chassis-number***slot***slot-number*：表示成员设备上指定单板的业务环回组信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

该命令可以用于了解当前系统指定业务环回组在各板的运行状态和驱动信息，方便定位与驱动配合的问题和分布式环境下各板信息不一致的问题。

**业务环回组 \-- 业务环回组Probe命令 \-- display system internal service-loopback interface-list**

------------------------------------------------------------------------

**[display system internal service-loopback interface-list**]命令用来显示接口事件处理队列节点信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal service-loopback interface-list slot**]*slot-number*

分布式设备－IRF模式：

**[display system internal service-loopback interface-list**]**chassis***chassis-number*** slot***slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**]*slot-mumber*：表示指定单板的接口事件队列信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]*slot-mumber*：显示指定成员设备的接口事件队列信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis**]*chassis-number***slot***slot-number*：表示成员设备上指定单板的接口事件队列信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

该命令用于定位接口事件处理过程中出现的时序问题。

