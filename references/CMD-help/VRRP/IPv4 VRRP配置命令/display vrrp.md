<!-- CMD-INDEX
  display vrrp                        | 任意视图             | L33
  display vrrp statistics             | 任意视图             | L641
  reset vrrp statistics               | 用户视图             | L993
  snmp-agent trap enable vrrp         | 系统视图             | L1033
  vrrp check-ttl enable               | 接口视图             | L1079
  vrrp dot1q                          | 三层以太网子接口视图/三层聚合子接口视图/三层RPR逻辑接口视图 | L1135
  vrrp dscp                           | 系统视图             | L1185
  vrrp mode                           | 系统视图             | L1225
  vrrp version                        | 接口视图             | L1287
  vrrp vrid                           | 接口视图             | L1345
  vrrp vrid authentication-mode       | 接口视图             | L1419
  vrrp vrid preempt-mode              | 接口视图             | L1511
  vrrp vrid priority                  | 接口视图             | L1581
  vrrp vrid shutdown                  | 接口视图             | L1649
  vrrp vrid source-interface          | 接口视图             | L1707
  vrrp vrid timer advertise           | 接口视图             | L1767
  vrrp vrid track                     | 接口视图             | L1841
  display vrrp ipv6                   | 任意视图             | L1969
  display vrrp ipv6 statistics        | 任意视图             | L2547
  reset vrrp ipv6 statistics          | 用户视图             | L2899
  vrrp ipv6 dot1q                     | 三层以太网子接口视图/三层聚合子接口视图/三层RPR逻辑接口视图 | L2939
  vrrp ipv6 dscp                      | 系统视图             | L2989
  vrrp ipv6 mode                      | 系统视图             | L3029
  vrrp ipv6 vrid                      | 接口视图             | L3083
  vrrp ipv6 vrid preempt-mode         | 接口视图             | L3161
  vrrp ipv6 vrid priority             | 接口视图             | L3231
  vrrp ipv6 vrid shutdown             | 接口视图             | L3297
  vrrp ipv6 vrid timer advertise      | 接口视图             | L3355
  vrrp ipv6 vrid track                | 接口视图             | L3427
-->

**VRRP \-- IPv4 VRRP配置命令 \-- display vrrp**

------------------------------------------------------------------------

**[display** **vrrp**]命令用来显示IPv4 VRRP备份组的状态信息。

【命令】

