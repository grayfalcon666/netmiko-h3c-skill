
**User Profile \-- User Profile配置命令 \-- display user-profile**

------------------------------------------------------------------------

**[display user-profile**]用来显示User Profile的配置信息和在线用户信息。

【命令】

集中式设备：

**[display user-profile** [ **session-group**   **name** *profile-name* ]]

分布式设备－独立运行模式/集中式IRF设备：

**[display** **user-profile** [ **session-group**   **name** *profile-name*   **slot**]*slot-number * **cpu** *cpu-number* ]

分布式设备－IRF模式：

**[display** **user-profile** [ **session-group**   **name** *profile-name*  ]**chassis***chassis-number***slot***slot-number* **cpu** *cpu-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[session-group**]：显示Session Group Profile的配置信息和在线用户信息。

**[name*** profile-name*]：表示User Profile的名称，为1～31个字符的字符串，只能包含英文字母a-z,A-Z、数字、下划线，且必须以英文字母开始，区分大小写。User Profile的名称必须全局唯一。如果未指定本参数，将显示所有User Profile的配置信息和在线用户信息。

**[slot*** slot-number*]：显示User Profile的配置信息和指定单板的在线用户信息，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示User Profile的配置信息和所有在位单板的在线用户信息。（分布式设备－独立运行模式）

**[slot*** slot-number*]：显示User Profile的配置信息和指定成员设备的在线用户信息，*slot-number*表示设备在IRF中的成员编号。如果未指定本参数，将显示User Profile的配置信息和所有成员设备的在线用户信息。（集中式IRF设备）（不支持IRF3的设备）

**[slot*** slot-number*]：显示User Profile的配置信息和指定成员设备/PEX的在线用户信息，*slot-number*表示设备在IRF中的成员编号或者PEX的虚拟槽位号。如果未指定本参数，将显示User Profile的配置信息和所有成员设备/PEX的在线用户信息。（集中式IRF设备）（支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示User Profile的配置信息和指定成员设备上指定单板的在线用户信息，*chassis-number*表示设备在IRF中的成员编号，*slot-number*表示单板所在的槽位号。如果未指定本参数，将显示User Profile的配置信息和所有成员设备上在位单板的在线用户信息。（分布式设备－IRF模式）（不支持IRF3的设备）

**[chassis** *chassis-number* **slot** *slot-number*]：显示User Profile的配置信息和指定单板的在线用户信息，*chassis-number*表示设备在IRF中的成员编号或者PEX对应的虚拟框号，*slot-number*表示单板或PEX所在的槽位号。如果未指定本参数，将显示User Profile的配置信息和所有单板的在线用户信息。（分布式设备－IRF模式）（支持IRF3的设备）

**[cpu** *cpu-number*]：指定CPU号。*cpu-number*表示CPU的编号。只有指定的**slot**支持多CPU时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式/集中式IRF设备/分布式设备－IRF模式）

【举例】

\# 显示在名称为aaa的User Profile配置信息及被授权该User Profile的在线用户信息。（集中式设备）

\<Sysname\> display user-profile name aaa

  User-Profile: aaa

    Inbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p1

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p2

    Connection-limit amount: 1000

    Connection-limit rate: 100

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : GigabitEthernet1/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Inbound: Policy p1

        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        Connection-limit rate: 100

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

\# 显示设备上的Session Group Profile配置信息及被授权该Session Group Profile的在线用户信息。（集中式设备）

\<Sysname\> display user-profile session-group

  Session-Group-Profile: aaa

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : Ethernet1/2/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        QMProfile: a

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

  Session-Group-Profile: bbb

    Outbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    User user_4:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/2

        IP address   : 172.16.187.166

        VPN          : N/A

        Service VLAN : 100

\# 显示2号单板上的User Profile配置信息及被授权该User Profile的在线用户信息。（分布式设备－独立运行模式）

\<Sysname\> display user-profile slot 2

  User-Profile: aaa

    Inbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p1

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p2

    Connection-limit amount: 1000

    Connection-limit rate: 100

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : GigabitEthernet1/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Inbound: Policy p1

        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        Connection-limit rate: 100

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

  User-Profile: bbb

    Inbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p3

      Connection-limit rate: 200

    User user_4:

    Authentication type: Portal

    Network attributes:

      Interface    : GigabitEthernet1/0/2

      IP address   : 172.16.187.166

      VPN          : N/A

      Service VLAN : 100

\# 显示2号成员设备上的Session Group Profile配置信息及被授权该Session Group Profile的在线用户信息。（集中式IRF设备）

\<Sysname\> display user-profile session-group slot 2

  Session-Group-Profile: aaa

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : Ethernet1/2/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        QMProfile: a

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

  Session-Group-Profile: bbb

    Outbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    User user_4:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/2

        IP address   : 172.16.187.166

        VPN          : N/A

        Service VLAN : 100

\# 显示在1号成员设备2号单板上名称为aaa的User Profile配置信息及被授权该User Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile name aaa chassis 1 slot 2

  User-Profile: aaa

    Inbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p1

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p2

    Connection-limit amount: 1000

    Connection-limit rate: 100

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : GigabitEthernet1/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Inbound: Policy p1

        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        Connection-limit rate: 100

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

\# 显示在1号成员设备2号单板上名称为aaa的Session Group Profile配置信息及被授权该Session Group Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile session-group name aaa chassis 1 slot 2

  Session-Group-Profile: aaa

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    User user_1:

      Authentication type: 802.1X

      Network attributes:

        Interface    : GigabitEthernet1/0/1

        MAC address  : 0000-1111-2222

      Failed action list:

        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

        QMProfile: a

    User user_2:

      Authentication type: Portal

      Network attributes:

        Interface    : GigabitEthernet1/0/3

        IP address   : 172.16.187.16

        VPN          : N/A

        Service VLAN : 100

\# 显示名称为bbb的User Profile配置信息及被授权该User Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile name bbb

  User-Profile: bbb

    Inbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p3

    Connection-limit rate: 200

    Chassis 1 Slot 2:

      User user_3:

        Authentication type: 802.1X

        Network attributes:

          Interface    : GigabitEthernet1/0/1

          MAC address  : 1111-2222-3333

        Failed action list:

          Connection-limit rate: 200

      User user_4:

        Authentication type: PPP

        Network attributes:

          Interface    : GigabitEthernet1/0/2

    Chassis 1 Slot 5:

      User user_5:

        Authentication type: IPoE

        Network attributes:

          MAC address  : 2222-3333-4444

\# 显示指定名称为bbb的Session Group Profile配置信息及被授权该Session Group Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile session-group name bbb

  Session-Group-Profile: bbb

    Outbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    Chassis 1 Slot 2:

      User user_3:

        Authentication type: 802.1X

        Network attributes:

          Interface    : GigabitEthernet1/0/1

          MAC address  : 1111-2222-3333

        Failed action list:

          Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

          QMProfile: a

      User user_4:

        Authentication type: PPP

        Network attributes:

          Interface    : GigabitEthernet1/0/2

    Chassis 1 Slot 5:

      User user_5:

        Authentication type: IPoE

        Network attributes:

          MAC address  : 2222-3333-4444

\# 显示所有的User Profile配置信息及被授权该User Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile

  User-Profile: aaa

    Inbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p1

    Connection-limit amount: 1000

    Connection-limit rate: 100

    Chassis 1 Slot 2:

      User user_1:

        Authentication type: 802.1X

        Network attributes:

          Interface    : GigabitEthernet1/0/1

          MAC address  : 0000-1111-2222

        Failed action list:

          Inbound: Policy p1

    Chassis 1 Slot 5:

      User user_6:

        Authentication type: PPP

        Network attributes:

          Interface    : GigabitEthernet1/0/3

  User-Profile: bbb

    Inbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

      Policy: p3

    Connection-limit rate: 200

    Chassis 1 Slot 5:

      User user_7:

        Authentication type: IPoE

        Network attributes:

          Interface    : GigabitEthernet1/0/2

          MAC address  : 0000-1111-2222

          IP address   : 172.16.187.166

          VPN          : N/A

          Service VLAN : 100

\# 显示所有的Session Group Profile配置信息及被授权该Session Group Profile的在线用户信息。（分布式设备－IRF模式）

\<Sysname\> display user-profile session-group

  Session-Group-Profile: aaa

    Outbound:

      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    Chassis 1 Slot 2:

      User user_1:

        Authentication type: 802.1X

        Network attributes:

          Interface    : GigabitEthernet1/0/1

          MAC address  : 0000-1111-2222

        Failed action list:

          Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

          QMProfile: a

    Chassis 1 Slot 5:

      User user_6:

        Authentication type: PPP

        Network attributes:

          Interface    : GigabitEthernet1/0/3

  Session-Group-Profile: bbb

    Outbound:

      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)

    QMProfile: a

    Chassis 1 Slot 5:

      User user_7:

        Authentication type: IPoE

        Network attributes:

          Interface    : GigabitEthernet1/0/2

          MAC address  : 0000-1111-2222

          IP address   : 172.16.187.166

          VPN          : N/A

          Service VLAN : 100

