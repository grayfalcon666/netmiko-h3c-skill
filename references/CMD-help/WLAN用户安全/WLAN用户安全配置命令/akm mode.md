
**WLAN用户安全 \-- WLAN用户安全配置命令 \-- akm mode**

------------------------------------------------------------------------

**[akm mode**]命令用来配置身份认证与密钥管理。

**[undo akm mode**]命令用来恢复缺省情况。

【命令】

**[akm mode**[ { **dot1x** \| **psk** }]]

**[undo akm mode**]

【缺省情况】

未配置身份认证与密钥管理。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dot1x**]：表示身份认证与密钥管理的模式是802.1X模式。

**[psk**]：表示身份认证与密钥管理的模式是PSK模式。

【使用指导】

·该命令只能在无线服务模板处于关闭的状态下进行配置，并且802.1X和PSK两种模式不能同时存在。

·802.1X模式和802.1X用户认证模式相互依赖，必须同时配置。有关802.1X的详细介绍请参见"WLAN配置指导"中的"WLAN用户接入认证"。

·PSK模式和MAC地址认证模式或Bypass用户认证模式相互依赖，必须同时配置。有关MAC地址认证和Bypass认证的详细介绍请参见"WLAN配置指导"中的"WLAN用户接入认证"。

·若配置了身份认证与密钥管理，则安全IE和加密套件必须配置。

【举例】

\# 配置身份认证与密钥管理模式为PSK模式。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security akm mode psk

【相关命令】

·**cipher-suite**

·**security-ie**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- cipher-suite**

------------------------------------------------------------------------

**[cipher-suite**]命令用来配置在帧加密时使用的加密套件。

**[undo cipher-suite**]命令用来禁用选择的加密套件。

【命令】

**[cipher-suite **[{ **ccmp \| tkip \| wep40 \| wep104 \| wep128** }]]

**[undo cipher-suite **[{ **ccmp \| tkip \| wep40 \| wep104 \| wep128** }]]

【缺省情况】

未配置加密套件。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ccmp**]：AES-CCMP加密套件。

**[tkip**]：TKIP加密套件。

**[wep40**]：WEP40加密套件。

**[wep104**]：WEP104加密套件。

**[wep128**]：WEP128加密套件。

【使用指导】

·该命令只能在无线服务模板处于关闭的状态下进行配置。

·如果配置了安全IE，则必须配置TKIP或者CCMP加密套件中的一种。

·WEP加密套件只能配置WEP40/WEP104/WEP128其中的一种，且需要配置与加密套件种类相对应的WEP密钥及WEP密钥ID。

·若配置了加密套件，则身份认证与密钥管理和安全IE则必须配置。

·WEP128和CCMP或TKIP不能同时配置。

【举例】

\# 配置TKIP加密套件。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security cipher-suite tkip

【相关命令】

·**security-ie**

·**wep key**

·**wep key-id**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey client-offline enable**

------------------------------------------------------------------------

**[gtk-rekey client-offline enable**]命令用来启动当无线客户端离线时更新GTK的功能。

**[undo gtk-rekey client-offline enable**]命令用来关闭无线客户端离线更新GTK的功能。

【命令】

**[gtk-rekey client-offline enable**]

**[undo gtk-rekey client-offline enable**]

【缺省情况】

无线客户端离线更新GTK功能关闭。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有开启了GTK更新功能，无线客户端离线时更新GTK的功能才能生效。

【举例】

\# 开启无线客户端时更新GTK功能。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security gtk-rekey client-offline enable

【相关命令】

·**gtk-rekey enable**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey enable**

------------------------------------------------------------------------

**[gtk-rekey enable**]命令用来开启更新GTK的功能。

**[undo gtk-rekey enable**]命令用来关闭更新GTK的功能。

【命令】

**[gtk-rekey enable**]

**[undo gtk-rekey enable**]

【缺省情况】

GTK更新功能处于开启状态。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启更新GTK功能。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security gtk-rekey enable

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- gtk-rekey method**

------------------------------------------------------------------------

**[gtk-rekey method**]命令用来配置GTK更新方法。

