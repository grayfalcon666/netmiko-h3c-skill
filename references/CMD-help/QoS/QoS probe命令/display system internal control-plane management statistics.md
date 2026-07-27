<!-- CMD-INDEX
  display system internal control-plane management statistics | Probe视图          | L8
  display system internal control-plane statistics | Probe视图          | L32
  reset system internal control-plane management statistics | Probe视图          | L78
  reset system internal control-plane statistics | Probe视图          | L102
-->

**QoS \-- QoS probe命令 \-- display system internal control-plane management statistics**

------------------------------------------------------------------------

![说明](QoS%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal control-plane management statistics**]命令用来显示管理口控制平面报文的统计信息。

【命令】

**[display system internal control-plane management statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**QoS \-- QoS probe命令 \-- display system internal control-plane statistics**

------------------------------------------------------------------------

![说明](QoS%20Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal control-plane statistics**]命令用来显示控制平面报文的统计信息。

【命令】

集中式设备：

**[display system internal control-plane statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal control-plane statistics** **slot** *slot-number* ]

分布式设备－IRF模式：

**[display system internal control-plane statistics chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：显示指定单板的控制平面的报文统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示指定成员设备的控制平面的报文统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的控制平面的报文统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-numbe*r]：显示指定成员设备上指定单板的控制平面的报文统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的控制平面的报文统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**QoS \-- QoS probe命令 \-- reset system internal control-plane management statistics**

------------------------------------------------------------------------

![说明](QoS%20Probe命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset system internal control-plane management statistics**]命令用来清除管理口控制平面报文的统计信息。

【命令】

**[reset system internal control-plane management statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**QoS \-- QoS probe命令 \-- reset system internal control-plane statistics**

------------------------------------------------------------------------

![说明](QoS%20Probe命令.files/image003.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[reset system internal control-plane statistics**]命令用来清除控制平面报文的统计信息

【命令】

集中式设备：

**[reset system internal control-plane statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal control-plane statistics** **slot** *slot-number* ]

分布式设备－IRF模式：

**[reset system internal control-plane statistics chassis** *chassis-number* **slot** *slot-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot*** slot-number*]：清除指定单板的控制平面的报文统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot*** slot-number*]：清除指定成员设备的控制平面的报文统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX上的控制平面的报文统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-numbe*r]：清除指定成员设备上指定单板的控制平面的报文统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上的控制平面的报文统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

