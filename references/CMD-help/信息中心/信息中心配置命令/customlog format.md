
**信息中心 \-- 信息中心配置命令 \-- customlog format**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[customlog format**]命令用来设置发往日志主机的用户定制的NAT444日志信息的输出格式。

**[undo customlog format**]命令用来恢复缺省情况。

【命令】

**[customlog format **[{ **unicom** \| **telecom** \| **cmcc** }]]

**[undo customlog format**]

【缺省情况】

设备不产生用户定制的NAT444的日志信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicom**]**：**设置发往日志主机的用户定制NAT444日志信息的输出格式为中国联通格式。

**[telecom**]**：**设置发往日志主机的用户定制NAT444日志信息的输出格式为中国电信格式。

**[cmcc**]**：**设置发往日志主机的用户定制NAT444日志信息的输出格式为中国移动格式。

【使用指导】

NAT444日志的相关信息请参考NAT手册。

【举例】

\# 设置发往日志主机的用户定制NAT444日志信息的输出格式为中国联通格式。

\<Sysname\> system

Sysname customlog format unicom

【相关命令】

·**customlog host**

**信息中心 \-- 信息中心配置命令 \-- customlog host**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[customlog host**]命令用来指定用户定制日志发送的日志主机并设置相关参数。

**[undo customlog host**]命令用来恢复缺省情况。

【命令】

**[customlog** **host** [ **vpn-instance** *vpn-instance-name*  { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }  **port** *port-number*  **export** { **cmcc-sessionlog** \| **cmcc-userlog** \| **telecom-sessionlog** \| **telecom-userlog** \| **unicom-sessionlog** \| **unicom-userlog** } \*]]

**[undo****customlog** **host** [ **vpn-instance** *vpn-instance-name*  { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }  **port** *port-number* ]]

【缺省情况】

没有指定日志主机和相关参数。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定日志主机所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示日志主机位于公网中。

*[hostname*]：指定日志的主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

*[ipv4-address*]：指定日志主机的IPv4地址。

**[ipv6** *ipv6-address*]：指定日志主机的IPv6地址。

*[port-number*]：指定日志主机接收日志信息的端口号，取值范围为1～65535，缺省值为514。该参数的值需要和日志主机侧的设置一致，否则日志主机接收不到日志信息。

**[cmcc-sessionlog**]**：**设备向指定的日志主机发送中国移动格式的基于session的NAT444用户定制日志。

**[cmcc-userlog**]**：**设备向指定的日志主机发送中国移动格式的基于用户的NAT444用户定制日志。

**[telecom-sessionlog**]**：**设备向指定的日志主机发送中国电信格式的基于session的NAT444用户定制日志。

**[telecom-userlog**]**：**设备向指定的日志主机发送中国电信格式的基于用户的NAT444用户定制日志。

**[unicom-sessionlog**]**：**设备向指定的日志主机发送中国联通格式的基于session的NAT444用户定制日志。

**[unicom-userlog**]**：**设备向指定的日志主机发送中国联通格式的基于用户的NAT444用户定制日志。

【使用指导】

用户最多可以指定4台不同主机同时接收设备产生的用户定制日志信息。

在配置设备向指定的日志主机发送指定格式的NAT444用户定制日志前，需要通过**customlog format**命令设置相应的NAT444日志输出格式，否则可以配置成功，但设备不产生相应的日志，日志主机将接收不到日志。

【举例】

\# 配置系统向IP地址为1.1.1.1的日志主机发送中国联通格式的基于session的NAT444用户定制日志日志信息。

\<Sysname\> system-view

Sysname customlog host 1.1.1.1 port 1000 export unicom-sessionlog unicom-userlog

【相关命令】

·**customlog host source**

**信息中心 \-- 信息中心配置命令 \-- customlog host source**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[customlog host** **source**]命令用来配置发送的日志信息的源IP地址。

**[undo** **customlog host** **source**]命令用来恢复缺省情况。

【命令】

**[customlog host source** *interface-type interface-number*]

**[undo****customlog host source**]

【缺省情况】

将根据路由来确定发送日志信息的出接口，使用该接口的主IP地址作为发送的日志信息的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定发送日志信息的源IP地址对应的出接口的类型和编号。

【使用指导】

配置日志信息的源IP地址后，不管实际使用哪个物理接口发送日志信息，日志信息的源IP地址均为指定接口的主IP地址。

【举例】

\# 配置使用Loopback0的IP地址作为发送的日志信息的源IP地址。

\<Sysname\> system-view

Sysname interface loopback 0

Sysname-LoopBack0 ip address 2.2.2.2 32

Sysname-LoopBack0 quit

Sysname customlog host source loopback 0

【相关命令】

·**customlog host**

**信息中心 \-- 信息中心配置命令 \-- customlog timestamp**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[customlog** **timestamp localtime**]命令用来设置发往日志主机的用户定制日志信息的时间戳为设备本地时间。

**[undo** **customlog** **timestamp** **localtime**]命令用来恢复缺省情况。

【命令】

**[customlog** **timestamp localtime**]

**[undo customlog timestamp localtime**]

【缺省情况】

发往日志主机的用户定制日志信息的时间戳为格林威治时间。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 设置发往日志主机的用户定制日志信息的时间戳系统本地时间。

\<Sysname\> system-view

Sysname customlog timestamp localtime

【相关命令】

·**customlog host**

**信息中心 \-- 信息中心配置命令 \-- diagnostic-logfile save**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[diagnostic-logfile** **save**]命令用来手动将诊断日志文件缓冲区中的内容全部保存到诊断日志文件。

【命令】

**[diagnostic-logfile** **save**]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

诊断日志文件的保存路径可以通过**info-center** **diagnostic-logfile** **directory**命令设置。

诊断日志文件保存成功后，诊断日志文件缓冲区中的内容会被清空。

【举例】

\# 手动将诊断日志文件缓冲区中的内容保存到诊断日志文件。

\<Sysname\> diagnostic-logfile save

The contents in the diagnostic log file buffer have been saved to the file flash:/ diagfile/diagfile.log.

【相关命令】

·**info-center diagnostic-logfile enable**

·**info-center diagnostic-logfile directory**

**信息中心 \-- 信息中心配置命令 \-- display diagnostic-logfile summary**

------------------------------------------------------------------------

![说明](信息中心命令.files/image002.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **diagnostic-logfile** **summary**]命令用来显示诊断日志文件的配置。

【命令】

