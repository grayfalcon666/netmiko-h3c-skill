::: {#-389127736 .myid}
[]{#_Toc404793914}[]{#struct_0_x1753_19767_1298088657}[]{#_Toc341864677}

**MFF \-- MFF调试命令 \-- debugging mac-forced-forwarding**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1753_19767_x1243761704}

[**[debugging mac-forced-forwarding]{lang="EN-US"}**]{#struct_0_x1753_19767_1492961933}

[**[undo debugging mac-forced-forwarding]{lang="EN-US"}**]{#struct_0_x1753_19767_1379853034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1753_19767_180922523}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1753_19767_x1018860752}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1753_19767_x1740651052}

[[network-admin]{lang="EN-US"}]{#struct_0_x1753_19767_221337973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1753_19767_1628252223}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1753_19767_932453717}

[**[debugging mac-forced-forwarding]{lang="EN-US"}**]{#struct_0_x1753_19767_x1044587323}[命令用来开启]{style="font-family:宋体"}[MFF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging mac-forced-forwarding]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MFF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MFF]{lang="EN-US"}]{#struct_0_x1753_19767_1295667975}[调试开关处于关闭状态]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mac-forced-forwarding]{lang="EN-US"}]{#struct_0_x1753_19767_x949170945}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1976399917}[[字段]{style="font-family:黑体"}]{#struct_0_x1753_19767_551162055}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1753_19767_x2054884117}

[[SendType:*send-type*    VLAN ID :*vlan-id*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1753_19767_569248766}

[[SrcMAC:*src-MAC-address*    SrcIP : *src-ip-address*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1753_19767_221403509}

[[DstMAC:*dst-MAC-address*    DstIP: *dst-ip-address*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1753_19767_751392366}

[[PacketType : *packet-type*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1753_19767_2101841592}

[[MFF]{lang="EN-US"}]{#struct_0_x1753_19767_x354448635}[发送报文的发送类型、接口所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、源]{style="font-family:宋体"}[IP]{lang="EN-US"}[、源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[、目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[以及报文类型]{style="font-family:宋体"}

[[动作类型：]{style="font-family:宋体"}]{#struct_0_x1753_19767_1123915618}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_VLAN]{lang="EN-US"}]{#struct_0_x1753_19767_792974569}[：]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[内广播]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_VLAN_EX_SRCPORT]{lang="EN-US"}]{#struct_0_x1753_19767_1658764221}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[内排除源端口广播]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_USER]{lang="EN-US"}]{#struct_0_x1753_19767_221469045}[：遍历用户端口广播]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_NETWORK]{lang="EN-US"}]{#struct_0_x1753_19767_1897724139}[：遍历网络端口广播]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_NETWORK_EX_SRC]{lang="EN-US"}]{#struct_0_x1753_19767_1083648699}[：向下行网络端口广播]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_SENDTYPE_UNICAST]{lang="EN-US"}]{#struct_0_x1753_19767_x1216490913}[：单播]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MFF_RECPKT]{lang="EN-US"}]{#struct_0_x1753_19767_x1262754154}[：收到报文开始处理]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文类型：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1753_19767_x1532273244}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REPLY]{lang="EN-US"}]{#struct_0_x1753_19767_221534581}[：应答]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_x1753_19767_x9087535}[：请求]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRATUITOUS]{lang="EN-US"}]{#struct_0_x1753_19767_x692871667}[：免费]{lang="EN-US" style="font-family:宋体"}[ARP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1753_19767_51950091}

[[\# ]{lang="EN-US"}]{#struct_0_x1753_19767_x1200279815}[在设备上开启]{style="font-family:宋体"}[MFF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-forced-forwarding]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1753_19767_x1066832559}

[[\*Aug  7 11:55:26:906 2011 Sysname ARP/7/]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1753_19767_x873045387}[MFF: -MDC=1]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\""}

[[SendType   :MFF_SENDTYPE_VLAN_EX_SRCPORT       VLAN ID :100]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1753_19767_221600117}

[[ SrcMAC     :000d-5619-f7bc                     SrcIP   :100.1.1.1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1753_19767_1025737744}

[[ DstMAC     :0000-0000-0000                     DstIP   :100.1.1.100]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1753_19767_860143336}

[[ PacketType :REQUEST]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1753_19767_x576534415}

[ ]{lang="EN-US"}
