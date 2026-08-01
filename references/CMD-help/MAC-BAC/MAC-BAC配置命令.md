<!-- CMD-INDEX
  display wlan ap-list                | 任意视图             | L15
  display wlan bas-ac                 | 任意视图             | L75
  display wlan client                 | 任意视图             | L163
  mac-address                         | AP列表视图           | L231
  wlan ap-list                        | 系统视图             | L277
  wlan bas-ac ap aging-time           | 系统视图             | L325
  wlan bas-ac authentication          | 系统视图             | L365
  wlan bas-ac client aging-time       | 系统视图             | L419
  wlan load-balance ap ap-list        | 系统视图             | L459
  wlan master-ac enable               | 系统视图             | L505
  wlan master-ac port                 | 系统视图             | L541
-->

**MAC-BAC \-- MAC-BAC配置命令 \-- display wlan ap-list**

------------------------------------------------------------------------

**[display wlan ap-list**]命令用来显示AP列表的信息。

【命令】

**[display wlan ap-list **] *ap-list-name*

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[ap-list-name*]：AP列表的名字，为1～31个字符的字符串，区分大小写。如果未指定本参数，则显示所有的AP列表信息。

【举例】

\# 显示所有的AP列表信息。

\<Sysname\> display wlan ap-list

AP-list name: name1

Number of APs: 2

 mac-address 0000-e27c-6e80

 mac-address 0000-e27c-79fa 

表1-1 display wlan ap-list命令显示信息描述表

字段

描述

AP-list name

AP列表名称

Number of APs

AP列表中的AP数量

mac-address

AP的MAC地址

**MAC-BAC \-- MAC-BAC配置命令 \-- display wlan bas-ac**

------------------------------------------------------------------------

**[display wlan bas-ac**]命令用来显示Master AC管理的BAS AC信息。

【命令】

