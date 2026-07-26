::: {#-1345648796 .myid}
[]{#_Toc404793889}[]{#struct_0_x2007_x2076_x1505620401}

**uRPF \-- uRPF调试命令 \-- debugging ip urpf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_1253386532}

[**[debugging ip urpf ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2007_x2076_318335381}

[**[undo debugging ip urpf ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2007_x2076_x1421411851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1647933010}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2007_x2076_468781449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_432878441}

[[network-admin]{lang="EN-US"}]{#struct_0_x2007_x2076_1405373653}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2007_x2076_x1090998417}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1551252169}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2007_x2076_x641314561}[：指定的接口类型和编号。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1890238822}

[**[debugging ip urpf]{lang="EN-US"}**]{#struct_0_x2007_x2076_x1224091958}[命令用来打开]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ip urpf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[uRPF]{lang="EN-US"}]{#struct_0_x2007_x2076_x483840677}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x2007_x2076_x1647867474}[[表1-1 ]{lang="EN-US"}[debugging ip urpf]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2049584392}[[字段]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1028094142}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2007_x2076_818226291}

[[uRPF  uRPF-Discard: Packet from *ip-address* via *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2007_x2076_1705814024}

[[从指定接口收到的源地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2007_x2076_x1839336113}[的报文被丢弃]{style="font-family:宋体"}

[[uRPF  uRPF-Discard-Suppress: Packet from *ip-address* via *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2007_x2076_x748860233}

[[从指定接口收到的源地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2007_x2076_x748351020}[的报文被]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[抑制后，匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则成功，然后被转发]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1648064082}

[[\# ]{lang="EN-US"}]{#struct_0_x2007_x2076_1986764401}[在一台启动了]{style="font-family:宋体"}[uRPF]{lang="EN-US"}[调试信息开关的设备上，收到源地址不可识别的报文，则打印以下调试信息。]{style="font-family:宋体"}

[[[\<Sysname\> debugging ip urpf]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}]{#struct_0_x2007_x2076_1888831869}

[\*0.3933516 Sysname URPF/7/debug_info:]{lang="EN-US"}

[ uRPF uRPF-Discard: Packet from 2.2.2.5 via GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2007_x2076_x423433461}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的源地址为]{style="font-family:宋体"}[2.2.2.5]{lang="EN-US"}[的报文被丢弃]{style="font-family:宋体"}*

*[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}*

::: {.Section3 style="layout-grid:15.75pt"}
:::

::: {#291808326 .myid}
[]{#_Toc404793892}[]{#struct_0_x2007_x2076_x546251390}

**IPv6 uRPF \-- IPv6 uRPF调试命令 \-- debugging ipv6 urpf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_355173695}

[**[debugging ipv6 urpf ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2007_x2076_1715167506}

[**[undo debugging ipv6 urpf ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2007_x2076_x1647998546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_1655165058}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2007_x2076_338157037}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_482963284}

[[network-admin]{lang="EN-US"}]{#struct_0_x2007_x2076_251267285}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2007_x2076_2141523890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x494812460}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2007_x2076_x1132315279}[：指定的接口类型和编号。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_264041868}

[**[debugging ipv6 urpf]{lang="EN-US"}**]{#struct_0_x2007_x2076_x1647670866}[命令用来打开]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 urpf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}]{#struct_0_x2007_x2076_x472088749}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表2-1 ]{lang="EN-US"}[debugging ipv6 urpf]{lang="EN-US"}]{#struct_0_x2007_x2076_1469734079}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2050437128}[[字段]{style="font-family:黑体"}]{#struct_0_x2007_x2076_x1467603490}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2007_x2076_1228288185}

[[uRPF6  uRPF6-Discard: Packet from *ipv6-address* via *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2007_x2076_x1186277134}

[[从指定接口收到的源地址为]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_x2007_x2076_x240581698}[的报文被丢弃]{style="font-family:宋体"}

[[uRPF6  uRPF6-Discard-Suppress: Packet from *ipv6-address* via *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2007_x2076_312247763}

[[从指定接口收到的源地址为]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_x2007_x2076_x1647605330}[的报文被]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[抑制后，匹配]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[规则成功，然后被转发]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2007_x2076_1553648347}

[[\# ]{lang="EN-US"}]{#struct_0_x2007_x2076_x1605514846}[在一台启动了]{style="font-family:宋体"}[IPv6 uRPF]{lang="EN-US"}[调试信息开关的设备上，收到源地址不可识别的报文，则打印以下调试信息。]{style="font-family:宋体"}

[[[\<Sysname\>debugging ipv6 urpf]{lang="EN-US" style="font-size:8.5pt"}]{.TerminalDisplayChar}]{#struct_0_x2007_x2076_x495185885}

[\*0.3933516 Sysname URPF6/7/debug_info:]{lang="EN-US"}

[ uRPF6 uRPF6-Discard: Packet from 2000::5 via GigabitEthernet1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2007_x2076_x1904704661}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的源地址为]{style="font-family:宋体"}[2000::5]{lang="EN-US"}[的报文被丢弃]{style="font-family:宋体"}*
