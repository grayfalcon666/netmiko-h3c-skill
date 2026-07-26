
**ANCP \-- ANCP配置命令 \-- aging-time**

------------------------------------------------------------------------

**[aging-time**]命令用来配置线路表项的老化时间。

**[undo aging-time**]命令用来恢复缺省情况。

【命令】

**[aging-time** *value*]

**[undo aging-time**]

【缺省情况】

线路表项的老化时间为150秒。

【视图】

ANCP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：线路表项的老化时间，取值范围为0～65535，单位为秒。取值为0表示在线路状态变为Down时立即删除该线路表项。

【使用指导】

线路表项即设备记录的用户DSL线路信息。当用户所在的接入线路上线或变化时，设备会创建或更新相应线路表项。当用户所在的接入线路下线时，设备将在老化时间过后删除对应的线路表项。

需要注意的是，如果ANCP客户端在收到设备下发的业务策略后需要将线路重启（即将线路down掉，让其重新接入），则需要在设备上配置较长的线路表项老化时间。

【举例】

\# 配置ANCP邻居test1的线路表项的老化时间为100秒。

\<Sysname\> system-view

sysname ancp neighbor test1

sysname-ancp-neighbor-test1 aging-time 100

**ANCP \-- ANCP配置命令 \-- ancp access-loop-configure**

------------------------------------------------------------------------

**[ancp access-loop-configure**]命令用来向对端DSLAM下发指定线路的业务策略。

【命令】

