
**应急Shell \-- 应急Shell配置命令 \-- copy**

------------------------------------------------------------------------

**[copy**]命令用来复制文件。

【命令】

**[copy ***fileurl-source fileurl-dest*]

【视图】

用户视图

【参数】

*[fileurl-source*]：源文件的名称。

*[fileurl-dest*]：目标文件或者文件夹的名称。如果文件夹作为*fileurl-dest*，则系统会将文件复制到指定文件夹，使用源文件名作为目标文件名。

【使用指导】

执行该命令时，如果指定的目标文件不存在，则系统会先创建该文件，再复制内容；如果指定的目标文件已存在，则系统会提示是否覆盖该文件，如果选择"Y",系统会将目标文件的内容替换成源文件的内容，如果选择"N"，则不做任何处理。

【举例】

\# 将文件test.cfg在当前文件夹下复制一份，并命名为testbackup.cfg。

\<boot\> copy flash:/test.cfg flash:/testbackup.cfg

Copy flash:/test.cfg to flash:/testbackup.cfg?[Y/N:y]

Start to copy flash:/test.cfg to flash:/testbackup.cfg\...Done.

\# 将文件test.cfg在当前文件夹下复制到已存在的文件testbackup.cfg。

\<boot\> copy flash:/test.cfg flash:/testbackup.cfg

Copy flash:/test.cfg to flash:/testbackup.cfg?[Y/N:y]

flash:/testbackup.cfg already exists. Overwrite it?[Y/N:y]

Start to copy flash:/test.cfg to flash:/testbackup.cfg\...Done.

**应急Shell \-- 应急Shell配置命令 \-- delete**

------------------------------------------------------------------------

**[delete**]命令用来彻底删除指定文件。

【命令】

**[delete ***file-url*]

【视图】

用户视图

【参数】

*[file-url*]：要彻底删除的文件的名称。

【举例】

\# 彻底删除当前目录下的文件tt.cfg。

\<boot\> delete flash:/tt.cfg

Delete flash:/tt.cfg? [Y/N:y]

Deleting the file permanently will take a long time. Please wait\...

Start to delete flash:/tt.cfg\...Done.

**应急Shell \-- 应急Shell配置命令 \-- dir**

------------------------------------------------------------------------

**[dir**]命令用来显示目录或文件信息。

【命令】

**[dir ** **/all** ]  *file-url*

【视图】

用户视图

【参数】

**[/all**]：显示当前目录下所有的文件及子文件夹信息，显示内容包括隐藏文件和文件夹。不指定该参数时，显示当前目录下所有非隐藏的文件及子文件夹信息。

*[file*-*url*]：显示指定的文件或文件夹的信息。不指定该参数时，显示当前目录下的文件及子文件夹信息。

【举例】

\# 显示系统中所有的文件及文件夹信息。

\<boot\> dir /all

Directory of flash:

     0      drw-           -  Jan 01 2012 00:06:09     01

     1      drw-           -  Sep 15 2012 04:03:14     pki

     2      drw-           -  Jan 01 2012 00:04:07     test

     3      drw-           -  Aug 26 2012 02:48:00     license

     4      drw-           -  Nov 05 2012 06:45:07     logfile

     5      -rwh          20  Oct 20 2012 09:09:52     .snmpboots

     6      drw-           -  Nov 05 2012 05:56:22     diagfile

     7      drwh           -  Aug 20 2012 09:23:48     .trash

     8      -rw-         816  Aug 20 2012 06:15:00     ifindex.dat

     9      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg

    10      -rw-       60620  Aug 31 2012 09:01:43     startup.mdb

    11      drw-           -  Sep 30 2012 04:43:24     versionInfo

    12      drw-           -  Nov 05 2012 05:56:22     seclog

    13      -rwh          18  Aug 20 2012 09:09:34     .pathfile

    14      -rw-    11238400  Aug 30 2012 11:06:53     boot-t2301001.bin

    15      -rw-           0  Aug 31 2012 05:04:40     lauth.dat

    16      -rw-        4383  Oct 20 2012 06:15:00     test.cfg

61440 KB total (11108 KB free)

\# 显示系统中所有的非隐藏文件及文件夹信息。

\<boot\> dir

Directory of flash:

     0      drw-           -  Jan 01 2012 00:06:09     01

     1      drw-           -  Sep 15 2012 04:03:14     pki

     2      drw-           -  Jan 01 2012 00:04:07     test

     3      drw-           -  Aug 26 2012 02:48:00     license

     4      drw-           -  Nov 05 2012 06:45:07     logfile

     5      drw-           -  Nov 05 2012 05:56:22     diagfile

     6      -rw-         816  Aug 20 2012 06:15:00     ifindex.dat

     7      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg

     8      -rw-       60620  Aug 31 2012 09:01:43     startup.mdb

     9      drw-           -  Sep 30 2012 04:43:24     versionInfo

    10      drw-           -  Nov 05 2012 05:56:22     seclog

    11      -rw-    11238400  Aug 30 2012 11:06:53     boot-t2301001.bin

    12      -rw-           0  Aug 31 2012 05:04:40     lauth.dat

    13      -rw-        4383  Aug 20 2012 06:15:00     test.cfg

