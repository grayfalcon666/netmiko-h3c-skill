
**OSPF \-- OSPF probe命令 \-- display system internal ospf event-log**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf event-log**]命令用来显示OSPF的日志信息。

【命令】

集中式设备：

**[display**[ **system** **internal** **ospf** **event-log** { **gr** \| **ha** \| **interface** \| **nib** \| **notify** \| **upgrade** }]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **system** **internal** **ospf** **event-log** { **gr** \| **interface** \| **nib** \| **notify** \| { **ha** \| **upgrade** } [ **standby** **slot** *slot-number* [ **cpu** *cpu-number* ] ] }]]

分布式设备－IRF模式：

**[display**[ **system** **internal** **ospf** **event-log** { **gr** \| **interface** \| **nib** \| **notify** \| { **ha** \| **upgrade** } [ **standby** **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ] }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gr**]：显示GR日志。

**[ha**]：显示HA事件处理日志信息。

**[interface**]：显示接口事件日志。

**[nib**]：显示NIB日志。

**[notify**]：显示接口通知日志。

**[upgrade**]：显示升级平滑日志信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPF日志信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的日志信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPF日志信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF的日志信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPF日志信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的日志信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- display system internal ospf flood-list**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf flood-list**]命令用来显示OSPF的flooding信息。

【命令】

