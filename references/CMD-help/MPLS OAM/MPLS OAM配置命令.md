<!-- CMD-INDEX
  bfd discriminator                   | VSI LDP PW视图     | L18
  display l2vpn pw bfd                | 任意视图             | L94
  display mpls bfd                    | 任意视图             | L234
  mpls bfd enable                     | 系统视图             | L408
  mpls bfd (for LSP)                  | 系统视图             | L448
  mpls bfd (for TE tunnel)            | Tunnel接口视图       | L538
  mpls periodic-tracert (for LSP)     | 系统视图             | L618
  ping mpls ipv4                      | 任意视图             | L692
  ping mpls pw                        | 任意视图             | L860
  ping mpls te                        | 任意视图             | L932
  tracert mpls ipv4                   | 任意视图             | L1002
  tracert mpls te                     | 任意视图             | L1156
  vccv bfd                            | PW模板视图           | L1216
  vccv cc                             | PW模板视图           | L1286
-->

**MPLS OAM \-- MPLS OAM配置命令 \-- bfd discriminator**

------------------------------------------------------------------------

**[bfd discriminator**]命令用来配置检测PW的BFD会话的本地标识符和远端标识符。

**[undo bfd discriminator**]命令用来恢复缺省情况。

【命令】

**[bfd discriminator local** *local-id* **remote** *remote-id* ]

**[undo bfd discriminator**]

【缺省情况】

没有指定检测PW的BFD会话的本地标识符和远端标识符，系统自动为BFD会话分配本地标识符和远端标识符。

【视图】

VSI LDP PW视图

VSI static PW视图

交叉连接PW视图

VSI LDP备份PW视图

VSI static备份PW视图

交叉连接备份PW视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[local*** local-id*]：指定BFD会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[remote*** remote-id*]：指定BFD会话的远端标识符，取值范围为1～4294967295。

【使用指导】

可以通过两种方式配置检测PW的BFD会话：

·静态方式：如果通过**bfd** **discriminator**命令指定了本地和远端的标识符，则根据指定的标识符建立BFD会话。采用这种方式时，要求本地和远端设备上都通过本命令手工指定标识符，并要求两端配置的本地和远端标识符匹配（即本地PE上配置的本地标识符与远端PE上配置的远端标识符相同；本地PE上配置的远端标识符与远端PE上配置的本地标识符相同），否则无法建立检测PW的BFD会话。

·动态方式：如果没有通过**bfd** **discriminator**命令指定本地和远端的标识符，则自动运行MPLS Ping来协商标识符，并根据协商好的标识符建立BFD会话。

【举例】

\# 在VSI LDP PW视图下，配置检测该PW的BFD会话的本地标识符和远端标识符均为1。

\<Sysname\> system-view

Sysname vsi ttt

Sysname-vsi-ttt pwsignaling ldp 

Sysname-vsi-ttt-ldp peer 22.22.2.2 pw-id 1 pw-class ttt

Sysname-vsi-ttt-ldp-22.22.2.2-1 bfd discriminator local 1 remote 1

【相关命令】

·**display l2vpn pw bfd**

·**mpls bfd enable**

·**vccv bfd**

·**vccv cc**

**MPLS OAM \-- MPLS OAM配置命令 \-- display l2vpn pw bfd**

------------------------------------------------------------------------

**[display l2vpn pw bfd**]命令用来显示PW的BFD检测信息。

【命令】

**[display l2vpn pw bfd ** **peer** *peer-ip* **pw-id** *pw-id* ]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[peer** *peer-ip* **pw-id** *pw-id*]：显示指定PW的BFD检测信息。*peer-ip*为远端PE的LSR ID，*pw-id*为PW ID，取值范围为1～4294967295。如果不指定本参数，则显示所有PW的BFD检测信息。

【举例】

\# 显示所有PW的BFD检测信息。

\<Sysname\> display l2vpn pw bfd

 Total number of sessions: 1, 1 up, 0 down, 0 init

 FEC Type: PW FEC-128

 FEC Info:

   Peer IP: 22.22.2.2

   PW ID: 1

 VSI Index: 0                        Link ID: 8

 Local Discr: 514                    Remote Discr: 514

 Source IP: 11.11.1.1                Destination IP: 127.0.0.2

 Session State: Up                   Session Role: Active

 Template Name: -

表1-1 display l2vpn pw bfd命令显示信息描述表

字段

描述

Total number of sessions

BFD会话总数，及处于up、down和init状态的BFD数目

FEC Type

BFD检测的FEC类型，取值为PW FEC-128

FEC Info

FEC相关信息

Peer IP

远端PE的LSR ID

PW ID

PW ID

VSI Index

PW所属VSI的索引，当PW为VPLS的PW时显示该信息

本字段的支持情况与设备的型号有关，请以设备的实际情况为准

Connection ID

PW所属交叉连接的ID，当PW为VPWS的PW时显示该信息

Link ID

PW对应的Link ID

Local Discr

BFD会话的本地标识符

Remote Discr

BFD会话的远端标识符

Source IP

BFD会话的源IP地址，为本端设备的MPLS LSR ID

Destination IP

BFD会话的目的IP地址，为127.0.0.0/8网段的地址

Session State

BFD会话状态，取值包括：

·Init：BFD会话处于初始化状态

·Up：BFD会话处于up状态

·Down：BFD会话处于down状态

Session Role

本端设备在BFD会话中的角色，取值包括：

·Active：BFD会话的发起端

·Passive：BFD会话的接收端

Template Name

BFD会话参数的模板名称

【相关命令】