**[display **]**wlan bas-ac**\**[mac-address ***mac-address*  **verbose** ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[mac-address **]*mac-address*：显示指定MAC地址的BAS AC的信息。如果未指定本参数，则显示所有BAS AC的信息。

**[verbose**]：显示BAS AC的详细信息。如果未指定本参数，则显示BAS AC的简要信息。

【举例】

\# 显示指定MAC地址的BAS AC的简要信息。

\<Sysname\> display wlan bas-ac mac-address 000f-e212-ff01

MAC address            IP address             AP count/Maximum AP capacity

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

000f-e212-ff01         192.168.33.21          1/192

\# 显示指定MAC地址的BAS AC的详细信息。

\<Sysname\> display wlan bas-ac mac-address 000f-e212-ff01 verbose

MAC address                 :000f-e212-ff01

IP address                  :192.168.33.21

CAPWAP IP address           :192.168.33.22

CAPWAP IPv6 address         :NA

AP count                    :1

Maximum AP capacity         :192

表1-2 display wlan bas-ac命令显示信息描述表

字段

描述

MAC address

BAS AC的MAC地址

IP address

BAS AC的IP地址

AP count/Maximum AP capacity

与BAS AC建立隧道的AP数量/BAS AC上可支持隧道连接的最大AP数量

CAPWAP IP address

Master AC获取到BAS AC上报的CAPWAP IPv4地址

NA表示Master AC没有获取到BAS AC上报的CAPWAP IP地址

CAPWAP IPv6 address

Master AC获取到BAS AC上报的CAPWAP IPv6地址

NA表示Master AC没有获取到BAS AC上报的CAPWAP IPv6地址

**MAC-BAC \-- MAC-BAC配置命令 \-- display wlan client**

------------------------------------------------------------------------

**[display wlan client**]命令用来显示Master AC管理的各BAS AC上的客户端信息。

【命令】

**[display wlan client****mac-address**[ *mac-address* \| **bas-ac mac-address** *mac-address* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[mac-address*** mac-address*]：显示指定MAC地址的客户端信息。

**[bas-ac **]**mac-address ***mac-address*：显示指定MAC地址的BAS AC上的所有客户端信息。

【使用指导】

如果未指定**mac-address**或**bas-ac mac-address**参数，则显示Master AC管理的所有客户端的信息。

【举例】

\# 显示指定MAC地址的客户端信息。

\<Sysname\> display wlan client mac-address 001c-f08f-f804

MAC address       IP address        BAS-AC MAC address       BAS-AC IP address 

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- 

001c-f08f-f804    192.168.11.11     000f-e212-ff01           192.168.33.21

表1-3 display wlan client命令显示信息描述表

字段

描述

MAC Address

客户端的MAC地址

IP Address

客户端的IP地址

BAS-AC MAC Address

客户端所在BAS AC的MAC地址

BAS-AC IP Address

客户端所在BAS AC的IP地址

**MAC-BAC \-- MAC-BAC配置命令 \-- mac-address**

------------------------------------------------------------------------

**[mac-address**]命令用来将与指定MAC地址匹配的AP加入到AP列表中。

**[undo mac-address**]命令用来删除已配置的MAC地址。

【命令】

**[mac-address **]*mac-address*

**[undo mac-address **] *mac-address*

【缺省情况】

AP列表中不存在AP成员。

【视图】

AP列表视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[mac-address*]：AP成员的MAC地址，与该MAC地址匹配的AP加入到AP列表中。

【使用指导】

执行**undo mac-address**命令时，如果未指定任何参数，则删除AP列表中的所有MAC地址。

【举例】

\# 将MAC地址为000f-e233-9000的AP加入到名字为name1的AP列表。

\<Sysname\> system-view

Sysname wlan ap-list name1

Sysname-wlan-aplist-name1 mac-address 000f-e233-9000

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan ap-list**

------------------------------------------------------------------------

**[wlan ap-list**]命令用来创建AP列表。

**[undo **]**wlan ap-list**命令用来删除AP列表。

【命令】

**[wlan ap-list**]*ap-list-name*

**[undo wlan ap-list **] *ap-list-name*

【缺省情况】

不存在AP列表。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ap-list-name*]：AP列表的名字，为1～31个字符的字符串，区分大小写。

【使用指导】

·一个AP可以加入不同的AP列表。

·执行**undo wlan ap-list**命令时，如果未指定任何参数，则删除所有AP列表。

【举例】

\# 创建名字为name1的AP列表。

\<Sysname\> system-view

Sysname wlan ap-list name1

Sysname-wlan-aplist-name1

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan bas-ac ap aging-time**

------------------------------------------------------------------------

**[wlan bas-ac ap aging-time**]命令用来配置BAS AC与Master AC断开连接后，BAS AC上AP信息的老化时间。

**[undo wlan bas-ac ap aging-time**]命令用来恢复缺省情况。

【命令】

**[wlan bas-ac ap aging-time **]*seconds*

**[undo wlan bas-ac ap aging-time**]

【缺省情况】

BAS AC上AP信息的老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：BAS AC上AP信息的老化时间，取值范围为1～60，单位为秒。

【举例】

\# 配置BAS AC上的AP信息老化时间为10秒。

\<Sysname\> system-view

Sysname wlan bas-ac ap aging-time 10

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan bas-ac authentication**

------------------------------------------------------------------------

**[wlan bas-ac authentication**]命令用来配置用于验证BAS AC报文的密钥。

**[undo wlan bas-ac authentication**]命令用来删除已配置的密钥。

【命令】

**[wlan bas-ac authentication**[ { **cipher** \| **simple** } *authentication-key*]]

**[undo wlan bas-ac authentication**]

【缺省情况】

没有配置用于验证BAS AC报文的密钥。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[cipher**]：以密文方式设置密钥。

**[simple**]：以明文方式设置密钥。

*[authentication-key*]：设置的明文密钥或密文密钥，区分大小写。明文密钥为1～16个字符的字符串，密文密钥为24～53个字符的字符串。

【使用指导】

配置认证功能后，Master AC发送报文时会使用MD5算法对报文内容计算出消息摘要，并将消息摘要添加到发送的报文中。BAS AC接收到报文后，也进行同样地计算，并将计算结果和消息中的摘要进行比较。如果一致，则认证通过，接收该消息；否则认证失败，丢弃该消息。

需要注意的是：

·以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。

·在BAS AC和MAC AC上需要配置相同的密钥。

【举例】

\# 配置BAS AC的密钥为明文12345。

\<Sysname\> system-view

Sysname wlan bas-ac authentication simple 12345

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan bas-ac client aging-time**

------------------------------------------------------------------------

**[wlan bas-ac client aging-time**]命令用来配置BAS AC与Master AC断开连接后，BAS AC上客户端信息的老化时间。

**[undo wlan bas-ac client aging-time**]命令用来恢复缺省情况。

【命令】

**[wlan bas-ac client aging-time **]*seconds*

**[undo wlan bas-ac client aging-time**]

【缺省情况】

BAS AC上客户端信息的老化时间为30秒。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[seconds*]：BAS AC上客户端信息的老化时间，取值范围为1～60，单位为秒。

【举例】

\# 配置BAS AC上客户端信息老化时间为10秒。

\<Sysname\> system-view

Sysname wlan bas-ac client aging-time 10

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan load-balance ap ap-list**

------------------------------------------------------------------------

**[wlan load-**]**balance ap ap-list**命令用来配置基于热点分配BAS AC功能，即将AP列表下的AP分配到同一个BAS AC上。

**[undo wlan load-**]**balance ap ap-list**命令取消配置基于热点分配BAS AC功能。

【命令】

**[wlan load-**]**balance ap ap-list ***ap-list-name*

**[undo wlan load-**]**balance ap ap-list** [ *ap-list-name* ]

【缺省情况】

没有配置基于热点分配BAS AC功能，即由Master AC根据负载均衡算法为AP指定BAS AC。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[ap-list-name*]：基于热点分配BAS AC的AP列表，为1～31个字符的字符串，区分大小写。

【使用指导】

·多次执行**wlan load-balance ap ap-list**命令，可以配置对多个AP列表开启基于热点分配BAS AC功能。

·执行**undo wlan load-balance ap ap-list**命令时，如果未指定任何参数，则取消所有已配置的基于热点分配BAS AC功能。

【举例】

\# 配置基于热点分配BAS AC功能，将名字为name1的AP列表下的AP分配到同一个BAS AC上。

\<Sysname\> system-view

Sysname wlan load-balance ap ap-list name1

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan master-ac enable**

------------------------------------------------------------------------

**[wlan master-ac enable**]命令用来开启Master AC功能。

**[undo wlan master-ac enable**]命令用来关闭Master AC功能。

【命令】

**[wlan master-ac enable**]

**[undo wlan master-ac enable**]

【缺省情况】

Master AC功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【举例】

\# 开启Master AC功能。

\<Sysname\> system-view

Sysname wlan master-ac enable

**MAC-BAC \-- MAC-BAC配置命令 \-- wlan master-ac port**

------------------------------------------------------------------------

**[wlan master-ac port**]命令用来配置Master AC的端口号。

**[undo wlan master-ac port**]命令用来恢复缺省情况。

【命令】

**[wlan master-ac port ***port-number*]

**[undo wlan master-ac port** *port-number*]

【缺省情况】

Master AC的端口号为35001。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[port-number*]：Master AC的端口号，取值范围为1～65535。

【举例】

\# 配置Master AC的端口号为5000。

\<Sysname\> system-view

Sysname wlan master-ac port 5000

