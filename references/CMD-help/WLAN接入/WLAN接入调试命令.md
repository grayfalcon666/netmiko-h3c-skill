<!-- CMD-INDEX
  debugging wlan client               | 任意视图             | L6
  debugging wlan client mac           | 任意视图             | L470
-->

**WLAN接入 \-- WLAN接入调试命令 \-- debugging wlan client**

------------------------------------------------------------------------

【命令】

**[debugging wlan client**[ { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } [ **verbose** ] }]]

**[undo debugging wlan client **[{ **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } [ **verbose** ] }]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示客户端所有类型的调试开关。

**[error**]：表示客户端错误类型的调试开关。

**[event**]：表示客户端事件类型的调试开关。

**[fsm**]：表示客户端状态机类型调试开关。

**[timer**]：表示客户端定时器类型调试开关。

**[packet receive**]：表示客户端接收报文的调试开关。

**[packet send**]：表示客户端发送报文的调试开关。

**[verbose**]：显示详细的调试信息，如果不指定，显示简要的调试信息。

【描述】

**[debugging wlan client**]命令用来打开客户端调试信息开关。**undo debugging wlan client**命令用来关闭客户端调试信息开关。

缺省情况下，客户端调试信息开关处于关闭状态。

表1-1 debugging wlan client error命令输出信息描述表（AC/FAT AP）

字段

描述

Failed to send the (re)association response.

发送（重）关联回应失败

Failed to send the delete mobile message to the uplink device.

上行同步delete mobile消息失败

Failed to enable packet socket for BSS *BSSID*.

使能BSS *BSSID*的packet socket 失败

Failed to assign the port to a VLAN when creating a BSS.

创建BSS时向端口添加Vlan失败

Failed to remove the port from a VLAN.

端口退出Vlan失败

Failed to inform service *service* of AP event.

向业务模块*service*通知AP事件失败

*[service*]取值如下：

·BASIC：基础模块

·11ABG：802.11abg

·WMM：无线QoS

·11R：802.11r

·11I：802.11i

·11N：802.11n

·11AC：802.11ac

·ROAM：漫游模块

·11W：802.11w

·WLAS AM：无线接入认证端

·WLAS CM：无线接入客户端

·VLAN：VLAN

·FWD_POLICY：策略转发

·SAVI：源地址有效验证

·MCO：组播优化

Failed to inform service *service* of radio event.

向业务模块*service*通知radio事件失败

*[service*]取值如下：

·BASIC：基础模块

·11ABG：802.11abg

·WMM：无线QoS

·11R：802.11r

·11I：802.11i

·11N：  802.11n

·11AC：802.11ac

·ROAM：漫游模块

·11W：802.11w

·WLAS AM：无线接入认证端

·WLAS CM：无线接入客户端

·VLAN：VLAN

·FWD_POLICY：策略转发

·SAVI：源地址有效验证

·MCO：组播优化

APID: *APID[, *Radio ID*: RadioID, *WLAN ID*: WlanID*] Failed to delete all clients.

删除所有的Client失败

Failed to get BSS *BSSID*.

获取BSS *BSSID*失败.

Failed to create a BSS.

创建BSS失败。

Received unsupported queue message.

收到了不支持的队列消息

BSSID: *BSSID* Failed to send add wlan message to downlink device.

发送下行add wlan消息失败

BSSID: *BSSID* Failed to send delete wlan message to downlink device.

发送下行delete wlan消息失败

Failed to disable packet socket for BSS *BSSID*.

去使能BSS *BSSID*的packet socket 失败

MAC: *mac-address*, BSSID: *BSSID* Failed to send add mobile message to downlink device.

下同步add mobile消息失败

MAC: *mac-address*, BSSID: *BSSID* Failed to send add mobile message to uplink device.

上同步add mobile消息失败

MAC: *mac-address*, BSSID: *BSSID* Failed to send delete mobile message to downlink device.

