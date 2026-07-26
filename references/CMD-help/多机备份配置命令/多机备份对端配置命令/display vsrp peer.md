::: {#1969371457 .myid}
[]{#_Toc404796088}[]{#struct_0_16980_17120_468451780}[]{#_Toc350446335}[]{#_Toc350329042}[]{#_Toc349805340}

**多机备份配置命令 \-- 多机备份对端配置命令 \-- display vsrp peer**

------------------------------------------------------------------------

[**[display vsrp peer]{lang="EN-US"}**]{#struct_0_16980_17120_182501474}[命令用来显示]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[组信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1770283384}

[**[display vsrp peer]{lang="EN-US"}**[ \[ *peer-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_x319182373}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x544806689}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_119690807}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x748047695}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_2033437019}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_1924442958}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1958485133}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_x817635961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1630810290}

[*[peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_x336391141}*[：]{style="font-family:宋体"}*[多机备份组名称，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x642985827}

[[不指定多机备份组名称时，命令显示所有的多机备份组信息。]{style="font-family:宋体"}]{#struct_0_16980_17120_1874572259}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1718033815}

[]{#_Toc136937987}[]{#_Toc99445936}[]{#_Toc34203769}[]{#_Toc33197993}[]{#_Toc350446336}[]{#_Toc350329043}[]{#_Toc349805341}[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x850876588}[显示已创建的多机备份组]{style="font-family:宋体"}[pname]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display vsrp peer pname]{lang="EN-US"}]{#struct_0_16980_17120_x1230162061}

[VSRP peer name: pname]{lang="EN-US"}

[ TCP status: Connected]{lang="EN-US"}

[ Peer IP: 11.0.0.3]{lang="EN-US"}

[ Local IP: 10.0.0.3]{lang="EN-US"}

[ Port: 6000]{lang="EN-US"}

[ Track ID: 5]{lang="EN-US"}

[ Track status: Positive]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1351690196}[显示全部已创建的多机备份组的信息]{style="font-family:宋体"}

[[\<Sysname\> display vsrp peer]{lang="EN-US"}]{#struct_0_16980_17120_x1735252778}

[VSRP peer name: pname1]{lang="EN-US"}

[ TCP status: Connected]{lang="EN-US"}

[ Peer IP: 11.0.0.3]{lang="EN-US"}

[ Local IP: 10.0.0.3]{lang="EN-US"}

[ Port: 6000]{lang="EN-US"}

[ Track ID: 5]{lang="EN-US"}

[ Track status: Positive]{lang="EN-US"}

[VSRP peer name: pname2]{lang="EN-US"}

[ TCP status]{lang="EN-US"}[：]{style="font-family:宋体"}[Disconnected]{lang="EN-US"}

[ Peer IP: 10.0.0.2]{lang="EN-US"}

[ Local IP: 11.0.0.2]{lang="EN-US"}

[ Port: 5000]{lang="EN-US"}

[ Track ID: 5]{lang="EN-US"}

[ Track status: Negative]{lang="EN-US"}

[[表]{style="font-family:宋体"}[1-1 display vsrp peer]{lang="EN-US"}]{#struct_0_16980_17120_211119373}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1744435953}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_16980_17120_923098114}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_16980_17120_x77217931}

[[VSRP peer name]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x841095033}

[[多机备份组名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_596488858}

[[TCP status]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x2098619264}

[[多机备份组]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x1768096920}[TCP]{lang="EN-US" style="font-size:9.0pt"}[连接状态，取值包含：]{style="font-size:9.0pt;font-family:宋体"}

[[Disconnected]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_10889059}[：连接已断开]{style="font-size:9.0pt;font-family:宋体"}

[[Connected]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x954683723}[：连接已建立]{style="font-size:9.0pt;font-family:宋体"}

[[Peer IP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x138373896}

[[多机备份组中]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_1620006614}[TCP]{lang="EN-US" style="font-size:9.0pt"}[连接的对端]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址]{style="font-size:9.0pt;font-family:
  宋体"}

[[Local IP]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_728910506}

[[多机备份组中]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x999281723}[TCP]{lang="EN-US" style="font-size:9.0pt"}[连接的本端]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址]{style="font-size:9.0pt;font-family:
  宋体"}

[[Port]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_351187174}

[[多机备份组中]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x99973477}[TCP]{lang="EN-US" style="font-size:9.0pt"}[连接绑定的端口号]{style="font-size:9.0pt;font-family:宋体"}

[[Track ID]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_1098774707}

[[多机备份组关联的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x373871944}[Track]{lang="EN-US" style="font-size:9.0pt"}[项]{style="font-size:9.0pt;font-family:宋体"}

[[Track status]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x1692889500}

[[多机备份组关联的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_1013090870}[Track]{lang="EN-US" style="font-size:9.0pt"}[项状态，取值包含：]{style="font-size:9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_16980_17120_261621034}[：表示状态正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NotReady]{lang="EN-US"}]{#struct_0_16980_17120_x441321379}[：表示无效值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_16980_17120_157123983}[：表示状态异常]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1903411553 .myid}
[]{#_Toc404796089}[]{#struct_0_16980_17120_566802218}

**多机备份配置命令 \-- 多机备份对端配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_16980_17120_x1211552763}[命令用来配置到多机备份对端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**]{#struct_0_16980_17120_1581783393}[命令用来删除到多机备份对端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1883636348}

[**[peer ]{lang="EN-US"}***[peer-ip-address]{lang="EN-US"}***[ local ]{lang="EN-US"}***[local-ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **port** *port-id* \]]{lang="EN-US"}]{#struct_0_16980_17120_2000380002}

[**[undo peer]{lang="EN-US"}**]{#struct_0_16980_17120_x562882874}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x2010313988}

[[未配置到]{style="font-family:宋体"}]{#struct_0_16980_17120_x1573686983}[多机备份]{style="font-family:宋体"}[对端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1870517508}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x1547601045}[对端视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x638317628}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_704152702}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x1093082456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_459142360}

[*[peer-ip-address]{lang="EN-US"}*]{#struct_0_16980_17120_x671357348}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[多机备份中]{style="font-family:宋体"}[的对端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}***[ local-ip-address]{lang="EN-US"}*]{#struct_0_16980_17120_2132886159}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[多机备份中]{style="font-family:宋体"}[的本端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}***[ port-id]{lang="EN-US"}*]{#struct_0_16980_17120_1693326945}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接绑定的端口号，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，默认端口号为]{style="font-family:宋体"}[60032]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1235108361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_52869590}[TCP]{lang="EN-US"}[连接时，本端和对端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须为单播地址，且不允许配置为全零地址或环回地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_482817773}[TCP]{lang="EN-US"}[连接时，本端和对端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能相同；任意两个多机备份组内]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的本端和对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_x475813406}[TCP]{lang="EN-US"}[连接时，绑定的端口号不能与已有的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听服务使用的端口号冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若多机备份组内已配置]{style="font-family:宋体"}]{#struct_0_16980_17120_142571422}[TCP]{lang="EN-US"}[连接，重新配置一条]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时，需要先删除当前]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，否则无法配置成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1737924331}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x243640313}[在名为]{style="font-family:宋体"}[pname]{lang="EN-US"}[的多机备份组中，创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，本端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[11.0.0.2]{lang="EN-US"}[，对端设备]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[10.0.0.1]{lang="EN-US"}[，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接绑定的端口号为]{style="font-family:宋体"}[7000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1364332943}

[\[Sysname\] vsrp peer pname]{lang="EN-US"}

[\[Sysname-vsrp-peer-pname\] peer 10.0.0.1 local 11.0.0.2 port 7000]{lang="EN-US"}
:::

::: {#-679178060 .myid}
[]{#_Toc404796090}[]{#struct_0_16980_17120_x2054207690}

**多机备份配置命令 \-- 多机备份对端配置命令 \-- peer ipv6**

------------------------------------------------------------------------

[**[peer ipv6]{lang="EN-US"}**]{#struct_0_16980_17120_x1949691084}[命令用来配置到多机备份对端的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[undo peer ipv6]{lang="EN-US"}**]{#struct_0_16980_17120_x1185290948}[命令用来删除到多机备份对端的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_211902685}

[**[peer ipv6 ]{lang="EN-US"}***[peer-ipv6-address]{lang="EN-US"}***[ local ]{lang="EN-US"}***[local-ipv6-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **port** *port-id* \]]{lang="EN-US"}]{#struct_0_16980_17120_1132519903}

[**[undo peer ipv6]{lang="EN-US"}**]{#struct_0_16980_17120_x1035451211}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2054666441}

[[未配置到]{style="font-family:宋体"}]{#struct_0_16980_17120_354654147}[多机备份]{style="font-family:宋体"}[对端的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1597919148}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x974635349}[对端视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2002362218}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_30102205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1929901348}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1878546600}

[*[peer-ipv6-address]{lang="EN-US"}*]{#struct_0_16980_17120_x2054731977}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[多机备份中]{style="font-family:宋体"}[的对端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}***[ local-ipv6-address]{lang="EN-US"}*]{#struct_0_16980_17120_x2056661975}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[多机备份中]{style="font-family:宋体"}[的本端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}***[ port-id]{lang="EN-US"}*]{#struct_0_16980_17120_x677680524}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:\"Calibri\",\"sans-serif\""}[TCP]{lang="EN-US"}[连接绑定的端口号，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，默认端口号为]{style="font-family:宋体"}[60032]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2056518978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_x1453922550}[IPv6 TCP]{lang="EN-US"}[连接时，本端和对端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址必须为单播地址，且不允许配置为全零地址或环回地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_1481449544}[IPv6 TCP]{lang="EN-US"}[连接时，本端和对端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不能相同；任意两个多机备份组内]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接的本端和对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_1785546413}[IPv6 TCP]{lang="EN-US"}[连接时，绑定的端口号不能与已有的]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[监听服务使用的端口号冲突。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若多机备份组内已配置]{style="font-family:宋体"}]{#struct_0_16980_17120_x2054535369}[IPv6 TCP]{lang="EN-US"}[连接，重新配置一条]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接时，需要先删除当前]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接，否则无法配置成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1078369743}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1566146934}[在名为]{style="font-family:宋体"}[pname]{lang="EN-US"}[的多机备份组中，创建]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接，本端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，对端设备]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2::2]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv6 TCP]{lang="EN-US"}[连接绑定的端口号为]{style="font-family:宋体"}[7000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1072689329}

[\[Sysname\] vsrp peer pname]{lang="EN-US"}

[\[Sysname-vsrp-peer-pname\] peer ipv6 2::2 local 1::1 port 7000]{lang="EN-US"}
:::

::: {#1609214304 .myid}
[]{#_Toc404796091}[]{#struct_0_16980_17120_752106785}

**多机备份配置命令 \-- 多机备份对端配置命令 \-- track**

------------------------------------------------------------------------

[**[track]{lang="EN-US"}**]{#struct_0_16980_17120_x492460605}[命令用来配置监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_16980_17120_x1377753563}[命令用来取消监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1793034057}

[**[track]{lang="EN-US"}***[ track-entry-number]{lang="EN-US"}*]{#struct_0_16980_17120_1746807581}

[**[undo track]{lang="EN-US"}**]{#struct_0_16980_17120_x595997196}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_210606891}

[[未配置监视指定的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_16980_17120_1206172738}[项]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1863828844}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_468889371}[对端视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1426451562}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1234085877}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x1436824039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_166386824}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_16980_17120_x1497584145}*[：]{style="font-family:宋体"}*[被监视]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_532616172}

[[用户可以通过多机备份组关联]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_16980_17120_1543804758}[来快速检测通道是否可用。未关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项时，多机备份组只能依靠]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的状态来检查通道是否可用。当关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[状态为]{style="font-family:宋体"}[Positive]{lang="EN-US"}[或]{style="font-family:宋体"}[NotReady]{lang="EN-US"}[时，多机备份模块才会尝试与对端设备建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接；当关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[的状态为]{style="font-family:宋体"}[Negative]{lang="EN-US"}[时，断开与对端设备的控制]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_16980_17120_x539987866}[连接有效时，设备上的]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[功能才是生效的。]{style="font-family:宋体"}

[[Track]{lang="EN-US"}]{#struct_0_16980_17120_x219970268}[项的详细介绍请参见"可靠性配置指导"中的"]{style="font-family:宋体"}[Track]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1118317828}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x745706665}[在名为]{style="font-family:宋体"}[pname]{lang="EN-US"}[的多机备份对端视图下，配置关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，]{style="font-family:宋体"}[Track]{lang="EN-US"}[序号为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1326317105}

[\[Sysname\] vsrp peer pname]{lang="EN-US"}

[\[Sysname-vsrp-peer-pname\] track 10]{lang="EN-US"}
:::

::: {#-1747699635 .myid}
[]{#_Toc404796092}[]{#struct_0_16980_17120_x773865624}

**多机备份配置命令 \-- 多机备份对端配置命令 \-- vsrp peer**

------------------------------------------------------------------------

[**[vsrp peer]{lang="EN-US"}**]{#struct_0_16980_17120_284844245}[命令用来创建多机备份对端并进入多机备份对端视图。如果已创建多机备份对端，执行该命令直接进入多机备份对端视图。]{style="font-family:宋体"}

[**[undo vsrp peer]{lang="EN-US"}**]{#struct_0_16980_17120_x1146204512}[命令用来删除指定的多机备份对端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1500266947}

[**[vsrp peer ]{lang="EN-US"}***[peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_1466965808}

[**[undo vsrp peer]{lang="EN-US"}***[ peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1640588884}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x1851171747}

[[未创建]{style="font-family:宋体;color:black"}]{#struct_0_16980_17120_1797731878}[多机备份]{style="font-family:宋体"}[对端。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1242569815}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x169192030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1722354166}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1198235240}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x1543326077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1402566250}

[*[peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_x199586951}[：多机备份对端名称，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1329663809}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上最多支持创建]{style="font-family:宋体"}]{#struct_0_16980_17120_2135069039}[64]{lang="EN-US"}[个多机备份对端。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除多机备份对端时，若已有多机备份实例关联该多机备份对端，需先解除关联关系，否则无法删除。]{style="font-family:宋体"}]{#struct_0_16980_17120_x791463718}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1121241172}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_127903934}[创建名称为]{style="font-family:宋体"}[pname]{lang="EN-US"}[的多机备份组并进入多机备份对端视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1211112344}

[\[Sysname\] vsrp peer pname]{lang="EN-US"}

[\[Sysname-vsrp-peer-pname\]]{lang="EN-US"}
:::

::: {#275825121 .myid}
[]{#_Toc136937988}[]{#_Toc99445937}[]{#_Toc34203770}[]{#_Toc33197994}[]{#_Toc404796094}[]{#struct_0_16980_17120_x1114679663}[]{#_Toc350446338}[]{#_Toc350329045}[]{#_Toc349805343}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- backup id**

------------------------------------------------------------------------

[**[backup id]{lang="EN-US"}**]{#struct_0_16980_17120_x179406818}[命令用来配置]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例的备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo backup id]{lang="EN-US"}**]{#struct_0_16980_17120_x1685537248}[命令用来删除]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例的备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x834771859}

[**[backup id ]{lang="EN-US"}***[backup-id]{lang="EN-US"}***[ peer ]{lang="EN-US"}***[peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_163517691}

[**[undo backup]{lang="EN-US"}***[ ]{lang="EN-US"}***[id]{lang="EN-US"}**]{#struct_0_16980_17120_643705796}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1379703235}

[[未配置]{style="font-family:宋体"}]{#struct_0_16980_17120_561031492}[多机备份实例的备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x830749011}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x1407642892}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_155878772}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_348910704}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x792671066}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_196260301}

[*[backup-id]{lang="EN-US"}*]{#struct_0_16980_17120_x1239109286}[：表示]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例的备份标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[peer-name]{lang="EN-US"}*]{#struct_0_16980_17120_1246163466}[：表示关联的]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[对端名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1876545310}

[[需要注意的是[:]{lang="EN-US"}]{style="font-family:宋体"}]{#struct_0_16980_17120_x797018336}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置多机备份实例备份]{style="font-family:宋体"}]{#struct_0_16980_17120_1178632299}[ID]{lang="EN-US"}[时，多机备份对端必须已存在，且]{style="font-family:宋体"}*[backup-id]{lang="EN-US"}*[在该多机备份对端内未被使用过。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置多机备份实例备份]{style="font-family:宋体"}]{#struct_0_16980_17120_1729601632}[ID]{lang="EN-US"}[时，若多机备份实例已配置备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[，则需先删除当前备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[后，才能配置新的备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1228625865}

[]{#_Toc350446339}[]{#_Toc350329046}[]{#_Toc349805344}[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1148839012}[配置名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的多机备份实例在多机备份对端]{style="font-family:宋体"}[pname]{lang="EN-US"}[中的备份]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1070740149}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] backup id 5 peer pname]{lang="EN-US"}
:::

::: {#1428856670 .myid}
[]{#_Toc404796095}[]{#struct_0_16980_17120_692847096}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- backup mode**

------------------------------------------------------------------------

[**[backup mode]{lang="EN-US"}**]{#struct_0_16980_17120_429004253}[命令用来设置]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例的备份模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo backup mode ]{lang="EN-US"}**]{#struct_0_16980_17120_x725591437}[命令用来恢复缺省]{style="font-family:宋体"}[情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x936610348}

[**[backup mode ]{lang="EN-US"}**[{ **hot** \| **warm** }]{lang="EN-US"}]{#struct_0_16980_17120_x6233383}

[**[undo backup mode]{lang="EN-US"}**]{#struct_0_16980_17120_1738983282}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x691369834}

[[多机备份实例的备份模式为热备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x932705171}[。]{style="font-family:宋体;
color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1686135890}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x737998416}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1028163534}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1731105169}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x643051363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x472087294}

[**[hot]{lang="EN-US"}**]{#struct_0_16980_17120_1011828889}[：表示热备份。]{style="font-family:宋体"}

[**[warm]{lang="EN-US"}**]{#struct_0_16980_17120_364488957}[：表示温备份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_870273881}

[[在不同的备份模式下，对于收到的备份信息，设备有以下处理方式：]{style="font-family:宋体"}]{#struct_0_16980_17120_x2098404792}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[热备份：当备用设备收到主用设备的备份信息后，立即下发备份信息到转发平面。这样，主用设备发生故障时，备用设备能马上指导报文转发，可以实现业务终端快速切换。]{style="font-family:宋体"}]{#struct_0_16980_17120_480938058}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[温备份：当备用设备收到主用设备的备份信息后，不会立即下发备份信息到转发平面，当主用设备发生故障后，设备的主备状态发生切换，备用设备才开始才开始下发备份信息到转发平面，并指导报文转发。业务切换到备用设备上的时间比热备份切换时间稍长。]{style="font-family:宋体"}]{#struct_0_16980_17120_x947450160}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1580265132}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x335250167}[设置多机备份实例备份模式为温备份。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x893066773}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] backup mode warm]{lang="EN-US"}
:::

::: {#-1805665752 .myid}
[]{#_Toc404796096}[]{#struct_0_16980_17120_x239333772}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- bind vrrp vrid**

------------------------------------------------------------------------

[**[bind vrrp vrid]{lang="EN-US"}**]{#struct_0_16980_17120_x1765779756}[命令用来绑定多机备份实例和]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组。]{style="font-family:宋体"}

[**[undo bind vrrp]{lang="EN-US"}**]{#struct_0_16980_17120_x497816500}[命令用来解]{style="font-family:宋体"}[除多机备份实例和]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组的绑定]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1622929441}

[**[bind vrrp vrid]{lang="EN-US"}***[ virtual-router-id ]{lang="EN-US"}***[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_16980_17120_923032578}

[**[undo bind vrrp]{lang="EN-US"}**]{#struct_0_16980_17120_766766151}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x597905989}

[[未绑定]{style="font-family:宋体"}]{#struct_0_16980_17120_x1102150558}[多机备份实例和]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1764048992}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x1050300692}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1778526482}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x900730867}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x1782713981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1202814159}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_16980_17120_x53611183}[：表示]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_16980_17120_815689077}[：表示]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组所属接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x44482651}

[[多机备份实例通过绑定]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_16980_17120_x1252567505}[备份组来确定自身的主备身份。一个多机备份实例只能绑定一个]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组。指定]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组时，]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组可以不存在于指定的接口下。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2076658826}

[]{#_Toc350446340}[]{#_Toc350329047}[]{#_Toc349805345}[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1194085205}[配置多机备份实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[与接口]{style="font-family:宋体"}[GigabitEthernet 2/0/2]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[2]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x999347259}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] bind vrrp vrid 2 interface gigabitethernet 2/0/2]{lang="EN-US"}
:::

::: {#46809331 .myid}
[]{#_Toc404796097}[]{#struct_0_16980_17120_x488516961}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- bind vrrp ipv6 vrid**

------------------------------------------------------------------------

[**[bind vrrp ipv6 vrid]{lang="EN-US"}**]{#struct_0_16980_17120_x488320353}[命令用来绑定多机备份实例和]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组。]{style="font-family:宋体"}

[**[undo bind vrrp ipv6]{lang="EN-US"}**]{#struct_0_16980_17120_781796494}[命令用来解除]{style="font-family:宋体"}[多机备份实例和]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组的绑定]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_52805360}

[**[bind vrrp ipv6 vrid]{lang="EN-US"}***[ virtual-router-id ]{lang="EN-US"}***[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_16980_17120_x1529982868}

[**[undo bind vrrp ipv6]{lang="EN-US"}**]{#struct_0_16980_17120_1703961559}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1003525984}

[[未绑定]{style="font-family:宋体"}]{#struct_0_16980_17120_1688758870}[多机备份实例和]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x133246415}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_911210682}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x488385889}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1094421400}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1879761806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1381875723}

[*[virtual-router-id]{lang="EN-US"}*]{#struct_0_16980_17120_476822899}[：表示]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_16980_17120_x1419666887}[：表示]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组所属接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_2106655013}

[[多机备份实例中的设备通过绑定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}]{#struct_0_16980_17120_792682163}[备份组来确定自身的主备身份。一个多机备份实例只能绑定一个]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组。指定]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组时，]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组可以不存在于指定的接口下。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x488189281}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_796398626}[配置多机备份实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[与接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 VRRP]{lang="EN-US"}[备份组]{style="font-family:宋体"}[2]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1223428401}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] bind vrrp ipv6 vrid 2 interface gigabitethernet 1/0/1]{lang="EN-US"}
:::

::: {#297699834 .myid}
[]{#_Toc404796098}[]{#struct_0_16980_17120_298097252}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- display vsrp instance**

------------------------------------------------------------------------

[**[display vsrp instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1592688528}[命令显示]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x222403901}

[**[display vsrp instance ]{lang="EN-US"}**[\[ *instance-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_x296788183}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1643544952}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_1918595265}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1679516237}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1242165254}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_x204020245}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x530452358}

[[mdc-operator ]{lang="EN-US"}]{#struct_0_16980_17120_x1193161779}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1022985869}

[*[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1702898454}*[：]{style="font-family:宋体"}*[多机备份实例名，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16980_17120_724796419}

[[不指定多机备份实例名称时，显示所有的多机备份实例信息。]{style="font-family:宋体"}]{#struct_0_16980_17120_x42247994}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_566736682}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_499318410}[显示已创建的多机备份实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display vsrp instance aaa]{lang="EN-US"}]{#struct_0_16980_17120_362616245}

[VSRP instance name: aaa]{lang="EN-US"}

[ VSRP peer name: pname1]{lang="EN-US"}

[ Backup ID: 10]{lang="EN-US"}

[ Bound VRID: VRRP VRID 1 interface GigabitEthernet2/0/1]{lang="EN-US"}

[ Instance status: Master]{lang="EN-US"}

[ Local status: Master]{lang="EN-US"}

[ Peer status: Backup]{lang="EN-US"}

[ Backup mode: Warm]{lang="EN-US"}

[ Traffic backup interval: 10(minutes)]{lang="EN-US"}

[ Traffic backup threshold: 50(MB)]{lang="EN-US"}

[ NAS IP: 10.0.0.1]{lang="EN-US"}

[ NAS port: GigabitEthernet2/0/2]{lang="EN-US"}

[ NAS ID: h3c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1484657775}[显示全部已创建的多机备份实例信息。]{style="font-family:宋体"}

[[\<Sysname\> display vsrp instance]{lang="EN-US"}]{#struct_0_16980_17120_2132820623}

[VSRP instance name: aaa]{lang="EN-US"}

[ VSRP peer name: pname1]{lang="EN-US"}

[ Backup ID: 10]{lang="EN-US"}

[ Bound VRID: VRRP VRID 1 interface GigabitEthernet2/0/1]{lang="EN-US"}

[ Instance status : Master]{lang="EN-US"}

[ Local status: Master]{lang="EN-US"}

[ Peer status: Backup]{lang="EN-US"}

[ Backup mode: Warm]{lang="EN-US"}

[ Traffic backup interval: 10(minutes)]{lang="EN-US"}

[ Traffic backup threshold: 50(MB)]{lang="EN-US"}

[ NAS IP: 10.0.0.1]{lang="EN-US"}

[ NAS port: GigabitEthernet2/0/2]{lang="EN-US"}

[ NAS ID: h3c]{lang="EN-US"}

[VSRP instance name: bbb]{lang="EN-US"}

[ VSRP peer name: pname2]{lang="EN-US"}

[ Backup ID: 10]{lang="EN-US"}

[ Bound VRID: VRRP VRID 2 interface GigabitEthernet3/0/1]{lang="EN-US"}

[ Instance status : Master]{lang="EN-US"}

[ Local status: Master]{lang="EN-US"}

[ Peer status: Backup]{lang="EN-US"}

[ Backup mode: Warm]{lang="EN-US"}

[ Traffic backup interval: 5(minutes)]{lang="EN-US"}

[ Traffic backup threshold: 100(MB)]{lang="EN-US"}

[ NAS IP: 10.0.0.2]{lang="EN-US"}

[ NAS port: GigabitEthernet3/0/2]{lang="EN-US"}

[ NAS ID: h3c]{lang="EN-US"}

[[表]{style="font-family:宋体"}[1-2 display vsrp instance]{lang="EN-US"}]{#struct_0_16980_17120_156370836}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1738512209}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_16980_17120_378711692}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_16980_17120_x988653564}

[[VSRP instance name]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x1758801773}

[[多机备份实例名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x604652281}

[[VSRP peer name]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x1976563595}

[[多机备份实例关联的多机备份对端名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x81824483}

[[Backup ID]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x596062732}

[[多机备份实例备份]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_1661811725}[ID]{lang="EN-US" style="font-size:9.0pt"}

[[Bound VRID]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x1030961312}

[[多机备份实例绑定接口下的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x1366702992}[VRID]{lang="EN-US" style="font-size:
  9.0pt"}

[[Instance status]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x967568386}

[[多机备份实例状态，状态取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_1694399573}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_x873971875}[：表示在该多机备份实例中，本设备作为主用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_1490783812}[：表示在该多级备份实例中，本设备作为备用设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16980_17120_1877473916}[：表示在该多机备份实例中，本设备不运行]{style="font-family:宋体"}

[[Local status]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x385963747}

[[本端本地状态，状态取值包括：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x940191568}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_1326251569}[：表示主用状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_1161996479}[：表示备用状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_16980_17120_1882328650}[：表示初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16980_17120_2029114042}[：表示未获取到本端本地状态]{style="font-family:宋体"}

[[Peer status]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x969845618}

[[对端本地状态，状态取值包括：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_1448765646}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_x733157976}[：表示主用状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_1706918971}[：表示备用状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_16980_17120_779011999}[：表示初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16980_17120_x1402631786}[：表示未获取到对端本地状态]{style="font-family:宋体"}

[[Backup mode]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_211129789}

[[多机备份实例备份模式，取值为：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x1785303802}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="EN-US"}]{#struct_0_16980_17120_2111618159}[：热备份]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="EN-US"}]{#struct_0_16980_17120_x656630333}[：温备份]{lang="EN-US" style="font-family:宋体"}

[[Traffic backup interval]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x1002507575}

[[流量备份时间间隔]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x486254875}

[[Traffic backup threshold]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_x965667155}

[[流量备份阈值]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_163452155}

[[NAS IP]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_959160279}

[[业务逻辑]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_x285438763}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址]{style="font-size:9.0pt;font-family:宋体"}

[[NAS port]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_16980_17120_1640210456}

[[业务逻辑接口名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_1989559324}

[[NAS ID]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_16980_17120_596461200}

[[业务逻辑主机名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_16980_17120_592587972}

[ ]{lang="EN-US"}

::: {#-175403411 .myid}
[]{#_Toc404796099}[]{#struct_0_16980_17120_1729536096}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- nas**

------------------------------------------------------------------------

[**[nas]{lang="EN-US"}**]{#struct_0_16980_17120_x453424627}[命令用来配置]{style="font-family:宋体"}[NAS]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[**[undo nas]{lang="EN-US"}**]{#struct_0_16980_17120_x987619297}[命令用来删除已配置的]{style="font-family:宋体"}[NAS]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1579488502}

[**[nas]{lang="EN-US"}**[ { **id** *host-name* **\| ip** *ip-address* \| **port** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_16980_17120_x1881567318}

[**[undo]{lang="EN-US"}**[ **nas** \[ **id** \| **ip** \| **port** \]]{lang="EN-US"}]{#struct_0_16980_17120_1301841877}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1094162306}

[[未配置]{style="font-family:宋体"}[NAS]{lang="EN-US"}]{#struct_0_16980_17120_333737816}[参数]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x272387830}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_x750565080}[实例视图]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_16980_17120_x1222923414}[缺省用户角色]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_756911877}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1510184271}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2111973514}

[**[id]{lang="EN-US"}***[ host-name]{lang="EN-US"}*]{#struct_0_16980_17120_99484407}[：表示]{style="font-family:宋体"}[业务逻辑主机名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[127]{lang="EN-US"}[个字符的字符串，不区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_16980_17120_1089090813}[：表示业务逻辑]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_16980_17120_x643116899}[：表示]{style="font-family:宋体"}[业务逻辑的]{style="font-family:宋体"}[接口类型和接口编号，目前支持接口类型为[:]{lang="EN-US"}三层]{style="font-family:宋体"}[以太网接口类型和三层聚合接口类型。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_16980_17120_x1210755809}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[NAS(Network Access Server)]{lang="EN-US"}]{#struct_0_16980_17120_1716901023}[表示网络接入服务。用户可以通过本命令在多机备份实例下配置业务逻辑]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、业务逻辑接口和业务逻辑主机名，使互为备份的设备上发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Authentication Dial-In User Service]{lang="EN-US"}[，远程认证拨号用户服务）]{style="font-family:宋体"}[服务器报文的]{style="font-family:宋体"}[NAS-IP-Address]{lang="EN-US"}[、]{style="font-family:宋体"}[NAS-Port]{lang="EN-US"}[属性以及上送给]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器报文的]{style="font-family:宋体"}[Option82]{lang="EN-US"}[字段信息保持一致。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1804824732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置业务逻辑]{style="font-family:宋体"}]{#struct_0_16980_17120_1921459220}[IP]{lang="EN-US"}[地址时，必须配置为单播地址，且不允许配置为全零地址或环回地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置业务逻辑接口时，允许配置成当前设备上不存在的接口。逻辑接口的位置信息格式为"槽位号]{style="font-family:宋体"}]{#struct_0_16980_17120_x590132015}[/]{lang="EN-US"}[子卡号]{style="font-family:宋体"}[/]{lang="EN-US"}[接口号"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1652309098}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1956271463}[配置业务逻辑]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x681725766}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] nas ip 2.2.2.2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_407014421}[配置业务逻辑接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1842999822}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] nas port gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1232690208}[配置业务逻辑主机名为]{style="font-family:宋体"}[bbb]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_964760793}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] nas id bbb]{lang="EN-US"}
:::

::: {#-1619988208 .myid}
[]{#_Toc136937990}[]{#_Toc99445939}[]{#_Toc34203772}[]{#_Toc33197996}[]{#_Toc404796100}[]{#struct_0_16980_17120_x1522918861}[]{#_Toc350446341}[]{#_Toc350329048}[]{#_Toc349805346}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- traffic backup**

------------------------------------------------------------------------

[**[traffic backup]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_16980_17120_922967042}[命令用来设置]{style="font-family:宋体"}[流量备份时间间隔或流量阈值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo traffic backup]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_16980_17120_444944708}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_35842120}

[**[traffic backup]{lang="EN-US"}**[ { **interval** *interval-value* \| **threshold** *threshold-value* } \*]{lang="EN-US"}]{#struct_0_16980_17120_964001339}

[**[undo traffic backup]{lang="EN-US"}**[ \[ **interval** \| **threshold** \]]{lang="EN-US"}]{#struct_0_16980_17120_1983114443}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_2143635907}

[[多机备份实例的流量备份时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_16980_17120_560191942}[分钟，流量阈值缺省值为]{style="font-family:宋体"}[50MB]{lang="EN-US"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_2129800019}

[[多机备份]{style="font-family:宋体"}]{#struct_0_16980_17120_1147414104}[实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x107908890}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1577281880}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_806433624}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2051069604}

[*[interval-value]{lang="EN-US"}*]{#struct_0_16980_17120_1964307719}[：表示流量备份时间间隔，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟（]{style="font-family:宋体"}[min]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[threshold-value]{lang="EN-US"}*]{#struct_0_16980_17120_x222264275}[：表示流量阈值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[，单位为兆字节（]{style="font-family:宋体"}[MB]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1644310083}

[[多机备份实例支持配置流量备份时间间隔和流量备份阈值。以特定业务为例，当业务持续转发时间达到流量备份时间间隔或转发业务的流量达到阈值时，多机备份实例需要对该业务模块数据进行备份操作。]{style="font-family:宋体"}]{#struct_0_16980_17120_x865129531}

[[当流量备份时间间隔和流量阈值均为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_16980_17120_1216868483}[时，表示不备份用户流量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1759467267}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_2027857643}[当流量备份时间达到为]{style="font-family:宋体"}[50]{lang="EN-US"}[分钟时，进行业务模块数据的备份操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1168159168}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] traffic backup interval 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_201073522}[当转发流量达到]{style="font-family:宋体"}[200MB]{lang="EN-US"}[时，进行业务模块数据的备份操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x32418216}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] traffic backup threshold 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1458705915}[恢复流量备份时间和流量阈值为缺省值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1837463596}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\] undo traffic backup]{lang="EN-US"}
:::

::: {#-1572398753 .myid}
[]{#_Toc404796101}[]{#struct_0_16980_17120_x2121430727}

**多机备份配置命令 \-- 多机备份实例配置命令 \-- vsrp instance（系统视图）**

------------------------------------------------------------------------

[**[vsrp instance]{lang="EN-US"}**]{#struct_0_16980_17120_1712663056}[命令用来创建]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例并进入]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例视图。如果指定的]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例已创建，则该命令直接用来进入该]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例视图。]{style="font-family:宋体"}

[**[undo vsrp instance]{lang="EN-US"}**]{#struct_0_16980_17120_771925774}[命令用来删除已创建的]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1995087877}

[**[vsrp instance]{lang="EN-US"}***[ instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x2053792032}

[**[undo vsrp instance]{lang="EN-US"}***[ instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_700954410}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1615125549}

[[未创建]{style="font-family:宋体"}]{#struct_0_16980_17120_x322608422}[多机备份实例]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1320835472}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x818819859}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1819018073}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x492787198}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_16980_17120_x251487508}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_87671372}

[*[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_1312912660}[：表示]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x877716790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多机备份实例作为业务应用模块的关联实体，在实际应用中，须配置关联多机备份对端并绑定]{style="font-family:宋体"}]{#struct_0_16980_17120_2003418701}[VRRP]{lang="EN-US"}[备份组，备份模式及流量备份方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备上最多支持创建]{style="font-family:宋体"}]{#struct_0_16980_17120_x1095713595}[1024]{lang="EN-US"}[个多机备份实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1691578211}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x589319376}[创建名为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的多机备份实例，并进入多机备份实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x2027928945}

[\[Sysname\] vsrp instance aaa]{lang="EN-US"}

[\[Sysname-vsrp-instance-aaa\]]{lang="EN-US"}
:::

::: {#-1991023472 .myid}
[]{#_Toc404796103}[]{#struct_0_16980_17120_350640715}

**多机备份配置命令 \-- 配置IPv6虚拟地址 \-- ipv6 virtual-address**

------------------------------------------------------------------------

[**[ipv6 virtual-address]{lang="EN-US"}**]{#struct_0_16980_17120_1694857665}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[虚拟地址，并绑定多机备份实例。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[ipv6 virtual-address]{lang="EN-US"}**]{#struct_0_16980_17120_x2051683259}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x179166652}

[**[ipv6 virtual-address ]{lang="EN-US"}***[ipv6-address ]{lang="EN-US"}***[vsrp ]{lang="EN-US"}***[vsrp-instance]{lang="EN-US"}*]{#struct_0_16980_17120_694074779}

[**[undo ipv6 virtual-address]{lang="EN-US"}**]{#struct_0_16980_17120_x397812166}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1039351153}

[[未配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16980_17120_1878565024}[虚拟地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120880226}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_x393270654}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_97592702}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1955588546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_91528925}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_463416590}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_16980_17120_643152047}[：配置的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US"}[虚拟地址，该地址必须为链路本地地址，]{style="font-family:宋体"}[局域网内的主机可以通过这个虚拟地址与外部网络进行通信]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[**[vsrp ]{lang="EN-US"}***[vsrp-instance]{lang="EN-US"}*]{#struct_0_16980_17120_202569418}[：]{style="font-family:宋体"}[绑定的多机备份实例名称。]{style="font-family:宋体"}*[vsrp-instance]{lang="EN-US"}*[为多机备份的实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_104224045}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[接口上使能]{style="font-family:宋体"}]{#struct_0_16980_17120_x1618787301}[IPv6 IPoE]{lang="EN-US"}[或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的多机备份功能时，必须与本命令配合使用，本命令绑定的多机备份实例必须与该接口上]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[绑定的多机备份实例保持一致，否则会影响多机备份功能正常使用，导致多机备份后倒换后]{style="font-family:宋体"}[,]{lang="EN-US" style="font-family:宋体"}[局域网内的主机无法访问外部网络]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[接口上未开启]{style="font-family:宋体"}]{#struct_0_16980_17120_627447495}[IPv6 IPoE]{lang="EN-US"}[或]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[的多机备份功能时，请不要在该接口上配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[虚拟地址，否则可能导致设备上原来的链路本地地址不可用。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[请不要将此命令与]{style="font-family:宋体"}]{#struct_0_16980_17120_x861017745}[IPv6 VRRP]{lang="EN-US"}[备份组配置在同一个接口上，否则可能导致多机备份功能不能正常使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x905490279}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_x1120945762}[配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[虚拟]{style="font-family:宋体"}[地址为]{style="font-family:宋体"}[fe80::10]{lang="EN-US"}[，并绑定多机备份实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1402151683}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 virtual-address fe80::10 vsrp aaa]{lang="EN-US"}
:::

::: {#1491388115 .myid}
[]{#_Toc404796105}[]{#struct_0_16980_17120_x454894252}[]{#_Toc380605116}

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ip subscriber vsrp-instance**

------------------------------------------------------------------------

[**[ip subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_2011766940}[命令用来指定接口上]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[功能绑定的多机备份实例。]{style="font-family:
宋体"}

[**[undo ip subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1175658049}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1594283490}

[**[ip subscriber vsrp-instance ]{lang="EN-US"}***[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_366657174}

[**[undo ip subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_914276429}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1292144410}

[[接口上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_16980_17120_695085819}[功能未绑定多机备份实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1128223387}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_x1121011298}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1135187386}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x414176444}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1356350644}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x768452816}

[*[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_2049837690}[：表示接口绑定]{style="font-family:宋体"}[的多机备份实例名]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x72880305}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_x1500732827}[支持多机备份是指当一台设备故障时（包括设备故障、链路故障等），]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户的业务可以自动切换到备用设备上来，已上线的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户不需要重新拨号，计费、授权信息不丢失。]{style="font-family:宋体"}

[[用户通过该命令配置接口下]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_16980_17120_x470786135}[会话和指定多机备份实例关联，继而就可以通过多机备份提供的数据备份通道实时备份此接口上接入的动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1134214727}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_1191330543}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使能]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[多机备份的功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并绑定]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例]{style="font-family:宋体"}[instance1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_16980_17120_781408460}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber vsrp-instance instance1]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_222936587}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ip subscriber ]{lang="EN-US"}**]{#struct_0_16980_17120_x1154889496}**[vsrp-port]{lang="EN-US"}**
:::

::: {#438323134 .myid}
[]{#_Toc404796106}[]{#struct_0_16980_17120_x1121076834}[]{#_Toc380605117}

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ip subscriber vsrp-port**

------------------------------------------------------------------------

[**[ip subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_597689074}[命令用来配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo ip subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_209527447}[用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x881320367}

[**[ip subscriber vsrp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_1327907983}

[**[undo ip subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1164033574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1631629730}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_37635348}[建立]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60033]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_33625662}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x1961885836}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1506763156}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1946440765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1619327404}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_189037026}

[*[port-number]{lang="ES-AR"}*]{#struct_0_16980_17120_x1120618082}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_872001093}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_1713048219}[在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此条通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，可以通过本命令调整]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1138141693}

[[\#]{lang="SV"}[ ]{lang="SV"}]{#struct_0_16980_17120_2078187610}[配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_908160811}

[\[Sysname\] ip subscriber vsrp-port 20000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_94760959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ip subscriber ]{lang="EN-US"}**]{#struct_0_16980_17120_709329923}**[vsrp-instance]{lang="EN-US"}**
:::

::: {#824932745 .myid}
[]{#_Toc404796107}[]{#struct_0_16980_17120_878781811}[]{#_Toc380605155}

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ipv6 subscriber vsrp-instance**

------------------------------------------------------------------------

[**[ipv6 subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_257944873}[命令用来指定接口上的]{style="font-family:
宋体"}[IPv6 IPoE]{lang="EN-US"}[功能绑定的多机备份实例。]{style="font-family:
宋体"}

[**[undo ip subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1470004178}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120683618}

[**[ipv6 subscriber vsrp-instance ]{lang="EN-US"}***[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1944567480}

[**[undo ipv6 subscriber vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_735027824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x185749467}

[[接口上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_16980_17120_1951929550}[功能未绑定多机备份实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_86856748}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_x585352472}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1857594517}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1274020636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_691156232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1292108381}

[*[instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1514981367}[：表示接口绑定的]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1201740900}

[[用户通过该命令配置接口下]{style="font-family:宋体;color:windowtext"}]{#struct_0_16980_17120_514139017}[IPv6]{lang="EN-US" style="color:windowtext"}[ ]{lang="EN-US"}[IPoE]{lang="EN-US" style="color:windowtext"}[会话和指定多机备份实例关联，继而就可以通过多机备份提供的数据备份通道实时备份此接口上接入的动态]{style="font-family:宋体;
color:windowtext"}[IPv6]{lang="EN-US" style="color:windowtext"}[ ]{lang="EN-US"}[IPoE]{lang="EN-US" style="color:windowtext"}[会话信息。]{style="font-family:宋体;
color:windowtext"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1121142371}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_1837316913}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使能]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[多机备份的功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并绑定]{style="font-family:宋体"}[多机备份]{style="font-family:宋体"}[实例为]{style="font-family:宋体"}[instance1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_593439753}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_527345260}

[[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber vsrp-instance instance1]{lang="SV" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_x1938879043}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1314302404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ipv6 subscriber ]{lang="EN-US"}**]{#struct_0_16980_17120_543693842}**[vsrp-port]{lang="EN-US"}**
:::

::: {#-1259751003 .myid}
[]{#_Toc404796108}[]{#struct_0_16980_17120_2109646822}[]{#_Toc380605156}

**多机备份配置命令 \-- IPoE支持多机备份功能配置命令 \-- ipv6 subscriber vsrp-port**

------------------------------------------------------------------------

[**[ipv6 subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x181403425}[命令用来配置]{style="font-family:
宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo ipv6 subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x910241711}[用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x499557025}

[**[ipv6 subscriber vsrp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_x641951073}

[**[undo ipv6 subscriber vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1981122122}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x418542053}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_x1121207907}[建立]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60040]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x674406499}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x22561239}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x445453609}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1651729229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x246866300}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1221241296}

[*[port-number]{lang="ES-AR"}*]{#struct_0_16980_17120_736458254}[：]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1258675491}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_2072824974}[支持多机备份是指当一台设备故障时（包括设备故障、链路故障等），]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户的业务可以自动切换到备用设备上来，已上线的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户不需要重新拨号，计费、授权信息不丢失。]{style="font-family:宋体"}

[[IPoE]{lang="EN-US"}]{#struct_0_16980_17120_x984811023}[在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此条通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，可以通过本命令调整]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1266006539}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_1564348271}[配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[建立]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_16980_17120_x1121273443}

[\[Sysname\] ipv6 subscriber vsrp-port 20000]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1633716335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ipv6 subscriber ]{lang="EN-US"}**]{#struct_0_16980_17120_621189953}**[vsrp-instance]{lang="EN-US"}**
:::

::: {#-649471501 .myid}
[]{#_Toc404796110}[]{#struct_0_16980_17120_x10873247}[]{#_Toc375318229}[]{#_Toc359232048}[]{#_Toc357684243}

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- display ppp sync-session**

------------------------------------------------------------------------

[**[display ppp sync-session]{lang="EN-US"}**]{#struct_0_16980_17120_x1282275250}[命令用来查看同步的]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1291307882}

[**[display ppp sync-session ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[vsrp-instance]{lang="EN-US"}**[ ]{lang="EN-US"}*[vsrp-instance-name]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_16980_17120_858705251}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1161910333}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x887044753}[]{#_Toc32639298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1121338979}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1916724656}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_1029363509}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_2133496276}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_x250208281}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_24942263}

[**[vsrp-instance]{lang="EN-US"}***[ ]{lang="EN-US"}[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x2033765949}[：显示指定多机备份]{style="font-family:宋体"}[实例同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，将显示所有多机备份实例同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1267523182}

[[在主用设备和备用设备上都可以查询同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_16980_17120_1609412866}[会话信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在主用设备上查看的是主用设备同步给备用设备的]{style="font-family:宋体"}]{#struct_0_16980_17120_1575893549}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在备用设备上查看的是备用设备从主用设备同步过来的]{style="font-family:宋体"}]{#struct_0_16980_17120_1868605597}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[]{#struct_0_16980_17120_x1456956776}[[【举例】]{style="font-family:黑体"}]{#_Toc32639300}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1120880227}[查看同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display ppp sync-session]{lang="EN-US"}]{#struct_0_16980_17120_x1959354595}

[VSRP instance: vsrp1]{lang="EN-US"}

[VSRP instance state: Master]{lang="EN-US"}

[Total synchronized PPP sessions: 2]{lang="EN-US"}

[SID    MAC address     Interface     IP address       Username]{lang="EN-US"}

[1      00e0-1500-0410  GE1/0/1       2.2.2.2          user1@isp1]{lang="EN-US"}

[2      00e0-1500-0411  GE1/0/1       2.2.2.3          user1@isp1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSRP instance: vsrp2]{lang="EN-US"}

[VSRP instance state: Backup]{lang="EN-US"}

[Total synchronized PPP sessions: 1]{lang="EN-US"}

[SID    MAC address     Interface     IP address       Username]{lang="EN-US"}

[1      00e0-1500-0413  GE1/0/2       2.3.2.2          user1@isp1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSRP instance: vsrp3]{lang="EN-US"}

[VSRP instance state: Down]{lang="EN-US"}

[Total synchronized PPP sessions: 0]{lang="EN-US"}

[SID    MAC address     Interface     IP address       Username]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[ display ppp sync-session]{lang="EN-US"}]{#struct_0_16980_17120_1212825515}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1931769880}[[字段]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120945763}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16980_17120_1326731672}

[[VSRP instance]{lang="EN-US"}]{#struct_0_16980_17120_x806574047}

[[多机备份实例名称]{style="font-family:宋体"}]{#struct_0_16980_17120_x1121011299}

[[VSRP instance state]{lang="EN-US"}]{#struct_0_16980_17120_430896555}

[[多机备份实例状态：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1121076835}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_x2131194281}[：表示在该多机备份实例中，本设备作为主用设备，此时显示的是本设备同步给备用设备的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_x1120618083}[：表示在该多机备份实例中，本设备作为备用设备，此时显示的是本设备从主用设备同步过来的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16980_17120_x1856882262}[：表示在该多机备份实例中，本设备不运行，此时没有同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息（在下面两种情况下设备会处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态：一是当]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组处于]{style="font-family:宋体"}[initialize]{lang="EN-US"}[状态时，互相备份的两台设备在对应]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中将都处于无法运行状态；二是本端]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例不存在或者配置不完整）]{style="font-family:宋体"}

[[Total synchronized PPP sessions]{lang="EN-US"}]{#struct_0_16980_17120_x1120683619}

[[同步的]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_16980_17120_784315875}[会话数目]{style="font-family:宋体"}

[[SID]{lang="EN-US"}]{#struct_0_16980_17120_x1121142372}

[[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_x2054365856}[会话]{style="font-family:宋体"}[session ID]{lang="EN-US"}

[[MAC address]{lang="EN-US"}]{#struct_0_16980_17120_x1121207908}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16980_17120_441338748}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_16980_17120_x1121273444}

[[接入的接口名称]{style="font-family:宋体"}]{#struct_0_16980_17120_x67632394}

[[IP address]{lang="EN-US"}]{#struct_0_16980_17120_x1121338980}

[[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16980_17120_x6179469}[地址]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_16980_17120_x2010784485}

[[用户名称]{style="font-family:宋体"}]{#struct_0_16980_17120_x1120880228}

[ ]{lang="EN-US"}

::: {#1166932525 .myid}
[]{#_Toc404796111}[]{#struct_0_16980_17120_x1556070068}[]{#_Toc375318230}[]{#_Toc359246082}[]{#_Toc357684244}

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- display pppoe-server sync-session**

------------------------------------------------------------------------

[**[display pppoe-server sync-session]{lang="EN-US"}**]{#struct_0_16980_17120_1470811442}[命令用来查看同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_425574248}

[**[display pppoe-server sync-session]{lang="EN-US"}**[ \[ **vsrp-instance** *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_960767797}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x586899685}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x1120945764}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_2086246559}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1519889438}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_x1256692789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x273666665}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_391691877}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1395433563}

[**[vsrp-instance]{lang="EN-US"}***[ ]{lang="EN-US"}[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1196492202}[：显示指定多机备份]{style="font-family:宋体"}[实例同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[表示多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，将显示所有多机备份实例同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1552871233}

[[在主用设备和备用设备上都可以查询同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_1921232752}[会话信息：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在主用设备上查看的是主用设备同步给备用设备的]{style="font-family:宋体"}]{#struct_0_16980_17120_x1310057125}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在备用设备上查看的是备用设备从主用设备同步过来的]{style="font-family:宋体"}]{#struct_0_16980_17120_x1665330775}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1121011300}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1490958993}[查看同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display pppoe-server sync-session]{lang="EN-US"}]{#struct_0_16980_17120_1015240006}

[VSRP instance: vsrp1]{lang="EN-US"}

[VSRP instance state: Master]{lang="EN-US"}

[Total synchronized PPPoE sessions: 2]{lang="EN-US"}

[SID    Service VLAN  Customer VLAN  MAC address    Interface]{lang="EN-US"}

[1      1             1              00e0-1500-0410 GE1/0/1]{lang="EN-US"}

[2      1             1              00e0-1500-0411 GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSRP instance: vsrp2]{lang="EN-US"}

[VSRP instance state: Backup]{lang="EN-US"}

[Total synchronized PPPoE sessions: 1]{lang="EN-US"}

[SID    Service VLAN  Customer VLAN  MAC address    Interface]{lang="EN-US"}

[1      1             2              00e0-1500-0413 XGE1/0/2]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSRP instance: vsrp3]{lang="EN-US"}

[VSRP instance state: Down]{lang="EN-US"}

[Total synchronized PPPoE sessions: 0]{lang="EN-US"}

[SID    Service VLAN  Customer VLAN  MAC address    Interface]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display pppoe-server sync-session]{lang="EN-US"}]{#struct_0_16980_17120_2069038439}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1939980436}[[字段]{style="font-family:黑体"}]{#struct_0_16980_17120_x1121076836}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16980_17120_x565110340}

[[VSRP instance]{lang="EN-US"}]{#struct_0_16980_17120_x1120618084}

[[VSRP]{lang="EN-US"}]{#struct_0_16980_17120_1678570147}[实例名称]{style="font-family:宋体"}

[[VSRP instance state]{lang="EN-US"}]{#struct_0_16980_17120_x1060686753}

[[多机备份实例状态：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1120683620}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_x1588271584}[：表示在该多机备份实例中，本设备作为主用设备，此时显示的是本设备同步给备用设备的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_x1121142373}[：表示在该多机备份实例中，本设备作为备用设备，此时显示的是本设备从主用设备同步过来的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_16980_17120_674517499}[：表示在该多机备份实例中，本设备不运行，此时没有同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话信息（在下面两种情况下设备会处于]{style="font-family:宋体"}[Down]{lang="EN-US"}[状态：一是当]{style="font-family:宋体"}[VRRP]{lang="EN-US"}[备份组处于]{style="font-family:宋体"}[initialize]{lang="EN-US"}[状态时，互相备份的两台设备在对应]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例中将都处于无法运行状态；二是本端多机备份实例不存在或者配置不完整）]{style="font-family:宋体"}

[[Total synchronized PPPoE sessions]{lang="EN-US"}]{#struct_0_16980_17120_x1121207909}

[[同步的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_x1124745193}[会话数目]{style="font-family:宋体"}

[[SID]{lang="EN-US"}]{#struct_0_16980_17120_x1121273445}

[[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_1498451547}[会话]{style="font-family:宋体"}[session ID]{lang="EN-US"}

[[Service VLAN]{lang="EN-US"}]{#struct_0_16980_17120_x1121338981}

[[服务提供商]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16980_17120_1559904472}

[[Customer VLAN]{lang="EN-US"}]{#struct_0_16980_17120_x1206365822}

[[用户]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_16980_17120_x1120880229}

[[MAC address]{lang="EN-US"}]{#struct_0_16980_17120_1172813287}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_16980_17120_x1120945765}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_16980_17120_520162618}

[[接入的接口名称]{style="font-family:宋体"}]{#struct_0_16980_17120_x1121011301}

[ ]{lang="EN-US"}

::: {#-433610411 .myid}
[]{#_Toc404796112}[]{#struct_0_16980_17120_75124948}

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- ppp vsrp-port**

------------------------------------------------------------------------

[**[ppp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1404487434}[命令用来配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo ppp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_42172728}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1989407855}

[**[ppp vsrp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_x1863989134}

[**[undo ppp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1175420722}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x165858171}

[[PPP]{lang="EN-US"}]{#struct_0_16980_17120_x1121076837}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60035]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1000973601}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x141316568}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1455445329}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1479811704}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1701891551}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1239728868}

[*[port-number]{lang="ES-AR"}*]{#struct_0_16980_17120_x337045292}[：]{style="font-family:宋体"}[PPP]{lang="SV"}[会话]{style="font-family:宋体"}[数]{style="font-family:
宋体"}[据备份通道的]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_577936031}

[[PPP]{lang="EN-US"}]{#struct_0_16980_17120_x513465308}[会话在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[用户可以通过本命令指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_16980_17120_x1796788115}[连接的端口号，如果不指定则用缺省端口号发起连接。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1120618085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的端口号不能与系统中已经使用的端口号冲突。]{style="font-family:宋体"}]{#struct_0_16980_17120_x1050313208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主用设备和备用设备上配置的对应端口号必须一致，否则]{style="font-family:宋体"}]{#struct_0_16980_17120_1577969119}[TCP]{lang="EN-US"}[连接将建立失败，数据备份通道不通]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x112649621}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1947073766}[指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_808012689}

[\[Sysname\] ppp vsrp-port 20000]{lang="EN-US"}
:::

::: {#-2062090440 .myid}
[]{#_Toc336084869}[]{#_Toc332298259}[]{#_Toc404796113}[]{#struct_0_16980_17120_1634761303}[]{#_Toc375318232}[]{#_Toc359246092}[]{#_Toc357684248}

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- pppoe-server vsrp-instance**

------------------------------------------------------------------------

[**[pppoe-server vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x176250850}[命令用来配置接口下]{style="font-family:
宋体"}[PPPoE Server]{lang="EN-US"}[绑定指定的多机备份实例。]{style="font-family:
宋体"}

[**[undo pppoe-server vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1039269416}[命令用来取消接口下]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[绑定的多机备份实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1701901128}

[**[pppoe-server vsrp-instance ]{lang="EN-US"}***[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x8677537}

[**[undo pppoe-server vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1120683621}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1140611771}

[[接口下]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}]{#struct_0_16980_17120_x1700743128}[未绑定多机备份实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1709134159}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_978712121}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/EFM]{lang="EN-US"}[子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1002244596}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x682101105}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1674397439}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x884253068}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_309120935}[：多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x947833231}

[[在接口下配置本命令后，就可以通过多机备份模块提供的数据备份通道实时备份接口上接入的]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_1952947512}[会话信息和]{style="font-family:宋体"}[PPP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1121142366}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，多机备份实例可以不存在，但只有配置了多机备份实例后本命令才生效。]{style="font-family:宋体"}]{#struct_0_16980_17120_271298508}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能绑定一个多机备份实例，同一接口下的多个子接口可以绑定同一个多机备份实例。]{style="font-family:宋体"}]{#struct_0_16980_17120_x830173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同接口不能绑定同一个多机备份实例。如果要绑定的多机备份实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。]{style="font-family:宋体"}]{#struct_0_16980_17120_x2063632274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口下配置本命令，会清除接口下所有已经上线的用户。]{style="font-family:宋体"}]{#struct_0_16980_17120_x746758360}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_2119546442}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1171463679}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口下]{style="font-family:宋体"}[PPPoE Server]{lang="EN-US"}[绑定名为]{style="font-family:宋体"}[vsrp1]{lang="EN-US"}[的多机备份实例。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_297079235}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] pppoe-server vsrp-instance vsrp1]{lang="EN-US"}
:::

::: {#164939516 .myid}
[]{#_Toc404796114}[]{#struct_0_16980_17120_x960360032}[]{#_Toc375318233}[]{#_Toc359246101}[]{#_Toc357684249}

**多机备份配置命令 \-- PPPoE支持多机备份功能配置命令 \-- pppoe-server vsrp-port**

------------------------------------------------------------------------

[**[pppoe-server vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x1110957850}[命令用来配置]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号。]{style="font-family:宋体"}

[**[undo pppoe-server vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x1687886605}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2047022897}

[**[pppoe-server vsrp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_x836893853}

[**[undo pppoe-server vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x1121207902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1077691026}

[[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_1411434050}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号为]{style="font-family:宋体"}[60034]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x718678264}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_1478326200}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x165744436}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1496386602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1844158321}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2063734643}

[*[port-number]{lang="ES-AR"}*]{#struct_0_16980_17120_x256334285}[：]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1086709820}

[[PPPoE]{lang="EN-US"}]{#struct_0_16980_17120_1700437725}[会话在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[用户可以通过本命令指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_16980_17120_x1121273438}[连接的端口号，如果不指定则用缺省端口号发起连接。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1680311750}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的端口号不能与系统中已经使用的端口号冲突。]{style="font-family:宋体"}]{#struct_0_16980_17120_x986122103}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主用设备和备用设备上配置的对应端口号必须一致，否则]{style="font-family:宋体"}]{#struct_0_16980_17120_x16819407}[TCP]{lang="EN-US"}[连接将建立失败，数据备份通道不通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_2102194984}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1670911620}[指定]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[会话数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[30000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x465539803}

[\[Sysname\] pppoe-server vsrp-port 30000]{lang="EN-US"}
:::

::: {#371253597 .myid}
[]{#_Toc404796116}[]{#struct_0_16980_17120_x1607769366}[]{#_Toc379813159}[]{#_Toc369009550}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp session vsrp**

------------------------------------------------------------------------

[**[display l2tp session vsrp]{lang="EN-US"}**]{#struct_0_16980_17120_986017919}[命令用来显示多机备份实例下的]{style="font-family:
宋体"}[L2TP]{lang="EN-US"}[会话信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1121338974}

[**[display l2tp session vsrp]{lang="EN-US"}**[ \[ *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_x1974958113}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1709540262}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_1375806276}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_454750118}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_369075080}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_1362841677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_877971300}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_x112409817}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1209664217}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x94570989}[：多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有多机备份实例下的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120880222}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1932328174}[显示多机备份实例]{style="font-family:宋体"}[abc]{lang="EN-US"}[下的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp session vsrp abc]{lang="EN-US"}]{#struct_0_16980_17120_x566380011}

[]{#_Toc95359215}[]{#_Toc85604325}[]{#_Toc81386704}[]{#_Toc74661827}[]{#_Toc72589790}[]{#_Toc72589517}[]{#_Toc72589002}[]{#_Toc65921172}[]{#_Toc65919120}[]{#_Toc65919095}[]{#_Toc65910729}[]{#_Toc65909974}[]{#_Toc60125184}[VSRP instance name: abc]{lang="EN-US"}

[Local session ID: 1]{lang="EN-US"}

[Remote session ID: 1]{lang="EN-US"}

[Local tunnel ID: 1]{lang="EN-US"}

[State: Established]{lang="EN-US"}

[User ID: 00e0fc112233000300000004]{lang="EN-US"}

[Interface: Virtual-Access0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display l2tp session vsrp]{lang="EN-US"}]{#struct_0_16980_17120_x1107877631}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1916684333}[[字段]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120945758}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16980_17120_x595779237}

[[VSRP instance name]{lang="EN-US"}]{#struct_0_16980_17120_x1121011294}

[[会话所属的多机备份实例的名称]{style="font-family:宋体"}]{#struct_0_16980_17120_x1121076830}

[[Local session ID]{lang="EN-US"}]{#struct_0_16980_17120_x1371679394}

[[本端的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_x1120618078}

[[Remote session ID]{lang="EN-US"}]{#struct_0_16980_17120_66415079}

[[远端的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_x1120683614}

[[Local tunnel ID]{lang="EN-US"}]{#struct_0_16980_17120_x1121142367}

[[本端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_x1294785433}

[[State]{lang="EN-US"}]{#struct_0_16980_17120_x1121207903}

[[会话的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_1651192329}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_16980_17120_x1121273439}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-tunnel]{lang="EN-US"}]{#struct_0_16980_17120_x1121338975}[：等待建立隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-reply]{lang="EN-US"}]{#struct_0_16980_17120_x408874172}[：等待]{lang="EN-US" style="font-family:宋体"}[ICRP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_16980_17120_x1120880223}[：会话成功建立]{lang="EN-US" style="font-family:宋体"}

[[User ID]{lang="EN-US"}]{#struct_0_16980_17120_x1120945759}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_2133104118}

[[Interface]{lang="EN-US"}]{#struct_0_16980_17120_x1121011295}

[[LAC]{lang="EN-US"}]{#struct_0_16980_17120_2044034663}[侧]{style="font-family:宋体"}[PPP]{lang="EN-US"}[链路的]{style="font-family:宋体"}[VA]{lang="EN-US"}[接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1993718314 .myid}
[]{#_Toc404796117}[]{#struct_0_16980_17120_x1121076831}[]{#_Toc379813160}[]{#_Toc369009551}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp tunnel vsrp**

------------------------------------------------------------------------

[**[display l2tp tunnel vsrp]{lang="DE"}**]{#struct_0_16980_17120_194404547}[命令用来显示多机备份实例下的]{style="font-family:宋体"}[L2TP]{lang="DE"}[隧道信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_873588234}

[**[display l2tp tunnel vsrp]{lang="EN-US"}**[ \[ *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_378411237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1600420461}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x1286642392}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1854317670}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x308742922}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_x1077540783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x117260639}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_x1120618079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1632499020}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x2074131243}[：]{style="font-family:宋体"}[多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有多机备份实例下的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_519874192}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1336726455}[显示多机备份实例]{style="font-family:宋体"}[abc]{lang="EN-US"}[下]{style="font-family:宋体"}[的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp tunnel vsrp abc]{lang="EN-US"}]{#struct_0_16980_17120_524364681}

[VSRP instance name: abc]{lang="EN-US"}

[Local tunnel ID: 1]{lang="EN-US"}

[Remote tunnel ID: 1]{lang="EN-US"}

[State: Established]{lang="EN-US"}

[Sessions: 1]{lang="EN-US"}

[Remote address: 20.1.1.2]{lang="EN-US"}

[Remote port: 1701]{lang="EN-US"}

[Remote name: lns]{lang="EN-US"}

[Local address: 2.2.2.2]{lang="EN-US"}

[Sequence number sent (Ns): 2]{lang="EN-US"}

[Sequence number expected (Nr): 3]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display l2tp tunnel vsrp]{lang="EN-US"}]{#struct_0_16980_17120_x935626763}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1896246686}[[字段]{style="font-family:黑体"}]{#struct_0_16980_17120_x1120683615}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16980_17120_36866401}

[[VSRP instance name]{lang="EN-US"}]{#struct_0_16980_17120_440625013}

[[隧道所属的多机备份实例的名称]{style="font-family:宋体"}]{#struct_0_16980_17120_36931937}

[[Local tunnel ID]{lang="EN-US"}]{#struct_0_16980_17120_x1899369762}

[[本端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_36735329}

[[Remote tunnel ID]{lang="EN-US"}]{#struct_0_16980_17120_36800865}

[[远端的隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_16980_17120_34623657}

[[State]{lang="EN-US"}]{#struct_0_16980_17120_36604257}

[[隧道的状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_36669793}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Idle]{lang="EN-US"}]{#struct_0_16980_17120_x205384823}[：空闲状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait-reply]{lang="EN-US"}]{#struct_0_16980_17120_36473185}[：等待]{lang="EN-US" style="font-family:宋体"}[SCCRP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_16980_17120_1609750702}[：隧道成功建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stopping]{lang="EN-US"}]{#struct_0_16980_17120_36538721}[：正在]{lang="EN-US" style="font-family:宋体"}[断开隧道]{style="font-family:宋体"}

[[Sessions]{lang="EN-US"}]{#struct_0_16980_17120_37390689}

[[隧道上的会话数目]{style="font-family:宋体"}]{#struct_0_16980_17120_1786358260}

[[Remote address]{lang="EN-US"}]{#struct_0_16980_17120_37456225}

[[对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16980_17120_36866400}[地址]{style="font-family:宋体"}

[[Remote port]{lang="EN-US"}]{#struct_0_16980_17120_x1898027147}

[[对端]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_36931936}[使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Remote name]{lang="EN-US"}]{#struct_0_16980_17120_36735328}

[[隧道对端的名称]{style="font-family:宋体"}]{#struct_0_16980_17120_181538371}

[[Local address]{lang="EN-US"}]{#struct_0_16980_17120_36800864}

[[本端的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_16980_17120_36604256}[地址]{style="font-family:宋体"}

[[Sequence number sent (Ns)]{lang="EN-US"}]{#struct_0_16980_17120_2099743448}

[[发送报文的序号]{style="font-family:宋体"}]{#struct_0_16980_17120_36669792}

[[Sequence number expected (Nr)]{lang="EN-US"}]{#struct_0_16980_17120_36473184}

[[期望接收到的下一个控制报文中]{style="font-family:宋体"}[Ns]{lang="EN-US"}]{#struct_0_16980_17120_x346564434}[字段的值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_2079342274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[reset l2tp tunnel]{lang="EN-US"}**]{#struct_0_16980_17120_x661778154}[（]{lang="EN-US" style="font-family:宋体"}[二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入]{style="font-family:宋体"}[/L2TP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

::: {#-36031710 .myid}
[]{#_Toc404796118}[]{#struct_0_16980_17120_36538720}[]{#_Toc379813161}[]{#_Toc369009552}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- display l2tp vsrp**

------------------------------------------------------------------------

[**[display l2tp vsrp]{lang="DE"}**]{#struct_0_16980_17120_x332125228}[命令用来显示应用于]{style="font-family:宋体"}[L2TP]{lang="DE"}[的多机备份实例的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_10459911}

[**[display l2tp vsrp ]{lang="EN-US"}**[\[ *vsrp-instance-name* \]]{lang="EN-US"}]{#struct_0_16980_17120_196782253}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1452459013}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16980_17120_2068439286}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1993086858}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_5456358}

[[network-operator]{lang="EN-US"}]{#struct_0_16980_17120_356497835}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_255632741}

[[mdc-operator]{lang="EN-US"}]{#struct_0_16980_17120_x654514256}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_37390688}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x169956876}[：]{style="font-family:宋体"}[多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示应用于]{style="font-family:宋体"}[L2TP]{lang="DE"}[的所有多机备份实例的运行信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1290853702}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_459143636}[显示应用于]{style="font-family:宋体"}[L2TP]{lang="DE"}[的多机备份实例]{style="font-family:宋体"}[abc]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2tp vsrp abc]{lang="EN-US"}]{#struct_0_16980_17120_37456224}

[VSRP instance name: abc]{lang="EN-US"}

[VSRP mode: Hot]{lang="EN-US"}

[VSRP status: Switched]{lang="EN-US"}

[Local VSRP state: Master/Up]{lang="EN-US"}

[Remote VSRP state: Backup]{lang="EN-US"}

[VSRP channel state: Synced]{lang="EN-US"}

[Sent messages: 13005]{lang="EN-US"}

[Received messages: 23]{lang="EN-US"}

[Discarded sent messages: 22]{lang="EN-US"}

[Discarded received messages: 13]{lang="EN-US"}

[Sent tunnel add messages: 8000]{lang="EN-US"}

[Received tunnel add messages: 0]{lang="EN-US"}

[Sent tunnel delete messages: 5500]{lang="EN-US"}

[Received tunnel delete messages: 0]{lang="EN-US"}

[Sent session add messages: 20000]{lang="EN-US"}

[Received session add messages: 0]{lang="EN-US"}

[Sent session delete messages: 10000]{lang="EN-US"}

[Received session delete messages: 0]{lang="EN-US"}

[Current tunnels: 2500]{lang="EN-US"}

[Current sessions: 10000]{lang="EN-US"}

[Added tunnels: 8000]{lang="EN-US"}

[Deleted tunnels: 5500]{lang="EN-US"}

[Added sessions: 20000]{lang="EN-US"}

[Deleted sessions: 10000]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display l2tp vsrp]{lang="EN-US"}]{#struct_0_16980_17120_x610579805}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1891539546}[[字段]{style="font-family:黑体"}]{#struct_0_16980_17120_734003898}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16980_17120_36866399}

[[VSRP instance name]{lang="EN-US"}]{#struct_0_16980_17120_1283864376}

[[多机备份实例的名称]{style="font-family:宋体"}]{#struct_0_16980_17120_36931935}

[[VSRP mode]{lang="EN-US"}]{#struct_0_16980_17120_36735327}

[[备份模式，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_x245428669}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hot]{lang="EN-US"}]{#struct_0_16980_17120_36800863}[：热]{lang="EN-US" style="font-family:宋体"}[备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Warm]{lang="EN-US"}]{#struct_0_16980_17120_36604255}[：温]{lang="EN-US" style="font-family:宋体"}[备份]{style="font-family:宋体"}

[[VSRP status]{lang="EN-US"}]{#struct_0_16980_17120_525765336}

[[多机备份组的主备切换状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_36669791}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Switching]{lang="EN-US"}]{#struct_0_16980_17120_x587721847}[：]{lang="EN-US" style="font-family:宋体"}[正在进行主备]{style="font-family:宋体"}[切换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Switched]{lang="EN-US"}]{#struct_0_16980_17120_36473183}[：]{lang="EN-US" style="font-family:宋体"}[主备]{style="font-family:宋体"}[切换完成]{lang="EN-US" style="font-family:宋体"}

[[Local VSRP state]{lang="EN-US"}]{#struct_0_16980_17120_36538719}

[[本端多机备份组状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1471242129}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master/Up]{lang="EN-US"}]{#struct_0_16980_17120_37390687}[：]{lang="EN-US" style="font-family:宋体"}[本端作为主设备]{style="font-family:宋体"}[/]{lang="EN-US"}[多机备份组可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup/Up]{lang="EN-US"}]{#struct_0_16980_17120_37456223}[：本端作为备设备]{style="font-family:宋体"}[/]{lang="EN-US"}[多机备份组可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master/Down]{lang="EN-US"}]{#struct_0_16980_17120_963398307}[：]{lang="EN-US" style="font-family:宋体"}[本端作为主设备]{style="font-family:宋体"}[/]{lang="EN-US"}[多机备份组不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup/Down]{lang="EN-US"}]{#struct_0_16980_17120_36866398}[：]{lang="EN-US" style="font-family:宋体"}[本端作为备设备]{style="font-family:宋体"}[/]{lang="EN-US"}[多机备份组不可用]{style="font-family:宋体"}

[[Remote VSRP state]{lang="EN-US"}]{#struct_0_16980_17120_x1054787784}

[[对端多机备份组状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_36931934}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Master]{lang="EN-US"}]{#struct_0_16980_17120_36735326}[：]{lang="EN-US" style="font-family:宋体"}[对端作为主设备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_16980_17120_2093223491}[：对端作为备设备]{style="font-family:宋体"}

[[VSRP channel state]{lang="EN-US"}]{#struct_0_16980_17120_36800862}

[[数据备份通道状态，取值包括：]{style="font-family:宋体"}]{#struct_0_16980_17120_36604254}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disconnected]{lang="EN-US"}]{#struct_0_16980_17120_x1812886824}[：断开]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Snycing]{lang="EN-US"}]{#struct_0_16980_17120_36669790}[：正在]{lang="EN-US" style="font-family:宋体"}[数据同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Synced]{lang="EN-US"}]{#struct_0_16980_17120_36473182}[：数据同步]{lang="EN-US" style="font-family:宋体"}[完成]{style="font-family:宋体"}

[[Sent messages]{lang="EN-US"}]{#struct_0_16980_17120_35772590}

[[本设备发送的备份消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36538718}

[[Received messages]{lang="EN-US"}]{#struct_0_16980_17120_37390686}

[[本设备接收的备份消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_x2081641996}

[[Discarded sent messages]{lang="EN-US"}]{#struct_0_16980_17120_37456222}

[[本设备在发送方向丢弃的消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36866405}

[[Discarded received messages]{lang="EN-US"}]{#struct_0_16980_17120_1205299061}

[[本设备在接收方向丢弃的消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36931941}

[[Sent tunnel add messages]{lang="EN-US"}]{#struct_0_16980_17120_36735333}

[[本设备发送的新建隧道消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_555981224}

[[Received tunnel add messages]{lang="EN-US"}]{#struct_0_16980_17120_36800869}

[[本设备接收的新建隧道消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36604261}

[[Sent tunnel delete messages]{lang="EN-US"}]{#struct_0_16980_17120_x275644557}

[[本设备发送的删除隧道消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36669797}

[[Received tunnel delete messages]{lang="EN-US"}]{#struct_0_16980_17120_36473189}

[[本设备接收的删除隧道消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_x391194450}

[[Sent session add messages]{lang="EN-US"}]{#struct_0_16980_17120_36538725}

[[本设备发送的新建会话消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_37390693}

[[Received session add messages]{lang="EN-US"}]{#struct_0_16980_17120_x2089536167}

[[本设备接收的新建会话消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_37456229}

[[Sent session delete messages]{lang="EN-US"}]{#struct_0_16980_17120_36866404}

[[本设备发送的删除会话消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_x1133353099}

[[Received session delete messages]{lang="EN-US"}]{#struct_0_16980_17120_36931940}

[[本设备接收的删除会话消息数]{style="font-family:宋体"}]{#struct_0_16980_17120_36735332}

[[Current tunnels]{lang="EN-US"}]{#struct_0_16980_17120_x1400333912}

[[多机备份实例下的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_36800868}[隧道数]{style="font-family:宋体"}

[[Current sessions]{lang="EN-US"}]{#struct_0_16980_17120_36604260}

[[多机备份实例下的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_36669796}[会话数]{style="font-family:宋体"}

[[Added tunnels]{lang="EN-US"}]{#struct_0_16980_17120_x1779362935}

[[多机备份实例下新建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_36473188}[隧道的次数]{style="font-family:宋体"}

[[Deleted tunnels]{lang="EN-US"}]{#struct_0_16980_17120_36538724}

[[多机备份实例下删除]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_432548820}[隧道的次数]{style="font-family:宋体"}

[[Added sessions]{lang="EN-US"}]{#struct_0_16980_17120_37390692}

[[多机备份实例下新建]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_37456228}[会话的次数]{style="font-family:宋体"}

[[Deleted sessions]{lang="EN-US"}]{#struct_0_16980_17120_1602950342}

[[多机备份实例下删除]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_2021597894}[会话的次数]{style="font-family:宋体"}

[]{#_Toc96758199}[]{#_Toc54583756}[]{#_Toc35242896}[]{#_Toc16936660}[]{#_Toc15876338}[ ]{lang="EN-US"}

::: {#602584322 .myid}
[]{#_Toc404796119}[]{#struct_0_16980_17120_x26627362}[]{#_Toc379813162}[]{#_Toc369009553}[]{#_Toc359316247}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- l2tp tunnel-id**

------------------------------------------------------------------------

[**[l2tp tunnel-id]{lang="EN-US"}**]{#struct_0_16980_17120_6585969}[命令用来配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[的分配范围。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[l2tp tunnel-id]{lang="EN-US"}**]{#struct_0_16980_17120_1603015878}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x693212425}

[**[l2tp tunnel-id]{lang="EN-US"}**[ *low high*]{lang="EN-US"}]{#struct_0_16980_17120_x759022518}

[**[undo ]{lang="EN-US"}[l2tp tunnel-id]{lang="EN-US"}**]{#struct_0_16980_17120_1766328431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x822890733}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_1915617757}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[的分配范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x391612039}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_x1719452370}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x228257179}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_30575636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1602819270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1535427493}

[*[low]{lang="SV"}*]{#struct_0_16980_17120_x1667165606}[：]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配范围的下边界值，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[high]{lang="SV"}*]{#struct_0_16980_17120_527766185}[：]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配范围的上边界值，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，并且上边界值不能小于下边界值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_149139505}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_x905267554}[多机备份组网中的两台]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备可以利用不同的多机备份实例来实现负载分担，比如：在多机备份实例]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:宋体"}[LAC1]{lang="EN-US"}[为主用设备，]{style="font-family:宋体"}[LAC2]{lang="EN-US"}[为备用设备；而在多机备份实例]{style="font-family:宋体"}[2]{lang="EN-US"}[中]{style="font-family:宋体"}[LAC2]{lang="EN-US"}[为主用设备，]{style="font-family:宋体"}[LAC1]{lang="EN-US"}[为备用设备。这种情况下，要求不同多机备份实例中的主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[不能冲突，因此需要为两台]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备配置不同的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配范围。]{style="font-family:宋体"}

[[需要注意的是，当]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_16980_17120_x921547124}[设备上存在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时，不能修改]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[分配范围。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x537490276}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_1164239513}[配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[的分配范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_112141264}

[\[Sysname\] l2tp tunnel-id 20 100]{lang="EN-US"}
:::

::: {#2139316113 .myid}
[]{#_Toc404796120}[]{#struct_0_16980_17120_1602884806}[]{#_Toc379813163}[]{#_Toc369009563}[]{#_Toc359316248}[]{#_Toc352760605}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- l2tp vsrp-port**

------------------------------------------------------------------------

[**[l2tp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_66647373}[命令用来配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo l2tp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x1688439968}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_1591960857}

[**[l2tp vsrp-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_16980_17120_2085050248}

[**[undo l2tp vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x595498251}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x153452207}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_x524482221}[数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60036]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x30545265}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_409143343}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1602688198}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1964886152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_978062953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1014981785}

[*[port-number]{lang="ES-AR"}*]{#struct_0_16980_17120_1269075819}[：]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数]{style="font-family:宋体"}[据备份通道的]{style="font-family:宋体"}[TCP]{lang="SV"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1362650414}

[[在进行]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_x626567610}[数据备份之前，主用和备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备之间需要先建立一条]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据备份通道，此通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。通过此命令可以调整]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的端口号。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x2021552996}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[主用和备用]{style="font-family:宋体"}]{#struct_0_16980_17120_x1333144090}[LAC]{lang="EN-US"}[设备必须配置相同的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，才能正确建立]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据备份通道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[指定的]{style="font-family:宋体"}]{#struct_0_16980_17120_x655321705}[L2TP]{lang="EN-US"}[数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号不能与系统中已经使用的端口号冲突。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1602753734}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1471566102}[配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_240314732}

[\[Sysname\] l2tp vsrp-port 20000]{lang="EN-US"}
:::

::: {#-575546779 .myid}
[]{#_Toc404796121}[]{#struct_0_16980_17120_1397060823}[]{#_Toc379813164}[]{#_Toc369009564}[]{#_Toc359316246}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- tunnel vsrp source-ip**

------------------------------------------------------------------------

[**[tunnel vsrp source-ip]{lang="EN-US"}**]{#struct_0_16980_17120_1786206383}[命令用来设置多机备份情况下]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址，即封装后]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道报文的源地址。]{style="font-family:宋体"}

[**[undo tunnel vsrp source-ip]{lang="EN-US"}**]{#struct_0_16980_17120_1763139809}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x145546385}

[**[tunnel vsrp source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_16980_17120_x1158916715}

[**[undo tunnel vsrp source-ip]{lang="EN-US"}**]{#struct_0_16980_17120_1297276222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1236615715}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_1602557126}[隧道的源端地址为本端]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道出接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_1236238617}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_x1652704716}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x945531535}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1656587721}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_2108683314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x143416559}

[*[ip-address]{lang="SV"}*]{#struct_0_16980_17120_x1042459217}[：多机备份情况下]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1512945049}

[[主用和备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}]{#struct_0_16980_17120_x1650213505}[设备必须使用本命令配置相同的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。配置了本命令后，主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备上会生成到源端地址的静态路由，路由的出接口为]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口。当主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备故障，发生主备倒换后，原主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备将删除该静态路由，并利用动态路由协议发布路由删除消息。新的主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备（即原备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备）会生成到源端地址的静态路由，并利用动态路由协议发布路由添加消息。这样，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[到远端的下行流量会自动切换到新的主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备上，]{style="font-family:宋体"}[LNS]{lang="EN-US"}[会认为原来的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道仍然保持建立。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_1602622662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_2048146027}[隧道的源端地址可以不是本设备上接口的地址，若是设备接口的地址必须保证是]{style="font-family:宋体"}[32]{lang="EN-US"}[位掩码的]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址，只要保证源端地址不与网络中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址冲突即可。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[建议为不同的]{style="font-family:宋体"}]{#struct_0_16980_17120_1603540166}[L2TP]{lang="EN-US"}[组配置不同的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[必须先配置]{style="font-family:宋体"}]{#struct_0_16980_17120_2043487044}[L2TP]{lang="EN-US"}[组关联的多机备份实例，才能为该]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组配置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_16980_17120_x834866994}[L2TP]{lang="EN-US"}[组下存在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时，不能修改或删除为该]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组配置的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道源端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_1142553064}[多机备份的情况下，如果]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[视图]{style="font-family:宋体"}[下同时配置了]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[source-ip]{lang="EN-US"}**[命令，将使用]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[命令指定的地址作为]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址；如果]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[视图]{style="font-family:宋体"}[下配置了]{lang="EN-US" style="font-family:宋体"}**[source-ip]{lang="EN-US"}**[命令，没有配置]{lang="EN-US" style="font-family:宋体"}**[tunnel vsrp source-ip]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}[，将会导致]{lang="EN-US" style="font-family:宋体"}[L2TP]{lang="EN-US"}[多机备份故障]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_498716306}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_1151724913}[设置]{style="font-family:宋体"}[多机备份情况下]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道的源端地址]{style="font-family:宋体"}[为]{style="font-family:宋体"}[2.2.2.2]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_16980_17120_1602950341}

[\[Sysname\] l2tp-group 1 mode lac]{lang="SV"}

[\[Sysname-l2tp1\] tunnel vsrp source-ip 2.2.2.2]{lang="SV"}

[]{#struct_0_16980_17120_2021794502}[]{#_Toc365465925}[]{#_Toc365465926}[]{#_Toc365465927}[]{#_Toc365465928}[]{#_Toc365465929}[]{#_Toc365465931}[]{#_Toc365465932}[]{#_Toc365465933}[【相关命令】]{style="font-family:
黑体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;
font-family:Wingdings"}**[source-ip]{lang="EN-US"}**]{#struct_0_16980_17120_x1196927788}[（二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入命令参考]{lang="EN-US" style="font-family:宋体"}[/L2TP]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#134190839 .myid}
[]{#_Toc404796122}[]{#struct_0_16980_17120_x178111405}[]{#_Toc379813165}

**多机备份配置命令 \-- L2TP支持多机备份功能配置命令 \-- vsrp-instance（L2TP组视图）**

------------------------------------------------------------------------

[**[vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_1898417505}[命令用来设置]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组关联的多机备份实例。]{style="font-family:宋体"}

[**[undo vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_928697540}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x106701462}

[**[vsrp]{lang="EN-US"}[-instance ]{lang="EN-US"}***[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x753441250}

[**[undo vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_1782742514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_2041351641}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_1603015877}[组没有关联任何多机备份实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x694064393}

[[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_x875169883}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1396238465}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x133975015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_547658738}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x405509273}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x339080519}[：]{style="font-family:宋体"}[多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x810950226}

[[为了实现]{style="font-family:宋体"}[L2TP]{lang="EN-US"}]{#struct_0_16980_17120_1602819269}[业务多机备份功能，需要将]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组与多机备份实例进行关联。关联生效之后，主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备将向备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备实时备份此]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的业务信息。某些情况下（如设备重启），备用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备也会向主用]{style="font-family:宋体"}[LAC]{lang="EN-US"}[设备请求]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组的业务信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1534837670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[一对主用和备用]{style="font-family:宋体"}]{#struct_0_16980_17120_1718080367}[LAC]{lang="EN-US"}[设备上的对应]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组必须关联相同的多机备份实例。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[配置]{style="font-family:宋体"}]{#struct_0_16980_17120_x799472342}[L2TP]{lang="EN-US"}[组关联的多机备份实例时，该]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组下所有已建立的]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道将会被清除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_16980_17120_1723940082}[L2TP]{lang="EN-US"}[组下存在]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[隧道时，不能修改或取消该]{style="font-family:宋体"}[L2TP]{lang="EN-US"}[组关联的多机备份实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x422497600}

[[\# ]{lang="SV"}]{#struct_0_16980_17120_318934205}[配置]{style="font-family:宋体"}[L2TP]{lang="SV"}[组]{style="font-family:宋体"}[1]{lang="SV"}[与多机备份实例]{style="font-family:
宋体"}[abc]{lang="SV"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_16980_17120_x1485142698}

[\[Sysname\] l2tp-group 1 mode lac]{lang="SV"}

[\[Sysname-l2tp1\] vsrp-instance []{#_Toc364952656}abc]{lang="EN-US"}
:::

::: {#1018063022 .myid}
[]{#struct_0_16980_17120_x2080705826}[]{#_Toc365963511}[]{#_Toc404796124}[]{#_Toc380606431}[]{#_Toc371518635}

**多机备份配置命令 \-- Portal支持多机备份功能配置命令 \-- portal vsrp-instance**

------------------------------------------------------------------------

[**[portal vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_1602884805}[命令用来配置接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[功能绑定的多机备份实例。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **portal vsrp-instance**]{lang="EN-US"}]{#struct_0_16980_17120_66450765}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x972916846}

[**[portal]{lang="EN-US"}**[ **vsrp-instance** *vsrp-instance-name*]{lang="EN-US"}]{#struct_0_16980_17120_x1868513662}

[**[undo]{lang="EN-US"}**[ **portal** **vsrp-instance** ]{lang="EN-US"}]{#struct_0_16980_17120_1182435933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x661602826}

[[接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_16980_17120_x1403319623}[功能未绑定多机备份实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x919702076}

[[接口视图]{style="font-family:宋体"}]{#struct_0_16980_17120_2066934153}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_x226224023}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1806315080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1519217420}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_111573503}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_1464033944}[：表示]{style="font-family:宋体"}[多机备份实例名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1602688197}

[[接口上引用多机备份实例后，接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_16980_17120_1965213832}[多机备份功能对于该接口上的]{style="font-family:宋体"}[IPv4 Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6 Portal]{lang="EN-US"}[用户都生效。]{style="font-family:宋体"}[Portal]{lang="EN-US"}[多机备份功能是指当主设备故障或链路故障时，主设备通过指定的多机备份实例将其上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[业务信息备份到备设备上，从而保证主设备故障时，主设备上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[业务可以自动切换到备用设备上，已上线的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户不需要重新认证，计费、授权信息不丢失。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_16980_17120_x1717653028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[同一设备上的不同主接口上引用的多机备份实例不能相同。]{style="font-family:宋体"}]{#struct_0_16980_17120_x445813428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[同一接口下的不同子接口可以引用相同的]{style="font-family:宋体"}]{#struct_0_16980_17120_x2042782407}[VSRP]{lang="EN-US"}[实例，也可以引用不同的多机备份实例。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[当接口上有在线]{style="font-family:宋体"}]{#struct_0_16980_17120_x284917772}[Portal]{lang="EN-US"}[用户时，配置、修改、取消接口上引用的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例，都会导致接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户下线。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[多机备份运行环境下，如果备用设备的接口上取消引用多机备份实例，则该接口上的]{style="font-family:宋体"}]{#struct_0_16980_17120_422159131}[Portal]{lang="EN-US"}[用户信息会被删除；如果主设备的接口上取消引用多机备份实例，则该接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户不会下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x456740846}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x808848728}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[多机备份功能，并引用]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1402759488}

[\[Sysname\] interface ]{lang="EN-US"}[gigabit]{lang="EN-US"}[ethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="EN-US"}[Ethernet1/0/1\] portal vsrp-instance ]{lang="EN-US"}[aaa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1572901120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display portal interface]{lang="EN-US"}**]{#struct_0_16980_17120_1928607890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[portal vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1602753733}
:::

::: {#-108891013 .myid}
[]{#_Toc404796125}[]{#struct_0_16980_17120_x1471893782}[]{#_Toc380606432}[]{#_Toc371518636}[]{#_Toc365963512}

**多机备份配置命令 \-- Portal支持多机备份功能配置命令 \-- portal vsrp-port**

------------------------------------------------------------------------

[**[portal vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_1113727503}[命令用来配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[建立数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo portal vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_x1535018657}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x877254071}

[**[portal vsrp-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_22729794}

[**[undo portal vsrp-port]{lang="EN-US"}**]{#struct_0_16980_17120_217647981}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_175968152}

[[Portal]{lang="EN-US"}]{#struct_0_16980_17120_218214449}[建立数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[60038]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_x679068413}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_560618691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1781332987}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1408601686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_1602557125}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1236435225}

[*[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_761712018}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_x419828857}

[[多机备份组网环境中，本端设备在进行]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_16980_17120_244545524}[数据备份之前，需要与对端备份设备建立一条多机备份数据备份通道，此通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。两端成功建立了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接后，]{style="font-family:宋体"}[Portal]{lang="EN-US"}[业务的数据信息将通过该通道进行实时备份。]{style="font-family:宋体"}

[[需要注意的是，本命令中指定的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_16980_17120_717281796}[端口号不能与系统中已经使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号冲突。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1533043602}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x142505547}[配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[建立数据备份通道使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_925348706}

[\[Sysname\] portal vsrp-port 20000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x839839242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[portal vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_1168642896}
:::

::: {#-96613770 .myid}
[]{#_Toc404796127}[]{#struct_0_16980_17120_524945136}[]{#_Toc377552895}

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- dhcp vsrp-instance**

------------------------------------------------------------------------

[**[dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_1602622661}[命令用来配置接口绑定指定多机备份实例。]{style="font-family:宋体"}

[**[undo dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_2048211563}[命令用来取消接口绑定多机备份实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_297380776}

[**[dhcp vsrp-instance ]{lang="EN-US"}***[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_55340683}

[**[undo dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x1387746894}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_1302709175}

[[接口下未绑定多机备份实例。]{style="font-family:宋体"}*[ ]{style="color:blue"}*]{#struct_0_16980_17120_498941187}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_149149585}

[[三层以太网接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_1860351477}[三层以太网子接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1065404553}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_678569391}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_400417834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x2006273190}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x2044928635}[：多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1603474629}

[[配置本命令时，多机备份实例名称可以不存在，但只有配置了多机备份实例后，本命令才生效。]{style="font-family:宋体"}]{#struct_0_16980_17120_x1498417709}

[[该配置用于匹配主用设备和备用设备用户所在接口。一个接口只能绑定一个多机备份实例，同一接口下的多个子接口可以绑定同一个多机备份实例。不同接口不能绑定同一个多机备份实例。如果要绑定的实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。]{style="font-family:宋体"}]{#struct_0_16980_17120_x1550468354}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_1155085828}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1001988596}[配置接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[绑定多机备份实例]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_x1625164625}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] dhcp vsrp-instance vsrp1]{lang="EN-US"}
:::

::: {#2047367763 .myid}
[]{#_Toc404796128}[]{#struct_0_16980_17120_1239290475}[]{#_Toc377552888}

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- dhcp vsrp port**

------------------------------------------------------------------------

[**[dhcp vsrp port]{lang="EN-US"}**]{#struct_0_16980_17120_1735202142}[命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器数据备份通道的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo dhcp vsrp port]{lang="EN-US"}**]{#struct_0_16980_17120_x17957226}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x872289384}[命令]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[**[dhcp vsrp port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_16980_17120_328198242}

[**[undo dhcp vsrp port]{lang="EN-US"}**]{#struct_0_16980_17120_702121109}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x1610838342}[缺省情况]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;
color:#0096d6"}

[[默认端口号为]{style="font-family:宋体"}[60037]{lang="EN-US"}]{#struct_0_16980_17120_1603540165}[。]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_2043290436}[视图]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[系统视图]{style="font-family:宋体"}]{#struct_0_16980_17120_686896914}

[[【]{style="font-size:10.0pt;font-family:
黑体;color:#0096d6"}]{#struct_0_16980_17120_910952117}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_1821619717}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_822103312}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1369877304}[参数]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[*[port-number]{lang="EN-US" style="color:black"}*]{#struct_0_16980_17120_404718337}[：]{style="font-family:宋体;
color:black"}[DHCP]{lang="EN-US" style="color:black"}[服务器]{style="font-family:宋体;color:black"}[数据备份通道]{style="font-family:宋体;
color:black"}[TCP]{lang="EN-US" style="color:black"}[的端口号，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[65535]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x698107436}[使用指导]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;
color:#0096d6"}

[[DHCP]{lang="EN-US"}]{#struct_0_16980_17120_1955043901}[服务器在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。用户可以通过命令指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的端口号，如果不指定则用默认端口号发起连接。]{style="font-family:宋体"}

[[使用本命令指定的端口号不能与系统中已经使用的端口号冲突。]{style="font-family:宋体"}]{#struct_0_16980_17120_x1672100032}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x2128074780}[举例]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x1037314454}[指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的数据备份通道端口号为]{style="font-family:宋体"}[30000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_1602950340}

[\[Sysname\] dhcp vsrp port 30000]{lang="EN-US"}
:::

::: {#-327991275 .myid}
[]{#_Toc404796129}[]{#struct_0_16980_17120_2021728966}[]{#_Toc377552898}

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- ipv6 dhcp vsrp-instance**

------------------------------------------------------------------------

[**[ipv6 dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_735497246}[命令用来配置接口绑定指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[多机备份实例。]{style="font-family:宋体"}

[**[undo ipv6 dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x22207684}[命令用来取消接口绑定]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[多机备份实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_894768954}

[**[ipv6 dhcp vsrp-instance ]{lang="EN-US"}***[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_765163156}

[**[undo ipv6 dhcp vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x984246841}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_x1838011014}

[[接口下未绑定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16980_17120_1745300622}[多机备份实例。]{style="font-family:宋体"}*[ ]{style="color:blue"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_718619638}

[[三层以太网接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_16980_17120_x2126428405}[三层以太网子接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1762015661}

[[network-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1391879464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16980_17120_x1928662592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_1603015876}

[*[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x694129929}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[多机备份实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不包含空格，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1149045808}

[[配置本命令时，]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16980_17120_x1504909819}[多机备份实例名称可以不存在。]{style="font-family:宋体"}

[[该配置用于匹配主备设备中用户所在接口。一个接口只能绑定一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_16980_17120_1532662885}[多机备份实例，同一接口下的多个子接口可以绑定同一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[多机备份实例。不同接口不能绑定同一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[多机备份实例。如果要绑定的实例已经与其它的接口绑定，则需要先与其它接口解绑定后，才能配置成功。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_x105054698}

[[\# ]{lang="EN-US"}]{#struct_0_16980_17120_x272514335}[配置接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[接口绑定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[多机备份实例]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_786486475}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 dhcp vsrp-instance vsrp1]{lang="EN-US"}
:::

::: {#643989992 .myid}
[]{#_Toc404796130}[]{#struct_0_16980_17120_380374461}[]{#_Toc377552899}

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- ipv6 dhcp vsrp port**

------------------------------------------------------------------------

[**[ipv6 dhcp vsrp port]{lang="EN-US" style="color:black"}**]{#struct_0_16980_17120_x590746120}[命令用来配置]{style="font-family:宋体;color:black"}[DHCPv6]{lang="EN-US" style="color:black"}[服务器]{style="font-family:宋体;
color:black"}[数据备份通道的]{style="font-family:宋体;color:black"}[TCP]{lang="EN-US" style="color:black"}[端口号。]{style="font-family:宋体;
color:black"}

[**[undo ipv6 dhcp vsrp port]{lang="EN-US" style="color:black"}**]{#struct_0_16980_17120_2032603003}[命令用来恢复缺省情况。]{style="font-family:宋体;color:black"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_16980_17120_x822313609}

[**[ipv6 dhcp vsrp port ]{lang="EN-US" style="color:black"}**]{#struct_0_16980_17120_1602819268}*[port-number]{lang="EN-US" style="color:black"}*

[**[undo ipv6 dhcp vsrp port]{lang="EN-US" style="color:black"}**]{#struct_0_16980_17120_x1534903206}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_16980_17120_136555986}

[[默认端口号为]{style="font-family:宋体;
color:black"}]{#struct_0_16980_17120_421274342}[60039]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16980_17120_510366388}

[[系统视图]{style="font-family:宋体;
color:black"}]{#struct_0_16980_17120_325820169}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16980_17120_1868474297}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_x1852103237}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_414009899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16980_17120_x176958540}

[*[port-number]{lang="EN-US" style="color:black"}*]{#struct_0_16980_17120_x1057792504}[：]{style="font-family:宋体;
color:black"}[DHCPv6]{lang="EN-US" style="color:black"}[服务器]{style="font-family:宋体;color:black"}[数据备份通道]{style="font-family:宋体;
color:black"}[TCP]{lang="EN-US" style="color:black"}[的端口号，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[65535]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_16980_17120_1919266677}

[[DHCPv6]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_x288756066}[服务器]{style="font-family:宋体;color:black"}[在进行数据备份之前，需要与对端备份设备建立一条数据备份通道，此通道为]{style="font-family:宋体;color:black"}[TCP]{lang="EN-US" style="color:black"}[连接。用户可以通过命令指定]{style="font-family:宋体;
color:black"}[TCP]{lang="EN-US" style="color:black"}[连接的端口号，如果不指定则用默认端口号发起连接。]{style="font-family:宋体;color:black"}

[[使用本命令指定的端口号不能与系统中已经使用的端口号冲突。]{style="font-family:宋体;
color:black"}]{#struct_0_16980_17120_1602884804}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16980_17120_66516301}

[[\# ]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_x1776020375}[指定]{style="font-family:宋体;color:black"}[DHCPv6]{lang="EN-US" style="color:black"}[服务器]{style="font-family:宋体;
color:black"}[的数据备份通道端口号为]{style="font-family:宋体;color:black"}[30000]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_16980_17120_49811737}

[\[Sysname\] ipv6 dhcp vsrp port 30000]{lang="EN-US"}
:::

::: {#-1670226942 .myid}
[]{#_Toc404796131}[]{#struct_0_16980_17120_1244066422}[]{#_Toc377552914}

**多机备份配置命令 \-- DHCP支持多机备份功能配置命令 \-- vsrp-instance(DHCPv4/DHCPv6地址池视图)**

------------------------------------------------------------------------

[**[vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_849512502}[命令用来配置]{style="font-family:宋体"}[DHCPv4/DHCPv6]{lang="EN-US"}[服务器地址池绑定指定多机备份实例。]{style="font-family:宋体"}

[**[undo vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_x358887384}[命令用来取消]{style="font-family:宋体"}[DHCPv4/DHCPv6]{lang="EN-US"}[服务器地址池绑定的多机备份实例。]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1259717336}[命令]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[**[vsrp-instance ]{lang="EN-US"}***[vsrp-instance-name]{lang="EN-US"}*]{#struct_0_16980_17120_x1643973514}

[**[undo vsrp-instance]{lang="EN-US"}**]{#struct_0_16980_17120_804808706}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_x488630694}[缺省情况]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;
color:#0096d6"}

[[DHCPv4/DHCPv6]{lang="EN-US"}]{#struct_0_16980_17120_1971078451}[服务器地址池未绑定多机备份实例。]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1602688196}[视图]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[DHCPv4/DHCPv6]{lang="EN-US"}]{#struct_0_16980_17120_1965279368}[地址池视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:
黑体;color:#0096d6"}]{#struct_0_16980_17120_628433875}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_474723445}

[[mdc-admin]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_1034312867}

[[【]{style="font-size:10.0pt;font-family:
黑体;color:#0096d6"}]{#struct_0_16980_17120_643104370}[参数]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[*[vsrp-instance-name]{lang="EN-US" style="color:black"}*]{#struct_0_16980_17120_988113969}[：]{style="font-family:
宋体;color:black"}[多机备份]{style="font-family:宋体;color:black"}[实例名称，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[31]{lang="EN-US" style="color:black"}[个字符的字符串，区分大小写。]{style="font-family:宋体;color:black"}

[[【]{style="font-size:10.0pt;font-family:
黑体;color:#0096d6"}]{#struct_0_16980_17120_984573223}[使用指导]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[在地址池下配置本命令后，就可以通过]{style="font-family:宋体;
color:black"}]{#struct_0_16980_17120_x74549174}[多机备份]{style="font-family:宋体;
color:black"}[模块提供的数据备份通道实时备份]{style="font-family:宋体;color:black"}[DHCP]{lang="EN-US" style="color:black"}[服务器地址池的表项信息。配置本命令时]{style="font-family:宋体;
color:black"}[多机备份]{style="font-family:宋体;color:black"}[实例可以不存在，但只有配置了]{style="font-family:宋体;color:black"}[多机备份]{style="font-family:
宋体;color:black"}[实例后本命令才生效。]{style="font-family:宋体;color:black"}

[[【]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}]{#struct_0_16980_17120_1120699884}[举例]{style="font-family:黑体;
color:#0096d6"}[】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}

[[\# ]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_494816537}[配置]{style="font-family:宋体;color:black"}[DHCPv4]{lang="EN-US" style="color:black"}[服务器地址池绑定多机备份实例]{style="font-family:宋体;
color:black"}[vsrp1]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_x1359556450}

[[\[Sysname\] dhcp server ip-pool p1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_740239801}

[[\[Sysname-dhcp-pool-p1\] vsrp-instance vsrp1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_1602753732}

[[\#]{lang="EN-US" style="color:black"}]{#struct_0_16980_17120_x1471959318}[配置]{style="font-family:宋体;color:black"}[DHCPv6]{lang="EN-US" style="color:black"}[服务器地址池绑定多机备份实例]{style="font-family:宋体;
color:black"}[vsrp1]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_110814141}

[[\[Sysname\] ipv6 dhcp pool p1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_x1696360345}

[[\[Sysname-dhcp6-pool-p1\] vsrp-instance vsrp1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_16980_17120_x433909049}

[ ]{lang="EN-US"}
:::
