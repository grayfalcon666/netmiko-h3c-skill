<!-- CMD-INDEX
  confidentiality-offset              | MKA策略视图          | L24
  display macsec                      | 任意视图             | L80
  display mka policy                  | 任意视图             | L292
  display mka session                 | 任意视图             | L382
  display mka statistics              | 任意视图             | L618
  macsec confidentiality-offset       | 以太网接口视图          | L728
  macsec desire                       | 以太网接口视图          | L788
  macsec replay-protection enable     | 以太网接口视图          | L830
  macsec replay-protection window-size | 以太网接口视图          | L886
  macsec validation mode              | 以太网接口视图          | L948
  mka apply policy                    | 以太网接口视图          | L1008
  mka enable                          | 以太网接口视图          | L1072
  mka policy                          | 系统视图             | L1120
  mka priority                        | 以太网接口视图          | L1186
  mka psk                             | 以太网接口视图          | L1242
  replay-protection enable            | MKA策略视图          | L1304
  replay-protection window-size       | MKA策略视图          | L1356
  reset mka session                   | 用户视图             | L1416
  reset mka statistics                | 用户视图             | L1454
  validation mode                     | MKA策略视图          | L1488
-->

**MACsec \-- MACsec配置命令 \-- confidentiality-offset**

------------------------------------------------------------------------

**[confidentiality-offset**]命令用来配置MACsec加密偏移量。

**[undo confidentiality-offset**]命令用来恢复缺省情况。

【命令】

**[confidentiality-offset** *offset-value*]

**[undo confidentiality-offset**]

【缺省情况】

MACsec加密偏移量为0，表示整个数据帧都要加密。

【视图】

MKA策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[offset-value*]：MACsec加密偏移量，取值包括0、30和50，单位为字节。

【使用指导】

·MACsec加密偏移量，表示从用户数据帧帧头开始偏移多少字节后开始加密。

·MACsec加密偏移量最终以密钥服务器发布的加密偏移量为准。如果本端不是密钥服务器，则应用密钥服务器发布的加密偏移量；如果本端是密钥服务器，则应用本端配置的加密偏移量。

·在MKA策略中配置的MACsec加密偏移量，在该MKA策略成功应用到接口上之后，将会覆盖该接口上配置的MACsec加密偏移量。

【举例】

\# 在MKA策略abcd中配置MACsec加密偏移量为30字节。

\<Sysname\> system-view

Sysname mka policy abcd

Sysname-mka-policy-abcd confidentiality-offset 30

【相关命令】

·**macsec confidentiality-offset**

·**mka apply policy**

**MACsec \-- MACsec配置命令 \-- display macsec**

------------------------------------------------------------------------

**[display** **macsec**]命令用来显示接口的MACsec运行信息。

【命令】

