
**802.11 \-- 802.11命令 \-- display system internal dot11 characteristics**

------------------------------------------------------------------------

!(802.11%20Probe命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备实际情况为准。

**[display system internal dot11 characteristics**]命令用来显示802.11侦听特征的统计信息和详细信息。

【命令】

集中式设备：

**[display system internal dot11 characteristics **[{ **bss** *bssid* \| **interface wlan-radio** *interface-number* }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal dot11 characteristics **[{ **bss** *bssid* \| **interface wlan-radio ** *interface-number* } **slot** *slot-number* [ **cpu** *cpu-number* ]]]

分布式设备－IRF模式：

**[display system internal dot11 characteristics **[{ **bss** *bssid* \| **interface wlan-radio** *interface-number* } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[bss ***bssid*]：显示BSS实体的特征统计信息和详细信息，包括BSS接收报文方向和发送报文方向。

**[wlan-radio ***interface-number*]：显示指定射频接口的特征统计信息和详细信息。

**[slot ***slot-number*]：显示指定单板的特征统计信息和详细信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的特征统计信息和详细信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的特征统计信息和详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的特征统计信息和详细信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的特征统计信息和详细信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或者PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**802.11 \-- 802.11命令 \-- display system internal dot11 verbose**

------------------------------------------------------------------------

![说明](802.11%20Probe命令.files/image001.png)

本命令的支持情况与设备型号有关，请以设备实际情况为准。

**[display system internal dot11 verbose**]命令用来显示802.11协议socket的详细信息。

【命令】

集中式设备：

**[display system internal dot11 verbose**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal dot11** **slot** *slot-number* [ **cpu** *cpu-number*  **verbose**]]

分布式设备－IRF模式：

**[display system internal dot11 chassis ***chassis-number*** slot ***slot-number * **cpu** *cpu-number* ] **verbose**

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的socket的详细信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的socket的详细信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的socket的详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定成员设备上的指定单板的socket的详细信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number* **slot** *slot-number*]：显示指定单板的socket的详细信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或者PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：表示CPU的编号。只有指定的slot支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。
