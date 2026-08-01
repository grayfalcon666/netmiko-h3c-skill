<!-- CMD-INDEX
  display system internal ospfv3 event-log | Probe视图          | L15
  display system internal ospfv3 interface | Probe视图          | L49
  display system internal ospfv3 interface standby | Probe视图          | L85
  display system internal ospfv3 lsdb | Probe视图          | L139
  display system internal ospfv3 lsdb standby | Probe视图          | L181
  display system internal ospfv3 nib  | Probe视图          | L259
  display system internal ospfv3 peer standby | Probe视图          | L291
  display system internal ospfv3 prefix | Probe视图          | L353
  display system internal ospfv3 standby | Probe视图          | L389
  display system internal ospfv3 status | Probe视图          | L435
  display system internal ospfv3 vlink standby | Probe视图          | L461
-->

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 event-log**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display** **system** **internal** **ospfv3** **event-log**]命令用来显示OSPFv3的各种日志信息。

【命令】

**[display**[ **system** **internal** **ospfv3** **event-log** { **gr** \| **nib** \| **rib** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[gr**]：显示GR状态机变迁记录。

**[nib**]：显示路由管理上报给OSPFv3的NIB信息。

**[rib**]：显示路由管理上报给OSPFv3的RIB信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 interface**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 interface**]命令用来显示OSPFv3的接口相关信息。

【命令】

**[display** **system** **internal** **ospfv3** **interface** [ **vpn-instance** *vpn-instance-name*  [ *interface-type* *interface-number* \| *ipv6-address* *prefix-length* ]]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定OSPFv3进程所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示OSPFv3位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[interface-type* *interface-number*]：接口类型和接口编号。

*[ipv6-address*]：IPv6地址前缀。

*[prefix-length*]：IPv6地址前缀长度，取值范围为0～128。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 interface standby**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 interface standby**]命令用来显示备份的OSPFv3接口信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospfv3** [ *process-id*  **interface** [ *interface-type interface-number* \| **verbose** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospfv3** [ *process-id*  **interface** [ *interface-type interface-number* \| **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

*[interface-type interface-number*]：接口类型和接口编号。显示指定接口的详细信息。

**[verbose**]：显示所有接口的详细信息。

**[standby slot**] *slot-number*：显示备份的指定单板的OSPFv3接口信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的接口信息。（分布式设备－独立运行模式）

**[standby slot**] *slot-number*：显示备份的指定成员设备的OSPFv3接口信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPFv3的接口信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPFv3接口信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的接口信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果未指定OSPFv3进程号，将显示所有OSPFv3进程的接口信息。

·如果未指定接口或参数**verbose**，将显示所有接口的概要信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 lsdb**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 lsdb**]命令用来显示LSA产生的来源及详细信息。

【命令】

**[display** **system** **internal** **ospfv3** [ *process-id*  **lsdb** { **inter-prefix** \| **inter-router** \| **intra-prefix** { **reference** **type-1** \| **reference** **type-2** } \| **router** }]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程下的map信息。

**[inter-prefix**]：显示Inter-area-prefix LSA的map信息。

**[inter-router**]：显示Inter-area-router LSA的map信息。

**[intra-prefix**]：显示Intra-area-prefix LSA的map信息。

**[reference** **type-1**]：显示引用Router-LSA的Intra-area-prefix LSA map信息。

**[reference** **type-2**]：显示引用Network-LSA的Intra-area-prefix LSA map信息。

**[router**]：显示Router-LSA的map信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 lsdb standby**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 lsdb standby**]命令用来显示备份的LSA信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospfv3 **[ *process-id*  **lsdb** [ { **external** \| **grace** \| **inter-prefix** \| **inter-router** \| **intra-prefix** \| **link** \| **network** \| **nssa** \| **router** \| **unknown** [ *type* ] }  *link-state-id*  [ **originate-router** *router-id* \| **self-originate** ] \| **statistics** \| **total** \| **verbose** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospfv3 **[ *process-id*  **lsdb** [ { **external** \| **grace** \| **inter-prefix** \| **inter-router** \| **intra-prefix** \| **link** \| **network** \| **nssa** \| **router** \| **unknown** [ *type* ] }  *link-state-id*  [ **originate-router** *router-id* \| **self-originate** ] \| **statistics** \| **total** \| **verbose** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的链路状态数据库信息。

**[external**]：显示链路状态数据库中Type-5 LSA（AS External LSA）的信息。

**[grace**]：显示链路状态数据库中Type-11 LSA（Grace LSA）的信息。

**[inter-prefix**]：显示链路状态数据库中Type-3 LSA（Inter-Area-Prefix LSA）的信息。

**[inter-router**]：显示链路状态数据库中Type-4 LSA（Inter-Area-Router LSA）的信息。

**[intra-prefix**]：显示链路状态数据库中Type-9 LSA（Intra-Area-Prefix LSA）的信息。

**[link**]：显示链路状态数据库中Type-8 LSA（Link LSA）的信息。

**[network**]：显示链路状态数据库中Type-2 LSA（Network LSA）的信息。

**[nssa**]：显示链路状态数据库中Type-7 LSA（NSSA LSA）的信息。

**[router**]：显示链路状态数据库中Type-1 LSA（Router LSA）的信息。

**[unknown**]：显示链路状态数据库中未知类型LSA的信息。

*[type*]：LSA类型，取值范围十六进制0～FFFF。如果未指定本参数，将显示所有未知类型LSA的信息。

*[link-state-id*]：链路状态ID，IPv4地址形式。

**[originate-router** *router-id*]：发布该LSA的路由器的Router ID。

**[self-originate**]：显示本地路由器自己产生的LSA的链路状态数据库信息。

**[statistics**]：显示链路状态数据库中LSA的统计信息。

**[total**]：显示链路状态数据库中各种LSA的总数。

**[verbose**]：显示详细信息。如果未指定本参数，将显示概要信息。

**[standby slot **]*slot-number*：显示备份的指定单板的OSPFv3链路状态数据库信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的链路状态数据库信息。（分布式设备－独立运行模式）

**[standby slot**] *slot-number*：显示备份的指定成员设备的OSPFv3链路状态数据库信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPFv3的链路状态数据库信息。（集中式IRF设备）

**[standby chassis**] *chassis-number* **slot** *slot-number*：显示备份的指定成员设备上指定单板的OSPFv3链路状态数据库信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的链路状态数据库信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 nib**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 nib**]命令用来显示OSPFv3的下一跳NIB信息。

【命令】

**[display** **system** **internal** **ospfv3** **nib** [ *nib-id*   **verbose** ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nib-id*]：路由下一跳信息的ID值，取值范围1～FFFFFFFF。

**[verbose**]：显示NIB详细信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 peer standby**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 peer standby**]命令用来显示备份的OSPFv3邻居信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospfv3** [ *process-id*   **area** *area-id*  **peer**  [ *interface-type interface-number*   **verbose**  \| *peer-router-id* \| **statistics** ] **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospfv3** [ *process-id*   **area** *area-id*  **peer**  [ *interface-type interface-number*   **verbose**  \| *peer-router-id* \| **statistics** ] **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。

**[area*** area-id*]：显示位于指定区域的邻居信息。*area-id*为区域的标识，可以是十进制整数（取值范围为0～4294967295，系统会将其处理成IPv4地址格式）或IPv4地址格式。

*[interface-type interface-number*]：接口类型和接口编号。

**[verbose**]：显示邻居的详细信息。

*[peer-router-id*]：显示指定邻居的信息。

**[statistics**]：显示OSPFv3邻居的统计信息。

**[standby slot **]*slot-number*：显示备份的指定单板的OSPFv3邻居的信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3邻居的信息。（分布式设备－独立运行模式）

**[standby slot **]*slot-number*：显示备份的指定成员设备的OSPFv3邻居的信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPFv3邻居的信息。（集中式IRF设备）

**[standby chassis **]*chassis-number*** slot ***slot-number*：显示备份的指定成员设备上指定单板的OSPFv3邻居的信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3邻居的信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

·如果未指定OSPFv3进程号，将显示所有OSPFv3进程的邻居信息。

·如果未指定区域，将显示所有区域的邻居信息。

·如果接口参数、邻居Router ID参数都不输入，则显示所有接口的邻居信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 prefix**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display** **system** **internal** **ospfv3** **prefix**]命令用来显示OSPFv3的前缀对应的LSA信息。

【命令】

**[display** **system** **internal** **ospfv3** [ *process-id*  **prefix** { **inter** \| **intra** }  *ipv6-address* *prefix-length* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的前缀对应的LSA信息。

**[inter**]**：**显示InterAs前缀对应的LSA信息。

**[intra**]**：**显示IntraAs前缀对应的LSA信息。

*[ipv6-address prefix-length*]：显示指定IPv6地址的OSPFv3前缀对应的LSA信息。*ipv6-address*表示IPv6地址前缀；*prefix-length*表示IPv6地址前缀长度，取值范围为0～128。如果未指定本参数，将显示所有的前缀对应的LSA信息。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 standby**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 standby**]命令用来显示备份的OSPFv3进程的信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospfv3** [ *process-id*   **verbose**  **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospfv3** [ *process-id*   **verbose**  **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的信息。

**[verbose**]：显示OSPFv3进程的详细信息。如果未指定本参数，将显示OSPFv3进程的概要信息。

**[standby slot**]* slot-number*：显示备份的指定单板的OSPFv3进程信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的进程信息。（分布式设备－独立运行模式）

**[standby slot**]* slot-number*：显示备份的指定成员设备的OSPFv3进程信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPFv3的进程信息。（集中式IRF设备）

**[standby chassis**]* chassis-number*** slot ***slot-number*：显示备份的指定成员设备上指定单板的OSPFv3进程信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的进程信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 status**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 status**]命令用来显示OSPFv3协议状态信息，包括内存门限状态，及各模块相关信息。

【命令】

**[display** **system** **internal** **ospfv3** **status**]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

**OSPFv3 \-- OSPFv3 probe命令 \-- display system internal ospfv3 vlink standby**

------------------------------------------------------------------------

![说明](OSPFv3%20Probe命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[display system internal ospfv3 vlink standby**]命令用来显示备份的OSPFv3虚连接信息。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[display system internal ospfv3** [ *process-id*  **vlink** **standby slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display system internal ospfv3** [ *process-id*  **vlink** **standby chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[process-id*]：OSPFv3进程号，取值范围为1～65535。如果未指定本参数，将显示所有OSPFv3进程的虚连接信息。

**[standby slot **]*slot-number*：显示备份的指定单板的OSPFv3的虚连接信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的虚连接信息。（分布式设备－独立运行模式）

**[standby slot **]*slot-number*：显示备份的指定成员设备的OSPFv3的虚连接信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示OSPFv3的虚连接信息。（集中式IRF设备）

**[standby chassis **]*chassis-number*** slot ***slot-number*：显示备份的指定成员设备上指定单板的OSPFv3的虚连接信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示OSPFv3的虚连接信息。（分布式设备－IRF模式）

**[cpu** *cpu-number*]：显示指定CPU的信息。*cpu-number*表示CPU编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