**[display** **diagnostic-logfile** **summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示诊断日志文件配置。

\<Sysname\> display diagnostic-logfile summary

  Diagnostic log file: Enabled.

  Diagnostic log file size quota: 10 MB

  Diagnostic log file directory: flash:/diagfile

  Writing frequency: 24 hour 0 min 0 sec

表1-1 display logfile summary命令显示信息描述表

字段

描述

Diagnostic log file

诊断日志文件当前的状态（Enabled表示已开启，Disabled表示未开启）

Diagnostic log file size quota

单个诊断日志文件最大能占用的存储空间的大小，单位为MB

Diagnostic log file directory

诊断日志文件存储的路径

Writing frequency

系统自动保存诊断日志文件的频率

**信息中心 \-- 信息中心配置命令 \-- display info-center**

------------------------------------------------------------------------

**[display** **info-center**]命令用来显示各个输出方向的信息。

【命令】

**[display** **info-center**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示各个输出方向的信息。（该命令的显示信息与设备的型号有关，请以设备的实际情况为准）

\<Sysname\> display info-center

Information Center: Enabled

Console: Enabled

Monitor: Enabled

Log host: Enabled

    IP address: 192.168.0.1, port number: 5000, host facility: local7

    IP address: 192.168.0.2, port number: 5001, host facility: local5

Log buffer: Enabled

    Max buffer size 1024, current buffer size 512,

    Current messages 0, dropped messages 0, overwritten messages 0

Log file: Enabled

Security log file: Enabled

Information timestamp format:

Loghost: Date

    Other output destination: Date

表1-2 display info-center命令显示信息描述表

字段

描述

Information Center

信息中心当前的状态（enabled表示已开启，disabled表示未开启）

Console

控制台方向当前的状态（enabled表示已开启，disabled表示未开启）

Monitor

监视终端方向当前的状态（enabled表示已开启，disabled表示未开启）

Log host: Enabled

    IP address: 192.168.0.1, port number: 5000, host facility: local7

    IP address: 192.168.0.2, port number: 5001, host facility: local5

日志主机方向的信息（只有通过**info-center** **loghost**命令设置后，才有下面具体的显示内容），包括日志主机的IP地址，日志主机接收日志信息的端口，日志主机的记录工具

Log buffer: Enabled

    Max buffer size 1024, current buffer size 512,

    Current messages 0, dropped messages 0, overwritten messages 0

日志缓冲区方向的信息，包括开启状态、最大容量、当前容量、当前信息数、已丢弃的信息数、被覆盖的信息数

Log file

日志文件方向当前的状态（enabled表示已开启，disabled表示未开启）

Security log file

安全日志文件方向当前的状态（enabled表示已开启，disabled表示未开启）

Information timestamp format:

    Loghost: Date

    Other output destination: Date

信息时间戳设置，包括日志主机输出方向和非日志主机输出方向日志信息的时间戳类型，分为boot、date、iso、none和no-year-date五种

**信息中心 \-- 信息中心配置命令 \-- display logbuffer**

------------------------------------------------------------------------

**[display** **logbuffer**]命令用来显示日志缓冲区的状态和日志缓冲区记录的日志信息。

【命令】

集中式设备：

**[display** **logbuffer** [ **reverse**  [ **level** *severity* \| **size** *buffersize* \| **cpu** *cpu-number* ] \*]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **logbuffer** [ **reverse**  [ **level** *severity* \| **size** *buffersize* \| **slot** *slot-number* [ **cpu** *cpu-number* ] ] \*]]

分布式设备－IRF模式：

**[display** **logbuffer** [ **reverse**  [ **level** *severity* \| **size** *buffersize* \| **chassis** *chassis-number* **slot** *slot-number* [ **cpu** *cpu-number* ] ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[reverse**]：指定日志的显示顺序为从新到旧。如果不指定该参数，将先显示旧日志，最后显示最新的日志。

**[level** *severity*]：显示日志缓存中指定级别日志的信息，*severity*表示信息级别，取值范围为0～7。不带该参数时将显示系统日志缓冲区内所有级别的日志信息。

表1-3 信息级别列表

数值

信息级别

描述

0

emergency

表示设备不可用的信息，如系统授权已到期

1

alert

表示设备出现重大故障，需要立刻做出反应的信息，如流量超出接口上限

2

critical

表示严重信息，如设备温度已经超过预警值，设备电源、风扇出现故障等

3

error

表示错误信息，如接口链路状态变化，存储卡拔出等

4

warning

表示警告信息，如接口连接断开，内存耗尽告警等

5

notification

表示正常出现但是重要的信息，如通过终端登录设备，设备重启等

6

informational

表示需要记录的通知信息，如通过命令行输入命令的记录信息，执行**ping**命令的日志信息等

7

debugging

表示调试过程产生的信息

****

**[size** *buffersize*]：显示日志缓冲区中指定条数的最新日志。*buffersize*表示要显示的日志缓冲区中最新的日志信息的条数，取值范围为1～1024。不带该参数时将显示系统日志缓冲区内所有的日志信息。

**[slot***slot-number*]：显示指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。*slot-number*表示单板所在的槽位号。如不指定本参数，将显示所有单板的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的日志缓冲区状态及日志缓冲区中记录的日志信息。*slot-number*表示设备在IRF中的成员编号。如不指定该参数，将显示所有成员设备的日志缓冲区状态及日志缓冲区中记录的日志信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot** *slot-number*]：显示指定成员设备/PEX的日志缓冲区状态及日志缓冲区中记录的日志信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果不指定本参数，将显示所有成员设备/PEX上的日志缓冲区状态及日志缓冲区中记录的日志信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如不指定该参数，则显示所有单板的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的日志缓冲区状态及日志缓冲区中记录的日志信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如不指定该参数，则显示所有单板上的日志缓冲区状态及日志缓冲区中记录的日志信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的日志缓冲区状态及日志缓冲区中记录的日志信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示系统日志缓冲区的状态和缓冲区记录的日志信息。（集中式设备）

\<Sysname\> display logbuffer

Log buffer: Enabled

Max buffer size: 1024

Actual buffer size: 512

Dropped messages: 0

Overwritten messages: 718

Current messages: 512

%Jun 17 15:57:09:578 2006 Sysname SYSLOG/7/SYS_RESTART:System restarted \--

......略......

\# 显示系统日志缓冲区的状态和缓冲区记录的日志信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display logbuffer slot 1

Log buffer: Enabled

Max buffer size: 1024

Actual buffer size: 512

Dropped messages: 0

Overwritten messages: 0

Current messages: 127

%Jun 19 18:03:24:55 2006 Sysname SYSLOG /7/SYS_RESTART:System restarted

......略......

\# 显示系统日志缓冲区的状态和缓冲区记录的日志信息。（分布式设备－IRF模式）

\<Sysname\> display logbuffer chassis 0 slot 1

Log buffer: Enabled

Max buffer size: 1024

Actual buffer size: 512

Dropped messages: 0

Overwritten messages: 0

Current messages: 127

%Jun 19 18:03:24:55 2006 Sysname SYSLOG/7/SYS_RESTART:System restarted

......略......

表1-4 display logbuffer命令显示信息描述表

字段

描述

Log buffer

是否允许输出到日志缓冲区方向（Enabled表示允许，Disabled表示不允许）

Max buffer size

允许的日志缓冲区可存储的最大信息条数

Actual buffer size

当前设置的日志缓冲区可存储的最大信息条数

Dropped messages

被丢弃的信息数（内存分配失败或分配日志缓冲区过小时丢失的信息数）

Overwritten messages

被覆盖的信息数（如果缓冲区存储空间不足，最早收到的信息数会被新的信息覆盖掉）

Current messages

当前记录的信息数

【相关命令】

·**info-center** **logbuffer**

·**reset** **logbuffer**

**信息中心 \-- 信息中心配置命令 \-- display logbuffer summary**

------------------------------------------------------------------------

**[display** **logbuffer** **summary**]命令用来显示系统日志缓冲区的概要信息。

【命令】

集中式设备：

**[display**[ **logbuffer** **summary** [ **level** *severity* \| **cpu** *cpu-number* ]]]

分布式设备－独立运行模式/集中式IRF设备：

**[display**[ **logbuffer** **summary** [ **level** *severity* \| **slot** *slot-number* * *[ **cpu** *cpu-number* ] ] \*]]

分布式设备－IRF模式：

**[display**[ **logbuffer** **summary** [ **level** *severity* \| **chassis** *chassis-number* **slot** *slot-number* * *[ **cpu** *cpu-number* ] ] \*]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[level** *severity*]：显示日志缓存中指定级别日志的概要信息，*severity*表示信息级别，取值范围为0～7，具体内容请参见[表]1-3(?-1632812546#_Ref127266393)。不带该参数时，将显示系统日志缓冲区内所有级别的日志概要信息。

**[slot***slot-number*]：显示指定单板的日志缓冲区的概要信息。*slot-number*表示单板所在的槽位号。如不指定该参数，将显示所有单板的日志缓冲区概要信息。（分布式设备－独立运行模式）

**[slot***slot-number*]：显示指定成员设备的日志缓冲区的概要信息。*slot-number*表示设备在IRF中的成员编号。如不指定该参数，将显示所有成员设备上的日志缓冲区概要信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot***slot-number*]：显示指定成员设备/PEX的日志缓冲区的概要信息。*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如不指定该参数，将显示所有成员设备/PEX上的日志缓冲区概要信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备上指定单板的日志缓冲区的概要信息。*chassis-numbe*r表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如不指定该参数，将显示所有单板上的日志缓冲区的概要信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板的日志缓冲区的概要信息。*chassis-numbe*r表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如不指定该参数，将显示所有单板上的日志缓冲区的概要信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu ***cpu-number*]：显示指定CPU上的日志缓冲区的概要信息。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 显示系统日志缓冲区的概要信息。（集中式设备）

\<Sysname\> display logbuffer summary

EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG

    0     0     0     0    22     0     1     0

\# 显示系统日志缓冲区的概要信息。（集中式IRF设备）

\<Sysname\> display logbuffer summary

  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG

     1     0     0     0     7     0    34    38     0

     2     0     0     0     0     0     0     0     0

     3     0     0     0     0     0     0     0     0

     4     0     0     0     0     0     0     0     0

\# 显示系统日志缓冲区的概要信息。（分布式设备－独立运行模式）

\<Sysname\> display logbuffer summary

  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG

     0     0     0     0     0     0     0     0     0

     1     0     0     0     0     0     0     0     0

     2     0     0     0     0     0     0     0     0

     3     0     0     0     0    16     0     1     0

\# 显示系统日志缓冲区的概要信息。（分布式设备－IRF模式）

\<Sysname\> display logbuffer summary

 CHASSIS  SLOT EMERG ALERT  CRIT ERROR  WARN NOTIF  INFO DEBUG

       1     0     0     0     0     1   238     0     1     0

       1     1     0     0     0     0     0     0     0     0

       1     2     0     0     0     0     1     0     0     0

       2     0     0     0     0     0     5     0     0     0

       2     1     0     0     0     0     1     0     0     0

表1-5 display logbuffer summary命令显示信息描述表

字段

描述

CHASSIS

IRF中设备的成员编号（分布式设备---IRF模式）

SLOT

单板所在的槽位号（分布式设备---独立运行模式/分布式设备---IRF模式）

SLOT

设备在IRF中的成员编号（集中式IRF设备）

EMERG

emergency级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

ALERT

alert级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

CRIT

critical级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

ERROR

error级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

WARN

warning级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

NOTIF

notification级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

INFO

informational级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

DEBUG

debugging级别的信息数，请参见[表]1-3(?-1632812546#_Ref127266393)

**信息中心 \-- 信息中心配置命令 \-- display logfile summary**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **logfile** **summary**]命令用来显示日志文件的配置。

【命令】

**[display** **logfile** **summary**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示日志文件配置。

\<Sysname\> display logfile summary

  Log file: Enabled.

  Log file size quota: 10 MB

  Log file directory: flash:/logfile

  Writing frequency: 0 hour 1 min 10 sec

表1-6 display logfile summary命令显示信息描述表

字段

描述

Log file

是否允许输出到日志文件方向（Enabled表示已开启，Disabled表示未开启）

Log file size quota

单个日志文件最大能占用的存储空间的大小，单位为MB

Log file directory

日志文件存储的路径

Writing frequency

系统自动保存日志文件的频率

**信息中心 \-- 信息中心配置命令 \-- display security-logfile summary**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display** **security-logfile** ]**summary**命令用来显示安全日志文件的概要信息。

【命令】

**[display** **security-logfile** ]**summary**

【视图】

任意视图

【缺省用户角色】

security-audit

【使用指导】

只有配置了安全日志管理员权限的本地用户才能使用本命令。安全日志管理员的配置请参见"安全命令参考"中的"AAA"。

【举例】

\# 显示安全日志文件概要信息。

\<Sysname\> display security-logfile summary

  Security log file: Enabled

  Security log file size quota: 10 MB

  Security log file directory: flash:/seclog

  Alarm threshold: 80%

  Current usage: 30%

  Writing frequency: 1 hour 0 min 0 sec

表1-7 display security-logfile summary命令显示信息描述表

字段

描述

Security log file

安全日志文件当前的状态（Enabled表示已开启，Disabled表示未开启）

Security log file size quota

单个安全日志文件最大能占用的存储空间的大小

Security log file directory

安全日志文件存储的路径

Alarm-threshold

安全日志文件使用率告警门限

Current usage

当前的安全日志文件使用率

Writing frequency

系统自动保存安全日志文件的频率

【相关命令】

·**authorization-attribute**（安全命令参考/AAA）

**信息中心 \-- 信息中心配置命令 \-- enable log updown**

------------------------------------------------------------------------

**[enable**] **log** **updown**命令用来设置允许端口在状态发生改变时生成Link up和Link down的日志信息。

**[undo**] **enable** **log** **updown**命令用来禁止端口在状态发生改变时生成Link up和Link down的日志信息。

【命令】

**[enable** **log** **updown**]

**[undo** **enable** **log** **updown**]

【缺省情况】

允许所有端口在状态发生改变时生成端口Link up和Link down的日志信息。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 禁止端口GigabitEthernet1/0/1在状态发生改变时生成Link up和Link down的日志信息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 undo enable log updown

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile enable**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **diagnostic-logfile** **enable**]命令用来开启诊断日志同步保存功能。

**[undo** **info-center** **diagose-logfile** **enable**]命令用来关闭诊断日志同步保存功能。

【命令】

**[info-center** **diagnostic-logfile** **enable**]

**[undo** **info-center** **diagnostic-logfile** **enable**]

【缺省情况】

允许诊断日志信息输出到诊断日志文件。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启诊断日志同步保存功能后，系统将诊断日志进行集中处理：当生成的诊断日志时，系统会将诊断日志信息同步保存到诊断日志文件。这样既实现了诊断日志的集中管理，又有利于用户随时快捷地查看诊断日志，了解设备状态。

【举例】

\# 开启诊断日志同步保存功能。

\<Sysname\> system-view

Sysname info-center diagnostic-logfile enable

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile frequency**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **diagnostic-logfile** **frequency**]命令用来设置设备自动保存诊断日志文件的频率。

**[undo** **info-center** **diagnostic-logfile** **frequency**]命令用来恢复缺省情况。

【命令】

**[info-center** **diagnostic-logfile** **frequency** *freq-sec*]

**[undo** **info-center** **diagnostic-logfile** **frequency**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[freq-sec*]：系统自动保存诊断日志文件的频率，取值范围为10～86400，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。

【使用指导】

设置设备自动保存诊断日志文件的频率后，诊断日志会先被输出到诊断日志文件缓冲区（diagnostic-logfile buffer），系统会按照配置中指定的频率将诊断日志文件缓冲区的内容写入诊断日志文件。

【举例】

\# 设置诊断日志自动保存到文件的频率为600秒。

\<Sysname\> system-view

Sysname info-center diagnostic-logfile frequency 600

【相关命令】

·**info-center ****diagnostic-logfile enable**

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile quota**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center**] **diagnostic-logfile** **quota**命令用来设置单个诊断日志文件最大能占用的存储空间的大小。

**[undo**] **info-center** **diagnostic-logfile** **quota**命令用来恢复缺省情况。

【命令】

**[info-center** **diagnostic-logfile** ]**quota** *size*

**[undo**] **info-center** **diagnostic-logfile** **quota**

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：单个诊断日志文件可使用的存储空间的最大值，单位为MB。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 设置单个诊断日志文件最大能占用的存储空间的大小为6MB。

\<Sysname\> system-view

Sysname info-center diagnostic-logfile quota 6

**信息中心 \-- 信息中心配置命令 \-- info-center diagnostic-logfile directory**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **diagnostic-logfile** ]**directory**命令用来修改存储诊断日志文件的路径。

【命令】

**[info-center** **diagnostic-logfile** **directory** *dir-name*]

【缺省情况】

存储诊断日志文件路径为存储设备根目录下的diagfile文件夹。对于支持CF卡分区的设备，存储诊断日志文件目录与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dir-name*]：诊断日志文件存储的路径，为1～64个字符的字符串。

