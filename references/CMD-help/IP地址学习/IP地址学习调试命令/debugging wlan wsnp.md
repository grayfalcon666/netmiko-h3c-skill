::: {#358280274 .myid}
[]{#_Toc404795321}[]{#struct_0_x5898_17832_x668563699}[]{#_Toc394063172}

**IP地址学习 \-- IP地址学习调试命令 \-- debugging wlan wsnp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5898_17832_x1957134596}

[**[debugging wlan wsnp]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x5898_17832_1558082218}

[**[undo debugging wlan wsnp]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x5898_17832_x469222437}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5898_17832_901122517}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5898_17832_x1206878015}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5898_17832_x954569089}

[[network-admin]{lang="EN-US"}]{#struct_0_x5898_17832_x1115821208}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5898_17832_557661167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5898_17832_x1367560144}

[**[all]{lang="EN-US"}**]{#struct_0_x5898_17832_384059457}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址学习模块所有的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x5898_17832_x1343657652}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址学习模块错误的调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5898_17832_1454099244}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址学习模块事件的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5898_17832_1964856658}

[**[debugging wlan wsnp]{lang="EN-US"}**]{#struct_0_x5898_17832_x1000468887}[命令用来打开]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址学习调试信息开关。]{style="font-family:宋体"}**[undo debugging wlan wsnp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址学习调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5898_17832_x1522631328}[地址学习调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging wlan wsnp error]{lang="EN-US"}]{#struct_0_x5898_17832_1984788380}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1782481914}[[字段]{style="font-family:黑体"}]{#struct_0_x5898_17832_152425009}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5898_17832_x784124902}

[[No WSNP data in client.]{lang="EN-US"}]{#struct_0_x5898_17832_741807826}

[[STA]{lang="EN-US"}]{#struct_0_x5898_17832_1851691129}[结构下没有]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[No client *ClientMAC* in BSS or no WSNP data in client *ClientMAC*.]{lang="EN-US"}]{#struct_0_x5898_17832_723955762}

[[BSS]{lang="EN-US"}]{#struct_0_x5898_17832_1613062147}[下没有客户端]{style="font-family:宋体"}*[ClientMAC]{lang="EN-US"}*[，或者客户端]{style="font-family:宋体"}*[ClientMAC]{lang="EN-US"}*[下没有]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[Captured an invalid *MessageType* packet: Its length (*PacketLength*) is not greater than *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_x2106319886}

[[拦截到非法的]{style="font-family:宋体"}*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_x1760633593}[类型报文，由于报文长度]{style="font-family:宋体"}*[PacketLength]{lang="EN-US"}*[必须比]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[长]{style="font-family:宋体"}

[*[MessageType ]{lang="EN-US"}*]{#struct_0_x5898_17832_562364706}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ARP]{lang="EN-US"}]{#struct_0_x5898_17832_1367387912}[：上行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_938247213}[：上行]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_x1196053663}[：下行]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x468690242}[：上行]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x678026870}[：下行]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1611840827}[：上行]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink UDPv6]{lang="EN-US"}]{#struct_0_x5898_17832_46978206}[：上行]{style="font-family:宋体"}[UDPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x957200315}[：上行]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x653790746}[：下行]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink unicast ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1156517201}[：下行单播]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink unicast UDPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x529485975}[：下行单播]{style="font-family:宋体"}[UDPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink broadcast ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_432579469}[：下行广播]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Captured an invalid *MessageType* packet: Its length (*PacketLength*) is not smaller than *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1061925683}

[[拦截到无效的]{style="font-family:宋体"}*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_x2020188032}[类型报文，由于报文长度]{style="font-family:宋体"}*[PacketLength]{lang="EN-US"}*[必须比]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[短]{style="font-family:宋体"}

[*[MessageType ]{lang="EN-US"}*]{#struct_0_x5898_17832_1035388605}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink ARP]{lang="EN-US"}]{#struct_0_x5898_17832_x1519105735}[：上行]{style="font-family:
  宋体"}[ARP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_x228389887}[：上行]{style="font-family:
  宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[downlink DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_733420146}[：下行]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1308129602}[：上行]{style="font-family:
  宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[downlink IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1540956890}[：下行]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_2004796039}[：上行]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink UDPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1134166145}[：上行]{style="font-family:
  宋体"}[UDPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[uplink DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1973824458}[：上行]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[downlink DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_497316900}[：下行]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[downlink unicast ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1837300176}[：下行单播]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[downlink unicast UDPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1468216361}[：下行单播]{style="font-family:宋体"}[UDPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[downlink broadcast ICMPv6]{lang="EN-US"}]{#struct_0_x5898_17832_871305138}[：下行广播]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Invalid *PktSocketType* DHCP packet: Message Type option not found.]{lang="EN-US"}]{#struct_0_x5898_17832_3451418}

[*[PktSocketType]{lang="EN-US"}*[ DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_x313214482}[报文未携带]{style="font-family:宋体"}[Message Type option]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uplink]{lang="EN-US"}]{#struct_0_x5898_17832_246588511}[：上行]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Downlink]{lang="EN-US"}]{#struct_0_x5898_17832_x1068767041}[：下行]{style="font-family:宋体"}

[[Discarded packet: Invalid IPv4 address *IPv4Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_291739715}

[[丢弃报文，由于报文]{style="font-family:宋体"}]{#struct_0_x5898_17832_x1254921065}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[\[*IPv4Addr*\]]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Discarded packet: Requested IP Address option not found.]{lang="EN-US"}]{#struct_0_x5898_17832_x1489995551}

[[丢弃报文，由于报文未携带]{style="font-family:宋体"}[Requested IP Address option]{lang="EN-US"}]{#struct_0_x5898_17832_429263919}

[[Discarded packet: Invalid IPv4 address length *IPLength*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1600312586}

[[丢弃报文，由于报文]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_853612796}[地址长度]{style="font-family:宋体"}*[IPLength]{lang="EN-US"}*[非法]{style="font-family:宋体"}

[[Discarded packet: Invalid packet length *PacketLength*.]{lang="EN-US"}]{#struct_0_x5898_17832_1998049527}

[[丢弃报文，由于报文长度]{style="font-family:宋体"}*[PacketLength]{lang="EN-US"}*]{#struct_0_x5898_17832_x813154500}[非法]{style="font-family:宋体"}

[[Discarded ]{lang="EN-US"}]{#struct_0_x5898_17832_x1239899002}[ND]{lang="EN-US"}[-]{lang="EN-US"}[NA packet]{lang="EN-US"}[: ]{lang="EN-US"}[It]{lang="EN-US"}[ is ]{lang="EN-US"}[not]{lang="EN-US"}[ the response to the ND-NS packet.]{lang="EN-US"}

[[丢弃报文，由于]{style="font-family:宋体"}[ND-NA]{lang="EN-US"}]{#struct_0_x5898_17832_1746432535}[报文不是]{style="font-family:宋体"}[ND-NS]{lang="EN-US"}[报文的回应报文]{style="font-family:宋体"}

[[Discarded packet: Option type *OptionType* or option length *Optionlength* is invalid.]{lang="EN-US"}]{#struct_0_x5898_17832_985291294}

[[丢弃报文，由于]{style="font-family:宋体"}[option]{lang="EN-US"}]{#struct_0_x5898_17832_x712471145}[类型]{style="font-family:宋体"}*[OptionType]{lang="EN-US"}*[无效或者]{style="font-family:宋体"}[option]{lang="EN-US"}[长度]{style="font-family:宋体"}*[Optionlength]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Discarded packet: MAC address *MACAddress* in the option is not the MAC address of the client.]{lang="EN-US"}]{#struct_0_x5898_17832_x19505659}

[[丢弃报文，由于]{style="font-family:宋体"}[option]{lang="EN-US"}]{#struct_0_x5898_17832_x297595282}[中的]{style="font-family:宋体"}[MAC ]{lang="EN-US"}[地址]{style="font-family:宋体"}*[MACAddress]{lang="EN-US"}*[与客户端地址不匹配]{style="font-family:宋体"}

[[Discarded packet: IP address is loopback IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_x342719521}

[[丢弃报文，由于]{style="font-family:宋体"}]{#struct_0_x5898_17832_x837145882}[IP]{lang="EN-US"}[地址是环路]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*

[[Discarded packet: IP address is multicast IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_x972842239}

[[丢弃报文，由于]{style="font-family:宋体"}]{#struct_0_x5898_17832_2016412210}[IP]{lang="EN-US"}[地址是组播]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*

[[Discarded packet:]{lang="EN-US"}[ IP address is unspecified IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_779358195}

[[丢弃报文，由于]{style="font-family:宋体"}]{#struct_0_x5898_17832_1438763523}[IP]{lang="EN-US"}[地址是未指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*

[[Discarded packet:]{lang="EN-US"}[ IP address is link local IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_1604421975}

[[丢弃报文，由于]{style="font-family:宋体"}]{#struct_0_x5898_17832_450328269}[IP]{lang="EN-US"}[地址是本地链路]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*

[[Discarded packet: Incomplete DHCPv6 *OptionType* option.]{lang="EN-US"}]{#struct_0_x5898_17832_x789830151}

[[丢弃报文，由于]{style="font-family:宋体"}]{#struct_0_x5898_17832_1206797674}[DHCPv6 option ]{lang="EN-US"}*[OptionType]{lang="EN-US"}*[不完整]{style="font-family:宋体"}

[[Discarded packet: Invalid header length *Length* of DHCPv6 *OptionType* option.]{lang="EN-US"}]{#struct_0_x5898_17832_839811425}

[[丢弃报文，由于]{style="font-family:宋体"}[DHCPv6 *OptionType* option]{lang="EN-US"}]{#struct_0_x5898_17832_2004632772}[头长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[*[OptionType]{lang="EN-US"}*]{#struct_0_x5898_17832_x1115755672}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x5898_17832_x244986120}[：]{style="font-family:宋体"}[Non-temporary Address]{lang="EN-US"}[非暂时地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TA]{lang="EN-US"}]{#struct_0_x5898_17832_x1884334577}[：]{style="font-family:宋体"}[Temporary Address]{lang="EN-US"}[暂时地址]{style="font-family:宋体"}

[[Discarded packet: Invalid length *Length* of DHCPv6 *OptionType* option.]{lang="EN-US"}]{#struct_0_x5898_17832_677018088}

[[丢弃报文，由于]{style="font-family:宋体"}[DHCPv6 *OptionType* option]{lang="EN-US"}]{#struct_0_x5898_17832_2053314344}[长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[*[OptionType]{lang="EN-US"}*]{#struct_0_x5898_17832_1613127683}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x5898_17832_202471832}[：]{style="font-family:宋体"}[Non-temporary Address]{lang="EN-US"}[非暂时地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TA]{lang="EN-US"}]{#struct_0_x5898_17832_2019347482}[：]{style="font-family:宋体"}[Temporary Address]{lang="EN-US"}[暂时地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IA]{lang="EN-US"}]{#struct_0_x5898_17832_604400804}[：]{style="font-family:宋体"}[Identify Association]{lang="EN-US"}[认证关联]{style="font-family:宋体"}

[[Discarded packet: Length of *OptionType* option is 0.]{lang="EN-US"}]{#struct_0_x5898_17832_47043742}

[[丢弃报文，由于]{style="font-family:宋体"}[Option\[*OptionType*\]]{lang="EN-US"}]{#struct_0_x5898_17832_1511122423}[中]{style="font-family:宋体"}[option]{lang="EN-US"}[长度]{style="font-family:宋体"}[0]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[Discarded packet: Incomplete packet.]{lang="EN-US"}]{#struct_0_x5898_17832_x875684911}

[[丢弃报文，由于报文不完整]{style="font-family:宋体"}]{#struct_0_x5898_17832_201381164}

[[Discarded packet: Invalid prefix length *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1519040199}

[[丢弃报文，由于前缀长度]{style="font-family:宋体"}]{#struct_0_x5898_17832_1998241415}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to add the source *Source* for IPv4 address *IPv4Addr*: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_1499522131}

[[添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_1706847955}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[失败，由于分配内存失败]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_497382436}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_861073666}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ARP]{lang="EN-US"}]{#struct_0_x5898_17832_349439962}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Failed to delete the source *Source* for IPv4 address *IPv4Addr*: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_x1068701505}

[[删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_x947931684}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[失败，由于分配内存失败]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_x1943566762}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_2031061832}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ARP]{lang="EN-US"}]{#struct_0_x5898_17832_1284084738}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Failed to add the source *Source* for IPv6 address *IPv6Addr*: Memory allocation failure. ]{lang="EN-US"}]{#struct_0_x5898_17832_184359164}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x723994678}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[失败，由于分配内存失败]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_1948135245}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1381724777}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ND]{lang="EN-US"}]{#struct_0_x5898_17832_2109350691}[：]{style="font-family:宋体"}[ND]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Failed to delete the source *Source* for IPv6 address *IPv6Addr*: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_1032787661}

[[删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_747550447}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[失败，由于分配内存失败]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_1347158578}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1674373266}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ND]{lang="EN-US"}]{#struct_0_x5898_17832_x1918719546}[：]{style="font-family:宋体"}[ND]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Failed to add the source *Source* for IPv6 prefix *IPv6Addr* whose length is *length*: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_x218925363}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x720621363}[前缀]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[前缀长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[失败，由于分配内存失败]{style="font-family:宋体"}

[*[MethodType]{lang="EN-US"}*]{#struct_0_x5898_17832_x1079937482}[取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ND]{lang="EN-US"}]{#struct_0_x5898_17832_x1785009304}[：]{style="font-family:宋体"}[ND]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Failed to send ]{lang="EN-US"}]{#struct_0_x5898_17832_1581318340}*[MessageType ]{lang="EN-US"}*[message to the uplink device.]{lang="EN-US"}

[[发送]{style="font-family:宋体"}]{#struct_0_x5898_17832_x21376320}*[MessageType]{lang="EN-US"}*[消息到上行设备失败]{style="font-family:宋体"}

[*[MessageType ]{lang="EN-US"}*]{#struct_0_x5898_17832_943874051}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 entry]{lang="EN-US"}]{#struct_0_x5898_17832_x1123339581}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv]{lang="EN-US"}]{#struct_0_x5898_17832_1426014470}[6]{lang="EN-US"}[ entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 prefix entry]{lang="EN-US"}]{#struct_0_x5898_17832_x622209890}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀选项]{style="font-family:宋体"}

[[Failed to send WSNP data for roaming clients to AP: Data length=*DataLen*.]{lang="EN-US"}]{#struct_0_x5898_17832_567548449}

[[发送漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}]{#struct_0_x5898_17832_x422250773}[数据]{style="font-family:宋体"}[(]{lang="EN-US"}[长度：]{style="font-family:宋体"}*[DataLen]{lang="EN-US"}*[)]{lang="EN-US"}[给]{style="font-family:宋体"}[AP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send ]{lang="EN-US"}]{#struct_0_x5898_17832_1117651119}*[MessageType ]{lang="EN-US"}*[to HA.]{lang="EN-US"}

[[发送]{style="font-family:宋体"}]{#struct_0_x5898_17832_2106673465}*[MessageType]{lang="EN-US"}*[消息到]{style="font-family:宋体"}[HA]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_x1927109870}[取值如下：]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 ]{lang="EN-US"}]{#struct_0_x5898_17832_x752146943}[entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 ]{lang="EN-US"}]{#struct_0_x5898_17832_x171871196}[entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 Prefix]{lang="EN-US"}]{#struct_0_x5898_17832_x297890193}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀表项]{style="font-family:宋体"}

[[Unsupported message type.]{lang="EN-US"}]{#struct_0_x5898_17832_x1895684432}

[[不支持消息类型]{style="font-family:宋体"}]{#struct_0_x5898_17832_x1737955137}

[[Invalid message type.]{lang="EN-US"}]{#struct_0_x5898_17832_x2052267544}

[[要解析的消息类型无效]{style="font-family:宋体"}]{#struct_0_x5898_17832_94434537}

[[Length of message from FA is invalid: Length= *MessageLength.*]{lang="EN-US"}]{#struct_0_x5898_17832_184424700}

[[来自]{style="font-family:宋体"}[FA]{lang="EN-US"}]{#struct_0_x5898_17832_x844104431}[的消息长度]{style="font-family:宋体"}*[MessageLength]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to process IP entry from FA.]{lang="EN-US"}]{#struct_0_x5898_17832_x1640087970}

[[处理来自]{style="font-family:宋体"}[FA]{lang="EN-US"}]{#struct_0_x5898_17832_x1381659241}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项失败]{style="font-family:宋体"}

[[Failed to get WSNP data for intra-AC roaming clients.]{lang="EN-US"}]{#struct_0_x5898_17832_1888239517}

[[获取]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x5898_17832_x735426698}[内漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to get WSNP data for inter-AC roaming clients.]{lang="EN-US"}]{#struct_0_x5898_17832_1347224114}

[[获取]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x5898_17832_x249138773}[间漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to recover WSNP data for roaming clients: Didn\'t get TLV data through TLV handle.]{lang="EN-US"}]{#struct_0_x5898_17832_x1429686882}

[[恢复漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}]{#struct_0_x5898_17832_x218859827}[数据失败：通过]{style="font-family:宋体"}[TLV handle ]{lang="EN-US"}[获取]{style="font-family:宋体"}[TLV]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to decode roam IPv4 entry: Invalid message length *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_1162871648}

[[解析漫游]{style="font-family:宋体"}]{#struct_0_x5898_17832_1001965411}[IPv4]{lang="EN-US"}[表项失败：消息长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to decode roam IPv6 entry: Invalid message length *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1784943768}

[[解析漫游]{style="font-family:宋体"}]{#struct_0_x5898_17832_698962489}[IPv6]{lang="EN-US"}[表项失败：消息长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to decode roam IPv6 prefix entry: Invalid message length *Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_x247649492}

[[解析漫游]{style="font-family:宋体"}]{#struct_0_x5898_17832_943939587}[IPv6]{lang="EN-US"}[前缀表项失败：消息长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Failed to notify module *moduleID* of IP event *event*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1167266754}

[[通知其它模块]{style="font-family:宋体"}[\[]{lang="EN-US"}]{#struct_0_x5898_17832_118488653}*[module]{lang="EN-US"}[ID]{lang="EN-US"}*[\]]{lang="EN-US"}[IP]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to initiate WSNP data in fake client: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_x622144354}

[[初始化]{style="font-family:宋体"}[fake STA]{lang="EN-US"}]{#struct_0_x5898_17832_x583913885}[结构中的]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据失败：分配内存失败]{style="font-family:宋体"}

[[Failed to initiate WSNP data in client: Memory allocation failure.]{lang="EN-US"}]{#struct_0_x5898_17832_x1699622725}

[[初始化]{style="font-family:宋体"}]{#struct_0_x5898_17832_2106739001}[STA]{lang="EN-US"}[结构中的]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据失败：分配内存失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x5898_17832_x1163841347}[[表1-2 ]{lang="EN-US"}[debugging wlan wsnp event]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1800475244}[[字段]{style="font-family:黑体"}]{#struct_0_x5898_17832_887730162}

[[描述]{style="font-family:黑体"}]{#struct_0_x5898_17832_x1878402476}

[[Captured *MessageType* packet.]{lang="EN-US"}]{#struct_0_x5898_17832_x1669081420}

[[拦截到]{style="font-family:宋体"}*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_1903230937}[报文]{style="font-family:宋体"}

[*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_1225401385}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ]{lang="EN-US"}[ARP]{lang="EN-US"}]{#struct_0_x5898_17832_1121822719}[-REQUEST]{lang="EN-US"}[：上行]{style="font-family:宋体"}[ARP]{lang="EN-US"}[-REQUEST]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ]{lang="EN-US"}[ARP-REPLY]{lang="EN-US"}]{#struct_0_x5898_17832_x1807868915}[：上行]{style="font-family:宋体"}[ARP-REPLY]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ]{lang="EN-US"}[DHCP-DECLINE]{lang="EN-US"}]{#struct_0_x5898_17832_x1999182250}[：]{lang="EN-US" style="font-family:宋体"}[上行]{style="font-family:宋体"}[DHCP-DECLINE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ]{lang="EN-US"}[DHCP-RELEASE]{lang="EN-US"}]{#struct_0_x5898_17832_x1970084255}[：]{lang="EN-US" style="font-family:宋体"}[上行]{style="font-family:宋体"}[DHCP-RELEASE]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink DHCP]{lang="EN-US"}[-ACK]{lang="EN-US"}]{#struct_0_x5898_17832_x171805660}[：]{lang="EN-US" style="font-family:宋体"}[下行]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink]{lang="EN-US"}[ ND]{lang="EN-US"}]{#struct_0_x5898_17832_x299867950}[-NS]{lang="EN-US"}[：上行]{style="font-family:宋体"}[ND-NS]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink ND-NA]{lang="EN-US"}]{#struct_0_x5898_17832_x1319265473}[：上行]{style="font-family:宋体"}[ND-NA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink DHCP6-DECLINE]{lang="EN-US"}]{#struct_0_x5898_17832_1597845940}[：上行]{style="font-family:宋体"}[DHCP6-DECLINE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[uplink DHCP6-RELEASE]{lang="EN-US"}]{#struct_0_x5898_17832_x1094077063}[：上行]{style="font-family:宋体"}[DHCP6-RELEASE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink unicast ND-RA]{lang="EN-US"}]{#struct_0_x5898_17832_1148599061}[：下行单播]{style="font-family:宋体"}[ND-RA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[downlink ]{lang="EN-US"}[DHCP6-REPLY]{lang="EN-US"}]{#struct_0_x5898_17832_x1152033632}[：下行]{style="font-family:宋体"}[DHCP6-REPLY]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Captured a downlink broadcast ND-RA packet in BSS *BSSID*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1262742746}

[[BSS\[*BSSID*\] ]{lang="EN-US"}]{#struct_0_x5898_17832_1484658713}[拦截到下行广播]{style="font-family:宋体"}[ND-RA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Added the source *Source* for IPv4 address *IPv4Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_335467095}

[[添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_x1737889601}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[的来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_x1380120524}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ARP]{lang="EN-US"}]{#struct_0_x5898_17832_12621661}[：]{style="font-family:宋体"}[ARP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_x5898_17832_524210}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Updated IPv4 address *IPv4Addr* successfully. Changed source from ARP to DHCP.]{lang="EN-US"}]{#struct_0_x5898_17832_665574392}

[[更新]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_1920968885}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[成功，学习方式由]{style="font-family:宋体"}[ARP]{lang="EN-US"}[改为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}

[[Failed to add IPv4 address *IPv4Addr*: The address already existed.]{lang="EN-US"}]{#struct_0_x5898_17832_x1719216231}

[[添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_x1843429923}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[失败，由于地址已存在]{style="font-family:宋体"}

[[Deleted IPv4 address *IPv4Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_184490236}

[[删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_717576571}[地址]{style="font-family:宋体"}*[IPv4Addr]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Failed to delete IPv4 address *IPv4Addr*: The address didn\'t exist. ]{lang="EN-US"}]{#struct_0_x5898_17832_x581076850}

[[删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x5898_17832_1937583416}[地址失败，由于地址不存在]{style="font-family:宋体"}

[[Added the source *Source* for IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_35883284}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1871954586}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_411371092}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1381593705}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ND]{lang="EN-US"}]{#struct_0_x5898_17832_x803353358}[：]{style="font-family:宋体"}[ND]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Updated IPv6 address *IPv6Addr* successfully. Changed source from ND to DHCPv6.]{lang="EN-US"}]{#struct_0_x5898_17832_x154895253}

[[更新]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x645813247}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[成功，来源由]{style="font-family:宋体"}[ND]{lang="EN-US"}[改为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}

[[Failed to add the source *Source* for IPv6 address *IPv6Addr*: The source already existed.]{lang="EN-US"}]{#struct_0_x5898_17832_1727307058}

[[要添加的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1688190826}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[已经存在]{style="font-family:宋体"}

[*[Source]{lang="EN-US"}*]{#struct_0_x5898_17832_198735700}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPv6]{lang="EN-US"}]{#struct_0_x5898_17832_1347289650}[：]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ND]{lang="EN-US"}]{#struct_0_x5898_17832_2045533582}[：]{style="font-family:宋体"}[ND]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[Deleted IPv6 address *IPv6Addr*.]{lang="EN-US"}]{#struct_0_x5898_17832_195085013}

[[删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x1484446710}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Failed to delete IPv6 address *IPv6Addr*: The address didn\'t exist. ]{lang="EN-US"}]{#struct_0_x5898_17832_x1472881640}

[[要删除的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_704522730}[地址]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[不存在]{style="font-family:宋体"}

[[Added the source *Source* for IPv6 prefix *IPv6Addr* whose length is *length*.]{lang="EN-US"}]{#struct_0_x5898_17832_1781129991}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_x218794291}[前缀]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[前缀长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[来源]{style="font-family:宋体"}*[Source]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Failed to add IPv6 prefix *IPv6Addr* whose length is *length*: The prefix already exists.]{lang="EN-US"}]{#struct_0_x5898_17832_x353786571}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5898_17832_108476169}[前缀]{style="font-family:宋体"}*[IPv6Addr]{lang="EN-US"}*[前缀长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[失败：已存在]{style="font-family:宋体"}

[[Sent ]{lang="EN-US"}]{#struct_0_x5898_17832_1344465829}*[MessageType ]{lang="EN-US"}*[message to the uplink device.]{lang="EN-US"}

[[发送]{style="font-family:宋体"}]{#struct_0_x5898_17832_x2049251965}*[MessageType]{lang="EN-US"}*[消息到上行设备成功]{style="font-family:宋体"}

[*[MessageType ]{lang="EN-US"}*]{#struct_0_x5898_17832_x1341180753}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 entry]{lang="EN-US"}]{#struct_0_x5898_17832_x1784878232}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv]{lang="EN-US"}]{#struct_0_x5898_17832_1610381263}[6]{lang="EN-US"}[ entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 prefix entry]{lang="EN-US"}]{#struct_0_x5898_17832_1490522286}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀选项]{style="font-family:宋体"}

[[Sent WSNP data for roaming clients to AP: Data length=*DataLen*.]{lang="EN-US"}]{#struct_0_x5898_17832_1477668572}

[[发送漫游用户迁移]{style="font-family:宋体"}]{#struct_0_x5898_17832_2053279718}[WSNP]{lang="EN-US"}[数据]{style="font-family:宋体"}[(]{lang="EN-US"}[长度：]{style="font-family:宋体"}*[DataLen]{lang="EN-US"}*[)]{lang="EN-US"}[给]{style="font-family:宋体"}[AP]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Sent ]{lang="EN-US"}]{#struct_0_x5898_17832_944005123}*[MessageType ]{lang="EN-US"}*[message to HA.]{lang="EN-US"}

[[发送]{style="font-family:宋体"}]{#struct_0_x5898_17832_958649850}*[MessageType]{lang="EN-US"}*[消息到]{style="font-family:宋体"}[HA]{lang="EN-US"}[成功]{style="font-family:宋体"}

[*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_746385341}[取值如下：]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 ]{lang="EN-US"}]{#struct_0_x5898_17832_x257058530}[entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 ]{lang="EN-US"}]{#struct_0_x5898_17832_x1119316354}[entry]{lang="EN-US"}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6 Prefix]{lang="EN-US"}]{#struct_0_x5898_17832_x622078818}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀表项]{style="font-family:宋体"}

[[Received *MessageType* message: APID=*APID*, CMD=*CMD*, length=*Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_2144052556}

[[接收到]{style="font-family:宋体"}*[MessageType]{lang="EN-US"}*]{#struct_0_x5898_17832_1141067300}[消息，]{style="font-family:宋体"}[APID=*APID*, CMD=*CMD*, length=*Length*.]{lang="EN-US"}

[*[MessageType ]{lang="EN-US"}*]{#struct_0_x5898_17832_1038941391}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[an up entry]{lang="EN-US"}]{#struct_0_x5898_17832_1096327010}[：上行表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a down entry]{lang="EN-US"}]{#struct_0_x5898_17832_2106804537}[：下行表项]{style="font-family:宋体"}

[[Received a fake entry from FA: Entry length=*Length*.]{lang="EN-US"}]{#struct_0_x5898_17832_1182263504}

[[接收到来自]{style="font-family:宋体"}[FA]{lang="EN-US"}]{#struct_0_x5898_17832_907805465}[的]{style="font-family:宋体"}[fake]{lang="EN-US"}[表项（表项长度]{style="font-family:宋体"}[= *Length*)]{lang="EN-US"}

[[Processed IP entry from FA successfully.]{lang="EN-US"}]{#struct_0_x5898_17832_x1813043970}

[[处理来自]{style="font-family:宋体"}[FA]{lang="EN-US"}]{#struct_0_x5898_17832_x171740124}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项成功]{style="font-family:宋体"}

[[Got WSNP data for intra-AC roaming clients.]{lang="EN-US"}]{#struct_0_x5898_17832_x1861811548}

[[获取]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x5898_17832_x2040083021}[内漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据成功]{style="font-family:宋体"}

[[Got WSNP data for inter-AC roaming clients.]{lang="EN-US"}]{#struct_0_x5898_17832_750479596}

[[获取]{style="font-family:宋体"}]{#struct_0_x5898_17832_1041060003}[AC]{lang="EN-US"}[间漫游用户迁移]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据成功]{style="font-family:宋体"}

[[Recovered WSNP data for roaming clients: Data length=*DataLen*.]{lang="EN-US"}]{#struct_0_x5898_17832_x1737824065}

[[恢复漫游用户迁移]{style="font-family:宋体"}[WANP]{lang="EN-US"}]{#struct_0_x5898_17832_1732150680}[数据成功，数据长度]{style="font-family:宋体"}[= *DataLen*]{lang="EN-US"}

[[Initialized WSNP data in fake STA successfully.]{lang="EN-US"}]{#struct_0_x5898_17832_x289270541}

[[初始化]{style="font-family:宋体"}[fake STA]{lang="EN-US"}]{#struct_0_x5898_17832_941835332}[结构中的]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据成功]{style="font-family:宋体"}

[[Destroyed WSNP data in fake STA.]{lang="EN-US"}]{#struct_0_x5898_17832_184555772}

[[销毁]{style="font-family:宋体"}[fake STA]{lang="EN-US"}]{#struct_0_x5898_17832_x1249575894}[结构中的]{style="font-family:宋体"}[WSNP]{lang="EN-US"}[数据成功]{style="font-family:宋体"}

[[Deleted WSNP information in the client.]{lang="EN-US"}]{#struct_0_x5898_17832_x632751601}

[[删除]{style="font-family:宋体"}[WSNP]{lang="EN-US"}]{#struct_0_x5898_17832_1506176538}[信息成功]{style="font-family:宋体"}

[[Initialized WSNP information in the client successfully.]{lang="EN-US"}]{#struct_0_x5898_17832_x1381528169}

[[初始化]{style="font-family:宋体"}[WSNP]{lang="EN-US"}]{#struct_0_x5898_17832_x1020357349}[信息成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5898_17832_219659290}

[[\# MAC]{lang="EN-US"}]{#struct_0_x5898_17832_x764779751}[地址为]{style="font-family:宋体"}[0023-8933-216b ]{lang="EN-US"}[静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.3.22]{lang="EN-US"}[的客户端成功上线后，其所在]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}[000f-e212-ff01]{lang="EN-US"}[，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[和]{style="font-family:宋体"}[AP]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan wsnp event]{lang="EN-US"}[开关，客户端成功上线后，]{style="font-family:宋体"}[AP]{lang="EN-US"}[上会有如下调试信息：]{style="font-family:宋体"}

[[\<H3C\>debugging wlan wsnp event]{lang="EN-US"}]{#struct_0_x5898_17832_x713494228}

[\*Sep 10 12:15:25:120 2014 H3C STAMGR/7/Event: Captured an uplink ARP-REQUEST packet.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x5898_17832_x1168988918}*[抓到上行]{style="font-family:宋体"}[ARP-REQUEST]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Sep 10 12:15:28:120 2014 H3C STAMGR/7/Event: \[MAC: 0023-8933-216b, BSSID: 000f-]{lang="EN-US"}]{#struct_0_x5898_17832_x1563707564}

[e212-ff01\]Added the IPv4 address\[10.1.3.22\] method\[ARP\].]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x5898_17832_x1201861819}*[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[\[10.1.3.22\]]{lang="EN-US"}[学习方式]{style="font-family:宋体"}[\[ARP\]]{lang="EN-US"}[成功。]{style="font-family:宋体"}*

[[AC]{lang="EN-US"}]{#struct_0_x5898_17832_945736965}[上会有如下调试信息]{style="font-family:宋体"}

[[\*Sep 10 12:15:28:818 2014 H3C STAMGR/7/Event: Received an up entry, APID=2, CMD=]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x5898_17832_x2022739082}

[[318767106, length=17.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x5898_17832_722052588}

[*[//]{lang="EN-US"}*]{#struct_0_x5898_17832_x2095399954}*[接收到上行表项消息。]{style="font-family:宋体"}*

[[\*Sep 10 12:15:28:819 2014 H3C STAMGR/7/Event: \[MAC: 0023-8933-216b, BSSID: 000f-]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x5898_17832_1347355186}

[[e212-ff01\]Added the IPv4 address\[10.1.3.22\] method\[ARP\]. ]{lang="EN-US"}]{#struct_0_x5898_17832_x1808210400}

[*[//]{lang="EN-US"}*]{#struct_0_x5898_17832_x702939402}*[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[\[10.1.3.22\]]{lang="EN-US"}[学习方式]{style="font-family:宋体"}[\[ARP\]]{lang="EN-US"}[成功。]{style="font-family:宋体"}*

[[\# MAC]{lang="EN-US"}]{#struct_0_x5898_17832_1394215737}[地址为]{style="font-family:宋体"}[0023-8933-216b ]{lang="EN-US"}[静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.3.22]{lang="EN-US"}[的客户端成功上线后，其所在]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}[000f-e212-ff01]{lang="EN-US"}[，在]{style="font-family:宋体"}[AC]{lang="EN-US"}[和]{style="font-family:宋体"}[AP]{lang="EN-US"}[端打开]{style="font-family:宋体"}[wlan wsnp error]{lang="EN-US"}[开关，]{style="font-family:宋体"}[STA]{lang="EN-US"}[成功上线后，]{style="font-family:宋体"}[AP]{lang="EN-US"}[上会有如下调试信息：]{style="font-family:宋体"}

[[\<H3C\> debugging wlan wsnp error]{lang="EN-US"}]{#struct_0_x5898_17832_1511700157}

[\*Sep 10 12:15:25:121 2014 H3C STAMGR/7/Error: \[MAC: 0023-8933-216b, BSSID: 000f-]{lang="EN-US"}

[e212-ff01\]Discard packet]{lang="EN-US"}[：]{style="font-family:宋体"}[Invalid IPv4 address\[0.0.0.0\].]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x5898_17832_x1291713346}*[丢弃报文：无效的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[\[0.0.0.0\]]{lang="EN-US"}*
