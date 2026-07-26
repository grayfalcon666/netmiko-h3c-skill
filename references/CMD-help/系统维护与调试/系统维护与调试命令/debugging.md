
**系统维护与调试 \-- 系统维护与调试命令 \-- debugging**

------------------------------------------------------------------------

**[debugging**]命令用打开指定模块的调试开关。

**[undo debugging**]命令用来关闭指定模块的调试开关。

【命令】

**[debugging** { **all** [ **timeout** *time*  \| *module-name*  *option*  }]]

**[undo**[ **debugging** { **all** \| *module-name* [ *option* ] }]]

【缺省情况】

所有模块的调试开关均处于关闭状态。

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：所有模块的调试开关。

**[timeout*** time*]：指定**debugging all**命令的生效时间。当使用**all**参数开启了所有的调试开关，则经过*time*时间，系统会自动执行**undo debugging all**命令来关闭所有的调试开关。取值范围为1～1440，单位为分钟。

*[module-name*]：模块名称，比如arp、device等。可以使用**debugging ？**命令查询设备当前支持的模块名。

*[option*]：模块的调试选项。对于不同的模块，调试选项的数量和内容都不相同。可以使用**debugging ***module-name ***？**命令查询设备当前支持的指定模块的调试选项。

【使用指导】

调试信息的输出会影响系统的运行效率，所以建议在进行网络故障诊断时根据需要打开某个功能模块的调试开关，不要同时打开多个功能模块的调试开关。

关于功能模块**debugging**命令以及debug信息的详细描述，请参见对应功能模块的Debug手册。

【举例】

\# 打开设备管理模块的调试开关。

\<Sysname\> debugging dev

【相关命令】

·**display debugging**

**系统维护与调试 \-- 系统维护与调试命令 \-- display debugging**

------------------------------------------------------------------------

**[display debugging**]命令用来显示系统中已经打开的调试开关。

【命令】

**[display** **debugging** [ *module-name* ]]

【视图】

任意视图

【缺省用户角色】

network-admin

network-operator

mdc-admin

mdc-operator

【参数】

*[module-name*]：显示指定模块调试开关的设置情况。*module-name*表示模块名，具体取值可通过执行**display** **debugging ?**命令来获取。

【举例】

\# 显示所有打开的调试开关。

\<Sysname\> display debugging

DEV debugging switch is on

【相关命令】

·**debugging**

**系统维护与调试 \-- 系统维护与调试命令 \-- ping**

------------------------------------------------------------------------

**[ping**]命令用来检查指定IP地址是否可达，并输出相应的统计信息。

【命令】

