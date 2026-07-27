<!-- CMD-INDEX
  display sflow                       | 任意视图             | L14
  sflow agent                         | 系统视图             | L170
  sflow collector                     | 系统视图             | L218
  sflow counter interval              | 二层以太网接口视图/三层以太网接口视图 | L272
  sflow counter collector             | 二层以太网接口视图/三层以太网接口视图 | L314
  sflow flow collector                | 二层以太网接口视图/三层以太网接口视图 | L356
  sflow flow max-header               | 二层以太网接口视图/三层以太网接口视图 | L398
  sflow sampling-mode                 | 二层以太网接口视图/三层以太网接口视图 | L444
  sflow sampling-rate                 | 二层以太网接口视图/三层以太网接口视图 | L492
  sflow source                        | 系统视图             | L538
-->

**sFlow \-- sFlow配置命令 \-- display sflow**

------------------------------------------------------------------------

**[display sflow**]命令用来显示sFlow的配置和运行信息。

【命令】

**[display sflow**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示sFlow的配置和运行信息。

\<Sysname\> display sflow

sFlow datagram version: 5

Global information:

Agent IP: 10.10.10.1(CLI)

Source address: 10.0.0.1 2001::1

Collector information:

ID    IP              Port  Aging      Size VPN-instance Description

1     22:2:20::10     6535  N/A        1400 vpn1         netserver

2     192.168.3.5     6543  500        1400              Office

Port information:

Interface      CID   Interval(s) FID   MaxHLen Rate       Mode      Status

GE1/0/1         1     100         1     128     1000       Random    Active

GE1/0/2         2     100         2     128     1000       Random    Active

表1-1 display sflow命令显示信息描述表

字段

描述

sFlow datagram version

sFlow报文版本号，取值只能为5，表示当前仅支持发送版本号为5的sFlow报文

Global information

sFlow全局信息

Agent IP

sFlow Agent的IP地址：

lCLI：表示手工配置的IP地址

lAuto：表示自动查找到的IP地址

Source address

sFlow报文的源地址

Collector information

sFlow Collector信息

ID

sFlow Collector编号

IP

接收sFlow报文的sFlow Collector的IP地址

Port

接收sFlow报文的sFlow Collector的端口号

Aging

sFlow Collector的剩余存活时间。如果显示为N/A，则表示对应的sFlow Collector不会老化

Size

每次发送sFlow报文时，sFlow数据部分的最大长度

VPN-instance

sFlow Collector的VPN实例名

Description

sFlow Collector的描述信息

Port information

已配置sFlow功能的接口信息

Interface

已配置sFlow功能的接口

CID

经过Counter采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号。如果没有指定sFlow Collector编号，显示为0

Interval(s)

Counter采样的时间间隔

FID

经过Flow采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号。如果没有指定sFlow Collector编号，显示为0

MaxHLen

从原始报文的头开始，允许拷贝的最大字节数

Rate

Flow采样的报文采样率

Mode

Flow采样的采样模式，其可能的取值如下：

lDetermine：表示固定采样

lRandom：表示随机采样

Status

接口的sFlow功能的启用状态，其可能的取值如下：

lSuspended：表示因接口处于down状态而挂起

lActive：表示因接口处于up状态而生效

**sFlow \-- sFlow配置命令 \-- sflow agent**

------------------------------------------------------------------------

**[sflow agent**]命令用来配置sFlow Agent的IP地址。

**[undo sflow agent**]命令用来恢复缺省情况。

【命令】

**[sflow agent **[{ **ip** *ip-address \|* **ipv6** *ipv6-address* }]]

**[undo sflow agent **[{ **ip** *\|* **ipv6** }]]

【缺省情况】

未配置sFlow Agent的IP地址。设备会定期检查是否存在sFlow Agent的IP地址，如果不存在，设备会自动查找一个IPv4地址作为sFlow Agent的IP地址。自动查找的IP地址信息不会保存在设备上。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：sFlow Agent的IPv4地址。

**[ipv6 ***ipv6-address*]：sFlow Agent的IPv6地址。

【使用指导】

l建议用户手工配置sFlow Agent的IP地址。

l在设备上只能配置一个sFlow Agent的IP地址，新配置的IP地址会覆盖已有的配置。

【举例】

\# 配置sFlow Agent的IP地址为10.10.10.1。

\<Sysname\> system-view

Sysname sflow agent ip 10.10.10.1

**sFlow \-- sFlow配置命令 \-- sflow collector**

------------------------------------------------------------------------

**[sflow collector**]命令用来配置sFlow Collector的参数。

**[undo sflow collector**]命令用来删除指定的sFlow Collector信息。

【命令】

**[sflow collector ***collector-id*****[ **vpn-instance** *vpn-instance-name*  { **ip** *ip-address* \| **ipv6** *ipv6-address* }  **port** *port-number*   **datagram-size** *size*   **time-out** *seconds  *  **description** *text* ]]

**[undo sflow collector ***collector-id*]

【缺省情况】

没有sFlow Collector的相关信息存在。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[collector-id*]：sFlow Collector的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。

**[vpn-instance ***vpn-instance-name*]：sFlow Collector关联的VPN实例名称，为1～31字符的字符串，不可以包含空格，区分大小写。缺省情况下，sFlow Collector不关联到任何VPN实例，位于公网。

**[ip*** ip-address*]：sFlow Collector的IPv4地址。

**[ipv6 ***ipv6-address*]：sFlow Collector的IPv6地址。

**[description*** text*]：sFlow Collector的描述信息。缺省情况下，sFlow Collector的描述信息为"CLI Collector"。

**[datagram-size ***size*]：发送sFlow报文时，sFlow数据部分的最大长度，取值范围为200～3000，单位为字节，缺省值为1400。

**[port** *port-number*]：sFlow Collector的UDP端口号，取值范围为1～65535，缺省值为6343。

**[time-out ***seconds*]：配置的sFlow Collector的参数的老化时间，当到达老化时间时，所配置的sFlow Collector的参数将被删除。取值范围为1～2147483647，单位为秒。缺省情况下，配置的sFlow Collector的参数不老化*。*

【举例】

\# 配置编号为2的Collector，关联的VPN实例名称为vpn1，目的IP为3.3.3.1，端口号保持缺省值，描述信息为"netserver"，老化时间为1200秒，sFlow数据部分的最大长度为1000字节。

\<Sysname\> system-view

Sysname sflow collector 2 vpn-instance vpn1 ip 3.3.3.1 description netserver  time-out 1200 datagram-size 1000

**sFlow \-- sFlow配置命令 \-- sflow counter interval**

------------------------------------------------------------------------

**[sflow counter interval**]命令用来配置Counter采样的时间间隔，同时开启Counter采样功能。

**[undo sflow counter interval**]命令用来恢复缺省情况。

【命令】

**[sflow counter interval*** interval-time*]

**[undo sflow counter interval**]

【缺省情况】

不进行Counter采样。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-time*]：Counter采样的时间间隔，取值范围为2～86400，单位为秒。

