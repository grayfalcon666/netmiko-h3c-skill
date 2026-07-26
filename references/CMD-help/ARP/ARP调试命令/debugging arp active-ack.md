::: {#-658767476 .myid}
[]{#_Toc404786007}[]{#struct_0_20717_31151_x328902286}[]{#_Toc341864675}

**ARP \-- ARP调试命令 \-- debugging arp active-ack**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_1001974523}

[**[debugging arp active-ack]{lang="EN-US"}**]{#struct_0_20717_31151_x554240723}

[**[undo debugging arp active-ack]{lang="EN-US"}**]{#struct_0_20717_31151_x1331236380}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_1767236635}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_1887834030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_2124237015}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_1062253187}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_800502231}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_1942508606}

[**[debugging arp active-ack]{lang="EN-US"}**]{#struct_0_20717_31151_1592953266}[命令用来打开]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[主动确认调试信息开关。]{style="font-family:宋体"}**[undo debugging arp active-ack]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[主动确认调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x421398086}[主动确认调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging arp active-ack]{lang="EN-US"}]{#struct_0_20717_31151_8037847}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_312693553}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_827828318}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_1922351989}

[[ARP active-ack for new event : ]{lang="EN-US"}]{#struct_0_20717_31151_x1036212074}

[[event-type: IP *ip-address*, MAC: *mac-address*, Port: *port-name*.]{lang="EN-US"}]{#struct_0_20717_31151_1592887730}

[[新学习]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x843068350}[表项主动确认信息：事件类型为]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[,]{lang="EN-US"}[事件相关节点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[,MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[,]{lang="EN-US"}[端口名为]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*

[[事件类型：]{style="font-family:黑体"}]{#struct_0_20717_31151_x1938508483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add a node]{lang="EN-US"}]{#struct_0_20717_31151_1041805755}[：添加探测节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Aging a node]{lang="EN-US"}]{#struct_0_20717_31151_1592822194}[：老化探测节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ack a node]{lang="EN-US"}]{#struct_0_20717_31151_x29266313}[：确认探测节点]{lang="EN-US" style="font-family:宋体"}

[[ARP active-ack for new event : ]{lang="EN-US"}]{#struct_0_20717_31151_1877264531}

[[Modify a node: IP *ip-address*, Old MAC: *old mac-address*, Old port: *old port-name*. New MAC: *new mac-address*, New port: *new port-name*.]{lang="EN-US"}]{#struct_0_20717_31151_1592756658}

[[更新]{style="font-family:黑体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1593215410}[表项主动确认信息：事件相关节点的]{style="font-family:黑体"}[IP]{lang="EN-US"}[为]{style="font-family:黑体"}*[ip-address,]{lang="EN-US"}*[更新前]{style="font-family:黑体"}[MAC]{lang="EN-US"}[为]{style="font-family:黑体"}*[old mac-address]{lang="EN-US"}*[,]{lang="EN-US"}[端口名为]{style="font-family:黑体"}[o*ld port-name.*]{lang="EN-US"}[更新后]{style="font-family:黑体"}[MAC]{lang="EN-US"}[为]{style="font-family:黑体"}*[new mac-address]{lang="EN-US"}*[，端口为]{style="font-family:黑体"}*[new port-name]{lang="EN-US"}*[.]{lang="EN-US"}

[[ARP active-ack probe node is up to the limit]{lang="EN-US"}]{#struct_0_20717_31151_x70666560}

[[主动确认探测节点数目达到上限]{style="font-family:宋体"}]{#struct_0_20717_31151_1510291626}

[[ARP active-ack status changed (IP: *ip-address*,  VLAN ID:*vlan-id*):]{lang="EN-US"}]{#struct_0_20717_31151_660639945}

[[State: *old state* \-\-\--\> *new state*]{lang="EN-US"}]{#struct_0_20717_31151_x633790663}

[[Trigger: received a changed packet. MAC: *mac-address*, Port: *port-name.*]{lang="EN-US"}]{#struct_0_20717_31151_1593149874}

[[ARP ]{lang="EN-US"}]{#struct_0_20717_31151_1593084338}[主动确认表项状态变化信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address,]{lang="EN-US"}*[ VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id.]{lang="EN-US"}*[状态从]{style="font-family:宋体"}*[old state]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new state]{lang="EN-US"}[。]{style="font-family:宋体"}*[触发条件为收到一个端口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*[或者]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[变化的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[状态：]{style="font-family:宋体"}]{#struct_0_20717_31151_x845206757}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAttack]{lang="EN-US"}]{#struct_0_20717_31151_319902981}[：]{style="font-family:宋体"}[无攻击状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OldSent ]{lang="EN-US"}]{#struct_0_20717_31151_x561170761}[：原用户探测报文已发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewSent]{lang="EN-US"}]{#struct_0_20717_31151_476848318}[：新用户探测报文已发送]{style="font-family:宋体"}

[[ARP active-ack status changed (IP: *ip-address*,  VLAN ID:*vlan-id*):]{lang="EN-US"}]{#struct_0_20717_31151_1593018802}

[[State: *old state* \-\-\--\> *new state*]{lang="EN-US"}]{#struct_0_20717_31151_1977463764}

[[Trigger: received an unchanged packet. MAC: *MAC-address*, port: *port-name.*]{lang="EN-US"}]{#struct_0_20717_31151_1023715612}

[[ARP ]{lang="EN-US"}]{#struct_0_20717_31151_1007736239}[主动确认表项状态变化信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address,]{lang="EN-US"}*[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id.]{lang="EN-US"}*[状态从]{style="font-family:宋体"}*[old state]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new state]{lang="EN-US"}[。]{style="font-family:宋体"}*[触发条件为收到一个端口或者]{style="font-family:宋体"}[MAC]{lang="EN-US"}[无变化的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[状态：]{style="font-family:宋体"}]{#struct_0_20717_31151_1815547074}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAttack]{lang="EN-US"}]{#struct_0_20717_31151_1593477554}[：]{style="font-family:宋体"}[无攻击状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OldSent]{lang="EN-US"}]{#struct_0_20717_31151_736087232}[：原用户探测报文已发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewSent]{lang="EN-US"}]{#struct_0_20717_31151_1373185154}[：新用户探测报文已发送]{style="font-family:宋体"}

[[ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):]{lang="EN-US"}]{#struct_0_20717_31151_2146800318}

[[State: *old state* \-\-\--\> *new state*]{lang="EN-US"}]{#struct_0_20717_31151_x2091043250}

[[Trigger: time out for old user.]{lang="EN-US"}]{#struct_0_20717_31151_1593412018}

[[ARP ]{lang="EN-US"}]{#struct_0_20717_31151_x1594331405}[主动确认表项状态变化信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address,]{lang="EN-US"}*[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id.]{lang="EN-US"}*[状态从]{style="font-family:宋体"}*[old state]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new state]{lang="EN-US"}[。]{style="font-family:宋体"}*[触发条件为老用户发送探测报文后在超时时间没没有收到回应报文]{style="font-family:宋体"}

[[状态：]{style="font-family:宋体"}]{#struct_0_20717_31151_x3109786}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAttack]{lang="EN-US"}]{#struct_0_20717_31151_x445343555}[：]{style="font-family:宋体"}[无攻击状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OldSent]{lang="EN-US"}]{#struct_0_20717_31151_x75064233}[：原用户探测报文已发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewSent]{lang="EN-US"}]{#struct_0_20717_31151_1592953267}[：新用户探测报文已发送]{style="font-family:宋体"}

[[ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):]{lang="EN-US"}]{#struct_0_20717_31151_x421463622}

[[State: *old state* \-\-\--\> *new state*]{lang="EN-US"}]{#struct_0_20717_31151_x1110417621}

[[Trigger: time out for new user.]{lang="EN-US"}]{#struct_0_20717_31151_457527410}

[[ARP ]{lang="EN-US"}]{#struct_0_20717_31151_1592887731}[主动确认表项状态变化信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address,]{lang="EN-US"}*[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id.]{lang="EN-US"}*[状态从]{style="font-family:宋体"}*[old state]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new state]{lang="EN-US"}[。]{style="font-family:宋体"}*[触发条件为新用户发送探测报文后在超时时间内没有收到回应报文]{style="font-family:宋体"}

[[状态：]{style="font-family:宋体"}]{#struct_0_20717_31151_x843002814}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAttac]{lang="EN-US"}]{#struct_0_20717_31151_2040211251}[：无攻击状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OldSent]{lang="EN-US"}]{#struct_0_20717_31151_1234480043}[：原用户探测报文已发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewSent]{lang="EN-US"}]{#struct_0_20717_31151_851776659}[：新用户探测报文已发送]{style="font-family:宋体"}

[[ARP active-ack status changed (IP: *ip-address*, VLAN ID:*vlan-id*):]{lang="EN-US"}]{#struct_0_20717_31151_1592822195}

[[State: *old state* \-\-\--\> *new state*]{lang="EN-US"}]{#struct_0_20717_31151_x29200777}

[[Trigger: new send state received a reply with a different source MAC or port.]{lang="EN-US"}]{#struct_0_20717_31151_x470115879}

[[ New MAC: *MAC-address*, new port: *port-name.*]{lang="EN-US"}]{#struct_0_20717_31151_1985896392}

[[ARP ]{lang="EN-US"}]{#struct_0_20717_31151_1592756659}[主动确认表项状态变化信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address,]{lang="EN-US"}*[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id.]{lang="EN-US"}*[状态从]{style="font-family:宋体"}*[old state]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new state]{lang="EN-US"}[。]{style="font-family:宋体"}*[触发条件为新用户发送探测报文后收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[或者端口变化的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[状态：]{style="font-family:宋体"}]{#struct_0_20717_31151_x427540100}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NoAttack]{lang="EN-US"}]{#struct_0_20717_31151_x1855913671}[：]{style="font-family:宋体"}[无攻击状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OldSent]{lang="EN-US"}]{#struct_0_20717_31151_x268435879}[：原用户探测报文已发送]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NewSen]{lang="EN-US"}]{#struct_0_20717_31151_1593215411}[：新用户探测报文已发送]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_x70732096}

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_x412880614}[在系统视图下，]{style="font-family:宋体"}[使能]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[主动确认功能。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp active-ack]{lang="EN-US"}]{#struct_0_20717_31151_334615328}

[\*Aug  7 11:39:59:921 2011 Sysname ARP/7/ARP_ACTIVE_ACK: -MDC=1; ]{lang="EN-US"}

[ARP active-ack for new event:]{lang="EN-US"}

[Ack a node: IP:192.168.80.203, MAC:2c41-3896-9424, Port:N/A]{lang="EN-US"}

::: {#601454720 .myid}
[]{#_Toc404786008}[]{#struct_0_20717_31151_1292486290}[]{#_Toc341864672}

**ARP \-- ARP调试命令 \-- debugging arp entry**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_670646630}

[**[debugging arp]{lang="EN-US"}**[ **entry**]{lang="EN-US"}]{#struct_0_20717_31151_x807407946}

[**[undo debugging arp entry]{lang="EN-US"}**]{#struct_0_20717_31151_1593149875}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_x736215265}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_258185955}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_1570191686}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_x186335164}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_1403751318}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_234854437}

[**[debugging arp entry]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_20717_31151_x424975091}[命令用来打开]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项状态调试信息开关。]{style="font-family:宋体"}**[undo debugging arp entry]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项状态调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_20717_31151_x172055563}[ARP]{lang="EN-US"}[表项状态调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging ARP entry]{lang="EN-US"}]{#struct_0_20717_31151_1125277546}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_334069124}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_1593084339}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_x845141221}

[[ARP entry status changed]{lang="EN-US"}]{#struct_0_20717_31151_x485456540}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x1656672732}[表项发生变化]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_20717_31151_x234348134}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x739997939}[表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_20717_31151_1627948327}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1593018803}[表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[state1]{lang="EN-US"}*[-\>*state2*]{lang="EN-US"}]{#struct_0_20717_31151_1977398228}

[[从状态]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_1064800340}*[state1]{lang="EN-US" style="font-size:9.0pt"}*[迁移到状态]{style="font-size:9.0pt;font-family:宋体"}*[state2]{lang="EN-US" style="font-size:9.0pt"}*[，共有四种状态：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INITIALIZE]{lang="EN-US"}]{#struct_0_20717_31151_1099453128}[：未解析状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[]{lang="EN-US"}[NO_AGE]{lang="EN-US"}]{#struct_0_20717_31151_x743376294}[：不老化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AGING]{lang="EN-US"}]{#struct_0_20717_31151_1593477555}[：老化处理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AGED]{lang="EN-US"}]{#struct_0_20717_31151_736021696}[：老化待删除状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1747520084}

[[\# Router A]{lang="EN-US"}]{#struct_0_20717_31151_x314109699}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项状态]{style="font-family:宋体"}[调试信息开关，从]{style="font-family:宋体"}[Router A ping Router B]{lang="EN-US"}[，可查看到如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp entry]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x1049230768}

[[\<Sysname\> ping -c 1 192.168.111.188]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x830905712}

[[PING 192.168.111.188 (192.168.111.188): 56 data bytes, press CTRL_C to break]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1403624434}

[[56 bytes from 192.168.111.188: icmp_seq=0 ttl=128 time=1.000 ms]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x988416495}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\-\-- 192.168.111.188 ping statistics \-\--]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1593412019}

[[1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x1594396941}

[[round-trip min/avg/max/std-dev = 1.000/1.000/1.000/0.000 ms]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x379905213}

[[\*Dec 17 14:28:34:762 2012 H3C ARP/7/ARP_ENTRY: -MDC=1; ARP entry status ch]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1723687094}

[[anged: MAC address: 000a-eb83-691e, IP address: 192.168.111.188, INITIALIZE -\> N]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1169145611}

[[O_AGE]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_951818933}

[*[// IP]{lang="EN-US"}*]{#struct_0_20717_31151_1227903819}*[地址为]{style="font-family:宋体"}[192.168.111.188]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项的状态由]{style="font-family:宋体"}[INITIALIZE]{lang="EN-US"}[迁移为]{style="font-family:宋体"}[NO_AGE]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1195931101 .myid}
[]{#_Toc404786009}[]{#struct_0_20717_31151_1742311563}

**ARP \-- ARP调试命令 \-- debugging arp error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1478969195}

[**[debugging arp]{lang="EN-US"}**[ **error**]{lang="EN-US"}]{#struct_0_20717_31151_2027004778}

[**[undo debugging arp]{lang="EN-US"}**[ **error**]{lang="EN-US"}]{#struct_0_20717_31151_1592953264}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_x421529158}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_413407921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1962659754}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_99731973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_x1391301318}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_x2146430840}

[**[debugging arp error]{lang="EN-US"}**]{#struct_0_20717_31151_x769804729}[命令用来打开]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}**[undo debugging arp error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_20717_31151_x239799243}[ARP]{lang="EN-US"}[的错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging arp error]{lang="EN-US"}]{#struct_0_20717_31151_509154031}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_330425621}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_1592887728}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_x843592639}

[[Packet discarded for the network state of receiving interface is down.]{lang="EN-US"}]{#struct_0_20717_31151_x320133128}

[[接收接口网络层状态]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_20717_31151_744906404}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the ARP packet is too short.]{lang="EN-US"}]{#struct_0_20717_31151_x1534568472}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1661435378}[报文长度太短，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the ARP packet is error.]{lang="EN-US"}]{#struct_0_20717_31151_2063309389}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1592822192}[报文错误，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the link state of the port is down.]{lang="EN-US"}]{#struct_0_20717_31151_x29397385}

[[端口链路层状态]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_20717_31151_x1204565834}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the sender IP is invalid.]{lang="EN-US"}]{#struct_0_20717_31151_1530645231}

[[报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x1152201264}[地址无效，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the sender IP is a broadcast IP.]{lang="EN-US"}]{#struct_0_20717_31151_837503161}

[[报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x712910346}[地址为广播]{style="font-family:宋体"}[IP]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the target IP is invaild. ]{lang="EN-US"}]{#struct_0_20717_31151_1592756656}

[[报文请求的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x426557060}[地址无效，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the target IP is a broadcast IP.]{lang="EN-US"}]{#struct_0_20717_31151_1262783648}

[[报文请求的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x2069778112}[地址为广播]{style="font-family:宋体"}[IP]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Failed to get the source MAC of the ARP reply.]{lang="EN-US"}]{#struct_0_20717_31151_x780584069}

[[获取应答报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x581757124}[失败]{style="font-family:宋体"}

[[Packet discarded for the source MAC is a multicast address.]{lang="EN-US"}]{#struct_0_20717_31151_1593215408}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x70142273}[是组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the source MAC is a broadcast address.]{lang="EN-US"}]{#struct_0_20717_31151_4261934}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_74323407}[是广播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the sender MAC address is the same as the receiving interface.]{lang="EN-US"}]{#struct_0_20717_31151_x2005531497}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x195802974}[和接口]{style="font-family:宋体"}[MAC]{lang="EN-US"}[相同，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for the number of ARP entries reaches the limit.]{lang="EN-US"}]{#struct_0_20717_31151_1593149872}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x736674017}[表项数目达到上限，报文被丢弃]{style="font-family:宋体"}

[[Packet discarded for ARP packet is not necessary to concerned.]{lang="EN-US"}]{#struct_0_20717_31151_x1701506967}

[[ARP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_20717_31151_x126001621}[不需要被学习，报文被丢弃]{style="font-size:9.0pt;font-family:宋体"}

[[Packet discarded for the type of receiving interface is L2VE.]{lang="EN-US"}]{#struct_0_20717_31151_x653232879}

[[报文入端口是[L2VE]{lang="EN-US"}口，报文被丢弃]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_1593084336}

[[Packet discarded for conflict with static entry.]{lang="EN-US"}]{#struct_0_20717_31151_x845075685}

[[和静态配置冲突，报文被丢弃]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_x2044480879}

[[sender IP]{lang="EN-US"}]{#struct_0_20717_31151_251380992}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_1593018800}[地址]{style="font-family:宋体"}

[[target IP]{lang="EN-US"}]{#struct_0_20717_31151_1977332692}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_1806573145}[地址]{style="font-family:宋体"}

[[MDC]{lang="EN-US"}]{#struct_0_20717_31151_358395560}

[[逻辑设备号]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_x584469265}

[[Interface]{lang="EN-US"}]{#struct_0_20717_31151_1593477552}

[[接口名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_735694016}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1306129294}

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_1946851462}[开启]{style="font-family:宋体"}[ARP]{lang="EN-US"}[错误调试信息开关，在报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址无效时，调试信息如下]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp error]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x826886289}

[[\*Oct 30 22:44:44:559 2012 Sysname ARP/7/ ARP_ERROR: -MDC=1;     ]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x292742994}

[[Packet discarded for target IP is invalid. Interface: M-E1/0/1  sender IP: 192.168.239.1  target IP : 192.168.239.251]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x1219609317}

[*[//]{lang="EN-US"}*]{#struct_0_20717_31151_x1726907024}*[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址无效，报文被丢弃。接口为]{style="font-family:宋体"}[M-E1/0/1]{lang="EN-US"}[，报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.239.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.239.251]{lang="EN-US"}*

::: {#1497765098 .myid}
[]{#_Toc404786010}[]{#struct_0_20717_31151_1593412016}[]{#_Toc341864676}

**ARP \-- ARP调试命令 \-- debugging arp fast-reply**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1594986765}

[**[debugging arp fast-reply]{lang="EN-US"}**]{#struct_0_20717_31151_1500710302}

[**[undo debugging arp fast-reply]{lang="EN-US"}**]{#struct_0_20717_31151_909386632}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1504747403}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_1036005399}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1054552565}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_106807209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_1157840121}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_x775805941}

[**[debugging arp fast-reply]{lang="EN-US"}**]{#struct_0_20717_31151_1592953265}[命令用来打开]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[快速应答调试信息开关。]{style="font-family:宋体"}**[undo debugging arp fast-reply]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[快速应答调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x421594694}[快速应答调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging arp fast-reply]{lang="EN-US"}]{#struct_0_20717_31151_1238707926}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_326410929}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_1711585003}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_518742610}

[[Src Interface]{lang="EN-US"}]{#struct_0_20717_31151_x2083303384}

[[源]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20717_31151_793365449}[下的端口]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20717_31151_1592887729}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20717_31151_x843527103}

[[SenderMAC]{lang="EN-US"}]{#struct_0_20717_31151_1629669928}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x1077261042}[报文携带的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[SenderIP]{lang="EN-US"}]{#struct_0_20717_31151_x85783427}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x430301026}[地址]{style="font-family:宋体"}

[[TargetMAC]{lang="EN-US"}]{#struct_0_20717_31151_1756392857}

[[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1592822193}[报文携带的目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[TargetIP]{lang="EN-US"}]{#struct_0_20717_31151_x29331849}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_334266613}[地址]{style="font-family:宋体"}

[[SrcEthMAC]{lang="EN-US"}]{#struct_0_20717_31151_1951563765}

[[以太层源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x1058158953}

[[DstEthMAC]{lang="EN-US"}]{#struct_0_20717_31151_x2033711985}

[[以太层目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_1592756657}

[[Packet type]{lang="EN-US"}]{#struct_0_20717_31151_x426622596}

[[报文类型：]{style="font-family:宋体"}]{#struct_0_20717_31151_x343217449}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_20717_31151_x411579999}[：]{style="font-family:宋体"}[ ARP]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REPLY:ARP]{lang="EN-US"}]{#struct_0_20717_31151_x686816572}[：]{style="font-family:宋体"}[应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRATUITOUS]{lang="EN-US"}]{#struct_0_20717_31151_x1942081886}[：]{style="font-family:宋体"}[免费]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Return: TargetIP is same as the local IP address of the VLAN interface.]{lang="EN-US"}]{#struct_0_20717_31151_1593215409}

[[处理结果：收到报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x70207809}[为本地]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的[IP]{lang="EN-US"}地址]{style="font-family:宋体"}

[[Return: Get info from ARP snooping: ]{lang="EN-US"}]{#struct_0_20717_31151_x577727154}

[[VLAN: *vlan-id*, port: *port-name* IP: *ip-address*, MAC: *MAC-address*]{lang="EN-US"}]{#struct_0_20717_31151_x570930773}

[[处理结果：从]{style="font-family:宋体"}[ARP snooping]{lang="EN-US"}]{#struct_0_20717_31151_605684448}[查到代答表项，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"} *[vlan-id]{lang="EN-US"}*[,]{lang="EN-US"}[端口为]{style="font-family:宋体"} *[port-name]{lang="EN-US"}*[ ,IP]{lang="EN-US"}[为]{style="font-family:宋体"} *[ip-address]{lang="EN-US"}*[, MAC]{lang="EN-US"}[为]{style="font-family:宋体"} *[MAC-address]{lang="EN-US"}*

[[Return: Get info from DHCP snooping:]{lang="EN-US"}]{#struct_0_20717_31151_1593149873}

[[ VLAN: *vlan-id*, port: *port-name* IP: *ip-address*, MAC: *MAC-address*]{lang="EN-US"}]{#struct_0_20717_31151_x736608481}

[[处理结果：从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_20717_31151_1762494388}[ ]{lang="EN-US" style="font-family:宋体"}[snooping]{lang="EN-US"}[查到代答表项，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"} *[vlan-id]{lang="EN-US"}*[,]{lang="EN-US"}[端口为]{style="font-family:宋体"} *[port-name]{lang="EN-US"}*[ ,IP]{lang="EN-US"}[为]{style="font-family:宋体"} *[ip-address]{lang="EN-US"}*[, MAC]{lang="EN-US"}[为]{style="font-family:宋体"} *[MAC-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1000593989}

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_x604513284}[在]{style="font-family:宋体"}[VLAN 299]{lang="EN-US"}[下使能快速应答功能。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp fast-reply]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_743341231}

[[\*Aug  7 11:55:26:906 2011 Sysname ARP/7/ARP_FAST_REPLY: -MDC=1-Chassis=1-Slot=3;]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x316677146}

[[Received ARP packet:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1593084337}

[[ Src Interface :GE1/0/2           VLAN ID   :299]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x845010149}

[[ SenderMAC     :000a-eb83-691e    SenderIP  :192.168.20.188]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x1626795930}

[[ TargetMAC     :0000-0000-0000    TargetIP  :192.168.20.120]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_1914223073}

[[ SrcEthMAC     :000a-eb83-691e    DstEthMAC :ffff-ffff-ffff]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_1987553175}

[[ PacketType    :REQUEST]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x1190591953}

[[ Return: TargetIP is the same as the interface VLAN.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x781026951}

::: {#479132572 .myid}
[]{#_Toc404786011}[]{#struct_0_20717_31151_x554685128}

**ARP \-- ARP调试命令 \-- debugging arp packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_1789176769}

[**[debugging arp packet]{lang="EN-US"}**]{#struct_0_20717_31151_1593018801}

[**[undo debugging arp packet]{lang="EN-US"}**]{#struct_0_20717_31151_1977267156}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_201489491}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_115722761}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1496713963}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_1399944808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_418785778}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_x516571440}

[**[debugging arp packet]{lang="EN-US"}**]{#struct_0_20717_31151_x891003418}[命令用来打开]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}**[undo debugging arp packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ARP]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1593477553}[的报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_20717_31151_735628480}[[表1-5 ]{lang="EN-US"}[debugging arp packet]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_319058725}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_1064253661}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_x888426015}

[[ARP_SEND: Send an ARP packet]{lang="EN-US"}]{#struct_0_20717_31151_769338911}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_x1507908271}[报文]{style="font-family:宋体"}

[[ARP_RCV: Receive an ARP packet]{lang="EN-US"}]{#struct_0_20717_31151_2023176538}

[[收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_20717_31151_1767718341}[报文]{style="font-family:宋体"}

[[operation]{lang="EN-US"}]{#struct_0_20717_31151_1593412017}

[[报文类型（]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_20717_31151_x1595052301}[：]{style="font-family:宋体"}[Request]{lang="EN-US"}[报文；]{style="font-family:宋体"}[2]{lang="EN-US"}[：]{style="font-family:宋体"}[Reply]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[sender MAC]{lang="EN-US"}]{#struct_0_20717_31151_1592953262}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x421660230}[地址]{style="font-family:宋体"}

[[sender IP]{lang="EN-US"}]{#struct_0_20717_31151_1592887726}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x843461567}[地址]{style="font-family:宋体"}

[[target MAC]{lang="EN-US"}]{#struct_0_20717_31151_1592756654}

[[目标]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20717_31151_x426688132}[地址]{style="font-family:宋体"}

[[target IP]{lang="EN-US"}]{#struct_0_20717_31151_1593215406}

[[目标]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_20717_31151_x70797633}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1172579587}

[[\# Router A]{lang="EN-US"}]{#struct_0_20717_31151_1593149870}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[相连，打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文调试信息开关，从]{style="font-family:宋体"}[Router A ping Router B]{lang="EN-US"}[，可查看到如下调试信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging arp packet]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x736542945}

[[\<Sysname\> ping -c 1 2.253.253.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_x1689662547}

[[\*Apr 19 16:02:20:832 2006 Sysname ARP/7/ARP_SEND: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1593018798}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:red"}[Sent an ARP message, operation: 1, sender MAC: 0000-0000-0001, sender IP: 2.2.1.1, target MAC: 0000-0000-0000, target IP: 2.253.253.1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_20717_31151_1550889933}*[发送一个]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文，目标]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.253.253.1]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.1.1]{lang="EN-US"}*

[[\*Apr 19 16:02:21:422 2006 Sysname ARP/7/ARP_RCV: -MDC=1; Received an ARP message, operation: 2, sender MAC:00e0-fc5a-ed28, sender IP:2.253.253.1, target MAC: 0000-0000-0001, target IP: 2.2.1.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_20717_31151_1593412014}

[*[// ]{lang="EN-US"}*]{#struct_0_20717_31151_x1595117837}*[收到一个]{style="font-family:宋体"}[ARP]{lang="EN-US"}[应答报文，目标]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.1.1]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.253.253.1]{lang="EN-US"}*

::: {#918894388 .myid}
[]{#_Toc404786012}[]{#struct_0_20717_31151_x837669433}

**ARP \-- ARP调试命令 \-- debugging arp pnp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_x589163761}

[**[debugging arp pnp]{lang="NO-BOK"}**]{#struct_0_20717_31151_x1737895991}

[**[undo debugging arp pnp]{lang="NO-BOK"}**]{#struct_0_20717_31151_x1158005298}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1315847897}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_1591419206}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_892223157}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_x261111227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_x1936747174}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1389918961}

[**[debugging arp pnp]{lang="EN-US"}**]{#struct_0_20717_31151_x837603897}[命令用来打开即插即用网关的调试信息开关。]{style="font-family:宋体"}**[undo debugging arp pnp]{lang="EN-US"}**[命令用来关闭即插即用网关的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，即插即用网关的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_20717_31151_x1772660873}

[[表1-6 ]{lang="EN-US"}[debugging arp pnp]{lang="EN-US"}]{#struct_0_20717_31151_623694706}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_548243456}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_1528273518}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_1255182835}

[[PACKET: (*interface-type* *interface-number-direction*)]{lang="EN-US"}]{#struct_0_20717_31151_x1338557509}

[[报文信息：（接口名]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_20717_31151_356640121}[报文方向）]{style="font-family:宋体"}

[*[OrgSrcIP]{lang="EN-US"}*[  -  *OrgDstIP* \-\-\-\-\--\>]{lang="EN-US"}]{#struct_0_20717_31151_x838193720}

[*[NewSrcIP]{lang="EN-US"}*[  -  *NewDstIP*]{lang="EN-US"}]{#struct_0_20717_31151_2022266537}

[[IP]{lang="EN-US"}]{#struct_0_20717_31151_x161989146}[转换前的报文原始二元组：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgSrcIP]{lang="EN-US"}*]{#struct_0_20717_31151_x801377944}[：原始源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[OrgDstIP]{lang="EN-US"}*]{#struct_0_20717_31151_x838128184}[：原始目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_20717_31151_768902880}[转换后的报文新二元组：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewSrcIP]{lang="EN-US"}*]{#struct_0_20717_31151_645314835}[：新源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NewDstIP]{lang="EN-US"}*]{#struct_0_20717_31151_x1399084026}[：新目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；]{style="font-family:宋体"}

[[The number of ARP PNP entries on the interface *interface-type interface-num* has reached the maximum.]{lang="EN-US"}]{#struct_0_20717_31151_952331235}

[[接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_20717_31151_x838324792}[下的即插即用网关用户表项达到最大数量，报文将被丢弃]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_1234898895}

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_x323110670}[在启用了即插即用网关功能的接口上，打开该设备]{style="font-family:宋体"}[ARP PNP]{lang="EN-US"}[调试信息开关，有]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文通过该接口时输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp pnp]{lang="EN-US"}]{#struct_0_20717_31151_247464144}

[\*Jan 30 17:18:48:610 2012 Sysname ARP/7/ARP_PNP: -MDC=1; ]{lang="EN-US"}

[PACKET: (GigabitEthernet1/0/2-in)]{lang="EN-US"}

[   192.168.1.100  -  2.2.2.100\-\-\-\-\--\>]{lang="EN-US"}

[   2.2.2.254  -  2.2.2.100]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_20717_31151_x1797082063}*[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[收到[IP]{lang="EN-US"}报文进行了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[转换（转换了源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_1377759596}[当用户表项满时会输出下列调试信息。]{style="font-family:宋体"}

[[The number of ARP PNP entries on the interface GigabitEthernet 1/0/2 has reached the maximum.]{lang="EN-US"}]{#struct_0_20717_31151_x744678612}

::: {#-1561870020 .myid}
[]{#_Toc404786013}[]{#struct_0_20717_31151_1497115215}[]{#_Toc341864674}

**ARP \-- ARP调试命令 \-- debugging arp source-mac**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_20717_31151_x467683744}

[**[debugging arp source-mac]{lang="EN-US"}**]{#struct_0_20717_31151_291602267}

[**[undo debugging arp source-mac]{lang="EN-US"}**]{#struct_0_20717_31151_1839206261}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20717_31151_x1918424023}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20717_31151_x1421904843}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20717_31151_1592953263}

[[network-admin]{lang="EN-US"}]{#struct_0_20717_31151_x421725766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20717_31151_1643553704}

[[【描述】]{style="font-family:黑体"}]{#struct_0_20717_31151_x869871977}

[**[debugging arp source-mac]{lang="EN-US"}**]{#struct_0_20717_31151_x1091791264}[命令用来打开源]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测调试信息开关。]{style="font-family:宋体"}**[undo debugging arp source-mac]{lang="EN-US"}**[命令用来关闭源]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，源]{style="font-family:宋体"}]{#struct_0_20717_31151_x1899677131}[MAC]{lang="EN-US"}[地址固定的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging arp source-mac]{lang="EN-US"}]{#struct_0_20717_31151_x183373811}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_345583190}[[字段]{style="font-family:黑体"}]{#struct_0_20717_31151_x1418211345}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20717_31151_1874014790}

[[Failed to add the node MAC: *MAC-address*]{lang="EN-US" style="font-size:
  9.0pt"}[, VLAN:]{lang="EN-US"}]{#struct_0_20717_31151_1592887727}*[ vlan-id]{lang="EN-US" style="font-size:9.0pt"}*[ ]{lang="EN-US"}[because the number of entries reaches the limit.]{lang="EN-US" style="font-size:9.0pt"}

[[表项达到上限，添加节点]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_x843396031}[,]{lang="EN-US" style="font-size:9.0pt"}[ MAC:]{lang="EN-US"}*[ MAC-address]{lang="EN-US" style="font-size:9.0pt"}*[,VLAN:]{lang="EN-US"}*[ vlan-id ]{lang="EN-US" style="font-size:9.0pt"}*[失败]{style="font-size:9.0pt;font-family:宋体"}

[*[Action-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_20717_31151_1267422542}[an entry to ]{lang="EN-US" style="font-size:9.0pt"}[hardware]{lang="EN-US"}[. MAC: *MAC-address.*]{lang="EN-US" style="font-size:9.0pt"}[ VLAN]{lang="EN-US"}[: *vlan-id.* Port:]{lang="EN-US" style="font-size:9.0pt"}[ ]{lang="EN-US"}*[portIfIndex.]{lang="EN-US" style="font-size:9.0pt"}*[ The result is *result.*]{lang="EN-US" style="font-size:9.0pt"}

[[添加表项到驱动的调试信息，动作为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_20717_31151_x1884144518}*[Action-type]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;
  font-family:宋体"}[MAC]{lang="EN-US" style="font-size:9.0pt"}*[为]{style="font-size:9.0pt;font-family:宋体"}*[MAC-address]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-family:宋体"}[端口索引为]{style="font-size:9.0pt;font-family:宋体"}*[portIfIndex]{lang="EN-US" style="font-size:9.0pt"}[。]{style="font-size:9.0pt;
  font-family:宋体"}*[返回值为]{style="font-size:9.0pt;font-family:宋体"}*[result]{lang="EN-US" style="font-size:9.0pt"}*

[*[Action-type:]{lang="EN-US" style="font-size:
  9.0pt"}*[ ]{lang="EN-US"}]{#struct_0_20717_31151_181816994}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_20717_31151_x154061497}[：]{style="font-family:宋体"}[下驱动增加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Del]{lang="EN-US"}]{#struct_0_20717_31151_x1448444671}[：]{style="font-family:宋体"}[下驱动删除]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20717_31151_1592822191}

[[\# ]{lang="EN-US"}]{#struct_0_20717_31151_x29462921}[在系统视图下，]{style="font-family:宋体"}[使能源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[固定]{style="font-family:宋体"}[ARP]{lang="EN-US"}[攻击检测功能，并选择过滤模式。]{style="font-family:宋体"}

[[\<Sysname\> debugging arp source-mac]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_239275251}

[[%Aug  7 11:16:22:466 2011 Sysname ARP/6/ARP SOURCE-MAC: -MDC=1; Failed to add the node MAC: 2c41-3896-9424, VLAN: 2 because the number of entries reaches the limit.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_20717_31151_x652451114}[]{#_Toc237322853}[]{#_Toc237402334}[]{#_Toc237322855}[]{#_Toc237402336}[]{#_Toc237322858}[]{#_Toc237402339}[]{#_Toc237322859}[]{#_Toc237402340}[]{#_Toc237322860}[]{#_Toc237402341}[]{#_Toc237322861}[]{#_Toc237402342}[]{#_Toc237322862}[]{#_Toc237402343}[]{#_Toc237322863}[]{#_Toc237402344}[]{#_Toc237322864}[]{#_Toc237402345}[]{#_Toc237322865}[]{#_Toc237402346}[]{#_Toc237322866}[]{#_Toc237402347}[]{#_Toc237322867}[]{#_Toc237402348}[]{#_Toc237322868}[]{#_Toc237402349}[]{#_Toc237322869}[]{#_Toc237402350}[]{#_Toc237322870}[]{#_Toc237402351}[]{#_Toc237322871}[]{#_Toc237402352}[]{#_Toc237322953}[]{#_Toc237402434}[]{#_Toc237322954}[]{#_Toc237402435}[]{#_Toc237323059}[]{#_Toc237402540}[]{#_Toc237323060}[]{#_Toc237402541}[]{#_Toc237323115}[]{#_Toc237402596}[]{#_Toc237323116}[]{#_Toc237402597}[]{#_Toc237323138}[]{#_Toc237402619}[]{#_Toc237323139}[]{#_Toc237402620}[]{#_Toc237323140}[]{#_Toc237402621}[]{#_Toc237323142}[]{#_Toc237402623}[]{#_Toc237323144}[]{#_Toc237402625}[]{#_Toc237323149}[]{#_Toc237402630}[]{#_Toc237323150}[]{#_Toc237402631}[]{#_Toc237323157}[]{#_Toc237402638}[]{#_Toc237323164}[]{#_Toc237402645}[]{#_Toc237323170}[]{#_Toc237402651}[]{#_Toc237323171}[]{#_Toc237402652}[]{#_Toc237323177}[]{#_Toc237402658}[]{#_Toc237323183}[]{#_Toc237402664}[]{#_Toc237323190}[]{#_Toc237402671}[]{#_Toc237323197}[]{#_Toc237402678}[]{#_Toc237323203}[]{#_Toc237402684}[]{#_Toc237323205}[]{#_Toc237402686}[]{#_Toc237323207}[]{#_Toc237402688}[]{#_Toc237323208}[]{#_Toc237402689}[]{#_Toc237323209}[]{#_Toc237402690}[]{#_Toc237323211}[]{#_Toc237402692}[]{#_Toc237323213}[]{#_Toc237402694}[]{#_Toc237323219}[]{#_Toc237402700}[]{#_Toc237323221}[]{#_Toc237402702}[]{#_Toc237323223}[]{#_Toc237402704}[]{#_Toc237323224}[]{#_Toc237402705}[]{#_Toc237323232}[]{#_Toc237402713}[]{#_Toc237323241}[]{#_Toc237402722}[]{#_Toc237323250}[]{#_Toc237402731}[]{#_Toc237323259}[]{#_Toc237402740}[]{#_Toc237323268}[]{#_Toc237402749}[]{#_Toc237323275}[]{#_Toc237402756}[]{#_Toc237323276}[]{#_Toc237402757}
