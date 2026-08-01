<!-- CMD-INDEX
  display sampler                     | 任意视图             | L6
  sampler                             | 系统视图             | L100
-->

**Sampler \-- Sampler配置命令 \-- display sampler**

------------------------------------------------------------------------

**[display sampler**]命令用来查看采样器的配置信息。

【命令】

集中式设备：

**[display sampler ** *sampler-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display sampler ** *sampler-name* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display sampler ** *sampler-name* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[sampler-name*]：采样器名称，为1～31个字符的字符串，不区分大小写。未指定该参数时，将显示所有采样器的信息。

**[slot ***slot-number*]：查看指定单板上的信息。*slot-number*表示单板的槽位号。未指定该参数，将显示主用主控板上的信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：查看指定成员设备上的信息。*slot-number*表示设备在IRF中的成员编号。未指定该参数时，将显示主用设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：查看指定成员设备/PEX上的信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数时，将显示主用设备上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：查看指定成员设备上指定单板上的信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。未指定该参数时，将显示主用设备主用主控板上的信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：查看指定单板上的信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。如果未指定该参数时，将显示主用设备主用主控板上的信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 查看采样器256的配置信息。

\<Sysname\> display sampler 256

 Sampler name: 256

  Mode: Fixed;  Packet-interval: 8

\# 查看采样器256的1号单板上的配置信息。（分布式设备－独立运行模式）

\<Sysname\> display sampler 256 slot 1

 Sampler name: 256

  Mode: Fixed;  Packet-interval: 8

\# 查看采样器256的1号框1号单板上的配置信息。（分布式设备－IRF模式）

\<Sysname\> display sampler 256 chassis 1 slot 1

 Sampler name: 256

  Mode: Fixed;  Packet-interval: 8

表1-1 display sampler命令显示信息描述表

字段

描述

Sampler name

采样器名称

Mode

采样器模式，包括固定采样（Fixed）和随机采样（Random）

Packet-interval

采样率

**Sampler \-- Sampler配置命令 \-- sampler**

------------------------------------------------------------------------

**[sampler**]命令用来创建采样器。

**[undo sampler**]命令用来删除指定采样器。

【命令】

**[sampler ***sampler-name*** mode **[{ **fixed** \| **random** } **packet-interval** *rate*]]

**[undo sampler ***sampler-name*]

【缺省情况】

未创建任何采样器。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[sampler-name*]：采样器名称，为1～31个字符的字符串，不区分大小写。

**[fixed**]：采样方式为固定采样，表示每组报文中的第一个报文被抽取。

**[random**]：采样方式为随机采样，表示每组报文中，任意一个报文都有可能被抽取。

*[rate*]：采样率，即在指定的多个报文中抽取一个报文进行采样。对于硬件采样，按照2的*rate*次方进行计算。例如，该参数设为8，表示在256（2的8次方）个报文中采样1个报文；该参数设为10，表示在1024（2的10次方）个报文中采样1个报文；对于软件采样，按照用户输入的实际参数进行采样。例如，该参数设为100，表示在100个报文中采样1个报文。不同型号的设备支持的取值范围和实际采样率不同，请以设备的实际情况为准。

【使用指导】

·不同型号的设备支持的采样器数目不同，请以设备的实际情况为准。

·该命令对所有单板生效。（分布式设备－独立运行模式/分布式设备－IRF模式）

【举例】

\# 创建一个名为abc的采样器，采用固定采样方式，设置采样率为8。

\<Sysname\> system-view

Sysname sampler abc mode fixed packet-interval 8
