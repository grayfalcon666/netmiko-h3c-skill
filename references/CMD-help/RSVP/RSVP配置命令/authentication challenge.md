
**RSVP \-- RSVP配置命令 \-- authentication challenge**

------------------------------------------------------------------------

**[authentication challenge**]命令用来全局或为指定RSVP邻居开启RSVP认证的challenge-response握手功能。

**[undo authentication challenge**]命令用来全局或为指定RSVP邻居关闭RSVP认证的challenge-response握手功能。

【命令】

**[authentication challenge**]

**[undo authentication challenge**]

【缺省情况】

认证的challenge-response握手功能处于关闭状态。

【视图】

RSVP视图/RSVP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了避免报文的重放（Replay）攻击，RSVP接收认证消息时要求认证消息的序列号依次增加，RSVP在接收RSVP SA（Security Association，安全联盟）中保存最后一次收到的消息的序列号，用于判断后续消息是否符合要求。但是，在新创建接收RSVP SA的时候，无法获取发送端的序列号，因此缺省情况下，创建接收RSVP SA时将接收序列号填写为零，这样对端发送任意序列号的消息就都能接收。这就增加了重放攻击的风险。为了避免这种风险，可以执行**authentication challenge**命令，使得在新建接收RSVP SA时执行challenge-response握手过程，获取发送端的序列号。

RSVP认证的challenge-response握手功能可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

【举例】

\# 在RSVP视图下全局开启RSVP认证的challenge-response握手功能。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp authentication challenge

\# 在RSVP邻居视图下开启本地设备与RSVP邻居1.1.1.9之间RSVP认证的challenge-response握手功能。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp peer 1.1.1.9

Sysname-rsvp-peer-1.1.1.9 authentication challenge

【相关命令】

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset ****rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- authentication key**

------------------------------------------------------------------------

**[authentication key**]命令用来全局或为指定RSVP邻居开启RSVP认证功能，并配置认证密钥。

**[undo authentication key**]命令用来全局或为指定RSVP邻居关闭RSVP认证功能。

【命令】

**[authentication key **[{ **cipher** \| **plain** } *auth-key*]]

**[undo authentication key**]

【缺省情况】

RSVP认证功能处于关闭状态，即不进行RSVP认证。

【视图】

RSVP视图/RSVP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文形式设置密钥。

**[plain**]：表示以明文形式设置密钥。

*[auth-key*]：认证密钥，区分大小写。如果采用明文（**plain**）形式，则为1～16个字符的明文字符串；如果采用密文（**cipher**）形式，则为1～53个字符的密文字符串。

【使用指导】

RSVP认证功能可以用来确保RSVP消息不会被篡改，防止伪造的资源预留请求非法占用网络资源。

配置RSVP认证功能后，发送RSVP消息时会使用MD5算法对认证密钥和消息内容计算出消息摘要，并将消息摘要添加到发送的RSVP消息中。对端接收到RSVP消息后，也进行同样地计算，并将计算结果和消息中的摘要进行比较。如果一致，则认证通过，接收该消息；否则认证失败，丢弃该消息。

RSVP认证功能可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

如果在多个视图下配置了认证密钥，则认证密钥的使用优先级顺序从高到低依次为：RSVP邻居视图、接口视图、RSVP视图。例如，如果在RSVP邻居视图和RSVP视图都开启了与特定邻居的RSVP认证功能，并配置了不同的认证密钥，则采用RSVP邻居视图下配置的密钥认证本地设备和该邻居之间的RSVP消息。

如果已经采用某个视图下配置的认证密钥建立了RSVP SA，则只有先删除当前视图下配置的认证密钥或执行**reset rsvp authentication**命令删除该RSVP SA，才会按照上述优先级顺序重新查找新的认证密钥并建立RSVP SA。

需要注意的是：

·本地设备上开启RSVP认证功能后，在相应的RSVP邻居上也需要开启RSVP认证功能，并配置相同的认证密钥。

·以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

\# 在RSVP视图下全局开启RSVP认证功能，并指定认证密钥为明文abcdefgh。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp authentication key plain abcdefgh

\# 在RSVP邻居视图下开启本地设备与邻居1.1.1.9之间的认证功能，并指定认证密钥为明文abcdefgh。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp peer 1.1.1.9

Sysname-rsvp-peer-1.1.1.9 authentication key plain abcdefgh

【相关命令】

·**authentication challenge**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- authentication lifetime**

------------------------------------------------------------------------

**[authentication lifetime**]命令用来全局或为指定RSVP邻居配置RSVP SA的空闲老化时间。

**[undo authentication lifetime**]命令用来恢复缺省情况。

【命令】

**[authentication lifetime ***life-time*]

**[undo authentication lifetime**]

【缺省情况】

RSVP SA的空闲老化时间为1800秒（30分钟）。

【视图】

RSVP视图/RSVP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[life-time*]：RSVP SA的空闲老化时间，取值范围为30～86400，单位为秒。

【使用指导】

开启了RSVP认证功能后，设备收发RSVP消息时会动态建立RSVP SA，以记录消息的序列号、方便对RSVP消息进行认证处理。

为了在不需要RSVP SA的时候，能够及时删除该RSVP SA，回收内存资源，每个RSVP SA都有其老化时间。当RSVP SA的空闲时间到达老化时间时，将删除该RSVP SA。设备发送和接收RSVP认证消息时，会更新对应RSVP SA的空闲时间，避免其被老化删除。

RSVP SA的空闲老化时间可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

采用某个视图下配置的认证密钥建立RSVP SA后，该RSVP SA的空闲老化时间为该视图下配置的老化时间。

修改RSVP SA的空闲老化时间后，只会对新建立的RSVP SA生效。要想使得修改后的空闲老化时间对已建立的RSVP SA生效，则需要执行**reset rsvp authentication**命令来删除并重新建立RSVP SA。

【举例】

\# 在RSVP视图下全局配置RSVP SA的空闲老化时间为100秒。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp authentication lifetime 100

\# 在RSVP邻居视图下配置本地设备与RSVP邻居1.1.1.9之间RSVP SA的空闲老化时间为100秒。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp peer 1.1.1.9

Sysname-rsvp-peer-1.1.1.9 authentication lifetime 100

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- authentication window-size**

------------------------------------------------------------------------

**[authentication window-size**]命令用来全局或为指定RSVP邻居配置对于带有认证信息的RSVP消息，最大可允许的乱序消息数量。

**[undo authentication window-size**]命令用来恢复缺省情况。

【命令】

**[authentication window-size ***numbe*]

**[undo authentication window-size**]

【缺省情况】

对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为1。

【视图】

RSVP视图/RSVP邻居视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最大可允许的乱序消息数量，取值范围为1～64。

【使用指导】

为了防止报文重放攻击，RSVP在带有认证信息的RSVP消息中携带唯一的序列号。每发送一个消息，序列号依次增加。如果接收到的消息序列号在允许的范围内，则接受该消息；否则，丢弃该消息。

RSVP判断报文序列号是否在允许范围内的方法为：

(1)在设备上记录最后一次接收到的RSVP报文的序列号。

(2)设备接收到新的RSVP报文时，将该报文的序列号与记录的序列号进行比较：

·如果大于记录的序列号，则将记录的序列号更新为该报文的序列号。

·如果等于记录的序列号，则认为是重放攻击，丢弃该报文。

·如果小于记录的序列号、大于（记录的序列号---本命令配置的window-size），且未收到过该序列号的报文，则接收该报文；若已经收到过该序列号的报文，则认为是重放攻击，丢弃该报文。

·如果小于等于（记录的序列号---本命令配置的window-size），则认为报文序列号不合法，丢弃该报文。

缺省情况下，最大可允许的乱序消息数量为1，即如果新收到的RSVP消息的序列号小于最后收到的消息序列号，则认为该消息是重放攻击，丢弃该消息。但是，如果在短时间内发送了多个RSVP消息，那么这些消息到达邻居时可能会产生乱序。若采用缺省情况，则会导致这些乱序消息被丢弃。此时，可以通过本命令配置较大的window-size解决此问题。

采用某个视图下配置的认证密钥建立RSVP SA后，该RSVP SA的最大可允许乱序消息数量为该视图下配置的值。

修改最大可允许的乱序消息数量后，只会对新建立的RSVP SA生效。要想使得修改后的最大可允许乱序消息数量对已建立的RSVP SA生效，则需要执行**reset rsvp authentication**命令来删除并重新建立RSVP SA。

【举例】

\# 在RSVP视图下全局配置对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为10。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp authentication window-size 10

\# 在RSVP邻居视图下配置本地设备和RSVP邻居1.1.1.9之间对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为10。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp peer 1.1.1.9

Sysname-rsvp-peer-1.1.1.9 authentication window-size 10

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- display rsvp**

------------------------------------------------------------------------

**[display rsvp**]命令用来显示RSVP的信息。

【命令】

**[display rsvp ** **interface**  *interface-type interface-number*  ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**]：显示接口的RSVP信息。

*[interface-type interface-number*]：显示指定接口的RSVP信息。*interface-type interface-number*为接口类型及接口编号。

【使用指导】

执行**display** **rsvp**命令时：

·如果不指定**interface**参数，则显示全局的RSVP信息。

·如果只指定**interface**参数，不指定*interface-type interface-number*参数，则显示所有接口的RSVP信息。

·如果指定**interface** interface-type interface-number参数，则显示指定接口的RSVP信息。

【举例】

\# 显示全局的RSVP信息。

\<Sysname\> display rsvp

LSR ID: 50.0.0.1                       Fast Reroute time: 300 sec

Refresh interval: 30 sec               Keep multiplier: 3

Hello interval: 3 sec                  Hello lost: 4

Graceful Restart: Disabled             DSCP value: 48

Authentication: Enabled

  Lifetime: 300 sec

  Window size: 64

  Challenge: Enabled