【使用指导】

在执行该配置前，存储诊断日志文件的文件夹必须为当前已创建的目录。

配置时，请注意：

·配置会在设备重启后失效（集中式设备）。

·配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。

·配置会在IRF重启或Master和Slave倒换后失效（集中式IRF设备）。

·配置会在IRF重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－IRF模式）。

【举例】

\# 设置存放诊断日志文件的目录为flash:/test。

\<Sysname\> mkdir test

Creating directory flash:/test\... Done.

\<Sysname\> system-view

Sysname info-center diagnostic-logfile directory flash:/test

**信息中心 \-- 信息中心配置命令 \-- info-center logfile overwrite-protection**

------------------------------------------------------------------------

**[info-center logfile overwrite-protection**]命令用来开启日志文件的写满保护功能。如果日志文件已经达到限额或空间不足，不允许覆盖写入新的日志。

**[undo info-center logfile overwrite-protection**]命令用来关闭日志文件的写满保护功能。如果日志文件已经达到限额或空间不足，则允许覆盖写入新的日志。

【命令】

**[info-center logfile overwrite-protection** [ **all-port-powerdown** ]]

**[undo info-center logfile overwrite-protection**]

【缺省情况】

日志文件的写满保护功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all-port-powerdown**]：表示如果日志文件已经达到限额或空间不足，则关闭所有的业务接口。

