::: {#558364840 .myid}
[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404792854}[]{#struct_0_x1090_x8456_1289999239}[]{#_Toc361324561}[]{#_Toc350844407}

**User Profile \-- User Profile配置命令 \-- display user-profile**

------------------------------------------------------------------------

[**[display user-profile]{lang="EN-US"}**]{#struct_0_x1090_x8456_170292426}[用来显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和在线用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x1802222067}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1090_x8456_1271955774}

[**[display user-profile]{lang="EN-US"}**[ \[ **session-group** \] \[ **name** *profile-name* \]]{lang="EN-US"}]{#struct_0_x1090_x8456_1712558516}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1090_x8456_1217926390}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **user-profile** \[ **session-group** \] \[ **name** *profile-name* \] \[ **slot**]{lang="EN-US"}]{#struct_0_x1090_x8456_649260349}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1090_x8456_x1364468694}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **user-profile** \[ **session-group** \] \[ **name** *profile-name* \] \[]{lang="EN-US"}]{#struct_0_x1090_x8456_1462388771}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_166309654}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1090_x8456_1127288689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x257697550}

[[network-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_888455825}

[[network-operator]{lang="EN-US"}]{#struct_0_x1090_x8456_x1997083687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_1704894232}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1090_x8456_1306195280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1025665738}

[**[session-group]{lang="EN-US"}**]{#struct_0_x1090_x8456_170357962}[：显示]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的配置信息和在线用户信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x1090_x8456_x309013046}[：表示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含英文字母]{style="font-family:宋体"}[\[a-z,A-Z\]]{lang="EN-US"}[、数字、下划线，且必须以英文字母开始，区分大小写。]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称必须全局唯一。如果未指定本参数，将显示所有]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和在线用户信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1090_x8456_x1448182817}[：显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和指定单板的在线用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和所有在位单板的在线用户信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1090_x8456_1218385142}[：显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和指定成员设备的在线用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和所有成员设备的在线用户信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x1090_x8456_728697165}[：显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的在线用户信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的在线用户信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1090_x8456_x359570667}[：显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和指定成员设备上指定单板的在线用户信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和所有成员设备上在位单板的在线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x1090_x8456_x2049977491}[：显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和指定单板的在线用户信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的配置信息和所有单板的在线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1090_x8456_1642721900}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[号。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x2022983665}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_943555071}[显示在]{style="font-family:宋体"}[名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile name aaa]{lang="EN-US"}]{#struct_0_x1090_x8456_942899710}

[  User-Profile: aaa]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p2]{lang="EN-US"}

[    Connection-limit amount: 1000]{lang="EN-US"}

[    Connection-limit rate: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Inbound: Policy p1 ]{lang="EN-US"}

[        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[        Connection-limit rate: 100]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x120332746}[显示设备上]{style="font-family:宋体"}[的]{style="font-family:
宋体"}[Session Group Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile session-group]{lang="EN-US"}]{#struct_0_x1090_x8456_943620606}

[  Session-Group-Profile: aaa]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : Ethernet1/2/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[        QMProfile: a]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Session-Group-Profile: bbb]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_4:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[        IP address   : 172.16.187.166]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x171882063}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile slot 2]{lang="EN-US"}]{#struct_0_x1090_x8456_943358461}

[  User-Profile: aaa]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p2]{lang="EN-US"}

[    Connection-limit amount: 1000]{lang="EN-US"}

[    Connection-limit rate: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Inbound: Policy p1]{lang="EN-US"}

[        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[        Connection-limit rate: 100]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  User-Profile: bbb]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p3]{lang="EN-US"}

[      Connection-limit rate: 200]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_4:]{lang="EN-US"}

[    Authentication type: Portal]{lang="EN-US"}

[    Network attributes:]{lang="EN-US"}

[      Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[      IP address   : 172.16.187.166]{lang="EN-US"}

[      VPN          : N/A]{lang="EN-US"}

[      Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x721199051}[显示]{style="font-family:宋体"}[2]{lang="EN-US"}[号成员设备上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile session-group slot 2]{lang="EN-US"}]{#struct_0_x1090_x8456_x1429556673}

[  Session-Group-Profile: aaa]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : Ethernet1/2/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[        QMProfile: a]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Session-Group-Profile: bbb]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_4:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[        IP address   : 172.16.187.166]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_1217991923}[显示在]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile name aaa chassis 1 slot 2]{lang="EN-US"}]{#struct_0_x1090_x8456_170292427}

[  User-Profile: aaa]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p2]{lang="EN-US"}