下同步delete mobile消息失败

MAC: *mac-address*, BSSID: *BSSID* Failed to send delete mobile message to uplink device.

上同步delete mobile消息失败

Failed to process radio up event.

处理radio up事件失败

表1-2 debugging wlan client error命令输出信息描述表(仅FAT AP)

字段

描述

Failed to process a probe request: The frame doesn\'t contain mandatory IE.

处理探测请求帧失败，由于报文没有包含强制IE元素

Failed to get the BSS: Invalid BSSID.

获取BSS失败：BSSID无效

Failed to decode the SSID IE: The length of the SSID exceeds the upper limit.

解析SSID IE失败，由于SSID 长度大于上限

Failed to decode the supported rates IE: The length exceeds the upper limit.

解析Supported rates IE失败，由于rates长度大于上限

Failed to decode the FH Parameter Set IE: Invalid length.

解析FH Parameter Set IE失败，由于FH Parameter Set长度为非标准长度

Failed to decode the DSSS Parameter Set IE: Invalid length.

解析DSSS Parameter Set IE失败，由于DSSS Parameter Set长度为非标准长度

Failed to decode the CF Parameter Set IE: Invalid length.

解析CF Parameter Set IE失败，由于CF Parameter Set长度为非标准长度

Failed to decode the TIM IE: Invalid length.

解析TIM IE失败，由于TIM长度为非标准长度

Failed to decode the IBSS Parameter Set IE: Invalid length.

解析IBSS Parameter Set IE失败，由于IBSS Parameter Set长度为非标准长度

Failed to decode the Country IE: Invalid length.

解析Country IE失败，由于Country长度为非标准长度

Failed to decode the Hopping Pattern Parameters IE: Invalid length.

解析Hopping Pattern Parameters IE失败，由于Hopping Pattern Parameters长度为非标准长度

Failed to decode the BSS Load IE: Invalid length.

解析BSS Load IE失败，由于BSS Load长度为非标准长度

Failed to decode the Challenge text IE: The length exceeds the upper limit or is equal to 0.

解析Challenge text IE失败，由于Challenge text 长度大于上限 或 等于0

Failed to decode the Power Constraint IE: Invalid length.

解析Power Constraint IE失败，由于Power Constraint长度为非标准长度

Failed to decode the TPC Report IE: Invalid  length.

解析TPC Report IE失败，由于TPC Report长度为非标准长度

Failed to decode the Supported Channels IE: Invalid length.

解析Supported Channels IE失败，由于Supported Channels长度为非标准长度

Failed to decode the Quiet IE: Invalid  length.

无效Quiet长度：

解析后的长度为非标准长度

Failed to decode the ERP IE: Invalid length.

解析ERP IE失败，由于ERP长度为非标准长度

Failed to decode the HT Capabilities IE: Invalid length.

解析HT Capabilities IE失败，由于HT Capabilities长度为非标准长度

Failed to decode the RSN Capabilities IE: The length is below the lower limit.

解析RSN IE失败，由于RSN长度小于下限

Failed to decode the Extended Supported Rates IE: The length is equal to 0.

解析Extended Supported Rates IE失败，由于Extended Supported Rates长度为0

Failed to decode the HT Operation IE: Invalid length.

解析HT Operation IE失败，由于HT Operation长度为非标准长度

Failed to decode the 20/40 BSS Coexistence IE: Invalid length.

解析20/40 BSS Coexistence IE失败，由于20/40 BSS Coexistence长度为非标准长度

Failed to decode the 20/40 BSS Intolerant Channel Report IE: The length is smaller than 1.

解析20/40 BSS Intolerant Channel Report IE失败，由于20/40 BSS Intolerant Channel Report长度小于1

Failed to decode the Extended Capabilities IE: Invalid length.

解析Extended Capabilities IE失败，由于Extended Capabilities长度为非标准长度

Failed to decode the Power Capability IE: Invalid length.

