
**多机备份配置命令 \-- 多机备份对端配置命令 \-- display vsrp peer**

------------------------------------------------------------------------

**[display vsrp peer**]命令用来显示多机备份组信息。

【命令】

**[display vsrp peer** [ *peer-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[peer-name*]*：*多机备份组名称，取值为1～31个字符的字符串，区分大小写。

【使用指导】

不指定多机备份组名称时，命令显示所有的多机备份组信息。

【举例】

\# 显示已创建的多机备份组pname的信息。

\<Sysname\> display vsrp peer pname

VSRP peer name: pname

 TCP status: Connected

 Peer IP: 11.0.0.3

 Local IP: 10.0.0.3

 Port: 6000

 Track ID: 5

 Track status: Positive

\# 显示全部已创建的多机备份组的信息

\<Sysname\> display vsrp peer

VSRP peer name: pname1

 TCP status: Connected

 Peer IP: 11.0.0.3

 Local IP: 10.0.0.3

 Port: 6000

 Track ID: 5

 Track status: Positive

VSRP peer name: pname2

 TCP status：Disconnected

 Peer IP: 10.0.0.2

 Local IP: 11.0.0.2

 Port: 5000

 Track ID: 5

 Track status: Negative

表1-1 display vsrp peer命令显示信息描述表

字段

描述

VSRP peer name

多机备份组名

TCP status

多机备份组TCP连接状态，取值包含：

Disconnected：连接已断开

Connected：连接已建立

Peer IP

多机备份组中TCP连接的对端IP地址

Local IP

多机备份组中TCP连接的本端IP地址

Port

多机备份组中TCP连接绑定的端口号

Track ID

多机备份组关联的Track项

Track status

多机备份组关联的Track项状态，取值包含：

·Positive：表示状态正常

·NotReady：表示无效值

·Negative：表示状态异常

**多机备份配置命令 \-- 多机备份对端配置命令 \-- peer**

------------------------------------------------------------------------

**[peer**]命令用来配置到多机备份对端的TCP连接。

**[undo peer**]命令用来删除到多机备份对端的TCP连接。

【命令】

**[peer ***peer-ip-address*** local ***local-ip-address***** **port** *port-id* ]

**[undo peer**]

【缺省情况】

未配置到多机备份对端的TCP连接。

【视图】

多机备份对端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-ip-address*]：表示多机备份中的对端设备IP地址。

**[local*** local-ip-address*]：表示多机备份中的本端设备IP地址。

**[port*** port-id*]：表示TCP连接绑定的端口号，取值范围为1024～65535，默认端口号为60032。

【使用指导】

·配置TCP连接时，本端和对端设备IP地址必须为单播地址，且不允许配置为全零地址或环回地址。

·配置TCP连接时，本端和对端设备IP地址不能相同；任意两个多机备份组内TCP连接的本端和对端IP地址不能完全相同。

·配置TCP连接时，绑定的端口号不能与已有的TCP监听服务使用的端口号冲突。

·若多机备份组内已配置TCP连接，重新配置一条TCP连接时，需要先删除当前TCP连接，否则无法配置成功。

【举例】

\# 在名为pname的多机备份组中，创建TCP连接，本端设备IP为11.0.0.2，对端设备IP为10.0.0.1，TCP连接绑定的端口号为7000。

\<Sysname\> system-view

Sysname vsrp peer pname

Sysname-vsrp-peer-pname peer 10.0.0.1 local 11.0.0.2 port 7000

**多机备份配置命令 \-- 多机备份对端配置命令 \-- peer ipv6**

------------------------------------------------------------------------

**[peer ipv6**]命令用来配置到多机备份对端的IPv6 TCP连接。

**[undo peer ipv6**]命令用来删除到多机备份对端的IPv6 TCP连接。

【命令】

**[peer ipv6 ***peer-ipv6-address*** local ***local-ipv6-address***** **port** *port-id* ]

**[undo peer ipv6**]

【缺省情况】

未配置到多机备份对端的IPv6 TCP连接。

【视图】

多机备份对端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-ipv6-address*]：表示多机备份中的对端设备IPv6地址。

**[local*** local-ipv6-address*]：表示多机备份中的本端设备IPv6地址。

**[port*** port-id*]：表示IPv6TCP连接绑定的端口号，取值范围为1024～65535，默认端口号为60032。

【使用指导】

·配置IPv6 TCP连接时，本端和对端设备IPv6地址必须为单播地址，且不允许配置为全零地址或环回地址。

·配置IPv6 TCP连接时，本端和对端设备IPv6地址不能相同；任意两个多机备份组内IPv6 TCP连接的本端和对端IPv6地址不能完全相同。

·配置IPv6 TCP连接时，绑定的端口号不能与已有的IPv6 TCP监听服务使用的端口号冲突。

·若多机备份组内已配置IPv6 TCP连接，重新配置一条IPv6 TCP连接时，需要先删除当前IPv6 TCP连接，否则无法配置成功。

【举例】

\# 在名为pname的多机备份组中，创建IPv6 TCP连接，本端设备IPv6地址为1::1，对端设备IPv6地址为2::2，IPv6 TCP连接绑定的端口号为7000。

\<Sysname\> system-view

Sysname vsrp peer pname

Sysname-vsrp-peer-pname peer ipv6 2::2 local 1::1 port 7000

**多机备份配置命令 \-- 多机备份对端配置命令 \-- track**

------------------------------------------------------------------------

**[track**]命令用来配置监视指定的Track项。

**[undo track**]命令用来取消监视指定的Track项。

【命令】

**[track*** track-entry-number*]

**[undo track**]

【缺省情况】

未配置监视指定的Track项。

【视图】

多机备份对端视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]*：*被监视Track项的序号，取值范围为1～1024，本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【使用指导】

用户可以通过多机备份组关联Track来快速检测通道是否可用。未关联Track项时，多机备份组只能依靠TCP连接的状态来检查通道是否可用。当关联Track状态为Positive或NotReady时，多机备份模块才会尝试与对端设备建立TCP连接；当关联Track的状态为Negative时，断开与对端设备的控制TCP连接。

当TCP连接有效时，设备上的多机备份功能才是生效的。

Track项的详细介绍请参见"可靠性配置指导"中的"Track"。

【举例】

\# 在名为pname的多机备份对端视图下，配置关联Track项，Track序号为10。

\<Sysname\> system-view

Sysname vsrp peer pname

Sysname-vsrp-peer-pname track 10

**多机备份配置命令 \-- 多机备份对端配置命令 \-- vsrp peer**

------------------------------------------------------------------------

**[vsrp peer**]命令用来创建多机备份对端并进入多机备份对端视图。如果已创建多机备份对端，执行该命令直接进入多机备份对端视图。

**[undo vsrp peer**]命令用来删除指定的多机备份对端。

