
**对象组 \-- 对象组Probe配置命令 \-- display system internal object-group**

------------------------------------------------------------------------

**[display system internal object-group**]命令用来显示对象组的配置和运行情况。

【命令】

集中式设备：

**[display system internal object-group**[ [ { { **ip** \| **ipv6** } **address** \| **port** \| **service** } [ **default** ]  **name** *object-group-name*  \| **name** *object-group-name* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal object-group**[ [ { { **ip \| ipv6** } **address \| port \| service** } [ **default** ]  **name** *object-group-name*  **\| name** *object-group-name* ] **slot** *slot-number*]]

分布式设备－IRF模式：

**[display system internal object-group**[ [ { { **ip \| ipv6** } **address \| port \| service** } [ **default** ]  **name** *object-group-name*  **\| name** *object-group-name* ] **chassis** *chassis-number* **slot** *slot-number*]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip address**]：指定对象组类型为IP地址对象组。

**[ipv6** **address**]：指定对象组类型为IPv6地址对象组。

**[port**]：指定对象组类型为端口对象组。

**[service**]：指定对象组类型为服务对象组。

**[default**]：指定默认对象组。

**[name*** object-group-name*]：指定对象组名称。*object-group-name*表示对象组的名称，为1～31个字符的字符串，不区分大小写。

**[slot** *slot-number*]：显示指定单板上对象组的配置和运行情况，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上对象组的配置和运行情况，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上对象组的配置和运行情况，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上对象组的配置和运行情况，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上对象组的配置和运行情况，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