**[ping** [ **ip**  [ **-a** *source-ip* \| **-c** *count* \| **-f** \| **-h** *ttl* \| **-i** *interface-type interface-number* \| **-m** *interval* \| **-n** \| **-p** *pad* \| **-q** \| **-r** \| **-s** *packet-size* \| **-t** *timeout* \| **-tos** *tos* \| **-v** \| { **-topology** *topo-name* \| **-vpn-instance** *vpn-instance-name* } ] \* *host*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[ip**]：支持IPv4协议。不指定该参数时，也表示支持IPv4协议。如果ping的目的主机名为i、ip、ipv、ipv6、l、ls、lsp时，需要先指定该关键字再指定主机名，如：ping ip ip。

**[-a** *source-ip*]：指定ICMP回显请求（ECHO-REQUEST）报文的源IP地址。该地址必须是设备上已配置的IP地址。不指定该参数时，ICMP回显请求报文的源IP地址是该报文出接口的主IP地址。

**[-c** *count*]：指定ICMP回显请求报文的发送次数，取值范围为1～4294967295，缺省值为5。

**[-f**]：将长度大于出接口MTU的报文直接丢弃，即不允许对发送的ICMP回显请求报文进行分片。

**[-h** *ttl*]：指定ICMP回显请求报文中的TTL值，取值范围为1～255，缺省值为255。

**[-i ***interface-type interface-number*]：指定发送ICMP回显请求报文的接口的类型和编号。不指定该参数时，将根据目的IP查找路由表或者转发表来确定发送ICMP回显请求报文的接口。

**[-m** *interval*]**：**指定发送ICMP回显请求报文的时间间隔，取值范围为1～65535，单位为毫秒，缺省值为200毫秒。

**[-n**]：对*host*参数不进行域名解析。不指定该参数时，如果*host*参数表示的是目的端的主机名，则设备会对*host*进行域名解析。

**[-p** *pad*]：指定ICMP回显请求报文的"PAD"字段的填充值，为1～8位的16进制数，取值范围为0～FFFFFFFF。如果指定的参数不够8位，则会在首部补0，使填充值达到8位。比如将*pad*设置为0x2f，则会重复使用0x0000002f去填充报文，以使发送报文的总长度达到设备要求值。填充值从0x01开始，逐渐递增，直到0xff，然后又从0x01开始循环，形如0x010203......feff01......，直至发送报文的总长度达到设备要求值。

**[-q**]：只显示统计信息。不指定该参数时，系统将显示包括统计信息在内的全部信息。

**[-r**]：记录路由信息。不指定该参数时，系统不记录路由。

**[-s ***packet-size*]：指定发送的ICMP回显请求报文的长度（不包括IP和ICMP报文头），取值范围为20～8100，单位为字节，缺省值为56字节。

**[-t ***timeout*]：指定ICMP回显应答（ECHO-REPLY）报文的超时时间，发送ICMP回显请求报文*timeout*时长后还没有收到ICMP回显应答报文，源端则认为ICMP回显应答报文超时。取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-tos** *tos*]：指定ICMP回显请求报文中的ToS域的值，取值范围为0～255，缺省值为0。

**[-v**]：显示接收到的非回显应答的ICMP报文。不指定该参数时，系统不显示非回显应答的ICMP报文。

**[-topology** *topo-name*]：[指定目的端所属的拓扑。]*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；取值为**base**时表示公网拓扑。如果未指定本参数，[则表示目的端位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**[-vpn-instance** *vpn-instance-name*]：指定目的端所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的端位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

*[host*]：目的端的IP地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

【使用指导】

如果要使用目的端的主机名执行ping操作，事先必须在设备上配置DNS（Domain Name System，域名系统）功能，否则会ping失败。

在执行命令过程中，键入\<Ctrl+C\>可终止ping操作。

【举例】

\# 检查IP地址为1.1.2.2的设备是否可达。

\<Sysname\> ping 1.1.2.2

Ping 1.1.2.2 (1.1.2.2): 56 data bytes, press CTRL_C to break

56 bytes from 1.1.2.2: icmp_seq=0 ttl=254 time=2.137 ms

56 bytes from 1.1.2.2: icmp_seq=1 ttl=254 time=2.051 ms

56 bytes from 1.1.2.2: icmp_seq=2 ttl=254 time=1.996 ms

56 bytes from 1.1.2.2: icmp_seq=3 ttl=254 time=1.963 ms

56 bytes from 1.1.2.2: icmp_seq=4 ttl=254 time=1.991 ms

\-\-- Ping statistics for 1.1.2.2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 1.963/2.028/2.137/0.062 ms

\# 检查私网vpn1中IP地址为1.1.2.2的设备是否可达。

\<Sysname\> ping -vpn-instance vpn1 1.1.2.2

Ping 1.1.2.2 (1.1.2.2): 56 data bytes, press CTRL_C to break

56 bytes from 1.1.2.2: icmp_seq=0 ttl=254 time=2.137 ms

56 bytes from 1.1.2.2: icmp_seq=1 ttl=254 time=2.051 ms

56 bytes from 1.1.2.2: icmp_seq=2 ttl=254 time=1.996 ms

56 bytes from 1.1.2.2: icmp_seq=3 ttl=254 time=1.963 ms

56 bytes from 1.1.2.2: icmp_seq=4 ttl=254 time=1.991 ms

\-\-- Ping statistics for 1.1.2.2 in VPN instance vpn1 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 1.963/2.028/2.137/0.062 ms

\# 检查IP地址为1.1.2.2的设备是否可达，只显示检查结果。

\<Sysname\> ping -q 1.1.2.2

Ping 1.1.2.2 (1.1.2.2): 56 data bytes, press CTRL_C to break

\-\-- Ping statistics for 1.1.2.2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 1.962/2.196/2.665/0.244 ms

\# 检查IP地址为1.1.2.2的设备是否可达，并显示路由信息。

\<Sysname\> ping -r 1.1.2.2

Ping 1.1.2.2 (1.1.2.2): 56 data bytes, press CTRL_C to break

56 bytes from 1.1.2.2: icmp_seq=0 ttl=254 time=4.685 ms

RR:      1.1.2.1

         1.1.2.2

         1.1.1.2

         1.1.1.1

56 bytes from 1.1.2.2: icmp_seq=1 ttl=254 time=4.834 ms  (same route)

56 bytes from 1.1.2.2: icmp_seq=2 ttl=254 time=4.770 ms  (same route)

56 bytes from 1.1.2.2: icmp_seq=3 ttl=254 time=4.812 ms  (same route)

56 bytes from 1.1.2.2: icmp_seq=4 ttl=254 time=4.704 ms  (same route)

\-\-- Ping statistics for 1.1.2.2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 4.685/4.761/4.834/0.058 ms

以上显示信息表明本设备与1.1.2.2之间路由可达，具体路由为1.1.1.1 \<-\> {1.1.1.2; 1.1.2.1} \<-\> 1.1.2.2。

表1-1 ping命令显示信息描述表

字段

描述

Ping 1.1.2.2 (1.1.2.2): 56 data bytes, press CTRL_C to break

检查IP地址为1.1.2.2的设备是否可达。每个ICMP回显请求报文中的数据为56字节，按组合键Ctrl+C可以终止ping操作

56 bytes from 1.1.2.2: icmp_seq=0 ttl=254 time=4.685 ms

收到IP地址为1.1.2.2的设备回复的ICMP响应报文，若超时仍没有收到ICMP响应报文，则不输出信息

·bytes表示ICMP响应报文中的数据字节数

·icmp_seq表示报文序号，用来判断报文是否有分组丢失、失序或重复

·ttl表示ICMP响应报文中的TTL值

·time表示响应时间

RR:

ICMP回显请求报文经过的路由器，采用倒序显示，距离目的端越近的路由器越先显示

\-\-- Ping statistics for 1.1.2.2 \-\--

Ping操作中收发数据的统计结果

\-\-- Ping statistics for 1.1.2.2 in VPN instance vpn1 \-\--

在VPN实例中执行Ping操作，Ping过程中收发数据的统计结果

5 packet(s) transmitted

发送的ICMP回显请求报文数

5 packet(s) received

收到的ICMP响应报文数

0.0% packet loss

未响应请求报文占发送的总请求报文的百分比

round-trip min/avg/max/std-dev = 4.685/4.761/4.834/0.058 ms

响应时间的最小值、平均值、最大值和标准方差，单位为毫秒

**系统维护与调试 \-- 系统维护与调试命令 \-- ping ipv6**

------------------------------------------------------------------------

**[ping ipv6**]命令用来检查指定IPv6地址是否可达，并输出相应的统计信息。

【命令】

**[ping ipv6**[ [ **-a** *source-ipv6* \| **-c** *count \|* **-i** *interface-type interface-number* \| **-m** *interval \|* **-q** \| **-s** *packet-size* \| **-t** *timeout \|* **-tc** *traffic-class \| **-*****v \| -vpn-instance** *vpn-instance-name* ] \* *host*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a** *source-ipv6*]：指定ICMPv6回显请求报文中的源IPv6地址。该地址必须是设备上已配置的合法IPv6地址。不指定该参数时，ICMPv6回显请求报文的源IPv6地址是该报文出接口的地址（地址选择原则遵循RFC 3484）。

**[-c** *count*]：指定发送的ICMPv6回显请求报文的数目，取值范围为1～4294967295，缺省值为5。

**[-i ***interface-type interface-number*]：指定出接口的接口类型与接口编号。对端是组播地址或者是链路本地地址则必须指定此参数。不指定该参数时，将根据目的IP查找路由表或者转发表来确定发送ICMPv6回显请求报文的接口。

**[-m** *interval*]：指定发送ICMPv6回显请求报文的时间间隔，取值范围为1～65535，单位为毫秒，缺省值为1000毫秒。

**[-q**]：只显示统计信息。不指定该参数时，系统将显示包括统计信息在内的全部信息。

**[-s ***packet-size*]：指定发送的ICMPv6回显请求报文的长度（不包括IPv6和ICMPv6报文头），取值范围为20～8100，单位为字节，缺省值为56字节。

**[-t ***timeout*]：指定ICMPv6回显应答报文的超时时间，取值范围为0～65535，单位为毫秒，缺省值为2000毫秒。

**[-tc*** traffic-class*]：IPv6 ICMP报文中的Traffic Class域的值。取值范围为0～255，缺省值为0。

**[-v**]：显示ICMPv6回显应答报文的详细信息。不指定该参数时，显示ICMPv6回显应答报文的简要信息。详细信息比简要信息多dst和idx字段，dst表示回显应答报文的目的地址，idx表示回显应答报文的入接口索引。

**[-vpn-instance** *vpn-instance-name*]：指定目的端所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的端位于公网中。

*[host*]：目的端的IPv6地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

【使用指导】

如果要使用目的端的主机名执行**ping ipv6**操作，事先必须在设备上配置DNS功能，否则会ping ipv6失败。

在执行命令过程中，键入\<Ctrl+C\>可终止**ping ipv6**操作。

【举例】

\# 检查IPv6地址为2001::2的设备是否可达。

\<Sysname\> ping ipv6 2001::2

Ping6(56 data bytes) 2001::1 \--\> 2001::2, press CTRL_C to break

56 bytes from 2001::2, icmp_seq=0 hlim=64 time=62.000 ms

56 bytes from 2001::2, icmp_seq=1 hlim=64 time=23.000 ms

56 bytes from 2001::2, icmp_seq=2 hlim=64 time=20.000 ms

56 bytes from 2001::2, icmp_seq=3 hlim=64 time=4.000 ms

56 bytes from 2001::2, icmp_seq=4 hlim=64 time=16.000 ms

\-\-- Ping6 statistics for 2001::2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 4.000/25.000/62.000/20.000 ms

\# 检查IPv6地址为2001::2的设备是否可达，只显示统计信息。

\<Sysname\> ping ipv6 --q 2001::2

Ping6(56 data bytes) 2001::1 \--\> 2001::2, press CTRL_C to break

\-\-- Ping6 statistics for 2001::2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 4.000/25.000/62.000/20.000 ms

\# 检查IPv6地址为2001::2的设备是否可达，显示详细ping信息。

\<Sysname\> ping ipv6 --v 2001::2

Ping6(56 data bytes) 2001::1 \--\> 2001::2, press CTRL_C to break

56 bytes from 2001::2, icmp_seq=0 hlim=64 dst=2001::1 idx=3 time=62.000 ms

56 bytes from 2001::2, icmp_seq=1 hlim=64 dst=2001::1 idx=3 time=23.000 ms

56 bytes from 2001::2, icmp_seq=2 hlim=64 dst=2001::1 idx=3 time=20.000 ms

56 bytes from 2001::2, icmp_seq=3 hlim=64 dst=2001::1 idx=3 time=4.000 ms

56 bytes from 2001::2, icmp_seq=4 hlim=64 dst=2001::1 idx=3 time=16.000 ms

\-\-- Ping6 statistics for 2001::2 \-\--

5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss

round-trip min/avg/max/std-dev = 4.000/25.000/62.000/20.000 ms

以上信息表明，目的端可达，源端发出的ICMPv6回显请求报文均能得到回应，报文往返时间的最小值、平均值、最大值和标准方差分别为4ms、25ms、62ms和20ms。

表1-2 {.FigureDescriptionChar}ping ipv6命令显示信息描述表{.FigureDescriptionChar}

字段

描述

Ping6 (56 data bytes)

2001::1 \--\> 2001::2, press CTRL_C to break

从源地址2001::1给目的地址2001::2发送一个ICMPv6回显请求报文，每个ICMPv6回显请求报文中的数据为56字节，按组合键Ctrl+C可以终止IPv6 ping操作

56 bytes from 2001::2,

icmp_seq=1 hlim=64 dst=2001::1 idx=3 time=62.000 ms

收到IPv6地址为2001::2的设备回复的ICMPv6响应报文，其中：

·数据字节数为56

·报文序号为1

·hop limit值为64

·目的地址为2001::1（使用**-v**参数时才显示该字段）

·报文入接口的索引为3（使用**-v**参数时才显示该字段）

·响应时间是62ms

\-\-- Ping6 statistics for 2001::2 \-\--

IPv6 ping操作中收发数据的统计结果

5 packet(s) transmitted

发送的ICMPv6回显请求报文数

5 packet(s) received

收到的ICMPv6响应报文数

0.0% packet loss

未响应请求报文占发送的总请求报文的百分比

round-trip min/avg/max/ std-dev =4.000/25.000/62.000/20.000 ms

响应时间的最小值、平均值、最大值和标准方差，单位为毫秒

**系统维护与调试 \-- 系统维护与调试命令 \-- tracert**

------------------------------------------------------------------------

【命令】

**[tracert**[ [ **-a** *source-ip* \| **-f** *first-ttl* \| **-m** *max-ttl* \| **-p** *port* \| **-q** *packet-number* \| **-t** *tos* \| { **-topology** *topo-name* \| **-vpn-instance** *vpn-instance-name* } \| **-w** *timeout* ] \* *host*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-a** *source-ip*]：指定tracert报文的源IP地址。该地址必须是设备上已配置的合法IP地址。不指定该参数时，tracert报文的源IP地址是该报文出接口的主IP地址。

**[-f*** first*-*ttl*]：指定一个初始TTL，即第一个报文所允许的最大跳数。取值范围为1～255，且小于或等于最大TTL，缺省值为1。

**[-m ***max*-*ttl*]：指定一个最大TTL，即一个报文所允许的最大跳数。取值范围为1～255，且大于或等于初始TTL，缺省值为30。

**[-p*** port*]：指定目的端的UDP端口号，取值范围为1～65535，缺省值为33434。用户一般不需要更改此选项。

**[-q** *packet-number*]：指定每次发送的探测报文个数，取值范围为1～65535，缺省值为3。

**[-t** *tos*]：Tracert报文中ToS域的值。取值范围为0～255，缺省值为0。

**[-topology** *topo-name*]：[指定目的端所属的拓扑。]*topo-name*表示拓扑名，为1～31个字符的字符串，区分大小写；取值为**base**时表示公网拓扑。如果未指定本参数，[则表示目的端位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]

**[-vpn-instance** *vpn-instance-name*]：指定目的端所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的端位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。

**[-w*** timeout*]：指定探测报文的响应报文的超时时间，取值范围是1～65535，单位为毫秒，缺省值为5000毫秒。

*[host*]：目的端的IP地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

【使用指导】

**[tracert**]命令用来查看IPv4报文从源端传到目的端所经过的路径。

当用户使用**ping**命令测试发现网络出现故障后，可以用**tracert**命令分析出现故障的网络节点。

**[tracert**]命令的输出信息包括到达目的端所经过的所有三层设备的IP地址，如果某设备不能回应ICMP错误消息（可能因为路由不可达或者没有开启ICMP错误报文处理功能），则输出"\* \* \*"。

在执行命令过程中，键入\<Ctrl+C\>可终止此次tracert操作。

【举例】

\# 查看报文从源端到目的端（IP地址为1.1.2.2）所经过的路径。

\<Sysname\> tracert 1.1.2.2

traceroute to 1.1.2.2 (1.1.2.2), 30 hops at most, 40 bytes each packet, press CTRL_C to break

 1  1.1.1.2 (1.1.1.2) 673 ms 425 ms 30 ms

 2  1.1.2.2 (1.1.2.2) 580 ms 470 ms 80 ms

\# 查看报文从源端到目的端（IP地址为192.168.0.46）所经过的路径（途经MPLS网络）。

\<Sysname\> tracert 192.168.0.46

traceroute to 192.168.0.46 (192.168.0.46), 30 hops at most, 40 bytes each packet, press CTRL_C to break

 1  192.0.2.13 (192.0.2.13)  0.661 ms  0.618 ms  0.579 ms

 2  192.0.2.9 (192.0.2.9)  0.861 ms  0.718 ms  0.679 ms

    MPLS Label=100048 Exp=0 TTL=1 S=1

 3  192.0.2.5 (192.0.2.5)  0.822 ms  0.731 ms  0.708 ms

    MPLS Label=100016 Exp=0 TTL=1 S=1

 4  192.0.2.1 (192.0.2.1)  0.961 ms  8.676 ms  0.875 ms

表1-3 tracert命令显示信息描述表

字段

描述

traceroute to 1.1.2.2 (1.1.2.2)

查看IP报文从当前设备传到地址为1.1.2.2的设备所经过的路径

hops at most

探测报文的最大跳数，可使用**-m**参数配置

bytes each packet

探测报文字节数

press CTRL_C to break

在执行命令过程中，键入\<Ctrl+C\>可终止此次tracert操作

1  1.1.1.2 (1.1.1.2) 673 ms 425 ms 30 ms

TTL值为1的探测报文的探测结果，内容包括：第一跳的域名（如果没有配置域名则显示IP地址）、IP地址、三份探测报文的往返时间

每次发送探测报文的份数可以使用**-q**参数配置

MPLS Label=100048 Exp=0 TTL=1 S=1

当源端到目的端途经MPLS网络时，ICMP超时报文中会携带MPLS标签信息：

·Label：标签值，用来标识一个FEC

·Exp：保留，协议中没有明确规定，通常用作服务等级

·TTL：TTL值

·S：MPLS支持多重标签，值为1时表示此标签为最底层标签，值为0时表示此标签为其它层标签

**系统维护与调试 \-- 系统维护与调试命令 \-- tracert ipv6**

------------------------------------------------------------------------

**[tracert ipv6**]命令用来查看IPv6报文从源端传到目的端所经过的路径。

【命令】

**[tracert ipv6**[ [ **-f** *first-hop* \| **-m** *max-hops* \| **-p** *port* \| **-q** *packet-number* \| **-t** *traffic-class* \| **-vpn-instance** *vpn-instance-name* \| **-w** *timeout* ] \* *host*]]

【视图】

任意视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[-f*** first-hop*]：指定一个初始hoplimit，即第一个报文所允许的跳数。取值范围为1～255，且小于或等于*max-hops*，缺省值为1。

**[-m*** max-hops*]：指定一个最大hoplimit，即一个报文所允许的最大跳数。取值范围为1～255，且大于或等于*first-hop*，缺省值为30。

**[-p*** port*]：指定目的端的UDP端口号，取值范围为1～65535，缺省值为33434。用户一般不需要更改此选项。

**[-q** *packet-number*]：指定每次发送的探测报文个数，取值范围为1～65535，缺省值为3。

**[-t** *traffic-class*]：IPv6 tracert报文中的Traffic Class域的值。取值范围为0～255，缺省值为0。

**[-vpn-instance** *vpn-instance-name*]：指定目的端所属的VPN。*vpn-instance-name*表示MPLS L3VPN的VPN实例名称，为1～31个字符的字符串，区分大小写。如果未指定本参数，则表示目的端位于公网中。

**[-w*** timeout*]：指定探测报文的响应报文的超时时间，取值范围为1\~65535，单位为毫秒，缺省值为5000毫秒。

*[host*]：目的端的IPv6地址或主机名。其中，主机名为1～253个字符的字符串，不区分大小写，字符串仅可包含字母、数字、"-"、"\_"或"."。

【使用指导】

当用户使用**ping ipv6**命令测试发现网络出现故障后，可以用**tracert ipv6**命令来帮助查找出现故障的网络节点。

本命令的输出信息包括到达目的端所经过的所有三层设备的IPv6地址，如果某设备不能回应ICMP错误消息（可能因为路由不可达或者没有开启ICMP错误报文处理功能），则输出"\*  \*  \*"。

在执行命令过程中，键入\<Ctrl+C\>可终止此次tracert ipv6操作。

【举例】

\# 查看报文从源端到目的端（IPv6地址为2001:3::2）所经过的路径。

\<Sysname\> tracert ipv6 2001:3::2

traceroute to 2001:3::2(2001:3::2), 30 hops at most, 60 byte packets , press CTRL_C to break

 1  2001:1::2  0.661 ms  0.618 ms  0.579 ms

 2  2001:2::2  0.861 ms  0.718 ms  0.679 ms

 3  2001:3::2  0.822 ms  0.731 ms  0.708 ms

表1-4 tracert ipv6命令显示信息描述表

字段

描述

traceroute to 2001:3::2

查看IPv6报文从当前设备发送到地址为2001:3::2的设备所经过的路径

hops at most

探测报文的最大跳数，可使用**-m**参数配置

byte packets

探测报文字节数

1  2001:1::2  0.661 ms  0.618 ms  0.579 ms

*[hoplimit*]值为1的探测报文的探测结果，内容包括：第一跳的IPv6地址、三份探测报文的往返时间（每次发送探测报文的份数可以使用**-q**参数配置）

