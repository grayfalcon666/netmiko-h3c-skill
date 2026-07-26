
**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security accounting-start-fail offline**

------------------------------------------------------------------------

**[client-security accounting-start-fail offline**]命令用来开启计费请求失败用户下线功能，即计费开始请求发送失败后，强制用户下线。

**[undo client-security accounting-start-fail offline**]命令用来恢复缺省情况。

【命令】

**[client-security accounting-start-fail offline**]

**[undo client-security accounting-start-fail offline**]

【缺省情况】

计费开始请求发送失败后，用户保持在线。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

【举例】

\# 在无线服务模板service1下开启计费请求失败用户下线功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security accounting-start-fail offline

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authentication fail-vlan**

------------------------------------------------------------------------

**[client-security authentication fail-vlan**]命令用来配置指定服务模板下的认证失败VLAN。

**[undo client-security authentication fail-vlan**]命令用来恢复缺省情况。

【命令】

**[client-security authentication fail-vlan** *vlan-id*]

**[undo client-security authentication fail-vlan**]

【缺省情况】

没有配置认证失败VLAN。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[vlan-id*]：认证失败VLAN的VLAN ID，取值范围为1～4094。

【使用指导】

该配置为服务模板下的配置，只能在服务模板去使能的状态下进行配置。

这里的认证失败是认证服务器因某种原因明确拒绝用户认证通过，比如用户密码错误，而不是认证超时或网络连接等原因造成的认证失败。

如果配置了认证失败VLAN，则认证失败的用户将被加入该VLAN，同时设备会启动一个30秒的定时器，定期对用户进行重新认证：

·如果是802.1X认证用户，设备将向用户发送单播EAP-Request/Identity报文进行重新认证。另外，802.1X用户也可以主动再次发起认证。

·如果是MAC地址认证用户，设备将直接向认证服务器发起重新认证。

如果用户重认证通过，则设备将根据认证服务器或设备是否给用户下发VLAN来重新指定该用户所在VLAN：如果认证服务器或设备给用户下发了VLAN，则用户将被加入该下发的VLAN，否则用户将被加入初始VLAN；如果用户重认证仍然失败，则用户仍然留在认证失败VLAN中。

【举例】

\# 在无线服务模板1下配置认证失败VLAN为VLAN 10。

\<Sysname\> sysname-view

Sysname wlan service-template 1

Sysname-wlan-st-1 client-security authentication fail-vlan 10

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authentication-mode**

------------------------------------------------------------------------

**[client-security authentication-mode**]命令用来配置无线用户接入认证模式。

**[undo client-security authentication-mode**]命令用来恢复缺省情况。

【命令】

**[client-security authentication-mode**[ { **dot1x** \| **dot1x-then-mac** \| **mac** \| **mac-then-dot1x** \| **oui-then-dot1x** }]]

**[undo client-security authentication-mode**]

【缺省情况】

不对用户进行认证即Bypass认证，直接接入。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dot1x**]：表示只进行802.1X认证。

**[dot1x-then-mac**]：表示先进行802.1X认证，如果失败，再进行MAC地址认证。如果认证成功，则不进行MAC地址认证。

**[mac**]：表示只进行MAC地址认证。

**[mac-then-dot1x**]：表示先进行MAC地址认证，如果失败，再进行802.1X认证。如果认证成功，则不进行802.1X认证。

**[oui-then-dot1x**]：表示先进行OUI认证，如果失败，再进行802.1X认证。如果认证成功，则不进行802.1X认证。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

以上各模式下，每个无线服务模板上均允许接入多个认证通过的用户。802.1X用户的数目由**dot1x max-user**命令配置，MAC地址认证用户的数目由**mac-authentication max-user**命令配置。

【举例】

\# 在无线服务模板service1下配置无线用户接入认证模式为MAC地址认证模式。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security authentication-mode mac

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authorization-fail offline**

------------------------------------------------------------------------

**[client-security authorization-fail offline**]命令用来开启授权失败后的用户下线功能，即授权信息下发失败后，强制用户下线。

**[undo client-security authorization-fail offline**]命令用来恢复缺省情况。

【命令】

**[client-security authorization-fail offline**]

**[undo client-security authorization-fail offline**]

【缺省情况】

