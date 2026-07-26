::: {#806804351 .myid}
[]{#_Toc404784249}[]{#struct_0_x4270_11236_219407577}[]{#_Toc175457893}[]{#_Toc287608520}[]{#_Toc205804228}

**VLAN终结 \-- VLAN终结调试命令 \-- debugging vlan-termination**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4270_11236_1651616260}

[**[debugging ]{lang="EN-US"}**]{#struct_0_x4270_11236_1736534310}**[vlan-termination]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **all** \| **error** \| **event** \| **packet** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}

[**[undo debugging ]{lang="EN-US"}**]{#struct_0_x4270_11236_1026245130}**[vlan-termination]{lang="EN-US"}[ ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4270_11236_x1586112946}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4270_11236_x305094838}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4270_11236_1195754219}

[[network-admin]{lang="EN-US"}]{#struct_0_x4270_11236_x1474024775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4270_11236_x980195408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4270_11236_x1986884754}

[**[all]{lang="EN-US"}**]{#struct_0_x4270_11236_219473113}[：表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的所有调试开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x4270_11236_x1047668877}[：表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的错误调试开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x4270_11236_x1024754057}[：表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的事件调试开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x4270_11236_2131118859}[：表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的报文调试开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_x4270_11236_x129651444}*[ interface-type interface-number]{lang="EN-US"}*[：指定的接口类型和编号。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4270_11236_x1198164423}

[**[debugging vlan-termination]{lang="EN-US"}**]{#struct_0_x4270_11236_x1351477899}[命令用来打开]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[终结的调试开关。]{style="font-family:宋体"}**[undo debugging  vlan-termination]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结的调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_x4270_11236_x610774474}[VLAN]{lang="EN-US"}[终结的所有调试开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging vlan-termination]{lang="EN-US"}]{#struct_0_x4270_11236_1901897004}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1117312014}[[字段]{style="font-family:黑体"}]{#struct_0_x4270_11236_219538649}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4270_11236_2034578630}

[*[interface-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x4270_11236_1735306642}

[*[state1 ]{lang="EN-US"}*[to unique dot1q, DRV modify interface, VLAN ID *VID* ]{lang="EN-US"}]{#struct_0_x4270_11236_1142107147}

[[创建]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_527236276}[接口，接口状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[切换到]{style="font-family:宋体"}[unique dot1q]{lang="EN-US"}[，]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动，下驱动时使用的]{style="font-family:宋体"}*[VID]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface-name]{lang="EN-US"}]{#struct_0_x4270_11236_x1146745502}[表示接口名，形如：]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[state1]{lang="EN-US"}]{#struct_0_x4270_11236_2081087017}[接口原来的终结类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VID]{lang="EN-US"}]{#struct_0_x4270_11236_219604185}[表示当前子接口的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x4270_11236_x363735146}

[*[state1]{lang="EN-US"}*[ to *unique qinq*, DRV modify interface, the first VLAN ID is *VID1*, and the second VLAN ID is *VID2*]{lang="EN-US"}]{#struct_0_x4270_11236_2011850858}

[[创建]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_1963937}[接口，接口状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[切换到]{style="font-family:宋体"}[unique qinq]{lang="EN-US"}[，]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_x48139195}[表示接口名，形如：]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1.0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[state1]{lang="EN-US"}*]{#struct_0_x4270_11236_1349892393}[接口原来的终结类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[VID1]{lang="EN-US"}*]{#struct_0_x4270_11236_1876908447}[表示当前子接口的外层]{style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VID2]{lang="EN-US"}*]{#struct_0_x4270_11236_219669721}[表示当前子接口的内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x4270_11236_x1595031286}

[*[state1]{lang="EN-US"}*[ to ambiguous dot1q (ambiguous qinq), DRV modify interface, the number of nodes is *NUM*]{lang="EN-US"}]{#struct_0_x4270_11236_1564481446}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_2117453790}[接口状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[切换到]{style="font-family:宋体"}[ambiguous dot1q]{lang="EN-US"}[或者]{style="font-family:宋体"}[ambiguous qinq]{lang="EN-US"}[，接口生成一个]{style="font-family:宋体"}*[NUM]{lang="EN-US"}[个]{style="font-family:宋体"}*[节点的链表]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x4270_11236_x961307824}

[*[state1]{lang="EN-US"}*[ to untagged (default/none), DRV modify interface]{lang="EN-US"}]{#struct_0_x4270_11236_219735257}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_410214992}[接口状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[切换到]{style="font-family:宋体"}[untagged]{lang="EN-US"}[、]{style="font-family:宋体"}[default]{lang="EN-US"}[或者]{style="font-family:宋体"}[none]{lang="EN-US"}

[[DRV create interface *interface-name*, which is not bound]{lang="EN-US"}]{#struct_0_x4270_11236_x899799045}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_x1363014447}[接口被创建时不是绑定的]{style="font-family:宋体"}

[[DRV create interface *interface-name,* which is bound to first is VLAN ID *VID*]{lang="EN-US"}]{#struct_0_x4270_11236_x1769309916}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_218752217}[接口被创建时是绑定的，]{style="font-family:宋体"}[VID]{lang="EN-US"}[表示绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[DRV destroy interface *interface-name,* whose config is none]{lang="EN-US"}]{#struct_0_x4270_11236_x113933857}[（]{style="font-family:宋体"}[default/untagged]{lang="EN-US"}[）]{style="font-family:宋体"}

[[删除]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_472479022}[接口，删除之前的配置为]{style="font-family:宋体"}[none]{lang="EN-US"}[（]{style="font-family:宋体"}[default/untagged]{lang="EN-US"}[）]{style="font-family:宋体"}

[[DRV destroy interface *interface-name,* whose config is unique dot1q, VLAN ID *VID*]{lang="EN-US"}]{#struct_0_x4270_11236_x1300553921}

[[删除]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_x80920779}[接口，删除之前的配置为]{style="font-family:宋体"}[unique dot1q]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[VID]{lang="EN-US"}*

[[DRV destroy interface *interface-name,* whose config is ambiguous dot1q: the number of nodes is *NUM*]{lang="EN-US"}]{#struct_0_x4270_11236_218817753}

[[删除]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_66504798}[接口，删除之前的配置为]{style="font-family:宋体"}[ambiguous dot1q]{lang="EN-US"}[，模糊终结节点的个数]{style="font-family:宋体"}*[NUM]{lang="EN-US"}*

[[DRV destroy interface *interface-name*, whose config is unique qinq: the first VLAN ID is *VID1*, and the second VLAN ID is *VID2*]{lang="EN-US"}]{#struct_0_x4270_11236_171852968}

[[删除]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_x2005191482}[接口，删除之前的配置为]{style="font-family:宋体"}*[unique qinq]{lang="EN-US"}*[，]{style="font-family:宋体"}*[VID1]{lang="EN-US"}*[表示]{style="font-family:宋体"}[unique qinq]{lang="EN-US"}[的第一层]{style="font-family:宋体"}[VLAN ID, *VID2*]{lang="EN-US"}[表示]{style="font-family:宋体"}*[unique qinq]{lang="EN-US"}*[的第二层的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[DRV destroy interface *interface-name,* whose config is ambiguous qinq: the first VLAN ID is *VID,* and the number of nodes is *NUM*]{lang="EN-US"}]{#struct_0_x4270_11236_x33807403}

[[删除]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_219276502}[接口，删除之前的配置为]{style="font-family:宋体"}[ambiguous qinq]{lang="EN-US"}[，]{style="font-family:宋体"}*[VID]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ambiguous qinq]{lang="EN-US"}[的第一层]{style="font-family:宋体"}[VLAN ID, ]{lang="EN-US"}[模糊终结节点的个数]{style="font-family:宋体"}*[NUM]{lang="EN-US"}*

[[*[interface-name]{lang="EN-US"}*]{.TableTextChar}[:]{lang="EN-US"}]{#struct_0_x4270_11236_x1334990368}

[[OUT packet, len [*length*]{.TableTextChar}]{lang="EN-US"}]{#struct_0_x4270_11236_804745130}

[*[context]{lang="EN-US"}*]{#struct_0_x4270_11236_475517334}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_219342038}[接口发送一个报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，报文内容为]{style="font-family:宋体"}*[context]{lang="EN-US"}*

[[*[interface-name]{lang="EN-US"}*]{.TableTextChar}[:]{lang="EN-US"}]{#struct_0_x4270_11236_1434930344}

[[IN packet, len [*length*]{.TableTextChar}]{lang="EN-US"}]{#struct_0_x4270_11236_x1618996232}

[*[context]{lang="EN-US"}*]{#struct_0_x4270_11236_x1508924588}

[*[interface-name]{lang="EN-US"}*]{#struct_0_x4270_11236_219407574}[接口接收一个报文，报文长度为]{style="font-family:宋体"}[length]{lang="EN-US"}[，报文内容为]{style="font-family:宋体"}*[context]{lang="EN-US"}*

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](VLAN终结Debug.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4270_11236_1651616257}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[接口有]{lang="EN-US" style="font-family:
KaiTi_GB2312"}[7]{lang="EN-US"}]{#struct_0_x4270_11236_1736206633}[种状态]{lang="EN-US" style="font-family:KaiTi_GB2312"}[none]{lang="EN-US"}[、]{lang="EN-US" style="font-family:KaiTi_GB2312"}[default]{lang="EN-US"}[、]{lang="EN-US" style="font-family:KaiTi_GB2312"}[untagged]{lang="EN-US"}[、]{lang="EN-US" style="font-family:KaiTi_GB2312"}[unique dot1q]{lang="EN-US"}[、]{lang="EN-US" style="font-family:KaiTi_GB2312"}[unique qinq]{lang="EN-US"}[、]{lang="EN-US" style="font-family:KaiTi_GB2312"}[ambiguous dot1q]{lang="EN-US"}[和]{lang="EN-US" style="font-family:KaiTi_GB2312"}[ambiguous qinq]{lang="EN-US"}[，默认状态为]{lang="EN-US" style="font-family:KaiTi_GB2312"}[none]{lang="EN-US"}[。]{lang="EN-US" style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4270_11236_625945637}

[[\# ]{lang="EN-US"}]{#struct_0_x4270_11236_1077169005}[打开]{style="font-family:宋体"}[debug]{lang="EN-US"}[开关，创建子接口]{style="font-family:宋体"}[GigabitEthernet1/0/]{lang="EN-US"}[1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[终结功能。]{style="font-family:宋体"}

[[\<Sysname\> debugging vlan-termination all]{lang="EN-US"}]{#struct_0_x4270_11236_x1599530123}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:]{lang="EN-US"}

[DRV create interface GigabitEthernet1/0/1.1, which is not bound]{lang="EN-US"}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x4270_11236_1012954622}*[创建子接口]{style="font-family:
宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q untagged]{lang="EN-US"}]{#struct_0_x4270_11236_219473110}

[\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[    none  to untagged, DRV modify interface]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x4270_11236_x1047668878}[ ]{lang="EN-US"}*[配置子接口为]{style="font-family:
宋体"}[untagged]{lang="EN-US"}[，控制平面利用]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 1]{lang="EN-US"}]{#struct_0_x4270_11236_1253790604}

[\*Feb 24 10:34:57:804 2023 Sysname ETH/7/EVENT:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[    untagged to unique dot1q, DRV modify interface, VLAN ID 0x1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_1466180784}*[配置子接口的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，控制平面利用]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 1 second-dot1q 3]{lang="EN-US"}]{#struct_0_x4270_11236_x1707715675}

[\*Mar 26 17:07:25:156 2008 Sysname ETH/7/EVENT:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[    unique dot1q to unique qinq, DRV modify interface, the first VLAN ID is 0x1]{lang="EN-US"}[，]{style="font-family:宋体"}[ and the second VLAN ID is 0x3]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_497963015}*[配置接口的明确]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[，控制平面利用]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 1 second-dot1q 10 12]{lang="EN-US"}]{#struct_0_x4270_11236_219538646}

[\*Mar 26 17:07:25:156 2008 Sysname ETH/7/EVENT:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[    unique qinq to ambiguous qinq, DRV modify interface, the number of nodes is 3]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_2034578621}*[配置接口的模糊]{style="font-family:宋体"}[QinQ]{lang="EN-US"}[，控制平面利用]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] undo vlan-type dot1q vid 1 second-dot1q 3 10 12]{lang="EN-US"}]{#struct_0_x4270_11236_1735372179}

[\*Feb 24 10:50:19:644 2023 Sysname ETH/7/EVENT:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[    ambiguous qinq  to none, DRV modify interface]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x4270_11236_x35914124}[ ]{lang="EN-US"}*[配置子接口为]{style="font-family:
宋体"}[none]{lang="EN-US"}[，控制平面利用]{style="font-family:宋体"}[modify]{lang="EN-US"}[下驱动]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] vlan-type dot1q vid 1 second-dot1q 13]{lang="EN-US"}]{#struct_0_x4270_11236_x314278553}

[\[Sysname-GigabitEthernet1/0/1.1\] ip address 12.1.1.2 255.255.255.0]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.1\] ping -c 1 12.1.1.1]{lang="EN-US"}

[\*Mar 26 17:27:52:609 2008 Sysname ETH/7/PACKET:]{lang="EN-US"}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[     OUT packet,len 50]{lang="EN-US"}

[    ff ff ff ff ff ff 00 e0 14 03 32 00 81 00 00 01]{lang="EN-US"}

[    81 00 00 0d 08 06 00 01 08 00 06 04 00 01 00 e0]{lang="EN-US"}

[    14 03 32 00 0c 01 01 02 00 00 00 00 00 00 0c 01]{lang="EN-US"}

[    01 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_219604182}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[发送一个长度为]{style="font-family:宋体"}[50]{lang="EN-US"}[的广播报文，报文的内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[13]{lang="EN-US"}[，外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Mar 26 17:27:52:671 2008 Sysname ETH/7/PACKET:]{lang="EN-US"}]{#struct_0_x4270_11236_x363735149}

[ GigabitEthernet1/0/1:]{lang="EN-US"}

[     IN packet,len 50]{lang="EN-US"}

[    00 e0 14 03 32 00 00 e0 14 03 28 00 81 00 00 01]{lang="EN-US"}

[    81 00 00 0d 08 06 00 01 08 00 06 04 00 02 00 e0]{lang="EN-US"}

[    14 03 28 00 0c 01 01 01 00 e0 14 03 32 00 0c 01]{lang="EN-US"}

[    01 02]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_2012440682}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的一个长度为]{style="font-family:宋体"}[50]{lang="EN-US"}[的单播报文，报文带有双层]{style="font-family:宋体"}[VLAN TAG]{lang="EN-US"}[，内层为]{style="font-family:宋体"}[13]{lang="EN-US"}[，外层为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Mar 26 17:27:52:671 2008 Sysname ETH/7/PACKET:]{lang="EN-US"}]{#struct_0_x4270_11236_635173152}

[ GigabitEthernet1/0/1.1:]{lang="EN-US"}

[     IN packet,len 42]{lang="EN-US"}

[    00 e0 14 03 32 00 00 e0 14 03 28 00 08 06 00 01]{lang="EN-US"}

[    08 00 06 04 00 02 00 e0 14 03 28 00 0c 01 01 01]{lang="EN-US"}

[    00 e0 14 03 32 00 0c 01 01 02]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_x921529876}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.1]{lang="EN-US"}[收到一个长度为]{style="font-family:宋体"}[42]{lang="EN-US"}[的单播报文，此时报文的]{style="font-family:宋体"}[VLAN TAG]{lang="EN-US"}[已经被去掉]{style="font-family:宋体"}*

[[\[Sysname-GigabitEthernet1/0/1.1\] quit]{lang="EN-US"}]{#struct_0_x4270_11236_219669718}

[\[Sysname\] undo interface gigabitethernet 1/0/1.1]{lang="EN-US"}

[\*Mar 26 17:07:25:156 2008 Sysname SIFVLAN/7/EVENT:]{lang="EN-US"}

[DRV destroy interface GigabitEthernet1/0/1.1, whose config is unique qinq: the first VLAN ID is 0x1, and the second VLAN ID is 0xd]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4270_11236_361283841}*[删除子接口]{style="font-family:宋体"}*
