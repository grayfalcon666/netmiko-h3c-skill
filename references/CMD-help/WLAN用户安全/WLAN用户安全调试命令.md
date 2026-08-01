<!-- CMD-INDEX
  debugging wlan usersec              | 用户视图             | L5
-->

**WLAN用户安全 \-- WLAN用户安全调试命令 \-- debugging wlan usersec**

------------------------------------------------------------------------

【命令】

**[debugging**[ **wlan** **usersec** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } [ **verbose** ] }]]

**[undo**[ **debugging** **wlan** **usersec** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } [ **verbose** ] }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示usersec所有类型调试信息开关。

**[error**]：表示usersec错误类型调试信息开关。

**[event**]：表示usersec事件类型调试信息开关。

**[timer**]：表示usersec定时器调试信息开关。

**[fsm**]：表示usersec状态机调试信息开关。

**[packet**]：表示usersec报文调试信息开关。

**[receive**]：表示usersec报文接收调试信息开关。

**[send**]：表示usersec报文发送调试信息开关。

**[verbose**]：表示usersec报文的详细调试信息开关。

【描述】

**[debugging wlan usersec**]命令用来打开usersec调试信息开关。**undo debugging wlan usersec**命令用来关闭usersec调试信息开关。

缺省情况下，usersec模块调试信息开关处于关闭状态。

表1-1 debugging wlan usersec error命令输出信息描述表

字段

描述

 

No security info in the client.

客户端中没有安全信息

No security info in BSS *BSSID*.

BSS *BSSID*中没有安全信息

No security info in service template *STName*.

ST *STName*中没有安全信息

BSS *BSSID* doesn\'t support shared-key authentication.

BSS不支持shared-key认证算法

Failed to process the 1st shared-key authentication frame: *Reason*.

因为*Reason*，处理第1条shared-key认证报文失败

*[Reason*]取值如下：

Invalid transmission sequence number *TransNum*：传输序列号*TransNum*无效

Failed to process the 3rd shared-key authentication frame: *Reason*.

因为*Reason*，处理第3条shared-key认证报文失败

*[Reason*]取值如下：

·Invalid challenge text：挑战码无效

·Invalid transmission sequence number *TransNum*：传输序列号*TransNum*无效

·Invalid challenge text length *ChlgTxtLength*：挑战码长度*ChlgTxtLength*无效

·Unencrypted frame：报文未加密

·Non-existent challenge IE or unsuccessful challenge IE decoding： 挑战IE不存在或者解析挑战IE不正确

Failed to send the response for the unsuccessful shared-key authentication to the client.

向客户端发送shared-key认证失败回应报文失败

Failed to send the response for the successful shared-key authentication to the client.

向客户端发送shared-key认证成功回应报文失败

Failed to send the *MsgType* message to the down-link device.

下发*MsgType*消息失败

*[MsgType*]取值如下：

·L2 authentication result：二层认证结果

·L2 authorization result：二层授权结果

·L3 authentication result：三层认证结果

Failed to send the *MsgType* message to the up-link device.

上报*MsgType*类型消息失败

*[MsgType*]取值如下：

·starting L2 authentication：开始二层认证

·starting L3 authentication：开始三层认证

Invalid sent session key length *SendKeyLen* or invalid received session key length *RecvKeyLen*.

Send session key长度*SendKeyLen*或者received session key长度*RecvKeyLen*不合法

Failed to send 4-way handshake message 3: *Reason.*

因为*Reason*，发送四次握手message3报文失败

*[Reason*]取值如下：

·Unsuccessful IE encoding：解析IE失败

·Unsuccessful GTK KDE obtaining：获取GTK KDE失败

·Unsuccessful key data encrypting：加密key data失败

·Unsuccessful EAPOL-Key frame constructing：构造EAPOL-Key报文失败

Failed to send group handshake message 1: *Reason*.

因为*Reason*，发送组播握手message1报文失败

*[Reason*]取值如下：

