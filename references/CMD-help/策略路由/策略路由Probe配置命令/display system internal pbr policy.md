
**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr policy**

------------------------------------------------------------------------

**[display system internal pbr policy**]用于显示用户态下的策略路由信息。

【命令】

集中式设备：

**[display system internal pbr policy****]\*[policy-name* \**[setup **]**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal pbr slot**]*slot-number * **cpu** *cpu-number*  ** policy** \*[policy-name *\**[setup** ]]

分布式设备－IRF模式：

**[display system internal pbr chassis**]*chassis-number*** slot***slot-number***** **cpu** *cpu-number*  **policy** \*[policy-name*\**[setup**]**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[policy**]*policy-name*：显示用户态下指定策略路由的信息。policy-name为策略名，为1～19个字符的字符串，区分大小写。

**[setup**]：显示用户态下指定策略的接口应用信息。

**[slot*** slot-number*]：显示用户态下指定单板上的策略路由信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示用户态下指定成员设备的策略路由信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示用户态下指定成员设备/PEX的策略路由信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示用户态下指定成员设备上指定单板的策略路由信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示用户态下指定单板的策略路由信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示用户态下指定CPU上策略路由信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr kernel policy**

------------------------------------------------------------------------

**[display system internal pbr kernel policy**]用于显示内核态下的策略路由信息。

【命令】

集中式设备：

**[display system internal pbr kernel policy****]\*[policy-name* \**[setup **]**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal pbr slot**]*slot-number***** **cpu** *cpu-number*  **kernel policy** \*[policy-name *\**[setup **]**]

分布式设备－IRF模式：

**[display system internal pbr chassis**]*chassis-number*** slot***slot-number***** **cpu** *cpu-number*  **kernel policy** \*[policy-name *\**[setup **]**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[policy**]*policy-name*：显示内核态下指定策略路由的信息。policy-name为策略名，为1～19个字符的字符串，区分大小写。

**[setup**]：显示内核态指定策略的接口应用信息。

**[slot*** slot-number*]：显示内核态下指定单板上的策略路由信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示内核态下指定成员设备的策略路由信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示内核态下指定成员设备/PEX的策略路由信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示内核态下指定成员设备上指定单板的策略路由信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示内核态下指定单板的策略路由信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示内核态下指定CPU上策略路由信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**策略路由 \-- 策略路由Probe配置命令 \-- display system internal pbr fib**

------------------------------------------------------------------------

**[display system internal pbr fib**]命令用来显示用户态下下一跳的配置信息。

【命令】

集中式设备：

**[display system internal pbr fib ** **vpn-instance** *vpn-instance-name* ]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal pbr slot**]*slot-number***** **cpu** *cpu-number*  **fib**  **vpn-instance** *vpn-instance-name*

分布式设备－IRF模式：

**[display system internal pbr chassis**]*chassis-number*** slot***slot-number***** **cpu** *cpu-number*  **fib**  **vpn-instance** *vpn-instance-name*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance ***vpn-instance-name*]：显示用户态下指定私网内下一跳的配置信息，不指定该参数为公网内下一跳。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。指定的VPN实例必须已经存在。

**[slot*** slot-number*]：显示用户态下指定单板指定私网内下一跳的配置信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示用户态下指定成员设备的指定私网内下一跳的配置信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示用户态下指定成员设备/PEX的指定私网内下一跳的配置信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示用户态下指定成员设备上指定单板的指定私网内下一跳的配置信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示用户态下指定单板的指定私网内下一跳的配置信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示用户态下指定CPU上指定私网内下一跳的配置信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

