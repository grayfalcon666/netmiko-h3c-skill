
**CFD \-- CFD配置命令 \-- cfd ais enable**

------------------------------------------------------------------------

**[cfd ais enable**]命令用来开启告警抑制功能。

**[undo cfd ais enable**]命令用来关闭告警抑制功能。

【命令】

**[cfd ais enable**]

**[undo cfd ais enable**]

【缺省情况】

告警抑制功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启告警抑制功能。

\<Sysname\> system-view

Sysname cfd ais enable

【相关命令】

·**cfd ****aislevel**

·**cfd ais period**

**CFD \-- CFD配置命令 \-- cfd ais level**

------------------------------------------------------------------------

**[cfd ais level**]命令用来配置AIS报文的发送级别。

**[undo cfd ais level**]命令用来恢复缺省情况。

【命令】

**[cfd ais level ***level-value*** service-instance ***instance-id*]

**[undo cfd ais level ***level-value*** service-instance ***instance-id*]

【缺省情况】

没有配置AIS报文的发送级别。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level ***level-value*]：表示AIS报文的发送级别，*level-value*的取值范围为1～7。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【使用指导】

如果服务实例中没有配置AIS报文的发送级别，则该服务实例中的MEP将无法发送AIS报文。

【举例】

\# 配置服务实例1内AIS报文的发送级别为3。

\<Sysname\> system-view

Sysname cfd ais level 3 service-instance 1

【相关命令】

·**cfd ****aisenable**

·**cfd ais period**

**CFD \-- CFD配置命令 \-- cfd ais period**

------------------------------------------------------------------------

**[cfd ais period**]命令用来配置AIS报文的发送周期。

**[undo cfd ais period**]命令用来恢复缺省情况。

【命令】

**[cfd ais period ***period-value*** service-instance ***instance-id*]

**[undo cfd ais period ***period-value* **service-instance** *instance-id*]

【缺省情况】

AIS报文的发送周期为1秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[period ***period-value*]：表示发送周期，*period-value*的取值为1或60，单位为秒。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【举例】

\# 配置服务实例1内AIS报文的发送周期为60秒。

\<Sysname\> system-view

Sysname cfd ais period 60 service-instance 1

【相关命令】

·**cfd ****aisenable**

·**cfd ais level**

**CFD \-- CFD配置命令 \-- cfd ais-track link-status global**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cfd ais-track link-status global**]命令用来开启端口状态与AIS的联动功能。

**[undo cfd ais-track link-status global**]命令用来关闭端口状态与AIS联动功能。

【命令】

**[cfd ais-track link-status global**]

**[undo cfd ais-track link-status global**]

【缺省情况】

端口状态与AIS联动功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启端口状态与AIS联动功能。

\<Sysname\> system-view

Sysname cfd ais-track link-status global

【相关命令】

·**cfd ais-track link-status level**

·**cfd ais-track link-status ****period**

·**cfd ais-track link-status ****vlan**

**CFD \-- CFD配置命令 \-- cfd ais-track link-status level**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cfd ais-track link-status level**]命令用来配置EAIS报文的发送级别。

**[undo cfd ais-track link-status**]命令用来恢复缺省情况。

【命令】

**[cfd ais-track link-status level ***level-value*]

**[undo cfd ais-track link-status level**]

【缺省情况】

没有配置EAIS报文的发送级别。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[level*** level-value*]：表示EAIS报文的发送级别，*level-value*的取值范围为0～7。

【使用指导】

·如果端口上没有配置EAIS报文的发送级别，那么该端口将无法触发EAIS报文。

·以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置EAIS报文的发送级别为3。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd ais-track link-status level 3

【相关命令】

·**cfd ais-track link-status ****global**

·**cfd ais-track link-status ****period**

·**cfd ais-track link-status ****vlan**

**CFD \-- CFD配置命令 \-- cfd ais-track link-status period**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cfd ais-track link-status period**]命令用来配置EAIS报文的发送周期。

**[undo cfd ais-track link-status period**]命令用来恢复缺省情况。

【命令】

**[cfd ais-track link-status period ***period-value*]

**[undo cfd ais-track link-status period**]

【缺省情况】

没有配置EAIS报文的发送周期。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[period ***period-value*]：表示发送周期，*period-value*的取值为1或60，单位为秒。

【使用指导】

·如果端口上没有配置EAIS报文的发送周期，那么该端口将无法触发EAIS报文。

·以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置EAIS报文的发送周期为60秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd ais-track link-status period 60

【相关命令】

·**cfd ais-track link-status ****global**

·**cfd ais-track link-status ****level**

·**cfd ais-track link-status ****vlan**

**CFD \-- CFD配置命令 \-- cfd ais-track link-status vlan**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cfd ais-track link-status vlan**]命令用来配置EAIS报文的发送VLAN。

**[undo cfd ais-track link-status vlan**]命令用来删除指定的发送VLAN。

【命令】

**[cfd ais-track link-status vlan **]*vlan-list*

**[undo cfd ais-track link-status vlan **]*vlan-list*

【缺省情况】

EAIS报文只在本端口的缺省VLAN内发送。

【视图】

二层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[vlan **]*vlan-list*：指定EAIS报文发送的VLAN范围。*vlan-list*为VLAN列表，表示多个VLAN。其表示方式为*vlan-list* = { *vlan-id* [ **to** *vlan-id*  }&\<1-10\>]，其中，*vlan-id*为指定VLAN的编号，取值范围为1～4094。&\<1-10\>表示前面的参数最多可以输入10次。

【使用指导】

·EAIS报文将在本命令所指定VLAN与本设备上实际存在VLAN的交集内发送。

·如果多次执行本命令，将取各次所配置VLAN的合集。

·以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上配置EAIS报文的发送VLAN为VLAN 100～200。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd ais-track link-status vlan 100 to 200

【相关命令】

·**cfd ais-track link-status ****global**

·**cfd ais-track link-status ****level**

·**cfd ais-track link-status ****period**

**CFD \-- CFD配置命令 \-- cfd cc enable**

------------------------------------------------------------------------

**[cfd cc enable**]命令用来在接口下开启指定MEP的CCM报文发送功能。

**[undo cfd cc enable**]命令用来在接口下关闭指定MEP的CCM报文发送功能。

【命令】

**[cfd cc service-instance ***instance-id*** mep ***mep-id*** enable**]

**[undo cfd cc service-instance ***instance-id*** mep ***mep-id*** enable**]

【缺省情况】

MEP的CCM报文发送功能处于关闭状态。

【视图】

二层以太网接口视图/三层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep*** mep-id*]：表示MEP的编号，*mep-id*的取值范围为1～8191。

【使用指导】

以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在端口GigabitEthernet1/0/1上开启服务实例5内MEP 3的CCM报文发送功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd cc service-instance 5 mep 3 enable

【相关命令】

·**cfd cc interval**

**CFD \-- CFD配置命令 \-- cfd cc interval**

------------------------------------------------------------------------

**[cfd cc interval**]命令用来配置MEP发送的CCM报文中时间间隔域的值。

**[undo cfd cc interval**]命令用来恢复缺省情况。

【命令】

**[cfd cc interval ***interval-value*** service-instance ***instance-id*]

**[undo cfd cc interval** [ *interval-value*  **service-instance** *instance-id*]]

【缺省情况】

MEP发送的CCM报文中时间间隔域的值为4。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interval ***interval-value*]：表示CCM报文中时间间隔域（Interval域）的值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【使用指导】