Statistics:

  PSB number: 5                        RSB number: 5

  LSP number: 5                        Request number: 5

  Peer number: 5                       SA number: 5

表1-1 display rsvp命令显示信息描述表

字段

描述

LSR ID

标签交换路由器ID

Fast Reroute time

为决定一条LSP是否应使用新的、更好的备份隧道而进行扫描的时间间隔，单位为秒

Refresh interval

路径和预留消息的刷新时间间隔，单位为秒

Keep multiplier

PSB和RSB的超时倍数

Hello interval

Hello Request消息的发送时间间隔，单位为秒

Hello lost

最多可以接受的Hello消息连续丢失次数

Graceful Restart

是否开启Graceful Restart能力，取值包括Enabled和Disabled

DSCP value

发送的RSVP报文的DSCP优先级

Authentication

是否开启RSVP认证功能，取值包括Enabled和Disabled

Lifetime

RSVP SA的空闲老化时间，单位为秒

Window size

最大可允许的乱序消息数量

Challenge

是否开启认证的challenge-response握手功能，取值包括Enabled和Disabled

Statistics

RSVP统计信息

PSB number

PSB总数

RSB number

RSB总数

LSP number

RSVP协议建立的LSP总数

Request number

RSVP请求信息数据块总数

Peer number

RSVP协议动态生成的邻居的总数

SA number

RSVP SA的总数

\# 显示所有接口的RSVP信息。

\<Sysname\> display rsvp interface

Interface: GE1/0/1                      Logical interface handle: 0x3

State: Up                              IP address: 50.1.0.1

MPLS TE: Enabled                       RSVP: Enabled

Hello: Enabled                         BFD: Enabled

Summary refresh: Enabled               Reliability: Disabled

Retransmit interval: 500 ms            Retransmit increment: 1

Authentication: Enabled

  Lifetime: 300 sec

  Window size: 64

  Challenge: Enabled

Bypass tunnels: Tunnel0

Interface: GE1/0/2                      Logical interface handle: 0x67

State: Up                              IP address: 50.2.0.1

MPLS TE: Enabled                       RSVP: Enabled

Hello: Enabled                         BFD: Enabled

Summary refresh: Disabled              Reliability: Disabled

Retransmit interval: 500 ms            Retransmit increment: 1

Authentication: Enabled

  Lifetime: 300 sec

  Window size: 64

  Challenge: Enabled

Bypass tunnels: Tunnel0, Tunnel1, Tunnel2

表1-2 display rsvp interface命令显示信息描述表

字段

描述

Interface

接口的名称

Logical interface handle

接口的逻辑接口索引

State

RSVP所记录的接口状态，取值包括Up和Down

IP address

RSVP当前所用的接口的IP地址

MPLS TE

接口上是否开启MPLS TE能力，取值包括Enabled和Disabled

RSVP

接口上是否开启RSVP能力，取值包括Enabled和Disabled

Hello

接口上是否开启Hello扩展功能，取值包括Enabled和Disabled

BFD

接口上是否开启BFD检测功能，取值包括Enabled和Disabled

Summary refresh

接口上是否开启摘要刷新功能，取值包括Enabled和Disabled

Reliability

接口上是否开启RSVP消息的可靠传递功能，取值包括Enabled和Disabled

Retransmit interval

初始的重传时间间隔，单位为毫秒

Retransmit increment

重传时间增量

Authentication

接口上是否开启RSVP认证功能，取值包括Enabled和Disabled

Lifetime

RSVP SA的空闲老化时间，单位为秒

Window size

最大可允许的乱序消息数量

Challenge

接口是否开启认证的challenge-response握手功能，取值包括Enabled和Disabled

Bypass tunnels

接口下配置的用于快速重路由的旁路隧道。如果没有配置任何旁路隧道，则显示为None

**RSVP \-- RSVP配置命令 \-- display rsvp authentication**

------------------------------------------------------------------------

**[display rsvp authentication**]命令用来显示本地设备与RSVP邻居建立的RSVP SA信息。

【命令】