·Unsuccessful key data encrypting：加密key data失败

·Unsuccessful EAPOL-Key frame constructing：构造EAPOL-key报文失败

·Unsuccessful GTK KDE obtaining：获取GTK KDE失败

Failed to process 4-way handshake message 2: *Reason.*

因为*Reason*，处理四次握手message2报文失败

*[Reason*]取值如下：

·Unsuccessful PTK generating：产生PTK失败

·Invalid descriptor type：descriptor type无效

·Invalid replay counter：replay counter 无效

·Invalid Key IV：KeyIV无效

·Invalid key data length *KeyDataLength*：key data长度*KeyDataLength*无效

·Invalid MIC：MIC无效

·Unsuccessful frame decoding：解析报文失败

·Unsuccessful IE decoding：解析IE失败

·Invalid IE：IE无效

Failed to process 4-way handshake message 4: *Reason.*

因为*Reason*，处理四次握手message4报文失败

*[Reason*]取值如下：

·Invalid descriptor type：descriptor type无效

·Invalid replay counter：replay counter 无效

·Invalid Key IV：KeyIV无效

·Invalid key data length *KeyDataLength*：key data长度*KeyDataLength*无效

·Invalid MIC：MIC无效

·Unsuccessful frame decoding：解析报文失败

Failed to process group handshake message 2: *Reason.*

因为*Reason*，处理组播握手message2报文失败

*[Reason*]取值如下：

·Invalid descriptor type：descriptor type无效

·Invalid replay counter：replay counter 无效

·Invalid Key IV：KeyIV无效

·Invalid key data length *KeyDataLength*：key data长度*KeyDataLength*无效

·Invalid MIC：MIC无效

·Unsuccessful frame decoding：解析报文失败

Failed to process the 4-way handshake request: *Reason.*

因为*Reason*，处理四次握手request报文失败

*[Reason*]取值如下：

·Invalid replay counter：replay counter 无效

·Invalid MIC：MIC无效

·Unsuccessful frame decoding：解析报文失败

·The current client hasn\'t finished key negotiation or 4-way handshake：当前客户端还未完成密钥协商或者四次握手

Failed to process the MIC failure report: *Reason.*

因为*Reason*，处理MIC错误报告报文失败

*[Reason*]取值如下：

·Invalid replay counter：replay counter 无效

·Unsuccessful frame decoding：解析报文失败

·Invalid RSC：RSC无效

·The current client hasn\'t finished key negotiation：当前客户端未完成密钥协商

BSS *BSSID* failed to process the time-based GTK rekey.

BSS *BSSID*处理基于时间更新GTK失败

BSS *BSSID* failed to process the packet-based GTK rekey.

BSS *BSSID*处理基于报文更新GTK失败

BSS *BSSID* failed to process the stationoff-based GTK rekey.

BSS *BSSID*处理基于客户端下线更新GTK失败

Failed to send the add mobile message.

发送add mobile消息失败

BSS *BSSID* failed to send the update WLAN message.

BSS *BSSID*发送update wlan消息失败

Failed to add security TLV data to the add mobile message.

·添加安全TLV数据至add mobile类型消息失败

BSS *BSSID* failed to add security TLV data to the add WLAN message.

添加安全TLV数据至add wlan 类型消息失败

Failed to get security TLV data from the add mobile message.

从add mobile消息中获取安全TLV数据失败

Failed to get security TLV data from the add WLAN message.

从add wlan消息中获取安全TLV数据失败

Failed to fill the add mobile message: *Reason*.

因为*Reason*，填充add mobile消息失败

*[Reason*]取值如下：

·Unsuccessful WEP key decrypting：解密wep key失败

BSS *BSSID* failed to fill the add WLAN message: *Reason*.

因为*Reason*，填充add wlan消息失败

*[Reason*]取值如下：

·Unsuccessful GTK decrypting：解密GTK失败

Failed to process the add mobile message: *Reason*.

因为*Reason*，处理add mobile消息失败