**[undo gtk-rekey method**]命令用来恢复缺省情况。

【命令】

**[gtk-rekey method** { **packet-based** [ *packet*  \| **time-based**  *time*  }]]

**[undo gtk-rekey method**]

【缺省情况】

GTK更新采用基于时间的方法，时间间隔为86400秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[packet-based**]：表示基于数据包的更新方法。

*[packet*]：指定传输的数据包（包括组播和广播）的数目，在传送指定数目的数据包（包括组播和广播）后更新GTK，取值范围为5000～4294967295。如果未指定本参数，则表示传输10000000个报文后进行密钥更新。

**[time-based**]：表示基于时间的GTK更新方法。

*[time*]：指定GTK密钥更新的周期。取值范围为180～604800，单位为秒。如果未指定本参数，则表示时间间隔是86400秒。

【使用指导】

·只有开启了GTK更新功能，GTK更新方法才能生效。

·使用该命令配置GTK密钥更新方法，新配置的方法会覆盖前一次的配置。例如，如果先配置了基于数据包的方法，然后又配置了基于时间的方法，则最后生效的是基于时间的方法。

·若该命令在无线服务模板处于开启状态下配置，则分为以下几种情况：

¡基于时间的GTK的更新方式不改变，只改变时间值，则该配置在重新创建定时器后生效；

¡基于报文数的GTK更新方式不改变，只改变报文数值，则该新的配置立即生效；

¡更新方式由基于时间更新改为基于报文数更新，则删除GTK更新定时器，在组播或广播报文数大于配置的数目值之后立即生效；

¡更新方式由基于报文数更新改为基于时间更新，则GTK不再基于报文数目更新，而是创建GTK更新定时器，定时器超时之后更新GTK。

【举例】

\# 配置基于时间的GTK更新方法。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security gtk-rekey method time-based 3600

\# 配置基于数据包的GTK更新方法。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security gtk-rekey method packet-based 600000

【相关命令】

·**gtk-rekey enable**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- key-derivation**

------------------------------------------------------------------------

**[key-derivation**]命令用来配置密钥衍生算法。

**[undo key-derivation**]命令用来恢复缺省情况。

【命令】

**[key-derivation**[ { **sha1** \| **sha1-and-sha256** \| **sha256** }]]

**[undo key-derivation**]

【缺省情况】

密钥衍生算法为sha1。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[sha1**]：表示SHA1算法，它使用HMAC-SHA1算法进行迭代计算产生密钥。

**[sha1-and-sha256**]：表示SHA1和SHA256算法，它使用HMAC-SHA1或HMAC-SHA256算法进行迭代计算产生密钥。

**[sha256**]：表示SHA256算法，它使用HMAC-SHA256算法进行迭代计算产生密钥。

【使用指导】

·当使用RSNA安全机制，密钥衍生算法才会生效。

·如果配置保护管理帧功能为**mandatory**模式，建议指定密钥衍生类型为**sha256。**

【举例】

\# 配置密钥衍生算法为SHA256。

\<Sysname\> system-view

Sysname wlan service-template 1

Sysname-wlan-st-1 key-derivation sha256

【相关命令】

·**akm mode**

·**cipher-suite**

·**security-ie**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf**

------------------------------------------------------------------------

**[pmf**]命令用来开启保护管理帧功能。

**[undo pmf**]命令用来关闭保护管理帧功能。

【命令】

**[pmf**[ { **mandatory** \| **optional** }]]

**[undo pmf**]

【缺省情况】

保护管理帧功能处于关闭状态。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[optional**]：指定保护管理帧功能为可选模式，即支持或不支持保护管理帧功能的客户端均可接入。

**[mandatory**]：指定保护管理帧功能为强制模式，即不支持保护管理帧功能的客户端无法接入。

【使用指导】

当使用RSNA安全机制且配置了CCMP加密套件和RSN安全信息元素时，保护管理帧功能才会生效。

【举例】

\# 开启保护管理帧功能。

\<Sysname\> system-view

Sysname wlan service-template 1

Sysname-wlan-st-1 pmf optional

【相关命令】

·**security-ie**