61440 KB total (11108 KB free)

\# 显示文件config.cfg的相关信息。

\<boot\> dir flash:/config.cfg

Directory of flash:

     0      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg

61440 KB total (11108 KB free)

表1-1 dir命令显示信息描述表

字段

说明

Directory of

当前显示的目录

7      -rw-        3231  Aug 31 2012 09:01:41     startup.cfg

文件或文件夹的信息：

·7表示编号，由系统自动分配

·-rw-表示属性。第一个字符如果是d表示文件夹，如果显示为"-"，则表示它是文件；第二个字符是r，表示本文件或文件夹是可读的；第三个字符是w，表示本文件或文件夹是可写的；第四个字符如果是h，表示本文件或文件夹是隐藏的，如果显示为"-"，则表示它是可见的

·3231表示文件大小，单位为字节。如果显示为"-"，则表示它是文件夹

·Aug 31 2012 09:01:41表示最近一次修改的时间

·startup.cfg表示文件或文件夹的名称

61440 KB total (11108 KB free)

存储介质存储空间的大小，单位为千字节（存储介质中空闲存储空间的大小，单位为千字节）

**应急Shell \-- 应急Shell配置命令 \-- display copyright**

------------------------------------------------------------------------

**[display copyright**]命令用来显示版权信息。

【命令】

**[display copyright**]

【视图】

任意视图

【举例】

\# 显示版权信息。（本命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<boot\> display copyright

......略......

**应急Shell \-- 应急Shell配置命令 \-- display install package**

------------------------------------------------------------------------

**[display install package**]命令用来显示指定软件包的信息。

【命令】

**[display install package ***package*]

【视图】

任意视图

【参数】

*[package*]：表示软件包的名称，为1～63个字符的字符串，不区分大小写。该文件必须是存储介质根目录下，后缀名为.bin的文件，且文件名中必须包含存储介质的名称，形如flash:/a.bin。

【举例】

\# 显示软件包system.bin的信息。

\<boot\> display install package flash:/system.bin

  flash:/system.bin

  Package

  Vendor: H3C

  Product: xxxx

  Service name: system

  Platform version: 7.1

  Product version: Alpha 0101

  Supported board: mpu

  Component

  Component: Comware system

  Description: system package

表1-2 display install package命令显示信息描述表

字段

描述

Package

软件包的信息

Vendor

厂商

Product

产品名称

Service name

软件包所包含的服务名称

·如果显示为boot，表示该软件包为Boot包

·如果显示为system，表示该软件包为System包

·如果显示为patch，表示该软件包为补丁包

·如果显示为其它值，则表示该软件包为提供某项功能的Feature包

Platform version

平台版本号

Product version

产品版本号，通过该信息可以判断System包和Boot包版本是否一致

Supported board

软件包支持的板类型（本字段的取值情况与设备的型号有关，请以设备的实际情况为准）：

·mpu表示主控板

·lc表示业务板

·sfc表示网板

Component

组件信息，表示软件包的组成部分

Component

组件信息名称

Description

软件包的描述信息

**应急Shell \-- 应急Shell配置命令 \-- display interface m-eth0**

------------------------------------------------------------------------

**[display interface m-eth0**]命令用来显示管理以太网接口M-Eth0的信息，包括IP地址、up/down状态以及报文统计息等。

【命令】

**[display interface m-eth0**]

【视图】

任意视图

【举例】

\# 显示管理以太网接口M-Eth0的信息。

\<boot\> display interface m-eth0

m-eth0 current state: UP

Line protocol current state: UP

The Maximum Transmit Unit is 1500

Inet4 Address is 192.168.20.189/24

Inet6 Address is 1:1::1:1/64 Scope:Global

Inet6 Address is FE80::202:3FF:FE04:506/10 Scope:Link

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: c4ca-d94c-e201

IPV6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: c4ca-d94c-e201

Input:  8983 packets, 0 errors, 0 dropped, 0 overruns, 2 frame

Output: 431 packets, 0 errors, 0 dropped, 0 overruns, 0 carrier,

        0 collisions, 1000 txqueuelen

Input bytes:804168 

Output bytes:30367

表1-3 display interface m-eth0命令显示信息描述表

字段

描述

m-eth0 current state

接口的物理状态，状态可能为：

·Administratively DOWN：表示该接口已经通过shutdown命令被关闭，即管理状态为关闭

·DOWN：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路故障）

·UP：该端口的管理状态和物理状态均为开启

Line protocol current state

接口的链路层状态，其值直接取用接口的物理状态的当前值

