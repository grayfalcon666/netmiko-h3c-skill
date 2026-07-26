
**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal rawip**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal rawip**]命令用来显示设备上所有RawIP连接的摘要信息。

【命令】

集中式设备：

**[display system internal rawip**]

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal **rawip{.commandkeywordsChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal **rawip{.commandkeywordsChar}chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}  **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有RawIP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有RawIP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有RawIP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有RawIP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal tcp**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal tcp**]命令用来显示设备上所有TCP连接的摘要信息。

【命令】

集中式设备：

display {.commandkeywordsChar}**system internal **tcp{.commandkeywordsChar}

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal **tcp{.commandkeywordsChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal **tcp{.commandkeywordsChar}chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有TCP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有TCP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有TCP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有TCP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal tcp-proxy statistics**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

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

**[slot**]*slot-number*：显示指定单板上的TCP代理的统计信息，*slot-number*表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。如果未指定本参数，则显示所有单板上的信息。（分布式设备－独立运行模式）

**[slot**]*slot-number*：显示指定成员设备上TCP代理的统计的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，则显示所有成员设备上的信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot**]*slot-number*：显示指定成员设备/PEX上的TCP代理的统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，则显示所有成员设备/PEX上的信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定成员设备指定单板上的TCP代理的统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis**]*chassis-number***slot***slot-number*：显示指定单板上的TCP代理的统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，则显示所有单板上的表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的TCP代理的统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

本命令可以显示IPv4 TCP和IPv6 TCP代理的统计信息。

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system interval tcp-proxy verbose**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system interval tcp-proxy verbose**]命令用来显示TCP代理连接的详细信息。

【命令】

集中式设备：

**[display system interval tcp-proxy verbose**]

分布式设备－独立运行模式/集中式IRF设备：

**[display system interval tcp-proxy verbose slot ***slot-number* [ **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system interval tcp-proxy verbose chassis ***chassis-number ***slot** *slot-number* [**cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有TCP代理连接的详细信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有TCP代理连接的详细信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号， slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有TCP代理连接的详细信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有TCP代理连接的详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP性能优化 \-- IP性能优化Probe配置命令 \-- display system internal udp**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display system internal udp**]命令用来显示设备上所有UDP连接的摘要信息。

【命令】

集中式设备：

**[display system internal udp**]

分布式设备－独立运行模式/集中式IRF设备：

display {.commandkeywordsChar}**system internal **udp{.commandkeywordsChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

分布式设备－IRF模式：

display {.commandkeywordsChar}**system internal **udp{.commandkeywordsChar}chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number {.commandparameterChar} **cpu** cpu-number{.commandparameterChar}[ ]{.commandparameterChar}

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备上获取的所有UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备/PEX上获取的所有UDP连接的摘要信息[。]slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定成员设备的指定单板上获取的所有UDP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号， slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar}chassis-number{.commandparameterChar}slot{.commandkeywordsChar}slot-number{.commandparameterChar}：显示从指定单板上获取的所有UDP连接的摘要信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu **]*cpu-number*：显示从指定CPU上获取的所有UDP连接的摘要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP性能优化 \-- IP性能优化Probe配置命令 \-- reset system internal tcp-proxy statistics**

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

**IP性能优化 \-- IP性能优化Probe配置命令 \-- tcp-proxy statistics**

------------------------------------------------------------------------

![说明](IP性能优化Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[tcp-proxy statistics**]命令用来开始或停止TCP代理统计计数。

【命令】

**[tcp-proxy statistics**[ [ **off** \| **on** }]]

【缺省情况】]

不进行TCP代理统计计数。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[off**]：表示停止TCP代理统计计数。

**[on**]：表示开始TCP代理统计计数。

【使用指导】

本命令可以开始或停止IPv4 TCP和IPv6 TCP代理统计计数。
