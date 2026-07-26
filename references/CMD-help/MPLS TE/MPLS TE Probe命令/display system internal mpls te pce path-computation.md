::: {#-1848213911 .myid}
[]{#_Toc404799878}[]{#struct_0_11341_x1459_1506434717}[]{#_Toc395683269}[]{#_Toc365359825}

**MPLS TE \-- MPLS TE Probe命令 \-- display system internal mpls te pce path-computation**

------------------------------------------------------------------------

[**[display system internal mpls te pce path-computation]{lang="EN-US"}**]{#struct_0_11341_x1459_x832217452}[命令用来显示]{style="font-family:宋体"}[PCE]{lang="EN-US"}[路径计算过程的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11341_x1459_884507675}

[**[display system internal mpls te pce path-computation ]{lang="EN-US"}**[\[ **source**]{lang="EN-US"}**[ ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[destination ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_11341_x1459_312189378}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11341_x1459_894535615}

[[Probe]{lang="EN-US"}]{#struct_0_11341_x1459_x832217451}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11341_x1459_884442139}

[[network-admin]{lang="EN-US"}]{#struct_0_11341_x1459_309973391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_11341_x1459_x832217450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11341_x1459_884376603}

[**[source]{lang="EN-US"}[ ]{lang="EN-US"}***[ip-ddress]{lang="EN-US"}*]{#struct_0_11341_x1459_1233887671}[：]{style="font-family:宋体"}[指定计算路径的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_11341_x1459_x2141473209}[：]{style="font-family:宋体"}[指定计算路径的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}
:::

::: {#-1132018162 .myid}
[]{#_Toc361151985}[]{#_Toc354415015}[]{#_Toc404799879}[]{#struct_0_11341_x1459_87835851}[]{#_Toc366002383}[]{#_Toc360021292}[]{#_Toc347149196}[]{#_Toc317060393}[]{#_Toc249440373}

**MPLS TE \-- MPLS TE Probe命令 \-- mpls te path-calculation**

------------------------------------------------------------------------

[**[mpls te path-calculation]{lang="FR"}**]{#struct_0_11341_x1459_1060155264}[命令用来]{style="font-family:宋体"}[根据指定的约束条件进行]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算并返回计算结果。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_11341_x1459_x1025664330}

[**[mpls te path-calculation]{lang="EN-US"}**[ { **destination** *address* \| **tunnel-interface** **tunnel** *number* \[ **destination** *address* \] } \[ **bandwidth** \[ **ct0** \| **ct1** \| **ct2** \| **ct3** \] *bandwidth-value* \] \[ **priority** *setup-priority* \[ *hold-priority* \] \] \[ **affinity** *attribute-value* \[ **mask** *mask-value* \] \]]{lang="EN-US"}]{#struct_0_11341_x1459_114929257}

[[【视图】]{style="font-family:黑体"}]{#struct_0_11341_x1459_871783139}

[[Probe]{lang="FR"}]{#struct_0_11341_x1459_543337233}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_11341_x1459_x312349325}

[[network-admin]{lang="FR"}]{#struct_0_11341_x1459_1030554235}

[[mdc-admin]{lang="FR"}]{#struct_0_11341_x1459_2052866571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_11341_x1459_x1465820179}

[**[destination]{lang="FR"}**]{#struct_0_11341_x1459_1073360932}*[ address]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算的目的地址。]{style="font-family:宋体"}

[**[tunnel-interface tunnel]{lang="FR"}**]{#struct_0_11341_x1459_1377449261}*[ number]{lang="FR"}*[：]{style="font-family:
宋体"}[从指定]{style="font-family:宋体"}[Tunnel]{lang="FR"}[接口获取]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算使用的约束条件。]{style="font-family:宋体"}*[number]{lang="FR"}*[为]{style="font-family:宋体"}[Tunnel]{lang="FR"}[接口的编号，]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[bandwidth]{lang="FR"}**]{#struct_0_11341_x1459_1982601998}[ \[ **ct0** \| **ct1** \| **ct2** \| **ct3** \] *bandwidth-value*]{lang="FR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算需要满足的带宽条件。如果没有指定任何]{style="font-family:宋体"}[CT]{lang="FR"}[，]{style="font-family:宋体"}[则隧道流量属于]{style="font-family:
宋体"}[CT 0]{lang="FR"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ct0]{lang="EN-US"}**]{#struct_0_11341_x1459_1805970386}[：]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道流量属于]{lang="EN-US" style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ct1]{lang="EN-US"}**]{#struct_0_11341_x1459_x691658037}[：]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道流量属于]{lang="EN-US" style="font-family:宋体"}[CT 1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ct2]{lang="EN-US"}**]{#struct_0_11341_x1459_x975863411}[：]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道流量属于]{lang="EN-US" style="font-family:宋体"}[CT 2]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ct3]{lang="EN-US"}**]{#struct_0_11341_x1459_711096221}[：]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[隧道流量属于]{lang="EN-US" style="font-family:宋体"}[CT 3]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bandwidth-value]{lang="FR"}*]{#struct_0_11341_x1459_x1003879597}[：]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道所需的带宽，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为]{lang="EN-US" style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[priority]{lang="FR"}**]{#struct_0_11341_x1459_593235237}[ *setup-priority* \[ *hold-priority* \]]{lang="FR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算的建立优先级和保持优先级。]{style="font-family:宋体"}*[setup-priority]{lang="FR"}*[为]{style="font-family:宋体"}[建立优先级]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[7]{lang="FR"}[；]{style="font-family:
宋体"}*[hold-priority]{lang="FR"}*[为保持优先级]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[7]{lang="FR"}[。数值越小优先级越高。如果不指定]{style="font-family:宋体"}*[hold-priority]{lang="EN-US"}*[参数，则保持优先级与建立优先级相同。]{style="font-family:宋体"}

[**[affinity]{lang="EN-US"}**[ *attribute-value* \[ **mask** *mask-value* \]]{lang="EN-US"}]{#struct_0_11341_x1459_610790775}[：指定]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[计算的亲和属性及其掩码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attribute-value]{lang="EN-US"}*]{#struct_0_11341_x1459_1234986208}[为亲和属性，取值范围为]{style="font-family:宋体"}[0x00000000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFFFF]{lang="EN-US"}[，即为]{style="font-family:宋体"}[32]{lang="EN-US"}[位的二进制数。亲和属性中的每一位二进制数代表一种属性，属性值为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-value]{lang="EN-US"}*]{#struct_0_11341_x1459_x692901186}[为亲和属性掩码，取值范围为]{style="font-family:宋体"}[0x00000000]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFFFFFFFF]{lang="EN-US"}[，即为]{style="font-family:宋体"}[32]{lang="EN-US"}[位的二进制数。掩码中的每一位二进制数都表示是否检查该位的链路属性。掩码为]{style="font-family:宋体"}[1]{lang="EN-US"}[，表示需要检查该位的链路属性，只有该位的链路属性满足一定条件时，才可以使用该链路；掩码为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示不检查该位的链路属性，不管该位的链路属性与隧道的亲和属性是否相同，都可以使用该链路。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_11341_x1459_1073033252}

[[通过本命令可以指定的]{style="font-family:宋体"}]{#struct_0_11341_x1459_x991581787}[CSPF]{lang="FR"}[计算约束条件包括隧道所需带宽、优先级和亲和属性。约束条件可以通过以下两种方式指定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_11341_x1459_x1049972365}**[tunnel]{lang="FR"}***[ number]{lang="FR"}*[参数，采用该]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="FR"}[接口下配置的约束条件进行]{lang="EN-US" style="font-family:宋体"}[CSPF]{lang="FR"}[计算。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[通过指定]{style="font-family:宋体"}]{#struct_0_11341_x1459_x751950673}**[destination]{lang="FR"}**[、]{style="font-family:宋体"}**[bandwidth]{lang="FR"}**[、]{style="font-family:宋体"}**[priority]{lang="FR"}**[或]{style="font-family:宋体"}**[affinity]{lang="EN-US"}**[参数，手工指定]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[计算的约束条件。]{style="font-family:宋体"}

[[手工指定的约束条件优先级高于通过]{style="font-family:宋体"}]{#struct_0_11341_x1459_x55577878}[Tunnel]{lang="FR"}[接口获取的约束条件，即如果在指定]{style="font-family:宋体"}**[tunnel]{lang="FR"}***[ number]{lang="FR"}*[参数的同时，指定了]{style="font-family:宋体"}**[destination]{lang="FR"}**[、]{style="font-family:宋体"}**[bandwidth]{lang="FR"}**[、]{style="font-family:宋体"}**[priority]{lang="FR"}**[或]{style="font-family:宋体"}**[affinity]{lang="FR"}**[参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则采用手工指定的约束条件进行]{style="font-family:宋体"}[CSPF]{lang="FR"}[计算。]{style="font-family:宋体"}
:::
