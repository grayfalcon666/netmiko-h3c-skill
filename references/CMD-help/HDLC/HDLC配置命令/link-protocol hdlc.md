
**HDLC \-- HDLC配置命令 \-- link-protocol hdlc**

------------------------------------------------------------------------

**[link-protocol** **hdlc**]命令用来配置接口封装HDLC协议。

【命令】

**[link-protocol hdlc**]

【缺省情况】

接口封装PPP协议。

【视图】

POS接口视图/Serial接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

HDLC为链路层协议，可承载IP、IPv6等网络层协议。

【举例】

\# 配置接口Serial2/1/0封装HDLC协议。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 link-protocol hdlc

**HDLC \-- HDLC配置命令 \-- timer-hold**

------------------------------------------------------------------------

**[timer-hold**]命令用来配置接口发送keepalive报文的周期。

**[undo timer-hold**]命令用来恢复缺省情况。

【命令】

**[timer-hold*** seconds*]

**[undo timer-hold**]

【缺省情况】

接口发送keepalive报文的周期为10秒。

【视图】

POS接口视图/Serial接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：接口发送keepalive报文的周期，取值范围为0～32767，单位为秒。

【使用指导】

HDLC协议使用轮询机制来确认链路状态是否正常。

当接口上封装的链路层协议为HDLC时，链路层会周期性地向对端发送keepalive报文（可以通过**timer-hold**命令修改keepalive报文的发送周期），keepalive报文中携带了本端发送序号和前一次收到的对端发送序号。当接口收到对端发来的、携带有本端前一次发送序号的keepalive报文后，接口下次发送的keepalive报文中的发送序号将加一，否则发送序号不变。如果接口在*retry*个（可以通过**timer-hold retry**命令修改该个数）keepalive周期内无法收到对端发来的、携带有本端前一次发送序号的keepalive报文，链路层会认为对端故障，上报链路层Down。

需要注意的是：

·如果将keepalive报文的发送周期配置为0秒，则不发送keepalive报文。

·在配置keepalive报文的发送周期时，建议链路两端的设置保持一致。

·如果网络的延迟比较大，或拥塞程度较高，可以适当加大keepalive报文的发送间隔，以避免链路被认为发生故障而被关闭。

【举例】

\# 配置接口Serial2/1/0发送keepalive报文的周期为100秒。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-serial2/1/0 timer-hold 100

【相关命令】

·**timer-hold retry**

**HDLC \-- HDLC配置命令 \-- timer-hold retry**

------------------------------------------------------------------------

**[timer-hold** **retry**]命令用来配置允许接口重传的keepalive报文个数。

**[undo timer-hold retry**]命令用来恢复缺省情况。

【命令】

**[timer-hold** **retry** *retry*]

**[undo timer-hold retry**]

【缺省情况】

允许接口重传的keepalive报文个数为5。

【视图】

POS接口视图/Serial接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retry*]：允许接口重传的keepalive报文个数，取值范围为1～255。

【使用指导】

HDLC协议使用轮询机制来确认链路状态是否正常。

当接口上封装的链路层协议为HDLC时，链路层会周期性地向对端发送keepalive报文（可以通过**timer-hold**命令修改keepalive报文的发送周期），keepalive报文中携带了本端发送序号和前一次收到的对端发送序号。当接口发送keepalive报文后，如果在keepalive周期内收到对端发来的keepalive应答报文（该报文携带有本端前一次发送序号），接口下次发送的keepalive报文中的发送序号将加一，否则，每经过一个keepalive周期，接口将重发一次keepalive报文，该报文的发送序号不变。如果接口重发第*retry*个（可以通过**timer-hold retry**命令修改该个数）keepalive报文后，在keepalive周期内仍然没有收到对端发来的keepalive应答报文，链路层会认为对端故障，上报链路层down。

需要注意的是，如果网络的延迟比较大，或拥塞程度较高，可以适当加大*retry*值，以避免链路被认为发生故障而被关闭。

【举例】

\# 配置允许接口Serial2/1/0重传的keepalive报文个数为10。

\<Sysname\> system-view

Sysname interface serial 2/1/0

Sysname-Serial2/1/0 timer-hold retry 10

【相关命令】

·**timer-hold**

**HDLC \-- HDLC链路捆绑配置命令 \-- bandwidth**

------------------------------------------------------------------------

