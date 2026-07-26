::: {#-518441501 .myid}
[]{#_Toc404784762}[]{#struct_0_x1776_15264_x995380350}[]{#_Toc355345082}[]{#_Toc87257691}

**二层转发调试命令 \-- 普通二层转发 \-- debugging mac-forwarding**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x1316018743}

[**[debugging mac-forwarding]{lang="EN-US"}**[ { **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1776_15264_x753567973}

[**[undo debugging mac-forwarding]{lang="EN-US"}**[ { **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1776_15264_x907034063}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x635649304}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1776_15264_1342444305}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x370219210}

[**[error]{lang="EN-US"}**]{#struct_0_x1776_15264_380168297}[：表示二层转发错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1776_15264_18625145}[：表示二层转发报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x1907222920}

[**[debugging mac-forwarding]{lang="EN-US"}**]{#struct_0_x1776_15264_x1375594996}[命令用来打开]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[转发调试开关。]{style="font-family:宋体"}**[undo debugging mac-forwarding]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[转发调试开关。]{style="font-family:宋体"}

[[缺省情况下，调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1776_15264_x1598705336}

[[表1-1 ]{lang="EN-US"}[debugging mac-forwarding]{lang="EN-US"}]{#struct_0_x1776_15264_x827412907}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1519178207}[[字段]{style="font-family:黑体"}]{#struct_0_x1776_15264_1614801550}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1776_15264_1240305542}

[[Receiving]{lang="EN-US"}]{#struct_0_x1776_15264_x370153674}

[[接收报文]{style="font-family:宋体"}]{#struct_0_x1776_15264_1143436946}

[[Sending]{lang="EN-US"}]{#struct_0_x1776_15264_963545004}

[[发送报文]{style="font-family:宋体"}]{#struct_0_x1776_15264_1375220282}

[[Deliver]{lang="EN-US"}]{#struct_0_x1776_15264_1256469825}

[[将报文上送到上层]{style="font-family:宋体"}]{#struct_0_x1776_15264_1242780876}

[[vlan]{lang="EN-US"}]{#struct_0_x1776_15264_1763656572}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1776_15264_x370743499}[发送报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[interface]{lang="EN-US"}]{#struct_0_x1776_15264_1531410246}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1776_15264_1140790418}[发送报文的接口]{style="font-family:宋体"}

[[payload ]{lang="EN-US"}]{#struct_0_x1776_15264_x2107686026}

[[报文信息，以]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_x1776_15264_x370677963}[进制格式打印前]{style="font-family:宋体"}[64]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[Discarding]{lang="EN-US"}]{#struct_0_x1776_15264_1125861834}

[[报文被丢弃]{style="font-family:宋体"}]{#struct_0_x1776_15264_1477486452}

[[Sending interface STP status is not forwarding. Packet discarded.]{lang="EN-US"}]{#struct_0_x1776_15264_x381554656}

[[发送接口的]{style="font-family:宋体"}[STP]{lang="EN-US"}]{#struct_0_x1776_15264_1349764745}[状态不为]{style="font-family:宋体"}[forwarding]{lang="EN-US"}[。丢弃报文]{style="font-family:宋体"}

[[The output interface is down. Packet discarded.]{lang="EN-US"}]{#struct_0_x1776_15264_x370612427}

[[发送接口物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1776_15264_1349764743}[。丢弃报文]{style="font-family:宋体"}

[[Unknown unicast, broadcast or multicast packet discarded by frame action.]{lang="EN-US"}]{#struct_0_x1776_15264_x96077540}

[[当目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1776_15264_x1115264914}[为未知、广播、组播时丢弃报文]{style="font-family:宋体"}

[[Frame discarded for Destination MAC is Drop.]{lang="EN-US"}]{#struct_0_x1776_15264_x370546891}

[[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1776_15264_1526775307}[为丢弃类型，丢弃报文]{style="font-family:宋体"}

[[Frame discarded for VLAN tag is invalid.]{lang="EN-US"}]{#struct_0_x1776_15264_x1683696211}

[[VLAN tag]{lang="EN-US"}]{#struct_0_x1776_15264_x488100396}[无效丢弃报文]{style="font-family:宋体"}

[[Frame discarded by invalid MAC address.]{lang="EN-US"}]{#struct_0_x1776_15264_785663072}

[[MAC]{lang="EN-US"}]{#struct_0_x1776_15264_x371005643}[地址无效丢弃报文]{style="font-family:宋体"}

*[ ]{lang="EN-US"}*

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x442409112}

[[\# ]{lang="EN-US"}]{#struct_0_x1776_15264_862912}[打开转发报文调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-forwarding packet]{lang="EN-US"}]{#struct_0_x1776_15264_x932711411}

[\*Aug  3 05:12:33:619 2013 Sysname MACFW/7/MACFW_PACKET:]{lang="EN-US"}

[Sending, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01]{lang="EN-US"}

[08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01]{lang="EN-US"}

[00 00 00 00 00 00 C0 A8 28 CA 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt : Sending an ethernet frame.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_x370940107}*[本地接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送报文]{style="font-family:宋体"}*

[[\*Aug  3 05:12:33:621 2013 Sysname MACFW/7/MACFW_PACKET:]{lang="EN-US"}]{#struct_0_x1776_15264_1906246372}

[Receiving, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 1C BD B9 E3 BD BB 00 26 E0 E0]{lang="EN-US"}

[03 FF FF 00 22 00 00 00 00 00 00 FF FF FF FF FF]{lang="EN-US"}

[FF 04 52 00 00 00 00 1C BD B9 E3 BD BB 40 00 00]{lang="EN-US"}

[03 00 04 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt : Receiving an ethernet frame.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_125701475}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到报文]{style="font-family:宋体"}*

[[\*Aug  3 05:12:33:622 2013 Sysname MACFW/7/MACFW_PACKET:]{lang="EN-US"}]{#struct_0_x1776_15264_x370874571}

[Delivering, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01]{lang="EN-US"}

[08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01]{lang="EN-US"}

[00 00 00 00 00 00 C0 A8 28 66 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt: Deliver packet to layer2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_x838478484}*[将接收的报文送到上层处理]{style="font-family:宋体"}*

[[\*Aug  3 05:12:33:623 2013 Sysname MACFW/7/MACFW_PACKET:]{lang="EN-US"}]{#struct_0_x1776_15264_1959823219}

[Discarding, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01]{lang="EN-US"}

[08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01]{lang="EN-US"}

[00 00 00 00 00 00 C0 A8 28 66 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt: Sending interface STP status is not forwarding. Packet discarded.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_x839465417}*[发送接口的]{style="font-family:宋体"}[STP]{lang="EN-US"}[状态为]{style="font-family:宋体"}[discarding]{lang="EN-US"}[将报文丢弃]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1776_15264_1621793675}[打开转发报文调试开关。]{style="font-family:宋体"}

[[\<Sysname\>debugging mac-forwarding error]{lang="EN-US"}]{#struct_0_x1776_15264_x1275031224}

[\*Aug  3 05:12:34:619 2013 Sysname MACFW/7/MACFW_ERROR:]{lang="EN-US"}

[prompt: Frame discarded by invalid MAC address.]{lang="EN-US"}

[*[// MAC]{lang="EN-US"}*]{#struct_0_x1776_15264_x1240255776}*[地址无效]{style="font-family:宋体"}*

::::: {#-813413176 .myid}
[]{#_Toc404784764}[]{#struct_0_x1776_15264_769190289}[]{#_Toc355345090}[]{#_Toc352334627}[]{#_Toc207446736}[]{#_Toc207445113}[]{#_Toc207444972}

**二层转发调试命令 \-- Bridge转发 \-- debugging bridge**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](二层转发Debug.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1776_15264_973231824}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1776_15264_839243809}
:::

[ ]{lang="EN-US"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x1432826637}

[**[debugging bridge ]{lang="EN-US"}**[{ **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1776_15264_884505380}

[**[undo debugging bridge ]{lang="EN-US"}**[{ **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1776_15264_738322628}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x813938968}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1776_15264_x370219211}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1776_15264_380102761}

[**[all]{lang="EN-US"}**]{#struct_0_x1776_15264_x52790984}[：表示]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[转发所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1776_15264_580655915}[：表示]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[转发错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1776_15264_1878797507}[：表示]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[转发报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x129467475}

[**[debugging ]{lang="EN-US"}[bridge]{lang="EN-US"}**]{#struct_0_x1776_15264_1945275586}[命令用来打开或关闭]{style="font-family:宋体"}[bridge]{lang="EN-US"}[转发调试开关。]{style="font-family:宋体"}

[[缺省情况下，调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1776_15264_x676141505}

[[表1-2 ]{lang="EN-US"}[debugging bridge]{lang="EN-US"}]{#struct_0_x1776_15264_669945184}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1535540969}[[字段]{style="font-family:黑体"}]{#struct_0_x1776_15264_x370153675}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1776_15264_1143371410}

[[Receiving]{lang="EN-US"}]{#struct_0_x1776_15264_x1080182635}

[[接收报文]{style="font-family:宋体"}]{#struct_0_x1776_15264_1288935038}

[[Sending]{lang="EN-US"}]{#struct_0_x1776_15264_x266224303}

[[发送报文]{style="font-family:宋体"}]{#struct_0_x1776_15264_23917326}

[[vlan]{lang="EN-US"}]{#struct_0_x1776_15264_2138267482}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1776_15264_x774028029}[发送报文的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[interface]{lang="EN-US"}]{#struct_0_x1776_15264_x550871868}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1776_15264_x258572689}[发送报文的接口]{style="font-family:宋体"}

[[payload]{lang="EN-US"}]{#struct_0_x1776_15264_x864089796}

[[报文信息，以]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_x1776_15264_x773962493}[进制格式打印前]{style="font-family:宋体"}[64]{lang="EN-US"}[字节]{style="font-family:宋体"}

[[Discarding]{lang="EN-US"}]{#struct_0_x1776_15264_x2061505504}

[[报文被丢弃]{style="font-family:宋体"}]{#struct_0_x1776_15264_149635132}

[[The packet is handling or discarded by service process!]{lang="EN-US"}]{#struct_0_x1776_15264_x773831421}

[[报文被业务进程处理或丢弃]{style="font-family:宋体"}]{#struct_0_x1776_15264_x1649635735}

[[Frame discarded for Bridge is not found!]{lang="EN-US"}]{#struct_0_x1776_15264_88321013}

[[根据]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1776_15264_348819851}[未找到]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[的帧被丢弃]{style="font-family:宋体"}

[[Frame discarded by invalid MAC address!]{lang="EN-US"}]{#struct_0_x1776_15264_29215226}

[[MAC]{lang="EN-US"}]{#struct_0_x1776_15264_x774290173}[地址无效的帧被丢弃]{style="font-family:宋体"}

[[Frame discarded because of incorrect encapsulation type for the POS interface.]{lang="EN-US"}]{#struct_0_x1776_15264_x1995817653}

[[POS]{lang="EN-US"}]{#struct_0_x1776_15264_1874422681}[口丢弃收到的链路层封装类型不正确的帧]{style="font-family:宋体;color:#1F497D"}

[[Invalid frame was discarded.]{lang="EN-US"}]{#struct_0_x1776_15264_733065702}

[[丢弃非法链路层报文]{style="font-family:宋体"}]{#struct_0_x1776_15264_530291872}

[[Sending an ethernet frame.]{lang="EN-US"}]{#struct_0_x1776_15264_1677047477}

[[发送一个以太帧]{style="font-family:宋体"}]{#struct_0_x1776_15264_1074494484}

[[Receiving an ethernet frame.]{lang="EN-US"}]{#struct_0_x1776_15264_x777189641}

[[接收一个以太帧]{style="font-family:宋体"}]{#struct_0_x1776_15264_941090948}

[[Sending a PPP frame.]{lang="EN-US"}]{#struct_0_x1776_15264_1136350229}

[[发送一个]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x1776_15264_1437537600}[帧]{style="font-family:宋体"}

[[Receiving a PPP frame.]{lang="EN-US"}]{#struct_0_x1776_15264_1027978919}

[[接收一个]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x1776_15264_292083602}[帧]{style="font-family:宋体"}

[[Sending an HDLC frame.]{lang="EN-US"}]{#struct_0_x1776_15264_x1699594973}

[[发送一个]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_x1776_15264_x429733712}[帧]{style="font-family:宋体"}

[[Receiving an HDLC frame.]{lang="EN-US"}]{#struct_0_x1776_15264_x2058592435}

[[接收一个]{style="font-family:宋体"}[HDLC]{lang="EN-US"}]{#struct_0_x1776_15264_x742638790}[帧]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1776_15264_x2136473129}

[[\# ]{lang="EN-US"}]{#struct_0_x1776_15264_845547111}[打开所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging bridge all]{lang="EN-US"}]{#struct_0_x1776_15264_458738076}

[\*Aug  3 05:12:33:619 2013 Sysname BRIDGE/7/BRIDGE_PACKET:]{lang="EN-US"}

[Sending, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 00 0F 29 00 20 01 08 06 00 01]{lang="EN-US"}

[08 00 06 04 00 01 00 0F 29 00 20 01 C0 A8 28 01]{lang="EN-US"}

[00 00 00 00 00 00 C0 A8 28 CA 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt : Sending an ethernet frame]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_x774224637}*[本地接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送报文]{style="font-family:宋体"}*

[[\*Aug  3 05:12:33:621 2013 Sysname BRIDGE/7/BRIDGE_PACKET:]{lang="EN-US"}]{#struct_0_x1776_15264_x1782066105}

[Receiving, vlan = 2, interface = GigabitEthernet1/0/1, payload =]{lang="EN-US"}

[FF FF FF FF FF FF 1C BD B9 E3 BD BB 00 26 E0 E0]{lang="EN-US"}

[03 FF FF 00 22 00 00 00 00 00 00 FF FF FF FF FF]{lang="EN-US"}

[FF 04 52 00 00 00 00 1C BD B9 E3 BD BB 40 00 00]{lang="EN-US"}

[03 00 04 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[prompt : Receiving an ethernet frame]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_1512637366}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到报文]{style="font-family:宋体"}*

[[\*Aug  3 05:12:34:619 2013 Sysname BRIDGE/7/ BRIDGE_ERROR:]{lang="EN-US"}]{#struct_0_x1776_15264_x774159101}

[Frame discarded for Bridge is not found!]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1776_15264_x950343544}*[根据]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[未找到]{style="font-family:宋体"}[Bridge]{lang="EN-US"}[的帧被丢弃]{style="font-family:宋体"}*