【命令】

**[vsrp peer ***peer-name*]

**[undo vsrp peer*** peer-name*]

【缺省情况】

未创建多机备份对端。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-name*]：多机备份对端名称，取值为1～31个字符的字符串，区分大小写。

【使用指导】

·设备上最多支持创建64个多机备份对端。

·删除多机备份对端时，若已有多机备份实例关联该多机备份对端，需先解除关联关系，否则无法删除。

【举例】

\# 创建名称为pname的多机备份组并进入多机备份对端视图。

\<Sysname\> system-view

Sysname vsrp peer pname

Sysname-vsrp-peer-pname

**多机备份配置命令 \-- 多机备份实例配置命令 \-- backup id**

------------------------------------------------------------------------

**[backup id**]命令用来配置多机备份实例的备份ID。

**[undo backup id**]命令用来删除多机备份实例的备份ID。

【命令】

**[backup id ***backup-id*** peer ***peer-name*]

**[undo backup******id**]

【缺省情况】

未配置多机备份实例的备份ID。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[backup-id*]：表示多机备份实例的备份标识符，取值范围为1～1024。

*[peer-name*]：表示关联的多机备份对端名称，为1～31个字符的字符串，区分大小写。

【使用指导】

需要注意的是:

·配置多机备份实例备份ID时，多机备份对端必须已存在，且*backup-id*在该多机备份对端内未被使用过。

·配置多机备份实例备份ID时，若多机备份实例已配置备份ID，则需先删除当前备份ID后，才能配置新的备份ID。

【举例】

\# 配置名为aaa的多机备份实例在多机备份对端pname中的备份ID为5。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa backup id 5 peer pname

**多机备份配置命令 \-- 多机备份实例配置命令 \-- backup mode**

------------------------------------------------------------------------

**[backup mode**]命令用来设置多机备份实例的备份模式。

**[undo backup mode **]命令用来恢复缺省情况。

【命令】

**[backup mode **[{ **hot** \| **warm** }]]

**[undo backup mode**]

【缺省情况】

多机备份实例的备份模式为热备份。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[hot**]：表示热备份。

**[warm**]：表示温备份。

【使用指导】

在不同的备份模式下，对于收到的备份信息，设备有以下处理方式：

·热备份：当备用设备收到主用设备的备份信息后，立即下发备份信息到转发平面。这样，主用设备发生故障时，备用设备能马上指导报文转发，可以实现业务终端快速切换。

·温备份：当备用设备收到主用设备的备份信息后，不会立即下发备份信息到转发平面，当主用设备发生故障后，设备的主备状态发生切换，备用设备才开始才开始下发备份信息到转发平面，并指导报文转发。业务切换到备用设备上的时间比热备份切换时间稍长。

【举例】

\# 设置多机备份实例备份模式为温备份。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa backup mode warm

**多机备份配置命令 \-- 多机备份实例配置命令 \-- bind vrrp vrid**

------------------------------------------------------------------------

**[bind vrrp vrid**]命令用来绑定多机备份实例和VRRP备份组。

**[undo bind vrrp**]命令用来解除多机备份实例和VRRP备份组的绑定。

【命令】

**[bind vrrp vrid*** virtual-router-id ***interface*** interface-type interface-number*]

**[undo bind vrrp**]

【缺省情况】

未绑定多机备份实例和VRRP备份组。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：表示VRRP备份组ID，取值范围为1～255。

**[interface** *interface-type interface-number*]：表示VRRP备份组所属接口的接口类型和接口编号。

【使用指导】

多机备份实例通过绑定VRRP备份组来确定自身的主备身份。一个多机备份实例只能绑定一个VRRP备份组。指定VRRP备份组时，VRRP备份组可以不存在于指定的接口下。

【举例】

\# 配置多机备份实例aaa与接口GigabitEthernet 2/0/2上IPv4的VRRP备份组2绑定。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa bind vrrp vrid 2 interface gigabitethernet 2/0/2

**多机备份配置命令 \-- 多机备份实例配置命令 \-- bind vrrp ipv6 vrid**

------------------------------------------------------------------------

**[bind vrrp ipv6 vrid**]命令用来绑定多机备份实例和IPv6 VRRP备份组。

**[undo bind vrrp ipv6**]命令用来解除多机备份实例和IPv6 VRRP备份组的绑定。

【命令】

**[bind vrrp ipv6 vrid*** virtual-router-id ***interface*** interface-type interface-number*]

**[undo bind vrrp ipv6**]

【缺省情况】

未绑定多机备份实例和IPv6 VRRP备份组。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：表示IPv6 VRRP备份组ID，取值范围为1～255。

**[interface** *interface-type interface-number*]：表示IPv6 VRRP备份组所属接口的接口类型和接口编号。

【使用指导】

多机备份实例中的设备通过绑定IPv6 VRRP备份组来确定自身的主备身份。一个多机备份实例只能绑定一个IPv6 VRRP备份组。指定IPv6 VRRP备份组时，IPv6 VRRP备份组可以不存在于指定的接口下。

【举例】

\# 配置多机备份实例aaa与接口GigabitEthernet1/0/1上IPv6 VRRP备份组2绑定。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa bind vrrp ipv6 vrid 2 interface gigabitethernet 1/0/1

**多机备份配置命令 \-- 多机备份实例配置命令 \-- display vsrp instance**

------------------------------------------------------------------------

**[display vsrp instance**]命令显示多机备份实例信息。

【命令】

**[display vsrp instance ** *instance-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-name*]*：*多机备份实例名，取值为1～31个字符的字符串，区分大小写。

【描述】

不指定多机备份实例名称时，显示所有的多机备份实例信息。

【举例】

\# 显示已创建的多机备份实例aaa信息。

\<Sysname\> display vsrp instance aaa

VSRP instance name: aaa

 VSRP peer name: pname1

 Backup ID: 10

 Bound VRID: VRRP VRID 1 interface GigabitEthernet2/0/1

 Instance status: Master

 Local status: Master

 Peer status: Backup

 Backup mode: Warm

 Traffic backup interval: 10(minutes)

 Traffic backup threshold: 50(MB)

 NAS IP: 10.0.0.1

 NAS port: GigabitEthernet2/0/2

 NAS ID: h3c

\# 显示全部已创建的多机备份实例信息。

\<Sysname\> display vsrp instance

VSRP instance name: aaa

 VSRP peer name: pname1

 Backup ID: 10

 Bound VRID: VRRP VRID 1 interface GigabitEthernet2/0/1

 Instance status : Master

 Local status: Master

 Peer status: Backup

 Backup mode: Warm

 Traffic backup interval: 10(minutes)

 Traffic backup threshold: 50(MB)

 NAS IP: 10.0.0.1

 NAS port: GigabitEthernet2/0/2

 NAS ID: h3c

