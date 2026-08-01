<!-- CMD-INDEX
  debugging system internal stg       | Probe视图          | L8
  debugging system internal stp       | Probe视图          | L50
  display system internal stp bridge-info | Probe视图          | L82
  display system internal stp port-info | Probe视图          | L126
-->

**生成树 \-- 生成树Probe命令 \-- debugging system internal stg**

------------------------------------------------------------------------

**[debugging system internal stg**]命令用来开启STG调试信息开关。

**[undo debugging system internal stg**]命令用来关闭STG调试信息开关。

【命令】

**[debugging system internal stg **[{ **all** \| **bind** \| **error** \| **map** \| **state** \| **tc** }]]

**[undo debugging system internal stg **[{ **all** \| **bind** \| **error** \| **map** \| **state** \| **tc** }]]

【缺省情况】

STG调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示STG所有调试信息开关。

**[bind**]：表示STG与VLAN绑定调试信息开关。

**[error**]：表示STG错误调试信息开关。

**[map**]：表示STG与STI映射事件调试信息开关。

**[state**]：表示STG状态设置调试信息开关。

**[tc**]：表示TC事件调试信息开关。

**生成树 \-- 生成树Probe命令 \-- debugging system internal stp**

------------------------------------------------------------------------

**[debugging system internal stp**]命令用来开启生成树进程间通信调试开关。

**[undo debugging system internal stp**]命令用来关闭生成树进程间通信调试开关。

【命令】

**[debugging system internal stp ipc **]

**[undo debugging system internal stp ipc**]

【缺省情况】

生成树进程间通信调试开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipc**]：表示生成树进程间通信调试信息开关。

**生成树 \-- 生成树Probe命令 \-- display system internal stp bridge-info**

------------------------------------------------------------------------

**[display system internal stp bridge-info**]命令用来显示生成树指定实例桥配置信息及运行状态。

【命令】

集中式设备：

**[display system internal stp bridge-info instance ***instance-id*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal stp bridge-info instance ***instance-id*** slot ***slot-number*]

分布式设备－IRF模式：

**[display system internal stp bridge-info instance ***instance-id*** chassis ***chassis-number*** slot ***slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance** *instance-id*]：显示指定实例的生成树桥配置信息和运行状态，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。

**[slot*** slot-number*]：显示指定单板的生成树桥配置信息和运行状态，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的生成树桥配置信息和运行状态，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的生成树桥配置信息和运行状态，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备指定单板上的生成树桥配置信息和运行状态，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的生成树桥配置信息和运行状态，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**生成树 \-- 生成树Probe命令 \-- display system internal stp port-info**

------------------------------------------------------------------------

display system internal stp port-info命令用来显示生成树指定实例端口配置信息及运行状态。

【命令】

**[display system internal stp port-info instance** *instance-id* **interface** *interface-type interface-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[instance** *instance-id*]：显示指定实例的生成树端口配置信息和运行状态，*instance-id*为MSTI的编号，取值范围为0～4094，0表示CIST。

**[interface** *interface-type* *interface-number*]：显示指定端口上的生成树端口信息和运行状态，*interface-type* *interface-number*表示端口类型和端口编号。

