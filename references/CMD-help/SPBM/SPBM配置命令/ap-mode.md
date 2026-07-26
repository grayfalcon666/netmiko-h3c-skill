::: {#-1521777620 .myid}
[]{#_Toc326076027}[]{#_Toc326076011}[]{#_Toc404798162}[]{#struct_0_17931_14437_x1815210731}[]{#_Toc326076028}

**SPBM \-- SPBM配置命令 \-- ap-mode**

------------------------------------------------------------------------

[**[ap-mode]{lang="EN-US"}**]{#struct_0_17931_14437_2128573173}[命令用来配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[协议的运行模式。]{style="font-family:宋体"}

[**[undo ap-mode]{lang="EN-US"}**]{#struct_0_17931_14437_x2006612652}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1495065692}

[**[ap-mode ]{lang="EN-US"}**[{ **both** \| **multicast** \| **off** }]{lang="EN-US"}]{#struct_0_17931_14437_800044661}

[**[undo ap-mode]{lang="EN-US"}**]{#struct_0_17931_14437_x541448634}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x838552024}

[[AP]{lang="EN-US"}]{#struct_0_17931_14437_x761148504}[协议运行在]{style="font-family:宋体"}[both]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x419398680}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1815407339}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x305986648}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1580344583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x87478486}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1759237388}

[**[both]{lang="EN-US"}**]{#struct_0_17931_14437_2147480845}[：表示对单播表项、组播表项都进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[multicast]{lang="EN-US"}**]{#struct_0_17931_14437_1779840981}[：表示仅对组播表项进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[off]{lang="EN-US"}**]{#struct_0_17931_14437_641086470}[：表示关闭]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x303514860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPBN]{lang="EN-US"}]{#struct_0_17931_14437_x1815341803}[整网各节点独立收集拓扑信息，并进行独立计算。网络拓扑震荡时，各节点收敛速度可能不一致，导致各节点计算的速度不一致，网络瞬间可能形成环路。可通过]{style="font-family:宋体"}[AP]{lang="EN-US"}[协议来保证不出现临时环路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_17931_14437_x1037623733}[AP]{lang="EN-US"}[模式后，对应的表项在生效前需进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测，检测通过（即链路状态数据库同步完成）后，才能指导转发，检测不通过则表项不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1051406574}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1318623000}[配置]{style="font-family:宋体"}[AP]{lang="EN-US"}[协议运行在]{style="font-family:宋体"}[multicast]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1344813474}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] ap-mode multicast]{lang="EN-US"}
:::

::: {#-1541660845 .myid}
[]{#_Toc404798163}[]{#struct_0_17931_14437_249102913}

**SPBM \-- SPBM配置命令 \-- area-authentication send-only**

------------------------------------------------------------------------

[**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_x1815014123}[命令用来配置不对收到的报文（包括]{style="font-family:
宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:
宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）进行验证密码检查。]{style="font-family:宋体"}

[**[undo area-authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_1496680893}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2017503118}

[**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_213903}

[**[undo area-authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_1802725247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1355639444}

[[如果配置了区域验证方式和验证密码，则对收到的报文进行验证密码检查。]{style="font-family:宋体"}]{#struct_0_17931_14437_x1814948587}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2090864431}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_592853254}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x693564293}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1597372536}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_145452950}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1815145195}

[[配置区域验证方式和验证密码时如果没有配置本命令，则在发送的报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_655820666}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中按照]{style="font-family:宋体"}**[area-authentication-mode]{lang="EN-US"}**[命令指定的方式携带验证密码，并对收到的报文进行验证密码的检查，只有通过检查后，该报文中的路由信息才会加入到本地]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中。当需要更改密码时，由于两台设备的密码更改操作不完全同步，导致瞬时的密码不一致、业务中断。此时，可以通过配置不对收到的报文进行验证密码检查，保证业务不会中断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_756435885}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1060607247}[配置不对收到的报文进行验证密码检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_147620803}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] area-authentication send-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x439311850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_1174564252}
:::

::: {#702106844 .myid}
[]{#_Toc404798164}[]{#struct_0_17931_14437_x1815079659}

**SPBM \-- SPBM配置命令 \-- area-authentication-mode**

------------------------------------------------------------------------

[**[area-authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_1978373218}[命令用来配置区域验证方式和验证密码。]{style="font-family:宋体"}

[**[undo area-authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_x350508602}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x949315774}

[**[area-authentication-mode ]{lang="EN-US"}**[{ **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* }]{lang="EN-US"}]{#struct_0_17931_14437_x954420445}

[**[undo area-authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_1783886477}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1814751979}

[[没有配置区域验证方式和验证密码，不进行区域验证。]{style="font-family:宋体"}]{#struct_0_17931_14437_613459068}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1161688777}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_382447275}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x215608037}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2003077196}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1814686443}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2081861118}

[**[md5]{lang="EN-US"}**]{#struct_0_17931_14437_x1389014305}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17931_14437_742624774}[：简单验证模式。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17931_14437_452371841}[：表示以密文的形式输入密码。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_17931_14437_844350490}[：表示密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_17931_14437_x1815276266}[：表示以明文的形式输入密码。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_17931_14437_1448294029}[：表示明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_1956475306}

[[配置区域验证方式和验证密码后，将在发送的报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x1051206266}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中按照设定的方式携带验证密码，并对收到的报文进行验证密码的检查。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1815210730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一区域内的]{style="font-family:宋体"}]{#struct_0_17931_14437_x600310182}[SPBM]{lang="EN-US"}[设备必须配置相同的验证方式和验证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式配置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17931_14437_1362817304}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1135443199}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2044029249}[配置区域采用简单验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[，以明文形式输入密码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1815407338}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] area-authentication-mode simple plain 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x439573994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_3299096}
:::

::: {#679388335 .myid}
[]{#_Toc404798165}[]{#struct_0_17931_14437_x1872070589}

**SPBM \-- SPBM配置命令 \-- b-vlan**

------------------------------------------------------------------------

[**[b-vlan]{lang="EN-US"}**]{#struct_0_17931_14437_x1215946947}[命令用来为]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo b-vlan]{lang="EN-US"}**]{#struct_0_17931_14437_x1762393630}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_410461744}

[**[b-vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_136408442}

[**[undo b-vlan]{lang="EN-US"}**]{#struct_0_17931_14437_1860445754}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1047370314}

[[SPB VSI]{lang="EN-US"}]{#struct_0_17931_14437_2035958778}[实例未指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1815341802}

[[VSI SPB]{lang="EN-US"}]{#struct_0_17931_14437_1691259622}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_207568761}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1177784368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1984186641}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1727552159}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_x1067770771}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1520312986}

[[配置]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}]{#struct_0_17931_14437_407412244}[实例时必须为其指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，只有]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[都相同的]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例才能互通。]{style="font-family:宋体"}

[[需要注意的是，一个]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}]{#struct_0_17931_14437_x1815014122}[实例只能指定一个]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，不同]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例可以指定相同的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1232202462}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1649360019}[为]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[（]{style="font-family:宋体"}[I-SID 256]{lang="EN-US"}[）指定]{style="font-family:宋体"}[B-VLAN 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1014700711}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] spb i-sid 256]{lang="EN-US"}

[\[Sysname-vsi-vpn1-256\] b-vlan 100]{lang="EN-US"}
:::

::: {#1475841160 .myid}
[]{#_Toc326076030}[]{#_Toc404798166}[]{#struct_0_17931_14437_1276783101}

**SPBM \-- SPBM配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

[**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_17931_14437_1327343937}[命令用来配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[自动计算链路开销值时依据的带宽参考值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bandwidth-reference**]{lang="EN-US"}]{#struct_0_17931_14437_x796945961}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x419462056}

[**[bandwidth-reference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_17931_14437_x1814948586}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_17931_14437_638018924}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x668849837}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x803212915}[自动计算链路度量值时依据的带宽参考值为]{style="font-family:宋体"}[40000Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_272107401}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1269322993}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1007893790}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x897012146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1900297223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1815145194}

[*[value]{lang="EN-US"}*]{#struct_0_17931_14437_x910263275}[：带宽参考值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483648]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_1061123107}

[[当接口链路开销值和全局链路开销值都为缺省值时，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_940618110}[会自动计算接口链路的开销值。]{style="font-family:宋体"}

[[链路开销值的计算公式为"链路开销值＝（带宽参考值÷带宽）×]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_17931_14437_x1815079658}["，链路开销值的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x750510137}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1888219754}[配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[进程的带宽参考值为]{style="font-family:宋体"}[200Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1113897094}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] bandwidth-reference 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x438853098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[circuit-cost]{lang="EN-US"}**]{#struct_0_17931_14437_x438787562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm cost]{lang="EN-US"}**]{#struct_0_17931_14437_x749304605}
:::

::: {#110450494 .myid}
[]{#_Toc404798167}[]{#struct_0_17931_14437_x276417794}[]{#_Toc365969223}[]{#_Toc365969296}[]{#_Toc366584188}

**SPBM \-- SPBM配置命令 \-- bridge-priority**

------------------------------------------------------------------------

[**[bridge-priority]{lang="EN-US"}**]{#struct_0_17931_14437_520571277}[命令用来配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的桥优先级。]{style="font-family:宋体"}

[**[undo bridge-priority]{lang="EN-US"}**]{#struct_0_17931_14437_x1724044714}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1814751978}

[**[bridge-priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_17931_14437_x2115424287}

[**[undo bridge-priority]{lang="EN-US"}**]{#struct_0_17931_14437_x2049564036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_157610828}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_242585607}[的桥优先级为]{style="font-family:宋体"}[32768]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x948814552}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x172474527}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x437005075}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1018206885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1814686442}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_647022237}

[*[priority]{lang="EN-US"}*]{#struct_0_17931_14437_x1557266311}[：表示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的桥优先级，该数值越小表示优先级越高。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[61440]{lang="EN-US"}[之间]{style="font-family:宋体"}[4096]{lang="EN-US"}[的倍数，如]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[4096]{lang="EN-US"}[、]{style="font-family:宋体"}[8192]{lang="EN-US"}[等。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1109420834}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1943061817}[的桥优先级与设备的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[共同组成设备的桥]{style="font-family:宋体"}[ID]{lang="EN-US"}[。桥]{style="font-family:宋体"}[ID]{lang="EN-US"}[与]{style="font-family:宋体"}[ECT]{lang="EN-US"}[掩码进行异或操作，计算后的数值越小，则越优先选择该设备所在的转发路径来承载流量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1423030384}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1505899480}[配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的桥优先级为]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x187876260}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] bridge-priority 4096]{lang="EN-US"}
:::

::: {#188490618 .myid}
[]{#_Toc404798168}[]{#struct_0_17931_14437_x1815276269}

**SPBM \-- SPBM配置命令 \-- circuit-cost**

------------------------------------------------------------------------

[**[circuit-cost]{lang="EN-US"}**]{#struct_0_17931_14437_1045009502}[命令用来全局配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的链路开销值。]{style="font-family:宋体"}

[**[undo circuit-cost]{lang="EN-US"}**]{#struct_0_17931_14437_1720474953}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1295737068}

[**[circuit-cost]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_17931_14437_x1369715475}

[**[undo circuit-cost]{lang="EN-US"}**]{#struct_0_17931_14437_1217564844}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1758516970}

[[未全局配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1330538696}[的链路开销值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x677922471}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1815210733}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_965773759}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_625676945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x760990019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2020073049}

[*[value]{lang="EN-US"}*]{#struct_0_17931_14437_35499043}[：链路开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_670916964}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值参与]{style="font-family:宋体"}]{#struct_0_17931_14437_x606331014}[SPT]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Shortest Path Tree]{lang="EN-US"}[，最短路径树）]{lang="EN-US" style="font-family:宋体"}[的计算。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局配置的]{style="font-family:宋体"}]{#struct_0_17931_14437_x1733859910}[SPBM]{lang="EN-US"}[链路开销值将对所有]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[接口生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局和接口同时配置了]{style="font-family:宋体"}]{#struct_0_17931_14437_x1815407341}[SPBM]{lang="EN-US"}[的链路开销值时，优先选择接口的配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_50047104}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_352392112}[全局配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的链路开销值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_120168175}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] circuit-cost 11]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1482805846}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_17931_14437_1220853109}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm cost]{lang="EN-US"}**]{#struct_0_17931_14437_1482871382}
:::

::: {#-1476714212 .myid}
[]{#_Toc404798169}[]{#struct_0_17931_14437_83269694}[]{#_Toc365969226}[]{#_Toc365969299}[]{#_Toc366584191}

**SPBM \-- SPBM配置命令 \-- control-address**

------------------------------------------------------------------------

[**[control-address]{lang="EN-US"}**]{#struct_0_17931_14437_x882622874}[命令用来配置]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo control-address]{lang="EN-US"}**]{#struct_0_17931_14437_75783159}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_65176148}

[**[control-address]{lang="EN-US"}**[ { **all-cb** \| **all-is** \| **all-l1-is** \| **all-l2-is** \| **all-pb** }]{lang="EN-US"}]{#struct_0_17931_14437_1488307945}

[**[undo control-address]{lang="EN-US"}**]{#struct_0_17931_14437_x1815341805}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_125175681}

[[SPB IS-IS]{lang="EN-US"}]{#struct_0_17931_14437_102721807}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}**[all-pb]{lang="EN-US"}**[，对应]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-002E]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1114822907}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_735058663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x519549111}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2041053881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x299973966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_648464563}

[**[all-cb]{lang="EN-US"}**]{#struct_0_17931_14437_x1815014125}[：]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-002F]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-is]{lang="EN-US"}**]{#struct_0_17931_14437_333881479}[：]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0900-2B00-0005]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-l1-is]{lang="EN-US"}**]{#struct_0_17931_14437_385824956}[：]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-0014]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-l2-is]{lang="EN-US"}**]{#struct_0_17931_14437_1286556808}[：]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-0015]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-pb]{lang="EN-US"}**]{#struct_0_17931_14437_x2002296827}[：]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0180-C200-002E]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_740568428}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1814948589}[配置]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文的控制]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}**[all-is]{lang="EN-US"}**[，对应]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0900-2B00-0005]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x928065017}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] control-address all-is]{lang="EN-US"}[]{#_Toc326076035}[]{#_Toc323196009}[]{#_Toc323114953}[]{#_Toc287541528}
:::

::: {#-1607827180 .myid}
[]{#_Toc404798170}[]{#struct_0_17931_14437_1258726050}[]{#_Toc342496206}

**SPBM \-- SPBM配置命令 \-- display l2vpn minm connection**

------------------------------------------------------------------------

[**[display l2vpn minm connection]{lang="EN-US"}**]{#struct_0_17931_14437_x2031523565}[命令用来显示]{style="font-family:
宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_304933864}

[**[display l2vpn minm connection ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_17931_14437_1043914695}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1815145197}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1818620080}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1643903765}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1934567468}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1833388383}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1030205024}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1540410179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_727401296}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_17931_14437_x2019490631}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定该参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1815079661}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1621946250}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn minm connection]{lang="EN-US"}]{#struct_0_17931_14437_x1243788923}

[Total number of MinM connections: 6]{lang="EN-US"}

[Types: MC - multicast, UC - unicast]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 1]{lang="EN-US"}

[Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface]{lang="EN-US"}

[64       10001     9999-8888-7777  1234   SPB     UC    GE1/0/1]{lang="EN-US"}

[65       10001     9999-8988-7777  1234   SPB     UC    GE1/0/1]{lang="EN-US"}

[-        10001     0011-2222-3333  1234   SPB     MC    GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 2]{lang="EN-US"}

[Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface]{lang="EN-US"}

[68       10002     9999-8888-7777  1234   SPB     UC    GE1/0/1]{lang="EN-US"}

[69       10002     9999-8988-7777  1234   SPB     UC    GE1/0/1]{lang="EN-US"}

[-        10002     9999-9088-7777  1234   SPB     MC    GE1/0/1]{lang="EN-US"}

[                                                        GE1/0/2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display l2vpn minm connection]{lang="EN-US"}]{#struct_0_17931_14437_x279867656}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1461049515}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1814751981}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_258211748}

[[VSI name]{lang="EN-US"}]{#struct_0_17931_14437_608028776}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_x1518291074}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_17931_14437_1249469127}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_17931_14437_1674271943}[连接的链路标识符]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1889550159}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_17931_14437_x1814686445}

[[BMAC]{lang="EN-US"}]{#struct_0_17931_14437_x1275292064}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_921030500}[地址]{style="font-family:宋体"}

[[BVLAN]{lang="EN-US"}]{#struct_0_17931_14437_209355041}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17931_14437_824593486}

[[Owner]{lang="EN-US"}]{#struct_0_17931_14437_510102560}

[[表项生成者，取值为]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_17931_14437_x1815276268}[或]{style="font-family:宋体"}[SPB]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_17931_14437_x1683873853}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1439293186}[连接的属性标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MC]{lang="EN-US"}]{#struct_0_17931_14437_237404366}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UC]{lang="EN-US"}]{#struct_0_17931_14437_x1083663065}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17931_14437_x1815210732}

[[出接口]{style="font-family:宋体"}]{#struct_0_17931_14437_x1763109596}

[ ]{lang="EN-US"}

::: {#485530473 .myid}
[]{#_Toc404798171}[]{#struct_0_17931_14437_756506201}[]{#_Toc342496207}[]{#_Toc242067216}

**SPBM \-- SPBM配置命令 \-- display l2vpn minm forwarding**

------------------------------------------------------------------------

[**[display l2vpn minm forwarding]{lang="EN-US"}**]{#struct_0_17931_14437_604513148}[命令用来显示]{style="font-family:
宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x597255533}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_900563794}

[**[display l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_17931_14437_792502045}

[[分布式设备―独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_1549605469}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ ]{lang="EN-US"}]{#struct_0_17931_14437_x1815407340}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x1516036837}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* ]{lang="EN-US"}]{#struct_0_17931_14437_x32332938}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_228137586}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1874899283}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1793923732}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2125923915}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_278608209}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1025475009}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1815341804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1440908260}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_17931_14437_x293094627}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定该参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1679362129}[：显示指定单板上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示主控板上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备―独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x801029333}[：显示指定成员设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1569896370}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_1858537970}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主控板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1569568690}[：显示指定单板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主控板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_1005863998}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x256510932}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1661596265}[显示所有的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn minm forwarding]{lang="EN-US"}]{#struct_0_17931_14437_x1815014124}

[Total number of MinM connections: 6]{lang="EN-US"}

[Types: MC - multicast, UC - unicast]{lang="EN-US"}

[Status Flag: \* - inactive]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 1]{lang="EN-US"}

[Link ID I-SID     BMAC            BVLAN Owner Type Interface]{lang="EN-US"}

[64      10001     9999-8888-7777  1234  SPB   UC   GE1/0/1]{lang="EN-US"}

[65      10001     9999-8988-7777  1234  SPB   UC   GE1/0/1]{lang="EN-US"}

[-       10001     0011-2222-3333  1234  SPB   MC   GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 2]{lang="EN-US"}

[Link ID I-SID     BMAC            BVLAN Owner Type Interface]{lang="EN-US"}

[68      10002     9999-8888-7777  1234  SPB   UC   GE1/0/1]{lang="EN-US"}

[69      10002     9999-8988-7777  1234  SPB   UC   GE1/0/1]{lang="EN-US"}

[-       10002     9999-9088-7777  1234  SPB   MC   GE1/0/1]{lang="EN-US"}

[                                                   GE1/0/2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display l2vpn minm forwarding]{lang="EN-US"}]{#struct_0_17931_14437_1899965420}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1462398187}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_519812437}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_197532145}

[[VSI name]{lang="EN-US"}]{#struct_0_17931_14437_x1814948588}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1800818338}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_17931_14437_x2025535557}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_17931_14437_585779363}[连接的链路标识符]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_1555543782}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_17931_14437_238339748}

[[BMAC]{lang="EN-US"}]{#struct_0_17931_14437_x1815145196}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_252536139}[地址]{style="font-family:宋体"}

[[BVLAN]{lang="EN-US"}]{#struct_0_17931_14437_778935135}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17931_14437_19845672}

[[Owner]{lang="EN-US"}]{#struct_0_17931_14437_1364968835}

[[表项生成者，取值为]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_17931_14437_1204661708}[或]{style="font-family:宋体"}[SPB]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_17931_14437_x1815079660}

[[属性标记，取值包括：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1106937105}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MC]{lang="EN-US"}]{#struct_0_17931_14437_x1079045105}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UC]{lang="EN-US"}]{#struct_0_17931_14437_x239895929}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17931_14437_931306514}

[[出接口]{style="font-family:宋体"}]{#struct_0_17931_14437_x1814751980}

[[如果接口后面带有"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_17931_14437_1824295689}["，则表示该表项不生效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1007637280 .myid}
[]{#_Toc404798172}[]{#struct_0_17931_14437_1012061769}[]{#_Toc342496208}

**SPBM \-- SPBM配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

[**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_17931_14437_241209488}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1518783240}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_1662035694}**[l2vpn]{lang="EN-US"}**[ ]{lang="EN-US"}**[vsi]{lang="EN-US"}**[ \[]{lang="EN-US"}*[ ]{lang="EN-US"}***[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*[ ]{lang="EN-US"}[\] \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1173120309}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1814686444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1453591291}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2124656604}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1297727893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_834941445}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1922206348}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1284393712}

[**[name]{lang="EN-US"}**]{#struct_0_17931_14437_x1920728325}*[ vsi-name]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定该参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_62568236}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。如果未指定该参数，则显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_563995866}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2080004123}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_17931_14437_563930330}

[VSI Name: 0]{lang="EN-US"}

[  VSI Index               : 0]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : -]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  SPB I-SID               : 10000]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: 1]{lang="EN-US"}

[  VSI Index               : 1]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : -]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  SPB I-SID               : 10001]{lang="EN-US"}

[  SPB Connections:]{lang="EN-US"}

[    BMAC            BVLAN            Link ID    Type]{lang="EN-US"}

[    9999-8888-7777  1234             64         Unicast]{lang="EN-US"}

[    9999-8988-7777  1234             65         Unicast]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    BAGG1 srv1                       0          Down]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display l2vpn vsi]{lang="EN-US"}]{#struct_0_17931_14437_x1292142380}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1761057291}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1713075016}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x1795798568}

[[VSI Name]{lang="EN-US"}]{#struct_0_17931_14437_18765563}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_563864794}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_17931_14437_1431217935}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1803270025}[索引]{style="font-family:宋体"}

[[VSI Description]{lang="EN-US"}]{#struct_0_17931_14437_997073962}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_265369917}[的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}

[[VSI State]{lang="EN-US"}]{#struct_0_17931_14437_382814483}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_563799258}[的状态，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_17931_14437_x323490755}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17931_14437_x2106719909}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_17931_14437_1316353657}[：通过]{lang="EN-US" style="font-family:
  宋体"}**[shutdown]{lang="EN-US"}**[命令手工关闭]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_17931_14437_x1532975244}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_39290181}[上配置的最大传输单元]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_17931_14437_563733722}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1659610726}[的带宽限制值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[Broadcast Restrain]{lang="EN-US"}]{#struct_0_17931_14437_x772332340}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_x880546961}[的广播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播流量速率超出特定值（带宽限制值×广播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃广播报文]{style="font-family:宋体"}

[[Multicast Restrain]{lang="EN-US"}]{#struct_0_17931_14437_174730755}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_563668186}[的组播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的组播流量速率超出特定值（带宽限制值×组播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃组播报文]{style="font-family:宋体"}

[[Unknown Unicast Restrain]{lang="EN-US"}]{#struct_0_17931_14437_867602499}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_x872210174}[的未知单播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的未知单播流量速率超出特定值（带宽限制值×未知单播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃未知单播流量报文]{style="font-family:宋体"}

[[MAC Learning]{lang="EN-US"}]{#struct_0_17931_14437_x1275461162}

[[是否使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_563602650}[地址学习功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17931_14437_x1501947168}[：使能了]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17931_14437_x186431228}[：未使能]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[MAC Tabel Limit]{lang="EN-US"}]{#struct_0_17931_14437_1416018311}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_56666620}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}]{#struct_0_17931_14437_563537114}[，表示不限制]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[Drop Unknown]{lang="EN-US"}]{#struct_0_17931_14437_606965658}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1168437435}[内学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，是否禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17931_14437_955024262}[：表示禁止转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17931_14437_564520154}[：表示允许转发]{lang="EN-US" style="font-family:宋体"}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_17931_14437_933013418}

[[是否使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}]{#struct_0_17931_14437_127099040}[能力。取值为]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[，表示使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力；如果未使能]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力，则不显示该字段]{style="font-family:宋体"}

[[Hub-spoke]{lang="EN-US"}]{#struct_0_17931_14437_x1569568689}[不适用于]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[不关心该字段取值]{style="font-family:宋体"}

[[SPB I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1014156320}

[[SPB]{lang="EN-US"}]{#struct_0_17931_14437_564454618}[骨干网服务实例编号]{style="font-family:宋体"}

[[SPB Connections]{lang="EN-US"}]{#struct_0_17931_14437_x2146994292}

[[SPB]{lang="EN-US"}]{#struct_0_17931_14437_x1564020927}[连接]{style="font-family:宋体"}

[[BMAC]{lang="EN-US"}]{#struct_0_17931_14437_563995867}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x2080004124}[地址]{style="font-family:宋体"}

[[BVLAN]{lang="EN-US"}]{#struct_0_17931_14437_1193397058}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1729442456}

[[Type]{lang="EN-US"}]{#struct_0_17931_14437_563930331}

[[属性标记，取值包括：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1292142381}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast]{lang="EN-US"}]{#struct_0_17931_14437_x146991075}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unicast]{lang="EN-US"}]{#struct_0_17931_14437_563864795}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[ACs]{lang="EN-US"}]{#struct_0_17931_14437_1431217936}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1803335561}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_17931_14437_189426450}

[[接入电路，取值为二层接口名称和以太网服务实例，如]{style="font-family:宋体"}[GE1/0/1 srv1]{lang="EN-US"}]{#struct_0_17931_14437_563799259}

[[Link ID]{lang="EN-US"}]{#struct_0_17931_14437_x323490756}

[[AC]{lang="EN-US"}]{#struct_0_17931_14437_x2106785445}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_17931_14437_563733723}

[[AC]{lang="EN-US"}]{#struct_0_17931_14437_1659610725}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1080847813 .myid}
[]{#_Toc404798173}[]{#struct_0_17931_14437_x772135732}

**SPBM \-- SPBM配置命令 \-- display spbm agreement-protocol**

------------------------------------------------------------------------

[**[display spbm agreement-protocol]{lang="EN-US"}**]{#struct_0_17931_14437_1083793357}[命令用来显示指定接口上指定]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法的]{style="font-family:宋体"}[AP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1886257787}

[**[display spbm agreement-protocol status interface]{lang="EN-US"}**[ *interface-type interface-number* **ect** *ect-number*]{lang="EN-US"}]{#struct_0_17931_14437_2093143421}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1228795384}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_563668187}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_867602500}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x115430304}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x89795939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x413922016}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_357558733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x481397779}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17931_14437_x635723167}[：显示指定接口的]{style="font-family:宋体"}[AP]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}

[**[ect]{lang="EN-US"}**[ *ect-number*]{lang="EN-US"}]{#struct_0_17931_14437_1761630034}[：]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_563602651}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1501947167}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[ECT 1]{lang="EN-US"}[的]{style="font-family:宋体"}[AP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm agreement-protocol status interface gigabitethernet 1/0/1 ect 1]{lang="EN-US"}]{#struct_0_17931_14437_563537115}

[Port AP information:]{lang="EN-US"}

[TxDigest : 00000000000000000000000000003f1f5e5270ce]{lang="EN-US"}

[RxDigest : 00000000000000000000000000003f1f5e5270ce]{lang="EN-US"}

[NBRAPMode: Both]{lang="EN-US"}

[TxAN     : 1                     TxDAN    : 0]{lang="EN-US"}

[RxAN     : 0                     RxDAN    : 0]{lang="EN-US"}

[TxValid  : No                    RxValid  : No]{lang="EN-US"}

[MisOrder : No                    TopoAgree: Yes]{lang="EN-US"}

[CalcEnd  : Yes                   AgreeSend: Normal]{lang="EN-US"}

[ ]{lang="EN-US"}

[Port SPT AP information:]{lang="EN-US"}

[SystemID : 0011.2200.0001]{lang="EN-US"}

[Role     : ROOT             SelectedRole: ROOT]{lang="EN-US"}

[PSTState : 2                ReRoot      : No]{lang="EN-US"}

[Agree    : Yes              Agreed      : Yes]{lang="EN-US"}

[Sync     : No               Synced      : Yes]{lang="EN-US"}

[Forward  : Yes              Forwarding  : Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[Port SPT AP information:]{lang="EN-US"}

[SystemID : 0011.2200.0101]{lang="EN-US"}

[Role     : DESI             SelectedRole: DESI]{lang="EN-US"}

[PSTState : 2                ReRoot      : No]{lang="EN-US"}

[Agree    : Yes              Agreed      : Yes]{lang="EN-US"}

[Sync     : No               Synced      : Yes]{lang="EN-US"}

[Forward  : Yes              Forwarding  : Yes]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display spbm agreement-protocol]{lang="EN-US"}]{#struct_0_17931_14437_606965657}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1749831275}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1168437438}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_954303366}

[[TxDigest]{lang="EN-US"}]{#struct_0_17931_14437_1393880264}

[[本地摘要]{style="font-family:宋体"}]{#struct_0_17931_14437_x682338389}

[[RxDigest]{lang="EN-US"}]{#struct_0_17931_14437_564520155}

[[邻居摘要]{style="font-family:宋体"}]{#struct_0_17931_14437_933013419}

[[NBRAPMode]{lang="EN-US"}]{#struct_0_17931_14437_127099041}

[[邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_x1014156319}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both]{lang="EN-US"}]{#struct_0_17931_14437_204520702}[：表示对单播表项、组播表项都进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast]{lang="EN-US"}]{#struct_0_17931_14437_x553193462}[：表示仅对组播表项进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_17931_14437_564454619}[：表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[模式关闭]{style="font-family:宋体"}

[[TxAN]{lang="EN-US"}]{#struct_0_17931_14437_x2146994293}

[[本地的一致号]{style="font-family:宋体"}]{#struct_0_17931_14437_2063014}

[[TxDAN]{lang="EN-US"}]{#struct_0_17931_14437_346297882}

[[本地的丢弃一致号]{style="font-family:宋体"}]{#struct_0_17931_14437_1002612045}

[[RxAN]{lang="EN-US"}]{#struct_0_17931_14437_x1442694546}

[[邻居的一致号]{style="font-family:宋体"}]{#struct_0_17931_14437_563995864}

[[RxDAN]{lang="EN-US"}]{#struct_0_17931_14437_x2080004125}

[[邻居的丢弃一致号]{style="font-family:宋体"}]{#struct_0_17931_14437_x1535486297}

[[TxValid]{lang="EN-US"}]{#struct_0_17931_14437_1062083650}

[[本地摘要是否可用]{style="font-family:宋体"}]{#struct_0_17931_14437_x1927564896}

[[RxValid]{lang="EN-US"}]{#struct_0_17931_14437_563930328}

[[邻居摘要是否可用]{style="font-family:宋体"}]{#struct_0_17931_14437_1046509788}

[[MisOrder]{lang="EN-US"}]{#struct_0_17931_14437_1968528558}

[[摘要报文乱序标记]{style="font-family:宋体"}]{#struct_0_17931_14437_1517268558}

[[TopoAgree]{lang="EN-US"}]{#struct_0_17931_14437_563864792}

[[拓扑一致标记]{style="font-family:宋体"}]{#struct_0_17931_14437_1431217929}

[[CalcEnd]{lang="EN-US"}]{#struct_0_17931_14437_1802483594}

[[拓扑计算是否结束标记]{style="font-family:宋体"}]{#struct_0_17931_14437_x919556398}

[[AgreeSend]{lang="EN-US"}]{#struct_0_17931_14437_x1863926851}

[[发送摘要报文的状态：]{style="font-family:宋体"}]{#struct_0_17931_14437_563799256}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_17931_14437_x323490749}[ormal]{lang="EN-US"}[：普通发送]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_17931_14437_x2106982052}[ast]{lang="EN-US"}[：快速发送]{lang="EN-US" style="font-family:宋体"}

[[SystemID]{lang="EN-US"}]{#struct_0_17931_14437_2018770450}

[[端口所在树的树根的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_17931_14437_563733720}

[[Role]{lang="EN-US"}]{#struct_0_17931_14437_1659610728}

[[端口在树上当前的角色：]{style="font-family:宋体"}]{#struct_0_17931_14437_x771414836}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_17931_14437_847566061}[：根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTE]{lang="EN-US"}]{#struct_0_17931_14437_563668184}[：可选端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DESI]{lang="EN-US"}]{#struct_0_17931_14437_867602501}[：指定端口]{lang="EN-US" style="font-family:宋体"}

[[SelectedRole]{lang="EN-US"}]{#struct_0_17931_14437_x115430305}

[[端口在树上新计算出的角色：]{style="font-family:宋体"}]{#struct_0_17931_14437_x89861475}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_17931_14437_563602648}[：根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTE]{lang="EN-US"}]{#struct_0_17931_14437_454367976}[：可选端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DESI]{lang="EN-US"}]{#struct_0_17931_14437_582895885}[：指定端口]{lang="EN-US" style="font-family:宋体"}

[[PSTState]{lang="EN-US"}]{#struct_0_17931_14437_563537112}

[[端口的]{style="font-family:宋体"}[PST]{lang="EN-US"}]{#struct_0_17931_14437_606965660}[状态]{style="font-family:宋体"}

[[ReRoot]{lang="EN-US"}]{#struct_0_17931_14437_x405540669}

[[端口是否需要重启]{style="font-family:宋体"}]{#struct_0_17931_14437_1643704645}

[[Agree]{lang="EN-US"}]{#struct_0_17931_14437_564520152}

[[端口是否需要发送一致标记]{style="font-family:宋体"}]{#struct_0_17931_14437_933013420}

[[Agreed]{lang="EN-US"}]{#struct_0_17931_14437_1701077144}

[[端口是否已经发送一致标记]{style="font-family:宋体"}]{#struct_0_17931_14437_564454616}

[[Sync]{lang="EN-US"}]{#struct_0_17931_14437_x2146994278}

[[端口是否进行同步]{style="font-family:宋体"}]{#struct_0_17931_14437_1211523379}

[[Synced]{lang="EN-US"}]{#struct_0_17931_14437_x149510484}

[[端口是否已经同步]{style="font-family:宋体"}]{#struct_0_17931_14437_563995865}

[[Forward]{lang="EN-US"}]{#struct_0_17931_14437_x2080004126}

[[端口是否要迁移到转发状态]{style="font-family:宋体"}]{#struct_0_17931_14437_x1938770824}

[[Forwarding]{lang="EN-US"}]{#struct_0_17931_14437_563930329}

[[端口当前是否处于转发状态]{style="font-family:宋体"}]{#struct_0_17931_14437_1046509787}

[ ]{lang="EN-US"}

::: {#1465220207 .myid}
[]{#_Toc404798174}[]{#struct_0_17931_14437_1969118382}

**SPBM \-- SPBM配置命令 \-- display spbm b-vlan**

------------------------------------------------------------------------

[**[display spbm b-vlan]{lang="EN-US"}**]{#struct_0_17931_14437_x1231704371}[命令用来显示]{style="font-family:宋体"}[SPBM B-VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法应用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_260847658}

[**[display spbm b-vlan]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_17931_14437_563864793}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1431217930}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1802942345}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1769093521}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_954249630}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x2127583913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_38433431}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1218396357}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1337375038}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_563799257}[：显示指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法应用情况，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法应用情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x323490750}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2106392229}[显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display spbm b-vlan]{lang="EN-US"}]{#struct_0_17931_14437_x1186075496}

[B-VLAN 1:]{lang="EN-US"}

[  Mode: SPBM]{lang="EN-US"}

[  Local use: Yes      Remote use: No]{lang="EN-US"}

[  ECT-Index]{lang="EN-US"}[：]{style="font-family:宋体"}[1        Algorithm: 00-80-c2-01  Mask: 0x00]{lang="EN-US"}

[  I-SID list: 300-302, 305, 309]{lang="EN-US"}

[B-VLAN 2:]{lang="EN-US"}

[  Mode: SPBM]{lang="EN-US"}

[  Local use: Yes      Remote use: No]{lang="EN-US"}

[  ECT-Index]{lang="EN-US"}[：]{style="font-family:宋体"}[1        Algorithm: 00-80-c2-01  Mask: 0x00]{lang="EN-US"}

[  I-SID list: 400-402, 404]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display spbm b-vlan]{lang="EN-US"}]{#struct_0_17931_14437_x1676141939}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1774285515}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_563733721}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1659610727}

[[Mode]{lang="EN-US"}]{#struct_0_17931_14437_x772266804}

[[系统使用的模式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17931_14437_1480834430}

[[Local use]{lang="EN-US"}]{#struct_0_17931_14437_x1017100073}

[[本地]{style="font-family:宋体"}]{#struct_0_17931_14437_x1850666159}[B-VLAN]{lang="EN-US"}[是否承载流量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_17931_14437_563668185}[：表示本地]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[承载流量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_17931_14437_867602502}[：表示本地]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[不承载流量]{lang="EN-US" style="font-family:宋体"}

[[Remote use]{lang="EN-US"}]{#struct_0_17931_14437_x115430302}

[[远端]{style="font-family:宋体"}]{#struct_0_17931_14437_x90189155}[B-VLAN]{lang="EN-US"}[是否承载流量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_17931_14437_168060540}[：表示远端]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[承载流量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_17931_14437_1572257334}[：表示远端]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[不承载流量]{style="font-family:宋体"}

[[ECT-Index]{lang="EN-US"}]{#struct_0_17931_14437_563602649}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_454367977}[索引]{style="font-family:宋体"}

[[Algorithm]{lang="EN-US"}]{#struct_0_17931_14437_582895884}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_x1343633751}[算法]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_17931_14437_x423399510}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_563537113}[算法对应的掩码]{style="font-family:宋体"}

[[I-SID list]{lang="EN-US"}]{#struct_0_17931_14437_606965659}

[[本地]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17931_14437_1168437436}[B-VLAN]{lang="EN-US"}[上承载的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无承载]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1129927485 .myid}
[]{#_Toc404798175}[]{#struct_0_17931_14437_954958726}

**SPBM \-- SPBM配置命令 \-- display spbm bridge**

------------------------------------------------------------------------

[**[display spbm bridge]{lang="EN-US"}**]{#struct_0_17931_14437_182458961}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的桥信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x603829071}

[**[display spbm bridge]{lang="EN-US"}**]{#struct_0_17931_14437_x1127478441}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_564520153}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_933013421}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1701077145}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1136034238}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x876068176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1113236288}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x591308170}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_906592516}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_564454617}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的桥信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm bridge]{lang="EN-US"}]{#struct_0_17931_14437_x2146994279}

[System ID            Priority    SPSource ID    Host name]{lang="EN-US"}

[5555.1111.1111       32768       128            SPB-1]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display spbm bridge]{lang="EN-US"}]{#struct_0_17931_14437_x1517359976}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1777250283}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1944836713}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x1050114261}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x1912746900}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_734769591}

[[Priority]{lang="EN-US"}]{#struct_0_17931_14437_563995862}

[[桥优先级]{style="font-family:宋体"}]{#struct_0_17931_14437_x2080004119}

[[SPSource ID]{lang="EN-US"}]{#struct_0_17931_14437_1146146283}

[[最短路径源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_663652365}

[[Host name]{lang="EN-US"}]{#struct_0_17931_14437_433417064}

[[主机名，设备未配置主机名则显示对应的系统]{style="font-family:宋体"}]{#struct_0_17931_14437_1040580531}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1935733584 .myid}
[]{#_Toc404798176}[]{#struct_0_17931_14437_563930326}

**SPBM \-- SPBM配置命令 \-- display spbm bvlan-info**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **spbm** **bvlan-info**]{lang="EN-US"}]{#struct_0_17931_14437_1046509774}[用来显示]{style="font-family:宋体"}[SPBM B-VLAN]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1969314977}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1697634726}

[**[display]{lang="EN-US"}**[ **spbm bvlan-info**]{lang="EN-US"}]{#struct_0_17931_14437_307645926}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1997532264}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **spbm bvlan-info** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_1085847990}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x951593918}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **spbm** **bvlan-info** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_2112591002}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_563864790}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1431217931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1803007881}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x930905677}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1144480788}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1299955149}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_706467313}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1064539890}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x19913995}[：显示指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_563799254}[：显示指定成员设备的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x3484744}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x323490751}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_1082941477}[：显示指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_x560351015}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2106457765}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1844100109}[显示]{style="font-family:宋体"}[SPBM B-VLAN]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display spbm bvlan-info]{lang="EN-US"}]{#struct_0_17931_14437_x314113081}

[Epoch: 0x1]{lang="EN-US"}

[Config B-VLAN list:]{lang="EN-US"}

[  1-7, 20]{lang="EN-US"}

[Driver B-VLAN list:]{lang="EN-US"}

[  1]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display spbm bvlan-info]{lang="EN-US"}]{#struct_0_17931_14437_1338405953}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1770720363}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_338808203}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_563733718}

[[Epoch]{lang="EN-US"}]{#struct_0_17931_14437_x296704400}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1526335308}[时间戳]{style="font-family:宋体"}

[[Config B-VLAN list]{lang="EN-US"}]{#struct_0_17931_14437_x1772455808}

[[映射到]{style="font-family:宋体"}[MSTI 4092]{lang="EN-US"}]{#struct_0_17931_14437_x1185048726}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[列表（已通过激活]{style="font-family:宋体"}[MST]{lang="EN-US"}[域的配置使映射关系生效）]{style="font-family:宋体"}

[[Driver B-VLAN list]{lang="EN-US"}]{#struct_0_17931_14437_x1770737612}

[[下发驱动的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_563668182}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1817280501 .myid}
[]{#_Toc404798177}[]{#struct_0_17931_14437_867602495}

**SPBM \-- SPBM配置命令 \-- display spbm bvlan-info statistics**

------------------------------------------------------------------------

[**[display spbm bvlan-info statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x872210178}[命令用来显示]{style="font-family:宋体"}[SPBM B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1274674730}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_1691435182}

[**[display spbm bvlan-info]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_17931_14437_929019393}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_69343428}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm bvlan-info]{lang="EN-US"}**[ **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_251325868}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_2056953153}[模式：]{style="font-family:宋体"}

[**[display spbm bvlan-info statistics]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_563602646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_454367966}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1373419251}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1271087744}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_282586560}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1767257978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1413716032}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1609241091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_563537110}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_606965662}[：显示指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x405540671}[：显示指定成员设备的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x3222600}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_1644228934}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x973004135}[：显示指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_198639588}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_166848750}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1238334588}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上单板]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm bvlan-info statistics chassis 1 slot 0]{lang="EN-US"}]{#struct_0_17931_14437_564520150}

[SPBM B-VLAN basic statistics:]{lang="EN-US"}

[RefreshMsg     : 1           AgeNumber        : 0]{lang="EN-US"}

[DrvAddNumber   : 1           DrvDeleteNumber  : 0]{lang="EN-US"}

[SPBM B-VLAN error statistics:]{lang="EN-US"}

[BVLANMsgError  : 0           BVLANCreatFail   : 0]{lang="EN-US"}

[DrvEnableFail  : 0           DrvDisableFail   : 0]{lang="EN-US"}

[AllocBVLANFail : 0]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display spbm bvlan-info statistics]{lang="EN-US"}]{#struct_0_17931_14437_933013422}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1772443275}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1701077142}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1136492990}

[[SPBM B-VLAN basic statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1276772908}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_1773331914}[基础统计]{style="font-family:宋体"}

[[RefreshMsg]{lang="EN-US"}]{#struct_0_17931_14437_x1987002227}

[[刷新]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_564454614}[的消息计数]{style="font-family:宋体"}

[[AgeNumber]{lang="EN-US"}]{#struct_0_17931_14437_x2146994280}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_1568081419}[老化计数]{style="font-family:宋体"}

[[DrvAddNumber]{lang="EN-US"}]{#struct_0_17931_14437_1453901927}

[[通知驱动添加]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1342197939}[消息计数]{style="font-family:宋体"}

[[DrvDeleteNumber]{lang="EN-US"}]{#struct_0_17931_14437_563995863}

[[通知驱动删除]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x2080004120}[消息计数]{style="font-family:宋体"}

[[SPBM B-VLAN error statistics]{lang="EN-US"}]{#struct_0_17931_14437_x775971410}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1388343737}[错误统计]{style="font-family:宋体"}

[[BVLANMsgError]{lang="EN-US"}]{#struct_0_17931_14437_237969886}

[[收到]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1400011790}[错误消息计数]{style="font-family:宋体"}

[[BVLANCreatFail]{lang="EN-US"}]{#struct_0_17931_14437_563930327}

[[申请]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_1046509773}[内存失败计数]{style="font-family:宋体"}

[[DrvEnableFail]{lang="EN-US"}]{#struct_0_17931_14437_1968856225}

[[通知驱动]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x899084696}[生效失败计数]{style="font-family:宋体"}

[[DrvDisableFail]{lang="EN-US"}]{#struct_0_17931_14437_x635635804}

[[通知驱动]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_563864791}[失效失败计数]{style="font-family:宋体"}

[[AllocBVLANFail]{lang="EN-US"}]{#struct_0_17931_14437_1431217932}

[[分配]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_1803073417}[失败计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1305928924 .myid}
[]{#_Toc404798178}[]{#struct_0_17931_14437_x967266482}

**SPBM \-- SPBM配置命令 \-- display spbm common statistics**

------------------------------------------------------------------------

[**[display spbm common statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x1094853572}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_563799255}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x323490752}

[**[display spbm common]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_17931_14437_x2106523301}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1393423342}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm common]{lang="EN-US"}**[ **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_785046598}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_729269144}[模式：]{style="font-family:宋体"}

[**[display spbm common statistics]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_x74069662}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2076551701}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1498813059}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_563733719}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x296704401}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1526400844}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_809998160}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1928462654}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1341622950}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x551631536}[：显示指定单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1057063378}[：显示指定成员设备的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x3484743}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_563668183}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x3419207}[：显示指定单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_199032801}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_867602496}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x872210175}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[公共统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm common statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1275395626}

[UMACReDRVCount    : 0           MMACReDRVCount      : 0]{lang="EN-US"}

[ActiveFail        : 0           AllocMsgFail        : 0]{lang="EN-US"}

[RTMsgTypeError    : 0           WriteQueFail        : 0]{lang="EN-US"}

[SyncRTMsgFail     : 0           CommMsgTypeError    : 0]{lang="EN-US"}

[ComQueMsgTypeError: 0           TimerQueMsgTypeError: 0]{lang="EN-US"}

[EpochNumber       : 0           GetBMACNumber       : 1]{lang="EN-US"}

[GetBMACFail       : 0           SetIfNumber         : 6]{lang="EN-US"}

[AgeIfNumber       : 0           SetIfErrNumber      : 0]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display spbm common statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1815824228}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1767977451}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_563602647}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_454367967}

[[UMACReDRVCount]{lang="EN-US"}]{#struct_0_17931_14437_x1373419252}

[[单播表项重新下发驱动计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1457795611}

[[MMACReDRVCount]{lang="EN-US"}]{#struct_0_17931_14437_x430056022}

[[组播表项重新下发驱动计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x965347205}

[[ActiveFail]{lang="EN-US"}]{#struct_0_17931_14437_563537111}

[[备板变主板失败]{style="font-family:宋体"}]{#struct_0_17931_14437_606965661}

[[AllocMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x405540668}

[[申请内存失败]{style="font-family:宋体"}]{#struct_0_17931_14437_1643770181}

[[RTMsgTypeError]{lang="EN-US"}]{#struct_0_17931_14437_1480803196}

[[错误的路由消息类型]{style="font-family:宋体"}]{#struct_0_17931_14437_1332675030}

[[WriteQueFail]{lang="EN-US"}]{#struct_0_17931_14437_564520151}

[[外部消息写队列失败]{style="font-family:宋体"}]{#struct_0_17931_14437_933013423}

[[SyncRTMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_1701077143}

[[路由消息同步失败]{style="font-family:宋体"}]{#struct_0_17931_14437_1136427454}

[[CommMsgTypeError]{lang="EN-US"}]{#struct_0_17931_14437_x2053196095}

[[错误的消息类型]{style="font-family:宋体"}]{#struct_0_17931_14437_564454615}

[[ComQueMsgTypeError]{lang="EN-US"}]{#struct_0_17931_14437_x2146994281}

[[错误的队列类型]{style="font-family:宋体"}]{#struct_0_17931_14437_x1160801936}

[[TimerQueMsgTypeError]{lang="EN-US"}]{#struct_0_17931_14437_x470261958}

[[定时器队列消息类型错误]{style="font-family:宋体"}]{#struct_0_17931_14437_2005241149}

[[EpochNumber]{lang="EN-US"}]{#struct_0_17931_14437_2130079807}

[[全局老化计数，当表项的时间戳小于该值时，则表项需要老化]{style="font-family:宋体"}]{#struct_0_17931_14437_648231127}

[[GetBMACNumber]{lang="EN-US"}]{#struct_0_17931_14437_806342122}

[[获取驱动]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_1998446986}[计数]{style="font-family:宋体"}

[[GetBMACFail]{lang="EN-US"}]{#struct_0_17931_14437_1433747815}

[[获取驱动]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_2130014271}[失败]{style="font-family:宋体"}

[[SetIfNumber]{lang="EN-US"}]{#struct_0_17931_14437_1847014965}

[[接口下发驱动使能数目]{style="font-family:宋体"}]{#struct_0_17931_14437_2138927472}

[[AgeIfNumber]{lang="EN-US"}]{#struct_0_17931_14437_1310894457}

[[接口老化计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1944901260}

[[SetIfErrNumber]{lang="EN-US"}]{#struct_0_17931_14437_2129948735}

[[接口下发驱动失败使能数目]{style="font-family:宋体"}]{#struct_0_17931_14437_x1225733397}

[ ]{lang="EN-US"}

::: {#-1174544815 .myid}
[]{#_Toc404798179}[]{#struct_0_17931_14437_750209451}

**SPBM \-- SPBM配置命令 \-- display spbm ect**

------------------------------------------------------------------------

[**[display spbm ect]{lang="EN-US"}**]{#struct_0_17931_14437_x1190929200}[命令用来显示]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法信息以及使用对应]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1873766826}

[**[display spbm ect]{lang="EN-US"}**[ \[ *ect-index* \]]{lang="EN-US"}]{#struct_0_17931_14437_x160773707}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_2129883199}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1610775503}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_202711150}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_384146329}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_2107950900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_7804448}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x627328965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x117725720}

[*[ect-index]{lang="EN-US"}*]{#struct_0_17931_14437_x1748553581}[：]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。如果未指定该参数，则显示所有的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法信息以及使用对应]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_2129817663}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1969638974}[显示所有的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm ect]{lang="EN-US"}]{#struct_0_17931_14437_2129686591}

[ECT-1:]{lang="EN-US"}

[    Algorithm: 00-80-c2-01     Mask: 0x00]{lang="EN-US"}

[    Active B-VLANs: 1-10]{lang="EN-US"}

[    Inactive B-VLANs: 31-4094]{lang="EN-US"}

[ECT-2:]{lang="EN-US"}

[    Algorithm: 00-80-c2-02     Mask: 0xff]{lang="EN-US"}

[    Active B-VLANs: 11-20]{lang="EN-US"}

[    Inactive B-VLANs: 21-30]{lang="EN-US"}

[ECT-3:]{lang="EN-US"}

[    Algorithm: 00-80-c2-03     Mask: 0x88]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-4:]{lang="EN-US"}

[    Algorithm: 00-80-c2-04     Mask: 0x77]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-5:]{lang="EN-US"}

[    Algorithm: 00-80-c2-05     Mask: 0x44]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-6:]{lang="EN-US"}

[    Algorithm: 00-80-c2-06     Mask: 0x33]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-7:]{lang="EN-US"}

[    Algorithm: 00-80-c2-07     Mask: 0xcc]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-8:]{lang="EN-US"}

[    Algorithm: 00-80-c2-08     Mask: 0xbb]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-9:]{lang="EN-US"}

[    Algorithm: 00-80-c2-09     Mask: 0x22]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-10:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0a     Mask: 0x11]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-11:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0b     Mask: 0x66]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-12:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0c     Mask: 0x55]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-13:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0d     Mask: 0xaa]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-14:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0e     Mask: 0x99]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-15:]{lang="EN-US"}

[    Algorithm: 00-80-c2-0f     Mask: 0xdd]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[ECT-16:]{lang="EN-US"}

[    Algorithm: 00-80-c2-10     Mask: 0xee]{lang="EN-US"}

[    Active B-VLANs: N/A]{lang="EN-US"}

[    Inactive B-VLANs: N/A]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display spbm ect]{lang="EN-US"}]{#struct_0_17931_14437_1159478884}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1792156331}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x250820243}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x327093495}

[[Algorithm]{lang="EN-US"}]{#struct_0_17931_14437_2129621055}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_x414081983}[算法]{style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_17931_14437_x934781674}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_x1031573990}[算法对应的掩码]{style="font-family:宋体"}

[[Active B-VLANs]{lang="EN-US"}]{#struct_0_17931_14437_x1513235270}

[[配置在该]{style="font-family:宋体"}]{#struct_0_17931_14437_x1998990582}[ECT]{lang="EN-US"}[算法下的生效]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法下不存在生效]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[Inactive B-VLANs]{lang="EN-US"}]{#struct_0_17931_14437_2130604095}

[[配置在该]{style="font-family:宋体"}]{#struct_0_17931_14437_x2058865047}[ECT]{lang="EN-US"}[算法下无效]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示该]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法下不存在无效]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-918996383 .myid}
[]{#_Toc326076042}[]{#_Toc323196016}[]{#_Toc323114960}[]{#_Toc404798180}[]{#struct_0_17931_14437_x62696475}

**SPBM \-- SPBM配置命令 \-- display spbm ect-migration**

------------------------------------------------------------------------

[**[display spbm ect-migration]{lang="EN-US"}**]{#struct_0_17931_14437_2130538559}[命令用来显示指定]{style="font-family:
宋体"}[I-SID]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[迁移相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2100974184}

[**[display spbm ect-migration i-sid]{lang="EN-US"}**[ *i-sid*]{lang="EN-US"}]{#struct_0_17931_14437_666960536}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x835159003}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x83553715}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_356811944}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1116412649}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_1329339239}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_2130079808}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_649214167}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_189318701}

[*[i-sid]{lang="EN-US"}*]{#struct_0_17931_14437_x980628182}[：指定的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[255]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x13655972}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2126179665}[显示]{style="font-family:宋体"}[I-SID 300]{lang="EN-US"}[的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[迁移相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm ect-migration i-sid 300]{lang="EN-US"}]{#struct_0_17931_14437_x1396535514}

[ECT            B-VLAN    T    R]{lang="EN-US"}

[00-80-c2-01    1         0    1]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display spbm ect-migration]{lang="EN-US"}]{#struct_0_17931_14437_2130014272}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1794187659}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1847211573}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_604813492}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_1828410242}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_693252952}[算法]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_238429964}

[[该]{style="font-family:宋体"}]{#struct_0_17931_14437_2129948736}[I-SID]{lang="EN-US"}[映射的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[T]{lang="EN-US"}]{#struct_0_17931_14437_x1225930005}

[[T]{lang="EN-US"}]{#struct_0_17931_14437_x1993723166}[标志是否置位定义了设备在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[对应组播组中的传输状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_2129883200}[：置位，表示该设备是传输者。如果采用核心复制，]{style="font-family:宋体"}[BEB]{lang="EN-US"}[将]{style="font-family:宋体"}[T]{lang="EN-US"}[标志置位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_1109623848}[：未置位，表示该设备不是传输者。如果采用头端复制，]{style="font-family:宋体"}[BEB]{lang="EN-US"}[不将]{style="font-family:宋体"}[T]{lang="EN-US"}[标志置位]{style="font-family:宋体"}

[[R]{lang="EN-US"}]{#struct_0_17931_14437_2129817664}

[[R]{lang="EN-US"}]{#struct_0_17931_14437_x1969442366}[标志是否置位定义了设备在]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[对应组播组中的接收状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_435556503}[：置位，表示该设备是接收者]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_402573611}[：未置位，表示该设备不是接收者]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1761279537 .myid}
[]{#_Toc404798181}[]{#struct_0_17931_14437_x1245946439}

**SPBM \-- SPBM配置命令 \-- display spbm fast-channel statistics**

------------------------------------------------------------------------

[**[display spbm fast-channel statistics]{lang="EN-US"}**]{#struct_0_17931_14437_1581432191}[命令用来显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速泛洪通道的相关统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1206022720}

[**[display spbm fast-channel statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x1245880903}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1357476038}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1246077511}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_409157870}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1005559541}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1246011975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1574624428}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x2019261333}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1246208583}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_864047037}[显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速泛洪通道的相关统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm fast-channel statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1246143047}

[                   Fast channel information for SPBM]{lang="EN-US"}

[                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name              : 1]{lang="EN-US"}

[B-VLAN                : 1]{lang="EN-US"}

[I-SID                 : 255]{lang="EN-US"}

[State                 : Active]{lang="EN-US"}

[Replication mode      : tandem]{lang="EN-US"}

[ECT algorithm         : 00-80-c2-01]{lang="EN-US"}

[LSPs sent count       : 10]{lang="EN-US"}

[LSPs received count   : 20]{lang="EN-US"}

[LSP timer             : 10]{lang="EN-US"}

[LSPs transmitted count: 10]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display spbm fast-channel statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1487797702}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1152256869}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1246339655}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x1246274119}

[[VSI name]{lang="EN-US"}]{#struct_0_17931_14437_635823554}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_x1245422151}[名称]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1245356615}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1245946438}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_15348250}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_17931_14437_x1245880902}

[[State]{lang="EN-US"}]{#struct_0_17931_14437_x1246077510}

[[快速泛洪通道状态，取值为：]{style="font-family:宋体"}]{#struct_0_17931_14437_1975241811}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_17931_14437_x1246011974}[：表示快速泛洪通道可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_17931_14437_x1246208582}[：表示]{lang="EN-US" style="font-family:宋体"}[快速泛洪通道不可用]{style="font-family:宋体"}

[[Replication mode]{lang="EN-US"}]{#struct_0_17931_14437_x1246143046}

[[组播复制模式，取值为：]{style="font-family:宋体"}]{#struct_0_17931_14437_1241085653}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[head-end]{lang="EN-US"}]{#struct_0_17931_14437_x1246339654}[：表示头端复制模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[tandem]{lang="EN-US"}]{#struct_0_17931_14437_x1246274118}[：表示核心复制模式]{lang="EN-US" style="font-family:宋体"}

[[ECT algorithm]{lang="EN-US"}]{#struct_0_17931_14437_x1245422150}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x637551327}[对应的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法]{style="font-family:宋体"}

[[LSPs sent count]{lang="EN-US"}]{#struct_0_17931_14437_x1245356614}

[[通过快速泛洪通道发送]{style="font-family:宋体"}]{#struct_0_17931_14437_x1245946441}[LSP]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[[当发生以下任意一种情况时，本字段清零：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1245880905}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[reset spbm database]{lang="EN-US"}**]{#struct_0_17931_14437_x1246077513}[命令]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x753641544}[为]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[的]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行]{style="font-family:宋体"}]{#struct_0_17931_14437_x1246011977}[进程分布优化。]{style="font-family:宋体"}[有关]{style="font-family:宋体"}[进程分布优化的详细介绍，请参见"可靠性配置指导"中的"进程分布优化"]{style="font-family:宋体"}

[[LSPs received count]{lang="EN-US"}]{#struct_0_17931_14437_x1246208585}

[[通过快速泛洪通道接收的]{style="font-family:宋体"}]{#struct_0_17931_14437_x1246143049}[LSP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[当发生以下任意一种情况时，本字段清零：]{style="font-family:宋体"}]{#struct_0_17931_14437_2000600540}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[reset spbm database]{lang="EN-US"}**]{#struct_0_17931_14437_x1246339657}[命令]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1246274121}[为]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[的]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[进行]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17931_14437_x1245422153}[进程分布优化]{lang="EN-US" style="font-family:宋体"}

[[LSP timer]{lang="EN-US"}]{#struct_0_17931_14437_x1245356617}

[[快速泛洪通道发送]{style="font-family:宋体"}]{#struct_0_17931_14437_x339589280}[LSP]{lang="EN-US"}[的最小时间间隔，单位为毫秒。不可配]{style="font-family:宋体"}

[[LSPs transmitted count]{lang="EN-US"}]{#struct_0_17931_14437_x1245946440}

[[快速泛洪通道一次最多可以发送的]{style="font-family:宋体"}]{#struct_0_17931_14437_x1245880904}[LSP]{lang="EN-US"}[个数。不可配]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#680808573 .myid}
[]{#_Toc404798182}[]{#struct_0_17931_14437_1742536186}[]{#_Toc374027607}

**SPBM \-- SPBM配置命令 \-- display spbm graceful-restart event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_1742601722}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_x1089947604}
:::

[ ]{lang="EN-US"}

[**[display spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_1028034890}[命令用来显示]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x228957845}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x779514594}

[**[display ]{lang="EN-US"}[spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_675140818}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1645696137}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[spbm graceful-restart event-log]{lang="EN-US"}**[ **slot**]{lang="EN-US"}[ *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1230551841}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_1742667258}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[spbm graceful-restart event-log chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1877279607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_983840463}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1096392748}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x322672495}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x516232489}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_666888380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_686396703}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1742732794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x697214395}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x220727321}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x1738830622}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x3484749}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_1723001795}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_x3419213}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_358393971}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1314308694}[显示成员设备]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display spbm graceful-restart event-log slot 0]{lang="EN-US"}]{#struct_0_17931_14437_1742798330}

[SPBM log information:]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Initialization).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSDB synchronization).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSP stability).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (LSP generation).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (SPF computation).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Flush smooth).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter GR phase (Finish).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 GR complete.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1607854153}[显示单板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}[ display spbm graceful-restart event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_607188306}

[SPBM log information:]{lang="EN-US"}

[Oct  5 12:54:53 2013 -Slot=1 HA backup channel was blocked.]{lang="EN-US"}

[Oct  5 12:54:56 2013 -Slot=1 HA backup channel was unblocked.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x890991325}[显示单板]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}[ display spbm graceful-restart event-log slot 2]{lang="EN-US"}]{#struct_0_17931_14437_x1235897875}

[SPBM log information:]{lang="EN-US"}

[Oct  6 15:50:56 2013 -Slot=2 Memory restore on the standby MPU triggered data batch backup.]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display spbm graceful-restart event-log]{lang="EN-US"}]{#struct_0_17931_14437_1742208511}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x685668195}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_449964272}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1334401852}

[[Initialization]{lang="EN-US"}]{#struct_0_17931_14437_696098807}

[[进入]{style="font-family:宋体"}]{#struct_0_17931_14437_1742274047}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[初始化阶段]{style="font-family:宋体"}

[[LSDB synchronization]{lang="EN-US"}]{#struct_0_17931_14437_471626159}

[[进入]{style="font-family:宋体"}]{#struct_0_17931_14437_1282177999}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[同步阶段]{style="font-family:宋体"}

[[LSP stability]{lang="EN-US"}]{#struct_0_17931_14437_1742339583}

[[进入]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x1126802077}[稳定阶段]{style="font-family:宋体"}

[[LSP generation]{lang="EN-US"}]{#struct_0_17931_14437_x1097506711}

[[进入]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_542517786}[生成阶段]{style="font-family:宋体"}

[[SPF computation]{lang="EN-US"}]{#struct_0_17931_14437_1742405119}

[[进入路由计算阶段]{style="font-family:宋体"}]{#struct_0_17931_14437_1262216577}

[[F]{lang="EN-US"}]{#struct_0_17931_14437_x501805135}[lush ]{lang="EN-US"}[s]{lang="EN-US"}[mooth]{lang="EN-US"}

[[进入内核数据平滑阶段]{style="font-family:宋体"}]{#struct_0_17931_14437_1742470655}

[[Finish]{lang="EN-US"}]{#struct_0_17931_14437_x1880210610}

[[进入]{style="font-family:宋体"}]{#struct_0_17931_14437_x1700594288}[GR]{lang="EN-US"}[的结束阶段]{style="font-family:宋体"}

[[GR complete]{lang="EN-US"}]{#struct_0_17931_14437_1742536191}

[[完成]{style="font-family:宋体"}]{#struct_0_17931_14437_1654163351}[GR]{lang="EN-US"}

[[HA backup channel was blocked]{lang="EN-US"}]{#struct_0_17931_14437_x1621244125}

[[降级（主进程变为备进程）过程中进入实时备份和批量备份通道阻塞状态]{style="font-family:宋体"}]{#struct_0_17931_14437_1196270360}

[[HA backup channel was unblocked]{lang="EN-US"}]{#struct_0_17931_14437_1742601727}

[[降级结束退出实时备份和批量备份通道阻塞状态]{style="font-family:宋体"}]{#struct_0_17931_14437_x1090144212}

[[Memory restore on the standby MPU triggered data batch backup]{lang="EN-US"}]{#struct_0_17931_14437_x148986157}

[[备板内存恢复之后，会主动触发一次数据批量备份请求]{style="font-family:宋体"}]{#struct_0_17931_14437_1742667263}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1876820858}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_1469635922}

::::::: {#144871584 .myid}
[]{#_Toc404798183}[]{#struct_0_17931_14437_1279997451}[]{#_Toc363139065}[]{#_Toc365969240}[]{#_Toc365969313}[]{#_Toc366584205}

**SPBM \-- SPBM配置命令 \-- display spbm graceful-restart status**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1897791441}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_x1916390568}
:::

[ ]{lang="EN-US"}

[**[display spbm graceful-restart status]{lang="EN-US"}**]{#struct_0_17931_14437_1929804524}[命令用来显示]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_2129752128}

[**[display spbm graceful-restart status]{lang="EN-US"}**]{#struct_0_17931_14437_x42463112}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_189560371}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_47577753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2121544273}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1539920378}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_213849080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1120401122}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_2129686592}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x438422524}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_29346763}[显示]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm graceful-restart status]{lang="EN-US"}]{#struct_0_17931_14437_2129621056}

[ ]{lang="EN-US"}

[                         Restart information for SPBM]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Restart status             : Restarting]{lang="EN-US"}

[Restart phase              : LSDB synchronization]{lang="EN-US"}

[Restart interval           : 300]{lang="EN-US"}

[SA bit                     : Supported]{lang="EN-US"}

[Total number of interfaces : 2]{lang="EN-US"}

[Number of waiting LSPs     : 3]{lang="EN-US"}

[T2 remaining time          : 41]{lang="EN-US"}

[Interface      T1 remaining time  RA received  CSNP received  T1 expirations]{lang="EN-US"}

[GE1/0/1        2                  Y            N              2]{lang="EN-US"}

[GE1/0/2        2                  Y            N              2]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image003.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x999281750}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_351252707}
:::

[ ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display spbm graceful-restart status]{lang="EN-US"}]{#struct_0_17931_14437_x414016447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1793953291}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1360479509}
:::::::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1139691992}

[[Restart status]{lang="EN-US"}]{#struct_0_17931_14437_x1109876667}

[[当前设备的]{style="font-family:宋体"}[Restart]{lang="EN-US"}]{#struct_0_17931_14437_2130604096}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarting]{lang="EN-US"}]{#struct_0_17931_14437_x2059061655}[：主备倒换、保留]{style="font-family:宋体"}[FIB]{lang="EN-US"}[的过程。该状态下能保证进行转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Starting]{lang="EN-US"}]{#struct_0_17931_14437_x672699766}[：对于不保留]{style="font-family:宋体"}[FIB]{lang="EN-US"}[的主备倒换或设备重启后进入的状态。该状态下不能保证转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_17931_14437_x1395332785}[omplete]{lang="EN-US"}[：完成]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[Restart phase]{lang="EN-US"}]{#struct_0_17931_14437_113066580}

[[当前设备的]{style="font-family:宋体"}[Restart]{lang="EN-US"}]{#struct_0_17931_14437_x2029924910}[阶段：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_17931_14437_2130538560}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[初始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_17931_14437_x2100384361}[：]{lang="EN-US" style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[同步]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_17931_14437_1904433854}[：本地]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[稳定阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_17931_14437_319139526}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生成和泛洪]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[First SPF computation]{lang="EN-US"}]{#struct_0_17931_14437_x451564139}[：第一次拓扑计算]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_17931_14437_2130079805}[：完成]{lang="EN-US" style="font-family:宋体"}

[[Restart Interval]{lang="EN-US"}]{#struct_0_17931_14437_648362199}

[[设备预期完成重启的时间间隔，单位为秒，在该时间间隔内邻居不会断掉与重启设备的邻接关系]{style="font-family:宋体"}]{#struct_0_17931_14437_1628491099}

[[SA bit]{lang="EN-US"}]{#struct_0_17931_14437_x1438341121}

[[设备是否支持]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_17931_14437_777136123}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Supported]{lang="EN-US"}]{#struct_0_17931_14437_2130014269}[：支持，]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位为]{style="font-family:宋体"}[1]{lang="EN-US"}[，重启设备的邻居不会发布与重启设备的邻接关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_17931_14437_1846490676}[：不支持，]{style="font-family:宋体"}[SA]{lang="EN-US"}[位清空为]{style="font-family:宋体"}[0]{lang="EN-US"}[，重启设备的邻居会继续发布与重启设备的邻接关系]{style="font-family:宋体"}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_17931_14437_1359233871}

[[当前使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_2129948733}[的接口数]{style="font-family:宋体"}

[[Number of waiting LSPs]{lang="EN-US"}]{#struct_0_17931_14437_x1225602325}

[[GR Restarter]{lang="EN-US"}]{#struct_0_17931_14437_x1892456926}[从]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步时，未完成同步的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[T2 remaining time]{lang="EN-US"}]{#struct_0_17931_14437_2124641165}

[[T2]{lang="EN-US"}]{#struct_0_17931_14437_2129883197}[定时器剩余的时间，单位为秒，]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器用来控制]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的同步时间]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_17931_14437_x1611168719}

[[接口名称]{style="font-family:宋体"}]{#struct_0_17931_14437_x339090324}

[[T1 remaining time]{lang="EN-US"}]{#struct_0_17931_14437_330949041}

[[接口上]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_17931_14437_2129817661}[定时器剩余的时间，单位为秒，]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器用来控制带]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的重传时间]{style="font-family:宋体"}

[[RA received]{lang="EN-US"}]{#struct_0_17931_14437_x1969770046}

[[接口上是否收到邻居发送的带]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_17931_14437_600679507}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[CSNP received]{lang="EN-US"}]{#struct_0_17931_14437_999115874}

[[接口上是否收到完整的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_17931_14437_2129752125}[报文，即是否完成与]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[T1 expirations]{lang="EN-US"}]{#struct_0_17931_14437_x43315080}

[[T1]{lang="EN-US"}]{#struct_0_17931_14437_x279191024}[定时器的超时次数，超时达到]{style="font-family:宋体"}[10]{lang="EN-US"}[次后，不会再进行带]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的重传]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-952345107 .myid}
[]{#_Toc404798184}[]{#struct_0_17931_14437_x793735841}

**SPBM \-- SPBM配置命令 \-- display spbm interface**

------------------------------------------------------------------------

[**[display spbm interface]{lang="EN-US"}**]{#struct_0_17931_14437_1783137308}[命令用来显示使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x711863005}

[**[display spbm interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_2129686589}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1160003171}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_333230498}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1127990828}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1428840734}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_1488728793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x339094990}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x847376582}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1328720557}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17931_14437_2129621053}[：显示指定接口的信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定该参数，则显示所有使能]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[功能接口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_x413688767}[：显示接口的详细信息。如果未指定该参数，则显示接口的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x99321927}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1183714313}[显示使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能的接口的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm interface]{lang="EN-US"}]{#struct_0_17931_14437_x1845868162}

[                        Interface information for SPBM]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                   Circuit ID    State     MTU      Cost]{lang="EN-US"}

[GE1/0/1                     1             Up        1497     10]{lang="EN-US"}

[GE1/0/2                     2             Up        1497     100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1908784163}[显示使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能的接口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm interface verbose]{lang="EN-US"}]{#struct_0_17931_14437_2130604093}

[                        Interface information for SPBM]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                   Circuit ID    State     MTU      Cost]{lang="EN-US"}

[GE1/0/1                     1             Up        1497     10]{lang="EN-US"}

[Hello timer           : 10]{lang="EN-US"}

[Hello multiplier      : 3]{lang="EN-US"}

[LSP timer             : 33]{lang="EN-US"}

[LSP transmitted count : 5]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                   Circuit ID    State     MTU      Cost]{lang="EN-US"}

[GE1/0/2                     2             Up        1497     100]{lang="EN-US"}

[Hello timer           : 10]{lang="EN-US"}

[Hello multiplier      : 3]{lang="EN-US"}

[LSP timer             : 33]{lang="EN-US"}

[LSP transmitted count : 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2059258263}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_17931_14437_2130538557}

[                        Interface information for SPBM]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface                   Circuit ID    State     MTU      Cost]{lang="EN-US"}

[GE1/0/1                     1             Up        1497     10]{lang="EN-US"}

[Hello timer           : 10]{lang="EN-US"}

[Hello multiplier      : 3]{lang="EN-US"}

[LSP timer             : 33]{lang="EN-US"}

[LSP transmitted count : 5]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display spbm interface]{lang="EN-US"}]{#struct_0_17931_14437_x2100318824}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1783644299}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1506079387}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1280458068}

[[Interface]{lang="EN-US"}]{#struct_0_17931_14437_1499648532}

[[接口名]{style="font-family:宋体"}]{#struct_0_17931_14437_1761653648}

[[Circuit ID]{lang="EN-US"}]{#struct_0_17931_14437_2130079806}

[[电路]{style="font-family:宋体"}]{#struct_0_17931_14437_648296663}[ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_17931_14437_x1522252857}

[[接口状态]{style="font-family:宋体"}]{#struct_0_17931_14437_x2106366728}

[[MTU]{lang="EN-US"}]{#struct_0_17931_14437_x65662321}

[[接口]{style="font-family:宋体"}]{#struct_0_17931_14437_1355781370}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_17931_14437_2130014270}

[[接口的链路开销值]{style="font-family:宋体"}]{#struct_0_17931_14437_1847080501}

[[Hello timer]{lang="EN-US"}]{#struct_0_17931_14437_x2113387562}

[[Hello]{lang="EN-US"}]{#struct_0_17931_14437_x2018706060}[报文发送时间间隔，单位为秒]{style="font-family:宋体"}

[[Hello multiplier]{lang="EN-US"}]{#struct_0_17931_14437_50306839}

[[Hello]{lang="EN-US"}]{#struct_0_17931_14437_2129948734}[报文失效数目]{style="font-family:宋体"}

[[LSP timer]{lang="EN-US"}]{#struct_0_17931_14437_x1225798933}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x49551817}[的最小时间间隔，单位为毫秒]{style="font-family:宋体"}

[[LSP transmitted count]{lang="EN-US"}]{#struct_0_17931_14437_1650950449}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x992861203}[的数目]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc321837760}

::: {#-1361374228 .myid}
[]{#_Toc404798185}[]{#struct_0_17931_14437_2129883198}[]{#_Toc330889111}

**SPBM \-- SPBM配置命令 \-- display spbm lsdb**

------------------------------------------------------------------------

[**[display spbm lsdb]{lang="EN-US"}**]{#struct_0_17931_14437_x1610841039}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1697198006}

[**[display spbm lsdb]{lang="EN-US"}**[ \[ \[ **lsp-id** *lspid* \| **lsp-name** *lspname* \] \| **local** \| **verbose** \] \*]{lang="EN-US"}]{#struct_0_17931_14437_x1858940795}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_60450282}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_545445900}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1921039154}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x846546673}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_2129817662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1969573438}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1357811077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1307005069}

[**[lsp-id]{lang="EN-US"}***[ lspid]{lang="EN-US"}*]{#struct_0_17931_14437_1747748298}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}*[SYSID.Pseudonode ID-fragment num]{lang="EN-US"}*[，其中，]{style="font-family:宋体"}*[SYSID]{lang="EN-US"}*[是产生该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的节点的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[Pseudonode ID]{lang="EN-US"}*[是伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[fragment num]{lang="EN-US"}*[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。如果未指定该参数，则显示链路状态数据库中所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识对应的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[lsp-name]{lang="EN-US"}***[ lspname]{lang="EN-US"}*]{#struct_0_17931_14437_x194975661}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，形式为]{style="font-family:宋体"}*[Symbolic name-fragment num]{lang="EN-US"}*[，其中，]{style="font-family:宋体"}*[Symbolic name]{lang="EN-US"}*[是产生该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的节点名称，]{style="font-family:宋体"}*[fragment num]{lang="EN-US"}*[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。如果未指定该参数，则显示链路状态数据库中所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称对应的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_17931_14437_x688159659}[：显示本设备产生的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。如果未指定该参数，则显示链路状态数据库中所有设备产生的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_x81193948}[：显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[详细信息。如果未指定该参数，则显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_2129752126}

[[如果未指定任何参数，则显示链路状态数据库中的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x43118472}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_202641314}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1909949872}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm lsdb]{lang="EN-US"}]{#struct_0_17931_14437_x2056504263}

[                         Database information for SPBM]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSP ID: \* - Local LSP]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID                Seq Num      Checksum      Holdtime      Length  Overload]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[4455.6677.0001.00-00  0x00000fd2   0x1cea        1044          236     0]{lang="EN-US"}

[4455.6677.0001.00-01  0x00000fd2   0x1cea        1044          256     0]{lang="EN-US"}

[4455.6677.0003.00-00\* 0x00001448   0x3d27        683           323     0]{lang="EN-US"}

[4455.6677.0003.00-01\* 0x00001448   0xbd27        683           723     0]{lang="EN-US"}

[4455.6677.0004.00-00  0x00000ff8   0xd1d9        1090          323     0]{lang="EN-US"}

[4455.6677.0004.00-01  0x00000ff8   0xd7d9        1090          329     0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_2129686590}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm lsdb verbose]{lang="EN-US"}]{#struct_0_17931_14437_2130604094}

[                         Database information for SPBM]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LSP ID: \* - Local LSP]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID                Seq Num      Checksum      Holdtime      Length  Overload]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0011.2200.0001.00-00  0x0000000e   0x29ef        429           69      0]{lang="EN-US"}

[System ID           : 0011.2200.0001]{lang="EN-US"}

[NLPID               : SPBM]{lang="EN-US"}

[Area address        : 00.0000]{lang="EN-US"}

[MT capability TLV   :]{lang="EN-US"}

[ MT ID       : 00]{lang="EN-US"}

[ MT overload : 0]{lang="EN-US"}

[ SPB instance sub-TLV:]{lang="EN-US"}

[   CIST root identifier : 0000-0000-0000-0000]{lang="EN-US"}

[   CIST ERPC            : 0]{lang="EN-US"}

[   Bridge priority      : 32768]{lang="EN-US"}

[   SPSourceID           : 100]{lang="EN-US"}

[   Number of trees      : 1]{lang="EN-US"}

[     B-VLAN: 10      U-Bit: 1    ECT: 00-80-c2-01    SPVID: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[0011.2200.0001.00-01  0x0000000f   0x209e        1190          66      0]{lang="EN-US"}

[System ID           : 0011.2200.0001]{lang="EN-US"}

[Hostname            : 0011.2200.0001.00]{lang="EN-US"}

[MT capability TLV   :]{lang="EN-US"}

[ MT ID       : 00]{lang="EN-US"}

[ MT overload : 0]{lang="EN-US"}

[ SPBM Service Identifier and Unicast Address sub-TLV:]{lang="EN-US"}

[   B-MAC     : 0011-2200-0001]{lang="EN-US"}

[   B-VLAN    : 10]{lang="EN-US"}

[     I-SID   : 300(R)]{lang="EN-US"}

[Extended neighbor reachability TLV:]{lang="EN-US"}

[ Hostname    : 0011.2200.0101.00]{lang="EN-US"}

[ Cost        : 11]{lang="EN-US"}

[ Port number : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[0011.2200.0101.00-00\* 0x00000002   0x3846        1190          69      0]{lang="EN-US"}

[System ID           : 0011.2200.0101]{lang="EN-US"}

[NLPID               : SPBM]{lang="EN-US"}

[Area address        : 00.0000]{lang="EN-US"}

[MT capability TLV   :]{lang="EN-US"}

[ MT ID       : 00]{lang="EN-US"}

[ MT overload : 0]{lang="EN-US"}

[ SPB instance sub-TLV:]{lang="EN-US"}

[   CIST root identifier : 0000-0000-0000-0000]{lang="EN-US"}

[   CIST ERPC            : 0]{lang="EN-US"}

[   Bridge priority      : 32768]{lang="EN-US"}

[   SPSourceID           : 10]{lang="EN-US"}

[   Number of Trees      : 1]{lang="EN-US"}

[     B-VLAN: 10      U-Bit: 1    ECT: 00-80-c2-01    SPVID: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[0011.2200.0101.00-01\* 0x00000002   0xfdcd        1190          66      0]{lang="EN-US"}

[System ID           : 0011.2200.0101]{lang="EN-US"}

[Hostname            : 0011.2200.0101.00]{lang="EN-US"}

[MT capability TLV   :]{lang="EN-US"}

[ MT ID       : 00]{lang="EN-US"}

[ MT overload : 0]{lang="EN-US"}

[ SPBM Service Identifier and Unicast Address sub-TLV:]{lang="EN-US"}

[   B-MAC     : 0011-2200-0101]{lang="EN-US"}

[   B-VLAN    : 10]{lang="EN-US"}

[     I-SID   : 300(R)]{lang="EN-US"}

[     I-SID   : 301(T&R)]{lang="EN-US"}

[Extended neighbor reachability TLV:]{lang="EN-US"}

[ Hostname    : 0011.2200.0001.00]{lang="EN-US"}

[ Cost        : 10]{lang="EN-US"}

[ Port number : 1]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display spbm lsdb]{lang="EN-US"}]{#struct_0_17931_14437_x2058930583}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1784853099}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_122136333}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1741394391}

[[LSP ID]{lang="EN-US"}]{#struct_0_17931_14437_2130538558}

[[链路状态报文]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_x2100908648}[，]{style="font-family:宋体"}[\*]{lang="EN-US"}[表示本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[Seq Num]{lang="EN-US"}]{#struct_0_17931_14437_1175407392}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x175604847}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_17931_14437_1817761073}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_101617712}[校验和]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_17931_14437_2130079803}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_648493271}[生存时间，单位为秒]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_17931_14437_x483233443}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_804442025}[长度]{style="font-family:宋体"}

[[Overload]{lang="EN-US"}]{#struct_0_17931_14437_x964338440}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_2130014267}[中]{style="font-family:宋体"}[Overload]{lang="EN-US"}[的置位情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_1847408180}[：表示置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_x1009719246}[：表示没有置位]{lang="EN-US" style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x234417649}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_1652131014}[生成设备的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[NLPID]{lang="EN-US"}]{#struct_0_17931_14437_2129948731}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x1225471253}[生成设备运行的协议]{style="font-family:宋体"}

[[Area address]{lang="EN-US"}]{#struct_0_17931_14437_x741583022}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_619420821}[生成设备的区域地址]{style="font-family:宋体"}

[[MT capability TLV]{lang="EN-US"}]{#struct_0_17931_14437_2129883195}

[[多拓扑能力]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_17931_14437_x1611037647}

[[MT ID]{lang="EN-US"}]{#struct_0_17931_14437_x390151722}

[[多拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_1425125637}

[[MT overload]{lang="EN-US"}]{#struct_0_17931_14437_1752094191}

[[多拓扑能力]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_17931_14437_2129817659}[中]{style="font-family:宋体"}[overload]{lang="EN-US"}[的置位情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_x1970294335}[：表示置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_1005571370}[：表示没有置位]{lang="EN-US" style="font-family:宋体"}

[[SPB instance sub-TLV]{lang="EN-US"}]{#struct_0_17931_14437_1531680733}

[[SPB]{lang="EN-US"}]{#struct_0_17931_14437_2129752123}[实例子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[CIST root identifier]{lang="EN-US"}]{#struct_0_17931_14437_x42921864}

[[CIST]{lang="EN-US"}]{#struct_0_17931_14437_1045079434}[根标识]{style="font-family:宋体"}

[[CIST ERPC]{lang="EN-US"}]{#struct_0_17931_14437_x250978998}

[[CIST]{lang="EN-US"}]{#struct_0_17931_14437_2129686587}[外部根路径开销]{style="font-family:宋体"}

[[Bridge priority]{lang="EN-US"}]{#struct_0_17931_14437_1159609955}

[[桥优先级]{style="font-family:宋体"}]{#struct_0_17931_14437_x1012116217}

[[SPSourceID]{lang="EN-US"}]{#struct_0_17931_14437_1931969955}

[[最短路径源]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_2129621051}

[[Number of trees]{lang="EN-US"}]{#struct_0_17931_14437_x413819839}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_1915290463}[算法与]{style="font-family:宋体"}[Base VID]{lang="EN-US"}[元组数目]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_2130604091}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x2059127191}

[[U-Bit]{lang="EN-US"}]{#struct_0_17931_14437_1055291449}

[[该]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x469520196}[是否承载流量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_2130538555}[：]{style="font-family:宋体"}[表示承载]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_x2100187752}[：]{style="font-family:宋体"}[表示不承载]{lang="EN-US" style="font-family:宋体"}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_x1857225495}

[[ECT]{lang="EN-US"}]{#struct_0_17931_14437_2130079804}[算法]{style="font-family:宋体"}

[[SPVID]{lang="EN-US"}]{#struct_0_17931_14437_648427735}

[[SPBV]{lang="EN-US"}]{#struct_0_17931_14437_x479742079}[标记]{style="font-family:宋体"}

[[SPBM Service Identifier and Unicast Address sub-TLV]{lang="EN-US"}]{#struct_0_17931_14437_x2023443466}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1263928579}[服务实例和单播地址子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_2130014268}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1846556212}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_1375438738}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17931_14437_2129948732}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1225667861}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_1117399201}[值及标记：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_x642632315}[：]{lang="EN-US" style="font-family:宋体"}[Transmit]{lang="EN-US"}[位置位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_17931_14437_2129883196}[：]{lang="EN-US" style="font-family:宋体"}[Receive]{lang="EN-US"}[位置位]{lang="EN-US" style="font-family:宋体"}

[[Extended neighbor reachability TLV]{lang="EN-US"}]{#struct_0_17931_14437_1464954776}

[[扩展邻居可达]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_17931_14437_x384228076}

[[Hostname]{lang="EN-US"}]{#struct_0_17931_14437_x1611234255}

[[主机名，如果主机未配置则显示设备的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_17931_14437_2129817660}

[[Cost]{lang="EN-US"}]{#struct_0_17931_14437_x1969704510}

[[链路开销]{style="font-family:宋体"}]{#struct_0_17931_14437_992844499}

[[Port number]{lang="EN-US"}]{#struct_0_17931_14437_2129752124}

[[邻居建立的端口个数]{style="font-family:宋体"}]{#struct_0_17931_14437_x43249544}

[ ]{lang="EN-US"}

::: {#-1716663083 .myid}
[]{#_Toc332722569}[]{#_Toc404798186}[]{#struct_0_17931_14437_x1083991152}[]{#_Toc332722571}

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fdb**

------------------------------------------------------------------------

[**[display spbm multicast-fdb]{lang="EN-US"}**]{#struct_0_17931_14437_x1119476848}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1168671954}

[**[display spbm multicast-fdb]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[b-vlan]{lang="EN-US"}**[ *vlan-id* \| **i-sid** *i-sid* \| **system-id** *system-id* \]]{lang="EN-US"}]{#struct_0_17931_14437_2129686588}

[**[display spbm multicast-fdb]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[b-vlan]{lang="EN-US"}**[ *vlan-id* \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_1868239303}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1159937635}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x136973396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2081400932}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x157448385}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x802187415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x932688207}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1785694125}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1606530663}

[**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_2129621052}[：显示指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[i-sid]{lang="EN-US"}**[ *i-sid*]{lang="EN-US"}]{#struct_0_17931_14437_x413754303}[：显示指定]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[255]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[system-id]{lang="EN-US"}***[ system-id]{lang="EN-US"}*]{#struct_0_17931_14437_1136239916}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[System ID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[XXXX.XXXX.XXXX]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[System ID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_17931_14437_349209529}[：显示组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_515180563}

[[如果]{style="font-family:宋体"}**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_x376910945}[、]{style="font-family:宋体"}**[i-sid]{lang="EN-US"}**[ *i-sid*]{lang="EN-US"}[和]{style="font-family:宋体"}**[system-id]{lang="EN-US"}***[ system-id]{lang="EN-US"}*[三个参数都未指定，则显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1164968672}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1044730416}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fdb]{lang="EN-US"}]{#struct_0_17931_14437_729945170}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID            MAC address      B-VLAN   Flags Port]{lang="EN-US"}

[0011.2200.de01       9334-6900-03e8   7        T     GE1/0/2]{lang="EN-US"}

[0011.2200.de01       9334-6900-0190   4        T     GE1/0/2]{lang="EN-US"}

[0011.2200.de01       9334-6900-01f4   5        T     GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1039159805}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fdb count]{lang="EN-US"}]{#struct_0_17931_14437_x1216874412}

[Total entries: 2]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display spbm multicast-fdb]{lang="EN-US"}]{#struct_0_17931_14437_x104085080}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1810828939}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_2130604092}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x2059323799}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_1951407371}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_1679946829}

[[MAC address]{lang="EN-US"}]{#struct_0_17931_14437_x1895370877}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1389450446}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_2130538556}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x2100253288}[地址对应接口所属的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[Flags]{lang="EN-US"}]{#struct_0_17931_14437_1974943781}

[[报文转发标志：]{style="font-family:宋体"}]{#struct_0_17931_14437_1881188483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_17931_14437_x2110533005}[：]{style="font-family:宋体"}[表示出隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_x598803548}[：表示转发]{style="font-family:宋体"}

[[如果字段显示为两个转发标志的组合，如]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_17931_14437_1901709523}[，则表示两个报文转发动作都有发生]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_505953534}

[[出端口，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17931_14437_x341848721}[表示没有出端口]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_705505425}

[[组播]{style="font-family:宋体"}[FDB]{lang="EN-US"}]{#struct_0_17931_14437_x439469790}[表项计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1716663088 .myid}
[]{#_Toc404798187}[]{#struct_0_17931_14437_x1477218943}[]{#_Toc404004329}[]{#_Toc404067765}[]{#_Toc404259965}[]{#_Toc404004330}[]{#_Toc404067766}[]{#_Toc404259966}[]{#_Toc404004331}[]{#_Toc404067767}[]{#_Toc404259967}[]{#_Toc404004332}[]{#_Toc404067768}[]{#_Toc404259968}[]{#_Toc404004333}[]{#_Toc404067769}[]{#_Toc404259969}[]{#_Toc404004334}[]{#_Toc404067770}[]{#_Toc404259970}[]{#_Toc404004335}[]{#_Toc404067771}[]{#_Toc404259971}[]{#_Toc404004336}[]{#_Toc404067772}[]{#_Toc404259972}[]{#_Toc404004337}[]{#_Toc404067773}[]{#_Toc404259973}[]{#_Toc404004338}[]{#_Toc404067774}[]{#_Toc404259974}[]{#_Toc404004339}[]{#_Toc404067775}[]{#_Toc404259975}[]{#_Toc404004340}[]{#_Toc404067776}[]{#_Toc404259976}[]{#_Toc404004341}[]{#_Toc404067777}[]{#_Toc404259977}[]{#_Toc404004342}[]{#_Toc404067778}[]{#_Toc404259978}[]{#_Toc404004343}[]{#_Toc404067779}[]{#_Toc404259979}[]{#_Toc404004344}[]{#_Toc404067780}[]{#_Toc404259980}[]{#_Toc404004345}[]{#_Toc404067781}[]{#_Toc404259981}[]{#_Toc404004346}[]{#_Toc404067782}[]{#_Toc404259982}[]{#_Toc404004347}[]{#_Toc404067783}[]{#_Toc404259983}[]{#_Toc404004354}[]{#_Toc404067790}[]{#_Toc404259990}

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fib**

------------------------------------------------------------------------

[**[display spbm multicast-fib]{lang="EN-US"}**]{#struct_0_17931_14437_x512884304}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1258792332}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x2068366467}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **mac-address** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_x300788767}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_302220898}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_633050715}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **mac-address** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_x599065692}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_349275065}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x64584950}[模式：]{style="font-family:宋体"}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **mac-address** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_1297886020}

[**[display spbm multicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_x1374597037}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1607876829}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x978645991}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_761880729}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x219848390}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_1192458240}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x599131228}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1640124152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1728986372}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_17931_14437_303070515}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_2052179386}[：显示指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[mac-address]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*[ **b-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_17931_14437_794577012}[：显示指定]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址及]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。如果未指定该参数，则显示所有组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_x1846859383}[：显示组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的详细信息。如果未指定该参数，则显示组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_283317926}[：显示指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x599196764}[：显示指定成员设备的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1215173333}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x872083755}[：显示指定成员设备上指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1215632084}[：显示指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_999244863}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1082488369}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_329503252}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fib]{lang="EN-US"}]{#struct_0_17931_14437_1756129011}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[MAC address    B-VLAN Flags Port]{lang="EN-US"}

[0300-0b00-0001 1      TE    GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_56935996}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fib verbose]{lang="EN-US"}]{#struct_0_17931_14437_1245851390}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[MAC address    B-VLAN Flags Epoch       Port                     Port flag]{lang="EN-US"}

[0300-0b00-0001 1      TE    0x1         GE1/0/2                  Done]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2017700563}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0300-0b00-0001]{lang="EN-US"}[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fib mac-address 0300-0b00-0001 b-vlan 1 verbose]{lang="EN-US"}]{#struct_0_17931_14437_x599262300}

[MAC address: 0300-0b00-0001    B-VLAN     : 1]{lang="EN-US"}

[Flags  : TE                 Driver flag: Done         Epoch: 0x1]{lang="EN-US"}

[Context: 0xffffffff 0xffffffff 0xffffffff 0xffffffff]{lang="EN-US"}

[Port                     Context                 Port flag]{lang="EN-US"}

[GE1/0/2                  0xffffaaaa  0xffffaaaa  Done]{lang="EN-US"}

[GE1/0/1                  0xffffaaaa  0xffffbbbb  Done]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2023312394}[显示]{style="font-family:宋体"}[B-VLAN 100]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fib b-vlan 100 count]{lang="EN-US"}]{#struct_0_17931_14437_50002564}

[Total entries: 3]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display spbm multicast-fib]{lang="EN-US"}]{#struct_0_17931_14437_1896758348}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1805882059}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1615416456}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x654110689}

[[MAC address]{lang="EN-US"}]{#struct_0_17931_14437_x598279260}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_758057993}[组播转发的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_408169768}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1988870398}[组播转发的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Flags]{lang="EN-US"}]{#struct_0_17931_14437_1356494449}

[[报文转发标志：]{style="font-family:宋体"}]{#struct_0_17931_14437_x938388963}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_17931_14437_x598344796}[：表示出隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_x845023162}[：表示转发]{style="font-family:宋体"}

[[如果字段显示为两个转发标志的组合，如]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_17931_14437_x71853107}[，则表示两个报文转发动作都有发生]{style="font-family:宋体"}

[[Driver flag]{lang="EN-US"}]{#struct_0_17931_14437_x1216586265}

[[下发驱动标记：]{style="font-family:宋体"}]{#struct_0_17931_14437_1653450330}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nores]{lang="EN-US"}]{#struct_0_17931_14437_x598803547}[：下发驱动资源不足，此时该表项不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Done]{lang="EN-US"}]{#struct_0_17931_14437_1900857555}[：下发驱动成功]{style="font-family:宋体"}

[[Epoch]{lang="EN-US"}]{#struct_0_17931_14437_906068150}

[[表项的时间戳]{style="font-family:宋体"}]{#struct_0_17931_14437_x1404967475}

[[Context]{lang="EN-US"}]{#struct_0_17931_14437_x744756750}

[[保存]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}]{#struct_0_17931_14437_x598869083}[表项下发驱动后返回的驱动信息]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_1146948925}

[[出端口，其中]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_17931_14437_640149381}[表示无出端口]{style="font-family:宋体"}

[[Context]{lang="EN-US"}]{#struct_0_17931_14437_x28470969}

[[出端口对应的驱动信息]{style="font-family:宋体"}]{#struct_0_17931_14437_858461401}

[[Port flag]{lang="EN-US"}]{#struct_0_17931_14437_x598934619}

[[端口下发驱动标记：]{style="font-family:宋体"}]{#struct_0_17931_14437_1100937460}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nores]{lang="EN-US"}]{#struct_0_17931_14437_x1925218154}[：下发驱动资源不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Done]{lang="EN-US"}]{#struct_0_17931_14437_x1347410799}[：下发驱动成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_17931_14437_x599000155}[：端口未下发驱动]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_1465085848}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1868370375}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2073304043 .myid}
[]{#_Toc404798188}[]{#struct_0_17931_14437_x60015547}[]{#_Toc404004356}[]{#_Toc404067792}[]{#_Toc404259992}[]{#_Toc404004357}[]{#_Toc404067793}[]{#_Toc404259993}[]{#_Toc404004358}[]{#_Toc404067794}[]{#_Toc404259994}[]{#_Toc404004359}[]{#_Toc404067795}[]{#_Toc404259995}[]{#_Toc404004360}[]{#_Toc404067796}[]{#_Toc404259996}[]{#_Toc404004361}[]{#_Toc404067797}[]{#_Toc404259997}[]{#_Toc404004362}[]{#_Toc404067798}[]{#_Toc404259998}[]{#_Toc404004363}[]{#_Toc404067799}[]{#_Toc404259999}[]{#_Toc404004364}[]{#_Toc404067800}[]{#_Toc404260000}[]{#_Toc404004365}[]{#_Toc404067801}[]{#_Toc404260001}[]{#_Toc404004366}[]{#_Toc404067802}[]{#_Toc404260002}[]{#_Toc404004367}[]{#_Toc404067803}[]{#_Toc404260003}[]{#_Toc404004368}[]{#_Toc404067804}[]{#_Toc404260004}[]{#_Toc404004369}[]{#_Toc404067805}[]{#_Toc404260005}[]{#_Toc404004370}[]{#_Toc404067806}[]{#_Toc404260006}[]{#_Toc404004371}[]{#_Toc404067807}[]{#_Toc404260007}[]{#_Toc404004372}[]{#_Toc404067808}[]{#_Toc404260008}[]{#_Toc404004373}[]{#_Toc404067809}[]{#_Toc404260009}[]{#_Toc404004374}[]{#_Toc404067810}[]{#_Toc404260010}[]{#_Toc404004375}[]{#_Toc404067811}[]{#_Toc404260011}[]{#_Toc404004376}[]{#_Toc404067812}[]{#_Toc404260012}[]{#_Toc404004377}[]{#_Toc404067813}[]{#_Toc404260013}[]{#_Toc404004378}[]{#_Toc404067814}[]{#_Toc404260014}[]{#_Toc404004379}[]{#_Toc404067815}[]{#_Toc404260015}[]{#_Toc404004380}[]{#_Toc404067816}[]{#_Toc404260016}[]{#_Toc404004381}[]{#_Toc404067817}[]{#_Toc404260017}[]{#_Toc404004382}[]{#_Toc404067818}[]{#_Toc404260018}[]{#_Toc404004383}[]{#_Toc404067819}[]{#_Toc404260019}[]{#_Toc404004384}[]{#_Toc404067820}[]{#_Toc404260020}[]{#_Toc404004391}[]{#_Toc404067827}[]{#_Toc404260027}

**SPBM \-- SPBM配置命令 \-- display spbm multicast-fib statistics**

------------------------------------------------------------------------

[**[display spbm multicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x971163678}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x971016558}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_1368833336}

[**[display spbm multicast-fib]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_17931_14437_1198698646}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1317096561}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm multicast-fib]{lang="EN-US"}**[ **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_x1523539962}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x598279259}[模式：]{style="font-family:宋体"}

[**[display spbm multicast-fib statistics]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_757468172}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x76503615}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_429251582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1504158112}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2102802271}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1548149979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x973881684}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x598344795}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x844826554}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x468232661}[：显示指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x266991150}[：显示指定成员设备的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1215632083}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_21403201}[：显示指定成员设备上指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1580501184}[：显示指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1373342597}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_819868597}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x641282100}[显示成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上单板]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-fib statistics chassis 1 slot 0]{lang="EN-US"}]{#struct_0_17931_14437_x598803550}

[SPBM multicast FIB basic statistics:]{lang="EN-US"}

[RefreshMsg      : 0           DeleteMsg        : 0]{lang="EN-US"}

[AddIfMsg        : 1           DeleteIfMsg      : 0]{lang="EN-US"}

[AddMMACNumber   : 1           DeleteMMACNumber : 0]{lang="EN-US"}

[DeleteNotFound  : 0           AgeNumber        : 0]{lang="EN-US"}

[DrvAdd          : 1           DrvDelete        : 0]{lang="EN-US"}

[DrvAddIf        : 0           DrvDeleteIf      : 0]{lang="EN-US"}

[DrvModifyFlag   : 0]{lang="EN-US"}

[SPBM multicast FIB error statistics:]{lang="EN-US"}

[MMACMsgError    : 0           RefreshMsgFail   : 0]{lang="EN-US"}

[DeleteMsgFail   : 0           AddIfMsgFail     : 0]{lang="EN-US"}

[DeleteIfMsgFail : 0           AddMMACFail      : 0]{lang="EN-US"}

[DrvOtherFail    : 0           DrvDeleteFail    : 0]{lang="EN-US"}

[DrvNoResource   : 0           SynMsgFail       : 0]{lang="EN-US"}

[AllocEntryFail  : 0           AllocReDrvMsgFail: 0]{lang="EN-US"}

[AllocDrvMsgFail : 0]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display spbm multicast-fib statistics]{lang="EN-US"}]{#struct_0_17931_14437_1901185236}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1802349675}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1683516113}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1454399491}

[[SPBM multicast FIB basic statistics]{lang="EN-US"}]{#struct_0_17931_14437_x598869086}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1146621245}[组播转发表基础统计信息]{style="font-family:宋体"}

[[RefreshMsg]{lang="EN-US"}]{#struct_0_17931_14437_x1696155605}

[[添加组播表项消息计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x1314927289}

[[DeleteMsg]{lang="EN-US"}]{#struct_0_17931_14437_1544590751}

[[组播组播表项删除消息计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1629569837}

[[AddIfMsg]{lang="EN-US"}]{#struct_0_17931_14437_x598934622}

[[添加出接口消息计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1100347639}

[[DeleteIfMsg]{lang="EN-US"}]{#struct_0_17931_14437_1981383137}

[[删除出接口消息计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x1971584259}

[[AddMMACNumber]{lang="EN-US"}]{#struct_0_17931_14437_918456913}

[[创建组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x599000158}[地址计数]{style="font-family:宋体"}

[[DeleteMMACNumber]{lang="EN-US"}]{#struct_0_17931_14437_x1630198467}

[[删除组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x37862379}[地址计数]{style="font-family:宋体"}

[[DeleteNotFound]{lang="EN-US"}]{#struct_0_17931_14437_578516835}

[[删除时，查找不到合适的组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_361677169}[地址计数]{style="font-family:宋体"}

[[AgeNumber]{lang="EN-US"}]{#struct_0_17931_14437_x599065694}

[[当前启动老化状态时老化表项的个数]{style="font-family:宋体"}]{#struct_0_17931_14437_x64978166}

[[DrvAdd]{lang="EN-US"}]{#struct_0_17931_14437_x1321761267}

[[添加驱动表项计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x1402053022}

[[DrvDelete]{lang="EN-US"}]{#struct_0_17931_14437_x599131230}

[[删除驱动表项计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x1640648441}

[[DrvAddIf]{lang="EN-US"}]{#struct_0_17931_14437_750878}

[[驱动表项增加出接口计数]{style="font-family:宋体"}]{#struct_0_17931_14437_240453956}

[[DrvDeleteIf]{lang="EN-US"}]{#struct_0_17931_14437_x599196766}

[[驱动表项删除出接口计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x871952683}

[[DrvModifyFlag]{lang="EN-US"}]{#struct_0_17931_14437_1969351714}

[[驱动表项修改转发标记计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1081788555}

[[SPBM multicast FIB error statistics]{lang="EN-US"}]{#struct_0_17931_14437_x599262302}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1896889420}[组播转发表错误统计信息]{style="font-family:宋体"}

[[MMACMsgError]{lang="EN-US"}]{#struct_0_17931_14437_x1986576844}

[[无效的表项消息计数]{style="font-family:宋体"}]{#struct_0_17931_14437_1133524207}

[[RefreshMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x598279262}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_757926921}[地址添加消息处理失败计数]{style="font-family:宋体"}

[[DeleteMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x1091239476}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x381037669}[地址删除消息处理失败计数]{style="font-family:宋体"}

[[AddIfMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x598344798}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x845678522}[地址添加出接口消息处理失败计数]{style="font-family:宋体"}

[[DeleteIfMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x517491098}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x598803549}[地址删除出接口消息处理失败计数]{style="font-family:宋体"}

[[AddUMACFail]{lang="EN-US"}]{#struct_0_17931_14437_1901775059}

[[创建组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1282960021}[地址表项失败计数]{style="font-family:宋体"}

[[DrvOtherFail]{lang="EN-US"}]{#struct_0_17931_14437_2129425993}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x598869085}[地址修改转发标记消息处理失败计数]{style="font-family:宋体"}

[[DrvDeleteFail]{lang="EN-US"}]{#struct_0_17931_14437_1146555709}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x937106078}[地址下发驱动删除失败计数]{style="font-family:宋体"}

[[DrvNoResource]{lang="EN-US"}]{#struct_0_17931_14437_x598934621}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1100413175}[地址下发驱动资源不足计数]{style="font-family:宋体"}

[[SynMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x1151619384}

[[驱动信息同步失败计数]{style="font-family:宋体"}]{#struct_0_17931_14437_x599000157}

[[AllocEntryFail]{lang="EN-US"}]{#struct_0_17931_14437_x1631050435}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x733557636}[地址表项内存申请失败计数]{style="font-family:宋体"}

[[AllocReDrvMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x599065693}

[[重刷组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x64519414}[地址表项内存申请失败计数]{style="font-family:宋体"}

[[AllocDrvMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x606323110}

[[组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x599131229}[地址下发驱动内存申请失败计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#673041602 .myid}
[]{#_Toc404798189}[]{#struct_0_17931_14437_x1640189688}[]{#_Toc332722573}

**SPBM \-- SPBM配置命令 \-- display spbm multicast-pw**

------------------------------------------------------------------------

[**[display spbm multicast-pw]{lang="EN-US"}**]{#struct_0_17931_14437_348139215}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[（]{style="font-family:宋体"}[BEB]{lang="EN-US"}[间建立的组播隧道）信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1012431530}

[**[display spbm multicast-pw]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ **i-sid** ]{lang="EN-US"}*[i-sid ]{lang="EN-US"}*[\]]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[count]{lang="EN-US"}**[ \]]{lang="EN-US"}]{#struct_0_17931_14437_x1457341263}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x541877192}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_381930195}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x95647836}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x599196765}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x872149291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2034636670}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1541227170}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1374964702}

[**[i-sid ]{lang="EN-US"}***[i-sid]{lang="EN-US"}*]{#struct_0_17931_14437_x2118504104}[：显示指定]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[255]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_17931_14437_x1931160251}[：显示组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[计数。如果未指定该参数，则显示组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x565438846}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x599262301}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-pw]{lang="EN-US"}]{#struct_0_17931_14437_1896823884}

[System ID            I-SID      MAC address    B-VLAN Port]{lang="EN-US"}

[0011.2200.0101       300        0300-0a00-012c 10     GE1/0/1]{lang="EN-US"}

[                                                      GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1867977159}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[所有的组播]{style="font-family:宋体"}[PW]{lang="EN-US"}[计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm multicast-pw count]{lang="EN-US"}]{#struct_0_17931_14437_301893218}

[Total entries: 2]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[display spbm multicast-pw]{lang="EN-US"}]{#struct_0_17931_14437_x813565476}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1822062731}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1638846382}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_70844912}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x598279261}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_757992457}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_825159382}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_17931_14437_x309206906}

[[MAC address]{lang="EN-US"}]{#struct_0_17931_14437_1641339382}

[[MAC]{lang="EN-US"}]{#struct_0_17931_14437_376921443}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x598344797}

[[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x844957626}[地址对应接口所属的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_x458175830}

[[出端口列表]{style="font-family:宋体"}]{#struct_0_17931_14437_2081925886}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_348947385}

[[组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_17931_14437_x1582433572}[计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#260523924 .myid}
[]{#_Toc404798190}[]{#struct_0_17931_14437_1339055051}[]{#_Toc374027619}[]{#_Toc404004394}[]{#_Toc404067830}[]{#_Toc404260030}[]{#_Toc404004395}[]{#_Toc404067831}[]{#_Toc404260031}[]{#_Toc404004396}[]{#_Toc404067832}[]{#_Toc404260032}[]{#_Toc404004397}[]{#_Toc404067833}[]{#_Toc404260033}[]{#_Toc404004404}[]{#_Toc404067840}[]{#_Toc404260040}

**SPBM \-- SPBM配置命令 \-- display spbm non-stop-routing event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_1551814167}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_106779042}
:::

[ ]{lang="EN-US"}

[**[display spbm non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_17931_14437_x588033171}[命令用来显示]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1772368023}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x445721734}

[**[display ]{lang="EN-US"}[spbm non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_1456637455}**[ event-log]{lang="EN-US"}**

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x452463475}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[spbm non-stop-routing event-log]{lang="EN-US"}**[ **slot**]{lang="EN-US"}[ *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_1339120587}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x798878476}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[spbm non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_x1357086257}**[ event-log]{lang="EN-US"}**[ **chassis**]{lang="EN-US"}[ ]{lang="EN-US"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1105226659}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1416950427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_758154253}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1963101137}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_1339186123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1209455676}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1395446593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x417513114}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_123237550}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_1410387511}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x1215501018}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_457275876}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_x530296318}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1287486354}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1339251659}[显示成员设备]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display spbm non-stop-routing event-log slot 0]{lang="EN-US"}]{#struct_0_17931_14437_x800415547}

[SPBM log information]{lang="EN-US"}[：]{style="font-family:宋体"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Initialization).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Smooth).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (LSP stability).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (LSP generation).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (SPF computation).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Flush smooth).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 enter NSR phase (Finish).]{lang="EN-US"}

[Aug 22 08:21:17 2013 -Slot=0 NSR complete.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2005190547}[显示单板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}[ display spbm non-stop-routing event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_504153605}

[SPBM log information:]{lang="EN-US"}

[Oct  5 12:54:53 2013 -Slot=1 HA backup channel was blocked.]{lang="EN-US"}

[Oct  5 12:54:55 2013 -Slot=1 HA backup channel was unblocked.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1339317195}[显示单板]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\>]{lang="EN-US"}[ display spbm non-stop-routing event-log slot 2]{lang="EN-US"}]{#struct_0_17931_14437_367048550}

[SPBM log information:]{lang="EN-US"}

[Oct  6 15:50:56 2013 -Slot=2 Memory restore on the standby MPU triggered data batch backup.]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[display spbm non-stop-routing event-log]{lang="EN-US"}]{#struct_0_17931_14437_633572057}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x343723293}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x138217844}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1339382731}

[[Initialization]{lang="EN-US"}]{#struct_0_17931_14437_733675127}

[[进入]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17931_14437_1339448267}[的初始化阶段]{style="font-family:宋体"}

[[Smooth]{lang="EN-US"}]{#struct_0_17931_14437_x1238714003}

[[进入]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17931_14437_1000618585}[的平滑阶段]{style="font-family:宋体"}

[[LSP stability]{lang="EN-US"}]{#struct_0_17931_14437_1339513803}

[[进入]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x2029156077}[稳定阶段]{style="font-family:宋体"}

[[LSP generation]{lang="EN-US"}]{#struct_0_17931_14437_1338923984}

[[进入]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x472545129}[生成阶段]{style="font-family:宋体"}

[[SPF computation]{lang="EN-US"}]{#struct_0_17931_14437_1338989520}

[[进入路由计算阶段]{style="font-family:宋体"}]{#struct_0_17931_14437_709116975}

[[Flush smooth]{lang="EN-US"}]{#struct_0_17931_14437_x1725487726}

[[进入内核数据平滑阶段]{style="font-family:宋体"}]{#struct_0_17931_14437_1339055056}

[[Finish]{lang="EN-US"}]{#struct_0_17931_14437_1552010775}

[[进入]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17931_14437_1339120592}[的结束阶段]{style="font-family:宋体"}

[[NSR complete]{lang="EN-US"}]{#struct_0_17931_14437_x798681867}

[[完成]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17931_14437_1339186128}

[[HA backup channel was blocked]{lang="EN-US"}]{#struct_0_17931_14437_x1209127996}

[[降级（主进程变为备进程）过程中进入实时备份和批量备份通道阻塞状态]{style="font-family:宋体"}]{#struct_0_17931_14437_1339251664}

[[HA backup channel was unblocked]{lang="EN-US"}]{#struct_0_17931_14437_x799563580}

[[降级结束退出实时备份和批量备份通道阻塞状态]{style="font-family:宋体"}]{#struct_0_17931_14437_2140850236}

[[Memory restore on the standby MPU triggered data batch backup]{lang="EN-US"}]{#struct_0_17931_14437_1339317200}

[[备板内存恢复之后，会主动触发一次数据批量备份请求]{style="font-family:宋体"}]{#struct_0_17931_14437_x1206601875}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2005047668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ spbm ]{lang="EN-US"}**]{#struct_0_17931_14437_1339382736}**[non-stop-routing]{lang="EN-US"}[ event-log]{lang="EN-US"}**

::::: {#2067844463 .myid}
[]{#_Toc404798191}[]{#struct_0_17931_14437_734002807}[]{#_Toc374027620}

**SPBM \-- SPBM配置命令 \-- display spbm non-stop-routing status**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1113862359}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_1608091273}
:::

[ ]{lang="EN-US"}

[**[display spbm non-stop-routing status]{lang="EN-US"}**]{#struct_0_17931_14437_x1537959797}[命令用来显示]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x558471740}

[**[display spbm non-stop-routing status]{lang="EN-US"}**]{#struct_0_17931_14437_x430604815}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1339448272}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1238517396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_995137579}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2074672190}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x361426441}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1758518506}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1413691067}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1851001694}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1339513808}[显示]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm non-stop-routing status]{lang="EN-US"}]{#struct_0_17931_14437_x2028435181}

[ ]{lang="EN-US"}

[                     Nonstop Routing information for SPBM]{lang="EN-US"}

[                     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[NSR phase: Finish]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[display spbm non-stop-routing status]{lang="EN-US"}]{#struct_0_17931_14437_1751331446}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x326976277}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_1130999964}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1338923985}

[[NSR phase]{lang="EN-US"}]{#struct_0_17931_14437_x472479593}

[[当前设备的]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17931_14437_1338989521}[阶段：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_17931_14437_709182511}[：进入]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[的初始化阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_17931_14437_1347329535}[：进入]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[的平滑阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_17931_14437_1339055057}[：进入]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[稳定阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_17931_14437_1551945239}[：进入]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生成阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPF computation]{lang="EN-US"}]{#struct_0_17931_14437_1339120593}[：进入路由计算阶段]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flush smooth]{lang="EN-US"}]{#struct_0_17931_14437_x798616331}[：进入内核数据平滑阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_17931_14437_1339186129}[：]{lang="EN-US" style="font-family:宋体"}[进入]{style="font-family:宋体"}[NSR]{lang="EN-US"}[的]{style="font-family:宋体"}[结束阶段]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-498498066 .myid}
[]{#_Toc404798192}[]{#struct_0_17931_14437_x598869088}

**SPBM \-- SPBM配置命令 \-- display spbm peer**

------------------------------------------------------------------------

[**[display spbm peer]{lang="EN-US"}**]{#struct_0_17931_14437_1146228029}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x156440338}

[**[display]{lang="EN-US"}**[ **spbm** **peer** \[ **system-id** *system-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_x794692982}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1427358408}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1184075835}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1053134570}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1634685577}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x598934624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1100216567}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1975520612}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1626721179}

[**[system-id ]{lang="EN-US"}***[system-id]{lang="EN-US"}*]{#struct_0_17931_14437_x1532051079}**[：]{style="font-family:宋体"}**[显示指定邻居的信息，]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[XXXX.XXXX.XXXX]{lang="EN-US"}[。如果未指定该参数，则显示所有邻居的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_x87166194}[：显示邻居的详细信息。如果未指定该参数，则显示邻居的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1120760278}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x702803606}[显示所有邻居的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm peer]{lang="EN-US"}]{#struct_0_17931_14437_x599000160}

[                          Peer information for SPBM]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID         Port                        Circuit ID    State    Holdtime]{lang="EN-US"}

[5555.1111.1111    GE1/0/2                     1             Up       28s]{lang="EN-US"}

[5555.1111.2222    GE1/0/3                     1             Up\*      20s]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1630722754}[显示所有邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm peer verbose]{lang="EN-US"}]{#struct_0_17931_14437_x599196768}

[                          Peer information for SPBM]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID         Port                        Circuit ID    State    Holdtime]{lang="EN-US"}

[5555.1111.1111    GE1/0/2                     1             Up       28s]{lang="EN-US"}

[Peer information:]{lang="EN-US"}

[  Host name: spbm-2]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[Local information:]{lang="EN-US"}

[  Host name: spbm-1]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format Selector      : 0]{lang="EN-US"}

[    Region Name          : spb]{lang="EN-US"}

[    Revision Level       : 0]{lang="EN-US"}

[    Configuration Digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID         Port                        Circuit ID    State    Holdtime]{lang="EN-US"}

[5555.1111.2222    GE1/0/3                     1             Up       20s]{lang="EN-US"}

[Peer information:]{lang="EN-US"}

[  Host name: spbm-3]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[Local information:]{lang="EN-US"}

[  Host name: spbm-1]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x872345899}[显示]{style="font-family:宋体"}[System ID]{lang="EN-US"}[为]{style="font-family:宋体"}[5555.1111.1111]{lang="EN-US"}[的邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm peer system-id 5555.1111.1111 verbose]{lang="EN-US"}]{#struct_0_17931_14437_x598279264}

[                          Peer information for SPBM]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID         Port                        Circuit ID    State    Holdtime]{lang="EN-US"}

[5555.1111.1111    GE1/0/1                     1             Up       28s]{lang="EN-US"}

[Peer information:]{lang="EN-US"}

[  Host name: spbm-2]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[Local information:]{lang="EN-US"}

[  Host name: spbm-1]{lang="EN-US"}

[  Circuit ID: 1      Cost: 10]{lang="EN-US"}

[  MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  Aux MCID information:]{lang="EN-US"}

[    Format selector      : 0]{lang="EN-US"}

[    Region name          : spb]{lang="EN-US"}

[    Revision level       : 0]{lang="EN-US"}

[    Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[  AP information:]{lang="EN-US"}

[    AN: 2    DAN: 0    Valid: 1]{lang="EN-US"}

[    Format identifier       : 0]{lang="EN-US"}

[    Format capabilities     : 0]{lang="EN-US"}

[    Convention identifier   : 0]{lang="EN-US"}

[    Convention capabilities : 0]{lang="EN-US"}

[    Edge count              : 2]{lang="EN-US"}

[    Topology digest         : 0x000000dc12854410daa2c29221f095144f661000]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display spbm peer]{lang="EN-US"}]{#struct_0_17931_14437_758320137}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1817259819}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x598344800}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x507447217}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x230142157}

[[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x468923581}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_889814914}

[[与对端相连的本地]{style="font-family:宋体"}]{#struct_0_17931_14437_x598803551}[SPBM]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_17931_14437_1901250772}

[[邻居电路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_2093818925}

[[State]{lang="EN-US"}]{#struct_0_17931_14437_138061390}

[[邻居状态：]{style="font-family:宋体"}]{#struct_0_17931_14437_x268631403}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_17931_14437_x598869087}[：表示请求与邻居建立连接]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_17931_14437_1146686781}[：表示邻居已建立，与邻居间的连接处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，邻居可以承载流量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up\*]{lang="EN-US"}]{#struct_0_17931_14437_x536508422}[：表示邻居已建立，与邻居间的连接处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，但邻居不能承载流量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_17931_14437_1905035085}[：表示邻居已建立，与邻居间的连接处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_17931_14437_1825860329}

[[抑制时间，如果在抑制时间内没有收到邻居发送的]{style="font-family:宋体"}]{#struct_0_17931_14437_x598934623}[Hello]{lang="EN-US"}[报文，则认为邻居已经失效，如果收到了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则抑制时间将重置为初始值]{style="font-family:宋体"}

[[Peer information]{lang="EN-US"}]{#struct_0_17931_14437_1100282103}

[[邻居信息]{style="font-family:宋体"}]{#struct_0_17931_14437_403258102}

[[Host name]{lang="EN-US"}]{#struct_0_17931_14437_x2005365854}

[[邻居主机名，未配置主机名时显示邻居]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_17931_14437_1776868358}

[[Circuit ID]{lang="EN-US"}]{#struct_0_17931_14437_x599000159}

[[邻居电路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_x1630132931}

[[Cost]{lang="EN-US"}]{#struct_0_17931_14437_x1090355948}

[[邻居链路]{style="font-family:宋体"}]{#struct_0_17931_14437_1179207541}[开销值]{style="font-family:宋体"}

[[MCID information]{lang="EN-US"}]{#struct_0_17931_14437_x599065695}

[[邻居携带的主]{style="font-family:宋体"}]{#struct_0_17931_14437_x64912630}[MCID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Aux MCID information]{lang="EN-US"}]{#struct_0_17931_14437_x501459672}

[[邻居携带的辅助]{style="font-family:宋体"}]{#struct_0_17931_14437_x1846474021}[MCID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Format selector]{lang="EN-US"}]{#struct_0_17931_14437_x599131231}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_x1640713977}[生成树协议规定的选择因子，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，不可配置]{style="font-family:宋体"}

[[Region name]{lang="EN-US"}]{#struct_0_17931_14437_x1965194264}

[[邻居]{style="font-family:宋体"}[MST]{lang="EN-US"}]{#struct_0_17931_14437_1387616593}[域的域名]{style="font-family:宋体"}

[[Revision level]{lang="EN-US"}]{#struct_0_17931_14437_1296523373}

[[邻居]{style="font-family:宋体"}[MST]{lang="EN-US"}]{#struct_0_17931_14437_x599196767}[域的修订级别，可使用命令]{style="font-family:宋体"}**[revision-level]{lang="EN-US"}**[来配置，缺省为]{style="font-family:宋体"}[0]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Configuration digest]{lang="EN-US"}]{#struct_0_17931_14437_x872018219}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_707812546}[配置摘要]{style="font-family:宋体"}

[[AP information]{lang="EN-US"}]{#struct_0_17931_14437_x599262303}

[[邻居携带的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_1896954956}[信息，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示未携带]{style="font-family:宋体"}[AP]{lang="EN-US"}[相关信息]{style="font-family:宋体"}

[[AN]{lang="EN-US"}]{#struct_0_17931_14437_x845403657}

[[邻居携带的]{style="font-family:宋体"}[Agreement Number]{lang="EN-US"}]{#struct_0_17931_14437_x876897098}

[[DAN]{lang="EN-US"}]{#struct_0_17931_14437_x598279263}

[[邻居携带的]{style="font-family:宋体"}[Discarded Agreement Number]{lang="EN-US"}]{#struct_0_17931_14437_757861385}

[[Valid]{lang="EN-US"}]{#struct_0_17931_14437_775655154}

[[邻居携带的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_719689320}[摘要是否有效：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_x598344799}[：]{style="font-family:宋体"}[表示摘要无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_x845612986}[：]{style="font-family:宋体"}[表示摘要有效]{lang="EN-US" style="font-family:宋体"}

[[Format identifier]{lang="EN-US"}]{#struct_0_17931_14437_x24696734}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_967280393}[摘要类型标识]{style="font-family:宋体"}

[[Format capabilities]{lang="EN-US"}]{#struct_0_17931_14437_x1008809932}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_1701677140}[摘要格式类型]{style="font-family:宋体"}

[[Convention identifier]{lang="EN-US"}]{#struct_0_17931_14437_967214857}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_974368284}[约定标识，发布环路避免的转发规则：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_920680449}[：表示无需匹配邻居的摘要信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17931_14437_967149321}[：表示发送者将继续进行无环路的组播和单播发送，即邻居之间严格]{style="font-family:宋体"}[Agreement]{lang="EN-US"}[之后才能转发流量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17931_14437_x934689082}[：表示发送者继续进行无环路的组播转发]{style="font-family:宋体"}

[[Convention capabilities]{lang="EN-US"}]{#struct_0_17931_14437_x1058073830}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_967083785}[支持的摘要协商能力]{style="font-family:宋体"}

[[Edge count]{lang="EN-US"}]{#struct_0_17931_14437_x1283155294}

[[邻居]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_x763041459}[协议计算摘要需要的参数]{style="font-family:宋体"}

[[Topology digest]{lang="EN-US"}]{#struct_0_17931_14437_967018249}

[[邻居]{style="font-family:宋体"}]{#struct_0_17931_14437_x138986452}[拓朴摘要信息]{style="font-family:宋体"}

[[Local information]{lang="EN-US"}]{#struct_0_17931_14437_x277087809}

[[本地信息]{style="font-family:宋体"}]{#struct_0_17931_14437_966952713}

[[Hostname]{lang="EN-US"}]{#struct_0_17931_14437_x50355826}

[[本地主机名，未配置主机名时显示]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_17931_14437_966887177}

[[Circuit ID]{lang="EN-US"}]{#struct_0_17931_14437_x781654275}

[[本地电路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_554506138}

[[Cost]{lang="EN-US"}]{#struct_0_17931_14437_966821641}

[[本地链路]{style="font-family:宋体"}]{#struct_0_17931_14437_x1991430856}[开销值]{style="font-family:宋体"}

[[MCID information]{lang="EN-US"}]{#struct_0_17931_14437_197119952}

[[本地携带的]{style="font-family:宋体"}]{#struct_0_17931_14437_967804681}[MCID]{lang="EN-US"}

[[Aux MCID information]{lang="EN-US"}]{#struct_0_17931_14437_1613041201}

[[本地携带的辅助]{style="font-family:宋体"}]{#struct_0_17931_14437_967739145}[MCID]{lang="EN-US"}

[[Format selector]{lang="EN-US"}]{#struct_0_17931_14437_1853808281}

[[本地生成树协议规定的选择因子，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17931_14437_1714931945}[，不可配置]{style="font-family:宋体"}

[[Region name]{lang="EN-US"}]{#struct_0_17931_14437_967280394}

[[本地]{style="font-family:宋体"}[MST]{lang="EN-US"}]{#struct_0_17931_14437_x1008809931}[域的域名]{style="font-family:宋体"}

[[Revision level]{lang="EN-US"}]{#struct_0_17931_14437_967214858}

[[本地]{style="font-family:宋体"}[MST]{lang="EN-US"}]{#struct_0_17931_14437_974368287}[域的修订级别，可使用命令]{style="font-family:宋体"}**[revision-level]{lang="EN-US"}**[来配置，缺省为]{style="font-family:宋体"}[0]{lang="EN-US"}[级]{style="font-family:宋体"}

[[Configuration digest]{lang="EN-US"}]{#struct_0_17931_14437_967149322}

[[本地配置摘要]{style="font-family:宋体"}]{#struct_0_17931_14437_x934689081}

[[AP information]{lang="EN-US"}]{#struct_0_17931_14437_x1057877222}

[[本地携带的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_967083786}[信息，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表项未携带]{style="font-family:宋体"}[AP]{lang="EN-US"}[相关信息]{style="font-family:宋体"}

[[AN]{lang="EN-US"}]{#struct_0_17931_14437_x1283155293}

[[本地携带的]{style="font-family:宋体"}[Agreement Number]{lang="EN-US"}]{#struct_0_17931_14437_967018250}

[[DAN]{lang="EN-US"}]{#struct_0_17931_14437_x2095301595}

[[本地携带的]{style="font-family:宋体"}[Discarded Agreement Number]{lang="EN-US"}]{#struct_0_17931_14437_966952714}

[[Valid]{lang="EN-US"}]{#struct_0_17931_14437_x50355831}

[[本地发送的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_1944622617}[摘要是否有效：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17931_14437_966887178}[：表示摘要无效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_x781654290}[：表示摘要有效]{style="font-family:宋体"}

[[Format identifier]{lang="EN-US"}]{#struct_0_17931_14437_966821642}

[[本地摘要类型标识]{style="font-family:宋体"}]{#struct_0_17931_14437_x1991430859}

[[Format capabilities]{lang="EN-US"}]{#struct_0_17931_14437_967804682}

[[本地摘要格式类型]{style="font-family:宋体"}]{#struct_0_17931_14437_1613041202}

[[Convention identifier]{lang="EN-US"}]{#struct_0_17931_14437_967739146}

[[本地约定标识，发布环路避免的转发规则：]{style="font-family:宋体"}]{#struct_0_17931_14437_1853808280}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17931_14437_967280391}[：表示无需匹配邻居的摘要信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17931_14437_x1008809934}[：表示发送者将继续进行无环路的组播和单播发送，即邻居之间严格]{style="font-family:宋体"}[Agreement]{lang="EN-US"}[之后才能转发流量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17931_14437_967214855}[：表示发送者继续进行无环路的组播转发]{style="font-family:宋体"}

[[Convention capabilities]{lang="EN-US"}]{#struct_0_17931_14437_974368282}

[[本地支持的摘要协商能力]{style="font-family:宋体"}]{#struct_0_17931_14437_920680451}

[[Edge count]{lang="EN-US"}]{#struct_0_17931_14437_967149319}

[[本地]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_17931_14437_639289022}[摘要边数]{style="font-family:宋体"}

[[Topology digest]{lang="EN-US"}]{#struct_0_17931_14437_967083783}

[[本地拓朴摘要信息]{style="font-family:宋体"}]{#struct_0_17931_14437_x1283155296}

[]{#_Toc326076038}[]{#_Toc323196012}[[ ]{lang="EN-US"}]{#_Toc323114956}

::: {#-1295625806 .myid}
[]{#_Toc404798193}[]{#struct_0_17931_14437_967018247}[]{#_Toc326076034}[]{#_Toc323196008}[]{#_Toc323114952}

**SPBM \-- SPBM配置命令 \-- display spbm summary**

------------------------------------------------------------------------

[**[display spbm summary]{lang="EN-US"}**]{#struct_0_17931_14437_x138986454}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x276694593}

[**[display spbm summary]{lang="EN-US"}**]{#struct_0_17931_14437_1686689076}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_437864173}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x571298766}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1396333822}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_966952711}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x50355828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x11692510}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1006358317}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1866183862}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1016949010}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm summary]{lang="EN-US"}]{#struct_0_17931_14437_966887175}

[                   Summary information for SPBM]{lang="EN-US"}

[                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Area address           : 00.0000]{lang="EN-US"}

[System ID              : 0011.2200.0001]{lang="EN-US"}

[System control address : 0180-c200-002e]{lang="EN-US"}

[System name            : spb-1]{lang="EN-US"}

[Bridge priority        : 32768]{lang="EN-US"}

[SPSource ID            : 200]{lang="EN-US"}

[SPSource mode          : Static]{lang="EN-US"}

[Agreement mode         : Both]{lang="EN-US"}

[MCID information:]{lang="EN-US"}

[  Format selector      : 0]{lang="EN-US"}

[  Region name          : spb]{lang="EN-US"}

[  Revision level       : 0]{lang="EN-US"}

[  Configuration digest : 0x0253c1480d244e443b21e7c364d6e2a7]{lang="EN-US"}

[B-VLANs                : 1-10, 100-200]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[display spbm summary]{lang="EN-US"}]{#struct_0_17931_14437_x781654277}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1840801163}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_554375066}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x167890054}

[[Area address]{lang="EN-US"}]{#struct_0_17931_14437_966821639}

[[区域地址]{style="font-family:宋体"}]{#struct_0_17931_14437_729558336}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_x1378885447}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_x1487508482}

[[System control address]{lang="EN-US"}]{#struct_0_17931_14437_1539876180}

[[协议控制地址]{style="font-family:宋体"}]{#struct_0_17931_14437_967804679}

[[System name]{lang="EN-US"}]{#struct_0_17931_14437_1275334201}

[[系统名]{style="font-family:宋体"}]{#struct_0_17931_14437_x496302186}

[[Bridge priority]{lang="EN-US"}]{#struct_0_17931_14437_711081110}

[[桥优先级]{style="font-family:宋体"}]{#struct_0_17931_14437_153188364}

[[SPSource ID]{lang="EN-US"}]{#struct_0_17931_14437_967739143}

[[最短路径源]{style="font-family:宋体"}]{#struct_0_17931_14437_1853808275}[ID]{lang="EN-US"}

[[SPSource mode]{lang="EN-US"}]{#struct_0_17931_14437_1715194086}

[[最短路径源模式：]{style="font-family:宋体"}]{#struct_0_17931_14437_x518203543}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_17931_14437_967280392}[：表明为静态配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_17931_14437_x1008809933}[：表明为动态生成]{style="font-family:宋体"}

[[Agreement mode]{lang="EN-US"}]{#struct_0_17931_14437_x1027206215}

[[AP]{lang="EN-US"}]{#struct_0_17931_14437_x621520975}[模式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both]{lang="EN-US"}]{#struct_0_17931_14437_967214856}[：表示对单播表项、组播表项都进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast]{lang="EN-US"}]{#struct_0_17931_14437_974368285}[：表示仅对组播表项进行]{style="font-family:宋体"}[AP]{lang="EN-US"}[检测]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_17931_14437_920680450}[：表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[模式关闭]{style="font-family:宋体"}

[[MCID information]{lang="EN-US"}]{#struct_0_17931_14437_967149320}

[[本地]{style="font-family:宋体"}]{#struct_0_17931_14437_x934689083}[MCID]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Format selector]{lang="EN-US"}]{#struct_0_17931_14437_x1058008294}

[[生成树协议规定的选择因子，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17931_14437_1689010504}[，不可配置]{style="font-family:宋体"}

[[Region name]{lang="EN-US"}]{#struct_0_17931_14437_967083784}

[[MST]{lang="EN-US"}]{#struct_0_17931_14437_x1283155295}[域的域名]{style="font-family:宋体"}

[[Revision level]{lang="EN-US"}]{#struct_0_17931_14437_1965841896}

[[MST]{lang="EN-US"}]{#struct_0_17931_14437_967018248}[域的修订级别，可使用命令]{style="font-family:宋体"}**[revision-level]{lang="EN-US"}**[来配置，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Configuration digest]{lang="EN-US"}]{#struct_0_17931_14437_x138986451}

[[配置摘要]{style="font-family:宋体"}]{#struct_0_17931_14437_x276891201}

[[B-VLANs]{lang="EN-US"}]{#struct_0_17931_14437_1960221216}

[[本地配置的]{style="font-family:宋体"}]{#struct_0_17931_14437_1243990184}[B-VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-786860686 .myid}
[]{#_Toc332722568}[]{#_Toc404798194}[]{#struct_0_17931_14437_x1793683864}[]{#_Toc332722570}

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fdb**

------------------------------------------------------------------------

[**[display spbm unicast-fdb]{lang="EN-US"}**]{#struct_0_17931_14437_x414728013}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1360557977}

[**[display spbm unicast-fdb]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[b-mac]{lang="EN-US"}**[ *mac-address* \| **b-vlan** *vlan-id* \| **system-id** *system-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_17931_14437_966952712}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x50355825}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x11692515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1006358320}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1462964871}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_356742313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1253878173}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x885667610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_966887176}

[**[b-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_17931_14437_x781654276}[：显示指定]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_554440602}[：显示指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[system-id]{lang="EN-US"}**[ *system-id*]{lang="EN-US"}]{#struct_0_17931_14437_x266373195}[：显示指定]{style="font-family:宋体"}[System ID]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[XXXX.XXXX.XXXX]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[System ID]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_17931_14437_x1350633388}[：显示单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项计数。如果未指定本参数，则显示单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_1622626722}

[[如果]{style="font-family:宋体"}**[b-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_17931_14437_1622561186}[、]{style="font-family:宋体"}**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*[和]{style="font-family:宋体"}**[system-id]{lang="EN-US"}**[ *system-id*]{lang="EN-US"}[三个参数都未指定，则显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1175994687}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_175638100}[显示所有]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fdb]{lang="EN-US"}]{#struct_0_17931_14437_966821640}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[System ID            B-MAC            B-VLAN   Flags Port]{lang="EN-US"}

[0011.2200.0001       0011-2200-0001   9        T     GE1/0/2]{lang="EN-US"}

[0011.2200.0001       0011-2200-0001   4        T     GE1/0/2]{lang="EN-US"}

[0011.2200.0001       0011-2200-0001   5        T     GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_571222161}[显示所有的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fdb count]{lang="EN-US"}]{#struct_0_17931_14437_1564573640}

[Total entries: 2]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[display spbm unicast-fdb]{lang="EN-US"}]{#struct_0_17931_14437_1383903703}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1835480043}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1976958544}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_967804680}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_1613041200}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_x1720479607}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_173724856}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1333347786}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1412060056}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_967739144}[对应接口所属的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[Flags]{lang="EN-US"}]{#struct_0_17931_14437_1853808282}

[[报文转发标志：]{style="font-family:宋体"}]{#struct_0_17931_14437_1714866409}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_17931_14437_x1731138222}[：表示出隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_x1489638724}[：表示转发]{lang="EN-US" style="font-family:宋体"}

[[如果字段显示为两个转发标志的组合，如]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_17931_14437_967280389}[，则表示两个报文转发动作都有发生]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_947505194}

[[出端口]{style="font-family:宋体"}]{#struct_0_17931_14437_x1348608520}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_x591577253}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1870816605}[单播]{style="font-family:宋体"}[FDB]{lang="EN-US"}[表项计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1902605933 .myid}
[]{#_Toc404798195}[]{#struct_0_17931_14437_974368280}[]{#_Toc404004410}[]{#_Toc404067846}[]{#_Toc404260046}[]{#_Toc404004411}[]{#_Toc404067847}[]{#_Toc404260047}[]{#_Toc404004412}[]{#_Toc404067848}[]{#_Toc404260048}[]{#_Toc404004413}[]{#_Toc404067849}[]{#_Toc404260049}[]{#_Toc404004414}[]{#_Toc404067850}[]{#_Toc404260050}[]{#_Toc404004415}[]{#_Toc404067851}[]{#_Toc404260051}[]{#_Toc404004416}[]{#_Toc404067852}[]{#_Toc404260052}[]{#_Toc404004417}[]{#_Toc404067853}[]{#_Toc404260053}[]{#_Toc404004418}[]{#_Toc404067854}[]{#_Toc404260054}[]{#_Toc404004419}[]{#_Toc404067855}[]{#_Toc404260055}[]{#_Toc404004420}[]{#_Toc404067856}[]{#_Toc404260056}[]{#_Toc404004421}[]{#_Toc404067857}[]{#_Toc404260057}[]{#_Toc404004422}[]{#_Toc404067858}[]{#_Toc404260058}[]{#_Toc404004423}[]{#_Toc404067859}[]{#_Toc404260059}[]{#_Toc404004424}[]{#_Toc404067860}[]{#_Toc404260060}[]{#_Toc404004425}[]{#_Toc404067861}[]{#_Toc404260061}[]{#_Toc404004426}[]{#_Toc404067862}[]{#_Toc404260062}[]{#_Toc404004427}[]{#_Toc404067863}[]{#_Toc404260063}[]{#_Toc404004428}[]{#_Toc404067864}[]{#_Toc404260064}[]{#_Toc404004429}[]{#_Toc404067865}[]{#_Toc404260065}[]{#_Toc404004430}[]{#_Toc404067866}[]{#_Toc404260066}[]{#_Toc404004431}[]{#_Toc404067867}[]{#_Toc404260067}[]{#_Toc404004432}[]{#_Toc404067868}[]{#_Toc404260068}[]{#_Toc404004439}[]{#_Toc404067875}[]{#_Toc404260075}[]{#_Toc347676218}[]{#_Toc347676219}[]{#_Toc347676220}[]{#_Toc347676221}[]{#_Toc347676222}[]{#_Toc347676223}[]{#_Toc347676224}[]{#_Toc347676225}[]{#_Toc347676226}[]{#_Toc347676227}[]{#_Toc347676228}[]{#_Toc347676229}[]{#_Toc347676230}[]{#_Toc347676231}[]{#_Toc347676232}[]{#_Toc347676233}[]{#_Toc347676234}[]{#_Toc347676235}[]{#_Toc347676236}[]{#_Toc347676237}[]{#_Toc347676244}

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fib**

------------------------------------------------------------------------

[**[display spbm unicast-fib]{lang="EN-US"}**]{#struct_0_17931_14437_920680453}[命令用来显示]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1245975783}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x727784218}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-mac** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_1725378317}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_x1398080771}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1763714855}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-mac** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_x458225530}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_x342416136}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_967149317}[模式：]{style="font-family:宋体"}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-mac** *mac-address* \[ **b-vlan** *vlan-id* \] \| **b-vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_17931_14437_639289028}

[**[display spbm unicast-fib]{lang="EN-US"}**[ \[ **b-vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] **count**]{lang="EN-US"}]{#struct_0_17931_14437_1330802584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x707249112}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1141836339}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1688238291}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_528907911}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x214813136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x403606191}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_967083781}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1283155298}

[**[b-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_17931_14437_1918787729}[：显示指定]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。在配置时，用户可以省去]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址中每段开头的"]{style="font-family:宋体"}[0]{lang="EN-US"}["，例如输入"]{style="font-family:宋体"}[f-e2-1]{lang="EN-US"}["即表示输入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为"]{style="font-family:宋体"}[000f-00e2-0001]{lang="EN-US"}["。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[b-vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_17931_14437_2088008033}[：显示指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[b-mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*[ **b-vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_17931_14437_x1241201124}[：显示指定]{style="font-family:
宋体"}[B-MAC]{lang="EN-US"}[及]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。如果未指定本参数，则显示所有的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17931_14437_1225775707}[：显示单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的详细信息。如果未指定本参数，则显示单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的简要信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x445196882}[：显示指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_967018245}[：显示指定成员设备的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_350910609}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x138986456}[：显示指定成员设备上指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1990589307}[：显示指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_x959703380}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_17931_14437_215057337}[：显示单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x276825665}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1320378578}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表的所有表项的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fib]{lang="EN-US"}]{#struct_0_17931_14437_747362522}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[B-MAC          B-VLAN Flags Port]{lang="EN-US"}

[0011-2200-0101 1      T     GE1/0/1]{lang="EN-US"}

[0011-2200-0101 2      T     GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x115247058}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表的所有表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fib verbose]{lang="EN-US"}]{#struct_0_17931_14437_966952709}

[Flags: E-Egress T-Transit]{lang="EN-US"}

[ ]{lang="EN-US"}

[B-MAC          B-VLAN Flags Driver flag Epoch       Port]{lang="EN-US"}

[0011-2200-0101 1      T     Done        0x1         GE1/0/2]{lang="EN-US"}

[0011-2200-0101 2      T     Done        0x1         GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2006670972}[显示]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[为]{style="font-family:宋体"}[0011-2200-0101]{lang="EN-US"}[、]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fib b-mac 0011-2200-0101 b-vlan 1 verbose]{lang="EN-US"}]{#struct_0_17931_14437_x1024538941}

[B-MAC  : 0011-2200-0101   B-VLAN     : 1]{lang="EN-US"}

[Port   : GE1/0/2]{lang="EN-US"}

[Flags  : T                Driver flag: Done]{lang="EN-US"}

[Epoch  : 0x1]{lang="EN-US"}

[Context: 0xffffffff 0xffffffff 0xffffffff 0xffffffff]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1351026604}[显示]{style="font-family:宋体"}[B-VLAN 100]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fib b-vlan 100 count]{lang="EN-US"}]{#struct_0_17931_14437_x756806568}

[Total entries: 2]{lang="EN-US"}

[[表1-26 ]{lang="EN-US"}[display spbm unicast-fib]{lang="EN-US"}]{#struct_0_17931_14437_x1948372486}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1831980715}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_939215855}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_966887173}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_x781654279}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_554243994}[单播转发表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1739109172}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_230735084}[单播转发表项的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_x2072897854}

[[出端口]{style="font-family:宋体"}]{#struct_0_17931_14437_966821637}

[[Flags]{lang="EN-US"}]{#struct_0_17931_14437_729558330}

[[报文转发标志：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1378885453}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_17931_14437_481925522}[：表示出隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_967804677}[：表示转发]{lang="EN-US" style="font-family:宋体"}

[[如果字段显示为两个转发标志的组合，如]{style="font-family:宋体"}[TE]{lang="EN-US"}]{#struct_0_17931_14437_1275334199}[，则表示两个报文转发动作都有发生]{style="font-family:宋体"}

[[Driver flag]{lang="EN-US"}]{#struct_0_17931_14437_1077151631}

[[下发驱动标记：]{style="font-family:宋体"}]{#struct_0_17931_14437_1907343436}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nores]{lang="EN-US"}]{#struct_0_17931_14437_2122035061}[：表示下发驱动资源不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Done]{lang="EN-US"}]{#struct_0_17931_14437_967739141}[：表示下发驱动成功]{style="font-family:宋体"}

[[Epoch]{lang="EN-US"}]{#struct_0_17931_14437_1853808277}

[[老化时间戳，用于表示表项是否需要老化]{style="font-family:宋体"}]{#struct_0_17931_14437_1715063014}

[[Context]{lang="EN-US"}]{#struct_0_17931_14437_1823844180}

[[保存]{style="font-family:宋体"}[SPBM FDB]{lang="EN-US"}]{#struct_0_17931_14437_967280390}[下刷驱动后返回的驱动信息]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_x1260765349}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_753609342}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1724220490 .myid}
[]{#_Toc404798196}[]{#struct_0_17931_14437_967018246}[]{#_Toc404004441}[]{#_Toc404067877}[]{#_Toc404260077}[]{#_Toc404004442}[]{#_Toc404067878}[]{#_Toc404260078}[]{#_Toc404004443}[]{#_Toc404067879}[]{#_Toc404260079}[]{#_Toc404004444}[]{#_Toc404067880}[]{#_Toc404260080}[]{#_Toc404004445}[]{#_Toc404067881}[]{#_Toc404260081}[]{#_Toc404004446}[]{#_Toc404067882}[]{#_Toc404260082}[]{#_Toc404004447}[]{#_Toc404067883}[]{#_Toc404260083}[]{#_Toc404004448}[]{#_Toc404067884}[]{#_Toc404260084}[]{#_Toc404004449}[]{#_Toc404067885}[]{#_Toc404260085}[]{#_Toc404004450}[]{#_Toc404067886}[]{#_Toc404260086}[]{#_Toc404004451}[]{#_Toc404067887}[]{#_Toc404260087}[]{#_Toc404004452}[]{#_Toc404067888}[]{#_Toc404260088}[]{#_Toc404004453}[]{#_Toc404067889}[]{#_Toc404260089}[]{#_Toc404004454}[]{#_Toc404067890}[]{#_Toc404260090}[]{#_Toc404004455}[]{#_Toc404067891}[]{#_Toc404260091}[]{#_Toc404004456}[]{#_Toc404067892}[]{#_Toc404260092}[]{#_Toc404004457}[]{#_Toc404067893}[]{#_Toc404260093}[]{#_Toc404004458}[]{#_Toc404067894}[]{#_Toc404260094}[]{#_Toc404004459}[]{#_Toc404067895}[]{#_Toc404260095}[]{#_Toc404004460}[]{#_Toc404067896}[]{#_Toc404260096}[]{#_Toc404004461}[]{#_Toc404067897}[]{#_Toc404260097}[]{#_Toc404004462}[]{#_Toc404067898}[]{#_Toc404260098}[]{#_Toc404004463}[]{#_Toc404067899}[]{#_Toc404260099}[]{#_Toc404004464}[]{#_Toc404067900}[]{#_Toc404260100}[]{#_Toc404004465}[]{#_Toc404067901}[]{#_Toc404260101}[]{#_Toc404004466}[]{#_Toc404067902}[]{#_Toc404260102}[]{#_Toc404004467}[]{#_Toc404067903}[]{#_Toc404260103}[]{#_Toc404004468}[]{#_Toc404067904}[]{#_Toc404260104}[]{#_Toc404004469}[]{#_Toc404067905}[]{#_Toc404260105}[]{#_Toc404004476}[]{#_Toc404067912}[]{#_Toc404260112}

**SPBM \-- SPBM配置命令 \-- display spbm unicast-fib statistics**

------------------------------------------------------------------------

[**[display spbm unicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x138986453}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x277022273}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_2140728014}

[**[display spbm unicast-fib]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}]{#struct_0_17931_14437_x959587315}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1196047826}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display spbm unicast-fib]{lang="EN-US"}**[ **statistics** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_x195514214}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x1465583501}[模式：]{style="font-family:宋体"}

[**[display spbm unicast-fib statistics]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_966952710}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x50355827}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x11692513}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1006358318}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1819129695}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x831689867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2128997612}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1141903485}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_707741910}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_966887174}[：显示指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x781654278}[：显示指定成员设备的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定该参数，则显示所有成员设备的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_350910610}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定该参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_554309530}[：显示指定成员设备上指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定该参数，则显示所有成员设备上所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_350451851}[：显示指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定该参数，则显示所有单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_600154639}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[如果未指定该参数，则显示所有]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1401083136}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x843468976}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表项统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-fib statistics]{lang="EN-US"}]{#struct_0_17931_14437_966821638}

[SPBM unicast FIB basic statistics:]{lang="EN-US"}

[RefreshMsg     : 1           DeleteMsg        : 0]{lang="EN-US"}

[AddUMACNumber  : 1           DeleteUMACNumber : 0]{lang="EN-US"}

[DeleteNotFound : 0           AgeNumber        : 0]{lang="EN-US"}

[DrvAdd         : 1           DrvDelete        : 0]{lang="EN-US"}

[DrvDelRefresh  : 0]{lang="EN-US"}

[SPBM unicast FIB error statistics:]{lang="EN-US"}

[UMACMsgError   : 0           RefreshMsgFail   : 0]{lang="EN-US"}

[DeleteMsgFail  : 0           AddUMACFail      : 0]{lang="EN-US"}

[DrvOtherFail   : 0           DrvDeleteFail    : 0]{lang="EN-US"}

[DrvNoResource  : 0           SynMsgFail       : 0]{lang="EN-US"}

[AllocEntryFail : 0           AllocReDrvMsgFail: 0]{lang="EN-US"}

[[表1-27 ]{lang="EN-US"}[display spbm unicast-fib statistics]{lang="EN-US"}]{#struct_0_17931_14437_729558335}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1858972171}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1378885448}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x1890793009}

[[SPBM unicast FIB basic statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1827678419}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_967804678}[单播转发表基础统计信息]{style="font-family:宋体"}

[[RefreshMsg]{lang="EN-US"}]{#struct_0_17931_14437_1275334200}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x496367722}[地址刷新消息]{style="font-family:宋体"}

[[DeleteMsg]{lang="EN-US"}]{#struct_0_17931_14437_1459657313}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1777994607}[地址删除消息]{style="font-family:宋体"}

[[AddUMACNumber]{lang="EN-US"}]{#struct_0_17931_14437_967739142}

[[创建单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1853808276}[地址计数]{style="font-family:宋体"}

[[DeleteUMACNumber]{lang="EN-US"}]{#struct_0_17931_14437_1715128550}

[[删除单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_218016224}[地址计数]{style="font-family:宋体"}

[[DeleteNotFound]{lang="EN-US"}]{#struct_0_17931_14437_246382934}

[[删除时查找不到合适的单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1405372602}[地址计数]{style="font-family:宋体"}

[[AgeNumber]{lang="EN-US"}]{#struct_0_17931_14437_x1145330703}

[[当前启动老化状态时老化表项的个数]{style="font-family:宋体"}]{#struct_0_17931_14437_x426682352}

[[DrvAdd]{lang="EN-US"}]{#struct_0_17931_14437_x744822061}

[[驱动表项添加]{style="font-family:宋体"}]{#struct_0_17931_14437_x1405438138}

[[DrvDelete]{lang="EN-US"}]{#struct_0_17931_14437_1862612430}

[[驱动表项删除]{style="font-family:宋体"}]{#struct_0_17931_14437_x224707395}

[[DrvDelRefresh]{lang="EN-US"}]{#struct_0_17931_14437_x1207333655}

[[驱动表项]{style="font-family:宋体"}[Modify]{lang="EN-US"}]{#struct_0_17931_14437_x1405503674}[时删除]{style="font-family:宋体"}

[[UMACMsgError]{lang="EN-US"}]{#struct_0_17931_14437_609717838}

[[无效的单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1808897527}[地址消息]{style="font-family:宋体"}

[[SPBM unicast FIB error statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1749253963}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1405569210}[单播转发表错误统计信息]{style="font-family:宋体"}

[[RefreshMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x65434628}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_730936989}[地址刷新消息处理失败]{style="font-family:宋体"}

[[DeleteMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_1608131455}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1405634746}[地址删除消息处理失败]{style="font-family:宋体"}

[[AddUMACFail]{lang="EN-US"}]{#struct_0_17931_14437_881366602}

[[创建单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x836237404}[地址表项失败]{style="font-family:宋体"}

[[DrvOtherFail]{lang="EN-US"}]{#struct_0_17931_14437_x1405700282}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x681925356}[地址下发驱动添加或更新]{style="font-family:宋体"}

[[DrvDeleteFail]{lang="EN-US"}]{#struct_0_17931_14437_1171688528}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1304399851}[地址下发驱动删除]{style="font-family:宋体"}

[[DrvNoResource]{lang="EN-US"}]{#struct_0_17931_14437_x1405765818}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x240439074}[地址下发驱动资源不足]{style="font-family:宋体"}

[[SynMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_1834298054}

[[信息同步失败]{style="font-family:宋体"}]{#struct_0_17931_14437_x1405831354}

[[AllocEntryFail]{lang="EN-US"}]{#struct_0_17931_14437_x963793648}

[[单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x57114828}[地址表项内存申请失败]{style="font-family:宋体"}

[[AllocReDrvMsgFail]{lang="EN-US"}]{#struct_0_17931_14437_x1404848314}

[[重刷单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_1753336232}[地址表项内存申请失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-861822883 .myid}
[]{#_Toc404798197}[]{#struct_0_17931_14437_1021340046}[]{#_Toc332722572}

**SPBM \-- SPBM配置命令 \-- display spbm unicast-pw**

------------------------------------------------------------------------

[**[display spbm unicast-pw]{lang="EN-US"}**]{#struct_0_17931_14437_x52808705}[命令用来显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[（]{style="font-family:宋体"}[BEB]{lang="EN-US"}[间建立的单播隧道）信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1624017877}

[**[display spbm unicast-pw ]{lang="EN-US"}**[\[ **i-sid** *i-sid* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_17931_14437_x686047413}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1404913850}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_984541890}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1493435858}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2140583413}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_x535837988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_2129233229}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_1124304108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405372601}

[**[i-sid ]{lang="EN-US"}***[i-sid]{lang="EN-US"}*]{#struct_0_17931_14437_420753238}[：显示指定]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[255]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。如果未指定该参数，则显示所有]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[的单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_17931_14437_1313678796}[：显示单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[计数。如果未指定该参数，则显示单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x143939134}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_476588837}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[所有单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-pw]{lang="EN-US"}]{#struct_0_17931_14437_1285724293}

[System ID            I-SID      B-MAC          B-VLAN Port]{lang="EN-US"}

[000f.e201.0101       300        000f-e201-0101 100    GE1/0/1]{lang="EN-US"}

[000f.e201.0102       300        000f-e201-0102 100    GE1/0/2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1064964551}[显示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[所有单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[计数。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-pw count]{lang="EN-US"}]{#struct_0_17931_14437_264054038}

[Total entries: 2]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[display spbm unicast-pw]{lang="EN-US"}]{#struct_0_17931_14437_1602701686}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1851319531}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405438137}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_x153810205}

[[System ID]{lang="EN-US"}]{#struct_0_17931_14437_647361293}

[[系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17931_14437_x2028339311}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1997589896}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_x1405503673}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_1013002365}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17931_14437_x2073289739}[地址]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x726916497}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_x1066854259}[对应接口所属的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}

[[Port]{lang="EN-US"}]{#struct_0_17931_14437_x1405569209}

[[B-MAC]{lang="EN-US"}]{#struct_0_17931_14437_1856945209}[对应的接口]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_17931_14437_x501119390}

[[单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_17931_14437_865733192}[计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#268291876 .myid}
[]{#_Toc404798198}[]{#struct_0_17931_14437_x1932373009}[]{#_Toc404067915}[]{#_Toc404260115}[]{#_Toc404067916}[]{#_Toc404260116}[]{#_Toc404067917}[]{#_Toc404260117}[]{#_Toc404067918}[]{#_Toc404260118}[]{#_Toc404067925}[]{#_Toc404260125}

**SPBM \-- SPBM配置命令 \-- display spbm unicast-tree**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **spbm unicast-tree**]{lang="EN-US"}]{#struct_0_17931_14437_1332538620}[用来显示单播树信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_354662734}

[**[display spbm unicast-tree]{lang="EN-US"}**]{#struct_0_17931_14437_x1405700281}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x278640829}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1603599681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_633286104}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1958708223}

[[network-operator]{lang="EN-US"}]{#struct_0_17931_14437_1854785930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1291967916}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17931_14437_x1484796894}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405765817}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_2132213921}[显示]{style="font-family:宋体"}[B-VLAN 100]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[单播树信息。]{style="font-family:宋体"}

[[\<Sysname\> display spbm unicast-tree]{lang="EN-US"}]{#struct_0_17931_14437_x229016335}

[                         SPF tree information for SPBM]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Flags: S-Node is on SPF tree       D-Node or Link is to be deleted]{lang="EN-US"}

[           O-Node is overload          I-Node is invalid]{lang="EN-US"}

[           T-Node is on tent list      P-Neighbor is parent node]{lang="EN-US"}

[           C-Neighbor is child node    L-Link is on changelist]{lang="EN-US"}

[           V-Link is involved          N-Link is a new path]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node: 0011.2200.0001]{lang="EN-US"}

[  LinkCount: 0x1    NodeFlags: T S]{lang="EN-US"}

[SPF link: \--\>0011.2200.0101]{lang="EN-US"}

[  Cost: 0xb      NewCost: 0xb      LinkFlags: P]{lang="EN-US"}

[ ]{lang="EN-US"}

[SPF node: 0011.2200.0101]{lang="EN-US"}

[  LinkCount: 0x1    NodeFlags: S]{lang="EN-US"}

[SPF link: \--\>0011.2200.0001]{lang="EN-US"}

[  Cost: 0xa      NewCost: 0xb      LinkFlags: C]{lang="EN-US"}

[[表1-29 ]{lang="EN-US"}[display spbm unicast-tree]{lang="EN-US"}]{#struct_0_17931_14437_x1405831353}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1846685163}[[字段]{style="font-family:黑体"}]{#struct_0_17931_14437_602290293}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17931_14437_1408958517}

[]{#_Hlk352575538}[[Flags]{lang="EN-US"}]{#struct_0_17931_14437_x1787705444}

[]{#OLE_LINK23}[]{#OLE_LINK22}[]{#OLE_LINK21}[[节点或链路标志：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1117912829}

[]{#OLE_LINK20}[]{#OLE_LINK19}[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_17931_14437_x1404848313}[：表示节点在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_17931_14437_x1782116177}[：表示节点或链路待删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_17931_14437_x1255774707}[：表示节点置位]{lang="EN-US" style="font-family:宋体"}[OVERLOAD]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_17931_14437_x1555361712}[：表示节点无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_17931_14437_x1404913849}[：表示节点是候选节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_17931_14437_x937706875}[：表示节点是]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上指定链路的父节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_17931_14437_x1578894977}[：表示节点是是]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上指定链路的子节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_17931_14437_x1924767026}[：表示链路在链路变化链上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_17931_14437_x1405372604}[：表示链路置位]{lang="EN-US" style="font-family:宋体"}[INVOLVED]{lang="EN-US"}[标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_17931_14437_x338761649}[：表示链路是新增的]{style="font-family:宋体"}

[[SPF node]{lang="EN-US"}]{#struct_0_17931_14437_1948020247}

[[SPF]{lang="EN-US"}]{#struct_0_17931_14437_198919130}[节点信息]{style="font-family:宋体"}

[[LinkCount]{lang="EN-US"}]{#struct_0_17931_14437_x1405438140}

[[以每个]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_17931_14437_x2076321114}[节点为源的链路数]{style="font-family:宋体"}

[[NodeFlags]{lang="EN-US"}]{#struct_0_17931_14437_1350775053}

[]{#struct_0_17931_14437_x920134226}[]{#OLE_LINK34}[[SPF]{lang="EN-US"}]{#OLE_LINK33}[节点标志]{style="font-family:宋体"}

[[SPF link]{lang="EN-US"}]{#struct_0_17931_14437_x1405503676}

[[SPF]{lang="EN-US"}]{#struct_0_17931_14437_1772517252}[链路信息]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_17931_14437_676690789}

[[该链路源节点发布的度量值]{style="font-family:宋体"}]{#struct_0_17931_14437_x837261533}

[[NewCost]{lang="EN-US"}]{#struct_0_17931_14437_x1405569212}

[[该链路源节点和目的节点协商后的度量值]{style="font-family:宋体"}]{#struct_0_17931_14437_x1228234042}

[[LinkFlags]{lang="EN-US"}]{#struct_0_17931_14437_942211912}

[[链路标志]{style="font-family:宋体"}]{#struct_0_17931_14437_282356538}

[ ]{lang="EN-US"}

::: {#-1741618431 .myid}
[]{#_Toc404798199}[]{#struct_0_17931_14437_x1405634748}

**SPBM \-- SPBM配置命令 \-- ect**

------------------------------------------------------------------------

[**[ect]{lang="EN-US"}**]{#struct_0_17931_14437_1331705296}[命令用来配置]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法之间的映射关系。]{style="font-family:宋体"}

[**[undo ect]{lang="EN-US"}**]{#struct_0_17931_14437_530894252}[命令用来取消]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法之间的映射关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_920135847}

[**[ect ]{lang="EN-US"}***[ect-index]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_17931_14437_x322246932}**[b-]{lang="EN-US"}[vlan]{lang="EN-US"}**[ *vlan-id-list*]{lang="EN-US"}

[**[undo ect ]{lang="EN-US"}***[ect-index]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_17931_14437_x1257236611}**[b-]{lang="EN-US"}[vlan]{lang="EN-US"}**[ \[ *vlan-id-list* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1115679771}

[[所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1706740455}[都映射到]{style="font-family:宋体"}[ECT 1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405700284}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_480874058}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1375072444}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x534157625}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1304593472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1946660519}

[*[ect-index]{lang="EN-US"}*]{#struct_0_17931_14437_x1216461933}[：]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_17931_14437_2131038775}[：]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405765820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_17931_14437_x596734970}[SPBN]{lang="EN-US"}[内通过不同]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法决策出不同的]{style="font-family:宋体"}[SPT]{lang="EN-US"}[，每个]{style="font-family:宋体"}[SPT]{lang="EN-US"}[对应一个转发路径，不同的]{style="font-family:宋体"}[SPT]{lang="EN-US"}[间形成流量的负载分担。]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法与]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[之间有映射关系，一组]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[可以映射到同一]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法，后续该组]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的流量都在该]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法决策的]{style="font-family:宋体"}[SPT]{lang="EN-US"}[内进行转发。通过调整]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法的映射关系可以达到调整网络负载分担的目的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居间]{style="font-family:宋体"}]{#struct_0_17931_14437_x1836255052}[B-VLAN]{lang="EN-US"}[和]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法的映射关系不一致时，邻居间的链路不能承载流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_17931_14437_1064571335}**[undo ect]{lang="EN-US"}**[命令时，若指定的]{style="font-family:宋体"}[ECT]{lang="EN-US"}[算法索引值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，则该配置无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_387031566}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1137997329}[配置]{style="font-family:宋体"}[B-VLAN 100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[映射到]{style="font-family:宋体"}[ECT 2]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1331499906}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] ect 2 b-vlan 100 to 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1107797931}[取消所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[ECT 2]{lang="EN-US"}[的映射关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1405831356}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] undo ect 2 b-vlan]{lang="EN-US"}
:::

::: {#1202717567 .myid}
[]{#_Toc404798200}[]{#struct_0_17931_14437_199005766}[]{#_Toc320886182}[]{#_Toc303839440}[]{#_Toc252200750}[]{#_Toc163546253}[]{#_Toc131667486}

**SPBM \-- SPBM配置命令 \-- flash-flood**

------------------------------------------------------------------------

[**[flash-flood]{lang="EN-US"}**]{#struct_0_17931_14437_877645134}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能。]{style="font-family:宋体"}

[**[undo flash-flood]{lang="EN-US"}**]{#struct_0_17931_14437_55040396}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1254806244}

[**[flash-flood]{lang="EN-US"}**[ \[ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* \] \*]{lang="EN-US"}]{#struct_0_17931_14437_x572591022}

[**[undo flash-flood]{lang="EN-US"}**]{#struct_0_17931_14437_1228705222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_451990960}

[[未配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x1404848316}[快速扩散功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1378831650}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1075665340}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1141468526}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_167146048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x487508854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_188522488}

[**[flood-count]{lang="EN-US"}***[ flooding-count]{lang="EN-US"}*]{#struct_0_17931_14437_323897880}[：在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算前快速扩散的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[max-timer-interval]{lang="EN-US"}***[ flooding-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x1404913852}[：在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散之前的等待时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x178257524}

[[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x873576222}[快速扩散功能后，当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发生变化而导致]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算时，在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算前，将把导致]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散出去，扩散后，整网重新计算]{style="font-family:宋体"}[SPF]{lang="EN-US"}[。从而大大缩短设备之间由于进行]{style="font-family:宋体"}[LSP]{lang="EN-US"}[同步而导致]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[不一致的时间，提高全网的快速收敛性能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_265207296}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x308072621}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能，在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算前快速扩散的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[，在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散之前的等待时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1808464054}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] flash-flood flood-count 10 max-timer-interval 100]{lang="EN-US"}
:::

::::: {#63544256 .myid}
[]{#_Toc404798201}[]{#struct_0_17931_14437_202529609}

**SPBM \-- SPBM配置命令 \-- graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1138014405}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_1745256300}
:::

[ ]{lang="EN-US"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_17931_14437_x1405372603}[命令用来使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_17931_14437_1583552652}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1787268499}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_17931_14437_1817498324}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_17931_14437_499951995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1890396765}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1891123716}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405438139}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_296528489}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1029511550}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_981182421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_449771040}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x446020593}

[[SPBM GR]{lang="EN-US"}]{#struct_0_17931_14437_x1389893834}[功能与]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[功能互斥，即]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[和]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1744839144}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1405503675}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x2119165517}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] graceful-restart]{lang="EN-US"}
:::::

::::: {#1056335496 .myid}
[]{#_Toc404798202}[]{#struct_0_17931_14437_x2117933117}

**SPBM \-- SPBM配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1138407621}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_x1138211013}
:::

[ ]{lang="EN-US"}

[**[graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_17931_14437_1423649468}[命令用来配置]{style="font-family:
宋体"}[GR]{lang="EN-US"}[时]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[**[undo graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_17931_14437_x498512629}[命令用来配置]{style="font-family:宋体"}[GR]{lang="EN-US"}[时]{style="font-family:宋体"}[SA]{lang="EN-US"}[不置位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_2116369614}

[**[graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_17931_14437_122366013}

[**[undo graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_17931_14437_x1405569211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1500649313}

[[GR]{lang="EN-US"}]{#struct_0_17931_14437_x285655781}[时]{style="font-family:宋体"}[SA]{lang="EN-US"}[位处于置位状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1552118725}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_2091884120}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x228581998}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1578928675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_602834834}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x108878451}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_226989753}[配置]{style="font-family:宋体"}[GR]{lang="EN-US"}[时]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x549030269}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] graceful-restart suppress-sa]{lang="EN-US"}
:::::

::::: {#2003638588 .myid}
[]{#_Toc404798203}[]{#struct_0_17931_14437_960827495}

**SPBM \-- SPBM配置命令 \-- graceful-restart t2**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1137555653}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_492591771}
:::

[ ]{lang="EN-US"}

[**[graceful-restart t2]{lang="EN-US"}**]{#struct_0_17931_14437_x1405700283}[命令用来配置]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器值。]{style="font-family:宋体"}

[**[undo graceful-restart t2]{lang="EN-US"}**]{#struct_0_17931_14437_884158585}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x936247484}

[**[graceful-restart t2]{lang="EN-US"}**[ *t2-value*]{lang="EN-US"}]{#struct_0_17931_14437_x1568635880}

[**[undo graceful-restart t2]{lang="EN-US"}**]{#struct_0_17931_14437_19875984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_2082063066}

[[SPBM GR]{lang="EN-US"}]{#struct_0_17931_14437_x465439140}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器值为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x330698485}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1405765819}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1325644867}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_587882796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_2139777440}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_2079763118}

[*[t2-value]{lang="EN-US"}*]{#struct_0_17931_14437_x1820222207}[：指定]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器值，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_983335166}

[[T2]{lang="EN-US"}]{#struct_0_17931_14437_x1404848315}[定时器用来控制设备的]{style="font-family:宋体"}[GR]{lang="EN-US"}[时间间隔。]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器值在]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello PDU]{lang="EN-US"}[中为保持时间，这样在该设备]{style="font-family:宋体"}[GR]{lang="EN-US"}[的时间内邻居不会断掉与其的邻接关系。如果]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器超时后，]{style="font-family:宋体"}[GR]{lang="EN-US"}[还没有完成，则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x975547123}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x68990619}[配置]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1707987317}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] graceful-restart t2 120]{lang="EN-US"}
:::::

::: {#-1398635010 .myid}
[]{#_Toc404798204}[]{#struct_0_17931_14437_860823299}[]{#_Toc326076018}[]{#_Toc310604351}[]{#_Toc53487862}

**SPBM \-- SPBM配置命令 \-- is-name**

------------------------------------------------------------------------

[**[is-name]{lang="EN-US"}**]{#struct_0_17931_14437_x1404913851}[命令用来使能动态主机名映射功能并为当前设备配置主机名称。]{style="font-family:宋体"}

[**[undo is-name]{lang="EN-US"}**]{#struct_0_17931_14437_x581542051}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1143430039}

[**[is-name]{lang="EN-US"}**[ *is-name*]{lang="EN-US"}]{#struct_0_17931_14437_x270711981}

[**[undo is-name]{lang="EN-US"}**]{#struct_0_17931_14437_2142211599}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1051153481}

[[动态主机名映射功能处于关闭状态且没有为当前设备配置主机名称。]{style="font-family:宋体"}]{#struct_0_17931_14437_x2076644173}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405372606}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_824037765}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1130305212}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x875573704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1035962629}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1852497577}

[*[is-name]{lang="EN-US"}*]{#struct_0_17931_14437_632353869}[：为当前设备配置的主机名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_903665544}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1275063158}[使能动态主机名映射功能，并为当前设备配置主机名称为]{style="font-family:宋体"}[spbm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_1474800037}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] is-name spbm]{lang="EN-US"}
:::

::: {#2070950537 .myid}
[]{#_Toc404798205}[]{#struct_0_17931_14437_x602395192}

**SPBM \-- SPBM配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_17931_14437_x1920059362}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_17931_14437_x602329656}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_2000816782}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_17931_14437_1807089567}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_17931_14437_1536507235}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1569699495}

[[L2VPN]{lang="EN-US"}]{#struct_0_17931_14437_1883841365}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x737940725}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x2068454663}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x602264120}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x323632343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1697322284}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2039936924}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_413461338}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_1186887025}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::: {#-1110888516 .myid}
[]{#_Toc404798206}[]{#struct_0_17931_14437_161166336}[]{#_Toc320886213}

**SPBM \-- SPBM配置命令 \-- log-peer-change**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_17931_14437_x1405503678}[命令用来配置邻接状态变化时生成日志信息。]{style="font-family:宋体"}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_17931_14437_x2072111350}[命令用来配置邻接状态变化时不生成日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1803698500}

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_17931_14437_x192296832}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_17931_14437_x1314320714}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1116903499}

[[邻接状态变化时生成日志信息。]{style="font-family:宋体"}]{#struct_0_17931_14437_x1775393226}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_153501057}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1405569214}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2034803096}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x742673059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_67935481}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x989780803}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1731478797}[配置邻接状态变化时不生成日志信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1405634750}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] undo log-peer-change   ]{lang="EN-US"}
:::

::: {#227164563 .myid}
[]{#_Toc404798207}[]{#struct_0_17931_14437_1688001192}

**SPBM \-- SPBM配置命令 \-- multicast replicate-mode**

------------------------------------------------------------------------

[**[multicast ]{lang="EN-US"}[replicate-mode]{lang="EN-US"}**]{#struct_0_17931_14437_x540283899}[命令用来配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播转发模式。]{style="font-family:宋体"}

[**[undo multicast ]{lang="EN-US"}[replicate-mode]{lang="EN-US"}**]{#struct_0_17931_14437_x1592681463}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2102245039}

[**[multicast replicate-mode]{lang="EN-US"}**[ { **head-end** \| **tandem** }]{lang="EN-US"}]{#struct_0_17931_14437_1980929595}

[**[undo multicast replicate-mode]{lang="EN-US"}**]{#struct_0_17931_14437_1950238231}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405700286}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1643673472}[组播转发模式采用头端复制模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1855311603}

[[VSI SPB]{lang="EN-US"}]{#struct_0_17931_14437_433565849}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1727486545}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1405765822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1759534384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_677684382}

[**[head-end]{lang="EN-US"}**]{#struct_0_17931_14437_1264618786}[：头端复制模式。]{style="font-family:宋体"}

[**[tandem]{lang="EN-US"}**]{#struct_0_17931_14437_1363259066}[：核心复制模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1797452528}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1582011063}[配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[组播转发模式采用核心复制模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1460054184}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] spb i-sid 256]{lang="EN-US"}

[\[Sysname-vsi-vpn1-256\] multicast replicate-mode ]{lang="EN-US"}[tandem]{lang="EN-US"}
:::

::::: {#-1306605503 .myid}
[]{#_Toc404798208}[]{#struct_0_17931_14437_2046389272}

**SPBM \-- SPBM配置命令 \-- multicast-bvlan enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1151709150}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_x1404848318}
:::

**[ ]{lang="EN-US"}**

[**[multicast-bvlan enable]{lang="EN-US"}**]{#struct_0_17931_14437_140198124}[命令用来使能组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo multicast-bvlan enable]{lang="EN-US"}**]{#struct_0_17931_14437_x1251109022}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_283773591}

[**[multicast-bvlan enable]{lang="EN-US"}**]{#struct_0_17931_14437_991150451}

[**[undo multicast-bvlan enable]{lang="EN-US"}**]{#struct_0_17931_14437_1053619479}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x364817147}

[[组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x1250209279}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1404913854}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x984826578}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1488965983}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1203491113}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1499077139}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_17552561}

[[支持组播核心复制模式的设备，缺省会使用同一]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x440772172}[来承载单播流量和组播流量。由于芯片限制会出现组播报文无法复制的问题，此时通过组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能可以解决该问题。]{style="font-family:宋体"}

[[组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}]{#struct_0_17931_14437_x217569222}[功能使用奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[（]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值为奇数）来承载单播流量，使用偶数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[（]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值为偶数）来承载组播流量。]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文中仅携带奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，链路计算时会使用奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[来生成对应的单播转发表项，同时使用对应的偶数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[（奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[值＋]{style="font-family:宋体"}[1]{lang="EN-US"}[）来生成对应的组播转发表项。后续用户侧报文入]{style="font-family:宋体"}[SPBN]{lang="EN-US"}[时，会在奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[内进行单播发送，在偶数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[内进行组播发送。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1405372605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_17931_14437_760197733}[SPBN]{lang="EN-US"}[中，只要有一台设备需使能组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能，则其他所有]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[设备也必须使能组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使能组播双]{style="font-family:宋体"}]{#struct_0_17931_14437_x52963742}[B-VLAN]{lang="EN-US"}[模式与关闭组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[模式间进行切换时，会引起临时断流，所有对应]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[表项都会删除重建。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户需要保证配置组播双]{style="font-family:宋体"}]{#struct_0_17931_14437_1662815484}[B-VLAN]{lang="EN-US"}[时对应的奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[和偶数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[都与实例]{style="font-family:宋体"}[4092]{lang="EN-US"}[映射，且在这些]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[流量经过的端口上都允许对应]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[通过。若仅配置奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[或偶数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，则]{style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文无法携带该奇数]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能组播]{style="font-family:宋体"}]{#struct_0_17931_14437_x1560307246}[双]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能后，]{lang="EN-US" style="font-family:宋体"}[SPB IS-IS]{lang="EN-US"}[协议报文只携带奇数]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，故对于]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[之间的映射关系，要求]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[必须与奇数]{lang="EN-US" style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[建立映射关系。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1757702426}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x784385161}[使能组播双]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_726895529}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] multicast-bvlan enable]{lang="EN-US"}
:::::

::::: {#-1554088180 .myid}
[]{#_Toc404798209}[]{#struct_0_17931_14437_x1792981758}[]{#_Toc374027640}

**SPBM \-- SPBM配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1779615833}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_49530094}
:::

[ ]{lang="EN-US"}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_x755940114}[命令用来使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_x1471614228}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_326023672}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_x1146747220}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_17931_14437_x783431846}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x683165304}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1792916222}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1303115717}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_437232658}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_586734479}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x475196080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_119717270}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_32206680}

[[SPBM NSR]{lang="EN-US"}]{#struct_0_17931_14437_x878458693}[功能与]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[功能互斥，即]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[和]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1792850686}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x159427145}[使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x2087337392}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] non-stop-routing]{lang="EN-US"}
:::::

::: {#1032656458 .myid}
[]{#_Toc404798210}[]{#struct_0_17931_14437_x1358226742}[]{#_Toc374018989}[]{#_Toc374019074}[]{#_Toc374019243}[]{#_Toc375136377}[]{#_Toc374018990}[]{#_Toc374019075}[]{#_Toc374019244}[]{#_Toc375136378}[]{#_Toc374018991}[]{#_Toc374019076}[]{#_Toc374019245}[]{#_Toc375136379}[]{#_Toc374018992}[]{#_Toc374019077}[]{#_Toc374019246}[]{#_Toc375136380}[]{#_Toc374018993}[]{#_Toc374019078}[]{#_Toc374019247}[]{#_Toc375136381}[]{#_Toc374018994}[]{#_Toc374019079}[]{#_Toc374019248}[]{#_Toc375136382}[]{#_Toc374018995}[]{#_Toc374019080}[]{#_Toc374019249}[]{#_Toc375136383}[]{#_Toc374018996}[]{#_Toc374019081}[]{#_Toc374019250}[]{#_Toc375136384}[]{#_Toc374018997}[]{#_Toc374019082}[]{#_Toc374019251}[]{#_Toc375136385}[]{#_Toc374018998}[]{#_Toc374019083}[]{#_Toc374019252}[]{#_Toc375136386}[]{#_Toc374018999}[]{#_Toc374019084}[]{#_Toc374019253}[]{#_Toc375136387}[]{#_Toc374019000}[]{#_Toc374019085}[]{#_Toc374019254}[]{#_Toc375136388}[]{#_Toc374019001}[]{#_Toc374019086}[]{#_Toc374019255}[]{#_Toc375136389}[]{#_Toc374019002}[]{#_Toc374019087}[]{#_Toc374019256}[]{#_Toc375136390}

**SPBM \-- SPBM配置命令 \-- reset spbm bvlan-info statistics**

------------------------------------------------------------------------

[**[reset spbm bvlan-info statistics]{lang="EN-US"}**]{#struct_0_17931_14437_53825984}[用来清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1405569213}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_337849899}

[**[reset spbm bvlan-info statistics]{lang="EN-US"}**]{#struct_0_17931_14437_154634280}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_806312642}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset spbm bvlan-info statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_x389994216}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x2062280772}[模式：]{style="font-family:宋体"}

[**[reset spbm bvlan-info statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_867658023}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_648564301}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1405634749}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x234378645}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1601537806}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2119597801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x606629475}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x611513575}[：清除指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1587972943}[：清除指定成员设备的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x52767134}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1405700285}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x52308382}[：清除指定单板的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_1648045431}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_2046957999}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x268112132}[清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm bvlan-info statistics]{lang="EN-US"}]{#struct_0_17931_14437_x929429002}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1138145475}[清除单板]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm bvlan-info statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x163508575}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1137948867}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm bvlan-info statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_129246486}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1394589861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ spbm bvlan-info statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x1294982017}
:::

::: {#1445807212 .myid}
[]{#_Toc404798211}[]{#struct_0_17931_14437_431363296}

**SPBM \-- SPBM配置命令 \-- reset spbm database**

------------------------------------------------------------------------

[**[reset spbm database]{lang="EN-US"}**]{#struct_0_17931_14437_712312752}[用来清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_17931_14437_7513506}

[**[reset spbm database]{lang="EN-US"}**[ \[ **graceful-restart** \]]{lang="EN-US"}]{#struct_0_17931_14437_1319362005}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1433279506}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1593263514}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1583678690}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1997447237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1064514363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1354621977}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_17931_14437_x1547325395}[：清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的数据库信息之后，可以通过]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式来恢复数据。如果未指定本参数，则在清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的数据库信息后，只能以非]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式来恢复数据。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x890111023}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1085845765}[清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> reset spbm database]{lang="EN-US"}]{#struct_0_17931_14437_x1407730313}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_2093808381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ spbm ]{lang="EN-US"}**]{#struct_0_17931_14437_1287235156}**[lsdb]{lang="EN-US"}**
:::

::::: {#-630369038 .myid}
[]{#_Toc404798212}[]{#struct_0_17931_14437_x1793243901}[]{#_Toc374027643}

**SPBM \-- SPBM配置命令 \-- reset spbm graceful-restart event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1361108577}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_x27758336}
:::

[ ]{lang="EN-US"}

[**[reset spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_1343583997}[命令用来清除]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1565380257}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x209693711}

[**[reset spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_323058952}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1793178365}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset spbm graceful-restart event-log]{lang="EN-US"}**[ **slot**]{lang="EN-US"}[ *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_158133258}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x1969582506}[模式：]{style="font-family:宋体"}

[**[reset spbm graceful-restart event-log]{lang="EN-US"}**[ **chassis**]{lang="EN-US"}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1102733479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_723510676}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x704572866}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_937560082}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x653897109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_833733327}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1793112829}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_551278665}*[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_1291050496}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x53029277}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_x1116710748}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_x1982215391}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1156158706}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x910998541}[清除单板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm graceful-restart event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x1301317674}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_306184628}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM GR]{lang="EN-US"}[日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm graceful-restart event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x1793047293}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_332466894}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display spbm graceful-restart event-log]{lang="EN-US"}**]{#struct_0_17931_14437_521982076}
:::::

::: {#239491984 .myid}
[]{#_Toc404798213}[]{#struct_0_17931_14437_437918411}

**SPBM \-- SPBM配置命令 \-- reset spbm multicast-fib statistics**

------------------------------------------------------------------------

[**[reset spbm multicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_1710944782}[用来清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x665725327}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_x1694013333}

[**[reset spbm multicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x1405765821}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_969348971}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset spbm multicast-fib statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_x1125557154}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_522434605}[模式：]{style="font-family:宋体"}

[**[reset spbm multicast-fib statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_x1609549362}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_928252367}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x976215977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1408917415}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1405831357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1367078175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1399399519}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_210238320}[：清除指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_1440522795}[：清除指定成员设备的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x52701597}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1371383290}[：清除指定成员设备上指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x147021151}[：清除指定单板的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_485311553}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1794581490}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1404848317}[清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm multicast-fib statistics]{lang="EN-US"}]{#struct_0_17931_14437_187252291}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1138211011}[清除单板]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm multicast-fib statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_449728988}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1256576399}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的组播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm multicast-fib statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x1138276547}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x231724911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ spbm multicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_x776925109}
:::

::::: {#-510907186 .myid}
[]{#_Toc404798214}[]{#struct_0_17931_14437_x1792850685}[]{#_Toc374027646}

**SPBM \-- SPBM配置命令 \-- reset spbm non-stop-routing event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SPBM命令.files/image002.png){#图片 36 width="62" height="25"}]{lang="EN-US"}]{#struct_0_17931_14437_x1725511086}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17931_14437_1771952940}
:::

[ ]{lang="EN-US"}

[**[reset spbm non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_17931_14437_1634409753}[命令用来清除]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_931939536}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_209223967}

[**[reset spbm non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_17931_14437_107754098}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1792785149}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset spbm non-stop-routing event-log]{lang="EN-US"}**[ **slot**]{lang="EN-US"}[ *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_1497345096}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x74860902}[模式：]{style="font-family:宋体"}

[**[reset spbm non-stop-routing event-log]{lang="EN-US"}**[ **chassis**]{lang="EN-US"}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x1559680256}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1580735686}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_1123597855}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_27508383}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2084420035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1754764424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1792719613}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x929262692}*[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x1875383837}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_17931_14437_x52832676}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_x1965225248}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_17931_14437_108402650}*[chassis-number]{lang="EN-US"}***[ slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_799860098}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_281034233}[清除单板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm non-stop-routing event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_2041974476}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_863200153}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SPBM NSR]{lang="EN-US"}[日志信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm non-stop-routing event-log slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x1792654077}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1955127586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display spbm non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_17931_14437_x1692994387}
:::::

::: {#-1022995187 .myid}
[]{#_Toc404798215}[]{#struct_0_17931_14437_x1649271397}

**SPBM \-- SPBM配置命令 \-- reset spbm unicast-fib statistics**

------------------------------------------------------------------------

[**[reset spbm unicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_2130703399}[用来清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_656178445}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17931_14437_436799400}

[**[reset spbm unicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_2145390572}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x1597819217}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset spbm unicast-fib statistics]{lang="EN-US"}**[ **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_x1404913853}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17931_14437_x1744341465}[模式：]{style="font-family:宋体"}

[**[reset spbm unicast-fib statistics]{lang="EN-US"}**[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_17931_14437_x1947798425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1579839579}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x293332334}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_340016273}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x800902634}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_160711339}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x542200026}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x1337978711}[：清除指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_914378810}[：清除指定成员设备的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ ]{lang="EN-US"}[slot-number]{lang="EN-US"}*]{#struct_0_17931_14437_x53029284}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_2024015445}[：清除指定成员设备上指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_17931_14437_x408237278}[：清除指定单板的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_17931_14437_x321978397}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_873515410}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_774528086}[清除]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm unicast-fib statistics]{lang="EN-US"}]{#struct_0_17931_14437_x1943721453}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1138079940}[清除单板]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm unicast-fib statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x331688332}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x709589078}[清除成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[上]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的单播]{style="font-family:宋体"}[FIB]{lang="EN-US"}[表统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset spbm unicast-fib statistics slot 1]{lang="EN-US"}]{#struct_0_17931_14437_x191100230}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_931074503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display spbm unicast-fib statistics]{lang="EN-US"}**]{#struct_0_17931_14437_8224928}
:::

::: {#116059579 .myid}
[]{#_Toc404798216}[]{#struct_0_17931_14437_160645803}[]{#_Toc320886223}[]{#_Toc310604371}[]{#_Toc290886815}[]{#_Toc252200791}[]{#_Toc163546306}[]{#_Toc50204117}

**SPBM \-- SPBM配置命令 \-- set-overload**

------------------------------------------------------------------------

[**[set-overload]{lang="EN-US"}**]{#struct_0_17931_14437_193579072}[命令用来配置]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[过载标志位。]{style="font-family:宋体"}

[**[undo set-overload]{lang="EN-US"}**]{#struct_0_17931_14437_908072124}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_52890040}

[**[set-overload]{lang="EN-US"}**[ \[ **on-startup** \[ \[ **start-from-nbr**]{lang="EN-US"}[ *system-id* \[ *timeout1* \[ *nbr-timeout* \] \] \] \| *timeout2* \]]{lang="EN-US"}]{#struct_0_17931_14437_1818048925}

[**[undo set-overload]{lang="EN-US"}**]{#struct_0_17931_14437_x1717196289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x369302881}

[[未配置]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_17931_14437_x1162278367}[过载标志位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_160580267}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_326973874}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1871357593}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1154909142}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1251134830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x193306614}

[**[on-startup]{lang="EN-US"}**]{#struct_0_17931_14437_1405161211}[：系统启动时将过载标志位置位。]{style="font-family:宋体"}

[**[start-from-nbr]{lang="EN-US"}**[ *system-id* \[ *timeout1* \[ *nbr-timeout* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_160514731}[：从系统启动时开始计算，如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内仍未与指定邻居建立邻接关系，过载标志位将结束置位状态；如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内与指定邻居建立了邻接关系，过载标志位将继续保持置位状态，]{style="font-family:宋体"}[且从与指定邻居建立邻接关系时重新计时，在]{style="font-family:宋体"}*[timeout1]{lang="EN-US"}*[参数配置的时长内保持置位状态。]{style="font-family:宋体"}

[*[system-id]{lang="EN-US"}*]{#struct_0_17931_14437_x2008186470}[：指定邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[system-id]{lang="EN-US"}*[的格式为]{style="font-family:宋体"}[XXXX.XXXX.XXXX]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[timeout1]{lang="EN-US"}*]{#struct_0_17931_14437_x641736981}[：]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[*[nbr-timeout]{lang="EN-US"}*]{#struct_0_17931_14437_481580502}[：取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒（]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[*[timeout2]{lang="EN-US"}*]{#struct_0_17931_14437_x2121577335}[：]{style="font-family:宋体"}[从系统启动时开始计算，过载标志位保持置位状态的时间长度，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_2086243934}

[[当]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_883619347}[设备因为内存不足或其他原因无法记录完整的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[时，将会导致区域路由的计算错误。在故障排除过程中，通过给怀疑有问题的设备配置]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[过载标志位，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[将在该设备发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文中把]{style="font-family:宋体"}[Overload]{lang="EN-US"}[位置位，以通知其他设备该设备发生了问题，无法正确的执行路由选择和报文转发，从而可以将其从]{style="font-family:宋体"}[SPBN]{lang="EN-US"}[中暂时隔离，便于进行故障定位。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17931_14437_996189027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{lang="EN-US" style="font-family:宋体"}**[on-startup]{lang="EN-US"}**]{#struct_0_17931_14437_160449195}[参数，]{lang="EN-US" style="font-family:宋体"}[SPBM]{lang="EN-US"}[将立即把过载标志位置位且一直保持置位状态]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[直到用户通过]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **set-overload**]{lang="EN-US"}[命令]{style="font-family:宋体"}[清除过载标志位。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定]{style="font-family:宋体"}]{#struct_0_17931_14437_x1213163523}**[on-startup]{lang="EN-US"}**[参数，过载标志位将在系统启动时开始置位，并且在]{style="font-family:宋体"}*[timeout2]{lang="EN-US"}*[参数]{style="font-family:宋体"}[指定的时长内保持置位状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1865748882}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1469665653}[配置]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[过载标志位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_1404985064}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] set-overload]{lang="EN-US"}
:::

::: {#870763228 .myid}
[]{#_Toc404798217}[]{#struct_0_17931_14437_x1138014404}[]{#_Toc376192856}[]{#_Toc371320950}[]{#_Toc365452541}

**SPBM \-- SPBM配置命令 \-- snmp context-name**

------------------------------------------------------------------------

[**[snmp context-name]{lang="EN-US"}**]{#struct_0_17931_14437_179172359}[命令用来配置管理]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[**[undo snmp context-name]{lang="EN-US"}**]{#struct_0_17931_14437_751237761}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1409720361}

[**[snmp context-name ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_17931_14437_x1138342084}

[**[undo snmp context-name]{lang="EN-US"}**]{#struct_0_17931_14437_2075499018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1872818280}

[[没有配置管理]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1776579181}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x686875912}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x331182987}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1814377666}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1138407620}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x93345872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_205883245}

[*[context-name]{lang="EN-US"}*]{#struct_0_17931_14437_x337498537}[：管理]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1058109588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_203339909}[使用]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Management Information Base]{lang="EN-US"}[，管理信息库）]{lang="EN-US" style="font-family:宋体"}[对]{style="font-family:宋体"}[NMS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Network Management System]{lang="EN-US"}[，网络管理系统）]{lang="EN-US" style="font-family:宋体"}[提供]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[对象的管理，但标准]{style="font-family:宋体"}[IS-IS MIB]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[为单实例的管理对象，无法同时对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[和]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[进行管理。因此，参考]{style="font-family:宋体"}[RFC 4750]{lang="EN-US"}[中对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[多实例的管理方法，为管理]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[定义一个上下文名称，以区分从]{style="font-family:宋体"}[NMS]{lang="EN-US"}[来的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求是要对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[还是]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[进行管理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于上下文名称只是]{style="font-family:宋体"}]{#struct_0_17931_14437_x862963653}[SNMPv3]{lang="EN-US"}[独有的概念，因此对于]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[，会将团体名映射为上下文名称以对不同协议进行区分。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有使用]{lang="EN-US" style="font-family:宋体"}[IS]{lang="EN-US"}]{#struct_0_17931_14437_x1138211012}[-]{lang="EN-US"}[IS MIB]{lang="EN-US"}[的特性，如]{lang="EN-US" style="font-family:宋体"}[TRILL]{lang="EN-US"}[、]{style="font-family:宋体"}[EVI]{lang="EN-US"}[、]{style="font-family:宋体"}[SPB]{lang="EN-US"}[M]{lang="EN-US"}[、]{style="font-family:宋体"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[等，都需要支持配置]{lang="EN-US" style="font-family:宋体"}[上下文名称]{style="font-family:宋体"}[以区分]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求的管理对象。]{lang="EN-US" style="font-family:宋体"}[各特性实际配置的上下文名称是互斥的，即不允许不同的特性配置相同的上下文名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_46444461}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x2139457576}[配置管理]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称为]{style="font-family:宋体"}[spbm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_1593418211}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] snmp context-name spbm]{lang="EN-US"}
:::

::: {#671813558 .myid}
[]{#_Toc342496209}[]{#_Toc404798218}[]{#struct_0_17931_14437_440297932}[]{#_Toc353820843}[]{#_Toc353116135}

**SPBM \-- SPBM配置命令 \-- snmp-agent trap enable spbm**

------------------------------------------------------------------------

[**[snmp-agent trap enable spbm]{lang="EN-US"}**]{#struct_0_17931_14437_951330579}[命令用来开启]{style="font-family:
宋体"}[SPBM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable spbm]{lang="EN-US"}**]{#struct_0_17931_14437_160383659}[命令用来关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x329708512}

[**[snmp-agent trap enable spbm ]{lang="EN-US"}**[\[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **b-mac-conflict** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}]{#struct_0_17931_14437_x549638377}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| ]{lang="NO-BOK"}**[own-lsp-purge]{lang="EN-US"}**[ \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **spsource-conflict** \| **version-skew** \] **\***]{lang="EN-US"}

[**[undo snmp-agent trap enable spbm ]{lang="EN-US"}**[\[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **b-mac-conflict** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}]{#struct_0_17931_14437_x1138276548}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| ]{lang="NO-BOK"}**[own-lsp-purge]{lang="EN-US"}**[ \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **spsource-conflict** \| **version-skew** \] **\***]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1022511510}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1869427545}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1197548657}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x1116884177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_160318123}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1890740122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_550867480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x71637481}

[**[adjacency-state-change]{lang="EN-US"}**]{#struct_0_17931_14437_x1137555652}[：表示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[邻居状态变化的告警信息。]{style="font-family:宋体"}

[**[area-mismatch]{lang="EN-US"}**]{#struct_0_17931_14437_x1073492170}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_17931_14437_733970785}[：表示认证信息错误的告警信息。]{style="font-family:宋体"}

[**[authentication-type]{lang="EN-US"}**]{#struct_0_17931_14437_x1137621188}[：表示认证信息类型错误的告警信息。]{style="font-family:宋体"}

[**[b-mac-conflict]{lang="EN-US"}**]{#struct_0_17931_14437_1701815494}[：表示远端]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[与本地]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[发生冲突的告警信息。]{style="font-family:宋体"}

[**[buffsize-mismatch]{lang="EN-US"}**]{#struct_0_17931_14437_816921652}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文长度和产生缓冲区大小不匹配的告警信息。]{style="font-family:宋体"}

[**[id-length-mismatch]{lang="EN-US"}**]{#struct_0_17931_14437_962996539}[：表示]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[报文中]{style="font-family:宋体"}[System ID]{lang="EN-US"}[长度不匹配的告警信息。]{style="font-family:宋体"}

[**[lsdboverload-state-change]{lang="EN-US"}**]{#struct_0_17931_14437_x613747466}[：表示]{style="font-family:
宋体"}[LSDB]{lang="EN-US"}[过载状态变化的告警信息。]{style="font-family:宋体"}

[**[lsp-parse-error]{lang="NO-BOK"}**]{#struct_0_17931_14437_589711196}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文解析错误的告警信息。]{style="font-family:宋体"}

[**[lsp-size-exceeded]{lang="EN-US"}**]{#struct_0_17931_14437_1862652649}[：表示超大的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文导致泛洪失败的告警信息。]{style="font-family:宋体"}

[**[max-seq-exceeded]{lang="EN-US"}**]{#struct_0_17931_14437_x1138079945}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号超过最大序列号的告警信息。]{style="font-family:宋体"}

[**[maxarea-mismatch]{lang="NO-BOK"}**]{#struct_0_17931_14437_x1091203219}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文最大区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[own-lsp-purge]{lang="NO-BOK"}**]{#struct_0_17931_14437_516542027}[：表示尝试清除本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的告警信息。]{style="font-family:宋体"}

[**[protocol-support]{lang="EN-US"}**]{#struct_0_17931_14437_100877137}[：表示报文协议支持类型不匹配的告警信息。]{style="font-family:宋体"}

[**[rejected-adjacency]{lang="NO-BOK"}**]{#struct_0_17931_14437_1232246827}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文邻接不匹配丢弃的告警信息。]{style="font-family:宋体"}

[**[skip-sequence-number]{lang="EN-US"}**]{#struct_0_17931_14437_x2099762139}[：表示跳过已经产生过的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号的告警信息。]{style="font-family:宋体"}

[**[spsource-conflict]{lang="EN-US"}**]{#struct_0_17931_14437_x410686991}[：表示远端]{style="font-family:宋体"}[SPSource ID]{lang="EN-US"}[与本地配置]{style="font-family:宋体"}[SPSource ID]{lang="EN-US"}[发生冲突的告警信息。]{style="font-family:宋体"}

[**[version-skew]{lang="EN-US"}**]{#struct_0_17931_14437_x1138145481}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文版本号不匹配的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1873495012}

[[如果未指定参数任何参数，表示开启或关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x803124830}[的全部告警功能。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1941152822}[的告警功能后，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[会生成告警信息，用于报告本模块的重要事件。生成的告警信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过配置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_160252587}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1474532790}[关闭]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的全部告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_686444388}

[\[Sysname\] undo snmp-agent trap enable spbm]{lang="EN-US"}
:::

::: {#-216030531 .myid}
[]{#_Toc404798219}[]{#struct_0_17931_14437_1995412380}

**SPBM \-- SPBM配置命令 \-- spb i-sid**

------------------------------------------------------------------------

[**[spb i-sid]{lang="EN-US"}**]{#struct_0_17931_14437_1800892155}[命令用来创建]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[VSI SPB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo spb i-sid]{lang="EN-US"}**]{#struct_0_17931_14437_1149319599}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_840392037}

[**[spb i-sid]{lang="EN-US"}**[ *i-sid*]{lang="EN-US"}]{#struct_0_17931_14437_161235627}

[**[undo ]{lang="EN-US"}[spb i-sid]{lang="EN-US"}**]{#struct_0_17931_14437_x2144080258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1224588752}

[[未创建]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}]{#struct_0_17931_14437_x2097282064}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x632484830}

[[VSI]{lang="EN-US"}]{#struct_0_17931_14437_732172329}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x424708257}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x604264880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_161170091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1538131138}

[*[i-sid]{lang="EN-US"}*]{#struct_0_17931_14437_990617697}[：指定]{style="font-family:宋体"}[SPB]{lang="EN-US"}[的骨干网服务实例编号，取值范围为]{style="font-family:宋体"}[255]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1782633716}

[[创建]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}]{#struct_0_17931_14437_x1802495956}[实例就是创建一个]{style="font-family:宋体"}[SPB]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Switch Instance]{lang="EN-US"}[，虚拟交换实例），并同时指定其]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[。]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[是]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例的唯一编号，用来标识同一类型的服务，在同一个]{style="font-family:宋体"}[SPBN]{lang="EN-US"}[中必须指定相同的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[。有关]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[VPLS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_17931_14437_1079521320}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[的]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例专门提供给]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速泛洪通道，用于快速泛洪]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。该]{style="font-family:宋体"}[SPB VSI]{lang="EN-US"}[实例在创建后]{style="font-family:宋体"}[即可开启]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速泛洪通道，无需与接口或以太网服务实例关联。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_17931_14437_1621426769}[视图下，]{style="font-family:宋体"}[PBB]{lang="EN-US"}[（]{style="font-family:宋体"}[Provider Backbone Bridge]{lang="EN-US"}[，运营商骨干网桥）和]{style="font-family:宋体"}[SPB]{lang="EN-US"}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[不能相同。有关]{style="font-family:宋体"}[PBB]{lang="EN-US"}[的详细介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[PBB]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x56014301}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_2009497232}[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[指定]{style="font-family:宋体"}[SPB]{lang="EN-US"}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}[256]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI SPB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_160711340}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] spb i-sid 256]{lang="EN-US"}

[\[Sysname-vsi-vpn1-256\]]{lang="EN-US"}
:::

::: {#-1942264947 .myid}
[]{#_Toc404798220}[]{#struct_0_17931_14437_1414115119}

**SPBM \-- SPBM配置命令 \-- spbm**

------------------------------------------------------------------------

[**[spbm]{lang="EN-US"}**]{#struct_0_17931_14437_x1353489704}[命令用来全局使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，并进入]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[视图。如果]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能已全局使能，则直接进入]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo spbm]{lang="EN-US"}**]{#struct_0_17931_14437_375715465}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1951615486}

[**[spbm]{lang="EN-US"}**]{#struct_0_17931_14437_x258220592}

[**[undo spbm]{lang="EN-US"}**]{#struct_0_17931_14437_x1264258594}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_160645804}

[[全局的]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_193579065}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1048243009}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17931_14437_896050576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_847557653}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1431565842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_2076877404}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_160580268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局使能]{style="font-family:宋体"}]{#struct_0_17931_14437_326973875}[SPBM]{lang="EN-US"}[功能后才可进行其他]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[相关配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局关闭]{style="font-family:宋体"}]{#struct_0_17931_14437_1871357594}[SPBM]{lang="EN-US"}[功能时会删除所有]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1154843606}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x822991631}[全局使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能，并进入]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1989249449}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\]]{lang="EN-US"}
:::

::: {#-1156461151 .myid}
[]{#_Toc404798221}[]{#struct_0_17931_14437_460154986}[]{#_Toc362510284}

**SPBM \-- SPBM配置命令 \-- spbm authentication send-only**

------------------------------------------------------------------------

[**[spbm authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_459827306}[命令用来配置不对收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文进行验证密码检查。]{style="font-family:宋体"}

[**[undo spbm authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_334882324}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_459761770}

[**[spbm authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_459958378}

[**[undo]{lang="EN-US"}[ spbm authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_x1630214669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_459892842}

[[如果配置了接口验证方式和验证密码，则对收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17931_14437_460613738}[报文进行验证密码检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2144244642}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_460548202}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_460089449}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_460023913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_158476440}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_460220521}

[[配置邻居关系验证方式和验证密码时如果没有配置本命令，则在发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17931_14437_460154985}[报文中按照]{style="font-family:宋体"}**[spbm authentication-mode]{lang="EN-US"}**[命令指定的方式携带验证密码，并对收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文进行验证密码的检查，只有通过检查后，才会形成邻居关系。当需要更改密码时，由于两台设备的密码更改操作不完全同步，导致瞬时的密码不一致、邻居关系中断。此时，可以通过配置不对收到的报文进行验证密码检查，保证邻居关系不中断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1371613313}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_459827305}[配置不对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文进行验证密码检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_459761769}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm authentication send-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1079390245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm ]{lang="EN-US"}[authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_1079455781}
:::

::: {#-1872099048 .myid}
[]{#_Toc404798222}[]{#struct_0_17931_14437_1686419713}[]{#_Toc362510285}

**SPBM \-- SPBM配置命令 \-- spbm authentication-mode**

------------------------------------------------------------------------

[**[spbm authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_459958377}[命令用来配置邻居关系验证方式和验证密码。]{style="font-family:宋体"}

[**[undo spbm authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_459892841}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_460613737}

[**[spbm authentication-mode]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_17931_14437_x2144244651}**[md5]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[simple]{lang="EN-US"}**[ } { ]{lang="EN-US"}**[cipher ]{lang="EN-US"}***[cipher-string]{lang="EN-US"}*[ \| ]{lang="EN-US"}**[plain]{lang="EN-US"}***[ plain-string]{lang="EN-US"}*[ }]{lang="EN-US"}

[**[undo spbm authentication-mode]{lang="EN-US"}**]{#struct_0_17931_14437_460548201}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_460089452}

[[没有配置邻居关系验证方式和验证密码，不进行邻居关系验证。]{style="font-family:宋体"}]{#struct_0_17931_14437_x1387339796}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_460023916}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_460220524}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_432821803}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_460154988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_459827308}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_459761772}

[**[md5]{lang="EN-US"}**]{#struct_0_17931_14437_x652232440}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17931_14437_459958380}[：简单验证模式。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17931_14437_459892844}[：表示以密文的形式输入密码。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_17931_14437_x1195795068}[：表示密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_17931_14437_460613740}[：表示以明文的形式输入密码。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_17931_14437_460548204}[：表示明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x837343688}

[[配置邻居关系验证方式和验证密码后，将在发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17931_14437_460089451}[报文中按照设定的方式携带验证密码，并对收到的报文进行验证密码的检查。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17931_14437_460023915}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两台]{style="font-family:宋体"}]{#struct_0_17931_14437_158476438}[SPBM]{lang="EN-US"}[设备要形成邻居关系必须在相应接口上配置相同的验证方式和验证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式配置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17931_14437_460220523}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_460154987}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_459827307}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置邻居关系采用简单验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[，以明文形式输入密码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_334882323}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm authentication-mode simple plain 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1080242214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm authentication send-only]{lang="EN-US"}**]{#struct_0_17931_14437_1079652387}
:::

::: {#-107531184 .myid}
[]{#_Toc404798223}[]{#struct_0_17931_14437_x1057850195}[]{#_Toc365969278}[]{#_Toc365969351}[]{#_Toc366584243}

**SPBM \-- SPBM配置命令 \-- spbm cost**

------------------------------------------------------------------------

[**[spbm cost]{lang="EN-US"}**]{#struct_0_17931_14437_373014474}[命令用来配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[的接口链路开销值。]{style="font-family:宋体"}

[**[undo spbm cost]{lang="EN-US"}**]{#struct_0_17931_14437_x1307559415}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1247145299}

[**[spbm cost]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_17931_14437_1196408255}

[**[undo]{lang="EN-US"}**[ **spbm cost**]{lang="EN-US"}]{#struct_0_17931_14437_x362237108}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_160449196}

[[自动计算链路开销值。]{style="font-family:宋体"}]{#struct_0_17931_14437_x1213163522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_299664941}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_2075800316}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x725080193}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_1827602540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x685499184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_160383660}

[*[value]{lang="EN-US"}*]{#struct_0_17931_14437_1626606615}[：链路开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x468759960}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口链路开销值为]{style="font-family:宋体"}]{#struct_0_17931_14437_1675817256}[16777215]{lang="EN-US"}[时，可以通过该接口与邻居建立连接关系，但邻居不能承载流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当全局和接口同时配置链路开销值时，优先选择接口配置的链路开销值。]{style="font-family:宋体"}]{#struct_0_17931_14437_1942321930}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1309099881}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_160318124}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的链路开销值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1890740119}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm cost 5]{lang="EN-US"}
:::

::: {#-2009234403 .myid}
[]{#_Toc326076012}[]{#_Toc163546280}[]{#_Toc50204102}[]{#_Toc33866101}[]{#_Toc404798224}[]{#struct_0_17931_14437_1310447903}[]{#_Toc326076013}[]{#_Toc163546283}[]{#_Toc50204104}[]{#_Toc33866103}[]{#_Toc290911758}

**SPBM \-- SPBM配置命令 \-- spbm enable**

------------------------------------------------------------------------

[**[spbm enable]{lang="EN-US"}**]{#struct_0_17931_14437_x341935812}[命令用来在当前接口上使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo spbm enable]{lang="EN-US"}**]{#struct_0_17931_14437_x1815235613}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x51950540}

[**[spbm enable]{lang="EN-US"}**]{#struct_0_17931_14437_1277571150}

[**[undo]{lang="EN-US"}**[ **spbm enable**]{lang="EN-US"}]{#struct_0_17931_14437_160252588}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1474532779}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1895642609}[功能在接口上处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_809856821}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_x335491816}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1458007543}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_961279192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1339773362}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_161235628}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只需在]{style="font-family:宋体"}]{#struct_0_17931_14437_460548203}[BEB]{lang="EN-US"}[的上行口及]{style="font-family:宋体"}[BCB]{lang="EN-US"}[的接口上使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能接口上]{style="font-family:宋体"}]{#struct_0_17931_14437_x2144080267}[SPBM]{lang="EN-US"}[功能后才可进行接口上其他]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[相关配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭接口上]{style="font-family:宋体"}]{#struct_0_17931_14437_x1627676671}[SPBM]{lang="EN-US"}[功能时会删除该接口下所有]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[相关配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1115032238}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1085283312}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1374289128}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm enable]{lang="EN-US"}
:::

::: {#2045356553 .myid}
[]{#_Toc404798225}[]{#struct_0_17931_14437_818989390}

**SPBM \-- SPBM配置命令 \-- spbm timer hello**

------------------------------------------------------------------------

[**[spbm timer hello]{lang="EN-US"}**]{#struct_0_17931_14437_161170092}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo spbm timer hello]{lang="EN-US"}**]{#struct_0_17931_14437_1538131137}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_989634657}

[**[spbm timer hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_17931_14437_282222605}

[**[undo spbm timer hello]{lang="EN-US"}**]{#struct_0_17931_14437_x1228522012}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x263346439}

[[Hello]{lang="EN-US"}]{#struct_0_17931_14437_x533472120}[报文的发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x136524854}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_160711337}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x542200012}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1337716564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x290913699}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1871198014}

[*[seconds]{lang="EN-US"}*]{#struct_0_17931_14437_590635082}[：配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x993455349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备在邻居关系保持时间内（邻居关系保持时间＝允许失效的]{style="font-family:宋体"}]{#struct_0_17931_14437_160645801}[Hello]{lang="EN-US"}[报文×]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔）一直没有收到来自邻居设备的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，将宣告邻居关系失效。通过配置允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目和]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻居关系保持时间，从而控制设备监测到邻居关系已经失效并重新进行路由计算所需的时长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送时间间隔越短，网络收敛越快，但同时会占用更多的带宽资源和设备资源，请根据实际情况进行配置。]{style="font-family:宋体"}]{#struct_0_17931_14437_160580265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居关系保持时间最大为]{style="font-family:宋体"}]{#struct_0_17931_14437_x597349462}[65535]{lang="EN-US"}[秒。如果配置本命令后，计算出的邻居关系保持时间超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则配置失败，配置前的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔不做改变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_326973872}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1871357587}[配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的发送时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1154646999}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm timer hello 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1432870327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm timer holding-multiplier]{lang="EN-US"}**]{#struct_0_17931_14437_x675986024}
:::

::: {#-1661614079 .myid}
[]{#_Toc404798226}[]{#struct_0_17931_14437_x27541881}

**SPBM \-- SPBM配置命令 \-- spbm timer holding-multiplier**

------------------------------------------------------------------------

[**[spbm timer holding-multiplier]{lang="EN-US"}**]{#struct_0_17931_14437_160514729}[命令用来配置允许失效的]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文数目。]{style="font-family:
宋体"}

[**[undo spbm timer holding-multiplier]{lang="EN-US"}**]{#struct_0_17931_14437_330465682}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x725613342}

[**[spbm timer holding-multiplier]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_17931_14437_1782669166}

[**[undo spbm timer holding-multiplier]{lang="EN-US"}**]{#struct_0_17931_14437_2035238636}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1002197713}

[[允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_17931_14437_x867461150}[报文数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_1069716962}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_160449193}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1213163517}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x460046554}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x901587971}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_565268247}

[*[value]{lang="EN-US"}*]{#struct_0_17931_14437_x1914492001}[：允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2117451096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[失效的]{style="font-family:宋体"}]{#struct_0_17931_14437_160383657}[Hello]{lang="EN-US"}[报文数目，即宣告邻居失效前接口连续未收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目（每当一个]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔内没有收到邻居]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，就认为一个]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备在邻居关系保持时间内（邻居关系保持时间＝允许失效的]{style="font-family:宋体"}]{#struct_0_17931_14437_x329708514}[Hello]{lang="EN-US"}[报文数目×]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔）一直没有收到来自邻居设备的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，将宣告邻居关系失效。通过配置允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目和]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻居关系保持时间，从而控制设备监测到邻居关系已经失效并重新进行路由计算所需的时长。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[邻居关系保持时间最大为]{style="font-family:宋体"}]{#struct_0_17931_14437_x1741707692}[65535]{lang="EN-US"}[秒。如果配置本命令后，计算出的邻居关系保持时间超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒，则配置失败，配置前的允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目不做改变。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1235764227}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x619298975}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上允许失效的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数目为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_2045212365}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm timer holding-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1383091671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[spbm timer hello]{lang="EN-US"}**]{#struct_0_17931_14437_1502669842}
:::

::: {#162822040 .myid}
[]{#_Toc404798227}[]{#struct_0_17931_14437_160318121}

**SPBM \-- SPBM配置命令 \-- spbm timer lsp**

------------------------------------------------------------------------

[**[spbm timer lsp]{lang="EN-US"}**]{#struct_0_17931_14437_x1890740124}[命令用来配置发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔以及一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目。]{style="font-family:宋体"}

[**[undo spbm timer lsp]{lang="EN-US"}**]{#struct_0_17931_14437_1713666894}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_786230817}

[**[spbm timer lsp]{lang="EN-US"}**[ *time* \[ **count** *count* \]]{lang="EN-US"}]{#struct_0_17931_14437_1356371216}

[**[undo]{lang="EN-US"}**[ **spbm timer lsp**]{lang="EN-US"}]{#struct_0_17931_14437_x1703497574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_331121741}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_160252585}[的最小时间间隔为]{style="font-family:宋体"}[33]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1474532792}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17931_14437_1849243802}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_364564349}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_2117519091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_x242996997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_611669530}

[*[time]{lang="EN-US"}*]{#struct_0_17931_14437_x647805877}[：发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_17931_14437_161235625}[：一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x2144080256}

[[当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_17931_14437_x61789338}[的内容发生变化时，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[将把发生变化的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散出去，用户可以对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送时间间隔以及一次可以最多发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目进行调节。]{style="font-family:宋体"}

[[当存在大量]{style="font-family:宋体"}[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x418351785}[接口或大量路由时，会发送大量的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[风暴的出现。在这种情况下，建议将]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的发送时间间隔配置得稍大一些。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_343629225}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1774062200}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_492057071}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] spbm timer lsp 500]{lang="EN-US"}
:::

::: {#-834079892 .myid}
[]{#_Toc404798228}[]{#struct_0_17931_14437_646192895}[]{#_Toc131842023}[]{#_Toc131842774}[]{#_Toc131842024}[]{#_Toc131842775}[]{#_Toc131842025}[]{#_Toc131842776}

**SPBM \-- SPBM配置命令 \-- spsource**

------------------------------------------------------------------------

[**[spsource]{lang="EN-US"}**]{#struct_0_17931_14437_161170089}[命令用来配置]{style="font-family:宋体"}[SPSource ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo spsource]{lang="EN-US"}**]{#struct_0_17931_14437_x418183990}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1827173442}

[**[spsource]{lang="EN-US"}**[ *spsource-id*]{lang="EN-US"}]{#struct_0_17931_14437_82416022}

[**[undo spsource]{lang="EN-US"}**]{#struct_0_17931_14437_x1513337942}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_859367899}

[[SPSource ID]{lang="EN-US"}]{#struct_0_17931_14437_x347288270}[由协议动态生成。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_160711338}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x542200025}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1337782103}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1973154351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_201616511}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x813869549}

[*[spsource-id]{lang="EN-US"}*]{#struct_0_17931_14437_x1652358310}[：最短路径源标记，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1743259150}

[[SPSource ID]{lang="EN-US"}]{#struct_0_17931_14437_193579071}[用来区分同一实例中不同的设备。静态配置时需保证配置的]{style="font-family:宋体"}[SPSource ID]{lang="EN-US"}[整网唯一。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_908072123}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_52890039}[配置]{style="font-family:宋体"}[SPSource ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_249229974}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] spsource 100]{lang="EN-US"}
:::

::: {#408390348 .myid}
[]{#_Toc291226679}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404798229}[]{#struct_0_17931_14437_x2147011981}[]{#_Toc266971096}[]{#_Toc265680005}[]{#_Toc263067816}[]{#_Toc207010292}[]{#_Toc207010025}[]{#_Toc139515316}[]{#_Toc137103149}

**SPBM \-- SPBM配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

[**[timer]{lang="EN-US"}**[ **lsp-generation**]{lang="EN-US"}]{#struct_0_17931_14437_388452740}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的时间间隔。]{style="font-family:宋体"}

[**[undo timer lsp-generation]{lang="EN-US"}**]{#struct_0_17931_14437_160580266}[命令用来恢复缺省情况]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_326973873}

[**[timer lsp-generation]{lang="EN-US"}**[ *maximum-interval* \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_1871357588}

[**[undo timer lsp-generation]{lang="EN-US"}**]{#struct_0_17931_14437_x1154581463}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1877213740}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x1024756941}[重新生成的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_700604892}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1411624762}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_160514730}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x2008186469}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_568051064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_432563926}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x697878252}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x550600243}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x683806002}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x499700061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_17931_14437_x849215510}[命令在网络拓扑稳定的情况下将]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[时间间隔缩小到]{lang="EN-US" style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络拓扑震荡的情况下进行相应惩罚]{lang="EN-US" style="font-family:宋体"}[（如]{style="font-family:宋体"}[连续触发路由计算]{lang="EN-US" style="font-family:宋体"}[n]{lang="EN-US"}[次时，时间间隔]{style="font-family:宋体"}[增加]{lang="EN-US" style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[×]{lang="EN-US" style="font-family:宋体"}[2^n-2^]{lang="EN-US"}[），]{lang="EN-US" style="font-family:宋体"}[最终的时间间隔]{style="font-family:宋体"}[最大不超过]{lang="EN-US" style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中]{lang="EN-US" style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x1213163524}[和]{lang="EN-US" style="font-family:
宋体"}*[incremental-interva]{lang="EN-US"}*[l]{lang="EN-US"}[的]{style="font-family:宋体"}[配置值不允许大于]{lang="EN-US" style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[的]{style="font-family:宋体"}[配置值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1106233995}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_x1873301624}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x633356529}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] timer lsp-generation 10 100 200]{lang="EN-US"}
:::

::: {#490996559 .myid}
[]{#_Toc404798230}[]{#struct_0_17931_14437_x1630865127}

**SPBM \-- SPBM配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

[**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_17931_14437_1556085465}[命令用来配置当前设备生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间。]{style="font-family:宋体"}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_17931_14437_160383658}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x329708513}

[**[timer lsp-max-age]{lang="EN-US"}**[ *second*s]{lang="EN-US"}]{#struct_0_17931_14437_x1741773228}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_17931_14437_x788253974}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_x396832857}

[[当前设备生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17931_14437_1060519278}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_595337959}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1876313190}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_160318122}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x1890740121}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_954152007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x820158121}

[*[seconds]{lang="EN-US"}*]{#struct_0_17931_14437_x1934645845}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_1078262129}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令仅对当前设备生效。]{style="font-family:宋体"}]{#struct_0_17931_14437_x1215968675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每一个]{style="font-family:宋体"}]{#struct_0_17931_14437_506928765}[LSP]{lang="EN-US"}[都包含一个最大生存时间。当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[驻留在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的时间达到最大生存时间时，]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[将删除该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的内容，只保留该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的摘要信息（保留]{style="font-family:宋体"}[60]{lang="EN-US"}[秒），并将该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的剩余生存时间置]{style="font-family:宋体"}[0]{lang="EN-US"}[后，通知其他设备删除此]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。网络管理员可根据网络规模对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间进行调整。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1982434494}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_160252586}[配置当前设备生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x1474532789}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] timer lsp-max-age 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_1896363505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_17931_14437_x483001601}
:::

::: {#-1091829735 .myid}
[]{#_Toc404798231}[]{#struct_0_17931_14437_1591261345}

**SPBM \-- SPBM配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_17931_14437_x1070930857}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期。]{style="font-family:宋体"}

[**[undo timer lsp-refresh]{lang="EN-US"}**]{#struct_0_17931_14437_x2028350666}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_161235626}

[**[timer lsp-refresh]{lang="EN-US"}**[ *second*s]{lang="EN-US"}]{#struct_0_17931_14437_x2144080257}

[**[undo]{lang="EN-US"}**[ **timer lsp-refresh**]{lang="EN-US"}]{#struct_0_17931_14437_x1627873279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_788574090}

[[LSP]{lang="EN-US"}]{#struct_0_17931_14437_x49717977}[刷新周期为]{style="font-family:宋体"}[900]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1952838614}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_1991674028}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1882641707}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_161170090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1538131139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_990552161}

[*[seconds]{lang="EN-US"}*]{#struct_0_17931_14437_648197643}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1386200121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每一个]{style="font-family:宋体"}]{#struct_0_17931_14437_708913856}[LSP]{lang="EN-US"}[都有一个最大生存时间，每个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[都会随着时间的推移而被老化，因此每台设备必须定时刷新自己生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，以防止]{style="font-family:宋体"}[LSP]{lang="EN-US"}[被老化删除。另外，通过定时刷新]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，还可以使整个区域中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[保持同步。用户可对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新周期进行配置，提高]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新频率可以加快网络收敛速度，但是将占用更多的带宽。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_17931_14437_729331955}[命令配置的时间必须小于]{lang="EN-US" style="font-family:宋体"}**[timer lsp-max-age]{lang="EN-US"}**[命令配置的时间，以保证在]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[失效前进行刷新。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_x438295208}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_160711335}[配置当前系统的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x542200014}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] timer lsp-refresh 1200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1337847636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_17931_14437_x1426871069}
:::

::: {#1171776781 .myid}
[]{#_Toc404798232}[]{#struct_0_17931_14437_606983309}[]{#_Toc320886228}[]{#_Toc297189191}[]{#_Toc290886820}[]{#_Toc252200796}[]{#_Toc163546312}[]{#_Toc50204124}[]{#_Toc33866123}

**SPBM \-- SPBM配置命令 \-- timer spf**

------------------------------------------------------------------------

[**[timer spf]{lang="EN-US"}**]{#struct_0_17931_14437_384406809}[命令用来配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算[时间间隔]{#_Hlt23147082}。]{style="font-family:宋体"}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_17931_14437_267313203}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_160645799}

[**[timer spf]{lang="EN-US"}**[ *maximum-interval* \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_17931_14437_243368255}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_17931_14437_810873367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_1064290510}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x2067835891}[路由计算的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1563771517}

[[SPBM]{lang="EN-US"}]{#struct_0_17931_14437_x1614695647}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_x684440317}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_160580263}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_326973870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_1871357589}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x1154515927}[：]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_544994190}[：]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_17931_14437_x1580030362}[：]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17931_14437_x640554672}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_17931_14437_160514727}[命令在网络拓扑稳定的情况下将连续路由计算的时间间隔缩小到]{lang="EN-US" style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络拓扑震荡的情况下进行相应惩罚]{lang="EN-US" style="font-family:宋体"}[（如]{style="font-family:宋体"}[连续触发路由计算]{lang="EN-US" style="font-family:宋体"}[n]{lang="EN-US"}[次时，时间间隔]{style="font-family:宋体"}[增加]{lang="EN-US" style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[×]{lang="EN-US" style="font-family:宋体"}[2^n-2^]{lang="EN-US"}[），]{lang="EN-US" style="font-family:宋体"}[最终的时间间隔]{style="font-family:宋体"}[最大不超过]{lang="EN-US" style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令中]{lang="EN-US" style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_17931_14437_330465696}[和]{lang="EN-US" style="font-family:
宋体"}*[incremental-interval]{lang="EN-US"}*[的]{style="font-family:宋体"}[配置值不允许大于]{lang="EN-US" style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[的]{style="font-family:宋体"}[配置值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1613038822}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_211397118}[配置]{style="font-family:宋体"}[SPBM]{lang="EN-US"}[路由计算的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_818315960}

[\[Sysname\] spbm]{lang="EN-US"}

[\[Sysname-spbm\] timer spf 10 100 300]{lang="EN-US"}
:::

::: {#-981054953 .myid}
[]{#_Toc404798233}[]{#struct_0_17931_14437_x1005614182}

**SPBM \-- SPBM配置命令 \-- vsi**

------------------------------------------------------------------------

[**[vsi]{lang="EN-US"}**]{#struct_0_17931_14437_1695605754}[命令用来创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[已经存在，则直接进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vsi**]{lang="EN-US"}]{#struct_0_17931_14437_x1686063560}[命令用来删除指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_17931_14437_2733308}

[**[vsi]{lang="IT"}**]{#struct_0_17931_14437_x1005548646}[ *vsi-name*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_17931_14437_x696354300}[ ]{lang="IT"}**[vsi]{lang="IT"}**[ *vsi-name*]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17931_14437_151124047}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_17931_14437_288097641}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1400286499}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17931_14437_x254548660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17931_14437_1316591428}

[[network-admin]{lang="EN-US"}]{#struct_0_17931_14437_x776957979}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17931_14437_1632192999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17931_14437_x1005483110}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_17931_14437_x1384980915}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17931_14437_1856829162}

[[\# ]{lang="EN-US"}]{#struct_0_17931_14437_1454462028}[创建名为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17931_14437_x715048103}

[\[Sysname\] vsi test]{lang="EN-US"}

[\[Sysname-vsi-test\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17931_14437_x550799728}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_17931_14437_x1504501018}

[ ]{lang="EN-US"}
:::