VSRP instance name: bbb

 VSRP peer name: pname2

 Backup ID: 10

 Bound VRID: VRRP VRID 2 interface GigabitEthernet3/0/1

 Instance status : Master

 Local status: Master

 Peer status: Backup

 Backup mode: Warm

 Traffic backup interval: 5(minutes)

 Traffic backup threshold: 100(MB)

 NAS IP: 10.0.0.2

 NAS port: GigabitEthernet3/0/2

 NAS ID: h3c

表1-2 display vsrp instance命令显示信息描述表

字段

描述

VSRP instance name

多机备份实例名

VSRP peer name

多机备份实例关联的多机备份对端名

Backup ID

多机备份实例备份ID

Bound VRID

多机备份实例绑定接口下的VRID

Instance status

多机备份实例状态，状态取值包括：

·Master：表示在该多机备份实例中，本设备作为主用设备

·Backup：表示在该多级备份实例中，本设备作为备用设备

·Down：表示在该多机备份实例中，本设备不运行

Local status

本端本地状态，状态取值包括：

·Master：表示主用状态

·Backup：表示备用状态

·Init：表示初始化状态

·Down：表示未获取到本端本地状态

Peer status

对端本地状态，状态取值包括：

·Master：表示主用状态

·Backup：表示备用状态

·Init：表示初始化状态

·Down：表示未获取到对端本地状态

Backup mode

多机备份实例备份模式，取值为：

·Hot：热备份

·Warm：温备份

Traffic backup interval

流量备份时间间隔

Traffic backup threshold

流量备份阈值

NAS IP

业务逻辑IP地址

NAS port

业务逻辑接口名

NAS ID

业务逻辑主机名

**多机备份配置命令 \-- 多机备份实例配置命令 \-- nas**

------------------------------------------------------------------------

**[nas**]命令用来配置NAS参数。

**[undo nas**]命令用来删除已配置的NAS参数。

【命令】

**[nas**[ { **id** *host-name* **\| ip** *ip-address* \| **port** *interface-type interface-number* }]]

**[undo**[ **nas** [ **id** \| **ip** \| **port** ]]]

【缺省情况】

未配置NAS参数。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[id*** host-name*]：表示业务逻辑主机名，为1～127个字符的字符串，不区分大小写。

**[ip*** ip-address*]：表示业务逻辑IP地址。

**[port** *interface-type interface-number*]：表示业务逻辑的接口类型和接口编号，目前支持接口类型为[:三层]以太网接口类型和三层聚合接口类型。

【使用指导】

NAS(Network Access Server)表示网络接入服务。用户可以通过本命令在多机备份实例下配置业务逻辑IP地址、业务逻辑接口和业务逻辑主机名，使互为备份的设备上发送给RADIUS（Remote Authentication Dial-In User Service，远程认证拨号用户服务）服务器报文的NAS-IP-Address、NAS-Port属性以及上送给DHCP服务器报文的Option82字段信息保持一致。

需要注意的是：

·配置业务逻辑IP地址时，必须配置为单播地址，且不允许配置为全零地址或环回地址。

·配置业务逻辑接口时，允许配置成当前设备上不存在的接口。逻辑接口的位置信息格式为"槽位号/子卡号/接口号"。

【举例】

\# 配置业务逻辑IP地址为2.2.2.2。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa nas ip 2.2.2.2

\# 配置业务逻辑接口为GigabitEthernet1/0/1。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa nas port gigabitethernet 1/0/1

\# 配置业务逻辑主机名为bbb。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa nas id bbb

**多机备份配置命令 \-- 多机备份实例配置命令 \-- traffic backup**

------------------------------------------------------------------------

**[traffic backup**]命令用来设置流量备份时间间隔或流量阈值。

**[undo traffic backup**]命令用来恢复缺省情况。

【命令】

**[traffic backup**[ { **interval** *interval-value* \| **threshold** *threshold-value* } \*]]

**[undo traffic backup**[ [ **interval** \| **threshold** ]]]

【缺省情况】

多机备份实例的流量备份时间间隔为10分钟，流量阈值缺省值为50MB。

【视图】

多机备份实例视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：表示流量备份时间间隔，取值范围为0～1440，单位为分钟（min）。

*[threshold-value*]：表示流量阈值，取值范围为0～100000，单位为兆字节（MB）。

【使用指导】

多机备份实例支持配置流量备份时间间隔和流量备份阈值。以特定业务为例，当业务持续转发时间达到流量备份时间间隔或转发业务的流量达到阈值时，多机备份实例需要对该业务模块数据进行备份操作。

当流量备份时间间隔和流量阈值均为0时，表示不备份用户流量。

【举例】

\# 当流量备份时间达到为50分钟时，进行业务模块数据的备份操作。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa traffic backup interval 50

\# 当转发流量达到200MB时，进行业务模块数据的备份操作。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa traffic backup threshold 200

\# 恢复流量备份时间和流量阈值为缺省值。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa undo traffic backup

**多机备份配置命令 \-- 多机备份实例配置命令 \-- vsrp instance（系统视图）**

------------------------------------------------------------------------

**[vsrp instance**]命令用来创建多机备份实例并进入多机备份实例视图。如果指定的多机备份实例已创建，则该命令直接用来进入该多机备份实例视图。

**[undo vsrp instance**]命令用来删除已创建的多机备份实例。

【命令】

**[vsrp instance*** instance-name*]

**[undo vsrp instance*** instance-name*]

【缺省情况】

未创建多机备份实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-name*]：表示多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·多机备份实例作为业务应用模块的关联实体，在实际应用中，须配置关联多机备份对端并绑定VRRP备份组，备份模式及流量备份方式。

·设备上最多支持创建1024个多机备份实例。

【举例】

\# 创建名为aaa的多机备份实例，并进入多机备份实例视图。

\<Sysname\> system-view

Sysname vsrp instance aaa

Sysname-vsrp-instance-aaa

**多机备份配置命令 \-- 配置IPv6虚拟地址 \-- ipv6 virtual-address**

------------------------------------------------------------------------

**[ipv6 virtual-address**]命令用来配置IPv6虚拟地址，并绑定多机备份实例。

**[undo ipv6 virtual-address**]命令用来恢复缺省情况。

【命令】

**[ipv6 virtual-address ***ipv6-address ***vsrp ***vsrp-instance*]

**[undo ipv6 virtual-address**]

【缺省情况】

未配置IPv6虚拟地址。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/三层RPR逻辑接口视图/VLAN接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ipv6-address*]：配置的IPv6虚拟地址，该地址必须为链路本地地址，局域网内的主机可以通过这个虚拟地址与外部网络进行通信。

**[vsrp ***vsrp-instance*]：绑定的多机备份实例名称。*vsrp-instance*为多机备份的实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

