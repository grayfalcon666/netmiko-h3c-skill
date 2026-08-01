<!-- CMD-INDEX
  debugging source binding            | 用户视图             | L5
-->

**IP Source Guard \-- IP Source Guard调试命令 \-- debugging source binding**

------------------------------------------------------------------------

【命令】

**[debugging **[{ **ip** \| **ipv6** } **source binding** { **all** \| **error** \| **event** }]]

**[undo debugging **[{ **ip** \| **ipv6** } **source binding** { **all** \| **error** \| **event** }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：表示IPv4绑定功能的调试信息开关。

**[ipv6**]：表示IPv6绑定功能的调试信息开关。

**[all**]：表示所有调试信息开关。

**[error**]：表示错误调试信息开关。

**[event**]：表示事件调试信息开关。

【描述】

**[debugging source binding**]命令用来打开IPv4或IPv6绑定功能的调试信息开关。**undo debugging source binding**命令用来关闭指定的绑定功能调试信息开关。

缺省情况下，端口绑定功能的调试信息开关处于关闭状态。

表1-1 debugging source binding error命令输出信息描述表

字段

描述

Failed to assign binding info message.

下发绑定信息相关的消息失败

Failed to assign request for getting large data.

下发获取大量数据的请求消息失败

表1-2 debugging source binding event命令输出信息描述表

字段

描述

The module *module* has associated with IPCIM successfully.

*[module*]模块与IPCIM关联成功

The module *module* has been disassociated.

*[module*]模块成功去关联

Received addEntry message.

接收到添加表项的消息

Received deleteEntry message.

接收到删除表项的消息

Received updateEntry message.

接收到更新表项的消息

Received deleteEntryByKeyword message.

接收到根据关键字删除表项的消息

Start smoothing process for module *module*.

开始对*module*模块进行平滑处理

The smoothing process for module *module* ended.

*[module*]模块平滑处理结束

Received message to delete interface *interface-type interface-number*.

接收到删除接口*interface-type interface-number*的消息

Received message to activate interface *interface-type interface-number*.

接收到激活接口*interface-type interface-number*的消息

Received message to deactivate interface *interface-type interface-number*.

接收到去激活接口*interface-type interface-number*的消息

Deleted the specified binding entries, VPN = v*pn-instance-name*.

删除属于VPN *vpn-instance-name*的绑定表项

Deleted the specified binding entries, ifIndex = *ifindex*.

删除接口索引为*ifindex*的接口上的绑定表项

Deleted the specified binding entries, portIndex = *portindex*.

删除端口索引为*portindex*的端口上的绑定表项

Deleted the specified binding entries,

clientVLAN = *client-vlan-id*.

删除属于clientVLAN *client-vlan-id*的绑定表项

Deleted the specified binding entries, secondVLAN = *second-vlan-id*.

删除属于secondVLAN *second-vlan-id*的绑定表项

Deleted the specified binding entries, serviceVLAN = *service-vlan-id*.

删除属于serviceVLAN *service-vlan-id*的绑定表项

Deleted the specified binding entries, privatetype = *privatetype.*

删除私有类型为*privatetype*的绑定表项

Deleted the specified binding entries, MAC = *mac-address*.

删除MAC地址为*mac-address*.的绑定表项

Deleted the specified binding entries, IP = *ip-address*, VPN = v*pn-instance-name*.

删除指定的绑定表项，IP地址为*ip-address*，且属于VPN *vpn-instance-name*

Deleted the specified binding entries, source module = *module*.

删除来源模块为*module*的绑定表项

Found a binding entry: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.

查找到一条绑定表项：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，VLAN ID为*vlan-id*

Binding entry not found: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.

查找绑定表项失败：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，vlan为*vlan-id*

Added a rule for driver: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, gatewayMAC = *gw-mac-address*, VLAN = *vlan-id,* drvContext0 *= drvcontext0*, drvContext1 = *drvcontext1*, returnCode = *return-code*.

添加驱动规则：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，用户侧网关MAC地址为*gw-mac-address*，VLAN为*vlan-id*，drvContext[0]为*drvcontext[0]*，drvContext[1]为*drvcontext[1]*，处理结果代码为*return-code*

Deleted a rule for driver: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, gatewayMAC = *gw-mac-address*, VLAN = *vlan-id*, drvContext0 *= drvcontext0*, drvContext1 = *drvcontext1*, returnCode = *return-code*.

删除驱动规则：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，用户侧网关MAC地址为*gw-mac-address*， vlan为*vlan-id*，drvContext[0]为*drvcontext[0]*，drvContext[1]为*drvcontext[1]*，处理结果代码为*return-code*

Added a default rule for driver, returnCode = *returnvalue*.

为驱动添加一条缺省规则，下驱动结果为*returnvalue*

Deleted a default rule for driver, returnCode = *returnvalue*.

为驱动删除一条缺省规则，下驱动结果为*returnvalue*

Added a binding entry: module = *module*, ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.

添加一条绑定表项：来源模块为*module*，接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，VLAN ID为*vlan-id*

Deleted a binding entry: module = *module*, ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.

删除一条绑定表项：来源模块为*module*，接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，VLAN ID为*vlan-id*

Updated a binding entry (module = *module*):

Old info: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*,

VPN *=* v*pn-index.*

New info: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*,

VPN *=* v*pn-index.*

更新来源模块为*module*的绑定表项：

老的表项信息：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，vlan为*vlan-id*，VPN为v*pn-index*

新的表项信息：接口索引为*ifindex*，IP地址为*ip-address*，MAC地址为*mac-address*，vlan为*vlan-id*，VPN为v*pn-index*

Number of driver assignments has reached the maximum.

驱动下发的次数达到最大值

Deleted binding entries using the reset command.

使用reset命令删除了绑定表项

【举例】

\# 在设备上打开IPv4绑定功能的错误调试信息开关，并通过命令行添加IPv4静态绑定表项，当表项下发失败时，可能输出如下调试信息。

\<Sysname\> debugging ip source binding error

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001

\*Apr 28 18:27:30:866 2011 sysname IPSG/7/ERROR: -MDC=1; Failed to assign binding info message.

*// 表项下发内核失败*

\# 在设备上打开IPv4绑定功能的事件调试信息开关，并通过命令行添加IPv4静态绑定表项，输出如下调试信息。

\<Sysname\> debugging ip source binding event

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001

\*Apr 28 18:37:30:866 2011 sysname IPSG/7/EVENT: -MDC=1; Added a rule for driver: ifIndex = 0x34, IP = 192.168.0.1, MAC = 0001-0001-0001, gatewayMAC = ffff-ffff-ffff,

 VLAN = 0xffff, drvContext[0 = 0x4, drvContext1 = 0x4, returnCode = 0x0.]

\*Apr 28 18:37:30:866 2011 sysname IPSG/7/EVENT: -MDC=1; Added a binding entry: module = Static, ifIndex = 0x1, IP = 192.168.0.1, MAC = 0001-0001-0001, VLAN = 65536.

*// 成功添加一条静态绑定表项*

\# 删除一条IPv4静态绑定表项，输出如下调试信息。

Sysname-GigabitEthernet1/0/1 undo ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001

\*Apr 28 18:40:48:812 2011 sysname IPSG/7/EVENT: -MDC=1; Deleted a rule for driver: if

Index = 0x34, IP = 192.168.0.1, MAC = 0001-0001-0001, gatewayMac = ffff-ffff-fff

f, VLAN = 0xffff, drvContext[0 = 0x4, drvContext1 = 0x4, returnCode = 0x0.]

\*Apr 28 18:40:48:812 2011 sysname IPSG/7/EVENT: -MDC=1; Deleted a binding entry: module = Static, ifIndex = 0x1, IP = 192.168.0.1, MAC = 0001-0001-0001, VLAN = 65536.

*// 成功删除一条静态绑定表项*
