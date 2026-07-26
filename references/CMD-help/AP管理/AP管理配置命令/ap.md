
**AP管理 \-- AP管理配置命令 \-- ap**

------------------------------------------------------------------------

**[ap**]命令用来配置AP名字入组规则。

**[undo ap**]命令用来删除AP名字入组规则。

【命令】

**[ap** *ap-name-list*]

**[undo ap** *ap-name-list*]

【缺省情况】

未配置AP名字入组规则。

【视图】

AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

ap-name-list:AP的名字列表，表示方式为ap-name-list=}&\<1[-10\>]。其中ap-name为AP的名字，为1～63个字符的字符串，可以包含字母、数字及下划线，不区分大小写，&\<[1-10\>]表示前面的参数最多可以输入10个。

【使用指导】

·本命令不检查指定的AP是否存在。

·不同型号的设备支持的最大AP数不同，请以设备的实际情况为准。

·AP名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于MAC地址入组规则。AP优先根据AP名字入组规则匹配入组，其次是AP序列号入组规则，然后是AP MAC 地址入组规则，若未匹配到任何入组规则，则AP将被加入到默认组。

·默认组视图下不能进行该配置。

【举例】

\# 在AP组视图下添加名字入组规则。

\<System\> system-view

System wlan ap-group group1

System-wlan-ap-group-group1 ap ap1 ap2 ap3

【相关命令】

·**wlan****ap-group**

**AP管理 \-- AP管理配置命令 \-- cir**

------------------------------------------------------------------------

**[cir**]命令用来设置承诺信息速率和承诺突发尺寸以实现流量保护功能。

**[undo cir**]命令用来恢复缺省情况。

【命令】

**[cir ***committed-information-rate* [ **cbs** *committed-burst-size* ]]

**[undo cir**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：未设置承诺信息速率和承诺突发尺寸

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cir ***committed-information-rate*]：承诺信息速率，取值范围为40～1000000，单位为Kbps。

**[cbs*** committed-burst-size*]：承诺突发尺寸，取值范围为2500～62500000。如果未指定本参数，则表示承诺突发尺寸为500毫秒以CIR速率通过的流量，单位为Bytes。

【使用指导】

开启流量保护功能后可以对AC和AP间的数据流量进行限速，防止由于AP遭受超过其处理能力的数据流量冲击，使AP无法及时向AC回复报文而导致AP频繁重启。

有关**cir**命令的详细介绍与配置请参见"ACL和QoS命令参考"中的"QoS策略"。

【举例】

\# 设置承诺速率为60Kbps，承诺突发尺寸为3000Bytes。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-wlan-ap-ap1 cir 60 cbs 3000

**AP管理 \-- AP管理配置命令 \-- description(AP view)**

------------------------------------------------------------------------

**[description**]命令用来设置AP的描述信息。

**[undo description**]命令用来清除AP的描述信息。

【命令】

**[description** *text*]

**[undo description**]

【缺省情况】

未设置AP的描述信息。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：网络中AP的描述信息，为1～64个字符的字符串，区分大小写。

【使用指导】

当存在多个AP时，可以配置每个AP的描述信息，以便区别各个AP。

使用**display wlan ap**命令可以看到配置的描述信息。

【举例】

\# 设置ap1的描述信息。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-ap-ap1 description L3-office

**AP管理 \-- AP管理配置命令 \-- description(AP group view)**

------------------------------------------------------------------------

**[description **]命令用来配置AP组的描述信息。

**[undo description**]命令用来清除AP组的描述信息。

【命令】

**[description ***text*]

**[undo description**]

【缺省情况】

未配置AP组的描述信息。

【视图】

AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[text*]：AP组的描述信息，为1～64个字符的字符串，区分大小写。

【使用指导】

当存在多个AP组时，可以配置每个AP组的描述信息，以便区别各个AP组。

使用**display wlan ap-group**命令可以看到配置的描述信息。

【举例】

\# 设置group1的描述信息。

\<Sysname\> system-view

Sysname wlan ap-group group1

Sysname-ap-group-group1 description L3-office

【相关命令】

·**wlan ap-group**

·**display wlan ap-group**

**AP管理 \-- AP管理配置命令 \-- display wlan ap**

------------------------------------------------------------------------

**[display wlan ap**]命令用来显示指定AP或所有AP的信息。

【命令】

