
**射频资源测量 \-- 射频资源测量配置命令 \-- display wlan measure-report**

------------------------------------------------------------------------

**[display wlan measure-report**]命令用于显示客户端的测量报告信息。

【命令】

**[display wlan measure-report ap ***ap-name*** radio ***radio-number***** **client mac-address** *mac-address* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ap*** ap-name*]：指定客户端关联的AP，为1～63个字符的字符串，不区分大小写。

**[radio*** radio-number*]：指定AP的射频号。取值范围与AP设备的型号有关，请以设备的实际情况为准。

**[client**]**：**指定客户端的MAC地址。

**[mac-address ***mac-address*]：客户端的MAC地址，格式为H-H-H。

【使用指导】

如果不指定**client mac-address**参数，将显示所有客户端的测量信息。

**射频资源测量 \-- 射频资源测量配置命令 \-- measure**

------------------------------------------------------------------------

**[measure**]命令用于开启测量功能。

**[undo measure**]命令用于恢复缺省情况。

【命令】

**[measure ****[all **[\| ]**link**[ \| **neighbor** \| **radio** \| **spectrum** \| **tpc** } { **enable** \| **disable** }]]

**[undo measure**]

【缺省情况】]

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，测量功能处于关闭状态。

FAT AP设备：Radio接口视图下，测量功能处于关闭状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有测量。

**[link**]：链路测量，测量针对链路测量请求帧的RCPI、RSNI和链路冗余等信息。

**[neighbor**]：邻居测量，测量邻居AP的信道号、BSSID等信息。

**[radio**]：射频测量，包括信道负载测量、噪声分布测量、Beacon测量、Frame测量、STA统计测量、位置信息测量和传输流测量。

**[spectrum**]：频谱测量，包括Basic测量、CCA测量和RPI测量。

**[tpc**]：传输功率控制测量，测量客户端的链路冗余和传输功率。

**[enable**]：开启测量。

**[disable**]：关闭测量。

【使用指导】

·只有开启射频资源测量功能，link、neighbor、radio测量功能才会生效。

·只有开启频谱管理功能，spectrum、tpc测量功能才会生效。有关频谱管理功能相关配置的详细介绍请参见"WLAN配置指导"中的"WLAN RRM"。

【举例】

·AC设备举例

\# 开启频谱测量。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 measure spectrum enable

·FAT AP设备举例

\# 开启频谱测量。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 measure spectrum enable

【相关命令】

·**measure-duration**

·**measure-interval**

·**resource-measure**

·**spectrum-management**

**射频资源测量 \-- 射频资源测量配置命令 \-- measure-duration**

------------------------------------------------------------------------

**[measure-duration**]命令用于配置测量持续时间。

**[undo measure-duration**]命令用于恢复缺省情况。

【命令】

**[measure-duration ***time*]

**[undo measure-duration**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，测量持续时间为500TU。

FAT AP设备：Radio接口视图下，测量持续时间为500TU。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[time*]：测量持续时间，取值范围0～1000，单位为TU（Time Unit，1TU=1024微秒）。

【使用指导】

开启测量功能后，在AP向客户端发送的测量请求报文中携带配置的测量持续时间。

【举例】

·AC设备举例

\# 配置测量持续时间为512TU。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 measure-duration 512

·FAT AP设备举例

\# 配置测量持续时间为512TU。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 measure-duration 512

【相关命令】

·**measure**

·**measure-interval**

**射频资源测量 \-- 射频资源测量配置命令 \-- measure-interval**

------------------------------------------------------------------------

**[measure-interval**]命令用于配置发送测量请求的时间间隔。

**[undo measure-interval**]命令用于恢复缺省情况。

【命令】

**[measure-interval ***value*]

**[undo measure-interval**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，发送测量请求间隔时间为30秒。

FAT AP设备：Radio接口视图下，发送测量请求间隔时间为30秒。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[value*]：发送测量请求的时间间隔，取值范围30～60，单位为秒。

【使用指导】

开启测量功能后，AP以配置的时间间隔定时向客户端发送的测量请求报文。

【举例】

·AC设备举例

\# 配置发送测量请求间隔时间为35秒。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 measure-interval 35

·FAT AP设备举例

\# 配置发送测量请求间隔时间为35秒。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 measure-interval 35

【相关命令】

·**measure**

·**measure-duration**

**射频资源测量 \-- 射频资源测量配置命令 \-- resource-measure**

------------------------------------------------------------------------

**[resource-measure**]** enable**命令用于开启射频资源测量功能。

**[resource-measure**]** disable**命令用于关闭射频资源测量功能。

**[undo **]**resource-measure**命令用于恢复缺省情况。

【命令】

**[resource measure**]****[{ **enable** \| **disable** }]

**[undo **]**resource measure**

【缺省情况】

射频资源测量功能处于关闭状态。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启射频资源测量功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 2

Sysname-wlan-ap-ap1-radio-2 resource-measure enable

【使用指导】

开启射频资源测量功能后：

·AP发送的Beacon、Probe Response和Association Response、Reassociation Response帧中，能力集字段中的Radio Measurement位会被置位，并携带AP支持的射频资源测量能力信息，用于告知客户端，AP支持射频资源测量，以及支持的测量类型。

·AP通过定期发送Measurement Pilot帧协助客户端更快地扫描到AP。Measurement Pilot报文可视为轻量级的Beacon帧，其发送的频率比Beacon帧高，但携带的信息比Beacon帧少。

**射频资源测量 \-- 射频资源测量配置命令 \-- rm-capability mode**

------------------------------------------------------------------------

**[rm-capability mode**]命令用于配置对客户端射频测量能力集的检查模式。

**[undo rm-capability mode**]命令用于恢复缺省情况。

【命令】

**[rm-capability mode **]**[none **[\| ]**partial**}

**[undo rm-capability mode**]

【缺省情况】]

不检查客户端射频测量能力集。

【视图】

Radio视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：完全匹配模式。只有客户端的射频测量能力集与AP的能力集全部匹配，才允许客户端上线，否则，不允许客户端上线。

**[none**]：不检查模式，即不检查客户端射频测量能力集。

**[partial**]：部分匹配模式。配置部分匹配模式时，客户端的射频测量能力集与设备的能力集只要有一个匹配，则允许客户端上线，否则，不允许客户端上线。

【使用指导】

只有开启射频资源测量功能，射频测量能力集检查功能才会生效。

【举例】

\# 配置对客户端射频测量能力集的检查模式为部分匹配模式。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 2

Sysname-wlan-ap-ap1-radio-2 resource-measure enable

Sysname-wlan-ap-ap1-radio-2 rm-capability mode partial

【相关命令】

·**resource-measure**

