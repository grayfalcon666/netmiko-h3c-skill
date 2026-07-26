
**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog mbuf dump**

------------------------------------------------------------------------

![说明](Flow日志Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal userlog mbuf dump**]命令用来显示指定个数的USERLOG UDP报文内容。

【命令】

集中式设备

**[display system internal userlog mbuf dump count ***number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal userlog mbuf dump count ***number***** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal userlog mbuf dump count ***number***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[count** *number*]：指定显示报文[的个数。]*number*为需要显示内容的日志个数，取值范围为1-100。

**[slot** *slot-number*]：指定显示报文[所在的单板。]*slot-number*为单板所在的槽位号。如未指定该参数，则默认在当前主控板上显示报文内容。[（分布式设备－独立运行模式）]

**[slot** *slot-number*]：指定显示报文[的成员设备。]*slot-number*为设备在IRF中的成员编号。如未指定该参数，则默认在当前主控板上显示报文内容。[（集中式]IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定显示报文的成员设备/PEX。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号[。如未指定该参数，则默认在当前主控板上显示报文内容。（集中式]IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定显示报文[的成员设备和单板。]*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则默认在当前主控板上显示报文内容。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定显示报文的单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如未指定该参数，则默认在当前主控板上显示报文内容。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定显示报文[设备的]CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog statistic**

------------------------------------------------------------------------

![说明](Flow日志Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal userlog statistic**]命令用来显示USERLOG模块的运行统计信息。

【命令】

集中式设备

**[display system internal userlog statistic**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal userlog statistic** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal userlog statistic ** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定查看统计信息的单板。*slot-number*为单板所在的槽位号。如未指定该参数，则默认在显示当前主控板的统计信息。[（分布式设备－独立运行模式）]

**[slot** *slot-number*]：指定查看统计信息的成员设备。*slot-number*为设备在IRF中的成员编号。如未指定该参数，则默认在显示当前主控板的统计信息。[（集中式]IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定查看统计信息的成员设备/PEX。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号[。如未指定该参数，则默认在显示当前主控板的统计信息。（集中式]IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定查看统计信息的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则默认在显示当前主控板的统计信息。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定查看统计信息的单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所在的槽位号。如未指定该参数，则默认在显示当前主控板的统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定查看统计信息的成员设备所在的CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**Flow日志 \-- Flow日志Probe命令 \-- display system internal userlog test**

------------------------------------------------------------------------

![说明](Flow日志Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal userlog mbuf test**]命令用来发送指定个数的FLOW测试日志，并显示日志发送结果信息。

【命令】

集中式设备

**[display system internal userlog test count ***number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal userlog test count ***number***** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal userlog test count ***number***** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[count** *number*]：指定发送测试日志个数。*number*为发送测试日志的个数，取值范围为1-3000。

**[slot** *slot-number*]：指定发送测试日志的单板。*slot-number*为单板所在的槽位号。如未指定该参数，则默认在当前主控板上发送测试日志。[（分布式设备－独立运行模式）]

**[slot** *slot-number*]：指定发送测试日志的成员设备。*slot-number*为设备在IRF中的成员编号。如未指定该参数，则默认在当前主控板上发送测试日志。[（集中式]IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：指定发送测试日志的成员设备/PEX。*slot-number*为设备在IRF中的成员编号或者PEX的虚拟槽位号[。如未指定该参数，则默认在当前主控板上发送测试日志。（集中式]IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定发送测试日志的成员设备和单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如未指定该参数，则默认在当前主控板上发送测试日志。[（分布式设备－]IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定发送测试日志的单板。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号[，]*slot-number*表示单板或PEX所[在的槽位号。如未指定该参数，则默认在当前主控板上发送测试日志。（分布式设备－]IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定发送测试日志的CPU。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