设置授权信息下发失败后，用户保持在线。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

如果开启了授权失败后的用户下线功能，当下发的授权ACL、User Profile不存在、已授权ACL、User Profile被删除，或者ACL、User Profile下发失败时，将强制用户下线；

如果没有开启授权失败后的用户下线功能，当下发的授权ACL、User Profile不存在、已授权ACL、User Profile被删除，或者ACL、User Profile下发失败时，用户保持在线，授权ACL、User Profile不生效，设备打印Log信息。

【举例】

\# 在无线服务模板service1下开启授权失败用户下线功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security authorization-fail offline

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security ignore-authorization**

------------------------------------------------------------------------

**[client-security ignore-authorization**]命令用来配置忽略RADIUS服务器或设备本地下发的授权信息。

**[undo client-security** **ignore-authorization**]命令用来恢复缺省情况。

【命令】

**[client-security ignore-authorization**]

**[undo client-security ignore-authorization**]

【缺省情况】

应用RADIUS服务器或设备本地下发的授权信息。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

当用户通过RADIUS认证或本地认证后，RADIUS服务器或设备会根据用户帐号配置的相关属性进行授权，比如动态下发VLAN等。若不希望接受这类动态下发的授权属性，则可通过配置本命令来忽略。

【举例】

\# 在无线服务模板service1下配置忽略RADIUS服务器或设备本地下发的授权信息。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security ignore-authorization

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection action**

------------------------------------------------------------------------

**[client-security** **intrusion-protection action**]命令用来配置当接收到非法报文时采取的入侵保护措施。

**[undo client-security** **intrusion-protection action**]命令用来恢复缺省情况。

【命令】

**[client-security intrusion-protection action**[ { **service-stop** \| **temporary-block** \| **temporary-service-stop** }]]

**[undo client-security intrusion-protection action**]

【缺省情况】

默认入侵检测模式为临时将用户MAC加入阻塞MAC列表中，即源MAC地址为此非法MAC地址的用户将不能和AP建立连接。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-stop**]：直接关闭收到非法报文的BSS提供的所有服务。

**[temporary-block**]：临时将用户MAC加入阻塞MAC列表中。

**[temporary-service-stop**]：临时将收到非法报文的BSS所提供的所有服务关闭。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

只有开启入侵保护功能后，入侵保护措施才生效。开启入侵保护功能由**client-security intrusion-protection enable**命令配置。

临时阻止非法用户上线的时间由**client-security intrusion-protection timer temporary-block**命令配置。

临时关闭收到非法报文的BSS所提供服务的时间由**client-security intrusion-protection timer temporary-service-stop**命令配置。

用户所属BSS提供的服务已关闭的情况下，用户可以手工在Radio口上重新生成该BSS使得用户正常接入。

【举例】

\# 在无线服务模板service1下配置入侵保护措施为**service-stop**。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security intrusion-protection enable

Sysname-wlan-st-service1 client-security intrusion-protection action service-stop

【相关命令】

·**client-security intrusion-protection enable**

·**client-security intrusion-protection temporary-block timer**

·**client-security intrusion-protection temporary-service-stop timer**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection enable**

------------------------------------------------------------------------

**[client-security intrusion-protection enable**]命令用来开启入侵保护功能。

**[undo client-security intrusion-protection enable**]命令用来恢复缺省情况。

【命令】

**[client-security intrusion-protection enable**]

**[undo client-security intrusion-protection enable**]

【缺省情况】

入侵保护功能处于关闭状态。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

当设备检测到一个认证失败的用户试图通过该无线服务模板绑定的BSS（基本服务集）接入时，如果入侵保护功能处于开启状态，则设备将对其所在的BSS采取相应的安全措施。具体的安全措施由**client-security** **intrusion-protection action**命令指定。

【举例】

\# 在无线服务模板service1下开启入侵保护功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security intrusion-protection enable

【相关命令】

·**client-security** **intrusion-protection action**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection timer temporary-block**

------------------------------------------------------------------------

**[client-security intrusion-protection timer temporary-block**]命令用来配置临时阻塞非法入侵用户的时长。

**[undo client-security intrusion-protection timer temporary-block**]命令用来恢复缺省情况。

【命令】

**[client-security intrusion-protection timer temporary-block** *value*]