**[bandwidth**]命令用来配置接口的期望带宽。

**[undo bandwidth**]命令用来恢复缺省情况。

【命令】

**[bandwidth**]*bandwidth-value*

**[undo bandwidth**]

【缺省情况】

接口的期望带宽＝接口的波特率÷1000（kbit/s）。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth-value*]：表示接口的期望带宽，取值范围为1～400000000，单位为kbit/s。

【使用指导】

接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术-IP路由配置指导"中的"OSPF"、"OSPFv3"和"IS-IS"。

【举例】

\# 设置HDLC捆绑接口1的期望带宽为1000kbit/s。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 bandwidth 1000

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle id**

------------------------------------------------------------------------

**[bundle id**]命令用来将当前接口加入指定的HDLC捆绑。

**[undo bundle id**]命令用来将接口从HDLC捆绑中退出。

【命令】

**[bundle id** *bundle-id*]

**[undo bundle id**]

【缺省情况】

接口不属于任何HDLC捆绑。

【视图】

POS接口视图/Serial接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bundle-id*]：HDLC捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·一个接口只能加入一个HDLC捆绑，如果需要加入其他HDLC捆绑，必须先退出原来的HDLC捆绑。

·加入HDLC捆绑的接口封装的链路层协议必须为HDLC。接口加入HDLC捆绑之后不允许修改链路层协议。

·HDLC捆绑接口没有创建的情况下，也允许将接口加入HDLC捆绑。

【举例】

\# 将POS接口2/2/0加入HDLC捆绑1。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 bundle id 1

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle load-balance**

------------------------------------------------------------------------

**[bundle load-balance**]命令用来配置负载分担方式。

**[undo bundle load-balance**]命令用来恢复缺省情况。

【命令】

**[bundle load-balance**[ { **per-flow** \| **per-packet** }]]

**[undo bundle load-balance**]

【缺省情况】

采用逐包负载分担。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[per-flow**]：逐流负载分担。

**[per-packet**]：逐包负载分担。

【使用指导】

负载分担方式分为逐流负载分担和逐包负载分担两种，原理如下：

·逐流负载分担：通过源IP地址和目的IP地址等将报文分成不同的流，同一条流的报文将在同一个选中成员接口上发送。目前支持IPv4、IPv6报文根据源IP地址和目的IP地址进行分流，MPLS报文根据标签进行分流。

·逐包负载分担：以报文为单位，轮流从所有选中成员接口中选择接口发送报文。

【举例】

\# 配置HDLC捆绑接口1采用逐流负载分担方式发送报文。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 bundle load-balance per-flow

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle max-active links**

------------------------------------------------------------------------

**[bundle max-active links**]命令用来配置最多选中成员接口数目。

**[undo bundle max-active links**]命令用来取消限制。

【命令】

**[bundle max-active links **]*number*

**[undo bundle max-active links**]

【缺省情况】

以设备支持的最多选中成员接口数目为准。不同设备支持的最多选中成员接口数目不同，请以设备的实际情况为准。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最多选中成员接口数目，取值范围为1～16。

【使用指导】

·本命令配置的值不能小于**bundle min-active links**命令配置的值。

·本命令一般需要和**bundle member-priority**命令配合使用，以保证两台设备相互连接的接口能够同时处于选中状态（只有两端接口同时处于选中状态，报文才能发送成功），避免出现一端接口处于选中状态，而另一端接口没有处于选中状态的情况。

【举例】

\# 配置最多选中成员接口数目为8。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 bundle max-active links 8

【相关命令】

·**bundle member-priority**

·**bundle min-active links**

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle member-priority**

------------------------------------------------------------------------

**[bundle member-priority**]命令用来配置接口的捆绑优先级。

**[undo bundle member-priority**]命令用来恢复缺省情况。

【命令】

**[bundle member-priority **]*priority*

**[undo bundle member-priority**]

【缺省情况】

接口的捆绑优先级为32768。

【视图】

POS接口视图/Serial接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：接口的捆绑优先级，取值范围为1～65535。*priority*值越大，接口的捆绑优先级越低。

【举例】

\# 配置POS接口2/2/0的捆绑优先级为1。

\<Sysname\> system-view

Sysname interface pos 2/2/0

Sysname-Pos2/2/0 bundle member-priority 1

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle min-active bandwidth**

------------------------------------------------------------------------