CCM报文中时间间隔域的值、CCM报文的发送间隔和远端MEP的超时时间这三者之间的关系如[表]1-1(?-1572688889#_Ref138497021)所示。

表1-1 参数关系表

CCM报文中时间间隔域的值

CCM报文的发送间隔

远端MEP的超时时间

1

10/3毫秒

35/3毫秒

2

10毫秒

35毫秒

3

100毫秒

350毫秒

4

1秒

3.5秒

5

10秒

35秒

6

60秒

210秒

7

600秒

2100秒

![说明](CFD命令.files/image001.png)

[表]1-1(?-1572688889#_Ref138497021)中时间间隔域的取值范围与设备的型号有关，请以设备的实际情况为准。

【举例】

\# 配置服务实例2内MEP发送的CCM报文中时间间隔域的值为7。

\<Sysname\> system-view

Sysname cfd cc interval 7 service-instance 2

【相关命令】

·**cfd cc enable**

**CFD \-- CFD配置命令 \-- cfd dm one-way**

------------------------------------------------------------------------

**[cfd dm one-way**]命令用来开启单向时延测试功能，通过从源MEP发送1DM报文到目标MEP来测试设备间的单向时延。

【命令】

**[cfd dm one-way service-instance ***instance-id*** mep ***mep-id*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **number** *number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep ***mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[number*** number*]：表示1DM报文的发送数量，*number*的取值范围为2～10，缺省值为5。

【使用指导】

单向时延的测试结果需在目标MEP上通过**display cfd dm one-way history**命令来显示。

【举例】

\# 在服务实例1内测试源MEP 1101到目标MEP 1003的单向时延。

\<Sysname\> cfd dm one-way service-instance 1 mep 1101 target-mep 1003

5 1DMs have been sent. Please check the result on the remote device.

表1-2 cfd dm one-way命令显示信息描述表

字段

描述

5 1DMs have been sent

已发送5个1DM报文

Please check the result on the remote device

请在目标设备上查看结果

【相关命令】

·**display cfd dm one-way history**

·**reset cfd dm one-way history**

**CFD \-- CFD配置命令 \-- cfd dm two-way**

------------------------------------------------------------------------

**[cfd dm two-way**]命令用来开启双向时延测试功能，通过从源MEP发送DMM报文到目标MEP，并检测回应的DMR报文来测试设备间的双向时延。

【命令】

**[cfd dm two-way service-instance ***instance-id*** mep ***mep-id*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **number** *number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep ***mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[number*** number*]：表示DMM报文的发送数量，*number*的取值范围为2～10，缺省值为5。

【举例】

\# 在服务实例1内测试源MEP 1101到目标MEP 2001的双向时延。

\<Sysname\> cfd dm two-way service-instance 1 mep 1101 target-mep 2001

Frame delay:

Reply from 0010-fc00-6512: 10ms

Reply from 0010-fc00-6512: 9ms

Reply from 0010-fc00-6512: 11ms

Reply from 0010-fc00-6512: 5ms

Reply from 0010-fc00-6512: 5ms

Average: 8ms

Sent DMMs: 5        Received: 5        Lost: 0

Frame delay variation: 5ms 4ms 6ms 0ms 0ms

Average: 3ms

表1-3 cfd dm two-way命令显示信息描述表

字段

描述

Frame delay

帧时延

Reply from 0010-fc00-6512

从MAC地址为0010-FC00-6512的MEP返回的DMR报文的时延

Average

帧时延或帧时延变化的平均值

Sent DMMs

发送的DMM报文总数

Received

收到的DMR报文总数

Lost

丢失的DMR报文总数

Frame delay variation

帧时延变化

**CFD \-- CFD配置命令 \-- cfd enable**

------------------------------------------------------------------------

**[cfd enable**]命令用来使能CFD功能。

**[undo cfd enable**]命令用来关闭CFD功能。

【命令】

**[cfd enable**]

**[undo cfd enable**]

【缺省情况】

CFD功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 使能CFD功能。

\<Sysname\> system-view

Sysname cfd enable

**CFD \-- CFD配置命令 \-- cfd hardware-cc**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[cfd hardware-cc**]命令用来开启硬件检测功能。

**[undo cfd hardware-cc**]用来关闭硬件检测功能。

【命令】

**[cfd hardware-cc service-instance*** instance-id* **remote-mep** *mep-list*]

**[undo** **cfd hardware-cc service-instance** *instance-id* **remote-mep** *mep-list*]

【缺省情况】

硬件检测功能处于关闭状态。

【视图】

二层以太网接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance**]* instance-id*：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[remote-mep **]*mep-list*：表示远端MEP的编号列表，表示多个远端MEP。表示方式为*mep-list* = { *mep-id* [ **to** *mep-id*  }&\<1-10\>]。其中，*mep-id*为MEP的编号，取值范围为1～8191。&\<1-10\>表示前面的参数最多可以输入10次。

【举例】

\# 在端口GigabitEthernet1/0/1上开启硬件检测功能，在服务实例1内对远端MEP 5进行硬件检测。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd hardware-cc service-instance 1 remote-mep 5

**CFD \-- CFD配置命令 \-- cfd linktrace**

------------------------------------------------------------------------

**[cfd linktrace**]命令用来查找源MEP到目标MP的路径，通过从源MEP发送LTM报文到目标MP，并检测回应的LTR报文来确定设备间的路径。

【命令】

**[cfd linktrace service-instance ***instance-id*** mep ***mep-id*****[{ **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **ttl** *ttl-value* ]  **hw-only** ]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep*** mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MP的MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[ttl ***ttl-value*]：表示生存时间值，*ttl-value*的取值范围为1～255，缺省值为64。

**[hw-only**]：表示所发送的LTM报文的HW-only位置位。当设置了此参数时，表示接收LTM报文的MIP在硬件转发表中找不到目标MAC地址时，不对报文进行广播；否则，将对报文进行广播。

【举例】

\# 在服务实例1内查找源MEP 1101到目标MEP 2001的路径。

\<Sysname\> cfd linktrace service-instance 1 mep 1101 target-mep 2001

Linktrace to MEP 2001 with the sequence number 1101-43361:

MAC address               TTL     Last MAC         Relay action

0010-fc00-6512            63      0010-fc00-6500   Hit

表1-4 cfd linktrace命令显示信息描述表

字段

描述

Linktrace to MEP 2001 with the sequence number 1101-43361

以序列号1101-43361发送LTM报文到目标MEP 2001

MAC address

LTR报文中的源MAC地址

TTL

LTM报文经过此设备时的TTL值

Last MAC

LTM报文所经过上一跳设备的MAC地址

Relay action

表示转发设备在MAC地址表中是否找到了目标MAC地址：

·Hit：表示本设备就是目标MAC地址

·FDB：表示在转发表中找到了目标MAC地址

·MPDB：表示没有找到目标MAC地址，或者在MEP或MIP数据库中找到了目标MAC地址

【相关命令】

·**cfd linktrace auto-detection**

·**display cfd linktrace-reply**

**CFD \-- CFD配置命令 \-- cfd linktrace auto-detection**

------------------------------------------------------------------------

**[cfd linktrace auto-detection**]命令用来开启自动发送LTM报文功能。

**[undo cfd linktrace auto-detection**]命令用来关闭自动发送LTM报文功能。

【命令】

**[cfd linktrace auto-detection** [ **size** *size-value* ]]

**[undo cfd linktrace auto-detection**]

【缺省情况】

自动发送LTM报文功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[size*** size-value*]：表示缓冲区只记录最近*size-value*次自动检测的结果，*size-value*的取值范围为1～100，以发送的次数为单位，缺省值为5次，即缓冲区只记录最近*5*次自动检测的结果。

【使用指导】

·开启本功能后，当源MEP在3.5个CCM报文发送周期内未收到目标MEP发来的CCM报文，从而判定与目标MEP的连接出错时，将发送LTM报文（该LTM报文的目地为目标MEP，LTM报文中TTL字段为最大值255），通过检测回应的LTR报文来定位故障。

·关闭自动发送LTM报文的功能后，缓冲区中的内容将被删除，记录被清空。

·支持硬件检测功能的单板上所配置的外向MEP，不会自动发送LTM报文。

【举例】

\# 开启自动发送LTM报文功能，且缓冲区只记录最近100次自动检测的结果。

\<Sysname\> system-view

Sysname cfd linktrace auto-detection size 100

【相关命令】

·**cfd linktrace**

·**display cfd linktrace-reply auto-detection**

**CFD \-- CFD配置命令 \-- cfd loopback**

------------------------------------------------------------------------

**[cfd loopback**]命令用来开启环回功能，从源MEP向目标MP发送LBM报文并接收LBR报文。

【命令】

**[cfd loopback service-instance ***instance-id*** mep ***mep-id*****[{ **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **number** *number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep*** mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MP的MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[number*** number*]：表示发送LBM报文数量，*number*的取值范围为1～10，缺省值为5。

【举例】

\# 开启环回功能，检查服务实例1内MEP 1101到2001的链路状况（假设链路状态正常）。

\<Sysname\> cfd loopback service-instance 1 mep 1101 target-mep 2001

Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404:

Reply from 0010-fc00-6512: sequence number=1101-43404 Time=5ms

Reply from 0010-fc00-6512: sequence number=1101-43405 Time=5ms

Reply from 0010-fc00-6512: sequence number=1101-43406 Time=5ms

Reply from 0010-fc00-6512: sequence number=1101-43407 Time=5ms

Reply from 0010-fc00-6512: sequence number=1101-43408 Time=5ms

Sent: 5        Received: 5        Lost: 0

\# 开启环回功能，检查服务实例1内MEP 1101到2001的链路状况（假设链路状态不正常）。

\<Sysname\> cfd loopback service-instance 1 mep 1101 target-mep 2001

Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404:

Sent: 5        Received: 0        Lost: 5

表1-5 cfd loopback命令显示信息描述表

字段

描述

Loopback to 0010-fc00-6512 with the sequence number start from 1101-43404

以1101-43404为起始序列号发送LBM报文到MAC地址为0010-FC00-6512的MEP

Reply from 0010-fc00-6512

表示从MAC地址为0010-FC00-6512的目标MP返回

sequence number

LBR报文中的序列号

Time=5ms

表示从发出LBM报文到收到LBR报文的时间间隔为5毫秒

Sent

发送LBM报文的数量

Received

收到LBR报文的数量

Lost

丢失LBR报文的数量

**CFD \-- CFD配置命令 \-- cfd md**

------------------------------------------------------------------------

**[cfd md**]命令用来创建MD。

**[undo cfd md**]命令用来删除MD。

【命令】

**[cfd md ***md-name*****[ **index** *index-value*  **level** *level-value* [ **md-id** { **dns** *dns-name* \| **mac** *mac-address* *subnumber* \| **none** } ]]]

**[undo cfd md ***md-name*]

【缺省情况】

没有创建MD。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[md ***md-name*]：表示字符串格式的MD名称，*md-name*为1～43个字符的字符串，可以由字母、数字和特殊字符（包括\` \~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } [  \| : ; \' \< \> , . /]）组成。

**[index** *index-value*]：表示MD的索引号，*index-value*的取值范围为1～4294967295。如果未指定本参数，系统将自动分配尚未使用的最小索引号。不建议用户手工指定MD的索引号，最好由系统来自动分配。

**[level*** level-value*]：表示MD的级别，*level-value*的取值范围为0～7。

**[md-id**]：表示MEP所发送的报文携带的MD名称。如果未指定本参数，该名称就是*md-name*。

**[dns** *dns-name*]：表示采用DNS名称的MD名称，*dns-name*表示DNS的名称。

**[mac** *mac-address* *subnumber*]：表示由MAC地址和一个整数构成的MD名称，*mac-address*表示MAC地址，*subnumber*的取值范围为0～65535。

**[none**]：表示MEP所发送的报文不携带MD名称。

【使用指导】

·MD的名称应符合IEEE802.1ag-2007中表21-19的规定。

·当输入的MD名称错误或已存在，或者指定的索引号已被使用时，将不能创建MD。

·删除MD时，基于该MD的配置均被删除。

【举例】

\# 创建级别为3的MD test_md1。

\<Sysname\> system-view

Sysname cfd md test_md1 level 3

\# 创建级别为5的MD test_md2，且MEP发送的报文携带的MD名称由MAC地址1-1-1和整数1构成。

\<Sysname\> system-view

Sysname cfd md test_md2 level 5 md-id mac 1-1-1 1

**CFD \-- CFD配置命令 \-- cfd mep**

------------------------------------------------------------------------

**[cfd mep**]命令用来创建MEP。

**[undo cfd mep**]命令用来删除MEP。

【命令】

在二层以太网接口视图或二层聚合接口视图下：

**[cfd mep ***mep-id*** service-instance ***instance-id*[ { **inbound \| outbound** }]]

**[undo cfd mep ***mep-id*** service-instance*** instance-id*]

在三层以太网接口视图下：

**[cfd mep ***mep-id*** service-instance ***instance-id* **outbound**]

**[undo cfd mep ***mep-id*** service-instance*** instance-id*]

【缺省情况】

接口上不存在MEP。

【视图】

二层以太网接口视图/三层以太网接口视图/二层聚合接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[mep ***mep-id*]：表示MEP的编号，*mep-id*的取值范围为1～8191。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[inbound**]：表示建立的是内向MEP。

**[outbound**]：表示建立的是外向MEP。

【使用指导】

·在创建MEP时，通过指定的服务实例确定该MEP所在的MA和MD。

·创建的MEP必须已包含在对应服务实例的MEP列表中，否则不能创建成功。

·以太网接口视图下的配置只对当前接口生效；聚合接口视图下的配置对当前接口及其成员端口均生效；聚合成员端口上的配置，只有当成员端口退出聚合组后才能生效。

【举例】

\# 在服务实例5内配置MEP列表，在端口GigabitEthernet1/0/1上创建服务实例5内的外向MEP 3。

\<Sysname\> system-view

Sysname cfd md test_md level 3

Sysname cfd service-instance 5 ma-id vlan-based md test_md vlan 100

Sysname cfd meplist 3 service-instance 5

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 cfd mep 3 service-instance 5 outbound

【相关命令】

·**cfd meplist**

**CFD \-- CFD配置命令 \-- cfd meplist**

------------------------------------------------------------------------

**[cfd meplist**]命令用来配置MEP列表，包括允许配置的本地MEP和需要监控的远端MEP。

**[undo cfd meplist**]命令用来删除已配置的MEP列表。

【命令】

**[cfd meplist ***mep-list*** service-instance ***instance-id*****]

**[undo cfd meplist ***mep-list*** service-instance ***instance-id*****]

【缺省情况】

不存在MEP列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[meplist ***mep-list*]：表示MEP的编号列表，表示多个MEP。表示方式为*mep-list* = { *mep-id* [ **to** *mep-id*  }&\<1-10\>]。其中，*mep-id*为MEP的编号，取值范围为1～8191。&\<1-10\>表示前面的参数最多可以输入10次。

**[service-instance ***instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【使用指导】

·在配置MEP列表之前必须先创建MD和服务实例。

·删除MEP列表时，基于该列表的本地MEP的配置均被删除。

【举例】

\# 在服务实例5内配置MEP为9到15的MEP列表。

\<Sysname\> system-view

Sysname cfd md test_md level 3

Sysname cfd service-instance 5 ma-id vlan-based md test_md vlan 100

Sysname cfd meplist 9 to 15 service-instance 5

【相关命令】

·**cfd md**

·**cfd service-instance**

**CFD \-- CFD配置命令 \-- cfd mip-rule**

------------------------------------------------------------------------

**[cfd mip-rule**]命令用来配置MIP的创建规则，系统将按照此规则在接口上自动创建MIP。

**[undo cfd mip-rule**]命令用来恢复缺省情况。

【命令】

**[cfd mip-rule **[{ **default** \| **explicit** } **service-instance** *instance-id*]]

**[undo cfd mip-rule**[ [ **default** \| **explicit** ] **service-instance** *instance-id*]]

【缺省情况】

没有配置MIP的创建规则，系统不自动创建MIP。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[default**]：表示Default规则，即：当接口上没有更低级别的MIP时，在本级别创建MIP。在此规则下，接口上即使没有配置MEP也可创建MIP。

**[explicit**]：表示Explicit规则，即：当接口上没有更低级别的MIP且有更低级别的MEP时，在本级别创建MIP。在此规则下，接口上只有配置了更低级别的MEP时才可创建MIP。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【举例】

\# 在服务实例5内配置MIP的创建规则为Default规则。

\<Sysname\> system-view

Sysname cfd mip-rule default service-instance 5

**CFD \-- CFD配置命令 \-- cfd service-instance**

------------------------------------------------------------------------

**[cfd service-instance**]命令用来创建服务实例。

**[undo cfd service-instance**]命令用来删除服务实例。

【命令】

**[cfd service-instance*** instance-id ***ma-id**[ { **icc-based** *ma-name* \| **integer** *ma-num* \| **string** *ma-name* \| **vlan-based** [ *vlan-id* ] }  **ma-index** *index-value*  **md** *md-name*  **vlan** *vlan-id* ]]

**[undo cfd service-instance ***instance-id*]

【缺省情况】

不存在服务实例。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[ma-id**]：表示创建MA。

**[icc-based** *ma-name*]：表示以ICC（ITU Carrier Codes，国际电信联盟运营商代码）格式的字符串为名称的MA，*ma-name*为1～13个字符的字符串。

**[integer** *ma-num*]：表示以整数为名称的MA，*ma-num*的取值范围为0～65535。

**[string** *ma-name*]：表示以普通字符串为名称的MA，*ma-name*为1～45个字符的字符串，可以由字母、数字和特殊字符（包括\` \~ ! @ \# \$ % \^ & \* ( ) \_ - + = { } [  \| : ; \' \< \> , . /]）组成。

**[vlan-based** [ *vlan-id* ]]：表示以VLAN编号为名称的MA，*vlan-id*的取值范围为1～4094。如果未指定*vlan-id*，则使用**vlan** *vlan-id*参数所指定的VLAN编号作为MA的名称；而如果不指定**vlan** *vlan-id*参数，则必须在本参数中指定*vlan-id*。

**[ma-index** *index-value*]：表示MA的索引号，*index-value*的取值范围为1～4294967295。如果未指定本参数，系统将自动分配尚未使用的最小索引号。不建议用户手工指定MA的索引号，最好由系统来自动分配。

**[md*** md-name*]：表示MD的名称，*md-name*为1～43个字符的字符串，可以由字母、数字和特殊字符（包括\` \~ ! @ \# \$ % \^ & \* ( ) - \_ + = { } [  \| : ; \' \< \> , . /]）组成。

**[vlan** *vlan-id*]：表示MA所服务的VLAN，*vlan-id*的取值范围为1～4094。

【使用指导】

·服务实例根据MD中定义的VLAN划分，每个VLAN是一个MA，有一个MA名称，并指定一个服务实例编号。MA的索引号代表了一个MD中的特定MA，它只在特定MD中唯一，不同MD中可以使用相同的MA索引号。

·MA的名称应符合IEEE802.1ag-2007中表21-20的规定。

·创建MA时，如果指定了**vlan-based** [ *vlan-id* ]或**vlan** *vlan-id*参数，该MA就称为带VLAN属性的MA；否则称为不带VLAN属性的MA。

·在创建服务实例之前，必须先为该服务实例创建MD。

·在删除服务实例时，基于该服务实例的配置均被删除。

·删除服务实例将不仅解除该服务实例与MA之间的关联，MA本身也将被删除。

【举例】

\# 创建级别为3的MD test_md，并创建服务实例5，该服务实例的MA以VLAN编号为名称，且服务于VLAN 100。

\<Sysname\> system-view

Sysname cfd md test_md level 3

Sysname cfd service-instance 5 ma-id vlan-based md test_md vlan 100

【相关命令】

·**cfd md**

**CFD \-- CFD配置命令 \-- cfd slm**

------------------------------------------------------------------------

**[cfd slm**]命令用来开启单向丢包测试功能，通过从源MEP发送LMM报文到目标MEP，并检测回应的LMR报文来测试设备间的单向丢包情况。

【命令】

**[cfd slm service-instance ***instance-id*** mep ***mep-id*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **number** *number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep ***mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[number*** number*]：表示LMM报文的发送数量，*number*的取值范围为2～10，缺省值为5。

【举例】

\# 在服务实例1内测试源MEP 1101到目标MEP 2001的单向丢包情况。

\<Sysname\> cfd slm service-instance 1 mep 1101 target-mep 2001

Reply from 0010-fc00-6512

Far-end frame loss: 10    Near-end frame loss: 20

Reply from 0010-fc00-6512

Far-end frame loss: 40    Near-end frame loss: 40

Reply from 0010-fc00-6512

Far-end frame loss: 0     Near-end frame loss: 10

Reply from 0010-fc00-6512

Far-end frame loss: 30    Near-end frame loss: 30

Average

Far-end frame loss: 20    Near-end frame loss: 25

Far-end frame loss rate: 25.00%      Near-end frame loss rate: 32.00%

Sent LMMs: 5    Received: 5    Lost: 0

表1-6 cfd slm命令显示信息描述表

字段

描述

Reply from 0010-fc00-6512

从MAC地址为0010-FC00-6512的目标MEP返回的LMR报文

Far-end frame loss

目标MEP的帧丢失数

Near-end frame loss

源MEP的帧丢失数

Far-end frame loss rate

目标MEP的帧丢失率

Near-end frame loss rate

源MEP的帧丢失率

Average

帧丢失数平均值

Sent LMMs

发送的LMM报文总数

Received

收到的LMR报文总数

Lost

丢失的LMR报文总数

**CFD \-- CFD配置命令 \-- cfd tst**

------------------------------------------------------------------------

**[cfd tst**]命令用来开启比特错误测试功能，通过从源MEP发送TST报文到目标MEP来测试设备间的比特错误。

【命令】

**[cfd tst service-instance ***instance-id*** mep ***mep-id*[ { **target-mac** *mac-address* \| **target-mep** *target-mep-id* } [ **number** *number* ]  **length-of-test** *length*  [ **pattern-of-test** { **all-zero** \| **prbs** } [ **with-crc** ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

**[mep ***mep-id*]：表示源MEP的编号，*mep-id*的取值范围为1～8191。

**[target-mac*** mac-address*]：表示目标MAC地址，*mac-address*的格式为H-H-H。

**[target-mep*** target-mep-id*]：表示目标MEP的编号，*target-mep-id*的取值范围为1～8191。

**[number*** number*]：表示TST报文的发送数量，*number*的取值范围为1～10，缺省值为5。

**[length-of-test*** length*]：表示TST报文中Test TLV（Type/Length/Value，类型/长度/值）中的长度值，*length*的取值范围为4～1400，缺省值为64。

**[pattern-of-test **[{ **all-zero** \| **prbs** } [ **with-crc** ]]]：表示TST报文中Test TLV的模式，一共有四种模式，分别是：**all-zero**（不带CRC-32校验码的全0值）、**prbs**（不带CRC-32校验码的伪随机序列）、**all-zero******with-crc**（带CRC-32校验码的全0值）和**prbs** **with-crc**（带CRC-32校验码的伪随机序列）。缺省模式为**all-zero**。

【使用指导】

比特错误的测试结果需在目标MEP上通过**display cfd tst**命令来显示。

【举例】

\# 在服务实例1内测试源MEP 1101到目标MEP 1003的比特错误。

\<Sysname\> cfd tst service-instance 1 mep 1101 target-mep 1003

5 TSTs have been sent. Please check the result on the remote device.

表1-7 cfd tst命令显示信息描述表

字段

描述

5 TSTs have been sent

已发送5个TST报文

Please check the result on the remote device

请在目标设备上查看结果

【相关命令】

·**display cfd tst**

·**reset cfd tst**

**CFD \-- CFD配置命令 \-- display cfd ais**

------------------------------------------------------------------------

**[display cfd ais**]命令用来显示MEP上AIS的配置和动态信息。

【命令】

**[display cfd ais** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance*** instance-id*]：显示指定服务实例内的信息，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例内的信息。

**[mep*** mep-id*]：显示指定MEP的信息，*mep-id*的取值范围为1～8191。如果未指定本参数，将显示所有MEP的信息。

【举例】

\# 显示所有服务实例内所有MEP上AIS的配置和动态信息。

\<Sysname\> display cfd ais

Service instance: 5

AIS level: 4    AIS period: 1s

MEP ID: 1

AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57

AIS state machine: Previous state: NO_RECEIVE

                   Current state: RECEIVE

MEP ID: 2

AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57

AIS state machine: Previous state: NO_RECEIVE

                   Current state: RECEIVE

Service instance: 20

AIS level: 3    AIS period: 60s

MEP ID: 10

AIS condition: yes   Time to enter the condition: 2013/01/22 10:43:57

AIS state machine: Previous state: NO_RECEIVE

                   Current state: RECEIVE

Service instance: 100

AIS level: 6    AIS period: 1s

MEP ID: 20

AIS condition: no    Time to enter the condition: 2013/01/22 11:40:01

AIS state machine: Previous state: IDLE

                   Current state: NO_RECEIVE

MEP ID: 50

AIS condition: no    Time to enter the condition: -

AIS state machine: Previous state: IDLE

                   Current state: NO_RECEIVE

表1-8 display cfd ais命令显示信息描述表

字段

描述

Service instance

MEP所在的服务实例

AIS level

AIS报文的发送级别

AIS period

AIS报文的发送周期

MEP ID

MEP的编号

AIS condition

抑制告警的状态：

·yes：表示正在抑制告警

·no：表示没有抑制告警

Time to enter the condition

上次进入抑制告警状态的时间（"-"表示开启了告警抑制功能，但MEP从未收到过AIS报文）

AIS state machine

AIS报文接收状态机

Previous state

上一个状态：

·IDLE：表示未激活

·NO_RECEIVE：表示激活

·RECEIVE：表示收到AIS报文

Current state

当前状态：

·IDLE：表示未激活

·NO_RECEIVE：表示激活

·RECEIVE：表示收到AIS报文

**CFD \-- CFD配置命令 \-- display cfd ais-track link-status**

------------------------------------------------------------------------

![说明](CFD命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[display cfd ais-track link-status**]命令用来显示与端口状态相关联的AIS的配置和动态信息。

【命令】

**[display cfd ais-track link-status** [ **interface** *interface-type interface-number *]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface ***interface-type interface-number*]：显示指定端口的信息，*interface-type interface-number*表示端口类型和端口编号。如果未指定本参数，将显示所有端口的信息。

【举例】

\# 显示与所有端口的端口状态相关联的AIS的配置和动态信息。

\<Sysname\> display cfd ais-track link-status

AIS tracking link-status is enabled.

Interface GigabitEthernet1/0/1:

AIS level: 5          AIS period: 1s

Configured VLANs: 1, 10-100, 103

Send VLANs: 1, 10-100, 103

AIS condition: yes     Time to enter the condition: 2013/02/26 10:43:57

Interface GigabitEthernet1/0/2:

AIS level: 5          AIS period: 1s

Configured VLANs: 1-4094

Send VLANs: 1-2000

AIS condition: yes     Time to enter the condition: 2013/02/26 10:44:57

表1-9 display cfd ais-track link-status命令显示信息描述表

字段

描述

AIS tracking link-status is enabled

端口状态与AIS联动功能处于开启状态

AIS tracking link-status is disabled

端口状态与AIS联动功能处于关闭状态

Interface

与AIS联动的端口

AIS level

端口上EAIS报文的发送级别

AIS period

端口上EAIS报文的发送周期

Configured VLANs

端口上配置的EAIS报文发送的VLAN范围

Send VLANs

端口上实际的EAIS报文发送的VLAN范围

AIS condition

EAIS报文的发送状态：

·yes：表示正在发送EAIS报文

·no：表示没有发送EAIS报文

Time to enter the condition

最近一次链路故障激发EAIS报文发送的时间

**CFD \-- CFD配置命令 \-- display cfd dm one-way history**

------------------------------------------------------------------------

**[display cfd dm one-way history**]命令用来显示单向时延的测试结果。

【命令】

**[display cfd dm one-way history** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance*** instance-id*]：显示指定服务实例内的测试结果，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例内的测试结果。

**[mep*** mep-id*]：显示指定MEP的测试结果，*mep-id*的取值范围为1～8191。如果未指定本参数，将显示所有MEP的测试结果。

【使用指导】

对于内向MEP，其所属服务实例内所有MEP的单向时延测试结果都相同。

【举例】

\# 显示所有服务实例内所有MEP上单向时延的测试结果。

\<Sysname\> display cfd dm one-way history

Service instance: 1

MEP ID: 1003

Sent 1DM total number: 0

Received 1DM total number: 5

Frame delay: 10ms 9ms 11ms 5ms 5ms

Delay average: 8ms

Frame delay variation: 5ms 4ms 6ms 0ms 0ms

Variation average: 3ms

MEP ID: 1004

Sent 1DM total number: 0

Received 1DM total number: 5

Frame delay: 10ms 9ms 11ms 5ms 5ms

Delay average: 8ms

Delay variation: 5ms 4ms 6ms 0ms 0ms

Variation average: 3ms

Service instance: 2

No MEP exists in the service instance.

Service instance: 3

MEP ID: 1023

Sent 1DM total number: 5

Received 1DM total number: 10

Frame delay: 20ms 9ms 8ms 7ms 1ms 5ms 13ms 17ms 9ms 10ms

Delay average: 9ms

Delay variation: 19ms 8ms 7ms 6ms 0ms 4ms 12ms 16ms 8ms 9ms

Variation average: 8ms

Service instance: 4

MEP ID: 1023

Sent 1DM total number: 77

Received 1DM total number: 0

表1-10 display cfd dm one-way history命令显示信息描述表

字段

描述

Service instance

MEP所在的服务实例

MEP ID

MEP的编号

Sent 1DM total number

发出的1DM报文数量

Received 1DM total number

收到的1DM报文数量

Frame delay

帧时延

Delay average

帧时延的平均值

Delay variation

帧时延变化

Variation average

帧时延变化的平均值

No MEP exists in the service instance

本服务实例内没有MEP

【相关命令】

·**cfd ****dm one-way**

·**reset cfd dm one-way history**

**CFD \-- CFD配置命令 \-- display cfd linktrace-reply**

------------------------------------------------------------------------

**[display cfd linktrace-reply**]命令用来显示MEP上获得的LTR报文信息。

【命令】

**[display cfd linktrace-reply** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance*** instance-id*]：显示指定服务实例内的信息，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例内的信息。

**[mep*** mep-id*]：显示指定MEP的信息，*mep-id*的取值范围为1～8191。如果未指定本参数，将显示所有MEP的信息。

【使用指导】

本命令只显示执行**cfd linktrace**命令所收到的LTR报文信息。

【举例】

\# 显示所有服务实例内所有MEP保存的LTR报文信息。

\<Sysname\> display cfd linktrace-reply

Service instance: 1       MEP ID: 1003

MAC address               TTL     Last MAC          Relay action

0000-fc00-6505            63      0000-fc00-6504    MPDB

000f-e269-a852            62      0000-fc00-6505    FDB

0000-fc00-6508            61      000f-e269-a852    Hit

Service instance: 2       MEP ID: 1023

MAC address               TTL     Last MAC          Relay action

0000-fc00-6508            61      000f-e269-a852    Hit

表1-11 display cfd linktrace-reply命令显示信息描述表

字段

描述

Service instance

发送LTM报文的MEP所在的服务实例

MEP ID

发送LTM报文的MEP的编号

MAC address

LTR报文中的源MAC地址

TTL

LTM经过此设备时的TTL值

Last MAC

LTM报文所经过上一跳设备的MAC地址

Relay action

表示转发设备在MAC地址表中是否找到了目标MAC地址：

·Hit：表示本设备就是目标MAC地址

·FDB：表示在转发表中找到了目标MAC地址

·MPDB：表示没有找到目标MAC地址，或者在MEP或MIP数据库中找到了目标MAC地址

【相关命令】

·**cfd linktrace**

**CFD \-- CFD配置命令 \-- display cfd linktrace-reply auto-detection**

------------------------------------------------------------------------

**[display cfd linktrace-reply auto-detection**]命令用来显示自动发送LTM报文后收到的LTR报文信息。

【命令】

**[display cfd linktrace-reply auto-detection ** **size** *size-value* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[size*** size-value*]：显示最近*size-value*次自动检测的结果，*size-value*的取值范围为1～100。如果未指定本参数，将显示缓冲区中的全部信息。

【使用指导】

本命令只显示执行**cfd linktrace auto-detection**命令所收到的LTR报文信息。

【举例】

\# 显示自动发送LTM报文所收到的LTR报文的内容。

\<Sysname\> display cfd linktrace-reply auto-detection

Service instance: 1       MEP ID: 1003    Time: 2013/05/22 10:43:57

Target MEP ID: 2005       TTL: 64

MAC address               TTL     Last MAC          Relay action

0000-fc00-6505            63      0000-fc00-6504    MPDB

000f-e269-a852            62      0000-fc00-6505    FDB

0000-fc00-6508            61      000f-e269-a852    Hit

Service instance: 2       MEP ID: 1023    Time: 2013/05/22 10:44:06

Target MEP ID: 2025       TTL: 64

MAC address               TTL     Last MAC          Relay action

0000-fc00-6508            61      000f-e269-a852    Hit

表1-12 display cfd linktrace-reply auto-detection命令显示信息描述表

字段

描述

Service instance

发送LTM报文的MEP所在的服务实例

MEP ID

发送LTM报文的MEP的编号

Time

自动发送LTM报文的时间

Target MEP ID

目标MEP的编号

TTL

自动发送的LTM报文中的初始TTL值

MAC address

LTR报文的源MAC地址

TTL

LTM报文经过此设备时的TTL值

Last MAC

LTM报文所经过上一跳设备的MAC地址

Relay action

表示转发设备在MAC地址表中是否找到了目标MAC地址：

·Hit：表示本设备就是目标MAC地址

·FDB：表示在转发表中找到了目标MAC地址

·MPDB：表示没有找到目标MAC地址，或者在MEP或MIP数据库中找到了目标MAC地址

【相关命令】

·**cfd linktrace auto-detection**

**CFD \-- CFD配置命令 \-- display cfd md**

------------------------------------------------------------------------

**[display cfd md**]命令用来显示MD的配置信息。

【命令】

**[display cfd md**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示MD的配置信息。

\<Sysname\> display cfd md

CFD is enabled.

Maintenance domains configured: 4 in total

Level  Index      Maintenance domain                          MD format  MD ID

0      1          md_0                                        CHARSTRING md_0

1      2          md_1                                        DNS        dns1

2      3          md_2                                        MAC        0001-00

01-0001-1

3      4          md_3                                        NONE       Without

 ID

表1-13 display cfd md命令显示信息描述表

字段

描述

CFD is enabled

表示CFD功能处于开启状态

CFD is disabled

表示CFD功能处于关闭状态

Maintenance domains configured

系统配置的MD个数

Level

MD级别

Index

MD索引号

Maintenance domain

MD名称

MD format

MD名称的格式：

·CHARSTRING：表示字符串格式

·DNS：表示采用DNS名称

·MAC：表示由MAC地址和一个整数构成

·NONE：表示不携带MD名称

MD ID

MD ID的值：

·在CHARSTRING格式下，显示MD名称本身

·在DNS格式下，显示为DNS名称

·在MAC格式下，显示方式为MAC address-Subnumber

·在NONE格式下，显示为Without ID

**CFD \-- CFD配置命令 \-- display cfd mep**

------------------------------------------------------------------------

**[display cfd mep**]命令用来显示MEP的属性和运行信息。

【命令】

**[display cfd mep ***mep-id*** service-instance ***instance-id*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[mep ***mep-id*]：表示MEP的编号，*mep-id*的取值范围为1～8191。

**[service-instance*** instance-id*]：表示服务实例的编号，*instance-id*的取值范围为1～32767。

【举例】

\# 显示服务实例1内MEP 50的属性和运行信息。

\<Sysname\> display cfd mep 50 service-instance 1

Interface: GigabitEthernet1/0/2

Maintenance domain: md_0

Maintenance domain index：1

Maintenance association: ma_0

Maintenance association index：1

Level: 0        VLAN: 1         Direction: Outbound

Current state: Active          CCM send: Enabled

FNG state: FNG_DEFECT_REPORTED

CCM:

Current state: CCI_WAITING

Interval: 1s        SendCCM: 12018

Loopback:

NextSeqNumber: 8877

SendLBR: 0          ReceiveInOrderLBR: 0          ReceiveOutOrderLBR: 0

Linktrace:

NextSeqNumber: 8877

SendLTR: 0          ReceiveLTM: 0

No CCM received from some remote MEPs.

One or more streams of error CCMs is received. The last received CCM:

Maintenance domain: (Without ID)

Maintenance association: matest1

MEP ID: 5      Sequence Number:0x50A

MAC Address: 0011-2233-4402

Received Time: 2013/03/06 13:01:34

One or more streams of cross-connect CCMs is received. The last received CCM:

Maintenance domain: mdtest1

Maintenance association:matest1

MEP ID: 6      Sequence Number:0x63A

MAC Address: 0011-2233-4401

Received Time: 2013/03/06 13:01:34

Some other MEPs are transmitting the RDI bit.

表1-14 display cfd mep命令显示信息描述表

字段

描述

Interface

MEP所在的接口

Maintenance domain

MEP所在的MD（如果MD为无MD名称的格式，则该MD的名称显示为Without ID）

Maintenance domain index

MEP所在MD的索引号

Maintenance association

MEP所在的MA

Maintenance association index

MEP所在MA的索引号

Level

MD的级别

VLAN

MA所在的VLAN

Direction

MEP的方向

Current state

MEP的当前状态，包括：

·Active：激活

·Inactive：未激活

CCM send

MEP是否发送CCM报文

FNG state

FNG（Fault Notification Generator，错误提示生成器）状态机的状态值（"-"表示不支持本字段）：

·FNG_RESET：故障已清除

·FNG_DEFECT：检测到故障

·FNG_REPORT_DEFECT：报告故障

·FNG_DEFECT_REPORTED：已报告故障

·FNG_DEFECT_CLEARING：故障清除中

CCM

与CCM报文有关的信息

Current state

CCM报文发送状态的状态值（"-"表示不支持本字段）：

·CCI_IDLE：初始状态

·CCI_WAITING：发送状态

Interval

CCM报文发送的时间间隔（"Not supported"表示该MEP不支持该间隔的检测）

SendCCM

MEP已发送的CCM报文的数量（"-"表示不支持本字段）

Loopback

与环回相关的信息

NextSeqNumber

下一个要发送的LBM报文的序号

SendLBR

MEP已发送的LBR报文的数量。如果MEP为入方向，则不进行LBR报文的计数

ReceiveInOrderLBR

MEP收到的序列正确的LBR报文的数量

ReceiveOutOrderLBR

MEP收到的乱序的LBR报文的数量

Linktrace

与链路跟踪相关的信息

NextSeqNumber

下一个要发送的LTM报文的序号

SendLTR

MEP已发送的LTR报文的数量。如果MEP为入方向，则不进行LTR报文的计数

ReceiveLTM

MEP收到的LTM报文的数量

No CCM received from some remote MEPs.

表明没有收到某些远端MEP发送的CCM报文（本信息在有CCM报文丢失的时候才会显示）

One or more streams of error CCMs is received. The last received CCM:

表明收到了错误的CCM报文，并显示最后一个错误的CCM报文的内容（本信息在收到了错误的CCM报文时才会显示）

Maintenance domain

最后一个错误CCM报文所属的MD（"-"表示不支持本字段）

Maintenance association

最后一个错误CCM报文所属的MA（"-"表示不支持本字段）

MEP

发送最后一个错误CCM报文的MEP编号（"-"表示不支持本字段）

Sequence Number

最后一个错误CCM报文的序列号（"-"表示不支持本字段）

MAC Address

发送错误CCM报文的MAC地址

Received Time

收到最后一个错误CCM报文的时间（"-"表示不支持本字段）

One or more streams of cross-connect CCMs is received. The last received CCM:

网络的配置中可能存在有交叉连接的情况，本信息表明收到了交叉连接的报文，并显示最后一个交叉连接的报文的内容（本信息在收到CCM报文后，认为属于交叉连接时才显示）

Some other MEPs are transmitting the RDI bit.

收到了其他MEP发送的RDI（Remote Defect Indication，远程故障指示）标志位被置位的CCM报文（本信息在收到该种类型的CCM报文后才显示）

**CFD \-- CFD配置命令 \-- display cfd meplist**

------------------------------------------------------------------------

**[display cfd meplist**]命令用来显示服务实例内的MEP列表。

【命令】

**[display cfd meplist** [ **service-instance** *instance-id* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance*** instance-id*]：显示指定服务实例内的MEP列表，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例内的MEP列表。

【举例】

\# 显示服务实例5内的MEP列表。

\<Sysname\> display cfd meplist service-instance 5

Service instance: 5

MEP list: 1 to 20, 30, 50.

表1-15 display cfd meplist命令显示信息描述表

字段

描述

Service instance

MEP所在的服务实例

MEP list

MEP列表，NULL表示该服务实例没有MEP列表

**CFD \-- CFD配置命令 \-- display cfd mp**

------------------------------------------------------------------------

**[display cfd mp**]命令用来显示MP的信息。

【命令】

**[display cfd mp ** **interface** *interface-type interface-number* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[interface*** interface-type interface-number*]：显示指定接口上的信息，*interface-type interface-number*表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的信息。

【使用指导】

MP信息的显示顺序：按照接口名称的顺序排列；在同一个接口上，按照先显示服务于VLAN的MP,再显示不服务于任何VLAN的MP的顺序排列。服务于VLAN的MP按照VLAN ID从小到大的顺序排列；在同一个VLAN内按照MIP、MEP（级别从高到低）的顺序排列；不服务于任何VLAN的MEP按级别从高到低的顺序排列。

【举例】

\# 显示所有接口上MP的信息。

\<Sysname\> display cfd mp

Interface GigabitEthernet1/0/1   VLAN 100

MIP              Level: 2    Service instance: 102

Maintenance domain: md_2

Maintenance domain index：3

Maintenance association: ma_2

Maintenance association index: 3

MEP ID: 101      Level: 1    Service instance: 101    Direction: Inbound

Maintenance domain: md_1

Maintenance domain index：2

Maintenance association: ma_1

Maintenance association index: 2

MEP ID: 100      Level: 0    Service instance: 100    Direction: Outbound

Maintenance domain: md_0

Maintenance domain index：1

Maintenance association: ma_0

Maintenance association index: 1

表1-16 display cfd mp命令显示信息描述表

字段

描述

Interface GigabitEthernet1/0/1   VLAN 100

接口GigabitEthernet1/0/1在VLAN 100中的MP信息

MIP

该MP是MIP

Level

MP所处的MD级别

Service instance

MP所在的服务实例

Maintenance domain

MP所属的MD

Maintenance domain  index

MP所属MD的索引号

Maintenance association

MP所属的MA

Maintenance association index

MP所属MA的索引号

MEP ID

MEP的编号

Direction

MEP的方向：

·Inbound：表示入方向

·Outbound：表示出方向

**CFD \-- CFD配置命令 \-- display cfd remote-mep**

------------------------------------------------------------------------

**[display cfd remote-mep**]命令用来显示远端MEP的信息。

【命令】

**[display cfd remote-mep service-instance ***instance-id*** mep ***mep-id*]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance*** instance-id*]：显示指定服务实例内的远端MEP信息，*instance-id*的取值范围为1～32767。

**[mep*** mep-id*]：显示指定MEP所对应的远端MEP信息，*mep-id*的取值范围为1～8191。

【举例】

\# 显示服务实例4内MEP 10所对应的远端MEP信息。

\<Sysname\> display cfd remote-mep service-instance 4 mep 10

MEP ID   MAC address      State        Time                  MAC status

20       00e0-fc00-6565   OK           2013/03/06 02:36:38   UP

30       00e0-fc27-6502   OK           2013/03/06 02:36:38   DOWN

40       00e0-fc00-6510   FAILED       2013/03/06 02:36:39   DOWN

50       00e0-fc52-baa0   OK           2013/03/06 02:36:44   DOWN

60       0010-fc00-6502   OK           2013/03/06 02:36:42   DOWN

表1-17 display cfd remote-mep命令显示信息描述表

字段

描述

MEP ID

远端MEP的编号

MAC address

远端MEP所在设备的MAC地址（"-"表示不支持本字段）

State

远端MEP的运行状态：

·OK

·FAILED

Time

远端MEP最后进入FAILED或OK状态的时间（"-"表示不支持本字段）

MAC status

最后一次收到的远端MEP发送的CCM报文中表示该MEP所在接口的状态（"-"表示不支持本字段）：

·UP：表示已准备好传输报文

·DOWN：表示无法传输报文

·TESTING：表示处于测试模式

·UNKNOWN：表示状态无法确认

·DORMANT：表示处于休眠中

·NOT-PRESENT：表示某些组件不在位

·LLD：表示因底层无连接而down掉

**CFD \-- CFD配置命令 \-- display cfd service-instance**

------------------------------------------------------------------------

**[display cfd service-instance**]命令用来显示服务实例的配置信息。

【命令】

**[display cfd service-instance ** *instance-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[instance-id*]：显示指定服务实例的信息，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例的信息。

【举例】

\# 显示所有服务实例的配置信息。

\<Sysname\> display cfd service-instance

Service instances configured (2 in total):

Service instance 5:

Maintenance domain: md_5

Maintenance domain index: 5

Maintenance association: ma_5

Maintenance association index: 5

Level: 5  VLAN: 5   MIP rule: NONE   CCM interval: 1s   Direction: Inbound

MEP ID: 730  Interface: GigabitEthernet1/0/1

Service instance 6:

Maintenance domain: (Without ID)

Maintenance domain index: 6

Maintenance association: ma_6

Maintenance association index: 6

Level: 6  VLAN: 6   MIP rule: NONE   CCM interval: 1s   Direction: Outbound

MEP ID: 731  Interface: GigabitEthernet1/0/2

表1-18 display cfd service-instance命令显示信息描述表

字段

描述

Service instances configured

系统中配置的服务实例的个数

Service instance

服务实例的编号

Maintenance domain

该服务实例所在的MD（如果MD为无MD名称的格式，则该MD的名称显示为Without ID）

Maintenance domain index

该服务实例所在MD的索引号

Maintenance association:

该服务实例所在的MA

Maintenance association index

该服务实例所在MA的索引号

Level

MD的级别

VLAN

MA所在的VLAN

MIP rule

服务实例上配置的创建MIP的规则

CCM interval

该服务实例内的MEP发送CCM报文的间隔

Direction

在服务实例上配置的MEP的方向

MEP ID

在服务实例上配置的MEP的编号

Interface

在服务实例上配置的MEP所处的接口

**CFD \-- CFD配置命令 \-- display cfd status**

------------------------------------------------------------------------

**[display cfd status**]命令用来显示CFD和AIS的开启状态。

【命令】

**[display cfd status**]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【举例】

\# 显示CFD的开启状态。

\<Sysname\> display cfd status

CFD is enabled.

AIS is disabled.

表1-19 display cfd status命令显示信息描述表

字段

描述

CFD is enabled

表示CFD功能处于开启状态

AIS is enabled

表示AIS功能处于开启状态

CFD is disabled

表示CFD功能处于关闭状态

AIS is disabled

表示AIS功能处于关闭状态

**CFD \-- CFD配置命令 \-- display cfd tst**

------------------------------------------------------------------------

**[display cfd tst**]命令用来显示比特错误的测试结果。

【命令】

**[display cfd tst** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[service-instance**]* instance-id*：显示指定服务实例内的测试结果，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将显示所有服务实例内的测试结果。

**[mep*** mep-id*]：显示指定MEP的测试结果，*mep-id*的取值范围为1～8191。如果未指定本参数，将显示所有MEP的测试结果。

【使用指导】

对于内向MEP，其所属服务实例内所有MEP的比特错误测试结果都相同。

【举例】

\# 显示所有服务实例内所有MEP上比特错误的测试结果。

\<Sysname\> display cfd tst

Service instance: 1

MEP ID: 1003

Sent TST total number: 0

Received TST total number: 5

Received from 0010-fc00-6510, Bit True,  sequence number 0

Received from 0010-fc00-6510, Bit True,  sequence number 1

Received from 0010-fc00-6510, Bit True,  sequence number 2

Received from 0010-fc00-6510, Bit True,  sequence number 3

Received from 0010-fc00-6510, Bit True,  sequence number 4

MEP ID: 1004

Sent TST total number: 5

Received TST total number: 0

Service instance: 2

No MEP exists in the service instance.

Service instance: 3

MEP ID: 1023

Sent TST total number: 5

Received TST total number: 0

表1-20 display cfd tst命令显示信息描述表

字段

描述

Service instance

MEP所在的服务实例

MEP ID

MEP的编号

Sent TST total number

发送的TST报文总数

Received TST total number

收到的TST报文总数

Received from 0010-fc00-6510, Bit True,  sequence number 0

从MAC地址为0010-FC00-6510的MEP收到的序列号为0的TST报文：

·Bit True：表示没有发生比特错误

·Bit False：表示发生了比特错误

No MEP exists in the service instance

本服务实例内没有MEP

【相关命令】

·**cfd ****tst**

·**reset cfd ****tst**

**CFD \-- CFD配置命令 \-- reset cfd dm one-way history**

------------------------------------------------------------------------

**[reset cfd dm one-way history**]命令用来清除单向时延的测试结果。

【命令】

**[reset cfd dm one-way history** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance**]* instance-id*：清除指定服务实例内的测试结果，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将清除所有服务实例内的测试结果。

**[mep*** mep-id*]：清除指定MEP的测试结果，*mep-id*的取值范围为1～8191。如果未指定本参数，将清除所有MEP的测试结果。

【使用指导】

清除某内向MEP的单向时延测试结果，将会清除其所属服务实例内的所有单向时延测试结果。

【举例】

\# 清除所有服务实例内所有MEP上单向时延的测试结果。

\<Sysname\> reset cfd dm one-way history

【相关命令】

·**cfd ****dm one-way**

·**display cfd dm one-way history**

**CFD \-- CFD配置命令 \-- reset cfd tst**

------------------------------------------------------------------------

**[reset cfd tst**]命令用来清除比特错误的测试结果。

【命令】

**[reset cfd tst** [ **service-instance** *instance-id* [ **mep** *mep-id*  ]]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[service-instance**]* instance-id*：清除指定服务实例内的测试结果，*instance-id*为服务实例的编号，取值范围为1～32767。如果未指定本参数，将清除所有服务实例内的测试结果。

**[mep*** mep-id*]：清除指定MEP的测试结果，*mep-id*的取值范围为1～8191。如果未指定本参数，将清除所有MEP的测试结果。

【使用指导】

清除某内向MEP的比特错误测试结果，将会清除其所属服务实例内的所有比特错误测试结果。

【举例】

\# 清除所有服务实例内所有MEP上比特错误的测试结果。

\<Sysname\> reset cfd tst

【相关命令】

·**cfd ****tst**

·**display cfd tst**

