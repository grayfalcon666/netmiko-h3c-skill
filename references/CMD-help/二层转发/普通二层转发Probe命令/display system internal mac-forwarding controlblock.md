
**二层转发 \-- 普通二层转发Probe命令 \-- display system internal mac-forwarding controlblock**

------------------------------------------------------------------------

![说明](二层转发Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal mac-forwarding controlblock**]命令用来显示二层转发的接口控制信息。

【命令】

集中式设备：

**[display system internal mac-forwarding controlblock interface***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-forwarding controlblock interface***interface-type interface-number* **slot** *slot-number * **cpu**]* cpu-number*

分布式设备－IRF模式：

**[display system internal mac-forwarding controlblock interface***interface-type interface-number* **chassis** *chassis-number* **slot**]*****slot-number * **cpu*** cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的二层转发控制信息。其中，*interface-type interface-number*为指定接口类型和接口编号。

**[slot** *slot-number*]：显示指定单板的二层转发控制信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的二层转发控制信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的二层转发控制信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的二层转发控制信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的二层转发控制信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的二层转发控制信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**二层转发 \-- 快速二层转发Probe命令 \-- display system internal mac-forwarding cache ip verbose**

------------------------------------------------------------------------

![说明](二层转发Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal mac-forwarding cache ip verbose**]命令用来显示IP快转表项的详细内容。

【命令】

集中式设备：

**[display system internal mac-forwarding cache ip** [ *ip-address*  **verbose**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-forwarding cache ip** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

分布式设备－IRF模式：

**[display system internal mac-forwarding cache** **ip** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：显示指定IP地址的快速转发表信息。如果不指定*ip-address*，将显示所有快速转发表信息。

**[slot**]*slot-number*：显示指定单板的快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的快速转发表信息。*slot-number*表示单板的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果不指定**slot***slot-number*，将显示所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**二层转发 \-- 快速二层转发Probe命令 \-- display system internal mac-forwarding cache ipv6 verbose**

------------------------------------------------------------------------

![说明](二层转发Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal mac-forwarding cache** **ipv6 verbose**]命令用来显示分布式各板IPv6快转表项的详细内容。

【命令】

集中式设备：

**[display system internal mac-forwarding cache ipv6** [ *ipv6-address*  **verbose**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal mac-forwarding cache ipv6** [ *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

分布式设备－IRF模式：

**[display system internal mac-forwarding cache ipv6** [ *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：显示指定IPv6地址的IPv6快速转发表信息。如果不指定*ipv6-address*，将显示所有IPv6地址的IPv6快速转发表信息。

**[slot**]*slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上IPv6快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**二层转发 \-- Bridge快速转发Probe命令 \-- display system internal bridge cache ip verbose**

------------------------------------------------------------------------

![说明](二层转发Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal bridge cache ip verbose**]命令用来显示Bridge转发创建的IP快速转发表的详细内容。

【命令】

集中式设备：

**[display system internal bridge cache ip** [ *ip-address*  **verbose**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal bridge cache ip** [ *ip-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

分布式设备－IRF模式：

**[display system internal bridge cache** **ip** [ *ip-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：显示指定IP地址的快速转发表信息。如果不指定*ip-address*，将显示所有快速转发表信息。

**[slot**]*slot-number*：显示指定单板的快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的快速转发表信息。*slot-number*表示单板的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的快速转发表信息。*slot-number*表示设备在IRF中的成员编号。如果不指定**slot***slot-number*，将显示所有成员设备的快速转发表信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的快速转发表信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**二层转发 \-- Bridge快速转发Probe命令 \-- display system internal bridge cache ipv6 verbose**

------------------------------------------------------------------------

![说明](二层转发Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal bridge cache ipv6 verbose**]命令用来显示Bridge转发创建的IPv6快速转发表的详细内容。

【命令】

集中式设备：

**[display system internal bridge cache ipv6** [ *ipv6-address*  **verbose**]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal bridge cache ipv6** [ *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

分布式设备－IRF模式：

**[display system internal bridge cache** **ipv6** [ *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ] **verbose**]]

【视图】

probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：显示指定IPv6地址的IPv6快速转发表信息。如果不指定*ipv6-address*，将显示所有IPv6地址的IPv6快速转发表信息。

**[slot**]*slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的IPv6快速转发表信息。如果不指定**slot***slot-number*，将显示所有成员设备/PEX的IPv6快速转发表信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备上指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板的IPv6快速转发表信息。如果不指定**chassis***chassis-number***slot***slot-number*，将显示所有单板的IPv6快速转发表信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu**]*cpu-number*：显示指定CPU上IPv6快速转发表信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