【举例】

\# 在GigabitEthernet1/0/1上配置Counter采样的时间间隔为120秒，同时开启Counter采样功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow counter interval 120

**sFlow \-- sFlow配置命令 \-- sflow counter collector**

------------------------------------------------------------------------

**[sflow counter collector**]命令用来配置经过Counter采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号。

**[undo sflow counter collector**]命令用来恢复缺省情况。

【命令】

**[sflow counter collector ***collector-id*]

**[undo sflow counter collector**]

【缺省情况】

Counter采样和sFlow Collector没有绑定关系，即没有指定目的sFlow Collector编号。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[collector-id*]：sFlow Collector的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在GigabitEthernet1/0/1上配置经过Counter采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号为2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow counter collector 2

**sFlow \-- sFlow配置命令 \-- sflow flow collector**

------------------------------------------------------------------------

**[sflow flow collector**]命令用来配置经过Flow采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号。

**[undo sflow flow collector**]命令用来恢复缺省情况。

【命令】

**[sflow flow collector ***collector-id*]

**[undo sflow flow collector**]

【缺省情况】

Flow采样和sFlow Collector没有绑定关系，即没有指定目的sFlow Collector编号。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[collector-id*]：sFlow Collector的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 在GigabitEthernet1/0/1上配置经过Flow采样后，sFlow Agent输出sFlow报文的目的sFlow Collector编号为2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow flow collector 2

