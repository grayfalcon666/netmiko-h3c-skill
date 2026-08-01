<!-- CMD-INDEX
  display system internal irf global  | Probe视图          | L12
  display system internal irf msg     | Probe视图          | L44
  display system internal irf roledb  | Probe视图          | L78
  display system internal irf topodb  | Probe视图          | L110
  irf link-status auto-recovery enable | Probe视图          | L142
  irf link-status detect enable       | Probe视图          | L186
  reset system internal irf msg       | Probe视图          | L226
  display system internal pex-port verbose | Probe视图          | L258
-->

**IRF \-- IRF2 Probe命令 \-- display system internal irf global**

------------------------------------------------------------------------

**[display system internal irf global**]命令用来显示IRF的部分全局信息。

【命令】

集中式IRF设备：

**[display system internal irf global** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display system internal irf global** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）

**[chassis** *chassis-number* slot *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）

**IRF \-- IRF2 Probe命令 \-- display system internal irf msg**

------------------------------------------------------------------------

**[display system internal irf msg**]命令用来显示IRF的日志信息。

【命令】

集中式IRF设备：

**[display system internal irf msg** [ **reverse**   **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display system internal irf msg ** **reverse** ]  **chassis** *chassis-number* **slot** *slot-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reverse**]：表示反向显示信息，先显示时间新的日志，再显示时间旧的日志。不指定该参数时，表示按时间先后顺序显示信息。

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）

**IRF \-- IRF2 Probe命令 \-- display system internal irf roledb**

------------------------------------------------------------------------

**[display system internal irf roledb**]命令用来显示IRF的角色数据库信息。

【命令】

集中式IRF设备：

**[display system internal irf roledb** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display system internal irf roledb** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）

**[chassis** *chassis-number* slot *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）

**IRF \-- IRF2 Probe命令 \-- display system internal irf topodb**

------------------------------------------------------------------------

**[display system internal irf topodb**]命令用来显示IRF的拓扑数据库信息。

【命令】

集中式IRF设备：

**[display system internal irf topodb** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[display system internal irf topodb** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，则表示主设备。（集中式IRF设备）。

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）

**IRF \-- IRF2 Probe命令 \-- irf link-status auto-recovery enable**

------------------------------------------------------------------------

![说明](IRF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[irf link-status auto-recovery enable**]命令用来使能IRF链路故障恢复功能。

**[undo irf link-status auto-recovery enable**]命令用来关闭IRF链路故障恢复功能。

【命令】

**[irf link-status auto-recovery enable**]

**[undo irf link-status auto-recovery enable**]

【缺省情况】

IRF链路故障恢复功能处于使能状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能IRF链路故障恢复功能后，系统能自动对检测到的IRF链路故障尝试修复，增强系统的稳定性。

该命令仅供调试IRF链路故障恢复功能运行是否正常。如果调试结束，请输入使能命令，确保设备的IRF链路故障恢复功能处于使能状态。

需要注意的是：

·只有先使能IRF链路状态检测功能，本命令才生效。

·本命令只在IRF模式下支持。配置**undo irf link-status auto-recovery enable**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

**IRF \-- IRF2 Probe命令 \-- irf link-status detect enable**

------------------------------------------------------------------------

![说明](IRF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[irf link-status detect enable**]命令用来使能IRF链路状态检测功能。

**[undo irf link-status detect enable**]命令用来关闭IRF链路状态检测功能。

【命令】

**[irf link-status detect enable**]

**[undo irf link-status detect enable**]

【缺省情况】

IRF链路状态检测功能处于使能状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

使能IRF链路的状态检测功能后，当存在多于一条IRF物理连接时，系统会检测每条IRF物理连接是否连通，确保系统能及时发现故障链路。

该命令仅供调试IRF链路的状态检测功能运行是否正常。如果调试结束，请输入使能命令，确保设备的IRF链路状态检测功能处于使能状态。

需要注意的是，本命令只在IRF模式下支持。配置**undo irf link-status detect enable**命令并保存配置后，切换到独立运行模式，该配置将失效。即便之后再切换回IRF模式，仍需重新配置。

**IRF \-- IRF2 Probe命令 \-- reset system internal irf msg**

------------------------------------------------------------------------

**[reset system internal irf msg**]命令用来清空IRF日志消息。

【命令】

集中式IRF设备：

**[reset system internal irf msg** [ **slot** *slot-number* ]]

分布式设备－IRF模式：

**[reset system internal irf msg** [ **chassis** *chassis-number* **slot** *slot-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：表示设备在IRF中的成员编号。不指定该参数时，表示主设备。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示主控板所在的槽位号。不指定该参数时，则表示IRF中的全局主用主控板。（分布式设备－IRF模式）

**IRF \-- IRF3 Probe命令 \-- display system internal pex-port verbose**

------------------------------------------------------------------------

**[display system internal pex-port verbose**]命令用来显示PEX端口的信息，包括PEX端口的编号、描述信息、绑定的物理端口的信息等。

【命令】

集中式IRF设备：

**[display system internal pex-port verbose slot** *slot-number*]

分布式设备－IRF模式：

**[display system internal pex-port verbose chassis ***chassis-number* **slot** *slot-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：显示指定成员设备/PEX上保存的PEX端口的信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板/PEX上保存的PEX端口的信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板/PEX所在的槽位号。（分布式设备－IRF模式）