表1-1 表1-1 display user-profile 命令显示信息描述表

字段

描述

User-Profile

User Profile名称

Inbound

在入方向上应用的策略

Outbound

在出方向上应用的策略

Session-Group-Profile

Session Group Profile名称

CIR

承诺信息速率，单位为kbps

CBS

承诺突发尺寸，也就是容纳突发流量的令牌桶深度，单位为byte

EBS

超出突发尺寸，在双令牌桶算法中超出突发流量超过承诺突发流量的部分，单位为byte

PIR

峰值信息速率

Connection-limit amount

用户最大连接数

Connection-limit rate

用户最大连接速率

Policy

策略名

QMProfile

队列调度策略

User user_1

与User Profile或Session Group Profile关联的用户信息

Authentication type

用户认证类型

·802.1X

·Portal

·PPP

·IPoE

·MACA

Network attributes

用户特征信息

Failed action list

在该用户上应用失败的动作

**User Profile \-- User Profile配置命令 \-- qos queue**

------------------------------------------------------------------------

**[qos queue**]命令用来在User Profile中为会话指定进入的队列。

**[undo qos queue**]命令用来取消配置。

【命令】

**[qos queue **[{ *queue-id* \| *queue-name* }]]

**[undo qos queue**]

【缺省情况】

User Profile下没有指定进入的队列。