*[Reason*]取值如下：

·UnsuccessfulWEP keyencrypting：加密wep key失败

BSS *BSSID* failed to process the add WLAN message: *Reason*.

因为*Reason*，处理add wlan消息失败

*[Reason*]取值如下：

·Unsuccessful GTK encrypting：加密GTK失败

Failed to fill security driver information for the client.

客户端填充安全驱动信息失败

Failed to fill security driver information for BSS *BSSID*.

BSS *BSSID*填充安全驱动信息失败

Failed to process the (re)association request without security IE: *Reason*.

因为*Reason*，处理不带安全IE的(重)关联请求失败

*[Reason*]取值如下：

·Invalid security mode of the client：客户端的安全模式无效

Failed to process the reassociation request without security IE: *Reason*.

因为*Reason*，处理不带安全IE的重关联请求失败

*[Reason*]取值如下：

·Security IE already exists in the client：客户端结构下已存在IE

Failed to process the association request without security IE: *Reason*.

因为*Reason*，处理不带安全IE的关联请求失败

*[Reason*]取值如下：

·No WEP key exists：Wep key 不存在

·The shared-key client failed to save the WEP key：shared-key模式下客户端填充wep key失败

Failed to process the (re)association request with security IE: *Reason*.

因为*Reason*，处理带安全IE的(重)关联请求失败

*[Reason*]取值如下：

·Invalid security IE：安全IE无效

·The client doesn\'t use open system authentication：客户端链路认证方式不是open-system

·The BSS is configured with no cipher suite：BSS下未配置加密套件

Failed to process the (re)association request with RSN IE: *Reason*.

因为*Reason*，处理带RSNIE的(重)关联请求失败

*[Reason*]取值如下：

·The security mode for the BSS is not RSN：BSS下安全模式不是RSN

Failed to process the reassociation request with RSN IE: *Reason*.

因为*Reason*，处理带RSNIE的重关联请求失败

*[Reason*]取值如下：

·Invalid capability field in the frame：报文中的capability字段无效

·Invalid cipher suite or AKM mode in the frame：报文中的cipher suite 或者AMK无效

Failed to process the (re)association request with WPA IE: *Reason*.

因为*Reason*，处理带WPAIE的(重)关联请求失败

*[Reason*]取值如下：

·The security mode for the BSS is not WPA：BSS中安全模式不是WPA

Failed to process the reassociation request with WPA IE: *Reason*.

因为*Reason*，处理带WPAIE的重关联请求失败

*[Reason*]取值如下：

·Invalid IE in the frame：报文中的IE无效

Failed to select a unicast cipher suite for the client.

客户端选择单播加密套件失败

Failed to select an AKM mode for the client.

客户端选择AKM模式失败

Invalid element ID in the RSN IE.

RSN IE中element ID无效

Invalid version in the RSN IE.

RSN IE中版本无效

Invalid group cipher suite in the security IE.

安全IE中组播加密套件无效

Invalid unicast cipher suite in the security IE.

安全IE中单播加密套件无效

Invalid element ID in the WPA IE.

WPA IE中element ID无效

Invalid OUI in the WPA IE.

WPA IE中OUI无效

Invalid OUI type in the WPA IE.

WPA IE中OUI类型无效

Invalid version in the WPA IE.

WPA IE中版本无效

Failed to get security info for roaming clients.

获取漫游用户迁移安全信息失败

BSS *BSSID* failed to inherit PMK from service template *STName*: *Reason*.

因为*Reason*， BSS* BSSID*从服务模板*STName*继承PMK失败

*[Reason*]取值如下：

·Unsuccessful PSK decoding：解析PSK失败

·The PSK was not converted to PMK：把PSK转成PMK失败

BSS *BSSID* failed to inherit the group cipher suite from service template *STName*.

BSS* BSSID*从服务模板*STName*中继承组播加密套件失败

BSS *BSSID* failed to inherit the WEP key configuration from service template *STName*.

