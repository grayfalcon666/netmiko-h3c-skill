::: {#642268123 .myid}
[]{#_Toc132549861}[]{#_Toc122421146}[]{#_Toc59352309}[]{#_Toc59352314}[]{#_Toc404793860}[]{#struct_0_53887_18384_x681949418}[]{#_Toc234836598}[]{#_Toc154550815}[]{#_Toc154550818}[]{#_Toc154550820}[]{#_Toc154550821}[]{#_Toc154550824}[]{#_Toc154550826}[]{#_Toc154550827}

**ND攻击防御 \-- ND攻击防御调试命令 \-- debugging ipv6 nd detection packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_53887_18384_x314305264}

[**[debugging ipv6 nd detection packet]{lang="EN-US"}**]{#struct_0_53887_18384_846667996}

[**[undo debugging ipv6 nd detection packet]{lang="EN-US"}**]{#struct_0_53887_18384_x1984217892}

[[【视图】]{style="font-family:黑体"}]{#struct_0_53887_18384_494526553}

[[用户视图]{style="font-family:宋体"}]{#struct_0_53887_18384_x676736697}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_53887_18384_629849674}

[[network-admin]{lang="EN-US"}]{#struct_0_53887_18384_x1682365474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_53887_18384_x1700952451}

[[【描述】]{style="font-family:黑体"}]{#struct_0_53887_18384_1756470398}

[**[debugging ]{lang="EN-US"}[ipv6 nd detection packet]{lang="EN-US"}**]{#struct_0_53887_18384_x1232526187}[命令用来打开]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[ipv6 nd detection packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}]{#struct_0_53887_18384_x563608669}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 nd detection packet]{lang="EN-US"}]{#struct_0_53887_18384_x809206609}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_177918166}[[字段]{style="font-family:黑体"}]{#struct_0_53887_18384_x1378625034}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_53887_18384_958664037}

[[Received *packet-type* packet on untrust port *port-name*, no matching entry, dropped it.]{lang="EN-US"}]{#struct_0_53887_18384_748393682}

[[从非信任口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_53887_18384_x1891743731}[接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文，由于没有表项匹配，故丢弃。其中]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*[可以是二层以太口或者二层聚合口。]{style="font-family:宋体"}*[Packet-type]{lang="EN-US"}*[是：]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  6.5pt;font-family:Wingdings"}[RS]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_53887_18384_x1882215359}[：]{style="font-size:9.0pt;font-family:宋体"}[Router Solicitation]{lang="EN-US" style="font-size:9.0pt"}[报文]{style="font-size:
  9.0pt;font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  6.5pt;font-family:Wingdings"}[NS]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_53887_18384_1073466772}[：]{style="font-size:9.0pt;font-family:宋体"}[Neighbor Solicitation]{lang="EN-US" style="font-size:9.0pt"}[报文]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_53887_18384_x1812402142}[：]{lang="EN-US" style="font-family:宋体"}[Neighbor Advertisement]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[Received *packet-type* packet on untrust port *port-name*, dropped it. ]{lang="EN-US"}]{#struct_0_53887_18384_x1022687794}

[[从非信任口]{style="font-family:宋体"}[port-name]{lang="EN-US"}]{#struct_0_53887_18384_834997078}[接收到]{style="font-family:宋体"}[packet-type]{lang="EN-US"}[报文，丢弃。其中]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*[可以是二层以太网端口或二层聚合口，]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[是：]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  6.5pt;font-family:Wingdings"}[RR]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_53887_18384_x1999151490}[：]{style="font-size:9.0pt;font-family:宋体"}[ICMPv6 redirect]{lang="EN-US" style="font-size:9.0pt"}[报文]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RA]{lang="EN-US"}]{#struct_0_53887_18384_1193182216}[：]{lang="EN-US" style="font-family:宋体"}[Router Advertisement]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_53887_18384_x1702531239}

[[\# ]{lang="EN-US"}]{#struct_0_53887_18384_1289414644}[打开]{style="font-family:宋体"}[ND Detection]{lang="EN-US"}[报文调试信息开关，并收到]{style="font-family:宋体"}[ND]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 nd detection packet]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_53887_18384_1697990998}

[*[// ]{lang="EN-US"}*]{#struct_0_53887_18384_x650160244}*[在聚合口]{style="font-family:宋体"}[BAGG1]{lang="EN-US"}[上收到]{style="font-family:宋体"}[NA]{lang="EN-US"}[报文，由于未找到匹配表项而丢弃]{style="font-family:宋体"}*

[[\*Jul 25 14:10:50:414 2014 H3C ND/7/ND DETECTION PACKET: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_53887_18384_40098942}

[[ Received NA packet on untrust port BAGG1, no matching entry, dropped it.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_53887_18384_x349968914}
