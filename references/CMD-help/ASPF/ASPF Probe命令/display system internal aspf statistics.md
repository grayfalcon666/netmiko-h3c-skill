
**ASPF \-- ASPF Probe命令 \-- display system internal aspf statistics**

------------------------------------------------------------------------

**[display system internal aspf statistics**]命令用来查看ASPF、报文过滤以及对象策略模块的丢包统计信息。

【命令】

集中式设备：

**[display system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**]：查看接口上的ASPF丢包统计信息。

**[zone-pair**]：查看域间实例上的ASPF丢包统计信息。

**[ipv4**]： 查看IPv4报文的丢包统计信息。

**[ipv6**]： 查看IPv6报文的丢包统计信息。

**[slot ***slot-number*]：显示指定单板上的丢包统计信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有单板上的丢包统计信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备上的丢包统计信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示显示所有成员设备上的丢包统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的丢包统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的丢包统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的丢包统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示显示所有成员设备的所有单板上的丢包统计表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的丢包统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的丢包统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的丢包统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**ASPF \-- ASPF Probe命令 \-- reset system internal aspf statistics**

------------------------------------------------------------------------

**[reset system internal aspf statistics**]命令用来清除ASPF、报文过滤以及对象策略模块的丢包统计信息。

【命令】

集中式设备：

**[reset system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[reset system internal aspf statistics**[ { **interface** \| **zone-pair** } { **ipv4** \| **ipv6** } ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**]：清除接口上的ASPF丢包统计信息。

**[zone-pair**]：清除域间实例上的ASPF丢包统计信息。

**[ipv4**]：清除IPv4报文的丢包统计信息。

**[ipv6**]：清除IPv6报文的丢包统计信息。

**[slot ***slot-number*]：清除指定单板上的丢包统计信息，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示清除所有单板上的丢包统计信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备上的丢包统计信息，*slot-number*表示设备在IRF中的成员编号。若不指定该参数，则表示清除所有成员设备上的丢包统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX上的丢包统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示清除所有成员设备/PEX上的丢包统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备的指定单板上的丢包统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。若不指定该参数，则表示清除所有成员设备的所有单板上的丢包统计表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上的丢包统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示清除所有单板上的丢包统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：清除指定CPU上的丢包统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）
