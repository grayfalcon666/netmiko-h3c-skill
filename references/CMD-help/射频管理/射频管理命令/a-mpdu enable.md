
**射频管理 \-- 射频管理命令 \-- a-mpdu enable**

------------------------------------------------------------------------

**[a-mpdu enable**]命令用来开启A-MPDU功能。

**[a-mpdu disable**]命令用来关闭A-MPDU功能。

**[undo a-mpdu**]命令用来恢复缺省情况。

【命令】

**[a-mpdu**[ { **disable** \| **enable** }]]

**[undo a-mpdu**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，A-MPDU功能处于开启状态。

FAT AP设备：Radio接口视图下，A-MPDU功能处于开启状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令仅对802.11n或802.11ac模式的Radio有效。当进行Radio模式切换时，Radio会恢复该功能的缺省情况。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 关闭A-MPDU功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 a-mpdu disable

·FAT AP设备举例

\# 关闭A-MPDU功能。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 a-mpdu disable

**射频管理 \-- 射频管理命令 \-- a-msdu enable**

------------------------------------------------------------------------

**[a-msdu enable**]命令用来开启A-MSDU功能。

**[a-msdu disable**]命令用来关闭A-MSDU功能。

**[undo a-msdu**]命令用来恢复缺省情况。

【命令】

**[a-msdu**[ { **disable** \| **enable** }]]

**[undo a-msdu**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，A-MSDU功能处于开启状态。

FAT AP设备：Radio接口视图下，A-MSDU功能处于开启状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令仅对802.11n和802.11ac模式的Radio有效。在进行Radio模式切换的时候，设备会恢复该功能在该模式下的缺省情况。

·目前，设备只支持接收A-MSDU报文，不支持发送A-MSDU。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 关闭A-MSDU功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 a-msdu disable

·FAT AP设备举例

\# 关闭A-MSDU功能。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 a-msdu disable

**射频管理 \-- 射频管理命令 \-- ap-model**

------------------------------------------------------------------------

**[ap-model**]命令用来创建并进入AP组下的AP型号视图。

**[undo ap-model**]命令用来删除组下AP型号视图及AP型号下的配置。

【命令】

**[ap-model ***ap-model*]

**[undo ap-model ***ap-model*]

【缺省情况】

没有AP型号配置。

【视图】

AP组视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ap-model*]：AP型号名。

【使用指导】

在ap-model视图下可以进入radio视图，在此视图下可以配置radio的物理参数。

【举例】

\# 在AP组视图下设置AP的型号为WA4620i-ACN。

\<System\> system-view

System wlan ap-group group1

System-wlan-ap-group-group1 ap-model WA4620i-ACN

System-wlan-ap-group-group1-apmodel-WA4620i-ACN

**射频管理 \-- 射频管理命令 \-- beacon-interval**

------------------------------------------------------------------------

**[beacon-interval**]命令用来配置发送Beacon帧的时间间隔。

**[undo beacon-interval**]命令用来恢复缺省情况。

【命令】

**[beacon-interval ***interval*]

**[undo beacon-interval**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置

AC设备：AP组Radio视图下，发送Beacon帧的时间间隔为100TU。

FAT AP设备：Radio接口视图下，发送Beacon帧的时间间隔为100TU。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[interval*]：发送Beacon帧的时间间隔，取值范围为32～8191，单位为TU（Time Unit，1TU=1024微秒）。

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置发送Beacon帧的时间间隔为1000TU。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 beacon-interval 1000

·AC设备举例（AP组Radio视图）

\# 配置发送Beacon帧的时间间隔为1000TU。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 beacon-interval 1000

·FAT AP设备举例

\# 配置发送Beacon帧的时间间隔为1000TU。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11g

Sysname-WLAN-Radio1/0/2 beacon-interval 1000

**射频管理 \-- 射频管理命令 \-- channel**

------------------------------------------------------------------------

**[channel**]命令用来配置射频工作信道。

**[undo** **channel**]命令用来恢复缺省情况。

【命令】

**channel**[ [{ **lock** \| **unlock** } ]}

**[undo channel**]

【缺省情况】]

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，工作信道为**auto**模式，信道为unlock模式。

FAT AP设备：Radio接口视图下，工作信道为**auto**模式，信道为unlock模式。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[channel-number*]：手动配置的射频工作信道。取值范围由国家码和射频类型决定。

**[auto lock**]：自动选择信道并加锁模式，由设备根据实际环境自动选择最优信道，并将该信道锁定。

**[auto unlock**]：自动选择信道并解锁模式。由设备根据实际环境自动选择最优信道，并将该信道设置为无锁模式。

【使用指导】

·**channel** *channel-number*、**chanel auto lock**和**channel auto unlock**此三条命令互斥，任何一条命令都可以将前一条配置覆盖。

·在手工指定工作信道模式时，如果在当前工作信道上发现雷达信号，则设备会立即将工作信道调整至其他信道。雷达信号消失后，设备会恢复到指定的工作信道上。

·在自动选择信道模式上，无论是信道的加锁与否，如果在当前工作信道上发现雷达信号，则设备会立即将工作信道调整至其他信道。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置射频工作信道号为149。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 channel 149

·AC设备举例（AP组Radio视图）

\# 配置射频工作信道号为149。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 channel 149

·FAT AP设备举例

\# 配置射频工作信道号为6。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 channel 6

**射频管理 \-- 射频管理命令 \-- channel band-width**

------------------------------------------------------------------------

**[channel band-width**]命令用来设置带宽模式。

**[undo channel band-width**]命令用来恢复缺省情况**。**

【命令】

**[channel band-width **[{ **20** \| **40** \| **80** \| **auto-switch** }]]

**[undo channel band-width**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，802.11ac射频模式的带宽模式为80MHz，802.11an射频模式的带宽模式为40MHz，802.11gn射频模式的带宽模式为20MHz。

FAT AP设备：Radio接口视图下，802.11ac射频模式的带宽模式为80MHz，802.11an射频模式的带宽模式为40MHz，802.11gn射频模式的带宽模式为20MHz。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[20**]：将带宽模式设置成20MHz。

**[40**]：将带宽模式设置成40MHz。

**[80**]：将带宽模式设置成80MHz。

**[auto-switch**]：允许在20MHz和40MHz之间自动切换。仅当Radio模式为dot11gn模式时，支持配置本参数。

【使用指导】

该命令仅对802.11n或802.11ac类型的Radio有效。在进行Radio模式切换的时候，带宽恢复切换模式下的缺省值。

在指定带宽为40MHz情况下，如果找到两条可以绑定到一起的相邻信道，那么使用40MHz带宽；如果找不到可以绑定的相邻信道，那么实际只能使用20MHz带宽。

在指定带宽为80MHz情况下，如果找到一组可以绑定为80MHz的相邻信道，那么使用80MHz带宽；如果找不到可以绑定为80MHz的一组信道，但可以找到两条可以绑定为40MHz带宽的信道，那么使用40MHz带宽；如果找不到可以绑定的信道，那么实际只能使用20MHz带宽。

【举例】

\# 配置40MHz带宽。

\<AC\> system-view

AC wlan ap ap1 model WA2620i-AGN

AC-wlan-ap-ap1 radio 1

AC-wlan-ap-ap1-radio-1 type dot11an

AC-wlan-ap-ap1-radio-1 channel band-width 40

**射频管理 \-- 射频管理命令 \-- client dot11n-only enable**

------------------------------------------------------------------------

**[client dot11n-only enable**]命令用来开启仅允许802.11n或802.11ac用户接入的功能。

**[client dot11n-only disable**]命令用来关闭仅允许802.11n或802.11ac用户接入的功能。

**[undo client dot11n-only**]命令用来恢复缺省情况。

【命令】

**[client dot11n-only**[ { **disable** \| **enable** }]]

**[undo client dot11n-only**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，802.11an类型的Radio允许802.11a、802.11an、802.11n、802.11ac用户接入；802.11gn类型的Radio允许802.11b/g、802.11gn、802.11n、802.11ac用户接入；802.11ac类型的Radio允许802.11a、802.11an、802.11ac用户接入。

FAT AP设备：Radio接口视图下，802.11an类型的Radio允许802.11a、802.11an、802.11n、802.11ac用户接入；802.11gn类型的Radio允许802.11b/g、802.11gn、802.11n、802.11ac用户接入；802.11ac类型的Radio允许802.11a、802.11an、802.11ac用户接入。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·当执行**client dot11n-only enable**命令后，只有802.11n或802.11ac的客户端才能接入AP。如果用户需要兼容802.11a/b/g的客户端，同时还要接入802.11n或802.11ac的客户端，则必须关闭**client dot11n-only**命令。

·配置**client dot11n-only enable**命令前，需要先配置802.11n基本MCS的最大索引。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 开启仅允许802.11n或802.11ac用户接入的功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 client dot11n-only enable

·FAT AP设备举例

\# 开启仅允许802.11n或802.11ac用户接入的功能。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 client dot11n-only enable

**射频管理 \-- 射频管理命令 \-- display wlan ap-model**

------------------------------------------------------------------------

**[display wlan ap-model**]命令用来显示AP型号的信息。

【命令】

**[display wlan ap-model**[ { **all** \| **name** *model-name* }]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[all**]：显示所有AP型号的信息。

**[name ***model-name*]：显示指定AP型号的信息。

【举例】

\<Sysname\> display wlan ap-model name WA2620i-AGN

AP model        : WA2620i-AGN

Alias           : WA2620i-AGN

Vendor name     : H3C

Vendor ID       : 25506

Radio count     : 2

 Radio 1:

  Mode          : 802.11a, 802.11an

  Default mode  : 802.11an

  BSS count     : 16

 Radio 2:

  Mode          : 802.11b, 802.11g, 802.11gn

  Default mode  : 802.11gn

  BSS count     : 16

表1-1 display wlan ap-model命令显示信息描述表

字段

描述

AP model

AP 型号名

Alias

AP型号别名

Vendor name

产商名

Vendor ID

产商ID

Radio count

射频个数

Mode

支持的射频类型

Default mode

默认的射频类型

BSS count

一个Radio可以创建的最大基本服务集个数

**射频管理 \-- 射频管理命令 \-- distance**

------------------------------------------------------------------------

**[distance**]命令用来配置射频可覆盖的最远距离。

**[undo distance**]命令用来恢复缺省情况。

【命令】

**[distance **]*distance*

**[undo distance**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，射频可覆盖的最远距离为1公里。

FAT AP设备：Radio接口视图下，射频可覆盖的最远距离为1公里。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[distance*]：射频可覆盖的最远距离，取值范围为1～40，单位为公里。

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置射频可覆盖的最远距离为5公里。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 distance 5

·AC设备举例（AP组Radio视图）

\# 配置射频可覆盖的最远距离为5公里。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 distance 5

·FAT AP设备举例

\# 配置射频可覆盖的最远距离为5公里。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11g

Sysname-WLAN-Radio1/0/2 distance 5

**射频管理 \-- 射频管理命令 \-- dot11n mandatory maximum-mcs**

------------------------------------------------------------------------

**[dot11n mandatory maximum-mcs**]命令用来配置射频802.11n的基本MCS最大索引。

**[undo dot11n mandatory maximum-mcs**]命令用来恢复缺省情况。

【命令】

**[dot11n mandatory maximum-mcs ***index*]

**[undo dot11n mandatory maximum-mcs**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，未配置任何802.11n的基本MCS速率集。

FAT AP设备：Radio接口视图下，未配置任何802.11n的基本MCS速率集。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index*]：指定射频802.11n基本MCS速率集的最大MCS索引值，取值范围为0～76。

【使用指导】

·如果用户需要在指定Radio下配置**[client dot11n-only**]** enable**命令，则必须配置802.11n基本MCS最大索引。

·如果用户需要在指定Radio下配置**dot11n multicast-mcs**命令，则必须配置802.11n基本MCS最大索引。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 设置射频802.11n基本MCS速率集的最大MCS索引为14。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 dot11n mandatory maximum-mcs 14

·FAT AP设备举例

\# 设置射频802.11n基本MCS速率集的最大MCS索引为14。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 dot11n mandatory maximum-mcs 14

**射频管理 \-- 射频管理命令 \-- dot11n multicast-mcs**

------------------------------------------------------------------------

**[dot11n multicast-mcs**]命令用来配置射频802.11n的组播MCS索引。

**[undo dot11n multicast-mcs**]命令用来恢复缺省情况。

【命令】

**[dot11n multicast-mcs ***index*]

**[undo dot11n multicast-mcs**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，未配置任何802.11n组播MCS索引。

FAT AP设备：Radio接口视图下，未配置任何802.11n组播MCS索引。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[Index*]：指定射频802.11n组播MCS索引值，取值范围为0～76。

【使用指导】

·当接入的客户端都是802.11n客户端时，组播MCS索引才会生效。

·当存在非802.11n客户端时，只能选用基础模式的组播速率，即802.11a/b/g的组播速率。

·组播MCS索引起作用时，无论带宽模式设置的是20MHz模式还是40MHz模式，统一采用20MHz模式对应的速率。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 设置射频802.11n组播MCS索引为14：

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 dot11n mandatory maximum-mcs 15

Sysname-wlan-ap-ap1-radio-1 dot11n multicast-mcs 14

·FAT AP设备举例

\# 设置射频802.11n组播MCS的最大索引为14。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 dot11n mandatory maximum-mcs 15

Sysname-WLAN-Radio1/0/1 dot11n multicast-mcs 14

**射频管理 \-- 射频管理命令 \-- dot11n support maximum-mcs**

------------------------------------------------------------------------

**[dot11n support maximum-mcs**]命令用来配置射频802.11n支持MCS的最大索引。

**[undo dot11n support maximum-mcs**]命令用来恢复缺省情况。

【命令】

**[dot11n support maximum-mcs ***index*]

**[undo dot11n support maximum-mcs**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，802.11n支持MCS最大索引值为76。

FAT AP设备：Radio接口视图下，802.11n支持MCS最大索引值为76。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[index*]：指定射频802.11n支持MCS的最大索引值，取值范围为0～76。

【使用指导】

用该命令指定的802.11n支持MCS最大索引不能小于**dot11n mandatory maximum-mcs**命令配置的802.11n基本MCS最大索引。

【举例】

·AC设备举例

\# 设置射频802.11n支持MCS的最大索引为14。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

AC-wlan-ap-ap1-radio-1 dot11n support maximum-mcs 14

·FAT AP设备举例

\# 设置射频802.11n支持MCS的最大索引为14。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 dot11n support maximum-mcs 14

**射频管理 \-- 射频管理命令 \-- max-power**

------------------------------------------------------------------------

**[max-power**]命令用来配置射频最大传输功率。

**[undo**]**max-power**命令用来恢复缺省情况。

【命令】

**[max-power*** radio-power*]

**[undo max-power**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，射频使用支持的最大功率。

FAT AP设备：Radio接口视图下，射频使用支持的最大功率。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[radio-power*]：射频的最大传输功率，其取值范围由国家码和射频类型决定。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

【使用指导】

·最大功率和国家码、信道、AP型号、射频类型和天线类型相关，如果采用802.11n，那么射频的最大功率和带宽类型也相关。

·改变射频类型、射频的工作信道、国家码、天线类型、带宽、天线增益等属性时，max-power的值会自动改变。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置射频最大传输功率为15dBm。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 max-power 15

·AC设备举例（AP组Radio视图）

\# 配置射频最大传输功率为15dBm。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 max-power 15

·FAT AP设备举例

\# 配置射频最大传输功率为15dBm。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11g

Sysname-WLAN-Radio1/0/2 max-power 15

**射频管理 \-- 射频管理命令 \-- power-lock enable**

------------------------------------------------------------------------

**[power**]**-lock enable**命令用来开启功率锁定功能。

**[power**]**-lock disable**命令用来关闭功率锁定功能。

**[undo power**]**-lock**命令用来恢复缺省情况。

【命令】

**[power-lock**[ { **enable** \| **disable** }]]

**[undo power**]**-lock**

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，功率锁定功能处于关闭状态。

【视图】

AC设备：Radio视图/AP组Radio视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·如果先开启功率调整，再配置锁定功率，AC会自动将当前传输功率设置并锁定为自动功率调整后的功率值，在AC重启后，AP能继续使用锁定的功率调整值。

·如果先配置锁定功率命令，后开启功率调整功能，由于功率已经被锁定，功率调整功能不会运行，所以在开启功率调整功能前，请确保功率没有被锁定。

·锁定功率后，如果信道发生调整，并且锁定的功率值 \> 调整后使用信道支持的最大功率，在这种情况下，设备会将功率值调整为信道支持的最大功率。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

关于功率调整功能的详细介绍，请参见"WLAN配置指导"中的"WLAN RRM"。

【举例】

·Radio视图

\# 配置锁定功率。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 power lock

·AP组Radio视图

\# 配置锁定功率。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 power lock

**射频管理 \-- 射频管理命令 \-- preamble**

------------------------------------------------------------------------

**[preamble**]命令用来配置前导码类型。

**[undo preamble**]命令用来恢复缺省情况。

【命令】

**[preamble**[ { **long** \| **short** }]]

**[undo preamble**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，Radio使用短前导码。

FAT AP设备：Radio接口视图下，Radio使用短前导码。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[long**]：长和短前导码。在网络中如果有客户端使用早期的客户端网卡，可以选择长前导码兼容这些客户端。

**[short**]：短前导码。选择短前导码能使网络同步性能更好，一般选择短前导码。

【使用指导】

·前导码是位于数据包起始处的一组bit位，接收者可以据此同步并准备接收数据。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置前导码类型为长前导码。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 2

Sysname-wlan-ap-ap1-radio-2 preamble long

·AC设备举例（AP组Radio视图）

\# 配置前导码类型为长前导码。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 preamble long

·FAT AP设备举例

\# 配置前导码类型为长前导码。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11g

Sysname-WLAN-Radio1/0/2 preamble long

**射频管理 \-- 射频管理命令 \-- radio enable**

------------------------------------------------------------------------

**[radio enable**]命令用来开启射频功能。

**[radio disable**]命令用来关闭射频功能。

**[undo**]**radio**命令用来恢复缺省情况。

【命令】

**[radio**[ { **enable** \| **disable** }]]

**[undo radio**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，射频处于关闭状态。

【视图】

AC设备：Radio视图/AP组Radio视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 开启射频功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 radio enable

·AC设备举例（AP组Radio视图）

\# 开启射频功能。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 radio enable

**射频管理 \-- 射频管理命令 \-- radio**

------------------------------------------------------------------------

**[radio**]命令用来进入Radio视图。

【命令】

**[radio ***radio-id*]

【视图】

AC设备：AP视图/AP组ap-model视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[radio-id*]：取值范围与AP设备的型号有关，请以设备的实际情况为准。

【举例】

\# 进入Radio视图。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1

\# 进入AP组Radio视图。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-apgroup1ap-model WA4620i-ACN

Sysname-wlan-ap-apgroup1-ap-model-WA4620i-ACNradio 1

**射频管理 \-- 射频管理命令 \-- rate**

------------------------------------------------------------------------

**[rate**]命令用来配置射频速率。

**[undo rate**]命令用来恢复缺省情况。

【命令】

**[rate**[ { **disabled** \| **mandatory** \| **multicast** \| **supported** } *rate-value*]]

**[undo rate**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下：

·802.11a/802.11an：

¡ 禁用速率：{.ItemListCharChar}无。

¡ 强制速率：{.ItemListCharChar}6，12，24。

¡ 组播速率：{.ItemListCharChar}从强制速率中选取最大值。{.ItemListCharChar}

¡ 支持速率：{.ItemListCharChar}9，18，36，48，54。{.ItemListCharChar}

·802.11b：

¡禁用速率：无。

¡强制速率：1，2。

¡组播速率：从强制速率中选取最大值。

¡支持速率：5.5，11。

·802.11g/802.11gn：

¡禁用速率：无。

¡强制速率：1，2，5.5，11。

¡组播速率：从强制速率中选取最大值。

¡支持速率：6，9，12，18，24，36，48，54。

FAT AP设备：Radio接口视图下：

·802.11a/802.11an：

¡ 禁用速率：{.ItemListCharChar}无。

¡ 强制速率：{.ItemListCharChar}6，12，24。

¡ 组播速率：{.ItemListCharChar}从强制速率中选取最大值。{.ItemListCharChar}

¡ 支持速率：{.ItemListCharChar}9，18，36，48，54。{.ItemListCharChar}

·802.11b：

¡禁用速率：无。

¡强制速率：1，2。

¡组播速率：从强制速率中选取最大值。

¡支持速率：5.5，11。

·802.11g/802.11gn：

¡禁用速率：无。

¡强制速率：1，2，5.5，11。

¡组播速率：从强制速率中选取最大值。

¡支持速率：6，9，12，18，24，36，48，54。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[disabled**]：禁用速率。AP禁用的速率。

**[mandatory**]：强制速率。客户端关联AP时，AP要求客户端必须支持的速率。

**[multicast**]：组播速率，即AP向客户端发送组播报文的速率。组播速率必须在强制速率中选取。

**[supported**]：支持速率。AP所支持的速率。客户端关联AP后，可以在AP支持的"支持速率集"中选用更高/更低的速率发送报文。

*[rate-value*]：速率值，单位为Mbps。可配置多个速率，用空格分隔。

·802.11a/802.11an：可以取值6、9、12、18、24、36、48、54。

·802.11b：可以取值1、2、5.5、11。

·802.11g/802.1gn：可以取值1、2、5.5、6、9、11、12、18、24、36、48、54。

【使用指导】

·强制速率和组播速率不能为空。当强制速率只有一个值时，用户不能将这个值配置成支持速率或者禁止速率。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例（Radio视图）

\# 配置强制速率为6Mbps、12Mbps、24Mbps。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 rate **mandatory** 6 12 24

·AC设备举例（AP组Radio视图）

\# 配置强制速率为6Mbps、12Mbps、24Mbps。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 rate mandatory 6 12 24

·FAT AP设备举例

\# 配置强制速率为6Mbps、12Mbps、24Mbps。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11g

Sysname-WLAN-Radio1/0/2 rate mandatory 6 12 24

**射频管理 \-- 射频管理命令 \-- short-gi enable**

------------------------------------------------------------------------

**[short-gi enable**]命令用来开启Short-GI功能。

**[short-gi disable**]命令用来关闭Short-GI功能。

**[undo short-gi**]命令用来恢复缺省情况。

【命令】

**[short-gi**[ { **disable** \| **enable** }]]

**[undo short-gi**]

【缺省情况】

AC设备：Radio视图下，继承AP组配置。

AC设备：AP组Radio视图下，Short GI功能处于开启状态。

FAT AP设备：Radio接口视图下，Short GI功能处于开启状态。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

·该命令仅在支持802.11n和802.11ac的Radio上支持。在进行Radio模式切换的时候，设备会恢复该模式下该功能的缺省情况。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

【举例】

·AC设备举例

\# 关闭Short GI功能。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

Sysname-wlan-ap-ap1-radio-1 short-gi disable

·FAT AP设备举例

\#关闭Short GI功能。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/1

Sysname-WLAN-Radio1/0/1 short-gi disable

**射频管理 \-- 射频管理命令 \-- type**

------------------------------------------------------------------------

**[type**]命令用来配置射频类型。

**[undo** **type**]命令用来恢复缺省情况。

【命令】

**[type **[{ **dot11a** \| **dot11an** \| **dot11b** \| **dot11g** \| **dot11gn** }]]

**[undo type**]

【缺省情况】

缺省情况与设备的型号有关，请以设备的实际情况为准。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[dot11a**]：指定射频类型为802.11a。

**[dot11an**]：指定射频类型为802.11n（5GHz）模式。

**[dot11b**]：指定射频类型类型为802.11b。

**[dot11g**]：指定射频类型类型为802.11g。

**[dot11gn**]：指定射频类型为802.11n（2.4GHz）模式。

【使用指导】

·AC设备：修改射频类型时，如果射频处于开启状态，会导致客户端下线。修改射频类型后，当前Radio视图下与射频类型有关的命令，例如信道、最大功率、速率都会恢复为缺省值。

·AC设备：Radio视图下配置的优先级高于AP组的配置。

·FAT AP设备：修改射频类型时，如果射频处于开启状态，会导致客户端下线。修改射频类型后，当前Radio接口下与射频类型有关的命令，例如信道、最大功率、速率都会恢复为缺省值。

【举例】

·AC设备举例（Radio视图）

\# 配置射频类型为802.11n（5GHz）模式。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 type dot11an

·AC设备举例（AP组Radio视图）

\# 配置射频类型为802.11n（5GHz）模式。

\<Sysname\> system-view

Sysname wlan ap-group apgroup1

Sysname-wlan-ap-group-apgroup1 ap-model WA4620i-ACN

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN radio 1

Sysname-wlan-ap-group-apgroup1-ap-model-WA4620i-ACN-radio-1 type dot11an

·FAT AP设备举例

\# 配置Radio接口类型为802.11n（5GHz）模式。

\<Sysname\> system-view

Sysname interface wlan-radio 1/0/2

Sysname-WLAN-Radio1/0/2 type dot11an