l接口上使能IPv6 IPoE或DHCPv6的多机备份功能时，必须与本命令配合使用，本命令绑定的多机备份实例必须与该接口上IPv6 IPoE或DHCPv6绑定的多机备份实例保持一致，否则会影响多机备份功能正常使用，导致多机备份后倒换后,局域网内的主机无法访问外部网络。

l接口上未开启IPv6 IPoE或DHCPv6的多机备份功能时，请不要在该接口上配置IPv6虚拟地址，否则可能导致设备上原来的链路本地地址不可用。

l请不要将此命令与IPv6 VRRP备份组配置在同一个接口上，否则可能导致多机备份功能不能正常使用。

【举例】

\# 配置IPv6虚拟地址为fe80::10，并绑定多机备份实例aaa。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 virtual-address fe80::10 vsrp aaa

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ip subscriber vsrp-instance**

------------------------------------------------------------------------

**[ip subscriber vsrp-instance**]命令用来指定接口上IPv4 IPoE功能绑定的多机备份实例。

**[undo ip subscriber vsrp-instance**]用来恢复缺省情况。

【命令】

**[ip subscriber vsrp-instance ***instance-name*]

**[undo ip subscriber vsrp-instance**]

【缺省情况】

接口上的IPv4 IPoE功能未绑定多机备份实例。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-name*]：表示接口绑定的多机备份实例名，为1～31个字符的字符串，区分大小写。

【使用指导】

IPoE支持多机备份是指当一台设备故障时（包括设备故障、链路故障等），IPoE用户的业务可以自动切换到备用设备上来，已上线的IPoE用户不需要重新拨号，计费、授权信息不丢失。

用户通过该命令配置接口下IPv4 IPoE会话和指定多机备份实例关联，继而就可以通过多机备份提供的数据备份通道实时备份此接口上接入的动态IPv4 IPoE会话信息。

【举例】

\# 在接口GigabitEthernet1/0/1上使能IPv4 IPoE会话多机备份的功能，并绑定多机备份实例instance1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip subscriber vsrp-instance instance1

【相关命令】

·**ip subscriber ****vsrp-port**

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ip subscriber vsrp-port**

------------------------------------------------------------------------

**[ip subscriber vsrp-port**]命令用来配置IPoE建立IPv4数据备份通道使用的TCP端口号。

**[undo ip subscriber vsrp-port**]用来恢复缺省情况。

【命令】

**[ip subscriber vsrp-port ***port-number*]

**[undo ip subscriber vsrp-port**]

【缺省情况】

IPoE建立IPv4数据备份通道使用的TCP端口号为60033。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：TCP端口号，取值范围为1～65535。

【使用指导】

IPoE在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此条通道为TCP连接，可以通过本命令调整IPoE建立IPv4数据备份通道使用的TCP端口号。

【举例】

\#配置IPoE建立IPv4数据备份通道使用的TCP端口号为20000。

\<Sysname\> system-view

Sysname ip subscriber vsrp-port 20000

【相关命令】

·**ip subscriber ****vsrp-instance**

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ipv6 subscriber vsrp-instance**

------------------------------------------------------------------------

**[ipv6 subscriber vsrp-instance**]命令用来指定接口上的IPv6 IPoE功能绑定的多机备份实例。

**[undo ip subscriber vsrp-instance**]用来恢复缺省情况。

【命令】

**[ipv6 subscriber vsrp-instance ***instance-name*]

**[undo ipv6 subscriber vsrp-instance**]

【缺省情况】

接口上的IPv6 IPoE功能未绑定多机备份实例。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[instance-name*]：表示接口绑定的多机备份实例名，为1～31个字符的字符串，区分大小写。

【使用指导】

用户通过该命令配置接口下IPv6IPoE会话和指定多机备份实例关联，继而就可以通过多机备份提供的数据备份通道实时备份此接口上接入的动态IPv6IPoE会话信息。

【举例】

\# 在接口GigabitEthernet1/0/1上使能IPv6 IPoE会话多机备份的功能，并绑定多机备份实例为instance1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 subscriber vsrp-instance instance1

【相关命令】

·**ipv6 subscriber ****vsrp-port**

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ipv6 subscriber vsrp-port**

------------------------------------------------------------------------

**[ipv6 subscriber vsrp-port**]命令用来配置IPoE建立IPv6数据备份通道使用的TCP端口号。

**[undo ipv6 subscriber vsrp-port**]用来恢复缺省情况。

【命令】

**[ipv6 subscriber vsrp-port ***port-number*]

**[undo ipv6 subscriber vsrp-port**]

【缺省情况】

IPoE建立IPv6数据备份通道使用的TCP端口号为60040。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：TCP端口号，取值范围为1～65535。

【使用指导】

IPoE支持多机备份是指当一台设备故障时（包括设备故障、链路故障等），IPoE用户的业务可以自动切换到备用设备上来，已上线的IPoE用户不需要重新拨号，计费、授权信息不丢失。

IPoE在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此条通道为TCP连接，可以通过本命令调整IPoE建立IPv6数据备份通道使用的TCP端口号。

【举例】

\# 配置IPoE建立IPv6数据备份通道使用的TCP端口号为20000。

\<Sysname\> system-view

Sysname ipv6 subscriber vsrp-port 20000

【相关命令】

·**ipv6 subscriber ****vsrp-instance**

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- display ppp sync-session**

------------------------------------------------------------------------

**[display ppp sync-session**]命令用来查看同步的PPP会话信息。

【命令】