BSS* BSSID*从服务模板*STName*中继承wep key配置失败

Failed to deactivate the security information in the client.

去激活客户端中的安全信息失败

Failed to initialize PMF info in service template *STName*: Failed to allocate memory.

由于申请内存空间失败，初始化服务模板*STName*中PMF信息失败。

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to initialize PMF info in BSS: Failed to allocate memory.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，由于申请内存空间失败，初始化BSS中PMF信息失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to initialize PMF info in client: Failed to allocate memory.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，由于申请内存空间失败，初始化客户端中PMF信息失败。

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to add PMF TLV to the add wlan message.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，向add wlan消息中追加PMF TLV数据失败。

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to add PMF TLV to the update wlan message.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，向update wlan消息中追加PMF TLV数据失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to add PMF TLV to the add mobile message.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，向add mobile消息中追加PMF TLV数据失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to send SA query response.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，发送安全关联询问应答报文失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Invalid SA query transaction ID.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，安全关联询问应答中的transaction ID是无效的。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to send SA query request.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，发送安全关联询问请求报文失败。

The security IE must be RSN and the cipher suite must be CCMP when PMF is enabled.

若配置PMF开关，安全IE必须配置为RSN并且加密套件必须配置为CCMP。

Failed to update IGTK for BSS *BSSID*: Failed to generate IGTK.

由于生成IGTK失败，BSS *BSSID*更新IGTK失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* PMF negotiation failed: Invalid client security mode or security IE when PMF status is mandatory.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。当PMF为强制状态时，客户端的安全模式或者安全IE信息非法。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* PMF negotiation failed: Unmatched PMF capabilities.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。PMF协商过程中，客户端关联报文中RSN capability携带的MFPC/MFPR两位与BSS的PMF status不匹配，导致PMF协商失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* PMF negotiation failed: PMF is disabled in the BSS.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。BSS的PMF开关为关闭状态，客户端关联报文中携带的MFPR位为1，即要求PMF能力。此时PMF协商失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to send (re)association response.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。发送（重）关联响应失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to negotiate the group management cipher suite: Unmatched group management cipher suite in RSN IE.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，由于RSN IE中的组加密套件不匹配，协商组加密套件失败。

表1-2 debugging wlan usersec event命令输出信息描述表

字段

描述

Started processing the shared-key authentication frame: Transmission number=*TransNum*.

开始处理shared-key认证报文，且传输序列号为*TransNum*.

Filled challenge IE successfully.

填充挑战IE成功

Processed the 1st shared-key authentication frame successfully.

处理第1条shared-key认证报文成功

Processed the 3rd shared-key authentication frame successfully.

处理第3条shared-key认证报文成功

Started user authentication.

开始用户认证

Started L3 authentication.

开始三层认证

Started L2 authentication.

开始二层认证

Started key negotiation: Key negotiation status= *KeyNegoStatus*, security mode=*SecMode*.

为*KeyNegoStatus*开始密钥协商，且安全模式为*SecMode*

*[SecMode*]取值如下：

·1：WPA ，Wi-Fi protected Access Wi-Fi防护访问

·2：RSN ，Robust Security Network 固安网络

*[KeyNegoStatus*]取值取下：

·1：Normal，正常上线

·2：Reauth，重认证

·3：Request，请求

·4：Rekey，密钥更新

Started GTK negotiation: Key negotiation status= *KeyNegoStatus*, security mode=*SecMode*.

为*KeyNegoStatus*开始组播密钥协商，且安全模式为*SecMode*

*[SecMode*]取值如下：

·1：WPA ，Wi-Fi protected Access Wi-Fi防护访问

·2：RSN ，Robust Security Network 固安网络

*[KeyNegoStatus*]取值取下：

·1：Normal，正常上线

·2：Reauth，重认证

·3：Request，请求

·4：Rekey，密钥更新

Started processing L2 authentication: Result=*L2AuthResult*, Authentication status=*AuthenticationStatus.*

