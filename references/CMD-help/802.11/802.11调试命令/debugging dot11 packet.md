::::: {#-1966226442 .myid}
[]{#_Toc404795307}[]{#struct_0_x1161_x7119_586163531}

**802.11 \-- 802.11调试命令 \-- debugging dot11 packet**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](802.11%20Debug.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1161_x7119_x1308783980}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1161_x7119_x1298351219}
:::

[ ]{lang="EN-US"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1161_x7119_192206353}

[**[debugging dot11 ]{lang="EN-US"}[packet]{lang="EN-US"}**]{#struct_0_x1161_x7119_895193522}

[**[undo debugging dot11]{lang="EN-US"}**[ **packet**]{lang="EN-US"}]{#struct_0_x1161_x7119_891680956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1161_x7119_1420475270}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1161_x7119_x1090005624}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1161_x7119_1362414401}

[[无]{style="font-family:宋体"}]{#struct_0_x1161_x7119_77342132}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1161_x7119_1420475269}

[]{#_Toc130718926}[**[debugging dot11]{lang="EN-US"}**[ **packet**]{lang="EN-US"}]{#struct_0_x1161_x7119_x1090464375}[命令用来打开]{style="font-family:宋体"}[802.11]{lang="EN-US"}[协议报文监听的调试信息开关。]{style="font-family:宋体"}**[undo debugging dot11]{lang="EN-US"}**[ **packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[802.11]{lang="EN-US"}[协议报文监听的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[802.11]{lang="EN-US"}]{#struct_0_x1161_x7119_x1791531361}[协议报文监听的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging dot11 packet]{lang="EN-US"}]{#struct_0_x1161_x7119_1017941228}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x719345104}[[字段]{style="font-family:黑体"}]{#struct_0_x1161_x7119_1420475268}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1161_x7119_x1090529911}

[[DOT11_moniter: Matched  a 802.11 protocol packet]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475267}

[[特征匹配到一个]{style="font-family:宋体"}[802.11]{lang="EN-US"}]{#struct_0_x1161_x7119_x1089809015}[协议报文]{style="font-family:宋体"}

[[Action: *action*]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475274}

[[特征对报文的处理动作，有以下处理方式：]{style="font-family:宋体"}]{#struct_0_x1161_x7119_x1089743480}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forward]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475273}[：继续转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redirect]{lang="EN-US"}]{#struct_0_x1161_x7119_x1090071160}[：重定向]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Copy]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475272}[：复制]{lang="EN-US" style="font-family:宋体"}

[[Characteristics flag: x]{lang="EN-US"}]{#struct_0_x1161_x7119_x1090136696}

[[特征有效字段标记，用]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475271}[进制格式打印]{style="font-family:宋体"}

[[Priority: *priority*]{lang="EN-US"}]{#struct_0_x1161_x7119_x1089940088}

[[特征的优先级，数值越大优先级越高]{style="font-family:宋体"}]{#struct_0_x1161_x7119_1420475278}

[[Phase: *phase*]{lang="EN-US"}]{#struct_0_x1161_x7119_1420475277}

[[特征的侦听阶段，有以下几个阶段：]{style="font-family:宋体"}]{#struct_0_x1161_x7119_x1089809016}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Radio_Recv]{lang="EN-US"}]{#struct_0_x1161_x7119_x535839866}[：]{lang="EN-US" style="font-family:宋体"}[Radio]{lang="EN-US"}[入方向侦听阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BSS_Recv]{lang="EN-US"}]{#struct_0_x1161_x7119_1691030353}[：]{lang="EN-US" style="font-family:宋体"}[BSS]{lang="EN-US"}[入方向侦听阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BSS_Send]{lang="EN-US"}]{#struct_0_x1161_x7119_x535839867}[：]{lang="EN-US" style="font-family:宋体"}[BSS]{lang="EN-US"}[出方向侦听阶段]{lang="EN-US" style="font-family:宋体"}

[[Context\[0\]]{lang="EN-US"}]{#struct_0_x1161_x7119_x535839868}

[[特征上下文]{style="font-family:宋体"}]{#struct_0_x1161_x7119_1691947857}

[[Context\[1\]]{lang="EN-US"}]{#struct_0_x1161_x7119_x535839869}

[[特征上下文]{style="font-family:宋体"}]{#struct_0_x1161_x7119_x535839862}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1161_x7119_1691292497}

[[\# ]{lang="EN-US"}]{#struct_0_x1161_x7119_1723494321}[在设备上打开]{style="font-family:宋体"}[802.11]{lang="EN-US"}[协议报文监听的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging dot11 packet]{lang="EN-US"}]{#struct_0_x1161_x7119_x535839863}

[\*Dec 8 09:58:04:957 2013 Sysname DOT11/7/DOT11_moniter: Matched a 802.11 protocol packet, Action: Redirect, Characteristics flag: 0x8000, Priority: 64, Phase: BSS_Recv, Context\[0\]: 0x0, Context\[1\]: 0x1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1161_x7119_1691226961}*[匹配到一个符合]{style="font-family:宋体"}[802.11]{lang="EN-US"}[特征的报文，特征序列号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[，报文特征地址有效字段为]{style="font-family:宋体"}[0x8000]{lang="EN-US"}[，对报文的处理动作为重定向。]{style="font-family:宋体"}*
