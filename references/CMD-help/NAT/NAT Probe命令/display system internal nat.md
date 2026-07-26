
**NAT \-- NAT Probe命令 \-- display system internal nat**

------------------------------------------------------------------------

**[display system internal nat**]命令用来显示内核的NAT配置信息。

【命令】

集中式设备：

**[display system internal nat**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nat slot ***slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display system internal nat chassis ***chassis-number ***slot ***slot-number * **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的内核的NAT配置信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的内核的NAT配置信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的内核的NAT配置信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的内核的NAT配置信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的内核的NAT配置信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**] *cpu-number*：显示指定CPU上的内核的NAT配置信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的具体型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**NAT \-- NAT Probe命令 \-- display system internal nat controller**

------------------------------------------------------------------------

![说明](NAT%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal nat controller**]命令用来显示处理NAT业务的引擎信息。

【命令】

**[display system internal nat controller**]

【视图】

Probe视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

如果没有配置引流备份组，以引擎为单位显示所有引擎，如果配置了引擎备份组，则以备份组为单位显示所有备份组及其成员中的引擎。

每个双机热备备份组中包含两个引擎成员，主引擎负责处理所有的安全业务，当主引擎发生故障时，备引擎升级成主引擎。

**NAT \-- NAT Probe命令 \-- display system internal nat flow**

------------------------------------------------------------------------

![说明](NAT%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal nat flow**]命令用来显示NAT配置相关的引流规则。

【命令】

**[display system internal nat flow **[\| **server** \| **static** }]

【视图】]

Probe视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有NAT配置的引流规则。

**[dynamic**]：显示NAT动态地址转换配置相关的引流规则。

**[server**]：显示NAT内部服务器配置相关的引流规则。

**[static**]：显示NAT静态地址转换配置相关的引流规则。

**[portblock**]：显示NAT 444端口块映射配置相关的引流规则。

【使用指导】

多引擎环境下，为保证同一条流的正向报文和反向报文由同一个引擎处理，NAT模块会在接口板下发相应的引流规则。

引擎是多形态防火墙中用来处理安全业务的最小单元，存在于安全插卡（SecBlade）上。一个SecBlade上会有一个或者多个业务引擎，简称SPE，每个SPE之间相互独立，每个SPE由一个多核CPU组成。