解析Power Capability IE失败，由于Power Capability长度为非标准长度

APID: *APID[, *Radio ID*: RadioID, *Session ID*: SessionID*] Failed to process radio down event.

处理Radio Down事件失败

表1-3 debugging wlan client event命令输出信息描述表

字段

描述

Can\'t create BSS: The AP is in down state.

由于AP处于 Down状态，不满足创建BSS的条件

Can\'t create BSS: The service template is disabled.

由于服务模板未使能，不满足创建BSS的条件

APID *APID[, *Radio ID*RadioID, *WLAN ID*WlanID*] Received update BSS message.

成功收到Update BSS消息

APID *APID[, *Radio ID*RadioID*] Processed AP create event successfully.

处理AP Create事件成功

APID *APID[, *Radio ID*RadioID*] Processed radio down event successfully.

处理Radio Down事件成功

APID *APID[, *Radio ID*RadioID, *WLAN ID*WlanID*] BSS already exists.

BSS已经存在

APID *APID[, *Radio ID*RadioID*] Unsupported radio event *event*.

无效的Radio事件*event*

APID *APID*  Unsupported AP event *event*.

无效的AP事件*event*

APID: *APID* Received add wlan response message.

收到add wlan响应消息

APID: *APID* Received delete wlan response message.

收到delete wlan响应消息

BSSID: *BSSID* Sent add wlan message to downlink device.

成功发送下行add wlan消息

BSSID: *BSSID* Sent delete wlan message to downlink device.

成功发送下行delete wlan消息

MAC: *mac-address*, BSSID: *BSSID* Sent add mobile message to downlink device.

下同步add mobile消息成功

MAC: *mac-address*, BSSID: *BSSID* Received add mobile response message from downlink device.

收到下同步add mobile回应

MAC: *mac-address*, BSSID: *BSSID* Can\'t send add mobile message to uplink device: Reached the end of the IOCTL tunnel.

因为已经是顶层，不能发送上同步add mobile消息

MAC: *mac-address*, BSSID: *BSSID* Sent add mobile message to uplink device.

上同步add mobile消息成功

MAC: *mac-address*, BSSID: *BSSID* Received add mobile response message from the uplink device.

收到上同步add mobile回应

MAC: *mac-address*, BSSID: *BSSID* Sent delete mobile message to downlink device.

下同步delete mobile消息成功

APID :*APID* Received delete mobile response message from downlink device.

收到下同步delete mobile回应

MAC: *mac-address*, BSSID: *BSSID* Can\'t send delete mobile message to uplink device: Reached the end of the IOCTL tunnel.

因为已经是顶层，不能发送上同步delete mobile消息

MAC: *mac-address*, BSSID: *BSSID* Sent delete mobile message to uplink device.

上同步delete mobile消息成功

APID: *APID* Received delete mobile response message from uplink device.

收到上同步delete mobile回应

表1-4 debugging wlan client event命令输出信息描述表(仅FAT AP)

字段

描述

APID: *APID* Failed to reply to the broadcast probe request: The AP is not allowed to reply to broadcast probe requests.

AP设置不允许回复广播探查

APID *APID[, *Radio ID*RadioID*] Processed radio up event successfully.

处理Radio Up事件成功

APID *APID[, *Session ID*SessionID*] Processed AP down event successfully.

处理AP Down事件成功

BSSID: *BSSID* Processing update beacon.

处理Update beacon

表1-5 debugging wlan client fsm命令输出信息描述表

字段

描述

Changed the client\'s status from *state1* to*state2*.

Client状态从*state1*迁移到state2

state1和state2*取值*如下：

·UnAuth：未认证状态

·Auth：认证状态

·UserAuth：用户认证状态

·Run： Run状态

MAC: *MAC* BSSID: *BSSID* Received disassociation in the Run state: Reason code=*reasoncode*.

由于*reasoncode*，收到处于Run状态的客户端的去关联报文

【举例】