**[undo client-security intrusion-protection timer temporary-block**]

【缺省情况】

临时阻塞非法入侵用户时间为180秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：阻塞非法入侵用户时长，取值范围为60～300，单位为秒。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

当入侵检测功能处于使能状态且入侵保护措施为临时阻塞非法用户（**temporary-block**）时，如果用户认证失败，则在该配置所指定的时间范围内，源MAC地址为此非法MAC地址的用户将无法认证成功，在这段时间之后恢复正常。

【举例】

\# 在无线服务模板service1下配置临时阻塞非法入侵用户时长为120秒。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security intrusion-protection enable

Sysname-wlan-st-service1 client-security intrusion-protection action temporary-block

Sysname-wlan-st-service1 client-security intrusion-protection temporary-block timer 120

【相关命令】

·**client-security intrusion-protection enable**

·**client-security intrusion-protection action**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection timer temporary-service-stop**

------------------------------------------------------------------------

**[client-security intrusion-protection timer temporary-service-stop**]命令用来配置临时关闭BSS服务的时长。

**[undo client-security intrusion-protection timer temporary-service-stop**]命令用来恢复缺省情况。

【命令】

**[client-security intrusion-protection timer******temporary-service-stop ***value *]

**[undo client-security intrusion-protection timer temporary-service-stop**]

【缺省情况】

临时关闭BSS服务时长为20秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：无线服务临时关闭时长，取值范围为10～300，单位为秒。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

当入侵保护功能处于使能状态，且入侵保护措施为临时关闭服务（**temporary-service-stop**）时，如果设备检测到非法报文，则在该配置指定的时间段内关闭用户所在的BSS所提供的所有服务，在此期间用户将无法通过该服务接入网络，这段时间之后恢复正常。

【举例】

\# 在无线服务模板service1下配置临时关闭BSS服务的时长为30秒。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 client-security intrusion-protection enable

Sysname-wlan-st-service1 client-security intrusion-protection action temporary-service-stop

Sysname-wlan-st-service1 client-security intrusion-protection temporary-service-stop timer 30

【相关命令】

·**client-security intrusion-protection enable**

·**client-security intrusion-protection action**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- display wlan client-security block-mac （仅AC）**

------------------------------------------------------------------------

!(WLAN用户接入认证命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display wlan client-security block-mac**]命令用来显示阻塞MAC地址信息。

【命令】

