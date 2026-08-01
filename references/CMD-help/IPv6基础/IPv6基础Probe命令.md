<!-- CMD-INDEX
  display system internal ipv6 rawip  | Probe视图          | L32
  display system internal ipv6 tcp    | Probe视图          | L76
  display system internal ipv6 udp    | Probe视图          | L120
  display system internal tcp-proxy statistics | Probe视图          | L164
  display system interval ipv6 tcp-proxy verbose | Probe视图          | L226
  reset system internal tcp-proxy statistics | Probe视图          | L274
  tcp-proxy statistics                | Probe视图          | L298
  debugging system internal nd        | Probe视图          | L336
  debugging system internal nd sub-features | Probe视图          | L368
  display system internal nd dad      | Probe视图          | L402
  display system internal nd entry    | Probe视图          | L446
  display system internal nd ifcb     | Probe视图          | L490
  display system internal nd machash  | Probe视图          | L536
  display system internal nd probe    | Probe视图          | L584
  display system internal nd rbhash   | Probe视图          | L628
  display system internal nd reload   | Probe视图          | L676
  display system internal nd rule     | Probe视图          | L720
  display system internal nd snooping | Probe视图          | L770
  display system internal nd static   | Probe视图          | L820
  display system internal nd statistics | Probe视图          | L846
  display system internal nd suppression xconnect-group verbose | Probe视图          | L890
  reset system internal nd statistics | Probe视图          | L934
  display system internal ipv6 address | Probe视图          | L978
  display system internal ipv6 pathmtu | Probe视图          | L1028
  debugging system internal ipv6 fib prefix |                  | L1080
  display system internal ipv6 fib prefix | Probe视图          | L1142
  display system internal ipv6 fib prefix entry-status | Probe视图          | L1188
  display system internal ipv6 fib prefix ipv6 | Probe视图          | L1236
-->

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 rawip**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal ipv6 rawip**]命令用来显示设备上所有IPv6 RawIP连接的摘要信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal ipv6 rawip**slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal ipv6 rawip**chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有IPv6 RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有IPv6 RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有IPv6 RawIP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 RawIP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有IPv6 RawIP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 tcp**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal ipv6 tcp**]命令用来显示设备上所有IPv6 TCP连接的摘要信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal ipv6 tcp**slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal ipv6 tcp**chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有IPv6 TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有IPv6 TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有IPv6 TCP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号， slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 TCP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有IPv6 TCP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal ipv6 udp**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal ipv6 udp**]命令用来显示设备上所有IPv6 UDP连接的摘要信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal ipv6 udp**slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal ipv6 udp**chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有IPv6 UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有IPv6 UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有IPv6 UDP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 UDP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有IPv6 UDP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6基础Probe命令 \-- display system internal tcp-proxy statistics**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal tcp-proxy statistics**]命令用来显示TCP代理的统计信息。

【命令】

集中式设备：

**[display system internal tcp-proxy statistics**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal tcp-proxy statistics**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** } ] **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[display system internal tcp-proxy statistics**[ { **all** \| **api** \| **error** \| **fsm** \| **packet** }] **chassis** *chassis-number***slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：显示所有统计信息。

**[api**]：显示API统计信息。

**[error**]：显示错误统计信息。

**[fsm**]：显示状态机统计信息。

**[packet**]：显示报文统计信息。

**[slot**]*slot-number*：显示指定单板上的IPv6 TCP代理的统计信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。如果未指定本参数，则显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上IPv6 TCP代理的统计的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的IPv6 TCP代理的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的IPv6 TCP代理的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板上的IPv6 TCP代理的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv6 TCP代理的统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以显示IPv4 TCP和IPv6 TCP代理的统计信息。

**IPv6基础 \-- IPv6基础Probe命令 \-- display system interval ipv6 tcp-proxy verbose**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system interval ipv6 tcp-proxy verbose**]命令用来显示IPv6 TCP代理连接的详细信息。

【命令】

集中式设备：