**sFlow \-- sFlow配置命令 \-- sflow flow max-header**

------------------------------------------------------------------------

**[sflow flow max-header**]命令用来配置在进行报文内容拷贝时，从原始报文的头部开始，允许拷贝的最大字节数。拷贝的内容会记录在生成的采样样本中。

**[undo sflow flow max-header**]命令用来恢复缺省情况。

【命令】

**[sflow flow max-header ***length*]

**[undo sflow flow max-header**]

【缺省情况】

从原始报文的头部开始，允许拷贝的最大字节数为128字节。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[length*]：从原始报文的头部开始，允许拷贝的最大字节数，取值范围为18～512。

【用户指导】

建议用户使用缺省配置。

【举例】

\# 在GigabitEthernet1/0/1上配置在进行报文内容拷贝时，从原始报文的头部开始，允许拷贝的最大字节数为60字节。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow flow max-header 60

**sFlow \-- sFlow配置命令 \-- sflow sampling-mode**

------------------------------------------------------------------------

**[sflow sampling-mode**]命令用来设置Flow采样的采样模式。

**[undo** **sflow sampling-mode**]命令用来恢复缺省情况。

【命令】

**[sflow sampling-mode**[ { **determine** \| **random** }]]

**[undo sflow sampling-mode**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[determine**]：表示采样模式为固定采样，采样率由**sflow sampling-rate*** rate*命令决定。例如，在配置此模式后，设定采样率为4000，设备会随机在1～4000个报文中选取其中的一个报文进行采样，比如第10个报文，下一次设备会抽取第4010个报文进行采样，以此类推。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。

**[random**]：表示采样模式为随机采样，采样率由**sflow sampling-rate*** rate*命令决定。设备会保持平均在每*rate*个报文中抽取一个报文进行采样，可能从每*rate*个报文中随机抽取任意一个或多个报文进行采样，也可能在某段的*rate*个报文中不采样报文。例如，在配置此模式后，设定报文的采样率为4000，设备可能会在1～4000个报文中选取其中的一个报文进行采样，在4001～8000个报文中选取其中的多个报文进行采样，在8001～12000个报文中不进行任何采样，但在长期时间内的总体趋势是4000个报文中抽取一个进行采样。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。

【举例】

\# 在GigabitEthernet1/0/1上配置Flow采样的采样模式为固定采样。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow sampling-mode determine

【相关命令】

l**sflow sampling-rate**

**sFlow \-- sFlow配置命令 \-- sflow sampling-rate**

------------------------------------------------------------------------

**[sflow sampling-rate**]命令用来配置Flow采样的报文采样率，即在*rate*个报文中抽取一个报文进行采样，同时开启Flow采样功能。

**[undo sflow sampling-rate**]命令用来恢复缺省情况。

【命令】

**[sflow sampling-rate*** rate*]

**[undo sflow sampling-rate**]

【缺省情况】

不进行Flow采样

【视图】

二层以太网接口视图/三层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[rate*]：Flow采样的报文采样率，取值范围与设备的型号相关，请以设备的实际情况为准。

【举例】

\# 在GigabitEthernet1/0/1上配置Flow采样的报文采样率为4000，即在4000个报文中抽取一个报文进行采样，同时开启Flow采样功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 sflow sampling-rate 4000

【相关命令】

l**sflow sampling-mode**

**sFlow \-- sFlow配置命令 \-- sflow source**

------------------------------------------------------------------------

**[sflow source**]命令用来配置sFlow报文的源IP地址。

**[undo sflow source**]命令用来恢复缺省情况。

【命令】

**[sflow source **[{ **ip** *ip-address \|* **ipv6** *ipv6-address* } \*]]

**[undo sflow source **[{ **ip** *\|* **ipv6** } \*]]

【缺省情况】

设备使用路由决定的源IP地址作为sFlow报文的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip*** ip-address*]：sFlow报文的源IPv4地址。

**[ipv6 ***ipv6-address*]：sFlow报文的源IPv6地址。

【举例】

\# 配置sFlow报文的源IPv4地址为10.0.0.1。

\<Sysname\> system-view

Sysname sflow source ip 10.0.0.1