开始处理*ReasonStatus*二层认证的结果*L2AuthResult*

*[L2AuthResult*]取值如下：

·0：success，成功

·1：failed-offline，失败下线

·2：failed-online，失败不下线

*[AuthenticationStatus*]取值如下：

·1：Normal，正常上线

·2：Reauth，重认证

Started processing L3 authentication: Result=*L3AuthResult.*

开始处理三层认证结果*L3AuthResult*

*[L3AuthResult*]取值如下：

·0：success，成功

·1： failed，失败

Started processing L2 authorization: VLAN ID=*VLANID*.

开始处理授权结果：VLANID=* VLANID.*

Started processing key negotiation: Result=*KeyNegoResult.*

开始处理密钥协商成功的结果*KeyNegoResult*

*[KeyNegoResult*]取值如下：

·success：成功

·discard packet：丢弃报文

·failed：失败

Finished user authentication: Result=*UserAuthResult*

用户认证结束，认证结果*UserAuthResult*

*[UserAuthResult*]取值如下：

·success：成功

·failed with reasoncode *ReasonCode*：失败，原因为*ReasonCode*

AP *APID* received a *MsgType* message: CMD=*CMDValue*, length=*Len*.

AP *APID*接收到一个*MsgType*类型消息，且CMD的值为*CMDValue*，消息长度为*Len*

*[MsgType*]取值如下：

·up：上报的

·down：下发的

Processed *MsgType* successfully.

处理*MsgType*类型报文成功

*[MsgType*]取值如下：

·4-way handshake message 2：四次握手message 2

·4-way handshake message 4：四次握手message 4

·group handshake message 2：组播握手message 2

·4-way handshake request：四次握手请求

Times of resending the *MsgType* reached the limit: Maximum resending times=*MaxResndTimes*.

重发*MsgType*类型报文的次数达到最大值*MaxResndTimes*

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Started packet-based GTK rekey for BSS *BSSID*.

开始为BSS *BSSID*处理基于报文更新GTK

Started stationoff-based GTK rekey for BSS *BSSID*: Client MAC address=*StaMac*.

开始为BSS* BSSID*处理基于客户端 *StaMac*下线更新GTK

Updated GTK for BSS *BSSID*.

BSS* BSSID*更新GTK成功

Filled security information in the add mobile message successfully.

向add mobile消息中填充安全信息成功

BSS *BSSID* filled security information in the *MsgType* message successfully.

BSS *BSSID*向*MsgType*类型消息中填充安全信息成功*MsgType*取值如下

·add WLAN：加入WLAN

·update WLAN：更新WLAN

Processed security information in the add mobile message successfully.

处理add mobile消息中的安全信息成功

BSS *BSSID* processed security information in the *MsgType* message successfully.

BSS *BSSID* 处理*MsgType*类型消息中的安全信息成功*MsgType *取值如下：

·add WLAN：加入WLAN

·update WLAN：更新WLAN

Filled security info about clients in the driver successfully.

客户端填充安全驱动信息成功

Filled security info about BSS *BSSID* in the driver successfully.

BSS *BSSID* 填充安全驱动信息成功

Filled security info about clients in the kernel successfully.

填充客户端安全信息到内核成功

Filled security info about BSS *BSSID* in the kernel successfully.

填充BSS安全信息到内核成功

The clear-type client processed the (re)association request without security IE successfully.

clear模式下的客户端处理不带安全IE的(重)关联请求成功

The shared-key client processed the (re)association request without security IE successfully.

shared-key模式下的客户端处理不带安全IE的(重)关联请求成功

Selected unicast cipher suite *PCipherSuite* for the client.

客户端选择单播加密套件*PCipherSuite*成功

*[PCipherSuite*]取值如下：

·2：TKIP

·4：CCMP

Selected AKM mode *AkmMode* for the client.

客户端选择AKM模式*AkmMode*成功

*[AkmMode*]取值如下：

·1：DOT1X

·2：PSK

Processed the (re)association request with RSN IE successfully.

