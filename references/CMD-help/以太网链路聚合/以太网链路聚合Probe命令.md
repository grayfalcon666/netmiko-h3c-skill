<!-- CMD-INDEX
  display system internal link-aggregation global | Probe视图          | L6
  display system internal link-aggregation interface | Probe视图          | L48
-->

**以太网链路聚合 \-- 以太网链路聚合Probe命令 \-- display system internal link-aggregation global**

------------------------------------------------------------------------

**[display system internal link-aggregation global**]命令用来显示聚合模块的系统内部全局信息。

【命令】

集中式设备：

**[display system internal link-aggregation global**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal link-aggregation slot ***slot-number*** global**]

分布式设备－IRF模式：

**[display system internal link-aggregation chassis ***chassis-number*** slot ***slot-number*** global**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备所在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备所在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示设备及单板的位置。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号列表。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示设备及单板的位置。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号列表。（分布式设备－IRF模式）（支持IRF3的设备）

**以太网链路聚合 \-- 以太网链路聚合Probe命令 \-- display system internal link-aggregation interface**

------------------------------------------------------------------------

**[display system internal link-aggregation interface**]命令用来显示聚合模块的系统内部接口信息。

【命令】

集中式设备：

**[display system internal link-aggregation interface**[ { **bridge-aggregation** \| **route-aggregation** } *interface-number* [ **kernel** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

**[display system internal link-aggregation interface**[ *interface-type interface-number* [ **kernel** \| **lacp** \| **lacppdu** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal link-aggregation slot ***slot-number*** interface**[ { **bridge-aggregation** \| **route-aggregation** } *interface-number* [ **kernel** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

**[display system internal link-aggregation slot ***slot-number*** interface**[ *interface-type interface-number* [ **kernel** \| **lacp** \| **lacppdu** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

分布式设备－IRF模式：

**[display system internal link-aggregation chassis ***chassis-number*** slot ***slot-number*** interface**[ { **bridge-aggregation** \| **route-aggregation** } *interface-number* [ **kernel** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

**[display system internal link-aggregation chassis ***chassis-number*** slot ***slot-number*** interface**[ *interface-type interface-number* [ **kernel** \| **lacp** \| **lacppdu** \| **statistics** [ **ipv4** \| **ipv6** ] ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bridge-aggregation**]：显示二层聚合接口所对应聚合组的系统内部信息。

**[route-aggregation**]：显示三层聚合接口所对应聚合组的系统内部信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-number*]：聚合接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。必须是当前已经创建的聚合接口编号。

*[interface-type interface-number*]：聚合成员口。其中，*interface-type*为接口类型，*interface-number*为接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[kernel**]：内核数据。

**[statistics**]：数据统计值。

**[ipv4**]：**IPv4报文统计值。**

**[ipv6**]：**IPv6报文统计值。**

**[lacp**]：动态聚合数据。

**[lacppdu**]：LACP报文统计值。

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备所在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备所在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示设备及单板的位置。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号列表。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：表示设备及单板的位置。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号列表。（分布式设备－IRF模式）（支持IRF3的设备）

【使用指导】

·如果未指定**kernel**、**lacp**、**lacppdu**和**statistics**参数，则显示LAGG主线程中接口的基本数据。

·如果未指定**ipv4、ipv6**参数，则显示所有报文统计值。

·部分显示数据重复，实际上是保存在不同的线程中，定位问题时可互相佐证，利于问题的分析。

