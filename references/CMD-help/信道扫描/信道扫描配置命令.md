<!-- CMD-INDEX
  scan idle-time                      | AC设备：Radio视图/AP组Radio视图 | L7
  scan max-service-time               | AC设备：Radio视图/AP组Radio视图 | L69
  scan scan-time                      | AC设备：Radio视图/AP组Radio视图 | L125
-->

**信道扫描 \-- 信道扫描配置命令 \-- scan idle-time**

------------------------------------------------------------------------

**[scan idle-time**]命令用来配置服务周期空闲时长。

**[undo scan idle-time**]命令用来恢复缺省情况。

【命令】

**[scan idle-time** *idle-time*]

**[undo scan idle-time**]

【缺省情况】

Radio视图：继承AP组配置

AP组Radio视图：服务周期空闲时间为100毫秒。

Radio接口视图：服务周期空闲时间为100毫秒。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[idle-time*]：服务周期的空闲时长，取值范围60～5000，单位为毫秒。

【使用指导】

·服务周期空闲时长指在服务周期内，工作信道上持续无流量的时长。

·一个服务周期内，若流量停止的时间达到空闲时间，且当前周期已停留超过一个扫描周期时间，则切换到下一个扫描周期。但如果没有达到扫描时间，即使空闲时间超时，也不应切换到扫描周期。即，服务周期空闲时长和扫描时长都不能大于服务周期最大持续时间。

·**scan idle-time**实际生效时间为**beacon interval**的整数倍，当配置的*idle-time*小于*beacon interval*时，实际按照*beacon interval*生效。

**[【举例】**]

\# 将ap1下的radio1的服务周期空闲时长配置为500毫秒。

*[\<Sysna*me*\> system-view* ]

Sysna*me wlan ap ap1* model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 scan idle-time 500

【相关命令】

·**beacon interval**

**信道扫描 \-- 信道扫描配置命令 \-- scan max-service-time**

------------------------------------------------------------------------

**[scan max-service-time**]命令用来配置服务周期最大持续时间。

**[undo scan max-service-time**]命令用来恢复缺省情况。

【命令】

**[scan max-service-time**[ { *max-service-time* \| **no-limit** }]]

**[undo scan max-service-time**]

【缺省情况】

Radio视图：继承AP组配置

AP组Radio视图：服务周期的最大持续时间为5000毫秒。

Radio接口视图：服务周期的最大持续时间为5000毫秒。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-service-time*]：服务周期的最大持续时间，取值范围100～5000，单位为毫秒。

**[no-limit**]：不限制最大服务时间，直到信道闲置（流量停止时间达到空闲时间）才切换。当最大服务时间被配置为no-limit时，AP将始终优先保证服务类业务，只要存在业务流量，就不会进行扫描。

【使用指导】

当前服务周期达到最大持续时间后，如果有信道需要扫描，不论流量是否停止，都将切换到下一个扫描周期。服务周期最大持续时间不能少于扫描周期持续时间。

【举例】

\# 配置服务周期最大持续时间为3000毫秒。

\<Sysname\> system-view

Sysname wlan ap ap1model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 scan max-service-time 3000

**信道扫描 \-- 信道扫描配置命令 \-- scan scan-time**

------------------------------------------------------------------------

**[scan scan-time**]命令用来配置扫描时长。

**[undo scan scan-time**]命令用来恢复缺省情况。

【命令】

**[scan scan-time*** scan-time*]

**[undo scan scan-time**]

【缺省情况】

Radio视图：继承AP组配置

AP组Radio视图：扫描时长为100毫秒。

Radio接口视图：扫描时长为100毫秒。

【视图】

AC设备：Radio视图/AP组Radio视图

FAT AP设备：Radio接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[scan-time*]：扫描时间，取值范围100～5000，单位为毫秒。

【使用指导】

扫描时长指射频信道扫描周期持续的固定时间，同时也用来约定服务周期内提供扫描的时间长度，扫描时间不能大于最大服务时间。当前扫描周期达到扫描时间后，将切换到下一个扫描周期或服务周期。

【举例】

\# 配置扫描时间为500毫秒。

\<Sysname\> system-view

Sysname wlan ap ap1 model WA4620i-ACN

Sysname-wlan-ap-ap1 radio 1

Sysname-wlan-ap-ap1-radio-1 scan scan-time 500

![说明](信道扫描命令.files/image001.png)

此命令的支持情况与设备的类型有关，请以设备的实际情况为准。

