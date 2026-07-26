
**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix**

------------------------------------------------------------------------

**[display system internal fib prefix**]命令用来显示IPv4 FIB前缀基本信息。

【命令】

集中式设备：

**[display system internal fib prefix **[[ **topology** *topo-name* \| **vpn-instance** [vpn-instance-name ]{.commandparameterChar}]]]

分布式设备－独立运行模式/集中式IRF设备：

display system internal fib prefix  topology *topo-name*[\|] vpn-instance [vpn-instance-name]{.commandparameterChar} slot slot-number {.commandparameterChar} cpu *cpu-number*

分布式设备－IRF模式：

**[display system internal fib prefix **\**[topology**[ *topo-name* \| **vpn-instance** *vpn-instance-name* ] **chassis** chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[topology** *topo-name*]：显示指定拓扑的IPv4 FIB前缀基本信息。*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；取值为**base**时表示公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv4 FIB前缀基本信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv4 FIB前缀基本信息。

**[slot** *slot-number*]：显示指定单板上的IPv4 FIB前缀基本信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv4 FIB前缀基本信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IPv4 FIB前缀基本信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv4 FIB前缀基本信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv4 FIB前缀基本信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的IPv4 FIB前缀基本信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix ip**

------------------------------------------------------------------------

**[display system internal fib** **prefix** *ip*]命令用来显示IPv4 FIB前缀详细信息。

【命令】

集中式设备：

display system internal fib prefix vpn-instancevpn-instance-name{.commandparameterChar} ip {.commandparameterChar}[[*mask* \| *mask-length*]]

分布式设备－独立运行模式/集中式IRF设备：

display system internal fib prefix vpn-instancevpn-instance-name{.commandparameterChar} ip {.commandparameterChar}\*[mask*[ \| *mask-length*]]slot slot-number{.commandparameterChar} [ cpu *cpu-number*]

分布式设备－IRF模式：

**[display system internal fib prefix ** **vpn-instance**]*****vpn-instance-name*********ip{.commandparameterChar}****[[ *mask* \| *mask-length* ]]  **chassis** [chassis-number{.commandparameterChar} **slot** slot-number{.commandparameterChar}  **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的IPv4 FIB前缀详细信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv4 FIB前缀详细信息。

*[ip*]：显示指定IP地址的IPv4 FIB前缀详细信息。

*[mask*]：IP地址掩码。

*[mask-length*]：IP地址掩码长度，即掩码中连续"1"的个数。

**[slot** *slot-number*]：显示指定单板上的IPv4 FIB前缀详细信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv4 FIB前缀详细信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX上的IPv4 FIB前缀详细信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的IPv4 FIB前缀详细信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的IPv4 FIB前缀详细信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的IPv4 FIB前缀详细信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib prefix entry-status**

------------------------------------------------------------------------

**[display system internal fib prefix entry-status**]命令用来显示下驱动失败或者待老化的IPv4 FIB表项信息。

【命令】

集中式设备：

display system internal fibprefix [vpn-instancevpn-instance-name]{.commandparameterChar} entry-status status{.commandparameterChar}

分布式设备－独立运行模式/集中式IRF设备：

display system internal fib prefix vpn-instancevpn-instance-name{.commandparameterChar}  entry-status status{.commandparameterChar}slot slot-number{.commandparameterChar} [ cpu *cpu-number*]

分布式设备－IRF模式：

**[display system internal fib** **prefix** [ **vpn-instance** [vpn-instance-name{.commandparameterChar}] **entry-status{.commandparameterChar}**status{.commandparameterChar} **chassis** chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：显示指定VPN实例的下驱动失败或者待老化的IPv4 FIB表项信息。*vpn-instance-name*为VPN实例的名称，为1～31个字符的字符串，区分大小写。如果不指定VPN实例，则显示公网的IPv4 FIB表项信息。

**[entry-status*** status*]：用于匹配FIB表项；取值范围为\<A,F\>，"A"表示需要被老化的IPv4 FIB表项信息，"F"表示下刷驱动失败的IPv4 FIB表项信息。

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的下驱动失败或者待老化的IPv4 FIB表项信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上的下驱动失败或者待老化的IPv4 FIB表项信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX上的下驱动失败或者待老化的IPv4 FIB表项信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的下驱动失败或者待老化的IPv4 FIB表项信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的下驱动失败或者待老化的IPv4 FIB表项信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的下驱动失败或者待老化的IPv4 FIB表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib running-status**

------------------------------------------------------------------------

**[display system internal fib running-status**]命令用来显示IPv4 FIB、IPv6 FIB、VN全局信息。

【命令】

集中式设备：

display system internal fibrunning-status

分布式设备－独立运行模式/集中式IRF设备：

display system internal fibrunning-statusslot slot-number{.commandparameterChar} [ cpu *cpu-number*]

分布式设备－IRF模式：

**[display system internal fib ****running-status** **chassis** [chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的IPv4 FIB、IPv6 FIB、VN全局信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上的IPv4 FIB、IPv6 FIB、VN全局信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX上的IPv4 FIB、IPv6 FIB、VN全局信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的IPv4 FIB、IPv6 FIB、VN全局信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的IPv4 FIB、IPv6 FIB、VN全局信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的IPv4 FIB、IPv6 FIB、VN全局信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib statistics**

------------------------------------------------------------------------

**[display system internal fib statistics**]命令用来显示IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。

【命令】

集中式设备：

display system internal fibstatistics

分布式设备－独立运行模式/集中式IRF设备：

display system internal fib statisticsslot slot-number{.commandparameterChar} [cpu *cpu-number* ]

分布式设备－IRF模式：

**[display system internal fib statistics** **chassis** [chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX上的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的IPv4 FIB、IPv6 FIB、VN表项操作的统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn**

------------------------------------------------------------------------

**[display system internal fib vn**]命令用来显示VN表项信息。

【命令】

集中式设备：

display system internal fib vn next-hop next-hop{.commandparameterChar}

display system internal fib vn  id[ [id \|]{.commandparameterChar}]**index index{.commandparameterChar} }

分布式设备－独立运行模式/集中式IRF设备：

display system internal fibvn next-hop next-hop{.commandparameterChar} slot slot-number {.commandparameterChar}cpu *cpu-number*

display system internal fib vn  id[ [id \| ]{.commandparameterChar}]index index{.commandparameterChar} } slot slot-number {.commandparameterChar}cpu *cpu-number*

分布式设备－IRF模式：

**[display system internal fib vn** [ **next-hop** *next-hop*  **chassis** chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

**[display system internal fib vn**[ { **id** *id \|* **index** *index* } **chassis** [chassis-number]{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[id ***id*]：按指定VN ID显示VN表项详细信息。

**[index*** index*]：按指定VN索引显示VN表项详细信息。

**[next-hop** *next-hop*]：显示指定下一跳的VN表项基本信息，可以输入IPv4、IPv6地址。

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的VN表项信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上的VN表项信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX上的VN表项信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的VN表项信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的VN表项信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的VN表项信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn reference**

------------------------------------------------------------------------

**[display system internal fib vn reference**]命令用来显示前缀关联VN的信息。

【命令】

集中式设备：

display system internal fib vn  id[ [id \| ]{.commandparameterChar}]index index{.commandparameterChar} } reference

分布式设备－独立运行模式/集中式IRF设备：

display system internal fibvn [id[ [id \|]{.commandparameterChar}]**index index]{.commandparameterChar} } reference slot slot-number{.commandparameterChar} [cpu *cpu-number* ]

分布式设备－IRF模式：

**[display system internal fib vn**[ { **id** *id \|* **index** *index* } **reference** **chassis** [chassis-number]{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[id ***id*]：按指定VN ID显示VN信息。

**[index*** index*]：按指定VN指针显示VN信息。

**[reference**]：显示关联该VN的前缀信息。

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的前缀关联VN的信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上的前缀关联VN的信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX上的前缀关联VN的信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的前缀关联VN的信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的前缀关联VN的信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的前缀关联VN的信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- display system internal fib vn entry-status**

------------------------------------------------------------------------

**[display system internal fib vn entry-status**]命令用来显示指定状态的VN表项基本信息。

【命令】

集中式设备：

display system internal fib vnentry-status status{.commandparameterChar}

分布式设备－独立运行模式/集中式IRF设备：

display system internal fibvn entry-status status {.commandparameterChar}slot slot-number{.commandparameterChar} [cpu *cpu-number* ]

分布式设备－IRF模式：

**[display system internal fib vn** **entry-status** [status{.commandparameterChar} **chassis** chassis-number{.commandparameterChar} **slot** slot-number {.commandparameterChar} **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[entry-status** [status{.commandparameterChar}]]：按指定状态显示VN信息。取值范围为\<A,F,R\>，"A"表示待老化表项，"F"表示下驱动失败表项，"R"表示由于被关联而未删除的表项。

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板上的指定状态的VN表项基本信息。slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式－独立运行模式）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备的指定状态的VN表项基本信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备/PEX的指定状态的VN表项基本信息。slot-number{.commandparameterChar}表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定成员设备上指定单板的指定状态的VN表项基本信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号，slot-number{.commandparameterChar}表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

chassis{.commandkeywordsChar} [chassis-number{.commandparameterChar} ]slot{.commandkeywordsChar} [slot-number{.commandparameterChar}]：显示指定单板的指定状态的VN表项基本信息。chassis-numbe{.commandparameterChar}r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，slot-number{.commandparameterChar}表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的指定状态的VN表项基本信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe配置命令 \-- reset system internal fib statistics**

------------------------------------------------------------------------

**[reset system internal fib statistics**]命令用来清除FIB统计信息。

【命令】

集中式设备：

**[reset system internal fib statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset system internal fib statistics******slot*** slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[reset system internal fib statistics******chassis ***chassis-number*** slot*** slot-number***** **cpu** *cpu-number* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的FIB统计信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备的FIB统计信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：清除指定成员设备/PEX的FIB统计信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备上指定单板的FIB统计信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板的FIB统计信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU的FIB统计信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe调试命令 \-- debugging system internal fib prefix**

------------------------------------------------------------------------

**[debugging system internal fib **]命令用来打开FIB调试信息开关。

**[undo debugging system internal fib**]命令用来关闭FIB调试信息开关。

【命令】

集中式设备：

debugging system internal fib prefix  all [\| ]message [\|] hardware }

undo debugging system internal fib prefix   all [\| ]message [\|] hardware }

分布式设备－独立运行模式/集中式IRF设备：

debugging system internal fib prefix   all [\| ]message [\|] hardware } slot slot-number{.commandparameterChar} [cpu *cpu-number* ]

undo debugging system internal fib prefix  all [\| ]message [\|] hardware } slot slot-number {.commandparameterChar}cpu *cpu-number*

分布式设备－ IRF模式：

debugging system internal fib prefix  all [\| ]message [\|] hardware } chassis chassis-number{.commandparameterChar} slot *slot-number *cpu *cpu-number*

undo debugging system internal fib prefix  all [\| ]message [\|] hardware } chassis *chassis-number*slot *slot-number*  [cpu *cpu-number* ]

【缺省情况】

FIB 调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：打开所有调试开关。

**[message**]：打开message调试开关，打印路由下发和板间同步的IPv4 FIB前缀消息。

**[hardware**]：打开hardware调试开关，打印下发驱动信息以及驱动返回的消息。

**[slot ***slot-number*]：打开指定单板的调试开关。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：打开指定成员设备的调试开关。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：打开指定成员设备/PEX的调试开关。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定成员设备上指定单板的调试开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定单板的调试开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：打开指定CPU的调试开关。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**IP转发基础 \-- IP转发基础Probe调试命令 \-- debugging system internal fib vn**

------------------------------------------------------------------------

**[debugging system internal fib vn **]命令用来打开VN调试信息开关。

**[undo debugging system internal fib vn**]命令用来关闭VN调试信息开关。

【命令】

集中式设备：

debugging system internal fib vn   all [\| ]message [\|] hardware [\|] bind [\|] notify}

undo d debugging system internal fib vn   all [\| ]message [\|] hardware [\|] bind [\|] notify }

分布式设备－独立运行模式/集中式IRF设备：

debugging system internal fib vn   all [\| ]message [\|] hardware [\|] bind [\|] notify } slot slot-number{.commandparameterChar}  [cpu *cpu-number* ]

undo debugging system internal fib vn   all [\| ]message [\|] hardware [\|] bind [\|] notify } slot slot-number {.commandparameterChar}cpu *cpu-number*

分布式设备－独立运行模式/集中式IRF设备：

debugging system internal fib vn   all [\| ]message [\|] hardware [\|] bind [\|] notify } chassis chassis-number{.commandparameterChar} slot *slot-number *cpu *cpu-number*

undo debugging system internal fib vn  all [\| ]message [\|] hardware [\|] bind [\|] notify } chassis *chassis-number*slot *slot-number* [cpu *cpu-number* ]

【缺省情况】

VN 调试信息开关处于关闭状态。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：打开所有调试开关。

**[message**]：打开message调试开关,显示路由下发和板间同步的vn消息。

**[hardware**]：打开hardware调试开关，显示下发驱动的信息以及驱动返回的信息。

**[bind**]：打开bind调试开关，显示前缀绑定vn，vn绑定adj/nhlfe的相关信息。

**[notify**]：打开notify调试开关，显示adj/nhlfe通知vn，以及vn通知前缀的信息。

**[slot ***slot-number*]：打开指定单板的调试开关。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot ***slot-number*]：打开指定成员设备的调试开关。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：打开指定成员设备/PEX的调试开关。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定成员设备上指定单板的调试开关。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：打开指定单板的调试开关。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：打开指定CPU的调试开关。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

