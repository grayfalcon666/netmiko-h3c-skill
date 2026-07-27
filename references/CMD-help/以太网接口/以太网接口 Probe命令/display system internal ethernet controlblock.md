<!-- CMD-INDEX
  display system internal ethernet controlblock | Probe视图          | L6
  display system internal ethernet character | Probe视图          | L52
-->

**以太网接口 \-- 以太网接口 Probe命令 \-- display system internal ethernet controlblock**

------------------------------------------------------------------------

**[display system internal ethernet controlblock**]命令用来显示接口的控制块信息，它记录了链路层参数的值。

【命令】

集中式设备：

**[display system internal ethernet controlblock interface** { *interface-type interface-number* }]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ethernet controlblock interface** { *interface-type interface-number* } **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ethernet controlblock interface** { *interface-type interface-number* } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：表示接口类型和接口编号。

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**以太网接口 \-- 以太网接口 Probe命令 \-- display system internal ethernet character**

------------------------------------------------------------------------

**[display system internal ethernet character**]命令用来显示以太网模块侦听的特征统计信息和详细信息。

【命令】

集中式设备：

**[display system internal ethernet character**[ { **global** \| **interface** *interface-type interface-number* }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ethernet character**[ { **global** \| **interface** *interface-type interface-number* } **slot** *slot-number* [ **cpu** *cpu-number* ]]]

分布式设备－IRF模式：

**[display system internal ethernet character**[ { **global** \| **interface** *interface-type interface-number* } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[global**]：显示全局的以太特征。全局特征表示对设备上所有报文进行匹配。

**[interface** *interface-type interface-number*]：表示接口类型和接口编号。

**[slot ***slot-number*]：表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

以太网模块主要实现链路层报文接收去封装和发送加封装等处理。上层应用模块（如STP，LLDP等）需要侦听处理协议报文，指定侦听的范围（如指定接口上的报文或者设备上所有报文），侦听的协议报文具有指定的特征（如特殊的以太协议类型、特定的MAC等），并将这些特征下发给以太网模块，以太网模块在指定阶段（如收包MAC阶段/收包LLC阶段/发包三层口阶段等）会根据注册的特征库对报文进行匹配。匹配上了这些特征就交给这个阶段处理，不匹配就交给下一个阶段处理。