The Maximum Transmit Unit

接口的MTU

Inet4 Address

接口的IPv4地址，给接口配置IPv4地址后才显示该信息

Inet6 Address

接口的IPv6地址，给接口配置IPv6地址后才显示该信息。Scope:Global表示该地址为全球单播地址

Inet6 Address is FE80::202:3FF:FE04:506/10 Scope:Link

接口的IPv6链路本地地址，该地址在接口物理状态变为UP时，由系统自动生成

IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address

IPv4报文发送帧格式，以及硬件地址

IPv6 Packet Frame Type，

Hardware Address

IPv6报文发送帧格式，以及硬件地址

Input: 8983 packets, 0 errors, 0 dropped, 0 overruns, 2 frame

接口接收的报文的统计信息：报文总数，错误报文数，丢弃报文数，队列溢出报文数，帧队列错误报文数

Output: 431 packets, 0 errors, 0 dropped, 0 overruns, 0 carrier,  0 collisions, 1000 txqueuelen

接口发送的报文的统计信息：报文总数，错误报文数，丢弃报文数，队列溢出报文数，载波出错报文数，冲突的报文数，每个队列允许的最大帧数

Input bytes

接口接收的报文的总字节数

Output bytes

接口发送的报文的总字节数

**应急Shell \-- 应急Shell配置命令 \-- display ip routing-table**

------------------------------------------------------------------------

**[display ip routing-table**]命令用来显示IPv4路由信息表。

【命令】

**[display ip routing-table**]

【视图】

任意视图

【举例】

\# 显示IPv4路由信息表。

\<boot\> display ip routing-table

Kernel IP routing table

Destination     Gateway         Genmask         Flags Metric Ref    Use Iface

192.168.116.0   \*               255.255.255.0   U     0      0        0 m-eth0

default         192.168.116.1   0.0.0.0         UG    0      0        0 m-eth0

表1-4 display ip routing-table命令显示信息描述表

字段

描述

Kernel IP routing table

IPv4路由表信息

Destination

目的地址（取值为default时表示缺省路由）

Gateway

网关（如果不需要使用网关，则该字段显示为"\*"）

Genmask

掩码（取值为0.0.0.0时表示缺省路由的掩码）

Flags

标志位：

·G：网关路由

·H：主机路由

·D：通过邻居发现学习到的缺省路由

·A：通过路由发布学习到的路由

·C：缓存表项，用于快速转发去往某目的地的报文

·U：可用路由

Metric

路由开销

Ref

表示路由表项被其它表项引用的次数，即和其它表项间的依赖关系

Use

表示这条表项被使用过的次数，即该路由被匹配到的次数

Iface

出接口

**应急Shell \-- 应急Shell配置命令 \-- display ipv6 routing-table**

------------------------------------------------------------------------

**[display ipv6 routing-table**]命令用来显示IPv6路由信息表。

【命令】

**[display ipv6 routing-table**]

【视图】

任意视图

【举例】

\# 显示IPv6路由信息表。

\<boot\> display ipv6 routing-table

Kernel IPv6 routing table

Destination                                 Next Hop

    Flags Metric Ref    Use Iface

::1/128                                     ::

    U     0      0        1 lo

FE80::201:2FF:FE03:406/128                  ::

    U     0      0        1 lo

FE80::/64                                   ::

    U     256    0        0 m-eth0

FF02::1:2/128                               FF02::1:2

    UC    0      2888     0 m-eth0

FF00::/8                                    ::

    U     256    0        0 m-eth0

表1-5 display ipv6 routing-table命令显示信息描述表

字段

描述

Kernel IPv6 routing table

IPv6路由表信息

Destination

目的地址

Next Hop

下一跳

Flags

标志位：

·G：网关路由

·H：主机路由

·D：通过邻居发现学习到的缺省路由

·A：通过路由发布学习到的路由

·C：缓存表项，用于快速转发去往某目的地的报文

·U：可用路由

Metric

路由开销

Ref

表示路由表项被其它表项引用的次数，即和其它表项间的依赖关系

Use

表示这条表项被使用过的次数，即该路由被匹配到的次数

Iface

出接口，lo表示环回口

**应急Shell \-- 应急Shell配置命令 \-- display version**

------------------------------------------------------------------------

**[display version**]命令用来显示Boot包的版本信息，包括当前使用的平台版本号、产品版本号等的相关信息。

【命令】

**[display version**]

【视图】

任意视图

【举例】

\# 查看Boot包的版本信息。（不同设备的版本信息不同，请以设备的实际情况为准）

\<boot\> display version

......略......

**应急Shell \-- 应急Shell配置命令 \-- format**

------------------------------------------------------------------------

**[format**]命令用来格式化存储介质。

【命令】

**[format ***device*]

【视图】

用户视图

【参数】

*[device*]：为存储介质的名称。该参数的具体取值与设备型号有关，请以设备的实际情况为准。