**[ancp** **access-loop-configure** **circuit-id** *circuit-id* **service-profile** *profile-name* [ **timeout** *time-value* ]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[circuit-id*** circuit-id*]：用户的接入线路ID，为1～63个字符的字符串，区分大小写。可以通过**display ancp access-loop**命令查看用户的接入线路ID。

**[service-profile*** profile-name*]：设备下发的业务策略的名称，为1～64个字符的字符串，区分大小写。

**[timeout ***time-value*]：系统等待对端回应的超时时间，取值范围为0～60，单位为秒，缺省值为5秒。取值为0表示不关注对端回应。

【使用指导】

执行本命令可以向对端DSLAM下发指定线路的业务策略，业务策略的具体参数（如QoS参数、带宽等）需要在对端的DSLAM设备上定义。

【举例】

\# 向接入线路ID为Dslam1/1:100的线路下发业务策略text-profile，不关注对端回应。

\<Sysname\> system-view

Sysname ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile timeout 0

\# 指定接入线路不存在。

\<Sysname\> system-view

Sysname ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile

Issuing service profile name text-profile for Dslam1/1:100. Please wait...

Access line Dslam1/1:100 doesn't exist.

\# 向接入线路ID为Dslam1/1:100的线路下发业务策略text-profile，下发成功。

\<Sysname\> system-view

Sysname ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile timeout 10

Issuing service profile name text-profile for Dslam1/1:100. Please wait...

Issued the service profile name successfully.

Status info: xxxxxxxxxxxxxxxxxxxx

\# 向接入线路ID为Dslam1/1:100的线路下发业务策略text-profile，下发失败。

\<Sysname\> system-view

Sysname ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile

Issuing service profile name text-profile for Dslam1/1:100. Please wait...

Failed to issue the service profile name. Operation timed out.

Status info: xxxxxxxxxxxxxxxxxxxx

下发业务策略失败的原因还有如下几种：

Failed to issue the service profile name. Invalid request message.

Failed to issue the service profile name. One or more of the specified ports are down.

Failed to issue the service profile name. Out of resources.

Failed to issue the service profile name. Request message type not implemented.

Failed to issue the service profile name. Malformed message.

Failed to issue the service profile name. Mandatory TLV missing.

Failed to issue the service profile name. Invalid TLV contents.

Failed to issue the service profile name. Unknown error.

表1-1 下发业务策略结果显示信息描述表

显示信息

描述

Access line Dslam1/1:100 doesn\'t exist

指定接入线路不存在

The DSL line configuration capability is not supported

指定接入线路对应的邻居不支持线路配置能力

Issued the service profile name succeessfully

下发业务策略成功

Status info: xxxxxxxxxxxxxxxxxxxx

该信息为对端DSLAM反馈的详细信息，如果对端不反馈则不显示，具体显示信息请以实际情况为准

Failed to issue the service profile name

下发业务策略失败

Operation timed out

下发业务策略超时

Invalid request message

无效的请求报文

One or more of the specified ports are down

一个或者多个指定接入线路对应的端口状态为down

Out of resources

DSLAM资源不足

Request message type not implemented

请求报文类型不支持

Malformed message

非法报文

Mandatory TLV missing

必要的TLV丢失

Invalid TLV contents

无效的TLV内容

Unknown error

未知的错误

【相关命令】

·**display ancp access-loop**

**ANCP \-- ANCP配置命令 \-- ancp enable**

------------------------------------------------------------------------

**[ancp enable**]命令用来使能ANCP功能。

**[undo ancp enable**]命令用来恢复缺省情况。

【命令】

**[ancp enable**]

**[undo ancp enable**]

【缺省情况】

ANCP功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有在使能ANCP功能并配置了建立ANCP邻接的源接口后，系统才开始进行TCP监听并处理ANCP客户端建立TCP连接的请求和ANCP业务。

关闭ANCP功能后，所有ANCP邻接会被断开，TCP监听功能关闭。

【举例】

\# 使能ANCP功能。

\<Sysname\> system-view

Sysname ancp enable

【相关命令】

·**ancp source-interface**

·**source-interface**

**ANCP \-- ANCP配置命令 \-- ancp neighbor**

------------------------------------------------------------------------

**[ancp neighbor**]命令用来创建ANCP邻居并进入该ANCP邻居视图。

**[undo ancp neighbor**]命令用来删除指定的ANCP邻居。

【命令】

**[ancp neighbor** *neighbor-name*]

**[undo ancp neighbor** *neighbor-name*]

【缺省情况】

不存在ANCP邻居。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[neighbor-name*]：ANCP邻居的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

用户可以创建多个ANCP邻居，并为每个ANCP邻居分别配置参数，从而对每个ANCP邻居进行单独管理。

执行本命令时，如果不存在该ANCP邻居则创建一个新的ANCP邻居并进入该ANCP邻居视图，如果存在该ANCP邻居则直接进入该ANCP邻居视图。

删除ANCP邻居时，会清除ANCP邻居下的所有配置信息和状态信息，并断开已经建立的ANCP邻接关系和TCP连接。

【举例】

\# 创建ANCP邻居test1，并进入该ANCP邻居视图。

\<Sysname\> system-view

sysname ancp neighbor test1

sysname-ancp-neighbor-test1

**ANCP \-- ANCP配置命令 \-- ancp oam**

------------------------------------------------------------------------

**[ancp oam**]命令用来触发对指定接入线路的ANCP OAM检测。

【命令】

**[ancp oam**[ [ **count** *test-counter* \| **timeout** *time-value* ] \* **access-loop** *circuit-id*]]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[count***test-counter*]：DSLAM进行探测的次数，取值范围为1～32，缺省值为5。

**[timeout ***time-value*]：系统等待ANCP OAM检测回应的超时时间，取值范围为1～60，单位为秒，缺省值为5秒。

**[access-loop***circuit-id*]：用户的接入线路ID，为1～63个字符的字符串，区分大小写。可以通过**display ancp access-loop**命令查看用户的接入线路ID。

【使用指导】

ANCP OAM检测用于检测用户的接入线路是否正常。

执行本命令后，系统会向对端DSLAM发送ANCP OAM检测消息，该消息中携带了本命令配置的各参数值。收到ANCP OAM检测消息后，DSLAM检测指定的接入线路的状态，最多进行*test-counter*次探测，并反馈检测结果。如果在本命令所配置的超时时间内未收到ANCP OAM的检测回应，则表明ANCP OAM检测失败。

【举例】

\# 配置对指定接入线路的OAM检测，指定接入线路不存在。

\<Sysname\> system-view

sysname ancp oam count 5 timeout 5 access-loop Dslam1/1:100

OAM testing Dslam1/1:100. Please wait...

Access line Dslam1/1:100 doesn\'t exist.

\# 配置对指定接入线路的OAM检测，检测结果成功。

\<Sysname\> system-view

sysname ancp oam count 5 timeout 5 access-loop Dslam1/1:100

OAM testing Dslam1/1:100. Please wait...

OAM test succeeded.

Status info: xxxxxxxxxxxxxxxxxxxx

\# 配置对指定接入线路的OAM检测，检测结果失败。

\<Sysname\> system-view

sysname ancp oam count 5 timeout 5 access-loop Dslam2/1:100

OAM testing Dslam2/1:100. Please wait...

OAM test failed. Loopback test timed out

Status info: xxxxxxxxxxxxxxxxxxxx

检测结果还有如下几种：

The neighbor doesn\'t support OAM operation.

OAM test failed. One or more of the specified ports don't exist.

OAM test failed. Loopback test timed out.

OAM test failed. DSL access line status showtime.

OAM test failed. DSL access line status idle.

OAM test failed. DSL access line status silent.

OAM test failed. DSL access line status training.

OAM test failed. DSL access line integrity error.

OAM test failed. DSLAM resource not available.

OAM test failed. Invalid test parameter.

OAM test failed. Unknown error.

表1-2 ANCP OAM检测结果显示信息描述表

显示信息

描述

Access line Dslam1/1:100 doesn\'t exist

指定接入线路不存在

The neighbor doesn\'t support OAM operation.

指定接入线路对应的邻居不支持OAM检测能力

OAM test succeeded

OAM检测成功

Status info: xxxxxxxxxxxxxxxxxxxx

该信息为对端DSLAM反馈的详细信息，如果对端不反馈则不显示，具体显示信息请以实际情况为准

OAM test failed

OAM检测失败

One or more of the specified ports don't exist

一个或者多个指定接入线路对应的端口不存在

Loopback test timed out

环回检测超时

DSL access line status showtime

DSL接入线路状态为SHOWTIME

关于SHOWTIME状态的详细介绍请参见ITU-T G.993.2

DSL access line status idle

DSL接入线路状态为IDLE

关于IDLE状态的详细介绍请参见ITU-T G.993.2

DSL access line status silent

DSL接入线路状态为SILENT

关于SILENT状态的详细介绍请参见ITU-T G.993.2

DSL access line status training

DSL接入线路状态为TRAINING

关于TRAINING状态的详细介绍请参见ITU-T G.993.2

DSL access line integrity error

DSL接入线路不完整

DSLAM resource not available

DSLAM资源不可用

Invalid test parameter

检测参数非法

Unknown error

未知的错误

【相关命令】

·**display ancp access-loop**

**ANCP \-- ANCP配置命令 \-- ancp session interval**

------------------------------------------------------------------------

**[ancp session interval**]命令用来配置发送邻接报文的时间间隔。

**[undo ancp session interval**]命令用来恢复缺省情况。

【命令】

**[ancp session interval** *interval-value*]

**[undo ancp session** **interval**]

【缺省情况】

发送邻接报文的时间间隔为25秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval-value*]：发送邻接报文的时间间隔，取值范围为1～25，单位为秒。