·**cipher-suite**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf association-comeback**

------------------------------------------------------------------------

**[pmf association-comeback**]命令用来配置保护管理帧的关联返回时间。

**[undo pmf association-comeback**]命令用来恢复缺省情况。

【命令】

**[pmf** **association-comeback** *time*]

**[undo pmf** **association-comeback**]

【缺省情况】

保护管理帧的关联返回时间为1秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：保护管理帧的关联返回时间，取值范围为1～20，单位为秒。

【使用指导】

当AP收到客户端的关联重关联请求帧，AP会拒绝此客户端的关联/重关联请求帧，并且向客户端发送关联/重关联响应帧，其中携带了保护管理帧关联返回时间。到了保护管理帧关联返回时间，AP才会接收客户端的关联/重关联请求帧。

【举例】

\# 配置保护管理帧的关联返回时间为2秒。

\<Sysname\> system-view

Sysname wlan service-template 1

Sysname-wlan-st-1 pmf association-comeback 2

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf saquery retrycount**

------------------------------------------------------------------------

**[pmf** **saquery retrycount**]命令用来配置AP发送SA Query request的最大重传次数。

**[undo pmf saquery retrycount**]命令用来恢复缺省情况。

【命令】

**[pmf** **saquery retrycount** *count*]

**[undo pmf** **saquery retrycount** ]

【缺省情况】

AC发送SA Query request帧的最大重传次数为4次。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[count*]：表示AP发送SA Query request帧的最大重传次数，取值范围为1～16。

【使用指导】

若AP在SA Query重试次数内收到SA Query响应帧，则认为客户端在线，并且在关联返回时间内，不再响应关联/重关联请求，当关联返回时间超时后，再次收到客户端的关联/重关联请求帧时，则会再次触发SA Query过程。若AP在SA Query重试次数内未收到SA Query响应帧，并且关联返回时间已经超时，则AP将认为客户端已经掉线，当再次收到该客户端的关联/重关联请求帧时，允许其重新接入。若在关联返回时间内，SA Query过程未完成，则当关联返回时间超时后，再次收到客户端的关联/重关联请求帧时，AP将发送关联/重关联响应帧，响应状态值为"关联/重关联临时被拒绝，稍后重连"，并携带通过**pmf** **association-comeback**命令指定关联返回时间，但不重新触发SA Query过程。

【举例】

\# 设置AC发送SA Query request帧的最大重传次数为3。

\<Sysname\> system-view

Sysname wlan service-template 1

Sysname-wlan-st-1 pmf saquery retrycount 3

【相关命令】

·**pmf**[ { **mandatory** \| **optional** }]

·**pmf saquery retrycount**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- pmf saquery retrytimeout**

------------------------------------------------------------------------

**[pmf saquery retrytimeout**]命令用来设置AP发送SA Query request帧的时间间隔。

**[undo pmf saquery retrytimeout**]命令用来恢复缺省情况。

【命令】

**[pmf saquery retrytimeout** *timeout*]

**[undo pmf saquery retrytimeout**]

【缺省情况】

AP发送SA Query request帧的时间间隔为200毫秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[timeout*]：指定AP发送SA Query request帧的时间间隔,取值范围为100～500，单位为毫秒。

【举例】

\# 设置AP发送SA Query request帧的时间间隔为300毫秒。

\<Sysname\> system-view

Sysname wlan service-template 1

Sysname-wlan-st-1 pmf saquery retrytimeout 300

【相关命令】

[·**pmf**[ { **mandatory** \| **optional** }]]

·**pmf saquery retry****timeout**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- preshared-key**

------------------------------------------------------------------------

**[preshared-key**]命令用来配置PSK密钥。

**[undo preshared-key**]命令用来删除已配置的PSK密钥。

【命令】

**[preshared-key**[ { **pass-phrase \| raw-key** } { **cipher \| simple** } *key*]]

**[undo preshared-key**]

【缺省情况】

未配置PSK密钥。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[pass-phrase**]：以字符串方式输入预共享密钥。

**[raw-key**]：以十六进制数方式输入预共享密钥。

**[cipher**]：以密文方式设置密钥。

