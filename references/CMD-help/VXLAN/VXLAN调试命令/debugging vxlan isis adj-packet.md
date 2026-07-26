::: {#-1577855922 .myid}
[]{#_Toc404798458}[]{#struct_0_13426_x3709_186435003}[]{#_Toc389037836}[]{#_Toc373940586}[]{#_Toc372115297}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis adj-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_186435000}

[**[debugging vxlan isis adj-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_186435001}

[**[undo]{lang="EN-US"}**[ **debugging vxlan isis adj-packet** \[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_2142750144}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1271281466}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2142750145}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1271215930}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_2142750142}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_2142750143}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2142750140}

[**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_2142750141}[：]{style="font-family:宋体"}[表示接收]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_13426_x3709_1271478074}[：]{style="font-family:宋体"}[表示发送]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_13426_x3709_2142750138}[：表示详细调试信息，即打印报文的内容。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2142750139}

[**[debugging vxlan isis adj-packet]{lang="EN-US"}**]{#struct_0_13426_x3709_1272002359}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[vxlan isis adj-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_2142750136}[的邻居报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果未指定]{style="font-family:宋体"}**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_2142750137}[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则表示接收和发送]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging vxlan isis adj-packet]{lang="EN-US"}]{#struct_0_13426_x3709_1271346999}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1473018254}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x195902015}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x195902018}

[[IIH discarded: *String* error.]{lang="EN-US"}]{#struct_0_13426_x3709_x195902020}

[[收到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_13426_x3709_x195902019}[报文解析]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时发生错误。]{style="font-family:宋体"}*[String]{lang="EN-US"}*[为错误原因，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[protocol support TLV decode]{lang="EN-US"}]{#struct_0_13426_x3709_x195902021}[：协议支持]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[area address TLV decode]{lang="EN-US"}]{#struct_0_13426_x3709_x195902024}[：区域地址]{lang="EN-US" style="font-family:宋体"}[TLV]{lang="EN-US"}[解码错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[neighbor TLV decode]{lang="EN-US"}]{#struct_0_13426_x3709_1760413120}[：邻居]{lang="EN-US" style="font-family:
  宋体"}[TLV]{lang="EN-US"}[解码错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[system]{lang="EN-US"}]{#struct_0_13426_x3709_1760413121}[：系统错误]{lang="EN-US" style="font-family:宋体"}

[[IIH contained *String* that is not supported by the interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_1760413119}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_13426_x3709_1760413116}[报文的特征与接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[的特征不匹配。]{style="font-family:宋体"}*[String]{lang="EN-US"}*[为]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文与接口不匹配的特征，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PDU type(Level-]{lang="EN-US"}]{#struct_0_13426_x3709_1760413114}*[number]{lang="EN-US"}*[)]{lang="EN-US"}[：]{style="font-family:宋体"}[Level-*number*]{lang="EN-US"}[的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[supported ]{lang="EN-US"}[protocol]{lang="EN-US"}]{#struct_0_13426_x3709_1760413112}[：支持的协议]{style="font-family:宋体"}

[[Neighbor entry set to down state: IIH contains the same SNPA as the entry, but their system IDs are different.]{lang="EN-US"}]{#struct_0_13426_x3709_951109056}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_13426_x3709_951109054}[报文与已有邻居有相同的]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[地址，但是系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[不同，将这个邻居置]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IIH discarded: The packet has the same System ID as a neighbor entry, but their SNPAs are different.]{lang="EN-US"}]{#struct_0_13426_x3709_951109055}

[[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_13426_x3709_951109053}[报文与已有邻居有相同的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[，但是]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[地址不同，丢弃该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Level-*Number* neighbor(*Address*)\'s two-way check *String*.]{lang="EN-US"}]{#struct_0_13426_x3709_951109050}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_951109048}[的邻居]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[检查结果为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[。]{style="font-family:宋体"}*[Address]{lang="EN-US"}*[表示邻居的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543104}[ed]{lang="EN-US"}[：通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543103}[ed]{lang="EN-US"}[：不通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[was pending]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543105}[：邻居信息没有收集完整，需要继续等待]{style="font-family:宋体"}

[[ADJ discarded packet: The system was in disabled state.]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543107}

[[系统处于去使能状态，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543109}[模块收到的报文]{style="font-family:宋体"}

[[ADJ discarded packet: The interface was not up.]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543111}

[[接口处于非]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_13426_x3709_188597696}[状态，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块收到的报文]{style="font-family:宋体"}

[[ADJ discarded packet: The packet was sent by the local device.]{lang="EN-US"}]{#struct_0_13426_x3709_188597694}

[[收到的是本设备自己的报文，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_13426_x3709_188597695}[模块收到的报文]{style="font-family:宋体"}

[*[String]{lang="EN-US"}*[ sent LAN L1 IIH on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_188597693}

[[边缘设备在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_188597691}[上发送了]{style="font-family:宋体"}[LAN L1 Hello]{lang="EN-US"}[类型报文，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ED]{lang="EN-US"}]{#struct_0_13426_x3709_188597688}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DED]{lang="EN-US"}]{#struct_0_13426_x3709_2144912832}

[[Received LAN L1 IIH from *Address* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912830}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_2144912828}[上从地址]{style="font-family:宋体"}*[Address]{lang="EN-US"}*[收到了]{style="font-family:宋体"}[LAN L1 Hello]{lang="EN-US"}[类型报文]{style="font-family:宋体"}

[[ADJ discarded packet: PDU type *Number* not supported.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912827}

[[收到了不支持的报文，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_13426_x3709_2144912825}[模块收到的报文，]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[为报文的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型值]{style="font-family:宋体"}

[[Not enough PDU space for area address TLV.]{lang="EN-US"}]{#struct_0_13426_x3709_x193739328}

[[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_x193739329}[长度已经达到最大值，没有空间保存区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1653994281}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x193739332}[打开接收]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[邻居报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis adj-packet receive]{lang="EN-US"}]{#struct_0_13426_x3709_x193739331}

[\*Feb 24 19:12:29:731 2014 SwitchB OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-ADJ: Received LAN L1 IIH from 0011-2200-0001 on interface Tunnel500.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x1653469992}*[从接口]{style="font-family:宋体"}[Tunnel500]{lang="EN-US"}[上接收到地址为]{style="font-family:宋体"}[0011-2200-0001]{lang="EN-US"}[的邻居发送的]{style="font-family:宋体"}[LAN L1 Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Feb 24 19:12:29:732 2014 SwitchB OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_13426_x3709_x193739334}

[OVERLAYISIS-0-ADJ: Level-1 neighbor (0011.2200.0001)\'s two-way check passed.]{lang="EN-US"}

[*[// L1]{lang="EN-US"}*]{#struct_0_13426_x3709_x1653142312}*[邻居]{style="font-family:宋体"}[0011.2200.0001]{lang="EN-US"}[通过]{style="font-family:宋体"}[Two-way]{lang="EN-US"}[检查。]{style="font-family:宋体"}*

::: {#1647142261 .myid}
[]{#_Toc404798459}[]{#struct_0_13426_x3709_x193739333}[]{#_Toc389037837}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x193739336}

[**[debugging vxlan isis all]{lang="EN-US"}**]{#struct_0_13426_x3709_x1653273384}

[**[undo debugging vxlan isis all]{lang="EN-US"}**]{#struct_0_13426_x3709_x193739335}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575808}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_1744738863}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575809}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_1744673327}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_1762575806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575807}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_1745066543}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575804}

[**[debugging vxlan isis all]{lang="EN-US"}**]{#struct_0_13426_x3709_1745001007}[命令用来打开所有与]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[相关的调试信息开关。]{style="font-family:
宋体"}**[undo debugging vxlan isis all]{lang="EN-US"}**[命令用来关闭所有与]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[相关的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有与]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_1762575805}[相关的调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575802}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1745394223}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis all]{lang="EN-US"}]{#struct_0_13426_x3709_1762575803}
:::

::: {#838744018 .myid}
[]{#_Toc404798460}[]{#struct_0_13426_x3709_1745328687}[]{#_Toc389037838}[]{#_Toc373940588}[]{#_Toc372115299}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1762575800}

[**[debugging vxlan isis error]{lang="EN-US"}**]{#struct_0_13426_x3709_1762575801}

[**[undo debugging vxlan isis error]{lang="EN-US"}**]{#struct_0_13426_x3709_1745197615}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_953271744}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_953271745}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x117975797}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_953271742}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_953271743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x117975795}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_953271740}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_953271741}

[**[debugging vxlan isis]{lang="EN-US"}[ error]{lang="EN-US"}**]{#struct_0_13426_x3709_x117975793}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan isis]{lang="EN-US"}[ error]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_953271738}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging vxlan isis error]{lang="EN-US"}]{#struct_0_13426_x3709_x927279864}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1355606619}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_953271736}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_953271737}

[[Failed to get local MAC addresses of VXLAN *Number*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380415}

[[获取]{style="font-family:宋体"}[VXLAN *Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380418}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to add remote MAC address *mac-address* to VXLAN *number*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380420}

[[在]{style="font-family:宋体"}[VXLAN *number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380419}[中添加远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to create local MAC attribute.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380421}

[[创建本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380424}[地址属性失败]{style="font-family:宋体"}

[[Failed to notify the DEC module to handle local MAC conflict.]{lang="EN-US"}]{#struct_0_13426_x3709_169133473}

[[通知]{style="font-family:宋体"}[DEC]{lang="EN-US"}]{#struct_0_13426_x3709_169133472}[模块（路由维护模块）处理本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址冲突失败]{style="font-family:宋体"}

[[LAN ADJ data reached the limit.]{lang="EN-US"}]{#struct_0_13426_x3709_169133470}

[[LAN ADJ]{lang="EN-US"}]{#struct_0_13426_x3709_169133469}[数据已达最大值]{style="font-family:宋体"}

[[Failed to get ADJ pointer when starting hello timer.]{lang="EN-US"}]{#struct_0_13426_x3709_171296159}

[[当启动]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_13426_x3709_171296154}[定时间器时，获取]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[维护数据失败]{style="font-family:宋体"}

[[Failed to start level-*Number* hello timer. ]{lang="EN-US"}]{#struct_0_13426_x3709_171296152}

[[启动]{style="font-family:宋体"}[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_2127611296}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to start hold timer.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611295}

[[启动]{style="font-family:宋体"}[Hold]{lang="EN-US"}]{#struct_0_13426_x3709_2127611293}[定时器失败]{style="font-family:宋体"}

[[Failed to get system\'s area address when encoding area address TLV.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611291}

[[编码区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_13426_x3709_2127611289}[时获取区域地址失败]{style="font-family:宋体"}

[[Failed to get interface *interface-name*\'s MTU.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611288}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x211040864}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send IIH on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x211040866}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x211040867}[上发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to create hello timer on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x211040869}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x211040871}[上创建]{style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to process interface MTU change event.]{lang="EN-US"}]{#struct_0_13426_x3709_1745274273}

[[处理接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_13426_x3709_1745274272}[变化事件失败]{style="font-family:宋体"}

[[Failed to activate interface *interface-index*.]{lang="EN-US"}]{#struct_0_13426_x3709_1745274270}

[[激活接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_13426_x3709_1745274268}[失败]{style="font-family:宋体"}

[[Error occurred when sending notification that interface *interface-index* was removed.]{lang="EN-US"}]{#struct_0_13426_x3709_1745274267}

[[通知接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_13426_x3709_1745274265}[删除事件错误]{style="font-family:宋体"}

[[Invalid startup phase *phase-number*. Event ignored.]{lang="EN-US"}]{#struct_0_13426_x3709_935970209}

[[无效的重启阶段，忽略该事件，]{style="font-family:宋体"}*[phase-number]{lang="EN-US"}*]{#struct_0_13426_x3709_935970207}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_13426_x3709_935970205}[：表示系统处于非重启阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_935970203}[：表示系统处于重启停止阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_935970201}[：表示系统处于重启清除数据阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681951}[：表示系统处于清除数据后的后续处理阶段]{style="font-family:宋体"}

[[Failed to create LSP change notification message.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681953}

[[创建]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681956}[变化通知消息失败]{style="font-family:宋体"}

[[PDU\'s level(1) did not match the interface\'s level (*CirLevel*) setting.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681958}

[[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681960}[报文中的]{style="font-family:宋体"}[level]{lang="EN-US"}[（]{style="font-family:宋体"}[1]{lang="EN-US"}[）与接口]{style="font-family:宋体"}[level]{lang="EN-US"}[（]{style="font-family:宋体"}*[CirLevel]{lang="EN-US"}*[）不匹配]{style="font-family:宋体"}

[[Failed to set UPDT socket option.]{lang="EN-US"}]{#struct_0_13426_x3709_164808096}

[[设置]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_13426_x3709_164808093}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项失败]{style="font-family:宋体"}

[[Failed to start *Type* timer on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_164808091}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_164808089}[上启动定时器失败。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[为定时器类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_2121123233}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_2121123231}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2121123230}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP flooding]{lang="EN-US"}]{#struct_0_13426_x3709_2121123227}

[[Failed to stop LSP flooding timer on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_2121123226}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_2121123224}[上停止]{style="font-family:宋体"}[LSP]{lang="EN-US"}[泛洪定时器失败]{style="font-family:宋体"}

[[Failed to stop level-1 timer on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x217528929}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x217528931}[上停止]{style="font-family:宋体"}[Lever-1]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to add MAC address to list.]{lang="EN-US"}]{#struct_0_13426_x3709_x217528934}

[[向链表中添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_x217528936}[地址失败]{style="font-family:宋体"}

[[Failed to update LSP information.]{lang="EN-US"}]{#struct_0_13426_x3709_1738786207}

[[更新]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_1738786205}[信息失败]{style="font-family:宋体"}

[[Failed to add LSP information.]{lang="EN-US"}]{#struct_0_13426_x3709_1738786202}

[[添加]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_1738786200}[信息失败]{style="font-family:宋体"}

[[PDU ignored: Interface *interface-name* was not operational.]{lang="EN-US"}]{#struct_0_13426_x3709_929482143}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_929482141}[处于不可操作状态，忽略]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Failed to obtain interface index.]{lang="EN-US"}]{#struct_0_13426_x3709_929482139}

[[获取接口索引失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_929482138}

[[Failed to send packet: transmit buffer length=*Length*, return length=*ReturnLength*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1409170015}

[[发送报文失败，发送缓冲区大小为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*]{#struct_0_13426_x3709_x1409170018}[，返回值为]{style="font-family:宋体"}*[ReturnLength]{lang="EN-US"}*

[[LSP size *LspSize* exceeded interface\'s MTU size (*CirMtu*).]{lang="EN-US"}]{#struct_0_13426_x3709_x1409170020}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1409170023}[的大小]{style="font-family:宋体"}*[LspSize]{lang="EN-US"}*[大于接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}*[CirMtu]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to send LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_166970785}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_166970784}[报文失败]{style="font-family:宋体"}

[[Failed to send level-*Number Type* packet.]{lang="EN-US"}]{#struct_0_13426_x3709_166970781}

[[发送]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_166970779}[的]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[类型报文失败，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_166970777}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_2123285921}

[[Failed to install LSP with sequence number 0.]{lang="EN-US"}]{#struct_0_13426_x3709_2123285918}

[[安装序号为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13426_x3709_2123285915}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to *Type* level-*Number* area address *address*.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366241}

[[操作]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x215366243}[区域地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[失败，操作类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_13426_x3709_x215366246}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_1740948897}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Failed to *Type* level-*Number* supported protocol *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_13426_x3709_1740948894}

[[操作]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_1740948892}[的支持的协议类型]{style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[（]{style="font-family:宋体"}*[ProString]{lang="EN-US"}*[）失败，操作类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*

[*[ProString]{lang="EN-US"}*]{#struct_0_13426_x3709_1740948890}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OVERLAY]{lang="EN-US"}[-ISIS]{lang="EN-US"}]{#struct_0_13426_x3709_931644833}[：]{style="font-family:宋体"}[OVERLAY ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown]{lang="EN-US"}]{#struct_0_13426_x3709_931644831}[：]{style="font-family:宋体"}[其它协议]{lang="EN-US" style="font-family:宋体"}

[*[Type]{lang="EN-US"}*]{#struct_0_13426_x3709_931644828}[的具体取值可以如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_13426_x3709_931644826}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_931644824}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Failed to add level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007329}

[[添加]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007331}[由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息失败]{style="font-family:宋体"}

[[Failed to delete level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007333}

[[删除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007336}[由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息失败]{style="font-family:宋体"}

[[Failed to modify level-*Number*  neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_177784224}

[[更新]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_177784222}[由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息失败]{style="font-family:宋体"}

[[Failed to add level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_177784220}

[[添加]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_2136262040}[由]{style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的伪节点邻居信息失败]{style="font-family:宋体"}

[[Failed to delete level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID.*]{lang="EN-US"}]{#struct_0_13426_x3709_x202390113}

[[删除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x202390116}[由]{style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的伪节点邻居信息失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x202390117}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1899098370}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis error]{lang="EN-US"}]{#struct_0_13426_x3709_x202390118}

[\*Mar 18 14:28:41:744 2013 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-ERR: Failed to send level-1 CSNP PDU.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x202390119}*[发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文失败。]{style="font-family:宋体"}*

::: {#2062355005 .myid}
[]{#_Toc404798461}[]{#struct_0_13426_x3709_x202390120}[]{#_Toc389037839}[]{#_Toc373940589}[]{#_Toc372115300}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1898901763}

[**[debugging vxlan isis event]{lang="EN-US"}**]{#struct_0_13426_x3709_1753925025}

[**[undo debugging vxlan isis event]{lang="EN-US"}**]{#struct_0_13426_x3709_1753925024}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x155919132}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_1753925023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1753925022}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_1753925021}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_1753925020}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x156181276}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_1753925019}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1753925018}

[**[debugging vxlan isis event]{lang="EN-US"}**]{#struct_0_13426_x3709_1753925017}[命令用来打开]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:
宋体"}**[undo debugging vxlan isis event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x155984671}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging vxlan isis event]{lang="EN-US"}]{#struct_0_13426_x3709_1753925016}[命令输出的信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1302940994}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_944620961}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_944620959}

[[DED changed on *interface-name*: old DED=*old-ded-mac*, new DED=*new-ded-mac*.]{lang="EN-US"}]{#struct_0_13426_x3709_944620958}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_944620957}[所属网段的]{style="font-family:宋体"}[DED]{lang="EN-US"}[发生改变，原来的]{style="font-family:宋体"}[DED]{lang="EN-US"}[为]{style="font-family:宋体"}*[old-ded-mac]{lang="EN-US"}*[，新的]{style="font-family:宋体"}[DED]{lang="EN-US"}[为]{style="font-family:宋体"}*[new-ded-mac]{lang="EN-US"}*

[[System was in disabled state.]{lang="EN-US"}]{#struct_0_13426_x3709_944620955}

[[系统处于去使能状态]{style="font-family:宋体"}]{#struct_0_13426_x3709_944620954}

[[Main thread notified other threads of tunnel interface status change.]{lang="EN-US"}]{#struct_0_13426_x3709_944620952}

[[主线程通知其他线程]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031199}[接口状态改变]{style="font-family:宋体"}

[[Refreshed interface parameters on interface *interface-index*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031201}

[[刷新]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031202}[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[下保存的接口的各种参数]{style="font-family:宋体"}

[[Interface *interface-name* created successfully.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031203}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1394031205}[创建成功]{style="font-family:宋体"}

[[Interface *interface-name* deleted successfully.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031207}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1394031208}[删除成功]{style="font-family:宋体"}

[[Notified UPDT thread that LSP MTU size changed from *value1* to *value2*.]{lang="EN-US"}]{#struct_0_13426_x3709_173458848}

[[通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_13426_x3709_173458847}[线程]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文发送的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大小由]{style="font-family:宋体"}*[value1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[value2]{lang="EN-US"}*

[[Received interface delete acknowledge event. Flag: *bDel*.]{lang="EN-US"}]{#struct_0_13426_x3709_173458845}

[[收到一个删除接口应答事件，标志为]{style="font-family:宋体"}*[bDel]{lang="EN-US"}*]{#struct_0_13426_x3709_173458844}

[[Reset finished: reason code=*reason-code.*]{lang="EN-US"}]{#struct_0_13426_x3709_173458842}

[*[reason-code]{lang="EN-US"}*]{#struct_0_13426_x3709_173458841}[引起的复位完成。]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[为原因码，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_2129773985}[：]{lang="EN-US" style="font-family:宋体"}**[reset ]{lang="EN-US"}[vxlan]{lang="EN-US"}[ isis]{lang="EN-US"}**[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_2129773983}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_2129773981}[：]{lang="EN-US" style="font-family:宋体"}[VXLAN ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_13426_x3709_2129773980}[：协议进程降级引起的复位]{style="font-family:宋体"}

[[Received *string* on interface *interface-index.*]{lang="EN-US"}]{#struct_0_13426_x3709_2129773978}

[[在接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_13426_x3709_2129773976}[上收到如下事件：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface active event]{lang="EN-US"}]{#struct_0_13426_x3709_x208878176}[：接口激活事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface deactive event]{lang="EN-US"}]{#struct_0_13426_x3709_x208878178}[：接口去激活事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface ]{lang="EN-US"}]{#struct_0_13426_x3709_x208878180}[create ]{lang="EN-US"}[event]{lang="EN-US"}[：接口]{lang="EN-US" style="font-family:宋体"}[创建]{style="font-family:宋体"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface delete event]{lang="EN-US"}]{#struct_0_13426_x3709_x208878183}[：接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN \--\> UP event]{lang="EN-US"}]{#struct_0_13426_x3709_1747436961}[：接口]{lang="EN-US" style="font-family:
  宋体"}[UP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP \--\> DOWN event]{lang="EN-US"}]{#struct_0_13426_x3709_1747436959}[：接口]{lang="EN-US" style="font-family:
  宋体"}[DOWN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[speed change event]{lang="EN-US"}]{#struct_0_13426_x3709_1747436958}[：接口速率变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU change event]{lang="EN-US"}]{#struct_0_13426_x3709_1747436956}[：]{lang="EN-US" style="font-family:
  宋体"}[MTU]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[Reset entered phase *phase-code*.]{lang="EN-US"}]{#struct_0_13426_x3709_1747436954}

[[复位进入]{style="font-family:宋体"}*[phase-code]{lang="EN-US"}*]{#struct_0_13426_x3709_1747436952}[阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_938132896}[：]{lang="EN-US" style="font-family:宋体"}[表示重启停止阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_938132895}[：表示重启清除数据阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_938132893}[：表示清除数据后的后续处理阶段]{style="font-family:宋体"}

[[Processed reset event reply: sender module ID=*module-number*, event ID=*event-number*, reset phase code=*phase-code*.]{lang="EN-US"}]{#struct_0_13426_x3709_938132891}

[[处理模块]{style="font-family:宋体"}*[module-number]{lang="EN-US"}*]{#struct_0_13426_x3709_938132889}[回复的]{style="font-family:宋体"}[reset]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event-number]{lang="EN-US"}*[，当前重启阶段为]{style="font-family:宋体"}*[phase-code]{lang="EN-US"}*

[*[module-number]{lang="EN-US"}*]{#struct_0_13426_x3709_938132888}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_x1400519264}[：]{lang="EN-US" style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_x1400519265}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_x1400519267}[：]{lang="EN-US" style="font-family:宋体"}[DEC]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_x1400519269}[：]{style="font-family:宋体"}[DATA]{lang="EN-US"}[模块]{style="font-family:宋体"}

[*[event-number]{lang="EN-US"}*]{#struct_0_13426_x3709_x1400519270}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_x1400519272}[：]{lang="EN-US" style="font-family:宋体"}[停止工作事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_175621536}[：]{lang="EN-US" style="font-family:宋体"}[清除数据事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_175621535}[：]{lang="EN-US" style="font-family:宋体"}[重启恢复事件]{style="font-family:宋体"}

[*[phase-code]{lang="EN-US"}*]{#struct_0_13426_x3709_175621533}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_175621530}[：]{lang="EN-US" style="font-family:宋体"}[重启停止阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_175621528}[：]{lang="EN-US" style="font-family:宋体"}[重启清除数据阶段]{style="font-family:宋体"}

[[Reset processing module received reset event *event-type*.]{lang="EN-US"}]{#struct_0_13426_x3709_2131936671}

[[复位处理模块收到复位事件]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_13426_x3709_2131936668}[。]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_2131936666}[：]{lang="EN-US" style="font-family:宋体"}**[reset ]{lang="EN-US"}[vxlan isis]{lang="EN-US"}**[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_2131936664}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_x206715488}[：]{lang="EN-US" style="font-family:宋体"}[VXLAN ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_13426_x3709_x206715490}[：协议进程降级引起的复位]{style="font-family:宋体"}

[[Reset started.]{lang="EN-US"}]{#struct_0_13426_x3709_x206715491}

[[复位开始]{style="font-family:宋体"}]{#struct_0_13426_x3709_x206715493}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x206715494}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x206715495}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis event]{lang="EN-US"}]{#struct_0_13426_x3709_x206715496}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-EVT: Main thread notified other threads of tunnel interface status change.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_1749599649}*[主线程通知其他线程]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口状态改变。]{style="font-family:宋体"}*

::: {#-1475078459 .myid}
[]{#_Toc404798462}[]{#struct_0_13426_x3709_x1144496991}[]{#_Toc389037840}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis graceful-restart**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1749599648}

[**[debugging vxlan isis graceful-restart]{lang="EN-US"}**]{#struct_0_13426_x3709_1749599647}

[**[undo debugging vxlan isis graceful-restart]{lang="EN-US"}**]{#struct_0_13426_x3709_1749599646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1143776095}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_1749599645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1749599644}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_1749599643}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_1749599642}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1144038239}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_1749599641}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1749599640}

[**[debugging vxlan isis graceful-restart]{lang="EN-US"}**]{#struct_0_13426_x3709_940295585}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的平滑重启调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan isis graceful-restart]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的平滑重启调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_940295584}[的平滑重启调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging vxlan isis graceful-restart]{lang="EN-US"}]{#struct_0_13426_x3709_940295583}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x932013366}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_940295581}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_940295580}

[[Graceful restart completed.]{lang="EN-US"}]{#struct_0_13426_x3709_940295578}

[[平滑重启完成]{style="font-family:宋体"}]{#struct_0_13426_x3709_940295577}

[[T3 timer stopped.]{lang="EN-US"}]{#struct_0_13426_x3709_940295576}

[[T3]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356576}[定时器停止]{style="font-family:宋体"}

[[T3 timer expired before T2 timer.]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356578}

[[T3]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356579}[定时器在]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器之前失效]{style="font-family:宋体"}

[[Level-*Number* T2 timer expired.]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356581}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356583}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器失效]{style="font-family:宋体"}

[[Graceful restart entered *Type* phase.]{lang="EN-US"}]{#struct_0_13426_x3709_186434977}

[[平滑重启进入]{style="font-family:宋体"}*[Type]{lang="EN-US"}*]{#struct_0_13426_x3709_186434975}[阶段，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[指示了类型可以取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting]{lang="EN-US"}]{#struct_0_13426_x3709_186434974}[：启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[restarting]{lang="EN-US"}]{#struct_0_13426_x3709_186434973}[：重启]{lang="EN-US" style="font-family:宋体"}

[[Received T2 timer cancel event.]{lang="EN-US"}]{#struct_0_13426_x3709_186434971}

[[收到]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_13426_x3709_186434970}[定时器取消事件]{style="font-family:宋体"}

[[Level-*Number* T2 timer stopped.]{lang="EN-US"}]{#struct_0_13426_x3709_186434969}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_2144912799}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}

[[Received module\'s GR phase: module=Mid, module\'s phase=*Phase,* system\'s current GR phase=*GrPhase*.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912797}

[[收到模块]{style="font-family:宋体"}*[Mid]{lang="EN-US"}*]{#struct_0_13426_x3709_2144912795}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态]{style="font-family:宋体"}*[Phase]{lang="EN-US"}*[，当前]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态是]{style="font-family:宋体"}*[GrPhase]{lang="EN-US"}*

[[正常情况下模块的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_13426_x3709_2144912793}[与系统的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态应当一致，否则视为异常]{style="font-family:宋体"}

[*[Mid]{lang="EN-US"}*]{#struct_0_13426_x3709_x193739359}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_13426_x3709_x193739361}[：主模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_x193739362}[：]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_x193739364}[：]{style="font-family:宋体"}[Update]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_x193739366}[：]{style="font-family:宋体"}[DEC]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_x193739367}[：]{style="font-family:宋体"}[DATA]{lang="EN-US"}[模块]{style="font-family:宋体"}

[*[Phase]{lang="EN-US"}*]{#struct_0_13426_x3709_1762575777}[和]{style="font-family:宋体"}*[GrPhase]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_13426_x3709_1762575776}[：初始阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_1762575774}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_1762575773}[：路由计算阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_1762575771}[：接收本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址上报的阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_1762575769}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_13426_x3709_1762575768}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新和泛洪的阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_953271712}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[完成的阶段]{lang="EN-US" style="font-family:宋体"}

[[Stopped level-*Number* T1 timer.]{lang="EN-US"}]{#struct_0_13426_x3709_953271711}

[[停止]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_953271709}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[Interface *interface-name* received level-*Number* IIH with *Type* bit set.]{lang="EN-US"}]{#struct_0_13426_x3709_953271707}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_953271705}[收到]{style="font-family:宋体"}[level-*Number* hello]{lang="EN-US"}[报文，报文中的]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[位置位，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[位取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RR]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380448}[：重启请求位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RA]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380449}[：重启抑制位]{lang="EN-US" style="font-family:宋体"}

[[Failed to purge level-*Number* LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380451}

[[清除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380452}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Started purging local level-*Number* LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380454}

[[开始清除本地的]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380455}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Purged level-*Number* LSP *PseudoId*-*FragNum*.]{lang="EN-US"}]{#struct_0_13426_x3709_169133538}

[[清除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_169133540}[的]{style="font-family:宋体"}[LSP *PseudoId*-*FragNum*]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Finished purging local level-*Number* LSPs.]{lang="EN-US"}]{#struct_0_13426_x3709_169133542}

[[结束清除本地的]{style="font-family:宋体"}[level-*Number* LSP]{lang="EN-US"}]{#struct_0_13426_x3709_169133544}[报文]{style="font-family:宋体"}

[[Level-*Number* LSDB synchronization completed.]{lang="EN-US"}]{#struct_0_13426_x3709_169133545}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_169133547}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[Level-*Number* CSNP setting synchronization completed on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_2125448675}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_2125448677}[上]{style="font-family:宋体"}[Level-*Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[设置同步完成]{style="font-family:宋体"}

[[Level-*Number* LSDB synchronization completed.]{lang="EN-US"}]{#struct_0_13426_x3709_2125448679}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_2125448682}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[Level-*Number* T1 timer expired *Number* times on interface *interface-index*]{lang="EN-US"}]{#struct_0_13426_x3709_x213203486}

[[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_13426_x3709_x213203484}[下，]{style="font-family:宋体"}[Level-*Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1459194846}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x213203483}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的平滑重启]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis graceful-restart]{lang="EN-US"}]{#struct_0_13426_x3709_x213203482}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-GR: Level-1 LSDB synchronization completed.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_13426_x3709_x1459325918}*[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成。]{style="font-family:宋体"}*

::: {#-1480217476 .myid}
[]{#_Toc404798463}[]{#struct_0_13426_x3709_x213203481}[]{#_Toc389037841}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis ha**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1459522526}

[**[debugging vxlan isis ha]{lang="EN-US"}**]{#struct_0_13426_x3709_683465896}

[**[undo debugging vxlan isis ha]{lang="EN-US"}**]{#struct_0_13426_x3709_x213203480}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x213203479}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_x213203478}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1459981277}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x213203477}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_1743111650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1743111651}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_1743111652}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1886537644}

[**[debugging vxlan isis ha]{lang="EN-US"}**]{#struct_0_13426_x3709_1743111653}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan isis ha]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:
宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_1743111654}[的]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关处于关闭状态]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging vxlan isis ha]{lang="EN-US"}]{#struct_0_13426_x3709_1743111655}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1059216783}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1743111657}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1743111659}

[[Received HA *event* event.]{lang="EN-US"}]{#struct_0_13426_x3709_933807586}

[[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_933807588}[通知事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EPOLLUP]{lang="EN-US"}]{#struct_0_13426_x3709_933807589}[：]{lang="EN-US" style="font-family:宋体"}[epoll]{lang="EN-US"}[挂起]{style="font-family:宋体"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch backup]{lang="EN-US"}]{#struct_0_13426_x3709_933807590}[：批量备份事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_13426_x3709_933807592}[：进程停止事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[degrade]{lang="EN-US"}]{#struct_0_13426_x3709_933807593}[：降级事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[upgrade]{lang="EN-US"}]{#struct_0_13426_x3709_933807594}[：升级事件]{lang="EN-US" style="font-family:宋体"}

[[Received real-time backup data.]{lang="EN-US"}]{#struct_0_13426_x3709_x1404844574}

[[收到实备数据]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1404844573}

[[Received batch backup data.]{lang="EN-US"}]{#struct_0_13426_x3709_x1404844572}

[[收到批量备份数据]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1404844570}

[[Notified thread to stop work.]{lang="EN-US"}]{#struct_0_13426_x3709_x1404844569}

[[通知线程停止工作]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1404844567}

[[Processed HA upgrade.]{lang="EN-US"}]{#struct_0_13426_x3709_x1404844565}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_171296226}[升级事件]{style="font-family:宋体"}

[[HA smooth ended.]{lang="EN-US"}]{#struct_0_13426_x3709_171296227}

[[HA]{lang="EN-US"}]{#struct_0_13426_x3709_171296229}[平滑结束]{style="font-family:宋体"}

[[HA smooth started.]{lang="EN-US"}]{#struct_0_13426_x3709_171296230}

[[HA]{lang="EN-US"}]{#struct_0_13426_x3709_171296232}[平滑开始]{style="font-family:宋体"}

[[No process found. HA smooth ended.]{lang="EN-US"}]{#struct_0_13426_x3709_171296233}

[[不存在任何进程，]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_171296235}[平滑结束]{style="font-family:宋体"}

[[External initialization for HA.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611362}

[[HA]{lang="EN-US"}]{#struct_0_13426_x3709_2127611364}[时进行外部初始化]{style="font-family:宋体"}

[[Notified thread to start work.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611366}

[[通知线程开始工作]{style="font-family:宋体"}]{#struct_0_13426_x3709_2127611368}

[[Started VXLAN-ISIS process during HA upgrade.]{lang="EN-US"}]{#struct_0_13426_x3709_2127611370}

[[当]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_x211040798}[升级时开始启动]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1329344080}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x211040797}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的高可用性]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis ha]{lang="EN-US"}]{#struct_0_13426_x3709_x211040796}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-HA: Received HA upgrade event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x1329999440}*[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}[升级事件]{style="font-family:宋体"}*[。]{style="font-family:宋体"}

::: {#530884181 .myid}
[]{#_Toc404798464}[]{#struct_0_13426_x3709_x211040795}[]{#_Toc389037842}[]{#_Toc373940592}[]{#_Toc372115303}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis local-mac**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1330196048}

[**[debugging vxlan isis local-mac]{lang="EN-US"}**]{#struct_0_13426_x3709_x211040794}

[**[undo debugging vxlan isis local-mac]{lang="EN-US"}**]{#struct_0_13426_x3709_x1330130512}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040793}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_x211040792}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040791}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x1329933904}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_x211040790}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040789}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1329409615}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1745274338}

[**[debugging vxlan isis local-mac]{lang="EN-US"}**]{#struct_0_13426_x3709_1745274339}[命令用来打开]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging vxlan isis local-mac**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_1745274340}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging vxlan isis local-mac]{lang="EN-US"}]{#struct_0_13426_x3709_1745274341}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1005174300}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1745274342}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1745274344}

[[Received local MAC address information: operation type=O*pType*, MAC type=*MacType*, VSI=*vsi-index*, MAC=*MacAddr*.]{lang="EN-US"}]{#struct_0_13426_x3709_1745274345}

[[收到本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_1745274346}[地址信息，]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[，操作类型为]{style="font-family:宋体"}*[OpType]{lang="EN-US"}*[，]{style="font-family:宋体"}*[OpType]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_13426_x3709_935970274}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_935970275}[：删除]{lang="EN-US" style="font-family:宋体"}

[[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_935970276}[地址类型为]{style="font-family:宋体"}*[MacType]{lang="EN-US"}*[，]{style="font-family:宋体"}*[MacType]{lang="EN-US"}*[的取值为]{style="font-family:宋体"}[dynamic]{lang="EN-US"}[，表示动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_935970277}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_935970278}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis local-mac]{lang="EN-US"}]{#struct_0_13426_x3709_935970279}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-LMAC: Received local MAC address information: operation type=add, MAC type=dynamic, VSI=2, MAC=aa-bb-cc.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_935970280}*[收到本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，在]{style="font-family:宋体"}[VSI 2]{lang="EN-US"}[内添加动态的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[aa-bb-cc]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1728096015 .myid}
[]{#_Toc404798465}[]{#struct_0_13426_x3709_x1904780926}[]{#_Toc389037843}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis misc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_935970281}

[**[debugging vxlan isis misc]{lang="EN-US"}**]{#struct_0_13426_x3709_935970282}

[**[undo debugging vxlan isis misc]{lang="EN-US"}**]{#struct_0_13426_x3709_x1904780924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_935970283}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1402681886}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1402681885}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681884}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_x797210695}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1402681883}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1402681882}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1960010109}

[**[debugging vxlan isis misc]{lang="EN-US"}**]{#struct_0_13426_x3709_x1402681881}[命令用来打开与]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程无关的其它调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}**[undo debugging vxlan isis misc]{lang="EN-US"}**[命令用来关闭与]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程无关的其它调试信息开关]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，与]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681880}[进程无关的其它调试信息开关]{style="font-family:宋体"}[处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging vxlan isis misc]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681879}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x989420345}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1402681878}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_164808162}

[[Failed to receive local MAC message.]{lang="EN-US"}]{#struct_0_13426_x3709_164808163}

[[接收本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_164808164}[消息失败]{style="font-family:宋体"}

[[Process created successfully.]{lang="EN-US"}]{#struct_0_13426_x3709_164808165}

[[进程创建成功]{style="font-family:宋体"}]{#struct_0_13426_x3709_164808167}

[[Failed to connect to DEV module.]{lang="EN-US"}]{#struct_0_13426_x3709_164808168}

[[连接]{style="font-family:宋体"}[DEV]{lang="EN-US"}]{#struct_0_13426_x3709_164808169}[模块失败]{style="font-family:宋体"}

[[Error occurred when sending HA response (UPGRADE_OVER).]{lang="EN-US"}]{#struct_0_13426_x3709_164808171}

[[发送]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_2121123299}[升级完成应答错误]{style="font-family:宋体"}

[[Started HA upgrade-wait timer to wait for the reset operation to complete.]{lang="EN-US"}]{#struct_0_13426_x3709_2123285990}

[[为了等待重启结束，启动]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_13426_x3709_2123285991}[升级等待定时器为了]{style="font-family:宋体"}

[[Error occurred during external initialization for HA.]{lang="EN-US"}]{#struct_0_13426_x3709_2123285993}

[[HA]{lang="EN-US"}]{#struct_0_13426_x3709_2123285995}[时外部初始化错误]{style="font-family:宋体"}

[[Delivery of global packet to CPU was *Type*.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366174}

[[全局的报文是否允许发送到]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_13426_x3709_x215366173}[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[表示操作的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nable]{lang="EN-US"}]{#struct_0_13426_x3709_x215366171}[d]{lang="EN-US"}[：允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isable]{lang="EN-US"}]{#struct_0_13426_x3709_x215366169}[d]{lang="EN-US"}[：不允许]{lang="EN-US" style="font-family:宋体"}

[[Process *ProcessID* is deleted successfully.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366168}

[[进程]{style="font-family:宋体"}*[ProcessID]{lang="EN-US"}*]{#struct_0_13426_x3709_x215366166}[删除成功，]{style="font-family:宋体"}*[ProcessID]{lang="EN-US"}*[为进程索引号]{style="font-family:宋体"}

[[Failed to get system node *Number*.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366165}

[[获取系统节点失败，]{style="font-family:宋体"}*[Number]{lang="EN-US"}*]{#struct_0_13426_x3709_1740948963}[为系统索引]{style="font-family:宋体"}

[[Received DEV EPOLLHUP event.]{lang="EN-US"}]{#struct_0_13426_x3709_1740948965}

[[收到]{style="font-family:宋体"}[DEV]{lang="EN-US"}]{#struct_0_13426_x3709_1740948966}[模块发送过来的]{style="font-family:宋体"}[EPOLLHUP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Service port event triggered IS-IS module to connect to L2VPN module.]{lang="EN-US"}]{#struct_0_13426_x3709_1740948968}

[[服务端口事件触发]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_1740948969}[与]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[模块建立连接]{style="font-family:宋体"}

[[Received VXLAN *Type* event.]{lang="EN-US"}]{#struct_0_13426_x3709_1740948970}

[[收到]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_13426_x3709_931644898}[事件。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[为事件的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_13426_x3709_931644899}[：创建事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_931644901}[：删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EPOLLHUP]{lang="EN-US"}]{#struct_0_13426_x3709_931644902}[：]{style="font-family:宋体"}[EPOLL]{lang="EN-US"}[挂起事件]{style="font-family:宋体"}

[[Received VSI *Type* event.]{lang="EN-US"}]{#struct_0_13426_x3709_931644904}

[[收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_13426_x3709_931644905}[事件。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[为事件的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_13426_x3709_931644907}[：创建事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007262}[：删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[hutdown]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007260}[：关闭事件]{style="font-family:
  宋体"}

[[Received L2VPN *Type* event.]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007259}

[[收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007257}[事件。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[为事件的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch begin]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007256}[：批量通告开始]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch end]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007254}[：批量通告结束]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[global disable]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007253}[：]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[全局去使能]{style="font-family:宋体"}

[[Received L2VIF *Type* event.]{lang="EN-US"}]{#struct_0_13426_x3709_177784291}

[[收到]{style="font-family:宋体"}[L2VIF]{lang="EN-US"}]{#struct_0_13426_x3709_177784292}[事件。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[为事件的类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_13426_x3709_177784294}[：创建事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_177784295}[：删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface type *interface*]{lang="EN-US"}]{#struct_0_13426_x3709_177784297}*[-]{lang="EN-US"}[type]{lang="EN-US"}*[：接口类型事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_177784298}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1202593084}[打开与]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[进程无关的其它调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis misc]{lang="EN-US"}]{#struct_0_13426_x3709_2134099426}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-MISC: Received VXLAN create event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x829277991}*[收到]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[创建事件。]{style="font-family:宋体"}*

::: {#-1842245546 .myid}
[]{#_Toc404798466}[]{#struct_0_13426_x3709_2134099427}[]{#_Toc389037844}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis route**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2134099428}

[**[debugging]{lang="EN-US"}[ vxlan isis route ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_2134099429}

[**[undo debugging vxlan isis route]{lang="EN-US"}[ ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_x829212455}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2134099430}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2134099431}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2134099432}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x829540134}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_2134099433}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2134099434}

[**[verbose]{lang="EN-US"}**]{#struct_0_13426_x3709_2134099435}[：表示]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[路由计算的详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x204552734}

[**[debugging vxlan isis route]{lang="EN-US"}**]{#struct_0_13426_x3709_1394608140}[命令用来打开]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的路由计算调试信息开关。]{style="font-family:
宋体"}**[undo]{lang="EN-US"}**[ **debugging vxlan isis route**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的路由计算调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x204552732}[的路由计算调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging vxlan isis route]{lang="EN-US"}]{#struct_0_13426_x3709_1394739212}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x614162408}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x204552730}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x204552728}

[[Flush remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, operation=*Type*.]{lang="EN-US"}]{#struct_0_13426_x3709_x204552726}

[[下刷]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_x204552725}[表项，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[，操作类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_13426_x3709_1751762403}[：无]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_13426_x3709_1751762405}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_13426_x3709_1751762407}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update]{lang="EN-US"}]{#struct_0_13426_x3709_1751762409}[：更新]{lang="EN-US" style="font-family:宋体"}

[[Failed to flush remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, error=*ErrorId*.]{lang="EN-US"}]{#struct_0_13426_x3709_1751762411}

[[下刷]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_942458338}[表项失败，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[，错误]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[ErrorId]{lang="EN-US"}*

[*[Type]{lang="EN-US"}*[ remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*, flag=*bConflictFlag*, conf=*ucConfidence*.]{lang="EN-US"}]{#struct_0_13426_x3709_942458341}

[[操作远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_942458342}[地址表项，操作类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[，具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_13426_x3709_942458344}[ed]{lang="EN-US"}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_13426_x3709_942458346}[d]{lang="EN-US"}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Update]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193822}[d]{lang="EN-US"}[：更新]{lang="EN-US" style="font-family:宋体"}

[[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193820}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[，所属]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，冲突标记为]{style="font-family:宋体"}*[bConflictFlag]{lang="EN-US"}*[，优先级标记为]{style="font-family:宋体"}*[ucConfidence]{lang="EN-US"}*

[[Queried remote MAC entry: VXLAN=*Number*, MAC=*MacAddr*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193818}

[[查询远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193816}[表项：]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*

[[Added remote MAC entry to the flush table: VSI=*vsi-index*, MAC=*MacAddr*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193814}

[[将远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_179946979}[表项添加至下刷表：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*

[[Found remote MAC entry in the flush table: VSI=*vsi-index*, MAC=*MacAddr*.]{lang="EN-US"}]{#struct_0_13426_x3709_179946982}

[[在下刷表中找到要处理的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_179946984}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_179946986}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x1006682445}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的路由计算调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis route]{lang="EN-US"}]{#struct_0_13426_x3709_2136262114}

[\*Jun  8 08:29:44:658 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-ROUTE: Updated remote MAC entry: VXLAN=1, MAC=aa-bb-cc, flag=0, conf=1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_2136262115}*[更新远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项：]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[aa-bb-cc]{lang="EN-US"}[，冲突标记为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1635876601 .myid}
[]{#_Toc404798467}[]{#struct_0_13426_x3709_2136262116}[]{#_Toc389037845}[]{#_Toc373940595}[]{#_Toc372115306}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis self-originate-update**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2136262117}

[**[debugging vxlan isis self-originate-update]{lang="EN-US"}**]{#struct_0_13426_x3709_2136262119}

[**[undo debugging vxlan isis self-originate-update]{lang="EN-US"}**]{#struct_0_13426_x3709_2136262120}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2136262122}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2136262123}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x202390046}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x202390045}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_x202390044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x202390043}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_x202390042}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x202390041}

[**[debugging vxlan isis self-originate-update]{lang="EN-US"}**]{#struct_0_13426_x3709_x202390040}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地更新调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan isis self-originate-update]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地更新调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x202390038}[的本地更新调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging vxlan isis self-originate-update]{lang="EN-US"}]{#struct_0_13426_x3709_x202390037}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x797837303}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1753925091}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1753925092}

[[Purged level-*Number* LSP \[*LSPId*.*PseudoId*-*FragNum*\].]{lang="EN-US"}]{#struct_0_13426_x3709_1753925094}

[[清除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_1753925096}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号）]{style="font-family:宋体"}

[[VXLAN-ISIS level-*Number* LSP overflowed.]{lang="EN-US"}]{#struct_0_13426_x3709_1753925098}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_944621026}[的]{style="font-family:宋体"}[level-*Number* LSP]{lang="EN-US"}[已满]{style="font-family:宋体"}

[[Failed to add area address or supported protocol: remaining space of level-*Number* LSP fragment 0 was not enough.]{lang="EN-US"}]{#struct_0_13426_x3709_944621028}

[[当添加区域地址或协议支持时]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_944621030}[的零分片]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中剩余空间不足]{style="font-family:宋体"}

[[Started rebuilding all level-*Number* LSPs on Tunnel *tunnel-number*.]{lang="EN-US"}]{#struct_0_13426_x3709_944621032}

[[开始对]{style="font-family:宋体"}[Tunnel *tunnel-number*]{lang="EN-US"}]{#struct_0_13426_x3709_944621033}[、]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[进行]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Finished rebuilding all level-*Number* LSPs on Tunnel *tunnel-number*.]{lang="EN-US"}]{#struct_0_13426_x3709_944621035}

[[Tunnel *tunnel-number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031133}[、]{style="font-family:
  宋体"}[level-*Number*]{lang="EN-US"}[所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作结束]{style="font-family:宋体"}

[[MTU change triggered rebuilding.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031132}

[[MTU]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031129}[改变触发]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[LSP sequence number exceeded the limit.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031127}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031126}[的序列号超过最大值（需要反转）]{style="font-family:宋体"}

[[Generated level-*Number* LSP \[*LSPId*.*PseudoId*-*FragNum*\]: sequence number=*SeqNumi,* length=*LspLen*.]{lang="EN-US"}]{#struct_0_13426_x3709_173458914}

[[生成序列号为]{style="font-family:宋体"}*[SeqNum]{lang="EN-US"}*]{#struct_0_13426_x3709_173458916}[、长度为]{style="font-family:宋体"}*[LspLen]{lang="EN-US"}*[的]{style="font-family:宋体"}[level-*Number* LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号）]{style="font-family:宋体"}

[[LSP processing triggered rebuilding on Tunnel *tunnel-number*.]{lang="EN-US"}]{#struct_0_13426_x3709_173458918}

[[在]{style="font-family:宋体"}[Tunnel *tunnel-number*]{lang="EN-US"}]{#struct_0_13426_x3709_173458920}[上的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[处理触发]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[LSP lifetime change triggered rebuilding on all Tunnels.]{lang="EN-US"}]{#struct_0_13426_x3709_173458922}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2129774050}[生存时间触发在所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[上的]{style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{style="font-family:宋体"}

[*[Type ]{lang="EN-US"}*[level-*Number* area address *address*.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774053}

[[操作]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_2131936741}[的区域地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[*[Type]{lang="EN-US"}*]{#struct_0_13426_x3709_2131936743}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_13426_x3709_2131936746}[：]{lang="EN-US" style="font-family:宋体"}[Added]{lang="EN-US"}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_13426_x3709_x206715421}[：]{lang="EN-US" style="font-family:宋体"}[Deleted]{lang="EN-US"}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Added level-*Number* supported protocol type *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_13426_x3709_x206715418}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x206715416}[添加支持的协议类型]{style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[（]{style="font-family:宋体"}*[ProString]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Removed level-*Number* supported protocol type *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_13426_x3709_x206715413}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_1749599716}[删除支持的协议类型]{style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[（]{style="font-family:宋体"}*[ProString]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Added level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_1749599719}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_1749599721}[添加由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息]{style="font-family:宋体"}

[[Removed level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_1749599723}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_940295651}[删除由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息]{style="font-family:宋体"}

[[Modified level-*Number* neighbor: system *systemID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_940295652}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_940295654}[更新由]{style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的邻居信息]{style="font-family:宋体"}

[[Added level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_940295656}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_940295658}[添加由]{style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的伪节点邻居信息]{style="font-family:宋体"}

[[Removed level-*Number* pseudo neighbor: pseudo *pseudoID* -\> neighbor *neighborID*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356510}

[[为]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356508}[删除由]{style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{style="font-family:宋体"}*[neighborID]{lang="EN-US"}*[的伪节点邻居信息]{style="font-family:宋体"}

[[Failed to add MAC address to VXLAN *Number*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356506}

[[为]{style="font-family:宋体"}[VXLAN *Number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1398356504}[添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Removed MAC address from VXLAN *Number*.]{lang="EN-US"}]{#struct_0_13426_x3709_186435042}

[[为]{style="font-family:宋体"}[VXLAN *Number*]{lang="EN-US"}]{#struct_0_13426_x3709_186435046}[删除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Removed all MAC addresses from VXLAN *Number*.]{lang="EN-US"}]{#struct_0_13426_x3709_186435048}

[[删除]{style="font-family:宋体"}[VXLAN *Number*]{lang="EN-US"}]{#struct_0_13426_x3709_186435050}[的所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_186435051}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_2142750178}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的本地更新调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis self-originate-update]{lang="EN-US"}]{#struct_0_13426_x3709_2142750179}

[OVERLAYISIS---0-ORG: Generated level-1 LSP \[0011.2233.4401.00-00\]: sequence number=0x00000001, length=71.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_2142750180}*[生成序列号为]{style="font-family:宋体"}[0x00000001]{lang="EN-US"}[、长度为]{style="font-family:宋体"}[71]{lang="EN-US"}[的]{style="font-family:宋体"}[L1 LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[0011.2233.4401.00-00]{lang="EN-US"}*[）。]{style="font-family:宋体"}

::: {#1950336376 .myid}
[]{#_Toc404798468}[]{#struct_0_13426_x3709_2142750181}[]{#_Toc389037846}[]{#_Toc373940596}[]{#_Toc372115307}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis snp-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2142750182}

[**[debugging vxlan isis snp-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_1271674670}

[**[undo debugging vxlan isis snp-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_2142750183}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2142750184}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2142750185}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2142750186}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_2142750187}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_x195901982}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x195901981}

[**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_2120659447}[：]{style="font-family:宋体"}[表示接收]{style="font-family:宋体"}[VXLAN IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_13426_x3709_x195901980}[：]{style="font-family:宋体"}[表示发送]{style="font-family:宋体"}[VXLAN IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_13426_x3709_x195901979}[：表示详细调试信息，即打印报文的内容。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x195901978}

[**[debugging vxlan isis snp-packet]{lang="EN-US"}**]{#struct_0_13426_x3709_2120069610}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging vxlan isis snp-packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_x195901977}[的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果未指定]{style="font-family:宋体"}**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_x195901976}[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则表示接收和发送]{style="font-family:宋体"}[VXLAN IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging evi isis snp-packet]{lang="EN-US"}]{#struct_0_13426_x3709_x195901975}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x309674800}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x195901974}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1760413154}

[[Received *PduName* from *SourceId* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_1760413156}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_1760413157}[上收到来自于]{style="font-family:宋体"}*[SourceId]{lang="EN-US"}*[的]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[，]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_1760413159}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_1760413161}

[[Received *PduName* from *SourceId* on interface *interface-name:* LSP range=*StartLSPId*.*StartPseudoId*-*StartFragNum* to *EndLSPId*.*EndPseudoId*-*EndFragNum.*]{lang="EN-US"}]{#struct_0_13426_x3709_1760413163}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_951109090}[上收到来自于]{style="font-family:宋体"}*[SourceId]{lang="EN-US"}*[的]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[，]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[取值包括]{style="font-family:宋体"}[L1 CSNP]{lang="EN-US"}[和]{style="font-family:宋体"}[L1 PSNP]{lang="EN-US"}[，]{style="font-family:宋体"}[PDU]{lang="EN-US"}[包括的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[范围为起始]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}*[StartLSPId]{lang="EN-US"}*[.*StartPseudoId*-*StartFragNum*]{lang="EN-US"}[）到结束]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}*[EndLSPId]{lang="EN-US"}*[.*EndPseudoId*-*EndFragpNum*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Failed to process SNP packet.]{lang="EN-US"}]{#struct_0_13426_x3709_951109092}

[[处理]{style="font-family:宋体"}[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_951109094}[报文失败]{style="font-family:宋体"}

[[Failed to find current LSP\'s digest to create CSNP.]{lang="EN-US"}]{#struct_0_13426_x3709_951109096}

[[没有找到当前的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_951109098}[摘要来创建]{style="font-family:宋体"}[CSNP]{lang="EN-US"}

[[Level-*Number* CSNP timer expired on a non-DED interface (*interface-name*).]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543070}

[[非]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543067}[的接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上]{style="font-family:宋体"}[lever-*Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Sent *PduName* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1387543065}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1387543062}[上发送]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[。]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_188597730}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_188597733}

[[Level-*Number* PSNP timer expired on a DED interface (*interface-name*).]{lang="EN-US"}]{#struct_0_13426_x3709_188597735}

[[DED]{lang="EN-US"}]{#struct_0_13426_x3709_188597737}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上]{style="font-family:宋体"}[lever-*Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Invalid LSP ID in SNP.]{lang="EN-US"}]{#struct_0_13426_x3709_188597739}

[[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_2144912866}[中包含无效的]{style="font-family:宋体"}[LSPID]{lang="EN-US"}

[[Incorrect LSP digest TLV length(*TlvLen*) in SNP.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912868}

[[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_2144912869}[中携带错误的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Number of LSP digests in SNP exceeded the limit.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912871}

[[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_2144912873}[中包含]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要的个数超过限制]{style="font-family:宋体"}

[[Incorrect TLV length in SNP.]{lang="EN-US"}]{#struct_0_13426_x3709_2144912875}

[[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_x193739293}[中携带错误的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Invalid TLV in SNP.]{lang="EN-US"}]{#struct_0_13426_x3709_x193739291}

[[SNP]{lang="EN-US"}]{#struct_0_13426_x3709_x193739290}[中携带无效的]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Older than the digest in LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_x193739288}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x193739286}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[，比]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的旧]{style="font-family:宋体"}

[[Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Newer than the digest in LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_1762575846}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_1762575848}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[，比]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的新]{style="font-family:宋体"}

[[Processed LSP digest *LSPId*.*PseudoId*--*FragNum*. Result: Same as the digest in LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_1762575851}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_953271778}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[，与]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的新旧相同]{style="font-family:宋体"}

[[Processed digest of *LSPId*.*PseudoId*--*FragNum*: digest not contained in LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_953271780}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_953271782}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[，在]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}

[[PSNP not processed: current ED was not a DED.]{lang="EN-US"}]{#struct_0_13426_x3709_953271784}

[[当前]{style="font-family:宋体"}[ED]{lang="EN-US"}]{#struct_0_13426_x3709_953271786}[不是]{style="font-family:宋体"}[DED]{lang="EN-US"}[，不处理]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[SNPType]{lang="EN-US"}*[ can\'t be processed before DED election.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380382}

[[在]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380380}[选举前不处理]{style="font-family:宋体"}*[SNPType]{lang="EN-US"}*[报文，]{style="font-family:宋体"}*[SNPType]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380378}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380376}

[[CSNP didn\'t contain digest for LSP *LSPId*.*PseudoId*-*FragNum*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1385380374}

[[在]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_169133635}[中没有]{style="font-family:宋体"}[LSP *LSPId*.*PseudoId*-*FragNum*]{lang="EN-US"}[的摘要]{style="font-family:宋体"}

[[DED doesn\'t process CSNP.]{lang="EN-US"}]{#struct_0_13426_x3709_169133637}

[[DED]{lang="EN-US"}]{#struct_0_13426_x3709_169133639}[上不处理]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Invalid SNP PDU type.]{lang="EN-US"}]{#struct_0_13426_x3709_169133643}

[[无效的]{style="font-family:宋体"}[SNP PDU]{lang="EN-US"}]{#struct_0_13426_x3709_2125448770}[类型]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2125448773}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_2125448775}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[ SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis snp-packet send]{lang="EN-US"}]{#struct_0_13426_x3709_2127611463}

[\*Dec 19 15:40:51:337 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-SNP: Sent L1 CSNP on interface Tunnel1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_2127611462}*[在]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

::: {#-236476655 .myid}
[]{#_Toc404798469}[]{#struct_0_13426_x3709_2127611465}[]{#_Toc389037847}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2127611464}

[**[debugging vxlan isis timer]{lang="EN-US"}**]{#struct_0_13426_x3709_2127611467}

[**[undo debugging vxlan isis timer]{lang="EN-US"}**]{#struct_0_13426_x3709_2127611466}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040701}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_x211040702}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040699}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x211040697}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_x211040698}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x211040695}

[[无]{style="font-family:宋体"}]{#struct_0_13426_x3709_x211040693}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1008849328}

[**[debugging vxlan isis]{lang="EN-US"}[ timer]{lang="EN-US"}**]{#struct_0_13426_x3709_1745274435}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan isis]{lang="EN-US"}[ timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[VXLAN IS-IS]{lang="EN-US"}[的定时器调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_1745274439}[的定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging vxlan isis timer]{lang="EN-US"}]{#struct_0_13426_x3709_x2007273046}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x108935311}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1745274441}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1745274440}

[[Started *Type* timer: value=*value*.]{lang="EN-US"}]{#struct_0_13426_x3709_1745274443}

[[启动]{style="font-family:宋体"}]{#struct_0_13426_x3709_1745274442}*[Type]{lang="EN-US"}*[定时器，时间为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T2]{lang="EN-US"}]{#struct_0_13426_x3709_935970370}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T3]{lang="EN-US"}]{#struct_0_13426_x3709_935970373}

[[Reset *Type* timer: value=*value*.]{lang="EN-US"}]{#struct_0_13426_x3709_935970372}

[[重置]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*]{#struct_0_13426_x3709_935970375}[定时器，]{lang="EN-US" style="font-family:宋体"}[重置后的]{style="font-family:宋体"}[时间为]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值]{lang="EN-US" style="font-family:宋体"}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T2]{lang="EN-US"}]{#struct_0_13426_x3709_935970377}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T3]{lang="EN-US"}]{#struct_0_13426_x3709_935970376}

[[Level-*Number* adjacency *SystemId* hold timer expired on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_935970379}

[[接口]{lang="EN-US" style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_935970378}[下的]{lang="EN-US" style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[的邻居]{lang="EN-US" style="font-family:宋体"}*[SystemId]{lang="EN-US"}*[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Level-*Number* hello timer expired on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681790}

[[接口]{lang="EN-US" style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1402681788}[下的]{lang="EN-US" style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[H]{lang="EN-US"}[ello]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Started sequence number wrap delay timer: value=*value* ms.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681785}

[[启动]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681786}[序列号达到最大值的翻转等待定时器，定时器时长为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Level-*Number* CSNP timer expired on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681783}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1402681781}[下的]{style="font-family:宋体"}[level-*Number* CSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Level-*Number* flood timer expired on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1402681782}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_164808259}[下的]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[泛洪定时器超时]{style="font-family:宋体"}

[[Level-*Number* LSP \[*LSPId*.*PseudoId*-*FragNum*\] generation timer expired.]{lang="EN-US"}]{#struct_0_13426_x3709_164808258}

[[leve]{lang="EN-US"}]{#struct_0_13426_x3709_164808261}[l]{lang="EN-US"}[-*Number*]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{lang="EN-US" style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}[生成定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Started level-*Number* LSP \[*LSPId*.*PseudoId*-*FragNum*\] generation timer: value= *TimeValue* (ms).]{lang="EN-US"}]{#struct_0_13426_x3709_164808263}

[[启动]{style="font-family:宋体"}[level-*Number* ]{lang="EN-US"}]{#struct_0_13426_x3709_164808262}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号）生成定时器，定时器时长为]{style="font-family:宋体"}*[TimeValue]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Stopped level-*Number* LSP \[*LSPId*.*PseudoId*-*FragNum*\] generation timer.]{lang="EN-US"}]{#struct_0_13426_x3709_164808265}

[[停止]{lang="EN-US" style="font-family:宋体"}[leve]{lang="EN-US"}]{#struct_0_13426_x3709_164808264}[l]{lang="EN-US"}[-*Number*]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{lang="EN-US" style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}[生成定时器]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_164808267}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1827822246}[打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的定时器]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis timer]{lang="EN-US"}]{#struct_0_13426_x3709_164808266}

[\*Dec 20 10:18:29:955 2011 Sysname OLISIS/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OVERLAYISIS-0-TMR: Level-1 hello timer expired on interface Tunnel1.]{lang="EN-US"}

[*[// Tunnel1]{lang="EN-US"}*]{#struct_0_13426_x3709_1827822245}*[上的]{style="font-family:宋体"}[Lever-1 Hello]{lang="EN-US"}[报文发送定时器超时。]{style="font-family:宋体"}*

::: {#-814476786 .myid}
[]{#_Toc404798470}[]{#struct_0_13426_x3709_2121123395}[]{#_Toc389037848}[]{#_Toc373940598}[]{#_Toc372115309}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan isis update-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1685947606}

[**[debugging vxlan isis update-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_2121123394}

[**[undo debugging vxlan isis update-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_13426_x3709_2121123397}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1686078678}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2121123396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1686013142}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_2121123399}

[[mdc-admim]{lang="EN-US"}]{#struct_0_13426_x3709_1685685462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_2121123398}

[**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_1685619926}[：]{style="font-family:宋体"}[表示接收]{style="font-family:宋体"}[VXLAN IS-IS LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_13426_x3709_2121123401}[：]{style="font-family:宋体"}[表示发送]{style="font-family:宋体"}[VXLAN IS-IS LSP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_13426_x3709_2121123400}[：表示详细调试信息，即打印报文内容。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1417182001}

[**[debugging vxlan isis update-packet]{lang="EN-US"}**]{#struct_0_13426_x3709_x1589689985}[命令用来打开]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging vxlan isis update-packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_2121123403}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[执行本命令时，如果未指定]{style="font-family:宋体"}**[receive]{lang="EN-US"}**]{#struct_0_13426_x3709_2121123402}[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则表示接收和发送]{style="font-family:宋体"}[VXLAN IS-IS LSP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[表1-12 ]{lang="EN-US"}[debugging vxlan isis update-packet]{lang="EN-US"}]{#struct_0_13426_x3709_x1417050929}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_490114138}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x217528765}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x217528763}

[[Flooded *PduName* *LSPId*.*PseudoId*-*FragNum* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x217528764}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x217528761}[上泛洪]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[），]{style="font-family:
  宋体"}*[PduName]{lang="EN-US"}*[的取值包括：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x217528762}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_13426_x3709_x217528759}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_13426_x3709_x217528760}

[[L1 LSP *Type* on interface *interface-name*: SNPA=*SnpaAddr*, LSP ID=*LSPId*.*PseudoId*--*FragNum*, sequence number=*Sequence*, hold time=*HoldTime*.]{lang="EN-US"}]{#struct_0_13426_x3709_x217528757}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x217528758}[上从地址]{style="font-family:宋体"}*[SnpaAddr]{lang="EN-US"}*[接收到或向该地址发送的]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[、序列号为]{style="font-family:
  宋体"}*[Sequence]{lang="EN-US"}*[、时间为]{style="font-family:宋体"}*[HoldTime]{lang="EN-US"}*[的]{style="font-family:宋体"}[L1 LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[Type]{lang="EN-US"}*]{#struct_0_13426_x3709_1738786371}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receive]{lang="EN-US"}]{#struct_0_13426_x3709_1738786370}[d]{lang="EN-US"}[：接收]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sen]{lang="EN-US"}]{#struct_0_13426_x3709_1738786372}[t]{lang="EN-US"}[：发送]{lang="EN-US" style="font-family:宋体"}

[*[Type ]{lang="EN-US"}*[remote address: VXLAN*=Number*, MAC*=MacAddr*.]{lang="EN-US"}]{#struct_0_13426_x3709_1738786375}

[[对远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_1738786374}[地址进行操作，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_13426_x3709_1738786377}[ed]{lang="EN-US"}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_13426_x3709_1738786376}[d]{lang="EN-US"}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modif]{lang="EN-US"}]{#struct_0_13426_x3709_1738786379}[ied]{lang="EN-US"}[：修改]{lang="EN-US" style="font-family:宋体"}

[[LSP\'s sequence number was 0.]{lang="EN-US"}]{#struct_0_13426_x3709_1738786378}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_929482307}[报文的序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Illegal IS type in level-1 LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_929482309}

[[Level-1]{lang="EN-US"}]{#struct_0_13426_x3709_929482308}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文中存在无效的]{style="font-family:宋体"}[IS]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Checksum was 0.]{lang="EN-US"}]{#struct_0_13426_x3709_929482311}

[[校验和为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_13426_x3709_929482310}

[[Checksum error.]{lang="EN-US"}]{#struct_0_13426_x3709_929482312}

[[校验和错误]{style="font-family:宋体"}]{#struct_0_13426_x3709_929482315}

[[Invalid extended IS reachability TLV.]{lang="EN-US"}]{#struct_0_13426_x3709_929482314}

[[不支持的扩展]{style="font-family:宋体"}[IS]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169853}[可达性]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Supported protocol mismatch.]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169851}

[[支持的协议不匹配]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1409169852}

[[LSP had more than *Count* area addresses.]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169849}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169850}[中区域地址数量超过最大值]{style="font-family:宋体"}

[[LSP had incorrect area address length (*Length*).]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169847}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169848}[中区域地址长度错误，长度为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*

[[LSP had incorrect area address (*AreaAddr*).]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169845}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1409169846}[中区域地址错误，地址为]{style="font-family:宋体"}*[AreaAddr]{lang="EN-US"}*

[[Invalid VXLAN TLV.]{lang="EN-US"}]{#struct_0_13426_x3709_166970947}

[[无效的]{style="font-family:宋体"}[VXLAN TLV]{lang="EN-US"}]{#struct_0_13426_x3709_166970949}

[[Invalid MAC reachability TLV.]{lang="EN-US"}]{#struct_0_13426_x3709_166970948}

[[无效的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_13426_x3709_166970951}[可达性]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Incorrect area address TLV in LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_166970952}

[[在]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_166970954}[报文中存在错误的区域地址]{style="font-family:宋体"}[TLV ]{lang="EN-US"}

[[Incorrect TLV length in the received LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_2123286082}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2123286085}[报文中]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度错误]{style="font-family:宋体"}

[[A version of local LSP *LSPId*.*PseudoId*-*FragNum* was generated with a newer sequence number (Seq) than the version in the LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_2123286084}

[[本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2123286087}[的序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中新]{style="font-family:宋体"}

[[A new version of non-local LSP *LSPId*.*PseudoId*-*FragNum* was received with a newer sequence number (Seq) than the version in the LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_2123286086}

[[非本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2123286089}[的序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中新]{style="font-family:宋体"}

[[The new version of LSP *LSPId*.*PseudoId*-*FragNum* contained a sequence number (*Seq*) older than the version in the LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_2123286091}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_2123286090}[的序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中旧]{style="font-family:宋体"}

[[The new version of LSP *LSPId*.*PseudoId*-*FragNum* contained the same sequence number (*Seq*) as the version in the LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366078}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x215366076}[的序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中相同]{style="font-family:宋体"}

[*[LspType]{lang="EN-US"}*[ LSP *LSPId*.*PseudoId*-*FragNum Seq* didn\'t exist in LSDB.]{lang="EN-US"}]{#struct_0_13426_x3709_x215366074}

[[LSDB]{lang="EN-US"}]{#struct_0_13426_x3709_x215366071}[中不存在]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId*-*FragNum*]{lang="EN-US"}[、序列号为]{style="font-family:宋体"}*[Seq]{lang="EN-US"}*[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}*[LspType]{lang="EN-US"}*[为]{style="font-family:宋体"}[LSP]{lang="EN-US"}[类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Non-local]{lang="EN-US"}]{#struct_0_13426_x3709_x215366069}[：非本地的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_13426_x3709_x215366070}[：本地的]{lang="EN-US" style="font-family:宋体"}

[[PDU discarded: PDU size (*Size*) exceeded receive buffer size (*SizeBuf*).]{lang="EN-US"}]{#struct_0_13426_x3709_1740949059}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_1740949061}[大小]{style="font-family:宋体"}*[Size]{lang="EN-US"}*[大于接收缓冲区大小]{style="font-family:宋体"}*[SizeBuf]{lang="EN-US"}*[，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[PDU discarded: PDU size (*Size*) smaller than common header\'s length (*Length*).]{lang="EN-US"}]{#struct_0_13426_x3709_1740949060}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_1740949062}[大小]{style="font-family:宋体"}*[Size]{lang="EN-US"}*[小于]{style="font-family:宋体"}[PDU]{lang="EN-US"}[通用报文头长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[，丢弃]{style="font-family:宋体"}[PDU ]{lang="EN-US"}

[[PDU discarded: PDU size (*Size*) smaller than value (*Length*) in the Length Indicator field.]{lang="EN-US"}]{#struct_0_13426_x3709_1740949065}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_1740949064}[大小]{style="font-family:宋体"}*[Size]{lang="EN-US"}*[小于]{style="font-family:宋体"}[PDU]{lang="EN-US"}[填充的报文头长度]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[PDU discarded: PDU length mismatch, recvLen=*RecvLength*, encodeLen=*EncodeLenght*.]{lang="EN-US"}]{#struct_0_13426_x3709_1740949066}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_931644995}[长度]{style="font-family:宋体"}*[RecvLength]{lang="EN-US"}*[与报文中指示的长度]{style="font-family:宋体"}*[EncodeLenght]{lang="EN-US"}*[不匹配，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[PDU discarded on interface (*interface-name*): PDU contained the same SNPA address as local system.]{lang="EN-US"}]{#struct_0_13426_x3709_931644994}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_931644997}[上收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文中]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[的地址与本地一样，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[PDU discarded: VXLAN-ISIS process was disabled.]{lang="EN-US"}]{#struct_0_13426_x3709_931644996}

[[VXLAN IS-IS]{lang="EN-US"}]{#struct_0_13426_x3709_931644999}[进程处于]{style="font-family:宋体"}[disabled]{lang="EN-US"}[状态，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Failed to check received packet.]{lang="EN-US"}]{#struct_0_13426_x3709_931644998}

[[检查接收到的报文失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_931645001}

[[PDU discarded: LSP or SNP common header error.]{lang="EN-US"}]{#struct_0_13426_x3709_931645000}

[[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_931645003}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[通用报文头错误，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[PDU level mismatch.]{lang="EN-US"}]{#struct_0_13426_x3709_1212686922}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_931645002}[报文级别不匹配]{style="font-family:宋体"}

[[PDU discarded: no active neighbor with SNPA (*SnpaAddr*) existed on the interface (*interface-name*).]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007165}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1407007166}[上不存在激活的邻居]{style="font-family:宋体"}*[SnpaAddr]{lang="EN-US"}*[，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Failed to process LSP.]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007163}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007164}[报文失败]{style="font-family:宋体"}

[[PDU discarded: the PDU was not LSP or SNP.]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007161}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007162}[报文不是]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x2185895}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_953951262}[打开]{style="font-family:宋体"}[VXLAN IS-IS update-packet]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan isis update-packet receive]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007159}

[\*Jun  8 08:31:21:994 2011 Sysname OLISIS/7/DEBUG: -MDC=1; ]{lang="EN-US"}

[OVERLAYISIS-0-UPDT: PDU level mismatch.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_45064880}*[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文级别不匹配。]{style="font-family:宋体"}*

::: {#2080355834 .myid}
[]{#_Toc404798471}[]{#struct_0_13426_x3709_196130918}[]{#_Toc389037849}[]{#_Toc386011001}[]{#_Toc367864357}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan neighbor-discovery client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1407007160}

[**[debugging vxlan neighbor-discovery client]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13426_x3709_x1164985309}

[**[undo debugging vxlan neighbor-discovery client]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13426_x3709_x1738128849}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1024308117}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1407007157}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x405273814}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_527924260}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x1407007158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1521019061}

[**[all]{lang="EN-US"}**]{#struct_0_13426_x3709_177784387}[：表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_13426_x3709_812361888}[：表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[表项调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13426_x3709_x1164185081}[：表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13426_x3709_x1365121274}[：表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_13426_x3709_177784386}[：表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_812361887}

[**[debugging vxlan neighbor-discovery client]{lang="EN-US"}**]{#struct_0_13426_x3709_x1164185082}[命令用来打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan neighbor-discovery client]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_13426_x3709_177784389}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-13 ]{lang="EN-US"}[debugging vxlan neighbor-discovery client entry]{lang="EN-US"}]{#struct_0_13426_x3709_812361890}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_768405658}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_177784388}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_177784391}

[[Failed to find the server node.]{lang="EN-US"}]{#struct_0_13426_x3709_x1526290278}

[[查找服务器节点失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_177784390}

 

[*[operate-name]{lang="EN-US"}*[: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_177784393}

[[[操作表项信息，接口为]{style="font-family:宋体"}]{.TableTextChar}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_177784392}[[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}]{.TableTextChar}[[为]{style="font-family:宋体"}]{.TableTextChar}*[netid-value]{lang="EN-US"}*[[，]{style="font-family:宋体"}[IP]{lang="EN-US"}]{.TableTextChar}[[地址为]{style="font-family:宋体"}]{.TableTextChar}*[ip-address]{lang="EN-US"}*

[*[operate-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1526290277}[[的取值可能为：]{style="font-family:宋体"}]{.TableTextChar}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Added neighbor]{lang="EN-US"}]{#struct_0_13426_x3709_177784395}[：添加邻居节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted neighbor]{lang="EN-US"}]{#struct_0_13426_x3709_177784394}[：删除邻居节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Added server node]{lang="EN-US"}]{#struct_0_13426_x3709_2134099523}[：添加服务器节点]{lang="EN-US" style="font-family:
  宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted server node]{lang="EN-US"}]{#struct_0_13426_x3709_2134099522}[：删除服务器节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Added dummy]{lang="EN-US"}]{#struct_0_13426_x3709_2134099525}[：添加]{lang="EN-US" style="font-family:宋体"}[Dummy]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted dummy]{lang="EN-US"}]{#struct_0_13426_x3709_1509177561}[：删除]{lang="EN-US" style="font-family:宋体"}[Dummy]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}

 

[[Added tunnel: interface= *interface-name*, peer address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2134099524}

[[添加隧道：接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_2134099527}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

 

[[Deleted tunnel: interface= *interface-name*, peer address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2134099526}

[[删除隧道：接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_1509374169}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

 

[ ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[debugging vxlan neighbor-discovery client error]{lang="EN-US"}]{#struct_0_13426_x3709_2134099529}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_797763480}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1509439705}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_2134099528}

[[Failed to create run info.]{lang="EN-US"}]{#struct_0_13426_x3709_1751762501}

[[创建运行信息失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_1751762500}

 

[[Failed to create hash.]{lang="EN-US"}]{#struct_0_13426_x3709_349453177}

[[创建]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_13426_x3709_1751762503}[失败]{style="font-family:宋体"}

 

[[Failed to start ENDP service.]{lang="EN-US"}]{#struct_0_13426_x3709_1751762502}

[[启动]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_13426_x3709_1751762505}[服务失败]{style="font-family:宋体"}

 

[[Failed to create tunnel connection.]{lang="EN-US"}]{#struct_0_13426_x3709_349256569}

[[创建与隧道的连接失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_1751762504}

 

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging vxlan neighbor-discovery client event]{lang="EN-US"}]{#struct_0_13426_x3709_349191033}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_558988057}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1751762507}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1751762506}

[[Created *timer-name* timer: timer interval= *time-value*, timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_942458435}

[[创建]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x967409930}[定时器，时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*[，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

[*[timer-name]{lang="EN-US"}*]{#struct_0_13426_x3709_942458434}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register]{lang="EN-US"}]{#struct_0_13426_x3709_942458437}[：注册定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIPC reconnect]{lang="EN-US"}]{#struct_0_13426_x3709_942458436}[：]{lang="EN-US" style="font-family:宋体"}[LIPC]{lang="EN-US"}[重连定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[neighbor aging]{lang="EN-US"}]{#struct_0_13426_x3709_x967409933}[：邻居老化定时器]{lang="EN-US" style="font-family:宋体"}

 

[[Modified register timer: timer interval= *time-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_942458439}

[[修改注册定时器的时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_13426_x3709_942458438}

 

[[Deleted *timer-name* timer: timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_x967409935}

[[删除]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_13426_x3709_942458441}[定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

[*[timer-name]{lang="EN-US"}*]{#struct_0_13426_x3709_942458440}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register]{lang="EN-US"}]{#struct_0_13426_x3709_942458443}[：注册定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIPC reconnect]{lang="EN-US"}]{#struct_0_13426_x3709_2135916280}[：]{lang="EN-US" style="font-family:宋体"}[LIPC]{lang="EN-US"}[重连定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[neighbor aging]{lang="EN-US"}]{#struct_0_13426_x3709_942458442}[：邻居老化定时器]{lang="EN-US" style="font-family:宋体"}

 

[[Received tunnel restart event.]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193725}

[[收到隧道重启事件]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1396193726}

 

[[Started ENDP service.]{lang="EN-US"}]{#struct_0_13426_x3709_606165282}

[[启动]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193723}[服务]{style="font-family:宋体"}

 

[[Started smoothing neighbor information.]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193724}

[[开始平滑邻居信息]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1396193721}

 

[[Finished smoothing neighbor information.]{lang="EN-US"}]{#struct_0_13426_x3709_1365680169}

[[邻居信息平滑结束]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1396193722}

 

[[Stopped ENDP service.]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193719}

[[停止]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_13426_x3709_x1396193720}[服务]{style="font-family:宋体"}

 

[*[interface-name ]{lang="EN-US"}*[received interface *event-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x200403772}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1396193717}[收到接口事件，事件类型为]{style="font-family:宋体"}*[event-name]{lang="EN-US"}*

[*[event-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1396193718}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up event]{lang="EN-US"}]{#struct_0_13426_x3709_179947075}[：接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down event]{lang="EN-US"}]{#struct_0_13426_x3709_2120898597}[：接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create event]{lang="EN-US"}]{#struct_0_13426_x3709_179947074}[：接口创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete event]{lang="EN-US"}]{#struct_0_13426_x3709_179947077}[：接口删除]{lang="EN-US" style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[debugging vxlan neighbor-discovery client packet]{lang="EN-US"}]{#struct_0_13426_x3709_2120898599}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_628114463}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_179947076}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_179947079}

[[Interface *interface-name* received a packet: packet type= *type-value*, network ID= *netid-value*, server address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2120898609}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_179947078}[收到一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_13426_x3709_179947081}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_2076268585}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_179947080}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_13426_x3709_179947083}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_179947082}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

 

[[Interface *interface-name s*ent a packet: packet type= *type-value*, network ID= *netid-value*, server address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2076268586}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_2136262211}[发送一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_13426_x3709_2136262210}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_2136262213}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_x1684213361}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_13426_x3709_2136262212}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_2136262215}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

 

[[Peer info: IP address= *ipaddr-value*, system ID= *macaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1684082289}

[[对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13426_x3709_2136262214}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*

 

[[Invalid peer info: IP address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2136262217}

[[失效的对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13426_x3709_2136262216}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

 

[[Packet failed header check.]{lang="EN-US"}]{#struct_0_13426_x3709_x1684016753}

[[报文头检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2136262219}

 

[[Packet failed fixed header check.]{lang="EN-US"}]{#struct_0_13426_x3709_2136262218}

[[报文固定头检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_x202389949}

 

[[Packet failed required content check.]{lang="EN-US"}]{#struct_0_13426_x3709_x837809544}

[[报文强制部分检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_x202389950}

 

[[Packet failed extended content check.]{lang="EN-US"}]{#struct_0_13426_x3709_x202389947}

[[报文扩展部分检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_x202389948}

 

[[Transaction ID mismatch.]{lang="EN-US"}]{#struct_0_13426_x3709_x202389945}

[[事务]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13426_x3709_x202389946}[不相等]{style="font-family:宋体"}

 

[[Packet failed authentication.]{lang="EN-US"}]{#struct_0_13426_x3709_x837875080}

[[认证失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_x202389943}

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x838202760}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x202389944}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[表项调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery client entry]{lang="EN-US"}]{#struct_0_13426_x3709_x838006152}

[\*Sep  6 17:14:34:243 2011 Sysname ENDC/7/ENTRY: -MDC=1; Add neighbor: interface= Tunnel1, network ID= 1; IP address= 1.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x746194828}*[添加邻居节点，接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[[\*Sep  6 17:14:34:246 2011 Sysname ENDC/7/ENTRY: -MDC=1; Added tunnel: interface= Tunnel1, ieer address= 1.1.1.1.]{lang="EN-US"}]{#struct_0_13426_x3709_x202389941}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x838333832}*[添加隧道，接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x1956751664}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[事件调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[发送注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery client event]{lang="EN-US"}]{#struct_0_13426_x3709_x202389942}

[\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created register timer: time interval= 15s, timer ID= 10.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x838137224}*[创建注册定时器，时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1753925187}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[报文调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery client packet]{lang="EN-US"}]{#struct_0_13426_x3709_1800330474}

[\*Sep  6 17:22:10:772 2011 Sysname ENDC/7/PACKET: -MDC=1; Interface Tunnel1 received a packet: packet type= 4, network ID= 1, server address= 1.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x812375028}*[接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[收到一个报文，报文类型为注册应答报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[[\*Sep  6 17:22:10:773 2011 Sysname ENDC/7/PACKET: -MDC=1; Peer info: IP address= 1.1.1.1, system ID= 0011-2200-0101.]{lang="EN-US"}]{#struct_0_13426_x3709_1113403407}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_1753925186}*[对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0011-2200-0101]{lang="EN-US"}*

::: {#-932966588 .myid}
[]{#_Toc404798472}[]{#struct_0_13426_x3709_1800264938}[]{#_Toc389037850}[]{#_Toc386011002}[]{#_Toc367864358}[]{#_Toc287608520}[]{#_Toc205804228}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan neighbor-discovery server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1221462379}

[**[debugging vxlan neighbor-discovery server]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13426_x3709_1753925189}

[**[undo debugging vxlan neighbor-discovery server]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13426_x3709_1800723690}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_364752615}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_1753925188}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1800658154}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_x1652111237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13426_x3709_1753925191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1800199401}

[**[all]{lang="EN-US"}**]{#struct_0_13426_x3709_x2000798402}[：表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_13426_x3709_1753925190}[：表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[表项调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13426_x3709_1800133865}[：表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13426_x3709_x10899662}[：表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_13426_x3709_1753925193}[：表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_1800068329}

[**[debugging vxlan neighbor-discovery server]{lang="EN-US"}**]{#struct_0_13426_x3709_x2043885372}[命令用来打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan neighbor-discovery server]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_13426_x3709_x473249981}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-17 ]{lang="EN-US"}[debugging vxlan neighbor-discovery server entry]{lang="EN-US"}]{#struct_0_13426_x3709_1753925192}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_981102314}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_1800002793}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_1753925195}

[[Added client: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_1753925194}

[[增加客户，接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_944621123}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

 

[[Deleted client: interface= *interface-name*, network ID= *netid-value*, IP address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1776953800}

[[删除客户，接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_944621122}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

 

[ ]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[debugging vxlan neighbor-discovery server error]{lang="EN-US"}]{#struct_0_13426_x3709_x1776953799}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1016487163}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_944621125}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_944621124}

[[Failed to create run info.]{lang="EN-US"}]{#struct_0_13426_x3709_944621127}

[[创建运行信息失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_x1776953796}

 

[ ]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[debugging vxlan neighbor-discovery server event]{lang="EN-US"}]{#struct_0_13426_x3709_944621126}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1032839163}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1776953795}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_944621129}

[[Created aging timer: timer interval= *time-value*, timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_944621128}

[[创建老化定时器，时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_13426_x3709_x1776953789}[，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

 

[[Modified aging timer: timer interval= *time-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_944621131}

[[修改老化定时器的时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_13426_x3709_944621130}

 

[[Deleted aging timer: timer id= *id-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_561698363}

[[删除]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031037}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*[的老化定时器]{style="font-family:宋体"}

 

[*[interface-name ]{lang="EN-US"}*[received interface *event-name*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031038}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_564281287}[收到接口事件，事件类型为]{style="font-family:宋体"}*[event-name]{lang="EN-US"}*

[*[event-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1394031035}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up event]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031036}[：接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down event]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031033}[：接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create event]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031034}[：接口创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete event]{lang="EN-US"}]{#struct_0_13426_x3709_x1048856821}[：接口删除]{lang="EN-US" style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[debugging vxlan neighbor-discovery server packet]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031031}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1063319543}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1808371708}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1394031032}

[[Packet failed authentication.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031029}

[[认证失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2130299692}

 

[[Interface *interface-name* received a packet: packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_x1394031030}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_173459011}[收到一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户端服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_13426_x3709_x1570565002}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_173459010}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_173459013}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_13426_x3709_x1570565000}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_173459012}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

 

[[Interface *interface-name* sent a packet: ]{lang="EN-US"}]{#struct_0_13426_x3709_173459015}

[[packet type= *type-value*[, network ID= ]{.TableTextChar}*netid-value*[, client address= ]{.TableTextChar}*ipaddr-value*[.]{.TableTextChar}]{lang="EN-US"}]{#struct_0_13426_x3709_173459014}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13426_x3709_x1570565005}[发送一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_13426_x3709_173459017}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_13426_x3709_173459016}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_13426_x3709_173459019}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_13426_x3709_x1570564994}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_173459018}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

 

[[Client info: IP address= *ipaddr-value*, system ID= *macaddr-value*, register interval= *time-value*.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774147}

[[报文中携带的客户信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13426_x3709_767448280}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*[，桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，注册时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*

 

[[Packet failed validity check.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774146}

[[合法性检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2129774149}

 

[[Packet failed header check.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774148}

[[报文头检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_768431320}

 

[[Packet failed fixed header check.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774151}

[[报文固定头检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2129774150}

 

[[Packet failed required content check.]{lang="EN-US"}]{#struct_0_13426_x3709_767907031}

[[报文强制部分检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2129774153}

 

[[Packet failed extended content check.]{lang="EN-US"}]{#struct_0_13426_x3709_2129774152}

[[报文扩展部分检测失败]{style="font-family:宋体"}]{#struct_0_13426_x3709_2129774155}

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_767579351}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1939509077}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[表项调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery server entry]{lang="EN-US"}]{#struct_0_13426_x3709_2129774154}

[\*Sep  6 16:49:49:180 2011 Sysname ENDS/7/ENTRY: -MDC=1; Added client: interface= Tunnel0, network ID= 1, IP address= 1.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_767644887}*[增加客户，接口为]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x1593412161}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[事件调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery server event]{lang="EN-US"}]{#struct_0_13426_x3709_x208878013}

[\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created aging timer: time interval= 75s, timer ID= 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_1063294653}*[创建老化定时器，时间间隔为]{style="font-family:宋体"}[75]{lang="EN-US"}[秒，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_x1946802563}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[报文调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan neighbor-discovery server packet]{lang="EN-US"}]{#struct_0_13426_x3709_380154240}

[\*Sep  6 16:58:30:600 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 received a packet: packet type= 3, network ID= 1, client address= 1.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x208878014}*[接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[收到一个报文：报文类型为注册报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*

[[\*Sep  6 17:01:02:276 2011 Sysname ENDS/7/PACKET: -MDC=1; Client info: IP address= 1.1.1.2, system ID= 0011-2200-0101, register interval= 5s.]{lang="EN-US"}]{#struct_0_13426_x3709_1063360189}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_1603163111}*[报文中携带的客户信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0011-2200-0101]{lang="EN-US"}[，注册时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Sep  6 16:58:30:604 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 sent a packet: packet type= 4, network ID= 1, client address= 1.1.1.2.]{lang="EN-US"}]{#struct_0_13426_x3709_x208878011}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_1063163581}*[接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[发送一个报文：报文类型为注册应答报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*

::: {#1245172315 .myid}
[]{#_Toc404798473}[]{#struct_0_13426_x3709_769636291}[]{#_Toc389037852}

**VXLAN \-- VXLAN调试命令 \-- debugging vxlan tunnel**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x950774386}

[**[debugging vxlan]{lang="EN-US"}**[ **tunnel** { **all** \| **error** \| **packet** } \[ **interface** **tunnel** *tunnel-number* \]]{lang="EN-US"}]{#struct_0_13426_x3709_109649992}

[**[undo debugging vxlan]{lang="EN-US"}**[ **tunnel** { **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_13426_x3709_1821982392}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x324658184}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13426_x3709_2052695674}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x699805234}

[[network-admin]{lang="EN-US"}]{#struct_0_13426_x3709_753763452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13426_x3709_433334276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1401136603}

[**[all]{lang="EN-US"}**]{#struct_0_13426_x3709_1550137356}[：表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13426_x3709_x269814601}[：表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_13426_x3709_x1703414732}[：表示]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道报文调试信息开关。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}**[ *tunnel-number*]{lang="EN-US"}]{#struct_0_13426_x3709_x125237115}[：表示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的调试信息开关。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x492401638}

[**[debugging vxlan tunnel]{lang="EN-US"}**]{#struct_0_13426_x3709_184332683}[命令用来打开]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的调试信息开关。]{style="font-family:宋体"}**[undo debugging vxlan tunnel]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}]{#struct_0_13426_x3709_x286816166}[隧道的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-21 ]{lang="EN-US"}[debugging vxlan tunnel error]{lang="EN-US"}]{#struct_0_13426_x3709_1873948322}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x376568837}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1625125114}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x232257503}

[[Packet dropped because the destination tunnel interface was not found.]{lang="EN-US"}]{#struct_0_13426_x3709_x1401202139}

[[对出隧道报文进行解封装时，找不到对应的隧道接口，报文被丢弃]{style="font-family:宋体"}]{#struct_0_13426_x3709_x352411126}

[[Packet dropped because the number of packet loops exceeded six.]{lang="EN-US"}]{#struct_0_13426_x3709_x287867408}

[[本机环回次数超过]{style="font-family:宋体"}[6]{lang="EN-US"}]{#struct_0_13426_x3709_x2013355201}[次，就丢弃报文]{style="font-family:宋体"}

[[Incorrect VXLAN header.]{lang="EN-US"}]{#struct_0_13426_x3709_1038180726}

[[VXLAN]{lang="EN-US"}]{#struct_0_13426_x3709_x1242884870}[报文头错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[debugging vxlan tunnel packet]{lang="EN-US"}]{#struct_0_13426_x3709_1998842999}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x374693949}[[字段]{style="font-family:黑体"}]{#struct_0_13426_x3709_x1401267675}

[[描述]{style="font-family:黑体"}]{#struct_0_13426_x3709_x717166235}

[[Tunnel*number* packet: After de-encapsulation, length is *length*]{lang="EN-US"}]{#struct_0_13426_x3709_x1826112688}

[[隧道]{style="font-family:宋体"}[Tunnel*number*]{lang="EN-US"}]{#struct_0_13426_x3709_x1091347998}[报文处理：解封装后，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Tunnel*number* packet: After encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_13426_x3709_x1798104803}

[[隧道]{style="font-family:宋体"}[Tunnel*number*]{lang="EN-US"}]{#struct_0_13426_x3709_1045311917}[报文处理：加封装后，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Before de-encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_13426_x3709_x931743595}

[[解封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_13426_x3709_x1401333211}[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13426_x3709_x277852454}

[[\# ]{lang="EN-US"}]{#struct_0_13426_x3709_1743318068}[打开本端的]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[报文调试信息开关。在两台设备之间建立]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[隧道，并分别配置参数使隧道接口]{style="font-family:宋体"}[up]{lang="EN-US"}[。在接收端收到一个经过]{style="font-family:宋体"}[VXLAN]{lang="EN-US"}[加封装的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vxlan tunnel packet]{lang="EN-US"}]{#struct_0_13426_x3709_x345904942}

[\*Sep  6 11:49:46:053 2011 Sysname VXLAN/7/packet: -MDC=1;]{lang="EN-US"}

[ Before de-encapsulation,]{lang="EN-US"}

[   1.1.1.2-\>1.1.1.1 (length = 120)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x2041561277}*[接收到的报文解封装前，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[120]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 11:49:46:053 2011 Sysname VXLAN/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_13426_x3709_2125102535}

[ Tunnel0 packet: After de-encapsulation, length is 84]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13426_x3709_x128839631}*[接收到的报文解封装后，报文长度为]{style="font-family:宋体"}[84]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[]{#_Toc277669731}[]{#_Toc277669732}[]{#_Toc277669735}[]{#_Toc277669736}[]{#_Toc277669737}[]{#_Toc277669738}[]{#_Toc277669739}[]{#_Toc277669740}[]{#_Toc277669741}[]{#_Toc277669742}[]{#_Toc277669743}[]{#_Toc277669744}[]{#_Toc277669745}[]{#_Toc277669746}[]{#_Toc277669795}[]{#_Toc277669796}[]{#_Toc277669824}[]{#_Toc277669825}[]{#_Toc277669845}[]{#_Toc277669846}[]{#_Toc277669865}[]{#_Toc277669866}[]{#_Toc277669867}[]{#_Toc277669868}[]{#_Toc277669869}[]{#_Toc277669871}[]{#_Toc277669872}[]{#_Toc277669873}[]{#_Toc277669874}[]{#_Toc277669879}[]{#_Toc277669883}[]{#_Toc277669887}[]{#_Toc277669888}[]{#_Toc277669891}[]{#_Toc277669892}[]{#_Toc277669894}[]{#_Toc277669899}[]{#_Toc277669900}[]{#_Toc277669901}[]{#_Toc277669902}[]{#_Toc277669903}[]{#_Toc277669904}[]{#_Toc277669905}[]{#_Toc277669906}[]{#_Toc277669907}[]{#_Toc277669908}[]{#_Toc277669910}[]{#_Toc277669912}[]{#_Toc277669916}[]{#_Toc277669920}[]{#_Toc277669921}[]{#_Toc277669924}[]{#_Toc277669925}[]{#_Toc277669926}[]{#_Toc277669927}[]{#_Toc277669930}[]{#_Toc277669931}[]{#_Toc277669932}[]{#_Toc277669933}[]{#_Toc277669934}[]{#_Toc277669935}[]{#_Toc277669936}[]{#_Toc277669937}[]{#_Toc277669938}[]{#_Toc277669939}[]{#_Toc277669940}[]{#_Toc277669941}[]{#_Toc277669990}[]{#_Toc277669991}[]{#_Toc277670043}[]{#_Toc277670044}[]{#_Toc277670067}[]{#_Toc277670068}[]{#_Toc277670087}[]{#_Toc277670088}[]{#_Toc277670089}[]{#_Toc277670090}[]{#_Toc277670091}[]{#_Toc277670092}[]{#_Toc277670095}[]{#_Toc277670097}[]{#_Toc277670098}[]{#_Toc277670099}[]{#_Toc277670100}[]{#_Toc277670105}[]{#_Toc277670109}[]{#_Toc277670115}[]{#_Toc277670119}[]{#_Toc277670122}[]{#_Toc277670127}[]{#_Toc277670128}[]{#_Toc277670129}[]{#_Toc277670131}[]{#_Toc277670133}[]{#_Toc277670134}[]{#_Toc277670138}[]{#_Toc277670139}[]{#_Toc277670140}[]{#_Toc277670141}[]{#_Toc277670142}[]{#_Toc277670143}[]{#_Toc277670144}[]{#_Toc277670145}[]{#_Toc277670149}[]{#_Toc277670150}[]{#_Toc277670153}[]{#_Toc277670157}[]{#_Toc277670161}[]{#_Toc277670162}[ ]{lang="EN-US"}