【使用指导】

格式化操作将导致存储介质上的所有文件丢失，并且不可恢复。尤其需要注意的是，如果存储介质上有启动配置文件和启动文件，格式化该存储介质，将丢失启动配置文件和启动文件，导致设备重启后无法启动，请谨慎操作。

【举例】

\# 格式化Flash。

\<boot\> format flash:

All data on flash: will be lost, continue?[Y/N:y]

Formatting flash:... Done.

**应急Shell \-- 应急Shell配置命令 \-- ftp**

------------------------------------------------------------------------

**[ftp**]命令用来访问FTP服务器。

【命令】

**[ftp **[{ *server-ipv4-address* \| **ipv6** *server-ipv6-address* } { **get** *remote-file* *local-file* \| **put** *local-file* *remote-file* }]]

【视图】

用户视图

【参数】

*[server-ipv4-address*]：FTP服务器的IPv4地址。

*[server-ipv6-address*]：FTP服务器的IPv6地址。

**[get ***remote-file* *local-file*]：表示从FTP服务器上下载一个文件到本地，*remote-file*表示FTP服务器上的文件的名称，*local-file*表示本地的文件的名称。

**[put ***local-file* *remote-file*]：表示从本地上传一个文件到FTP服务器，*local-file*表示本地的文件的名称，*remote-file*表示FTP服务器上的文件的名称。

【使用指导】

当网络拥塞，文件传输速度很慢的时候，用户可以使用\<Ctrl+C\>组合键中断本次FTP操作，稍后再试。

【举例】

\# 使用用户名test、密码123到FTP服务器192.168.1.100上下载文件111.txt，保存到本地时使用名称222.txt。

\<boot\> ftp 192.168.1.100 get 111.txt flash:/222.txt

User: test

Password: \*\*\*

**应急Shell \-- 应急Shell配置命令 \-- install load**

------------------------------------------------------------------------

**[install load**]命令用来加载System包，并引导设备进入Comware系统。

【命令】

**[install** **load** *system-package*]

【视图】

用户视图

【参数】

*[system-package*]：System包的名称，为1～63个字符的字符串，不区分大小写。该文件必须是设备存储介质根目录下，后缀名为.bin的文件，且文件名中必须包含存储介质的名称，形如flash:/startup-system.bin。（集中式设备）

*[system-package*]：System包的名称，为1～63个字符的字符串，不区分大小写。该文件必须是当前主控板存储介质根目录下，后缀名为.bin的文件，且文件名中必须包含存储介质的名称，不能包含slot信息，形如flash:/startup-system.bin。（分布式设备－独立运行模式）

*[system-package*]：System包的名称，为1～63个字符的字符串，不区分大小写。该文件必须是本成员设备存储介质根目录下，后缀名为.bin的文件，且文件名中必须包含存储介质的名称，不能包含slot信息，形如flash:/startup-system.bin。（集中式IRF设备）

*[system-package*]：System包的名称，为1～63个字符的字符串，不区分大小写。该文件必须是当前主控板存储介质根目录下，后缀名为.bin的文件，且文件名中必须包含存储介质的名称，不能包含chassis和slot信息，形如flash:/startup-system.bin。（分布式设备－IRF模式）

【使用指导】

执行该命令，系统会同时更新主用下次启动软件包列表，新列表中只包含Boot包和System包，以保证设备下次能够正常启动。如需运行Feature包和补丁包，须重新下载、安装，具体配置步骤请参见"基础配置指导"中的"软件升级"和"ISSU"。

【举例】

\# 加载System包，进入Comware系统。

\<boot\> install load flash:/system.bin

Check package flash:/system.bin \...

Extracting package \...

Loading\...

Line con1 is available.

Press ENTER to get started.

**应急Shell \-- 应急Shell配置命令 \-- interface m-eth0**

------------------------------------------------------------------------

**[interface m-eth0**]命令用来进入管理以太网接口视图。

【命令】

**[interface m-eth0**]

【视图】

系统视图

【使用指导】

进入管理以太网接口视图后，可以给管理以太网接口配置IP地址和网关。

【举例】

\# 进入管理以太网接口视图。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0

【相关命令】

·**quit**

**应急Shell \-- 应急Shell配置命令 \-- ip address**

------------------------------------------------------------------------

**[ip address**]命令用来配置管理以太网接口的IPv4地址。

**[undo ip address**]命令用来恢复缺省情况。

【命令】

**[ip**[ **address** *ip-address* { *mask-length* \| *mask* }]]

**[undo ip address**]

【缺省情况】

管理以太网接口下没有配置IPv4地址。

【视图】

管理以太网接口视图

【参数】

*[ip-address*]：IPv4地址，为点分十进制格式。

*[mask-length*]：子网掩码长度，取值范围为1～31。

*[mask*]：子网掩码，为点分十进制格式。

