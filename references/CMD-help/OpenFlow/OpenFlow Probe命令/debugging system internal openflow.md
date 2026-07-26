
**OpenFlow \-- OpenFlow Probe命令 \-- debugging system internal openflow**

------------------------------------------------------------------------

**[debugging **]**system internal openflow**命令用来打开OpenFlow调试信息开关。

**[undo debugging **]**system internal openflow**命令用来关闭OpenFlow调试信息开关。

【命令】

**[debugging **]**system internal openflow**

**[undo debugging **]**system internal openflow**

【缺省情况】

OpenFlow调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**OpenFlow \-- OpenFlow Probe命令 \-- display system internal openflow instance**

------------------------------------------------------------------------

**[display system internal openflow instance**]命令用来显示OpenFlow内部实例信息和流表信息。

【命令】

**[display system internal openflow instance**[ { **inner** \| **inner-redirect** } [ **flow-table** [ *table-id* ] \| **group**  *group-id*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[inner**]：内部二次引流实例运行信息。

**[inner-redirect**]：内部引流实例运行信息。

**[flow-table ** *table-id* ]：流表信息。*table-id*为流表ID，取值范围为0～254。如果未指定本参数，将显示所有流表的信息。

**[group** [ *group-id* ]]：Group表项信息。*group-id*为Group ID，取值范围为0～0xffffff00。如果未指定本参数，将显示实例所有Group表项的信息。