处理带RSN IE的关联请求成功

Processed the (re)association request with WPA IE successfully.

处理带WPA IE的关联请求成功

Processed (re)association request with security IE successfully. The client is not allowed to go online: TKIP countermeasure is active.

处理带安全IE的关联请求成功，但是由于TKIP反制处于激活状态所以不允许客户端上线。

Got the security info for roaming clients.

获取漫游用户迁移安全信息成功

Recovered the security info (length: *Lengh*) for roaming clients.

恢复漫游用户迁移安全信息(长度：消息长度)成功

BSS *BSSID* inherited security information from service template *STName*.

BSS* BSSID*从服务模板*STName*继承安全信息成功

Initialized security information in BSS *BSSID*.

初始化BSS* BSSID*中安全信息成功

Deleted security information in BSS *BSSID*.

删除BSS* BSSID*中安全信息成功

Initialized security information in the client.

初始化客户端中的安全信息成功

Deleted security information in the client.

删除客户端中的安全信息成功

Initialized security information in service template *STName*.

初始化服务模板*STName*中的安全信息成功

Deleted security information in service template *STName*.

删除服务模板*STName*中的安全信息成功

Deactivated security information in the client.

去激活客户端中的安全信息成功

Initialized PMF information in service template *STName*.

初始化服务模板*STName*中PMF信息成功。

Deleted PMF information in service template *STName*.

删除服务模板*STName*中PMF信息成功。

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to get PMF info in BSS: PMF info does not exist in the BSS.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，由于BSS中pmf信息不存在，获取pmf信息失败

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Initialized PMF information in BSS.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，BSS中的PMF信息初始化完成。

Inherited PMF information for BSS *BSSID* from service template *STName*.

BSS* BSSID*从服务模板*STName*继承PMF信息成功。

APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Deleted PMF information in BSS.

APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*， BSS中的PMF信息删除完成。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Initialized PMF information in client.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，客户端中的PMF信息初始化完成。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Deleted PMF information in client.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，客户端中的PMF信息删除完成。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to get PMF info in client: PMF info in the client does not exist.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，客户端中不存在PMF信息。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Sent SA query request.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*， 发送安全关联询问请求报文成功。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Sent SA query response.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*， 发送安全关联询问应答报文成功。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Sent (re)association response.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。发送（重）关联响应成功。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Discarded (re)association request: AP is not prepared for association.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*。AP未准备好处理与客户端的关联，所以丢弃（重）关联请求帧。

表1-3 debugging wlan usersec fsm命令输出信息描述表

字段

描述

4-way handshake FSM changed state from *State1* to *State2*.

四次握手状态机切换，*State1*-\>*State2*。

·*State1*取值如下：

·NULL：未定义状态

·IDLE：空闲状态

·WAITMSG2：发送完message 1等待message 2状态

·WAITMSG4：发送完message 3等待message 4状态

·4WAYDONE：四次握手完成状态

*[State2*]取值如下：

·IDLE：空闲状态

·WAITMSG2：发送完message 1等待message 2状态

·WAITMSG4：发送完message 3等待message 4状态

·4WAYDONE：四次握手完成状态

·DONE：密钥协商完成状态

Group handshake FSM changed state from *State1* to *State2*.

组播握手状态机切换，*State1*-\>*State2*。

·*State1*取值如下：

·NULL：未定义状态

·GKHS_IDLE：空闲状态

·GKHS_WAITMSG2：发送完message 1等待message 2状态

*[State2*]取值如下：

·GKHS_IDLE：空闲状态

·GKHS_WAITMSG2：发送完message 1等待message 2状态

·GKHS_DONE：组播握手完成状态

表1-4 debugging wlan usersec packet receive命令输出信息描述表

字段

描述

Received a *MsgType*.

接收到*MsgType*类型报文

*[MsgType*]取值如下：

·4-way handshake message 2：四次握手message 2

·4-way handshake message 4：四次握手message 4

