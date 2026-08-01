<!-- CMD-INDEX
  cac policy                          | AC设备：Radio视图/AP组Radio视图 | L11
  edca radio                          |                  | L97
  reset wlan wmm                      | 用户视图             | L249
  svp                                 | AC设备：Radio视图/AP组Radio视图 | L287
  wmm                                 | AC设备：Radio视图/AP组Radio视图 | L371
  wmm edca client（ac-be和ac-bk）        |                  | L455
  wmm edca client（ac-vo和ac-vi）        |                  | L583
-->

**WLAN QoS \-- WLAN QoS命令 \-- cac policy**

------------------------------------------------------------------------

**[cac policy**]命令用来配置开启CAC（Connect Admission Control，连接准入控制）功能后使用的接入控制策略。

**[undo cac policy**]命令用来恢复缺省情况。

【命令】

**[cac policy** { **channelutilization** [ *channelutilization-value*  \| **client**  *users-number*  }]]

**[undo cac policy**]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，使用基于客户端数量的CAC策略，客户端数量为20。

·FAT AP设备：Radio接口视图下，使用基于客户端数量的CAC策略，客户端数量为20。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[channelutilization**]：CAC使用基于信道利用率的准入策略。

*[channelutilization-value*]：允许接入的信道最大利用率，即单位时间内，允许接入AC-VO和AC-VI优先级的业务流占用信道的有效时间与客户端回复的响应帧中Medium Time字段中携带值的百分比，有效时间为可用于实际收发数据的时间。取值范围为0～100，为百分比形式，缺省值为65%。

**[client**]：CAC使用基于客户端数量的准入策略。

*[users-number*]：允许接入的客户端的最大个数，取值范围为0～124。如果一个客户端同时接入AC-VO和AC-VI优先级业务流，接入客户端的个数按1计算。

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置开启CAC功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为70％。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 cac policy channelutilization 70

·AC设备举例（AP组Radio视图）

\# 配置开启CAC功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为70％。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1cac policy channelutilization 70

·FAT AP设备举例

\# 配置开启CAC功能后使用的基于信道利用率的接入控制策略，允许信道最大利用率为70％。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 cac policy channelutilization 70

**WLAN QoS \-- WLAN QoS命令 \-- edca radio**

------------------------------------------------------------------------

**[edca radio**]命令用来配置Radio的工作参数。

**[undo edca radio**]命令用来恢复缺省情况。

【命令】

**[edca radio**[ { **ac-be** \| **ac-bk** \| **ac-vi** \| **ac-vo** } { **aifsn** *aifsn-value* \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **noack** \| **txoplimit** *txoplimit-value* } \*]]