**[display** **vrrp** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的IPv4 VRRP备份组状态信息。其中，*interface-type* *interface-number*为接口类型和接口编号。

**[vrid*** virtual-router-id*]：显示指定IPv4 VRRP备份组的状态信息。其中，*virtual-router-id*为IPv4 VRRP备份组号，取值范围为1～255。

**[verbose**]：显示IPv4 VRRP备份组状态的详细信息。如果不指定本参数，则显示IPv4 VRRP备份组状态的简要信息。

【使用指导】

如果不指定接口名和备份组号，则显示该路由器上所有IPv4 VRRP备份组的状态信息；如果只指定接口名，不指定备份组号，则显示该接口上的所有IPv4 VRRP备份组的状态信息；如果同时指定接口名和备份组号，则显示该接口上指定IPv4 VRRP备份组的状态信息。

【举例】

\# VRRP工作在标准协议模式时，显示全部IPv4 VRRP备份组的简要信息。

\<Sysname\> display vrrp

IPv4 Virtual Router Information:

 Running Mode      : Standard

 Total number of virtual routers : 1

 Interface          VRID  State        Running Adver   Auth     Virtual

                                       Pri     Timer   Type        IP

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 GE1/0/1            1     Master       150     100     Simple   1.1.1.1

表1-1 display vrrp命令显示信息描述表（标准协议模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Standard（标准协议模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Running Pri

路由器的运行优先级，即路由器当前的优先级。配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Auth Type

认证类型，包括：

·None：无认证

·Simple：简单字符认证

·MD5：MD5认证

Virtual IP

备份组的虚拟IP地址

\# VRRP工作在标准协议模式时，显示全部IPv4 VRRP备份组的详细信息。

\<Sysname\> display vrrp verbose

IPv4 Virtual Router Information:

 Running Mode      : Standard

 Total number of virtual routers : 2

   Interface GigabitEthernet1/0/1

     VRID           : 1                    Adver Timer  : 100

     Admin Status   : Up                   State        : Master

     Config Pri     : 150                  Running Pri  : 150

     Preempt Mode   : Yes                  Delay Time   : 5

     Auth Type      : Simple               Key          : \*\*\*\*\*\*

     Virtual IP     : 1.1.1.1

Virtual MAC    : 0000-5e00-0101

     Master IP      : 1.1.1.2

VRRP Track Information:

     Track Object   : 1                    State : Positive   Pri Reduced : 50

   Interface GigabitEthernet1/0/1

     VRID           : 11                   Adver Timer  : 100

     Admin Status   : Up                   State        : Backup

     Config Pri     : 80                   Running Pri  : 80

     Preempt Mode   : Yes                  Delay Time   : 0

     Become Master  : 2370ms left

     Auth Type      : None

     Virtual IP     : 1.1.1.11

Virtual MAC    : 0000-5e00-010b

     Master IP      : 1.1.1.12

表1-2 display vrrp verbose命令显示信息描述表（标准协议模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Standard（标准协议模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Admin Status

管理状态，包括Up和Down两种状态

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Config Pri

路由器的配置优先级，即通过**vrrp vrid priority**命令指定的路由器优先级

Running Pri

路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Preempt Mode

抢占模式，取值包括：

·Yes：路由器工作在抢占模式

·No：路由器工作在非抢占模式

Delay Time

抢占延迟时间，单位为厘秒

Become Master

切换到Master状态需要等待的时间，单位为毫秒，只有处于Backup状态时才会显示此信息

Auth Type

认证类型，包括：

·None：无认证

·Simple：简单字符认证

·MD5：MD5认证

Key

认证字，无认证时不显示此信息

Virtual IP

备份组的虚拟IP地址

Virtual MAC

备份组虚拟IP地址对应的虚拟MAC地址。只在路由器为Master状态时，才会显示此信息

Master IP

处于Master状态的路由器所对应接口的主IP地址

VRRP Track Information

VRRP备份组监视的Track项信息。执行**vrrp vrid track**命令后，才会显示此信息

Track Object

监视的Track项

State

Track项的状态，Track项的状态可包括Negative、Positive和NotReady

Pri Reduced

监视的Track项状态为Negative时，优先级降低的数额

Switchover

快速切换。显示此信息时表示当监视的Track项变为Negative状态时，Backup路由器会马上抢占成为Master路由器

\# VRRP工作在负载均衡模式时，显示全部IPv4 VRRP备份组的简要信息。

\<Sysname\> display vrrp

IPv4 Virtual Router Information:

 Running Mode      : Load Balance

 Total number of virtual routers : 1

 Interface          VRID  State        Running Address             Active

                                       Pri

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 GE1/0/1            1     Master       150     1.1.1.1             Local

 \-\-\-\--              VF 1  Active       255     000f-e2ff-0011      Local

表1-3 display vrrp命令显示信息描述表（负载均衡模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Load Balance（负载均衡模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）*number*或虚拟转发器编号VF *number*

State

对于虚拟备份组（VRID为*number*），该字段表示当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的状态，取值为Active、Listening或Initialize

Running Pri

对于虚拟备份组（VRID为*number*），该字段表示路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的运行优先级，配置监视指定Track项后，虚拟转发器的优先级会根据Track项的状态改变

Address

对于虚拟备份组（VRID为*number*），该字段表示备份组的虚拟IP地址

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的虚拟MAC地址

Active

对于虚拟备份组（VRID为*number*），该字段表示Master的接口IP地址，当前路由器为Master时，显示为local

对于虚拟转发器（VRID为VF *number*），该字段表示AVF的接口IP地址，当前虚拟转发器为AVF时，显示为local

\# VRRP工作在负载均衡模式时，显示全部IPv4 VRRP备份组的详细信息。

\<Sysname\> display vrrp verbose

IPv4 Virtual Router Information:

 Running Mode      : Load Balance

 Total number of virtual routers : 2

   Interface GigabitEthernet1/0/1

     VRID           : 1                    Adver Timer  : 100

     Admin Status   : Up                   State        : Master

     Config Pri     : 150                  Running Pri  : 150

     Preempt Mode   : Yes                  Delay Time   : 5

     Auth Type      : None

     Virtual IP     : 10.1.1.1

                      10.1.1.2

                      10.1.1.3

     Member IP List : 10.1.1.10 (Local, Master)

                      10.1.1.20 (Backup)

   VRRP Track Information:

     Track Object   : 1                    State : Positive   Pri Reduced : 50

   Forwarder Information: 2 Forwarders 1 Active

     Config Weight  : 255

     Running Weight : 255

    Forwarder 01

     State          : Active

     Virtual MAC    : 000f-e2ff-0011 (Owner)

     Owner ID       : 0000-5e01-1101

     Priority       : 255

     Active         : local

    Forwarder 02

     State          : Listening

     Virtual MAC    : 000f-e2ff-0012 (Learnt)

     Owner ID       : 0000-5e01-1103

     Priority       : 127

     Active         : 10.1.1.20

   Forwarder Weight Track Information:

     Track Object   : 1          State : Positive   Weight Reduced : 250

   Interface GigabitEthernet1/0/1

     VRID           : 11                   Adver Timer  : 100

     Admin Status   : Up                   State        : Backup

     Config Pri     : 80                   Running Pri  : 80

     Preempt Mode   : Yes                  Delay Time   : 0

     Become Master  : 2370ms left

     Auth Type      : None

     Virtual IP     : 10.1.1.11

                    : 10.1.1.12

                    : 10.1.1.13

     Member IP List : 10.1.1.10 (Local, Backup)

                      10.1.1.15 (Master)

   Forwarder Information: 2 Forwarders 1 Active

     Config Weight  : 255

     Running Weight : 255

    Forwarder 01

     State          : Active

     Virtual MAC    : 000f-e2ff-40b1 (Learnt)

     Owner ID       : 0000-5e01-1103

     Priority       : 127

     Active         : 10.1.1.15

    Forwarder 02

     State          : Listening

     Virtual MAC    : 000f-e2ff-40b2 (Owner)

     Owner ID       : 0000-5e01-1101

     Priority       : 255

     Active         : local

表1-4 display vrrp verbose命令显示信息描述表（负载均衡模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Load Balance（负载均衡模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Admin Status

管理状态，包括Up和Down两种状态

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Config Pri

路由器的配置优先级，即通过**vrrp vrid priority**命令指定的路由器优先级

Running Pri

路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Preempt Mode

抢占模式，取值包括：

·Yes：路由器工作在抢占模式

·No：路由器工作在非抢占模式

Delay Time

抢占延迟时间，单位为厘秒

Become Master

切换到Master状态需要等待的时间，单位为毫秒，只有处于Backup状态时才会显示此信息

Auth Type

认证类型，包括：

·None：无认证

·Simple：简单字符认证

·MD5：MD5认证

Key

认证字，无认证时不显示此信息

Virtual IP

备份组的虚拟IP地址列表

Member IP List

备份组中成员设备的IP地址列表：

·Local：表示本地设备的IP地址

·Master：表示处于Master状态的成员设备的IP地址

·Backup：表示处于Backup状态的成员设备的IP地址

VRRP Track Information

VRRP备份组监视的Track项信息，执行**vrrp vrid track**命令后，才会显示此信息

Track Object

监视的Track项

State

Track项的状态，Track项的状态包括Negative、Positive和NotReady

Pri Reduced

监视的Track项状态为Negative时，优先级降低的数额，执行**vrrp vrid track**命令后，才会显示此信息

Switchover

快速切换，显示此信息时表示当监视的Track项变为Negative状态时，Backup路由器会马上抢占成为Master路由器

Forwarder Information: 2 Forwarders 1 Active

虚拟转发器信息：路由器的虚拟转发器数目为2，处于Active状态的虚拟转发器数目为1

Config Weight

虚拟转发器的配置权重，取值为255

Running Weight

虚拟转发器的运行权重，即虚拟转发器当前的权重，配置监视指定Track项后，虚拟转发器的权重会根据Track项的状态改变

Forwarder 01

虚拟转发器01的信息

State

虚拟转发器的状态，取值为Active、Listening或Initialize

Virtual MAC

虚拟转发器的虚拟MAC地址

Owner ID

虚拟转发器拥有者的接口实际MAC地址

Priority

虚拟转发器的优先级，取值范围为1～255

Active

AVF的接口IP地址，当前转发器为AVF时，显示为local

Forwarder Weight Track Configuration

虚拟转发器权重监视配置信息。执行**vrrp vrid weight** **track**命令后，才会显示此信息

Track Object

权重监视的Track项。执行**vrrp vrid weight** **track**命令后，才会显示此信息

State

Track项的状态，Track项的状态包括Negative、Positive和NotReady

Weight Reduced

监视的Track项状态为Negative时，权重降低的数额。执行**vrrp vrid weight** **track**命令后，才会显示此信息

**VRRP \-- IPv4 VRRP配置命令 \-- display vrrp statistics**

------------------------------------------------------------------------

**[display vrrp statistics**]命令用来显示IPv4 VRRP备份组的统计信息。

【命令】

**[display vrrp** **statistics** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的IPv4 VRRP备份组统计信息。其中，*interface-type* *interface-number*为接口类型和接口编号。

**[vrid ***virtual-router-id*]：显示指定备份组的IPv4 VRRP统计信息。其中，*virtual-router-id*为IPv4 VRRP备份组号，取值范围为1～255。

【使用指导】

如果不输入接口名和备份组号，则显示该路由器上所有IPv4 VRRP备份组的统计信息；如果只输入接口名，不输入备份组号，则显示该接口上的所有IPv4 VRRP备份组的统计信息；如果同时输入接口名和备份组号，则显示该接口上指定IPv4 VRRP备份组的统计信息。

【举例】

\# VRRP工作在标准协议模式时，显示所有IPv4 VRRP备份组的统计信息。

\<Sysname\> display vrrp statistics

 Interface               : GigabitEthernet1/0/1

 VRID                    : 1

 CheckSum Errors         : 0          Version Errors                : 0

 Invalid Pkts Rcvd  :      0          Unexpected Pkts Rcvd          : 0

 IP TTL Errors           : 0          Advertisement Interval Errors : 0

 Invalid Auth Type       : 0          Auth Failures                 : 0

 Packet Length Errors    : 0          Auth Type Mismatch            : 0

 Become Master           : 1          Address List Errors           : 0

 Adver Rcvd              : 0          Priority Zero Pkts Rcvd       : 0

 Adver Sent              : 807        Priority Zero Pkts Sent       : 0

 Global statistics

 CheckSum Errors         : 0

 Version Errors          : 0

 VRID Errors             : 0

\# VRRP工作在负载均衡模式时，显示全部IPv4 VRRP备份组的统计信息。

\<Sysname\> display vrrp statistics

 Interface               : GigabitEthernet1/0/1

 VRID                    : 1

 CheckSum Errors         : 0          Version Errors                : 0

 Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0

 IP TTL Errors           : 0          Advertisement Interval Errors : 0

 Invalid Auth Type       : 0          Auth Failures                 : 0

 Packet Length Errors    : 0          Auth Type Mismatch            : 0

 Become Master           : 39         Address List Errors           : 0

 Become AVF              : 13         Packet Option Errors          : 0

 Adver Rcvd              : 2562       Priority Zero Pkts Rcvd       : 1

 Adver Sent              : 16373      Priority Zero Pkts Sent       : 49

 Request Rcvd            : 2          Reply Rcvd                    : 10

 Request Sent            : 12         Reply Sent                    : 2

 Release Rcvd            : 0          VF Priority Zero Pkts Rcvd    : 1

 Release Sent            : 0          VF Priority Zero Pkts Sent    : 11

 Redirect Timer Expires  : 1          Time-out Timer Expires        : 0

 Global statistics

 CheckSum Errors         : 0

 Version Errors          : 0

 VRID Errors             : 0

表1-5 display vrrp statistics显示信息描述表（标准协议模式）

字段

描述

Interface

备份组所在接口

VRID

备份组号

CheckSum Errors

校验和错误的报文数

Version Errors

版本号错误的报文数

Invalid Pkts Rcvd

接收到报文类型错误的报文数

Unexpected Pkts Rcvd

接收到未期望的报文数

Advertisement Interval Errors

VRRP通告报文发送时间间隔错误的报文数

IP TTL Errors

TTL错误的报文数

Auth Failures

认证失败的报文数

Invalid Auth Type

认证类型无效的报文数

Auth Type Mismatch

认证类型不匹配的报文数

Packet Length Errors

VRRP报文长度错误的报文数

Address List Errors

备份组虚拟IP地址列表错误的报文数

Become Master

成为Master路由器的次数

Priority Zero Pkts Rcvd

收到的优先级为0的VRRP通告报文的数目

Adver Rcvd

收到的VRRP通告报文的数目

Priority Zero Pkts Sent

发送的优先级为0的VRRP通告报文的数目

Adver Sent

发送的VRRP通告报文的数目

Global statistics

所有备份组的全局统计信息

CheckSum Errors

校验和错误的报文总数

Version Errors

版本号错误的报文总数

VRID Errors

备份组号错误的报文总数

表1-6 display vrrp statistics显示信息描述表（负载均衡模式）

字段

描述

Interface

备份组所在接口

VRID

备份组号

CheckSum Errors

校验和错误的报文数

Version Errors

版本号错误的报文数

Invalid Pkts Rcvd

接收到报文类型错误的报文数

Unexpected Pkts Rcvd

接收到未期望的报文数

Advertisement Interval Errors

VRRP通告报文发送时间间隔错误的报文数

IP TTL Errors

TTL错误的报文数

Auth Failures

认证错误的报文数

Invalid Auth Type

认证类型无效的报文数

Auth Type Mismatch

认证类型不匹配的报文数

Packet Length Errors

VRRP报文长度错误的报文数

Address List Errors

虚拟IP地址列表错误的报文数

Become Master

成为Master路由器的次数

Redirect Timer Expires

Redirect Timer超时的次数

Become AVF

成为AVF的次数

Time-out Timer Expires

Time-out Timer超时的次数

Adver Rcvd

收到的Advertisement报文的数目

Request Rcvd

收到的Request报文的数目

Adver Sent

发送的Advertisement报文的数目

Request Sent

发送的Request报文的数目

Reply Rcvd

收到的Reply报文的数目

Release Rcvd

收到的Release报文的数目

Reply Sent

发送的Reply报文的数目

Release Sent

发送的Release报文的数目

Priority Zero Pkts Rcvd

收到的路由器优先级为0的Advertisement报文的数目

VF Priority Zero Pkts Rcvd

收到的虚拟转发器优先级为0的Advertisement报文的数目

Priority Zero Pkts Sent

发送的路由器优先级为0的Advertisement报文的数目

VF Priority Zero Pkts Sent

发送的虚拟转发器优先级为0的Advertisement报文的数目

Packet Option Errors

报文状态选项错误的次数

Global statistics

所有备份组的全局统计信息

CheckSum Errors

校验和错误的报文总数

Version Errors

版本号错误的报文总数

VRID Errors

备份组号错误的报文总数

【相关命令】

·**reset vrrp statistics**

**VRRP \-- IPv4 VRRP配置命令 \-- reset vrrp statistics**

------------------------------------------------------------------------

**[reset vrrp statistics**]命令用来清除IPv4 VRRP备份组的统计信息。

【命令】

**[reset vrrp statistics ** **interface** *interface-type interface-number*  **vrid** *virtual-router-id*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：清除指定接口的IPv4 VRRP备份组统计信息。其中，*interface-type interface-number*为接口类型和接口编号。

**[vrid ***virtual-router-id*]：清除指定备份组的IPv4 VRRP统计信息。其中，*virtual-router-id*为IPv4 VRRP备份组号，取值范围为1～255。

【使用指导】

在清除IPv4 VRRP备份组统计信息时，如果不输入接口名和备份组号，则清除该路由器上所有IPv4 VRRP备份组的统计信息；如果只输入接口名，不输入备份组号，则清除该接口上所有IPv4 VRRP备份组的统计信息；如果同时输入接口名和备份组号，则清除该接口上指定IPv4 VRRP备份组的统计信息。

【举例】

\# 清除所有接口上所有IPv4 VRRP备份组的VRRP统计信息。

\<Sysname\> reset vrrp statistics

【相关命令】

·**display vrrp** **statistics**

**VRRP \-- IPv4 VRRP配置命令 \-- snmp-agent trap enable vrrp**

------------------------------------------------------------------------

**[snmp-agent** **trap** **enable vrrp**]命令用来在全局下开启VRRP告警功能。

**[undo** **snmp-agent** **trap** **enable vrrp**]命令用来在全局下关闭VRRP告警功能。

【命令】

**[snmp-agent**[ **trap** **enable** **vrrp** [ **auth-failure** \| **new-master** ]]]

**[undo**[ **snmp-agent** **trap** **enable** **vrrp** [ **auth-failure** \| **new-master** ]]]

【缺省情况】

VRRP的告警功能处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[auth-failure**]：配置该参数后，当VRRP备份组中的设备收到的VRRP通告报文中的认证类型或认证字与本地不匹配时，会产生RFC2787规定的告警信息。

**[new-master**]：配置该参数后，当备份组中设备从Initialize或Backup状态升级为Master状态时，会产生RFC2787规定的告警信息。

【使用指导】

开启告警功能后，设备就可以向目的主机发送告警信息。具体是发送Inform报文还是Trap报文，以及发往哪个目的主机，请通过**snmp-agent** **target-host**命令来配置。

【举例】

\# 当VRRP备份组中的设备收到的VRRP通告报文中的认证类型或认证字与本地不匹配时，发送RFC2787规定的告警信息。

\<Sysname\> system-view

Sysname snmp-agent trap enable vrrp auth-failure

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp check-ttl enable**

------------------------------------------------------------------------

**[vrrp check-ttl enable**]命令用来使能对IPv4 VRRP报文TTL域的检查。

**[undo vrrp check-ttl enable**]命令用来禁止对IPv4 VRRP报文的TTL域的检查。

【命令】

**[vrrp check-ttl enable**]

**[undo vrrp check-ttl enable**]

【缺省情况】

检查IPv4 VRRP报文的TTL域。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

Master路由器定时发送VRRP通告报文，来通告它的存在。该报文以组播的形式在本网段内传播，不能被路由器转发，因此报文中的TTL值不会改变。Master路由器在发送VRRP通告报文时，将报文中的TTL值设置为255。如果配置备份组里的路由器检查VRRP报文的TTL域，则Backup路由器接收到TTL值小于255的VRRP通告报文时，将丢弃该报文，从而有效防止来自其他网段的攻击。

不同厂商的设备实现可能不同，在与其他厂商设备互通时，检查VRRP报文的TTL域可能导致错误地丢弃报文，这时可以通过**undo** **vrrp** **check-ttl** **enable**命令禁止检查VRRP报文的TTL域。

【举例】

·路由应用

\# 禁止检查IPv4 VRRP报文的TTL域。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo vrrp check-ttl enable

·交换应用

\# 禁止检查IPv4 VRRP报文的TTL域。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 undo vrrp check-ttl enable

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp dot1q**

------------------------------------------------------------------------

**[vrrp dot1q**]命令用来配置IPv4 VRRP的控制VLAN。

**[undo vrrp dot1q**]命令用来恢复缺省情况。

【命令】

**[vrrp dot1q vid ***vlan-id*]**** **secondary-dot1q** *secondary-**vlan-id *

**[undo vrrp dot1q**]

【缺省情况】

没有指定IPv4 VRRP的控制VLAN，即VLAN终结支持广播/组播功能后，Master在所有模糊终结的VLAN内发送VRRP通告报文。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vid ***vlan-id*]：指定IPv4 VRRP的控制VLAN（外层VLAN）的编号，*vlan-id*的取值范围为1～4094。

**[secondary-dot1q ***secondary-vlan-id*]：指定内层VLAN的编号，*secondary-vlan-id*的取值范围为1～4094。

【使用指导】

·重复执行本命令，新的配置将覆盖原有配置。

·只有在三层以太网子接口、三层聚合子接口和三层RPR逻辑接口下执行本命令才会生效；在其他接口视图下也可以执行本命令，但不会生效。

【举例】

\# 配置IPv4 VRRP的控制VLAN（外层VLAN）ID为2，内层VLAN ID为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.2

Sysname-GigabitEthernet1/0/1.2 vrrp dot1q vid 2 secondary-dot1q 100

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp dscp**

------------------------------------------------------------------------

**[vrrp dscp**]命令用来配置VRRP报文的DSCP优先级。

**[undo vrrp dscp**]命令用来恢复缺省值。

【命令】

**[vrrp dscp ***dscp-value*]

**[undo vrrp dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：VRRP报文的DSCP优先级，取值范围为0～63，缺省值为48。

【使用指导】

DSCP用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的VRRP报文中携带的DSCP优先级的取值。

【举例】

\# 配置VRRP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname vrrp dscp 30

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp mode**

------------------------------------------------------------------------

![说明](VRRP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vrrp mode**]命令用来配置IPv4 VRRP的工作模式。

**[undo vrrp mode**]命令用来恢复缺省情况。

【命令】

**[vrrp mode load-balance ** **version-8** ]

**[undo vrrp mode**]

【缺省情况】

IPv4 VRRP工作在标准协议模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[load-balance**]：指定IPv4 VRRP工作在负载均衡模式。

**[version-8**]：发送的协议报文携带的版本号为8。

【使用指导】

创建IPv4 VRRP备份组后，仍然可以修改IPv4 VRRP的工作模式。修改IPv4 VRRP的工作模式后，路由器上所有的IPv4 VRRP备份组都会工作在该模式。

只有接口配置的IPv4 VRRP使用的版本为VRRPv2时，指定**version-8**参数才会生效。若备份组满足以下所有条件时，需要配置**version-8**参数：

·备份组中存在使用ComwareV5版本软件的路由器；

·备份组中所有路由器的IPv4 VRRP均需要工作在负载均衡模式；

·备份组中所有路由器的IPv4 VRRP使用的版本均要配置为VRRPv2。

【举例】

\# 配置IPv4 VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp mode load-balance

【相关命令】

·**display** **vrrp**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp version**

------------------------------------------------------------------------

**[vrrp version**]命令用来配置接口下IPv4 VRRP使用的版本。

**[undo vrrp version**]命令用来恢复缺省情况。

【命令】

**[vrrp version ***version-number*]

**[undo vrrp version**]

【缺省情况】

IPv4 VRRP使用的版本为VRRPv3。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[version-number*]：VRRP协议的版本号，取值为2或3，其中2表示使用VRRPv2版本（RFC 3768），3表示使用VRRPv3版本（RFC 5798）。

【使用指导】

IPv4 VRRP备份组中的所有路由器上配置的IPv4 VRRP版本必须一致。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1上IPv4 VRRP使用的版本为VRRPv2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp version 2

·交换应用

\# 配置VLAN接口10上IPv4 VRRP使用的版本为VRRPv2。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 vrrp version 2

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid**

------------------------------------------------------------------------

**[vrrp vrid**]命令用来创建IPv4 VRRP备份组，并配置IPv4 VRRP备份组的虚拟IP地址，或为一个已经存在的IPv4 VRRP备份组添加一个虚拟IP地址。

**[undo vrrp vrid**]命令用来删除一个已经存在的IPv4 VRRP备份组的所有配置，或删除已经存在的IPv4 VRRP备份组中的虚拟IP地址。

【命令】

**[vrrp vrid***virtual-router-id*** virtual-ip** *virtual-address*]

**[undo vrrp vrid** *virtual-router-id* [ **virtual-ip** [ *virtual-address*  ]]]

【缺省情况】

未创建IPv4 VRRP备份组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

**[v**]**irtual-ip***virtual-address*：备份组的虚拟IP地址。不能为全零地址(0.0.0.0)、广播地址(255.255.255.255)、环回地址、非A/B/C类地址和其它非法IP地址(如0.0.0.1)。删除IPv4 VRRP备份组中的虚拟IP地址时，如果不指定*virtual-address*参数，则表示删除该备份组中的所有虚拟IP地址。

【使用指导】

·重复执行本命令，可以为IPv4 VRRP备份组配置多个虚拟IP地址，但每个备份组最多只能配置16个虚拟IP地址。

·如果没有为备份组配置虚拟IP地址，但是为备份组进行了其他配置（如优先级、抢占方式等），则该备份组会存在于设备上，并处于Inactive状态，此时备份组不起作用。

·建议将备份组的虚拟IP地址和备份组中设备下行接口的IP地址配置为同一网段，否则可能导致局域网内的主机无法访问外部网络。

·IPv4 VRRP工作在负载均衡模式时，要求备份组的虚拟IP地址和接口的IP地址不能相同。否则，IPv4 VRRP负载均衡功能将无法正常工作。

【举例】

·路由应用

\# 创建IPv4 VRRP备份组1，配置IPv4 VRRP备份组1的虚拟IP地址为10.10.10.10。为IPv4 VRRP备份组1添加一个虚拟IP地址10.10.10.11。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 10.10.10.10

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 virtual-ip 10.10.10.11

·交换应用

\# 创建IPv4 VRRP备份组1，配置IPv4 VRRP备份组1的虚拟IP地址为10.10.10.10。为IPv4 VRRP备份组1添加一个虚拟IP地址10.10.10.11。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 virtual-ip 10.10.10.10

Sysname-Vlan-interface2 vrrp vrid 1 virtual-ip 10.10.10.11

【相关命令】

·**display** **vrrp**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid authentication-mode**

------------------------------------------------------------------------

**[vrrp vrid authentication-mode**]命令用来配置备份组发送和接收IPv4 VRRP报文的认证方式和认证字。

**[undo vrrp vrid authentication-mode**]命令用来恢复缺省情况。

【命令】

**[vrrp vrid**[ *virtual-router-id* **authentication-mode** { **md5** \| **simple** } { **cipher** \| **plain** } *key*]]

**[undo vrrp vrid** *virtual-router-id* **authentication-mode**]

【缺省情况】

备份组发送和接收IPv4 VRRP报文时不进行认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

**[md5**]：表示使用MD5算法进行认证。

**[simple**]：表示使用简单字符进行认证。

**[cipher**]：表示以密文方式设置认证字。

**[plain**]：表示以明文方式设置认证字。

*[key*]：认证字，区分大小写。

·采用**md5**认证方式，当使用**cipher**参数时，*key*为1～41个字符的密文认证字；当使用**plain**参数时，*key*为1～8个字符的明文认证字。

·采用**simple**认证方式，当使用**cipher**参数时，*key*为1～41个字符的密文认证字；当使用**plain**参数时，*key*为1～8个字符的明文认证字。

【使用指导】

为了防止非法用户构造报文攻击备份组，VRRP通过在VRRP报文中增加认证字的方式，验证接收到的VRRP报文。VRRP提供了两种认证方式：

·**simple**：简单字符认证。发送VRRP报文的路由器将认证字填入到VRRP报文中，而收到VRRP报文的路由器会将收到的VRRP报文中的认证字和本地配置的认证字进行比较。如果认证字相同，则认为接收到的报文是真实、合法的VRRP报文；否则认为接收到的报文是一个非法报文。

·**md5**：MD5认证。发送VRRP报文的路由器利用认证字和MD5算法对VRRP报文进行摘要运算，运算结果保存在Authentication Header（认证头）中。收到VRRP报文的路由器会利用认证字和MD5算法进行同样的运算，并将运算结果与认证头的内容进行比较。如果相同，则认为接收到的报文是真实、合法的VRRP报文；否则认为接收到的报文是一个非法报文。

MD5认证比简单字符认证更安全，但是MD5认证需要进行额外的运算，占用的系统资源较多。

以明文或密文方式设置的验证字，均以密文的方式保存在配置文件中。

需要注意的是：

·一个接口上的不同备份组可以设置不同的认证方式和认证字；加入同一备份组的成员需要设置相同的认证方式和认证字。

·使用VRRPv3版本的IPv4 VRRP不支持认证。使用VRRPv3版本时，此配置不会生效。

【举例】

·路由应用

\# 设置GigabitEthernet1/0/1接口上备份组1发送和接收IPv4 VRRP报文的认证方式为**simple**，认证字为Sysname。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 authentication-mode simple plain Sysname

·交换应用

\# 设置VLAN接口2上备份组1发送和接收IPv4 VRRP报文的认证方式为**simple**，认证字为Sysname。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 authentication-mode simple plain Sysname

【相关命令】

·**display** **vrrp**

·**vrrp** **version**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid preempt-mode**

------------------------------------------------------------------------

**[vrrp vrid preempt-mode**]命令用来设置IPv4 VRRP备份组中的路由器工作在抢占方式，并配置抢占延迟时间。

**[undo vrrp vrid preempt-mode**]命令用来取消抢占方式，即设置IPv4 VRRP备份组中的路由器工作在非抢占方式。

**[undo vrrp vrid preempt-mode delay**]命令用来恢复抢占延迟时间为缺省值。

【命令】

**[vrrp vrid ***virtual-router-id*** preempt-mode** [ **delay** *delay-value* ]]

**[undo** **vrrp vrid** *virtual-router-id* **preempt-mode** [ **delay** ]]

【缺省情况】

IPv4 VRRP备份组中的路由器工作在抢占方式下，抢占延迟时间为0厘秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

**[delay*** delay-value*]：抢占延迟时间。*delay-value*取值范围为0～180000，单位为厘秒，缺省值为0厘秒。

【使用指导】

·如果备份组中的路由器工作在非抢占方式下，则只要Master路由器没有出现故障，Backup路由器即使随后被配置了更高的优先级也不会成为Master路由器。非抢占方式可以避免频繁地切换Master路由器。

·如果备份组中的路由器工作在抢占方式下，它一旦发现自己的优先级比当前的Master路由器的优先级高，就会对外发送VRRP通告报文。导致备份组内路由器重新选举Master路由器，并最终取代原有的Master路由器。相应地，原来的Master路由器将会变成Backup路由器。抢占方式可以确保承担转发任务的Master路由器始终是备份组中优先级最高的设备。

·为了避免备份组内的成员频繁进行主备状态转换，让Backup路由器有足够的时间搜集必要的信息（如路由信息），Backup路由器接收到优先级低于本地优先级的通告报文后，不会立即抢占成为Master路由器，而是等待一定时间后，才会重新选举新的Master路由器。

【举例】

·路由应用

\# 配置接口GigabitEthernet1/0/1工作在抢占方式，抢占延迟时间为5000厘秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 preempt-mode delay 5000

·交换应用

\# 配置VLAN接口2工作在抢占方式，抢占延迟时间为5000厘秒。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 preempt-mode delay 5000

【相关命令】

·**display** **vrrp**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid priority**

------------------------------------------------------------------------

**[vrrp vrid priority**]命令用来设置路由器在IPv4 VRRP备份组中的优先级。

**[undo vrrp vrid priority**]命令用来恢复缺省情况。

【命令】

**[vrrp vrid*** virtual-router-id* **priority** *priority-value*]

**[undo vrrp vrid** *virtual-router-id* **priority**]

【缺省情况】

路由器在IPv4 VRRP备份组中的优先级为100。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

*[priority-value*]：优先级的值，取值范围为1～254，该值越大表明优先级越高。

【使用指导】

优先级决定了路由器在备份组中的地位。优先级越高，越有可能成为Master路由器。优先级0是系统保留为特殊用途来使用的，255则是系统保留给IP地址拥有者的。

路由器为IP地址拥有者时，其运行优先级始终为255，表明只要其工作正常，则为Master路由器。

【举例】

·路由应用

\# 设置路由器在IPv4 VRRP备份组1中的优先级为150。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 priority 150

·交换应用

\# 设置交换机在IPv4 VRRP备份组1中的优先级为150。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 priority 150

【相关命令】

·**display** **vrrp**

·**vrrp** **vrid** **track**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid shutdown**

------------------------------------------------------------------------

**[vrrp vrid shutdown**]命令用来关闭指定的IPv4 VRRP备份组。

**[undo vrrp vrid shutdown**]命令用来恢复缺省情况。

【命令】

**[vrrp vrid*** virtual-router-id* **shutdown**]

**[undo vrrp vrid** *virtual-router-id* **shutdown**]

【缺省情况】

IPv4 VRRP备份组处于开启状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

【使用指导】

关闭IPv4 VRRP备份组功能通常用于暂时禁用备份组，但还需要再次启用该备份组的场景。关闭备份组后，该备份组的状态为Initialize，并且该备份组所有已存在的配置保持不变。在关闭状态下还可以对备份组进行配置。备份组再次被开启后，基于最新的配置，从Initialize状态重新开始运行。

【举例】

·路由应用

\# 关闭IPv4 VRRP备份组1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 shutdown

·交换应用

\# 关闭IPv4 VRRP备份组1。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 shutdown

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid source-interface**

------------------------------------------------------------------------

**[vrrp vrid source-interface**]命令用来为IPv4 VRRP备份组指定源接口，该源接口用来代替IPv4 VRRP备份组所在接口进行该备份组VRRP报文的收发。

**[undo vrrp vrid source-interface**]命令用来取消当前指定的源接口，VRRP报文通过IPv4 VRRP备份组所在接口进行收发。

【命令】

**[vrrp vrid** *virtual-router-id* **source-interface** *interface-type* *interface-number*]

**[undo vrrp vrid ***virtual-router-id* **source-interface**]

【缺省情况】

没有指定备份组的源接口，VRRP报文通过IPv4 VRRP备份组所在接口进行收发。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

*[interface-type interface-number*]：源接口的接口类型和接口编号。

【使用指导】

因组网要求或网络故障，导致同一个IPv4 VRRP备份组中的设备不能通过备份组所在接口进行VRRP协议报文交互时，可以使用本命令将其他能进行报文交互的接口设置为备份组源接口，用来代替备份组所在接口进行该备份组VRRP报文的收发。

【举例】

·路由应用

\# 设置接口GigabitEthernet1/0/1上备份组的源接口为接口GigabitEthernet1/0/2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 10 source-interface gigabitethernet 1/0/2

·交换应用

\# 设置VLAN接口10上备份组的源接口为VLAN接口20。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 vrrp vrid 10 source-interface vlan-interface 20

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid timer advertise**

------------------------------------------------------------------------

**[vrrp vrid timer advertise**]命令用来设置IPv4 VRRP备份组中的Master路由器发送VRRP通告报文的时间间隔。

**[undo vrrp vrid timer advertise**]命令用来恢复缺省情况。

【命令】

**[vrrp vrid ***virtual-router-id*** timer advertise ***adver-interval*]

**[undo vrrp vrid ***virtual-router-id*** timer advertise**]

【缺省情况】

IPv4 VRRP备份组中Master路由器发送VRRP通告报文的时间间隔为100厘秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

*[adver-interval*]：备份组中的Master路由器发送VRRP通告报文的间隔时间，取值范围为10～4095，单位为厘秒。使用VRRPv2版本时，该参数的实际生效值只能是100的整倍数，例如，配置该参数取值在10～100、101～200、4001～4095范围内时，实际生效值分别为100、200、4100；使用VRRPv3版本时，该参数的实际生效值与所配置数值相同。

【使用指导】

IPv4 VRRP备份组中的Master路由器会定时发送VRRP通告报文，通知备份组内的路由器自己工作正常。VRRP通告报文的发送时间间隔为本命令配置的值。

需要注意的是：

·建议配置VRRP通告报文的发送间隔大于100厘秒，否则会对系统的稳定性产生影响。

·使用VRRPv2版本时，IPv4 VRRP备份组中的所有路由器必须配置相同的VRRP通告报文时间间隔。

·使用VRRPv3版本时，IPv4 VRRP备份组中的路由器上配置的VRRP通告报文时间间隔可以不同。Master路由器根据自身配置的报文时间间隔定时发送通告报文，并在通告报文中携带Master路由器上配置的时间间隔；Backup路由器接收到Master路由器发送的通告报文后，记录报文中携带的Master路由器通告报文时间间隔，如果在3×记录的时间间隔＋Skew_Time内没有收到Master路由器发送的VRRP通告报文，则认为Master路由器出现故障，重新选举Master路由器。

·网络流量过大可能会导致Backup路由器在指定时间内没有收到Master路由器的VRRP通告报文，从而发生状态转换。可以通过将VRRP通告报文的发送时间间隔延长的办法来解决该问题。

【举例】

·路由应用

\# 设置IPv4 VRRP备份组1的Master路由器发送VRRP通告报文的间隔时间为500厘秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 timer advertise 500

·交换应用

\# 设置IPv4 VRRP备份组1的Master路由器发送VRRP通告报文的间隔时间为500厘秒。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 timer advertise 500

【相关命令】

·**display** **vrrp**

**VRRP \-- IPv4 VRRP配置命令 \-- vrrp vrid track**

------------------------------------------------------------------------

![说明](VRRP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[vrrp vrid track**]命令用来配置监视指定的Track项，即当Track项的状态为Negative时，立即将虚拟转发器切换为Active状态、降低路由器的优先级、立即切换成为Master路由器或降低本地虚拟转发器权重值。

**[undo vrrp vrid track**]命令用来取消监视指定的Track项。

【命令】

**[vrrp vrid**[ *virtual-router-id* **track** *track-entry-number* { **forwarder-switchover** **member-ip** *ip-address* \| **priority reduced** [ *priority-reduced* ] \| **switchover** \| **weight reduced**  *weight-reduced*  }]]

**[undo vrrp vrid** *virtual-router-id* **track** [ *track-entry-number*  [ **forwarder-switchover** \| **priority reduced** \| **switchover** \| **weight reduced** ]]]

【缺省情况】

没有指定被监视的Track项。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv4 VRRP备份组号，取值范围为1～255。

*[track-entry-number*]：被监视的Track项序号，*track-entry-number*取值范围为1～1024。

**[forwarder-switchover** **member-ip** *ip-address*]：虚拟转发器快速切换模式。当监视的Track项状态变为Negative时，如果本地设备上有处于Listening状态的虚拟转发器，且其对应的AVF地址为**member-ip**，则马上将该虚拟转发器切换到Active状态。*ip-address*为备份组中成员设备的IP地址。可以通过**display vrrp verbose**命令查看备份组中包含的成员设备。

**[priority reduced** [ *priority-reduced* ]]：当监视的Track项状态变为Negative时，降低本地路由器在备份组中的优先级。优先级降低的数值为*priority-reduced*，*priority-reduced*的取值范围为1～255，缺省值为10。

**[switchover**]：切换模式，当监视的Track项的状态变为Negative时，如果本路由器在备份组中处于Backup状态，则马上切换成为Master路由器。

**[weight reduced ** *weight-reduced* ]：当监视的Track项状态变为Negative时，当前路由器上属于指定IPv4 VRRP组的所有虚拟转发器的权重都降低指定的数值。权重降低的数值为*weight-reduced*，*weight-reduced*的取值范围为1～255，缺省值为30。

【使用指导】

需要注意的是：

·在执行本配置之前，需要先在接口上创建备份组并配置虚拟IP地址。

·执行**undo vrrp vrid track**命令时如果没有指定*track-entry-number*参数，则删除该备份组与所有Track项的关联。

·只有VRRP工作在负载均衡模式时，执行**forwarder-switchover** **member-ip** *ip-address*或**weight reduced ** *weight-reduced* 才会生效。

·虚拟转发器的权重值为255，虚拟转发器的失效下限为10。

·由于VF Owner的权重高于或等于失效下限时，它的优先级始终为255，不会根据虚拟转发器的权重改变。当监视的上行接口出现故障时，配置的权重降低数额需保证VF Owner的权重低于失效下限，即权重降低的数额大于245，其他的虚拟转发器才能接替VF Owner成为AVF。

·路由器在某个备份组中作为IP地址拥有者时，如果在该路由器上执行**vrrp vrid track priority reduced**或**vrrp vrid track switchover**命令，则该配置不会生效。该路由器不再作为IP地址拥有者后，之前的配置才会生效。

·被监视的Track项的状态由Negative变为Positive或NotReady后，对应的路由器优先级会自动恢复、对应虚拟转发器的权重会自动恢复、故障恢复后的原Master路由器会重新抢占为Master状态、故障恢复后的原AVF会重新抢占为Active状态。

·被监视的Track项可以是未创建的Track项。可以通过**vrrp vrid track**命令指定监视的Track项后，再通过**track**命令创建该Track项。

Track项的详细介绍请参见"可靠性配置指导"中的"Track"。

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上配置监视Track项1，当Track项1状态为Negative时，GigabitEthernet1/0/1接口上备份组1的优先级降低50。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 track 1 priority reduced 50

\# 在GigabitEthernet1/0/1接口上配置虚拟转发器监视Track项1，当Track项1状态为Negative时，如果本地设备上AVF地址为10.1.1.3的虚拟转发器处于Listening状态，则马上将该虚拟转发器切换到Active状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 track 1 forwarder-switchover member-ip 10.1.1.3

\# 在GigabitEthernet1/0/1接口上配置虚拟转发器权重监视Track项1，当Track项1状态为Negative时，GigabitEthernet1/0/1接口上IPv4 VRRP备份组1所有虚拟转发器的权重都降低50。

\<Sysname\> sysname-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp vrid 1 track 1 weight reduced 50

·交换应用

\# 在VLAN接口2上配置监视Track项1，当Track项1状态为Negative时，VLAN接口2上备份组1的优先级降低50。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 track 1 priority reduced 50

\# 在VLAN接口2上配置虚拟转发器监视Track项1，当Track项1状态为Negative时，如果本地设备上AVF地址为10.1.1.3的虚拟转发器处于Listening状态，则马上将该虚拟转发器切换到Active状态。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 track 1 forwarder-switchover member-ip 10.1.1.3

\# 在VLAN接口2上配置虚拟转发器权重监视Track项1，当Track项1状态为Negative时，VLAN接口2上IPv4 VRRP备份组1所有虚拟转发器的权重都降低50。

\<Sysname\> sysname-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp vrid 1 track 1 weight reduced 50

【相关命令】

·**display** **vrrp**

**VRRP \-- IPv6 VRRP配置命令 \-- display vrrp ipv6**

------------------------------------------------------------------------

**[display** **vrrp ipv6**]命令用来显示IPv6 VRRP备份组的状态信息。

【命令】

**[display** **vrrp ipv6** [ **interface** *interface-type interface-number* [ **vrid** *virtual-router-id*  ]  **verbose**  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的IPv6 VRRP备份组状态信息。其中，*interface-type* *interface-number*为接口类型和接口编号。

**[vrid ***virtual-router-id*]：显示指定IPv6 VRRP备份组的状态信息。其中，*virtual-router-id*为IPv6 VRRP备份组号，取值范围为1～255。

**[verbose**]：显示IPv6 VRRP备份组状态的详细信息。如果不指定本参数，则显示IPv6 VRRP备份组状态的简要信息。

【使用指导】

如果不指定接口名和备份组号，则显示该路由器上所有IPv6 VRRP备份组的状态信息；如果只指定接口名，不指定备份组号，则显示该接口上的所有IPv6 VRRP备份组的状态信息；如果同时指定接口名和备份组号，则显示该接口上指定IPv6 VRRP备份组的状态信息。

【举例】

\# VRRP工作在标准协议模式时，显示全部IPv6 VRRP备份组的简要信息。

\<Sysname\> display vrrp ipv6

IPv6 Virtual Router Information:

 Running Mode      : Standard

 Total number of virtual routers : 1

 Interface          VRID  State        Running Adver   Auth     Virtual

                                       Pri     Timer   Type        IP

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 GE1/0/1            1     Master       150     100     None     FE80::1

表1-7 display vrrp ipv6命令显示信息描述表（标准协议模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Standard（标准协议模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Running Pri

路由器的运行优先级，即路由器当前的优先级。配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Auth Type

认证类型，取值只能是None，表示无认证

Virtual IP

备份组的虚拟IP地址

\# VRRP工作在标准协议模式时，显示全部IPv6 VRRP备份组的详细信息。

\<Sysname\> display vrrp ipv6 verbose

IPv6 Virtual Router Information:

 Running Mode      : Standard

 Total number of virtual routers : 2

   Interface GigabitEthernet1/0/1

     VRID           : 1                    Adver Timer  : 100

     Admin Status   : Up                   State        : Master

     Config Pri     : 150                  Running Pri  : 150

     Preempt Mode   : Yes                  Delay Time   : 10

     Auth Type      : None

     Virtual IP     : FE80::1

     Virtual MAC    : 0000-5e00-0201

     Master IP      : FE80::2

   VRRP Track Information:

     Track Object   : 1                    State : Positive   Pri Reduced : 50

   Interface GigabitEthernet1/0/1

     VRID           : 11                   Adver Timer  : 100

     Admin Status   : Up                   State        : Backup

     Config Pri     : 80                   Running Pri  : 80

     Preempt Mode   : Yes                  Delay Time   : 0

     Become Master  : 2450ms left

     Auth Type      : None

     Virtual IP     : FE80::11

     Virtual MAC    : 0000-5e00-020b

     Master IP      : FE80::12

表1-8 display vrrp ipv6 verbose命令显示信息描述表（标准协议模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Standard（标准协议模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Admin Status

管理状态，包括Up和Down两种状态

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Config Pri

路由器的配置优先级，即通过**vrrp ipv6 vrid priority**命令指定的路由器优先级

Running Pri

路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Preempt Mode

抢占模式，取值包括：

·Yes：路由器工作在抢占模式

·No：路由器工作在非抢占模式

Become Master

切换到Master状态需要等待的时间，单位为毫秒，只有处于Backup状态时才会显示此信息

Delay Time

抢占延迟时间，单位为厘秒

Auth Type

认证类型，取值只能是None，表示无认证

Virtual IP

备份组的虚拟IP地址

Virtual MAC

备份组虚拟IP地址对应的虚拟MAC地址。只在路由器为Master状态时，才会显示此信息

Master IP

处于Master状态的路由器所对应接口的链路本地地址

VRRP Track Information

VRRP备份组监视的Track项信息。执行**vrrp ipv6 vrid track**命令后，才会显示此信息

Track Object

监视的Track项

State

Track项的状态，Track项的状态可包括Negative、Positive和NotReady

Pri Reduced

监视的Track项状态为Negative时，优先级降低的数额

Switchover

快速切换，显示此信息时表示当监视的Track项变为Negative状态时，Backup路由器会马上抢占成为Master路由器

\# VRRP工作在负载均衡模式时，显示全部IPv6 VRRP备份组的简要信息。

\<Sysname\> display vrrp ipv6

IPv6 Virtual Router Information:

 Running Mode      : Load Balance

 Total number of virtual routers : 1

 Interface          VRID  State        Running Address             Active

                                       Pri

 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

 GE1/0/1            1     Master       150     FE80::1             Local

 \-\-\-\--              VF 1  Active       255     000f-e2ff-4011      Local

表1-9 display vrrp ipv6命令显示信息描述表（负载均衡模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Load Balance（负载均衡模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）*number*或虚拟转发器编号VF *number*

State

对于虚拟备份组（VRID为*number*），该字段表示当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的状态，取值为Active、Listening或Initialize

Running Pri

对于虚拟备份组（VRID为*number*），该字段表示路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的运行优先级，即虚拟转发器当前的优先级，配置监视指定Track项后，虚拟转发器的优先级会根据Track项的状态改变

Address

对于虚拟备份组（VRID为*number*），该字段表示备份组的虚拟IP地址

对于虚拟转发器（VRID为VF *number*），该字段表示虚拟转发器的虚拟MAC地址

Active

对于虚拟备份组（VRID为*number*），该字段表示Master的接口的链路本地地址，当前路由器为Master时，显示为local

对于虚拟转发器（VRID为VF *number*），该字段表示AVF的接口的链路本地地址，当前虚拟转发器为AVF时，显示为local

\# VRRP工作在负载均衡模式时，显示全部IPv6 VRRP备份组的详细信息。

\<Sysname\> display vrrp ipv6 verbose

IPv6 Virtual Router Information:

 Running Mode      : Load Balance

 Total number of virtual routers : 2

   Interface GigabitEthernet1/0/1

     VRID           : 1                    Adver Timer  : 100

     Admin Status   : Up                   State        : Master

     Config Pri     : 150                  Running Pri  : 150

     Preempt Mode   : Yes                  Delay Time   : 5

     Auth Type      : None

     Virtual IP     : FE80::10

     Member IP List : FE80::3 (Local, Master)

                      FE80::2 (Backup)

     Master IP      : FE80::3

   VRRP Track Information:

     Track Object   : 1                    State : Positive   Pri Reduced : 50

   Forwarder Information: 2 Forwarders 1 Active

     Config Weight  : 255

     Running Weight : 255

    Forwarder 01

     State          : Active

     Virtual MAC    : 000f-e2ff-4011 (Owner)

     Owner ID       : 0000-5e01-1101

     Priority       : 255

     Active         : local

    Forwarder 02

     State          : Listening

     Virtual MAC    : 000f-e2ff-4012 (Learnt)

     Owner ID       : 0000-5e01-1103

     Priority       : 127

     Active         : FE80::2

   Forwarder Weight Track Information:

     Track Object   : 1          State : Positive   Weight Reduced : 250

   Interface GigabitEthernet1/0/1

     VRID           : 11                   Adver Timer  : 100

     Admin Status   : Up                   State        : Backup

     Config Pri     : 80                   Running Pri  : 80

     Preempt Mode   : Yes                  Delay Time   : 0

     Become Master  : 2450ms left

     Auth Type      : None

     Virtual IP     : FE80::11

     Member IP List : FE80::3 (Local, Backup)

                      FE80::2 (Master)

     Master IP      : FE80::2

   Forwarder Information: 2 Forwarders 1 Active

     Config Weight  : 255

     Running Weight : 255

    Forwarder 01

     State          : Active

     Virtual MAC    : 000f-e2ff-40b1 (Learnt)

     Owner ID       : 0000-5e01-1103

     Priority       : 127

     Active         : FE80::2

    Forwarder 02

     State          : Listening

     Virtual MAC    : 000f-e2ff-40b2 (Owner)

     Owner ID       : 0000-5e01-1101

     Priority       : 255

     Active         : local

表1-10 display vrrp ipv6 verbose命令显示信息描述表（负载均衡模式）

字段

描述

Running Mode

VRRP的工作模式，取值为Load Balance（负载均衡模式）

Total number of virtual routers

备份组的数目

Interface

备份组所在接口名

VRID

虚拟路由器号（即备份组号）

Adver Timer

VRRP通告报文发送时间间隔，单位为厘秒

Admin Status

管理状态，包括Up和Down两种状态

State

当前路由器在备份组中的状态，取值为Master，Backup，Initialize或Inactive

Config Pri

路由器的配置优先级，即通过**vrrp ipv6 vrid priority**命令指定的路由器优先级

Running Pri

路由器的运行优先级，即路由器当前的优先级，配置监视指定Track项后，路由器的优先级会根据Track项的状态改变

Preempt Mode

抢占模式，取值包括：

·Yes：路由器工作在抢占模式

·No：路由器工作在非抢占模式

Delay Time

抢占延迟时间，单位为厘秒

Become Master

切换到Master状态需要等待的时间，单位为毫秒，只有处于Backup状态时才会显示此信息

Auth Type

认证类型，取值只能是None，表示无认证

Virtual IP

备份组的虚拟IP地址列表

Member IP List

备份组中成员设备的IP地址列表：

·Local：表示本地设备的IP地址

·Master：表示处于Master状态的成员设备的IP地址

·Backup：表示处于Backup状态的成员设备的IP地址

VRRP Track Information

VRRP备份组监视的Track项信息，执行**vrrp ipv6 vrid track**命令后，才会显示此信息

Track Object

监视的Track项，执行**vrrp ipv6 vrid track**命令后，才会显示此信息

State

Track项的状态，Track项的状态包括Negative、Positive和NotReady

Pri Reduced

监视的Track项状态为Negative时，优先级降低的数额，执行**vrrp ipv6 vrid track**命令后，才会显示此信息

Switchover

快速切换，显示此信息时表示当监视的Track项变为Negative状态时，Backup路由器会马上抢占成为Master路由器

Forwarder Information: 2 Forwarders 1 Active

虚拟转发器信息：路由器的虚拟转发器数目为2，处于Active状态的虚拟转发器数目为1

Config Weight

虚拟转发器的配置权重，取值为255

Running Weight

虚拟转发器的运行权重，即虚拟转发器当前的权重，配置监视指定Track项后，虚拟转发器的权重会根据Track项的状态改变

Forwarder 01

虚拟转发器01的信息

State

虚拟转发器的状态，取值为Active、Listening或Initialize

Virtual MAC

虚拟转发器的虚拟MAC地址

Owner ID

虚拟转发器拥有者的接口实际MAC地址

Priority

虚拟转发器的优先级，取值范围为1～255

Active

AVF的接口的链路本地地址，当前转发器为AVF时，显示为local

Forwarder Weight Track Configuration

虚拟转发器权重监视配置信息。执行**vrrp ipv6 vrid weight** **track**命令后，才会显示此信息

Track Object

权重监视的Track项。执行**vrrp ipv6 vrid weight** **track**命令后，才会显示此信息

State

Track项的状态，Track项的状态包括Negative、Positive和NotReady

Weight Reduced

监视的Track项状态为Negative时，权重降低的数额。执行**vrrp ipv6 vrid weight** **track**命令后，才会显示此信息

**VRRP \-- IPv6 VRRP配置命令 \-- display vrrp ipv6 statistics**

------------------------------------------------------------------------

**[display vrrp ipv6 statistics**]命令用来显示IPv6 VRRP备份组的统计信息。

【命令】

**[display vrrp ipv6******statistics**** **interface** *interface-type interface-number*  **vrid** *virtual-router-id*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：显示指定接口的IPv6 VRRP备份组的统计信息。其中，*interface-type* *interface-number*为接口类型和接口编号。

**[vrid** *virtual-router-id*]：显示指定备份组号的IPv6 VRRP备份组统计信息，其中，*virtual-router-id*为IPv6 VRRP备份组号，取值范围为1～255。

【使用指导】

如果不输入接口名和备份组号，则显示该路由器上所有IPv6 VRRP备份组的统计信息；如果只输入接口名，不输入备份组号，则显示该接口上的所有IPv6 VRRP备份组的统计信息；如果同时输入接口名和备份组号，则显示该接口上指定IPv6 VRRP备份组的统计信息。

【举例】

\# VRRP工作在标准协议模式时，显示所有IPv6 VRRP备份组的统计信息。

\<Sysname\> display vrrp ipv6 statistics

 Interface               : GigabitEthernet1/0/1

 VRID                    : 1

 CheckSum Errors         : 0          Version Errors                : 0

 Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0

 Hop Limit Errors        : 0          Advertisement Interval Errors : 0

 Invalid Auth Type       : 0          Auth Failures                 : 0

 Packet Length Errors    : 0          Auth Type Mismatch            : 0

 Become Master           : 1          Address List Errors           : 0

 Adver Rcvd              : 0          Priority Zero Pkts Rcvd       : 0

 Adver Sent              : 425        Priority Zero Pkts Sent       : 0

 Global statistics

 CheckSum Errors         : 0

 Version Errors          : 0

 VRID Errors             : 0

\# VRRP工作在负载均衡模式时，显示全部IPv6 VRRP备份组的统计信息。

\<Sysname\> display vrrp ipv6 statistics

 Interface               : GigabitEthernet1/0/1

 VRID                    : 1

 CheckSum Errors         : 0          Version Errors                : 0

 Invalid Pkts Rcvd       : 0          Unexpected Pkts Rcvd          : 0

 Hop Limit Errors        : 0          Advertisement Interval Errors : 0

 Invalid Auth Type       : 0          Auth Failures                 : 0

 Packet Length Errors    : 0          Auth Type Mismatch            : 0

 Become Master           : 39         Address List Errors           : 0

 Become AVF              : 13         Packet Option Errors          : 0

 Adver Rcvd              : 2562       Priority Zero Pkts Rcvd       : 1

 Adver Sent              : 16373      Priority Zero Pkts Sent       : 49

 Request Rcvd            : 2          Reply Rcvd                    : 10

 Request Sent            : 12         Reply Sent                    : 2

 Release Rcvd            : 0          VF Priority Zero Pkts Rcvd    : 1

 Release Sent            : 0          VF Priority Zero Pkts Sent    : 11

 Redirect Timer Expires  : 1          Time-out Timer Expires        : 0

 Global statistics

 CheckSum Errors         : 0

 Version Errors          : 0

 VRID Errors             : 0

表1-11 display vrrp ipv6 statistics显示信息描述表（标准协议模式）

字段

描述

Interface

备份组所在接口

VRID

备份组号

CheckSum Errors

校验和错误的报文数

Version Errors

版本号错误的报文数

Invalid Pkts Rcvd

接收到报文类型错误的报文数

Unexpected Pkts Rcvd

接收到未期望的报文数

Advertisement Interval Errors

VRRP通告报文发送时间间隔错误的报文数

Hop Limit Errors

跳数限制错误的报文数

Auth Failures

认证失败的报文数

Invalid Auth Type

认证类型无效的报文数

Auth Type Mismatch

认证类型不匹配的报文数

Packet Length Errors

VRRP报文长度错误的报文数

Address List Errors

备份组虚拟IP地址列表错误的报文数

Become Master

成为Master路由器的次数

Priority Zero Pkts Rcvd

收到的优先级为0的VRRP通告报文的数目

Adver Rcvd

收到的VRRP通告报文的数目

Priority Zero Pkts Sent

发送的优先级为0的VRRP通告报文的数目

Adver Sent

发送的VRRP通告报文的数目

Global statistics

所有备份组的全局统计信息

CheckSum Errors

校验和错误的报文总数

Version Errors

版本号错误的报文总数

VRID Errors

备份组号错误的报文总数

表1-12 display vrrp ipv6 statistics显示信息描述表（负载均衡模式）

字段

描述

Interface

备份组所在接口

VRID

备份组号

CheckSum Errors

校验和错误的报文数

Version Errors

版本号错误的报文数

Invalid Pkts Rcvd

接收到报文类型错误的报文数

Unexpected Pkts Rcvd

接收到未期望的报文数

Advertisement Interval Errors

VRRP通告报文发送时间间隔错误的报文数

Hop Limit Errors

跳数限制错误的报文数

Auth Failures

认证错误的报文数

Invalid Auth Type

认证类型无效的报文数

Auth Type Mismatch

认证类型不匹配的报文数

Packet Length Errors

VRRP报文长度错误的报文数

Address List Errors

虚拟IP地址列表错误的报文数

Become Master

成为Master路由器的次数

Redirect Timer Expires

Redirect Timer超时的次数

Become AVF

成为AVF的次数

Time-out Timer Expires

Time-out Timer超时的次数

Adver Rcvd

收到的Advertisement报文的数目

Request Rcvd

收到的Request报文的数目

Adver Sent

发送的Advertisement报文的数目

Request Sent

发送的Request报文的数目

Reply Rcvd

收到的Reply报文的数目

Release Rcvd

收到的Release报文的数目

Reply Sent

发送的Reply报文的数目

Release Sent

发送的Release报文的数目

Priority Zero Pkts Rcvd

收到的路由器优先级为0的Advertisement报文的数目

VF Priority Zero Pkts Rcvd

收到的虚拟转发器优先级为0的Advertisement报文的数目

Priority Zero Pkts Sent

发送的路由器优先级为0的Advertisement报文的数目

VF Priority Zero Pkts Sent

发送的虚拟转发器优先级为0的Advertisement报文的数目

Packet Option Errors

报文状态选项错误的次数

Global statistics

所有备份组的全局统计信息

CheckSum Errors

校验和错误的报文总数

Version Errors

版本号错误的报文总数

VRID Errors

备份组号错误的报文总数

【相关命令】

·**reset vrrp ipv6 statistics**

**VRRP \-- IPv6 VRRP配置命令 \-- reset vrrp ipv6 statistics**

------------------------------------------------------------------------

**[reset vrrp ipv6 statistics**]命令用来清除IPv6 VRRP备份组的统计信息。

【命令】

**[reset vrrp ipv6 statistics ** **interface** *interface-type interface-number*  **vrid** *virtual-router-id*  ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：清除指定接口的IPv6 VRRP备份组统计信息。其中，*interface-type interface-number*为接口类型和接口编号。

**[vrid** *virtual-router-id*]：清除指定备份组的IPv6 VRRP统计信息。其中，*virtual-router-id*为IPv6 VRRP备份组号，取值范围为1～255。

【使用指导】

在清除IPv6 VRRP备份组统计信息时，如果不输入接口名和备份组号，则清除该路由器上所有IPv6 VRRP备份组的统计信息；如果只输入接口名，不输入备份组号，则清除该接口上所有IPv6 VRRP备份组的统计信息；如果同时输入接口名和备份组号，则清除该接口上指定IPv6 VRRP备份组的统计信息。

【举例】

\# 清除所有接口上所有备份组的IPv6 VRRP统计信息。

\<Sysname\> reset vrrp ipv6 statistics

【相关命令】

·**display vrrp ipv6******statistics**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 dot1q**

------------------------------------------------------------------------

**[vrrp ipv6 dot1q**]命令用来配置IPv6 VRRP的控制VLAN。

**[undo vrrp ipv6 dot1q**]命令用来恢复缺省情况。

【命令】

**[vrrp ipv6 dot1q vid ***vlan-id*]**** **secondary-dot1q** *secondary-**vlan-id *

**[undo vrrp ipv6 dot1q**]

【缺省情况】

没有指定IPv6 VRRP的控制VLAN，即VLAN终结支持广播/组播功能后，Master在所有模糊终结的VLAN内发送IPv6 VRRP通告报文。

【视图】

三层以太网子接口视图/三层聚合子接口视图/三层RPR逻辑接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vid ***vlan-id*]：指定IPv6 VRRP的控制VLAN（外层VLAN）的编号，*vlan-id*的取值范围为1～4094。

**[secondary-dot1q ***secondary-vlan-id*]：指定内层VLAN的编号，*secondary-vlan-id*的取值范围为1～4094。

【使用指导】

·重复执行本命令，新的配置将覆盖原有配置。

·只有在三层以太网子接口、三层聚合子接口和三层RPR逻辑接口视图下执行本命令才会生效；在其他接口视图下也可以执行本命令，但不会生效。

【举例】

\# 配置IPv6 VRRP的控制VLAN（外层VLAN）ID为2，内层VLAN ID为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1.2

Sysname-GigabitEthernet1/0/1.2 vrrp ipv6 dot1q vid 2 secondary-dot1q 100

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 dscp**

------------------------------------------------------------------------

**[vrrp ipv6 dscp**]命令用来配置IPv6 VRRP发送报文的DSCP优先级。

**[undo vrrp ipv6 dscp**]命令用来恢复缺省值。

【命令】

**[vrrp ipv6 dscp ***dscp-value*]

**[undo vrrp ipv6 dscp**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：IPv6 VRRP报文的DSCP优先级，取值范围为0～63，缺省值为56。

【使用指导】

DSCP用来体现报文自身的优先等级，决定报文传输的优先程度。配置的DSCP优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的IPv6 VRRP报文中携带的DSCP优先级的取值。

【举例】

\# 配置IPv6 VRRP报文的DSCP优先级为30。

\<Sysname\> system-view

Sysname vrrp ipv6 dscp 30

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 mode**

------------------------------------------------------------------------

![说明](VRRP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vrrp ipv6 mode**]命令用来配置IPv6 VRRP的工作模式。

**[undo vrrp ipv6 mode**]命令用来恢复缺省情况。

【命令】

**[vrrp ipv6 mode load-balance**]

**[undo vrrp ipv6 mode**]

【缺省情况】

IPv6 VRRP工作在标准协议模式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[load-balance**]：指定IPv6 VRRP工作在负载均衡模式。

【使用指导】

IPv6 VRRP工作在负载均衡模式时，要求备份组虚拟IPv6地址和接口的IPv6地址不能相同。否则，负载均衡功能将无法正常工作。

创建IPv6 VRRP备份组后，仍然可以修改工作模式。修改工作模式后，路由器上所有的IPv6 VRRP备份组都会工作在该模式。

【举例】

\# 配置IPv6 VRRP工作在负载均衡模式。

\<Sysname\> system-view

Sysname vrrp ipv6 mode load-balance

【相关命令】

·**display** **vrrp ipv6**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid**

------------------------------------------------------------------------

**[vrrp ipv6 vrid**]命令用来创建IPv6 VRRP备份组，配置IPv6 VRRP备份组的虚拟IPv6地址，或为一个已经存在的IPv6 VRRP备份组添加一个虚拟IPv6地址。

**[undo vrrp ipv6 vrid**]命令用来删除一个已经存在的IPv6 VRRP备份组的所有配置，或删除已经存在的IPv6 VRRP备份组中的虚拟IPv6地址。

【命令】

**[vrrp ipv6 vrid***virtual-router-id*** virtual-ip*** virtual-address* [ **link-local** ]]

**[undo vrrp ipv6 vrid*** virtual-router-id * **virtual-ip**  *virtual-address* [ **link-local**  ] ]

【缺省情况】

没有创建IPv6 VRRP备份组。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv6 VRRP备份组号，取值范围为1～255。

**[virtual-ip*** virtual-address*]：备份组的虚拟IPv6地址。删除IPv6 VRRP备份组中的虚拟IPv6地址时，如果不指定*virtual-address*参数，则表示删除该备份组中的所有虚拟IPv6地址。

**[link-local**]：虚拟IPv6地址为链路本地地址。

【使用指导】

·重复执行本命令，可以为备份组配置多个虚拟IPv6地址，但每个备份组最多只能配置16个虚拟IPv6地址。

·备份组的第一个虚拟IPv6地址必须是链路本地地址，链路本地地址必须最后删除。

·一个VRRP备份组中只允许有一个链路本地地址。

·如果没有为备份组配置虚拟IPv6地址，但是为备份组进行了其他配置（如优先级、抢占方式等），则该备份组会存在于设备上，并处于Inactive状态，此时备份组不起作用。

·建议将备份组的虚拟IPv6地址和接口的IPv6地址配置为同一网段，否则可能导致局域网内的主机无法访问外部网络。

【举例】

·路由应用

\# 创建IPv6 VRRP备份组1，配置IPv6 VRRP备份组1的虚拟IPv6地址为fe80::10。为IPv6 VRRP备份组1添加一个虚拟IPv6地址1::10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 virtual-ip 1::10

·交换应用

\# 创建IPv6 VRRP备份组1，配置IPv6 VRRP备份组1的虚拟IPv6地址为fe80::10。为IPv6 VRRP备份组1添加一个虚拟IPv6地址1::10。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 virtual-ip fe80::10 link-local

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 virtual-ip 1::10

【相关命令】

·**display vrrp ipv6**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid preempt-mode**

------------------------------------------------------------------------

**[vrrp ipv6 vrid preempt-mode**]命令用来配置IPv6 VRRP备份组中的路由器工作在抢占方式，并配置抢占延迟时间。

**[undo vrrp ipv6 vrid preempt-mode**]命令用来取消抢占方式，即配置IPv6 VRRP备份组中的路由器工作在非抢占方式。

**[undo vrrp ipv6 vrid preempt-mode delay**]命令用来恢复抢占延迟时间为缺省值。

【命令】

**[vrrp ipv6 vrid** *virtual-router-id* **preempt-mode** [ **delay** *delay-value* ]]

**[undo vrrp ipv6 vrid** *virtual-router-id* **preempt-mode** [ **delay** ]]

【缺省情况】

IPv6 VRRP备份组中的路由器工作在抢占方式，抢占延迟时间为0厘秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv6 VRRP备份组号，取值范围为1～255。

**[delay*** delay-value*]：抢占延迟时间。*delay-value*取值范围为0～180000，单位为厘秒，缺省值为0厘秒。

【使用指导】

·如果备份组中的路由器工作在非抢占方式下，则只要Master路由器没有出现故障，Backup路由器即使随后被配置了更高的优先级也不会成为Master路由器。非抢占方式可以避免频繁地切换Master路由器。

·如果备份组中的路由器工作在抢占方式下，它一旦发现自己的优先级比当前的Master路由器的优先级高，就会对外发送VRRP通告报文。导致备份组内路由器重新选举Master路由器，并最终取代原有的Master路由器。相应地，原来的Master路由器将会变成Backup路由器。抢占方式可以确保承担转发任务的Master路由器始终是备份组中优先级最高的路由器。

·为了避免备份组内的成员频繁进行主备状态转换，让Backup路由器有足够的时间搜集必要的信息（如路由信息），Backup路由器接收到优先级低于本地优先级的通告报文后，不会立即抢占成为Master，而是等待一定时间后，才会重新选举新的Master路由器。

【举例】

·路由应用

\# 配置路由器工作于抢占方式，抢占延迟时间为5000厘秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 10 preempt-mode delay 5000

·交换应用

\# 配置交换机工作于抢占方式，抢占延迟时间为5000厘秒。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 10 preempt-mode delay 5000

【相关命令】

·**display** **vrrp ipv6**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid priority**

------------------------------------------------------------------------

**[vrrp ipv6 vrid priority**]命令用来设置路由器在IPv6 VRRP备份组中的优先级。

**[undo vrrp ipv6 vrid priority**]命令用来恢复缺省情况。

【命令】

**[vrrp ipv6 vrid ***virtual-router-id* **priority** *priority-value*]

**[undo vrrp ipv6 vrid** *virtual-router-id* **priority**]

【缺省情况】

路由器在IPv6 VRRP备份组中的优先级为100。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv6 VRRP备份组号，取值范围为1～255。

*[priority-value*]：优先级的值，取值范围为1～254，该值越大表明优先级越高。

【使用指导】

优先级决定路由器在备份组中的地位。优先级越高，越有可能成为Master路由器。优先级0是系统保留为特殊用途来使用的，255则是系统保留给IP地址拥有者的。

路由器为IP地址拥有者时，其运行优先级始终为255，表明只要其工作正常，则为Master路由器。

【举例】

·路由应用

\# 设置路由器在IPv6 VRRP备份组1中的优先级为150。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 priority 150

·交换应用

\# 设置交换机在IPv6 VRRP备份组1中的优先级为150。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 priority 150

【相关命令】

·**display** **vrrp ipv6**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid shutdown**

------------------------------------------------------------------------

**[vrrp ipv6 vrid shutdown**]命令用来关闭指定的IPv6 VRRP备份组。

**[undo vrrp ipv6 vrid shutdown**]命令用来恢复缺省情况。

【命令】

**[vrrp ipv6 vrid*** virtual-router-id* **shutdown**]

**[undo vrrp ipv6 vrid** *virtual-router-id* **shutdown**]

【缺省情况】

IPv6 VRRP备份组处于开启状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：VRRP备份组号，取值范围为1～255。

【使用指导】

关闭IPv6 VRRP备份组功能通常用于暂时禁用备份组，但还需要再次启用该备份组的场景。关闭备份组后，该备份组的状态为Initialize，并且该备份组所有已存在的配置保持不变。在关闭状态下还可以对备份组进行配置。备份组再次被开启后，基于最新的配置，从Initialize状态重新开始运行。

【举例】

·路由应用

\# 关闭IPv6 VRRP备份组1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 shutdown

·交换应用

\# 关闭IPv6 VRRP备份组1。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 shutdown

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid timer advertise**

------------------------------------------------------------------------

**[vrrp ipv6 vrid timer advertise**]命令用来配置IPv6 VRRP备份组中Master路由器发送VRRP通告报文的时间间隔。

**[undo vrrp ipv6 vrid timer advertise**]命令用来恢复缺省情况。

【命令】

**[vrrp ipv6 vrid** *virtual-router-id* **timer advertise** *adver-interval*]

**[undo vrrp ipv6 vrid** *virtual-router-id* **timer advertise**]

【缺省情况】

IPv6 VRRP备份组中Master路由器发送VRRP通告报文的时间间隔为100厘秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv6 VRRP备份组号，取值范围为1～255。

*[adver-interval*]：IPv6 VRRP备份组中的Master路由器发送VRRP通告报文的间隔时间，取值范围为10～4095，单位为厘秒。

【使用指导】

IPv6 VRRP备份组中的Master路由器会定时发送VRRP通告报文，通知备份组内的路由器自己工作正常。VRRP通告报文的发送时间间隔为本命令配置的值。

需要注意的是：

·建议配置VRRP通告报文的发送间隔大于100厘秒，否则会对系统的稳定性产生影响。

·IPv6 VRRP备份组中的路由器上配置的VRRP通告报文时间间隔可以不同。Master路由器根据自身配置的报文时间间隔定时发送通告报文，并在通告报文中携带Master路由器上配置的时间间隔；Backup路由器接收到Master路由器发送的通告报文后，记录报文中携带的Master路由器通告报文时间间隔，如果在3×记录的时间间隔＋Skew_Time内没有收到Master路由器发送的VRRP通告报文，则认为Master路由器出现故障，重新选举Master路由器。

·网络流量过大可能会导致Backup路由器在指定时间内没有收到Master路由器的VRRP通告报文，从而发生状态转换。可以通过将VRRP通告报文的发送时间间隔延长的办法来解决该问题。

【举例】

·路由应用

\# 设置IPv6 VRRP备份组1的Master路由器发送VRRP通告报文的间隔时间为500厘秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 timer advertise 500

·交换应用

\# 设置IPv6 VRRP备份组1的Master路由器发送VRRP通告报文的间隔时间为500厘秒。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 timer advertise 500

【相关命令】

·**display** **vrrp ipv6**

**VRRP \-- IPv6 VRRP配置命令 \-- vrrp ipv6 vrid track**

------------------------------------------------------------------------

![说明](VRRP命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vrrp ipv6 vrid track**]命令用来配置监视指定的Track项，即当Track项的状态为Negative时，立即将虚拟转发器切换为Active状态、降低路由器的优先级、立即切换成为Master路由器或降低本地虚拟转发器权重值。

**[undo vrrp ipv6 vrid track**]命令用来取消监视指定的Track项。

【命令】

**[vrrp ipv6 vrid**[ *virtual-router-id* **track** *track-entry-number* { **forwarder-switchover** **member-ip** *ipv6-address* \| **priority reduced** [ *priority-reduced* ] \| **switchover** \| **weight reduced**  *weight-reduced*  }]]

**[undo vrrp ipv6 vrid** *virtual-router-id* **track** [ *track-entry-number*  [ **forwarder-switchover** \| **priority reduced** \| **switchover** \| **weight reduced** ]]]

【缺省情况】

没有指定被监视的Track项。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[virtual-router-id*]：IPv6 VRRP备份组号，取值范围为1～255。

*[track-entry-number*]：被监视的Track项序号，*track-entry-number*取值范围为1～1024。

**[forwarder-switchover** **member-ip** *ipv6-address*]：虚拟转发器快速切换模式。当监视的Track项状态变为Negative时，如果本地设备上有处于Listening状态的虚拟转发器，且其对应的AVF地址为**member-ip**，则马上将该虚拟转发器切换到Active状态。*ipv6-address*为备份组中成员设备的IPv6地址。可以通过**display vrrp verbose**命令查看备份组中包含的成员设备。

**[priority reduced** [ *priority-reduced* ]]：当监视的Track项状态变为Negative时，降低本地路由器在备份组中的优先级。优先级降低的数值为*priority-reduced*，*priority-reduced*的取值范围为1～255，缺省值为10。

**[switchover**]：切换模式，当监视的Track项的状态变为Negative时，如果本路由器在备份组中处于Backup状态，则马上切换成为Master路由器。

**[weight reduced ** *weight-reduced* ]：当监视的Track项状态变为Negative时，当前路由器上属于指定IPv4 VRRP组的所有虚拟转发器的权重都降低指定的数值。权重降低的数值为*weight-reduced*，*weight-reduced*的取值范围为1～255，缺省值为30。

【使用指导】

需要注意的是：

·在执行本配置之前，需要先在接口上创建备份组并配置虚拟IPv6地址。

·执行**undo vrrp ****ipv6 vrid track**命令时如果没有指定*track-entry-number*参数，则删除该备份组与所有Track项的关联。

·只有VRRP工作在负载均衡模式时，执行**forwarder-switchover** **member-ip** *ip**v6-address*或**weight reduced ** *weight-reduced* 才会生效。

·虚拟转发器的权重值为255，虚拟转发器的失效下限为10。

·由于VF Owner的权重高于或等于失效下限时，它的优先级始终为255，不会根据虚拟转发器的权重改变。当监视的上行接口出现故障时，配置的权重降低数额需保证VF Owner的权重低于失效下限，即权重降低的数额大于245，其他的虚拟转发器才能接替VF Owner成为AVF。

·路由器在某个备份组中作为IP地址拥有者时，如果在该路由器上执行**vrrp ipv6 vrid track priority reduced**或**vrrp ipv6 vrid track switchover**命令，则该配置不会生效。该路由器不再作为IP地址拥有者后，之前的配置才会生效。

·被监视的Track项的状态由Negative变为Positive或NotReady后，对应的路由器优先级会自动恢复、对应虚拟转发器的权重会自动恢复、故障恢复后的原Master路由器会重新抢占为Master状态、故障恢复后的原AVF会重新抢占为Active状态。

·被监视的Track项可以是未创建的Track项。可以通过**vrrp ipv6 vrid track**命令指定监视的Track项后，再通过**track**命令创建该Track项。

Track项的详细介绍请参见"可靠性配置指导"中的"Track"。

【举例】

·路由应用

\# 在GigabitEthernet1/0/1接口上配置监视Track项1，当Track项1状态为Negative时，GigabitEthernet1/0/1接口上IPv6 VRRP备份组1的优先级降低50。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 track 1 priority reduced 50

\# 在GigabitEthernet1/0/1接口上配置虚拟转发器监视Track项1，当Track项1状态为Negative时，如果本地设备上AVF地址为1::3的虚拟转发器处于Listening状态，则马上将该虚拟转发器切换到Active状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 track 1 forwarder-switchover member-ip 1::3

\# 在GigabitEthernet1/0/1接口上配置虚拟转发器权重监视Track项1，当Track项1状态为Negative时，GigabitEthernet1/0/1接口上IPv6 VRRP备份组1所有虚拟转发器的权重都降低50。

\<Sysname\> sysname-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 vrrp ipv6 vrid 1 track 1 weight reduced 50

·交换应用

\# 在VLAN接口2上配置监视Track项1，当Track项1状态为Negative时，VLAN接口2上IPv6 VRRP备份组1的优先级降低50。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 track 1 priority reduced 50

\# 在VLAN接口2上配置虚拟转发器监视Track项1，当Track项1状态为Negative时，如果本地设备上AVF地址为1::3的虚拟转发器处于Listening状态，则马上将该虚拟转发器切换到Active状态。

\<Sysname\> system-view

Sysname interface vlan-interface 2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 track 1 forwarder-switchover member-ip 1::3

\# 在VLAN接口2上配置虚拟转发器权重监视Track项1，当Track项1状态为Negative时，VLAN接口2上IPv6 VRRP备份组1所有虚拟转发器的权重都降低50。

\<Sysname\> sysname-view

Sysname interface vlan-interface2

Sysname-Vlan-interface2 vrrp ipv6 vrid 1 track 1 weight reduced 50

【相关命令】

·**display** **vrrp ipv6**