【使用指导】

多次使用本命令，最新配置生效。

需要注意的是：

·在手工关闭的管理以太网接口下配置或删除IP地址时，系统会同时自动激活该接口。

·请确保配置的IP地址没有和网络上其它设备的IP地址冲突。

【举例】

\# 将管理以太网接口的IP地址配置为192.168.1.1/24。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0 ip address 192.168.1.1 24

**应急Shell \-- 应急Shell配置命令 \-- ip gateway**

------------------------------------------------------------------------

**[ip gateway**]命令用来给管理以太网接口配置IPv4网关。

**[undo ip gateway**]命令用来恢复缺省情况。

【命令】

**[ip** **gateway** *ip-address*]

**[undo ip gateway**]

【缺省情况】

管理以太网接口下没有配置IPv4网关。

【视图】

管理以太网接口视图

【参数】

*[ip-address*]：IPv4网关的地址，为点分十进制格式。

【使用指导】

在IPv4网络中，当本设备需要和不在同一网段的远程设备通信时，需要配置IPv4网关来转发报文。

多次使用本命令，最新配置生效。

修改或者删除管理以太网接口的IP地址，会导致网关配置被删除。

【举例】

\# 将管理以太网接口的IPv4网关配置为192.168.1.5。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0 ip gateway 192.168.1.5

**应急Shell \-- 应急Shell配置命令 \-- ipv6 address**

------------------------------------------------------------------------

**[ipv6 address**]命令用来配置管理以太网接口的IPv6地址。

**[undo ipv6 address**]命令用来恢复缺省情况。

【命令】

**[ipv6** **address** *ipv6-address prefix-length*]

**[undo ipv6 address**]

【缺省情况】

管理以太网接口下没有配置IPv6地址。

【视图】

管理以太网接口视图

【参数】

*[ipv6-address*]：IPv6地址。

*[prefix-length*]：前缀的长度，取值范围为1～128。

【使用指导】

多次使用本命令，最新配置生效。

在手工关闭的管理以太网接口下配置或删除IPv6地址时，系统会同时自动激活该接口。

【举例】

\# 将管理以太网接口的IPv6地址配置为2001::1/64。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0 ipv6 address 2001::1 64

**应急Shell \-- 应急Shell配置命令 \-- ipv6 gateway**

------------------------------------------------------------------------

**[ipv6 gateway**]命令用来给管理以太网接口配置IPv6网关。

**[undo ipv6** **gateway**]命令用来恢复缺省情况。

【命令】

**[ipv6** **gateway** *link-local*]

**[undo ipv6** **gateway**]

【缺省情况】

管理以太网接口下没有配置IPv6网关。

【视图】

管理以太网接口视图

【参数】

*[link-local*]：IPv6网关的链路本地地址。

【使用指导】

在IPv6网络中，当本设备需要和不在同一网段的远程设备通信时，需要配置IPv6网关来转发报文。

多次使用本命令，最新配置生效。

修改或者删除管理以太网接口的IPv6地址，会导致IPv6网关配置被删除。

【举例】

\# 将管理以太网接口的IPv6网关配置为FE80::BAAF:67FF:FE27:DCD0。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0 ipv6 gateway FE80::BAAF:67FF:FE27:DCD0

**应急Shell \-- 应急Shell配置命令 \-- mkdir**

------------------------------------------------------------------------

**[mkdir**]命令用来在存储介质的指定路径下创建文件夹。

【命令】

**[mkdir** *directory*]

【视图】

用户视图

【参数】

*[directory*]：文件夹的名称。

【使用指导】

在使用该命令创建文件夹之前，指定的路径必须已经存在。比如：创建文件夹flash:/test/mytest，这时，test文件夹必须已经存在，否则，创建失败。

如果创建的文件夹与指定路径下的其它文件或文件夹重名，则创建操作失败。

【举例】

\# 在当前路径创建文件夹test。

\<boot\> mkdir flash:/test

Directory flash:/test created.

\# 在路径test/下创建文件夹subtest。

\<boot\> mkdir flash:/test/subtest

Directory flash:/test/subtest created.

【相关命令】

·**dir**

·**rmdir**

**应急Shell \-- 应急Shell配置命令 \-- more**

------------------------------------------------------------------------

**[more**]命令用来显示指定文件的内容。

【命令】

**[more ***file-url*]

【视图】

用户视图

【参数】

*[file-url*]：要显示的文件的名称。

【举例】

\# 显示文件test.txt的内容。

\<boot\> more flash:/test.txt

Have a nice day.

**应急Shell \-- 应急Shell配置命令 \-- move**

------------------------------------------------------------------------

**[move**]命令用来移动文件。

【命令】

**[move ***fileurl-source fileurl-dest*]

【视图】

用户视图

【参数】

*[fileurl-source*]：源文件的名称。为1～63个字符的字符串，不区分大小写。

