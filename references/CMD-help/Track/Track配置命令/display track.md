
**Track \-- Track配置命令 \-- display track**

------------------------------------------------------------------------

**[display track**]命令用来显示Track项信息。

【命令】

**[display track**  ****[\| ]**all **}

【视图】]

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[track-entry-number*]：显示指定Track项的信息。*track-entry-number*为Track项的序号，取值范围为1～1024。

**[all**]：显示所有Track项的信息。

【举例】

·路由应用

\# 显示所有Track项的信息。

\<Sysname\> display track all

Track ID: 1

  State: Positive

  Duration: 0 days 0 hours 0 minutes 7 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object：

    NQA entry: admin test

    Reaction: 10

Track ID: 2

  State: NotReady

  Duration: 0 days 0 hours 0 minutes 32 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object:

    BFD session mode: Echo

    Outgoing interface: GigabitEthernet1/0/1

    VPN instance name: -

    Remote IP: 192.168.40.1

    Local IP: 192.168.40.2

Track ID: 3

  State: Negative

  Duration: 0 days 0 hours 0 minutes 32 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object:

    Interface: GigabitEthernet1/0/2

    Protocol: IPv4

·交换应用

\# 显示所有Track项的信息。

\<Sysname\> display track all

Track ID: 1

  State: Positive

  Duration: 0 days 0 hours 0 minutes 7 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object：

    NQA entry: admin test

    Reaction: 10

Track ID: 2

  State: NotReady

  Duration: 0 days 0 hours 0 minutes 32 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object:

    BFD session mode: Echo

    Outgoing interface: Vlan-interface2

    VPN instance name: -

    Remote IP: 192.168.40.1

    Local IP: 192.168.40.2

Track ID: 3

  State: Negative

  Duration: 0 days 0 hours 0 minutes 32 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object:

    Interface:  Vlan-interface3

    Protocol: IPv4

Track ID: 4

  State: Negative

  Duration: 0 days 0 hours 0 minutes 32 seconds

  Notification delay: Positive 20, Negative 30 (in seconds)

  Tracked object:

    CFD service instance: 1, MEP ID: 2

表1-1 display track命令输出信息描述

字段

描述

Track ID

Track项序号

State

Track项的状态，取值包括：

·Positive：表示状态正常

·NotReady：表示无效值

·Negative：表示状态异常

Duration

Track项处于当前状态的持续时间

Notification delay: Positive 20, Negative 30 (in seconds)

通知延迟：

·Track项状态变为Positive后，延迟20秒通知应用模块

·Track项状态变为Negative后，延迟30秒通知应用模块

Tracked object

Track项关联的对象

NQA entry

Track项关联的NQA测试组

Reaction

Track项关联的联动项

BFD session mode

BFD会话的模式，当前只支持Echo模式

Outgoing interface

BFD会话报文的出接口

VPN instance name

BFD会话报文所属VPN实例的名称。如果属于公网，则显示为"-"

Remote IP

BFD会话报文的远端IP地址

Local IP

BFD会话报文的本地IP地址

Interface

Track项关联的接口

Protocol

监视接口的链路状态或网络层协议状态，取值包括：

·None：监视接口的链路状态

·IPv4：监视三层接口的IPv4协议状态

·IPv6：监视三层接口的IPv6协议状态

CFD service instance

CFD服务实例的编号

MEP ID

CFD MEP的编号

【相关命令】

·**track bfd**

·**track cfd**

·**track interface**

·**track interface protocol**

·**track nqa**

**Track \-- Track配置命令 \-- track bfd**

------------------------------------------------------------------------

