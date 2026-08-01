<!-- CMD-INDEX
  display session aging-time application | 任意视图             | L24
  display session aging-time state    | 任意视图             | L108
  display session relation-table      | 任意视图             | L196
  display session statistics          | 任意视图             | L424
  display session table ipv4          | 任意视图             | L720
  display session table ipv6          | 任意视图             | L1212
  reset session table ipv4            | 用户视图             | L1568
  reset session table ipv6            | 用户视图             | L1642
  reset session table                 | 用户视图             | L1716
  reset session statistics            | 用户视图             | L1772
  reset session relation-table        | 用户视图             | L1826
  session aging-time application      |                  | L1888
  session aging-time state            |                  | L2012
  session log bytes-active            | 系统视图             | L2102
  session log enable                  | 接口视图             | L2160
  session log packets-active          | 系统视图             | L2246
  session log time-active             | 系统视图             | L2304
  session statistic enable            | 系统视图             | L2362
  session persistent acl              | 系统视图             | L2408
  session synchronization enable      | 系统视图             | L2472
-->

**会话管理 \-- 会话管理配置命令 \-- display session aging-time application**

------------------------------------------------------------------------

**[display session aging-time application**]命令用来显示应用层协议的会话老化时间。

【命令】

**[display session aging-time application**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示当前各应用层协议的会话老化时间。

\<Sysname\> display session aging-time application

Application         Aging Time(s)

DNS                 60

FTP                 3600

GTP                 60

H225                3600

H245                3600

RAS                 300

RTSP                3600

SIP                 300

TFTP                60

ILS                 3600

MGCP                60

NBT                 3600

PPTP                3600

RSH                 60

SCCP                3600

SQLNET              600

XDMCP               3600

表1-1 display session aging-time application命令显示信息描述表

字段

描述

Application

应用层协议类型

Aging Time(s)

会话老化时间，单位为秒

【相关命令】

·**application aging-time**

**会话管理 \-- 会话管理配置命令 \-- display session aging-time state**

------------------------------------------------------------------------

**[display session aging-time state**]命令用来显示各协议状态的会话老化时间。

【命令】

**[display session aging-time state**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示当前各协议状态的会话老化时间。

\<Sysname\> display session aging-time state

State                     Aging Time(s)

SYN                       10

TCP-EST                   3600

FIN                       10

UDP-OPEN                  10

UDP-READY                 30

ICMP-REQUEST              30

ICMP-REPLY                10

RAWIP-OPEN                30

RAWIP-READY               60

UDPLITE-OPEN              30

UDPLITE-READY             60

DCCP-REQUEST              30

DCCP-EST                  3600

DCCP-CLOSEREQ             30

SCTP-INIT                 30

SCTP-EST                  3600

SCTP-SHUTDOWN             30

ICMPV6-REQUEST            60

ICMPV6-REPLY              30

表1-2 display session aging-time state命令显示信息描述表

字段

描述

State

各协议的状态类型

Aging Time(s)

会话老化时间，单位为秒

【相关命令】

·**session aging-time state**

**会话管理 \-- 会话管理配置命令 \-- display session relation-table**

------------------------------------------------------------------------

**[display session relation-table**]命令用来显示关联表项信息。

【命令】

集中式设备：

**[display session relation-table **[{ **ipv4** \| **ipv6** } ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display session relation-table **[{ **ipv4** \| **ipv6** } [ **slot** *slot-number* [ **cpu** *cpu-number* ] ]]]

分布式设备－IRF模式：

**[display session relation-table **[{ **ipv4** \| **ipv6** } ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4**]：显示IPv4关联表项。

**[ipv6**]：显示IPv6关联表项。

**[slot** *slot-number*]：显示指定单板上的关联表项信息，*slot-number*表示单板所在槽位号。不指定该参数时，显示所有单板上的关联表项信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的关联表项信息，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的关联表项信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的关联表项信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的关联表项信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的关联表项信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的关联表项信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的关联表项信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的关联表项信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的关联表项信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有的IPv4关联表项。（集中式设备）

\<Sysname\> display session relation-table ipv4

Source IP/port:      192.168.1.100/-

Destination IP/port: 192.168.2.100/99

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: 1/-/-

Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA

Source IP/port:      -/-

Destination IP/port: 192.168.2.200/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 3100s    App: H225

Total entries found:  2

\# 显示所有的IPv4关联表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session relation-table ipv4

Slot 1：

Source IP/port:      192.168.1.100/-

Destination IP/port: 192.168.2.100/99

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: 1/-/-

Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA

Source IP/port:      -/-

Destination IP/port: 192.168.2.200/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 3100s    App: H225

Total entries found:  2

\# 显示所有的IPv6关联表项。（集中式设备）

\<Sysname\> display session relation-table ipv6

Source IP:             2011::0002

Destination IP/port: 2011::0008/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 567s    App: FTP-DATA

Total entries found:  1

\# 显示所有的IPv6关联表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session relation-table ipv6

Slot 1：

Source IP:             2011::0002

Destination IP/port: 2011::0008/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 567s    App: FTP-DATA

Total entries found:  1

\# 显示所有的IPv4关联表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session relation-table ipv4

CPU 0 on slot 1：

Source IP/port:      192.168.1.100/-

Destination IP/port: 192.168.2.100/99

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: 1/-/-

Protocol: TCP(6)    TTL: 1234s    App: FTP-DATA

Source IP/port:      -/-

Destination IP/port: 192.168.2.200/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 3100s    App: H225

Total entries found:  2

\# 显示所有的IPv6关联表项。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session relation-table ipv6

CPU 0 on slot 1：

Source IP:             2011::0002

Destination IP/port: 2011::0008/1212

DS-Lite tunnel peer: -

VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: TCP(6)    TTL: 567s    App: FTP-DATA

Total entries found:  1

表1-3 display session relation-table命令显示信息描述表

字段

描述

Source IP/port

会话的源IP地址和端口号。如果未指定则显示"-/-"

IPv6会话无源端口号字段

Destination IP/port

会话的目的IP地址/端口号

DS-Lite tunnel peer

会话所属的DS-Lite隧道对端地址。未指定的参数则显示为"-"

VPN instance/VLAN ID/VLL ID

关联表项所属的MPLS L3VPN/二层转发时会话所属的VLAN ID/二层转发时会话所属的INLINE。未指定的参数则显示为"-"

Protocol

传输层协议类型

TTL

关联表的剩余存活时间，单位为秒

App

应用层协议类型

Total entries found

当前查找到的关联表总数

**会话管理 \-- 会话管理配置命令 \-- display session statistics**

------------------------------------------------------------------------

**[display session statistics**]命令用来显示会话统计信息。

【命令】

集中式设备：

**[display session statistics ** **summary** ]

分布式设备－独立运行模式/集中式IRF设备：

**[display session statistics ** **summary**   **slot** *slot-number* [ **cpu** *cpu-number*  ] ]

分布式设备－IRF模式：

**[display session statistics ** **summary** ]******chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[summary**]：显示会话统计信息的概要信息。不指定该参数时，显示会话统计信息的详细信息。

**[slot** *slot-number*]：显示指定单板上的会话统计信息，*slot-number*表示单板所在槽位号。不指定该参数时，显示所有单板上的会话统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的会话统计信息，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的会话统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的会话统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的会话统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的会话统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的会话统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的会话统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的会话统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的会话统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示所有会话统计信息的详细信息。

\<Sysname\> display session statistics

Current sessions: 3

     TCP sessions: 0

            TCP_SYN_SENT: 0                    TCP_SYN_RECV: 0

         TCP_ESTABLISHED: 0                    TCP_FIN_WAIT: 0

          TCP_CLOSE_WAIT: 0                    TCP_LAST_ACK: 0

           TCP_TIME_WAIT: 0                       TCP_CLOSE: 0

           TCP_SYN_SENT2: 0

     UDP sessions: 0

                UDP_OPEN: 0                       UDP_READY: 0

     ICMP sessions: 3

            ICMP_REQUEST: 0                      ICMP_REPLY: 3

     ICMPv6 sessions: 0

            ICMP_REQUEST: 0                      ICMP_REPLY: 0

     UDP-Lite sessions: 0

            UDPLITE_OPEN: 0                   UDPLITE_READY: 0

     SCTP sessions: 0

             SCTP_CLOSED: 0                SCTP_COOKIE_WAIT: 0

      SCTP_COOKIE_ECHOED: 0                SCTP_ESTABLISHED: 0

      SCTP_SHUTDOWN_SENT: 0              SCTP_SHUTDOWN_RECD: 0

  SCTP_SHUTDOWN_ACK_SENT: 0

     DCCP sessions: 0

            DCCP_REQUEST: 0                    DCCP_RESPOND: 0

           DCCP_PARTOPEN: 0                       DCCP_OPEN: 0

           DCCP_CLOSEREQ: 0                    DCCP_CLOSING: 0

           DCCP_TIMEWAIT: 0

     RAWIP sessions: 0

              RAWIP_OPEN: 0                     RAWIP_READY: 0

Current relation-table entries: 0

Session establishment rate: 0/s

          TCP:                   0/s

          UDP:                   0/s

         ICMP:                   0/s

       ICMPv6:                   0/s

     UDP-Lite:                   0/s

         SCTP:                   0/s

         DCCP:                   0/s

        RAWIP:                   0/s

Received TCP      :                   0 packets                    0 bytes

Received UDP      :                 118 packets                13568 bytes

Received ICMP     :                 105 packets                 8652 bytes

Received ICMPv6   :                   0 packets                    0 bytes

Received UDP-Lite :                   0 packets                    0 bytes

Received SCTP     :                   0 packets                    0 bytes

Received DCCP     :                   0 packets                    0 bytes

Received RAWIP    :                   0 packets                    0 bytes

表1-4 display session statistics命令显示信息描述表

字段

描述

Current sessions

系统当前的总会话数

TCP sessions

系统当前的TCP会话数，以及各协议状态下的会话数

UDP sessions

系统当前的UDP会话数，以及各协议状态下的会话数

ICMP sessions

系统当前的ICMP会话数，以及各协议状态下的会话数

ICMPv6 sessions

系统当前的ICMPv6会话数，以及各协议状态下的会话数

UDP-Lite sessions

系统当前的UDP-Lite会话数，以及各协议状态下的会话数

SCTP sessions

系统当前的SCTP会话数，以及各协议状态下的会话数

DCCP sessions

系统当前的DCCP会话数，以及各协议状态下的会话数

RAWIP sessions

系统当前的Raw IP会话数，以及各协议状态下的会话数

Current relation-table entries

总关联表项个数

Session establishment rate

系统创建会话的速率，以及创建各协议会话的速率

Received TCP

系统当前收到的TCP报文数、报文字节数

Received UDP

系统当前收到的UDP报文数、报文字节数

Received ICMP

系统当前收到的ICMP报文数、报文字节数

Received ICMPv6

系统当前收到的ICMPv6报文数、报文字节数

Received UDP-Lite

系统当前收到的UDP-Lite报文数、报文字节数

Received SCTP

系统当前收到的SCTP报文数、报文字节数

Received DCCP

系统当前收到的DCCP报文数、报文字节数

Received RAWIP

系统当前收到的Raw IP报文数、报文字节数

\# 显示所有会话统计信息的概要信息。（集中式设备）

\<Sysname\> display session statistics summary

Sessions  TCP       UDP       Rate      TCP rate  UDP rate

3         0         0         0/s       0/s       0/s

\# 显示会话统计信息的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session statistics summary

Slot CPU Sessions  TCP       UDP       Rate      TCP rate  UDP rate

2    1   3         0         0         0/s       0/s       0/s

\# 显示会话统计信息的概要信息。（分布式设备－IRF模式）

\<Sysname\> display session statistics summary

Chassis Slot CPU Sessions  TCP       UDP       Rate      TCP rate  UDP rate

1       2    1   3         0         0         0/s       0/s       0/s

表1-5 display session statistics summary命令显示信息描述表

字段

描述

Chassis

IRF成员编号（分布式设备－IRF模式）

Slot

单板所在的槽位号（分布式设备－独立运行模式）

IRF中的成员编号（集中式IRF设备）

CPU

CPU编号

Sessions

系统当前的总会话数

TCP

系统当前的TCP会话数

UDP

系统当前的UDP会话数

Rate

系统创建会话的速率

TCP rate

系统创建TCP会话的速率

UDP rate

系统创建UDP会话的速率

**会话管理 \-- 会话管理配置命令 \-- display session table ipv4**

------------------------------------------------------------------------

**[display session table ipv4**]命令用来显示IPv4会话表项信息。

【命令】

集中式设备：

**[display session table** **ipv4** [ **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display session table** **ipv4** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]]

分布式设备－IRF模式：

**[display session table** **ipv4** **chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板上的IPv4会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，显示所有单板上的IPv4会话表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv4会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的IPv4会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的IPv4会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的IPv4会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的IPv4会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的IPv4会话表项。（分布式IRF设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的IPv4会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的IPv4会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv4会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[source-ip** *start*-*source-ip* [ *end-source-ip* ]]：显示指定源IP地址的会话表项。其中，*start*-*source-ip*表示发起方到响应方会话的起始源IPv4地址，*end-source-ip*表示发起方到响应方会话的结束源IPv4地址。

**[destination-ip** *start*-*destination-ip* [ *end-destination-ip* ]]：显示指定目的IPv4地址的会话表项。其中，*start*-*destination-ip*表示发起方到响应方会话的起始目的IPv4地址，*end-destination-ip*表示发起方到响应方会话的结束目的IPv4地址。

**[protocol**[ { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]]：显示指定协议类型的IPv4会话表项。其中，IPv4传输层协议类型可包括：DCCP、ICMP、RawIP、SCTP、TCP、UDP和UDP-Lite。

**[source-port** *source-port*]：显示指定源端口号的IPv4会话表项。其中，*source-port*表示发起方到响应方会话的源端口号，取值为0～65535。

**[destination-port** *destination-port*]：显示指定目的端口号的IPv4会话表项。其中，*destination-port*表示发起方到响应方会话的目的端口号，取值为0～65535。

**[verbose**]：显示IPv4会话表项的详细信息。不指定该参数时，显示IPv4会话表项的概要信息。

【使用指导】

如果不指定任何参数，则显示所有的IPv4会话表项。

【举例】

\# 显示所有的IPv4会话表项的概要信息。（集中式设备）

\<Sysname\> display session table ipv4

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Total sessions found: 2

\# 显示所有的IPv4会话表项的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv4

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Total sessions found: 2

\# 显示所有的IPv4会话表项的详细信息。（集中式设备）

\<Sysname\> display session table ipv4 verbose

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         60 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

\# 显示所有的IPv4会话表项的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv4 verbose

Slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         60 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

\# 显示所有的IPv4会话表项的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv4 verbose

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 192.168.1.18/1877

  Destination IP/port: 192.168.1.55/22

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/22

  Destination IP/port: 192.168.1.18/1877

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: TCP(6)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: TCP_SYN_SENT

Application: SSH

Start time: 2011-07-29 19:12:36  TTL: 28s

Initiator-\>Responder:         1 packets         48 bytes

Responder-\>Initiator:         0 packets          0 bytes

Initiator:

  Source      IP/port: 192.168.1.18/1792

  Destination IP/port: 192.168.1.55/2048

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 192.168.1.55/1792

  Destination IP/port: 192.168.1.18/0

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: ICMP(1)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMP_REQUEST

Application: OTHER

Start time: 2011-07-29 19:12:33  TTL: 55s

Initiator-\>Responder:         1 packets         60 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 2

表1-6 display session table命令显示信息描述表

字段

描述

Initiator

发起方到响应方的连接对应的会话信息

Responder

响应方到发起方的连接对应的会话信息

Source IP/port

源IP地址/端口号

Destination IP/port

目的IP地址/端口号

DS-Lite tunnel peer

DS-Lite隧道对端地址。会话不属于任何DS-Lite隧道时，本字段显示为"-"

VPN instance/VLAN ID/VLL ID

会话所属的MPLS L3VPN/二层转发时会话所属的VLAN ID/二层转发时会话所属的INLINE。未指定的参数则显示为"-"

Protocol

传输层协议类型，取值包括：DCCP、ICMP、ICMPv6、Raw IP、SCTP、TCP、UDP、UDP-Lite

括号中的数字表示协议号

Inbound interface

报文的入接口

Source security zone

源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"-"

该参数的支持情况与设备的型号有关，请以设备的实际情况为准

State

会话状态

Application

应用层协议类型，取值包括：FTP、DNS等，OTHER表示未知协议类型，其对应的端口为非知名端口

Start time

会话创建时间

TTL

会话剩余存活时间，单位为秒

Initiator-\>Responder

发起方到响应方的报文数、报文字节数

Responder-\>Initiator

响应方到发起方的报文数、报文字节数

Total sessions found

当前查找到的会话表项总数

**会话管理 \-- 会话管理配置命令 \-- display session table ipv6**

------------------------------------------------------------------------

**[display session table ipv6**]命令用来显示IPv6会话表项信息。

【命令】

集中式设备：

**[display session table** **ipv6** [ **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display session table** **ipv6** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]]

分布式设备－IRF模式：

**[display session table** **ipv6** **chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *start*-*source-ip* [ *end-source-ip*  ]  **destination-ip** *start*-*destination-ip* [ *end-destination-ip*    **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[slot** *slot-number*]：显示指定单板上的IPv6会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，显示所有单板上的IPv6会话表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：显示指定成员设备上的IPv6会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，显示所有成员设备上的IPv6会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：显示指定成员设备/PEX上的IPv6会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。若不指定该参数，则表示显示所有成员设备/PEX上的IPv6会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定成员设备的指定单板上的IPv6会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的IPv6会话表项。（分布式IRF设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示指定单板上的IPv6会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。若不指定该参数，则表示显示所有单板上的IPv6会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：显示指定CPU上的IPv6会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[source-ip** *start*-*source-ip* [ *end-source-ip* ]]：显示指定源IPv6地址的会话表项。其中，*start*-*source-ip*表示发起方到响应方会话的起始源IPv6地址，*end-source-ip*表示发起方到响应方会话的结束源IPv6地址。

**[destination-ip** *destination-ip-start* [*destination-ip-end* ]]：显示指定目的IPv6地址的会话表项。其中，*start*-*destination-ip*表示发起方到响应方会话的起始目的IPv6地址，*end-destination-ip*表示发起方到响应方会话的结束目的IPv6地址。

**[protocol**[ { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]]：显示指定协议类型的IPv6会话表项。其中，IPv6传输层协议类型可包括：DCCP、ICMPv6、RawIP、SCTP、TCP、UDP和UDP-Lite。

**[source-port** *source-port*]：显示指定源端口号的IPv6会话表项。其中，*source-port*表示发起方到响应方IPv6会话的源端口号，取值为0～65535。

**[destination-port** *destination-port*]：显示指定目的端口号的IPv6会话表项。其中，*destination-port*表示发起方到响应方IPv6会话的目的端口号，取值为0～65535。

**[verbose**]：显示IPv6会话表项的详细信息。不指定该参数时，显示IPv6会话表项的概要信息。

【使用指导】

如果不指定任何参数，则显示所有的IPv6会话表项。

【举例】

\# 显示所有的IPv6会话表项的概要信息。（集中式设备）

\<Sysname\> display session table ipv6

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Total sessions found: 1

\# 显示所有的IPv6会话表项的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv6

Slot 1:

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Total sessions found: 1

\# 显示所有的IPv6会话表项的详细信息。（集中式设备）

\<Sysname\> display session table ipv6 verbose

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 2011::8/58473

  Destination IP/port: 2011::2/33024

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMPV6_REQUEST

Application: OTHER

Start time: 2011-07-29 19:23:41  TTL: 55s

Initiator-\>Responder:         1 packets         104 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示所有的IPv6会话表项的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv6 verbose

Slot 1:

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 2011::8/58473

  Destination IP/port: 2011::2/33024

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMPV6_REQUEST

Application: OTHER

Start time: 2011-07-29 19:23:41  TTL: 55s

Initiator-\>Responder:         1 packets         104 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

\# 显示所有的IPv6会话表项的概要信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv6

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Total sessions found: 1

\# 显示所有的IPv6会话表项的详细信息。（分布式设备－独立运行模式/集中式IRF设备）

\<Sysname\> display session table ipv6 verbose

CPU 0 on slot 1:

Initiator:

  Source      IP/port: 2011::2/58473

  Destination IP/port: 2011::8/32768

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/1

  Source security zone: Trust

Responder:

  Source      IP/port: 2011::8/58473

  Destination IP/port: 2011::2/33024

  DS-Lite tunnel peer: -

  VPN instance/VLAN ID/VLL ID: -/-/-

  Protocol: IPV6-ICMP(58)

  Inbound interface: GigabitEthernet1/0/2

  Source security zone: Local

State: ICMPV6_REQUEST

Application: OTHER

Start time: 2011-07-29 19:23:41  TTL: 55s

Initiator-\>Responder:         1 packets         104 bytes

Responder-\>Initiator:         0 packets          0 bytes

Total sessions found: 1

表1-7 display session table命令显示信息描述表

字段

描述

Initiator

发起方到响应方的连接对应的会话信息

Responder

响应方到发起方的连接对应的会话信息

Source IP/port

源IP地址/端口号

Destination IP/port

目的IP地址/端口号

DS-Lite tunnel peer

DS-Lite隧道对端地址。会话不属于任何DS-Lite隧道时，本字段显示为"-"

VPN instance/VLAN ID/VLL ID

会话所属的MPLS L3VPN/二层转发时会话所属的VLAN ID/二层转发时会话所属的INLINE。未指定的参数则显示为"-"

Protocol

传输层协议类型，取值包括：DCCP、ICMP、ICMPv6、Raw IP、SCTP、TCP、UDP、UDP-Lite

括号中的数字表示协议号

Inbound interface

报文的入接口

Source security zone

源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"-"

该参数的支持情况与设备的型号有关，请以设备的实际情况为准

State

会话状态

Application

应用层协议类型，取值包括：FTP、DNS等，OTHER表示未知协议类型，其对应的端口为非知名端口

Start time

会话创建时间

TTL

会话剩余存活时间，单位为秒

Initiator-\>Responder

发起方到响应方的报文数、报文字节数

Responder-\>Initiator

响应方到发起方的报文数、报文字节数

Total sessions found

当前查找到的会话表项总数

**会话管理 \-- 会话管理配置命令 \-- reset session table ipv4**

------------------------------------------------------------------------

**[reset session table ipv4**]命令用来删除IPv4会话表项。

【命令】

集中式设备：

**[reset session** **table ipv4** [ **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name*  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset session table** **ipv4** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port**  *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name* ]]

分布式设备－IRF模式：

**[reset session table** **ipv4** **chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port**  *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：删除指定单板上的IPv4会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，删除所有单板上的IPv4会话表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：删除指定成员设备上的IPv4会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，删除所有成员设备上的IPv4会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：删除指定成员设备/PEX上的IPv4会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，删除所有成员设备/PEX上的IPv4会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定成员设备的指定单板上的IPv4会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的IPv4会话表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定单板上的IPv4会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，删除所有单板上的IPv4会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：删除指定CPU上的IPv4会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[source-ip** *source-ip*]：删除指定源IP地址的IPv4会话表项。其中，*source-ip*表示发起方到响应方会话的源IPv4地址。

**[destination-ip** *destination-ip*]：删除指定目的IP地址的IPv4会话表项。其中，*destination-ip*表示发起方到响应方会话的目的IPv4地址。

**[protocol**[ { **dccp** \| **icmp** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]]：删除指定协议类型的会话表项。其中，IPv4传输层协议类型可包括：DCCP、ICMP、RawIP、SCTP、TCP、UDP和UDP-Lite。

**[source-port** *source-port*]：删除指定源端口号的IPv4会话表项。其中，*source-port*表示发起方到响应方会话的源端口号，取值为0～65535。

**[destination-port** *destination-port*]：删除指定目的端口号的IPv4会话表项。其中，*destination-port*表示发起方到响应方会话的目的端口号，取值为0～65535。

**[vpn-instance ***vpn-instance-name*]：删除指定VPN的IPv4会话表项。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。不指定该参数时，删除公网中的IPv4会话表项。

【使用指导】

如果不指定任何参数，则删除所有公网中的IPv4会话表项。

【举例】

\# 删除所有IPv4会话表项。

\<Sysname\> reset session table ipv4

\# 删除所有发起方源IP地址为10.10.10.10的IPv4会话表项。

\<Sysname\> reset session table ipv4 source-ip 10.10.10.10

【相关命令】

·**display session table ipv4**

**会话管理 \-- 会话管理配置命令 \-- reset session table ipv6**

------------------------------------------------------------------------

**[reset session table ipv6**]命令用来删除IPv6会话表项。

【命令】

集中式设备：

**[reset session** **table ipv6** [ **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name*  ]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset session table ipv6 **[ **slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port**  *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name* ]]

分布式设备－IRF模式：

**[reset session table** **ipv6** **chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]  **source-ip** *source-ip*   **destination-ip** *destination-ip*  [ **protocol** { **dccp** \| **icmpv6**  \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** } ]  **source-port** *source-port*   **destination-port** *destination-port*   **vpn-instance** *vpn-instance-name* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：删除指定单板上的IPv6会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，删除所有单板上的IPv6会话表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：删除指定成员设备上的IPv6会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，删除所有成员设备上的IPv6会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：删除指定成员设备/PEX上的IPv6会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，删除所有成员设备/PEX上的IPv6会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定成员设备的指定单板上的IPv6会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的IPv6会话表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定单板上的IPv6会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，删除所有单板上的IPv6会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：删除指定CPU上的IPv6会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

**[source-ip** *source-ip*]：删除指定源IP地址的IPv6会话表项。其中，*source-ip*表示发起方到响应方会话的源IPv6地址。

**[destination-ip** *destination-ip*]：删除指定目的IP地址的IPv6会话表项。其中，*destination-ip*表示发起方到响应方会话的目的IPv6地址。

**[protocol**[ { **dccp** \| **icmpv6** \| **raw-ip** \| **sctp** \| **tcp** \| **udp** \| **udp-lite** }]]：删除指定协议类型的IPv6会话表项。其中，IPv6传输层协议类型可包括：DCCP、ICMPv6、RawIP、SCTP、TCP、UDP和UDP-Lite。

**[source-port** *source-port*]：删除指定源端口号的IPv6会话表项。其中，*source-port*表示发起方到响应方会话的源端口号，取值为0～65535。

**[destination-port** *destination-port*]：删除指定目的端口号的IPv6会话表项。其中，*destination-port*表示发起方到响应方会话的目的端口号，取值为0～65535。

**[vpn-instance ***vpn-instance-name*]：删除指定VPN的IPv6会话表项。其中，*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。不指定该参数时，删除公网中的IPv6会话表项。

【使用指导】

如果不指定任何参数，则删除所有公网中的IPv6会话表项。

【举例】

\# 删除所有IPv6会话表项。

\<Sysname\> reset session table ipv6

\# 删除所有发起方源IP地址为2011::0002的IPv6会话表项。

\<Sysname\> reset session table ipv6 source-ip 2011::0002

【相关命令】

·**display session table ipv6**

**会话管理 \-- 会话管理配置命令 \-- reset session table**

------------------------------------------------------------------------

**[reset session table**]命令用来删除所有会话表项，包括IPv4和IPv6会话表项。

【命令】

集中式设备：

**[reset session table**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset session table ** **slot** *slot-number*  **cpu** *cpu-number*  ]

分布式设备－IRF模式：

**[reset session table ****chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：删除指定单板上的所有会话表项，*slot-number*表示单板所在槽位号。不指定该参数时，删除所有单板上的所有会话表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：删除指定成员设备上的所有会话表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，删除所有成员设备上的所有会话表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：删除指定成员设备/PEX上的所有会话表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，删除所有成员设备/PEX上的所有会话表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定成员设备的指定单板上的所有会话表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的所有会话表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定单板上的所有会话表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，删除所有单板上的所有会话表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：删除指定CPU上的所有会话表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 删除所有会话表项。

\<Sysname\> reset session table

【相关命令】

·**display session table**** ipv4**

·**display session table**** ipv6**

**会话管理 \-- 会话管理配置命令 \-- reset session statistics**

------------------------------------------------------------------------

**[reset session statistics**]命令用来清除会话统计信息。

【命令】

集中式设备：

**[reset session statistics**]

分布式设备－独立运行模式/集中式IRF设备：

**[reset session statistics** [ **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset session statistics** **chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[slot** *slot-number*]：清除指定单板的上会话统计信息，*slot-number*表示单板所在槽位号。不指定该参数时，清除所有单板上的会话统计信息。（分布式设备－独立运行模式）

**[slot** *slot-number*]：清除指定成员设备上的会话统计信息，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，清除所有成员设备上的会话统计信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：清除指定成员设备/PEX上的会话统计信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，清除所有成员设备/PEX上的会话统计信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定成员设备的指定单板上的会话统计信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，清除所有成员设备的所有单板上的会话统计信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：清除指定单板上的会话统计信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，清除所有单板上的会话统计信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：清除指定CPU上的会话统计信息，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 清除所有的会话统计信息。

\<Sysname\> reset session statistics

【相关命令】

·**display session statistics**

**会话管理 \-- 会话管理配置命令 \-- reset session relation-table**

------------------------------------------------------------------------

**[reset session** **relation-table**]命令用来删除关联表项。

【命令】

集中式设备：

**[reset session**[ **relation-table** [ **ipv4** \| **ipv6** ] ]]

分布式设备－独立运行模式/集中式IRF设备：

**[reset session**[ **relation-table** [ **ipv4** \| **ipv6** ]  **slot** *slot-number* [ **cpu** *cpu-number*  ]]]

分布式设备－IRF模式：

**[reset session**[ **relation-table** [ **ipv4** \| **ipv6** ] ]**chassis** *chassis-number*** slot** *slot-number* [ **cpu** *cpu-number*  ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：删除IPv4关联表项。

**[ipv6**]：删除IPv6关联表项。

**[slot** *slot-number*]：删除指定单板上的关联表项，*slot-number*表示单板所在槽位号。不指定该参数时，删除所有单板上的关联表项。（分布式设备－独立运行模式）

**[slot** *slot-number*]：删除指定成员设备上的关联表项，*slot-number*表示设备在IRF中的成员编号。不指定该参数时，删除所有成员设备上的关联表项。（集中式IRF设备）（不支持IRF3的设备）

**[slot ***slot-number*]：删除指定成员设备/PEX上的关联表项，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。不指定该参数时，删除所有成员设备/PEX上的关联表项。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定成员设备上指定单板的关联表项，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的关联表项。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：删除指定单板上的关联表项，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。不指定该参数时，删除所有单板上的关联表项。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：删除指定CPU上的关联表项，*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【使用指导】

如果不指定**ipv4**和**ipv6**，则删除所有的IPv4和IPv6关联表项。

【举例】

\# 删除所有的IPv4关联表项。

\<Sysname\> reset session relation-table ipv4

【相关命令】

·**display session relation-table**

**会话管理 \-- 会话管理配置命令 \-- session aging-time application**

------------------------------------------------------------------------

**[session aging-time application**]命令用来设置应用层协议的会话老化时间。

**[undo session aging-time application**]命令用来恢复缺省情况。如果不指定应用层协议类型，则将所有应用层协议的会话老化时间都恢复为缺省情况。

【命令】

**[session aging-time application **[\|]**h225**[ \| **h245** \| **ils** \| **mgcp** \| **nbt** \| **pptp** \| **ras** \| **rsh** \| **rtsp**  \|]**sccp**[ \| **sip**  \| **sqlnet**  \|]**tftp **[\| **xdmcp** } *time-value*]

**[undo session aging-time application**[ [ **dns** \| **ftp** \| **gtp** ] \|]**h225**[ \| **h245** \| **ras** \| **rtsp**  \| ]**sip **[\| ]**tftp **]

【缺省情况】]

各应用层协议的会话老化时间为：

·**dns**：60秒

·**ftp**：3600秒

·**gtp**：60秒

·**h225**：3600秒

·**h245**：3600秒

·**ils**：3600秒

·**mgcp**：60秒

·**nbt**：3600秒

·**pptp**：3600秒

·**ras**：300秒

·**rsh**：60秒

·**rtsp**：3600秒

·**sccp**：3600秒

·**sip**：300秒

·**sqlnet**：600秒

·**tftp**：60秒

·**xdmcp**：3600秒

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dns**]：表示DNS协议的会话老化时间。

**[ftp**]：表示FTP协议的会话老化时间。

**[gtp**]：表示GTP（GPRS Tunneling Protocol，GPRS隧道协议）协议的会话老化时间。

**[h225**]：表示H.225协议的会话老化时间。

**[h245**]：表示H.245协议的会话老化时间。

**[ils**]：表示ILS（Internet Locator Service，互联网定位服务）协议的会话老化时间。

**[mgcp**]：表示MGCP（Media Gateway Control Protocol，媒体网关控制协议）协议的会话老化时间。

**[nbt**]：表示NBT（NetBIOS over TCP/IP，基于TCP/IP的网络基本输入输出系统）协议的会话老化时间。

**[pptp**]：表示PPTP（Point-to-Point Tunneling Protocol，点到点隧道协议）协议的会话老化时间。

**[ras**]：表示RAS协议的会话老化时间。

**[rsh**]：表示RSH（Remote Shell，远程外壳）协议的会话老化时间。

**[rtsp**]：表示RTSP（Real Time Streaming Protocol，实时流协议）协议的会话老化时间。

**[sccp**]：表示SCCP（Skinny Client Control Protocol，瘦小客户端控制协议）协议的会话老化时间。

**[sip**]：表示SIP协议的会话老化时间。

**[sqlnet**]：表示SQLNET协议的会话老化时间。

**[tftp**]：表示TFTP协议的会话老化时间。

**[xdmcp**]：表示XDMCP（X Display Manager Control Protocol，X显示监控）协议的会话老化时间。

*[time-value*]：指定的老化时间，取值范围为5～100000，单位为秒。

【使用指导】

应用层协议的会话老化时间仅在会话进入稳态时生效（TCP会话的稳态为TCP-EST，UDP会话的稳态为UDP-READY）。

会话进入稳态后，如果该会话属于本命令中指定的一种应用层协议，则此会话的老化时间为指定的应用层协议老化时间；否则为传输层协议状态的老化时间（由**session aging-time state**命令配置）。

需要注意的是，对TCP会话来说，如果会话符合长连接会话的规则，那么该会话稳态的老化时间为长连接老化时间（由**session persistent acl**命令配置）。

【举例】

\# 设置FTP协议的会话老化时间为1800秒。

\<Sysname\> system-view

Sysname session aging-time application ftp 1800

【相关命令】

·**display ****session aging-time application**

·**session aging-time state**

·**session persist****ent acl**

**会话管理 \-- 会话管理配置命令 \-- session aging-time state**

------------------------------------------------------------------------

**[session aging-time state**]命令用来设置各协议状态的会话老化时间。

**[undo session aging-time state**]命令用来恢复缺省情况，如果不指定任何参数，则将所有协议状态的会话老化时间都恢复为缺省情况。

【命令】

**[session aging-time state **[{ **fin** \| **icmp-reply** \| **icmp-request** \| **rawip-open** \| **rawip-ready** \| **syn** \| **tcp-est** \| **udp-open** \| **udp-ready** } *time-value*]]

**[undo session aging-time state **[[ **fin** \| **icmp-reply** \| **icmp-request** \| **rawip-open** \| **rawip-ready** \| **syn** \| **tcp-est** \| **udp-open** \| **udp-ready** ]]]

【缺省情况】

各协议状态的会话老化时间为：

·**fin**：30秒

·**icmp-reply**：30秒

·**icmp-request**：60秒

·**rawip-open**：30秒

·**rawip-ready**：60秒

·**syn**：30秒

·**tcp-est**：3600秒

·**udp-open**：30秒

·**udp-ready**：60秒

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[fin**]：表示TCP协议FIN-WAIT状态的会话老化时间。

**[icmp-reply**]：表示ICMP协议REPLY状态的会话老化时间。

**[icmp-request**]：表示ICMP协议REQUEST状态的会话老化时间。

**[rawip-open**]：表示RAWIP-OPEN状态的会话老化时间。

**[rawip-ready**]：表示RAWIP-READY状态的会话老化时间。

**[syn**]：表示TCP协议SYN-SENT和SYN-RCV状态的会话老化时间。

**[tcp-est**]：表示TCP协议ESTABLISHED状态的会话老化时间。

**[udp-open**]：表示UDP协议OPEN状态的会话老化时间。

**[udp-ready**]：表示UDP协议READY状态的会话老化时间。

*[time-value*]：指定的老化时间，取值范围为5～100000，单位为秒。

【使用指导】

会话进入稳态后，如果该会话属于**session aging-time application**命令中指定的一种应用层协议，则此会话的老化时间为指定的应用层协议老化时间；否则为四层协议状态的老化时间（由**session aging-time state**命令配置）。

需要注意的是，对TCP会话来说，如果会话符合长连接会话的规则，那么该会话稳态的老化时间为长连接老化时间（由**session persistent acl**命令配置）。

【举例】

\# 设置TCP协议SYN-SENT和SYN-RCV状态的老化时间为60秒。

\<Sysname\> system-view

Sysname session aging-time state syn 60

【相关命令】

·**display session aging-time state**

·**session aging-time application**

·**session persist****ent acl**

**会话管理 \-- 会话管理配置命令 \-- session log bytes-active**

------------------------------------------------------------------------

![说明](会话管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[session log bytes-active**]命令用来配置输出会话日志的字节数流量阈值。

**[undo session log bytes-active**]命令用来恢复缺省情况。

【命令】

**[session log bytes-active** *bytes-value*]

**[undo session log** **bytes-active**]

【缺省情况】

不依据字节数流量阈值发送会话日志。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[bytes-value*]：表示发送会话日志的字节数阈值，取值范围为1～1000，单位为兆字节。

【使用指导】

如果设置的字节数阈值为*n*，则一个会话每传输*n*兆个字节整数倍时，设备就输出一次相应的会话日志。

同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。

同时只能有一种流量阈值有效，以最后一次配置的阈值类型为准，例如，先配置报文数阈值再配置字节数阈值，则当前有效的阈值是字节数阈值，只会输出达到字节数阈值的会话日志。

【举例】

\# 设置输出会话日志的字节数流量阈值为10兆字节。

\<Sysname\> system-view

Sysname session log bytes-active 10

【相关命令】

·**session log enable**

·**session log time-active**

**会话管理 \-- 会话管理配置命令 \-- session log enable**

------------------------------------------------------------------------

![说明](会话管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[session log enable**]命令用来使能会话日志功能。

**[undo session log enable**]命令用来关闭会话日志功能。

【命令】

**[session log enable **[{ **ipv4** \| **ipv6** } [ **acl** *acl-number* ] { **inbound** \| **outbound** }]]

**[undo session log enable **[{ **ipv4** \| **ipv6** } [ **acl** *acl-number* ] { **inbound** \| **outbound** }]]

【缺省情况】

会话日志功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv4**]：表示IPv4会话日志。

**[ipv6**]：表示IPv6会话日志。

**[acl ***acl-number*]：对与指定ACL相匹配的会话输出会话日志，其中*acl-number*表示ACL编号，取值范围为2000～3999。

**[inbound**]：指定输出入方向的会话日志。

**[outbound**]：指定输出出方向的会话日志。

【使用指导】

如果不指定ACL，则表示允许输出经过接口的所有IPv4或IPv6会话的日志。

可配置仅输出单方向的会话日志，也可以配置输出双向的会话日志。每个方向上最多可以配置一个IPv4 ACL规则和一个IPv6 ACL规则。

在未指定相关阈值（流量阈值、时间阈值）的情况下，若会话日志功能处于使能状态，则仅在会话表创建和删除的时候分别输出一次会话日志。

【举例】

\# 在GigabitEthernet1/0/1接口下开启会话日志功能，指定输出此接口入方向上的所有IPv4会话日志。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 session log enable ipv4 inbound

\# 在GigabitEthernet1/0/2接口下开启会话日志功能，指定输出此接口出方向上匹配ACL 2050的IPv4会话日志。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/2

Sysname-GigabitEthernet1/0/2 session log enable ipv4 acl 2050 outbound

\# 在GigabitEthernet1/0/3接口下开启会话日志功能，指定输出此接口出方向上匹配ACL 2050的IPv6会话日志。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/3

Sysname-GigabitEthernet1/0/3 session log enable ipv6 acl 2050 outbound

【相关命令】

·**session log bytes-active**

·**session log packets-active**

·**session log time-active**

**会话管理 \-- 会话管理配置命令 \-- session log packets-active**

------------------------------------------------------------------------

![说明](会话管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[session log packets-active**]命令用来配置输出会话日志的报文数流量阈值。

**[undo session log packets-active**]命令用来恢复缺省情况。

【命令】

**[session log packets-active ***packets-value*]

**[undo session log** **packets-active**]

【缺省情况】

不依据报文数流量阈值发送会话日志。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[packets-value*]：表示发送会话日志的报文数阈值，取值范围为1～1000，单位为兆包。

【使用指导】

如果设置的报文数阈值为*n*，则一个会话每收发*n*兆个报文，设备就输出一次相应的会话日志。

同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。

同时只能有一种流量阈值有效，以最后一次配置的阈值类型为准，例如，先配置报文数阈值再配置字节数阈值，则当前有效的阈值是字节数阈值，只会输出达到字节数阈值的会话日志。

【举例】

\# 设置输出会话日志的流量阈值为10兆报文数。

\<Sysname\> system-view

Sysname session log packets-active 10

【相关命令】

·**session log enable**

·**session log time-active**

**会话管理 \-- 会话管理配置命令 \-- session log time-active**

------------------------------------------------------------------------

![说明](会话管理命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[session log time-active**]命令用来配置输出会话日志的时间阈值。

**[undo session log time-active**]用来恢复缺省情况。

【命令】

**[session log time-active ***time-value*]

**[undo session log time-active**]

【缺省情况】

不依据时间阈值发送会话日志。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time-value*]：表示发送会话日志的时间阈值，取值范围为10～120，单位为分钟，只能为10的整数倍。

【使用指导】

如果设置的时间阈值为*n*，则每经过*n*分钟，设备就输出一次相应的会话日志。

同时配置了时间阈值和流量阈值的情况下，只要有一个阈值到达，就会输出相应的会话日志，并将所有的阈值统计信息清零。

【举例】

\# 设置输出会话日志的时间阈值为50分钟。

\<Sysname\> system

Sysname session log time-active 50

【相关命令】

·**session log enable**

·**session log bytes-active**

·**session log packets-active**

**会话管理 \-- 会话管理配置命令 \-- session statistic enable**

------------------------------------------------------------------------

**[session statistics enable**]命令用来开启会话统计功能。

**[undo session statistics enable**]命令用来恢复缺省情况。

【命令】

**[session statistics enable**]

**[undo session statistics enable**]

【缺省情况】

会话统计功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

开启会话统计功能之后，设备将对收到和发送的基于会话的业务报文数目和报文字节数进行统计，基于会话的报文统计信息可以通过**display session table**命令查看，基于报文类型的报文统计信息可以通过**display session statistics**命令查看。

【举例】

\# 开启会话统计功能。

\<Sysname\> system-view

Sysname session statistics enable

【相关命令】

·**display session statistics**

·**display session table**

**会话管理 \-- 会话管理配置命令 \-- session persistent acl**

------------------------------------------------------------------------

**[session persistent acl**]命令用来配置长连接会话规则。

**[undo session persistent acl**]命令用来清除长连接会话规则。

【命令】

**[session persistent acl** [ **ipv6**  *acl-number*  **aging-time** *time-value* ]]

**[undo session persistent acl ** **ipv6** ]

【缺省情况】

无长连接会话规则。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ipv6**]：指定IPv6 ACL。如果没有指定本参数，则表示IPv4 ACL。

*[acl-number*]：ACL编号，取值范围为2000～3999。

**[aging-time*** time-value*]：长连接会话的老化时间。其中，*time-value*表示指定的老化时间，取值范围为0～360，单位为小时，缺省值为24小时。0表示永不老化。

【使用指导】

长连接老化时间仅在TCP会话进入稳态（TCP-EST状态）时生效。在TCP会话处于稳态时，长连接老化时间具有最高的优先级，其次为应用层协议老化时间，最后为协议状态老化时间。

对于设置为永不老化的长连接会话，不会因为没有报文命中而被老化删除，只有当会话的发起方或响应方主动发起关闭连接请求或管理员使用**reset session table**命令手动删除该会话时，才会被删除。

长连接会话的配置仅影响后续生成的会话，对于已经生效的会话不产生作用。

【举例】

\# 配置符合ACL 2000规则的IPv4会话为长连接，老化时间为72小时。

\<Sysname\> system-view

Sysname session persistent acl 2000 aging-time 72

\# 配置符合ACL 3000规则的IPv6会话为长连接，老化时间为100小时。

\<Sysname\> system-view

Sysname session persistent acl ipv6 3000 aging-time 100

【相关命令】

·**session aging-time application**

·**session aging-time state**

**会话管理 \-- 会话管理配置命令 \-- session synchronization enable**

------------------------------------------------------------------------

**[session synchronization enable**]命令用来[开启会话业务热备份功能。]

**[undo [session synchronization enable]**]命令用来恢复缺省情况。

【命令】

**[session synchronization enable**]

**[undo [session synchronization enable]**]

【缺省情况】

会话业务热备份功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

会话业务热备份功能实现了多台设备之间会话以及基于会话的业务（NAT、ALG、ASPF）的动态表项的热备份。

【举例】

\# 开启会话[业务热备份能。]

\<Sysname\> system-view

Sysname session synchronization enable