**[display system internal ospf** [ *process-id*  **flood-list**  *interface-type* *interface-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的flooding信息。

*[interface-type* *interface-number*]：显示指定接口的flooding信息。如果未指定本参数，将显示所有接口的flooding信息。

**OSPF \-- OSPF probe命令 \-- display system internal ospf interface**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf******interface**]命令用来显示接口相关信息。

【命令】

**[display** **system** **internal** **ospf** **interface** [ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ip-address* { *mask* \| *mask-length* } ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance*** vpn-instance-name*]：显示指定VPN实例下接口相关信息。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示所有接口的信息。

*[ip-address*]：接口IP地址，点分十进制，显示指定IP地址和掩码/掩码长度接口的信息。

*[mask*]：网络掩码，点分十进制格式。

*[mask-length*]：网络掩码长度，取值范围为0～32。

**OSPF \-- OSPF probe命令 \-- display system internal ospf interface standby**

------------------------------------------------------------------------

**[display system internal ospf interface standby**]命令用来显示备份的OSPF接口信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospf** [ *process-id*  **interface** [ *interface-type interface-number* \| **verbose** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospf** [ *process-id*  **interface** [ *interface-type interface-number* \| **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的接口信息。

*[interface-type interface-number*]：接口类型和编号。显示指定接口的OSPF详细信息。

**[verbose**]：显示所有接口的OSPF详细信息。

**[standby slot** *slot-number*]：显示备份的指定单板的OSPF接口信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的接口信息。（分布式设备－独立运行模式）

**[standby slot** *slot-number*]：显示备份的指定成员设备的OSPF接口信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF的接口信息。（集中式IRF设备）

**[standby chassis** *chassis-number* **slot** *slot-number*]：显示备份的指定成员设备上指定单板的OSPF接口信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的接口信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- display system internal ospf lsdb**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf lsdb**]命令用来显示LSA产生的来源及详细信息。

【命令】

**[display** **system** **internal** **ospf** [ *process-id*  **lsdb** { **asbr** \| **ase** \| **nssa** \| **summary** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的LSA map信息。

**[asbr**]：显示数据库中Type-4 LSA（ASBR Summary LSA）的map信息。

**[ase**]：显示数据库中Type-5 LSA（AS External LSA）的map信息。

**[nssa**]：显示数据库中Type-7 LSA（NSSA External LSA）的map信息。

**[summary**]：显示数据库中Type-3 LSA（Network Summary LSA）的map信息。

**OSPF \-- OSPF probe命令 \-- display system internal ospf lsdb standby**

------------------------------------------------------------------------

**[display system internal ospf lsdb standby**]命令用来显示备份的OSPF链路状态数据库信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display ospf** [ *process-id*  **lsdb** [ **area** *area-id* \| **brief** \| [ { **asbr** \| **ase** \| **network** \| **nssa** \| **opaque-area** \| **opaque-as** \| **opaque-link** \| **router** \| **summary** } [ *link-state-id* ]   **originate-router** *advertising-router-id* \| **self-originate** ] ] **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display ospf** [ *process-id*  **lsdb** [ **area** *area-id* \| **brief** \| [ { **asbr** \| **ase** \| **network** \| **nssa** \| **opaque-area** \| **opaque-as** \| **opaque-link** \| **router** \| **summary** } [ *link-state-id* ]   **originate-router** *advertising-router-id* \| **self-originate** ] ] **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的链路状态数据库信息。

**[area*** area-id*]：显示数据库中指定区域的LSA信息。*area-id*表示区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其转换成IP地址格式）或者是IP地址格式*。*如果未指定本参数，将显示所有区域的信息。

**[brief**]：显示数据库的概要信息。

**[asbr**]：显示数据库中Type-4 LSA（ASBR Summary LSA）的信息。

**[ase**]：显示数据库中Type-5 LSA（AS External LSA）的信息。

**[network**]：显示数据库中Type-2 LSA（Network LSA）的信息。

**[nssa**]：显示数据库中Type-7 LSA（NSSA External LSA）的信息。

**[opaque-area**]：显示数据库中Type-10 LSA （Opaque-area LSA）的信息。

**[opaque-as**]：显示数据库中Type-11 LSA （Opaque-AS LSA）的信息。

**[opaque-link**]：显示数据库中Type-9 LSA（Opaque-link LSA）的信息。

**[router**]：显示数据库中Type-1 LSA（Router LSA）的信息。

**[summary**]：显示数据库中Type-3 LSA（Network Summary LSA）的信息。

*[link-state-id*]：链路状态ID，IP地址格式。

**[originate-router ***advertising-router-id*]：发布LSA报文的路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的LSA的数据库信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPF链路状态数据库信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的链路状态数据库信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPF链路状态数据库信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF的链路状态数据库信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPF链路状态数据库信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的链路状态数据库信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- display system internal ospf nib**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf nib**]命令用来显示NIB分配的下一跳信息。

【命令】

**[display** **system** **internal** **ospf** **nib** [ *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：路由下一跳信息的ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示NIB详细信息。

**OSPF \-- OSPF probe命令 \-- display system internal ospf peer standby**

------------------------------------------------------------------------

**[display system internal ospf peer standby**]命令用来显示备份的OSPF邻居信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display ospf ** *process-id* ] **peer**  **verbose**   *interface-type interface-number*   *neighbor-id*  **standby** **slot** *slot-number*  **cpu** *cpu-number*

分布式设备－IRF模式：

**[display ospf ** *process-id* ] **peer**  **verbose**   *interface-type interface-number*   *neighbor-id*  **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number*

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的各区域邻居的信息。

**[verbose**]：显示OSPF各区域邻居的详细信息。如果未指定本参数，将显示OSPF进程各区域邻居的概要信息。

*[interface-type interface-number*]：接口类型和编号。如果未指定本参数，将显示所有接口的OSPF邻居的信息。

*[neighbor-id*]：邻居路由器的Router ID。如果未指定本参数，将显示所有邻居路由器的OSPF邻居的信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPF各区域邻居的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF各区域邻居的信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPF各区域邻居的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF各区域邻居的信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPF各区域邻居的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF各区域邻居的信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- display system internal ospf peer statistics standby**

------------------------------------------------------------------------

**[display **]**system internal ospf peer statistics standby**命令用来显示备份的本地路由器所有OSPF邻居的统计信息，即处于各种状态的邻居数目。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display ospf** [ *process-id*  **peer** **statistics** **standby** **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display ospf** [ *process-id*  **peer** **statistics** **standby** **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的邻居统计信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPF邻居统计信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的邻居统计信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPF邻居统计信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF的邻居统计信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPF邻居统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的邻居统计信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- display system internal ospf prefix**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf prefix**]命令用来显示OSPF中前缀对应的LSA信息。

【命令】

**[display** **system** **internal** **ospf** [ *process-id*  **prefix** [ *ip-address* { *mask* \| *mask-length* } ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的前缀信息。

*[ip-address*]：路由的目的IP地址。如果未指定本参数，将显示所有前缀的信息。

*[mask*]：网络掩码，点分十进制格式。

*[mask-length*]：网络掩码长度，取值范围为0～32。

**OSPF \-- OSPF probe命令 \-- display system internal ospf router**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf router**]命令用来显示OSPF中到路由器节点的路由信息。

【命令】

**[display** **system** **internal** **ospf** [ *process-id*  **router**]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的信息。

**OSPF \-- OSPF probe命令 \-- display system internal ospf statistics**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf statistics**]命令用来显示OSPF的统计信息。

【命令】

**[display system internal ospf **[ *process-id*  **statistics** { **request-queue \| retrans-queue** }  *interface-type interface-number*   *neighbor-id* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的统计信息。

**[request-queue**]：邻居请求链计数。

**[retrans-queue**]：邻居重传链计数。

*[interface-type interface-number*]：接口类型和编号，显示指定接口的统计信息。

*[neighbor-id*]：显示指定邻居的统计信息。

**OSPF \-- OSPF probe命令 \-- display system internal ospf status**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospf status**]命令用来显示OSPF协议状态信息，包括内存门限状态，及各模块相关信息。

【命令】

**[display** **system** **internal** **ospf** **status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**OSPF \-- OSPF probe命令 \-- display system internal ospf vlink standby**

------------------------------------------------------------------------

**[display system internal ospf vlink standby**]命令用来显示备份的OSPF虚连接信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospf** [ *process-id*  **vlink** **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospf** [ *process-id*  **vlink** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPF进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPF进程的虚连接信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPF虚连接信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的虚连接信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPF虚连接信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPF的虚连接信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPF虚连接信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPF的虚连接信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPF \-- OSPF probe命令 \-- reset system internal ospf event-log**

------------------------------------------------------------------------

![说明](OSPF%20Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[reset system internal ospf event-log**]命令用来清除OSPF的日志信息。

【命令】

**[reset**[ **system internal ospf** **event-log** { **interface** \| **nib** \| **notify** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**]：接口事件相关日志。

**[nib**]：NIB的相关日志。

**[notify**]：接口通知相关日志。

