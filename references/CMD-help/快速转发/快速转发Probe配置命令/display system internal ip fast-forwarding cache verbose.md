
**快速转发 \-- 快速转发Probe配置命令 \-- display system internal ip fast-forwarding cache verbose**

------------------------------------------------------------------------

**[display system internal ip fast-forwarding cache verbose**]命令用来显示IPv4快转表项的详细内容。

【命令】

集中式设备：

**[display system internal ip fast-forwarding cache ** *ip-address* ] **verbose**

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ip fast-forwarding cache ** *ip-address* ] **verbose**  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal ip fast-forwarding cache** [ *ip-address*  **verbose**  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：显示指定IP地址的 IPv4 快转表详细信息。

**[slot**] *slot-number*： 显示指定单板的快转表详细信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的快转表详细信息。（分布式设备－独立运行模式）

**[slot**] *slot-number*：显示指定成员设备的快转表详细信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的快转表详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**] *slot-number*：显示指定成员设备/PEX的快转表详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的快转表详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的快转表详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转表详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定单板的快转表详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的快转表详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：显示指定CPU的快转表详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**快速转发 \-- 快速转发Probe配置命令 \-- display system internal ip fast-forwarding service-sequece**

------------------------------------------------------------------------

**[display system internal ip fast-forwarding service-sequece**]命令用来显示业务模块向快转模块的注册信息。

【命令】

**[display system internal ip fast-forwarding service-sequece**]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

**快速转发 \-- 快速转发Probe配置命令 \-- display system internal max-ecmp-num**

------------------------------------------------------------------------

**[display system internal max-ecmp-num**]命令用来显示分布式各板IPv4的最大等价路由条数配置。

【命令】

集中式设备：

**[display system internal max-ecmp-num**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal max-ecmp-num** [ **slot** *slot-number* [ **cpu** *cpu-number*  ] ]]

分布式设备－IRF模式：

**[display system internal max-ecmp-num** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] ** **]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot**] *slot-number*： 显示指定单板的最大等价路由条数配置信息。*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示主用主控板上的最大等价路由条数配置信息。（分布式设备－独立运行模式）

**[slot**] *slot-number*：显示指定成员设备的最大等价路由条数配置信息。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示Master设备上的最大等价路由条数配置信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**] *slot-number*：显示指定成员设备/PEX的最大等价路由条数配置信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示Master设备上的最大等价路由条数配置信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定成员设备上指定单板的最大等价路由条数配置信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板上的最大等价路由条数配置信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**] *chassis-number* **slot** *slot-number*：显示指定单板的最大等价路由条数配置信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示全局主用主控板上的最大等价路由条数配置信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的最大等价路由条数配置信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