[    Connection-limit amount: 1000]{lang="EN-US"}

[    Connection-limit rate: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Inbound: Policy p1 ]{lang="EN-US"}

[        Inbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[        Connection-limit rate: 100]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_1784804659}[显示在]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[2]{lang="EN-US"}[号单板上]{style="font-family:宋体"}[名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile session-group name aaa chassis 1 slot 2]{lang="EN-US"}]{#struct_0_x1090_x8456_170357963}

[  Session-Group-Profile: aaa]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    User user_1:]{lang="EN-US"}

[      Authentication type: 802.1X ]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[        MAC address  : 0000-1111-2222]{lang="EN-US"}

[      Failed action list:]{lang="EN-US"}

[        Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[        QMProfile: a]{lang="EN-US"}

[    User user_2:]{lang="EN-US"}

[      Authentication type: Portal]{lang="EN-US"}

[      Network attributes:]{lang="EN-US"}

[        Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[        IP address   : 172.16.187.16]{lang="EN-US"}

[        VPN          : N/A]{lang="EN-US"}

[        Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x977453894}[显示]{style="font-family:宋体"}[名称为]{style="font-family:宋体"}[bbb]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile name bbb]{lang="EN-US"}]{#struct_0_x1090_x8456_1735852083}

[  User-Profile: bbb]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p3]{lang="EN-US"}

[    Connection-limit rate: 200]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 2:]{lang="EN-US"}

[      User user_3:]{lang="EN-US"}

[        Authentication type: 802.1X]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[          MAC address  : 1111-2222-3333]{lang="EN-US"}

[        Failed action list:]{lang="EN-US"}

[          Connection-limit rate: 200]{lang="EN-US"}

[      User user_4:]{lang="EN-US"}

[        Authentication type: PPP]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_5:]{lang="EN-US"}

[        Authentication type: IPoE]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          MAC address  : 2222-3333-4444]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x1987510960}[显示指定]{style="font-family:宋体"}[名称为]{style="font-family:
宋体"}[bbb]{lang="EN-US"}[的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile session-group name bbb]{lang="EN-US"}]{#struct_0_x1090_x8456_x1356728505}

[  Session-Group-Profile: bbb]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 2:]{lang="EN-US"}

[      User user_3:]{lang="EN-US"}

[        Authentication type: 802.1X]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[          MAC address  : 1111-2222-3333]{lang="EN-US"}

[        Failed action list:]{lang="EN-US"}

[          Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[          QMProfile: a]{lang="EN-US"}

[      User user_4:]{lang="EN-US"}

[        Authentication type: PPP]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_5:]{lang="EN-US"}

[        Authentication type: IPoE]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          MAC address  : 2222-3333-4444]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x1561777281}[显示所有]{style="font-family:宋体"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile]{lang="EN-US"}]{#struct_0_x1090_x8456_1735589939}

[  User-Profile: aaa]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[    Connection-limit amount: 1000]{lang="EN-US"}

[    Connection-limit rate: 100]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 2:]{lang="EN-US"}

[      User user_1:]{lang="EN-US"}

[        Authentication type: 802.1X]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[          MAC address  : 0000-1111-2222]{lang="EN-US"}

[        Failed action list:]{lang="EN-US"}

[          Inbound: Policy p1]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_6:]{lang="EN-US"}

[        Authentication type: PPP]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[  User-Profile: bbb]{lang="EN-US"}

[    Inbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[      Policy: p3]{lang="EN-US"}

[    Connection-limit rate: 200]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_7:]{lang="EN-US"}

[        Authentication type: IPoE]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[          MAC address  : 0000-1111-2222]{lang="EN-US"}

[          IP address   : 172.16.187.166]{lang="EN-US"}

[          VPN          : N/A]{lang="EN-US"}

[          Service VLAN : 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x771078987}[显示所有]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[配置信息及被授权该]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的在线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display user-profile session-group]{lang="EN-US"}]{#struct_0_x1090_x8456_1735655475}

[  Session-Group-Profile: aaa]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 2:]{lang="EN-US"}

[      User user_1:]{lang="EN-US"}

[        Authentication type: 802.1X]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/1]{lang="EN-US"}

[          MAC address  : 0000-1111-2222]{lang="EN-US"}

[        Failed action list:]{lang="EN-US"}

[          Outbound: CIR 33 (kbps), CBS 2062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps) ]{lang="EN-US"}

