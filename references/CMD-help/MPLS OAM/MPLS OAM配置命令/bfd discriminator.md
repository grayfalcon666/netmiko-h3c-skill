::: {#1677447108 .myid}
[]{#_Toc404791711}[]{#struct_0_x1562_10515_x796291149}

**MPLS OAM \-- MPLS OAM配置命令 \-- bfd discriminator**

------------------------------------------------------------------------

[**[bfd discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x1196773149}[命令用来配置检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符和远端标识符。]{style="font-family:宋体"}

[**[undo bfd ]{lang="EN-US"}[discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x1004009881}[命令]{style="font-family:宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1986695108}

[**[bfd discriminator local]{lang="EN-US"}**[ *local-id* **remote** *remote-id* ]{lang="EN-US"}]{#struct_0_x1562_10515_541285468}

[**[undo bfd discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x1603222243}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_157044455}

[[没有指定检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x973601045}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符和远端标识符，系统自动为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话分配本地标识符和远端标识符。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1479569878}

[[VSI LDP PW]{lang="EN-US"}]{#struct_0_x1562_10515_1987945981}[视图]{style="font-family:宋体"}

[[VSI static PW]{lang="EN-US"}]{#struct_0_x1562_10515_x469451430}[视图]{style="font-family:宋体"}

[[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1816619552}[视图]{style="font-family:宋体"}

[[VSI LDP]{lang="EN-US"}]{#struct_0_x1562_10515_x566618747}[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[VSI static]{lang="EN-US"}]{#struct_0_x1562_10515_x1986891716}[备份]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[交叉连接备份]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1526215088}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1533558473}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x2138982068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1120582990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1464736231}

[**[local]{lang="EN-US"}***[ local-id]{lang="EN-US"}*]{#struct_0_x1562_10515_1082645190}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}***[ remote-id]{lang="EN-US"}*]{#struct_0_x1562_10515_1071103550}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的远端标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_321104264}

[[可以通过两种方式配置检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1986826180}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态方式：如果通过]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1858988511}**[bfd]{lang="EN-US"}**[ **discriminator**]{lang="EN-US"}[命令指定了本地和远端的标识符，则根据指定的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。采用这种方式时，要求本地和远端设备上都通过本命令手工指定标识符，并要求两端配置的本地和远端标识符匹配（即本地]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置的本地标识符与远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置的远端标识符相同；本地]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置的远端标识符与远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[上配置的本地标识符相同），否则无法建立检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态方式：如果没有通过]{style="font-family:宋体"}]{#struct_0_x1562_10515_1924319000}**[bfd]{lang="EN-US"}**[ **discriminator**]{lang="EN-US"}[命令指定本地和远端的标识符，则自动运行]{style="font-family:宋体"}[MPLS Ping]{lang="EN-US"}[来协商标识符，并根据协商好的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1214362250}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x992633515}[在]{style="font-family:宋体"}[VSI LDP PW]{lang="EN-US"}[视图下，配置检测该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符和远端标识符均为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_1555024021}

[\[Sysname\] vsi ttt]{lang="EN-US"}

[\[Sysname-vsi-ttt\] pwsignaling ldp  ]{lang="EN-US"}

[\[Sysname-vsi-ttt-ldp\] peer 22.22.2.2 pw-id 1 pw-class ttt]{lang="EN-US"}

[\[Sysname-vsi-ttt-ldp-22.22.2.2-1\] bfd discriminator local 1 remote 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1303031130}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1548018751}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x1986498500}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x1292060792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_x558397984}
:::

::: {#-2020907342 .myid}
[]{#_Toc404791712}[]{#struct_0_x1562_10515_x1271086590}

**MPLS OAM \-- MPLS OAM配置命令 \-- display l2vpn pw bfd**

------------------------------------------------------------------------

[**[display l2vpn pw bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_2117344086}[命令用来显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_157665909}

[**[display l2vpn pw bfd ]{lang="EN-US"}**[\[ **peer** *peer-ip* **pw-id** *pw-id* \]]{lang="EN-US"}]{#struct_0_x1562_10515_1432820570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2028147736}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_x972639648}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1986432964}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1525070298}

[[network-operator]{lang="EN-US"}]{#struct_0_x1562_10515_384971736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1139739534}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1562_10515_x1747547957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1066213947}

[**[peer]{lang="EN-US"}**[ *peer-ip* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_x1562_10515_x817884683}[：显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}*[peer-ip]{lang="EN-US"}*[为远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果不指定本参数，则显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x257972843}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_1998850484}[显示所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn pw bfd]{lang="EN-US"}]{#struct_0_x1562_10515_x420938844}

[ Total number of sessions: 1, 1 up, 0 down, 0 init]{lang="EN-US"}

[ ]{lang="EN-US"}

[ FEC Type: PW FEC-128]{lang="EN-US"}

[ FEC Info:]{lang="EN-US"}

[   Peer IP: 22.22.2.2]{lang="EN-US"}

[   PW ID: 1]{lang="EN-US"}

[ VSI Index: 0                        Link ID: 8]{lang="EN-US"}

[ Local Discr: 514                    Remote Discr: 514]{lang="EN-US"}

[ Source IP: 11.11.1.1                Destination IP: 127.0.0.2]{lang="EN-US"}

[ Session State: Up                   Session Role: Active]{lang="EN-US"}

[ Template Name: -]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display l2vpn pw bfd]{lang="EN-US"}]{#struct_0_x1562_10515_2001970833}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1046727865}[[字段]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1305864675}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1562_10515_177358848}

[[Total number of sessions]{lang="EN-US"}]{#struct_0_x1562_10515_747933587}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x420873308}[会话总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[和]{style="font-family:宋体"}[init]{lang="EN-US"}[状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[FEC Type]{lang="EN-US"}]{#struct_0_x1562_10515_441540525}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_1768509052}[检测的]{style="font-family:宋体"}[FEC]{lang="EN-US"}[类型，取值为]{style="font-family:宋体"}[PW FEC-128]{lang="EN-US"}

[[FEC Info]{lang="EN-US"}]{#struct_0_x1562_10515_1743790822}

[[FEC]{lang="EN-US"}]{#struct_0_x1562_10515_2080129906}[相关信息]{style="font-family:宋体"}

[[Peer IP]{lang="EN-US"}]{#struct_0_x1562_10515_891828819}

[[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_x1562_10515_x421069916}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}

[[PW ID]{lang="EN-US"}]{#struct_0_x1562_10515_x1107420698}

[[PW ID]{lang="EN-US"}]{#struct_0_x1562_10515_330578993}

[[VSI Index]{lang="EN-US"}]{#struct_0_x1562_10515_x381733635}

[[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x681979787}[所属]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的索引，当]{style="font-family:宋体"}[PW]{lang="EN-US"}[为]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[时显示该信息]{style="font-family:宋体"}

[[本字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x1562_10515_2027099417}

[[Connection ID]{lang="EN-US"}]{#struct_0_x1562_10515_x421004380}

[[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x316199424}[所属交叉连接的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，当]{style="font-family:宋体"}[PW]{lang="EN-US"}[为]{style="font-family:宋体"}[VPWS]{lang="EN-US"}[的]{style="font-family:宋体"}[PW]{lang="EN-US"}[时显示该信息]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_x1562_10515_x420478379}

[[PW]{lang="EN-US"}]{#struct_0_x1562_10515_1201120821}[对应的]{style="font-family:宋体"}[Link ID]{lang="EN-US"}

[[Local Discr]{lang="EN-US"}]{#struct_0_x1562_10515_x1429265463}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_68365997}[会话的本地标识符]{style="font-family:宋体"}

[[Remote Discr]{lang="EN-US"}]{#struct_0_x1562_10515_x420676700}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1082124188}[会话的远端标识符]{style="font-family:宋体"}

[[Source IP]{lang="EN-US"}]{#struct_0_x1562_10515_x211471662}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1717674488}[会话的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为本端设备的]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}

[[Destination IP]{lang="EN-US"}]{#struct_0_x1562_10515_x420611164}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x342460873}[会话的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址]{style="font-family:宋体"}

[[Session State]{lang="EN-US"}]{#struct_0_x1562_10515_1575031123}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x38944659}[会话状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x1562_10515_1906650663}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1562_10515_x420807772}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1562_10515_1644334398}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Session Role]{lang="EN-US"}]{#struct_0_x1562_10515_x1370263165}

[[本端设备在]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1821257059}[会话中的角色，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1562_10515_773104626}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的发起端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_x1562_10515_x420742236}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的接收端]{lang="EN-US" style="font-family:宋体"}

[[Template Name]{lang="EN-US"}]{#struct_0_x1562_10515_x324015436}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_516465316}[会话参数的模板名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_854761825}

[]{#_Toc275248925}[]{#_Toc67195986}[]{#_Toc67145811}[]{#_Toc61012174}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[bfd discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x49413617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x1530982701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_x420414556}

::: {#1056699700 .myid}
[]{#_Toc404791713}[]{#struct_0_x1562_10515_x1866518801}

**MPLS OAM \-- MPLS OAM配置命令 \-- display mpls bfd**

------------------------------------------------------------------------

[**[display mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1089273536}[命令用来显示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道或]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1653406954}

[**[display mpls bfd ]{lang="EN-US"}**[\[ **ipv4** *dest-addr* *mask-length* \| **te tunnel** *tunnel-number* \]]{lang="EN-US"}]{#struct_0_x1562_10515_1920756876}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1056066128}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_x164992655}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_455019228}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1869142402}

[[network-operator]{lang="EN-US"}]{#struct_0_x1562_10515_x420349020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1980504684}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1562_10515_x821671613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1501333964}

[**[ipv4 ]{lang="EN-US"}***[dest-addr]{lang="EN-US"}*[ *mask-length*]{lang="EN-US"}]{#struct_0_x1562_10515_x673775501}**[：]{style="font-family:宋体"}**[显示指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[te tunnel ]{lang="EN-US"}***[tunnel-number]{lang="EN-US"}*]{#struct_0_x1562_10515_x1431150478}**[：]{style="font-family:宋体"}**[显示指定]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}*[tunnel-number]{lang="EN-US"}*[为隧道接口的编号，取值范围为设备上已经创建的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2138205983}

[[执行本命令时如果没有指定任何参数，则显示所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1562_10515_481280345}[隧道和]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1163497702}

[]{#struct_0_x1562_10515_x420938843}[]{#_Toc293393940}[]{#_Toc293393941}[]{#_Toc293393942}[]{#_Toc293393943}[]{#_Toc293393944}[]{#_Toc293393945}[]{#_Toc293393946}[]{#_Toc293393947}[]{#_Toc293393948}[]{#_Toc293393949}[]{#_Toc293393950}[]{#_Toc293393951}[]{#_Toc293393952}[]{#_Toc293393953}[]{#_Toc293393954}[]{#_Toc293393955}[]{#_Toc293393958}[]{#_Toc293393959}[]{#_Toc293393975}[]{#_Toc293393976}[]{#_Toc293393978}[]{#_Toc293393979}[]{#_Toc293393980}[]{#_Toc293393981}[]{#_Toc293393994}[\# ]{lang="EN-US"}[显示目的地址为]{style="font-family:
宋体"}[22.22.2.2/32]{lang="EN-US"}[的]{style="font-family:
宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[]{#_Toc137974527}[[\<Sysname\> display mpls bfd ipv4 22.22.2.2 32]{lang="EN-US"}]{#struct_0_x1562_10515_2002167441}

[ Total number of sessions: 1, 1 up, 0 down, 0 init]{lang="EN-US"}

[ ]{lang="EN-US"}

[ FEC Type: LSP]{lang="EN-US"}

[ FEC Info:]{lang="EN-US"}

[   Destination: 22.22.2.2]{lang="EN-US"}

[   Mask Length: 32]{lang="EN-US"}

[ NHLFE ID: 1025]{lang="EN-US"}

[ Local Discr: 513                    Remote Discr: 513]{lang="EN-US"}

[ Source IP: 11.11.1.1                Destination IP: 127.0.0.1]{lang="EN-US"}

[ Session State: Up                   Session Role: Passive]{lang="EN-US"}

[ Template Name: -]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x1458670379}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测信息。]{style="font-family:宋体"}

[[\<Sysname\> display mpls bfd te tunnel 1]{lang="EN-US"}]{#struct_0_x1562_10515_x420873307}

[ Total number of sessions: 1, 1 up, 0 down, 0 init]{lang="EN-US"}

[ ]{lang="EN-US"}

[ FEC Type: TE Tunnel]{lang="EN-US"}

[ FEC Info:]{lang="EN-US"}

[   Source     : 100.1.1.1]{lang="EN-US"}

[   Destination: 200.1.1.1]{lang="EN-US"}

[   Tunnel ID  : 1]{lang="EN-US"}

[   LSP ID     : 100]{lang="EN-US"}

[ NHLFE ID: 1025]{lang="EN-US"}

[ Local Discr: 513                    Remote Discr: 513]{lang="EN-US"}

[ Source IP: 11.11.1.1                Destination IP: 127.0.0.1]{lang="EN-US"}

[ Session State: Up                   Session Role: Passive]{lang="EN-US"}

[ Template Name: -]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mpls bfd]{lang="EN-US"}]{#struct_0_x1562_10515_442261421}[命令]{style="font-family:黑体"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1070767775}[[字段]{style="font-family:黑体"}]{#struct_0_x1562_10515_1505250616}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1562_10515_1428562988}

[[Total number of sessions]{lang="EN-US"}]{#struct_0_x1562_10515_1027808379}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1605773387}[会话总数，及处于]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[和]{style="font-family:宋体"}[init]{lang="EN-US"}[状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[FEC Type]{lang="EN-US"}]{#struct_0_x1562_10515_x421069915}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1107617306}[检测的]{style="font-family:宋体"}[FEC]{lang="EN-US"}[类型，取值包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[和]{style="font-family:宋体"}[TE Tunnel]{lang="EN-US"}

[[FEC Info]{lang="EN-US"}]{#struct_0_x1562_10515_x2101551901}

[[FEC]{lang="EN-US"}]{#struct_0_x1562_10515_x679972678}[相关信息]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1835340778}[检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[时，]{style="font-family:宋体"}[FEC]{lang="EN-US"}[信息包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination]{lang="EN-US"}]{#struct_0_x1562_10515_997674627}[：]{lang="EN-US" style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mask Length]{lang="EN-US"}]{#struct_0_x1562_10515_570822231}[：]{lang="EN-US" style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址掩码]{lang="EN-US" style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x421004379}[检测]{style="font-family:宋体"}[TE]{lang="EN-US"}[隧道时，]{style="font-family:宋体"}[FEC]{lang="EN-US"}[信息包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source]{lang="EN-US"}]{#struct_0_x1562_10515_x315740667}[：隧道的源端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination]{lang="EN-US"}]{#struct_0_x1562_10515_x1413819714}[：隧道的目的端地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel ID]{lang="EN-US"}]{#struct_0_x1562_10515_194952396}[：隧道]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP ID]{lang="EN-US"}]{#struct_0_x1562_10515_2125254290}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[NHLFE ID]{lang="EN-US"}]{#struct_0_x1562_10515_x420676699}

[[对应的]{style="font-family:宋体"}[NHLFE]{lang="EN-US"}]{#struct_0_x1562_10515_873732203}[表项]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Local Discr]{lang="EN-US"}]{#struct_0_x1562_10515_x1714087879}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x2056540941}[会话的本地标识符]{style="font-family:宋体"}

[[Remote Discr]{lang="EN-US"}]{#struct_0_x1562_10515_869312510}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_1195560997}[会话的远端标识符]{style="font-family:宋体"}

[[Source IP]{lang="EN-US"}]{#struct_0_x1562_10515_x420611163}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x342526409}[会话的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为本端设备的]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}

[[Destination IP]{lang="EN-US"}]{#struct_0_x1562_10515_x1156688499}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x123059596}[会话的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress]{lang="EN-US"}]{#struct_0_x1562_10515_x420807771}[端]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{lang="EN-US" style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_x1562_10515_1644399934}[端]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{lang="EN-US" style="font-family:宋体"}[Ingress]{lang="EN-US"}[端的]{lang="EN-US" style="font-family:宋体"}[MPLS LSR]{lang="EN-US"}[ ]{lang="EN-US"}[ID]{lang="EN-US"}

[[Session State]{lang="EN-US"}]{#struct_0_x1562_10515_x1420796568}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x820364511}[会话状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x1562_10515_x1094898036}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1562_10515_x420742235}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1562_10515_x323949900}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Session Role]{lang="EN-US"}]{#struct_0_x1562_10515_x902751440}

[[本端设备在]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_1967679004}[会话中的角色，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1562_10515_x420414555}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的发起端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_x1562_10515_x1866584337}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的接收端]{lang="EN-US" style="font-family:宋体"}

[[Template Name]{lang="EN-US"}]{#struct_0_x1562_10515_1277365046}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_948146935}[会话参数的模板名称]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc328666328}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1370135468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd ]{lang="EN-US"}**[(for LSP)]{lang="EN-US"}]{#struct_0_x1562_10515_x420349019}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd ]{lang="EN-US"}**[(for TE tunnel)]{lang="EN-US"}]{#struct_0_x1562_10515_1979914859}

::: {#-1662096456 .myid}
[]{#_Toc404791714}[]{#struct_0_x1562_10515_1945110097}[]{#_Toc336438757}[]{#_Toc336438904}

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd enable**

------------------------------------------------------------------------

[**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_497501104}[命令用来使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[**[undo mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x1211126939}[命令用来关闭]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_183673666}

[**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_1760177034}

[**[undo mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x125598742}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x576936427}

[[MPLS  BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x420938846}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2001839761}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_596389850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1966891896}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_615739526}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_406962152}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_411087916}

[[如果没有通过本命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x1562_10515_505093873}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，则执行]{style="font-family:宋体"}**[mpls bfd ]{lang="EN-US"}**[(for LSP)]{lang="EN-US"}[、]{style="font-family:宋体"}**[mpls bfd ]{lang="EN-US"}**[(for TE tunnel)]{lang="EN-US"}[或]{style="font-family:宋体"}**[vccv bfd]{lang="EN-US"}**[命令后，不会创建检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道、]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1736423389}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x420873310}[使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_442064812}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}
:::

::: {#1214365350 .myid}
[]{#_Toc404791715}[]{#struct_0_x1562_10515_1587135613}[]{#_Toc329074907}

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd (for LSP)**

------------------------------------------------------------------------

[**[mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x1583825320}[命令用来配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[**[undo mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x2084654010}[用来取消使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1363537210}

[**[mpls bfd ]{lang="EN-US"}***[dest-addr]{lang="EN-US"}*[ *mask-length* \[ **nexthop** *nexthop-address* \[ **discriminator local** *local-id* **remote** *remote-id* \] \] \[ **template** *template-name* \]]{lang="EN-US"}]{#struct_0_x1562_10515_836141927}

[**[undo mpls bfd ]{lang="EN-US"}***[dest-addr]{lang="EN-US"}*[ *mask-length* \[ **nexthop** *nexthop-address* \]]{lang="EN-US"}]{#struct_0_x1562_10515_1788755119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1561902614}

[[未使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x421069918}[检测]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1108338202}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1415262899}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_773241923}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1889654036}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x2000325475}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x31003770}

[*[dest-addr]{lang="EN-US"}*[ *mask-length*]{lang="EN-US"}]{#struct_0_x1562_10515_21907028}[：]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1562_10515_211771226}[：]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nexthop]{lang="EN-US"}**[ *nexthop-address*]{lang="EN-US"}]{#struct_0_x1562_10515_x421004382}[：指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[下一跳地址。如果指定该参数，则只检测指定的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[；如果不指定该参数，则检测]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应的所有]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x316330496}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的标识符。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}***[ local-id]{lang="EN-US"}*]{#struct_0_x1562_10515_1963184709}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}***[ remote-id]{lang="EN-US"}*]{#struct_0_x1562_10515_331163161}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的远端标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[template ]{lang="EN-US"}***[te]{lang="EN-US"}[mplate-name]{lang="EN-US"}*]{#struct_0_x1562_10515_x1930852279}[：指定引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数的模板名称。]{style="font-family:宋体"}*[template-]{lang="EN-US"}[name]{lang="EN-US"}*[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_188789506}

[[通过]{style="font-family:宋体"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_578731383}[命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，并执行本命令后，设备上将会创建用来检测指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[出现故障时，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[可以快速检测到该故障，以便设备及时进行相应地处理，如将流量切换到备份]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[可以通过两种方式配置检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1562_10515_1753281010}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态方式：如果执行]{style="font-family:宋体"}]{#struct_0_x1562_10515_x2103922504}**[mpls bfd]{lang="EN-US"}**[命令时通过]{style="font-family:宋体"}**[discriminator]{lang="EN-US"}**[参数指定了本地和远端的标识符，则根据指定的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。采用这种方式时，要求本地和远端设备上都使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，通过]{style="font-family:宋体"}**[mpls bfd]{lang="EN-US"}**[命令配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性，并要求两端配置的本地和远端标识符匹配。该方式用来检测两台设备间从本地到远端和从远端到本地的一对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态方式：如果执行]{style="font-family:宋体"}]{#struct_0_x1562_10515_x420676702}**[mpls bfd]{lang="EN-US"}**[命令时没有通过]{style="font-family:宋体"}**[discriminator]{lang="EN-US"}**[参数指定本地和远端的标识符，则自动运行]{style="font-family:宋体"}[MPLS Ping]{lang="EN-US"}[来协商标识符，并根据协商好的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。采用这种方式时，要求本地和远端设备上都使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，但不需要在远端设备上执行]{style="font-family:宋体"}**[mpls bfd]{lang="EN-US"}**[命令。该方式用来检测两台设备间从本地到远端的一条单向]{style="font-family:宋体"}[LSP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[template ]{lang="EN-US"}***[te]{lang="EN-US"}[mplate-name]{lang="EN-US"}*]{#struct_0_x1562_10515_x1082255260}[参数，则]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话使用系统视图下配置的多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_1171188886}[会话的源地址为本端设备的]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[。因此，配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[功能前，需要先在本端设备上配置]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[，并确保远端设备上存在到达]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1416982520}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_1122022972}[配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到达目的地址]{style="font-family:宋体"}[22.22.2.2/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_1206787355}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] mpls bfd 22.22.2.2 32]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x1879211681}[配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到达目的地址]{style="font-family:宋体"}[22.22.2.2/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性，并指定待检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的下一跳地址为]{style="font-family:宋体"}[12.0.0.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_273284821}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] mpls bfd 22.22.2.2 32 nexthop 12.0.0.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_832744456}[配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测到达目的地址]{style="font-family:宋体"}[22.22.2.2/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性，并指定待检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的下一跳地址为]{style="font-family:宋体"}[12.0.0.2]{lang="EN-US"}[，本地标识符和远端标识符分别为]{style="font-family:宋体"}[1]{lang="EN-US"}[，引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_x420611166}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] mpls bfd 22.22.2.2 32 nexthop 12.0.0.2 discriminator local 1 remote 1 template test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x342329801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_356657760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_1992653803}
:::

::: {#-1942820472 .myid}
[]{#_Toc404791716}[]{#struct_0_x1562_10515_x1559299430}[]{#_Toc336433183}[]{#_Toc336438760}[]{#_Toc336438907}[]{#_Toc336438761}[]{#_Toc336438908}[]{#_Toc336438762}[]{#_Toc336438909}[]{#_Toc336438763}[]{#_Toc336438910}[]{#_Toc336438764}[]{#_Toc336438911}[]{#_Toc336438765}[]{#_Toc336438912}[]{#_Toc336438766}[]{#_Toc336438913}[]{#_Toc336438767}[]{#_Toc336438914}[]{#_Toc336438768}[]{#_Toc336438915}[]{#_Toc336438769}[]{#_Toc336438916}[]{#_Toc336438770}[]{#_Toc336438917}[]{#_Toc336438771}[]{#_Toc336438918}[]{#_Toc336438772}[]{#_Toc336438919}[]{#_Toc336438773}[]{#_Toc336438920}[]{#_Toc336438774}[]{#_Toc336438921}[]{#_Toc336438775}[]{#_Toc336438922}[]{#_Toc336438776}[]{#_Toc336438923}[]{#_Toc336438777}[]{#_Toc336438924}[]{#_Toc336438778}[]{#_Toc336438925}[]{#_Toc336438779}[]{#_Toc336438926}[]{#_Toc336438780}[]{#_Toc336438927}[]{#_Toc336438781}[]{#_Toc336438928}[]{#_Toc336438782}[]{#_Toc336438929}[]{#_Toc336438783}[]{#_Toc336438930}[]{#_Toc336438784}[]{#_Toc336438931}[]{#_Toc336438785}[]{#_Toc336438932}[]{#_Toc336438786}[]{#_Toc336438933}[]{#_Toc336438787}[]{#_Toc336438934}[]{#_Toc336438788}[]{#_Toc336438935}[]{#_Toc336438789}[]{#_Toc336438936}[]{#_Toc336438790}[]{#_Toc336438937}[]{#_Toc336438791}[]{#_Toc336438938}[]{#_Toc336438792}[]{#_Toc336438939}[]{#_Toc336438793}[]{#_Toc336438940}[]{#_Toc336438794}[]{#_Toc336438941}[]{#_Toc336438795}[]{#_Toc336438942}[]{#_Toc336438796}[]{#_Toc336438943}

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls bfd (for TE tunnel)**

------------------------------------------------------------------------

[**[mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x1077213997}[命令用来配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测当前隧道接口对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性。]{style="font-family:宋体"}

[**[undo mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_87691736}[命令用来取消使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测当前隧道接口对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x414866776}

[**[mpls bfd ]{lang="EN-US"}**[\[ **discriminator local** *local-id* **remote** *remote-id* \] \[ **template** *template-name* \]]{lang="EN-US"}]{#struct_0_x1562_10515_x420807774}

[**[undo mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1644203326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1775448198}

[[未使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x216349007}[检测隧道接口对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x962395527}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1562_10515_1514170348}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1533737719}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x648215732}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1455862489}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_833567451}

[**[discriminator]{lang="EN-US"}**]{#struct_0_x1562_10515_x420742238}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的标识符。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}***[ local-id]{lang="EN-US"}*]{#struct_0_x1562_10515_x324670796}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的本地标识符。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}***[ remote-id]{lang="EN-US"}*]{#struct_0_x1562_10515_2074608033}[：指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的远端标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[template ]{lang="EN-US"}***[te]{lang="EN-US"}[mplate-name]{lang="EN-US"}*]{#struct_0_x1562_10515_90670063}[：指定引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数的模板名称。]{style="font-family:宋体"}*[template-]{lang="EN-US"}[name]{lang="EN-US"}*[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_559874201}

[[通过]{style="font-family:宋体"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x1233363176}[命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，并执行本命令后，设备上将会创建用来检测指定]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。当]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道出现故障时，]{style="font-family:宋体"}[BFD]{lang="EN-US"}[可以快速检测到该故障，以便设备及时进行相应地处理，如将流量切换到备份隧道。]{style="font-family:宋体"}

[[可以通过两种方式配置检测]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}]{#struct_0_x1562_10515_x1239305283}[隧道的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态方式：如果执行]{style="font-family:宋体"}]{#struct_0_x1562_10515_x759476261}**[mpls bfd]{lang="EN-US"}**[命令时通过]{style="font-family:宋体"}**[discriminator]{lang="EN-US"}**[参数指定了本地和远端的标识符，则根据指定的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。采用这种方式时，要求本地和远端设备上都使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，通过]{style="font-family:宋体"}**[mpls bfd]{lang="EN-US"}**[命令配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测指定]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性，并要求两端配置的本地和远端标识符匹配。该方式用来检测两台设备间从本地到远端和从远端到本地的一对]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[动态方式：如果执行]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1382074644}**[mpls bfd]{lang="EN-US"}**[命令时没有通过]{style="font-family:宋体"}**[discriminator]{lang="EN-US"}**[参数指定本地和远端的标识符，则自动运行]{style="font-family:宋体"}[MPLS Ping]{lang="EN-US"}[来协商标识符，并根据协商好的标识符建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。采用这种方式时，要求本地和远端设备上都使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能，但不需要在远端设备上执行]{style="font-family:宋体"}**[mpls bfd]{lang="EN-US"}**[命令。该方式用来检测两台设备间从本地到远端的一条单向]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[执行本命令时，如果没有指定]{style="font-family:宋体"}**[template ]{lang="EN-US"}***[te]{lang="EN-US"}[mplate-name]{lang="EN-US"}*]{#struct_0_x1562_10515_x420414558}[参数，则]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话使用]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口视图下配置的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1867436305}[会话的源地址为本端设备的]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[。因此，配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道功能前，需要先在本端设备上配置]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[，并确保远端设备上存在到达]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[的路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1472863290}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x1285576543}[配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性，并指定引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数的模板为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_x1055303847}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] interface Tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] mpls bfd template test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_2048773136}[配置通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性，并本地标识符和远端标识符均为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_x114310500}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] interface Tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] mpls bfd discriminator local 1 remote 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x113716676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mpls bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x420349022}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_1980373612}
:::

::: {#527509693 .myid}
[]{#_Toc404791717}[]{#struct_0_x1562_10515_x1581776133}

**MPLS OAM \-- MPLS OAM配置命令 \-- mpls periodic-tracert (for LSP)**

------------------------------------------------------------------------

[**[mpls periodic-tracert]{lang="EN-US"}**]{#struct_0_x1562_10515_x2012457686}[命令用来使能指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mpls** **periodic-tracert**]{lang="EN-US"}]{#struct_0_x1562_10515_x806103608}[命令用来关闭指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}[对应]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x828015548}

[**[mpls periodic-tracert ]{lang="EN-US"}***[dest-addr]{lang="EN-US"}[ mask-length]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-u** *retry-attempt* \| **fec-check** \] \*]{lang="EN-US"}]{#struct_0_x1562_10515_x1241734497}

[**[undo mpls periodic-tracert ]{lang="EN-US"}***[dest-addr]{lang="EN-US"}*[ *mask-length*]{lang="EN-US"}]{#struct_0_x1562_10515_863127876}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1520774209}

[[LSP]{lang="EN-US"}]{#struct_0_x1562_10515_x420938845}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2002036369}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_x695664475}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1282410283}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_191772977}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1075655944}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1244369554}

[*[dest-addr]{lang="EN-US"}*]{#struct_0_x1562_10515_1171610985}[：]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1562_10515_906573005}[：]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-a ]{lang="EN-US"}***[source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_x420873309}[：指定]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文的源地址，缺省使用]{style="font-family:宋体"}[MPLS LSR ID]{lang="EN-US"}[作为]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}**[ *exp-value*]{lang="EN-US"}]{#struct_0_x1562_10515_441606061}[：指定]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[Exp]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}**[ *ttl-value*]{lang="EN-US"}]{#struct_0_x1562_10515_x1870401501}[：指定]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的最大值（即检测的最大跳数）。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-m]{lang="EN-US"}***[ wait-time]{lang="EN-US"}*]{#struct_0_x1562_10515_119670152}[：指定]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[功能的检测周期。]{style="font-family:宋体"}*[wait-time]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[**[-rtos ]{lang="EN-US"}***[tos-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x17374285}[：指定]{style="font-family:宋体"}[MPLS Echo Reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值**，**]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}**[ *time-out*]{lang="EN-US"}]{#struct_0_x1562_10515_375188437}[：指定发送]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-u]{lang="EN-US"}**[ *retry-attempt*]{lang="EN-US"}]{#struct_0_x1562_10515_367085749}[：指定]{style="font-family:宋体"}[MPLS Echo Request]{lang="EN-US"}[报文超时重试的次数。]{style="font-family:宋体"}*[retry-attempt]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[，单位为次数，缺省值为]{style="font-family:
宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[fec-check]{lang="EN-US"}**]{#struct_0_x1562_10515_x514166244}[：指定在]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点上进行]{style="font-family:宋体"}[FEC]{lang="EN-US"}[栈检查。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1591982923}

[[LSP]{lang="EN-US"}]{#struct_0_x1562_10515_x421069917}[的周期性]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[功能，即周期性地对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[进行]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[主动检测，该功能用来对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的错误点进行定位，对转发平面和控制平面一致性进行校验，并将发现的错误记录到系统日志（]{style="font-family:宋体"}[System Log Messages]{lang="EN-US"}[）中。管理员可以通过查看日志信息，了解]{style="font-family:宋体"}[LSP]{lang="EN-US"}[是否出现故障。]{style="font-family:宋体"}

[[如果同时配置了]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x1107486234}[自动检测]{style="font-family:宋体"}[LSP]{lang="EN-US"}[功能和周期性]{style="font-family:宋体"}[LSP Trace route]{lang="EN-US"}[功能，则周期性]{style="font-family:宋体"}[LSP Trace route]{lang="EN-US"}[检测到转发平面故障或转发平面与控制平面不一致时，会拆除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，并基于控制平面重新建立]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[执行本命令前，需先执行]{style="font-family:宋体"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_1179496507}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1334777023}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_1060550379}[使用周期性]{style="font-family:宋体"}[LSP Trace route]{lang="EN-US"}[功能，检测到达目的地]{style="font-family:宋体"}[11.11.1.1/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的有效性，并检查转发平面与控制平面是否一致。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_552751908}

[\[Sysname\] mpls bfd enable]{lang="EN-US"}

[\[Sysname\] mpls periodic-tracert 11.11.1.1 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x950846293}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x2046037979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd]{lang="EN-US"}**[ (for LSP)]{lang="EN-US"}]{#struct_0_x1562_10515_897136498}
:::

::: {#1909720745 .myid}
[]{#struct_0_x1562_10515_x562355867}[]{#_Toc404791718}[]{#_Toc336438798}[]{#_Toc336438945}[]{#_Toc336438799}[]{#_Toc336438946}[]{#_Toc336438800}[]{#_Toc336438947}[]{#_Toc336438801}[]{#_Toc336438948}[]{#_Toc336438802}[]{#_Toc336438949}[]{#_Toc336438803}[]{#_Toc336438950}[]{#_Toc336438804}[]{#_Toc336438951}[]{#_Toc336438805}[]{#_Toc336438952}[]{#_Toc336438806}[]{#_Toc336438953}[]{#_Toc336438807}[]{#_Toc336438954}[]{#_Toc336438808}[]{#_Toc336438955}[]{#_Toc336438809}[]{#_Toc336438956}[]{#_Toc336438810}[]{#_Toc336438957}[]{#_Toc336438811}[]{#_Toc336438958}[]{#_Toc336438812}[]{#_Toc336438959}[]{#_Toc336438813}[]{#_Toc336438960}[]{#_Toc336438814}[]{#_Toc336438961}[]{#_Toc336438815}[]{#_Toc336438962}[]{#_Toc336438816}[]{#_Toc336438963}[]{#_Toc336438817}[]{#_Toc336438964}[]{#_Toc336438818}[]{#_Toc336438965}[]{#_Toc336438819}[]{#_Toc336438966}[]{#_Toc336438820}[]{#_Toc336438967}[]{#_Toc336438821}[]{#_Toc336438968}[]{#_Toc336438822}[]{#_Toc336438969}[]{#_Toc336438823}[]{#_Toc336438970}[]{#_Toc336438824}[]{#_Toc336438971}[]{#_Toc336438825}[]{#_Toc336438972}[]{#_Toc336438826}[]{#_Toc336438973}[]{#_Toc336438827}[]{#_Toc336438974}[]{#_Toc336438828}[]{#_Toc336438975}[]{#_Toc336438829}[]{#_Toc336438976}

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls ipv4**

------------------------------------------------------------------------

[**[ping mpls ipv4]{lang="EN-US"}**]{#struct_0_x1562_10515_1907845123}[命令用来检测]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀类型]{style="font-family:宋体"}[MPLS LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x421004381}

[**[ping mpls ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** \] \* **ipv4** *dest-addr* *mask-length* \[ **destination** *start-address* \[ *end-address* \[ *address-increment* \] \] \]]{lang="EN-US"}]{#struct_0_x1562_10515_x316264960}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_53584993}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_765216017}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1913058452}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_3239040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1454242532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_628959099}

[**[-a]{lang="EN-US"}***[ source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_x1071097569}[：指定发送的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址为报文出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[-c ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x1562_10515_x1672583224}[：指定重复发送]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中目的地址相同的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的次数。]{style="font-family:宋体"}*[count]{lang="EN-US"}*[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中目的地址相同的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的重复发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}***[ exp-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x420676701}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}***[ ttl-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x1082058652}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-m]{lang="EN-US"}**[ *wait-time*]{lang="EN-US"}]{#struct_0_x1562_10515_x1468267684}[：指定连续发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}*[wait-time]{lang="EN-US"}*[为发送报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}**[ *reply-mode*]{lang="EN-US"}]{#struct_0_x1562_10515_x777310514}[：指定接收者对]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的应答模式。]{style="font-family:宋体"}*[reply-mode]{lang="EN-US"}*[为应答模式，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[1]{lang="EN-US"}[表示不回应，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应并携带]{style="font-family:宋体"}[Router Alert]{lang="EN-US"}[选项。缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-rtos]{lang="EN-US"}***[ tos-value]{lang="EN-US"}*]{#struct_0_x1562_10515_2046427708}[：指定]{style="font-family:宋体"}[MPLS echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-s ]{lang="EN-US"}***[packet-size]{lang="EN-US"}*]{#struct_0_x1562_10515_x1880428334}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度。]{style="font-family:宋体"}*[packet-size]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度（不包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[头和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头），取值范围为]{style="font-family:宋体"}[65]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}***[ time-out]{lang="EN-US"}*]{#struct_0_x1562_10515_x1480859954}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[为超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-v]{lang="EN-US"}**]{#struct_0_x1562_10515_1188427637}[：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。]{style="font-family:宋体"}

[*[dest-addr]{lang="EN-US"}*[ *mask-length*]{lang="EN-US"}]{#struct_0_x1562_10515_1654379712}[：检测指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的地址，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_x1562_10515_x420611165}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址，缺省值为]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[start-address]{lang="EN-US"}*]{#struct_0_x1562_10515_x342395337}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址或起始目的地址，该地址必须是]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址（本机环回地址）。如果指定了本参数，没有指定]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址为]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的发送次数由]{style="font-family:宋体"}**[-c ]{lang="EN-US"}***[count]{lang="EN-US"}*[参数决定；如果同时指定了本参数和]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址从]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[开始，依次增加]{style="font-family:宋体"}*[address-increment]{lang="EN-US"}*[，直到到达]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[，每个目的地址对应]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的发送次数由]{style="font-family:宋体"}**[-c ]{lang="EN-US"}***[count]{lang="EN-US"}*[参数决定。]{style="font-family:宋体"}

[*[end-address]{lang="EN-US"}*]{#struct_0_x1562_10515_1907405599}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[结束目的地址，该地址必须是]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址（本机环回地址）。]{style="font-family:宋体"}

[*[address-increment]{lang="EN-US"}*]{#struct_0_x1562_10515_x1015649676}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中目的地址的步进值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x448628220}

[[\# ]{lang="PT-BR"}]{#struct_0_x1562_10515_x24594842}[检测到达]{style="font-family:宋体"}[3.3.3.9/32]{lang="PT-BR"}[的]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[的连通性。]{style="font-family:宋体"}

[[\<Sysname\> ping mpls ipv4 3.3.3.9 32]{lang="EN-US"}]{#struct_0_x1562_10515_x420807773}

[MPLS ping FEC 3.3.3.9/32 with 100 bytes of data:]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=1 time=49 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=2 time=44 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=3 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=4 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=5 time=76 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for FEC 3.3.3.9/32 \-\--]{lang="EN-US"}

[5 packets transmitted, 5 packets received, 0.0% packet loss]{lang="EN-US"}

[Round-trip min/avg/max = 44/57/76 ms]{lang="EN-US"}

[[\# ]{lang="PT-BR"}]{#struct_0_x1562_10515_1644268862}[检测到达]{style="font-family:宋体"}[3.3.3.9/32]{lang="PT-BR"}[的]{style="font-family:宋体"}[LSP]{lang="PT-BR"}[的连通性，并指定如下参数：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复发送]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1562_10515_2131945713}[头中目的地址相同的]{lang="EN-US" style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的次数为]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[次。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示详细的应答信息。]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_1856159817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定]{style="font-family:宋体"}]{#struct_0_x1562_10515_1883788592}[IP]{lang="EN-US"}[头的目的地址范围为]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[～]{style="font-family:宋体"}[127.0.0.3]{lang="EN-US"}[，并指定目的地址的步进值为]{style="font-family:宋体"}[2]{lang="EN-US"}[，即]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址为]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[和]{style="font-family:宋体"}[127.0.0.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> ping mpls --c 3 --v ipv4 3.3.3.9 32 destination 127.0.0.1 127.0.0.3 2]{lang="EN-US"}]{#struct_0_x1562_10515_x420742237}

[MPLS ping FEC 3.3.3.9/32 with 100 bytes of data:]{lang="EN-US"}

[Destination address 127.0.0.1]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=1 time=49 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination address 127.0.0.3]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=2 time=44 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination address 127.0.0.1]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=3 time=60 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination address 127.0.0.3]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=4 time=60 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination address 127.0.0.1]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=5 time=76 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination address 127.0.0.3]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=6 time=57 ms Return Code=3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for FEC 3.3.3.9/32 \-\--]{lang="EN-US"}

[6 packets transmitted, 6 packets received, 0.0% packet loss]{lang="EN-US"}

[Round-trip min/avg/max = 44/57/76 ms]{lang="EN-US"}

[]{#struct_0_x1562_10515_x324080972}[[表1-3 ]{lang="EN-US"}[ping mpls ipv4]{lang="EN-US"}]{#_Ref329182139}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1072591693}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_x1562_10515_147390577}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_x1562_10515_x1684893260}

[[MPLS Ping FEC: 3.3.3.9/32 : 100 data bytes]{lang="EN-US"}]{#struct_0_x1562_10515_395622810}

[[检测]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_x309739227}[FEC]{lang="EN-US"}[目的地址为]{lang="EN-US" style="font-family:宋体"}[3.3.3.9/32]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的连通性，发送的]{lang="EN-US" style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的长度为]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[字节]{lang="EN-US" style="font-family:宋体"}

[[Destination address]{lang="EN-US"}]{#struct_0_x1562_10515_449055482}

[[IP]{lang="EN-US"}]{#struct_0_x1562_10515_x420414557}[头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[100 bytes from 100.1.2.1]{lang="EN-US"}]{#struct_0_x1562_10515_x1866453265}

[[从]{style="font-family:宋体"}[100.1.2.1]{lang="EN-US"}]{#struct_0_x1562_10515_x41525842}[接收到长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[字节的应答报文]{style="font-family:宋体"}

[[Sequence]{lang="EN-US"}]{#struct_0_x1562_10515_x1373800751}

[[应答报文的序列号，用来判断报文是否有分组丢失、失序或重复]{style="font-family:宋体"}]{#struct_0_x1562_10515_x200821366}

[[time]{lang="EN-US"}]{#struct_0_x1562_10515_x293509505}

[[报文的往返时延]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_x420349021}

[[Return]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_x1562_10515_1980439148}[Code]{lang="EN-US"}

[[返回码，括号内为返回子码]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1577302355}

[[Ping statistics for FEC 3.3.3.9/32]{lang="EN-US"}]{#struct_0_x1562_10515_1680906028}

[[LSP]{lang="EN-US"}]{#struct_0_x1562_10515_x1551081598}[检测的统计数据]{style="font-family:宋体"}

[[packets transmitted]{lang="EN-US"}]{#struct_0_x1562_10515_911595391}

[[发送的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_x420938848}[MPLS echo request]{lang="EN-US"}[报文数]{lang="EN-US" style="font-family:宋体"}

[[packets received]{lang="EN-US"}]{#struct_0_x1562_10515_2002757265}

[[接收的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_x308972255}[MPLS echo reply]{lang="EN-US"}[报文数]{lang="EN-US" style="font-family:宋体"}

[[packet loss]{lang="EN-US"}]{#struct_0_x1562_10515_x1043527538}

[[未响应请求报文占发送的总请求报文的百分比]{style="font-family:宋体"}]{#struct_0_x1562_10515_334574361}

[[R]{lang="EN-US"}]{#struct_0_x1562_10515_x420873312}[ound-trip min/avg/max]{lang="EN-US"}

[[往返时延的最小值、平均值和最大值]{style="font-family:宋体"}]{#struct_0_x1562_10515_441933740}

[ ]{lang="EN-US"}

::: {#-1011624091 .myid}
[]{#struct_0_x1562_10515_322397342}[]{#_Toc404791719}

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls pw**

------------------------------------------------------------------------

[**[ping mpls pw]{lang="EN-US"}**]{#struct_0_x1562_10515_437356554}[命令用来检测]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}[或静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1365279236}

[**[ping mpls ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** \] \* **pw** *ip-address* **pw-id** *pw-id*]{lang="EN-US"}]{#struct_0_x1562_10515_x1125679733}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x303007748}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_2088652363}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x421069920}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1107813911}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_78860676}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1126775616}

[**[-a]{lang="EN-US"}***[ source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_x441902453}[：指定发送的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址为报文出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[-c ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x1562_10515_1755719802}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的次数。]{style="font-family:宋体"}*[count]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}***[ exp-value]{lang="EN-US"}*]{#struct_0_x1562_10515_1261917420}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}***[ ttl-value]{lang="EN-US"}*]{#struct_0_x1562_10515_404456160}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-m]{lang="EN-US"}**[ *wait-time*]{lang="EN-US"}]{#struct_0_x1562_10515_x1774410863}[：指定连续发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}*[wait-time]{lang="EN-US"}*[为发送报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}**[ *reply-mode*]{lang="EN-US"}]{#struct_0_x1562_10515_x421004384}[：指定接收者对]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的应答模式。]{style="font-family:宋体"}*[reply-mode]{lang="EN-US"}*[为应答模式，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[1]{lang="EN-US"}[表示不回应，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应并携带]{style="font-family:宋体"}[Router Alert]{lang="EN-US"}[选项。缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-rtos]{lang="EN-US"}***[ tos-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x316461568}[：指定]{style="font-family:宋体"}[MPLS echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-s ]{lang="EN-US"}***[packet-size]{lang="EN-US"}*]{#struct_0_x1562_10515_1587568136}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度。]{style="font-family:宋体"}*[packet-size]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度（不包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[头和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头），取值范围为]{style="font-family:宋体"}[65]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}***[ time-out]{lang="EN-US"}*]{#struct_0_x1562_10515_418828791}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[为超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-v]{lang="EN-US"}**]{#struct_0_x1562_10515_x1945255805}[：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1562_10515_1386733921}[：指定对端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_x1562_10515_529269368}[：指定到对端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x854529386}

[[\# ]{lang="PT-BR"}]{#struct_0_x1562_10515_804594351}[检测到达对端]{style="font-family:宋体"}[PE]{lang="PT-BR"}[（]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址为]{style="font-family:宋体"}[3.3.3.9]{lang="PT-BR"}[）、]{style="font-family:宋体"}[PW ID]{lang="PT-BR"}[为]{style="font-family:宋体"}[301]{lang="PT-BR"}[的]{style="font-family:宋体"}[PW]{lang="PT-BR"}[的连通性。]{style="font-family:宋体"}

[[\<Sysname\> ping mpls pw 3.3.3.9 pw-id 301]{lang="EN-US"}]{#struct_0_x1562_10515_x420676704}

[MPLS ping PW 3.3.3.9 301 with 100 bytes of data:]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=1 time=49 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=2 time=44 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=3 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=4 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=5 time=76 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for PW 3.3.3.9 301 \-\--]{lang="EN-US"}

[5 packets transmitted, 5 packets received, 0.0% packet loss]{lang="EN-US"}

[Round-trip min/avg/max = 44/57/76 ms]{lang="EN-US"}

[[显示信息中各字段的解释，请参见]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1081862044}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?1909720745#_Ref329182139)[。]{style="font-family:宋体"}
:::

::: {#-2127058479 .myid}
[]{#_Toc404791720}[]{#struct_0_x1562_10515_1618137682}[]{#_Toc329867221}

**MPLS OAM \-- MPLS OAM配置命令 \-- ping mpls te**

------------------------------------------------------------------------

[**[ping mpls te]{lang="EN-US"}**]{#struct_0_x1562_10515_x978945640}[命令用来检测]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_41771185}

[**[ping mpls ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-c** *count* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-m** *wait-time* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-s** *packet-size* \| **-t** *time-out* \| **-v** \] \* **te** **tunnel** *interface-number*]{lang="EN-US"}]{#struct_0_x1562_10515_1925414862}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1219649774}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_1993618713}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1955220590}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1680968289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1618596434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2112351672}

[**[-a]{lang="EN-US"}***[ source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_1985381219}[：指定发送的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址为报文出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[-c ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x1562_10515_x1847858127}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的次数。]{style="font-family:宋体"}*[count]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}***[ exp-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x1552815881}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}***[ ttl-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x1717056533}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-m]{lang="EN-US"}**[ *wait-time*]{lang="EN-US"}]{#struct_0_x1562_10515_719500368}[：指定连续发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}*[wait-time]{lang="EN-US"}*[为发送报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}**[ *reply-mode*]{lang="EN-US"}]{#struct_0_x1562_10515_1618530898}[：指定接收者对]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的应答模式。]{style="font-family:宋体"}*[reply-mode]{lang="EN-US"}*[为应答模式，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[1]{lang="EN-US"}[表示不回应，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应并携带]{style="font-family:宋体"}[Router Alert]{lang="EN-US"}[选项。缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-rtos]{lang="EN-US"}***[ tos-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x1032125304}[：指定]{style="font-family:宋体"}[MPLS echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-s ]{lang="EN-US"}***[packet-size]{lang="EN-US"}*]{#struct_0_x1562_10515_x2126815132}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度。]{style="font-family:宋体"}*[packet-size]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文长度（不包括]{style="font-family:宋体"}[IP]{lang="EN-US"}[头和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头），取值范围为]{style="font-family:宋体"}[65]{lang="EN-US"}[～]{style="font-family:宋体"}[8100]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[100]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}***[ time-out]{lang="EN-US"}*]{#struct_0_x1562_10515_257208170}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[为超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-v]{lang="EN-US"}**]{#struct_0_x1562_10515_x1108954134}[：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1562_10515_669038798}[：检测指定隧道接口对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为隧道接口编号，取值范围为设备上已经创建的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_2107289383}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_1178874018}[检测隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的连通性。]{style="font-family:宋体"}

[[\<Sysname\> ping mpls te tunnel 1]{lang="EN-US"}]{#struct_0_x1562_10515_1618072147}

[MPLS ping TE tunnel Tunnel1 with 100 bytes of data:]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=1 time=49 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=2 time=44 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=3 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=4 time=60 ms]{lang="EN-US"}

[100 bytes from 100.1.2.1: Sequence=5 time=76 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for TE tunnel Tunnel1 \-\--]{lang="EN-US"}

[5 packets transmitted, 5 packets received, 0.0% packet loss]{lang="EN-US"}

[Round-trip min/avg/max = 44/57/76 ms]{lang="EN-US"}

[[显示信息中各字段的解释，请参见]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1376510990}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-3]{lang="EN-US"}](?1909720745#_Ref329182139)[。]{style="font-family:宋体"}
:::

::: {#1106107802 .myid}
[]{#struct_0_x1562_10515_559078298}[]{#_Toc404791721}[]{#_Toc366744531}[]{#_Toc366746461}[]{#_Toc366828615}[]{#_Toc336438832}[]{#_Toc336438979}[]{#_Toc336438833}[]{#_Toc336438980}[]{#_Toc336438834}[]{#_Toc336438981}[]{#_Toc336438835}[]{#_Toc336438982}[]{#_Toc336438836}[]{#_Toc336438983}[]{#_Toc336438837}[]{#_Toc336438984}[]{#_Toc336438838}[]{#_Toc336438985}[]{#_Toc336438839}[]{#_Toc336438986}[]{#_Toc336438840}[]{#_Toc336438987}[]{#_Toc336438841}[]{#_Toc336438988}[]{#_Toc336438842}[]{#_Toc336438989}[]{#_Toc336438843}[]{#_Toc336438990}[]{#_Toc336438844}[]{#_Toc336438991}[]{#_Toc336438845}[]{#_Toc336438992}[]{#_Toc336438846}[]{#_Toc336438993}[]{#_Toc336438847}[]{#_Toc336438994}[]{#_Toc336438848}[]{#_Toc336438995}[]{#_Toc336438849}[]{#_Toc336438996}[]{#_Toc336438850}[]{#_Toc336438997}[]{#_Toc336438851}[]{#_Toc336438998}[]{#_Toc336438852}[]{#_Toc336438999}[]{#_Toc336438853}[]{#_Toc336439000}[]{#_Toc336438854}[]{#_Toc336439001}[]{#_Toc336438855}[]{#_Toc336439002}[]{#_Toc336438856}[]{#_Toc336439003}[]{#_Toc336438857}[]{#_Toc336439004}[]{#_Toc336438858}[]{#_Toc336439005}[]{#_Toc336438859}[]{#_Toc336439006}[]{#_Toc336438860}[]{#_Toc336439007}[]{#_Toc336438861}[]{#_Toc336439008}[]{#_Toc336438862}[]{#_Toc336439009}[]{#_Toc336438863}[]{#_Toc336439010}[]{#_Toc336438864}[]{#_Toc336439011}[]{#_Toc336438865}[]{#_Toc336439012}[]{#_Toc336438866}[]{#_Toc336439013}

**MPLS OAM \-- MPLS OAM配置命令 \-- tracert mpls ipv4**

------------------------------------------------------------------------

[**[tracert mpls ipv4]{lang="EN-US"}**]{#struct_0_x1562_10515_x1851433199}[命令用来查看]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀类型]{style="font-family:宋体"}[MPLS LSP]{lang="EN-US"}[从]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点到]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点所经过的路径，并根据应答信息对错误点进行定位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x327071450}

[**[tracert mpls ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-v** \| **fec-check** \] \* **ipv4** *dest-addr mask-length* \[ **destination** *start-address* \[ *end-address* \[ *address-increment* \] \] \]]{lang="EN-US"}]{#struct_0_x1562_10515_x1925745398}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1369724698}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_x420611168}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x343247305}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_412076453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1796649773}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1009841296}

[**[-a]{lang="EN-US"}***[ source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_x1902806396}[：指定发送的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址为报文出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}***[ exp-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x336959089}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}***[ ttl-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x1443949763}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的最大值（即检测的最大跳数）。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}[ ]{lang="EN-US"}***[reply-mode]{lang="EN-US"}*]{#struct_0_x1562_10515_x1428418476}[：指定接收者对]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的应答模式。]{style="font-family:宋体"}*[reply-mode]{lang="EN-US"}*[为应答模式，取值为]{style="font-family:宋体"}[2]{lang="EN-US"}[和]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应并携带]{style="font-family:宋体"}[Router Alert]{lang="EN-US"}[选项。缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-]{lang="EN-US"}[rtos]{lang="EN-US"}**[ *tos-value*]{lang="EN-US"}]{#struct_0_x1562_10515_x420807776}[：指定]{style="font-family:宋体"}[MPLS echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}***[ time-out]{lang="EN-US"}*]{#struct_0_x1562_10515_1644072254}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[为超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-v]{lang="EN-US"}**]{#struct_0_x1562_10515_1757764260}**[：]{style="font-family:宋体"}**[指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。]{style="font-family:宋体"}

[**[fec-check]{lang="EN-US"}**]{#struct_0_x1562_10515_x1583984067}[：指定在]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点上进行]{style="font-family:宋体"}[FEC]{lang="EN-US"}[栈检查。]{style="font-family:宋体"}

[*[dest-addr]{lang="EN-US"}*[ *mask-length*]{lang="EN-US"}]{#struct_0_x1562_10515_503258114}[：查看指定]{style="font-family:宋体"}[LSP]{lang="EN-US"}[经过的路径。]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[的目的地址，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[FEC]{lang="EN-US"}[目的地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_x1562_10515_333287397}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址，缺省值为]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[start-address]{lang="EN-US"}*]{#struct_0_x1562_10515_x366313531}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址或起始目的地址，该地址必须是]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址（本机环回地址）。如果指定了本参数，没有指定]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址为]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[。如果同时指定了本参数和]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的目的地址从]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[开始，依次增加]{style="font-family:宋体"}*[address-increment]{lang="EN-US"}*[，直到到达]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[，对于每个目的地址都要执行一次]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[过程。]{style="font-family:宋体"}

[*[end-address]{lang="EN-US"}*]{#struct_0_x1562_10515_1752006327}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[结束目的地址，该地址必须是]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址（本机环回地址）。]{style="font-family:宋体"}

[*[address-increment]{lang="EN-US"}*]{#struct_0_x1562_10515_x943822480}[：表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中目的地址的步进值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x420742240}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x324146515}[查看到达目的地址]{style="font-family:宋体"}[5.5.5.9/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[从]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点到]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点所经过的路径，指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[头目的地址的范围为]{style="font-family:宋体"}[127.1.1.1]{lang="EN-US"}[～]{style="font-family:宋体"}[127.1.1.2]{lang="EN-US"}[，步进值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即对]{style="font-family:宋体"}[127.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[127.1.1.2]{lang="EN-US"}[两个地址分别进行一次]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> tracert mpls ipv4 5.5.5.9 32 destination 127.1.1.1 127.1.1.2 1]{lang="EN-US"}]{#struct_0_x1562_10515_1304237984}

[MPLS trace route FEC 5.5.5.9/32]{lang="EN-US"}

[  Destination address 127.1.1.1]{lang="EN-US"}

[  TTL   Replier            Time    Type      Downstream]{lang="EN-US"}

[  0                                Ingress   100.1.2.1/\[1025\]]{lang="EN-US"}

[  1     100.1.2.1          1 ms    Transit   100.2.4.1/\[1024\]]{lang="EN-US"}

[  2     100.2.4.1          63 ms   Transit   100.4.5.1/\[3\]]{lang="EN-US"}

[  3     100.4.5.1          129 ms  Egress]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination address 127.1.1.2]{lang="EN-US"}

[  TTL   Replier            Time    Type      Downstream]{lang="EN-US"}

[  0                                Ingress   100.1.3.1/\[1030\]]{lang="EN-US"}

[  1     100.1.3.1          1 ms    Transit   100.3.4.1/\[1024\]]{lang="EN-US"}

[  2     100.3.4.1          51 ms   Transit   100.4.5.1/\[3\]]{lang="EN-US"}

[  3     100.4.5.1          80 ms   Egress]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_32670197}[查看到达目的地址]{style="font-family:宋体"}[5.5.5.9/32]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[从]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点到]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点所经过的路径，显示详细的应答信息，并指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[头目的地址的范围为]{style="font-family:宋体"}[127.1.1.1]{lang="EN-US"}[～]{style="font-family:宋体"}[127.1.1.2]{lang="EN-US"}[，步进值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即对]{style="font-family:宋体"}[127.1.1.1]{lang="EN-US"}[和]{style="font-family:宋体"}[127.1.1.2]{lang="EN-US"}[两个地址分别进行一次]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> tracert mpls --v ipv4 5.5.5.9 32 destination 127.1.1.1 127.1.1.2 1]{lang="EN-US"}]{#struct_0_x1562_10515_x420414560}

[MPLS trace route FEC 5.5.5.9/32]{lang="EN-US"}

[  Destination address 127.1.1.1]{lang="EN-US"}

[  TTL   Replier            Time    Type      Downstream]{lang="EN-US"}

[  0                                Ingress   100.1.2.1/\[1025\]]{lang="EN-US"}

[  1     100.1.2.1          1 ms    Transit   100.2.4.1/\[1024\] ReturnCode 8(1)]{lang="EN-US"}

[  2     100.2.4.1          63 ms   Transit   100.4.5.1/\[3\] ReturnCode 8(1)]{lang="EN-US"}

[  3     100.4.5.1          129 ms  Egress    ReturnCode 3(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Destination address 127.1.1.2]{lang="EN-US"}

[  TTL   Replier            Time    Type      Downstream]{lang="EN-US"}

[  0                                Ingress   100.1.3.1/\[1030\]]{lang="EN-US"}

[  1     100.1.3.1          1 ms    Transit   100.3.4.1/\[1024\] ReturnCode 8(1)]{lang="EN-US"}

[  2     100.3.4.1          51 ms   Transit   100.4.5.1/\[3\] ReturnCode 8(1)]{lang="EN-US"}

[  3     100.4.5.1          80 ms   Egress    ReturnCode 3(1)]{lang="EN-US"}

[]{#struct_0_x1562_10515_x1866912014}[[表1-4 ]{lang="EN-US"}[tracert mpls ipv4]{lang="EN-US"}]{#_Ref329182432}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1068099619}[[字段]{lang="EN-US" style="font-family:
   黑体"}]{#struct_0_x1562_10515_144941287}
:::

[[描述]{lang="EN-US" style="font-family:黑体"}]{#struct_0_x1562_10515_1155422745}

[[MPLS trace route FEC]{lang="EN-US"}]{#struct_0_x1562_10515_x1046660269}

[[对指定]{style="font-family:宋体"}[FEC]{lang="EN-US"}]{#struct_0_x1562_10515_x420349024}[对应的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[进行]{style="font-family:宋体"}[Trace route]{lang="EN-US"}[操作]{style="font-family:宋体"}

[[Destination address]{lang="EN-US"}]{#struct_0_x1562_10515_1980766828}

[[IP]{lang="EN-US"}]{#struct_0_x1562_10515_1924096073}[头中的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_x1562_10515_x1149941073}

[[跳数]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_1037914852}

[[Replier]{lang="EN-US"}]{#struct_0_x1562_10515_1265385869}

[[应答的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1562_10515_x1002267916}[LSR]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_x1562_10515_x420938847}

[[接收到应答的时间，单位为毫秒]{style="font-family:宋体"}]{#struct_0_x1562_10515_2001905297}

[[Type]{lang="EN-US"}]{#struct_0_x1562_10515_1380474142}

[[LSR]{lang="EN-US"}]{#struct_0_x1562_10515_2023639382}[的类型，取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ingress]{lang="EN-US"}]{#struct_0_x1562_10515_581648652}[：入节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transit]{lang="EN-US"}]{#struct_0_x1562_10515_x420873311}[：中间节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Egress]{lang="EN-US"}]{#struct_0_x1562_10515_442130348}[：出节点]{lang="EN-US" style="font-family:宋体"}

[[Downstream]{lang="EN-US"}]{#struct_0_x1562_10515_x1500349289}

[[下游]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1562_10515_x1464025793}[地址及出标签值]{style="font-family:宋体"}

[[ReturnCode]{lang="EN-US"}]{#struct_0_x1562_10515_843873914}

[[返回码，括号内为返回子码]{style="font-family:宋体"}]{#struct_0_x1562_10515_x421069919}

[ ]{lang="EN-US"}

::: {#-2045195422 .myid}
[]{#_Toc404791722}[]{#struct_0_x1562_10515_1618268755}[]{#_Toc329867223}

**MPLS OAM \-- MPLS OAM配置命令 \-- tracert mpls te**

------------------------------------------------------------------------

[**[tracert mpls te]{lang="EN-US"}**]{#struct_0_x1562_10515_x1002198461}[命令用来查看]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道从]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点到]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点所经过的路径，并根据应答信息对错误点进行定位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_697467163}

[**[tracert mpls ]{lang="EN-US"}**[\[ **-a** *source-ip* \| **-exp** *exp-value* \| **-h** *ttl-value* \| **-r** *reply-mode* \| **-rtos** *tos-value* \| **-t** *time-out* \| **-v** \| **fec-check** \] \* **te** **tunnel** *interface-number*]{lang="EN-US"}]{#struct_0_x1562_10515_1618203219}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1753130902}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1562_10515_1024074993}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1823579797}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_677292783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x1235984594}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1618137683}

[**[-a]{lang="EN-US"}***[ source-ip]{lang="EN-US"}*]{#struct_0_x1562_10515_x978880104}[：指定发送的]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址。]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果没有指定本参数，则]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的源地址为报文出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[-exp]{lang="EN-US"}***[ exp-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x340131069}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中标签的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值。]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-h]{lang="EN-US"}***[ ttl-value]{lang="EN-US"}*]{#struct_0_x1562_10515_1256031584}[：指定]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文中]{style="font-family:宋体"}[TTL]{lang="EN-US"}[的最大值（即检测的最大跳数）。]{style="font-family:宋体"}*[ttl-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-r]{lang="EN-US"}[ ]{lang="EN-US"}***[reply-mode]{lang="EN-US"}*]{#struct_0_x1562_10515_1230942318}[：指定接收者对]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文的应答模式。]{style="font-family:宋体"}*[reply-mode]{lang="EN-US"}*[为应答模式，取值]{style="font-family:宋体"}[2]{lang="EN-US"}[和]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:
宋体"}[2]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文回应并携带]{style="font-family:宋体"}[Router Alert]{lang="EN-US"}[选项。缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-rtos]{lang="EN-US"}***[ tos-value]{lang="EN-US"}*]{#struct_0_x1562_10515_x850526933}[：指定]{style="font-family:宋体"}[MPLS echo reply]{lang="EN-US"}[报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值。]{style="font-family:宋体"}*[tos-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[ToS]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[-t]{lang="EN-US"}***[ time-out]{lang="EN-US"}*]{#struct_0_x1562_10515_1618596435}[：指定发送]{style="font-family:宋体"}[MPLS echo request]{lang="EN-US"}[报文后等待响应的超时时间。]{style="font-family:宋体"}*[time-out]{lang="EN-US"}*[为超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[-v]{lang="EN-US"}**]{#struct_0_x1562_10515_2112417208}[：指定显示详细的应答信息。如果没有指定本参数，则显示简要的应答信息。]{style="font-family:宋体"}

[**[fec-check]{lang="EN-US"}**]{#struct_0_x1562_10515_x374116925}[：指定在]{style="font-family:宋体"}[Transit]{lang="EN-US"}[节点上进行]{style="font-family:宋体"}[FEC]{lang="EN-US"}[栈检查。]{style="font-family:宋体"}

[**[tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_x1562_10515_90619292}[：]{style="font-family:宋体"}[查看指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口对应]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道经过的路径。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为已创建的模式为]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1743983811}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x642200046}[查看隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道从]{style="font-family:宋体"}[Ingress]{lang="EN-US"}[节点到]{style="font-family:宋体"}[Egress]{lang="EN-US"}[节点所经过的路径。]{style="font-family:宋体"}

[[\<Sysname\> tracert mpls te tunnel 1]{lang="FR"}]{#struct_0_x1562_10515_1618530899}

[MPLS trace route TE tunnel Tunnel1]{lang="FR"}

[  TTL   Replier            Time    Type      Downstream]{lang="FR"}

[  0                                Ingress   10.4.5.1/\[1025\]]{lang="FR"}

[  1     10.4.5.1           1 ms    Transit   100.3.4.1/\[1024\]]{lang="FR"}

[  2     100.3.4.1          63 ms   Transit   100.1.2.1/\[3\]]{lang="FR"}

[  3     100.1.2.1          129 ms  Egress]{lang="FR"}

[[显示信息中各字段的解释，请参见]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1032059768}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?1106107802#_Ref329182432)[。]{style="font-family:宋体"}
:::

::::: {#76344851 .myid}
[]{#_Toc404791723}[]{#struct_0_x1562_10515_x1108403738}[]{#_Toc366744534}[]{#_Toc366746464}[]{#_Toc366828618}[]{#_Toc336438868}[]{#_Toc336439015}[]{#_Toc336438869}[]{#_Toc336439016}[]{#_Toc336438870}[]{#_Toc336439017}[]{#_Toc336438871}[]{#_Toc336439018}[]{#_Toc336438872}[]{#_Toc336439019}[]{#_Toc336438873}[]{#_Toc336439020}[]{#_Toc336438874}[]{#_Toc336439021}[]{#_Toc336438875}[]{#_Toc336439022}[]{#_Toc336438876}[]{#_Toc336439023}[]{#_Toc336438877}[]{#_Toc336439024}[]{#_Toc336438878}[]{#_Toc336439025}[]{#_Toc336438879}[]{#_Toc336439026}[]{#_Toc336438880}[]{#_Toc336439027}[]{#_Toc336438881}[]{#_Toc336439028}[]{#_Toc336438882}[]{#_Toc336439029}[]{#_Toc336438883}[]{#_Toc336439030}[]{#_Toc336438884}[]{#_Toc336439031}[]{#_Toc336438885}[]{#_Toc336439032}[]{#_Toc336438886}[]{#_Toc336439033}[]{#_Toc336438887}[]{#_Toc336439034}[]{#_Toc336438888}[]{#_Toc336439035}[]{#_Toc336438889}[]{#_Toc336439036}[]{#_Toc336438890}[]{#_Toc336439037}[]{#_Toc336438891}[]{#_Toc336439038}[]{#_Toc336438892}[]{#_Toc336439039}[]{#_Toc336438893}[]{#_Toc336439040}[]{#_Toc336438894}[]{#_Toc336439041}[]{#_Toc336438895}[]{#_Toc336439042}[]{#_Toc336438896}[]{#_Toc336439043}

**MPLS OAM \-- MPLS OAM配置命令 \-- vccv bfd**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20OAM命令.files/image001.png){#图片 10 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1562_10515_181488775}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1562_10515_x1330087749}
:::

[ ]{lang="EN-US"}

[**[vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1124517992}[命令用来配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[**[undo vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1867169451}[用来取消使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x2007555211}

[**[vccv bfd ]{lang="EN-US"}**[\[ **raw-bfd** \] \[ **template** *template-name* \]]{lang="EN-US"}]{#struct_0_x1562_10515_655057402}

[**[undo vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1675637848}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x421004383}

[[未使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1562_10515_x316396032}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1944536203}

[[PW]{lang="EN-US"}]{#struct_0_x1562_10515_552569174}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1511168064}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_1416210915}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_2083980646}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x869242460}

[**[raw-bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1680017874}[：指定]{style="font-family:宋体"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[PW-ACH Encapsulation (without IP/UDP Headers)]{lang="EN-US"}[，即封装在]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道内的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文不携带]{style="font-family:宋体"}[IP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头。只有控制通道]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}**[control-word]{lang="EN-US"}**[时，指定本参数才会生效。]{style="font-family:宋体"}[如果没有指定本参数，则]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文的封装方式为]{style="font-family:宋体"}[IP/UDP Encapsulation (with IP/UDP Headers)]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[template ]{lang="EN-US"}***[template-]{lang="EN-US"}[name]{lang="EN-US"}*]{#struct_0_x1562_10515_x420676703}[：指定引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板。]{style="font-family:宋体"}*[template-]{lang="EN-US"}[name]{lang="EN-US"}*[为]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1082189724}

[[将]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1749873834}[与指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板关联，并在该]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图下执行本命令后，是否使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测该]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性以及]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文采用何种封装方式，由两端的配置共同决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两端]{style="font-family:宋体"}]{#struct_0_x1562_10515_1174561136}[PE]{lang="EN-US"}[上都配置了]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[且]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文封装方式相同，则采用该封装方式检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[否则，不使用]{style="font-family:宋体"}]{#struct_0_x1562_10515_x156844088}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1546313559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[要想建立检测]{style="font-family:宋体"}]{#struct_0_x1562_10515_x1221932495}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，两端设备上都需要执行]{style="font-family:宋体"}**[vccv bfd]{lang="EN-US"}**[命令，并执行]{style="font-family:宋体"}**[mpls bfd enable]{lang="EN-US"}**[命令使能]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行本命令时，如果没有指定]{lang="EN-US" style="font-family:宋体"}**[template ]{lang="EN-US"}***[te]{lang="EN-US"}[mplate-name]{lang="EN-US"}*]{#struct_0_x1562_10515_2033922682}[参数，则]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话使用系统视图下配置的多跳]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1226051457}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x420611167}[配置使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测]{style="font-family:宋体"}[PW]{lang="EN-US"}[的连通性，指定]{style="font-family:宋体"}[BFD]{lang="EN-US"}[报文封装方式为]{style="font-family:宋体"}[raw-bfd]{lang="EN-US"}[，并指定引用的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话参数模板为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_x342264265}

[\[Sysname\] pw-class test]{lang="EN-US"}

[\[Sysname-pw-test\] vccv bfd raw-bfd template aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1161510458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_x1589751002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_1822665998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_1136645588}
:::::

::::: {#2030980068 .myid}
[]{#_Toc404791724}[]{#struct_0_x1562_10515_x889532966}

**MPLS OAM \-- MPLS OAM配置命令 \-- vccv cc**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](MPLS%20OAM命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1562_10515_x1575265385}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1562_10515_x1716010452}
:::

[ ]{lang="EN-US"}

[**[vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_x420807775}[命令用来配置]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型。]{style="font-family:宋体"}

[**[undo vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_1644137790}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_961019046}

[**[vccv cc ]{lang="EN-US"}**[{ **control-word** \| **router-alert** \| **ttl** }]{lang="EN-US"}]{#struct_0_x1562_10515_x452648173}

[**[undo vccv cc]{lang="EN-US"}**]{#struct_0_x1562_10515_x1415473244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x644880309}

[[没有指定]{style="font-family:宋体"}[VCCV]{lang="EN-US"}]{#struct_0_x1562_10515_929370577}[控制通道类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1859048492}

[[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1835349536}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x420742239}

[[network-admin]{lang="EN-US"}]{#struct_0_x1562_10515_x324736332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1562_10515_138221640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1562_10515_x1978113814}

[**[control-word]{lang="EN-US"}**]{#struct_0_x1562_10515_1297521110}[：指定]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[类型为控制字类型。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[router-alert]{lang="EN-US"}**]{#struct_0_x1562_10515_x305863824}[：指定]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[类型为]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由器告警标签类型。]{style="font-family:宋体"}

[**[ttl]{lang="EN-US"}**]{#struct_0_x1562_10515_462912845}**[：]{style="font-family:宋体"}**[指定]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型，即]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值等于]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1562_10515_522175312}

[[用来检测]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_1356890454}[连通性的报文统称为]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文。]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[CC]{lang="EN-US"}[（]{style="font-family:宋体"}[Control Channel]{lang="EN-US"}[，控制通道）来传送]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[CC]{lang="EN-US"}]{#struct_0_x1562_10515_x420414559}[有以下几种类型：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[control-word]{lang="EN-US"}**]{#struct_0_x1562_10515_x1867370769}[类型：通过控制字，即]{style="font-family:宋体"}[PW-ACH]{lang="EN-US"}[（]{style="font-family:宋体"}[PW Associated Channel Header]{lang="EN-US"}[，]{style="font-family:宋体"}[PW]{lang="EN-US"}[随路通道首部），标识]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文。只有]{style="font-family:宋体"}[PW]{lang="EN-US"}[支持控制字时，才能选择这种类型。控制字的详细介绍，请参见"]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[MPLS L2VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[router-alert]{lang="EN-US"}**]{#struct_0_x1562_10515_x1319755770}[类型：通过在]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签之前携带]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[路由器告警标签来标识]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ttl]{lang="EN-US"}**]{#struct_0_x1562_10515_x1005275875}[类型：通过将]{style="font-family:
宋体"}[PW]{lang="EN-US"}[标签的]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[来标识]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[将]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_x1562_10515_x1084152780}[与指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板关联，并在该]{style="font-family:宋体"}[PW]{lang="EN-US"}[模板视图下执行本命令后，该]{style="font-family:宋体"}[PW]{lang="EN-US"}[是否使用指定的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[，由两端的配置共同决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果两端]{style="font-family:宋体"}]{#struct_0_x1562_10515_1026223423}[PE]{lang="EN-US"}[上配置了相同的]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[类型，则使用该]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[否则，不使用任何]{style="font-family:宋体"}]{#struct_0_x1562_10515_332698097}[VCCV]{lang="EN-US"}[控制通道]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1562_10515_411904574}

[[\# ]{lang="EN-US"}]{#struct_0_x1562_10515_x401912337}[配置]{style="font-family:宋体"}[VCCV]{lang="EN-US"}[控制通道类型为]{style="font-family:宋体"}[TTL]{lang="EN-US"}[超时类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1562_10515_x420349023}

[\[Sysname\] pw-class test]{lang="EN-US"}

[\[Sysname-pw-test\] vccv cc ttl]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1562_10515_1980308076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn pw bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_1938346684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mpls bfd enable]{lang="EN-US"}**]{#struct_0_x1562_10515_x153342976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vccv bfd]{lang="EN-US"}**]{#struct_0_x1562_10515_290982137}

[ ]{lang="EN-US"}
:::::