![说明](Track命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[track bfd**]命令用来创建和BFD会话关联的Track项。

**[undo track**]命令用来删除指定的Track项。

【命令】

**[track ***track-entry-number ***bfd echo interface ***interface-type interface-number*** remote ip ***remote-ip ***local ip ***local-ip *[[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* ]]]

**[undo track ***track-entry-number*]

【缺省情况】

设备上不存在任何Track项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

**[interface** *interface-type interface-number*]：BFD会话报文的出接口。*interface-type interface-number*为接口类型和接口编号。

**[remote ip*** remote-ip*]：BFD会话探测的远端IP地址。

**[local ip*** local-ip*]：BFD会话探测的本地IP地址。

**[delay**]：指定Track项状态发生变化时，延迟通知应用模块。如果不指定该参数，则Track项状态变化后立即通知应用模块。

**[negative** *negative-time*]：指定Track项状态变为Negative时，延迟通知应用模块的时间。*negative-time*为延迟时间，取值范围为1～300，单位为秒。

**[positive** *positive-time*]：指定Track项状态变为Positive时，延迟通知应用模块的时间。*positive-time*为延迟时间，取值范围为1～300，单位为秒。

【使用指导】

·Track项创建后，不能通过重复执行**track**命令的方式修改Track项关联的内容。只能删除Track项后，再重新创建Track项。

·Track项创建后，可以通过再次执行**track bfd delay**命令的方式修改延迟通知应用模块的时间。

·配置Track与BFD联动时，VRRP备份组的虚拟IP地址不能作为BFD会话探测的本地地址和远端地址。

【举例】

·路由应用

\# 创建与BFD会话关联的Track项1。BFD会话使用Echo报文进行探测，出接口为GigabitEthernet1/0/1，远端IP地址为192.168.40.1，本地IP地址为192.168.40.2。

\<Sysname\> system-view

Sysname track 1 bfd echo interface gigabitethernet 1/0/1 remote ip 192.168.40.1 local ip 192.168.40.2

·交换应用

\# 创建与BFD会话关联的Track项1。BFD会话使用Echo报文进行探测，出接口为VLAN接口 2，远端IP地址为1.1.1.1，本地IP地址为1.1.1.2。

\<Sysname\> system-view

Sysname track 1 bfd echo interface vlan-interface 2 remote ip 1.1.1.1 local ip 1.1.1.2

【相关命令】

·**display track**

**Track \-- Track配置命令 \-- track cfd**

------------------------------------------------------------------------

![说明](Track命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[track cfd**]命令用来创建和CFD连续性检测功能关联的Track项。

**[undo track**]命令用来删除指定的Track项。

【命令】

**[track ***track-entry-number*** cfd cc service-instance ***instance-id ***mep ***mep-id *[[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* ]]]

**[undo track ***track-entry-number*]

【缺省情况】

设备上不存在任何Track项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

**[service-instance ***instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep ***mep-id*]：表示MEP的编号，*mep-id*的取值范围为1～8191。

**[delay**]：指定Track项状态发生变化时，延迟通知应用模块。如果不指定该参数，则Track项状态变化后立即通知应用模块。

**[negative** *negative-time*]：指定Track项状态变为Negative时，延迟通知应用模块的时间。*negative-time*为延迟时间，取值范围为1～300，单位为秒。

**[positive** *positive-time*]：指定Track项状态变为Positive时，延迟通知应用模块的时间。*positive-time*为延迟时间，取值范围为1～300，单位为秒。

【使用指导】

·Track项创建后，不能通过重复执行**track**命令的方式修改Track项关联的内容。只能删除Track项后，再重新创建Track项。

·Track项创建后，可以通过再次执行**track cfd delay**命令的方式修改延迟通知应用模块的时间。

【举例】

\# 创建与CFD连续性检测功能关联的Track项1。指定CFD服务实例2，MEP编号为3。

\<Sysname\> system-view

Sysname track 1 cfd cc service-instance 2 mep 3

【相关命令】

·**display track**

·**cfd mep**（可靠性命令参考/CFD）

·**cfd service-instance**（可靠性命令参考/CFD）

**Track \-- Track配置命令 \-- track interface**

------------------------------------------------------------------------

**[track interface**]命令用来创建与指定接口链路状态关联的Track项。

**[undo track**]命令用来删除指定的Track项。

【命令】

**[track ***track-entry-number ***interface ***interface-type interface-number *[[ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* ]]]

**[undo track ***track-entry-number*]

【缺省情况】

设备上不存在任何Track项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

*[interface-type interface-number*]：监视的接口类型和接口编号。

**[delay**]：指定Track项状态发生变化时，延迟通知应用模块。如果不指定该参数，则Track项状态变化后立即通知应用模块。

**[negative** *negative-time*]：指定Track项状态变为Negative时，延迟通知应用模块的时间。*negative-time*为延迟时间，取值范围为1～300，单位为秒。

**[positive** *positive-time*]：指定Track项状态变为Positive时，延迟通知应用模块的时间。*positive-time*为延迟时间，取值范围为1～300，单位为秒。

【使用指导】

创建与接口链路状态关联的Track项后，接口的链路状态为up时，Track项的状态为Positive；接口的链路状态为down时，Track项的状态为Negative。通过**display ip interface brief**命令可以查看接口的链路状态。

需要注意的是：

·Track项创建后，不能通过重复执行**track**命令的方式修改Track项关联的内容。只能删除Track项后，再重新创建Track项。

·Track项创建后，可以通过再次执行**track interface delay**命令的方式修改延迟通知应用模块的时间。

【举例】

·路由应用

\# 创建与接口GigabitEthernet1/0/1的链路状态关联的Track项1。

\<Sysname\> system-view

Sysname track 1 interface gigabitethernet 1/0/1

·交换应用

\# 创建与VLAN接口10的链路状态关联的Track项1。

\<Sysname\> system-view

Sysname track 1 interface vlan-interface 10

【相关命令】

·**display track**

·**display ip interface brief**（三层技术-IP业务命令参考/IP地址）

**Track \-- Track配置命令 \-- track interface protocol**

------------------------------------------------------------------------

**[track interface protocol**]命令用来创建与指定接口网络层协议状态关联的Track项。

**[undo track**]命令用来删除指定的Track项。

【命令】

**[track ***track-entry-number ***interface ***interface-type interface-number*** protocol **[{ **ipv4** \| **ipv6** } [ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* ]]]

**[undo track ***track-entry-number*]

【缺省情况】

设备上不存在任何Track项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

*[interface-type interface-number*]：监视的接口类型和接口编号。

**[ipv4**]：监视接口的IPv4协议状态。接口的IPv4协议状态为up时，Track项的状态为Positive；接口的IPv4协议状态为down时，Track项的状态为Negative。通过**display ip interface brief**命令可以查看接口的IPv4协议状态。

**[ipv6**]：监视接口的IPv6协议状态。接口的IPv6协议状态为up时，Track项的状态为Positive；接口的IPv6协议状态为down时，Track项的状态为Negative。通过**display ipv6 interface brief**命令可以查看接口的IPv6协议状态。

**[delay**]：指定Track项状态发生变化时，延迟通知应用模块。如果不指定该参数，则Track项状态变化后立即通知应用模块。

**[negative** *negative-time*]：指定Track项状态变为Negative时，延迟通知应用模块的时间。*negative-time*为延迟时间，取值范围为1～300，单位为秒。

**[positive** *positive-time*]：指定Track项状态变为Positive时，延迟通知应用模块的时间。*positive-time*为延迟时间，取值范围为1～300，单位为秒。

【使用指导】

·Track项创建后，不能通过重复执行**track**命令的方式修改Track项关联的内容。只能删除Track项后，再重新创建Track项。

·Track项创建后，可以通过再次执行**track interface protocol delay**命令的方式修改延迟通知应用模块的时间。

【举例】

·路由应用

\# 创建与接口GigabitEthernet1/0/1的IPv4协议状态关联的Track项1。

\<Sysname\> system-view

Sysname track 1 interface gigabitethernet 1/0/1 protocol ipv4

·交换应用

\# 创建与VLAN接口2的IPv4协议状态关联的Track项1。

\<Sysname\> system-view

Sysname track 1 interface vlan-interface 2 protocol ipv4

【相关命令】

·**display ip interface brief**（三层技术-IP业务命令参考/IP地址）

·**display ipv6 interface brief**（三层技术-IP业务命令参考/IPv6基础）

·**display track**

**Track \-- Track配置命令 \-- track nqa**

------------------------------------------------------------------------

![说明](Track命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[track nqa**]命令用来创建与NQA测试组中指定联动项关联的Track项。

**[undo track**]命令用来删除指定的Track项。

【命令】

**[track ***track-entry-number ***nqa entry ***admin-name*[ *operation-tag* **reaction** *item-number* [ **delay** { **negative** *negative-time* \| **positive** *positive-time* } \* ]]]

**[undo track ***track-entry-number*]

【缺省情况】

设备上不存在任何Track项。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[track-entry-number*]：Track项的序号，取值范围为1～1024。

**[entry ***admin-name operation-tag*]：指定与Track项关联的NQA测试组。其中，*admin-name*为创建NQA测试组的管理员的名字，为1～32个字符的字符串，不区分大小写；*operation-tag*为NQA测试操作的标签，为1～32个字符的字符串，不区分大小写。

**[reaction ***item-number*]：指定与Track项关联的联动项。其中，*item-number*为联动项的序号，取值范围为1～10。

**[delay**]：指定Track项状态发生变化时，延迟通知应用模块。如果不指定该参数，则Track项状态变化后立即通知应用模块。

**[negative** *negative-time*]：指定Track项状态变为Negative时，延迟通知应用模块的时间。*negative-time*为延迟时间，取值范围为1～300，单位为秒。

**[positive** *positive-time*]：指定Track项状态变为Positive时，延迟通知应用模块的时间。*positive-time*为延迟时间，取值范围为1～300，单位为秒。

【使用指导】

·Track项创建后，不能通过重复执行**track**命令的方式修改Track项关联的内容。只能删除Track项后，再重新创建Track项。

·Track项创建后，可以通过再次执行**track nqa delay**命令的方式修改延迟通知应用模块的时间。

【举例】

\# 创建与NQA测试组（admin--test）中联动项3关联的Track项1。

\<Sysname\> system-view

Sysname track 1 nqa entry admin test reaction 3

【相关命令】

·**display track**