·group handshake message 2：组播握手message 2

·MIC failure report：MIC错误报告

·4-way handshake request：四次握手请求

·group handshake request：组播握手请求

表1-5 debugging wlan usersec packet receive verbose命令输出信息描述表

字段

描述

Received an EAPOL-Key frame from client *StaMacAddr* (Length=*Length*)

*[Packet context*]

接收到来自客户端 *StaMacAddr*的EAPOL-key报文(报文长度：*Length*)

*[Packet context*]：报文内容

表1-6 debugging wlan usersec packet send命令输出信息描述表

字段

描述

Failed to send a *MsgType*.

发送*MsgType*类型报文失败

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Sent a *MsgType*.

发送*MsgType*类型报文成功

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

表1-7 debugging wlan usersec packet send verbose命令输出信息描述表

字段

描述

Sent an EAPOL-Key frame to client *StaMacAddr* (Length=*Length*)

*[Packet context*]

发送EAPOL-key报文给客户端 *StaMacAddr* (报文长度：*Length*)

*[Packet context *]：报文内容

表1-8 debugging wlan usersec timer命令输出信息描述表

字段

描述

Created timer *TimerId* for resending *MsgType*.

创建*MsgType*类型报文重传定时器*TimerId*成功

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Deleted timer *TimerId* for resending *MsgType*.

删除*MsgType*类型报文重传定时器*TimerId*

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Timer TimerId for resending *MsgType* expired.

*[MsgType*]类型报文重传定时器*TimerId*超时

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Failed to create a timer for resending *MsgType*.

创建*MsgType*类型报文重传定时器失败

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Refreshed timer *TimerId* for resending *MsgType*.

刷新*MsgType*类型报文重传定时器成功

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Failed to refresh timer *TimerId* for resending *MsgType*.

刷新*MsgType*类型报文重传定时器失败

*[MsgType*]取值如下：

·4-way handshake message 1：四次握手message 1

·4-way handshake message 3：四次握手message 3

·group handshake message 1：组播握手message 1

Created *TimerType* timer *TimerId* for BSS *BSSID*.

BSS *BSSID*创建*TimerType*类型定时器*TimerId*成功

*[TimerType*]取值如下：

·TKIP detect：TKIP检测

·TKIP counter measure：TKIP反制

·GTK life：GTK更新

Deleted *TimerType* timer *TimerId* in BSS *BSSID*.

删除BSS *BSSID* 中的*TimerType*定时器*TimerId*

*[TimerType*]取值如下：

·TKIP detect：TKIP检测

·TKIP counter measure：TKIP反制

·GTK life：GTK更新

*[TimerType* timer *TimerId* in BSS *BSSID* expired.]

BSS *BSSID*中的*TimerType*定时器*TimerId*超时

*[TimerType*]取值如下：

·TKIP detect：TKIP检测

·TKIP counter measure：TKIP反制

·GTK life：GTK更新定时器

Failed to create *TimerType* timer for BSS *BSSID*.

BSS *BSSID*创建*TimerType*类型定时器失败

*[TimerType*]取值如下：

·TKIP detect：TKIP检测

·TKIP counter measure：TKIP反制

·GTK life：GTK更新定时器

Created PTK life timer *TimerId*.

创建PTK更新定时器*TimerId*成功

Deleted PTK life timer *TimerId*.

删除PTK更新定时器*TimerId*

PTK life timer *TimerId* expired.

PTK更新定时器*TimerId*超时

Failed to create a PTK life timer.

创建PTK更新定时器失败

Deleted timer *TimerId* for resending *MsgType*.

删除重传*MsgType*类型报文定时器

*[MsgType*]取值如下：

·4-way handshake message：四次握手message

·group handshake message：组播握手message

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Deleted SA query timer.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，删除SA Query定时器成功。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Failed to create SA query timer.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，创建SA Query定时器失败。

MAC: *UserMAC*, APID: *APID*, Radio ID: *RadioID*, BSSID: *BSSID* Created SA query timer.