**[bundle min-active bandwidth**]命令用来配置最小激活带宽。

**[undo bundle min-active bandwidth**]命令用来取消限制。

【命令】

**[bundle min-active bandwidth **]*bandwidth*

**[undo bundle min-active bandwidth**]

【缺省情况】

不进行限制。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bandwidth*]：最小激活带宽，取值范围为64～1342177280，单位为kbps。

【举例】

\# 配置最小激活带宽为1000kbps。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 bundle min-active bandwidth 1000

**HDLC \-- HDLC链路捆绑配置命令 \-- bundle min-active links**

------------------------------------------------------------------------

**[bundle min-active links**]命令用来配置最少选中成员接口数目。

**[undo bundle min-active links**]命令用来取消限制。

【命令】

**[bundle min-active links **]*number*

**[undo bundle min-active links**]

【缺省情况】

不进行限制。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最少选中成员接口数目，取值范围为1～16。

【使用指导】

本命令配置的值不能大于**bundle max-active links**命令配置的值。

【举例】

\# 配置最少选中成员接口数目为5。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 bundle min-active links 5

【相关命令】

·**bundle max-active links**

**HDLC \-- HDLC链路捆绑配置命令 \-- default**

------------------------------------------------------------------------

**[default**]命令用来恢复默认配置。

【命令】

**[default**]

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。

您可以在执行**default**命令后通过**display this**命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。

【举例】

\# 将HDLC捆绑接口1恢复为缺省配置。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 default

**HDLC \-- HDLC链路捆绑配置命令 \-- description**

------------------------------------------------------------------------

**[description**]命令用来设置当前接口的描述信息。

**[undo description**]命令用来恢复缺省情况。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

接口的描述信息为"*该接口的接口名* Interface"，比如：HDLC-bundle1 Interface。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：接口描述信息，为1～255个字符的字符串，区分大小写。

【举例】

\# 配置HDLC捆绑接口1的描述信息为"HDLC-bundle interface"。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 description HDLC-bundle interface

**HDLC \-- HDLC链路捆绑配置命令 \-- display bundle hdlc-bundle**

------------------------------------------------------------------------

**[display bundle hdlc-bundle**]命令用来显示HDLC捆绑信息。

【命令】

集中式设备：