**[undo edca radio**[ { **ac-be** \| **ac-bk** \| **ac-vi** \| **ac-vo** } { **aifsn** \| **all** \| **ecw** \| **noack** \| **txoplimit** }]]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，如[表]1-1(?1825905523#_Ref397345644)所示。

·FAT AP设备：Radio接口视图下，如表1-1(?1825905523#_Ref397345644)所示。

表1-1 Radio的工作参数的缺省值

AC

AIFSN

ECWmin

ECWmax

TXOP Limit

AC-BK

7

4

10

0

AC-BE

3

4

6

0

AC-VI

1

3

4

94

AC-VO

1

2

3

47

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac-be**]：AC-BE（尽力而为流）优先级队列。

**[ac-bk**]：AC-BK（背景流）优先级队列。

**[ac-vi**]：AC-VI（视频流）优先级队列。

**[ac-vo**]：AC-VO（语音流）优先级队列。

**[all**]：所有EDCA参数。

**[aifsn*** aifsn-value*]：仲裁帧间隙数，取值范围为1～15。

**[ecwmin*** ecwmin-value*]：最小竞争窗口指数形式，取值范围为0～15。

**[ecwmax*** ecwmax-value*]：最大竞争窗口指数形式，取值范围为0～15。**ecwmax**值必须大于等于**ecwmin**值。

**[noack**]：指定AC使用的ACK策略是No ACK。缺省ACK策略为No ACK。

**[txoplimit*** txoplimit-value*]：EDCA的TXOP Limit参数，以32微秒为单位，取值范围为0～65535，取值为0表示只允许传输一个MPDU。

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

对于802.11b类型的Radio，建议将AC-BK、AC-BE、AC-VI、AC-VO的TXOP Limit参数的值分别配置为0、0、188和102。

【举例】

·AC设备举例（Radio视图）

\# 配置Radio使用的AC-VO队列的AIFSN值为2。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 edca radio ac-vo aifsn 2

·AC设备举例（AP组Radio视图）

\# 配置Radio使用的AC-VO队列的AIFSN值为2。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1edca radio ac-vo aifsn 2

·FAT AP设备举例

\# 配置Radio使用的AC-VO队列的AIFSN值为2。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 edca radio ac-vo aifsn 2

**WLAN QoS \-- WLAN QoS命令 \-- reset wlan wmm**

------------------------------------------------------------------------

**[reset wlan wmm**]命令用来清空WMM统计信息。

【命令】

**[reset wlan wmm **[{ **client** { **all** \| **ap** *ap-name* \| **mac-address** *mac-address* } \| **radio** { **all** \| **ap** *ap-name* } }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[client**]：清除客户端的WMM信息。

**[all**]：清除所有Radio或客户端的WMM信息。

**[ap** *ap-name*]：指定AP的名字，为1～63个字符的字符串，不区分大小写。

**[mac-address*** mac-address*]：清除指定MAC地址的客户端WMM信息。

**[radio**]：清除Radio的WMM信息。

【举例】

\# 清空WMM统计信息。

\<Sysname\> reset wlan wmm radio all

**WLAN QoS \-- WLAN QoS命令 \-- svp**

------------------------------------------------------------------------

**[svp map-ac**]命令用来配置SVP映射功能，即将SVP报文放入指定的AC队列中。

**[undo svp map-ac**]命令用来恢复缺省情况。

【命令】

**[svp map-ac**[ { **ac-vi** \| **ac-vo** }]]

**[undo svp map-ac**]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，SVP映射功能处于关闭状态。

·FAT AP设备：Radio接口视图下，SVP映射功能处于关闭状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac-vi**]：AC-VI（视频流）优先级队列。

**[ac-vo**]：AC-VO（语音流）优先级队列。

【使用指导】

SVP映射只针对非WMM客户端接入，对WMM客户端不起作用。

AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置SVP映射功能，即将SVP报文放入AC-VO队列中。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 svp map-ac ac-vo

·AC设备举例（AP组Radio视图）

\# 配置SVP映射功能，即将SVP报文放入AC-VO队列中。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 svp map-ac ac-vo

·FAT AP设备举例

\# 配置SVP映射功能，即将SVP报文放入AC-VO队列中。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 svp map-ac ac-vo

**WLAN QoS \-- WLAN QoS命令 \-- wmm**

------------------------------------------------------------------------

**[wmm**]命令用来开启WMM功能。

**[undo** **wmm**]命令用来恢复缺省情况。

【命令】

**[wmm**[ { **disable** \| **enable** }]]

**[undo wmm**]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，WMM功能处于开启状态。

·FAT AP设备：Radio接口视图下，WMM功能处于开启状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disable**]：关闭WMM功能。

**[enable**]：开启WMM功能。

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

协议要求802.11n的客户端必须支持WLAN QoS，所以当Radio工作在802.11an或802.11gn的情况下，WMM功能必须开启，否则可能会导致关联后的802.11n的客户端无法通信

【举例】

·AC设备举例（Radio视图）

\# 关闭WMM功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 wmm disable

·AC设备举例（AP组Radio视图）

\# 关闭WMM功能。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 wmm disable

·FAT AP设备举例

\# 关闭WMM功能。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 wmm disable

**WLAN QoS \-- WLAN QoS命令 \-- wmm edca client（ac-be和ac-bk）**

------------------------------------------------------------------------

**[wmm edca client**]命令用来配置Radio和客户端的协商参数。

**[undo wmm edca client**]命令用来恢复缺省情况。

【命令】

**[wmm edca client**[ { **ac-be** \| **ac-bk** } { **aifsn** *aifsn-value* \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **txoplimit** *txoplimit-value* } \*]]

**[undo wmm edca client**[ { **ac-be** \| **ac-bk** } { **aifsn** \| **all** \| **ecw** \| **txoplimit** }]]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，如[表]1-2(?-154405993#_Ref171155503)所示。

·FAT AP设备：Radio接口视图下，如表1-2(?-154405993#_Ref171155503)所示。

表1-2 Radio和客户端的协商参数的缺省值

AC

AIFSN

ECWmin

ECWmax

TXOP Limit

AC-BK

7

4

10

0

AC-BE

3

4

10

0

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac-be**]：AC-BE（尽力而为流）优先级队列。

**[ac-bk**]：AC-BK（背景流）优先级队列。

**[all**]：所有EDCA参数。

**[aifsn*** aifsn-value*]：仲裁帧间隙数，取值范围为2～15。

**[ecwmin*** ecwmin-value*]：最小竞争窗口指数形式，取值范围为0～15。

**[ecwmax*** ecwmax-value*]：最大竞争窗口指数形式，取值范围为0～15。**ecwmax**值必须大于等于**ecwmin**值。

**[txoplimit*** txoplimit-value*]：传输机会限制，以32微秒为单位，取值范围为0～65535。取值为0表示只允许传输一个MPDU。

【使用指导】

·AC设备：Radio视图下配置的优先级高于AP组的配置。

·如果所有客户端都是802.11b客户端，建议将AC-BK、AC-BE的TXOP Limit参数的值分别配置为0、0。

·如果网络中同时存在802.11b客户端和802.11g客户端，则建议按TXOP Limit参数值使用[表]1-2(?-154405993#_Ref171155503)中缺省值。

【举例】

·AC设备举例（Radio视图）

\# 配置AC-BE的AIFSN值为5。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 wmm edca client ac-be aifsn 5

·AC设备举例（AP组Radio视图）

\# 配置AC-BE的AIFSN值为5。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 wmm edca client ac-be aifsn 5

·FAT AP设备举例

\# 配置AC-BE的AIFSN值为5。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 wmm edca client ac-be aifsn 5

**WLAN QoS \-- WLAN QoS命令 \-- wmm edca client（ac-vo和ac-vi）**

------------------------------------------------------------------------

**[wmm edca client**]命令用来配置Radio和客户端的协商参数。

**[undo wmm edca client**]命令用来恢复缺省情况。

【命令】

**[wmm edca client**[ { **ac-vi** \| **ac-vo** } { **aifsn** *aifsn-value* \| **cac** \| **ecw** **ecwmin** *ecwmin-value* **ecwmax** *ecwmax-value* \| **txoplimit** *txoplimit-value* } \*]]

**[undo wmm edca client**[ { **ac-vo** \| **ac-vi** } { **aifsn** \| **all** \| **cac** \| **ecw** \| **txoplimit** }]]

【缺省情况】

·AC设备：Radio视图下，继承AP组配置。

·AC设备：AP组Radio视图下，如[表]1-3(?-1211716778#_Ref168914192)所示。

·FAT AP设备：Radio接口视图下，如表1-3(?-1211716778#_Ref168914192)所示。

表1-3 Radio和客户端的协商参数的缺省值

AC

AIFSN

ECWmin

ECWmax

TXOP Limit

AC-VI

2

3

4

94

AC-VO

2

2

3

47

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ac-vi**]：AC-VI（视频流）优先级队列。

**[ac-vo**]：AC-VO（语音流）优先级队列。

**[aifsn*** aifsn-value*]：仲裁帧间隙数，取值范围为2～15。

**[all**]：所有EDCA参数。

**[cac**]：支持客户端使用连接准入控制。AC-VO和AC-VI支持CAC，缺省为关闭。

**[ecwmin*** ecwmin-value*]：最小竞争窗口指数形式，取值范围为0～15。

**[ecwmax*** ecwmax-value*]：最大竞争窗口指数形式，取值范围为0～15。**ecwmax**值必须大于等于**ecwmin**值。

**[txoplimit*** txoplimit-value*]：传输机会限制，以32微秒为单位，取值范围为0～65535。取值为0表示只允许传输一个MPDU。

【使用指导】

·AC设备：Radio视图下配置的优先级高于AP组的配置。

·如果所有上线客户端都是802.11b客户端，建议将AC-VI、AC-VO的TXOP Limit参数的值分别配置为188、102。

·如果网络中同时存在802.11b客户端和802.11g客户端，则建议按TXOP Limit参数值使用[表]1-3(?-1211716778#_Ref168914192)中缺省值。

·如果某优先级队列的CAC功能被启动，则高于此优先级队列的CAC功能会同时被启用。例如，使用**wmm edca client**命令启动AC-VI优先级CAC功能，则AC-VO优先级也同时启动CAC功能，但是，启动AC-VO优先级的CAC功能，AC-VI优先级的CAC功能不会被启用。

【举例】

·AC设备举例（Radio视图）

\# 配置AC-VO的AIFSN值为3。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 wmm edca client ac-vo aifsn 3

·AC设备举例（AP组Radio视图）

\# 配置AC-VO的AIFSN值为3。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 wmm edca client ac-vo aifsn 3

·FAT AP设备举例

\# 配置AC-VO的AIFSN值为3。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 wmm edca client ac-vo aifsn 3

