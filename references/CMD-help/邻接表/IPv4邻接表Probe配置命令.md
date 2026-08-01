<!-- CMD-INDEX
  display system internal adjacent-table | Probe视图          | L14
  display system internal adj4 statistics | probe视图          | L52
  reset system internal adj4 statistics | probe视图          | L90
  display system internal adj4 entry  | probe视图          | L128
  display system internal ipv6 adjacent-table | probe视图          | L170
  display system internal adj6 statistics | probe视图          | L208
  reset system internal adj6 statistics | probe视图          | L246
  display system internal adj6 entry  | probe视图          | L284
  debugging system internal adj4      | probe视图          | L326
  debugging system internal adj6      | probe视图          | L364
-->

**邻接表 \-- IPv4邻接表Probe配置命令 \-- display system internal adjacent-table**

------------------------------------------------------------------------

**[display system internal adjacent-table**]命令用来显示IPv4邻接表的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal adjacent-table slot**]*****slot-number *[ **cpu** *cpu-number*  [ **count** \| **verbose** ]]

分布式设备－IRF模式：

**[display system internal adjacent-table chassis** *chassis-number* **slot**]*****slot-number *[ **cpu** *cpu-number*  [ **count** \| **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的IPv4邻接表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv4邻接表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv4邻接表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[count**]：显示IPv4邻接表项的数目。

**[verbose**]：显示IPv4邻接表项的详细信息。

**邻接表 \-- IPv4邻接表Probe配置命令 \-- display system internal adj4 statistics**

------------------------------------------------------------------------

**[display system internal adj4 statistics**]命令用来显示IPv4邻接表项的统计信息。

【命令】

集中式设备：

**[display system internal adj4 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal adj4 statistics slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal adj4 statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的IPv4邻接表项的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv4邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv4邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表 \-- IPv4邻接表Probe配置命令 \-- reset system internal adj4 statistics**

------------------------------------------------------------------------

**[reset system internal adj4 statistics**]命令用来清除IPv4邻接表项的统计信息

【命令】

集中式设备：

**[reset system internal adj4 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal adj4 statistics slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[reset system internal adj4 statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的IPv4邻接表项的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的IPv4邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的IPv4邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表 \-- IPv4邻接表Probe配置命令 \-- display system internal adj4 entry**

------------------------------------------------------------------------

**[display system internal adj4 entry **]命令用来显示指定IPv4邻接表项的详细信息。

【命令】

集中式设备：

**[display system internal adj4 entry ***ip-address ***interface ***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal adj4 entry ***ip-address ***interface ***interface-type interface-number ***slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal adj4 entry ***ip-address ***interface ***interface-type interface-number*** chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：IPv4邻接表项中的IP地址。

**[interface**] *interface-type interface-number*：IPv4邻接表项所对应的三层接口类型和接口号。

**[slot** *slot-number*]：显示指定单板的IPv4邻接表项的信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv4邻接表项的信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv4邻接表项的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表 \-- IPv6邻接表Probe配置命令 \-- display system internal ipv6 adjacent-table**

------------------------------------------------------------------------

**[display system internal ipv6 adjacent-table**]命令用来显示IPv6邻接表的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 adjacent-table slot**]*****slot-number *[ **cpu** *cpu-number*  [ **count** \| **verbose** ]]

分布式设备－IRF模式：

**[display system internal ipv6 adjacent-table chassis** *chassis-number* **slot**]*****slot-number *[ **cpu** *cpu-number*  [ **count** \| **verbose** ]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6邻接表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6邻接表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6邻接表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[count**]：显示IPv6邻接表项的数目。

**[verbose**]：显示IPv6邻接表项的详细信息。

**邻接表 \-- IPv6邻接表Probe配置命令 \-- display system internal adj6 statistics**

------------------------------------------------------------------------

**[display system internal adj6 statistics **]命令用来显示IPv6邻接表项的统计信息。

【命令】

集中式设备：

**[display system internal adj6 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal adj6 statistics slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal adj6 statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定单板的IPv6邻接表项的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表 \-- IPv6邻接表Probe配置命令 \-- reset system internal adj6 statistics**

------------------------------------------------------------------------

**[reset system internal adj6 statistics**]命令用来清除IPv6邻接表项的统计信息

【命令】

集中式设备：

**[reset system internal adj6 statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal adj6 statistics slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[reset system internal adj6 statistics chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的IPv6邻接表项的统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的IPv6邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的IPv6邻接表项的统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表 \-- IPv6邻接表Probe配置命令 \-- display system internal adj6 entry**

------------------------------------------------------------------------

**[display system internal adj6 entry **]命令用来显示指定IPv6邻接表项的详细信息。

【命令】

集中式设备：

**[display system internal adj6 entry ***ipv6-address ***interface ***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal adj6 entry ***ipv6-address ***interface ***interface-type interface-number ***slot**]*****slot-number * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal adj6 entry ***ipv6-address ***interface ***interface-type interface-number*** chassis** *chassis-number* **slot**]*****slot-number * **cpu** *cpu-number*

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：IPv6邻接表项中的IPv6地址。

**[interface**] *interface-type interface-number*：IPv6邻接表项所对应的三层接口类型和接口号。

**[slot** *slot-number*]：显示指定单板的IPv6邻接表项的信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的IPv6邻接表项的信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的IPv6邻接表项的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**邻接表调试命令 \-- IPv4邻接表调试命令 \-- debugging system internal adj4**

------------------------------------------------------------------------

**[debugging system internal adj4**]命令用来打开IPv4邻接表调试开关。

**[undo debugging system internal adj4**]命令用来关闭IPv4邻接表调试开关。

【命令】

**[debugging system internal adj4 **[{ **hardware** \| **bind** \| **notify** \| **entry** }]]

**[undo debugging system internal adj4 **[{ **hardware** \| **bind** \| **notify** \| **entry** }]]

【缺省情况】

IPv4邻接表调试开关处于关闭状态。

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hardware**]：打开IPv4邻接表下驱动调试功能。

**[bind**]：打开VN/NHLFE表项绑定IPv4邻接表调试功能。

**[notify**]：打开IPv4邻接表项变化时，反刷VN和NHLFE表项调试功能。

**[entry**]：打开IPv4邻接表项更新时调试功能。

**邻接表调试命令 \-- IPv6邻接表调试命令 \-- debugging system internal adj6**

------------------------------------------------------------------------

**[debugging system internal adj6**]命令用来打开IPv6邻接表调试开关。

**[undo debugging system internal adj6**]命令用来关闭IPv6邻接表调试开关。

【命令】

**[debugging system internal adj6 **[{ **hardware** \| **bind** \| **notify** \| **entry** }]]

**[undo debugging system internal adj6 **[{ **hardware** \| **bind** \| **notify** \| **entry** }]]

【缺省情况】

IPv6邻接表调试开关处于关闭状态。

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hardware**]：打开IPv6邻接表下驱动调试功能。

**[bind**]：打开VN/NHLFE表项绑定IPv6邻接表调试功能。

**[notify**]：打开IPv6邻接表项变化时，反刷VN和NHLFE表项调试功能。

**[entry**]：打开IPv6邻接表项更新时调试功能。