[          QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_6:]{lang="EN-US"}

[        Authentication type: PPP]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Session-Group-Profile: bbb]{lang="EN-US"}

[    Outbound:]{lang="EN-US"}

[      CIR 512 (kbps), CBS 1062 (Bytes), EBS 0 (Bytes), PIR 888 (kbps)]{lang="EN-US"}

[    QMProfile: a]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Chassis 1 Slot 5:]{lang="EN-US"}

[      User user_7:]{lang="EN-US"}

[        Authentication type: IPoE]{lang="EN-US"}

[        Network attributes:]{lang="EN-US"}

[          Interface    : GigabitEthernet1/0/2]{lang="EN-US"}

[          MAC address  : 0000-1111-2222]{lang="EN-US"}

[          IP address   : 172.16.187.166]{lang="EN-US"}

[          VPN          : N/A]{lang="EN-US"}

[          Service VLAN : 100]{lang="EN-US"}

[]{#struct_0_x1090_x8456_x1354461343}[[表1-1 ]{lang="EN-US"}[表]{style="font-family:
黑体"}[1-1 ]{lang="EN-US"}]{#_Ref298418812}[display user-profile ]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x844140864}[[字段]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x1186153287}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1090_x8456_2015243558}

[[User-Profile ]{lang="EN-US"}]{#struct_0_x1090_x8456_899259022}

[[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_x28151309}[名称]{style="font-family:宋体"}

[[Inbound]{lang="EN-US"}]{#struct_0_x1090_x8456_1149685196}

[[在入方向上应用的策略]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x1086986806}

[[Outbound]{lang="EN-US"}]{#struct_0_x1090_x8456_1735458867}

[[在出方向上应用的策略]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x28722836}

[[Session-Group-Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_1217926387}

[[Session Group Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_649325884}[名称]{style="font-family:宋体"}

[[CIR]{lang="EN-US"}]{#struct_0_x1090_x8456_x2093836782}

[[承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x1090_x8456_x1099389388}

[[CBS]{lang="EN-US"}]{#struct_0_x1090_x8456_593377783}

[[承诺突发尺寸，也就是容纳突发流量的令牌桶深度，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_x1090_x8456_684238576}

[[EBS]{lang="EN-US"}]{#struct_0_x1090_x8456_2033174499}

[[超出突发尺寸，在双令牌桶算法中超出突发流量超过承诺突发流量的部分，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_x1090_x8456_x47368748}

[[PIR]{lang="EN-US"}]{#struct_0_x1090_x8456_x2113386032}

[[峰值信息速率]{style="font-family:宋体"}]{#struct_0_x1090_x8456_1218385139}

[[Connection-limit amount]{lang="EN-US"}]{#struct_0_x1090_x8456_x359242980}

[[用户最大连接数]{style="font-family:宋体"}]{#struct_0_x1090_x8456_63309993}

[[Connection-limit rate]{lang="EN-US"}]{#struct_0_x1090_x8456_x353880899}

[[用户最大连接速率]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x652938476}

[[Policy]{lang="EN-US"}]{#struct_0_x1090_x8456_x372336702}

[[策略名]{style="font-family:宋体"}]{#struct_0_x1090_x8456_965983680}

[[QMProfile]{lang="EN-US"}]{#struct_0_x1090_x8456_x4618242}

[[队列调度策略]{style="font-family:宋体"}]{#struct_0_x1090_x8456_1688278263}

[[User user_1]{lang="EN-US"}]{#struct_0_x1090_x8456_1735524403}

[[与]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_x407551477}[或]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[关联的用户信息]{style="font-family:宋体"}

[[Authentication type]{lang="EN-US"}]{#struct_0_x1090_x8456_1218319603}

[[用户认证类型]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x1504561787}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[802.1X]{lang="EN-US"}]{#struct_0_x1090_x8456_511189026}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Portal]{lang="EN-US"}]{#struct_0_x1090_x8456_1692463799}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPP]{lang="EN-US"}]{#struct_0_x1090_x8456_1229322848}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPoE]{lang="EN-US"}]{#struct_0_x1090_x8456_x384099019}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACA]{lang="EN-US"}]{#struct_0_x1090_x8456_247337928}

[[Network attributes]{lang="EN-US"}]{#struct_0_x1090_x8456_1217860852}

[[用户特征信息]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x566950880}

[[Failed action list]{lang="EN-US"}]{#struct_0_x1090_x8456_136330660}

[[在该用户上应用失败的动作]{style="font-family:宋体"}]{#struct_0_x1090_x8456_136789412}

[ ]{lang="EN-US"}

::: {#1603098714 .myid}
[]{#_Toc404792855}[]{#struct_0_x1090_x8456_1683562928}

**User Profile \-- User Profile配置命令 \-- qos queue**

------------------------------------------------------------------------

[**[qos queue]{lang="EN-US"}**]{#struct_0_x1090_x8456_1908968858}[命令用来在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[中为会话指定进入的队列。]{style="font-family:宋体"}

[**[undo qos queue]{lang="EN-US"}**]{#struct_0_x1090_x8456_x1271543904}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1089679106}

[**[qos queue ]{lang="EN-US"}**[{ *queue-id* \| *queue-name* }]{lang="EN-US"}]{#struct_0_x1090_x8456_x82163981}

[**[undo qos queue]{lang="EN-US"}**]{#struct_0_x1090_x8456_2008423180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_461415242}

[[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_475399820}[下没有指定进入的队列。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_593539996}

[[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_154023037}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_349979674}

[[network-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_x658753144}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_1217795316}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x940350826}

[**[queue ]{lang="EN-US"}**[{ ]{lang="EN-US"}*[queue-id ]{lang="EN-US"}*[\| *queue-name* }]{lang="EN-US"}]{#struct_0_x1090_x8456_1936527599}[：让应用此]{style="font-family:宋体"}[user profile]{lang="EN-US"}[的会话进入指定队列，]{style="font-family:宋体"}*[queue-id]{lang="EN-US"}*[表示队列序号，]{style="font-family:宋体"}*[queue-name]{lang="EN-US"}*[表示队列名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_781760176}

[[若指定进入的队列对应的是四队列调度策略，则可以配置的队列序号范围是]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1090_x8456_1736441907}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，超出范围则配置失败，不会进入指定队列。]{style="font-family:宋体"}

[[应用此命令可以为对多个会话指定不同的队列从而决定其不同优先级的调度方式。]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x1026000821}

[*[queue-id]{lang="EN-US"}*]{#struct_0_x1090_x8456_1735852084}[和]{style="font-family:宋体"}*[queue-name]{lang="EN-US"}*[的对应情况如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-2]{lang="EN-US"}](?1603098714#_Ref386643034)[所示。]{style="font-family:
宋体"}

[]{#struct_0_x1090_x8456_x1987576496}[[表1-2 ]{lang="EN-US"}*[queue-id]{lang="EN-US"}*]{#_Ref386643034}[数字和关键字对应表]{style="font-family:黑体"}

[]{#table_struct_0_510564096}[*[queue-id]{lang="EN-US" style="font-size:10.0pt"}*]{#struct_0_x1090_x8456_x28554354}[数字]{style="font-size:10.0pt;font-family:黑体"}
:::

[*[queue-id]{lang="EN-US" style="font-size:10.0pt"}*]{#struct_0_x1090_x8456_x1129066444}[关键字]{style="font-size:10.0pt;
   font-family:黑体"}

[[0]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735917620}

[[be]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x1593264604}

[[1]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_x1090_x8456_707445233}

[[af1]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735721012}

[[2]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x1575575523}

[[af2]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1612547535}

[[3]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735786548}

[[af3]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x1562236033}

[[4]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735589940}

[[af4]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x770620240}

[[5]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x1113128252}

[[ef]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735655476}

[[6]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1149619660}

[[cs6]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_x732996351}

[[7]{lang="EN-US" style="font-size:
  10.0pt"}]{#struct_0_x1090_x8456_1735458868}

[[cs7]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_x1090_x8456_x28788372}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1431775810}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x1311846988}[在名称为]{style="font-family:宋体"}[user]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[中，指定会话进入队列]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1090_x8456_247609926}

[\[Sysname\] user-profile user]{lang="EN-US"}

[\[Sysname-user-profile-user\] qos queue 7]{lang="EN-US"}

::: {#-1196132117 .myid}
[]{#_Toc404792856}[]{#struct_0_x1090_x8456_2003308313}

**User Profile \-- User Profile配置命令 \-- qos session-group identify**

------------------------------------------------------------------------

[**[qos session-group identify]{lang="EN-US"}**]{#struct_0_x1090_x8456_x1858618467}[命令用来在接口下配置会话组识别方式。]{style="font-family:
宋体"}

[**[undo qos session-group identify]{lang="EN-US"}**]{#struct_0_x1090_x8456_1762542420}[命令用来取消会话组识别方式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x1373160352}

[**[qos session-group identify ]{lang="EN-US"}**[{ **customer-vlan** \| **service-vlan** \| **customer-service-vlan \| subscriber-id** }]{lang="EN-US"}]{#struct_0_x1090_x8456_1658401013}

[**[undo qos session-group identify ]{lang="EN-US"}**]{#struct_0_x1090_x8456_1217729780}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_644101369}

[[接口下没有配置会话组识别方式。]{style="font-family:宋体"}]{#struct_0_x1090_x8456_571191743}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x1431541835}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x1561242495}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1257034171}

[[network-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_1271550634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_159528035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x2134681357}

[**[customer-vlan]{lang="EN-US"}**]{#struct_0_x1090_x8456_x1643208704}[：按内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[识别会话组，内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为用户的私网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-vlan]{lang="EN-US"}**]{#struct_0_x1090_x8456_1333304519}[：按外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[识别会话组，外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为运营商分配给用户的公网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[customer-service-vlan]{lang="EN-US"}**]{#struct_0_x1090_x8456_1570390739}[：按内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[识别会话组。]{style="font-family:宋体"}

[**[subscriber-id]{lang="EN-US"}**]{#struct_0_x1090_x8456_585774374}[：按]{style="font-family:宋体"}[subscriber id]{lang="EN-US"}[识别会话组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x811223329}

[[若要配置]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_1217664244}[，则必须首先指定会话组的识别方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x153168053}

[[\#]{lang="EN-US"}]{#struct_0_x1090_x8456_1387960027}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置基于外层]{style="font-family:宋体"}[vlan]{lang="EN-US"}[的会话组识别方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1090_x8456_x1046841783}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos session-group identify service-vlan]{lang="EN-US"}
:::

::: {#1744588217 .myid}
[]{#_Toc404792857}[]{#struct_0_x1090_x8456_2126197597}[]{#_Toc361324560}[]{#_Toc206560160}

**User Profile \-- User Profile配置命令 \-- user-profile**

------------------------------------------------------------------------

[**[user-profile]{lang="EN-US"}**]{#struct_0_x1090_x8456_116896362}[命令用来创建]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[或]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[并进入相应的视图]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **user-profile**]{lang="EN-US"}]{#struct_0_x1090_x8456_x1758547852}[命令用来删除指定的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_737807289}

[**[user-profile]{lang="EN-US"}**[ *profile-name* \[ **type session-group** \]]{lang="EN-US"}]{#struct_0_x1090_x8456_x643365698}

[**[undo user-profile]{lang="EN-US"}**[ *profile-name*]{lang="EN-US"}]{#struct_0_x1090_x8456_311538482}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x1650864468}

[[不存在任何]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_x300102334}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x104200280}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1090_x8456_x602017608}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1218122996}

[[network-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_431889353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1090_x8456_x532901656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1432055383}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x1090_x8456_x1868182004}[：表示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含英文字母]{style="font-family:宋体"}[\[a-z,A-Z\]]{lang="EN-US"}[、数字、下划线，且必须以英文字母开始，区分大小写。]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称必须全局唯一。]{style="font-family:宋体"}

[**[type session-group]{lang="EN-US"}**]{#struct_0_x1090_x8456_1735852085}[：指定创建的类型为]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_x12353514}

[[如果指定名称的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_x1922129044}[或]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[已存在，则直接进入该]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[或]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[的视图。]{style="font-family:宋体"}

[[User Profile]{lang="EN-US"}]{#struct_0_x1090_x8456_x1987642032}[的名称必须全局唯一。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1090_x8456_1499480786}

[[\# ]{lang="EN-US"}]{#struct_0_x1090_x8456_x1827252175}[创建名称为]{style="font-family:宋体"}[a123]{lang="EN-US"}[的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1090_x8456_x1954033107}

[\[Sysname\] user-profile a123]{lang="EN-US"}

[\[Sysname-user-profile-a123\]]{lang="EN-US"}[]{#_Toc166647677}

[[\# ]{lang="PT-BR"}]{#struct_0_x1090_x8456_x1168887730}[创建名称为]{style="font-family:宋体"}[a123]{lang="PT-BR"}[的]{style="font-family:宋体"}[Session Group Profile]{lang="PT-BR"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1090_x8456_1218057460}

[\[Sysname\] user-profile a123 type session-group]{lang="PT-BR"}

[\[Sysname-session-group-profile-a123\]]{lang="PT-BR"}
:::