*[fileurl-dest*]：目标文件或文件夹的名称。为1～63个字符的字符串，不区分大小写。

【使用指导】

执行该命令时，如果指定的目标文件不存在，则系统会先直接执行文件移动操作；如果指定的目标文件已存在，则系统会提示是否覆盖该文件，如果选择"Y",系统会执行文件移动操作，如果选择"N"，则不做任何处理。

【举例】

\# 移动文件config.cfg到目录flash:/test下。

\<boot\>move flash:/config.cfg flash:/test/

Move flash:/config.cfg to flash:/test/config.cfg?[Y/N:y]

\<boot\> dir flash:/test

Directory of flash:/test

     0      -rw-       77065  Oct 20 1939 06:15:02     test.mdb

61440 KB total (11108 KB free)

**应急Shell \-- 应急Shell配置命令 \-- ping**

------------------------------------------------------------------------

**[ping**]命令用来检查指定目的端是否可达。

【命令】

**[ping**[ [ **-c** *count \|* **-s** *size* ] \* *ip-address*]]

【视图】

任意视图

【参数】

**[-c** *count*]：指定发送的ICMP回显请求报文的数目，取值范围为1～2147483647，缺省值为5。

**[-s*** size*]：指定发送的ICMP回显请求报文的长度，取值范围为20～8100，单位为字节，缺省值为56字节。

*[ip-address*]：目的端的IPv4地址，为点分十进制格式。

【使用指导】

执行**ping**命令后，源端会给目的端发送ICMP回显请求报文。在执行命令过程中，键入\<Ctrl+C\>可终止**ping**操作。

【举例】

\# 检查到目的端1.2.1.1是否可达。

\<boot\> ping 1.2.1.1

PING 1.2.1.1 (1.2.1.1): 56 data bytes

56 bytes from 1.2.1.1: seq=0 ttl=128 time=2.243 ms

56 bytes from 1.2.1.1: seq=1 ttl=128 time=0.717 ms

56 bytes from 1.2.1.1: seq=2 ttl=128 time=0.891 ms

56 bytes from 1.2.1.1: seq=3 ttl=128 time=0.745 ms

56 bytes from 1.2.1.1: seq=4 ttl=128 time=0.911 ms

\-\-- 1.2.1.1 ping statistics \-\--

5 packets transmitted, 5 packets received, 0% packet loss

round-trip min/avg/max = 0.717/1.101/2.243 ms

表1-6 ping命令显示信息描述表

字段

描述

PING 1.2.1.1 (1.2.1.1)

检查IP地址为1.2.1.1的设备是否可达

56 data bytes

每个ICMP回显请求报文中的数据字节数

56 bytes from 1.2.1.1: seq=0 ttl=128 time=2.243 ms

收到IP地址为1.2.1.1的设备回复的ICMP响应报文

·bytes表示ICMP响应报文中数据的字节数

·seq表示报文序号，用来判断报文是否有分组丢失、失序或重复

·ttl表示ICMP响应报文中的TTL值

·time表示响应时间

\-\-- 1.2.1.1 ping statistics \-\--

Ping操作中收发数据的统计结果

5 packets transmitted

发送的ICMP回显请求报文数

5 packets received

收到的ICMP响应报文数

0% packet loss

未响应请求报文占发送的总请求报文的百分比

round-trip min/avg/max = 0.717/1.101/2.243 ms

响应时间的最小值、平均值、最大值和标准方差，单位为毫秒

**应急Shell \-- 应急Shell配置命令 \-- ping ipv6**

------------------------------------------------------------------------

**[ping ipv6**]命令用来检查指定IPv6地址是否可达。

【命令】

**[ping ipv6**[ [ **-c** *count* \| **-s** *size* ] \* *ipv6-address*]]

【视图】

任意视图

【参数】

**[-c** *count*]：指定发送的ICMPv6回显请求报文的数目，取值范围为1～2147483647，缺省值为5。

**[-s*** size*]：指定发送的ICMPv6回显请求报文的长度，取值范围为20～8100，单位为字节，缺省值为56字节。

*[ipv6-address*]：目的主机的IPv6地址。

【使用指导】

执行**ping ipv6**命令后，源端会给目的端发送ICMPv6回显请求报文。在执行命令过程中，键入\<Ctrl+C\>可终止**ping ipv6**操作。

【举例】

\# 检查到目的端2001::2是否可达。

\<boot\> ping ipv6 2001::2

ping ipv6 2001::2

PING 2001::2 (2001::2): 56 data bytes

56 bytes from 2001::2: seq=0 ttl=64 time=5.420 ms

56 bytes from 2001::2: seq=1 ttl=64 time=1.140 ms

56 bytes from 2001::2: seq=2 ttl=64 time=2.027 ms

56 bytes from 2001::2: seq=3 ttl=64 time=0.887 ms

56 bytes from 2001::2: seq=4 ttl=64 time=0.791 ms