【使用指导】

在TCP连接建立成功之后，ANCP客户端和ANCP服务器都会向对端发送SYN报文试图建立ANCP邻接，SYN报文中携带本端配置的发送邻接报文时间间隔；ANCP邻接建立过程中，两端协商发送邻接报文的时间间隔（取两端配置的时间间隔中的较大值），后续SYNACK、ACK报文均以协商后的时间间隔发送。

【举例】

\# 配置发送邻接报文的时间间隔为15秒。

\<Sysname\> system-view

sysname ancp session interval 15

**ANCP \-- ANCP配置命令 \-- ancp session retransmit**

------------------------------------------------------------------------

**[ancp session retransmit**]命令用来配置ANCP邻接建立过程中SYN、SYNACK报文的最大重传次数。

**[undo ancp session retransmit**]命令用来恢复缺省情况。

【命令】

**[ancp session retransmit** *retransmit-value*]

**[undo ancp session retransmit**]

【缺省情况】

SYN、SYNACK报文的最大重传次数为10次。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retransmit-value*]：最大重传次数，取值范围为3～255。

【使用指导】

在ANCP邻接建立过程中，如果在发送邻接报文的时间间隔内未收到对端回应的报文，则会向对端重新发送上一个报文。如果SYN或者SYNACK报文的重发次数达到该命令所配置的最大重传次数时还未收到对端回应的报文，则终止ANCP邻接建立过程，断开TCP连接。