**[display wlan ap****[{ **all** *\|* **name** *ap-name* } [ **radio** \| **verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc -admin

mdc -operator

【参数】

**[all**]：显示所有AP的信息。

**[name*** ap-name*]：指定AP的名称，*ap-name*表示AP的名称，为1～63个字符的字符串，可以包含字母、数字、下划线和横线。

**[radio**]：显示AP上radio的信息。

**[verbose**]：显示AP的详细信息。

【举例】

\# 显示所有AP的信息。

\<Sysname\> display wlan ap all

Total number of APs: 2

Total number of connected APs: 1

Total number of configured APs connected: 1

Total number of connected auto APs: 0

Maximum AP capacity: 60000

Remaining AP capacity: 59999

                                 AP information

 State : I = Idle,       J  = Join,       JA = JoinAck,    IL = ImageLoad

         C = Config,     DC = DataCheck,  R  = Run

AP name                AP ID   State   Model             Serial ID

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ap1                    1       I       WA4620i-AGN       210235A1BSC123000050

ap2                    2       R       WA5620i-AGN       210456B9CEN238400040

表1-1 display wlan ap name命令显示信息描述表

字段

描述

Total number of APs

AP的数量

Total number of connected APs

处于连接状态的AP的数量

Total number of configured APs connected

处于连接状态的手工AP数量

Total number of connected auto APs

处于连接状态的自动AP的数量

Maximum AP capacity

AC上最大AP容量

Remaining AP capacity

剩余AP容量，即最大AP容量减去处于连接状态的AP数

AP ID

AP的ID号，用于在AC上唯一标识一个AP

AP name

AP实体名

State

AP当前状态：

·I：空闲状态

·J：连接建立状态

·JA：LWAPP连接确认阶段

·IL：版本下载状态

·C：初始化配置下载状态

·DC：数据校验状态

·R：运行状态，表示AP与AC成功建立CAPWAP隧道

Model

AP型号信息

Serial ID

AP序列号，如果未指定，则显示为Not configured

\# 显示ap1的详细信息。

\<Sysname\> display wlan ap name ap1 verbose

AP name                       : ap1

AP ID                         : 1

State                         : Run

Model                         : WA4620i-AGN

Serial ID                     : 210235A1BSC123000050

IP address                    : 192.168.1.50

H/W version                   : Ver.C

S/W version                   : V700R001B49D001

Boot version                  : 1.01

Description                   : wtp1

Priority                      : 4

Echo interval                 : 10 seconds

Statistics report interval    : 50 seconds

CIR                           : 60 kbps

CBS                           : 3000 bytes

Jumbo frame value             : Disabled

MAC address                   : 80F6-2EBF-C580

MAC type                      : Local MAC & Split MAC

Tunnel mode                   : Local Bridging & 802.3 Frame & Native Frame

Discovery type                : Static Configuration

Retransmission count          : 3

Retransmission interval       : 5 seconds

Firmware upgrade              : Enabled

Sent control packets          : 1

Received control packets      : 1

Connection count              : 1

Radio 1:

    Basic BSSID               : N/A

    Admin state               : Down

    Radio type                : 802.11n(5GHz)

    Client dot11n-only        : Disabled

    Channel band-width        : 20/40MHz

    Secondary channel offset  : SCN

    Short GI for 20MHz        : Supported

    Short GI for 40MHz        : Supported

    A-MSDU                    : Enabled

    A-MPDU                    : Enabled

    Operational HT MCS Set:

        Mandatory             : Not configured

        Supported             : Not configured

    Channel                   : auto\<64\>

    Max power                 : 13 dBm

    Operational rate:

        Mandatory             : 6, 12, 24 Mbps

        Supported             : 9, 18, 36, 48, 54 Mbps

        Multicast             : 24 Mbps

        Disabled              : Not configured

    beacon-interval           : 100 time unit

    distance                  : 1 kilometer

Radio 2:

    Basic BSSID               : N/A

    Admin state               : Down

    Radio type                : 802.11n(2.4GHz)

    Client dot11n-only        : Disabled

    Channel band-width        : 20MHz

    Secondary channel offset  : SCN

    Short GI for 20MHz        : Supported

    Short GI for 40MHz        : Supported

    A-MSDU                    : Enabled

    A-MPDU                    : Enabled

    Operational HT MCS Set:

        Mandatory             : Not configured

        Supported             : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

                                10, 11, 12, 13, 14, 15

    Channel                   : auto\<6\>

    Max power                 : 20 dBm

    Preamble type             : short

    Operational rate:

        Mandatory             : 1, 2, 5.5, 11 Mbps

        Supported             : 6, 9, 12, 18, 24, 36, 48, 54 Mbps

        Multicast             : 11 Mbps

        Disabled              : Not configured

表1-2 display wlan ap name verbose命令显示信息描述表

字段

描述

AP ID

AP的ID号，用于唯一标识一个AP

State

AP当前状态：

·Idle：空闲状态

·Join：连接建立状态

·JoinAck：LWAPP连接确认状态

·Image Download：版本下载状态

·Config：初始化配置下载状态

·Data Check：数据校验状态

·Run：运行状态

Model

AP型号信息

Serial ID

AP序列号。如果未指定序列号，显示为Not configured

IP address

AP当前连接的IP地址

H/W version

AP当前硬件信息

S/W version

AP当前软件信息

Boot version

AP当前引导程序版本

Description

AP描述信息。如果未指定描述信息，显示为Not configured

Priority

AC配置的AP连接的优先级

Echo interval

AP的两次回声请求的时间间隔

Statistics report interval

AP上报统计信息的时间间隔

CIR

限制AC向AP发送数据报文的速率。如果未指定速率，显示为Not configured

CBS

限制AC向AP发送数据报文的突发尺寸。如果未指定突发尺寸，显示为Not configured

Jumbo frame value

AC配置的AP的Jumbo帧的最大长度。如果未指定最大长度，显示为Disabled

MAC address

AP的MAC地址

MAC type

AP与AC连接的MAC模式类型：

·Local MAC：AP侧数据帧支持802.3格式封装

·Split MAC：AP侧数据帧支持802.11格式封装

·Local & Split MAC：AP侧数据帧支持802.3与802.11格式封装

Tunnel mode

AP支持的隧道模式：

·Local Bridging：AP侧支持用户数据本地桥接，不上送给AC

·802.3 Frame：AP侧支持用户数据以802.3帧格式封装上传给AC

·Native Frame：AP侧支持用户数据以802.11帧格式封装上传给AC

·Local Bridging & 802.3 Frame：AP侧支持用户数据本地桥接、以802.3帧格式封装上传

·802.3 Frame & Native Frame：AP侧支持用户数据以802.3或802.11帧格式封装上传

·Local Bridging & Native Frame：AP侧支持用户数据本地桥接、以802.11帧格式封装上传

·Local Bridging & 802.3 Frame & Native Frame：AP侧支持用户数据本地桥接、以802.3或802.11帧格式封装上传

Discovery type

AP的发现方式：

·Static Configuration：AP使用静态配置的IPv4或IPv6地址发现AC

·DHCP：AP使用DHCP选项发现AC

·DNS：AP使用DHCP+DNS发现AC

·Unknown：未知的发现方式

Retransmission count

AC重传请求报文的重传次数

Retransmission interval

AC重传请求报文的重传间隔

Firmware upgrade

AP的版本下载：

·Enabled：开启AP的版本下载

·Disabled：关闭AP的版本下载

Sent control packets

AC在Run状态之后发送的控制报文的个数（包含Change State Event Response报文）

Received control packets

AC在Run状态之后接收的控制报文的个数（包含Change State Event Request报文）

Connection count

AP和AC的连接次数，只有在以下情况下连接次数会清零：

·AP重启

·重新配置AP序列号

需要注意的是，使用reset wlan ap命令不会造成AP连接次数清零

Basic BSSID

Radio的MAC地址。N/A表示AP还未与AC建立CAPWAP隧道

Admin state

Radio状态：

·Up：{.MsoCommentReference}Radio处于开启状态

·Down：{.MsoCommentReference}Radio处于关闭状态

Wireless mode

Radio类型：802.11a、802.11n（5GHz）、802.11b、802.11g、802.11n（2.4GHz）

Client dot11n-only

仅允许802.11n及802.11ac客户端接入功能：

·Disabled：兼容802.11a/b/g的无线客户端，同时还要接入802.11n或802.11ac的无线客户端

·Enabled：只有802.11n或802.11ac的无线客户端才能接入射频

Channel band-width

配置的带宽模式：

5MHz：工作带宽为5MHz

10MHz：工作带宽为10MHz

20MHz：工作带宽为20MHz

20/40MHz：工作带宽为20/40MHz

80MHz：工作带宽为80MHz

Secondary channel offset

802.11n射频模式中的辅信道信息：

SCA：Second Channel Above，表示射频当前工作在40MHz带宽模式，并且辅信道高于主信道

SCB：Second Channel Below，表示射频当前工作在40MHz带宽模式，并且辅信道低于主信道

SCN：表示射频未工作在40MHz带宽模式

Short GI for 20MHz

射频工作带宽为20MHz时，对于Short GI的支持情况：

Not supported：射频不支持20MHz Short GI

Supported：射频支持20MHz Short GI

Short GI for 40MHz

射频工作带宽为40MHz时，对于Short GI的支持情况：

Not supported：射频不支持40MHz Short GI

Supported：射频支持40MHz Short GI

Operational HT MCS Set

高吞吐操作MCS集：

·Supported：支持MCS索引

·Mandatory：强制MCS索引

A-MSDU

A-MSDU功能：

·Disabled：A-MSDU功能处于关闭状态

·Enabled：A-MSDU功能处于开启状态

A-MPDU

A-MPDU功能：

·Disabled：A-MPDU功能处于关闭状态

·Enabled：A-MPDU功能处于开启状态

Channel

Radio信道：

·Auto\<*Number*\>：表示自动信道模式根据实际环境自动选择最优信道

·*Number*：手动配置的工作信道

Maximum power

Radio的最大传输功率

Preamble type

前导码类型：

·Long：长和短前导码

·Short：短前导码

Operational rate

操作速率：

·Mandatory：强制速率

·Supported：支持速率

·Multicast：组播速率

·Disabled：禁止速率

·Not configured：未指定速率

\# 显示所有AP上的radio信息。

\<Sysname\> display wlan ap all radio

Total number of APs                       : 3

Total number of connected APs             : 1

Total number of connected auto APs        : 0

AP                    Radio ID             Channel           Tx power (dBm)

ap1                   1                    161               79

ap1                   2                    3                 100

ap2                   1                    157               79

ap2                   2                    11                100

ap3                   1                    161               79

ap3                   2                    5                 100

\# 显示ap1上的radio信息。

\<Sysname\> display wlan ap name ap1 radio

AP                    Radio ID             Channel          Tx power (dBm)

ap1                   1                    161              79

ap1                   2                    3                100

表1-3 display wlan ap name命令显示信息描述表

字段

描述

AP

AP名称

Radio ID

射频的ID号

Channel

射频使用的工作信道

Tx power (dBm)

射频的发送功率（缺省为最大功率）

**AP管理 \-- AP管理配置命令 \-- display wlan ap reboot-log**

------------------------------------------------------------------------

**[display wlan ap reboot-log**]命令用来显示指定AP的重启日志信息。

【命令】

**[display wlan ap reboot-log name** *ap-name*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc -admin

mdc -operator

【参数】

**[name*** ap-name*]：指定重启的AP的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

如果AP曾发生过系统崩溃，那么可以使用该命令查看相关信息，注意指定的AP必须处于Run状态。

【举例】

\# 显示名为ap1的AP的重启日志信息。

\<Sysname\> display wlan ap reboot-log name ap1

Debugging information is not available on the AC.

Downloading debugging data from AP. Continue? [Y/N:y]

Downloading debugging data. Please wait\...

Please enter the same command again to view the log messages.

【相关命令】

·**reset wlan ap reboot-log**

**AP管理 \-- AP管理配置命令 \-- display wlan ap-group**

------------------------------------------------------------------------

**[display wlan ap-group**]命令用来显示AP [Group]信息。

【命令】

**[display wlan ap-group** [\*group-name* []]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[group-name*]：显示指定的AP组信息。如果未指定本参数，表示显示所有AP组信息。

【举例】

\# 显示全部AP组的信息。

System display wlan ap-group

AP group name       : default-group

Description         : Not configured

AP model            : Not configured

APs                 : Not configured

AP group name       : group1

Description         : abcd

AP model            : WA2620i-AGN

AP grouping rules:

  AP name           : ap1, ap2

  Serial ID         : 123456789, 2345678

  MAC address       : 0012-2233-4455, 1112-3344-5566

APs                 : ap1 (AP name)

\# 显示指定AP组的信息。

System display wlan ap-group group1

AP group name       : group1

Description         : Not configured

AP model            : WA2620i-AGN

AP grouping rules:

  AP name           : ap1, ap2

  Serial ID         : 123456789, 2345678

  MAC address       : 0012-2233-4455, 1112-3344-5566

APs                 : ap1 (AP name)

表1-4 display wlan ap-group命令显示信息描述表

字段

描述

AP group name 

组名

AP grouping rules

入组规则

AP model

AP型号名

AP name

入组规则：AP名字列表

Serial ID

入组规则：AP 序列号列表

MAC address

入组规则：AP MAC地址列表

APs

AP组中的AP

【相关命令】

·**wlan ap-group**

**AP管理 \-- AP管理配置命令 \-- echo-interval**

------------------------------------------------------------------------

**[echo-interval**]命令用来设置两次回声请求的时间间隔。

**[undo echo-interval**]命令用来恢复缺省情况。

【命令】

**[echo-interval** *interval*]

**[undo echo-interval**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：AP发送回声请求的时间间隔为10秒。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定AP发送两次回声请求之间的时间间隔，取值范围为5～80，单位为秒。

【使用指导】

AP和AC之间通过保活机制来检查控制隧道是否正常工作。AP周期性地向AC发送回声请求Echo request报文，若一定时间内没有收到AC回复的Echo response报文，则AP断开控制隧道；若AC在一定时间内没有收到Echo request报文，则AC断开控制隧道。

【举例】

\# 设置ap3向AC发送的回声请求时间间隔为15秒。

\<Sysname\> system-view

Sysname wlan ap ap3 model WA4620i-AGN

Sysname-wlan-ap-ap3 echo-interval 15

**AP管理 \-- AP管理配置命令 \-- firmware-upgrade enable**

------------------------------------------------------------------------

**[firmware-upgrade enable**]命令用来开启AP版本下载功能。

**[firmware-upgrade disable**]命令用来关闭AP版本下载功能。

**[undo firmware-upgrade**]命令用来恢复缺省情况。

【命令】

**[firmware-upgrade**[ { **disable** \| **enable** }]]

**[undo firmware-upgrade**]

【缺省情况】

AP视图：开启AP版本下载功能。

AP组视图：未开启AP版本下载功能。

全局配置视图：AP版本下载功能处于开启状态。

【视图】

AP视图/AP组视图/全局配置视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：关闭AP版本下载功能。

**[enable**]：开启AP版本下载功能。

【使用指导】

·建立CAPWAP隧道过程中，如果开启AP版本下载功能，且AP的固件版本低于AC的固件版本时，则AP必须从AC上下载对应的固件版本文件后才能与AC建立CAPWAP隧道连接。

·建立CAPWAP隧道过程中，如果关闭AP版本下载功能，则不比较AP当前的固件版本和AC的固件版本，直接与AC建立CAPWAP隧道连接。

【举例】

\# 开启ap3的版本下载功能。

\<Sysname\> system-view

Sysname wlan ap ap3 model WA4620i-AGN

Sysname-wlan-ap-ap3 firmware-upgrade enable

**AP管理 \-- AP管理配置命令 \-- jumboframe enable**

------------------------------------------------------------------------

**[jumboframe enable**]命令用来开启Jumbo帧传输功能并设置Jumbo帧的最大长度。

**[undo jumboframe enable**]命令用来恢复缺省情况。

【命令】

**[jumboframe enable** *value*]

**[undo jumboframe enable**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：未开启Jumbo帧的传输功能。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：指定Jumbo帧的最大长度，取值范围为1500～1748，单位为字节。

【使用指导】

·Jumbo帧即超长帧，在进行文件传输等大吞吐量数据的时候，AP收到帧的长度可能大于标准以太网帧的长度，通过配置此命令允许不超过指定长度的超长帧通过。

·若AP收到的帧长度大于配置的Jumbo帧的最大长度，则AP会使用配置的Jumbo帧长度对该帧进行分片。

【举例】

\# 设置Jumbo帧的长度为1500字节。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-ap-ap1 jumboframe enable 1500

**AP管理 \-- AP管理配置命令 \-- mac-address**

------------------------------------------------------------------------

**[mac-address**]命令用来配置AP MAC 地址入组规则。

**[undo mac-address**]命令用来删除AP MAC 地址入组规则。

【命令】

**[mac-address** *mac-address*]

**[undo mac-address** *mac-address* ]

【缺省情况】

未配置AP MAC地址入组规则。

【视图】

AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：AP的MAC地址，形式为H-H-H。

【使用指导】

·同一AP组下AP MAC地址可配置多个。

·AP名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于MAC地址入组规则。AP优先根据AP名字入组规则匹配入组，其次是AP序列号入组规则，最后是AP MAC 地址入组规则，若为匹配到任何入组规则，则AP将被加入到默认组。

·若其它组已经存在该MAC地址入组规则，在新组配置该MAC地址入组规则，则原AP组将删除该MAC地址入组规则。

·默认组视图下不能进行该配置。

【举例】

\# 在AP组视图下添加AP MAC地址入组规则0AC1-F9B2-B1C2。

\<System\> system-view

System wlan ap-group group1

System-wlan-ap-group-group1 mac-address 0AC1-F9B2-B1C2

【相关命令】

·**wlan****ap-group**

**AP管理 \-- AP管理配置命令 \-- priority**

------------------------------------------------------------------------

**[priority**]命令用来配置AC上AP连接的优先级。

**[undo priority**]命令用来恢复缺省情况。

【命令】

**[priority** *priority*]

**[undo priority**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：AP连接的优先级为4。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority*]：AP连接的优先级，取值范围为0～255。该数值越大，优先级越高。

【使用指导】

建立CAPWAP隧道的过程中，AP会优先选择优先级高的AC建立隧道连接。

【举例】

\# 配置AP连接的优先级为255。

\<Sysname\> system-view

Sysname wlan ap ap3 model WA4620i-AGN

Sysname-wlan-ap-ap3 priority 255

**AP管理 \-- AP管理配置命令 \-- reset wlan ap**

------------------------------------------------------------------------

**[reset wlan ap**]命令用来重启AP。

【命令】

**[reset wlan ap**[ { **all** \| **name** *ap-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：重启连接到当前AC的所有AP。

**[name*** ap-name*]：指定重启AP的名称，为1～63个字符的字符串，不区分大小写。

【使用指导】

当AC要断开与AP的CAPWAP隧道连接时，输入此命令，AP重启，AC端与AP相关的连接资源将被清除。

【举例】

\# 重启ap1。

\<Sysname\> reset wlan ap name ap1

Reset the AP that has established or is to establish a primary tunnel with the AC. Continue? [Y/N:]

**AP管理 \-- AP管理配置命令 \-- reset wlan ap reboot-log**

------------------------------------------------------------------------

**[reset wlan ap reboot-log**]命令用来清除指定AP或全部AP的重启日志信息。

【命令】

**[reset wlan ap reboot-log**[ { **all** \| **name** *ap-name* }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：清除所有AP的重启日志信息。

**[name*** ap-name*]：清除指定名称的AP的重启日志信息，为1～63个字符的字符串，不区分大小写。

【举例】

\# 清除ap1的重启日志信息。

\<Sysname\> reset wlan ap reboot-log name ap1

【相关命令】

·**display wlan ap reboot-log**

**AP管理 \-- AP管理配置命令 \-- retransmit-count**

------------------------------------------------------------------------

**[retransmit-count**]命令用来设置AC发送给AP的请求报文重传次数。

**[undo retransmit-count**]命令用来恢复缺省情况。

【命令】

**[retransmit-count** *value*]

**[undo retransmit-count**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：请求报文重传次数为3次。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：指定请求报文重传次数，取值范围为2～5。

【使用指导】

为了使AC的请求报文尽可能的发送到AP，提高报文的可靠传输能力，AC会对请求报文进行重传。

重传次数为配置的请求报文重传次数。

AC发送给AP的请求报文包括Image Data Request报文、Configuration Update Request报文、Reset Request报文、Data Transfer Request报文、IEEE 802.11 WLAN Configuration Request报文和Station Configuration Request报文。

【举例】

\# 配置AC发往ap3的请求报文重传次数为4。

\<Sysname\> system-view

Sysname wlan ap ap3 model WA4620i-AGN

Sysname-wlan-ap-ap3 retransmit-count 4

【相关命令】

·**retransmit-interval**

**AP管理 \-- AP管理配置命令 \-- retransmit-interval**

------------------------------------------------------------------------

**[retransmit-interval**]命令用来设置请求报文重传的时间间隔。

**[undo retransmit-interval**]命令用来恢复缺省情况。

【命令】

**[retransmit-interval** *interval*]

**[undo retransmit-interva**l]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：请求报文重传的时间间隔为5秒。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定请求报文重传的时间间隔，取值范围为3～8，单位为秒。

【使用指导】

为了使AC的请求报文尽可能的发送到AP，提高报文的可靠传输能力，AC会对请求报文进行重传。

重传时间间隔为配置的请求报文重传时间。

AC发送给AP的请求报文包括Image Data Request报文、Configuration Update Request报文、Reset Request报文、Data Transfer Request报文、IEEE 802.11 WLAN Configuration Request报文和Station Configuration Request报文。

【举例】

\# 设置AC发往ap3的请求报文重传的时间间隔为6秒。

\<Sysname\> system-view

Sysname wlan ap ap3 model WA4620i-AGN

Sysname-wlan-ap-ap3 retransmit-interval 6

【相关命令】

·**retransmit-count**

**AP管理 \-- AP管理配置命令 \-- serial-id(AP view)**

------------------------------------------------------------------------

**[serial-id**]命令用来配置AP的序列号。

**[undo serial-id**]命令用来恢复缺省情况。

【命令】

**[serial-id** *serial-id*]

**[undo serial-id**]

【缺省情况】

未配置AP的序列号。

【视图】

AP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[serial-id*]：指定AP的序列号，序列号为每个AP的唯一标识，为1～127个字符的字符串，不区分大小写。

【使用指导】

如果AP已经与AC建立CAPWAP隧道连接，改变和删除序列号将触发CAPWAP隧道的拆除，AP将会重新发现AC并与AC建立CAPWAP隧道。

【举例】

\# 将ap1的序列号设置为210235A1BSC123000050。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-ap-ap1 serial-id 210235A1BSC123000050

**AP管理 \-- AP管理配置命令 \-- serial-id(AP group view)**

------------------------------------------------------------------------

**[serial-id**]命令用来配置AP序列号入组规则。

**[undo serial-id**]命令用来删除AP序列号入组规则。

【命令】

**[serial-id** *serial-id*]

**[undo serial-id** *serial-id*]

【缺省情况】

未配置AP序列号入组规则。

【视图】

AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[serial-id*]：AP序列号，为1～63个字符的字符串，输入后的字母自动改为大写形式。

【使用指导】

·同一AP组下AP序列号可配置多个。配置后符合该序列号的AP可以入组。

·AP名字如入规则的优先级高于序列号入组规则，序列号入组规则的优先级高于MAC地址入组规则。AP优先根据AP名字入组规则匹配入组，其次是AP序列号入组规则，最后是AP MAC 地址入组规则，若为匹配到任何入组规则，则AP将被加入到默认组。

·若其它组已经存在该序列号入组规则，在新组配置该序列号入组规则，则原AP组将删除该序列号入组规则。

·默认组视图下不能进行该配置。

【举例】

\# 在AP组视图下添加序列号入组规则serial-id SER123。

\<System\> system-view

System wlan ap-group group1

System-wlan-ap-group-group1 serial-id SERl123

【相关命令】

·**wlan****ap-group**

**AP管理 \-- AP管理配置命令 \-- statistics-interval**

------------------------------------------------------------------------

**[statistics-interval**]命令用来配置AP向AC上报Radio统计信息的时间间隔。

**[undo statistics-interval**]命令用来恢复缺省情况。

【命令】

**[statistics-interval** *interval*]

**[undo statistics-interval**]

【缺省情况】

AP视图：继承AP组配置。

AP组视图：AP向AC上报Radio统计信息的时间间隔为50秒。

【视图】

AP视图/AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：指定AP向AC上报Radio统计信息的时间间隔，取值范围为2～120，单位为秒。

【使用指导】

为了对AP的运行情况进行有效监控，AP会周期性的向AC上报Radio统计信息。

【举例】

\# 设置ap1上报Radio统计信息的时间间隔为10秒。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-wlan-ap-ap1 statistics-interval 10

**AP管理 \-- AP管理配置命令 \-- wlan ap**

------------------------------------------------------------------------

**[wlan ap**]命令用来创建并进入AP视图。

**[undo wlan ap**]命令用来删除指定的AP。

【命令】

**[wlan ap ***ap-name * **model** *model-name* ]

**[undo wlan ap*** ap-name *]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ap-name*]：AP的名称，为1～63个字符的字符串，不区分大小写。

**[model*** model-name*]：AP的型号名称，在创建AP时，该参数必须配置。

【使用指导】

·**wlan ap**命令用来创建并进入AP视图。如果指定的AP已创建，则该命令直接用来进入该AP视图。

·**undo wlan ap**命令用来删除指定的AP，如果AP已经与AC建立了CAPWAP隧道连接，使用**undo wlan ap**命令将会导致连接断开。

【举例】

\# 创建ap1。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-AGN

Sysname-wlan-ap-ap1

**AP管理 \-- AP管理配置命令 \-- wlan apdb file**

------------------------------------------------------------------------

**[wlan apdb file**]命令用来加载APDB用户脚本文件。

**[undo wlan apdb file**]命令用来卸载APDB用户脚本文件。

【命令】

**[wlan apdb file ***user.apdb*]

**[undo wlan apdb file**]

【视图】

系统视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[user.apdb*]：指定需要加载的APDB用户脚本文件名，为1～63个字符的字符串，区分大小写。apdb为文件后缀。

【使用指导】

·使用本命令加载用户脚本文件后，脚本文件中的AP型号信息将被加载到APDB中。

·用户脚本只能加载一个，支持重复加载，当重复加载时，新脚本内容会替换旧脚本内容。若旧脚本中的某个AP型号已经加入AP组及全局配置，且该AP型号在新脚本中被删除或者有修改时则不允许替换操作，提示用户加载失败。

【举例】

\# 加载名为user.apdb的用户脚本。

\<Sysname\> system-view

Sysname wlan apdb file user.apdb

**AP管理 \-- AP管理配置命令 \-- wlan ap-group**

------------------------------------------------------------------------

**[wlan ap-group**]命令用来创建一个AP组并进入AP组视图。

**[undo wlan ap-group**]命令用来删除一个AP组。

【命令】

**[wlan ap-group** *group-name*]

**[undo wlan ap-group** *group-name*]

【缺省情况】

存在默认组default-group，不允许删除。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[group-name*]：AP组的名称，为1～31个字符的字符串，不区分大小写。

【使用指导】

·最多可配置128个AP组。

·当执行该命令创建一个已经存在的组时，不会覆盖原有的组，而是进入AP组视图。

【举例】

\# 创建一个名为group1的AP组。

\<System\> system-view

System wlan ap-group group1

System-wlan-ap-group-group1

【相关命令】

·**display wlan ap-group**

**AP管理 \-- AP管理配置命令 \-- wlan auto-ap**

------------------------------------------------------------------------

**[wlan auto-ap**]命令用来开启自动AP功能。

**[undo wlan auto-ap**]命令用来恢复缺省情况。

【命令】

**[wlan auto-ap**]

**[undo wlan auto-ap**]

【缺省情况】

未开启自动AP功能。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·在无线网络中部署的AP数量较多时，使用自动AP功能可以减少管理员的配置工作量，并可以简化配置，避免多次配置AP序列号，同时降低了配置出错的概率。

·自动AP不能单独配置，需要固化为手工AP或者通过AP Group进行配置。

【举例】

\# 开启自动AP功能。

\<Sysname\> system-view

Sysname wlan auto-ap

**AP管理 \-- AP管理配置命令 \-- wlan global-configuration**

------------------------------------------------------------------------

**[wlan global-configuration**]命令用来进入全局配置视图。

【命令】

**[wlan global-configuration**]

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 进入全局配置视图。

\<System\> system-view

System wlan global-configuration

System-wlan-global-configuration

**AP管理 \-- AP管理配置命令 \-- wlan re-group**

------------------------------------------------------------------------

**[wlan re-group**]命令用于将一个或者一组AP规则迁移到指定AP组。

【命令】

**[wlan re-group*******old-group-name*[ \| mac-address *mac-address* \| serial-id *serial-id* } *group-name*]

【视图】]

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ap*** ap-name*]：将指定的AP名字入组规则迁移到目的AP组。

**[ap-list** *list-name*]：将指定的AP列表名的AP迁移到目的AP组。

**[mac-address ***mac-address*]：将指定的MAC地址入组规则迁移到目的组。

**[serial-id** *serial-id*]：将指定的序列号地址入组规则迁移到目的组。

**[ap-group** *old-group-name*]：将指定的AP组的入组规则迁移到目的AP组。*old-group-name*不能是默认组。

group-name：目的AP组名字，不能是默认组。

【举例】

\# 创建AP组group2。

\<System\> system-view

System wlan ap-group group2

System-wlan-ap-group-group2 quit

\# 创建AP组group1，在group1下配置三个AP名字规则ap1、ap2、ap3，并将ap1移至group2。

System wlan ap-group group1

System-wlan-ap-group-group1 ap ap1 ap2 ap3

System-wlan-ap-group-group1 quit

System wlan re-group ap ap1 group2

\# 创建AP列表list1，并且在list1下配置一个AP MAC地址2-2-2-2，并将list1移至group2。

System wlan ap-list list1

System-wlan-ap-list-list1 mac-address 2-2-2-2

System-wlan-ap-list-list1 quit

System wlan re-group ap-list list1 group2

\# 将group1中所有AP规则移至group2。

System wlan re-group ap-group group1 group2