**[display wlan client-security block-mac** [ **ap** *ap-name* [ **radio** *radio-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap** *ap-name*]：显示接入指定AP的所有阻塞MAC地址信息，*ap-name*表示AP的名称，为1～63个字符的字符串，不区分大小写。如果未指定本参数，则显示所有阻塞MAC地址信息。

**[radio** *radio-id*]：显示接入指定Radio的所有阻塞MAC地址信息，*radio-id*表示Radio编号，取值范围与设备型号有关。如果未指定本参数，则显示AP下所有Radio下的阻塞MAC地址信息。

【使用指导】

阻塞MAC是指入侵检测模式为**temporary-block**时，被加入到阻塞MAC列表中的用户。

【举例】

\# 显示所有阻塞 MAC地址信息。

\<Sysname\> display wlan client-security block mac-address

MAC address         AP ID       RADIO ID     BSSID

0002-0002-0002      1           1            00AB-0DE1-0001

000d-88f8-0577      1           1            0EF1-0001-02C1

Total entries: 2

表1-1 display wlan client-security block mac-address命令显示信息描述表

字段

描述

MAC address

阻塞MAC地址，格式为"H-H-H"

AP ID

阻塞MAC地址所在AP的编号

RADIO ID

阻塞MAC地址所在的Radio编号

BSSID

基本服务集标识符，格式为H-H-H

Total entries

阻塞MAC地址表项条数

【相关命令】

·**client-security instrusion-protection action**

·**client-security instrusion-protection timer temporary-block**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- display wlan client-security block-mac（仅FAT AP）**

------------------------------------------------------------------------

!(WLAN用户接入认证命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display wlan client-security block-mac**]命令用来显示阻塞MAC地址信息。

【命令】

**[display wlan client-security block-mac**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【使用指导】

阻塞MAC是指入侵检测模式为**temporary-block**时，被加入到阻塞MAC列表中的用户。

【举例】

\# 显示所有阻塞 MAC地址信息。

\<Sysname\> display wlan client-security block mac-address

MAC address         AP ID       RADIO ID     BSSID

0002-0002-0002      1           1            00AB-0DE1-0001

000d-88f8-0577      1           1            0EF1-0001-02C1

Total entries: 2

表1-2 display wlan client-security block mac-address命令显示信息描述表

字段

描述

MAC address

阻塞MAC地址，格式为"H-H-H"

AP ID

阻塞MAC地址所在AP的编号

RADIO ID

阻塞MAC地址所在的Radio编号

BSSID

基本服务集标识符，格式为H-H-H

Total entries

阻塞MAC地址表项条数

【相关命令】

·**client-security instrusion-protection action**

·**client-security instrusion-protection timer temporary-block**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x domain**

------------------------------------------------------------------------

**[dot1x domain**]命令用来指定无线服务模板下802.1X用户的认证域。

**[undo dot1x domain**]命令用来删除该无线服务模板下802.1X用户的认证域。

【命令】

**[dot1x domain** *domain-name*]

**[undo dot1x domain**]

【缺省情况】

未指定无线服务模板下的802.1X用户的认证域。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ISP域名，为1～255个字符的字符串，不区分大小写。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

从无线服务模板上接入的802.1X用户将按照如下先后顺序进行选择认证域：无线服务模板下指定的认证域\--\>用户名中指定的认证域\--\>系统缺省的认证域。

【举例】

\# 配置无线服务模板service1下802.1X用户使用认证域为my-domain。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 dot1x domain my-domain

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x handshake enable**

------------------------------------------------------------------------

**[dot1x handshake enable**]命令用来使能指定无线服务模板下的802.1X在线用户握手功能。

**[undo dot1x handshake enable**]命令用来恢复缺省情况。

【命令】

**[dot1x handshake enable**]

**[undo dot1x handshake enable**]

【缺省情况】

无线服务模板下的802.1X在线用户握手功能处于关闭状态，即不与802.1X在线用户进行握手。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

该命令只对进行802.1X接入认证且成功上线的用户有效。

使能802.1X握手功能之后，设备将定期向通过802.1X认证的在线用户发送握手报文，即单播EAP-Request/Identity报文，来检测用户的在线状态。握手报文发送的时间间隔由802.1X握手定时器控制（时间间隔通过命令**dot1x timer handshake-period**设置）。如果连续发送握手报文的次数达到802.1X报文最大重发次数，而还没有收到用户响应，则强制该用户下线。

【举例】

\# 在无线服务模板service1下使能802.1X握手功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 dot1x handshake enable

【相关命令】

·**dot1x handshake secure****enable**

·**dot1x retry**

·**dot1x timer handshake-period**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x handshake secure enable**

------------------------------------------------------------------------

**[dot1x handshake secure enable**]命令用来使能802.1X的在线用户的安全握手功能。

**[undo dot1x handshake secure enable**]命令用来恢复缺省情况。

【命令】

**[dot1x handshake secure enable**]

**[undo dot1x handshake secure enable**]

【缺省情况】

802.1X的在线用户的安全握手功能处于关闭状态，即不对802.1X在线用户进行安全握手检查。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

802.1X安全握手功能只有在开启了802.1X握手功能的前提下才生效。

该命令只对进行802.1X接入认证且成功上线的用户有效。

802.1X安全握手是指在握手报文中加入验证信息，以防止非法用户仿冒正常用户在线的802.1X的客户端与设备进行握手报文的交互。使能802.1X安全握手功能后，支持安全握手的客户端需要在每次向设备发送的握手应答报文中携带验证信息，设备将其与认证服务器下发的验证信息进行对比，如果不一致，则强制用户下线。

验证信息由认证服务器下发，当用户上线认证成功时，服务器在认证回复报文中携带验证密钥和验证信息。设备保存验证信息，而将验证密钥通过发送给客户端。之后，当用户需要响应设备的握手报文时，首先使用验证密钥计算出一个验证信息，然后将该验证信息携带在握手回应报文EAPOL EAP-Response Identity中发给设备。

服务器会周期性地更新验证密钥与验证信息，并通过计费响应报文下发给设备。设备同样会将验证密钥发送给客户端，而保存验证信息用于校验客户端响应报文的合法性。

【举例】

\# 在无线服务模板service1下使能802.1X安全握手功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 dot1x handshake enable

Sysname-wlan-st-service1 dot1x handshake secure enable

【相关命令】

·**dot1x handshake enable**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x max-user**

------------------------------------------------------------------------

**[dot1x max-user**]命令用来配置无线服务模板上的802.1X最大用户数。当接入此无线服务模板的802.1X用户数超过最大值后，新的用户将被拒绝。

**[undo dot1x max-user**]命令用来恢复缺省情况。

【命令】

**[dot1x max-user*** count*]

**[undo dot1x max-user**]

【缺省情况】

当前无线服务模板上允许同时接入的802.1X用户数为4096个。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：无线服务模板上最多允许同时接入的802.1X用户数，取值范围为1～4096。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

【举例】

\# 配置无线服务模板service1上的802.1X最大用户数为500。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 dot1x max-user 500

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x re-authenticate enable**

------------------------------------------------------------------------

**[dot1x re-authenticate enable**]命令用来开启无线服务模板上的802.1X周期性重认证功能。

**[undo dot1x re-authenticate enable**]命令用来关闭无线服务模板上的802.1X周期性重认证功能。

【命令】

**[dot1x re-authenticate enable**]

**[undo dot1x re-authenticate enable**]

【缺省情况】

无线服务模板上的802.1X周期性重认证功能处于关闭状态。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

无线服务模板启动了802.1X的周期性重认证功能后，设备会根据系统视图下配置的周期性重认证定时器（**dot1x timer reauth-period**）时间间隔对在线802.1X用户启动认证，以检测用户连接状态的变化，更新服务器下发的授权属性（例如ACL，VLAN，User Profile）。

用户进行802.1X认证成功后，如果服务器下发了Termination action和Session timeout属性，且Termination action取值为Radius-Request，Session timeout取值不为0，设备将以Session timeout为周期对用户进行重认证，以检测用户在线状态，并更新授权信息。

在认证服务器没有下发Terminal action和Session timeout属性或下发的Terminal action取值不为Request的情况下，如果使能802.1X重认证功能，设备也会定期向已经在线的802.1X用户发起重认证，此时重认证周期由802.1X重认证定时器配置。

【举例】

\# 在无线服务模板service1上开启802.1X重认证功能。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 dot1x re-authenticate enable

【相关命令】

·**dot1x timer**

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- mac-authentication domain**

------------------------------------------------------------------------

**[mac-authentication domain**]命令用来指定无线服务模板下MAC地址认证用户的认证域。

**[undo mac-authentication domain**]命令用来删除该无线服务模板下的MAC地址认证用户的认证域。

【命令】

**[mac-authentication domain** *domain-name*]

**[undo mac-authentication domain**]

【缺省情况】

未指定无线服务模板下的MAC地址认证用户的认证域。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[domain-name*]：ISP域名，为1\~255个字符的字符串，不区分大小写。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

从无线服务模板上接入的MAC地址认证用户将按照如下先后顺序进行选择认证域：无线服务模板下指定的认证域\--\>全局MAC地址认证域\--\>系统缺省的认证域。

【举例】

\# 配置无线服务模板service1下MAC地址认证用户使用的认证域为my-domain。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 mac-authentication domain my-domain

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- mac-authentication max-user**

------------------------------------------------------------------------

**[mac-authentication max-user**]命令用来配置无线服务模板上的MAC地址认证最大用户数。当接入此无线服务模板的MAC地址认证用户数超过最大值后，新接入的用户将被拒绝。

**[undo mac-authentication max-user**]命令用来恢复缺省情况。

【命令】

**[mac-authentication max-user** *count*]

**[undo mac-authentication max-user**]

【缺省情况】

当前无线服务模板上允许同时接入的MAC地址认证用户数为4096个。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：可接入无线服务模板的MAC地址认证用户个数，取值范围为1～4096。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。

【举例】

\# 配置最大接入MAC地址认证用户数为32个。

\<Sysname\> system-view

Sysname wlan service-template service1

Sysname-wlan-st-service1 mac-authentication max-user 32