【使用指导】

本命令仅FIPS模式下支持。

日志文件的写满保护功能处于关闭状态：

·对于支持单个日志文件的设备：当存储介质的空间达到设备支持的最大值，新产生的日志会从日志文件开头覆盖写入。此后如果用户先开启，再关闭日志写满保护功能，日志从日志文件开头覆盖写入，此时覆盖的有可能不是最旧的日志。

·对于支持多个日志文件的设备：当日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足时，系统会删除最旧的日志文件再创建新的日志文件。

日志文件的写满保护功能处于开启状态，日志将从当前日志文件的尾部开始进行记录。在记录日志的过程中，如果日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足，不再覆盖旧日志或删除最旧的日志文件，而是停止记录日志文件。

【举例】

\# 开启日志文件的写满保护功能。

\<Sysname\> system-view

Sysname info-center logfile overwrite-protection

**信息中心 \-- 信息中心配置命令 \-- info-center enable**

------------------------------------------------------------------------

**[info-center** **enable**]命令用来开启信息中心功能。

**[undo** **info-center** **enable**]命令用来关闭信息中心功能。

【命令】

**[info-center** **enable**]

**[undo** **info-center** **enable**]

【缺省情况】

信息中心处于开启状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启信息中心功能。

\<Sysname\> system-view

Sysname info-center enable

Information center is enabled.

**信息中心 \-- 信息中心配置命令 \-- info-center format**

------------------------------------------------------------------------

**[info-center format**]命令用来设置发往日志主机的日志信息的输出格式。

**[undo info-center format**]命令用来恢复缺省情况。

【命令】

[**[info-center format { unicom \| cmcc }]**]

**[undo info-center format**]

【缺省情况】

发往日志主机的日志信息的格式为非定制格式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[unicom**]**：**设置发往日志主机的日志信息的输出格式为中国联通格式。

**[cmcc**]**：**设置发往日志主机的日志信息的输出格式为中国移动格式。

【使用指导】

发往日志主机的日志信息有三种格式：非定制格式、中国联通格式和中国移动格式。有关日志信息格式的详细介绍请参见"网络管理和监控配置指导"中的"信息中心"。

【举例】

\# 设置发往日志主机的日志信息的格式为中国联通格式。

\<Sysname\> system-view

Sysname info-center format unicom

**信息中心 \-- 信息中心配置命令 \-- info-center logbuffer**

------------------------------------------------------------------------

**[info-center** **logbuffer**]命令用来允许日志信息输出到日志缓冲区。

**[undo** **info-center** **logbuffer**]命令用来禁止日志信息输出日志缓冲区。

【命令】

**[info-center** **logbuffer**]

**[undo** **info-center** **logbuffer**]

【缺省情况】

允许日志信息输出到日志缓冲区。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置允许日志信息输出到日志缓冲区。

\<Sysname\> system-view

Sysname info-center logbuffer

【相关命令】

·**display** **logbuffer**

·**info-center** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center logbuffer size**

------------------------------------------------------------------------

**[info-center** **logbuffer** **size**]命令用来配置日志缓冲区可存储的信息条数。

**[undo** **info-center** **logbuffer** **size**]命令用来恢复日志缓冲区可存储的信息条数为默认值。

【命令】

**[info-center** **logbuffer** **size** *buffersize*]

**[undo** **info-center** **logbuffer** **size**]

【缺省情况】

日志缓冲区可存储512条信息。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[buffersize*]：日志缓冲区可存储的信息条数，取值范围为0～1024，缺省值为512。

【举例】

\# 配置日志缓冲区可存储的信息条数为50。

\<Sysname\> system-view

Sysname info-center logbuffer size 50

\# 恢复日志缓冲区可存储的信息条数为512。

\<Sysname\> system-view

Sysname undo info-center logbuffer size

【相关命令】

·**display** **logbuffer**

·**info-center** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center logfile enable**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **logfile** **enable**]命令用来允许日志信息输出到日志文件。