**[display system interval ipv6 tcp-proxy verbose**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system interval ipv6 tcp-proxy verbose slot ***slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system interval ipv6 tcp-proxy verbose chassis ***chassis-number ***slot** *slot-number* [**cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有IPv6 TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有IPv6 TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有IPv6 TCP代理连接的详细信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号， slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有IPv6 TCP代理连接的详细信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有IPv6 TCP代理连接的详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6基础Probe命令 \-- reset system internal tcp-proxy statistics**

------------------------------------------------------------------------

**[reset system internal tcp-proxy statistics**]命令用来清除TCP代理连接的统计信息。

【命令】

**[reset system internal tcp-proxy statistics**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令可以清除IPv4 TCP和IPv6 TCP代理的统计信息。

**IPv6基础 \-- IPv6基础Probe命令 \-- tcp-proxy statistics**

------------------------------------------------------------------------

![说明](IPv6基础Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tcp-proxy statistics**]命令用来开始或停止TCP代理统计计数。

【命令】

**[tcp-proxy statistics**[ [ **off** \| **on** }]]

【缺省情况】]

不进行IPv6 TCP代理统计计数。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[off**]：表示停止IPv6 TCP代理统计计数。

**[on**]：表示开始IPv6 TCP代理统计计数。

【使用指导】

本命令可以开始或停止IPv4 TCP和IPv6 TCP代理统计计数。

**IPv6基础 \-- ND Probe命令 \-- debugging system internal nd**

------------------------------------------------------------------------

【命令】

**[debugging system internal nd**[ { **notify** \| **sync** }]]

**[undo debugging system internal nd**[ { **notify** \| **sync** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[notify**]**：**表示邻居发现的通知调试开关。

**[sync**]**：** 表示邻居发现的同步调试开关。

【描述】

**[debugging system internal nd**]命令用来打开邻居发现的调试信息开关。**undo debugging system internal nd**命令用来关闭邻居发现的外部通知调试信息开关。

缺省情况下，邻居发现的调试信息开关处于关闭状态。

**IPv6基础 \-- ND Probe命令 \-- debugging system internal nd sub-features**

------------------------------------------------------------------------

【命令】

**[debugging system internal nd sub-features**[ { **all** \| **event** \| **packet** }]]

**[undo debugging system internal nd sub-features**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示ND子特性的所有调试信息开关。

**[event**]：表示ND子特性的事件调试信息开关。

**[packet**]：表示ND子特性的报文调试信息开关。

【描述】

**[debugging system internal nd sub-features**]命令用来打开ND子特性的调试开关。**undo debugging system internal nd sub-features**命令用来关闭ND子特性的调试开关。

缺省情况下，ND子特性的调试开关处于关闭状态。

**IPv6基础 \-- ND Probe命令 \-- display system internal nd dad**

------------------------------------------------------------------------

**[display system internal nd dad**]命令用来显示DAD链信息。

【命令】

集中式设备：

**[display system internal nd dad**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd dad** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd dad** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的DAD链信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的DAD链信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的DAD链信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的DAD链信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的DAD链信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的DAD链信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd entry**

------------------------------------------------------------------------

**[display system internal nd entry**]命令用来显示各板上的ND表项信息。

【命令】

集中式设备：

**[display system internal nd entry**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd entry** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd entry** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ND表项信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ND表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ND表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ND表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ND表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的ND表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd ifcb**

------------------------------------------------------------------------

**[display system internal nd ifcb**]命令用来显示接口的ND控制块信息。

【命令】

集中式设备：

**[display system internal nd ifcb interface ***interface-type interface-number*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd ifcb interface*** interface-type interface-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd ifcb interface** *interface-type interface-number * **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的ND控制块信息。*interface-type interface-number*为接口类型和接口编号。

**[slot ***slot-number*]：显示指定单板的ND控制块信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ND控制块信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ND控制块信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ND控制块信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ND控制块信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的ND控制块信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd machash**

------------------------------------------------------------------------

**[display system internal nd machash**]命令用来显示各板上的machash表项。

【命令】

集中式设备：

**[display system internal nd machash vlan ***vlan-id ipv6-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd machash vlan ***vlan-id ipv6-address* **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd machash vlan ***vlan-id ipv6-address*** chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]:显示指定VLAN的信息。*vlan-id*表示指定VLAN的编号。

*[IPv6-address*]：指定IPv6地址。

**[slot ***slot-number*]：显示指定单板的machash表项，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的machash表项，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的machash表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的machash表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的machash表项。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的machash表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd probe**

------------------------------------------------------------------------

**[display system internal nd probe**]命令用来显示探测链信息。

【命令】

集中式设备：

**[display system internal nd probe**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd probe** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd probe** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的探测链信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的探测链信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的探测链信息，*slot-number*表示设备在IRF中的成员编号或PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的探测链信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的探测链信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的探测链信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd rbhash**

------------------------------------------------------------------------

**[display system internal nd rbhash**]命令用来显示指定板上rbhash表项信息。

【命令】

集中式设备：

**[display system internal nd rbhash vlan ***vlan-id ipv6-address*]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd rbhash vlan ***vlan-id ipv6-address ***slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd rbhash vlan ***vlan-id ipv6-address*** chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan ***vlan-id*]:显示指定VLAN上rbhash表项信息。*vlan-id*表示指定VLAN的编号。

*[ipv6-address*]：显示指定IPv6地址上rbhash表项信息。

**[slot ***slot-number*]：显示指定单板的rbhash表项信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的rbhash表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的rbhash表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：表示指定成员设备上指定单板的rbhash表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的rbhash表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的rbhash表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd reload**

------------------------------------------------------------------------

**[display system internal nd reload**]命令用来显示重刷链信息。

【命令】

集中式设备：

**[display system internal nd reload**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd reload** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd reload** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的重刷链信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的重刷链信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的重刷链信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的重刷链信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的重刷链信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的重刷链信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd rule**

------------------------------------------------------------------------

**[display system internal nd rule**]命令用来显示ND规则信息。

【命令】

集中式设备：

**[display system internal nd rule ***address* }]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd rule ***address* } **slot**]* slot-number  * **cpu** *cpu-number*

分布式设备－IRF模式：

**[display system internal nd rule ***address* } **chassis**] *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：显示所有ND规则信息。

**[interface **]*interface-type interface-number*：显示指定接口的ND规则信息，*interface-type interface-number*表示接口类型和接口编号。

*[ipv6-*]*address*：显示的指定IPv6地址的ND规则信息。

**[slot**]* slot-number*：显示指定单板ND规则信息，*slot-number*表示单板所在的槽位号。（分布式设备---独立运行模式）

**[slot**]* slot-number*：显示指定成员设备的ND规则信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]* slot-number*：显示指定成员设备/PEX的ND规则信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的ND规则信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备---IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的ND规则信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备---IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ND规则信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd snooping**

------------------------------------------------------------------------

**[display system internal nd snooping**]命令用来显示ND Snooping表项信息。

【命令】

集中式设备：

**[display system internal nd snooping **[[ **count** \| **global** \| **link-local** ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd snooping slot***slot-number *[ **cpu** *cpu-number*  [ **count** \| **global** \| **link-local** ]]]

分布式设备－IRF模式：

**[display system internal nd snooping chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  [ **count** \| **global** \| **link-local** ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ND Snooping表项信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ND Snooping表项信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ND Snooping表项信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ND Snooping表项信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ND Snooping表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的ND Snooping表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[count**]：显示ND Snooping表项的总个数。

**[global       **]：显示表项地址为全球单播地址的ND Snooping表项信息。

**[link-local**]：显示表项地址为链路本地地址的ND Snooping表项信息。

**IPv6基础 \-- ND Probe命令 \-- display system internal nd static**

------------------------------------------------------------------------

**[display system internal nd static**]命令用来显示ND静态配置。

【命令】

**[display system internal nd static ***ipv6-address ***interface ***interface-type interface-number*]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[IPv6-address*]:指定IPv6地址。

**[interface*** interface-type interface-number*]：显示指定接口的信息。*interface-type interface-number*为接口类型和接口编号。

**IPv6基础 \-- ND Probe命令 \-- display system internal nd statistics**

------------------------------------------------------------------------

**[display system internal nd statistics**]命令用来显示各板上的ND统计信息。

【命令】

集中式设备：

**[display system internal nd statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd statistics** **slot** *slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal nd statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ND统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ND统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ND统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ND统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ND统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的ND统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- display system internal nd suppression xconnect-group verbose**

------------------------------------------------------------------------

**[display system internal nd suppression xconnect-group verbose**]命令用来显示ND泛洪抑制表项的详细信息。

【命令】

集中式设备：

**[display system internal nd suppression xconnect-group verbose**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal nd suppression xconnect-group verbose** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal nd suppression xconnect-group verbose** [ **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：显示指定单板的ND泛洪抑制表项的详细信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ND泛洪抑制表项的详细信息。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的ND泛洪抑制表项的详细信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的ND泛洪抑制表项的详细信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的ND泛洪抑制表项的详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的ND泛洪抑制表项的详细信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定成员设备上指定单板的ND泛洪抑制表项的详细信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的ND泛洪抑制表项的详细信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：显示指定单板的ND泛洪抑制表项的详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的ND泛洪抑制表项的详细信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的ND泛洪抑制表项的详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- ND Probe命令 \-- reset system internal nd statistics**

------------------------------------------------------------------------

**[reset system internal nd statistics**]命令用来清除各板上的ND统计信息。

【命令】

集中式设备：

**[reset system internal nd statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal nd statistics slot ***slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[reset system internal nd statistics** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot ***slot-number*]：清除指定单板的ND统计信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：清除指定成员设备的ND统计信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX的ND统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX对应的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定成员设备上指定单板的ND统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis ***chassis-number ***slot ***slot-number*]：清除指定单板的ND统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：清除指定CPU的ND统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6地址管理 Probe命令 \-- display system internal ipv6 address**

------------------------------------------------------------------------

**[display system internal ipv6 address**]命令用来显示IPv6地址详细信息

【命令】

集中式设备：

**[display system internal ipv6 address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ipv6-address*  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ipv6-address*   **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal ipv6 address** [ **vpn-instance** *vpn-instance-name*   **interface** *interface-type interface-number*   *ipv6-address*   **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：显示的指定IPv6地址。

**[vpn-instance**]* vpn-instance-name*：显示指定VPN的IPv6地址。

**[interface **]*interface-type interface-number*：显示指定接口的IPv6地址，*interface-type interface-number*表示接口类型和接口编号。

**[slot**] *slot-number*：显示指定单板上的IPv6地址，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6地址。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv6地址，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的IPv6地址。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IPv6地址，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的IPv6地址。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6地址，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6地址。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6地址。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的IPv6地址。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的IPv6地址。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- IPv6 PathMTU Probe命令 \-- display system internal ipv6 pathmtu**

------------------------------------------------------------------------

**[display system internal ipv6 pathmtu**]命令用来显示IPv6的PMTU信息，信息全局同步。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 pathmtu** [ **vpn-instance** *vpn-instance-name*  { *ipv6-address* \| { **all** \| **dynamic** \| **static** }  **count**  }  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[display system internal ipv6 pathmtu **[ **vpn-instance** *vpn-instance-name*  { *ipv6-address* \| { **all** \| **dynamic** \| **static** }  **count**  }  **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN的IPv6 PMTU信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的IPv6 PMTU信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[ipv6-address*]：显示到达指定IPv6地址的PMTU信息。

**[all**]：显示所有公网的PMTU信息。

**[dynamic**]：显示所有动态PMTU信息。

**[static**]：显示所有静态PMTU信息。

**[count**]：显示PMTU表项数目。

**[slot** *slot-number*]：显示指定单板上的所有PMTU表项。*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上所有PMTU表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的所有PMTU表项。*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上所有PMTU表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的所有PMTU表项。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上所有PMTU表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板上的所有PMTU表项。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板的槽位号。如果未指定本参数，则显示所有单板上的所有PMTU表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的所有PMTU表项。*chassis-number*表示设备在IRF中的成员编号或者PEX的虚拟框号，*slot-number*表示单板或PEX的槽位号。如果未指定本参数，则显示所有单板上的所有PMTU表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU上的所有PMTU表项。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- Fib6 Probe命令 \-- debugging system internal ipv6 fib prefix**

------------------------------------------------------------------------

**[debugging system internal ipv6 fib prefix**]命令用来打开IPv6 FIB调试信息开关。

**[undo debugging system internal ipv6 fib prefix**]命令用来关闭IPv6 FIB调试信息开关。

【命令】

集中式设备：

**[debugging system internal ipv6 fib prefix**[ { **all** \| **message** \| **hardware** }]]

**[undo debugging system internal ipv6 fib prefix**[ { **all** \| **message** \| **hardware** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[debugging system internal ipv6 fib prefix**[ { **all** \| **message** \| **hardware** } **slot** ]]slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

**[undo debugging system internal ipv6 fib prefix**[ { **all** \| **message** \| **hardware** } **slot** ]]slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

**[debugging system internal ipv6 fib prefix**[ { **all** \| **message** \| **hardware** } **chassis** ]]chassis-number{.commandparameterChar} **slot** *slot-number* [ **cpu** *cpu-number* ]

**[undo debugging system internal ipv6 fib prefix **[{ **all** \| **message** \| **hardware** } **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ]]]

【缺省情况】

IPv6 FIB调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：打开所有调试开关。

**[message**]：打开前缀消息调试开关，打印路由下发和板间同步的IPv6 FIB前缀消息。

**[hardware**]：打开下驱动信息调试开关，打印下发驱动信息以及驱动返回的消息。

**[slot ***slot-number*]：打开指定单板的IPv6 FIB调试信息开关，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：打开指定成员设备的IPv6 FIB调试信息开关，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：打开指定成员设备/PEX的IPv6 FIB调试信息开关，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定成员设备上指定单板的IPv6 FIB调试信息开关，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定单板的IPv6 FIB调试信息开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：打开指定CPU的IPv6 FIB调试信息开关。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix**

------------------------------------------------------------------------

**[display system internal ipv6 fib prefix**]命令用来显示IPv6 FIB前缀基本信息。

【命令】

集中式设备：

**[display system internal ipv6 fib prefix ** **vpn-instance** ]vpn-instance-name {.commandparameterChar}

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 fib prefix** [ **vpn-instance** ]vpn-instance-name]{.commandparameterChar}  **slot** slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

**[display system internal ipv6 fib prefix ****vpn-instance** ]*vpn-instance-name***** **chassis** chassis-number{.commandparameterChar}** slot**slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv6 FIB前缀基本信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv6 FIB前缀基本信息。

**[slot ***slot-number*]：显示指定单板的IPv6 FIB前缀基本信息，*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：显示指定成员设备的IPv6 FIB前缀基本信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX的IPv6 FIB前缀基本信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv6 FIB前缀基本信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv6 FIB前缀基本信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的IPv6 FIB前缀基本信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix entry-status**

------------------------------------------------------------------------

**[display system internal ipv6 fib prefix entry-status**]命令用来显示下驱动失败或者待老化的IPv6 FIB表项信息信息。

【命令】

集中式设备：

**[display system internal ipv6 fib prefix** **entry-status**] status {.commandparameterChar} **vpn-instance**  vpn-instance-name {.commandparameterChar}

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 fib prefix** **entry-status**] status{.commandparameterChar} [ **vpn-instance** vpn-instance-name]{.commandparameterChar}  **slot** slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

**[display system internal ipv6 fib prefix entry-status **]status {.commandparameterChar} **vpn-instance**  vpn-instance-name{.commandparameterChar}  **chassis** chassis-number{.commandparameterChar}** slot**slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv6 FIB表项信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv6 FIB表项信息。

**[entry-status*** status*]：用于匹配IPv6 FIB表项；取值范围为\<A,F\>，"A"表示需要被老化的IPv6 FIB表项，"F"表示下刷驱动失败的IPv6 FIB表项。

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的下驱动失败或者待老化的IPv6 FIB表项信息，*slot-number*表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备的下驱动失败或者待老化的IPv6 FIB表项信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备/PEX的下驱动失败或者待老化的IPv6 FIB表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备上指定单板的下驱动失败或者待老化的IPv6 FIB表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的下驱动失败或者待老化的IPv6 FIB表项信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定CPU的下驱动失败或者待老化的IPv6 FIB表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IPv6基础 \-- Fib6 Probe命令 \-- display system internal ipv6 fib prefix ipv6**

------------------------------------------------------------------------

**[display system internal ipv6 fib prefix*** ipv6*]命令用来显示IPv6 FIB前缀详细信息。

【命令】

集中式设备：

**[display system internal ipv6 fib prefix** [ **vpn-instance** ]vpn-instance-name ]{.commandparameterChar} ipv6 {.commandparameterChar} *prefix-length*

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ipv6 fib prefix** [ **vpn-instance** ]vpn-instance-name]{.commandparameterChar}  ipv6 {.commandparameterChar} *prefix-length*  **slot** slot-number {.commandparameterChar} **cpu** cpu-number {.commandparameterChar}[]{.commandparameterChar}

分布式设备－IRF模式：

**[display system internal ipv6 fib prefix ** **vpn-instance**]*****vpn-instance-name*********ipv6{.commandparameterChar}****\*[prefix-length* ] **chassis** chassis-number{.commandparameterChar}** slot**slot-number{.commandparameterChar} [ **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv6 FIB前缀详细信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv6 FIB前缀详细信息。

*[ipv6*]：显示目的地址为指定IPv6地址的IPv6 FIB前缀详细信息。

*[prefix-length*]：指定IPv6{.commandparameterChar}地址的前缀{.commandparameterChar}长度，取值范围为0\~128。{.commandkeywordsChar}

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的IPv6 FIB前缀详细信息，*slot-number*表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备的IPv6 FIB前缀详细信息，*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备/PEX的IPv6 FIB前缀详细信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定成员设备上指定单板的{.commandparameterChar}IPv6 FIB前缀详细信息，chassis-number{.commandparameterChar}表示设备在{.commandparameterChar}IRF{.commandparameterChar}中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。{.commandparameterChar}（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示指定单板的{.commandparameterChar}IPv6 FIB前缀详细信息。chassis-number{.commandparameterChar}表示设备在{.commandparameterChar}IRF{.commandparameterChar}中的成员编号或者{.commandparameterChar}PEX{.commandparameterChar}对应的虚拟框号，slot-number{.commandparameterChar}表示单板或{.commandparameterChar}PEX{.commandparameterChar}所在的槽位号。{.commandparameterChar}（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示指定{.commandparameterChar}CPU{.commandparameterChar}的{.commandparameterChar}IPv6 FIB前缀详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）