\# 打开stamgr模块的所有类型的调试开关。

\<Sysname\> debugging wlan client all

APID: *APID* Deleted an AP.

*[//[APID: 1]*]*删除AP成功。*

\# 打开stamgr模块的状态机相关的调试开关。

\<Sysname\> debugging wlan client fsm

Changed the client\'s state from UnAuth to**Auth.

*[//Client*]*的状态由未认证状态迁移到了认证状态。*

**WLAN接入 \-- WLAN接入调试命令 \-- debugging wlan client mac**

------------------------------------------------------------------------

【命令】

**[debugging wlan client mac ***mac-address*]

**[undo debugging wlan client mac **]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：客户端MAC地址。

【描述】

**[debugging wlan client mac**]用来基于客户端MAC地址打开调试开关。**undo debugging wlan client mac**用来关闭指定MAC地址的客户端的调试开关。

缺省情况下，客户端的调试信息开关处于关闭状态

表1-6 debugging wlan client mac error命令输出信息描述表（仅AC）

字段

描述

MAC: *mac-address*, BSSID: *BSSID* Failed to send add mobile message to the uplink device.

Add Mobile上行同步失败。

MAC: *mac-address*, BSSID: *BSSID* Failed to fill VLAN information to the add mobile message.

Add Mobile消息中填充VLAN信息失败。

MAC: *mac-address*, BSSID: *BSSID* Failed to process the open system authentication request: The BSS doesn\'t support open system authentication.

BSS 不支持开放式认证

MAC: *mac-address*, BSSID: *BSSID* Failed to authenticate the client: Radio obtaining failure.

由于获取Radio失败，导致认证失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process the open system authentication request: Wrong serial number.

收到的开放式认证报文序列号错误，处理认证请求报文失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process IE in the (re)association request.

处理（重）关联请求报文IE失败

MAC: *mac-address*, BSSID: *BSSID* Failed to associate with the AP: The number of clients exceeded the limit.

由于关联客户端数据达到上限，关联AP失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Run state.

Run状态下处理（重）关联请求失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Run state without sending (re)association response.

Run状态下处理（重）关联请求失败，但不发送（重）关联响应

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Auth state.

Auth状态下处理（重）关联请求失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Auth state without sending (re)association response.

Auth状态下处理（重）关联请求失败，但不发送（重）关联响应

MAC: *mac-address*, BSSID: *BSSID* Failed to get AID.

获取AID失败

MAC: *mac-address*, BSSID: *BSSID* Failed to update radio capabilities.

更新Radio能力集失败

MAC: *mac-address*, BSSID: *BSSID* Failed to send add mobile messages.

下发Add mobile失败

MAC: *mac-address*, BSSID: *BSSID* Received invalid frame in Unauth state.

在Unauth状态下收到错误报文

MAC: *mac-address*, BSSID: *BSSID* Frame check failed: Invalid frame length.

由于报文长度不合法，报文校验失败

MAC: *mac-address*, BSSID: *BSSID* Frame check failed: Invalid frame header.

由于报文头无效，报文校验失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Userauth state without sending (re)association response.

Userauth状态下处理（重）关联失败，但不发送（重）关联响应

MAC: *mac-address*, BSSID: *BSSID* Failed to release AID.

释放AID失败

MAC: *mac-address*, BSSID: *BSSID* Failed to process the authentication request: Unsupported algorithm.

算法不支持导致处理认证请求失败。

MAC: *mac-address*, BSSID: *BSSID* Failed to process the authentication request: Mismatched algorithm.

算法不匹配导致处理认证请求失败。

MAC: *mac-address*, BSSID: *BSSID* Failed to send the (re)association response.

发送（重）关联回应失败

表1-7 debugging wlan client mac event命令输出信息描述表（仅AC）

字段

描述

MAC: *mac-address*, BSSID: *BSSID* Allocated AID successfully.

分配AID成功

MAC: *mac-address*, BSSID: *BSSID* Processing (re)association request...

处理（重）关联报文

MAC: *mac-address*, BSSID: *BSSID* Processing association request in Auth state...

认证状态下处理关联报文

MAC: *mac-address*, BSSID: *BSSID* Processed association request successfully, and sent association response.

处理关联请求成功，并发送关联回应

MAC: *mac-address*, BSSID: *BSSID* Processed (re)association request successfully when the client was in Run state .

用户处于Run状态下，（重）关联请求处理成功

MAC: *mac-address*, BSSID: *BSSID* Processed (re)association request successfully when the client was in Auth state.

用户处于Auth状态下，（重）关联请求处理成功

MAC: *mac-address*, BSSID: *BSSID* Checking association load of the device...

检查设备的关联负载

MAC: *mac-address*, BSSID: *BSSID* Failed to process (re)association request in Run state.

Userauth状态下处理（重）关联请求失败

表1-8 debugging wlan client timer命令输出信息描述表（仅AC）

字段

描述

MAC: *mac-address*, BSSID: *BSSID* Keepalive timer expired.

保活定时器超时

MAC: *mac-address*, BSSID: *BSSID* Idle timer expired.

闲置定时器超时

MAC: *mac-address*, BSSID: *BSSID* Userauth state timer expired.

用户认证状态状态定时器超时

MAC: *mac-address*, BSSID: *BSSID* Auth state timer expired.

认证状态状态定时器超时

MAC: *mac-address*, BSSID: *BSSID* Unauth state timer expired.

未认证状态状态定时器超时

MAC: *mac-address*, BSSID: *BSSID* Failed to process authentication request: The client is being deleted.

Client正在删除中，处理认证请求失败

MAC: *mac-address*, BSSID: *BSSID* Created keepalive timer.

创建保活定时器

MAC: *mac-address*, BSSID: *BSSID* Created idle timer.

创建闲置定时器

MAC: *mac-address*, BSSID: *BSSID* Created state timer.

创建状态定时器

MAC: *mac-address*, BSSID: *BSSID* Refreshed state timer.

刷新状态定时器

MAC: *mac-address*, BSSID: *BSSID* Refreshed keepalive timer.

刷新保活定时器

MAC: *mac-address*, BSSID: *BSSID* Deleted state timer.

删除状态定时器

MAC: *mac-address*, BSSID: *BSSID* Refreshed idle timer.

刷新闲置定时器

表1-9 debugging wlan client fsm命令输出信息描述表（仅AC）

字段

描述

MAC: *mac-address*, BSSID: *BSSID* Client state: Unauth.

Client状态： 未认证

MAC: *mac-address*, BSSID: *BSSID* Client state: Auth.

Client状态：已认证

MAC: *mac-address*, BSSID: *BSSID* Client state: Userauth.

Client状态：用户认证

MAC: *mac-address*, BSSID: *BSSID* Client state: Run.

Client状态： Run

MAC: *mac-address*, BSSID: *BSSID* Client went online. Status changed to Run.

Client已经上线，状态迁移到了Run

MAC: *mac-address*, BSSID: *BSSID* Client went offline. Status changed to Unauth.

Client已经下线，状态迁移到了Unauth

MAC: *mac-address*, BSSID: *BSSID* Received deauthentication or disassociation request from client in *state* state: Reason code=*Reasoncode*.

收到处于当前状态的Client发来的含有原因码的去认证/去关联报文

【举例】

\# 打开MAC地址为 05-0A-31-22-11-11的无线客户端的调试开关。

\<Sysname\> debugging wlan client mac 05-0A-31-22-11-11

MAC: *05-0A-31-22-11-11*, BSSID: *ab-ab-ab-ab-ab-ab* Created idle timer.

*[//BSSID*]*为ab-ab-ab-ab-ab-ab的无线服务为MAC地址为05-0A-31-22-11-11的用户创建了闲置定时器。*