**[undo** **info-center** **logfile** **enable**]命令用来禁止日志信息输出到日志文件。

【命令】

**[info-center** **logfile** **enable**]

**[undo** **info-center** **logfile** **enable**]

【缺省情况】

允许日志信息输出到日志文件。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 配置允许日志信息输出到日志文件。

\<Sysname\> system-view

Sysname info-center logfile enable

**信息中心 \-- 信息中心配置命令 \-- info-center logfile frequency**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **logfile** **frequency**]命令用来设置系统自动保存日志文件的频率。

**[undo** **info-center** **logfile** **frequency**]命令用来恢复缺省情况。

【命令】

**[info-center** **logfile** **frequency** *freq-sec*]

**[undo** **info-center** **logfile** **frequency**]

【缺省情况】

系统自动保存日志文件的频率与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[freq-sec*]：系统自动保存日志文件的频率，取值范围为1～86400，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。

【使用指导】

设置系统自动保存日志文件的频率后，系统会按照指定的频率将日志文件缓冲区的内容写入日志文件。

【举例】

\# 设置设备自动保存日志文件的频率为60000秒。

\<Sysname\> system-view

Sysname info-center logfile frequency 60000

【相关命令】

·**info-center** **logfile** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center logfile size-quota**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

****

**[info-center** **logfile** **size-quota**]命令用来设置单个日志文件最大能占用的存储空间的大小。

**[undo** **info-center** **logfile** **size-quota**]命令用来恢复缺省情况。

【命令】

**[info-center**] **logfile** **size-quota** *size*

**[undo**] **info-center** **logfile** **size-quota**

【缺省情况】

单个日志文件最大能占用的存储空间的大小与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：单个日志文件可使用的存储空间的最大值，单位为MB。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

当日志文件的大小达到设置的最大值时：

·对于只支持单个日志文件的设备，系统会使用最新日志覆盖最旧日志；

·对于支持多个日志文件的设备，系统会自动创建新的日志文件来保存新信息，日志文件的名称为logfile1.log、logfile2.log、......。当日志文件的个数达到设备支持的最大值或者设备可用存储介质的空间不足时，系统会删除最旧的日志文件再创建新的日志文件。

【举例】

\# 设置单个日志文件最大能占用的存储空间的大小为6MB。

\<Sysname\> system-view

Sysname info-center logfile size-quota 6

【相关命令】

·**info-center** **logfile** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center logfile directory**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **logfile** **directory**]命令用来设置存储日志文件的目录。

【命令】

**[info-center** **logfile** **directory** *dir-name*]

【缺省情况】

存储日志文件的目录与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dir-name*]：存储日志文件的路径，为1～64个字符的字符串。

【使用指导】

在执行该配置前，存储日志文件的目录必须为当前已创建的目录。

生成的日志文件的后缀名为.log，当缺省的存储器已满时，可以设置一个新的目录来存放新的日志信息。

配置时，请注意：

·配置会在设备重启后失效（集中式设备）。

·配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。

·配置会在IRF重启或主从设备倒换后失效（集中式IRF设备）。

·配置会在IRF重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－IRF模式）。

【举例】

\# 在根目录flash:下创建文件夹test。

\<Sysname\> mkdir test

Creating directory flash:/test\... Done.

\# 设置存放日志文件的目录为flash:/test。

\<Sysname\> system-view

Sysname info-center logfile directory flash:/test

【相关命令】

·**info-center** **logfile** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center logging suppress duplicates**

------------------------------------------------------------------------

**[info-center** **logging** **suppress** **duplicates**]命令用来开启抑制重复日志输出功能。

**[undo** **info-center** **logging** **suppress** **duplicate**]命令用来恢复缺省情况。

【命令】

**[info-center** **logging** **suppress** **duplicates**]

**[undo** **info-center** **logging** **suppress** **duplicates**]

【缺省情况】

抑制重复日志输出功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当设备持续向某个方向发送同一条日志信息时（发送间隔小于30秒），大量重复的信息会浪费设备资源和网络资源，并导致有用的信息被淹没，不利于设备的维护。为了避免此问题，可开启重复日志抑制功能。

开启重复日志抑制功能后，设备每产生一条新日志信息，在输出该日志信息的同时会启动该日志的抑制周期：

·该日志抑制周期内：如果设备后续连续生成的日志信息均与该日志信息相同（要求日志信息的如下字段均完全相同：模块名、信息等级、日志助记符、定位信息和信息文本），则系统会认为后续生成的日志是该日志的相同日志，后续生成的日志信息不再输出。

·该日志抑制周期结束后：如果设备后续仍连续生成该日志，系统输出被抑制的日志信息以及被抑制的数量，并启动下一个日志抑制周期。日志信息的第一个抑制周期为30秒，第二个抑制周期为2分钟，以后的抑制周期都是10分钟。

·如果在日志抑制周期内有其它新日志信息产生：系统会先输出被抑制的日志信息以及被抑制的数量，再输出新的日志信息，并开始新日志的抑制周期。

【举例】

\# 开启抑制重复日志输出功能。

·假设设备上Vlan-interface100的IP地址和网络中某设备的IP地址冲突，设备会频繁输出如下日志信息。

%Jan  1 07:27:48:636 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

·开启抑制重复日志输出功能。

\<Sysname\> system-view

Sysname info-center logging suppress duplicates

·设备会继续输出如下日志。

%Jan  1 07:27:48:636 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

%Jan  1 07:28:19:639 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

 This message repeated 4 times in last 30 seconds.

以上显示信息表明：开启开启抑制重复日志输出功能后，设备生成了一条IP地址冲突的日志，第一个抑制周期为30秒。

%Jan  1 07:30:19:643 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

 This message repeated 20 times in last 2 minutes.

以上显示信息表明抑制周期延长为120秒。

%Jan  1 07:30:20:541 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

 This message repeated 1 times in last 1 second.

%Jan  1 07:30:19:542 2000 Sysname CFGMAN/5/CFGMAN_CFGCHANGED: -EventIndex=[12-CommandSource=2-ConfigSource=4-ConfigDestination=2; Configuration is changed.]

以上显示信息表明在抑制周期内有新的日志产生。

%Jan  1 07:30:24:643 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

%Jan  1 07:30:55:645 2000 Sysname ARP/6/DUPIFIP:

Duplicate address 172.16.0.1 on interface Vlan-interface100, sourced from 00e0-fc58-123d

 This message repeated 4 times in last 30 seconds.

以上显示信息表明开始新一轮抑制。

**信息中心 \-- 信息中心配置命令 \-- info-center loghost**

------------------------------------------------------------------------

**[info-center** **loghost**]命令用来指定日志主机并设置相关输出参数。

**[undo** **info-center** **loghost**]命令用来恢复缺省情况。

【命令】

**[info-center** **loghost** [ **vpn-instance** *vpn-instance-name*   { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* } [ **port** *port-number* ]  **facility** *local-number* ]]

**[undo** **info****-center** **loghost** [ **vpn-instance** *vpn-instance-name*  { *hostname* \| *ipv4-address* \| **ipv6** *ipv6-address* }]]

【缺省情况】

没有指定日志主机和相关参数。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vpn-instance** *vpn-instance-name*]：指定日志主机所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示日志主机位于公网中。

*[hostname*]：指定日志的主机名，为1～253个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"-"、"\_"和"."。