**[simple**]：以明文方式设置密钥。

*[key*]：设置明文密钥或密文密钥，区分大小写。密钥长度的范围与选择的密钥参数有关，具体关系如下：

·对于**pass-phrase simple**，密钥是8～63个字符的字符串。

·对于**pass-phrase cipher**，密钥是8～117个字符的字符串。

·对于**raw-key simple**，密钥是64个十六进制数。

·对于**raw-key cipher**，密钥是8～117个字符串。

【使用指导】

·该命令只能在无线服务模板处于关闭的状态下进行配置。并且只有认证密钥管理模式为PSK时，此命令才能够生效，当认证密钥管理模式为802.1X时，配置了此项，无线服务模板可以使能，但此配置不会生效。

·PSK密钥只能配置一个。

【举例】

\# 配置使用明文字符串12345678作为PSK密钥。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security akm mode psk

Sysname-wlan-st-security akm preshared-key pass-phrase simple 12345678

【相关命令】

·**akm mode**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- ptk-lifetime**

------------------------------------------------------------------------

**[ptk-lifetime**]命令用来配置PTK的生存时间。

**[undo ptk-lifetime**]命令用来恢复缺省情况。

【命令】

**[ptk-lifetime** *time*]

**[undo ptk-lifetime**]

【缺省情况】

PTK的生存时间为43200秒。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：指定生存时间，取值范围为180～604800，单位为秒。

【使用指导】

若该命令在无线服务模板处于开启状态下配置，则在原有定时器超时后，再创建新的定时器。

【举例】

\# 配置PTK生存时间为200秒。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security ptk-lifetime 200

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- security-ie**

------------------------------------------------------------------------

**[security-ie**]命令用来配置信标和探查响应帧携带安全IE。

**[undo security-ie**]命令用来配置信标和探查响应帧不携带安全IE。

【命令】

**[security-ie **[{ **rsn** \| **wpa** }]]

**[undo security-ie **[{ **rsn** \| **wpa** }]]

【缺省情况】

信标和探查响应帧不携带WPA IE或RSN IE。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[rsn**]：设置在AP发送信标和探查响应帧时携带RSN IE。RSN IE通告了AP的RSN能力。

**[wpa**]：设置在AP发送信标和探查响应帧时携带WPA IE。WPA IE通告了AP的WPA能力。

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置，并且必须要配置CCMP或TKIP加密套件。

WPA IE和RSN IE可以同时配置。

若配置了安全IE，则认证密钥管理模式和加密套件必须配置。

【举例】

\# 配置信标帧和探查响应帧携带RSN信息元素。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security security-ie rsn

【相关命令】

·**cipher-suite**

[·**akm mode****dot1x**[ \| **psk** }]

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- tkip-cm-time**

------------------------------------------------------------------------

**[tkip-cm-time**]命令用来配置发起TKIP反制策略时间。

**[undo tkip-cm-time**]命令用来恢复缺省情况。

【命令】]

**[tkip-cm-time** *time*]

**[undo tkip-cm-time**]

【缺省情况】

发起TKIP反制策略时间为0，即不启动反制策略。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：设置发起TKIP反制策略时间，取值范围为0～3600，单位为秒。

【使用指导】

·只有在配置了TKIP加密套件时，此命令才能够生效。

·若该命令在无线服务模板处于开启状态时配置，则原有定时器超时后，再创建新的定时器。

·启动TKIP反制策略后，如果相邻两次MIC错误的时间间隔小于等于配置的时间，则会解除所有关联到该无线服务的无线客户端，并且只有在TKIP反制策略实施的时间（60s）后，才允许无线客户端重新建立关联。

【举例】

\# 配置发起TKIP反制策略时间为180秒。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security tkip-cm-time 180

【相关命令】

·**cipher-suite**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- user-authentication mode central**

------------------------------------------------------------------------