·**bfd discriminator**

·**vccv bfd**

·**vccv cc**

**MPLS OAM \-- MPLS OAM配置命令 \-- display mpls bfd**

------------------------------------------------------------------------

**[display mpls bfd**]命令用来显示LSP隧道或MPLS TE隧道的BFD检测信息。

【命令】

**[display mpls bfd **[[ **ipv4** *dest-addr* *mask-length* \| **te tunnel** *tunnel-number* ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

**[ipv4 ***dest-addr* *mask-length*]**：**显示指定FEC对应LSP的BFD检测信息。*dest-addr*为FEC目的IP地址，*mask-length*为目的地址的掩码长度，取值范围为0～32。

**[te tunnel ***tunnel-number*]**：**显示指定MPLS TE隧道的BFD检测信息。*tunnel-number*为隧道接口的编号，取值范围为设备上已经创建的MPLS TE隧道接口的编号。

【使用指导】

执行本命令时如果没有指定任何参数，则显示所有LSP隧道和MPLS TE隧道的BFD检测信息。

【举例】

\# 显示目的地址为22.22.2.2/32的LSP的BFD检测信息。

\<Sysname\> display mpls bfd ipv4 22.22.2.2 32

 Total number of sessions: 1, 1 up, 0 down, 0 init

 FEC Type: LSP

 FEC Info:

   Destination: 22.22.2.2

   Mask Length: 32

 NHLFE ID: 1025

 Local Discr: 513                    Remote Discr: 513

 Source IP: 11.11.1.1                Destination IP: 127.0.0.1

 Session State: Up                   Session Role: Passive

 Template Name: -

\# 显示接口Tunnel1对应的MPLS TE隧道的BFD检测信息。

\<Sysname\> display mpls bfd te tunnel 1

 Total number of sessions: 1, 1 up, 0 down, 0 init

 FEC Type: TE Tunnel

 FEC Info:

   Source     : 100.1.1.1

   Destination: 200.1.1.1

   Tunnel ID  : 1

   LSP ID     : 100

 NHLFE ID: 1025

 Local Discr: 513                    Remote Discr: 513

 Source IP: 11.11.1.1                Destination IP: 127.0.0.1

 Session State: Up                   Session Role: Passive

 Template Name: -

表1-2 display mpls bfd命令显示信息描述表

字段

描述

Total number of sessions

BFD会话总数，及处于up、down和init状态的BFD数目

FEC Type

BFD检测的FEC类型，取值包括LSP和TE Tunnel

FEC Info

FEC相关信息

BFD检测LSP时，FEC信息包括：

·Destination：FEC目的地址

·Mask Length：FEC目的地址掩码

BFD检测TE隧道时，FEC信息包括：

·Source：隧道的源端地址

·Destination：隧道的目的端地址

·Tunnel ID：隧道ID

·LSP ID：LSP的ID

NHLFE ID

对应的NHLFE表项ID

Local Discr

BFD会话的本地标识符

Remote Discr

BFD会话的远端标识符

Source IP

BFD会话的源IP地址，为本端设备的MPLS LSR ID

Destination IP

BFD会话的目的IP地址

·Ingress端，为127.0.0.0/8网段的地址

·Egress端，为Ingress端的MPLS LSRID

Session State

BFD会话状态，取值包括：

·Init：BFD会话处于初始化状态

·Up：BFD会话处于up状态

·Down：BFD会话处于down状态

Session Role

本端设备在BFD会话中的角色，取值包括：

·Active：BFD会话的发起端

·Passive：BFD会话的接收端

Template Name

BFD会话参数的模板名称

【相关命令】

·**mpls bfd **(for LSP)

·**mpls bfd **(for TE tunnel)

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd enable**

------------------------------------------------------------------------

**[mpls bfd enable**]命令用来使能MPLS与BFD联动功能。

**[undo mpls bfd enable**]命令用来关闭MPLS与BFD联动功能。

【命令】

**[mpls bfd enable**]

**[undo mpls bfd enable**]

【缺省情况】

MPLS  BFD功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【使用指导】

如果没有通过本命令使能MPLS与BFD联动功能，则执行**mpls bfd **(for LSP)、**mpls bfd **(for TE tunnel)或**vccv bfd**命令后，不会创建检测LSP、MPLS TE隧道、PW的BFD会话。

【举例】

\# 使能MPLS与BFD联动功能。

\<Sysname\> system-view

Sysname mpls bfd enable

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd (for LSP)**

------------------------------------------------------------------------

**[mpls bfd**]命令用来配置使用BFD检测指定FEC对应LSP的连通性。

**[undo mpls bfd**]用来取消使用BFD检测指定FEC对应LSP的连通性。

【命令】

**[mpls bfd ***dest-addr* *mask-length* [ **nexthop** *nexthop-address* [ **discriminator local** *local-id* **remote** *remote-id*  ]  **template** *template-name* ]]

**[undo mpls bfd ***dest-addr* *mask-length* [ **nexthop** *nexthop-address* ]]

【缺省情况】

未使用BFD检测FEC对应LSP的连通性。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dest-addr* *mask-length*]：FEC目的地址。

*[mask-length*]：FEC目的地址的掩码长度，取值范围为0～32。

**[nexthop** *nexthop-address*]：指定FEC下一跳地址。如果指定该参数，则只检测指定的LSP；如果不指定该参数，则检测FEC对应的所有LSP。

**[discriminator**]：指定BFD会话的标识符。

**[local*** local-id*]：指定BFD会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[remote*** remote-id*]：指定BFD会话的远端标识符，取值范围为1～4294967295。

**[template ***template-name*]：指定引用的BFD会话参数的模板名称。*template-name*为BFD会话参数模板的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

通过**mpls bfd enable**命令使能MPLS与BFD联动功能，并执行本命令后，设备上将会创建用来检测指定FEC对应LSP的BFD会话。当LSP出现故障时，BFD可以快速检测到该故障，以便设备及时进行相应地处理，如将流量切换到备份LSP。

可以通过两种方式配置检测LSP的BFD会话：

·静态方式：如果执行**mpls bfd**命令时通过**discriminator**参数指定了本地和远端的标识符，则根据指定的标识符建立BFD会话。采用这种方式时，要求本地和远端设备上都使能MPLS与BFD联动功能，通过**mpls bfd**命令配置使用BFD检测指定FEC对应LSP的连通性，并要求两端配置的本地和远端标识符匹配。该方式用来检测两台设备间从本地到远端和从远端到本地的一对LSP隧道。

·动态方式：如果执行**mpls bfd**命令时没有通过**discriminator**参数指定本地和远端的标识符，则自动运行MPLS Ping来协商标识符，并根据协商好的标识符建立BFD会话。采用这种方式时，要求本地和远端设备上都使能MPLS与BFD联动功能，但不需要在远端设备上执行**mpls bfd**命令。该方式用来检测两台设备间从本地到远端的一条单向LSP隧道。

执行本命令时，如果没有指定**template ***template-name*参数，则BFD会话使用系统视图下配置的多跳BFD会话参数。

BFD会话的源地址为本端设备的MPLS LSR ID。因此，配置BFD检测LSP功能前，需要先在本端设备上配置MPLS LSR ID，并确保远端设备上存在到达MPLS LSR ID的路由。

【举例】

\# 配置使用BFD检测到达目的地址22.22.2.2/32的LSP的连通性。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname mpls bfd 22.22.2.2 32

\# 配置使用BFD检测到达目的地址22.22.2.2/32的LSP的连通性，并指定待检测LSP的下一跳地址为12.0.0.2。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname mpls bfd 22.22.2.2 32 nexthop 12.0.0.2

\# 配置使用BFD检测到达目的地址22.22.2.2/32的LSP的连通性，并指定待检测LSP的下一跳地址为12.0.0.2，本地标识符和远端标识符分别为1，引用的BFD会话参数模板为test。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname mpls bfd 22.22.2.2 32 nexthop 12.0.0.2 discriminator local 1 remote 1 template test

【相关命令】

·**display mpls bfd**

·**mpls bfd enable**

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd (for TE tunnel)**

------------------------------------------------------------------------

**[mpls bfd**]命令用来配置使用BFD检测当前隧道接口对应MPLS TE隧道的连通性。

**[undo mpls bfd**]命令用来取消使用BFD检测当前隧道接口对应MPLS TE隧道的连通性。

【命令】

**[mpls bfd ** **discriminator local** *local-id* **remote** *remote-id* ]  **template** *template-name*

**[undo mpls bfd**]

【缺省情况】

未使用BFD检测隧道接口对应MPLS TE隧道的连通性。

【视图】

Tunnel接口视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[discriminator**]：指定BFD会话的标识符。

**[local*** local-id*]：指定BFD会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。

**[remote*** remote-id*]：指定BFD会话的远端标识符，取值范围为1～4294967295。

**[template ***template-name*]：指定引用的BFD会话参数的模板名称。*template-name*为BFD会话参数模板的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

通过**mpls bfd enable**命令使能MPLS与BFD联动功能，并执行本命令后，设备上将会创建用来检测指定MPLS TE隧道的BFD会话。当MPLS TE隧道出现故障时，BFD可以快速检测到该故障，以便设备及时进行相应地处理，如将流量切换到备份隧道。

可以通过两种方式配置检测MPLS TE隧道的BFD会话：

·静态方式：如果执行**mpls bfd**命令时通过**discriminator**参数指定了本地和远端的标识符，则根据指定的标识符建立BFD会话。采用这种方式时，要求本地和远端设备上都使能MPLS与BFD联动功能，通过**mpls bfd**命令配置使用BFD检测指定MPLS TE隧道的连通性，并要求两端配置的本地和远端标识符匹配。该方式用来检测两台设备间从本地到远端和从远端到本地的一对MPLS TE隧道。

·动态方式：如果执行**mpls bfd**命令时没有通过**discriminator**参数指定本地和远端的标识符，则自动运行MPLS Ping来协商标识符，并根据协商好的标识符建立BFD会话。采用这种方式时，要求本地和远端设备上都使能MPLS与BFD联动功能，但不需要在远端设备上执行**mpls bfd**命令。该方式用来检测两台设备间从本地到远端的一条单向MPLS TE隧道。

执行本命令时，如果没有指定**template ***template-name*参数，则BFD会话使用Tunnel接口视图下配置的BFD会话参数。

BFD会话的源地址为本端设备的MPLS LSR ID。因此，配置BFD检测MPLS TE隧道功能前，需要先在本端设备上配置MPLS LSR ID，并确保远端设备上存在到达MPLS LSR ID的路由。

【举例】

\# 配置通过BFD检测隧道接口Tunnel1对应MPLS TE隧道的连通性，并指定引用的BFD会话参数的模板为test。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname interface Tunnel 1

Sysname-Tunnel1 mpls bfd template test

\# 配置通过BFD检测隧道接口Tunnel1对应MPLS TE隧道的连通性，并本地标识符和远端标识符均为1。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname interface Tunnel 1

Sysname-Tunnel1 mpls bfd discriminator local 1 remote 1

【相关命令】

·**display mpls bfd**

·**mpls bfd enable**

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls periodic-tracert (for LSP)**

------------------------------------------------------------------------

**[mpls periodic-tracert**]命令用来使能指定FEC对应LSP的周期性Trace route功能。

**[undo** **mpls** **periodic-tracert**]命令用来关闭指定FEC对应LSP的周期性Trace route功能。

【命令】

**[mpls periodic-tracert ***dest-addr mask-length*****[[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-u** *retry-attempt* \| **fec-check** ] \*]]

**[undo mpls periodic-tracert ***dest-addr* *mask-length*]

【缺省情况】

LSP的周期性Trace route功能处于关闭状态。

【视图】

系统视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

*[dest-addr*]：FEC目的地址。

*[mask-length*]：FEC目的地址的掩码长度，取值范围为0～32。

**[-a ***source-ip*]：指定MPLS Echo Request报文的源地址，缺省使用MPLS LSR ID作为MPLS Echo Request报文的源地址。

**[-exp** *exp-value*]：指定MPLS Echo Request报文中标签的Exp值。*exp-value*取值范围为0～7，缺省值为0。

**[-h** *ttl-value*]：指定MPLS Echo Request报文中TTL的最大值（即检测的最大跳数）。*ttl-value*取值范围为1～255，缺省值为30。

**[-m*** wait-time*]：指定Trace route功能的检测周期。*wait-time*取值范围为15～120，单位为分钟，缺省值为60分钟。

**[-rtos ***tos-value*]：指定MPLS Echo Reply报文IP头的ToS值**，***tos-value*取值范围为0～7，缺省值为6。

**[-t** *time-out*]：指定发送MPLS Echo Request报文后等待响应的超时时间。*time-out*取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-u** *retry-attempt*]：指定MPLS Echo Request报文超时重试的次数。*retry-attempt*取值范围为1～9，单位为次数，缺省值为3次。

**[fec-check**]：指定在Transit节点上进行FEC栈检查。

【使用指导】

LSP的周期性Trace route功能，即周期性地对LSP进行Trace route主动检测，该功能用来对LSP的错误点进行定位，对转发平面和控制平面一致性进行校验，并将发现的错误记录到系统日志（System Log Messages）中。管理员可以通过查看日志信息，了解LSP是否出现故障。

如果同时配置了BFD自动检测LSP功能和周期性LSP Trace route功能，则周期性LSP Trace route检测到转发平面故障或转发平面与控制平面不一致时，会拆除BFD会话，并基于控制平面重新建立BFD会话。

执行本命令前，需先执行**mpls bfd enable**命令。

【举例】

\# 使用周期性LSP Trace route功能，检测到达目的地11.11.1.1/32的LSP的有效性，并检查转发平面与控制平面是否一致。

\<Sysname\> system-view

Sysname mpls bfd enable

Sysname mpls periodic-tracert 11.11.1.1 32

【相关命令】

·**mpls bfd enable**

·**mpls bfd** (for LSP)

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls ipv4**

------------------------------------------------------------------------

**[ping mpls ipv4**]命令用来检测IPv4地址前缀类型MPLS LSP的连通性。

【命令】

**[ping mpls **[[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** ] \* **ipv4** *dest-addr* *mask-length*  **destination** *start-address* [ *end-address* [ *address-increment*  ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a*** source-ip*]：指定发送的MPLS echo request报文的源地址。*source-ip*为源IP地址。如果没有指定本参数，则MPLS echo request报文的源地址为报文出接口的主IP地址。

**[-c ***count*]：指定重复发送IP头中目的地址相同的MPLS echo request报文的次数。*count*为IP头中目的地址相同的MPLS echo request报文的重复发送次数，取值范围为1～4294967295，缺省值为5。

**[-exp*** exp-value*]：指定MPLS echo request报文中标签的EXP值。*exp-value*为EXP值，取值范围为0～7，缺省值为0。

**[-h*** ttl-value*]：指定MPLS echo request报文中的TTL值。*ttl-value*为TTL值，取值范围为1～255，缺省值为255。

**[-m** *wait-time*]：指定连续发送MPLS echo request报文的时间间隔。*wait-time*为发送报文的时间间隔，取值范围为1～10000，单位为毫秒，缺省值为200毫秒。

**[-r** *reply-mode*]：指定接收者对MPLS echo request报文的应答模式。*reply-mode*为应答模式，取值范围为1～3，1表示不回应，2表示使用UDP报文回应，3表示使用UDP报文回应并携带Router Alert选项。缺省值为2。

**[-rtos*** tos-value*]：指定MPLS echo reply报文IP头的ToS值。*tos-value*为ToS值，取值范围为0～7，缺省值为6。

**[-s ***packet-size*]：指定MPLS echo request报文长度。*packet-size*为MPLS echo request报文长度（不包括IP头和UDP头），取值范围为65～8100，单位为字节，缺省值为100字节。

**[-t*** time-out*]：指定发送MPLS echo request报文后等待响应的超时时间。*time-out*为超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-v**]：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。

*[dest-addr* *mask-length*]：检测指定LSP的连通性。*dest-addr*为FEC的目的地址，*mask-length*为FEC目的地址的掩码长度，取值范围为0～32。

**[destination**]：指定MPLS echo request报文中IP头的目的地址，缺省值为127.0.0.1。

*[start-address*]：IP头的目的地址或起始目的地址，该地址必须是127.0.0.0/8网段的地址（本机环回地址）。如果指定了本参数，没有指定*end-address*参数，则IP头的目的地址为*start-address*，MPLS echo request报文的发送次数由**-c ***count*参数决定；如果同时指定了本参数和*end-address*参数，则IP头的目的地址从*start-address*开始，依次增加*address-increment*，直到到达*end-address*，每个目的地址对应MPLS echo request报文的发送次数由**-c ***count*参数决定。

*[end-address*]：IP头的结束目的地址，该地址必须是127.0.0.0/8网段的地址（本机环回地址）。

*[address-increment*]：表示IP头中目的地址的步进值，取值范围为1～16777215，缺省值为1。

【举例】

\# 检测到达3.3.3.9/32的LSP的连通性。

\<Sysname\> ping mpls ipv4 3.3.3.9 32

MPLS ping FEC 3.3.3.9/32 with 100 bytes of data:

100 bytes from 100.1.2.1: Sequence=1 time=49 ms

100 bytes from 100.1.2.1: Sequence=2 time=44 ms

100 bytes from 100.1.2.1: Sequence=3 time=60 ms

100 bytes from 100.1.2.1: Sequence=4 time=60 ms

100 bytes from 100.1.2.1: Sequence=5 time=76 ms

\-\-- Ping statistics for FEC 3.3.3.9/32 \-\--

5 packets transmitted, 5 packets received, 0.0% packet loss

Round-trip min/avg/max = 44/57/76 ms

\# 检测到达3.3.3.9/32的LSP的连通性，并指定如下参数：

·重复发送IP头中目的地址相同的MPLS echo request报文的次数为3次。

·显示详细的应答信息。

·指定IP头的目的地址范围为127.0.0.1～127.0.0.3，并指定目的地址的步进值为2，即IP头的目的地址为127.0.0.1和127.0.0.3。

\<Sysname\> ping mpls --c 3 --v ipv4 3.3.3.9 32 destination 127.0.0.1 127.0.0.3 2

MPLS ping FEC 3.3.3.9/32 with 100 bytes of data:

Destination address 127.0.0.1

100 bytes from 100.1.2.1: Sequence=1 time=49 ms Return Code=3(1)

Destination address 127.0.0.3

100 bytes from 100.1.2.1: Sequence=2 time=44 ms Return Code=3(1)

Destination address 127.0.0.1

100 bytes from 100.1.2.1: Sequence=3 time=60 ms Return Code=3(1)

Destination address 127.0.0.3

100 bytes from 100.1.2.1: Sequence=4 time=60 ms Return Code=3(1)

Destination address 127.0.0.1

100 bytes from 100.1.2.1: Sequence=5 time=76 ms Return Code=3(1)

Destination address 127.0.0.3

100 bytes from 100.1.2.1: Sequence=6 time=57 ms Return Code=3(1)

\-\-- Ping statistics for FEC 3.3.3.9/32 \-\--

6 packets transmitted, 6 packets received, 0.0% packet loss

Round-trip min/avg/max = 44/57/76 ms

表1-3 ping mpls ipv4命令显示信息描述表

字段

描述

MPLS Ping FEC: 3.3.3.9/32 : 100 data bytes

检测FEC目的地址为3.3.3.9/32的LSP的连通性，发送的MPLS echo request报文的长度为100字节

Destination address

IP头中的目的IP地址

100 bytes from 100.1.2.1

从100.1.2.1接收到长度为100字节的应答报文

Sequence

应答报文的序列号，用来判断报文是否有分组丢失、失序或重复

time

报文的往返时延

ReturnCode

返回码，括号内为返回子码

Ping statistics for FEC 3.3.3.9/32

LSP检测的统计数据

packets transmitted

发送的MPLS echo request报文数

packets received

接收的MPLS echo reply报文数

packet loss

未响应请求报文占发送的总请求报文的百分比

Round-trip min/avg/max

往返时延的最小值、平均值和最大值

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls pw**

------------------------------------------------------------------------

**[ping mpls pw**]命令用来检测LDP PW或静态PW的连通性。

【命令】

**[ping mpls **[[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** ] \* **pw** *ip-address* **pw-id** *pw-id*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a*** source-ip*]：指定发送的MPLS echo request报文的源地址。*source-ip*为源IP地址。如果没有指定本参数，则MPLS echo request报文的源地址为报文出接口的主IP地址。

**[-c ***count*]：指定发送MPLS echo request报文的次数。*count*为MPLS echo request报文发送次数，取值范围为1～4294967295，缺省值为5。

**[-exp*** exp-value*]：指定MPLS echo request报文中标签的EXP值。*exp-value*为EXP值，取值范围为0～7，缺省值为0。

**[-h*** ttl-value*]：指定MPLS echo request报文中的TTL值。*ttl-value*为TTL值，取值范围为1～255，缺省值为255。

**[-m** *wait-time*]：指定连续发送MPLS echo request报文的时间间隔。*wait-time*为发送报文的时间间隔，取值范围为1～10000，单位为毫秒，缺省值为200毫秒。

**[-r** *reply-mode*]：指定接收者对MPLS echo request报文的应答模式。*reply-mode*为应答模式，取值范围为1～3，1表示不回应，2表示使用UDP报文回应，3表示使用UDP报文回应并携带Router Alert选项。缺省值为2。

**[-rtos*** tos-value*]：指定MPLS echo reply报文IP头的ToS值。*tos-value*为ToS值，取值范围为0～7，缺省值为6。

**[-s ***packet-size*]：指定MPLS echo request报文长度。*packet-size*为MPLS echo request报文长度（不包括IP头和UDP头），取值范围为65～8100，单位为字节，缺省值为100字节。

**[-t*** time-out*]：指定发送MPLS echo request报文后等待响应的超时时间。*time-out*为超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-v**]：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。

*[ip-address*]：指定对端PE的IP地址。

**[pw-id*** pw-id*]：指定到对端PE的PW ID，取值范围为1～4294967295。

【举例】

\# 检测到达对端PE（IP地址为3.3.3.9）、PW ID为301的PW的连通性。

\<Sysname\> ping mpls pw 3.3.3.9 pw-id 301

MPLS ping PW 3.3.3.9 301 with 100 bytes of data:

100 bytes from 100.1.2.1: Sequence=1 time=49 ms

100 bytes from 100.1.2.1: Sequence=2 time=44 ms

100 bytes from 100.1.2.1: Sequence=3 time=60 ms

100 bytes from 100.1.2.1: Sequence=4 time=60 ms

100 bytes from 100.1.2.1: Sequence=5 time=76 ms

\-\-- Ping statistics for PW 3.3.3.9 301 \-\--

5 packets transmitted, 5 packets received, 0.0% packet loss

Round-trip min/avg/max = 44/57/76 ms

显示信息中各字段的解释，请参见 表1-3(?1909720745#_Ref329182139)。

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls te**

------------------------------------------------------------------------

**[ping mpls te**]命令用来检测MPLS TE隧道的连通性。

【命令】

**[ping mpls **[[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** ] \* **te** **tunnel** *interface-number*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a*** source-ip*]：指定发送的MPLS echo request报文的源地址。*source-ip*为源IP地址。如果没有指定本参数，则MPLS echo request报文的源地址为报文出接口的主IP地址。

**[-c ***count*]：指定发送MPLS echo request报文的次数。*count*为MPLS echo request报文发送次数，取值范围为1～4294967295，缺省值为5。

**[-exp*** exp-value*]：指定MPLS echo request报文中标签的EXP值。*exp-value*为EXP值，取值范围为0～7，缺省值为0。

**[-h*** ttl-value*]：指定MPLS echo request报文中的TTL值。*ttl-value*为TTL值，取值范围为1～255，缺省值为255。

**[-m** *wait-time*]：指定连续发送MPLS echo request报文的时间间隔。*wait-time*为发送报文的时间间隔，取值范围为1～10000，单位为毫秒，缺省值为200毫秒。

**[-r** *reply-mode*]：指定接收者对MPLS echo request报文的应答模式。*reply-mode*为应答模式，取值范围为1～3，1表示不回应，2表示使用UDP报文回应，3表示使用UDP报文回应并携带Router Alert选项。缺省值为2。

**[-rtos*** tos-value*]：指定MPLS echo reply报文IP头的ToS值。*tos-value*为ToS值，取值范围为0～7，缺省值为6。

**[-s ***packet-size*]：指定MPLS echo request报文长度。*packet-size*为MPLS echo request报文长度（不包括IP头和UDP头），取值范围为65～8100，单位为字节，缺省值为100字节。

**[-t*** time-out*]：指定发送MPLS echo request报文后等待响应的超时时间。*time-out*为超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-v**]：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。

**[tunnel*** interface-number*]：检测指定隧道接口对应的MPLS TE隧道。*interface-number*为隧道接口编号，取值范围为设备上已经创建的MPLS TE隧道接口的编号。

【举例】

\# 检测隧道接口Tunnel1对应的MPLS TE隧道的连通性。

\<Sysname\> ping mpls te tunnel 1

MPLS ping TE tunnel Tunnel1 with 100 bytes of data:

100 bytes from 100.1.2.1: Sequence=1 time=49 ms

100 bytes from 100.1.2.1: Sequence=2 time=44 ms

100 bytes from 100.1.2.1: Sequence=3 time=60 ms

100 bytes from 100.1.2.1: Sequence=4 time=60 ms

100 bytes from 100.1.2.1: Sequence=5 time=76 ms

\-\-- Ping statistics for TE tunnel Tunnel1 \-\--

5 packets transmitted, 5 packets received, 0.0% packet loss

Round-trip min/avg/max = 44/57/76 ms

显示信息中各字段的解释，请参见 表1-3(?1909720745#_Ref329182139)。

**MPLS OAM \-- MPLS OAM配置命令 \-- tracert mpls ipv4**

------------------------------------------------------------------------

**[tracert mpls ipv4**]命令用来查看IPv4地址前缀类型MPLS LSP从Ingress节点到Egress节点所经过的路径，并根据应答信息对错误点进行定位。

【命令】

**[tracert mpls **[[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-v** \| **fec-check** ] \* **ipv4** *dest-addr mask-length*  **destination** *start-address* [ *end-address* [ *address-increment*  ] ]]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a*** source-ip*]：指定发送的MPLS echo request报文的源地址。*source-ip*为源IP地址。如果没有指定本参数，则MPLS echo request报文的源地址为报文出接口的主IP地址。

**[-exp*** exp-value*]：指定MPLS echo request报文中标签的EXP值。*exp-value*为EXP值，取值范围为0～7，缺省值为0。

**[-h*** ttl-value*]：指定MPLS echo request报文中TTL的最大值（即检测的最大跳数）。*ttl-value*为TTL最大值，取值范围为1～255，缺省值为30。

**[-r***reply-mode*]：指定接收者对MPLS echo request报文的应答模式。*reply-mode*为应答模式，取值为2和3，2表示使用UDP报文回应，3表示使用UDP报文回应并携带Router Alert选项。缺省值为2。

**[-rtos** *tos-value*]：指定MPLS echo reply报文IP头的ToS值。*tos-value*为ToS值，取值范围为0～7，缺省值为6。

**[-t*** time-out*]：指定发送MPLS echo request报文后等待响应的超时时间。*time-out*为超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-v**]**：**指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。

**[fec-check**]：指定在Transit节点上进行FEC栈检查。

*[dest-addr* *mask-length*]：查看指定LSP经过的路径。*dest-addr*为FEC的目的地址，*mask-length*为FEC目的地址的掩码长度，取值范围为0～32。

**[destination**]：指定MPLS echo request报文中IP头的目的地址，缺省值为127.0.0.1。

*[start-address*]：IP头的目的地址或起始目的地址，该地址必须是127.0.0.0/8网段的地址（本机环回地址）。如果指定了本参数，没有指定*end-address*参数，则IP头的目的地址为*start-address*。如果同时指定了本参数和*end-address*参数，则IP头的目的地址从*start-address*开始，依次增加*address-increment*，直到到达*end-address*，对于每个目的地址都要执行一次Trace route过程。

*[end-address*]：IP头的结束目的地址，该地址必须是127.0.0.0/8网段的地址（本机环回地址）。

*[address-increment*]：表示IP头中目的地址的步进值，取值范围为1～16777215，缺省值为1。

【举例】

\# 查看到达目的地址5.5.5.9/32的LSP从Ingress节点到Egress节点所经过的路径，指定IP头目的地址的范围为127.1.1.1～127.1.1.2，步进值为1，即对127.1.1.1和127.1.1.2两个地址分别进行一次Trace route操作。

\<Sysname\> tracert mpls ipv4 5.5.5.9 32 destination 127.1.1.1 127.1.1.2 1

MPLS trace route FEC 5.5.5.9/32

  Destination address 127.1.1.1

  TTL   Replier            Time    Type      Downstream

  0                                Ingress   100.1.2.1/[1025]

  1     100.1.2.1          1 ms    Transit   100.2.4.1/[1024]

  2     100.2.4.1          63 ms   Transit   100.4.5.1/[3]

  3     100.4.5.1          129 ms  Egress

  Destination address 127.1.1.2

  TTL   Replier            Time    Type      Downstream

  0                                Ingress   100.1.3.1/[1030]

  1     100.1.3.1          1 ms    Transit   100.3.4.1/[1024]

  2     100.3.4.1          51 ms   Transit   100.4.5.1/[3]

  3     100.4.5.1          80 ms   Egress

\# 查看到达目的地址5.5.5.9/32的LSP从Ingress节点到Egress节点所经过的路径，显示详细的应答信息，并指定IP头目的地址的范围为127.1.1.1～127.1.1.2，步进值为1，即对127.1.1.1和127.1.1.2两个地址分别进行一次Trace route操作。

\<Sysname\> tracert mpls --v ipv4 5.5.5.9 32 destination 127.1.1.1 127.1.1.2 1

MPLS trace route FEC 5.5.5.9/32

  Destination address 127.1.1.1

  TTL   Replier            Time    Type      Downstream

  0                                Ingress   100.1.2.1/[1025]

  1     100.1.2.1          1 ms    Transit   100.2.4.1/[1024 ReturnCode 8(1)]

  2     100.2.4.1          63 ms   Transit   100.4.5.1/[3 ReturnCode 8(1)]

  3     100.4.5.1          129 ms  Egress    ReturnCode 3(1)

  Destination address 127.1.1.2

  TTL   Replier            Time    Type      Downstream

  0                                Ingress   100.1.3.1/[1030]

  1     100.1.3.1          1 ms    Transit   100.3.4.1/[1024 ReturnCode 8(1)]

  2     100.3.4.1          51 ms   Transit   100.4.5.1/[3 ReturnCode 8(1)]

  3     100.4.5.1          80 ms   Egress    ReturnCode 3(1)

表1-4 tracert mpls ipv4命令显示信息描述表

字段

描述

MPLS trace route FEC

对指定FEC对应的LSP进行Trace route操作

Destination address

IP头中的目的IP地址

TTL

跳数

Replier

应答的LSR地址

Time

接收到应答的时间，单位为毫秒

Type

LSR的类型，取值包括：

·Ingress：入节点

·Transit：中间节点

·Egress：出节点

Downstream

下游LSR地址及出标签值

ReturnCode

返回码，括号内为返回子码

**MPLS OAM \-- MPLS OAM配置命令 \-- tracert mpls te**

------------------------------------------------------------------------

**[tracert mpls te**]命令用来查看MPLS TE隧道从Ingress节点到Egress节点所经过的路径，并根据应答信息对错误点进行定位。

【命令】

**[tracert mpls **[[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-v** \| **fec-check** ] \* **te** **tunnel** *interface-number*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a*** source-ip*]：指定发送的MPLS echo request报文的源地址。*source-ip*为源IP地址。如果没有指定本参数，则MPLS echo request报文的源地址为报文出接口的主IP地址。

**[-exp*** exp-value*]：指定MPLS echo request报文中标签的EXP值。*exp-value*为EXP值，取值范围为0～7，缺省值为0。

**[-h*** ttl-value*]：指定MPLS echo request报文中TTL的最大值（即检测的最大跳数）。*ttl-value*为TTL最大值，取值范围为1～255，缺省值为30。

**[-r***reply-mode*]：指定接收者对MPLS echo request报文的应答模式。*reply-mode*为应答模式，取值2和3，2表示使用UDP报文回应，3表示使用UDP报文回应并携带Router Alert选项。缺省值为2。

**[-rtos*** tos-value*]：指定MPLS echo reply报文IP头的ToS值。*tos-value*为ToS值，取值范围为0～7，缺省值为6。

**[-t*** time-out*]：指定发送MPLS echo request报文后等待响应的超时时间。*time-out*为超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-v**]：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。

**[fec-check**]：指定在Transit节点上进行FEC栈检查。

**[tunnel*** interface-number*]：查看指定Tunnel接口对应MPLS TE隧道经过的路径。*interface-number*为已创建的模式为MPLS TE隧道的Tunnel接口的编号。

【举例】

\# 查看隧道接口Tunnel1对应的MPLS TE隧道从Ingress节点到Egress节点所经过的路径。

\<Sysname\> tracert mpls te tunnel 1

MPLS trace route TE tunnel Tunnel1

  TTL   Replier            Time    Type      Downstream

  0                                Ingress   10.4.5.1/[1025]

  1     10.4.5.1           1 ms    Transit   100.3.4.1/[1024]

  2     100.3.4.1          63 ms   Transit   100.1.2.1/[3]

  3     100.1.2.1          129 ms  Egress

显示信息中各字段的解释，请参见 表1-4(?1106107802#_Ref329182432)。

**MPLS OAM \-- MPLS OAM配置命令 \-- vccv bfd**

------------------------------------------------------------------------

![说明](MPLS%20OAM命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vccv bfd**]命令用来配置使用BFD检测PW的连通性。

**[undo vccv bfd**]用来取消使用BFD检测PW的连通性。

【命令】

**[vccv bfd ** **raw-bfd** ]  **template** *template-name*

**[undo vccv bfd**]

【缺省情况】

未使用BFD检测PW的连通性。

【视图】

PW模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[raw-bfd**]：指定检测PW的BFD报文的封装方式为PW-ACH Encapsulation (without IP/UDP Headers)，即封装在VCCV控制通道内的BFD控制报文不携带IP和UDP头。只有控制通道类型为**control-word**时，指定本参数才会生效。如果没有指定本参数，则BFD报文的封装方式为IP/UDP Encapsulation (with IP/UDP Headers)。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[template ***template-name*]：指定引用的BFD会话参数模板。*template-name*为BFD会话参数模板的名称，为1～31个字符的字符串，区分大小写。

【使用指导】

将PW与指定PW模板关联，并在该PW模板视图下执行本命令后，是否使用BFD检测该PW的连通性以及BFD报文采用何种封装方式，由两端的配置共同决定：

·如果两端PE上都配置了BFD检测PW且BFD报文封装方式相同，则采用该封装方式检测PW。

·否则，不使用BFD检测PW的连通性。

需要注意的是：

·要想建立检测PW的BFD会话，两端设备上都需要执行**vccv bfd**命令，并执行**mpls bfd enable**命令使能MPLS与BFD联动功能。

·执行本命令时，如果没有指定**template ***template-name*参数，则BFD会话使用系统视图下配置的多跳BFD会话参数。

【举例】

\# 配置使用BFD检测PW的连通性，指定BFD报文封装方式为raw-bfd，并指定引用的BFD会话参数模板为aaa。

\<Sysname\> system-view

Sysname pw-class test

Sysname-pw-test vccv bfd raw-bfd template aaa

【相关命令】

·**display l2vpn pw bfd**

·**mpls bfd enable**

·**vccv cc**

**MPLS OAM \-- MPLS OAM配置命令 \-- vccv cc**

------------------------------------------------------------------------

![说明](MPLS%20OAM命令.files/image001.png)

本命令的支持情况与设备的型号有关，请以设备的实际情况为准。

**[vccv cc**]命令用来配置VCCV控制通道类型。

**[undo vccv cc**]用来恢复缺省情况。

【命令】

**[vccv cc **[{ **control-word** \| **router-alert** \| **ttl** }]]

**[undo vccv cc**]

【缺省情况】

没有指定VCCV控制通道类型。

【视图】

PW模板视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[control-word**]：指定VCCV控制通道类型为控制字类型。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[router-alert**]：指定VCCV控制通道类型为MPLS路由器告警标签类型。

**[ttl**]**：**指定VCCV控制通道类型为TTL超时类型，即PW标签的TTL值等于1。

【使用指导】

用来检测PW连通性的报文统称为VCCV报文。PE通过CC（Control Channel，控制通道）来传送VCCV报文。

CC有以下几种类型：

·**control-word**类型：通过控制字，即PW-ACH（PW Associated Channel Header，PW随路通道首部），标识VCCV报文。只有PW支持控制字时，才能选择这种类型。控制字的详细介绍，请参见"MPLS配置指导"中的"MPLS L2VPN"。

·**router-alert**类型：通过在PW标签之前携带MPLS路由器告警标签来标识VCCV报文。

·**ttl**类型：通过将PW标签的TTL值设置为1来标识VCCV报文。

将PW与指定PW模板关联，并在该PW模板视图下执行本命令后，该PW是否使用指定的VCCV控制通道，由两端的配置共同决定：

·如果两端PE上配置了相同的VCCV控制通道类型，则使用该VCCV控制通道。

·否则，不使用任何VCCV控制通道。

【举例】

\# 配置VCCV控制通道类型为TTL超时类型。

\<Sysname\> system-view

Sysname pw-class test

Sysname-pw-test vccv cc ttl

【相关命令】

·**display l2vpn pw bfd**

·**mpls bfd enable**

·**vccv bfd**