**[display macsec **\**[ interface ***interface-type interface-number* [ \**verbose** ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示接口上的MACsec运行的摘要信息。*interface-type interface-number*表示指定接口类型和接口编号。不指定该参数，则表示显示所有接口上的MACsec运行信息。

**[verbose**]：显示接口上的MACsec运行的详细信息。若不指定该参数，则表示显示MACsec运行的摘要信息。

【举例】

\# 显示接口GigabitEthernet1/0/1上的MACsec运行的摘要信息。

\<Sysname\> display macsec interface gigabitethernet 1/0/1

Interface GigabitEthernet1/0/1

  Protect frames         : Yes

  Active MKA policy      : PL01

  Replay protection      : Enabled

  Replay window size     : 0 frames

  Confidentiality offset : 0 bytes

  Validation mode        : Check

\# 显示接口GigabitEthernet1/0/1上的MACsec运行的详细信息。

\<Sysname\> display macsec interface gigabitethernet 1/0/1 verbose

Interface GigabitEthernet1/0/1

  Protect frames         : Yes

  Active MKA policy      : PL01

  Replay protection      : Enabled

  Replay window size     : 0 frames

  Confidentiality offset : 0 bytes

  Validation mode        : Check

  Included SCI           : No

  SCI conflict           : No

  Cipher suite           : GCM-AES-128

  Transmit secure channel:

    SCI           : 000C29F6A4380004

      Elapsed time: 00h:02m:19s

      Current SA  : AN 0        PN 1

  Receive secure channels:

    SCI           : 000C29258D430124

      Elapsed time: 00h:02m:17s

      Current SA  : AN 0        LPN 1

      Previous SA : AN N/A      LPN N/A

表1-1 display macsec命令显示信息描述表

字段

描述

Interface

使能了MKA协议的接口名称

Protect frames

接口上是否开启MACsec数据帧保护功能，包括以下取值：

·Yes：需要进行MACsec数据帧保护

·No：不进行MACsec数据帧保护

接口上不存在MKA主要行动者时显示为N/A

Active MKA policy

接口应用的且生效的MKA策略。接口上未开启MACsec数据帧保护功能时，显示为N/A；如果接口上开启了MACsec数据帧保护功能但没有应用实际生效的策略，不显示该字段

Replay protection

接口的重播保护功能的开启状态，包括以下取值：

·Enabled：处于开启状态

·Disabled：处于关闭状态

接口上的MACsec数据帧保护功能未开启时显示为N/A

Replay window size

接口的重播保护窗口大小，单位为数据帧。接口上未开启MACsec数据帧保护功能或接口上未开启重播保护功能时，显示为N/A

Confidentiality offset

接口的加密偏移量，单位为字节。接口上未开启MACsec数据帧保护功能时显示为N/A

Validation mode

接口上的数据帧校验模式，包括以下取值：

·Check：检查模式

·Disabled：校验功能关闭

·Strict：严格校验模式

·N/A：接口上未开启MACsec数据帧保护功能

Included SCI

数据帧的SecTAG里是否携带SCI，包括以下取值：

·Yes：携带SCI

·No：未携带SCI

接口上未开启MACsec数据帧保护功能时显示为N/A

SCI conflict

收到的MKA协议报文的SCI和本端的SCI是否相同，包括以下取值：

·Yes：收到的MKA协议报文的SCI和本端的SCI相同

·No：没有收到MKA协议报文或者收到的MKA协议报文的SCI和本端的SCI不相同

Cipher suite

保护数据帧的加密套件。接口上未开启MACsec数据帧保护功能时，显示为N/A

Transmit secure channel

发送数据帧的安全通道信息。接口上未开启MACsec数据帧保护功能时，不显示安全通道信息

Receive secure channels

接收数据帧的安全通道信息。接口上的未开启MACsec数据帧保护功能时，不显示安全通道信息

Elapsed time

SC存在的时间

SCI

SCI信息，由MAC地址和Port ID组成，为一个十六进制数

Current SA

安全通道当前使用的SA

若无此信息，则对应的AN、PN和LPN显示为N/A

Previous SA

安全通道使用的前一个SA

若无此信息，则对应的AN和LPN显示为N/A

PN

发送的报文编号

AN

SA编号

LPN

SAK可接收的最小报文编号

【相关命令】

·**mka apply policy**

**MACsec \-- MACsec配置命令 \-- display mka policy**

------------------------------------------------------------------------

**[display mka policy**]命令用来显示MKA策略相关信息。

【命令】

**[display mka**[ { **default-policy** \| **policy** [ **name** *policy-name* ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[default-policy**]：表示显示默认的MKA策略。

**[policy**]：表示显示指定的MKA策略。

**[name** *policy-name*]：指定MKA策略名。*policy-name*为1～16个任意字符的字符串，区分大小写[。若不指定该参数，则表示显示所有当前已有的]MKA策略。

【举例】

\# 显示所有MKA策略相关信息。

\<Sysname\> display mka policy

PolicyName          ReplayProtection   WindowSize    ConfOffset    Validation

default-policy      Yes                0             0             Check

policy1             Yes                0             30            Check

policy2             Yes                100           0             Disabled

policy3             No                 0             0             Strict

policy4             Yes                200           50            Check

policy5             Yes                0             0             Check

表1-2 display mka policy命令显示信息描述表

字段

描述

PolicyName

MKA策略名

ReplayProtection

重播保护功能是否开启

WindowSize

重播保护窗口大小，单位为数据帧

ConfOffset

加密偏移量，单位为字节

Validation

数据帧校验模式，包括以下取值：

·Check：检查模式

·Disabled：校验功能关闭

·Strict：严格校验模式

【相关命令】

·**mka policy**

·**mka apply policy**

**MACsec \-- MACsec配置命令 \-- display mka session**

------------------------------------------------------------------------

**[display mka session**]命令用来显示MKA会话信息。

【命令】

**[display mka session **[ **interface*** interface-type interface-number*[ \| **local-sci** *sci-id* ]  **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口的MKA的会话信息。*interface-type interface-number*为接口类型和接口编号。若不指定该参数，则表示显示所有接口上的MKA会话信息。

**[local-sci*** sci-id*]：表示本地发送通道标识。*sci-id*为16个字符的十六进制数，不区分大小写。

**[verbose**]：显示接口上的MKA的会话的详细信息。若不指定该参数，则表示显示MKA的会话的简要信息。

【举例】

\# 显示接口GigabitEthernet1/0/1上的MKA会话摘要信息。

\<Sysname\> display mka session interface gigabitethernet 1/0/1

Interface GigabitEthernet1/0/1

Tx-SCI    : 000C29F6A4380004

Priority  : 0

Capability: 3

  CKN for participant: ABCD

    Key server            : Yes

    MI (MN)               : D7B00EDA353242704CC6B0DB (7)

    Live peers            : 1

    Potential peers       : 0

    Principal actor       : Yes

    MKA session status    : Secured

    Confidentiality offset: 30 bytes

\# 显示接口GigabitEthernet1/0/1上的MKA会话详细信息。

\<Sysname\> display mka session interface gigabitethernet 1/0/1 verbose

Interface GigabitEthernet1/0/1

Tx-SCI    : 000C29F6A4380004

Priority  : 0

Capability: 3

  CKN for participant: ABCD

    Key server            : Yes

    MI (MN)               : D7B00EDA353242704CC6B0DB (7)

    Live peers            : 1

    Potential peers       : 0

    Principal actor       : Yes

    MKA session status    : Secured

    Confidentiality offset: 30 bytes

    Current SAK status    : Rx & Tx

    Current SAK AN        : 0

    Current SAK KI (KN)   : 4273791304C1C26259C94C3400000001 (1)

    Previous SAK status   : N/A

    Previous SAK AN       : N/A

    Previous SAK KI (KN)  : N/A

    Live peer list:

    MI                        MN         Priority  Capability  Rx-SCI

    EA58DC3F8715953DBC6593F0  840        100       3           00E0020000000106

    Potential peer list:

    MI                        MN         Priority  Capability  Rx-SCI

    DA58DC3Q4573543DBC6699F0  3          200       3           00E0021200000107

表1-3 display mka session 命令显示信息描述表

字段

描述

Interface

接口名称

Tx-SCI

发送SCI，采用十六进制格式

Priority

表示密钥服务器的优先级，取值为0～255

Capability

MACsec能力，取值如下：

·0：表示不支持MACsec功能

·1：表示只支持完整性服务，不支持机密性服务

·2：表示支持完整性服务，可选择支持机密性服务（加密偏移量只能为0）

·3：表示支持完整性服务，可选择支持机密性服务（加密偏移量可支持0，30及50）

CKN for participant

MKA实例的CKN

Key server

本端是否为密钥服务器

MI

成员标识，采用十六进制格式

MN

消息序号

Live peers

已经学习到的对端的个数

Potential peers

正在协商中的对端的个数

Principal actor

该MKA实例是否为主要行动者。其中，MKA实例表示MKA协议在该接口上的运行实体，当该MKA实例处于Active状态时，被称为主要行动者

MKA session status

MKA会话的状态：

·Unknown：表示未知状态

·Pending：表示挂起状态

·Unauthenticated：表示未认证状态

·Authenticated：表示认证状态，接口已通过802.1X认证

·Secured：表示安全状态，会话将被保护

·N/A：表示该MKA实例不是主要行动者

Confidentiality offset

密钥服务器发布的加密偏移量，明文通信或该MKA实例不是主要行动者时显示为N/A

Current SAK status

当前使用的SAK的状态（Tx表示用于发送，Rx表示用于接收），当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

Current SAK AN

当前使用的SAK的SA编号，当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

Current SAK KI

当前使用的SAK的密钥标识，由12字节的密钥服务器的MI和KN组成，采用十六进制格式，当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

KN

SAK编号，当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

Previous SAK status

前一个SAK的状态（Tx表示用于发送，Rx表示用于接收），当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

Previous SAK AN

前一个SAK的SA编号，当该MKA实例不是主要行动者或SAK不存在时，显示为N/A

Previous SAK KI

前一个SAK的密钥标识，由12字节的密钥服务器的MI和KN组成，采用十六进制格式，当该MKA实例不是主要行动者或SAK不存在时，显为N/A

Live peer list

已经学习到的对端列表，当不存在Live peer时，不显示该字段

Potential peer list

正在协商过程中的对端列表，当不存在Potential peer时，不显示该字段

Rx-SCI

接收SCI，采用十六进制格式

【相关命令】

·**reset mka session**

**MACsec \-- MACsec配置命令 \-- display mka statistics**

------------------------------------------------------------------------

**[display mka statistics**]命令用来显示接口上的MKA统计信息。

【命令】

**[display mka statistics ** **interface** *i*]*nterface-type interface-number *

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface** *interface-type interface-number*]：指定接口类型和接口编号[。若不指定该参数，则表示显示所有接口上的]MKA统计信息。

【举例】

\# 显示接口GigabitEthernet1/0/1的MKA统计信息。

\<Sysname\> display mka statistics interface gigabitethernet 1/0/1

Interface GigabitEthernet1/0/1 statistics

MKPDUs with invalid CKN : 0

MKPDUs with invalid ICV : 0

MKPDUs with Rx error    : 0

CKN for participant     : ABCD

  Tx MKPDUs             : 2379

  Rx MKPDUs             : 2375

  MKPDUs with invalid MN: 0

  MKPDUs with Tx error  : 0

  SAKs distributed      : 0

  SAKs received         : 5

表1-4 display mka statistics命令显示信息描述表

字段

描述

Interface Gigabitethernet1/0/1 statistics

接口上的MKA统计信息

MKPDUs with invalid CKN

收到的且找不到匹配CKN的MKA协议报文个数

MKPDUs with invalid ICV

ICV校验失败的MKA协议报文个数

MKPDUs with Rx error

接收到错误的MKA协议报文个数

CKN for participant

MKA实例的CKN

Tx MKPDUs

实例发送的MKA协议报文个数

Rx MKPDUs

实例接收的MKA协议报文个数

MKPDUs with invalid MN

实例接收到非法MN的MKA协议报文个数

MKPDUs with Tx error

实例发送错误的MKA协议报文个数

SAKs distributed

实例分发的SAK个数

SAKs received

实例接收的SAK个数

【相关命令】

·**reset mka statistics**

**MACsec \-- MACsec配置命令 \-- macsec confidentiality-offset**

------------------------------------------------------------------------

**[macsec confidentiality-offset**]命令用来配置接口上的MACsec加密偏移量。

**[undo macsec confidentiality-offset**]命令用来恢复缺省情况。

【命令】

**[macsec confidentiality-offset ***offset-value*]

**[undo macsec confidentiality-offset**]

【缺省情况】

接口上的MACsec加密偏移量为0，表示整个数据帧都要加密。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[offset-value*]：数据帧的加密偏移量，取值包括0、30和50，单位为字节。

【使用指导】

MACsec加密偏移量，表示从用户数据帧帧头开始偏移多少字节后开始加密。

·如果首先在接口上通过**mka apply policy**命令应用MKA策略，然后在该接口上配置加密偏移量，则接口上应用的MKA策略将被取消，取而代之保存的配置将是，接口上配置的加密偏移量以及该MKA策略中的除加密偏移量之外的其它所有配置。

·如果本端不是密钥服务器，则应用密钥服务器发布的加密偏移量；如果本端是密钥服务器，则应用本端配置的加密偏移量，并将该值发布给对端。

【举例】

\# 配置接口GigabitEthernet1/0/1上的MACsec加密偏移量为30字节。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 macsec confidentiality-offset 30

【相关命令】

·**confidentiality-offset **

·**display macsec**

·**display mka session**

·**mka apply policy**

**MACsec \-- MACsec配置命令 \-- macsec desire**

------------------------------------------------------------------------

**[macsec desire**]命令用来启用MACsec保护，即接口期望对发送的数据帧进行MACsec保护。

**[undo macsec desire**]命令用来恢复缺省情况。

【命令】

**[macsec desire**]

**[undo** **macsec desire**]

【缺省情况】

接口上不需要对发送的数据帧进行MACsec保护。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

**[macsec desire**]命令仅用来告知对端，本端发送的数据帧需要进行MACsec保护，但最终本端发送的数据帧是否启用MACsec保护，要由密钥服务器来决策。决策策略是：密钥服务器和它的对端支持MACsec功能，且它们至少有一个请求MACsec保护。

【举例】

\# 配置接口GigabitEthernet1/0/1期望对发送的数据帧进行MACsec保护。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 macsec desire

**MACsec \-- MACsec配置命令 \-- macsec replay-protection enable**

------------------------------------------------------------------------

**[macsec replay-protection enable**]命令用来开启接口上的MACsec重播保护功能。

**[undo macsec replay-protection enable**]命令用来关闭接口上的MACsec重播保护功能。

【命令】

**[macsec replay-protection enable**]

**[undo macsec** **replay-protection enable**]

【缺省情况】

接口上的MACsec重播保护功能处于开启状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·MACsec重播保护功能可以单独开启，且仅针对接收到的数据帧。

·重播保护功能可以防止本端收到乱序或重复的数据帧。

·如果首先在接口上通过**mka apply policy**命令应用MKA策略，然后在该接口上使能MACsec重播保护功能，则接口上应用的MKA策略将被取消，取而代之保存的配置将是，接口上已开启MACsec重播保护功能以及该MKA策略中的除MACsec重播保护功能之外的其它所有配置。

【举例】

\# 开启接口GigabitEthernet1/0/1上的MACsec重播保护功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 macsec replay-protection enable

【相关命令】

·**display macsec**

·**mka apply policy**

·**macsec replay-protection window-size**

·**replay-protection enable**

**MACsec \-- MACsec配置命令 \-- macsec replay-protection window-size**

------------------------------------------------------------------------

**[macsec replay-protection window-size**]命令用来配置接口上的MACsec重播保护窗口大小。

**[undo** **macsec replay-protection window-size**]命令用来恢复缺省情况。

【命令】

**[macsec replay-protection window-size ***size-value*]

**[undo macsec** **replay-protection window-size**]

【缺省情况】

接口上的MACsec重播保护窗口大小为0个数据帧，表示不允许接收乱序或重复的数据帧。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size-value*]：重播保护窗口大小，取值范围为0～4294967295，单位为数据帧。

【使用指导】

在某些组网下（如数据帧经过运营商网络转发），因为用户数据帧的发送优先级不同，在转发过程中会被重新排序，最终到达接收端会出现乱序。如果要正常接收这些乱序的数据帧，需要开启重播保护功能，且配置重播保护窗口。假设配置的重播保护窗口大小为a，如果接收到了一个报文序号（PN，Packet Number）为x的报文，则下一个允许被接收的报文的PN必须大于或等于x-a。

·该功能仅在重播保护功能开启的情况下有效。

·请结合数据帧在传输网络中的转发途径，选择适当的重播保护窗口大小。若数据帧有可能被多次转发，那么乱序的可能性和乱序的范围会比较大，则建议适当调大重播保护窗口，反之调小。

·如果首先在接口上通过**mka apply policy**命令应用MKA策略，然后在该接口上配置了MACsec重播保护窗口大小，则接口上应用的MKA策略将被取消，取而代之保存的配置将是，接口上配置的MACsec重播保护窗口大小以及该MKA策略中的除MACsec重播保护窗口大小之外的其它所有配置。

【举例】

\# 配置接口GigabitEthernet1/0/1的MACsec重播保护窗口大小为100。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 macsec replay-protection window-size 100

【相关命令】

·**display macsec**

·**macsec replay-protection enable**

·**mka apply policy**

·**replay-protection window-size**

**MACsec \-- MACsec配置命令 \-- macsec validation mode**

------------------------------------------------------------------------

**[macsec validation mode**]命令用来配置接口上的MACsec校验模式。

 **undo macsec validation mode**命令用来恢复缺省情况。

【命令】

**[macsec validation mode **[{ **check** \| **disabled** \| **strict** }]]

**[undo****macsec validation mode**]

【缺省情况】

接口上的MACsec校验模式为**check**模式。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[check**]：检查模式，表示[只作校验，但不丢弃非法数据帧。]

disabled{.commandkeywords}：不对接收数据帧进行MACsec校验。

**[strict**]：严格校验模式，表示校验数据帧，并丢弃非法数据帧。

【使用指导】

·在网络中部署支持MACsec的设备时，为避免两端因密钥协商不一致而造成流量丢失，建议两端均先配置为**check**模式，在密钥协商成功后，再配置为**strict**模式。

·如果首先在接口上通过**mka apply policy**命令应用MKA策略，然后在该接口上配置MACsec校验模式，则接口上应用的MKA策略将被取消，取而代之保存的配置将是，接口上配置的MACsec校验模式及该MKA策略中的除MACsec校验模式之外的其它所有配置。

【举例】

\# 配置接口GigabitEthernet1/0/1 上的MACsec的校验模式为严格校验模式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 macsec validation mode strict

【相关命令】

·**display macsec**

·**mka apply policy**

·**validation mode**

**MACsec \-- MACsec配置命令 \-- mka apply policy**

------------------------------------------------------------------------

**[mka apply policy**]命令用来在接口上应用MKA策略。

**[undo mka apply policy**]命令用来取消接口上应用的MKA策略。

【命令】

**[mka apply policy** *policy-name*]

**[undo mka apply policy**]

【缺省情况】

接口上没有应用MKA策略。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：MKA策略名称，为1～16个任意字符的字符串，区分大小写。

【使用指导】

·接口上应用了MKA策略时，策略下配置的MACsec参数，包括加密偏移、校验模式、重播保护功能和重播保护窗口值会覆盖接口下配置的对应的MACsec参数，且当修改策略下的配置时，接口相应的配置也会改变。

·通过**undo ****mka apply policy**取消接口上应用的指定MKA策略时，接口上的加密偏移、MACsec校验模式、重播保护功能和重播保护窗口大小都恢复为缺省情况。

·当一个MKA策略被删除时，应用了该策略的接口上会自动应用缺省MKA策略default-policy。

·当接口应用了一个不存在的MKA策略时，该接口会自动应用缺省MKA策略default-policy。之后，如果该策略被创建后，则接口会自动应用配置的MKA策略。

【举例】

\# 在接口GigabitEthernet1/0/1上应用MKA策略abcd。

\<Syaname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mka apply policy abcd

【相关命令】

·**confidentiality-offset**

·**display mka policy**

·**replay-protection enable**

·**replay-protection window-size**

·**validation mode**

**MACsec \-- MACsec配置命令 \-- mka enable**

------------------------------------------------------------------------

**[mka enable**]命令用来使能接口上的MKA协议。

**[undo mka enable**]命令用来关闭接口上的MKA协议。

【命令】

**[mka enable**]

**[undo mka enable**]

【缺省情况】

接口上的MKA协议处于关闭状态。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·接口使能MKA协议后，将触发密钥协商过程，并在密钥协商成功之后建立MKA会话。

·MKA协议负责接口上MACsec安全通道的建立和管理，以及MACsec所使用密钥的协商。

【举例】

\# 在接口GigabitEthernet1/0/1上使能MKA协议。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mka enable

【相关命令】

·**display mka session**

**MACsec \-- MACsec配置命令 \-- mka policy**

------------------------------------------------------------------------

**[mka policy**]命令用来创建一个MKA策略，并进入MKA策略视图。如果该MKA策略已创建，则直接进入MKA策略视图。

**[undo mka policy**]命令用来删除指定的MKA策略。

【命令】

**[mka policy** *policy-name*]

**[undo mka policy** *policy-name*]

【缺省情况】

存在一个缺省的MKA策略，名称为default-policy。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[policy-name*]：MKA策略名，为1～16个任意字符的字符串，区分大小写。

【使用指导】

MKA（MACsec Key Agreement，MACsec密钥协商）策略用于管理在MKA策略视图下的相关配置，包括加密偏移量、接收数据帧校验模式、重播保护使能和重播保护窗口大小。

需要注意的是：

·系统中可配置多个MKA策略。

·缺省的MKA策略default-policy不能被删除和修改。

【举例】

\# 创建一个名称为abcd的MKA策略，并进入该MKA策略视图。

\<Syaname\> system-view

Sysname mka policy abcd

Sysname-mka-policy-abcd

【相关命令】

·**confidentiality-offset**

·**display mka****policy**

·**mka apply policy**

·**replay-protection enable**

·**replay-protection window-size**

·**validation mode**

**MACsec \-- MACsec配置命令 \-- mka priority**

------------------------------------------------------------------------

**[mka priority**]命令用来配置MKA密钥服务器的优先级。

**[undo mka priority**]命令用来恢复缺省情况。

【命令】

**[mka priority ***priority-value*]

**[undo mka priority**]

【缺省情况】

MKA密钥服务器的优先级为0。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[priority-value*]：MKA密钥服务器优先级，取值范围为0～255，值越小，优先级越高。

【使用指导】

MACsec使用的安全密钥通过MKA协议进行协商生成。密钥服务器负责生成和发布MKA会话所使用的安全密钥。

·如果采用802.1X认证生成的CAK，接入设备的接口自动被选举为密钥服务器。

·如果采用用户配置的预共享密钥，优先级较高（值较小）的接口被选举为密钥服务器。如果两端的优先级相同，则比较SCI（MAC地址+端口的ID），SCI值较小的一端将被选举为密钥服务器。

·优先级为255的设备端口不能被选举为密钥服务器。相互连接的端口不能都配置优先级为255，否则MKA会话选举不出密钥服务器。

【举例】

\# 在接口GigabitEthernet1/0/1上配置MKA密钥服务优先级为2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mka priority 2

【相关命令】

·**display mka session**

**MACsec \-- MACsec配置命令 \-- mka psk**

------------------------------------------------------------------------

**[mka psk**]命令用来配置MKA预共享CA密钥。

**[undo mka psk**]命令用来删除配置的MKA预共享CA密钥。

【命令】

**[mka psk ckn ***name*** cak simple ***value*]

**[undo mka psk**]

【缺省情况】

不存在MKA预共享密钥。

【视图】

以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ckn*** name*]：表示CA密钥的名称（CKN，CAK Name），*name*为2～64个字符的字符串，只能包含偶数个16进制数字，不区分大小写。

**[cak**]：表示CA密钥。

**[simple**]：表示以明文方式设置预共享密钥。

*[value*]：设置的明文密钥，为2～64个字符，且只能为偶数个16进制数，不区分大小写。

【使用指导】

CA密钥（CAK，Secure Connectivity Association Key）有两种来源：802.1X认证过程中生成的CAK；通过命令行手工配置。用户手工配置的CAK优先级高。

当接口上没有启用802.1X认证功能时，可以通过**mka psk**配置两端使用的CAK，但必须保证两端的CAK配置一致，否则不能建立正常的MKA会话。

需要注意的是：

·两端建立正常的MKA会话后，若要删除配置的CKN，则建议首先在密钥服务器端执行**undo mka psk**命令，然后在非密钥服务器端执行**mka psk**命令。

·删除配置的CKN会导致已建立的相应的MKA会话删除。

·当前系统支持的加密算法套件要求所使用的CKN、CAK的长度都必须为32个字符。在运行加密算法套件时，对于长度不足32个字符的CKN、CAK，系统会自动在其后补零，使其满足32个字符；对于长度大于32个字符的CKN、CAK，系统只获取其前32个字符。

【举例】

\# 在接口GigabitEthernet1/0/1上配置预共享CA密钥的名称为AB，预共享CA密钥为明文1234。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 mka psk ckn AB cak simple 1234

**MACsec \-- MACsec配置命令 \-- replay-protection enable**

------------------------------------------------------------------------

**[replay-protection enable**]命令用来开启MACsec重播保护功能。

**[undo replay-protection enable**]命令用来关闭MACsec重播保护功能。

【命令】

**[replay-protection enable**]

**[undo replay-protection enable**]

【缺省情况】

MACsec重播保护功能处于开启状态。

【视图】

MKA策略视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·MACsec重播保护功能可以单独开启，且仅针对接收到的数据帧。重播保护为了防止收到乱序或重复的数据帧。

·在MKA策略中开启的MACsec重播保护功能状态，在该MKA策略成功应用到接口上之后，将会覆盖该接口上已开启的MACsec重播保护功能状态。

【举例】

\# 在MKA策略abcd中开启MACsec重播保护功能。

\<Sysname\> system-view

Sysname mka policy abcd

Sysname-mka-policy-abcd replay-protection enable

【相关命令】

·**macsec replay-protection enable**

·**mka apply policy**

·**replay-protection window-size**

**MACsec \-- MACsec配置命令 \-- replay-protection window-size**

------------------------------------------------------------------------

**[replay-protection window-size**]命令用来配置MACsec重播保护窗口大小。

**[undo replay-protection window-size**]命令用来恢复缺省情况。

【命令】

**[replay-protection window-size ***size-value*]

**[undo replay-protection window-size**]

【缺省情况】

MACsec重播保护窗口大小为0个数据帧，表示不允许接收乱序或重复的数据帧。

【视图】

MKA策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[size-value*]：重播保护窗口大小，取值范围为0～4294967295，单位为数据帧。

【使用指导】

在某些组网下（如数据帧穿过运营商网络），数据帧因为发送优先级的不同，在转发过程中会被重新排序，最终到达接收端会出现乱序。如果要正常接收这些乱序的数据帧，需配置重播保护窗口。假设配置的重播保护窗口大小为a，如果接收到了一个报文序号（PN，Packet Number）为x的报文，则下一个允许被接收的报文的PN必须大于或等于x-a。

·该功能仅在重播保护功能开启的情况下有效。

·请结合数据帧在传输网络中的转发途径，选择适当的重播保护窗口大小。若数据帧有可能被多次转发，那么乱序的可能性和乱序的范围会比较大，则建议适当调大重播保护窗口，反之调小。

·在MKA策略中配置的MACsec重播保护窗口值，在该MKA策略成功应用到接口上之后，将会覆盖该接口上配置的MACsec重播保护窗口值。

【举例】

\# 在MKA策略abcd中配置重播保护窗口大小为100。

\<Sysname\> system-view

Sysname mka policy abcd

Sysname-mka-policy-abcd replay-protection window-size 100

【相关命令】

·**macsec replay-protection window-size**

·**macsec replay-protection enable**

·**mka apply policy**

**MACsec \-- MACsec配置命令 \-- reset mka session**

------------------------------------------------------------------------

**[reset mka session**]命令用来重建接口上的MKA会话。

【命令】

**[reset mka session ** **interface** *interface-type interface-number* ]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number*]：指定接口类型和接口编号。若不指定该参数，则表示重建所有接口上的MKA会话信息。

【使用指导】

重建接口上的MKA会话是指，先清除接口上的MKA会话，然后立即触发协商建立新的MKA会话。

【举例】

\# 重建接口GigabitEthernet1/0/1上的MKA会话。

\<Sysname\> reset mka session interface gigabitethernet 1/0/1

【相关命令】

·**display mka session**

**MACsec \-- MACsec配置命令 \-- reset mka statistics**

------------------------------------------------------------------------

**[reset mka statistics**]命令用来清除接口上的MKA统计信息。

【命令】

**[reset mka statistics ** **interface** *interface-type interface-number*]**

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface ***interface-type interface-number*]：指定接口类型和接口编号。若不指定该参数，则表示清除所有接口上的MKA统计信息。

【举例】

\# 清除接口GigabitEthernet1/0/1上的MKA统计信息。

\<Sysname\> reset mka statistics interface gigabitethernet 1/0/1

【相关命令】

·**display mka statistics**

**MACsec \-- MACsec配置命令 \-- validation mode**

------------------------------------------------------------------------

**[validation mode**]命令用来配置MACsec校验模式。

**[undo validation mode**]命令用来恢复缺省情况。

【命令】

**[validation mode**[ { **check** \| **disabled** \| **strict** }]]

**[undo validation mode**]

【缺省情况】

**[check**]模式，表示只作校验，但不丢弃非法数据帧。

【视图】

MKA策略视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[check**]：检查模式，表示[只作校验，但不丢弃非法数据帧。]

disabled{.commandkeywords}：不对接收数据帧进行MACsec校验。

**[strict**]：严格校验模式，表示校验数据帧，并丢弃非法数据帧。

【使用指导】

·在网络中部署支持MACsec的设备时，为避免两端因密钥协商不一致而造成流量丢失，建议两端均先配置为**check**模式，在密钥协商成功后，再配置为**strict**模式。

·在MKA策略中配置的MACsec校验模式，在该MKA策略成功应用到接口上之后，将会覆盖该接口上配置的MACsec校验模式。

【举例】

\# 在MKA策略abcd中配置MACsec校验模式为严格校验模式。

\<Sysname\> system-view

Sysname mka policy abcd

Sysname-mka-policy-abcd validation mode strict

【相关命令】

·**macsec validation mode**

·**mka apply policy**