*[ipv4-address*]：指定日志主机的IPv4地址。

**[ipv6** *ipv6-address*]：指定日志主机的IPv6地址。

**[port*** port-number*]：指定日志主机接收日志信息的端口号，取值范围为1～65535，缺省值为514。该参数的值需要和日志主机侧的设置一致，否则日志主机接收不到日志信息。

**[facility***local*-*number*]：设置日志主机的记录工具。取值范围为local0～local7，缺省值为local7。主要用于在日志主机端标志不同的日志来源，查找、过滤对应日志源的日志。

【使用指导】

用户只有使用**info-center** **enable**命令开启了信息中心功能，配置**info-center** **loghost**命令才会生效。

用户最多可以指定4台不同主机同时接收设备产生的日志信息。

【举例】

\# 配置系统向IP地址为1.1.1.1的日志主机发送日志信息。

\<Sysname\> system-view

Sysname info-center loghost 1.1.1.1

**信息中心 \-- 信息中心配置命令 \-- info-center loghost source**

------------------------------------------------------------------------

**[info-center** **loghost** **source**]命令用来配置发送的日志信息的源IP地址。

**[undo** **info-center** **loghost** **source**]命令用来恢复缺省情况。

【命令】

**[info-center** **loghost** **source** *interface-type interface-number*]

**[undo** **info-center** **loghost** **source**]

【缺省情况】

将根据路由来确定发送日志信息的出接口，使用该接口的主IP地址作为发送的日志信息的源IP地址。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interface-type interface-number*]：指定发送日志信息的源IP地址对应的出接口的类型和编号。

【使用指导】

配置日志信息的源IP地址后，不管实际使用哪个物理接口发送日志信息，日志信息的源IP地址均为指定接口的主IP地址。

用户只有使用**info-center enable**命令开启了信息中心功能，配置**info-center loghost source**命令才会生效。

【举例】

\# 配置使用Loopback0的IP地址作为发送的日志信息的源IP地址。

\<Sysname\> system-view

Sysname interface loopback 0

Sysname-LoopBack0 ip address 2.2.2.2 32

Sysname-LoopBack0 quit

Sysname info-center loghost source loopback 0

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile alarm-threshold**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **security-logfile** ]**alarm-threshold**命令用来设置安全日志文件使用率的告警门限。

**[undo** **info-center** **security-logfile** ]**alarm-threshold**命令用来恢复缺省情况。

【命令】

**[info-center** **security-logfile** ]**alarm-threshold** *usage*

**[undo** **info-center** **security-logfile** ]**alarm-threshold**

【缺省情况】

安全日志文件使用率的告警门限是80（即当安全日志文件使用率达到80％时，系统会提醒用户）。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[usage*]：安全日志文件使用率的告警门限，取值范围为1～100的整数。

【使用指导】

当安全日志文件大小达到上限时，新的安全日志会覆盖旧的安全日志，从而导致安全日志丢失。为防止这种情况发生，用户可以使用本命令设置安全日志文件使用率的告警门限。当使用率超过此门限值时，系统会发出日志提醒用户，此时，用户可以将安全日志文件进行备份，以防重要历史数据丢失。

【举例】

\# 设置当安全日志文件使用率达到90%时进行告警。

\<Sysname\> system-view

Sysname info-center security-logfile alarm-threshold 90

【相关命令】

·**info-center** **security-logfile** **size-quota**

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile enable**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **security-logfile** **enable**]命令用来开启安全日志同步保存功能。

**[undo** **info-center** **security-logfile** **enable**]命令用来关闭安全日志同步保存功能。

【命令】

**[info-center** **security-logfile** **enable**]

**[undo** **info-center** **security-logfile** **enable**]

【缺省情况】

安全日志同步保存功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启安全日志同步保存功能后，系统将安全日志进行集中处理：当生成的日志信息中有安全日志，在不影响日志信息现有输出规则的前提下，系统会将安全日志信息同步保存到专用的安全日志文件。这样既实现了安全日志的集中管理，又有利于用户随时快捷地查看安全日志，了解设备状态。

【举例】

\# 开启安全日志同步保存功能。

\<Sysname\> system-view

Sysname info-center security-logfile enable

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile frequency**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **security-logfile** **frequency**]命令用来设置设备自动保存安全日志文件的频率。

**[undo** **info-center** **security-logfile** **frequency**]命令用来恢复缺省情况。

【命令】

**[info-center** **security-logfile** **frequency** *freq-sec*]

**[undo** **info-center** **security-logfile** **frequency**]

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[freq-sec*]：系统自动保存安全日志文件的频率，取值范围为10～86400，单位为秒，不同设备支持的缺省值不同，请以设备的实际情况为准。

【使用指导】

设置设备自动保存安全日志文件的频率后，安全日志会先被输出到安全日志文件缓冲区（security-logfile buffer），系统会按照配置中指定的频率将安全日志文件缓冲区的内容写入安全日志文件。

【举例】

\# 设置安全日志自动保存到文件的频率为600秒。

\<Sysname\> system-view

Sysname info-center security-logfile frequency 600

【相关命令】

·**info-center** **security-logfile** **enable**

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile size-quota**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center**] **security-logfile** **size-quota**命令用来设置单个安全日志文件最大能占用的存储空间的大小。

**[undo**] **info-center** **security-logfile** **size-quota**命令用来恢复缺省情况。

【命令】

**[info-center** **security-logfile** ]**size-quota** *size*

**[undo**] **info-center** **security-logfile** **size-quota**

【缺省情况】

本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：单个安全日志文件可使用的存储空间的最大值，单位为MB。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 设置单个安全日志文件最大能占用的存储空间的大小为6MB。

\<Sysname\> system-view

Sysname info-center security-logfile size-quota 6

【相关命令】

·**info-center** **security-logfile** **alarm-threshold**

**信息中心 \-- 信息中心配置命令 \-- info-center security-logfile directory**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[info-center** **security-logfile** ]**directory**命令用来修改存储安全日志文件的路径。

【命令】

**[info-center** **security-logfile** **directory** *dir-name*]

【缺省情况】

存储安全日志文件路径为存储设备根目录下的seclog文件夹。对于支持CF卡分区的设备，存储安全日志文件目录与设备的型号有关，请以设备的实际情况为准。

【视图】

系统视图

【缺省用户角色】

security-audit

【参数】

*[dir-name*]：安全日志文件存储的路径，为1～64个字符的字符串。

【使用指导】

在执行该配置前，存储安全日志文件的文件夹必须为当前已创建的目录。

配置时，请注意：

·配置会在设备重启后失效（集中式设备）。

·配置会在设备重启或主备倒换后失效（分布式设备－独立运行模式）。

·配置会在IRF重启或主从设备倒换后失效（集中式IRF设备）。

·配置会在IRF重启或全局主用主控板和全局备用主控板主备倒换后失效（分布式设备－IRF模式）。

【举例】

\# 设置存放安全日志文件的目录为flash:/test。

\<Sysname\> mkdir test

Creating directory flash:/test\... Done.

\<Sysname\> system-view

Sysname info-center security-logfile directory flash:/test

**信息中心 \-- 信息中心配置命令 \-- info-center source**

------------------------------------------------------------------------