!(WLAN用户安全命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[user-authentication mode central**]命令用来配置用户认证模式为集中式认证。

**[undo user-authentication mode central**]命令用来取消集中式认证的用户认证模式。

【命令】

**[user-authentication mode central**]

**[undo user-authentication mode central**]

【缺省情况】

用户认证模式为集中式认证，即在MAC上认证。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

该命令只能在无线服务模板处于关闭的状态下进行配置。并且只有在Master AC上执行该命令时，才能够生效。

集中式认证是指用户认证和密钥协商不在同一个AC上，这种情况只有在MAC和BAC的组网情况下才有可能发生。当配置分层认证时，无线客户端虽然在BAC上上线，但二层认证和三层认证却在MAC上进行，在BAC上只进行密钥协商和下发VLAN操作。

·当客户端在BAC上线，在MAC上统一做认证，则为集中式认证，又称分层认证。

·当客户端在BAC上线，在BAC上做认证，则为分离式认证。

【举例】

\# 配置在MAC上进行用户接入认证。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security user-authentication mode central

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- wep key**

------------------------------------------------------------------------

**[wep key**]命令用来配置WEP密钥。

**[undo wep key**]命令用来删除已配置的WEP密钥。

【命令】

**[wep key**[ *key-id* { **wep40** \| **wep104** \| **wep128** } { **pass-phrase** \| **raw-key** } { **cipher** \| **simple** } *key*]]

**[undo wep key** *key-id*]

【缺省情况】

未配置WEP密钥。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[key-id*]：密钥的ID，取值范围为1～4。

**[wep40**]：设置WEP40密钥选项。

**[wep104**]：设置WEP104密钥选项。

**[wep128**]：设置WEP128密钥选项。

**[pass-phrase**]：表示共享密钥为字符串。

**[raw-key**]：表示共享密钥为十六进制数。

**[cipher**]：以密文方式设置密钥。

**[simple**]：以明文方式设置密钥。

*[key*]：设置明文密钥或密文密钥，区分大小写。明文密钥的长度范围和选择的密钥参数有关。具体关系如下。密文密钥为37～73个字符的字符串。

对于**wep40 pass-phrase**，密钥是5个字符的字符串。

对于**wep104 pass-phrase**，密钥是13个字符的字符串。

对于**wep128 pass-phrase**，密钥是16个字符的字符串。

对于**wep40 raw-key**，密钥是10个16进制数。

对于**wep104 raw-key**，密钥是26个16进制数。

对于**wep128 raw-key**，密钥是32个16进制数。

【使用指导】

·该命令只能在无线服务模板处于关闭的状态下进行配置。

·以明文或密文设置密钥，均以密文的方式保存在配置文件中。

·最多可以配置四个WEP密钥。

【举例】

\# 配置加密套件为WEP40，并配置WEP40密钥为明文12345。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security wep key 1 wep40 pass-phrase simple 12345

【相关命令】

·**cipher-suite**

·**wep key-id**

**WLAN用户安全 \-- WLAN用户安全配置命令 \-- wep key-id**

------------------------------------------------------------------------

**[wep key-id**]命令用来配置密钥ID。

**[undo wep key-id**]命令用来恢复缺省情况。

【命令】

**[wep key-id**[ { **1** \| **2** \| **3** \| **4** }]]

**[undo wep key-id**]

【缺省情况】

密钥ID为1。

【视图】

无线服务模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[1**]：选择密钥ID为1。

**[2**]：选择密钥ID为2。

**[3**]：选择密钥ID为3。

**[4**]：选择密钥ID为4。

【使用指导】

·该命令只能在无线服务模板处于关闭的状态下进行配置。当配置了多个密钥，可以通过配置密钥ID选择要使用的加密密钥。

·如果使用RSNA安全机制，密钥ID不能为1，需要配置其它密钥索引值。因为RSN和WPA协商的密钥ID将为1。

·只有在配置了与密钥长度相对应的WEP加密套件时，指定ID的密钥才会生效。

【举例】

\# 配置WEP40加密套件，WEP40密钥为明文12345，配置密钥ID为1。

\<Sysname\> system-view

Sysname wlan service-template security

Sysname-wlan-st-security cipher-suite wep40

Sysname-wlan-st-security wep key 1 wep40 pass-phrase simple 12345

Sysname-wlan-st-security wep key-id 1

【相关命令】

·**wep key**