【视图】

User Profile视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[queue ***[queue-id *[\| *queue-name* }]]：让应用此user profile的会话进入指定队列，*queue-id*表示队列序号，*queue-name*表示队列名称。

【使用指导】]

若指定进入的队列对应的是四队列调度策略，则可以配置的队列序号范围是0～3，超出范围则配置失败，不会进入指定队列。

应用此命令可以为对多个会话指定不同的队列从而决定其不同优先级的调度方式。

*[queue-id*]和*queue-name*的对应情况如[表]1-2(?1603098714#_Ref386643034)所示。

表1-2 *queue-id*数字和关键字对应表

*[queue-id*]数字

*[queue-id*]关键字

0

be

1

af1

2

af2

3

af3

4

af4

5

ef

6

cs6

7

cs7

【举例】

\# 在名称为user的User Profile中，指定会话进入队列7。

\<Sysname\> system-view

Sysname user-profile user

Sysname-user-profile-user qos queue 7

**User Profile \-- User Profile配置命令 \-- qos session-group identify**

------------------------------------------------------------------------

**[qos session-group identify**]命令用来在接口下配置会话组识别方式。

**[undo qos session-group identify**]命令用来取消会话组识别方式的配置。

【命令】

**[qos session-group identify **[{ **customer-vlan** \| **service-vlan** \| **customer-service-vlan \| subscriber-id** }]]

**[undo qos session-group identify **]

【缺省情况】

接口下没有配置会话组识别方式。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[customer-vlan**]：按内层VLAN识别会话组，内层VLAN为用户的私网VLAN。

**[service-vlan**]：按外层VLAN识别会话组，外层VLAN为运营商分配给用户的公网VLAN。

**[customer-service-vlan**]：按内层VLAN和外层VLAN识别会话组。

**[subscriber-id**]：按subscriber id识别会话组。

【使用指导】

若要配置Session Group Profile，则必须首先指定会话组的识别方式。

【举例】

\#在接口GigabitEthernet1/0/1上配置基于外层vlan的会话组识别方式。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 qos session-group identify service-vlan

**User Profile \-- User Profile配置命令 \-- user-profile**

------------------------------------------------------------------------

**[user-profile**]命令用来创建User Profile或Session Group Profile并进入相应的视图

**[undo** **user-profile**]命令用来删除指定的User Profile。

【命令】

**[user-profile** *profile-name* [ **type session-group** ]]

**[undo user-profile** *profile-name*]

【缺省情况】

不存在任何User Profile。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[profile-name*]：表示User Profile的名称，为1～31个字符的字符串，只能包含英文字母a-z,A-Z、数字、下划线，且必须以英文字母开始，区分大小写。User Profile的名称必须全局唯一。

**[type session-group**]：指定创建的类型为Session Group Profile。

【使用指导】

如果指定名称的User Profile或Session Group Profile已存在，则直接进入该User Profile或Session Group Profile的视图。

User Profile的名称必须全局唯一。

【举例】

\# 创建名称为a123的User Profile，并进入其视图。

\<Sysname\> system-view

Sysname user-profile a123

Sysname-user-profile-a123

\# 创建名称为a123的Session Group Profile，并进入其视图。

\<Sysname\> system-view

Sysname user-profile a123 type session-group

Sysname-session-group-profile-a123
