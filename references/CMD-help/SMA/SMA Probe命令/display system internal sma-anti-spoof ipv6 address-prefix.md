
**SMA \-- SMA Probe命令 \-- display system internal sma-anti-spoof ipv6 address-prefix**

------------------------------------------------------------------------

**[display system internal sma-anti-spoof ipv6 address-prefix**]命令用来显示地址前缀信息。

【命令】

集中式设备：

**[display system internal sma-anti-spoof ipv6 address-prefix ** *ipv6-address ipv6-prefix-length* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal sma-anti-spoof ipv6 address-prefix ** *ipv6-address ipv6-prefix-length* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal sma-anti-spoof ipv6 address-prefix ** *ipv6-address ipv6-prefix-length* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address ipv6-prefix-length*]：显示指定IPv6地址的前缀信息。*ipv6-prefix-length*为IPv6地址前缀长度，取值范围为1～128。

**[slot** *slot-number*]：显示指定单板上的地址前缀信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的地址前缀信息。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的地址前缀信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示Master设备上的地址前缀信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的地址前缀信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示Master设备上的地址前缀信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis **]*chassis-number*** slot ***slot-number*：显示指定成员设备上指定单板的地址前缀信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的地址前缀信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的地址前缀信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的地址前缀信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU上的地址前缀信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**SMA \-- SMA Probe命令 \-- display system internal sma-anti-spoof ipv6 packet-tag**

------------------------------------------------------------------------

**[display system internal sma-anti-spoof ipv6 packet-tag**]命令用来显示标签信息。

【命令】

集中式设备：

**[display system internal sma-anti-spoof ipv6 packet-tag ** *source-as-number destination-as-number* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal sma-anti-spoof ipv6 packet-tag ** *source-as-number destination-as-number* ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal sma-anti-spoof ipv6 packet-tag ***source-as-number destination-as-number* ]  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[source-as-number destination-as-number*]：显示指定AS对的标签信息。*source-as-number*表示源AS号，取值范围为0～4294967295，*destination-as-number*表示目的AS号，取值范围为0～4294967295。如果不指定本参数，则显示所有AS对的标签信息。

**[slot** *slot-number*]：显示指定单板上的标签信息。*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示主用主控板上的标签信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的标签信息。*slot-number*表示设备在IRF中的成员编号。如果不指定本参数，将显示Master设备上的标签信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示指定成员设备/PEX的标签信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示Master设备上的标签信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定成员设备上指定单板的标签信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果不指定本参数，将显示全局主用主控板上的标签信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number*** slot ***slot-number*]：显示指定单板的标签信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果不指定本参数，将显示全局主用主控板上的标签信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的标签信息。*cpu-number*表示CPU编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。