用户的MAC地址为*UserMAC*，APID为*APID*，RadioID为*RadioID*，BSSID为*BSSID*，创建SA Query定时器成功。

【举例】

\# 在RSN安全模式下，客户端上线密钥协商过程中，该客户端的MAC地址为000b-c002-9d11，

其所在BSS的BSSID为000f-e202-1213，在AC端打开wlan usersec packet send开关，会有

下调试信息：

\<H3C\>debugging wlan usersec packet send

%Apr  4 09:18:45:965 2014 H3C STAMGR/4/PktSend: [MAC:000b-c002-9d11, BSSID:000f-

e202-1213Sent 4-way handshake message1 successfully.]

*[//*]*成功发送四次握手message1消息。*

\# 在RSN安全模式下，客户端上线密钥协商过程中，在AC端打开wlan usersec packet send verbos

开关，会有如下调试信息：

\<H3C\>debugging wlan usersec packet send verbose

\*Apr  4 09:18:45:964 2014 H3C STAMGR/4/PktSend: Sent an EAPOL-key frame to client 000b-c002-9d11 (Length: 153)

 08 02 7f 00 00 0b c0 02 9d 11 00 0f e2 02 12 13

 00 0f e2 02 12 13 00 00 aa aa 03 00 00 00 88 8e

 01 03 00 75 02 00 8a 00 10 00 00 00 00 00 00 00

 00 55 f3 62 91 d2 85 a6 9b 3f 51 32 c7 02 08 b8

 78 f3 01 6b 83 42 31 d8 ea 41 5a 1f c2 7d 8e 93

 34 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

 00 00 16 dd 14 00 0f ac 04 00 00 00 00 00 00 00

 00 00 00 00 00 00 00 00 00

*[//*]*发送一个EAPOL-Key报文到客户端。*

\# 在RSN安全模式下，客户端上线密钥协商过程中，在AC端打开wlan usersec packet receive开关，会有如下调试信息：

\<H3C\>debugging wlan usersec packet receive

%Apr  4 09:18:46:096 2014 H3C STAMGR/4/PktRcv: [MAC:000b-c002-9d11, BSSID:000f-e

202-1213Received 4-way handshake massage2.]

*[//*]*接受到四次握手message2消息。*

\# 在RSN安全模式下，客户端上线密钥协商过程中，在AC端打开wlan usersec event开关，会有如下调试信息：

\<H3C\>debugging wlan usersec event

%Apr  4 09:18:46:110 2014 H3C STAMGR/4/Event: [MAC:000b-c002-9d11, BSSID:000f-e2

02-1213Processed 4-way handshake message2 successfully.]

*[//*]*处理四次握手message2报文成功。*

\# 在RSN安全模式下，客户端上线密钥协商过程中，在AC端打开wlan usersec timer开关，会有如下调试信息：

\<H3C\>debugging wlan usersec timer

%Apr  4 09:18:45:967 2014 H3C STAMGR/4/Timer: [MAC:000b-c002-9d11, BSSID:000f-e2

02-1213Created timer 1 for resending 4-way handshake message1 successfully.]

*[//*]*创建四次握手message1重传定时器成功。*

\# 在设备上配置支持802.11w的客户端上线，打开WPMF事件调试信息开关和定时器调试开关，打印如下调试信息：

\<AC\> debugging wlan usersec event

\*Jun 28 19:07:46:926 2014 H3C STAMGR/7/Event: MAC: 9cd3-6d9e-6742, APID: 2, RadioID: 2, BSSID: 000f-e2ff-0011 Initialized wpmf information in client.

*[//*]*初始化STA信息中的wpmf信息成功。*

\*Jun 28 19:07:47:070 2014 H3C STAMGR/7/Timer: MAC: 9cd3-6d9e-6742, APID: 2, RadioID: 2, BSSID: 000f-e2ff-0011 Created SA query timer.

*[//*]*创建一个安全连接询问定时器。*