**[info-center** **source**]命令用来配置日志信息的输出规则。

**[undo** **info**-**center** **source**]命令用来恢复缺省情况。

【命令】

**[info-center**[ **source** { *module-name* \| **default** } { **console** \| **logbuffer** \| **logfile** \| **loghost** \| **monitor** } { **deny** \| **level** *severity* }]]

**[undo**[ **info-center** **source** { *module-name* \| **default** } { **console** \| **logbuffer** \| **logfile** \| **loghost** \| **monitor** }]]

【缺省情况】

日志信息的输出规则请参见 表1-8(?-540823941#_Ref152648258)：

表1-8 输出方向的缺省输出规则

输出方向

允许输出的模块

log

security

diagnostic

hide

控制台

所有支持的模块

debugging

不能输出到控制台

不能输出到控制台

不能输出到控制台

监视终端

所有支持的模块

debugging

不能输出到控制台

不能输出到控制台

不能输出到控制台

日志主机

所有支持的模块

informational

不能输出到日志主机

不能输出到日志主机

informational

日志缓冲区

所有支持的模块

informational

不能输出到日志缓冲区

不能输出到日志缓冲区

informational

日志文件

所有支持的模块

informational

不能输出到日志文件

不能输出到日志文件

informational

安全日志文件

所有支持的模块，不能过滤

不能输出到安全日志文件

debugging（不能过滤）

不能输出到安全日志文件

不能输出到安全日志文件

诊断日志文件

所有支持的模块，不能过滤

不能输出到诊断日志文件

不能输出到诊断日志文件

debugging（不能过滤）

不能输出到诊断日志文件

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[module-name*]：设置指定应用模块日志信息的输出规则。比如要输出关于FTP的日志信息，就把该参数设置成FTP。系统支持的来源模块可以通过在系统视图下输入**info-center** **source** **?**进行查看。

**[default**]：设置当前允许输出的所有模块日志信息的输出规则，包含在系统视图下输入**info-center** **source** **？**查看到的所有具体模块。

**[console**]：输出到控制台。

**[logbuffer**]：输出到日志缓冲区。

**[logfile**]：输出到日志文件。

**[loghost**]：输出到日志主机。

**[monitor**]：输出到监视终端。

**[deny**]：禁止输出信息。

**[level** *severity*]：指定信息级别，取值范围为0～7，具体内容请参见[表]1-3(?-1632812546#_Ref127266393)。通过该参数可以控制允许/禁止输出的日志信息的最低级别。

【使用指导】

该命令用来配置日志信息的输出规则。例如实现IP模块的日志信息输出的过滤规则，用户可以设置IP模块的日志信息高于warning级别的可以输出到日志主机，而高于informational级别的可以输出到日志缓冲区。同时可以设置IP模块的告警信息发送到特定的方向等功能。

需要注意的是：

·如果没有使用*module-name*参数为应用模块单独设置输出规则，则该模块使用缺省的或者**default**参数设置的输出规则，否则使用单独设置的输出规则。

·如果多次使用本命令配置**default**或者某个模块的输出规则，则以最新的配置生效。

·如果应用模块单独设置输出规则后，必须使用*module-name*参数来修改或删除该规则，使用**default**参数进行的新配置对该模块不生效。

【举例】

\# 只允许VLAN模块的信息输出控制台，且输出信息的级别为emergency的日志信息。

\<Sysname\> system-view

Sysname info-center source default console deny

Sysname info-center source vlan console level emergency

\# 在前面例子基础上撤销控制台方向上VLAN模块的输出（即全部信息不在控制台显示）。

\<Sysname\> system-view

Sysname undo info-center source vlan console

**信息中心 \-- 信息中心配置命令 \-- info-center synchronous**

------------------------------------------------------------------------

**[info-center** **synchronous**]命令用来开启命令行输入回显功能。

**[undo** **info-center** **synchronous**]命令用来关闭命令行输入回显功能。

【命令】

**[info-center** **synchronous**]

**[undo** **info-center** **synchronous**]

【缺省情况】

命令行输入回显功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

当用户进行命令行、参数或者Y/N确认信息输入时，如果被大量的日志信息打断，用户可能记不清已经输入了哪些字符串，还需要输入哪些字符串。使用命令行输入回显功能，能够协助用户配置。系统会在日志信息输出完毕后回显用户已有的输入或者Y/N确认信息，以便用户继续执行配置。

【举例】

\# 开启设备命令行输入回显功能，输入**display** **current-configuration**命令查看设备当前配置。

\<Sysname\> system-view

Sysname info-center synchronous

Info-center synchronous output is on

Sysname display current-

此时，收到日志报文，则系统在所有的日志报文显示完以后，附加显示用户的输入（此例为"display current-"）。

%May 21 14:33:19:425 2007 Sysname SHELL/4/LOGIN: VTY login from 192.168.1.44

Sysname display current-

此时，用户可以继续输入configuration（完成命令**display current-configuration**的完整输入），回车，即可执行该命令。

\# 开启设备命令行输入回显功能，保存当前配置（输入交互信息）。

\<Sysname\> system-view

Sysname info-center synchronous

Info-center synchronous output is on

Sysname save

The current configuration will be written to the device. Are you sure? [Y/N:]

此时，收到日志信息，则系统会在所有的日志报文显示完以后，附加显示 Y/N:。

%May 21 14:33:19:425 2007 Sysname SHELL/4/LOGIN: VTY login from 192.168.1.44

Y/N:

此时，用户可以输入Y或者N，继续日志信息输出前的操作。

**信息中心 \-- 信息中心配置命令 \-- info-center timestamp**

------------------------------------------------------------------------

**[info-center** **timestamp**]命令用来设置发往控制台、监视终端、日志缓冲区和日志文件方向的日志信息的时间戳输出格式。

**[undo** **info-center** **timestamp**]命令用来恢复缺省情况。

【命令】

**[info-center** **timestamp**[ { **boot** \| **date** \| **none** }]]

**[undo**] **info-center** **timestamp**

【缺省情况】

时间戳输出格式为**date**格式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[boot**]：系统启动后经历的时间，格式为：xxx.yyy，其中xxx是系统自启动后经历时间的毫秒数高32位，yyy是低32位，形如0.21990989（等效于Jun 25 14:09:26:881 2007）。

**[date**]：系统当前的日期和时间，格式为"MMM DD hh:mm:ss:xxx YYYY"，形如Dec  8 10:12:21:708 2007。

·"MMM"为英语月份的缩写，具体取值如下：Jan，Feb，Mar，Apr，May，Jun，Jul，Aug，Sep，Oct，Nov，Dec。

·"DD"表示日期，如果日期的值小于10，则格式为"空格＋日期"，如" 7"。

·"hh:mm:ss:xxx"表示本地时间，hh的取值范围为00～23，mm和ss的取值范围均为00～59，xxx的取值范围为0～999。

·"YYYY"表示年份。

**[none**]：不带时间信息。

【举例】

\# 设置日志信息时间戳输出格式为boot格式。

\<Sysname\> system-view

Sysname info-center timestamp boot

【相关命令】

·**info-center** **timestamp** **loghost**

**信息中心 \-- 信息中心配置命令 \-- info-center timestamp loghost**

------------------------------------------------------------------------

**[info-center** **timestamp** **loghost**]命令用来设置发往日志主机的日志信息的时间戳输出格式。

**[undo** **info-center** **timestamp** **loghost**]命令用来恢复缺省情况。

【命令】

**[info-center** **timestamp**[ **loghost** { **date** \| **iso** \| **no-year-date** \| **none** }]]

**[undo** **info-center** **timestamp** **loghost**]

【缺省情况】

发往日志主机的日志信息的时间戳输出格式为**date**格式。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[date**]：系统当前日期和时间，格式为：mmm dd hh:mm:ss yyyy，形如Dec  8 10:12:21 2007，但最终显示格式由日志主机决定。

**[iso**]：设置时间戳采用ISO 8601标准格式，形如：2009-09-21T15:32:55。

**[no-year-date**]：系统当前日期和时间，但不包含年份信息。

**[none**]：不带时间信息。

【举例】

\# 设置发往日志主机的日志信息的时间戳为no-year-date格式。

\<Sysname\> system-view

Sysname info-center timestamp loghost no-year-date

【相关命令】

·**info-center** **timestamp**

**信息中心 \-- 信息中心配置命令 \-- info-center trace-logfile quota**

------------------------------------------------------------------------

**[info-center trace-logfile quota**]命令用来设置调试跟踪日志文件最大能占用的存储空间的大小。

**[undo info-center trace-logfile quota**]命令用来恢复缺省情况。

【命令】

**[info-center trace-logfile quota **]*size*

**[undo info-center trace-logfile quota**]

【缺省情况】

缺省情况下，调试跟踪日志文件最大能占用的存储空间的大小为1MB。

【视图】

系统视图

【支持的缺省用户角色】

network-admin

mdc-admin

【参数】

*[size*]：调试跟踪日志文件最大能占用的存储空间的大小，单位为MB。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【举例】

\# 设置调试跟踪日志文件最大能占用的存储空间的大小为6MB。

\<Sysname\> system-view

Sysname info-center trace-logfile quota 6

**信息中心 \-- 信息中心配置命令 \-- logfile save**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[logfile** **save**]命令用来手动将日志文件缓冲区中的内容全部保存到日志文件。

【命令】

**[logfile** **save**]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

日志文件的保存路径可以通过**info-center** **logfile** **directory**命令设置。

日志文件保存成功后，日志文件缓冲区中的内容会被清空。

【举例】

\# 手动将日志文件缓冲区中的内容保存到日志文件。

\<Sysname\> logfile save

The contents in the log file buffer have been saved to the file flash:/logfile/logfile.log.

【相关命令】

·**info-center** **logfile** **enable**

·**info-center** **logfile** **directory**

**信息中心 \-- 信息中心配置命令 \-- reset logbuffer**

------------------------------------------------------------------------

**[reset** **logbuffer**]命令用来清除日志缓冲区中的信息。

【命令】

**[reset** **logbuffer**]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 清除日志缓冲区中的信息。

\<Sysname\> reset logbuffer

【相关命令】

·**display** **logbuffer**

**信息中心 \-- 信息中心配置命令 \-- security-logfile save**

------------------------------------------------------------------------

![说明](信息中心命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[security-logfile**] **save**命令用来手动将安全日志文件缓冲区中的内容全部保存到安全日志文件。

【命令】

**[security-logfile**] **save**

【视图】

任意视图

【缺省用户角色】

security-audit

【使用指导】

安全日志文件保存成功后，安全日志文件缓冲区中的内容会被立即清空。

需要注意的是，只有配置了安全日志管理员权限的本地用户才能使用本命令。安全日志管理员的配置请参见"安全命令参考"中的"AAA"。

【举例】

\# 手动将安全日志缓冲区中的内容保存到安全日志文件。

\<Sysname\> security-logfile save

The contents in the security log file buffer have been saved to the file flash:/seclog/seclog.log.

【相关命令】

·**info-center** **security-logfile** **switch-directory**

·**authorization-attribute**（安全命令参考/AAA）

**信息中心 \-- 信息中心配置命令 \-- terminal debugging**

------------------------------------------------------------------------

**[terminal** **debugging**]命令用来开启当前终端对调试信息的显示功能。

**[undo** **terminal** **debugging**]命令用来关闭当前终端对调试信息的显示功能。

【命令】

**[terminal** **debugging**]

**[undo** **terminal** **debugging**]

【缺省情况】

当前终端对调试信息的显示功能处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果需要在控制台显示调试信息，请先配置**terminal** **debugging**命令，再使能信息中心功能（信息中心功能缺省处于使能状态），最后使用**debugging**命令打开功能模块的调试信息开关。

如果需要在监控终端上显示调试信息，请先配置**terminal** **monitor**和**terminal** **debugging**命令，再使能信息中心功能（信息中心功能缺省处于使能状态），最后使用**debugging**命令打开功能模块的调试信息开关。

需要注意的是，本命令只对当前连接有效。当终端与设备重新建立连接后，本命令会恢复到缺省情况。

执行**terminal logging level** 7命令或**terminal debugging**命令，都可以开启当前终端对调试信息的显示功能，但两条命令有如下区别：

·执行**terminal logging level** 7命令，当前终端允许输出级别为0～7的所有日志。

·执行**terminal debugging**命令，当前终端仅输出**terminal logging level**命令设置的日志信息和级别为7的调试信息。

【举例】

\# 允许debugging日志信息输出到控制台或者监视终端。

\<Sysname\> terminal debugging

The current terminal is enabled to display debugging information.

【相关命令】

·**terminal logging level**

·**terminal monitor**

**信息中心 \-- 信息中心配置命令 \-- terminal logging level**

------------------------------------------------------------------------

**[terminal** **logging** **level**]命令用来配置当前终端允许输出的日志信息的最低级别。

**[undo** **terminal** **logging** **level**]命令用来恢复缺省情况。

【命令】

**[terminal** **logging** **level** *severity*]

**[undo** **terminal** **logging** **level**]

【缺省情况】

当前终端允许输出的日志信息的最低级别均为6（Informational）。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[severity*]：当前终端允许输出的日志信息的最低级别，取值范围为0～7。

【使用指导】

在配置了当前终端允许输出的日志信息的最低级别后，当系统输出信息时，所有信息等级高于或等于设置等级的信息都会被输出。例如，当配置的允许输出的日志信息的最低级别6（informational）时，等级0～6的信息均会被输出。

本命令配置的显示属性只对当前连接有效，当终端与设备的连接超时、重新建立连接后，显示属性将恢复到缺省情况。

【举例】

\# 配置当前终端监控的最低日志级别为debugging。

\<Sysname\> terminal logging level 7

**信息中心 \-- 信息中心配置命令 \-- terminal monitor**

------------------------------------------------------------------------

**[terminal** **monitor**]命令用来允许日志信息输出到当前终端。

**[undo** **terminal** **monitor**]命令用来禁止日志信息输出到当前终端。

【命令】

**[terminal** **monitor**]

**[undo** **terminal** **monitor**]

【缺省情况】

允许日志信息输出到控制台，不允许日志信息输出到监视终端。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

本命令只对当前连接有效。当终端与设备重新建立连接后，本命令会恢复到缺省情况。

【举例】

\# 允许日志信息输出到监视终端。

\<Sysname\> terminal monitor

The current terminal is enabled to display logs.