【举例】

\# 配置SYN、SYNACK报文的最大重传次数为100次。

\<Sysname\> system-view

sysname ancp session retransmit 100

**ANCP \-- ANCP配置命令 \-- ancp source-interface**

------------------------------------------------------------------------

**[ancp source-interface**]命令用来配置建立ANCP邻接的全局源接口。

**[undo ancp source-interface**]命令用来删除全局源接口的配置。

【命令】

**[ancp source-interface loopback** *interface-number*]

**[undo ancp source-interface**]

【缺省情况】

未配置全局源接口。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[loopback ***interface-number*]：指定LoopBack接口为全局源接口。

【使用指导】

只有在使能ANCP功能并配置了建立ANCP邻接的源接口后，系统才开始进行TCP监听并处理ANCP客户端建立TCP连接的请求和ANCP业务。

指定了源接口后，系统使用该源接口的IP地址（IPv4主地址/第一个IPv6全球单播地址）和6068端口号作为本端的源地址和源端口号进行TCP监听，与对端建立TCP连接；系统发送ANCP报文时，ANCP报文的源地址为源接口的IP地址。

需要注意的是：

·删除源接口的配置后，TCP监听功能关闭；修改源接口后，使用新源接口的IP地址和6068端口号作为本端的源地址和源端口号进行TCP监听。对源接口的删除或者修改不会影响已经建立好的TCP连接。

·全局源接口对所有邻居生效，在邻居视图下配置的源接口只对当前邻居生效。如果同时配置了全局源接口和邻居视图下的源接口，则会优先使用邻居视图下配置的源接口。

【举例】

\# 配置建立ANCP邻接的全局源接口。

\<Sysname\> system-view

sysname ancp source-interface loopback 100

【相关命令】

·**ancp enable**

·**source-interface**

**ANCP \-- ANCP配置命令 \-- display ancp access-loop**

------------------------------------------------------------------------

**[display ancp access-loop**]命令用来显示ANCP接入线路表项信息。

【命令】

