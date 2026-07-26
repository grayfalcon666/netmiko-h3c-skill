::: {#7139293 .myid}
[]{#_Toc404800353}[]{#struct_0_19763_17727_58078993}[]{#_Toc361151985}[]{#_Toc354415015}[]{#_Toc300843382}[]{#_Toc300843383}[]{#_Toc307388003}[]{#_Toc307232835}[]{#_Toc339885941}[]{#_Toc339885942}[]{#_Toc339885943}[]{#_Toc339885944}[]{#_Toc339885945}[]{#_Toc339885946}[]{#_Toc339885947}[]{#_Toc339885948}[]{#_Toc339885949}[]{#_Toc339885950}[]{#_Toc339885951}[]{#_Toc339885952}[]{#_Toc339885953}[]{#_Toc339885954}[]{#_Toc339885955}[]{#_Toc339885956}[]{#_Toc339885969}

**VPLS \-- VPLS Probe命令 \-- display system internal l2vpn ldp**

------------------------------------------------------------------------

[**[display system internal l2vpn ldp]{lang="EN-US"}**]{#struct_0_19763_17727_1019358484}[命令用来显示]{style="font-family:宋体"}[LDP]{lang="EN-US"}[协议备进程的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19763_17727_x1769887208}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_19763_17727_1079336761}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display system internal l2vpn ldp ]{lang="EN-US"}**[\[ **peer** *ip-address* \[ **pw-id** *pw-id* \| **vpls-id** *vpls-id* \] \] \[ **verbose** \]]{lang="EN-US"}[  **standby slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_19763_17727_x1436880694}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_19763_17727_x325941081}[模式：]{style="font-family:宋体"}

[**[display system internal l2vpn ldp ]{lang="EN-US"}**[\[ **peer** *ip-address* \[ **pw-id** *pw-id* \| **vpls-id** *vpls-id* \] \] \[ **verbose** \]]{lang="EN-US"}[ **standby chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_19763_17727_x1418103200}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19763_17727_x1872380795}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19763_17727_x1204489340}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19763_17727_x1308758750}

[[network-admin]{lang="EN-US"}]{#struct_0_19763_17727_x705907394}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19763_17727_2071220126}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19763_17727_1079533369}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_19763_17727_x1432246023}[：显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[的]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[。如果没有指定本参数，则显示所有远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_19763_17727_1544884236}[：显示指定]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。本参数和]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[参数配合使用，如果只指定了]{style="font-family:宋体"}**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[参数，则显示指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[通过]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告的所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*]{#struct_0_19763_17727_493252708}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}*[vpls-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[，即]{style="font-family:宋体"}[VPLS]{lang="EN-US"}[实例标识符，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:
宋体"}[21]{lang="EN-US"}[个字符的字符串，]{style="font-family:宋体"}[VPLS ID]{lang="EN-US"}[有三种格式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_19763_17727_1440391778}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_19763_17727_x1788823405}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_19763_17727_1054508533}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数字，其中的自治系统号最小值为]{style="font-family:宋体"}[65536]{lang="EN-US"}[。例如：]{style="font-family:宋体"}[65536:1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_19763_17727_x106182331}[：]{style="font-family:宋体"}[显示详细信息。如果不指定本参数，则显示简要信息。]{style="font-family:宋体"}

[**[standby]{lang="EN-US"}**]{#struct_0_19763_17727_1079467833}**[：]{style="font-family:宋体"}**[显示指定]{style="font-family:宋体"}[LDP]{lang="EN-US"}[备进程的信息。]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_19763_17727_77953931}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[指定备进程所在的主控板。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为主控板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="PT-BR"}**]{#struct_0_19763_17727_x2019366312}*[ slot-number]{lang="PT-BR"}*[：]{style="font-family:宋体"}[指定备进程所在的成员设备。]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[为设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis ]{lang="PT-BR"}**]{#struct_0_19763_17727_x1386494537}*[chassis-number]{lang="PT-BR"}*[ **slot** *slot-number*]{lang="PT-BR"}[：]{style="font-family:宋体"}[指定备进程所在的成员设备和主控板。]{style="font-family:宋体"}*[chassis-number]{lang="PT-BR"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="PT-BR"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="PT-BR"}*[表示主控板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_19763_17727_80060947}[：]{style="font-family:
宋体"}[指定备进程所在的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19763_17727_x1558190967}

[[LDP]{lang="EN-US"}]{#struct_0_19763_17727_1598972622}[可以通过如下两种方式通告]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_19763_17727_1915579985}**[peer]{lang="EN-US"}**[命令手工指定远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的绑定关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[采用]{style="font-family:宋体"}]{#struct_0_19763_17727_417543367}[BGP]{lang="EN-US"}[协议自动发现远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[通告]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[和]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签的绑定关系。]{style="font-family:宋体"}

[[本命令可以用来显示通过上述两种方式通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_19763_17727_601265446}[标签。]{style="font-family:宋体"}

[[执行本命令时，如果指定了]{style="font-family:宋体"}**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*]{#struct_0_19763_17727_1079664441}[参数，则显示指定]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息；如果指定了]{style="font-family:宋体"}**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*[参数，则]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息；如果没有指定]{style="font-family:宋体"}**[pw-id ]{lang="EN-US"}***[pw-id]{lang="EN-US"}*[和]{style="font-family:宋体"}**[vpls-id ]{lang="EN-US"}***[vpls-id]{lang="EN-US"}*[参数，则同时显示]{style="font-family:宋体"}[FEC 128]{lang="EN-US"}[方式和]{style="font-family:宋体"}[FEC 129]{lang="EN-US"}[方式的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签相关信息。]{style="font-family:宋体"}

[[执行本命令时，本设备接收到的]{style="font-family:宋体"}[LDP PW]{lang="EN-US"}]{#struct_0_19763_17727_x650115283}[标签映射信息都会显示；而本设备通告的]{style="font-family:宋体"}[PW]{lang="EN-US"}[标签映射只有成功通告给远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[后才会显示。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