**[display bundle hdlc-bundle** [ *bundle-id* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display bundle hdlc-bundle** [ *bundle-id*  **slot** *slot-number*  **cpu** *cpu-number* ]]

分布式设备－IRF模式：

**[display bundle hdlc-bundle** [ *bundle-id*  **chassis** *chassis-number* **slot** *slot-number*  **cpu** *cpu-number* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[bundle-id*]：显示指定HDLC捆绑接口的捆绑信息。如果不指定本参数，将显示所有HDLC捆绑接口的捆绑信息。

**[slot** *slot-number*]：显示指定单板的HDLC捆绑信息。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备的HDLC捆绑信息。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的HDLC捆绑信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的HDLC捆绑信息。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的HDLC捆绑信息。*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU的HDLC捆绑信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

主用主控板显示信息中包括了所有成员接口的信息；备用主控板、接口板显示信息中只包括选中成员接口的信息，不包括非选中成员接口的信息。

【举例】

\# 显示主用主控板HDLC捆绑接口1的捆绑信息。（集中式设备）

\<Sysname\> display bundle hdlc-bundle 1

Bundle: HDLC-bundle1

  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps

  Selected members: 2, Total bandwidth: 1244160 kbps

  Member              State               Bandwidth(kbps)     Priority

  Pos2/2/1            Selected            622080              1

  Pos2/2/2            Selected            622080              2

  Pos2/2/4            Ready               622080              32768

  Pos2/2/3            Ready               622080              65535

  Pos2/2/5            Ready               155520              32768

  Pos2/2/6            Ready               155520              32768

\# 显示1号单板上CPU 0的HDLC捆绑接口1的捆绑信息。（分布式设备－独立运行模式）

\<Sysname\> display bundle hdlc-bundle 1 slot 1 cpu 0

Bundle: HDLC-bundle1, slot 1 cpu 0

  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps

  Selected members: 2, Total bandwidth: 1244160 kbps

  Member              State               Bandwidth(kbps)     Priority

  Pos2/2/1            Selected            622080              1

  Pos2/2/2            Selected            622080              2

\# 显示成员设备1上CPU 0的HDLC捆绑接口1的捆绑信息。（集中式IRF设备）

\<Sysname\> display bundle hdlc-bundle 1 slot 1 cpu 0

Bundle: HDLC-bundle1, slot 1 cpu 0

  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps

  Selected members: 2, Total bandwidth: 1244160 kbps

  Member              State               Bandwidth(kbps)     Priority

  Pos2/2/1            Selected            622080              1

  Pos2/2/2            Selected            622080              2

\# 显示成员设备1上1号单板上CPU 0的HDLC捆绑接口1的捆绑信息。（分布式设备－IRF模式）

\<Sysname\> display bundle hdlc-bundle 1 chassis 1 slot 1 cpu 0

Bundle: HDLC-bundle1, chassis 1, slot 1 cpu 0

  max-active links: 2, min-active links: 2, min-active bandwidth: 1000000 kbps

  Selected members: 2, Total bandwidth: 1244160 kbps

  Member              State               Bandwidth(kbps)     Priority

  Pos2/2/1            Selected            622080              1

  Pos2/2/2            Selected            622080              2

表1-1 display bundle hdlc-bundle命令显示信息描述表

字段

描述

Bundle

HDLC捆绑接口的名称

chassis

显示信息接口板所在成员设备编号

slot

显示信息所在接口板槽位号

cpu

显示信息所在CPU的编号

max-active links

HDLC捆绑接口上配置的最多选中成员接口数目（如果没有配置则不显示此配置项）

min-active links

HDLC捆绑接口上配置的最少选中成员接口数目（如果没有配置则不显示此配置项）

min-active bandwidth

HDLC捆绑接口上配置的最小激活带宽（如果没有配置则不显示此配置项）

Selected members

当前选中的成员接口数目

Total bandwidth

HDLC捆绑接口下所有选中成员接口带宽之和

Member

成员接口名称

State

成员接口状态，各含义如下：

·Selected：选中状态（接口板只显示该状态的成员接口信息）

·Ready：就绪状态

·Negotiated：协商状态

·Initial：初始状态

Bandwidth(kbps)

成员接口的带宽，单位为kbps

Priority

成员接口的捆绑优先级

**HDLC \-- HDLC链路捆绑配置命令 \-- display interface hdlc-bundle**

------------------------------------------------------------------------

**[display interface hdlc-bundle**]命令用来显示HDLC捆绑接口的相关信息。

【命令】

**[display interface** [ **hdlc-bundle** [ *bundle-id*    **brief** [ **description** \| **down** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[bundle-id*]：显示指定HDLC捆绑接口的相关信息。

**[brief**]：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。

**[description**]：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过27个字符，不指定该参数时，只显示描述信息中的前27个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。

**[down**]：显示当前物理状态为down的接口的信息以及down的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。

【使用指导】

·如果不指定**hdlc-bundle**参数，将显示设备支持的所有接口的相关信息。

·如果指定**hdlc-bundle**参数，不指定*bundle-id*参数，将显示所有HDLC捆绑接口的相关信息。

【举例】

\# 显示HDLC捆绑接口1的详细信息。

\<Sysname\> display interface hdlc-bundle 1

HDLC-bundle1

Current state: UP

Line protocol state: UP

Description: HDLC-bundle1 Interface

Bandwidth: 128kbps

Maximum Transmit Unit: 1500

Hold timer: 10 seconds, retry times: 5

Internet Address is 1.1.1.2/24 Primary

Link layer protocol: HDLC

Physical: HDLC-BUNDLE, baudrate: 128000 bps

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

Last clearing of counters: Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Input: 32 packets, 1842 bytes, 0 drops

Output: 27 packets, 1512 bytes, 0 drops

\# 显示HDLC捆绑接口1的概要信息。

\<Sysname\> display interface hdlc-bundle 1 brief

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Protocol: (s) - spoofing

Interface            Link Protocol Main IP         Description

HBDL1                UP   UP(s)    1.1.1.2

\# 显示当前物理状态为down的HDLC捆绑接口的信息以及down的原因。

\<Sysname\> display interface hdlc-bundle brief down

Brief information on interface(s) under route mode:

Link: ADM - administratively down; Stby - standby

Interface            Link Cause

HBDL2                ADM  Administratively

表1-2 display interface hdlc-bundle命令显示信息描述表

字段

描述

Current state

HDLC捆绑接口的物理状态和管理状态，状态可能为：

·DOWN ( Administratively )：表示该接口已经通过**shutdown**命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭

·UP：表示该接口的管理状态和物理状态均为开启

Line protocol state

HDLC捆绑接口的链路层协议状态，状态可能为：

·DOWN：表示数据链路层协议状态为关闭，一般是没有选中成员接口

·UP：表示数据链路层协议状态为开启

Description

HDLC捆绑接口的描述信息

Bandwidth

HDLC捆绑接口的期望带宽

Maximum Transmit Unit

HDLC捆绑接口的最大传输单元

Hold timer

当前接口发送keepalive报文的时间间隔

（HDLC捆绑接口不发送keepalive报文，此字段无意义）

retry times

允许接口重传的keepalive报文个数

（HDLC捆绑接口不发送keepalive报文，此字段无意义）

Internet Address is 1.1.1.2/24 Primary

HDLC捆绑接口的IP地址。如果接口尚未配置IP地址，本字段将变为"Internet protocol processing: disabled"

Link layer protocol

HDLC捆绑接口封装的链路层协议

Physical

HDLC捆绑接口的物理类型

baudrate

HDLC捆绑接口的波特率

Output queue - Urgent queuing: Size/Length/Discards 0/100/0

Output queue - Protocol queuing: Size/Length/Discards 0/500/0

Output queue - FIFO queuing: Size/Length/Discards 0/75/0

HDLC捆绑接口输出队列的类型：

·紧急发送队列的报文统计

·协议发送队列的报文统计

·先入先出发送队列的报文统计

Last clearing of counters

最近一次使用**reset counters interface**命令清除接口下的统计信息的时间。如果从设备启动一直没有执行**reset counters interface**命令清除过该接口下的统计信息，则显示Never

Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec

当前接口最近300秒内输入（input）和输出（output）报文的平均速率

Input: 32 packets, 1842 bytes, 0 drops

接口输入的报文总数（分别以包和字节为单位进行了统计），输入报文中丢弃的报文数

Output: 27 packets, 1512 bytes, 0 drops

接口输出的报文总数（分别以包和字节为单位进行了统计），输出报文中丢弃的报文数

Brief information on interface(s) under route mode

三层接口的概要信息

Link: ADM - administratively down; Stby - standby

·如果某接口的Link属性值为"ADM"，则表示该接口被管理员手工关闭了，需要在该接口下执行**undo shutdown**命令才能恢复接口本身的物理状态

·如果某接口的Link属性值为"Stby"，则表示该接口是一个备份接口，使用**display interface-backup state**命令可以查看该备份接口对应的主接口

Protocol: (s) - spoofing

如果某接口的Protocol属性值中带有"(s)"，则表示该接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Interface

接口名称缩写

Link

接口物理连接状态，取值可能为：

·UP：表示接口物理上是连通的

·ADM：表示接口被手工关闭了，需要执行**undo shutdown**命令才能打开接口

Protocol

接口数据链路层协议状态，取值可能为：

·UP：表示接口的数据链路层是连通的

·DOWN：表示接口的数据链路层不通

·UP(s)：表示接口的数据链路层协议状态显示为UP，但实际可能没有对应的链路，或者对应的链路不是永久存在而是按需建立的

Main IP

接口主IP地址（\--表示没有为该接口配置主IP地址）

Description

用户通过**description**命令给接口配置的描述信息。使用**display interface brief**命令，不指定**description**参数时，该字段最多显示27个字符；指定**description**参数时，可显示配置的全部描述信息

Cause

接口物理连接状态为down的原因，取值为Administratively时表示本链路被手工关闭了（配置了**shutdown**命令），需要执行**undo shutdown**命令才能恢复真实的物理状态

【相关命令】

·**reset counters interface**

**HDLC \-- HDLC链路捆绑配置命令 \-- interface hdlc-bundle**

------------------------------------------------------------------------

**[interface hdlc-bundle**]命令用来创建HDLC捆绑接口并进入HDLC捆绑接口视图。如果该HDLC捆绑接口已经存在，则直接进入该HDLC捆绑接口视图。

**[undo interface hdlc-bundle**]命令用来删除HDLC捆绑接口。

【命令】

**[interface hdlc-bundle ***bundle-id*]

**[undo interface hdlc-bundle ***bundle-id*]

【缺省情况】

不存在HDLC捆绑接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bundle-id*]：HDLC捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 创建HDLC捆绑接口1并进入HDLC捆绑接口视图。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1

**HDLC \-- HDLC链路捆绑配置命令 \-- mtu**

------------------------------------------------------------------------

**[mtu**]命令用来配置HDLC捆绑接口的MTU（Maximum Transmission Unit，最大传输单元）值。

**[undo mtu**]命令用来恢复缺省情况。

【命令】

**[mtu** *size*]

**[undo mtu**]

【缺省情况】

HDLC捆绑接口的MTU值为1500字节。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：接口的MTU值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

接口的MTU值影响IP协议报文在该接口上传输时的分片与重组。

需要注意的是，配置了**mtu**命令后需要执行命令**shutdown**和**undo shutdown**，这样该配置才能在接口上生效。

【举例】

\# 配置HDLC捆绑接口1的MTU值为1430字节。

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 mtu 1430

**HDLC \-- HDLC链路捆绑配置命令 \-- reset counters interface**

------------------------------------------------------------------------

**[reset counters interface**]命令用来清除HDLC捆绑接口的统计信息。

【命令】

**[reset counters interface ** **hdlc-bundle**  *bundle-id*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bundle-id*]：HDLC捆绑接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。

·如果不指定**hdlc-bundle**和*bundle-id*，则清除所有接口的统计信息；

·如果指定**hdlc-bundle**而不指定*bundle-id*，则清除所有HDLC捆绑接口的统计信息；

·如果同时指定**hdlc-bundle**和*bundle-id*，则清除指定HDLC捆绑接口的统计信息。

【举例】

\# 清除HDLC捆绑接口HDLC-bundle1上的统计信息。

\<Sysname\> reset counters interface hdlc-bundle1

【相关命令】

·**display interface hdlc-bundle**

**HDLC \-- HDLC链路捆绑配置命令 \-- service**

------------------------------------------------------------------------

**[service**]命令用来指定处理当前接口流量的业务板。

**[undo service**]命令用来恢复缺省情况。

【命令】

分布式设备－独立运行模式/集中式IRF设备：

**[service slot*** slot-number*]

**[undo service slot**]

分布式设备－IRF模式：

**[service chassis ***chassis-number*** slot*** slot-number*]

**[undo service chassis**]

【缺省情况】

没有指定处理当前接口流量的业务板。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：指定单板所在的槽位号。*slot-number*表示单板所在的槽位号。（分布式设备－独立运行模式）

**[slot** *slot-number*]：指定设备在IRF中的成员编号。*slot-number*表示设备在IRF中的成员编号。（集中式IRF设备）

**[chassis** *chassis-number* **slot** *slot-number*]：指定成员设备上的指定单板。*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。（分布式设备－IRF模式）

【使用指导】

没有通过**service**命令指定处理流量的业务板时，由收到数据流量的接口所在单板作为处理HDLC捆绑接口流量的业务板。为了避免同一个单板处理过多的流量，可以指定处理HDLC捆绑接口流量的业务板。

需要注意的是，如果拔出了本命令所指定的业务板，即使HDLC捆绑接口UP，流量也无法正常处理；如果重新插入指定的业务板，则流量可以恢复在该板的正常处理。

【举例】

\# 指定1号单板为处理HDLC捆绑接口1流量的业务板。（分布式设备－独立运行模式）

\# 指定1号成员设备为处理HDLC捆绑接口1流量的业务处理设备。（集中式IRF设备）

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 service slot 1

\# 指定1号成员设备的1号单板为处理HDLC捆绑接口1流量的业务板。（分布式设备－IRF模式）

\<Sysname\> system-view

Sysname interface hdlc-bundle 1

Sysname-HDLC-bundle1 service chassis 1 slot 1

**HDLC \-- HDLC链路捆绑配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭接口。

**[undo** **shutdown**]命令用来打开接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

接口处于打开状态。

【视图】

HDLC捆绑接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当打开HDLC捆绑接口时，会触发重新确定成员接口的状态；当关闭HDLC捆绑接口时，所有选中成员口都会变成协商状态。

【举例】

\# 关闭HDLC捆绑接口HDLC-bundle1。

\<Sysname\> system-view

Sysname hdlc-bundle 1

Sysname-HDLC-bundle1 shutdown