**[display rsvp authentication** [ **from** *ip-address*   **to** *ip-address*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[from*** ip-address*]：显示认证发起节点IP地址为指定地址的RSVP SA信息。*ip-address*为认证发起节点的IP地址。

**[to ***ip-address*]：显示认证目的节点IP地址为指定地址的RSVP SA信息。*ip-address*为认证目的节点的IP地址。

**[verbose**]：显示RSVP SA的详细信息。如果没有指定本参数，则显示RSVP SA的简要信息。

【使用指导】

开启了RSVP认证功能后，设备收发RSVP消息时会动态建立RSVP SA。RSVP SA中包含如下信息：认证发起节点的IP地址、认证目的节点的IP地址、认证方向、认证类型、认证密钥、认证空闲老化的剩余时间等。其中，认证发起节点和认证目的节点的IP地址从IP报文头或RSVP消息对象中获取，具体获取方法如[表]1-3(?2087967775#_Ref330996818)所示。

表1-3 认证发起节点和目的节点IP地址的获取方法

接收或发送的消息类型

认证发起节点的IP地址

认证目的节点的IP地址

Path

RSVP消息HOP对象中的地址

RSVP消息SESSION对象中的目的地址

PathTear

RSVP消息HOP对象中的地址

RSVP消息SESSION对象中的目的地址

PathError

IP报文头中的源IP地址

IP报文头中的目的IP地址

Resv

RSVP消息HOP对象中的地址

IP报文头中的目的IP地址

ResvTear

RSVP消息HOP对象中的地址

IP报文头中的目的IP地址

ResvError

RSVP消息HOP对象中的地址

IP报文头中的目的IP地址

ResvConfirm

IP报文头中的源IP地址

RSVP消息CONFIRM对象中的地址

ACK

IP报文头中的源IP地址

IP报文头中的目的IP地址

Srefresh

IP报文头中的源IP地址

IP报文头中的目的IP地址

Hello

IP报文头中的源IP地址

IP报文头中的目的IP地址

需要注意的是，执行**display rsvp authentication**命令时，如果没有指定**from*** ip-address*和**to ***ip-address*参数，则显示本地设备与所有邻居建立的RSVP SA的信息。

【举例】

\# 显示本地设备与所有邻居建立的RSVP SA的简要信息。

\<Sysname\> display rsvp authentication

From            To              Mode    Type      Key-ID       Expiration

57.10.10.1      57.10.10.2      Receive Interface 000103000000 280s

57.10.10.2      57.10.10.1      Send    Interface 000103000000 280s

表1-4 display rsvp authentication命令显示信息描述表

字段

描述

From

认证发起节点的IP地址

To

认证目的节点的IP地址

Mode

认证方向，取值包括：

·Receive：接收RSVP SA，用来对RSVP邻居发送给本地的消息进行认证处理

·Send：发送RSVP SA，用来对本地发送给RSVP邻居的消息进行认证处理

Type

认证类型，取值包括：

·Peer：表示根据RSVP邻居视图下的配置建立的RSVP SA

·Interface：表示根据接口视图下的配置建立的RSVP SA

·Global：表示根据RSVP视图下的配置建立的RSVP SA

Key-ID

RSVP SA的密钥ID

·若为发送RSVP SA，则显示本地的密钥ID

·若为接收RSVP SA，则显示对端发来的密钥ID

Expiration

RSVP SA空闲老化的剩余时间，单位为秒

\# 显示所有RSVP SA的详细信息。

\<Sysname\> display rsvp authentication verbose

From: 20.1.1.1                            To: 4.4.4.9

Mode: Send                                Type: Interface

Challenge: Supported                      Peer: 20.1.1.2

Local key ID: 0x000104000000              Peer key ID: 0x0

Lifetime: 1800 sec                        Expiration time: 1781 sec

Window size: 1

Last sent sequence number:

  5781735195480686593

From: 20.1.1.2                            To: 20.1.1.1

Mode: Receive                             Type: Interface

Challenge: Not configured                 Peer: 20.1.1.2

Local key ID: 0x0                         Peer key ID: 0x000104000000

Lifetime: 1800 sec                        Expiration time: 1798 sec

Window size: 1

Received sequence numbers:

  5781742445385482241

表1-5 display rsvp authentication verbose命令显示信息描述表

字段

描述

From

认证发起节点的IP地址

To

认证目的节点的IP地址

Mode

认证方向，取值包括：

·Receive：接收RSVP SA，用来对RSVP邻居发送给本地的消息进行认证处理

·Send：发送RSVP SA， 用来对本地发送给RSVP邻居的消息进行认证处理

Type

认证类型，取值包括：

·Peer：表示根据RSVP邻居视图下的配置建立的RSVP SA

·Interface：表示根据接口视图下的配置建立的RSVP SA

·Global：表示根据RSVP视图下的配置建立的RSVP SA

Challenge

认证的challenge-response握手状态，取值包括：

·Not configured：用于接收RSVP SA，表示本地没有开启challenge-response握手功能

·Configured：用于接收RSVP SA，表示本地开启了challenge-response握手功能

·In progress：本地开启challenge-response握手功能，向对端发送Integrity Challenge消息后，正在等待对端回应的Integrity Response消息

·Completed：本地开启challenge-response握手功能，向对端发送Integrity Challenge消息后，收到对端回应的Integrity Response消息，并通过认证检查

·Failed：本地开启challenge-response握手功能，向对端发送Integrity Challenge消息后，收到对端回应的Integrity Response消息，但未通过认证检查；或本地重复向对端发送三次Integrity Challenge消息后，仍然没有收到对端回应的合法Integrity Response消息；或对端未开启challenge-response握手功能

·Supported：用于发送RSVP SA，表示本端支持challenge-response握手功能

Peer

认证邻居的IP地址，表示是和哪个邻居建立的RSVP SA

Local key ID

本地的Key-ID，用于发送RSVP SA

Peer key ID

对端的Key-ID，用于接收RSVP SA

Lifetime

RSVP SA的空闲老化时间，单位为秒

Expiration time

RSVP SA空闲老化的剩余时间，单位为秒

Window size

最大可允许的乱序消息数量

Received sequence numbers

收到的消息的序列号，最多可显示Window-size数量的序列号

Last sent sequence number

最后发送的消息的序列号

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- display rsvp lsp**

------------------------------------------------------------------------

**[display rsvp lsp**]命令用来显示RSVP建立的CR-LSP信息。

【命令】

**[display rsvp lsp** [ **destination** *ip-address*   **source** *ip-address*   **tunnel-id** *tunnel-id*   **lsp-id** *lsp-id*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[destination** *ip-address*]：显示隧道目的地为指定值的CR-LSP的信息。*ip-address*为隧道的目的地址。

**[source** *ip-address*]：显示隧道源地址为指定值的CR-LSP的信息。*ip-address*为隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：显示隧道ID为指定值的CR-LSP的信息。*tunnel-id*为隧道ID，取值范围为0～65535。

**[lsp-id** *lsp-id*]：显示LSP ID为指定值的CR-LSP的信息。*lsp-id*为CR-LSP的ID，取值范围为0～65535。

**[verbose**]**：**显示CR-LSP的详细信息。如果没有指定本参数，则显示CR-LSP的简要信息。

【举例】

\# 显示RSVP建立的所有CR-LSP的简要信息。

\<Sysname\> display rsvp lsp

Destination     Source          Tunnel-ID LSP-ID Direction  Tunnel-name

50.0.0.1        50.0.0.3        0         1      Uni        Sysname_t0

50.0.0.1        50.0.0.3        1         2      Bi-Down    Sysname_t1

表1-6 display rsvp lsp 命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel-ID

隧道ID

LSP-ID

LSP ID

Direction

隧道方向，取值包括：

·Uni：Unidirectional CR-LSP，表示单向隧道

·Bi-Down：Bidirectional downstream CR-LSP，表示双向隧道的正向LSP

·Bi-Up：Bidirectional upstream CR-LSP，表示双向隧道的反向LSP

Tunnel-name

隧道名称，取值为*Sysname*\_t*tunnel-ID*。其中，*Sysname*为设备的名称，可以通过系统视图下的**sysname**命令配置；*tunnel-ID*为隧道ID

本字段最长为80个字符，如果隧道名称超过80个字符，则超过77个字符的部分以"\..."代替

\# 显示RSVP建立的所有CR-LSP的详细信息。

\<Sysname\> display rsvp lsp verbose

Tunnel name: Sysname_t1

Destination: 3.3.3.9                      Source: 1.1.1.9

Tunnel ID: 1                              LSP ID: 5

LSR type: Transit                         Direction: Unidirectional

Setup priority: 7                         Holding priority: 7

In-Label: 1146                            Out-Label: 3

In-Interface: GE1/0/2                    Out-Interface: GE1/0/4

Nexthop: 57.20.20.1                       Exclude-any: 0

Include-Any: 0                            Include-all: 0

Mean rate (CIR): 0.00 kbps                Mean burst size (CBS): 1000.00 bytes

Path MTU: 1500                            Class type: CT0

RRO number: 8

  57.10.10.1/32      Flag: 0x00 (No FRR)

  57.10.10.2/32      Flag: 0x40 (No FRR/In-Int)

  1146               Flag: 0x01 (Global label)

  2.2.2.9/32         Flag: 0x20 (No FRR/Node-ID)

  57.20.20.2/32      Flag: 0x00 (No FRR)

  57.20.20.1/32      Flag: 0x40 (No FRR/In-Int)

  3                  Flag: 0x01 (Global label)

  3.3.3.9/32         Flag: 0x20 (No FRR/Node-ID)

Fast Reroute protection: Ready

  FRR inner label: 3           Bypass tunnel: Tunnel253

Tunnel name: Sysname_t253

Destination: 3.3.3.9                      Source: 2.2.2.9

Tunnel ID: 253                            LSP ID: 17767

LSR type: Ingress                         Direction: Bidirectional, Downstream

Setup priority: 7                         Holding priority: 7

In-Label: -                               Out-Label: 1025

In-Interface: -                           Out-Interface: GE1/0/6

Nexthop: 10.11.112.135                    Exclude-any: 0

Include-Any: 0                            Include-all: 0

Mean rate (CIR): 125.00 kbps              Mean burst size (CBS): 0.00 bytes

Path MTU: 0                               Class type: CT0

RRO number: 8

  10.11.112.140/32   Flag: 0x00 (No FRR)

  10.11.112.135/32   Flag: 0x40 (No FRR/In-Int)

  1025               Flag: 0x01 (Global label)

  5.5.5.9/32         Flag: 0x20 (No FRR/Node-ID)

  57.40.40.3/32      Flag: 0x00 (No FRR)

  57.40.40.1/32      Flag: 0x40 (No FRR/In-Int)

  3                  Flag: 0x01 (Global label)

  3.3.3.9/32         Flag: 0x20 ((No FRR/Node-ID)

Fast Reroute protection: None

表1-7 display rsvp lsp verbose命令显示信息描述表

字段

描述

Tunnel name

隧道名称，取值为*Sysname*\_t*tunnel-ID*。其中，*Sysname*为设备的名称，可以通过系统视图下的**sysname**命令配置；*tunnel-ID*为隧道ID

Destination

隧道目的地址

Source

隧道的源地址

Tunnel ID

隧道ID

LSP ID

LSP ID

LSR type

标签交换路由器类型，取值包括Ingress、Transit和Egress

Direction

隧道方向，取值包括：

·Unidirectional：表示单向隧道

·Bidirectional, Downstream：表示双向隧道的正向LSP

·Bidirectional, Upstream：表示双向隧道的反向LSP

Setup priority

隧道的建立优先级

Holding priority

隧道的保持优先级

In-Label

隧道的入标签

Out-Label

隧道的出标签

In-Interface

隧道的入接口

Out-Interface

隧道的出接口

Nexthop

隧道的下一跳地址

Exclude-any

不接受的亲和属性，即如果链路属性与任意的Exclude-any亲和属性相同，则不能使用该链路

Include-any

接受的亲和属性，即如果链路属性与任意的Include-any亲和属性相同，则可以使用该链路

Include-all

接受的所有亲和属性，即只有链路属性与所有的Include-all亲和属性相同时，才能使用该链路

Mean rate (CIR)

平均速率，单位为kbit/s

Mean burst size (CBS)

平均峰值速率，单位为byte/s

Path MTU

路径的最大传输单元

Class type

LSP流量所属的服务类型

RRO number

RRO（Record Route Object，记录路由对象）的个数

如果RRO的个数不为零，则接下来显示RRO对象中所记录的IP地址或标签信息

只有Tunnel接口上配置了路由记录功能后，才会显示RRO信息

Flag

RRO对象中标记的值及其含义，标记含义的取值包括：

·No FRR：表示没有配置FRR保护

·FRR Avail：表示FRR保护可用

·In use：表示已经发生FRR切换

·BW：表示带宽保护

·Node-Prot：表示节点保护

·Node-ID：表示RRO对象中的地址为节点的LSR ID

·In-Int：表示RRO对象中的地址为入接口的地址

·Global label：表示全局标签空间

Fast Reroute protection

是否绑定了快速重路由的旁路隧道，取值包括：

·None：没有绑定快速重路由的旁路隧道

·Ready：绑定了快速重路由的旁路隧道，此时未进行切换

·Active：绑定了快速重路由的旁路隧道，此时已进行切换

FRR i{.MsoCommentReference}nner label

快速重路由旁路隧道的入口标签，只有绑定了旁路隧道才会显示此字段

Bypass tunnel

旁路隧道的名称，只有绑定了旁路隧道才会显示此字段

【相关命令】

·**display rsvp request**

·**display rsvp reservation**

·**display rsvp sender**

**RSVP \-- RSVP配置命令 \-- display rsvp peer**

------------------------------------------------------------------------

**[display rsvp peer**]命令用来显示RSVP邻居的信息。

【命令】

**[display rsvp peer** [ **interface** *interface-type interface-number*   **ip** *ip-address*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示通过指定接口连接的邻居的信息。*interface-type interface-number*为接口类型和接口编号。

**[ip*** ip-address*]：显示指定RSVP邻居的信息。*ip-address*为邻居的IP地址。

**[verbose**]：显示RSVP邻居的详细信息。如果不指定本参数，则显示RSVP的简要信息。

【举例】

\# 显示所有RSVP邻居的简要信息。

\<Sysname\> display rsvp peer

Peer             Interface                State    Type     Summary refresh

57.10.10.1       GE1/0/1                  Idle     Active   Enabled

57.20.20.1       GE1/0/2                  Init     Passive  Disabled

表1-8 display rsvp peer命令显示信息描述表

字段

描述

Peer

邻居地址

Interface

邻居所对应的接口名称

State

本地的Hello状态，取值包括：

·Idle：本地未开启Hello扩展功能

·Init：本地开启Hello扩展功能，与邻居进行Hello消息交互未成功或正在进行消息交互

·Up：本地开启Hello扩展功能，与邻居进行Hello消息交互成功

Type

本端设备在邻居关系中的角色，取值包括：

·Active：表示本端是主动方，主动向邻居发送Hello Request消息

·Passive：表示本端是被动方，被动接收邻居发来的Hello Request消息并回应Hello Ack消息

Summary refresh

邻居是否开启摘要刷新功能，取值包括Enabled和Disabled

\# 显示所有RSVP邻居的详细信息。

\<Sysname\> display rsvp peer verbose

Peer: 57.10.10.1                          Interface: GE1/0/2

Hello state: Idle                         Hello type: Active

PSB count: 1                              RSB count: 0

Src instance: 0x32e                       Dst instance: 0x0

Summary refresh: Enabled                  Graceful Restart state: Invalid

Peer GR restart time: 0 ms                Peer GR recovery time: 0 ms

Peer: 57.20.20.1                          Interface: GE1/0/4

Hello state: Init                         Hello type: Active

PSB count: 0                              RSB count: 1

Src instance: 0x32e                       Dst instance: 0x0

Summary refresh: Disabled                 Graceful Restart state: Ready

Peer GR restart time: 0 ms                Peer GR recovery time: 0 ms

表1-9 display rsvp peer verbose命令显示信息描述表

字段

描述

Peer

邻居地址

Interface

邻居所对应的接口名称

Hello state

本地的Hello状态，取值包括：

·Idle：本地未开启Hello扩展功能

·Init：本地开启Hello扩展功能，与邻居进行Hello消息交互未成功或正在进行消息交互

·Up：本地开启Hello扩展功能，与邻居进行Hello消息交互成功

Hello type

本端设备在邻居关系中的角色，取值包括：

·Active：表示本端是主动方，主动向邻居发送Hello Request消息

·Passive：表示本端是被动方，被动接收邻居发来的Hello Request消息并回应Hello Ack消息

PSB count

邻居对应的路径状态块的数量

RSB count

邻居对应的预留状态块的数量

Src instance

发送给邻居的Hello消息中携带的Src instance，即本地设备的instance

Dst instance

最后一次接收到邻居发来的Hello消息中的Src Instance，即邻居的instance

Summary refresh

邻居是否开启摘要刷新功能，取值包括Enabled和Disabled

Graceful Restart state

邻居的GR状态，取值包括：

·Invalid：邻居没有GR能力，或本地没有开启GR能力

·Ready：邻居具有GR能力

·Restarting：邻居正在重启

·Recovering：邻居正在恢复

Peer GR restart time

邻居的GR重启时间间隔，单位为毫秒

Peer GR recovery time

邻居的GR恢复时间间隔，单位为毫秒

**RSVP \-- RSVP配置命令 \-- display rsvp request**

------------------------------------------------------------------------

**[display rsvp request**]命令用来显示向上游设备发送的RSVP资源预留请求的信息。

【命令】

**[display rsvp request ** **destination** *ip-address* ]  **source** *ip-address*   **tunnel-id** *tunnel-id*   **prevhop** *ip-address*   **verbose**

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[destination** *ip-address*]：显示隧道目的地址为指定值的RSVP资源预留请求信息。*ip-address*为隧道的目的地。

**[source** *ip-address*]：显示隧道源地址为指定值的RSVP资源预留请求信息。*ip-address*为隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：显示隧道ID为指定值的RSVP资源预留请求信息。*tunnel-id*为隧道ID，取值范围为0～65535。

**[prevhop** *ip-address*]：显示向指定上游设备发送的RSVP资源预留请求信息。*ip-address*为RSVP资源预留请求信息的目的设备的地址，即隧道的前一跳地址。

**[verbose**]：显示向上游设备发送的RSVP资源预留请求的详细信息。如果不指定本参数，则显示向上游设备发送的RSVP资源预留请求的简要信息。

【举例】

\# 显示所有向上游设备发送的RSVP资源预留请求的简要信息。

\<Sysname\> display rsvp request

Destination     Source          Tunnel-ID Previous-hop      Style

3.3.3.9         1.1.1.9         1         57.10.10.1        SE

表1-10 display rsvp request命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel-ID

隧道ID

Previous-hop

前一跳地址

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

\# 显示所有向上游设备发送的RSVP资源预留请求的详细信息。

\<Sysname\> display rsvp request verbose

Destination: 3.3.3.9                      Source: 1.1.1.9

Tunnel ID: 1                              Style: SE

Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008

Sent message epoch: 0                     Sent message ID: 0

Out-Interface: GE1/0/2                    Refresh interval: 30000 ms

Unknown object number: 0

Flow descriptor 1:

  Flow specification:

    Mean rate (CIR): 50.00 kbps           Mean burst size (CBS): 1000.00 bytes

    Path MTU: 1500                        QoS service: Controlled-Load

  Filter specification 1:

    Sender address: 1.1.1.9               LSP ID: 23

    Label: 1110

表1-11 display rsvp request verbose命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel ID

隧道ID

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

Previous hop

前一跳地址

Previous hop LIH

前一跳设备的逻辑接口索引

Sent message epoch

发送消息携带的Message ID Object中Epoch字段的值

Sent message ID

发送消息中的Message ID

Out-Interface

消息的出接口名称

Refresh interval

路径和预留消息的刷新时间间隔，单位为毫秒

Unknown object number

无法识别的Object的个数

Flow descriptor

流量信息描述

Flow specification

流量规格信息

Mean rate (CIR)

平均速率，单位为kbit/s

Mean burst size (CBS)

平均峰值速率，单位为byte/s

Path MTU

路径的最大传输单元

QoS service

QoS业务类型，取值包括Controlled-Load和Guaranteed

Filter specification

过滤规格信息

Sender address

发送者地址，用来标识隧道的源端

LSP ID

LSP ID

Label

正向LSP的入标签

【相关命令】

·**display rsvp lsp**

·**display rsvp reservation**

·**display rsvp sender**

**RSVP \-- RSVP配置命令 \-- display rsvp reservation**

------------------------------------------------------------------------

**[display rsvp reservation**]命令用来显示RSVP资源预留状态信息。

【命令】

**[display rsvp reservation** [ **destination** *ip-address*   **source** *ip-address*   **tunnel-id** *tunnel-id*   **nexthop** *ip-address*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[destination** *ip-address*]：显示隧道目的地址为指定值的RSVP资源预留状态信息。*ip-address*为隧道的目的地。

**[source** *ip-address*]：显示隧道源地址为指定值的RSVP资源预留状态信息。*ip-address*为隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：显示隧道ID为指定值的RSVP资源预留状态信息。*tunnel-id*为隧道ID，取值范围为0～65535。

**[nexthop** *ip-address*]：显示根据从指定下游设备接收到的Resv消息创建的RSVP资源预留状态信息。*ip-address*为发送资源预留状态信息设备的地址，即隧道下一跳地址。

**[verbose**]：显示RSVP资源预留状态的详细信息。如果不指定本参数，则显示RSVP资源预留状态的简要信息。

【举例】

\# 显示所有RSVP资源预留状态的简要信息。

\<Sysname\> display rsvp reservation

Destination     Source          Tunnel-ID Nexthop           Style

3.3.3.9         1.1.1.9         1         57.20.20.1        SE

表1-12 display rsvp reservation命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel-ID

隧道ID

Nexthop

下一跳地址

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

\# 显示所有RSVP资源预留状态的详细信息。

\<Sysname\> display rsvp reservation verbose

Destination: 3.3.3.9                      Source: 1.1.1.9

Tunnel ID: 1                              Style: SE

Nexthop: 57.20.20.1                       Nexthop LIH: 0x35

Received message epoch: 0                 Received message ID: 0

In-Interface: GE1/0/4                     Unknown object number: 0

Flow descriptor 1:

  Flow specification:

    Mean rate (CIR): 50.00 kbps           Mean burst size (CBS): 1000.00 bytes

    Path MTU: 1500                        QoS service: Controlled-Load

  Filter specification 1:

    Sender address: 1.1.1.9               LSP ID: 23

    Label: 3

    RRO number: 3

      57.20.20.1/32      Flag: 0x40 (No FRR/In-Int)

      3                  Flag: 0x01 (Global label)

      3.3.3.9/32         Flag: 0x20 (No FRR/Node-ID)

表1-13 display rsvp reservation verbose命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel ID

隧道ID

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

Nexthop

下一跳地址

Nexthop LIH

与下一跳对应的本地出接口的逻辑接口索引

Received message epoch

接收消息携带的Message ID Object中Epoch字段的值

Received message ID

接收消息中的Message ID

In-Interface

消息的入接口名称

Unknown object number

无法识别的Object的个数

Flow descriptor

流量信息描述

Flow specification

流量规格信息

Mean rate (CIR)

平均速率，单位为kbit/s

Mean burst size (CBS)

平均峰值速率，单位为byte/s

Path MTU

路径的最大传输单元

QoS service

QoS业务类型，取值包括Controlled-Load和Guaranteed

Filter specification

过滤规格信息

Sender address

发送者地址，用来标识隧道的源端

LSP ID

LSP ID

Label

正向LSP的出标签

RRO number

RRO（Record Route Object，记录路由对象）的个数

如果RRO的个数不为零，则接下来显示RRO对象中所记录的IP地址或标签信息

只有Tunnel接口上配置了路由记录功能后，才会显示RRO信息

Flag

RRO对象中标记的值及其含义，标记含义的取值包括：

·No FRR：表示没有配置FRR保护

·FRR Avail：表示FRR保护可用

·In use：表示已经发生FRR切换

·BW：表示带宽保护

·Node-Prot：表示节点保护

·Node-ID：表示RRO对象中的地址为节点的LSR ID

·In-Int：表示RRO对象中的地址为入接口的地址

·Global label：表示全局标签空间

【相关命令】

·**display rsvp lsp**

·**display rsvp request**

·**display rsvp sender**

**RSVP \-- RSVP配置命令 \-- display rsvp sender**

------------------------------------------------------------------------

**[display rsvp sender**]命令用来显示RSVP路径状态信息。

【命令】

**[display rsvp sender** [ **destination** *ip-address*   **source** *ip-address*   **tunnel-id** *tunnel-id*   **lsp-id** *lsp-id*   **verbose** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[destination** *ip-address*]：显示隧道目的地址为指定值的RSVP路径状态信息。*ip-address*为隧道的目的地。

**[source** *ip-address*]：显示隧道源地址为指定值的RSVP路径状态信息。*ip-address*为隧道的源地址，即RSVP消息中Session对象的扩展tunnel ID。

**[tunnel-id** *tunnel-id*]：显示隧道ID为指定值的RSVP路径状态信息。*tunnel-id*为隧道ID，取值范围为0～65535。

**[lsp-id** *lsp-id*]：显示LSP ID为指定值的RSVP路径状态信息。*lsp-id*为CR-LSP的ID，取值范围为0～65535。

**[verbose**]：显示RSVP路径状态的详细信息。如果不指定本参数，则显示RSVP路径状态的简要信息。

【举例】

\# 显示所有RSVP 路径状态的简要信息。

\<Sysname\> display rsvp sender

Destination     Source          Tunnel-ID LSP-ID  Style     Bitrate

3.3.3.9         1.1.1.9         1         5       SE        0.00

3.3.3.9         2.2.2.9         253       17767   SE        125.00

表1-14 display rsvp sender命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道的源地址

Tunnel-ID

隧道ID

LSP-ID

LSP ID

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

Bitrate

隧道带宽，单位为kbit/s

\# 显示所有RSVP路径状态的详细信息。

\<Sysname\> display rsvp sender verbose

Destination: 3.3.3.9                      Source: 1.1.1.9

Tunnel ID: 1                              Style: SE

Sender address: 1.1.1.9                   LSP ID: 5

Setup priority: 7                         Holding priority: 7

FRR desired: Yes                          BW protection desired: Yes

Received upstream label: 1051             Sent upstream label: 1051

Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008

Mean rate (CIR): 0.00 kbps                Mean burst size (CBS): 1000.00 bytes

MTU: 1500                                 Qos service: Controlled-Load

Received message epoch: 0                 Received message ID: 0

Sent message epoch: 0                     Sent message ID: 0

In-Interface: GE1/0/2                    Local LIH: 0x35

Local address: 57.20.20.2                 Refresh interval: 30000 ms

Out-Interface: GE1/0/4                    Nexthop: 57.20.20.1

Unknown object number: 0

Received ERO number: 2

  57.10.10.2/32      Strict

  57.20.20.1/32      Loose

Sent ERO number: 1

  57.20.20.1/32      Loose

XRO number: 2

  67.10.10.1/32

  67.20.20.1/32

RRO number: 1

  57.10.10.1/32      Flag: 0x00 (No FRR)

Fast Reroute PLR: Active

  FRR inner label: 3                      Bypass tunnel: Tunnel253

  Sender Template:

    Sender address: 10.11.112.140         LSP ID: 5

  FRR ERO number: 1

    3.3.3.9/32         Strict

Fast Reroute MP: None

Destination: 3.3.3.9                      Source: 2.2.2.9

Tunnel ID: 253                            Style: SE

Sender address: 2.2.2.9                   LSP ID: 17767

Setup priority: 7                         Holding priority: 7

FRR desired: Yes                          BW protection desired: Yes

Received upstream label: 1115             Sent upstream label: 1115

Previous hop: 57.10.10.1                  Previous hop LIH: 0xf0008

Mean rate (CIR): 125.00 kbps              Mean burst size (CBS): 0.00 bytes

MTU: 1500                                 Qos service: Controlled-Load

Received message epoch: 0                 Received message ID: 0

Sent message epoch: 0                     Sent message ID: 0

In-Interface: GE1/0/2                    Local LIH: 0x67

Local address: 10.11.112.140              Refresh interval: 30000 ms

Out-Interface: GE1/0/6                   Nexthop: 10.11.112.135

Unknown object number: 0

Received ERO number: 5

  2.2.2.9/32         Strict

  10.11.112.140/32   Strict

  10.11.112.135/32   Strict

  57.40.40.3/32      Strict

  57.40.40.1/32      Strict

Sent ERO number: 3

  10.11.112.135/32   Strict

  57.40.40.3/32      Strict

  57.40.40.1/32      Strict

XRO number: 1

  67.40.40.1/32

RRO number: 0

Fast Reroute PLR: None

Fast Reroute MP: Active

  In-Interface: GE1/0/2

  Sender Template:

    Sender address: 10.11.112.140         LSP ID: 5

表1-15 display rsvp sender verbose命令显示信息描述表

字段

描述

Destination

隧道目的地址

Source

隧道源端设备的LSR ID

Tunnel ID

隧道ID

Style

资源预留风格，取值包括：

·SE：共享显式

·FF：固定过滤器

Sender address

发送者地址，用来标识隧道的源端

LSP ID

LSP ID

Setup priority

隧道建立优先级

Holding priority

隧道保持优先级

FRR desired

是否需要FRR保护标记，取值包括Yes 和No

BW protection desired

是否需要带宽保护标记，取值包括Yes 和No

Received upstream label

从上游收到的反向LSP标签

Sent upstream label

发送给下游的反向LSP标签

Previous hop

前一跳地址

Previous hop LIH

前一跳设备的逻辑接口索引

Mean rate (CIR)

平均速率，单位为kbit/s

Mean burst size (CBS)

平均峰值速率，单位为byte/s

Path MTU

路径的最大传输单元

QoS service

QoS业务类型，取值包括Controlled_Load和Guaranteed

Received message Epoch

接收消息携带的Message ID Object中Epoch字段的值

Received message ID

接收消息中的Message ID

Sent message epoch

发送消息携带的Message ID Object中Epoch字段的值

Sent message ID

发送消息中的Message ID

In-Interface

消息的入接口名称

Local LIH

本地的逻辑接口索引

Local address

Path消息的出接口IP地址

Refresh interval

路径和预留消息的刷新时间间隔，单位为毫秒

Out-Interface

消息的出接口名称

Nexthop

下一跳地址

Unknown object number

无法识别的Object的个数

Received ERO number

接收的ERO（Explicit Route Object，显式路由对象）的个数及其信息

ERO信息包括显式路径经过的节点的地址、该节点为松散下一跳（Loose）或严格下一跳（Strict）

Sent ERO number

发送的ERO的个数及其信息

ERO信息包括显式路径经过的节点的地址、该节点为松散下一跳（Loose）或严格下一跳（Strict）

XRO number

XRO（Exclude Route Object，排除路由对象）的个数

如果XRO的个数不为零，则接下来显示XRO对象中的地址，该地址为不希望路由经过的接口地址或节点LSR-ID，即XRO中的地址不会出现在路由经过的地址列表中。XRO中的地址信息没有先后顺序要求

RRO number

RRO（Record Route Object，记录路由对象）的个数

如果RRO的个数不为零，则接下来显示RRO对象中所记录的IP地址或标签信息

只有Tunnel接口上配置了路由记录功能后，才会显示RRO信息

Flag

RRO对象中标记的值及其含义，标记含义的取值包括：

·No FRR：表示没有配置FRR保护

·FRR Avail：表示FRR保护可用

·In use：表示已经发生FRR切换

·BW：表示带宽保护

·Node-Prot：表示节点保护

·Node-ID：表示RRO对象中的地址为节点的LSR ID

·In-Int：表示RRO对象中的地址为入接口的地址

·Global label：表示全局标签空间

Fast Reroute PLR

PLR（Point of Local Repair，本地修复节点）信息，取值包括：

·None：没有绑定快速重路由的旁路隧道

·Ready：绑定快速重路由的旁路隧道，此时未进行切换

·Active：绑定快速重路由的旁路隧道，此时已进行切换

FRR i{.MsoCommentReference}nner label

快速重路由旁路隧道的入口标签，只有为PLR节点才会显示此字段

Bypass tunnel

旁路隧道的隧道名称，只有为PLR节点才会显示此字段

Sender Template

发送者模板

Sender address

FRR切换后，Path消息的发送者地址，取值为PLR节点上旁路隧道的出接口地址

LSP ID

FRR切换后，Path消息所携带的LSP ID

Fast Reroute MP

MP（Merge Point，汇聚点）信息，取值包括：

·{.TableTextChar}Active：为{.TableTextChar}MP节点，且已进行FRR切换

·None：不是MP节点，或虽然是MP节点但没有发生FRR切换

In-Interface

消息的入接口名称

【相关命令】

·**display rsvp lsp**

·**display rsvp request**

·**display rsvp reservation**

**RSVP \-- RSVP配置命令 \-- display rsvp statistics**

------------------------------------------------------------------------

**[display rsvp** **statistics**]命令用来显示RSVP统计信息。

【命令】

**[display rsvp** **statistics** [ **interface** [ *interface-type* *interface-number*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface**]：显示接口的RSVP统计信息。

*[interface-type interface-number*]：显示指定接口的RSVP统计信息。*interface-type interface-number*为接口类型及接口编号。

【使用指导】

执行**display** **rsvp statistics**命令时：

·如果不指定**interface**参数，则显示全局的RSVP统计信息。

·如果只指定**interface**参数，不指定*interface-type interface-number*参数，则显示所有开启了RSVP能力的接口的RSVP统计信息。

·如果指定**interface*** interface-type interface-number*参数，则显示指定接口的RSVP统计信息。

【举例】

\# 显示全局的RSVP统计信息。

\<Sysname\> display rsvp statistics

Object                 Added            Deleted

  PSB                  3                1

  RSB                  3                1

  LSP                  3                1

Packet                 Received         Sent

  Path                 5                5

  Resv                 5                5

  PathError            0                0

  ResvError            0                0

  PathTear             0                0

  ResvTear             0                0

  ResvConf             0                0

  Bundle               0                0

  Ack                  0                0

  Srefresh             0                0

  Hello                0                0

  Challenge            0                0

  Response             0                0

  Error                0                0

\# 显示接口的RSVP统计信息。

\<Sysname\> display rsvp statistics interface

GE1/0/2:

Packet                 Received         Sent

  Path                 2                2

  Resv                 2                2

  PathError            0                0

  ResvError            0                0

  PathTear             0                0

  ResvTear             0                0

  ResvConf             0                0

  Bundle               0                0

  Ack                  0                0

  Srefresh             0                0

  Hello                0                0

  Challenge            0                0

  Response             0                0

  Error                0                0

GE1/0/4:

Packet                 Received         Sent

  Path                 3                3

  Resv                 3                3

  PathError            0                0

  ResvError            0                0

  PathTear             0                0

  ResvTear             0                0

  ResvConf             0                0

  Bundle               0                0

  Ack                  0                0

  Srefresh             0                0

  Hello                0                0

  Challenge            0                0

  Response             0                0

  Error                0                0

表1-16 display rsvp statistics命令显示信息描述表

字段

描述

PSB

添加/删除PSB的次数

RSB

添加/删除RSB的次数

LSP

添加/删除LSP的次数

Path

接收/发送的Path消息数量

Resv

接收/发送的Resv消息数量

PathError

接收/发送的Path Error消息数量

ResvError

接收/发送的Resv Error消息数量

PathTear

接收/发送的Path Tear消息数量

ResvTear

接收/发送的Resv Tear消息数量

ResvConf

接收/发送的Resv Conf消息数量

Bundle

接收/发送的Bundle消息数量

Ack

接收/发送的Ack消息数量

Srefresh

接收/发送的Srefresh消息数量

Hello

接收/发送的Hello消息数量

Challenge

接收/发送的Integrity Challenge消息数量

Response

接收/发送的Integrity Response消息数量

Error

接收/发送的错误消息数量

【相关命令】

·**reset** **rsvp** **statistics**

**RSVP \-- RSVP配置命令 \-- dscp**

------------------------------------------------------------------------

**[dscp**]命令用来配置发送的RSVP报文的DSCP优先级。

**[undo dscp**]命令用来恢复缺省情况。

【命令】

**[dscp ***dscp-value*]

**[undo dscp**]

【缺省情况】

发送的RSVP报文的DSCP优先级为48。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dscp-value*]：发送的RSVP报文的DSCP优先级，取值范围为0～63。

【使用指导】

DSCP（Differentiated Services Code point，差分服务编码点）携带在IP报文中的ToS字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定发送的RSVP报文中携带的DSCP优先级的取值。

【举例】

\# 配置发送的RSVP报文的DSCP优先级为56。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp dscp 56

【相关命令】

·**display rsvp**

**RSVP \-- RSVP配置命令 \-- graceful-restart enable**

------------------------------------------------------------------------

**[graceful-restart enable**]命令用来开启RSVP的GR（Graceful Restart，平滑重启）功能。

**[undo graceful-restart enable**]命令用来关闭RSVP的GR功能。

【命令】

**[graceful-restart enable**]

**[undo graceful-restart enable**]

【缺省情况】

RSVP的GR功能处于关闭状态。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

目前RSVP仅支持GR Helper方功能，即协助邻居设备进行GR重启，而自身不能进行GR重启。本地设备的NSF（Nonstop Forwarding，不间断转发）只能通过主备进程之间的NSR（Nonstop Routing，不间断路由）功能实现。

只有在接口视图下通过**rsvp hello enable**命令开启了RSVP的Hello扩展功能后，本地设备才能作为GR helper协助该接口所连接的邻居设备进行GR重启。

【举例】

\# 全局开启RSVP的GR功能。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp graceful-restart enable

【相关命令】

·**rsvp hello enable**

**RSVP \-- RSVP配置命令 \-- hello interval**

------------------------------------------------------------------------

**[hello interval**]命令用来配置Hello Request消息的发送时间间隔。

**[undo hello** **interval**]命令用来恢复缺省情况。

【命令】

**[hello **]**interval***interval*

**[undo hello **]**interval**

【缺省情况】

Hello Request消息的发送时间间隔为5秒。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：Hello Request消息的发送时间间隔，取值范围为1～60，单位为秒。

【使用指导】

在本命令指定的时间内，如果没有收到邻居发送的Hello Request消息，则主动向邻居发送Hello Request消息；如果收到了邻居发送的Hello Request消息，则立即向邻居回应Hello Ack消息。

只有在接口视图下通过**rsvp hello enable**命令开启了RSVP的Hello扩展功能后，设备才会通过该接口发送Hello消息，本命令才会生效。

【举例】

\# 配置Hello Request消息的发送时间间隔为10秒。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp hello interval 10

【相关命令】

·**hello lost**

·**rsvp hello enable**

**RSVP \-- RSVP配置命令 \-- hello lost**

------------------------------------------------------------------------

**[hello lost**]命令用来配置Hello消息连续丢失或错误的最大次数。

**[undo hello lost**]命令用来恢复缺省情况。

【命令】

**[hello lost** *times*]

**[undo hello lost**]

【缺省情况】

Hello消息连续丢失或错误的最大次数为4次。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[times*]：Hello消息连续丢失或错误的最大次数，取值范围为3～10。

【使用指导】

当连续未收到Hello消息或收到错误的Hello消息的次数达到本命令配置的次数时，认为邻居设备发生故障。如果配置了GR功能，则本地设备作为GR Helper协助邻居进行GR重启；如果没有配置GR功能，但配置了FRR功能，则进行FRR切换。

Hello消息连续丢失或错误的最大次数过大会导致不能快速检测到邻居的故障，过小则可能会导致错误地认为邻居出现故障。请根据实际组网和应用需求选择合适的值。

只有通过**rsvp hello enable**命令开启RSVP的Hello扩展功能后，本命令才会生效。

【举例】

\# 配置Hello消息连续丢失或错误的最大次数为6次。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp hello lost 6

【相关命令】

·**hello ****interval**

·**rsvp hello enable**

**RSVP \-- RSVP配置命令 \-- keep-multiplier**

------------------------------------------------------------------------

**[keep-multiplier**]命令用来配置PSB和RSB的老化超时倍数。

**[undo keep-multiplier**]命令用来恢复缺省情况。

【命令】

**[keep-multiplier** *number*]

**[undo keep-multiplier**]

【缺省情况】

PSB和RSB的老化超时倍数为3。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：PSB和RSB的老化超时倍数，取值范围为3～255。

【使用指导】

PSB和RSB老化时间的计算方法为：Expired_Time＝（keep-multiplier＋0.5）×1.5×refresh-time。其中，refresh-time为对端设备向本端通告的路径和预留消息刷新时间间隔。

为了避免设备上保存过多的PSB和RSB，占用系统资源，如果老化时间内没有收到Path或Resv刷新信息，相应的PSB或RSB将会被删除。

【举例】

\# 配置PSB和RSB的老化超时倍数为5。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp keep-multiplier 5

【相关命令】

·**refresh interval**

**RSVP \-- RSVP配置命令 \-- peer**

------------------------------------------------------------------------

**[pee**]**r**命令用来创建RSVP认证邻居，并进入RSVP邻居视图。在该视图下可以配置邻居的认证信息。

**[undo peer**]命令用来删除指定的RSVP认证邻居。

【命令】

**[pee**]**r ***ip-address*

**[undo pee**]**r ***ip-address*

【缺省情况】

设备上不存在任何RSVP认证邻居。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：RSVP认证邻居的地址。

【使用指导】

通过本命令创建RSVP认证邻居后，可以在RSVP邻居视图下为特定的邻居配置特定的认证信息（如认证密钥、RSVP SA的空闲老化时间等）。

设备接收到带认证对象的RSVP消息后，根据消息（Path，Path Tear消息）PHOP中的IP地址或消息（Path Error，Resv，Resv Error等除Path，Path Tear外的其它消息）的源IP地址来检查设备上是否存在与之匹配的认证邻居。如果存在且为该认证邻居配置了认证密钥，则根据认证邻居的密钥来检查消息是否合法；否则，根据接口视图或全局视图下配置的认证密钥来检查消息是否合法。如果三个视图下都没有配置认证密钥，则忽略消息中的认证对象，直接接收该消息。

设备发送RSVP消息时，根据消息目的IP地址所对应的下一跳地址来检查设备上是否存在与之匹配的认证邻居。如果存在且为该认证邻居配置了认证密钥，则根据认证邻居的密钥来设置认证对象；否则，根据接口视图或全局视图下配置的认证密钥来设置认证对象。如果三个视图下都没有配置认证密钥，则不在发送的消息中携带认证对象。

如果发生了FRR切换，则PLR节点所对应的下游认证邻居为旁路隧道的目的IP地址，MP节点所对应的上游认证邻居为PLR节点旁路隧道的物理出接口的IP地址。

【举例】

\# 创建RSVP认证邻居1.1.1.1，进入RSVP邻居视图，并配置此邻居的认证密钥为明文abcdfegh。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp peer 1.1.1.1

Sysname-rsvp-peer-1.1.1.1 authentication key plain abcdfegh

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

**RSVP \-- RSVP配置命令 \-- refresh interval**

------------------------------------------------------------------------

**[refresh interval**]命令用来配置路径消息和预留消息的刷新时间间隔。

**[undo refresh interval**]命令用来恢复缺省情况。

【命令】

**[refresh** **interval** *interval*]

**[undo refresh **]**interval**

【缺省情况】

路径消息和预留消息的刷新时间间隔为30秒。

【视图】

RSVP视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：路径消息和预留消息的刷新时间间隔，取值范围为10～65535，单位为秒。

【使用指导】

本命令具有如下作用：

·决定发送的路径消息和预留消息的刷新时间间隔。

·在路径消息和预留消息中携带本地配置的刷新时间间隔，以便对端设备根据该值计算PSB和RSB的老化时间。

【举例】

\# 配置路径和预留消息的刷新时间间隔为60秒。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp refresh interval 60

【相关命令】

·**keep-multiplier**

**RSVP \-- RSVP配置命令 \-- reset rsvp authentication**

------------------------------------------------------------------------

**[reset rsvp authentication**]命令用来手工清除RSVP SA。

【命令】

**[reset rsvp authentication ****from***ip-address ***to ***ip-address *]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[from*** ip-address*]：清除认证发起节点IP地址为指定地址的RSVP SA。*ip-address*为认证发起节点的IP地址。

**[to ***ip-address*]：清除认证目的节点IP地址为指定地址的RSVP SA。*ip-address*为认证目的节点的IP地址。

【使用指导】

执行**reset rsvp authentication**命令时，如果没有指定**from*** ip-address*和**to ***ip-address*参数，则清除本地设备与所有邻居建立的RSVP SA。

【举例】

\# 清除所有的RSVP SA。

\<Sysname\> reset rsvp authentication

\# 清除认证发起节点IP地址为1.1.1.1、认证目的节点IP地址为2.2.2.2的RSVP SA。

\<Sysname\> reset rsvp authentication from 1.1.1.1 to 2.2.2.2

【相关命令】

·**display rsvp authentication**

**RSVP \-- RSVP配置命令 \-- reset rsvp statistics**

------------------------------------------------------------------------

**[reset** **rsvp** **statistics**]命令用来清除RSVP的统计信息。

【命令】

**[reset** **rsvp** **statistics** [ **interface** [ *interface-type* *interface-number*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface**]：清除接口的RSVP统计信息。

*[interface-type interface-number*]：清除指定接口的RSVP统计信息。*interface-type interface-number*为接口类型及接口编号。

【使用指导】

执行**reset** **rsvp statistics**命令时：

·如果不指定**interface**参数，则清除全局的RSVP统计信息。

如果只指定**interface**参数，不指定*interface-type interface-number*参数，则清除所有开启了RSVP能力的接口的RSVP统计信息。

如果指定**interface*** interface-type interface-number*参数，则清除指定接口的RSVP统计信息。

【举例】

\# 清除全局的RSVP统计信息。

\<Sysname\> reset rsvp statistics

\# 清除所有开启了RSVP能力的接口的RSVP统计信息。

\<Sysname\> reset rsvp statistics interface

【相关命令】

·**display rsvp** **statistics**

**RSVP \-- RSVP配置命令 \-- rsvp**

------------------------------------------------------------------------

**[rsvp**]命令用来全局开启RSVP能力，并进入RSVP视图。

**[undo rsvp**]命令用来全局关闭RSVP能力。

【命令】

**[rsvp**]

**[undo rsvp**]

【缺省情况】

全局RSVP能力处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

全局开启RSVP能力时，需要同时通过**mpls te**命令全局开启MPLS TE能力。

【举例】

\# 全局开启RSVP能力，并进入RSVP视图。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp

【相关命令】

·**mpls te**（MPLS命令参考/MPLS TE）

·**rsvp enable**

**RSVP \-- RSVP配置命令 \-- rsvp authentication challenge**

------------------------------------------------------------------------

**[rsvp authentication challenge**]命令用来在接口下开启RSVP认证的challenge-response握手功能。

**[undo **]**rsvp authentication challenge**命令用来在接口下关闭RSVP认证的challenge-response握手功能。

【命令】

**[rsvp authentication challenge**]

**[undo rsvp authentication challenge**]

【缺省情况】

RSVP认证的challenge-response握手功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

为了避免报文的重放（Replay）攻击，RSVP接收认证消息时要求认证消息的序列号依次增加，RSVP在接收RSVP SA中保存最后一次收到的消息的序列号，用于判断后续消息是否符合要求。但是，在新创建接收RSVP SA的时候，无法获取发送端的序列号，因此缺省情况下，创建接收RSVP SA时将接收序列号填写为零，这样对端发送任意序列号的消息就都能接收。这就增加了重放攻击的风险。为了避免这种风险，可以执行**authentication challenge**命令，使得在新建接收RSVP SA时执行challenge-response握手过程，获取发送端的序列号。

RSVP认证的challenge-response握手功能可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启RSVP认证的challenge-response握手功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp authentication challenge

·交换应用

\# 在接口Vlan-interface10上开启RSVP认证的challenge-response握手功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp authentication challenge

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication key**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- rsvp authentication key**

------------------------------------------------------------------------

**[rsvp authentication key**]命令用来在接口下开启RSVP认证功能，并配置认证密钥。

**[undo rsvp authentication key**]命令用来在接口下关闭RSVP认证功能。

【命令】

**[rsvp authentication key **[{ **cipher** \| **plain** } *auth-key*]]

**[undo rsvp authentication key**]

【缺省情况】

RSVP认证功能处于关闭状态，即不进行RSVP认证。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：表示以密文形式设置密钥。

**[plain**]：表示以明文形式设置密钥。

*[auth-key*]：认证密钥，区分大小写。如果采用明文（**plain**）形式，则为1～16个字符的明文字符串；如果采用密文（**cipher**）形式，则为1～53个字符的密文字符串。

【使用指导】

RSVP认证功能可以用来确保RSVP消息不会被篡改，防止伪造的资源预留请求非法占用网络资源。

配置RSVP认证功能后，发送RSVP消息时会使用MD5算法对认证密钥和消息内容计算出消息摘要，并将消息摘要添加到发送的RSVP消息中。对端接收到RSVP消息后，也进行同样地计算，并将计算结果和消息中的摘要进行比较。如果一致，则认证通过，接收该消息；否则认证失败，丢弃该消息。

RSVP认证功能可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

如果在多个视图下配置了认证密钥，则认证密钥的使用优先级顺序从高到低依次为：RSVP邻居视图、接口视图、RSVP视图。例如，如果在RSVP邻居视图和RSVP视图都开启了与特定邻居的RSVP认证功能，并配置了不同的认证密钥，则采用RSVP邻居视图下配置的密钥认证本地设备和该邻居之间的RSVP消息。

如果已经采用某个视图下配置的认证密钥建立了RSVP SA，则只有先删除当前视图下配置的认证密钥或执行**reset rsvp authentication**命令删除该RSVP SA，才会按照上述优先级顺序重新查找新的认证密钥并建立RSVP SA。

需要注意的是：

·本地设备上开启RSVP认证功能后，在相应的RSVP邻居上也需要开启RSVP认证功能，并配置相同的认证密钥。

·以明文或密文形式设置的密钥，均以密文的方式保存在配置文件中。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启RSVP认证功能，并配置认证密钥为abcdefgh。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp authentication key plain abcdefgh

·交换应用

\# 在接口Vlan-interface10上开启RSVP认证功能，并配置认证密钥为abcdefgh。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp authentication key plain abcdefgh

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication lifetime**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- rsvp authentication lifetime**

------------------------------------------------------------------------

**[rsvp authentication lifetime**]命令用来在接口下配置RSVP SA的空闲老化时间。

**[undo rsvp** **authentication lifetime**]命令用来恢复缺省情况。

【命令】

**[rsvp authentication lifetime ***life-time*]

**[undo rsvp authentication lifetime**]

【缺省情况】

RSVP SA的空闲老化时间为1800秒（30分钟）。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[life-time*]：RSVP SA的空闲老化时间，取值范围为30～86400，单位为秒。

【使用指导】

开启了RSVP认证功能后，设备收发RSVP消息时会动态建立RSVP SA，以记录消息的序列号、方便对RSVP消息进行认证处理。

为了在不需要RSVP SA的时候，能够及时删除该RSVP SA，回收内存资源，每个RSVP SA都有其老化时间。当RSVP SA的空闲时间到达老化时间时，将删除该RSVP SA。设备发送和接收RSVP认证消息时，会更新对应RSVP SA的空闲时间，避免其被老化删除。

RSVP SA的空闲老化时间可以在如下视图配置：

·RSVP视图：该视图下的配置对所有RSVP SA生效。

·RSVP邻居视图：该视图下的配置只对与指定RSVP邻居之间的RSVP SA生效。

·接口视图：该视图下的配置只对根据指定接口下的配置生成的RSVP SA生效。

采用某个视图下配置的认证密钥建立RSVP SA后，该RSVP SA的空闲老化时间为该视图下配置的老化时间。

修改RSVP SA的空闲老化时间后，只会对新建立的RSVP SA生效。要想使得修改后的空闲老化时间对已建立的RSVP SA生效，则需要执行**reset rsvp authentication**命令来删除并重新建立RSVP SA。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RSVP SA的空闲老化时间为100秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp authentication lifetime 100

·交换应用

\# 在接口Vlan-interface10上配置RSVP SA的空闲老化时间为100秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp authentication lifetime 100

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication window-size**

**RSVP \-- RSVP配置命令 \-- rsvp authentication window-size**

------------------------------------------------------------------------

**[rsvp authentication window-size**]命令用来在接口下配置对于带有认证信息的RSVP消息，最大可允许的乱序消息数量。

**[undo** **rsvp authentication window-size**]命令用来恢复缺省情况。

【命令】

**[rsvp authentication window-size ***number*]

**[undo rsvp authentication window-size**]

【缺省情况】

对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[number*]：最大可允许的乱序消息数量，取值范围为1～64。

【使用指导】

为了防止报文重放攻击，RSVP在带有认证信息的RSVP消息中携带唯一的序列号。每发送一个消息，序列号依次增加。如果接收到的消息序列号在允许的范围内，则接受该消息；否则，丢弃该消息。

RSVP判断报文序列号是否在允许范围内的方法为：

(1)在设备上记录最后一次接收到的RSVP报文的序列号。

(2)设备接收到新的RSVP报文时，将该报文的序列号与记录的序列号进行比较：

·如果大于记录的序列号，则将记录的序列号更新为该报文的序列号。

·如果等于记录的序列号，则认为是重放攻击，丢弃该报文。

·如果小于记录的序列号、大于（记录的序列号---本命令配置的window-size），且未收到过该序列号的报文，则接收该报文；若已经收到过该序列号的报文，则认为是重放攻击，丢弃该报文。

·如果小于等于（记录的序列号---本命令配置的window-size），则认为报文序列号不合法，丢弃该报文。

缺省情况下，最大可允许的乱序消息数量为1，即如果新收到的RSVP消息的序列号小于最后收到的消息序列号，则认为该消息是重放攻击，丢弃该消息。但是，如果在短时间内发送了多个RSVP消息，那么这些消息到达邻居时可能会产生乱序。若采用缺省情况，则会导致这些乱序消息被丢弃。此时，可以通过本命令配置较大的window-size解决此问题。

采用某个视图下配置的认证密钥建立RSVP SA后，该RSVP SA的最大可允许乱序消息数量为该视图下配置的值。

修改最大可允许的乱序消息数量后，只会对新建立的RSVP SA生效。要想使得修改后的最大可允许乱序消息数量对已建立的RSVP SA生效，则需要执行**reset rsvp authentication**命令来删除并重新建立RSVP SA。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为10。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp authentication window-size 10

·交换应用

\# 在接口Vlan-interface10上配置对于带有认证信息的RSVP消息，最大可允许的乱序消息数量为10。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp authentication window-size 10

【相关命令】

·**authentication challenge**

·**authentication key**

·**authentication lifetime**

·**authentication window-size**

·**display rsvp authentication**

·**reset rsvp authentication**

·**rsvp authentication challenge**

·**rsvp authentication key**

·**rsvp authentication lifetime**

**RSVP \-- RSVP配置命令 \-- rsvp bfd enable**

------------------------------------------------------------------------

**[rsvp bfd enable**]命令用来配置通过BFD检测本地设备和RSVP邻居之间链路的状态。

**[undo rsvp bfd enable**]命令用来恢复缺省情况。

【命令】

**[rsvp bfd enable**]

**[undo rsvp bfd enable**]

【缺省情况】

不会通过BFD检测本地设备和RSVP邻居之间链路的状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

通常情况下，RSVP通过Hello消息检测邻居的状态，RSVP无法及时感知邻居的故障。执行本命令后，设备上会建立BFD会话，通过BFD会话来检测本地设备和RSVP邻居之间链路的状态。当RSVP邻居出现故障时，BFD能够快速检测到该故障，并通知RSVP进行相应的处理（例如，配置了FRR保护时，会进行FRR切换）。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置通过BFD检测本地设备和RSVP邻居之间链路的状态。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp bfd enable

·交换应用

\# 在接口Vlan-interface10上配置通过BFD检测本地设备和RSVP邻居之间链路的状态。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp bfd enable

**RSVP \-- RSVP配置命令 \-- rsvp enable**

------------------------------------------------------------------------

**[rsvp enable**]命令用来开启接口的RSVP能力。

**[undo rsvp enable**]命令用来关闭接口的RSVP能力。

【命令】

**[rsvp enable**]

**[undo rsvp enable**]

【缺省情况】

接口的RSVP能力处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

必须先在系统视图下通过**rsvp**命令全局开启RSVP能力，才能开启接口的RSVP能力。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启RSVP能力。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp quit

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp enable

·交换应用

\# 在接口Vlan-interface10上开启RSVP能力。

\<Sysname\> system-view

Sysname rsvp

Sysname-rsvp quit

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp enable

【相关命令】

·**rsvp**

**RSVP \-- RSVP配置命令 \-- rsvp hello enable**

------------------------------------------------------------------------

**[rsvp hello enable**]命令用来开启RSVP的Hello扩展功能。

**[undo rsvp hello enable**]命令用来关闭RSVP的Hello扩展功能。

【命令】

**[rsvp hello enable**]

**[undo rsvp hello enable**]

【缺省情况】

RSVP的Hello扩展功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

在接口视图下开启RSVP的Hello扩展功能后，设备会通过该接口发送和接收Hello消息，通过Hello消息检测邻居的状态。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启RSVP的Hello扩展功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp hello enable

·交换应用

\# 在接口Vlan-interface10上开启RSVP的Hello扩展功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp hello enable

【相关命令】

·**hello lost**

·**hello interval**

**RSVP \-- RSVP配置命令 \-- rsvp reduction retransmit increment**

------------------------------------------------------------------------

**[rsvp** **reduction retransmit** **increment**]命令用来配置RSVP消息可靠传递功能的重传增量。

**[undo** **rsvp** **reduction retransmit** **increment**]命令用来恢复缺省情况。

【命令】

**[rsvp reduction retransmit** **increment** *increment-value*]

**[undo **]**rsvp reduction retransmit** **increment**

【缺省情况】

RSVP消息可靠传递功能的重传增量为1。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[increment-value*]：重传增量，取值范围为1～10。

【使用指导】

通过**rsvp reduction srefresh** **reliability**命令开启RSVP消息的可靠传递功能后，重传增量和重传时间间隔共同决定了下一次重传消息的时间，详细介绍请参见"1.1.32  (?-1914564316#_Ref327966342)rsvp reduction srefresh(?-1914564316#_Ref327966357)"。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RSVP消息可靠传递功能的重传增量为2。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp reduction retransmit increment 2

·交换应用

\# 在接口Vlan-interface10上配置RSVP消息可靠传递功能的重传增量为2。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp reduction retransmit increment 2

【相关命令】

·**rsvp reduction retransmit interval**

·**rsvp reduction srefresh**

**RSVP \-- RSVP配置命令 \-- rsvp reduction retransmit interval**

------------------------------------------------------------------------

**[rsvp** **reduction retransmit** **interval**]命令用来配置RSVP消息可靠传递功能的重传时间间隔。

**[undo** **rsvp** **reduction retransmit** **interval**]命令用来恢复缺省情况。

【命令】

**[rsvp reduction retransmit** **interval** *retrans-timer-value*]

**[undo rsvp reduction retransmit** **interval**]

【缺省情况】

RSVP消息可靠传递功能的重传时间间隔为500毫秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[retrans-timer-value*]：重传时间间隔，取值范围为500～3000，单位为毫秒。

【使用指导】

通过**rsvp reduction srefresh** **reliability**命令开启RSVP消息的可靠传递功能后，重传增量和重传时间间隔共同决定了下一次重传消息的时间，详细介绍请参见"1.1.32  (?-1914564316#_Ref327966342)rsvp reduction srefresh(?-1914564316#_Ref327966357)"。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上配置RSVP消息可靠传递功能的重传时间间隔为1000毫秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp reduction retransmit interval 1000

·交换应用

\# 在接口Vlan-interface10上配置RSVP消息可靠传递功能的重传时间间隔为1000毫秒。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp reduction retransmit interval 1000

【相关命令】

·**rsvp reduction retransmit increment**

·**rsvp reduction srefresh**

**RSVP \-- RSVP配置命令 \-- rsvp reduction srefresh**

------------------------------------------------------------------------

**[rsvp reduction srefresh**]命令用来开启摘要刷新（Summary Refresh）功能和RSVP消息的可靠传递功能。

**[undo rsvp** **reduction srefresh**]命令用来关闭摘要刷新功能和RSVP消息的可靠传递功能。

【命令】

**[rsvp reduction srefresh**  **reliability** ]

**[undo rsvp reduction srefresh**]

【缺省情况】

摘要刷新功能和RSVP消息的可靠传递功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[reliability**]：开启RSVP消息的可靠传递功能。如果不指定本参数，则只开启摘要刷新功能。

【使用指导】

通常情况下，RSVP发送Path和Resv消息后，会周期性地（由**refresh interval**命令配置）发送带有同样状态、对象等信息的Path和Resv消息来维护路径和预留状态，该消息统称为Refresh消息。Refresh消息不仅用于在RSVP邻居节点进行状态同步，也用于恢复丢失的RSVP消息。

由于Refresh消息是周期性发送的，当网络中的RSVP会话比较多时，Refresh消息会加重网络负载，此时**refresh interval**命令配置的刷新时间间隔不宜过小；对于时延敏感的应用，当RSVP消息丢失时，希望能够尽快通过Refresh消息恢复丢失的消息，此时**refresh interval**命令配置的刷新时间间隔不宜过大。简单地调整刷新时间间隔无法同时解决这两类问题。

摘要刷新和RSVP消息的可靠传递功能可以很好地解决上述问题。

摘要刷新功能的工作机制为：发送Path和Resv消息时，在消息中携带Message ID，用来唯一标识一个消息；RSVP通过发送携带待刷新消息的Message ID的Srefresh消息，来刷新对应的Path和Resv消息。采用摘要刷新功能后，不必传送标准的Path和Resv消息，只需传递携带Path和Resv消息摘要的Srefresh消息，即可实现对RSVP路径和预留状态进行刷新，减少了网络上的Refresh消息流量，并加快了节点对刷新消息的处理速度。

RSVP消息的可靠传递功能是指对端设备需要应答本端发送的RSVP消息，否则将会重传此消息。其工作机制为：节点发送了携带Message_ID对象的消息，且Message_ID对象的ACK_Desired标识（是否需要应答标识）置位后，如果在重传时间Rf内没有收到携带对应Message_ID_ACK对象的消息，则重传时间Rf超时后重传此消息，并将重传时间置为（1＋Delta）×Rf。节点持续按照上述方法重传此消息，直到节点在重传时间超时前接收到对应的应答消息，或消息传送次数达到3次。

其中，重传时间Rf的初始值为**rsvp reduction retransmit** **interval**命令配置的值；Delta的值为**rsvp reduction retransmit** **increment**命令配置的值。

需要注意的是：

·开启摘要刷新功能后，将不会周期性发送Refresh消息维护路径和预留状态。

·Srefresh消息的发送周期由**refresh interval**命令决定。

【举例】

·路由应用

\# 在接口GigabitEthernet1/0/1上开启摘要刷新功能和RSVP消息的可靠传递功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 rsvp reduction srefresh reliability

·交换应用

\# 在接口Vlan-interface10上开启摘要刷新功能和RSVP消息的可靠传递功能。

\<Sysname\> system-view

Sysname interface vlan-interface 10

Sysname-Vlan-interface10 rsvp reduction srefresh reliability

【相关命令】

·**refresh interval**

·**rsvp reduction retransmit increment**

·**rsvp reduction retransmit interval**