**[display ancp access-loop**[ [ **circuit-id** *circuit-id* \| **neighbor** *neighbor-name* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[circuit-id*** circuit-id*]：用户的接入线路ID，为1～63个字符的字符串，区分大小写。可以通过**display ancp access-loop**命令查看用户的接入线路ID。

**[neighbor*** neighbor-name*]：ANCP邻居的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·如果未指定任何参数，则显示所有接入线路表项的简要信息。

·如果指定**circuit-id**参数，则显示指定接入线路的详细信息。

·如果指定**neighbor**参数，则显示指定ANCP邻居下的所有接入线路表项的简要信息。

【举例】

\# 显示所有接入线路表项的简要信息。

\<Sysname\> display ancp access-loop

Total entries: 1

Neighbor name     Peer ID           Circuit ID         State

bras              0001-0002-0003    circuit4:430       UP

\# 显示指定接入线路的详细信息。

\<Sysname\> display ancp access-loop circuit-id circuit4:430

Neighbor name                       : bras

Circuit ID                          : circuit4:430

Remote ID                           : -

Peer ID                             : 0001-0002-0003

DSL type                            : ADSL1

Actual data rate upstream           : 64 kbps

Actual data rate downstream         : 128 kbps

Min data rate upstream              : 32 kbps

Min data rate downstream            : 32 kbps

Attainable data rate upstream       : 1024 kbps

Attainable data rate downstream     : 8192 kbps

Max data rate upstream              : 1024 kbps

Max data rate downstream            : 8192 kbps

Min low power data rate upstream    : 32 kbps

Min low power data rate downstream  : 32 kbps

Max delay upstream                  : 20 s

Max delay downstream                : 8192 s

Actual delay upstream               : 20 s

Actual delay downstream             : 20 s

Data link                           : ETHERNET

Encapsulation 1                     : Untagged Ethernet

Encapsulation 2                     : NA

\# 显示指定ANCP邻居下的所有接入线路表项的简要信息。

\<Sysname\> display ancp access-loop neighbor dslam1

Total entries: 1

Neighbor name    Peer ID               Circuit ID                       State

dslam1           0001-0002-0003        001882362CFF eth 0/3/0/2:6       UP

表1-3 display ancp access-loop命令显示信息描述表

字段

描述

Total entries

表项总数

Neighbor name

ANCP邻居的名称

Peer ID

ANCP邻居ID，即线路所属的DSLAM的MAC地址

Circuit ID

接入线路的ID

Remote ID

远程ID

State

接入线路的状态，线路在线则为UP状态，反之为DOWN状态

DSL type

DSL类型：ADSL1、ADSL2、ADSL2+、VDSL1、VDSL2、SDSL、Other

Actual data rate upstream

接入线路的实际上行速率，单位为kbps

Actual data rate downstream

接入线路的实际下行速率，单位为kbps

Min data rate upstream

接入线路的上行最小速率，单位为kbps

Min data rate downstream

接入线路的下行最小速率，单位为kbps

Attainable data rate upstream

接入线路的上行可获速率，单位为kbps

Attainable data rate downstream

接入线路的下行可获速率，单位为kbps

Max data rate upstream

接入线路的上行最大速率，单位为kbps

Max data rate downstream

接入线路的下行最大速率，单位为kbps

Min low power data rate upstream

接入线路的上行低压最小速率，单位为kbps

Min low power data rate downstream

接入线路的下行低压最小速率，单位为kbps

Max delay upstream

接入线路的上行最大时延，单位为秒

Max delay downstream

接入线路的下行最大时延，单位为秒

Actual delay upstream

接入线路的上行实际时延，单位为秒

Actual delay downstream

接入线路的下行实际时延，单位为秒

Data link

数据链路类型：

·ATM ALL5：ATM链路

·ETHERNET：以太网链路

Encapsulation 1

封装头1的信息：

·NA：不携带封装头1的信息

·Untagged Ethernet：不带VLAN Tag的以太网报文

·Single-tagged Ethernet：携带一层VLAN Tag的以太网报文

·Double-tagged Ethernet：携带双层VLAN Tag的以太网报文

Encapsulation 2

封装头2的信息：

·NA：不携带封装头2的信息

·PPPoA LLC：基于逻辑链路控制的PPPoA报文

·PPPoA Null：PPPoA报文

·IPoA LLC：基于逻辑链路控制的IPoA报文

·IPoA Null：IPoA报文

·Ethernet over AAL5 LLC with FCS：携带FCS校验的基于ATM逻辑链路控制的以太网报文

·Ethernet over AAL5 LLC without FCS：不携带FCS校验的基于ATM逻辑链路控制的以太网报文

·Ethernet over AAL5 NULL with FCS：携带FCS校验的基于ATM的以太网报文

·Ethernet over AAL5 NULL without FCS：不携带FCS校验的基于ATM的以太网报文

【相关命令】

·**reset ancp access-loop**

**ANCP \-- ANCP配置命令 \-- display ancp neighbor**

------------------------------------------------------------------------

**[display ancp neighbor**]命令用来显示ANCP邻居信息，包括配置信息与状态信息。

【命令】

**[display ancp neighbor** [ *neighbor-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[neighbor-name*]：ANCP邻居的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·如果不指定ANCP邻居的名称，则显示当前所有ANCP邻居的简要信息。

·如果指定ANCP邻居的名称，则显示指定ANCP邻居的详细信息。

【举例】

\# 显示所有ANCP邻居的简要信息。

\<Sysname\> display ancp neighbor

Total entries: 2

Neighbor name       Peer ID             State      Access loop number

default-neighbor    -                   Unused     0

dslam1              0001-0002-0003      Used       3

\# 显示指定ANCP邻居的详细信息。

\<Sysname\> display ancp neighbor dslam1

Neighbor name                        : dslam1

Peer ID                              : 0001-0002-0003

Source interface                     : LoopBack1

Session message interval             : 25 s

Session message retransmit           : 255

Aging time                           : 150 s

State                                : Used

Peer IP                              : 1.1.1.1

Peer port                            : 8093

Neighbor capacities                  : discovery, line-cfg, oam

Negotiated interval                  : 25.0 s

Access loop number                   : 0

表1-4 display ancp neighbor命令显示信息描述表

字段

描述

Total entries

ANCP邻居总数

Neighbor name

ANCP邻居的名称

Peer ID

ANCP邻居的ID

Source interface

建立ANCP邻接的源接口

Session message interval

用户配置的发送邻接报文的时间间隔

Session message retransmit

ANCP邻接建立过程中SYN、SYNACK报文的最大重传次数

Aging time

ANCP邻居的接入线路表项的老化时间

State

ANCP邻居的使用情况：

·Used：表示已使用该ANCP邻居，即BRAS设备和该ANCP邻居对应的DSLAM之间已经建立了邻接关系

·Unused：表示未使用该ANCP邻居，即BRAS设备和该ANCP邻居对应的DSLAM之间还没有建立邻接关系

Peer IP

ANCP邻居的IP地址

Peer port

ANCP邻居的TCP端口号

Neighbor capacities

ANCP邻居支持的能力集：

·discovery：动态拓扑发现

·line-cfg：线路配置

·oam：OAM检测

Neigotiated interval

两端协商后的发送邻接报文的时间间隔

Access loop number

ANCP邻居下接入线路总数

【相关命令】

·**reset ancp neighbor**

**ANCP \-- ANCP配置命令 \-- display ancp statistic**

------------------------------------------------------------------------

**[display ancp statistic**]命令用来显示ANCP邻居的ANCP统计信息。

【命令】

**[display ancp statistic** [ **neighbor** *neighbor-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[neighbor*** neighbor-name*]：查看指定ANCP邻居的ANCP统计信息。*neighbor-name*表示ANCP邻居的名称，为1～31个字符的字符串，区分大小写。不指定本参数时，将显示所有ANCP邻居的ANCP统计信息。

【举例】

\# 显示当前所有ANCP邻居的ANCP统计信息。

\<Sysname\> display ancp statistic

Received ack packets                  : 1311

Received syn packets                  : 0

Received synack packets               : 2

Received reset ack packets            : 0

Received port up packets              : 1

Received port down packets            : 0

Received oam packets                  : 0

Received access loop config packets   : 0

Received update packets               : 0

Received generic response packets     : 0

Received unknown packets              : 0

Dropped packets                       : 0

Sent ack packets                      : 1311

Sent syn packets                      : 6

Sent synack packets                   : 0

Sent reset ack packets                : 0

Sent oam packets                      : 0

Sent access loop config packets       : 0

Sent generic response packets         : 0

Packets failing to be sent            : 0

Adjacency up                          : 2

Adjacency failed                      : 0

Adjacency down                        : 1

\# 显示指定ANCP邻居的ANCP统计信息。

\<Sysname\>display ancp statistic neighbor dslam1

Received ack packets                  : 981

Received syn packets                  : 0

Received synack packets               : 1

Received reset ack packets            : 0

Received port up packets              : 1

Received port down packets            : 0

Received oam packets                  : 0

Received access loop config packets   : 0

Received update packets               : 0

Received generic response packets     : 0

Received unknown packets              : 0

Dropped packets                       : 0

Sent ack packets                      : 981

Sent syn packets                      : 1

Sent synack packets                   : 1

Sent reset ack packets                : 0

Sent oam packets                      : 0

Sent access loop config packets       : 0

Sent generic response packets         : 0

Packets failing to be sent            : 0

表1-5 display ancp statistic命令显示信息描述表

字段

描述

Received ack packets

接收的ACK报文数

Received syn packets

接收的SYN报文数

Received synack packets

接收的SYNACK报文数

Received reset ack packets

接收的RSTACK报文数

（RSTACK报文：一种邻接报文，用于重置ANCP邻接）

Received port up packets

接收的Port Up报文数

（Port Up报文：线路上线报文。当AN感知到下挂线路上线时会发送Port Up报文通知BRAS设备上线接入线路的参数）

Received port down packets

接收的Port Down报文数

（Port Down报文：线路下线报文。当AN感知到下挂线路下线时会发送Port Down报文通知BRAS设备删除接入线路的参数）

Received oam packets

接收的线路OAM检测报文数

Received access loop config packets

接收的线路配置报文数

Received unknown packets

接收的未知报文数

Received update packets

接收的Update报文数

（Update报文：邻接更新报文。当组网环境中出现其它BRAS设备时，AN发送邻接更新报文通知BRAS设备组网环境中存在BRAS设备的数目和AN端下挂的接入线路数目）

Received generic response packets

接收的Generic Response报文数

（Generic Response报文：一般应答报文。该报文可以作为给请求报文的应答，也可以因为某种错误原因主动发送）

Dropped packets

丢弃的报文数

Sent ack packets

发送的ACK报文数

Sent syn packets

发送的SYN报文数

Sent synack packets

发送的SYNACK报文数

Sent reset ack packets

发送的RSTACK报文数

Sent oam packets

发送的线路OAM检测报文数

Sent access loop config packets

发送的线路配置报文数

Sent generic response packets

发送的Generic Response报文数

Packets failing to be sent

发送失败的报文数

Adjancency up

建立ANCP邻接成功的次数

Adjancency failed

建立ANCP邻接失败的次数

Adjancency down

关闭ANCP邻接的次数

【相关命令】

·**reset ancp statistic**

**ANCP \-- ANCP配置命令 \-- peer-id**

------------------------------------------------------------------------

**[peer-id**]命令用来配置ANCP邻居ID。

**[undo peer-id**]命令用来取消已配置的ANCP邻居ID。

【命令】

**[peer-id** *peer-id*]

**[undo peer-id**]

【缺省情况】

未配置ANCP邻居ID。

【视图】

ANCP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[peer-id*]：ANCP邻居ID，即ANCP客户端的MAC地址，唯一标识一个ANCP邻居，形式为H-H-H。

【使用指导】

TCP连接建立后，BRAS设备根据ANCP客户端的MAC地址来判断ANCP客户端所属的ANCP邻居。如果ANCP客户端的MAC地址与某个ANCP邻居ID匹配，则该ANCP客户端就属于该ANCP邻居。

需要注意的是：

·一个ANCP邻居只能配置一个ANCP邻居ID。不同ANCP邻居不允许配置相同的ANCP邻居ID。

·取消已配置的ANCP邻居ID时，会断开已经建立的ANCP邻接关系和TCP连接。

【举例】

\# 配置ANCP邻居test1的ANCP邻居ID为1-2-3。

\<Sysname\> system-view

sysname ancp neighbor test1

sysname-ancp-neighbor-test1 peer-id 1-2-3

【相关命令】

·**ancp neighbor**

**ANCP \-- ANCP配置命令 \-- reset ancp access-loop**

------------------------------------------------------------------------

**[reset ancp access-loop**]命令用来清除ANCP接入线路表项。

【命令】

**[reset ancp access-loop**[ [ **circuit-id** *circuit-id* \| **neighbor** *neighbor-name* ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[circuit-id*** circuit-id*]：用户的接入线路ID，为1～63个字符的字符串，区分大小写。可以通过**display ancp access-loop**命令查看用户的接入线路ID。

**[neighbor*** neighbor-name*]：ANCP邻居的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

·如果未指定任何参数，则清除所有ANCP接入线路表项。

·如果指定**circuit-id**参数，则清除指定接入线路的表项；

·如果指定**neighbor**参数，则清除指定ANCP邻居下的所有接入线路表项。

【举例】

\# 清除接入线路ID为0001-0002-0003 eth 1/162 3:11的线路表项。

\<Sysname\> reset ancp access-loop circuit-id "0001-0002-0003 eth 1/162 3:11"

【相关命令】

·**display ancp access-loop**

**ANCP \-- ANCP配置命令 \-- reset ancp neighbor**

------------------------------------------------------------------------

**[reset ancp neighbor**]命令用来清除ANCP邻居的状态信息，并关闭TCP连接。

【命令】

**[reset ancp neighbor** [ *neighbor-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[neighbor-name*]：清除指定ANCP邻居的状态信息，并关闭TCP连接。*neighbor-name*表示ANCP邻居的名称，为1～31个字符的字符串，区分大小写。如果不指定本参数，将清除所有ANCP邻居的状态信息，并关闭TCP连接。

【举例】

\# 清除ANCP邻居dslam1的状态信息，并关闭TCP连接。

\<Sysname\> reset ancp neighbor dslam1

【相关命令】

·**display ancp neighbor**

**ANCP \-- ANCP配置命令 \-- reset ancp statistic**

------------------------------------------------------------------------

**[reset ancp statistic**]命令用来清除ANCP邻居的ANCP统计信息。

【命令】

**[reset ancp statistic** [ **neighbor** *neighbor-name* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[neighbor** *neighbor-name*]：清除指定ANCP邻居的ANCP统计信息。*neighbor-name*表示ANCP邻居的名称，为1～31个字符的字符串，区分大小写。不指定本参数时，将清除所有ANCP邻居的ANCP统计信息。

【举例】

\# 清除ANCP邻居dslam1的ANCP统计信息。

\<Sysname\> reset ancp statistic neighbor dslam1

【相关命令】

·**display ancp statistic**

**ANCP \-- ANCP配置命令 \-- source-interface**

------------------------------------------------------------------------

**[source-interface**]命令用来在邻居视图下配置建立ANCP邻接的源接口。

**[undo source-interface**]命令用来删除邻居视图下所配置的建立ANCP邻接的源接口。

【命令】

**[source-interface loopback** *interface-number*]

**[undo source-interface**]

【缺省情况】

未配置邻居视图下的源接口。

【视图】

ANCP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[loopback ***interface-number*]：指定LoopBack接口为源接口。

【使用指导】

只有在使能ANCP功能并配置了建立ANCP邻接的源接口后，系统才开始进行TCP监听并处理ANCP客户端建立TCP连接的请求和ANCP业务。

指定了源接口后，系统使用该源接口的IP地址（IPv4主地址/第一个IPv6全球单播地址）和6068端口号作为本端的源地址和源端口号进行TCP监听，与对端建立TCP连接；系统发送ANCP报文时，ANCP报文的源地址为源接口的IP地址。

需要注意的是：

·删除源接口配置后，TCP监听功能关闭；修改源接口后，使用新源接口的IP地址和6068端口号作为本端的源地址和源端口号进行TCP监听。对源接口的删除或者修改不会影响已经建立好的TCP连接。

·在邻居视图下配置的源接口只对当前邻居生效。如果同时配置了全局源接口和邻居视图下的源接口，则会优先使用邻居视图下配置的源接口。

【举例】

\# 配置ANCP邻居test1建立ANCP邻接的源接口。

\<Sysname\> system-view

sysname ancp neighbor test1

sysname-ancp-neighbor-test1 source-interface loopback 100

【相关命令】

·**ancp enable**

·**ancp source-interface**
