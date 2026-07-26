
**预配置 \-- 预配置命令 \-- slot**

------------------------------------------------------------------------

![说明](预配置命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[slot**]命令用来进入slot视图。

【命令】

集中式设备/分布式设备－独立运行模式/集中式IRF设备：

**[slot ***slot-number*]

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[slot-number*]：表示子卡所在的槽位号。（集中式设备）

*[slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

*[slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

*[slot-number*]：表示设备在IRF中的成员编号或PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

【使用指导】

进入slot视图后，可以开启该slot的预配置功能。

【举例】

\# 进入slot 2的视图。

\<Sysname\> system-view

sysname slot 2

【相关命令】

·**provision**

**预配置 \-- 预配置命令 \-- chassis slot**

------------------------------------------------------------------------

![说明](预配置命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[chassis slot**]命令用来进入slot视图。

【命令】

**[chassis** *chassis-number*]{.CommandChar}**slot** *slot-number*

【视图】

系统视图

【缺省用户角色】

network-admin

【参数】

*[chassis-number*]{.CommandChar}**slot** *slot-number*：表示单板在IRF中的位置。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

*[chassis-number*]{.CommandChar}**slot** *slot-number*：表示单板或PEX在IRF中的位置。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

【举例】

\# 进入chassis 1 slot 2的视图。

\<Sysname\> system-view

sysname chassis 1 slot 2

Sysname-chassis-1-slot-2

【相关命令】

·**provision**

**预配置 \-- 预配置命令 \-- provision**

------------------------------------------------------------------------

**[provision**]命令用来开启指定业务板/PEX设备/子卡的预配置功能。

**[undo provision**]命令用来关闭指定业务板/PEX设备/子卡的预配置功能。

【命令】

**[provision ** **subslot** *sunslot-number* ] **model** *model*

**[undo provision ** **subslot** *sunslot-number* ] **model**

【缺省情况】

预配置功能处于关闭状态。

【视图】

slot视图

【缺省用户角色】

network-admin

【参数】

**[subslot ***subslot-number*]：用来开启子卡的预配置功能。*subslot-number*表示子卡所在的子槽位号。不指定该参数，表示开启单板的预配置功能。只有先开启单板的预配置功能，并且该单板支持子卡，才能帮助出*subslot-number*的取值，才能开启子卡的预配置功能。

**[model ***model*]：表示设备支持的业务板/PEX设备/子卡的类型，具体取值可通过输入**provision ** **subslot** *sunslot-number*  **model** **？**获取。

【使用指导】

开启预配置功能后：

·设备会为业务板/PEX设备/子卡自动生成接口，虽然使用**display interface**命令查看不到这些接口，但可以对这些接口进行配置，比如，进入接口视图配置接口的属性等。

·用户可对不在位的业务板/PEX设备/子卡进行部分配置，比如：**location** **slot** *slot-number*、**location** **chassis** *chassis-number* **slot** *slot-number*、**qos traffic-counter**等。

需要注意的是：

·当关闭指定单板/PEX设备的预配置功能后，设备会自动删除该单板/PEX设备及其子卡的所有预配置。

·当关闭指定子卡的预配置功能后，设备会自动删除该子卡的所有预配置。

【举例】

\# 开启slot 2上SIM3110类型单板的预配置功能。（集中式设备/分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> system-view

Sysname slot 2

Sysname-slot-2 provision model SIM3110

\# 开启chassis 1 slot 2上SIM3110类型单板的预配置功能。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname chassis 1 slot 2

Sysname-chassis-1-slot-2 provision model SIM3110

【相关命令】

·**slot**

·**chassis slot**

·**display provision failed-config**

**预配置 \-- 预配置命令 \-- display provision failed-config**

------------------------------------------------------------------------

**[display provision failed-config**]命令用来显示下发失败的预配置。

【命令】

**[display provision failed-config**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

对不存在的业务板/PEX设备/子卡进行预配置，当插入对应的业务板/PEX设备/子卡后，系统会自动下发预配置。如果预配置和当前生效的配置冲突，预配置可能会下发失败，请使用**display provision failed-config**来查看下发失败的配置。

还有一些特殊命令，可能在**display provision failed-config**命令的显示信息中却下发成功了，可能下发失败了却没在**display provision failed-config**命令的显示信息中，请使用**display current-configuration**命令来确认是否真的下发成功。这样的命令包括：

·**duplex**

·**location**

·**oc-3**

·**speed**

·**sflow**

·**threshold**

·**using oc-3****c**

【举例】

\# 显示下发失败的预配置。

\<Sysname\> display provision failed-config

Configuration applied at: Sat Jun 14 06:06:00 2014

Slot information: chassis 1 slot 1

Commands that failed to be applied:

\#

interface FortyGigE1/1/0/1

 speed 40000

\#

表1-1 display provision failed-config命令显示信息描述表

字段

描述

Configuration applied at

第一个下发失败的预配置的下发时间

Slot information

本次插入的所有业务板/PEX设备/子卡的槽位号

Commands that failed to be applied

下发失败的的具体预配置命令

【相关命令】

·**provision**
