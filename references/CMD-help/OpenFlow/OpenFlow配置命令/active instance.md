::: {#435281283 .myid}
[]{#_Toc404798402}[]{#struct_0_x9563_11471_193579069}[]{#_Toc348873558}

**OpenFlow \-- OpenFlow配置命令 \-- active instance**

------------------------------------------------------------------------

[**[active instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x1048243021}[命令用来激活]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo active instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x1931575368}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1252412008}

[**[active instance]{lang="IT"}**]{#struct_0_x9563_11471_x846447785}

[**[undo active instance]{lang="IT"}**]{#struct_0_x9563_11471_x1049992779}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_x1387017649}

[[未激活]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x736361209}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1724748362}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x595487085}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_160580264}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_326973871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1871357590}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1155105750}

[[新配置的实例信息（如]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1677780051}[VLAN]{lang="IT"}[配置、]{style="font-family:宋体"}[Table]{lang="IT"}[配置）必须通过重新激活实例来生效。若当前实例已经与控制器建立连接，激活新配置后会重新建立连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_562590774}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_434875701}[激活]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x817371088}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] active instance]{lang="EN-US"}
:::

::: {#1433120220 .myid}
[]{#_Toc404798403}[]{#struct_0_x9563_11471_107371945}[]{#_Toc348873548}

**OpenFlow \-- OpenFlow配置命令 \-- classification**

------------------------------------------------------------------------

[**[classification]{lang="EN-US"}**]{#struct_0_x9563_11471_160514728}[命令用来配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例的类型。]{style="font-family:宋体"}

[**[undo classification]{lang="EN-US"}**]{#struct_0_x9563_11471_330465683}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x725613343}

[**[classification ]{lang="EN-US"}**[{ **global** \| **port** \| **vlan** *vlan-id* \[ **mask** *vlan-mask* \] \[ **loosen** \] }]{lang="EN-US"}]{#struct_0_x9563_11471_1782603630}

[**[undo classification]{lang="EN-US"}**]{#struct_0_x9563_11471_x1472658797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_2012286595}

[[没有配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x549002847}[实例的类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_946284335}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_913100848}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_160449192}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1213163518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x507100721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1356001504}

[**[global]{lang="EN-US"}**]{#struct_0_x9563_11471_x742096962}[：全局实例。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**]{#struct_0_x9563_11471_977960352}[：接口实例，实例按接口划分。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_x9563_11471_146363589}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[实例，实例按]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[划分。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x9563_11471_1019392118}[：]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vlan-mask]{lang="EN-US"}*]{#struct_0_x9563_11471_x576316397}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[掩码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[loosen]{lang="EN-US"}**]{#struct_0_x9563_11471_x849215513}[：]{style="font-family:宋体"}[loosen]{lang="EN-US"}[模式。配置]{style="font-family:宋体"}[loosen]{lang="EN-US"}[模式后，如果接口所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与实例配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[存在交集，则接口就属于]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例。没有配置]{style="font-family:宋体"}[loosen]{lang="EN-US"}[模式时，只有当实例配置的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[是接口所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子集，该接口才属于]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_2127478230}

[[多次执行该命令，后配置覆盖前配置。]{style="font-family:宋体"}]{#struct_0_x9563_11471_513002686}

[[VLAN & mask]{lang="EN-US"}]{#struct_0_x9563_11471_160383656}[为实际生效]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[区间。]{style="font-family:宋体"}[mask]{lang="EN-US"}[比特位为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示符合，可以不连续；比特位为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示忽略。生效]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[区间，可通过]{style="font-family:宋体"}**[display openflow instance]{lang="EN-US"}**[查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x329708515}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1741642156}[配置]{style="font-family:宋体"}[OpenFlow VLAN]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[，掩码为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1180657788}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] classification vlan 255 mask 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1722100471}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display openflow ]{lang="EN-US"}**]{#struct_0_x9563_11471_489375557}**[instance]{lang="EN-US"}**
:::

::: {#1895679317 .myid}
[]{#_Toc404798404}[]{#struct_0_x9563_11471_160318120}[]{#_Toc348873551}

**OpenFlow \-- OpenFlow配置命令 \-- controller address**

------------------------------------------------------------------------

[**[controller address]{lang="EN-US"}**]{#struct_0_x9563_11471_x1890740123}[命令用来配置主连接。]{style="font-family:宋体"}

[**[undo controller address]{lang="EN-US"}**]{#struct_0_x9563_11471_2116951421}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x627211586}

[**[controller ]{lang="EN-US"}***[controller-id]{lang="EN-US"}***[ address]{lang="EN-US"}**[ { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **port** *port-number* \] \[ **local address** { **ip** *local-ip-address* \| **ipv6** *local-ipv6-address* } \[ **port** *local-port- number* \] \] \[ **ssl** *ssl-policy-name* \] \[ **vrf** *vrf-name* \]]{lang="EN-US"}]{#struct_0_x9563_11471_x45517496}

[**[undo controller ]{lang="EN-US"}***[controller-id ]{lang="EN-US"}***[address]{lang="EN-US"}**]{#struct_0_x9563_11471_x667345004}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_535128073}

[[没有配置主连接。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x2116086708}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1348189583}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_160252584}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1474532791}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x2042438967}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1504135186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1704367415}

[*[controller-id]{lang="IT"}*]{#struct_0_x9563_11471_717065039}[：控制器的]{style="font-family:宋体"}[ID]{lang="IT"}[号，取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[63]{lang="IT"}[。]{style="font-family:
宋体"}

[**[ip]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9563_11471_x1087183212}*[ip-address]{lang="IT"}*[：]{style="font-family:宋体"}[控制器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9563_11471_x1217738810}*[ipv6-address]{lang="IT"}*[：]{style="font-family:宋体"}[控制器的]{style="font-family:宋体"}[IPv6]{lang="IT"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9563_11471_x1813582811}*[port-number]{lang="IT"}*[：]{style="font-family:宋体"}[控制器建立连接使用的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[6633]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local address]{lang="EN-US"}**]{#struct_0_x9563_11471_x1360691810}[：指交换机与控制器连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，当交换机与控制器之间存在多条链路可以连接时，只要有一条链路能够连接，]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[就不会断开连接。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**[ *local-*]{lang="EN-US"}]{#struct_0_x9563_11471_x1553730352}*[ip-address]{lang="IT"}*[：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *local-*]{lang="EN-US"}]{#struct_0_x9563_11471_x1360691805}*[ipv6-address]{lang="IT"}*[：源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *local-*]{lang="EN-US"}]{#struct_0_x9563_11471_x1360691804}*[port-number]{lang="IT"}*[：源端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ssl]{lang="IT"}**]{#struct_0_x9563_11471_503736431}*[ ssl-policy-name]{lang="IT"}*[：]{style="font-family:宋体"}[安全连接的客户端安全策略，用于控制器认证交换机，每个控制器连接配置独立的安全策略。]{style="font-family:宋体"}*[ssl-policy-name]{lang="IT"}*[为]{style="font-family:宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[31]{lang="IT"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[vrf ]{lang="IT"}**]{#struct_0_x9563_11471_1728052758}*[vrf-name]{lang="IT"}*[：]{style="font-family:
宋体"}[指定控制器所在的]{style="font-family:宋体"}[VRF]{lang="IT"}[，]{style="font-family:宋体"}*[vrf-name]{lang="IT"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="IT"}[的]{style="font-family:宋体"}[VPN]{lang="IT"}[实例名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[31]{lang="IT"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[控制器]{style="font-family:宋体"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_161235624}

[[多次执行该命令可以添加多个控制器，与每个控制器仅允许建立一个主连接。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x2144080255}

[[主连接一般用于控制消息的处理（下发流表项、获取数据、信息上报等）。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x465073865}

[[建议控制器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9563_11471_x1000830597}[地址使用单播地址，否则交换机和控制器之间可能无法建立连接。]{style="font-family:宋体"}

[[建议源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9563_11471_215448991}[地址使用单播地址，且该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例下一个端口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，否则交换机和控制器之间可能无法建立连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_2006613551}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_630366997}[配置实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的控制器]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[6666]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x627892563}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] controller 1 address ip 1.1.1.1 port 6666]{lang="EN-US"}
:::

::: {#-1596721595 .myid}
[]{#struct_0_x9563_11471_x742096966}[]{#_Toc404798405}[]{#_Toc384108849}

**OpenFlow \-- OpenFlow配置命令 \-- controller auxiliary**

------------------------------------------------------------------------

[**[controller auxiliary]{lang="EN-US"}**]{#struct_0_x9563_11471_x742096967}[命令用来配置辅助连接。]{style="font-family:宋体"}

[**[undo controller auxiliary]{lang="EN-US"}**]{#struct_0_x9563_11471_146560197}[命令用来取消配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1500592098}

[**[controller]{lang="EN-US"}**[ *id* **auxiliary** *auxiliary-id* **transport** { **tcp** \| **udp** \| **ssl** *ssl-policy-name* } \[ **address** { **ip** *ip-address* \| **ipv6** *ipv6-address* } \] \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_x9563_11471_x707251253}

[**[undo]{lang="EN-US"}**[ **controller** *id* **auxiliary** *auxiliary-id*]{lang="EN-US"}]{#struct_0_x9563_11471_x1557633705}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_1171099437}

[[没有配置辅助连接。]{style="font-family:宋体"}]{#struct_0_x9563_11471_907615125}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1641292198}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x742096968}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_145970373}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x227031326}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_626881809}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x490958224}

[**[controller ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_x9563_11471_x1999928912}[：实例下]{style="font-family:宋体"}[controller]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auxiliary ]{lang="EN-US"}***[auxiliary-id]{lang="EN-US"}*]{#struct_0_x9563_11471_1596555201}[：辅助连接编号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ssl ]{lang="EN-US"}**]{#struct_0_x9563_11471_x692865574}*[ssl-policy-name]{lang="IT"}*[：]{style="font-family:宋体"}[SSL]{lang="IT"}[策略的名称，为]{style="font-family:
宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[31]{lang="IT"}[字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x9563_11471_41256056}[：控制器的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_x9563_11471_1633273269}[：控制器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port ]{lang="IT"}**]{#struct_0_x9563_11471_x838170119}*[port-number]{lang="IT"}*[：]{style="font-family:
宋体"}[控制器的端口号]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[65535]{lang="IT"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_411755025}

[[OpenFlow]{lang="IT"}]{#struct_0_x9563_11471_1739780168}[通道可以由一个主连接和多个辅助连接组成。辅助连接用于提高控制器和]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[交换机的通信能力。]{style="font-family:宋体"}

[[辅助连接命令行和主连接命令行不做额外的检查处理。如果配置冲突，辅助连接将无法建立。]{style="font-family:宋体"}]{#struct_0_x9563_11471_1596555200}

[[辅助连接的目的地址和端口号可以和主连接不一致。目的地址和端口号未配置时，和主连接一致。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x692800038}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x1142151509}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x605303867}[为实例]{style="font-family:宋体"}[1]{lang="EN-US"}[下编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[控制器配置编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的辅助连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_382434431}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] controller 10 auxiliary 1 transport tcp]{lang="EN-US"}
:::

::: {#-164170884 .myid}
[]{#_Toc404798406}[]{#struct_0_x9563_11471_x1626477809}[]{#_Toc348873554}[]{#_Toc328657561}

**OpenFlow \-- OpenFlow配置命令 \-- controller connect interval**

------------------------------------------------------------------------

[**[controller connect interval]{lang="EN-US"}**]{#struct_0_x9563_11471_1332588463}[命令用来配置]{style="font-family:
宋体"}[OpenFlow]{lang="EN-US"}[实例与控制器重连尝试的时间间隔。]{style="font-family:宋体"}

[**[undo controller connect interval]{lang="EN-US"}**]{#struct_0_x9563_11471_161170088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x418183989}

[**[controller connect interval ]{lang="EN-US"}**]{#struct_0_x9563_11471_1826583617}*[interval-value]{lang="IT"}*

[**[undo controller connect interval]{lang="EN-US"}**]{#struct_0_x9563_11471_1232113935}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_x157251178}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_784366917}[实例与控制器重连尝试的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1173766810}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x1586696119}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_406962261}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1726795280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_134141365}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_499830450}

[*[interval-value]{lang="IT"}*]{#struct_0_x9563_11471_312612343}[：重连]{style="font-family:宋体"}[尝试的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="IT"}[～]{style="font-family:宋体"}[120]{lang="IT"}[，单位为秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_128354579}

[[\# ]{lang="SV"}]{#struct_0_x9563_11471_1709227487}[配置实例]{style="font-family:宋体"}[1]{lang="SV"}[与控制器重连尝试的时间间隔]{style="font-family:
宋体"}[为]{style="font-family:宋体"}[10]{lang="SV"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x170098188}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] controller connect interval 10]{lang="EN-US"}
:::

::: {#-386738565 .myid}
[]{#_Toc404798407}[]{#struct_0_x9563_11471_1661033659}[]{#_Toc348873553}

**OpenFlow \-- OpenFlow配置命令 \-- controller echo-request interval**

------------------------------------------------------------------------

[**[controller echo-request interval]{lang="EN-US"}**]{#struct_0_x9563_11471_1726729744}[命令用来配置发送]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo controller echo-request interval]{lang="EN-US"}**]{#struct_0_x9563_11471_1609321709}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1224448167}

[**[controller echo-request interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_x9563_11471_x2043881422}

[**[undo controller echo-request interval]{lang="EN-US"}**]{#struct_0_x9563_11471_62113604}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_370930816}

[[发送]{style="font-family:宋体"}[Echo request]{lang="EN-US"}]{#struct_0_x9563_11471_x983580708}[报文的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1406682315}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1506687601}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1726664208}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1669488945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x824660373}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2146238053}

[*[interval-value]{lang="EN-US"}*]{#struct_0_x9563_11471_718035054}[：发送]{style="font-family:宋体"}[Echo request]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x935961201}

[[\# ]{lang="SV"}]{#struct_0_x9563_11471_x269390243}[配置实例]{style="font-family:宋体"}[1]{lang="SV"}[发送]{style="font-family:
宋体"}[Echo request]{lang="EN-US"}[报文的时间间隔]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10]{lang="SV"}[秒。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1013194983}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] controller echo-request interval 10]{lang="EN-US"}
:::

::: {#-391790199 .myid}
[]{#_Toc404798408}[]{#struct_0_x9563_11471_1726598672}[]{#_Toc348873557}

**OpenFlow \-- OpenFlow配置命令 \-- controller mode**

------------------------------------------------------------------------

[**[controller mode]{lang="EN-US"}**]{#struct_0_x9563_11471_851630097}[命令用来配置实例内的多个]{style="font-family:宋体"}[控制器]{style="font-family:宋体"}[的连接模式。]{style="font-family:宋体"}

[**[undo controller mode]{lang="IT"}**]{#struct_0_x9563_11471_1872764689}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1688402166}

[**[controller mode]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_x9563_11471_x2137541522}**[multiple]{lang="IT"}**[ \| **single** }]{lang="EN-US"}

[**[undo controller mode]{lang="EN-US"}**]{#struct_0_x9563_11471_x1488003580}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_1596046462}

[[连接模式为]{style="font-family:宋体"}]{#struct_0_x9563_11471_1261847016}[Multiple]{lang="IT"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1162380032}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1726533136}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1262653710}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_274968922}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x376024821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1154339849}

[**[multiple]{lang="EN-US"}**]{#struct_0_x9563_11471_909989229}[：多连接模式。]{style="font-family:宋体"}

[**[single]{lang="EN-US"}**]{#struct_0_x9563_11471_404459006}[：单连接模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x592826628}

[[当连接模式是]{style="font-family:宋体"}]{#struct_0_x9563_11471_x425455648}[Single]{lang="IT"}[时，一次仅连接一个]{style="font-family:宋体"}[控制器]{style="font-family:宋体"}[，其它作为备份，仅当连接断开才根据]{style="font-family:宋体"}[ID]{lang="IT"}[顺序连接备份]{style="font-family:宋体"}[控制器]{style="font-family:宋体"}[，直到连接成功。]{style="font-family:宋体"}

[[当连接模式为]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726467600}[Multiple]{lang="IT"}[时，同时连接所有]{style="font-family:宋体"}[控制器]{style="font-family:宋体"}[，]{style="font-family:宋体"}[当一个或者多个控制器失效或者连接断开时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[仍然能保证]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[交换机正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_2031402688}

[[\# ]{lang="IT"}]{#struct_0_x9563_11471_2040132172}[配置实例]{style="font-family:宋体"}[1]{lang="IT"}[的控制器连接模式为]{style="font-family:
宋体"}[Single]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_x9563_11471_59264439}

[\[Sysname\] openflow instance 1]{lang="IT"}

[\[Sysname-of-inst-1\] controller mode single]{lang="IT"}
:::

::: {#1891831073 .myid}
[]{#_Toc404798409}[]{#struct_0_x9563_11471_717523791}[]{#_Toc362963992}

**OpenFlow \-- OpenFlow配置命令 \-- datapath-id**

------------------------------------------------------------------------

[**[datapath-id]{lang="EN-US"}**]{#struct_0_x9563_11471_x2088148411}[命令用来配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo datapath-id]{lang="EN-US"}**]{#struct_0_x9563_11471_x1383314844}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_717065040}

[**[datapath-id ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_x9563_11471_x1076880805}

[**[undo datapath-id]{lang="EN-US"}**]{#struct_0_x9563_11471_x1847528065}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_x582587591}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x1366515038}[实例的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}[是由实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[和设备桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[组成，前]{style="font-family:宋体"}[16]{lang="EN-US"}[个比特是实例]{style="font-family:宋体"}[ID]{lang="EN-US"}[，后]{style="font-family:宋体"}[48]{lang="EN-US"}[个比特是设备桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_98018478}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_716999504}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1320124978}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1594581336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1738480785}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x606587352}

[*[id]{lang="EN-US"}*]{#struct_0_x9563_11471_717196112}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFFFFFFFFFFFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x294279215}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_232066063}[配置实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0x123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1968842656}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] datapath-id 123456]{lang="IT"}
:::

::: {#50529872 .myid}
[]{#_Toc404798410}[]{#struct_0_x9563_11471_x359759935}[]{#_Toc384108854}[]{#_Toc377731832}

**OpenFlow \-- OpenFlow配置命令 \-- default table-miss permit**

------------------------------------------------------------------------

[**[default table-miss permit]{lang="EN-US"}**]{#struct_0_x9563_11471_x1152703764}[命令用来配置]{style="font-family:
宋体"}[OpenFlow]{lang="EN-US"}[实例缺省的]{style="font-family:宋体"}[table miss ]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[**[undo default table-miss permit]{lang="EN-US"}**]{#struct_0_x9563_11471_554453172}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_84125651}

[**[default table-miss permit]{lang="EN-US"}**]{#struct_0_x9563_11471_x1744284675}

[**[undo default table-miss permit]{lang="EN-US"}**]{#struct_0_x9563_11471_x985385555}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x359759936}

[[缺省]{style="font-family:宋体"}[table miss]{lang="EN-US"}]{#struct_0_x9563_11471_x1152769300}[动作为丢弃]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x357946598}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x859949227}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_877404969}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1389507875}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_673109147}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x359759937}

[[如果配置了本命令，则实例下所有流表的缺省]{style="font-family:宋体"}[table miss]{lang="EN-US"}]{#struct_0_x9563_11471_x1152834836}[动作为走正常二三层转发；如果没有配置本命令，则实例下所有流表的缺省]{style="font-family:宋体"}[table miss]{lang="EN-US"}[动作为丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_287654072}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_395520167}[配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[table miss]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_220374959}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] default table-miss permit]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404798411}[]{#struct_0_x9563_11471_x12287628}[]{#_Toc348873549}

**OpenFlow \-- OpenFlow配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x9563_11471_x1559881554}[命令用来配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9563_11471_x1430518277}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1875986345}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x9563_11471_x1018826874}

[**[undo description]{lang="EN-US"}**]{#struct_0_x9563_11471_1726402064}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_500112527}

[[没有配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1372936649}[实例的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1372328058}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_833524987}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1841717026}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x583926672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x180081023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_215529635}

[*[text]{lang="EN-US"}*]{#struct_0_x9563_11471_1726336528}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1267944138}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_31008016}[配置实例]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[test-desc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_627607678}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] description test-desc]{lang="EN-US"}
:::

::: {#-176519058 .myid}
[]{#_Toc404798412}[]{#struct_0_x9563_11471_x359759939}[]{#_Toc384108856}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow auxiliary**

------------------------------------------------------------------------

[**[display openflow auxiliary]{lang="EN-US"}**]{#struct_0_x9563_11471_x1153490196}[命令用来]{style="font-family:
宋体"}[显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例的辅助连接信息和收发的报文统计信息等]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_1390263908}

[**[display]{lang="EN-US"}**[ **openflow** **instance** *instance-id* **auxiliary** \[ *controller-id* \[ **auxiliary** *auxiliary-id* \] \]]{lang="EN-US"}]{#struct_0_x9563_11471_x118359266}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x359759940}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1152900379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_629033825}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1860201040}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_1328255218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_243848784}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x359759941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1152965915}

[**[instance]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x9563_11471_1914013925}*[instance-id]{lang="IT"}*[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[controller-id]{lang="EN-US"}*]{#struct_0_x9563_11471_x1500403882}[：控制器编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[auxiliary ]{lang="EN-US"}***[auxiliary-id]{lang="EN-US"}*]{#struct_0_x9563_11471_1504434808}[：辅助连接编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_289600977}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_720253632}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[100]{lang="EN-US"}[的控制器辅助连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow instance 100 auxiliary]{lang="EN-US"}]{#struct_0_x9563_11471_x359759942}

[Controller ID: 1    Auxiliary connection number: 2]{lang="EN-US"}

[ Auxiliary connection ID : 1]{lang="EN-US"}

[  Controller IP address  : 192.168.49.48]{lang="EN-US"}

[  Controller port        : 6633]{lang="EN-US"}

[  Connect type           : TCP]{lang="EN-US"}

[  Connect state          : Established]{lang="EN-US"}

[  Packets sent           : 9]{lang="EN-US"}

[  Packets received       : 9]{lang="EN-US"}

[  SSL policy             : \--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Auxiliary connection ID : 2]{lang="EN-US"}

[  Controller IP address  : 192.168.49.49]{lang="EN-US"}

[   Controller port       : 6633]{lang="EN-US"}

[   Connect type          : TCP]{lang="EN-US"}

[   Connect state         : Established]{lang="EN-US"}

[   Packets sent          : 9]{lang="EN-US"}

[   Packets received      : 9]{lang="EN-US"}

[   SSL policy            : \--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display openflow auxiliary]{lang="EN-US"}]{#struct_0_x9563_11471_x1153031451}[命令显示描述表]{style="font-family:黑体"}

[]{#table_struct_0_1832450891}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x359759943}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1153096987}

[[Controller ID]{lang="EN-US"}]{#struct_0_x9563_11471_x359759944}

[[控制器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1152638235}

[[Auxiliary connection number]{lang="EN-US"}]{#struct_0_x9563_11471_1978892225}

[[辅助连接总数量]{style="font-family:宋体"}]{#struct_0_x9563_11471_1978892224}

[[Auxiliary connection ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1896276681}

[[辅助连接的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9563_11471_1978892223}

[[Controller IP address]{lang="EN-US"}]{#struct_0_x9563_11471_x1896473289}

[[已经配置在实例下的]{style="font-family:宋体"}[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_1978892222}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Controller port]{lang="EN-US"}]{#struct_0_x9563_11471_x1896407753}

[[当前连接]{style="font-family:宋体"}[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_1978892221}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Connect type]{lang="EN-US"}]{#struct_0_x9563_11471_1978892220}

[[连接类型，]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1896538825}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_1978892219}[：使用]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Controller]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_x1897128652}[：使用]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Controller]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_x9563_11471_1978892218}[：使用]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Controller]{lang="EN-US"}

[[Connect state]{lang="EN-US"}]{#struct_0_x9563_11471_x1897063116}

[[连接状态：]{style="font-family:宋体"}]{#struct_0_x9563_11471_1978892217}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x9563_11471_1978892216}[：未建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_x9563_11471_x1896145612}[：成功建立连接]{lang="EN-US" style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_x9563_11471_22577089}

[[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_921352652}[发送的报文的计数]{style="font-family:宋体"}

[[Packets received]{lang="EN-US"}]{#struct_0_x9563_11471_22577088}

[[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_x1034962484}[接收的报文的计数]{style="font-family:宋体"}

[[SSL policy]{lang="EN-US"}]{#struct_0_x9563_11471_22577087}

[[用于]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_22577086}[连接的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1012948448 .myid}
[]{#_Toc404798413}[]{#struct_0_x9563_11471_x1049046228}[]{#_Toc348873561}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow controller**

------------------------------------------------------------------------

[**[display openflow controller]{lang="EN-US"}**]{#struct_0_x9563_11471_x1076159990}[命令用来]{style="font-family:
宋体"}[显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例对应的控制器信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_95642142}

[**[display openflow]{lang="EN-US"}**[ { **instance** *instance-id* { **controller** \[ *controller-id* \] \| **listened** } \| **oap-instance** **listened** }]{lang="EN-US"}]{#struct_0_x9563_11471_668866405}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1727319568}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_97537399}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1122023816}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1335186088}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x1745398635}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1495724047}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_449739693}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_654847166}

[*[instance-id]{lang="IT"}*]{#struct_0_x9563_11471_1385601537}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[controller-id]{lang="IT"}*]{#struct_0_x9563_11471_716933968}[：控制器的]{style="font-family:宋体"}[ID]{lang="IT"}[号，取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[63]{lang="IT"}[。如果未指定本参数，将显示实例下所有控制器的信息。]{style="font-family:
宋体"}

[**[listened]{lang="IT"}**]{#struct_0_x9563_11471_22577084}[：实例启动的服务端连接的客户端]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[oap-instance]{lang="IT"}**]{#struct_0_x9563_11471_965982668}[：]{style="font-family:宋体"}[OpenFlow OAP]{lang="IT"}[实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_1943539144}

[[\# ]{lang="IT"}]{#struct_0_x9563_11471_980442274}[显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例]{style="font-family:宋体"}[100]{lang="IT"}[对应的控制器信息。]{style="font-family:
宋体"}

[[\<Sysname\> display openflow instance 100 controller]{lang="EN-US"}]{#struct_0_x9563_11471_2042582996}

[OpenFlow instance ID: 100]{lang="EN-US"}

[ Reconnect interval : 60 (s)]{lang="EN-US"}

[ Echo interval      : 5  (s)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Controller ID           : 1]{lang="EN-US"}

[ Controller IP address   : 192.168.49.49]{lang="EN-US"}

[ Controller port         : 6633]{lang="EN-US"}

[ Local IP address        : 192.0.0.1]{lang="EN-US"}

[ Local port              : 5566]{lang="EN-US"}

[ Controller role         : Equal]{lang="EN-US"}

[ Connect type            : TCP]{lang="EN-US"}

[ Connect state           : Established]{lang="EN-US"}

[ Packets sent            : 9]{lang="EN-US"}

[ Packets received        : 9]{lang="EN-US"}

[ SSL policy              : \--]{lang="EN-US"}

[ VRF name                : \--]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display openflow controller]{lang="EN-US"}]{#struct_0_x9563_11471_x1212985799}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1141477450}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_1726795281}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_134075829}

[[OpenFlow instance ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1000896133}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x744515674}[实例号]{style="font-family:宋体"}

[[Reconnect interval]{lang="EN-US"}]{#struct_0_x9563_11471_717589328}

[[实例内所有控制器的断开重连时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x9563_11471_717523792}

[[Echo interval]{lang="EN-US"}]{#struct_0_x9563_11471_x2088148408}

[[实例内所有控制器发送保活报文的时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_x9563_11471_717065037}

[[Controller ID]{lang="EN-US"}]{#struct_0_x9563_11471_565187808}

[[控制器的]{style="font-family:宋体"}]{#struct_0_x9563_11471_917878644}[ID]{lang="IT"}[号]{style="font-family:宋体"}

[[Controller IP address]{lang="EN-US"}]{#struct_0_x9563_11471_x457619727}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x69197050}[实例对应的控制器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Controller port]{lang="EN-US"}]{#struct_0_x9563_11471_1726729745}

[[当前连接控制器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_1609387245}[端口号]{style="font-family:宋体"}

[[Local IP address]{lang="EN-US"}]{#struct_0_x9563_11471_191659513}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_191659519}[实例对应的控制器的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Local port]{lang="EN-US"}]{#struct_0_x9563_11471_191659518}

[[当前连接控制器的源]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_191659517}[端口号]{style="font-family:宋体"}

[[Controller role]{lang="EN-US"}]{#struct_0_x9563_11471_1166901729}

[[控制器的角色：]{style="font-family:宋体"}]{#struct_0_x9563_11471_1120257854}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_x9563_11471_x1016086646}[：未连接，未配置角色]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Equal]{lang="EN-US"}]{#struct_0_x9563_11471_1992357241}[：控制器的角色是]{lang="EN-US" style="font-family:宋体"}[Equal]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_x9563_11471_1726664209}[：控制器的角色是]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Slave]{lang="EN-US"}]{#struct_0_x9563_11471_1669554481}[：控制器的角色是]{lang="EN-US" style="font-family:宋体"}[Slave]{lang="EN-US"}

[[Connect type]{lang="EN-US"}]{#struct_0_x9563_11471_1932404124}

[[连接类型，]{style="font-family:宋体"}]{#struct_0_x9563_11471_1042956845}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_x1575450863}[：使用]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接控制器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_x1658993828}[：使用]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[连接控制器]{lang="EN-US" style="font-family:宋体"}

[[Connect state]{lang="EN-US"}]{#struct_0_x9563_11471_1726598673}

[[连接状态：]{style="font-family:宋体"}]{#struct_0_x9563_11471_851564561}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_x9563_11471_x1962902437}[：未建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_x9563_11471_x674535026}[：成功建立连接]{lang="EN-US" style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_x9563_11471_x381722574}

[[已经向控制器发送的报文的计数]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726533137}

[[Packets received]{lang="EN-US"}]{#struct_0_x9563_11471_1262588174}

[[已经接收控制器的报文的计数]{style="font-family:宋体"}]{#struct_0_x9563_11471_698003020}

[[SSL policy]{lang="EN-US"}]{#struct_0_x9563_11471_1917409773}

[[用于]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_1726467601}[连接的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略的名称]{style="font-family:宋体"}

[[VRF name]{lang="EN-US"}]{#struct_0_x9563_11471_1324702695}

[[控制器所在的]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x9563_11471_900734126}[名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#995838192 .myid}
[]{#_Toc404798414}[]{#struct_0_x9563_11471_2031468224}[]{#_Toc348873560}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow flow-table**

------------------------------------------------------------------------

[**[display openflow flow-table]{lang="EN-US"}**]{#struct_0_x9563_11471_1985523192}[命令用来]{style="font-family:
宋体"}[显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例的流表信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1449065923}

[**[display openflow instance]{lang="EN-US"}**[ { *instance-id* \| **oap-instance** } **flow-table** \[ *table-id* \]]{lang="EN-US"}]{#struct_0_x9563_11471_x760271174}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1275357897}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1514745141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1993991864}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1970136190}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_1726402065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_500178063}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x164228208}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1801421878}

[*[instance-id]{lang="SV" style="color:black"}*]{#struct_0_x9563_11471_2066966498}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x1933738050}[：]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[*[table-id]{lang="SV" style="color:black"}*]{#struct_0_x9563_11471_x643432037}[：]{style="font-family:宋体"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[，取值范围为]{style="font-family:
宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[254]{lang="IT"}[。如果未指定本参数，将显示所有流表的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x1646581734}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_1238326668}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[100]{lang="EN-US"}[的所有流表信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow instance 100 flow-table]{lang="EN-US"}]{#struct_0_x9563_11471_1727319569}

[Instance 100 flow table information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table 0 information:]{lang="EN-US"}

[ Table type: MAC-IP, flow entry count: 1, total flow entry count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[MissRule (default) Flow entry information:]{lang="EN-US"}

[ cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: reset_counts]{lang="EN-US"}

[ \|no_pkt_counts\|no_byte_counts, byte count: \--, packet count: \--]{lang="EN-US"}

[Match information: any]{lang="EN-US"}

[Instruction information:]{lang="EN-US"}

[ Write actions:]{lang="EN-US"}

[  Drop]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flow entry rule 1 information:]{lang="EN-US"}

[ cookie: 0x0, priority: 1, hard time: 0, idle time: 0, flags: none,]{lang="EN-US"}

[ byte count: \--, packet count: \--]{lang="EN-US"}

[Match information:]{lang="EN-US"}

[ Ethernet destination MAC address: 0000-0000-0001]{lang="EN-US"}

[ Ethernet destination MAC address mask: ffff-ffff-ffff]{lang="EN-US"}

[ VLAN ID: 100, mask: 0xfff]{lang="EN-US"}

[Instruction information:]{lang="EN-US"}

[ Write actions:]{lang="EN-US"}

[  Output interface: GE1/0/4]{lang="EN-US"}

[ Write metadata/mask: 0x0000000000000001/0xffffffffffffffff]{lang="EN-US"}

[ Goto table: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Table 1 information:]{lang="EN-US"}

[ Table type: Extensibility, flow entry count: 2, total flow entry count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[MissRule (default) Flow entry information:]{lang="EN-US"}

[ cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: none,]{lang="EN-US"}

[ byte count: \--, packet count: 60]{lang="EN-US"}

[Match information: any]{lang="EN-US"}

[Instruction information:]{lang="EN-US"}

[ Write actions:]{lang="EN-US"}

[  Drop]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flow entry rule 1 information:]{lang="EN-US"}

[ cookie: 0x0, priority: 0, hard time: 0, idle time: 0, flags: flow_send_rem]{lang="EN-US"}

[ \|check_overlap, byte count: \--, packet count: 1]{lang="EN-US"}

[Match information:]{lang="EN-US"}

[ Input interface: GE1/0/3]{lang="EN-US"}

[ Ethernet source MAC address: 0000-0000-0001]{lang="EN-US"}

[ Ethernet source MAC address mask: ffff-ffff-ffff]{lang="EN-US"}

[Instruction information:]{lang="EN-US"}

[ Set meter: 100]{lang="EN-US"}

[ Apply actions:]{lang="EN-US"}

[  Output interface: GE1/0/4]{lang="EN-US"}

[ Write actions:]{lang="EN-US"}

[  Output interface: Controller, send length: 128 bytes]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display openflow flow-table]{lang="EN-US"}]{#struct_0_x9563_11471_97471863}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1172186250}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1858438816}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1495238031}

[[Table information]{lang="EN-US"}]{#struct_0_x9563_11471_1923436352}

[[流表信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_1727254033}

[[Table type]{lang="EN-US"}]{#struct_0_x9563_11471_x1660643455}

[[流表类型：]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726795278}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MAC-IP]{lang="EN-US"}]{#struct_0_x9563_11471_133617062}[：]{lang="EN-US" style="font-family:宋体"}[MAC-IP]{lang="EN-US"}[流表]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Extensibility]{lang="EN-US"}]{#struct_0_x9563_11471_2073040122}[：]{lang="EN-US" style="font-family:宋体"}[Extensibility]{lang="EN-US"}[流表]{lang="EN-US" style="font-family:宋体"}

[[flow entry]{lang="EN-US"}]{#struct_0_x9563_11471_716737358}[ count]{lang="EN-US"}

[[控制器下发的流表项个数]{style="font-family:宋体"}]{#struct_0_x9563_11471_716933966}

[[total flow entry]{lang="EN-US"}]{#struct_0_x9563_11471_x1384109944}[ count]{lang="EN-US"}

[[流表中流表项总个数]{style="font-family:宋体"}]{#struct_0_x9563_11471_x909932457}

[[Flow entry]{lang="EN-US"}[ rule]{lang="EN-US"}]{#struct_0_x9563_11471_4589710}[ information]{lang="EN-US"}

[[流表项信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726729742}

[[cookie]{lang="EN-US"}]{#struct_0_x9563_11471_2136856040}

[[流表项]{style="font-family:宋体"}[cookie]{lang="EN-US"}]{#struct_0_x9563_11471_x108061088}

[[priority]{lang="EN-US"}]{#struct_0_x9563_11471_1726664206}

[[流表项的优先级，数值越大，优先级越高]{style="font-family:宋体"}]{#struct_0_x9563_11471_1669620017}

[[hard time]{lang="EN-US"}]{#struct_0_x9563_11471_368661386}

[[流表项的]{style="font-family:宋体"}[hard time]{lang="EN-US"}]{#struct_0_x9563_11471_x1875314020}[超时时间，单位为秒，]{style="font-family:宋体"}[0]{lang="EN-US"}[代表永不超时。当定时器超时后就清除该流表项，无论该流表项是否匹配到数据流]{style="font-family:宋体"}

[[idle time]{lang="EN-US"}]{#struct_0_x9563_11471_x897092878}

[[流表项的]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726598670}[idle ]{lang="EN-US"}[time]{lang="EN-US"}[超时时间，单位为秒，]{style="font-family:宋体"}[0]{lang="EN-US"}[代表永不超时。如果]{style="font-family:宋体"}[idle ]{lang="EN-US"}[time]{lang="EN-US"}[超时时间内没有数据流匹配到该流表项，该流表项被清除]{style="font-family:
  宋体"}

[[flags]{lang="EN-US"}]{#struct_0_x9563_11471_851761169}

[[流表项的标志位：]{style="font-family:宋体"}]{#struct_0_x9563_11471_x2030589465}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[flow_send_rem]{lang="EN-US"}]{#struct_0_x9563_11471_x659581316}[：发送流表项删除消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[check_overlap]{lang="EN-US"}]{#struct_0_x9563_11471_1726533134}[：检查流表项重复]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[reset_counts]{lang="EN-US"}]{#struct_0_x9563_11471_1262522638}[：重置流表项统计信息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[no_pkt_counts]{lang="EN-US"}]{#struct_0_x9563_11471_x483115938}[：不统计报文计数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[no_byte_counts]{lang="EN-US"}]{#struct_0_x9563_11471_x335967379}[：不统计字节计数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_x9563_11471_1726467598}[：无标志位]{lang="EN-US" style="font-family:宋体"}

[[byte count]{lang="EN-US"}]{#struct_0_x9563_11471_x307773751}

[[匹配当前流表项的字节计数]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1232306969}

[[packet count]{lang="EN-US"}]{#struct_0_x9563_11471_894098651}

[[匹配当前流表项的报文计数]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726402062}

[[Match information]{lang="EN-US"}]{#struct_0_x9563_11471_500505743}

[[匹配规则信息（]{style="font-family:宋体"}]{#struct_0_x9563_11471_1125871800}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?995838192#_Ref349812296)[）]{style="font-family:宋体"}

[[Instruction information]{lang="EN-US"}]{#struct_0_x9563_11471_1470867315}

[[动作指令集信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726336526}

[[Set meter]{lang="EN-US"}]{#struct_0_x9563_11471_1267813066}

[[应用指定的]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_x352997221}[表]{style="font-family:宋体"}

[[Write metadata]{lang="EN-US"}]{#struct_0_x9563_11471_x1452490065}

[[写入元数据，元数据用来在不同流表间传递信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_1727319566}

[[Write metadata mask]{lang="EN-US"}]{#struct_0_x9563_11471_97144183}

[[元数据掩码]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1110205660}

[[Goto table]{lang="EN-US"}]{#struct_0_x9563_11471_1727254030}

[[进入下一级流表]{style="font-family:宋体"}]{#struct_0_x9563_11471_2078040500}

[[Clear actions]{lang="EN-US"}]{#struct_0_x9563_11471_x1416681338}

[[清除动作集中的所有动作]{style="font-family:宋体"}]{#struct_0_x9563_11471_1899322126}

[[Apply actions]{lang="EN-US"}]{#struct_0_x9563_11471_1726795279}

[[立即执行动作序列中的动作（]{style="font-family:宋体"}]{#struct_0_x9563_11471_133551526}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?995838192#_Ref349812331)[）]{style="font-family:宋体"}

[[Write actions]{lang="EN-US"}]{#struct_0_x9563_11471_1060752747}

[[更改动作集中的所有动作（]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726729743}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?995838192#_Ref349812331)[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x9563_11471_1608994029}[[表1-3 ]{lang="EN-US"}[流表项匹配规则信息]{style="font-family:
黑体"}]{#_Ref349812296}

[]{#table_struct_0_1162917514}[[匹配字段名称]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1559300816}

[[匹配掩码字段名称]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1562828072}

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x80014893}

[[Input interface]{lang="EN-US"}]{#struct_0_x9563_11471_1110021558}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x602369907}

[[入端口（]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726664207}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?995838192#_Ref349812380)[）]{style="font-family:宋体"}

[[Physical input interface]{lang="EN-US"}]{#struct_0_x9563_11471_1669685553}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x2002543987}

[[入物理端口]{style="font-family:宋体"}]{#struct_0_x9563_11471_4654299}

[[Metadata]{lang="EN-US"}]{#struct_0_x9563_11471_1649689840}

[[Metadata mask]{lang="EN-US"}]{#struct_0_x9563_11471_943021314}

[[元数据]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9563_11471_1726598671}[掩码]{style="font-family:宋体"}

[[Ethernet destination MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_851695633}

[[Ethernet destination MAC address]{lang="EN-US"}[ mask]{lang="EN-US"}]{#struct_0_x9563_11471_658770189}

[[以太网目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9563_11471_x1233990279}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[Ethernet source MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_x1837260400}

[[Ethernet source MAC address ]{lang="EN-US"}[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726533135}

[[以太网源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9563_11471_1262457102}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[Ethernet type]{lang="EN-US"}]{#struct_0_x9563_11471_x1312193659}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_2007235174}

[[以太网类型]{style="font-family:宋体"}]{#struct_0_x9563_11471_x543334871}

[[VLAN ID]{lang="EN-US"}]{#struct_0_x9563_11471_1726467599}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_x307708215}

[[VLAN ID/]{lang="EN-US"}]{#struct_0_x9563_11471_663590494}[掩码]{style="font-family:宋体"}

[[VLAN PCP]{lang="EN-US"}]{#struct_0_x9563_11471_x534239788}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_863310373}

[[VLAN]{lang="EN-US"}]{#struct_0_x9563_11471_1726402063}[优先级]{style="font-family:宋体"}

[[IP DSCP]{lang="EN-US"}]{#struct_0_x9563_11471_500571279}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1581307312}

[[DSCP]{lang="EN-US"}]{#struct_0_x9563_11471_1048304352}[（]{style="font-family:宋体"}[Differentiated Services Code Point]{lang="EN-US"}[，区分服务编码点）值]{style="font-family:
  宋体"}

[[IP ECN]{lang="EN-US"}]{#struct_0_x9563_11471_1726336527}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1267747530}

[[IP]{lang="EN-US"}]{#struct_0_x9563_11471_x1137474645}[头的]{style="font-family:宋体"}[ECN]{lang="EN-US"}[（]{style="font-family:宋体"}[Explicit Congestion Notification]{lang="EN-US"}[，显式拥塞通知）值]{style="font-family:宋体"}

[[IP protocol]{lang="EN-US"}]{#struct_0_x9563_11471_1454018307}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1727319567}

[[IPv4]{lang="EN-US"}]{#struct_0_x9563_11471_97078647}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议号]{style="font-family:宋体"}

[[IPv4 source address]{lang="EN-US"}]{#struct_0_x9563_11471_x540350583}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_x29028092}

[[IPv4]{lang="EN-US"}]{#struct_0_x9563_11471_1727254031}[源地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[IPv4 destination address]{lang="EN-US"}]{#struct_0_x9563_11471_2077974964}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_x1295058525}

[[IPv4]{lang="EN-US"}]{#struct_0_x9563_11471_602299949}[目的地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[TCP source port]{lang="EN-US"}]{#struct_0_x9563_11471_1726795276}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_134272422}

[[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_1149399307}[源端口]{style="font-family:宋体"}

[[TCP destination port]{lang="EN-US"}]{#struct_0_x9563_11471_1726729740}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1609059565}

[[TCP]{lang="EN-US"}]{#struct_0_x9563_11471_1200504162}[目的端口]{style="font-family:宋体"}

[[UDP source port]{lang="EN-US"}]{#struct_0_x9563_11471_x318769747}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726664204}

[[UDP]{lang="EN-US"}]{#struct_0_x9563_11471_1669751089}[源端口]{style="font-family:宋体"}

[[UDP destination port]{lang="EN-US"}]{#struct_0_x9563_11471_x1195128819}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726598668}

[[UDP]{lang="EN-US"}]{#struct_0_x9563_11471_851236882}[目的端口]{style="font-family:宋体"}

[[SCTP source port]{lang="EN-US"}]{#struct_0_x9563_11471_x632241180}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726533132}

[[SCTP]{lang="EN-US"}]{#struct_0_x9563_11471_1262391566}[（]{style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="EN-US"}[，流控制传输协议）源端口]{style="font-family:
  宋体"}

[[SCTP destination port]{lang="EN-US"}]{#struct_0_x9563_11471_x1278687096}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1440339970}

[[SCTP]{lang="EN-US"}]{#struct_0_x9563_11471_1726467596}[目的端口]{style="font-family:宋体"}

[[ICMPv4 type]{lang="EN-US"}]{#struct_0_x9563_11471_x307642679}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1612248977}

[[ICMPv4]{lang="EN-US"}]{#struct_0_x9563_11471_1726402060}[类型]{style="font-family:宋体"}

[[ICMPv4 code]{lang="EN-US"}]{#struct_0_x9563_11471_500374671}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x298976060}

[[ICMPv4]{lang="EN-US"}]{#struct_0_x9563_11471_1726336524}[代号]{style="font-family:宋体"}

[[ARP opcode]{lang="EN-US"}]{#struct_0_x9563_11471_1267681994}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1727319564}

[[ARP]{lang="EN-US"}]{#struct_0_x9563_11471_97275255}[操作类型]{style="font-family:宋体"}

[[ARP source IPv4 address]{lang="EN-US"}]{#struct_0_x9563_11471_1932576567}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1727254028}

[[ARP]{lang="EN-US"}]{#struct_0_x9563_11471_2077516211}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ARP target IPv4 address]{lang="EN-US"}]{#struct_0_x9563_11471_308012106}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726795277}

[[ARP]{lang="EN-US"}]{#struct_0_x9563_11471_134206886}[目标]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ARP source MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_1928194228}

[[ARP source MAC address ]{lang="EN-US"}[ mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726729741}

[[ARP]{lang="EN-US"}]{#struct_0_x9563_11471_1609125101}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[ARP target MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_1726664205}

[[ARP target MAC address]{lang="EN-US"}[ mask]{lang="EN-US"}]{#struct_0_x9563_11471_1669816625}

[[ARP]{lang="EN-US"}]{#struct_0_x9563_11471_x826339737}[目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPv6 source address]{lang="EN-US"}]{#struct_0_x9563_11471_1726598669}

[[IPv6 source address]{lang="EN-US"}[ mask]{lang="EN-US"}]{#struct_0_x9563_11471_851171346}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_1726533133}[源地址]{style="font-family:宋体"}

[[IPv6 destination address]{lang="EN-US"}]{#struct_0_x9563_11471_1262326030}

[[IPv6 ]{lang="EN-US"}[destination address mask]{lang="EN-US"}]{#struct_0_x9563_11471_x2069622892}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_1726467597}[目的地址]{style="font-family:宋体"}

[[IPv6 flow label]{lang="EN-US"}]{#struct_0_x9563_11471_x307577143}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1726402061}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_500440207}[流标签]{style="font-family:宋体"}

[[ICMPv6 type]{lang="EN-US"}]{#struct_0_x9563_11471_x1175836103}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1726336525}

[[ICMPv6]{lang="EN-US"}]{#struct_0_x9563_11471_1267616458}[类型]{style="font-family:宋体"}

[[ICMPv6 code]{lang="EN-US"}]{#struct_0_x9563_11471_1727319565}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_97209719}

[[ICMPv6]{lang="EN-US"}]{#struct_0_x9563_11471_1727254029}[代号]{style="font-family:宋体"}

[[IPv6 ND target address]{lang="EN-US"}]{#struct_0_x9563_11471_2077450675}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002088075}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_x1198483774}[邻居发现协议报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPv6 ND source MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_x498002661}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002153611}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_324428077}[邻居发现协议报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPv6 ND target MAC address]{lang="EN-US"}]{#struct_0_x9563_11471_x1002219147}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1785494108}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_x1002284683}[邻居发现协议的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MPLS label]{lang="EN-US"}]{#struct_0_x9563_11471_1757958750}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002350219}

[[MPLS]{lang="EN-US"}]{#struct_0_x9563_11471_x161366951}[第一个头部的标签]{style="font-family:宋体"}

[[MPLS tc]{lang="EN-US"}]{#struct_0_x9563_11471_x1002415755}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1171165484}

[[MPLS]{lang="EN-US"}]{#struct_0_x9563_11471_x1002481291}[第一个头部的]{style="font-family:宋体"}[TC]{lang="EN-US"}[（]{style="font-family:宋体"}[Traffic Class]{lang="EN-US"}[，流量等级）]{style="font-family:宋体"}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_x9563_11471_x86152916}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_x1002546827}

[[与一个逻辑口相关的]{style="font-family:宋体"}[MetaData]{lang="EN-US"}]{#struct_0_x9563_11471_602342620}

[[IPv6 extension header]{lang="EN-US"}]{#struct_0_x9563_11471_x1001563787}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1828748740}

[[IPv6]{lang="EN-US"}]{#struct_0_x9563_11471_x1001629323}[扩展头]{style="font-family:宋体"}

[[Output interface]{lang="EN-US"}]{#struct_0_x9563_11471_1238338373}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238534981}

[[出接口]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238666053}

[[VRF index]{lang="EN-US"}]{#struct_0_x9563_11471_1238600517}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1237748549}

[[VPN]{lang="EN-US"}]{#struct_0_x9563_11471_1237683013}[索引]{style="font-family:宋体"}

[[Fragment]{lang="EN-US"}]{#struct_0_x9563_11471_1238272836}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238207300}

[[分片标志]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238403908}

[[Physical output interface]{lang="EN-US"}]{#struct_0_x9563_11471_1238338372}

[[无]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238469444}

[[出物理端口]{style="font-family:宋体"}]{#struct_0_x9563_11471_1238666052}

[[CVLAN ID]{lang="EN-US"}]{#struct_0_x9563_11471_1238600516}

[[mask]{lang="EN-US"}]{#struct_0_x9563_11471_1237748548}

[[CVLAN ID/]{lang="EN-US"}]{#struct_0_x9563_11471_1237683012}[掩码]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x9563_11471_1237659720}[[表1-4 ]{lang="EN-US"}[流表项动作类型]{style="font-family:
黑体"}]{#_Ref349812331}

[]{#table_struct_0_1179793162}[[动作名称]{style="font-family:黑体"}]{#struct_0_x9563_11471_346768660}

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2064578770}

[[Drop]{lang="EN-US"}]{#struct_0_x9563_11471_x1948102172}

[[丢弃报文（非协议]{style="font-family:宋体"}[Action]{lang="EN-US"}]{#struct_0_x9563_11471_1957379363}[）]{style="font-family:宋体"}

[[Output interface]{lang="EN-US"}]{#struct_0_x9563_11471_x1002088074}

[[从指定端口发送报文（]{style="font-family:宋体"}]{#struct_0_x9563_11471_1530399581}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?995838192#_Ref349812380)[）]{style="font-family:宋体"}

[[send length]{lang="EN-US"}]{#struct_0_x9563_11471_x839367310}

[[当]{style="font-family:宋体"}[output]{lang="EN-US"}]{#struct_0_x9563_11471_1593148514}[类型为]{style="font-family:宋体"}[Controller]{lang="EN-US"}[时，指定上送报文的字节长度]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_x9563_11471_1947972532}

[[根据指定]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_791435640}[表处理报文]{style="font-family:宋体"}

[[Set queue]{lang="EN-US"}]{#struct_0_x9563_11471_x1002153610}

[[将流表项映射到指定队列]{style="font-family:宋体"}[ID ]{lang="EN-US"}]{#struct_0_x9563_11471_1890512018}

[[Set field]{lang="EN-US"}]{#struct_0_x9563_11471_x1642697003}

[[修改报文指定的域]{style="font-family:宋体"}]{#struct_0_x9563_11471_960960199}

[[Set MPLS TTL]{lang="EN-US"}]{#struct_0_x9563_11471_x1166756381}

[[设定]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x9563_11471_x1002219146}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域值]{style="font-family:宋体"}

[[Set IP TTL]{lang="EN-US"}]{#struct_0_x9563_11471_x219410167}

[[设定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9563_11471_460706467}[头的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[域值]{style="font-family:宋体"}

[[Push VLAN tag]{lang="EN-US"}]{#struct_0_x9563_11471_1802101071}

[[添加一个新的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x9563_11471_x1348364183}

[[Push MPLS tag]{lang="EN-US"}]{#struct_0_x9563_11471_x1002284682}

[[添加一个新的]{style="font-family:宋体"}[MPLS Tag]{lang="EN-US"}]{#struct_0_x9563_11471_191874809}

[[Pop MPLS tag]{lang="EN-US"}]{#struct_0_x9563_11471_x1498633835}

[[删除最外层的]{style="font-family:宋体"}[MPLS Tag]{lang="EN-US"}]{#struct_0_x9563_11471_882647639}

[[Push PBB tag]{lang="EN-US"}]{#struct_0_x9563_11471_x1002350218}

[[添加一个新的]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_x9563_11471_1404716990}[服务]{style="font-family:宋体"}[Tag]{lang="EN-US"}

[[Pop VLAN tag]{lang="EN-US"}]{#struct_0_x9563_11471_1674710200}

[[删除最外层的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_x9563_11471_x365480795}

[[Pop PBB tag]{lang="EN-US"}]{#struct_0_x9563_11471_x1634000565}

[[删除最外层]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_x9563_11471_x1002415754}[服务]{style="font-family:宋体"}[Tag]{lang="EN-US"}

[[Decrement MPLS TTL]{lang="EN-US"}]{#struct_0_x9563_11471_394918457}

[[MPLS]{lang="EN-US"}]{#struct_0_x9563_11471_247490768}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[减一]{style="font-family:宋体"}

[[Decrement IP TTL]{lang="EN-US"}]{#struct_0_x9563_11471_1300327996}

[[IP]{lang="EN-US"}]{#struct_0_x9563_11471_x1002481290}[的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[减一]{style="font-family:宋体"}

[[Copy TTL inwards]{lang="EN-US"}]{#struct_0_x9563_11471_x1652236857}

[[将最外层的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_x9563_11471_468405530}[拷贝到紧接最外层]{style="font-family:宋体"}

[[Copy TTL outwards]{lang="EN-US"}]{#struct_0_x9563_11471_544647541}

[[将紧接最外层的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_x9563_11471_x1002546826}[拷贝到最外层]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x9563_11471_x963741321}[[表1-5 ]{lang="EN-US"}[流表项端口类型]{style="font-family:
黑体"}]{#_Ref349812380}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OpenFlow命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x9563_11471_x53570044}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[具体支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x9563_11471_2062017209}
:::

[ ]{lang="EN-US"}

[]{#table_struct_0_1174920330}[[端口名称]{style="font-family:黑体"}]{#struct_0_x9563_11471_1177515912}

[[入端口]{style="font-family:黑体"}]{#struct_0_x9563_11471_70292022}

[[出端口]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1001563786}

[[说明]{style="font-family:黑体"}]{#struct_0_x9563_11471_262664799}

[[In port]{lang="EN-US"}]{#struct_0_x9563_11471_1928246012}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x310162709}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_438692068}

[[报文从入接口转发]{style="font-family:宋体"}]{#struct_0_x9563_11471_x695836386}

[[Table]{lang="EN-US"}]{#struct_0_x9563_11471_x1001629322}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x328424221}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_1803890414}

[[报文重新进入流表进行匹配]{style="font-family:宋体"}]{#struct_0_x9563_11471_1789862625}

[[Normal]{lang="EN-US"}]{#struct_0_x9563_11471_1991609653}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_914898675}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002088077}

[[报文正常转发]{style="font-family:宋体"}]{#struct_0_x9563_11471_x35684360}

[[Flood]{lang="EN-US"}]{#struct_0_x9563_11471_x2094492356}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_899961221}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_709396671}

[[报文广播发送]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002153613}

[[All]{lang="EN-US"}]{#struct_0_x9563_11471_x838371337}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_1595633050}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_243333782}

[[报文从所有接口发送]{style="font-family:宋体"}]{#struct_0_x9563_11471_111127080}

[[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_x1002219149}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_2059134494}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x717077046}

[[报文上送控制器]{style="font-family:宋体"}]{#struct_0_x9563_11471_124405327}

[[Local]{lang="EN-US"}]{#struct_0_x9563_11471_x1002284685}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1730439492}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1357583783}

[[报文上送本地]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_x9563_11471_x565733068}

[[Any]{lang="EN-US"}]{#struct_0_x9563_11471_x1002350221}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_194797873}

[[不支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_1925113734}

[[接口通配描述，不能作为入接口以及出接口]{style="font-family:宋体"}]{#struct_0_x9563_11471_x815165039}

[[（端口名称）]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002415757}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_1961002398}

[[支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1115734791}

[[实例有效端口，包含物理接口和逻辑接口（如聚合接口）]{style="font-family:宋体"}]{#struct_0_x9563_11471_872300870}

[ ]{lang="EN-US"}

::: {#-1550264228 .myid}
[]{#_Toc404798415}[]{#struct_0_x9563_11471_x2011818319}[]{#_Toc362963998}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow group**

------------------------------------------------------------------------

[**[display openflow group]{lang="EN-US"}**]{#struct_0_x9563_11471_x1953896899}[命令用来显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例的]{style="font-family:宋体"}[Group]{lang="EN-US"}[表项]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2011883855}

[**[display]{lang="EN-US"}**[ **openflow** **instance** { *instance-id* \| **oap-instance** } **group** \[ *group-id* \]]{lang="EN-US"}]{#struct_0_x9563_11471_2043647705}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2011687247}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x540442603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2011752783}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1071024105}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x2012080463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1388466784}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x2012145999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1100653665}

[*[instance-id]{lang="IT"}*]{#struct_0_x9563_11471_x2011949391}[：]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x361922628}[：]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[*[group-]{lang="IT"}*[id]{lang="EN-US"}]{#struct_0_x9563_11471_1976191328}[：]{style="font-family:宋体"}[Group ID]{lang="EN-US"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[0xffffff00]{lang="IT"}[。如果未指定本参数，将显示实例所有]{style="font-family:宋体"}[Group]{lang="EN-US"}[表项]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x2012014927}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x2021620324}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[Group]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow instance 100 group]{lang="EN-US"}]{#struct_0_x9563_11471_x2011294031}

[Instance 100 group table information:]{lang="EN-US"}

[ Group count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Group entry 103:]{lang="EN-US"}

[ Type: All, byte count: 55116, packet count: 401]{lang="EN-US"}

[ Bucket 1 information: ]{lang="EN-US"}

[Action count 1, watch port: any, watch group: any]{lang="EN-US"}

[Byte count 55116, packet count 401]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Output interface: BAGG100]{lang="EN-US"}

[ Bucket 2 information:]{lang="EN-US"}

[ Action count 1, watch port: any, watch group: any]{lang="EN-US"}

[  Byte count \--, packet count \--]{lang="EN-US"}

[  Output interface: Controller, send length: 128 bytes]{lang="EN-US"}

[ Referencedinformation:]{lang="EN-US"}

[  Count: 3]{lang="EN-US"}

[  Flow table 0]{lang="EN-US"}

[  Flow entry: 1, 2, 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Group entry 104:]{lang="EN-US"}

[ Type: All, byte count: 0, packet count: 0]{lang="EN-US"}

[ Bucket 1 information:]{lang="EN-US"}

[  Action count 1, watch port: any, watch group: any]{lang="EN-US"}

[  Byte count \--, packet count \--]{lang="EN-US"}

[  Output interface: Controller, send length: 128 bytes]{lang="EN-US"}

[ Referencedinformation:]{lang="EN-US"}

[  Count: 0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display openflow group]{lang="EN-US"}]{#struct_0_x9563_11471_x2011359567}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1405318402}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1558558075}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x445734375}

[[Group count]{lang="EN-US"}]{#struct_0_x9563_11471_x445799911}

[[当前实例包含的]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445603303}[表项的总个数]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x9563_11471_x445668839}

[[当前]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445996519}[表项的类型，]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[All]{lang="EN-US"}]{#struct_0_x9563_11471_x446062055}[：执行所有动作桶，用于组播或者广播]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Select]{lang="EN-US"}]{#struct_0_x9563_11471_x445865447}[：自动选择一个动作桶执行]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Indirect]{lang="EN-US"}]{#struct_0_x9563_11471_x445930983}[：始终执行固定的]{style="font-family:
  宋体"}[动作桶]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Fast failover]{lang="EN-US"}]{#struct_0_x9563_11471_x445210087}[：始终]{style="font-family:宋体"}[执行第一个活跃的动作桶]{lang="EN-US" style="font-family:宋体"}

[[Bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x445275623}

[[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445734374}[表项包含的]{style="font-family:宋体"}[bucket]{lang="EN-US"}

[[Action count]{lang="EN-US"}]{#struct_0_x9563_11471_x445799910}

[[当前]{style="font-family:宋体"}[bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x445603302}[包含的]{style="font-family:宋体"}[action]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[[Byte count]{lang="EN-US"}]{#struct_0_x9563_11471_x445668838}

[[group/bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x445996518}[的字节统计计数，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不支持]{style="font-family:宋体"}

[[packet count]{lang="EN-US"}]{#struct_0_x9563_11471_x862235118}

[[group/bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x446062054}[的报文统计计数，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不支持]{style="font-family:宋体"}

[[watch port]{lang="EN-US"}]{#struct_0_x9563_11471_x445865446}

[[影响]{style="font-family:宋体"}[bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x445930982}[的]{style="font-family:宋体"}[live]{lang="EN-US"}[状态的端口]{style="font-family:宋体"}

[[watch group]{lang="EN-US"}]{#struct_0_x9563_11471_x445210086}

[[影响]{style="font-family:宋体"}[bucket]{lang="EN-US"}]{#struct_0_x9563_11471_x445275622}[的]{style="font-family:宋体"}[live]{lang="EN-US"}[状态的]{style="font-family:宋体"}[group ID]{lang="EN-US"}

[[Output interface]{lang="EN-US"}]{#struct_0_x9563_11471_x445734377}

[[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445799913}[表项中包含的出端口]{style="font-family:宋体"}

[[Referenced information]{lang="EN-US"}]{#struct_0_x9563_11471_x445603305}

[[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445996521}[表项]{lang="EN-US" style="font-family:宋体"}[被流表项引用的信息]{style="font-family:宋体"}

[[Count]{lang="EN-US"}]{#struct_0_x9563_11471_x862693873}

[[引用]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x446062057}[表项的流表项的总个数]{style="font-family:宋体"}

[[Flow table]{lang="EN-US"}]{#struct_0_x9563_11471_x445865449}

[[引用]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445930985}[表项的流表项所在的流表]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Flow entry]{lang="EN-US"}]{#struct_0_x9563_11471_x445210089}

[[引用]{style="font-family:宋体"}[Group]{lang="EN-US"}]{#struct_0_x9563_11471_x445275625}[表项的流表项]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1593445552 .myid}
[]{#_Toc404798416}[]{#struct_0_x9563_11471_x1002481293}[]{#_Toc348873559}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow instance**

------------------------------------------------------------------------

[**[display openflow instance]{lang="EN-US"}**]{#struct_0_x9563_11471_1076646498}[命令用来显示]{style="font-family:
宋体"}[OpenFlow]{lang="IT"}[实例的详细信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_664858734}

[**[display openflow instance ]{lang="EN-US"}**[\[ *instance-id* \| **oap-instance** \]]{lang="EN-US"}]{#struct_0_x9563_11471_1039457920}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2050050360}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_860446962}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1255778685}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1214642565}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x1002546829}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1052681314}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_436711475}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1322970929}

[*[instance-id]{lang="IT"}*]{#struct_0_x9563_11471_97252421}[：]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，将显示所有实例的详细信息]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[**[oap-instance]{lang="IT"}**]{#struct_0_x9563_11471_1976729536}[：]{style="font-family:宋体"}[OpenFlow OAP]{lang="IT"}[实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x1106112957}

[[\# ]{lang="IT"}]{#struct_0_x9563_11471_x938973077}[显示所有]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow instance]{lang="IT"}]{#struct_0_x9563_11471_x1001563789}

[Instance 100 verbose information:]{lang="IT"}

[ ]{lang="IT"}

[Configuration information:]{lang="EN-US"}

[ Description   : test-desc]{lang="EN-US"}

[ Active status : Active]{lang="EN-US"}

[ Inactive configuration:]{lang="EN-US"}

[  Classification: VLAN, total VLANs(1)]{lang="EN-US"}

[   3]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(MAC-IP)]{lang="EN-US"}

[   Table ID(type): 1(Extensibility)]{lang="EN-US"}

[ Active configuration:]{lang="EN-US"}

[  Classification: VLAN, loosen mode, total VLANs(1)]{lang="EN-US"}

[   2]{lang="EN-US"}

[  In-band management VLAN, total VLANs(0)]{lang="EN-US"}

[   Empty VLAN]{lang="EN-US"}

[  Connect mode: Multiple]{lang="EN-US"}

[  MAC-address learning: Disabled]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(MAC-IP), count: 0]{lang="EN-US"}

[  Flow-entry max-limit: 65535]{lang="EN-US"}

[  Datapath ID: 0x0000001234567891]{lang="EN-US"}

[  Default table-miss: Drop]{lang="EN-US"}

[  Forbidden port: None]{lang="EN-US"}

[Port information:]{lang="EN-US"}

[ GigabitEthernet1/0/3]{lang="EN-US"}

[Active channel information:]{lang="EN-US"}

[ Controller 1 IP address: 192.168.49.49  port: 6633]{lang="EN-US"}

[ Controller 2 IP address: 192.168.43.49  port: 6633]{lang="EN-US"}

[ ]{lang="EN-US"}

[Instance 200 verbose information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Configuration information:]{lang="EN-US"}

[ Description   : test]{lang="EN-US"}

[ Active status : Active]{lang="EN-US"}

[ Inactive configuration:]{lang="EN-US"}

[  Classification: VLAN, total VLANs(1)]{lang="EN-US"}

[   1]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(MAC-IP)]{lang="EN-US"}

[   Table ID(type): 1(Extensibility)]{lang="EN-US"}

[ Active configuration:]{lang="EN-US"}

[  Classification: VLAN, total VLANs(1)]{lang="EN-US"}

[   4]{lang="EN-US"}

[  In-band management VLAN, total VLANs(0)]{lang="EN-US"}

[   Empty VLAN]{lang="EN-US"}

[  Connect mode: Multiple]{lang="EN-US"}

[  MAC-address learning: Disabled]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(MAC-IP), count: 0]{lang="EN-US"}

[  Flow-entry max-limit: 65535]{lang="EN-US"}

[  Datapath ID: 0x0000001234567890]{lang="EN-US"}

[  Default table-miss: Permit]{lang="EN-US"}

[  Forbidden port: VLAN interface]{lang="EN-US"}

[Port information:]{lang="EN-US"}

[ GigabitEthernet0/1/3]{lang="EN-US"}

[Active channel information:]{lang="EN-US"}

[ Fail-open mode: Secure]{lang="EN-US"}

[ ]{lang="EN-US"}

[Instance 300 verbose information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Configuration information:]{lang="EN-US"}

[ Description   : test]{lang="EN-US"}

[ Active status : Active]{lang="EN-US"}

[ Inactive configuration:]{lang="EN-US"}

[  None]{lang="EN-US"}

[ Active configuration:]{lang="EN-US"}

[  Classification: VLAN, total VLANs(4)]{lang="EN-US"}

[   8, 10, 12, 14]{lang="EN-US"}

[  In-band management VLAN, total VLANs(1)]{lang="EN-US"}

[   10]{lang="EN-US"}

[  Connect mode: Multiple]{lang="EN-US"}

[  MAC-address learning: Disabled]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(MAC-IP), count: 0]{lang="EN-US"}

[  Flow-entry max-limit: 65535]{lang="EN-US"}

[  Datapath ID: 0x0000001234567801]{lang="EN-US"}

[  Default table-miss: Drop]{lang="EN-US"}

[  Forbidden port: None]{lang="EN-US"}

[Port information:]{lang="EN-US"}

[ GigabitEthernet0/1/3]{lang="EN-US"}

[Active channel information:]{lang="EN-US"}

[ Failopen mode: Secure]{lang="EN-US"}

[ ]{lang="EN-US"}

[Instance 400 information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Configuration information:]{lang="EN-US"}

[ Description   : \--]{lang="EN-US"}

[ Active status : inactive]{lang="EN-US"}

[ Inactive configuration:]{lang="EN-US"}

[  Classification: Port]{lang="IT"}

[  Port configuration information:]{lang="IT"}

[   GigabitEthernet2/0/1]{lang="IT"}

[   GigabitEthernet2/0/2]{lang="IT"}

[   GigabitEthernet2/0/3]{lang="IT"}

[  In-band management VLAN, total VLANs(0)]{lang="EN-US"}

[   empty VLAN]{lang="EN-US"}

[  Connect mode: multiple]{lang="EN-US"}

[  MAC address learning: Enabled]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(Extensibility)]{lang="EN-US"}

[  Flow-entry max-limit: 65535 ]{lang="EN-US"}

[  Datapath ID: 0x000100e001000000]{lang="EN-US"}

[Active configuration:]{lang="EN-US"}

[  none]{lang="EN-US"}

[ ]{lang="EN-US"}

[Instance 500 information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Configuration information: ]{lang="EN-US"}

[ Description   : \--]{lang="EN-US"}

[ Active status : active]{lang="EN-US"}

[ Inactive configuration:]{lang="EN-US"}

[  none]{lang="EN-US"}

[ Active configuration:]{lang="EN-US"}

[  Classification: Port]{lang="IT"}

[  In-band management VLAN, total VLANs(0)]{lang="EN-US"}

[   empty VLAN]{lang="EN-US"}

[  Connect mode: multiple]{lang="EN-US"}

[  MAC address learning: Enabled]{lang="EN-US"}

[  Flow table:]{lang="EN-US"}

[   Table ID(type): 0(Extensibility), count: 0]{lang="EN-US"}

[  Flow-entry max-limit: 65535]{lang="EN-US"}

[  Datapath ID: 0x000100e001000000]{lang="EN-US"}

[Port information:]{lang="EN-US"}

[ GigabitEthernet2/0/1]{lang="EN-US"}

[ GigabitEthernet2/0/2]{lang="EN-US"}

[ GigabitEthernet2/0/3]{lang="EN-US"}

[Active channel information:]{lang="EN-US"}

[ Failopen mode: secure]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display openflow instance]{lang="EN-US"}]{#struct_0_x9563_11471_1378410046}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1206011594}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1001629325}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_431090666}

[[Configuration information]{lang="EN-US"}]{#struct_0_x9563_11471_418633741}

[[配置信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1332232160}

[[Description]{lang="EN-US"}]{#struct_0_x9563_11471_x1991777284}

[[实例的描述信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_839398432}

[[Active status]{lang="EN-US"}]{#struct_0_x9563_11471_x445996523}

[[实例状态：]{style="font-family:宋体"}]{#struct_0_x9563_11471_x446062059}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x9563_11471_1774288388}[：]{lang="EN-US" style="font-family:宋体"}[激活]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x9563_11471_964984315}[：未]{style="font-family:
  宋体"}[激活]{lang="EN-US" style="font-family:宋体"}

[[Inactive configuration]{lang="EN-US"}]{#struct_0_x9563_11471_x1002088076}

[[未生效的实例配置]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1601768301}

[[Active configuration]{lang="EN-US"}]{#struct_0_x9563_11471_1285261468}

[[已生效的实例配置]{style="font-family:宋体"}]{#struct_0_x9563_11471_1285458076}

[[Classification: VLAN, total VLANs]{lang="EN-US"}]{#struct_0_x9563_11471_x802013288}

[[实例]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9563_11471_x2121892901}[信息及]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[总个数]{style="font-family:宋体"}

[[Classification: Port]{lang="EN-US"}]{#struct_0_x9563_11471_964984318}

[[实例处于]{style="font-family:宋体"}[Port]{lang="EN-US"}]{#struct_0_x9563_11471_964984323}[模式]{style="font-family:宋体"}

[[loose mode]{lang="EN-US"}]{#struct_0_x9563_11471_x1002153612}

[[处于]{style="font-family:宋体"}[loosen]{lang="EN-US"}]{#struct_0_x9563_11471_727712604}[模式]{style="font-family:宋体"}

[[In-band management VLAN, total VLANs]{lang="EN-US"}]{#struct_0_x9563_11471_x446062058}

[[带内管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9563_11471_x445865450}[列表及]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Connect mode]{lang="EN-US"}]{#struct_0_x9563_11471_x445930986}

[[控制器连接模式：]{style="font-family:宋体"}]{#struct_0_x9563_11471_x445275626}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Single]{lang="EN-US"}]{#struct_0_x9563_11471_x1373667841}[：串行]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Multiple]{lang="EN-US"}]{#struct_0_x9563_11471_x1373667843}[：并行]{lang="EN-US" style="font-family:宋体"}

[[MAC-address learning]{lang="EN-US"}]{#struct_0_x9563_11471_1476579926}

[[MAC]{lang="EN-US"}]{#struct_0_x9563_11471_1476514390}[地址学习：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x9563_11471_202472956}[：允许]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x9563_11471_202472954}[：禁止]{lang="EN-US" style="font-family:宋体"}

[[Flow table]{lang="EN-US"}]{#struct_0_x9563_11471_x330401961}

[[实例的流表信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1002219148}

[[Table ID(type)]{lang="EN-US"}]{#struct_0_x9563_11471_x669748861}

[[流表]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9563_11471_1546484880}[，类型]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MAC-IP]{lang="EN-US"}]{#struct_0_x9563_11471_x385584915}[：]{lang="EN-US" style="font-family:宋体"}[MAC-IP]{lang="EN-US"}[类型流表]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Extensibility]{lang="EN-US"}]{#struct_0_x9563_11471_1416435512}[：]{lang="EN-US" style="font-family:宋体"}[Extensibility]{lang="EN-US"}[类型流表]{lang="EN-US" style="font-family:宋体"}

[[count]{lang="EN-US"}]{#struct_0_x9563_11471_x1002284684}

[[对应流表的流表项总个数]{style="font-family:宋体"}]{#struct_0_x9563_11471_998443863}

[[Flow-entry max-limit]{lang="EN-US"}]{#struct_0_x9563_11471_1476252246}

[[当前实例的流表最大个数限制]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476448854}

[[Datapath ID]{lang="EN-US"}]{#struct_0_x9563_11471_1476383318}

[[当前实例的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}]{#struct_0_x9563_11471_1477104214}

[[Default table-miss]{lang="EN-US"}]{#struct_0_x9563_11471_x179864064}

[[缺省]{style="font-family:宋体"}[table miss]{lang="EN-US"}]{#struct_0_x9563_11471_x179864066}[动作：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x9563_11471_x179864067}[：允许]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_x9563_11471_1776451068}[：丢弃]{lang="EN-US" style="font-family:宋体"}

[[Forbidden port]{lang="EN-US"}]{#struct_0_x9563_11471_1776451066}

[[禁止上送]{style="font-family:宋体"}[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_1776451071}[的端口类型：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VLAN interface]{lang="EN-US"}]{#struct_0_x9563_11471_1776451069}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Virtual Switch Interface]{lang="EN-US"}]{#struct_0_x9563_11471_1776451075}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}

[[Port information]{lang="EN-US"}]{#struct_0_x9563_11471_1477038678}

[[已加入实例的端口的名称列表]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476514391}

[[Active channel information]{lang="EN-US"}]{#struct_0_x9563_11471_1476710999}

[[生效的控制通道信息]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476645463}

[[IP address]{lang="EN-US"}]{#struct_0_x9563_11471_x1059234426}

[[已经配置在实例下的的控制器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9563_11471_x1002350220}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x9563_11471_1760881814}

[[当前连接]{style="font-family:宋体"}[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_x813840545}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Fail-open mode]{lang="EN-US"}]{#struct_0_x9563_11471_1476514388}

[[连接中断时的运行模式：]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476645460}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Standalone]{lang="EN-US"}]{#struct_0_x9563_11471_967147012}[：标准模式]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Secure]{lang="EN-US"}]{#struct_0_x9563_11471_x1371505157}[：安全模式]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1890025421 .myid}
[]{#_Toc404798417}[]{#struct_0_x9563_11471_799445648}[]{#_Toc362963999}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow meter**

------------------------------------------------------------------------

[**[display openflow meter]{lang="EN-US"}**]{#struct_0_x9563_11471_1476317780}[命令用来显示]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例的]{style="font-family:宋体"}[Meter]{lang="EN-US"}[表项]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_377584681}

[**[display openflow instance ]{lang="EN-US"}**[{ *instance-id* \| **oap-instance** } **meter** \[ *meter-id* \]]{lang="EN-US"}]{#struct_0_x9563_11471_1476252244}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1980898947}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476448852}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1476383316}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1560324550}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_1477104212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1138423979}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_1477038676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x296579020}

[*[instance-id]{lang="IT"}*]{#struct_0_x9563_11471_1476579925}[：]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_20414398}[：]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[*[meter-]{lang="IT"}*[id]{lang="EN-US"}]{#struct_0_x9563_11471_1476514389}[：]{style="font-family:宋体"}[Meter ID]{lang="EN-US"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[0xffff0000]{lang="IT"}[。如果未指定本参数，将显示实例所有]{style="font-family:宋体"}[Meter]{lang="EN-US"}[表项]{style="font-family:宋体"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_1178535640}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_1476710997}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[Meter]{lang="EN-US"}[表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow instance 100 meter]{lang="EN-US"}]{#struct_0_x9563_11471_1476645461}

[Meter flags: KBPS  \-- Rate value in kb/s, PKTPS \-- Rate value in packet/sec]{lang="EN-US"}

[             BURST \-- Do burst size,      STATS \-- Collect statistics]{lang="EN-US"}

[ ]{lang="EN-US"}

[Instance 100 meter table information:]{lang="EN-US"}

[ meter entry count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Meter entry 100 information:]{lang="EN-US"}

[ Meter flags: KBPS]{lang="EN-US"}

[ Band 1 information]{lang="EN-US"}

[ Type: drop, rate: 1024, burst size: 65536]{lang="EN-US"}

[ Byte count: \--, packet count: \--]{lang="EN-US"}

[ Referencedinformation:]{lang="EN-US"}

[  Count: 3]{lang="EN-US"}

[  Flow table: 0]{lang="EN-US"}

[  Flow entry: 1, 2, 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[Meter entry 200 information:]{lang="EN-US"}

[ Meter flags: KBPS]{lang="EN-US"}

[ Band 1 information]{lang="EN-US"}

[ Type: drop, rate: 10240, burst size: 655360]{lang="EN-US"}

[ Byte count: \--, packet count: \--]{lang="EN-US"}

[ Referenced information:]{lang="EN-US"}

[  Count: 0]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display openflow meter]{lang="EN-US"}]{#struct_0_x9563_11471_799380112}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1458888989}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_1476317781}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_1476448853}

[[Meter entry count]{lang="EN-US"}]{#struct_0_x9563_11471_1476383317}

[[当前实例包含的]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_1477104213}[表项的总个数]{style="font-family:宋体"}

[[Meter flags]{lang="EN-US"}]{#struct_0_x9563_11471_1477038677}

[[当前]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_1476579922}[表项的所携带的]{style="font-family:宋体"}[flags]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[KBPS]{lang="EN-US"}]{#struct_0_x9563_11471_1476514386}[：速率值以]{style="font-family:宋体"}[kbps]{lang="EN-US"}[为单位]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PKTPS]{lang="EN-US"}]{#struct_0_x9563_11471_1476710994}[：速率值以]{style="font-family:宋体"}[packet/sec]{lang="EN-US"}[（包]{style="font-family:宋体"}[/]{lang="EN-US"}[秒]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}[为单位]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BURST]{lang="EN-US"}]{#struct_0_x9563_11471_1476645458}[：帧大小]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[STATS]{lang="EN-US"}]{#struct_0_x9563_11471_1476252242}[：收集统计信息]{style="font-family:宋体"}

[[Band]{lang="EN-US"}]{#struct_0_x9563_11471_1476448850}

[[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_1476383314}[表项包含的]{style="font-family:宋体"}[band]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x9563_11471_1477104210}

[[band]{lang="EN-US"}]{#struct_0_x9563_11471_1476579923}[类型：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[drop]{lang="EN-US"}]{#struct_0_x9563_11471_1476514387}[：丢弃数据包]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[dscp_remark]{lang="EN-US"}]{#struct_0_x9563_11471_1476645459}[：修改数据包]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[头部的]{style="font-family:宋体"}[dscp]{lang="EN-US"}

[[rate]{lang="EN-US"}]{#struct_0_x9563_11471_1476317779}

[[速率]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476252243}

[[burst size]{lang="EN-US"}]{#struct_0_x9563_11471_1476448851}

[[帧大小]{style="font-family:宋体"}]{#struct_0_x9563_11471_1476383315}

[[Byte count]{lang="EN-US"}]{#struct_0_x9563_11471_1477104211}

[[band]{lang="EN-US"}]{#struct_0_x9563_11471_1477038675}[的字节统计计数，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不支持]{style="font-family:宋体"}

[[packet count]{lang="EN-US"}]{#struct_0_x9563_11471_x1252368965}

[[band]{lang="EN-US"}]{#struct_0_x9563_11471_x1252172357}[的报文统计计数，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不支持]{style="font-family:宋体"}

[[Reference information]{lang="EN-US"}]{#struct_0_x9563_11471_x1252237893}

[[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_x1252565573}[表项]{lang="EN-US" style="font-family:宋体"}[被流表项引用的信息]{style="font-family:宋体"}

[[Count]{lang="EN-US"}]{#struct_0_x9563_11471_x1252631109}

[[引用]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_x1252500037}[表项的流表项的总个数]{style="font-family:宋体"}

[[Flow table]{lang="EN-US"}]{#struct_0_x9563_11471_x1251779141}

[[引用]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_x1251844677}[表项的流表项所在的流表]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Flow entry]{lang="EN-US"}]{#struct_0_x9563_11471_x1252303428}

[[引用]{style="font-family:宋体"}[Meter]{lang="EN-US"}]{#struct_0_x9563_11471_x1252368964}[表项的流表项]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#570150521 .myid}
[]{#_Toc404798418}[]{#struct_0_x9563_11471_20414394}[]{#_Toc384108862}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow oap-context**

------------------------------------------------------------------------

[**[display openflow oap-context]{lang="EN-US"}**]{#struct_0_x9563_11471_20414393}[命令显示]{style="font-family:宋体"}[OAP]{lang="EN-US"}[的]{style="font-family:宋体"}[Context]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_400182575}

[**[display openflow oap-context ]{lang="EN-US"}**[\[ **oap-interface** *oap-interface-type oap-interface-number* \| **in-interface** *in-interface-type in-interface-number* \| **out-interface** *out-interface-type out-interface-number* \]]{lang="EN-US"}]{#struct_0_x9563_11471_x1730390909}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x385425011}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x563901456}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_20414392}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1556132561}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x1290027804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_441880255}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x2012478079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1354804325}

[**[oap-interface]{lang="EN-US"}**[ *oap-interface-type oap-interface-number*]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900735}[：]{lang="EN-US" style="font-family:宋体"}[OAP]{lang="EN-US"}[接口。]{lang="EN-US" style="font-family:宋体"}

[**[in-interface]{lang="EN-US"}**[ *in-interface-type in-interface-number*]{lang="EN-US"}]{#struct_0_x9563_11471_x1201223703}[：入接口。]{lang="EN-US" style="font-family:宋体"}

[**[out-interface]{lang="EN-US"}***[ out-interface-type out-interface-number]{lang="EN-US"}*]{#struct_0_x9563_11471_1476997458}[：出接口。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1934785260}

[[如果未指定任何接口，则显示所有]{style="font-family:宋体"}[OAP Context]{lang="EN-US"}]{#struct_0_x9563_11471_172871097}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x496618633}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_324567436}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[的]{style="font-family:宋体"}[OAP Context]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow oap-context]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900736}

[Total number: 2]{lang="EN-US"}

[ OAP client: 3]{lang="EN-US"}

[  Input interface  : GigabitEthernet1/0/1]{lang="EN-US"}

[  Output interface : GigabitEthernet1/0/2]{lang="EN-US"}

[  OAP interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[  VRF name         : \--]{lang="EN-US"}

[  OAP context      : 0xFFFFFFFFFFFFFFFF]{lang="EN-US"}

[ ]{lang="EN-US"}

[OAP client: 4]{lang="EN-US"}

[  Input interface  : GigabitEthernet1/0/1]{lang="EN-US"}

[  Output interface : GigabitEthernet1/0/2]{lang="EN-US"}

[  OAP interface    : GigabitEthernet1/0/3]{lang="EN-US"}

[  VRF name         : \--]{lang="EN-US"}

[  OAP context      : 0xFFFFFFFFFFFFFFFF]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display openflow instance oap-mode context]{lang="EN-US"}]{#struct_0_x9563_11471_x797939176}[命令显示描述表]{style="font-family:黑体"}

[]{#table_struct_0_1660970071}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1935900737}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1935900738}

[[Total number]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900739}

[[控制器（]{style="font-family:宋体"}[OAP client]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900740}[）的总数]{style="font-family:宋体"}

[[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900741}

[[控制器的编号]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1935900742}

[[Input interface]{lang="EN-US"}]{#struct_0_x9563_11471_x1935900743}

[[入接口的接口名]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1935900744}

[[Output interface]{lang="EN-US"}]{#struct_0_x9563_11471_x746422335}

[[出接口的接口名]{style="font-family:宋体"}]{#struct_0_x9563_11471_x746422336}

[[OAP interface]{lang="EN-US"}]{#struct_0_x9563_11471_x746422337}

[[OAP]{lang="EN-US"}]{#struct_0_x9563_11471_x746422338}[接口的接口名]{style="font-family:宋体"}

[[VRF name]{lang="EN-US"}]{#struct_0_x9563_11471_x746422339}

[[绑定的]{style="font-family:宋体"}[Vpn]{lang="EN-US"}]{#struct_0_x9563_11471_x746422340}[接口索引]{style="font-family:宋体"}

[[OAP context]{lang="EN-US"}]{#struct_0_x9563_11471_x746422341}

[[分配的]{style="font-family:宋体"}[OAP context]{lang="EN-US"}]{#struct_0_x9563_11471_x746422342}

[ ]{lang="EN-US"}

::: {#1243415769 .myid}
[]{#_Toc404798419}[]{#struct_0_x9563_11471_x1252172356}[]{#_Toc362963997}

**OpenFlow \-- OpenFlow配置命令 \-- display openflow summary**

------------------------------------------------------------------------

[**[display openflow summary]{lang="EN-US"}**]{#struct_0_x9563_11471_1445823586}[命令用来显示]{style="font-family:
宋体"}[OpenFlow]{lang="IT"}[实例的概要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1252237892}

[**[display openflow summary]{lang="EN-US"}**]{#struct_0_x9563_11471_x1252565572}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_919808017}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252631108}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_121879322}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1252434500}

[[network-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x1252500036}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1395645668}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9563_11471_x1251779140}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_2107260967}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1251844676}[显示]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display openflow summary]{lang="EN-US"}]{#struct_0_x9563_11471_x1252303431}

[Fail Open mode: Se \-- secure mode, Sa \-- standalone mode]{lang="EN-US"}

[Reactive flags: Y \-- Need active instance,]{lang="EN-US"}

[                N \-- Needn\'t active instance]{lang="EN-US"}

[ ]{lang="EN-US"}

[ID    Status    Datapath-ID         Channel    Table num  Port num  Reactive]{lang="EN-US"}

[1     Active    0x0000000100001221  Connected  2          8         Y]{lang="EN-US"}

[10    Inactive  -                   -          -          -         -]{lang="EN-US"}

[4094  Active    0x00000ffe00001221  Fail(Sa)   2          0         N]{lang="EN-US"}

[OAP   Active    0x0000100200001221  Fail(Sa)   1          8         N]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display openflow summary]{lang="EN-US"}]{#struct_0_x9563_11471_514954713}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1468248698}[[字段]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1252368967}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1252172359}

[[ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1252565575}

[[实例]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1252631111}[或]{style="font-family:宋体"}[OAP]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x9563_11471_x1252434503}

[[实例激活状态]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252500039}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[A]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_x9563_11471_x1251779143}[：实例已经激活]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x9563_11471_x1251844679}[：实例尚未激活]{style="font-family:
  宋体"}

[[Datapath-ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1252303430}

[[实例的]{style="font-family:宋体"}[Datapath ID]{lang="EN-US"}]{#struct_0_x9563_11471_x1252368966}[，未激活实例无取值]{style="font-family:宋体"}

[[Channel]{lang="EN-US"}]{#struct_0_x9563_11471_x1252237894}

[[与控制器连接通道的状态，未激活实例无取值]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252631110}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Connected]{lang="EN-US"}]{#struct_0_x9563_11471_x1252500038}[：与]{style="font-family:
  宋体"}[控制器]{lang="EN-US" style="font-family:宋体"}[已经建立安全通道]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Fail(Se)]{lang="EN-US"}]{#struct_0_x9563_11471_x1251779142}[：连接通道断开，连接中断模式为]{style="font-family:
  宋体"}[Secure]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Fail(Sa)]{lang="EN-US"}]{#struct_0_x9563_11471_x1251844678}[：连接通道断开，连接中断模式为]{style="font-family:
  宋体"}[Standalone]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[Table-num]{lang="EN-US"}]{#struct_0_x9563_11471_x1252303433}

[[实例中流表数目，未激活实例无取值]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252368969}

[[Port-num]{lang="EN-US"}]{#struct_0_x9563_11471_x1252237897}

[[属于该实例的接口数目，未激活实例无取值]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252565577}

[[Reactive]{lang="EN-US"}]{#struct_0_x9563_11471_x1252631113}

[[是否在激活实例后重新更改了配置，需要重新激活]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252434505}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_x9563_11471_x1252500041}[：配置已经改变了，需要重新激活]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x9563_11471_x1251779145}[：配置未改变，不需要重新激活]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1532446382 .myid}
[]{#_Toc404798420}[]{#struct_0_x9563_11471_x489437443}[]{#_Toc348873550}

**OpenFlow \-- OpenFlow配置命令 \-- fail-open mode**

------------------------------------------------------------------------

[**[fail-open mode]{lang="EN-US"}**]{#struct_0_x9563_11471_x1560632641}[命令用来配置交换机与控制器连接中断时的运行模式。]{style="font-family:宋体"}

[**[undo fail-open mode]{lang="EN-US"}**]{#struct_0_x9563_11471_x1143751751}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x253726486}

[**[fail-open mode]{lang="EN-US"}**[ { **secure** \| **standalone** }]{lang="EN-US"}]{#struct_0_x9563_11471_x1616365806}

[**[undo]{lang="EN-US"}**[ **fail-open** **mode**]{lang="EN-US"}]{#struct_0_x9563_11471_829714595}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_x761999319}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x819728022}[实例建立时，缺省为]{style="font-family:宋体"}[Secure]{lang="EN-US"}[模式，且为该实例下发]{style="font-family:宋体"}[Table Miss]{lang="EN-US"}[表项（动作为]{style="font-family:宋体"}[drop]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1002546828}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x513402627}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_534243688}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1927252052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1187484416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1093391485}

[**[secure]{lang="EN-US"}**]{#struct_0_x9563_11471_837725944}[：]{style="font-family:宋体"}[Secure]{lang="EN-US"}[模式，连接断开后，交换机根据流表项转发。]{style="font-family:宋体"}

[**[standalone]{lang="EN-US"}**]{#struct_0_x9563_11471_1594897755}[：]{style="font-family:宋体"}[Standalone]{lang="EN-US"}[模式，连接断开后，交换机正常转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_191089732}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1001563788}[配置交换机与控制器连接中断时的运行模式为]{style="font-family:宋体"}[Standalone]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x187673895}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] fail-open mode standalone]{lang="EN-US"}
:::

::: {#-334951453 .myid}
[]{#_Toc404798421}[]{#struct_0_x9563_11471_x2119184232}[]{#_Toc348873552}

**OpenFlow \-- OpenFlow配置命令 \-- flow-entry max-limit**

------------------------------------------------------------------------

[**[flow-entry max-limit]{lang="EN-US"}**]{#struct_0_x9563_11471_x1889075661}[命令用来配置]{style="font-family:宋体"}[Extensibility]{lang="EN-US"}[表的流表项个数上限。]{style="font-family:宋体"}

[**[undo flow-entry max-limit]{lang="EN-US"}**]{#struct_0_x9563_11471_x281546746}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1083059717}

[**[flow-entry]{lang="EN-US"}**[ **max-limit** *limit-value*]{lang="EN-US"}]{#struct_0_x9563_11471_x828291276}

[**[undo]{lang="EN-US"}**[ **flow-entry** **max-limit**]{lang="EN-US"}]{#struct_0_x9563_11471_x855804598}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_x9563_11471_x1001629324}

[[本命令的缺省情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1134993275}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1529855686}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_886035726}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_639671797}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1293504839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_439868717}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_818788618}

[*[limit-value]{lang="EN-US"}*]{#struct_0_x9563_11471_x1002088079}[：流表项上限值。取值范围和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_770884694}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_942011557}[配置]{style="font-family:宋体"}[Extensibility]{lang="EN-US"}[表的流表项个数上限为]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_863040507}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] flow-entry max-limit 256]{lang="EN-US"}
:::

::::: {#-387907546 .myid}
[]{#_Toc404798422}[]{#struct_0_x9563_11471_x714676427}[]{#_Toc348873556}

**OpenFlow \-- OpenFlow配置命令 \-- flow-table**

------------------------------------------------------------------------

[**[flow-table]{lang="EN-US"}**]{#struct_0_x9563_11471_x1728857070}[命令用来动态配置实例下的流表类型和]{style="font-family:宋体"}[ID]{lang="IT"}[。]{style="font-family:宋体"}

[**[undo flow-table]{lang="IT"}**]{#struct_0_x9563_11471_309662341}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_981594779}

[**[flow-table]{lang="IT"}**[ { ]{lang="EN-US"}]{#struct_0_x9563_11471_x1002153615}**[extensibility ]{lang="IT"}***[extensibility-table-id]{lang="IT"}***[ ]{lang="IT"}**[\| ]{lang="EN-US"}**[mac-ip]{lang="IT"}**[ *mac-ip-table-id*]{lang="IT"}[ }]{lang="EN-US"}[&\<1-n\>]{lang="IT"}

[**[undo flow-table]{lang="IT"}**]{#struct_0_x9563_11471_x1644940391}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1089505785}

[[实例包含了一个]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1751033876}[Extensibility]{lang="IT"}[流表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[为]{style="font-family:
宋体"}[0]{lang="IT"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x68765063}

[[OpenFlow]{lang="IT"}]{#struct_0_x9563_11471_2028553514}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1733920082}

[[network-admin]{lang="IT"}]{#struct_0_x9563_11471_885527547}

[[mdc-admin]{lang="IT"}]{#struct_0_x9563_11471_2006382548}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1002219151}

[**[extensibility ]{lang="IT"}**]{#struct_0_x9563_11471_1702969670}*[extensibility-table-id]{lang="IT"}*[：]{style="font-family:宋体"}[Extensibility]{lang="IT"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[，取值范围为]{style="font-family:
宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[254]{lang="IT"}[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[**[mac-ip]{lang="IT"}**]{#struct_0_x9563_11471_1767849018}[ *mac-ip-table-id*]{lang="IT"}[：]{style="font-family:宋体"}[MAC-IP]{lang="IT"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[，取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[254]{lang="IT"}[。]{style="font-family:
宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[&\<1-n\>]{lang="IT"}]{#struct_0_x9563_11471_1921458823}[：表示前面的参数最多可以输入]{style="font-family:宋体"}[n]{lang="IT"}[次，]{style="font-family:宋体"}[n]{lang="IT"}[的取值范围和设备的型号有关，请以设备的实际情况为准。需要注意的是，对于]{style="font-family:
宋体"}[MAC-IP]{lang="IT"}[流表，只能输入一次。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OpenFlow命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x9563_11471_1743111608}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[有的产品只支持先输入]{style="font-family:KaiTi_GB2312"}]{#struct_0_x9563_11471_1743111609}**[mac-ip]{lang="IT"}**[后输入]{style="font-family:KaiTi_GB2312"}**[extensibility]{lang="IT"}**[，不支持先输入]{style="font-family:KaiTi_GB2312"}**[extensibility]{lang="IT"}**[后输入]{style="font-family:KaiTi_GB2312"}**[mac-ip]{lang="IT"}**[。具体和设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x935667658}

[[用户激活实例之前配置当前实例将要使用的流表类型以及与之对应的流表]{style="font-family:宋体"}]{#struct_0_x9563_11471_x667056889}[ID]{lang="IT"}[。]{style="font-family:宋体"}

[[多次配置本命令，新配置将覆盖旧配置]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1252500040}[。]{style="font-family:
宋体"}

[[输入的]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1251779144}[Extensibility]{lang="IT"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[要大于]{style="font-family:
宋体"}[MAC-IP]{lang="IT"}[流表]{style="font-family:宋体"}[ID]{lang="IT"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_495639545}

[[\# ]{lang="IT"}]{#struct_0_x9563_11471_1306314979}[配置实例]{style="font-family:宋体"}[1]{lang="IT"}[流表类型为]{style="font-family:
宋体"}[MAC-IP]{lang="IT"}[表]{style="font-family:宋体"}[ID]{lang="IT"}[为]{style="font-family:宋体"}[0]{lang="IT"}[，]{style="font-family:宋体"}[Extensibility]{lang="IT"}[表]{style="font-family:宋体"}[ID]{lang="IT"}[为]{style="font-family:
宋体"}[1]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x1002284687}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] flow-table mac-ip 0 extensibility 1]{lang="EN-US"}
:::::

::::: {#1175827259 .myid}
[]{#_Toc404798423}[]{#struct_0_x9563_11471_933807550}[]{#_Toc381014869}

**OpenFlow \-- OpenFlow配置命令 \-- forbidden port**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OpenFlow命令.files/image002.png){border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_x9563_11471_x1956385892}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x9563_11471_933807551}
:::

[ ]{lang="EN-US"}

[**[forbidden port]{lang="EN-US"}**]{#struct_0_x9563_11471_933807548}[命令用来配置禁止上送]{style="font-family:宋体"}[Controller]{lang="EN-US"}[的端口类型。]{style="font-family:宋体"}

[**[undo forbidden port]{lang="EN-US"}**]{#struct_0_x9563_11471_x70748}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_933807549}

[**[forbidden port ]{lang="EN-US"}**[{ **vlan-interface** \| **vsi-interface** } \*]{lang="EN-US"}]{#struct_0_x9563_11471_x70749}

[**[undo forbidden port]{lang="EN-US"}**]{#struct_0_x9563_11471_933807546}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x70750}

[[所有接口都上送]{style="font-family:宋体"}[Controller]{lang="EN-US"}]{#struct_0_x9563_11471_933807547}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x70751}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_933807544}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x70752}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_933807545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1404844608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x395427599}

[**[vlan-interface]{lang="EN-US"}**]{#struct_0_x9563_11471_x1404844607}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[vsi-interface]{lang="EN-US"}**]{#struct_0_x9563_11471_x1404844610}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x751592423}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1576859339}[配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[禁止上送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x1404844612}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] forbidden port vlan-interface]{lang="EN-US"}
:::::

::: {#-60448219 .myid}
[]{#_Toc404798424}[]{#struct_0_x9563_11471_313452832}[]{#_Toc362964003}

**OpenFlow \-- OpenFlow配置命令 \-- in-band management vlan**

------------------------------------------------------------------------

[**[in-band management vlan]{lang="EN-US"}**]{#struct_0_x9563_11471_x1179274792}[命令用来配置带内管理]{style="font-family:宋体"}[VLAN]{lang="IT"}[。]{style="font-family:宋体"}

[**[undo in-band management vlan]{lang="EN-US"}**]{#struct_0_x9563_11471_313649440}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x513787215}

[**[in-band management vlan ]{lang="EN-US"}**[{ *vlan-id* \[ **to** *vlan-id* \] } &\<1-10\>]{lang="EN-US"}]{#struct_0_x9563_11471_313583904}

[**[undo in-bandmanagement vlan]{lang="EN-US"}**]{#struct_0_x9563_11471_314304800}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_76341292}

[[没有配置带内管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x9563_11471_313780513}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_313714977}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_313911585}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1078606472}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_313846049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_313518369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1146454286}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x9563_11471_313452833}[：]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1179274791}

[[缺省情况下]{style="font-family:宋体"}]{#struct_0_x9563_11471_314239265}[，]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例内的]{style="font-family:宋体"}[VLAN]{lang="IT"}[都是进行]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[转发的]{style="font-family:宋体"}[，]{style="font-family:宋体"}[实例无法通过这些]{style="font-family:宋体"}[VLAN]{lang="IT"}[与控制器建立连接。配置带内管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[后，这些]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内流量是正常转发的，可以用于实例与控制器建立连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_313780510}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_313911582}[在实例]{style="font-family:宋体"}[1]{lang="EN-US"}[中配置]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[为带内管理]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x1078606475}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] in-band management vlan 10]{lang="EN-US"}
:::

::: {#-799172938 .myid}
[]{#_Toc404798425}[]{#struct_0_x9563_11471_x364085313}[]{#_Toc384108868}

**OpenFlow \-- OpenFlow配置命令 \-- listening port**

------------------------------------------------------------------------

[**[listening prot]{lang="EN-US"}**]{#struct_0_x9563_11471_1489332070}[命令用来为]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例启动]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo listening port]{lang="EN-US"}**]{#struct_0_x9563_11471_x364085314}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1489397606}

[**[listening port ]{lang="EN-US"}***[port-number]{lang="EN-US"}***[ ssl ]{lang="EN-US"}***[ssl-policy-name]{lang="EN-US"}*]{#struct_0_x9563_11471_x1190800026}

[**[undo listening port]{lang="EN-US"}**]{#struct_0_x9563_11471_x406066520}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x52110922}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x1369695671}[实例下没有启动]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x364085315}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1489463142}[实例视图]{style="font-family:宋体"}[/OpenFlow OAP]{lang="EN-US"}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1154350513}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1574574622}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1250225836}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1594484188}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x9563_11471_1380344681}[：服务器的端口号，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[65535]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[ssl ]{lang="EN-US"}**]{#struct_0_x9563_11471_x1451406855}*[ssl-policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x364085316}

[[没有启动]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_1489528678}[服务器时，设备作为]{style="font-family:宋体"}[TCP/SSL]{lang="EN-US"}[客户端主动连接控制器（]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器，需要相应配置）；启动]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器之后，设备作为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端被动等待控制器（]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端）连接。]{style="font-family:宋体"}

[[一个实例只能启动一个]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x9563_11471_x1128607246}[服务器。必须先删掉已有配置才能进行新的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_883289106}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1466844397}[为]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[启动端口号为]{style="font-family:宋体"}[20000]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_887605734}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] listening port 20000 ssl ssl_name]{lang="EN-US"}
:::

::: {#1727447375 .myid}
[]{#_Toc404798426}[]{#struct_0_x9563_11471_x567640078}[]{#_Toc348873555}

**OpenFlow \-- OpenFlow配置命令 \-- mac-ip dynamic-mac aware**

------------------------------------------------------------------------

[**[mac-ip dynamic-mac aware]{lang="EN-US"}**]{#struct_0_x9563_11471_x292216440}[命令用来配置支持动态]{style="font-family:
宋体"}[MAC]{lang="IT"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo mac-ip dynamic-mac aware]{lang="EN-US"}**]{#struct_0_x9563_11471_x461107531}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x2074980099}

[**[mac-ip dynamic-mac aware]{lang="EN-US"}**]{#struct_0_x9563_11471_187441865}

[**[undo mac-ip dynamic-mac aware]{lang="EN-US"}**]{#struct_0_x9563_11471_973967270}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_447159222}

[[不支持动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x9563_11471_1936918879}[地址，即忽略控制器下发的此类消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1002350223}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x968001541}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_302617847}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1082511390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x865539213}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1115426583}

[[此功能仅在支持]{style="font-family:宋体"}]{#struct_0_x9563_11471_x58788625}[MAC-IP]{lang="IT"}[流表情况下]{style="font-family:宋体"}[，]{style="font-family:宋体"}[决定是否支持控制器在查询或者删除流表项时包含动态]{style="font-family:宋体"}[MAC]{lang="IT"}[地址]{style="font-family:宋体"}[（]{style="font-family:宋体"}[动态]{style="font-family:宋体"}[MAC]{lang="IT"}[表项变化不需要上报控制器]{style="font-family:
宋体"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_x434098528}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_x1002415759}[配置实例]{style="font-family:宋体"}[1]{lang="EN-US"}[支持动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1510663704}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] mac-ip dynamic-mac aware]{lang="EN-US"}
:::

::: {#-666783653 .myid}
[]{#_Toc404798427}[]{#struct_0_x9563_11471_314304798}[]{#_Toc362964005}

**OpenFlow \-- OpenFlow配置命令 \-- mac-learning forbidden**

------------------------------------------------------------------------

[**[mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x9563_11471_x612436907}[命令用来在实例配置的]{style="font-family:宋体"}[VLAN]{lang="IT"}[上禁止]{style="font-family:宋体"}[MAC]{lang="IT"}[地址学习]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x9563_11471_314239262}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_313780511}

[**[mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x9563_11471_x1247558615}

[**[undo mac-learning forbidden]{lang="EN-US"}**]{#struct_0_x9563_11471_313714975}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_278609084}

[[实例配置的]{style="font-family:宋体"}]{#struct_0_x9563_11471_313911583}[VLAN]{lang="IT"}[上]{style="font-family:宋体"}[允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_313846047}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_895683870}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_313518367}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_313452831}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1179274793}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_313649439}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_313583903}[配置实例]{style="font-family:宋体"}[1]{lang="EN-US"}[禁止]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x787661973}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] mac-learning forbidden]{lang="EN-US"}
:::

::: {#139248904 .myid}
[]{#_Toc404798428}[]{#struct_0_x9563_11471_1870898961}[]{#_Toc348873547}

**OpenFlow \-- OpenFlow配置命令 \-- openflow instance**

------------------------------------------------------------------------

[**[openflow instance]{lang="EN-US"}**]{#struct_0_x9563_11471_883789613}[命令用来创建]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[**[undo openflow instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x919845259}[命令用来删除]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1093324563}

[**[openflow instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_x9563_11471_x57003920}

[**[undo openflow instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_x9563_11471_242804775}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1002481295}

[[没有配置]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1883215552}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1546928450}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_70104298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_748889307}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_377547354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1729733031}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_305631564}

[*[instance-id]{lang="SV" style="color:black"}*]{#struct_0_x9563_11471_1383716131}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1002546831}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_1408846138}[创建]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_x214889447}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\]]{lang="EN-US"}
:::

::: {#-36456422 .myid}
[]{#_Toc404798429}[]{#struct_0_x9563_11471_1974566848}[]{#_Toc384108872}

**OpenFlow \-- OpenFlow配置命令 \-- openflow instance oap-instance**

------------------------------------------------------------------------

[**[openflow instance]{lang="EN-US"}**[ **oap-instance**]{lang="EN-US"}]{#struct_0_x9563_11471_x1606946814}[命令用来创建]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[**[undo openflow instance oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x377022337}[命令用来删除]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1974566847}

[**[openflow instance oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_x1607012350}

[**[undo openflow instance oap-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_415431062}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_896667629}

[[没有配置]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}]{#struct_0_x9563_11471_x730978114}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1779398706}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1319158270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1974566846}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1607077886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x292847789}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x475161780}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_1324387673}[创建]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[OpenFlow OAP]{lang="EN-US"}[实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1286586215}

[\[Sysname\] openflow instance oap-instance]{lang="EN-US"}

[\[Sysname-of-inst-oap\]]{lang="EN-US"}
:::

::::: {#-262067582 .myid}
[]{#_Toc404798430}[]{#struct_0_x9563_11471_2035413277}[]{#_Toc392924131}

**OpenFlow \-- OpenFlow配置命令 \-- openflow lossless enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OpenFlow命令.files/image002.png){#图片 1 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_x9563_11471_609910200}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x9563_11471_37245329}
:::

[ ]{lang="EN-US"}

[**[openflow lossless enable]{lang="EN-US"}**]{#struct_0_x9563_11471_1257901340}[命令用来开启]{style="font-family:
宋体"}[OpenFlow]{lang="EN-US"}[的无丢包模式。]{style="font-family:宋体"}

[**[undo openflow lossless enable]{lang="EN-US"}**]{#struct_0_x9563_11471_483569491}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_415182451}

[**[openflow lossless enable]{lang="EN-US"}**]{#struct_0_x9563_11471_x364692421}

[**[undo openflow lossless enable]{lang="EN-US"}**]{#struct_0_x9563_11471_696453818}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1416532130}

[[没有开启]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x1849091253}[的无丢包模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1946793370}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x693470078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x348248533}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1877849473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1862198639}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1711447346}

[[在某些设备的]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_918448250}[场景中，]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[的流表下发过程中设备可能会出现丢包，从而引发很多问题，比如流量误上送]{style="font-family:宋体"}[Controller]{lang="EN-US"}[，导致误下发]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[表项等，此时需要]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[的无丢包模式]{style="font-family:宋体"}[。在无丢包模式下，设备不会丢包，]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[在实际网络中可以正常使用，但是匹配能力会受限制，比如不能匹配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[在非]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x40326304}[场景中，请不要]{style="font-family:宋体"}[开启]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[的无丢包模式]{style="font-family:宋体"}[，否则会影响转发效率和能力级匹配。]{style="font-family:宋体"}

[[不同设备的]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1788116001}[场景是否需要使用此配置不同，请根据实际需要配置。]{style="font-family:宋体"}

[[要使配置生效，必须在配置后重启设备。在重启设备前，请保存当前配置。]{style="font-family:宋体"}]{#struct_0_x9563_11471_x366387064}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_963662118}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_462274013}[开启]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[的无丢包模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_872613863}

[\[Sysname\] openflow lossless enable]{lang="EN-US"}

[ Enable lossless traffic function? \[Y/N\]:y]{lang="EN-US"}

[ For the setting to take effect, save the configuration, and then reboot the device.]{lang="EN-US"}
:::::

::: {#139260955 .myid}
[]{#_Toc404798431}[]{#struct_0_x9563_11471_1745274301}[]{#_Toc391545529}

**OpenFlow \-- OpenFlow配置命令 \-- openflow-instance**

------------------------------------------------------------------------

[**[openflow-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_1745274298}[命令用来在接口下绑定]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo openflow-instance]{lang="EN-US"}**]{#struct_0_x9563_11471_1905422756}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1745274299}

[**[openflow-instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_x9563_11471_1905357220}

[**[undo openflow-instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_x9563_11471_1745274296}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1745274297}

[[接口下没有绑定]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1905750436}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_935970240}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_96164226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_935970241}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_935970238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_x1095476854}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_935970239}

[*[instance-id]{lang="SV" style="color:black"}*]{#struct_0_x9563_11471_x1095476853}[：]{style="font-family:宋体"}[OpenFlow]{lang="EN-US"}[实例号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_935970236}

[[\# OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_935970237}[实例]{style="font-family:宋体"}[1]{lang="EN-US"}[已存在，且为接口模式，配置接口]{style="font-family:宋体"}[GigabitEthernet]{lang="EN-US"}[1/0/1]{lang="EN-US"}[下绑定实例]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_935970234}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] openflow-instance 1]{lang="EN-US"}
:::

::: {#1212291552 .myid}
[]{#_Toc404798432}[]{#struct_0_x9563_11471_x1095476858}[]{#_Toc391545530}

**OpenFlow \-- OpenFlow配置命令 \-- port**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_x9563_11471_935970235}[命令用来在实例下绑定接口。]{style="font-family:宋体"}

[**[undo port]{lang="EN-US"}**]{#struct_0_x9563_11471_x1095476857}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_935970232}

[**[port]{lang="EN-US"}**[ *interface-type interface-number1* \[ **to** *interface-type interface-number2* \]]{lang="EN-US"}]{#struct_0_x9563_11471_x1402681928}

[**[undo port]{lang="EN-US"}***[ interface-type interface-number1]{lang="EN-US"}*[ \[ **to** *interface-type interface-number2* \]]{lang="EN-US"}]{#struct_0_x9563_11471_1529043492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1402681927}

[[实例下没有绑定接口。]{style="font-family:宋体"}]{#struct_0_x9563_11471_164808128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x215366210}

[[OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_1740948929}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x590616696}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1740948926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1740948927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x590747768}

[*[interface-type interface-number1 ]{lang="EN-US"}*[\[ **to** *interface-type interface-number2* \]]{lang="EN-US"}]{#struct_0_x9563_11471_1740948924}[：接口类型和编号，]{style="font-family:宋体"}*[interface-number2]{lang="EN-US"}*[的值要大于或等于]{style="font-family:宋体"}*[interface-number1]{lang="EN-US"}*[的值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1740948925}

[[\# OpenFlow]{lang="EN-US"}]{#struct_0_x9563_11471_x590878840}[实例下绑定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[到]{style="font-family:宋体"}[GigabitEthernet1/0/3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9563_11471_1740948922}

[\[Sysname\] openflow instance 1]{lang="EN-US"}

[\[Sysname-of-inst-1\] port gigabitethernet 1/0/1 to gigabitethernet 1/0/3]{lang="EN-US"}
:::

::: {#-925099402 .myid}
[]{#_Toc396293583}[]{#_Toc404798433}[]{#struct_0_x9563_11471_1110163353}

**OpenFlow \-- OpenFlow配置命令 \-- reset openflow instance controller statistics**

------------------------------------------------------------------------

[**[reset openflow instance controller statistics]{lang="EN-US"}**]{#struct_0_x9563_11471_x1390762182}[命令用来清除控制器发送和接收报文的统计计数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1214561235}

[**[reset openflow instance]{lang="EN-US"}**[ { *instance-id* { **controller** \[ *controller-id* \] \| **listened** } \| **[oap-instance]{style="color:black"}** **listened** } **statistics**]{lang="EN-US"}]{#struct_0_x9563_11471_x1964535834}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9563_11471_397773148}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9563_11471_x1703692283}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9563_11471_x1988733939}

[[network-admin]{lang="EN-US"}]{#struct_0_x9563_11471_273600061}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9563_11471_1110097817}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9563_11471_1724938687}

[*[instance-id]{lang="IT"}*]{#struct_0_x9563_11471_x201992296}[：]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例号，取值范围为]{style="font-family:宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[4094]{lang="IT"}[。]{style="font-family:
宋体"}

[*[controller-id]{lang="IT"}*]{#struct_0_x9563_11471_x703854438}[：控制器的]{style="font-family:宋体"}[ID]{lang="IT"}[号，取值范围为]{style="font-family:宋体"}[0]{lang="IT"}[～]{style="font-family:宋体"}[63]{lang="IT"}[。如果未指定本参数，清除实例下所有控制器发送和接收报文的统计计数。]{style="font-family:
宋体"}

[**[listened]{lang="IT" style="font-size:9.5pt;color:black"}**]{#struct_0_x9563_11471_x1349794732}[：]{style="font-size:9.5pt;font-family:宋体;color:black"}[实例启动的服务端连接的客户端。]{style="font-size:9.5pt;font-family:宋体;color:black"}

[**[oap-instance]{lang="IT" style="font-size:9.5pt;color:black"}**]{#struct_0_x9563_11471_x380621909}[：]{style="font-size:9.5pt;font-family:宋体;color:black"}[OpenFlow OAP]{lang="IT" style="font-size:9.5pt;color:black"}[实例。]{style="font-size:
9.5pt;font-family:宋体;color:black"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x9563_11471_895728071}

[[\# ]{lang="IT"}]{#struct_0_x9563_11471_x1398325539}[清除]{style="font-family:宋体"}[OpenFlow]{lang="IT"}[实例]{style="font-family:宋体"}[1]{lang="IT"}[对应的所有]{style="font-family:
宋体"}[控制器发送和接收报文的统计计数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset openflow instance 1 controller statistics]{lang="EN-US"}]{#struct_0_x9563_11471_835556892}

[[\# ]{lang="EN-US"}]{#struct_0_x9563_11471_1945297711}[清除]{style="font-family:宋体"}[OAP]{lang="EN-US"}[实例]{style="font-family:宋体"}[启动的服务端连接的客户端]{style="font-size:9.5pt;font-family:宋体;
color:black"}[发送和接收报文的统计计数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset openflow instance oap-instance listened statistics]{lang="EN-US"}]{#struct_0_x9563_11471_x1436746480}

[ ]{lang="EN-US"}
:::