**[display ppp sync-session **\**[vsrp-instance***vsrp-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsrp-instance***vsrp-instance-name*]：显示指定多机备份实例同步的PPP会话信息。*vsrp-instance-name*表示多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，将显示所有多机备份实例同步的PPP会话信息。

【使用指导】

在主用设备和备用设备上都可以查询同步的PPP会话信息：

·在主用设备上查看的是主用设备同步给备用设备的PPP会话信息。

·在备用设备上查看的是备用设备从主用设备同步过来的PPP会话信息。

【举例】

\# 查看同步的PPP会话信息。

\<Sysname\> display ppp sync-session

VSRP instance: vsrp1

VSRP instance state: Master

Total synchronized PPP sessions: 2

SID    MAC address     Interface     IP address       Username

1      00e0-1500-0410  GE1/0/1       2.2.2.2          user1@isp1

2      00e0-1500-0411  GE1/0/1       2.2.2.3          user1@isp1

VSRP instance: vsrp2

VSRP instance state: Backup

Total synchronized PPP sessions: 1

SID    MAC address     Interface     IP address       Username

1      00e0-1500-0413  GE1/0/2       2.3.2.2          user1@isp1

VSRP instance: vsrp3

VSRP instance state: Down

Total synchronized PPP sessions: 0

SID    MAC address     Interface     IP address       Username

表1-3  display ppp sync-session命令显示信息描述表

字段

描述

VSRP instance

多机备份实例名称

VSRP instance state

多机备份实例状态：

·Master：表示在该多机备份实例中，本设备作为主用设备，此时显示的是本设备同步给备用设备的PPP会话信息

·Backup：表示在该多机备份实例中，本设备作为备用设备，此时显示的是本设备从主用设备同步过来的PPP会话信息

·Down：表示在该多机备份实例中，本设备不运行，此时没有同步的PPP会话信息（在下面两种情况下设备会处于Down状态：一是当VRRP备份组处于initialize状态时，互相备份的两台设备在对应VSRP实例中将都处于无法运行状态；二是本端VSRP实例不存在或者配置不完整）

Total synchronized PPP sessions

同步的PPP会话数目

SID

PPPoE会话session ID

MAC address

用户MAC地址

Interface

接入的接口名称

IP address

用户IP地址

Username

用户名称

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- display pppoe-server sync-session**

------------------------------------------------------------------------

**[display pppoe-server sync-session**]命令用来查看同步的PPPoE会话信息。

【命令】

**[display pppoe-server sync-session** [ **vsrp-instance** *vsrp-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[vsrp-instance***vsrp-instance-name*]：显示指定多机备份实例同步的PPPoE会话信息。*vsrp-instance-name*表示多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，将显示所有多机备份实例同步的PPPoE会话信息。

【使用指导】

在主用设备和备用设备上都可以查询同步的PPPoE会话信息：

·在主用设备上查看的是主用设备同步给备用设备的PPPoE会话信息。

·在备用设备上查看的是备用设备从主用设备同步过来的PPPoE会话信息。

【举例】

\# 查看同步的PPPoE会话信息。

\<Sysname\> display pppoe-server sync-session

VSRP instance: vsrp1

VSRP instance state: Master

Total synchronized PPPoE sessions: 2

SID    Service VLAN  Customer VLAN  MAC address    Interface

1      1             1              00e0-1500-0410 GE1/0/1

2      1             1              00e0-1500-0411 GE1/0/1

VSRP instance: vsrp2

VSRP instance state: Backup

Total synchronized PPPoE sessions: 1

SID    Service VLAN  Customer VLAN  MAC address    Interface

1      1             2              00e0-1500-0413 XGE1/0/2

VSRP instance: vsrp3

VSRP instance state: Down

Total synchronized PPPoE sessions: 0

SID    Service VLAN  Customer VLAN  MAC address    Interface

表1-4 display pppoe-server sync-session命令显示信息描述表

字段

描述

VSRP instance

VSRP实例名称

VSRP instance state

多机备份实例状态：

·Master：表示在该多机备份实例中，本设备作为主用设备，此时显示的是本设备同步给备用设备的PPPoE会话信息

·Backup：表示在该多机备份实例中，本设备作为备用设备，此时显示的是本设备从主用设备同步过来的PPPoE会话信息

·Down：表示在该多机备份实例中，本设备不运行，此时没有同步的PPPoE会话信息（在下面两种情况下设备会处于Down状态：一是当VRRP备份组处于initialize状态时，互相备份的两台设备在对应VSRP实例中将都处于无法运行状态；二是本端多机备份实例不存在或者配置不完整）

Total synchronized PPPoE sessions

同步的PPPoE会话数目

SID

PPPoE会话session ID

Service VLAN

服务提供商VLAN

Customer VLAN

用户VLAN

MAC address

用户MAC地址

Interface

接入的接口名称

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- ppp vsrp-port**

------------------------------------------------------------------------

**[ppp vsrp-port**]命令用来配置PPP会话数据备份通道的TCP端口号。

**[undo ppp vsrp-port**]命令用来恢复缺省情况。

【命令】

**[ppp vsrp-port ***port-number*]

**[undo ppp vsrp-port**]

【缺省情况】

PPP会话数据备份通道的TCP端口号为60035。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：PPP会话数据备份通道的TCP端口号，取值范围为1～65535。

【使用指导】

PPP会话在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为TCP连接。

用户可以通过本命令指定TCP连接的端口号，如果不指定则用缺省端口号发起连接。

需要注意的是：

·指定的端口号不能与系统中已经使用的端口号冲突。

·主用设备和备用设备上配置的对应端口号必须一致，否则TCP连接将建立失败，数据备份通道不通

【举例】

\# 指定PPP会话数据备份通道的TCP端口号为20000。

\<Sysname\> system-view

Sysname ppp vsrp-port 20000

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- pppoe-server vsrp-instance**

------------------------------------------------------------------------

**[pppoe-server vsrp-instance**]命令用来配置接口下PPPoE Server绑定指定的多机备份实例。

**[undo pppoe-server vsrp-instance**]命令用来取消接口下PPPoE Server绑定的多机备份实例。

【命令】

**[pppoe-server vsrp-instance ***vsrp-instance-name*]

**[undo pppoe-server vsrp-instance**]

【缺省情况】

接口下PPPoE Server未绑定多机备份实例。

【视图】

三层以太网接口视图/三层以太网子接口视图/三层聚合接口视图/三层聚合子接口视图/EFM接口视图/EFM子接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在接口下配置本命令后，就可以通过多机备份模块提供的数据备份通道实时备份接口上接入的PPPoE会话信息和PPP会话信息。

需要注意的是：

·配置本命令时，多机备份实例可以不存在，但只有配置了多机备份实例后本命令才生效。

·一个接口只能绑定一个多机备份实例，同一接口下的多个子接口可以绑定同一个多机备份实例。

·不同接口不能绑定同一个多机备份实例。如果要绑定的多机备份实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。

·在接口下配置本命令，会清除接口下所有已经上线的用户。

【举例】

\# 配置GigabitEthernet1/0/1接口下PPPoE Server绑定名为vsrp1的多机备份实例。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 pppoe-server vsrp-instance vsrp1

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- pppoe-server vsrp-port**

------------------------------------------------------------------------

**[pppoe-server vsrp-port**]命令用来配置PPPoE会话数据备份通道的TCP端口号。

**[undo pppoe-server vsrp-port**]命令用来恢复缺省情况。

【命令】

**[pppoe-server vsrp-port ***port-number*]

**[undo pppoe-server vsrp-port**]

【缺省情况】

PPPoE会话数据备份通道的TCP端口号为60034。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：PPPoE会话数据备份通道的TCP端口号，取值范围为1～65535。

【使用指导】

PPPoE会话在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为TCP连接。

用户可以通过本命令指定TCP连接的端口号，如果不指定则用缺省端口号发起连接。

需要注意的是：

·指定的端口号不能与系统中已经使用的端口号冲突。

·主用设备和备用设备上配置的对应端口号必须一致，否则TCP连接将建立失败，数据备份通道不通。

【举例】

\# 指定PPPoE会话数据备份通道的TCP端口号为30000。

\<Sysname\> system-view

Sysname pppoe-server vsrp-port 30000

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp session vsrp**

------------------------------------------------------------------------

**[display l2tp session vsrp**]命令用来显示多机备份实例下的L2TP会话信息。

【命令】

**[display l2tp session vsrp** [ *vsrp-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有多机备份实例下的L2TP会话信息。

【举例】

\# 显示多机备份实例abc下的L2TP会话信息。

\<Sysname\> display l2tp session vsrp abc

VSRP instance name: abc

Local session ID: 1

Remote session ID: 1

Local tunnel ID: 1

State: Established

User ID: 00e0fc112233000300000004

Interface: Virtual-Access0

表1-5 display l2tp session vsrp命令显示信息描述表

字段

描述

VSRP instance name

会话所属的多机备份实例的名称

Local session ID

本端的会话ID

Remote session ID

远端的会话ID

Local tunnel ID

本端的隧道ID

State

会话的状态，取值包括：

·Idle：空闲状态

·Wait-tunnel：等待建立隧道

·Wait-reply：等待ICRP报文

·Established：会话成功建立

User ID

用户ID

Interface

LAC侧PPP链路的VA接口

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp tunnel vsrp**

------------------------------------------------------------------------

**[display l2tp tunnel vsrp**]命令用来显示多机备份实例下的L2TP隧道信息。

【命令】

**[display l2tp tunnel vsrp** [ *vsrp-instance-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示所有多机备份实例下的L2TP隧道信息。

【举例】

\# 显示多机备份实例abc下的L2TP隧道信息。

\<Sysname\> display l2tp tunnel vsrp abc

VSRP instance name: abc

Local tunnel ID: 1

Remote tunnel ID: 1

State: Established

Sessions: 1

Remote address: 20.1.1.2

Remote port: 1701

Remote name: lns

Local address: 2.2.2.2

Sequence number sent (Ns): 2

Sequence number expected (Nr): 3

表1-6 display l2tp tunnel vsrp命令显示信息描述表

字段

描述

VSRP instance name

隧道所属的多机备份实例的名称

Local tunnel ID

本端的隧道ID

Remote tunnel ID

远端的隧道ID

State

隧道的状态，取值包括：

·Idle：空闲状态

·Wait-reply：等待SCCRP报文

·Established：隧道成功建立

·Stopping：正在断开隧道

Sessions

隧道上的会话数目

Remote address

对端的IP地址

Remote port

对端L2TP使用的UDP端口号

Remote name

隧道对端的名称

Local address

本端的IP地址

Sequence number sent (Ns)

发送报文的序号

Sequence number expected (Nr)

期望接收到的下一个控制报文中Ns字段的值

【相关命令】

·**reset l2tp tunnel**（二层技术-广域网接入/L2TP）

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp vsrp**

------------------------------------------------------------------------

**[display l2tp vsrp**]命令用来显示应用于L2TP的多机备份实例的运行信息。

【命令】

**[display l2tp vsrp ** *vsrp-instance-name* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，则显示应用于L2TP的所有多机备份实例的运行信息。

【举例】

\# 显示应用于L2TP的多机备份实例abc的运行信息。

\<Sysname\> display l2tp vsrp abc

VSRP instance name: abc

VSRP mode: Hot

VSRP status: Switched

Local VSRP state: Master/Up

Remote VSRP state: Backup

VSRP channel state: Synced

Sent messages: 13005

Received messages: 23

Discarded sent messages: 22

Discarded received messages: 13

Sent tunnel add messages: 8000

Received tunnel add messages: 0

Sent tunnel delete messages: 5500

Received tunnel delete messages: 0

Sent session add messages: 20000

Received session add messages: 0

Sent session delete messages: 10000

Received session delete messages: 0

Current tunnels: 2500

Current sessions: 10000

Added tunnels: 8000

Deleted tunnels: 5500

Added sessions: 20000

Deleted sessions: 10000

表1-7 display l2tp vsrp命令显示信息描述表

字段

描述

VSRP instance name

多机备份实例的名称

VSRP mode

备份模式，取值包括：

·Hot：热备份

·Warm：温备份

VSRP status

多机备份组的主备切换状态，取值包括：

·Switching：正在进行主备切换

·Switched：主备切换完成

Local VSRP state

本端多机备份组状态，取值包括：

·Master/Up：本端作为主设备/多机备份组可用

·Backup/Up：本端作为备设备/多机备份组可用

·Master/Down：本端作为主设备/多机备份组不可用

·Backup/Down：本端作为备设备/多机备份组不可用

Remote VSRP state

对端多机备份组状态，取值包括：

·Master：对端作为主设备

·Backup：对端作为备设备

VSRP channel state

数据备份通道状态，取值包括：

·Disconnected：断开

·Snycing：正在数据同步

·Synced：数据同步完成

Sent messages

本设备发送的备份消息数

Received messages

本设备接收的备份消息数

Discarded sent messages

本设备在发送方向丢弃的消息数

Discarded received messages

本设备在接收方向丢弃的消息数

Sent tunnel add messages

本设备发送的新建隧道消息数

Received tunnel add messages

本设备接收的新建隧道消息数

Sent tunnel delete messages

本设备发送的删除隧道消息数

Received tunnel delete messages

本设备接收的删除隧道消息数

Sent session add messages

本设备发送的新建会话消息数

Received session add messages

本设备接收的新建会话消息数

Sent session delete messages

本设备发送的删除会话消息数

Received session delete messages

本设备接收的删除会话消息数

Current tunnels

多机备份实例下的L2TP隧道数

Current sessions

多机备份实例下的L2TP会话数

Added tunnels

多机备份实例下新建L2TP隧道的次数

Deleted tunnels

多机备份实例下删除L2TP隧道的次数

Added sessions

多机备份实例下新建L2TP会话的次数

Deleted sessions

多机备份实例下删除L2TP会话的次数

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- l2tp tunnel-id**

------------------------------------------------------------------------

**[l2tp tunnel-id**]命令用来配置L2TP隧道ID的分配范围。

**[undo l2tp tunnel-id**]命令用来恢复缺省情况。

【命令】

**[l2tp tunnel-id** *low high*]

**[undo l2tp tunnel-id**]

【缺省情况】

L2TP隧道ID的分配范围为1～65535。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[low*]：L2TP隧道ID分配范围的下边界值，取值为1～65535。

*[high*]：L2TP隧道ID分配范围的上边界值，取值为1～65535，并且上边界值不能小于下边界值。

【使用指导】

L2TP多机备份组网中的两台LAC设备可以利用不同的多机备份实例来实现负载分担，比如：在多机备份实例1中LAC1为主用设备，LAC2为备用设备；而在多机备份实例2中LAC2为主用设备，LAC1为备用设备。这种情况下，要求不同多机备份实例中的主用LAC设备建立的L2TP隧道的ID不能冲突，因此需要为两台LAC设备配置不同的L2TP隧道ID分配范围。

需要注意的是，当LAC设备上存在L2TP隧道时，不能修改L2TP隧道ID分配范围。

【举例】

\# 配置L2TP隧道ID的分配范围为20～100。

\<Sysname\> system-view

Sysname l2tp tunnel-id 20 100

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- l2tp vsrp-port**

------------------------------------------------------------------------

**[l2tp vsrp-port**]命令用来配置L2TP数据备份通道的TCP端口号。

**[undo l2tp vsrp-port**]命令用来恢复缺省情况。

【命令】

**[l2tp vsrp-port** *port-number*]

**[undo l2tp vsrp-port**]

【缺省情况】

L2TP数据备份通道的TCP端口号为60036。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：L2TP数据备份通道的TCP端口号，取值范围为1～65535。

【使用指导】

在进行L2TP数据备份之前，主用和备用LAC设备之间需要先建立一条L2TP数据备份通道，此通道为TCP连接。通过此命令可以调整TCP连接使用的端口号。

需要注意的是：

·主用和备用LAC设备必须配置相同的TCP端口号，才能正确建立L2TP数据备份通道。

·指定的L2TP数据备份通道的TCP端口号不能与系统中已经使用的端口号冲突。

【举例】

\# 配置L2TP数据备份通道的TCP端口号为20000。

\<Sysname\> system-view

Sysname l2tp vsrp-port 20000

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- tunnel vsrp source-ip**

------------------------------------------------------------------------

**[tunnel vsrp source-ip**]命令用来设置多机备份情况下L2TP隧道的源端地址，即封装后L2TP隧道报文的源地址。

**[undo tunnel vsrp source-ip**]命令用来恢复缺省情况。

【命令】

**[tunnel vsrp source-ip** *ip-address*]

**[undo tunnel vsrp source-ip**]

【缺省情况】

L2TP隧道的源端地址为本端L2TP隧道出接口的IP地址。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：多机备份情况下L2TP隧道的源端IP地址。

【使用指导】

主用和备用LAC设备必须使用本命令配置相同的L2TP隧道源端IP地址。配置了本命令后，主用LAC设备上会生成到源端地址的静态路由，路由的出接口为Loopback接口。当主用LAC设备故障，发生主备倒换后，原主用LAC设备将删除该静态路由，并利用动态路由协议发布路由删除消息。新的主用LAC设备（即原备用LAC设备）会生成到源端地址的静态路由，并利用动态路由协议发布路由添加消息。这样，LNS到远端的下行流量会自动切换到新的主用LAC设备上，LNS会认为原来的L2TP隧道仍然保持建立。

需要注意的是：

·L2TP隧道的源端地址可以不是本设备上接口的地址，若是设备接口的地址必须保证是32位掩码的Loopback接口地址，只要保证源端地址不与网络中的IP地址冲突即可。

·建议为不同的L2TP组配置不同的L2TP隧道源端IP地址。

·必须先配置L2TP组关联的多机备份实例，才能为该L2TP组配置L2TP隧道的源端IP地址。

·当L2TP组下存在L2TP隧道时，不能修改或删除为该L2TP组配置的L2TP隧道源端IP地址。

·在L2TP多机备份的情况下，如果L2TP组视图下同时配置了**tunnel vsrp source-ip**和**source-ip**命令，将使用**tunnel vsrp source-ip**命令指定的地址作为L2TP隧道的源端地址；如果L2TP组视图下配置了**source-ip**命令，没有配置**tunnel vsrp source-ip**命令，将会导致L2TP多机备份故障。

【举例】

\# 设置多机备份情况下L2TP隧道的源端地址为2.2.2.2。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 tunnel vsrp source-ip 2.2.2.2

【相关命令】

l**source-ip**（二层技术-广域网接入命令参考/L2TP）

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- vsrp-instance（L2TP组视图）**

------------------------------------------------------------------------

**[vsrp-instance**]命令用来设置L2TP组关联的多机备份实例。

**[undo vsrp-instance**]命令用来恢复缺省情况。

【命令】

**[vsrp-instance ***vsrp-instance-name*]

**[undo vsrp-instance**]

【缺省情况】

L2TP组没有关联任何多机备份实例。

【视图】

L2TP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

为了实现L2TP业务多机备份功能，需要将L2TP组与多机备份实例进行关联。关联生效之后，主用LAC设备将向备用LAC设备实时备份此L2TP组的业务信息。某些情况下（如设备重启），备用LAC设备也会向主用LAC设备请求L2TP组的业务信息。

需要注意的是：

·一对主用和备用LAC设备上的对应L2TP组必须关联相同的多机备份实例。

·配置L2TP组关联的多机备份实例时，该L2TP组下所有已建立的L2TP隧道将会被清除。

·当L2TP组下存在L2TP隧道时，不能修改或取消该L2TP组关联的多机备份实例。

【举例】

\# 配置L2TP组1与多机备份实例abc关联。

\<Sysname\> system-view

Sysname l2tp-group 1 mode lac

Sysname-l2tp1 vsrp-instance abc

**多机备份配置命令 \-- Portal支持多机备份功能配置命令 \-- portal vsrp-instance**

------------------------------------------------------------------------

**[portal vsrp-instance**]命令用来配置接口上的Portal功能绑定的多机备份实例。

**[undo** **portal vsrp-instance**]命令用来恢复缺省情况。

【命令】

**[portal** **vsrp-instance** *vsrp-instance-name*]

**[undo** **portal** **vsrp-instance** ]

【缺省情况】

接口上的Portal功能未绑定多机备份实例。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：表示多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

接口上引用多机备份实例后，接口上的Portal多机备份功能对于该接口上的IPv4 Portal和IPv6 Portal用户都生效。Portal多机备份功能是指当主设备故障或链路故障时，主设备通过指定的多机备份实例将其上的Portal业务信息备份到备设备上，从而保证主设备故障时，主设备上的Portal业务可以自动切换到备用设备上，已上线的Portal用户不需要重新认证，计费、授权信息不丢失。

需要注意的是：

·同一设备上的不同主接口上引用的多机备份实例不能相同。

·同一接口下的不同子接口可以引用相同的VSRP实例，也可以引用不同的多机备份实例。

·当接口上有在线Portal用户时，配置、修改、取消接口上引用的VSRP实例，都会导致接口上的Portal用户下线。

·多机备份运行环境下，如果备用设备的接口上取消引用多机备份实例，则该接口上的Portal用户信息会被删除；如果主设备的接口上取消引用多机备份实例，则该接口上的Portal用户不会下线。

【举例】

\# 在接口GigabitEthernet1/0/1上使能Portal多机备份功能，并引用VSRP实例aaa。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 portal vsrp-instance aaa

【相关命令】

·**display portal interface**

·**portal vsrp-port**

**多机备份配置命令 \-- Portal支持多机备份功能配置命令 \-- portal vsrp-port**

------------------------------------------------------------------------

**[portal vsrp-port**]命令用来配置Portal建立数据备份通道使用的TCP端口号。

**[undo portal vsrp-port**]命令用来恢复缺省情况。

【命令】

**[portal vsrp-port ***port-number*]

**[undo portal vsrp-port**]

【缺省情况】

Portal建立数据备份通道使用的TCP端口号为60038。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：TCP端口号，取值范围为1～65535。

【使用指导】

多机备份组网环境中，本端设备在进行Portal数据备份之前，需要与对端备份设备建立一条多机备份数据备份通道，此通道为TCP连接。两端成功建立了TCP连接后，Portal业务的数据信息将通过该通道进行实时备份。

需要注意的是，本命令中指定的TCP端口号不能与系统中已经使用的TCP端口号冲突。

【举例】

\# 配置Portal建立数据备份通道使用的TCP端口号20000。

\<Sysname\> system-view

Sysname portal vsrp-port 20000

【相关命令】

·**portal vsrp-instance**

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- dhcp vsrp-instance**

------------------------------------------------------------------------

**[dhcp vsrp-instance**]命令用来配置接口绑定指定多机备份实例。

**[undo dhcp vsrp-instance**]命令用来取消接口绑定多机备份实例。

【命令】

**[dhcp vsrp-instance ***vsrp-instance-name*]

**[undo dhcp vsrp-instance**]

【缺省情况】

接口下未绑定多机备份实例。**

【视图】

三层以太网接口/三层以太网子接口/三层聚合口/三层聚合子接口/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

配置本命令时，多机备份实例名称可以不存在，但只有配置了多机备份实例后，本命令才生效。

该配置用于匹配主用设备和备用设备用户所在接口。一个接口只能绑定一个多机备份实例，同一接口下的多个子接口可以绑定同一个多机备份实例。不同接口不能绑定同一个多机备份实例。如果要绑定的实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。

【举例】

\# 配置接口GigabitEthernet 1/0/1绑定多机备份实例1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 dhcp vsrp-instance vsrp1

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- dhcp vsrp port**

------------------------------------------------------------------------

**[dhcp vsrp port**]命令用来配置DHCP服务器数据备份通道的TCP端口号。

**[undo dhcp vsrp port**]命令用来恢复缺省情况。

【命令】

**[dhcp vsrp port ***port-number*]

**[undo dhcp vsrp port**]

【缺省情况】

默认端口号为60037。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：DHCP服务器数据备份通道TCP的端口号，取值范围为1～65535。

【使用指导】

DHCP服务器在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为TCP连接。用户可以通过命令指定TCP连接的端口号，如果不指定则用默认端口号发起连接。

使用本命令指定的端口号不能与系统中已经使用的端口号冲突。

【举例】

\# 指定DHCP服务器的数据备份通道端口号为30000。

\<Sysname\> system-view

Sysname dhcp vsrp port 30000

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- ipv6 dhcp vsrp-instance**

------------------------------------------------------------------------

**[ipv6 dhcp vsrp-instance**]命令用来配置接口绑定指定IPv6多机备份实例。

**[undo ipv6 dhcp vsrp-instance**]命令用来取消接口绑定IPv6多机备份实例。

【命令】

**[ipv6 dhcp vsrp-instance ***vsrp-instance-name*]

**[undo ipv6 dhcp vsrp-instance**]

【缺省情况】

接口下未绑定IPv6多机备份实例。**

【视图】

三层以太网接口/三层以太网子接口/三层聚合口/三层聚合子接口/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：IPv6多机备份实例名称，为1～31个字符的字符串，不包含空格，区分大小写。

【使用指导】

配置本命令时，IPv6多机备份实例名称可以不存在。

该配置用于匹配主备设备中用户所在接口。一个接口只能绑定一个IPv6多机备份实例，同一接口下的多个子接口可以绑定同一个IPv6多机备份实例。不同接口不能绑定同一个IPv6多机备份实例。如果要绑定的实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。

【举例】

\# 配置接口GigabitEthernet 1/0/1接口绑定IPv6多机备份实例1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ipv6 dhcp vsrp-instance vsrp1

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- ipv6 dhcp vsrp port**

------------------------------------------------------------------------

**[ipv6 dhcp vsrp port**]命令用来配置DHCPv6服务器数据备份通道的TCP端口号。

**[undo ipv6 dhcp vsrp port**]命令用来恢复缺省情况。

【命令】

**[ipv6 dhcp vsrp port **]*port-number*

**[undo ipv6 dhcp vsrp port**]

【缺省情况】

默认端口号为60039。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：DHCPv6服务器数据备份通道TCP的端口号，取值范围为1～65535。

【使用指导】

DHCPv6服务器在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为TCP连接。用户可以通过命令指定TCP连接的端口号，如果不指定则用默认端口号发起连接。

使用本命令指定的端口号不能与系统中已经使用的端口号冲突。

【举例】

\# 指定DHCPv6服务器的数据备份通道端口号为30000。

\<Sysname\> system-view

Sysname ipv6 dhcp vsrp port 30000

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- vsrp-instance(DHCPv4/DHCPv6地址池视图)**

------------------------------------------------------------------------

**[vsrp-instance**]命令用来配置DHCPv4/DHCPv6服务器地址池绑定指定多机备份实例。

**[undo vsrp-instance**]命令用来取消DHCPv4/DHCPv6服务器地址池绑定的多机备份实例。

【命令】

**[vsrp-instance ***vsrp-instance-name*]

**[undo vsrp-instance**]

【缺省情况】

DHCPv4/DHCPv6服务器地址池未绑定多机备份实例。

【视图】

DHCPv4/DHCPv6地址池视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vsrp-instance-name*]：多机备份实例名称，为1～31个字符的字符串，区分大小写。

【使用指导】

在地址池下配置本命令后，就可以通过多机备份模块提供的数据备份通道实时备份DHCP服务器地址池的表项信息。配置本命令时多机备份实例可以不存在，但只有配置了多机备份实例后本命令才生效。

【举例】

\# 配置DHCPv4服务器地址池绑定多机备份实例vsrp1。

\<Sysname\> system-view

Sysname dhcp server ip-pool p1

Sysname-dhcp-pool-p1 vsrp-instance vsrp1

\#配置DHCPv6服务器地址池绑定多机备份实例vsrp1。

\<Sysname\> system-view

Sysname ipv6 dhcp pool p1

Sysname-dhcp6-pool-p1 vsrp-instance vsrp1

