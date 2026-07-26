
**PPP \-- PPP Probe命令 \-- display system internal ppp statistics**

------------------------------------------------------------------------

**[display system internal ppp statistics**]命令用来显示PPP的统计信息。

【命令】

集中式设备：

**[display system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }]

分布式设备－独立运行模式]/集中式IRF设备：

**[display system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－]IRF模式：

**[display system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aggregation**]：显示PPP的聚合处理统计信息。

**[all**]：显示PPP的所有统计信息。

**[interface-event**]：显示PPP的接口处理统计信息。

**[vsrp** [ **vsrp-instance** *vsrp-instance-name* ]]：显示PPP的多机备份实例统计信息。*vsrp-instance-name*表示多机备份实例名称，为1～31个字符的字符串，区分大小写。不指定多机备份实例时，将显示所有多机备份实例的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot*** slot-number*]：显示指定单板的PPP统计信息。*slot-number*表示单板所在的槽位号。不指定本参数时，将显示所有单板的PPP统计信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的PPP统计信息。*slot-number*表示设备在IRF中的成员编号。不指定本参数时，将显示所有成员设备的PPP统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的PPP统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定本参数时，将显示所有成员设备/PEX上的PPP统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot*** slot-number*]：显示指定成员设备上指定单板的PPP统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的PPP统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot*** slot-number*]：显示指定单板的PPP统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定本参数时，将显示所有单板上的PPP统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的PPP统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

在主用设备和备用设备上都可以查询PPP的统计信息。

**PPP \-- PPP Probe命令 \-- display system internal pppoe-server statistics**

------------------------------------------------------------------------

**[display system internal pppoe-server statistics**]命令用来显示PPPoE server的统计信息。

【命令】

集中式设备:

**[display system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }]]

分布式设备---独立运行模式/集中式IRF设备：

**[display system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式[:]

**[display system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aggregation**]：显示PPPoE server的聚合处理统计信息。

**[all**]：显示PPPoE server的所有统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vsrp** [ **vsrp-instance** *vsrp-instance-name* ]]：显示PPPoE server的VSRP实例统计信息。*vsrp-instance-name*表示VSRP实例名称，为1～31个字符的字符串，区分大小写。不指定VSRP实例时，显示所有VSRP实例的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot** *slot-number*]：显示指定单板的PPPoE server统计信息。*slot-number*表示单板所在的槽位号。不指定本参数时，将显示所有单板的PPPoE server统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的PPPoE server统计信息。*slot-number*表示设备在IRF中的成员编号。不指定本参数时，将显示所有成员设备的PPPoE server统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的PPPoE server统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定本参数时，将显示所有成员设备/PEX上的PPPoE server统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的PPPoE server统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定本参数时，将显示所有成员设备上所有单板的PPPoE server统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的PPPoE server统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定本参数时，将显示所有单板上的PPPoE server统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的PPPoE server统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

在主用设备和备用设备上都可以查询PPPoE server的统计信息。

**PPP \-- PPP Probe命令 \-- reset system internal ppp statistics**

------------------------------------------------------------------------

**[reset system internal ppp statistics**]命令用来清除PPP的统计信息。

【命令】

集中式设备：

**[reset system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }]

分布式设备－独立运行模式]/集中式IRF设备：

**[reset system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]

分布式设备－]IRF模式：

**[reset system internal ppp statistics****interface-event**[ \| ]**vsrp** [ **vsrp-instance** *vsrp-instance-name*  }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】]

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aggregation**]：清除PPP的聚合处理统计信息。

**[all**]：清除PPP的所有统计信息。

**[interface-event**]：清除PPP的接口处理统计信息。

**[vsrp** [ **vsrp-instance** *vsrp-instance-name* ]]：清除PPP的VSRP实例统计信息。*vsrp-instance-name*表示VSRP实例名称，为1～31个字符的字符串，区分大小写。不指定VSRP实例时，将清除所有VSRP实例的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot*** slot-number*]：清除指定单板的PPP统计信息。*slot-number*表示单板所在的槽位号。不指定本参数时，将清除所有单板的PPP统计信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：清除指定成员设备的PPP统计信息。*slot-number*表示设备在IRF中的成员编号。不指定本参数时，将清除所有成员设备的PPP统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：清除指定成员设备/PEX的PPP统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定本参数时，将清除所有成员设备/PEX上的PPP统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot*** slot-number*]：清除指定成员设备上指定单板的PPP统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定本参数时，将清除所有成员设备上所有单板的PPP统计信息。（（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot*** slot-number*]：清除指定单板的PPP统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定本参数时，将清除所有单板上的PPP统计信息。（（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的PPP统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

在主用设备和备用设备上都可以清除PPP的统计信息。

**PPP \-- PPP Probe命令 \-- reset system internal pppoe-server statistics**

------------------------------------------------------------------------

**[reset system internal pppoe-server statistics**]命令用来清除PPPoE server的统计信息。

【命令】

集中式设备:

**[reset system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }]]

分布式设备---独立运行模式/集中式IRF设备：

**[reset system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备---IRF模式[:]

**[reset system internal pppoe-server statistics**[ { **aggregation** \| **all** \| **vsrp** [ **vsrp-instance** *vsrp-instance-name* ] }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[aggregation**]：清除PPPoE server的聚合处理统计信息。

**[all**]：清除PPPoE server的所有统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vsrp** [ **vsrp-instance** *vsrp-instance-name* ]]：清除PPPoE server的VSRP实例统计信息。*vsrp-instance-name*表示VSRP实例名称，为1～31个字符的字符串，区分大小写。不指定VSRP实例时，将清除所有VSRP实例的统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[slot** *slot-number*]：清除指定单板的PPPoE server统计信息。*slot-number*表示单板所在的槽位号。不指定本参数时，将清除所有单板的PPPoE server统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的PPPoE server统计信息。*slot-number*表示设备在IRF中的成员编号。不指定本参数时，将清除所有成员设备的PPPoE server统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的PPPoE server统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定本参数时，将清除所有成员设备/PEX上的PPPoE server统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的PPPoE server统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定本参数时，将清除所有单板上的PPPoE server统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的PPPoE server统计信息。*cpu-number*表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

在主用设备和备用设备上都可以清除PPPoE server的统计信息。