\-\-- 2001::2 ping statistics \-\--

5 packets transmitted, 5 packets received, 0% packet loss

round-trip min/avg/max = 0.791/2.053/5.420 ms 

该命令的显示信息描述表请参见 表1-6(?-1885171420#_Ref198434076)。

**应急Shell \-- 应急Shell配置命令 \-- pwd**

------------------------------------------------------------------------

**[pwd**]命令用来显示当前工作路径。

【命令】

**[pwd**]

【视图】

用户视图

【举例】

\# 显示当前工作路径。

\<boot\> pwd

flash:

**应急Shell \-- 应急Shell配置命令 \-- quit**

------------------------------------------------------------------------

**[quit**]命令用来从当前视图退回到上一级视图。

【命令】

**[quit**]

【视图】

系统视图/管理以太网接口视图

【举例】

\# 从管理以太网接口视图退回到用户视图。

boot-m-eth0 quit

boot quit

\<boot\>

**应急Shell \-- 应急Shell配置命令 \-- reboot**

------------------------------------------------------------------------

**[reboot**]命令用来重启设备。（集中式设备）

**[reboot**]命令用来重启当前登录的主控板。（分布式设备－独立运行模式/分布式设备－IRF模式）

**[reboot**]命令用来重启当前登录的成员设备。（集中式IRF设备）

【命令】

**[reboot**]

【视图】

用户视图

【举例】

\# 重启设备。（集中式设备）

\<boot\> reboot

\# 重启当前登录的主控板。（分布式设备－独立运行模式/分布式设备－IRF模式）

\<boot\> reboot

\# 重启当前登录的成员设备。（集中式IRF设备）

\<boot\> reboot

**应急Shell \-- 应急Shell配置命令 \-- reset ssh public-key**

------------------------------------------------------------------------

**[reset ssh public-key**]命令用来清除保存在本设备的所有SSH服务器的公钥。

【命令】

**[reset ssh public-key**]

【视图】

用户视图

【使用指导】

在设备上使用**ssh2**命令首次登录SSH服务器时，设备会将该服务器的公钥保存到本地，以便下次登录进行身份认证时使用。如果SSH服务器的公钥变更，因为新旧公钥不一致，会导致设备再次SSH登录该服务器失败。此时可使用**reset ssh public-key**命令来清除原公钥，重新执行**ssh2**命令触发新的SSH协商。

【举例】

\# 清除保存在本设备的所有SSH服务器的公钥。

\<boot\> ssh2 192.168.1.59

login as:client001

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!

Someone could be eavesdropping on you right now (man-in-the-middle attack)!

It is also possible that a host key has just been changed.

The fingerprint for the RSA key sent by the remote host is

83:2d:b6:90:4a:1b:0e:c1:ea:af:09:3a:65:09:8a:b3.

Please contact your system administrator.

RSA host key for 192.168.1.59 has changed and you have requested strict checking

.

Host key verification failed.

\<boot\> reset ssh public-key

\<boot\> ssh2 192.168.1.59

login as:client001

The authenticity of host \'192.168.1.59 (192.168.1.59)\' can\'t be established.

RSA key fingerprint is 83:2d:b6:90:4a:1b:0e:c1:ea:af:09:3a:65:09:8a:b3.

Are you sure you want to continue connecting (yes/no)? yes

Warning: Permanently added \'192.168.1.59\' (RSA) to the list of known hosts.

client001@192.168.1.59\'s password:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \* 

\* Without the owner\'s prior written consent,                                 \* 

\* no decompiling or reverse-engineering shall be allowed.                    \* 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\<Sysname.59\>

**应急Shell \-- 应急Shell配置命令 \-- rmdir**

------------------------------------------------------------------------

**[rmdir**]命令用来删除已有目录。

【命令】

**[rmdir** *directory*]

【视图】

用户视图

【参数】

*[directory*]：待删除的目录名。

【使用指导】

被删除的目录必须为空目录。即删除目录前，必须先删除该目录下的所有文件及子目录，文件的删除请参见**delete**命令。

【举例】

\# 删除目录mydir。

\<boot\> rmdir flash:/mydir

Remove directory flash:/mydir?[Y/N:y]

Directory flash:/1 removed. 

【相关命令】

·**delete**

·**dir**

·**mkdir**

**应急Shell \-- 应急Shell配置命令 \-- shutdown**

------------------------------------------------------------------------

**[shutdown**]命令用来关闭管理以太网接口。

**[undo shutdown**]命令用来打开管理以太网接口。

【命令】

**[shutdown**]

**[undo shutdown**]

【缺省情况】

管理以太网接口处于打开状态。

【视图】

管理以太网接口视图

【使用指导】

当管理以太网接口异常时，可通过**shutdown**命令关闭此接口，然后再通过**undo shutdown**命令重新打开。

【举例】

\# 关闭管理以太网接口。

\<boot\> system-view

boot interface m-eth0

boot-m-eth0 shutdown

\# 打开管理以太网接口。

boot-m-eth0 undo shutdown

**应急Shell \-- 应急Shell配置命令 \-- ssh2**

------------------------------------------------------------------------

**[ssh2**]命令用来使用SSH协议登录到SSH服务器。

【命令】

**[ssh2 **[{ *server-ipv4-address \|* **ipv6** *server-ipv6-address* }]]

【视图】

用户视图

【参数】

*[server-ipv4-address*]：SSH服务器的IPv4地址，为点分十进制格式。

**[ipv6** *server-ipv6-address*]：SSH服务器的IPv6地址。

【使用指导】

如果在登录过程中，SSH服务器长时间没有响应，用户可以使用\<Ctrl+C\>组合键中断本次SSH登录，稍后再试。

【举例】

\# 使用SSH协议第一次登录到SSH服务器192.168.1.59。

\<boot\> ssh2 192.168.1.59

login as:client001

The authenticity of host \'192.168.1.59 (192.168.1.59)\' can\'t be established.

RSA key fingerprint is 3d:ee:1f:f9:81:be:4f:aa:42:88:1c:ab:81:4e:95:6f.

Are you sure you want to continue connecting (yes/no)? yes

Warning: Permanently added \'192.168.1.59\' (RSA) to the list of known hosts.

client001@192.168.1.59\'s password:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \* 

\* Without the owner\'s prior written consent,                                 \* 

\* no decompiling or reverse-engineering shall be allowed.                    \* 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\<Syaname.59\>

\# 使用SSH协议再次登录到SSH服务器192.168.1.59。

\<boot\> ssh2 192.168.1.59

login as:client001

client001@192.168.1.59\'s password:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\* Copyright (c) 2004-2012 Hangzhou H3C Tech. Co., Ltd. All rights reserved.  \* 

\* Without the owner\'s prior written consent,                                 \* 

\* no decompiling or reverse-engineering shall be allowed.                    \* 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

\<Syaname.59\>

**应急Shell \-- 应急Shell配置命令 \-- system-view**

------------------------------------------------------------------------

**[system-view**]命令用来从用户视图进入系统视图。

【命令】

system-view

【视图】

用户视图

【使用指导】

应急Shell启动后直接进入用户视图。

【举例】

\# 从用户视图进入系统视图。

\<boot\> system-view

boot

【相关命令】

·**quit**

**应急Shell \-- 应急Shell配置命令 \-- telnet**

------------------------------------------------------------------------

**[telnet**]命令用来使用Telnet协议登录到Telnet服务器。

【命令】

**[telnet**[ { *server-ipv4-address \|* **ipv6** *server-ipv6-address* }]]

【视图】

用户视图

【参数】

*[server-ipv4-address*]：Telnet服务器的IPv4地址，为点分十进制格式。

*[server-ipv6-address*]：Telnet服务器的IPv6地址。

【使用指导】

如果在登录过程中，Telnet服务器长时间没有响应，用户可以使用\<Ctrl+K\>组合键中断本次Telnet登录，稍后再试。

【举例】

\# 使用Telnet协议登录到Telnet服务器192.168.100.1。

\<boot\> telnet 192.168.100.1

**应急Shell \-- 应急Shell配置命令 \-- tftp**

------------------------------------------------------------------------

**[tftp**]命令用来访问TFTP服务器。

【命令】

**[tftp**[ *server-ipv4-address* { **get** *remote-file local-file* \| **put** *local-file* *remote-file* }]]

**[tftp ipv6**[ *server-ipv6-address* { **get** *remote-file local-file* \| **put** *local-file* *remote-file* }]]

【视图】

用户视图

【参数】

*[server-ipv4-address*]：TFTP服务器的IPv4地址，点分十进制格式。

*[server-ipv6-address*]：TFTP服务器的IPv6地址。

**[get ***remote-file* *local-file*]：表示从TFTP服务器上下载一个文件到本地，*remote-file*表示TFTP服务器上的文件的名称，*local-file*表示本地的文件的名称。

**[put ***local-file* *remote-file*]：表示从本地上传一个文件到TFTP服务器，*local-file*表示本地的文件的名称，*remote-file*表示TFTP服务器上的文件的名称。

【使用指导】

当网络拥塞，文件传输速度很慢的时候，用户可以使用\<Ctrl+C\>组合键中断本次TFTP操作，稍后再试。

【举例】

\# 从TFTP服务器192.168.1.100上下载文件111.txt，保存到本地时使用的文件名为222.txt。

\<boot\> tftp 192.168.1.100 get 111.txt flash:/222.txt

\# 将设备的启动配置文件startup.cfg上传到TFTP服务器192.168.1.100。

\<boot\> tftp 192.168.1.100 put flash:/startup.cfg startup.cfg
