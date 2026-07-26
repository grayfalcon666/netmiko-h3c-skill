
**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp statistics**

------------------------------------------------------------------------

**[display system internal lipc stcp statistics**]命令用来显示LIPC单播的全局统计信息，用于分析单播的全局工作情况。

【命令】

**[display system internal lipc stcp statistics** [ **lip** *lip* ]]

【缺省情况】

显示本节点LIPC单播的统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp performance**

------------------------------------------------------------------------

**[display system internal lipc stcp performance**]命令用来显示单播的性能信息。

【命令】

**[display system internal lipc stcp performance** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIPC单播的性能信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

必须使用**lipc performance**命令打开相应的性能统计开关后，该命令才能输出性能信息。

【相关命令】

·**lipc performance**

**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp links**

------------------------------------------------------------------------

**[display system internal lipc stcp links**]命令用来显示单播的连接信息。包括收发包信息、状态信息、缓存信息等。

【命令】

**[display system internal lipc stcp links**[ { **all** \| **detail** *port* \| **global** *gport* \| **listening** \| **local** *lport* \| **singledetail** *lport rport* } [ **lip** *lip* ]]]

【缺省情况】

显示本节点LIPC单播的连接信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示显示本节点所有的单播连接信息。

**[detail** *port*]：表示指定端口号的具体信息，取值范围为0～65535。

**[global** *gport*]：表示全局知名端口号，取值范围为100～8100。

**[listening**]：表示显示本节点处于侦听状态的连接。

**[local** *lport*]：表示本地端口号，取值范围为10100～65535。

**[singledetail** *lport rport*]：表示指定本地端口号和目的端口号的具体信息，取值范围为0～65535。

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp status**

------------------------------------------------------------------------

**[display system internal lipc stcp status**]命令用来显示单播的传输状态。主要记录单播对象的传输序号、ACK序号、发送标志、接收状态。该命令通常用于分析单播的数据可靠传输问题。

【命令】

[**[display system internal lipc stcp status { recv \| send } ]** **lip** *lip* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[recv**]：显示接收端的单播传输状态。

**[send**]：显示发送端的单播传输状态。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp global-server**

------------------------------------------------------------------------

**[display system internal lipc stcp global-server**]命令显示LIPC单播的全局知名端口信息。

【命令】

**[display system internal lipc stcp global-server** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIPC单播的全局知名端口同步信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- STCP Probe命令 \-- display system internal lipc stcp event**

------------------------------------------------------------------------

**[display system internal lipc stcp event**]命令用来显示LIPC单播事件的信息。

【命令】

**[display system internal lipc stcp event**[ { **sync** \| **trans** } [ **lip** *lip* ]]]

【缺省情况】

显示本地节点LIPC单播的事件信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sync**]：显示LIPC单播控制报文事件信息。

**[trans**]：显示LIPC单播数据报文事件信息。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

该命令主要记录本节点和其他节点的连接/DACK/销毁/时序交互信息。当设备上连接很多时，该命令记录的条目很容易满（512条），此时会将最老的记录清除掉。因此，发现问题时，应当尽早执行该命令，获取事件信息，便于定位分析。

**LIPC \-- STCP Probe命令 \-- display system internal lipc stream**

------------------------------------------------------------------------

**[display system internal lipc stream**]命令用来查看流模式单播的记录信息。

【命令】

**[display system internal lipc stream**[ { **ack** \| **reass** \| **send** } **port** *portID* [ **lip** *lip* ]]]

【缺省情况】

显示本地节点LIPC单播流模式信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ack**]：表示查看指定端口号的收到ACK的记录。

**[reass**]：表示查看指定端口号的接收重组队列信息。

**[send**]：表示查看指定端口号的发送报文分片记录。

**[port ***portID*]：表示端口号，为0～65535的整数。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- MTCP模块Probe命令 \-- display system internal lipc mtcp statistics**

------------------------------------------------------------------------

**[display system internal lipc mtcp statistics**]命令用来显示LIPC组播的全局统计信息。

【命令】

**[display system internal lipc mtcp statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIPC组播的全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- MTCP模块Probe命令 \-- display system internal lipc mtcp performance**

------------------------------------------------------------------------

**[display system internal lipc mtcp performance**]命令显示LIPC组播性能信息。

【命令】

**[display system internal lipc mtcp performance** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIPC组播性能信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

必须打开相应得性能统计开关后，该命令才能输出性能信息。

【相关命令】

·**lipc performance**

**LIPC \-- MTCP模块Probe命令 \-- display system internal lipc mtcp group**

------------------------------------------------------------------------

**[display system internal lipc mtcp group**]命令用来显示LIPC显示某个组播组的成员信息或统计信息或状态机的历史变迁轨迹。

【命令】

**[display system internal lipc mtcp group ***portID*****[{ **history** \| **member** \| **statistics** } [ **lip** *lip* ]]]

【缺省情况】

显示本地节点某个组播组的成员信息或统计信息或状态机的历史变迁轨迹。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[portID*]：组播组的端口号，一个端口号标识一个组播组，取值范围为0～4294967295。

**[history**]：显示该组播组状态机的历史变迁轨迹。

**[member**]：显示该组播组的成员信息。

**[statistics**]：显示该组播组的统计信息。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- LGMP模块Probe命令 \-- display system internal lipc lgmp statistics**

------------------------------------------------------------------------

**[display system internal lipc lgmp statistics**]命令用来显示LIPC LGMP模块的统计信息。

【命令】

**[display system internal lipc lgmp statistics ** **lip** *lip* ]

【缺省情况】

显示本地节点LIPC LGMP模块的统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- LGMP模块Probe命令 \-- display system internal lipc lgmp group-list**

------------------------------------------------------------------------

**[display system internal lipc lgmp group-list**]命令用来查看系统中所有已经创建的组播组数目、组播端口号，以及组播组的HASH分布情况。

【命令】

**[display system internal lipc lgmp group-list** [ **lip** *lip* ]]

【缺省情况】

显示本地节点已经创建的组播组数目、组播端口号，以及组播组的HASH分布情况。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- LGMP模块Probe命令 \-- display system internal lipc lgmp group**

------------------------------------------------------------------------

**[display system internal lipc lgmp group**]命令用来显示一个指定组播组信息，包含成员信息和组播组相关的统计信息。

【命令】

**[display system internal lipc lgmp group** *groupID* [ **lip** *lip* ]]

【缺省情况】

显示本地节点指定组播组信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[groupID*]：表示组播组号，取值范围为0～4294967295。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- LGMP模块Probe命令 \-- display system internal lipc lgmp physical-group-list**

------------------------------------------------------------------------

**[display system internal lipc lgmp physical-group-list**]命令用来显示所有的硬件组播组信息，以便了解硬件组播组的使用情况。

【命令】

**[display system internal lipc lgmp physical-group-list** [ **lip** *lip* ]]

【缺省情况】

显示本节点显示所有的硬件组播组信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- LGMP模块Probe命令 \-- display system internal lipc lgmp physical-group**

------------------------------------------------------------------------

**[display system internal lipc lgmp physical-group**]命令用来显示指定的硬件组播组信息。

【命令】

**[display system internal lipc lgmp physical-group ***phyID* [ **lip** *lip* ]]

【缺省情况】

显示本地节点指定的硬件组播组信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[physical-group ***phyID*]：表示硬件组播组ID，取值范围为0～4294967295。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- PUBLISH模块Probe命令 \-- display system internal lipc publish statistics**

------------------------------------------------------------------------

**[display system internal lipc publish statistics**]命令用来显示LIPC  PUBLISH模块统计信息。

【命令】

**[display system internal lipc publish statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点PUBLISH模块的统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- PUBLISH模块Probe命令 \-- display system internal lipc publish global-cb**

------------------------------------------------------------------------

**[display system internal lipc publish global-cb**]命令用来显示LIPC PUBLISH模块全局控制块信息。

【命令】

**[display system internal lipc publish global-cb** [ **lip** *lip* ]]

【缺省情况】

显示本地节点PUBLISH模块全局控制块信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

一般用于诊断Pub模块在某个节点上是否乱序。

**LIPC \-- LCMP模块Probe命令 \-- display system internal lipc lcmp statistics**

------------------------------------------------------------------------

**[display system internal lipc lcmp statistics**]命令用来显示LIPC LCMP全局统计信息，包括收发包计数和错误计数。

【命令】

**[display system internal lipc lcmp statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LCMP全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- LIP模块Probe命令 \-- display system internal lipc lip statistics**

------------------------------------------------------------------------

**[display system internal lipc lip statistics**]命令用来显示LIPC LIP全局统计信息。包括LIP报文的收发计数和出错计数。

【命令】

**[display system internal lipc lip statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIP全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology link**

------------------------------------------------------------------------

**[display system internal lipc topology link**]命令用来显示LIPC 的拓扑链接信息。

【命令】

**[display system internal lipc topology link** [ **lip** *lip* ]]

【缺省情况】

显示本地节点LIPC 的拓扑链接信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology history**

------------------------------------------------------------------------

**[display system internal lipc topology history**]命令用来查看拓扑链接信息的历史变迁记录。

【命令】

**[display system internal lipc topology history** [ **lip** *lip* ]]

【缺省情况】

显示本地节点拓扑链接信息的历史变迁记录。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology status**

------------------------------------------------------------------------

**[display system internal lipc topology status**]命令用来显示节点的拓扑状态信息。

【命令】

**[display system internal lipc topology status** [ **lip** *lip* ]]

【缺省情况】

显示本地节点拓扑状态信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology statistics**

------------------------------------------------------------------------

**[display system internal lipc topology statistics**]命令用来查看拓扑相关的全局统计。记录了该全局事件发生的次数，并记录了最近六次发生该事件的时间（精确到0.1毫秒）。

【命令】

**[display system internal lipc topology statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点拓扑相关的全局统计。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology node**

------------------------------------------------------------------------

**[display system internal lipc topology node**]命令用来查看拓扑节点相关的统计信息。

【命令】

**[display system internal lipc topology node ***nodeID* [ **lip** *lip* ]]

【缺省情况】

显示本地节点上和其他拓扑节点相关的统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[nodeID*]：表示节点号，取值范围为0～32767。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

记录了该节点上事件发生的次数，并记录了最近六次发生该事件的时间（精确到0.1毫秒）。

**LIPC \-- TOPOLOGY模块Probe命令 \-- display system internal lipc topology process-time**

------------------------------------------------------------------------

**[display system internal lipc topology process-time**]命令用来查看发生拓扑事件时，通知各个模块耗时。

【命令】

**[display system internal lipc topology process-time** [ **lip** *lip* ]]

【缺省情况】

显示本地节点发生拓扑事件时，通知各个模块耗时。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- PHY模块Probe命令 \-- display system internal lipc physical**

------------------------------------------------------------------------

**[display system internal lipc physical**]命令用来显示驱动适配层的全局统计信息。用于统计LIPC与驱动交互的各种信息，包括收发包计数，驱动错误计数和驱动上报事件计数。

【命令】

**[display system internal lipc physical** [ **lip** *lip* ]]

【缺省情况】

显示本地节点驱动适配层的全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- PHY模块Probe命令 \-- display system internal lipc loop statistics**

------------------------------------------------------------------------

**[display system internal lipc loop statistics**]命令用来显示本地环回的统计信息。

【命令】

**[display system internal lipc loop statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点环回的统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- PCB模块Probe命令 \-- display system internal lipc pcb mbuf statistics**

------------------------------------------------------------------------

**[display system internal lipc pcb mbuf statistics**]命令用来显示LIPC各个PCB下的MBUF使用情况。

【命令】

**[display system internal lipc pcb mbuf statistics ** **lip** *lip* ]

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip*** lip*]：表示节点号，取值范围为0～32767。不指定该参数时，表示本节点。

**LIPC \-- PCB模块Probe命令 \-- display system internal lipc pcb statistics**

------------------------------------------------------------------------

**[display system internal lipc pcb statistics**]命令用来显示LIPC PCB模块全局统计信息。

【命令】

**[display system internal lipc pcb statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点PCB模块全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- SUDP模块Probe命令 \-- display system internal lipc sudp statistics**

------------------------------------------------------------------------

**[display system internal lipc sudp statistics**]命令用来显示LIPC SUDP模块的全局统计信息。

【命令】

**[display system internal lipc sudp statistics** [ **lip** *lip* ]]

【缺省情况】

显示本地节点SUDP模块的全局统计信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- SUDP模块Probe命令 \-- display system internal lipc sudp { global-port \| local-port }**

------------------------------------------------------------------------

**[display system internal lipc sudp**]命令用来查看所有SUDP全局知名端口号或本地端口号的信息。

【命令】

**[display system internal lipc [sudp { global-port \| local-port }]** [ **lip** *lip* ]]

【缺省情况】

显示本地节点SUDP全局知名端口号或本地端口号的信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- SUDP模块Probe命令 \-- display system internal lipc sudp pcb-info**

------------------------------------------------------------------------

**[display system internal lipc sudp pcb-info**]命令用来查看SUDP模块的PCB详细信息。

【命令】

**[display system internal lipc sudp pcb-info**[ { **all-port** \| **global-port** \| **local-port** \| **specific-port** *portID* } [ **lip** *lip* ]]]

【缺省情况】

显示本地节点SUDP模块的PCB详细信息。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all-port**]：显示所有PCB信息。

**[global-port**]：显示全局知名端口的PCB信息。

**[local-port**]：显示本地知名端口的PCB信息。

**[specific-port ***portID*]：表示指定端口号，取值范围为0～65535。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- 其他 \-- debugging lipc**

------------------------------------------------------------------------

**[debugging lipc**]命令用来打开LIPC的debug开关。

【命令】

**[debugging lipc **[{ **detail \| dump** *port* **\| lgmp \| mbuf \| mtcp \| pub \| stcp \| stream** \| **topo** } [ **lip** ]*lip*****]]

**[undo debugging lipc **[{ **detail \| dump** *port* **\| lgmp \| mbuf \| mtcp \| pub \| stcp \| stream** \| **topo** \| **stream** } [ **lip** ]*lip*****]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[detail**]：用来打开LIPC的报文详细内容的调试信息开关。

**[dump** *port*]：表示端口号，取值范围为0～65535。

**[lgmp**]：用来打开LIPC的LGMP模块的调试信息开关。

**[mbuf**]：用来打开LIPC的MBUF模块的调试信息开关。

**[mtcp**]：用来打开LIPC的MTCP模块调试信息开关。

**[pub**]：用来打开LIPC的PUB模块的调试信息开关。

**[stcp**]：用来打开LIPC的STCP模块的调试信息开关。

**[stream**]：用来打开LIPC的STREAM模块的调试信息开关。

**[topo**]：用来打开LIPC的TOPO模块的调试信息开关。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- 其他 \-- lipc ping**

------------------------------------------------------------------------

**[lipc ping**]命令ping其它节点并等待回应，用于检查与目的节点LIPC通信链路是否正常。

【命令】

**[lipc ping** *lip* [ **length** *len* **times** *number* ]]

【缺省情况】

发送长度为100字节的请求报文，发送10次。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lip*]：表示节点号，取值范围为0～32767。

**[length** *len*]：表示报文长度，取值范围为0～32767。

**[times** *number*]：表示发送次数，取值范围为0～32767。

【使用指导】

系统中有效的节点号可以使用**display system internal lipc topology link**命令获取，用户需自己保证节点号的有效性。

**LIPC \-- 其他 \-- lipc timeout**

------------------------------------------------------------------------

**[lipc timeout**]命令用来设置LIPC拓扑链路的超时时间。

【命令】

**[lipc timeout ***time* [ **lip** *lip* ]]

【缺省情况】

拓扑链路的超时时间为60秒。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[timeout ***time*]：表示超时时间，取值范围为3-65535。

**[lip ***lip*]*：*表示远端节点号，取值范围为0～32767。

【使用指导】

如果本节点的TOPOLOGY模块在超时时间内一直没有收到UP节点的心跳报文，则会断开与该节点的所有单播、组播连接。

通常，只有在使用KDB或者KGDB调试内核时，才需要修改该数值，以避免其他节点认为正处于内核调试状态的节点链路Down。

**LIPC \-- 其他 \-- lipc performance**

------------------------------------------------------------------------

**[lipc performance**]命令用来配置单播或者组播的性能统计功能，用于评测LIPC的传输性能。

【命令】

**[lipc performance**[ { **mtcp** \| **stcp** } { **clear** \| **off** \| **on** } [ **lip** *lip* ]]]

【缺省情况】

性能统计开关是关闭的。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mtcp**]：MTCP子模块的信息。

**[stcp**]：STCP子模块的信息。

**[clear**]：清除单播或者组播的性能统计信息。

**[off**]：关闭单播或者组播的性能统计开关。

**[on**]：打开单播或者组播的性能统计开关。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

**LIPC \-- 其他 \-- lipc dump-port**

------------------------------------------------------------------------

**[lipc dump-port**]命令打开指定单播端口的dump开关。

【命令】

**[lipc dump-port ***port *&\<1-5\>  **lip** *lip* ]

**[undo lipc dump-port** [ **lip** *lip* ]]

【缺省情况】

单播端口的dump开关是关闭的。

【视图】

Probe视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port *&\<1-5\>]：表示单播端口号，取值范围为0～65535。&\<1-5\>表示前面的参数最多可以输入5次。

**[lip ***lip*]：表示远端节点号，取值范围为0～32767。

【使用指导】

打开指定单播端口的dump开关后，系统会在/proc/lipc/dumpinfo文件中记录该端口的所有报文收发信息。
