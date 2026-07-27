<!-- CMD-INDEX
  ip irdp                             | 接口视图             | L10
  ip irdp address                     | 接口视图             | L64
  ip irdp lifetime                    | 接口视图             | L130
  ip irdp interval                    | 接口视图             | L196
  ip irdp multicast                   | 接口视图             | L264
  ip irdp preference                  | 接口视图             | L318
-->

**IRDP命令 \-- IRDP配置命令 \-- ip irdp**

------------------------------------------------------------------------

**[ip irdp**]命令用来使能接口的IRDP功能。

**[undo ip irdp**]命令用来关闭接口的IRDP功能。

【命令】

**[ip irdp**]

**[undo ip irdp**]

【缺省情况】

接口的IRDP功能处于关闭状态。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

只有使能接口的IRDP功能，其他IRDP相关配置才生效，设备才会从该接口发送路由公告消息RA（Router Advertisements）。

【举例】

l路由应用

\# 使能接口GigabitEthernet1/0/1的IRDP功能。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp

l交换应用

\# 使能VLAN接口100的IRDP功能。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp

**IRDP命令 \-- IRDP配置命令 \-- ip irdp address**

------------------------------------------------------------------------

**[ip** **irdp address**]命令用来配置接口代理公告的IP地址。

**[undo ip** **irdp address** *ip-address*]命令用来取消指定的接口代理公告的IP地址。

**[undo ip** **irdp address**]命令用来取消所有接口代理公告的IP地址。

【命令】

**[ip** **irdp address** *ip-address preference-value*]

**[undo ip** **irdp address** [ *ip-address* ]]

【缺省情况】

未配置接口代理公告的IP地址。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ip-address*]：代理公告的IP地址，为点分十进制格式，配置后接口发送的RA消息中除了该接口自己的IP地址，还包含这个代理公告IP地址。

*[preference-value*]：代理公告的IP地址的优先级，取值范围为-2147483648～2147483647。

【使用指导】

该命令支持重复配置，设备上接口最多支持配置4个代理公告的IP地址。

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1代理公告的IP地址为192.168.0.8，优先级为1600。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp address 192.168.0.8 1600

l交换应用

\# 配置VLAN接口100代理公告的IP地址为192.168.0.8，优先级为1600。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp address 192.168.0.8 1600

【相关命令】

l**ip irdp**

**IRDP命令 \-- IRDP配置命令 \-- ip irdp lifetime**

------------------------------------------------------------------------

**[ip** **irdp lifetime**]命令用来配置接口公告的IP地址的生命周期。

**[undo ip** **irdp lifetime**]命令用来恢复缺省情况。

【命令】

**[ip** **irdp lifetime** *lifetime-value*]

**[undo ip** **irdp lifetime**]

【缺省情况】

接口公告的IP地址的生命周期为1800秒。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[lifetime-value*]：公告的IP地址的生命周期，取值范围为4～9000，单位为秒。

【使用指导】

配置的IP地址的生命周期必须大于等于接口发送周期性RA的最大时间间隔，否则，系统会提示配置错误。

本配置对接口公告出去的所有IP地址（包括接口IP地址和代理公告的IP地址）有效。

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1公告的IP地址的生命周期为2000秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp lifetime 2000

l交换应用

\# 配置VLAN接口100公告的IP地址的生命周期为2000秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp lifetime 2000

【相关命令】

l**ip irdp**

l**ip irdp interval**

**IRDP命令 \-- IRDP配置命令 \-- ip irdp interval**

------------------------------------------------------------------------

**[ip irdp interval**]命令用来配置接口发送周期性RA的最大时间间隔和最小时间间隔。

**[undo ip irdp interval**]命令用来恢复缺省情况。

【命令】

**[ip irdp interval ***max-interval-value * *min-interval-value* ]

**[undo ip irdp interval**]

【缺省情况】

接口发送周期性RA的最大时间间隔为600秒，最小时间间隔为最大时间间隔的0.75倍。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[max-interval-value*]：发送周期性RA的最大时间间隔，取值范围为4～1800，单位为秒。

min-interval-value：发送周期性RA的最小时间间隔，取值范围为3～max-interval-value，单位为秒。

【使用指导】

发送周期性RA时，设备在最小时间间隔与最大时间间隔之间随机选取一个值作为周期性发送RA的时间间隔。

接口发送周期性RA的最大时间间隔必须小于等于接口公告的IP地址的生命周期。如果配置的最大时间间隔大于生命周期，那么系统会将生命周期自动调整为最大时间间隔的3倍。

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1发送周期性RA的最大时间间隔为500秒，最小时间间隔为300秒。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp interval 500 300

l交换应用

\# 配置VLAN接口100发送周期性RA的最大时间间隔为500秒，最小时间间隔为300秒。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp interval 500 300

【相关命令】

l**ip irdp**

l**ip irdp lifetime**

**IRDP命令 \-- IRDP配置命令 \-- ip irdp multicast**

------------------------------------------------------------------------

**[ip irdp multicast**]命令用来配置接口发送组播RA消息，报文的目的IP地址为224.0.0.1。

**[undo ip irdp multicast**]命令用来恢复缺省情况。

【命令】

**[ip irdp multicast**]

**[undo ip irdp multicast**]

【缺省情况】

接口发送广播RA消息。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1发送组播RA消息。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp multicast

l交换应用

\# 配置VLAN接口100发送组播RA消息。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp multicast

【相关命令】

l**ip irdp**

**IRDP命令 \-- IRDP配置命令 \-- ip irdp preference**

------------------------------------------------------------------------

**[ip** **irdp preference**]命令用来配置接口公告的接口IP地址的优先级。

**[undo ip** **irdp preference**]命令用来恢复缺省情况。

【命令】

**[ip** **irdp preference** *preference-value*]

**[undo ip** **irdp preference**]

【缺省情况】

接口公告的接口IP地址的优先级为0。

【视图】

接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[preference-value*]：公告的接口IP地址的优先级，取值范围为-2147483648～2147483647。

【使用指导】

接口公告的接口IP地址的优先级值越大，优先级越高。最小的优先级值（-2147483648）表示主机不要使用这个地址作为缺省路由。

【举例】

l路由应用

\# 配置接口GigabitEthernet1/0/1公告的接口IP地址的优先级为1。

\<Sysname\> system-view

Sysname interface gigabitethernet 1/0/1

Sysname-GigabitEthernet1/0/1 ip irdp preference 1

l交换应用

\# 配置VLAN接口100公告的接口IP地址的优先级为1。

\<Sysname\> system-view

Sysname interface vlan-interface 100

Sysname-Vlan-interface100 ip irdp preference 1

【相关命令】

l**ip irdp**
