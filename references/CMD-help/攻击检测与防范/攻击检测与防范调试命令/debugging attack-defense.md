::: {#-1574112770 .myid}
[]{#_Toc404793639}[]{#struct_0_x6596_18983_x972759706}[]{#_Toc130718952}[]{#_Toc87257691}

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging attack-defense**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x668473041}

[**[debugging attack-defense ]{lang="EN-US"}**]{#struct_0_x6596_18983_x811499752}[{ **all** \| **error** \| **event** }]{lang="EN-US"}

[**[undo debugging attack-defense ]{lang="EN-US"}**]{#struct_0_x6596_18983_1263076061}[{ **all** \| **error** \| **event** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1296232588}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6596_18983_x196917401}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1196516571}

[[network-admin]{lang="EN-US"}]{#struct_0_x6596_18983_x680504931}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6596_18983_420419383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x272638191}

[**[all]{lang="EN-US"}**]{#struct_0_x6596_18983_2021350896}[：表示攻击检测与防范所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6596_18983_x1583405373}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6596_18983_x792440927}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x551344602}

[**[debugging attack-defense]{lang="EN-US"}**]{#struct_0_x6596_18983_2078154715}[命令用来打开攻击检测与防范调试信息开关。]{style="font-family:
宋体"}**[undo debugging attack-defense]{lang="EN-US"}**[命令用来关闭攻击检测与防范调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，攻击检测与防范调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6596_18983_524876432}

[]{#struct_0_x6596_18983_x228171505}[[表1-1 ]{lang="EN-US"}[debugging attack-defense error]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_187974887}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_432764272}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1910306597}

[[Failed to ]{lang="EN-US"}[add a dynamic blacklist entry for IP *ip-address*.]{lang="EN-US"}]{#struct_0_x6596_18983_1972887014}

[[添加动态黑名单失败，]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x6596_18983_1242069765}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Failed to]{lang="EN-US"}[ add a dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.]{lang="EN-US"}]{#struct_0_x6596_18983_x243245745}

[[添加动态]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6596_18983_x1763069225}[客户端验证保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项失败，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[、端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Failed to]{lang="EN-US"}[ add a dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.]{lang="EN-US"}]{#struct_0_x6596_18983_655658847}

[[添加动态]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x6596_18983_130646336}[客户端验证保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项失败，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[、端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Failed to]{lang="EN-US"}[ add a dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.]{lang="EN-US"}]{#struct_0_x6596_18983_x101339447}

[[添加动态]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_x1947727240}[客户端验证保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项失败，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[、端口号为]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[ ]{lang="EN-US"}

[]{#struct_0_x6596_18983_x1566829051}[[表1-2 ]{lang="EN-US"}[debugging attack-defense event]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_187566721}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_189510886}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1049644104}

[[Detected an attack occurred.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1333694801}

[[Attack type: *type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1593852525}

[[Detected on: *interface-type interface-number / local*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1134980720}

[[Action: *action*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x789310478}

[[IP address: *ip-address*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1509276511}

[[Protocol: *protocol*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1878500520}

[[设备检测到一个攻击发生]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_x1435437605}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attack type]{lang="EN-US"}]{#struct_0_x6596_18983_2122654126}[：]{lang="EN-US" style="font-family:宋体"}[攻击类型，包括]{lang="EN-US" style="font-family:宋体"}[scan]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[syn-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[syn-ack-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ack-flood ]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[rst-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[fin-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[icmp-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[icmpv6-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[udp-flood]{lang="EN-US"}[等]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detected on]{lang="EN-US"}]{#struct_0_x6596_18983_x771861197}[：进行]{lang="EN-US" style="font-family:宋体"}[攻击防范的位置，包括接口或本机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Action]{lang="EN-US"}]{#struct_0_x6596_18983_x734622096}[：]{style="font-family:宋体"}[攻击防范的处理行为，]{style="font-family:宋体"}[包括以]{style="font-family:宋体"}[下动作的组合：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[none]{lang="EN-US"}]{#struct_0_x6596_18983_1532349459}[：不作任何处理]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[drop]{lang="EN-US"}]{#struct_0_x6596_18983_1414546813}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[logging]{lang="EN-US"}]{#struct_0_x6596_18983_650505657}[：发送日志]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[block-source]{lang="EN-US"}]{#struct_0_x6596_18983_x128979045}[：将攻击源的主机]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址加入黑名单，]{lang="EN-US" style="font-family:宋体"}[并阻断和丢弃来自该地址的后续报文]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[client-verify]{lang="EN-US"}]{#struct_0_x6596_18983_x857007316}[：将攻击目标的主机]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址加入到客户端验证的受保护]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IP addre]{lang="EN-US"}[ss]{lang="EN-US"}]{#struct_0_x6596_18983_1928446311}[：]{lang="EN-US" style="font-family:宋体"}[Scan]{lang="EN-US"}[攻击的攻击源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{lang="EN-US" style="font-family:宋体"}[Flood]{lang="EN-US"}[攻击的攻击目标]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protocol]{lang="EN-US"}]{#struct_0_x6596_18983_312416579}[：]{style="font-family:宋体"}[Scan]{lang="EN-US"}[攻击使用的协议（]{style="font-family:宋体"}[Scan]{lang="EN-US"}[攻击才显示此字段）]{style="font-family:宋体"}

[[Detected an attack ended.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1032153078}

[[Attack type: *type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x2143270976}

[[Detected on: *interface-type interface-number / local*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x514582033}

[[Action: *action*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x387651256}

[[IP address: *ip-address*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1297594826}

[[设备检测到一个攻击结束]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_x6596_18983_3156596}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attack type]{lang="EN-US"}]{#struct_0_x6596_18983_808212853}[：]{lang="EN-US" style="font-family:宋体"}[攻击类型，包括]{lang="EN-US" style="font-family:宋体"}[syn-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[syn-ack-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ack-flood ]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[rst-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[fin-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[icmp-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[icmpv6-flood]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[udp-flood]{lang="EN-US"}[等]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detected on]{lang="EN-US"}]{#struct_0_x6596_18983_x808129469}[：]{lang="EN-US" style="font-family:宋体"}[进行]{lang="EN-US" style="font-family:宋体"}[攻击防范的位置，包括接口或本机]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Action]{lang="EN-US"}]{#struct_0_x6596_18983_1696730277}[：]{style="font-family:宋体"}[攻击防范的处理行为，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[none]{lang="EN-US"}]{#struct_0_x6596_18983_x222013372}[：不作任何处理]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP addre]{lang="EN-US"}[ss]{lang="EN-US"}]{#struct_0_x6596_18983_1612799554}[：]{lang="EN-US" style="font-family:宋体"}[Scan]{lang="EN-US"}[攻击的攻击源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{lang="EN-US" style="font-family:宋体"}[Flood]{lang="EN-US"}[攻击的攻击目标]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Added a dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x218090245}

[[添加一个动态]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_1615843765}[TCP]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed an expired dynamic protected IP entry (*ip-address*: *port*) for TCP client verification.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x6596_18983_870360657}

[[动态的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_x545970561}[TCP]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项被删除，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Added a dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_2100014804}

[[添加一个动态]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_x6596_18983_34925013}[DNS]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed an expired dynamic protected IP entry (*ip-address*: *port*) for DNS client verification.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1133456360}

[[动态的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_x2096110207}[DNS]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项被删除，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Added a dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x6596_18983_737904263}

[[添加一个动态]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_533930863}[HTTP]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed an expired dynamic protected IP entry (*ip-address*: *port*) for HTTP client verification.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x2015123179}

[[动态的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_1857404604}[HTTP]{lang="EN-US" style="font-size:9.0pt"}[客户端验证保护]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[表项被删除，]{style="font-size:9.0pt;font-family:
  宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[、端口号为]{style="font-size:9.0pt;
  font-family:宋体"}*[port]{lang="EN-US" style="font-size:9.0pt"}*

[[Added a dynamic blacklist entry IP ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1195683295}[(*ip-address*), ]{lang="EN-US" style="font-size:9.0pt"}[aging time *aging-time*(s).]{lang="EN-US" style="font-size:9.0pt"}

[[添加一个动态黑名单表项，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_x6596_18983_x2059892460}[IP]{lang="EN-US" style="font-size:
  9.0pt"}[地址]{style="font-size:9.0pt;font-family:宋体"}*[ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，老化时间为]{style="font-size:9.0pt;font-family:宋体"}*[aging-time]{lang="EN-US" style="font-size:9.0pt"}*[秒]{style="font-size:9.0pt;
  font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1649676110}

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x874018830}[创建一个攻击防范策略，在策略中使能]{style="font-family:宋体"}[对本机]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[进行]{style="font-family:宋体"}[SYN flood]{lang="EN-US"}[攻击防范检测]{style="font-family:宋体"}[，触发阈值为]{style="font-family:宋体"}[10]{lang="EN-US"}[，防范动作为输出日志和加入]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项。在本机应用该策略]{style="font-family:宋体"}[。打开攻击防范报文调试信息开关后，当设备检测到发送速率超过阈值且目的地址为本机地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging attack-defense event]{lang="EN-US"}]{#struct_0_x6596_18983_x936682300}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/EVENT: -MDC=1; Detected an attack occurred.]{lang="EN-US"}

[Attack type: syn-flood]{lang="EN-US"}

[Detected on: local]{lang="EN-US"}

[Action: logging, client-verify]{lang="EN-US"}

[IP address: 1.1.1.1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1171311627}*[检测到一个攻击发生：]{style="font-family:宋体"}*

[*[攻击类型为]{style="font-family:宋体"}*]{#struct_0_x6596_18983_1663484049}*[syn-flood]{lang="EN-US"}*

[*[进行]{style="font-family:宋体"}*]{#struct_0_x6596_18983_1532569007}*[攻击防范的位置为本机]{style="font-family:宋体"}*

[*[攻击防范的处理行为]{style="font-family:宋体"}*]{#struct_0_x6596_18983_x2111028044}*[包括：]{style="font-family:
宋体"}[发送日志、将攻击目标的主机]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址加入到客户端验证的受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[列表中]{style="font-family:宋体"}*

[*[Flood]{lang="EN-US"}*]{#struct_0_x6596_18983_x1102330807}*[攻击的攻击目标]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ EVENT: -MDC=1; Added a dynamic protected IP entry (]{lang="EN-US"}]{#struct_0_x6596_18983_83592169}[1.1.1.1]{lang="EN-US"}[: 2003) of TCP client verify.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1963350653}*[添加一个动态]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[2003]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_322917356}[创建一个攻击防范策略，在策略中使能]{style="font-family:宋体"}[对本机]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[进行扫描攻击防范检测]{style="font-family:宋体"}[，攻击方防范的级别为]{style="font-family:宋体"}**[low]{lang="EN-US"}**[，防范动作为输出日志和]{style="font-family:宋体"}[阻断并丢弃来自该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的后续报文]{style="font-family:宋体"}[。在本机应用该策略]{style="font-family:宋体"}[。打开攻击防范错误调试信息开关后，当设备检测到源地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的报文端口变化数超过]{style="font-family:宋体"}**[low]{lang="EN-US"}**[级别的阈值]{style="font-family:宋体"}[，且此时设备资源不足时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging attack-defense error]{lang="EN-US"}]{#struct_0_x6596_18983_1997965590}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ERROR: -MDC=1; ]{lang="EN-US"}[Failed to ]{lang="EN-US"}[add a dynamic blacklist entry for IP 2.2.2.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1674818912}*[添加一个动态黑名单表项失败]{style="font-family:宋体"}*

::: {#1645832386 .myid}
[]{#_Toc404793640}[]{#struct_0_x6596_18983_469798695}

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify tcp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6596_18983_509946771}

[**[debugging client-verify tcp ]{lang="EN-US"}**]{#struct_0_x6596_18983_1194966215}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[**[undo debugging client-verify tcp ]{lang="EN-US"}**]{#struct_0_x6596_18983_120012989}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6596_18983_868760887}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6596_18983_42920953}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1196008990}

[[network-admin]{lang="EN-US"}]{#struct_0_x6596_18983_1293380214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6596_18983_x472557359}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x914470548}

[**[all]{lang="EN-US"}**]{#struct_0_x6596_18983_387371681}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证功能的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6596_18983_x871831477}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6596_18983_1994624613}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6596_18983_x1743508778}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1286984162}

[**[debugging client-verify tcp]{lang="EN-US"}**]{#struct_0_x6596_18983_409666604}[命令用来打开]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}**[undo debugging client-verify tcp]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6596_18983_967781794}[客户端验证功能的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging client-verify tcp error]{lang="EN-US"}]{#struct_0_x6596_18983_1019910817}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_217547407}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_176227327}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1801866783}

[[Failed to send a reply packet to client.]{lang="EN-US"}[ Reason: No route is found.]{lang="EN-US"}]{#struct_0_x6596_18983_x272703727}

[[向客户端回复报文失败，原因：找不到匹配的路由]{style="font-family:宋体"}]{#struct_0_x6596_18983_427128639}

[[Cookie is equal to correct ACK. Changed the cookie.]{lang="EN-US"}]{#struct_0_x6596_18983_2064440289}

[[Cookie]{lang="EN-US"}]{#struct_0_x6596_18983_x1247393849}[和正确的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[序号相同，修改]{style="font-family:宋体"}[Cookie]{lang="EN-US"}

[[Failed to copy data from mbuf.]{lang="EN-US"}]{#struct_0_x6596_18983_x1537433062}

[[拷贝]{style="font-family:宋体"}]{#struct_0_x6596_18983_1098902102}[mbuf]{lang="EN-US"}[中的报文失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging client-verify tcp event]{lang="EN-US"}]{#struct_0_x6596_18983_1594912336}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_216699327}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_x154898864}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x676882461}

[[Added a trusted node:]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x6596_18983_130580800}[ Type TCP, Source IP *src-ip-address*, VPN instance *vpn-instance-*]{lang="EN-US" style="font-size:9.0pt"}*[name.]{lang="EN-US" style="font-size:9.0pt"}*

[[[添加一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_774686650}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址：]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[类型为]{style="font-size:9.0pt;font-family:宋体"}[TCP]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed expired trusted node: Type = TCP, ]{lang="EN-US"}]{#struct_0_x6596_18983_x1345949771}

[[Source IP = *src-ip-address*, ]{lang="EN-US"}]{#struct_0_x6596_18983_x620623241}

[[VPN instance = *vpn-instance-name.*]{lang="EN-US"}]{#struct_0_x6596_18983_x2037358738}

[[[删除一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_x1398257532}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[：类型为]{style="font-size:9.0pt;font-family:宋体"}[TCP]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[New cookie created, cookie ID is]{lang="EN-US"}]{#struct_0_x6596_18983_x1435503141}*[ cookie-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[value is *cookie-value*]{lang="EN-US"}

[[[产生新]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_467158854}[cookie]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-id]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-size:9.0pt;
  font-family:宋体"}[cookie]{lang="EN-US" style="font-size:9.0pt"}[值是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-value]{lang="EN-US" style="font-size:9.0pt"}*

[[Cookie timed out.]{lang="EN-US"}]{#struct_0_x6596_18983_1082293074}

[[Cookie]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x471923942}[超时]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging client-verify tcp packet]{lang="EN-US"}]{#struct_0_x6596_18983_x715560778}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_211753621}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_486370646}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_116062930}

[[The SYN packet sourced from *src-ip-address* is untrusted, and it will be verified by TCP client-verify.]{lang="EN-US"}]{#struct_0_x6596_18983_x1567022259}

[[源地址为]{style="font-family:宋体"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x1354428431}[的报文不可信，需要对其进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}

[[The SYN ACK packet sourced from server is trusted.]{lang="EN-US"}]{#struct_0_x6596_18983_x1032218614}

[[来自服务器的]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}]{#struct_0_x6596_18983_1426848314}[报文可信]{style="font-family:宋体"}

[[The RST packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_x1518741585}

[[该]{style="font-family:宋体"}[RST]{lang="EN-US"}]{#struct_0_x6596_18983_x559397028}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[The ACK packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_x60374520}

[[该]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_460798091}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[Dropped SYN, and replied with SYN ACK.]{lang="EN-US"}]{#struct_0_x6596_18983_x216068706}

[[丢弃]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x6596_18983_1696664741}[报文，回复代理]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Replied with ACK to server.]{lang="EN-US"}]{#struct_0_x6596_18983_922102482}

[[向服务器回复]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_254705406}[报文]{style="font-family:宋体"}

[[Sent ACK to client.]{lang="EN-US"}]{#struct_0_x6596_18983_1954702562}

[[向客户端回复]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_x1339475072}[报文]{style="font-family:宋体"}

[[ACK cookie valid. Sent SYN to server.]{lang="EN-US"}]{#struct_0_x6596_18983_x946950578}

[[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_x1217785426}[报文的]{style="font-family:宋体"}[cookie]{lang="EN-US"}[有效，向服务器发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Adjusted the ACK sequence number, and then forwarded the ACK.]{lang="EN-US"}]{#struct_0_x6596_18983_x669437538}

[[调整报文响应序号，继续转发]{style="font-family:宋体"}]{#struct_0_x6596_18983_2099949268}

[[Adjusted the sequence number, and then forwarded the packet.]{lang="EN-US"}]{#struct_0_x6596_18983_x1507708566}

[[调整报文序号，继续转发]{style="font-family:宋体"}]{#struct_0_x6596_18983_469347824}

[[Protocol(*pro-type*) ,FLAG(*flags*)]{lang="EN-US"}]{#struct_0_x6596_18983_x1085235367}

[[SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*)]{lang="EN-US"}]{#struct_0_x6596_18983_x710719331}

[[Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)]{lang="EN-US"}]{#struct_0_x6596_18983_533865327}

[[WinSize(*WinSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_x419989127}

[[MSS(*MssSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_x2076900547}

[[设备向服务器或客户端发送的报文信息：]{style="font-family:宋体"}]{#struct_0_x6596_18983_x1815753620}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pro-type]{lang="EN-US"}*]{#struct_0_x6596_18983_1555860197}[：协议类型，包括]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Other]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[Other]{lang="EN-US"}[表示除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[以外的其它协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flags]{lang="EN-US"}*]{#struct_0_x6596_18983_x1307565039}[：报文标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_1649610574}[：源]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_x6596_18983_1836467086}[：源端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x2127710514}[：目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-port]{lang="EN-US"}*]{#struct_0_x6596_18983_673051559}[：目的端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqSeqNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_647344066}[：报文序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqAckNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_83526633}[：确认序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[WinSize]{lang="EN-US"}*]{#struct_0_x6596_18983_x1122060214}[：窗口大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MssSize]{lang="EN-US"}*]{#struct_0_x6596_18983_1990232300}[：]{lang="EN-US" style="font-family:宋体"}[MSS]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6596_18983_103313337}

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_1530562970}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证受保护]{style="font-family:宋体"}[IP 9.1.1.1]{lang="EN-US"}[，并在入接口上使能]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证单向代理功能。打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证报文调试信息开关后，当设备接收到客户端首次发送的目的主机存在且目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify tcp packet]{lang="EN-US"}]{#struct_0_x6596_18983_1966013866}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 9.1.1.1 is untrusted, and will be verified by TCP client-verify.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_2061349283}*[源地址为]{style="font-family:宋体"}[6.1.1.2]{lang="EN-US"}[的报文不可信，需要对其进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:]{lang="EN-US"}]{#struct_0_x6596_18983_2137724531}

[      Protocol(TCP), FLAG(SYNACK)]{lang="EN-US"}

[      SrcIP(9.1.1.1: 2200), DstIP(6.1.1.2: 1)]{lang="EN-US"}

[      Seq(0), AckSeq(369121992)]{lang="EN-US"}

[      WinSize(0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1293314678}*[丢弃]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，设备代替服务器端向客户端回复]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x1662768325}[在入接口上使能]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证单向代理功能。打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证事件调试信息开关后，当设备对来自客户端的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名为]{style="font-family:宋体"}[kkk]{lang="EN-US"}[且目的地址为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求验证通过时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify tcp event]{lang="EN-US"}]{#struct_0_x6596_18983_1860595636}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type TCP, Source IP 1.1.1.1, VPN instance kkk.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x1260938705}*[添加一个信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[，]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为[1.1.1.1]{lang="EN-US"}，所]{style="font-family:宋体"}[属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}[kkk]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_1137098111}[在入接口上使能]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证双向代理功能。打开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[客户端验证错误调试信息开关后，当设备接收到服务端首次发送的可信]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文，且设备资源不足时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify tcp error]{lang="EN-US"}]{#struct_0_x6596_18983_x152389134}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Failed to copy data from mbuf.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_200811112}*[拷贝]{style="font-family:宋体"}[mbuf]{lang="EN-US"}[中的报文失败]{style="font-family:宋体"}*

::: {#2048264961 .myid}
[]{#_Toc404793641}[]{#struct_0_x6596_18983_x272769263}

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify dns**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1624238381}

[**[debugging client-verify dns ]{lang="EN-US"}**]{#struct_0_x6596_18983_1594480881}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[**[undo debugging client-verify dns ]{lang="EN-US"}**]{#struct_0_x6596_18983_1800165424}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x66295088}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6596_18983_1220420016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x966053029}

[[network-admin]{lang="EN-US"}]{#struct_0_x6596_18983_x711819725}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6596_18983_99681119}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1917237651}

[**[all]{lang="EN-US"}**]{#struct_0_x6596_18983_130515264}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6596_18983_409156249}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6596_18983_x2141824370}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6596_18983_x9464140}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1268932645}

[**[debugging client-verify dns]{lang="EN-US"}**]{#struct_0_x6596_18983_x115852321}[命令用来打开]{style="font-family:
宋体"}[DNS]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}**[undo debugging client-verify dns]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[DNS]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x6596_18983_x1265899027}[客户端验证功能的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging client-verify dns error]{lang="EN-US"}]{#struct_0_x6596_18983_x99662849}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_212815245}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_522682774}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_590785749}

[[Failed to send a reply packet to client.]{lang="EN-US"}[ Reason: No route is found.]{lang="EN-US"}]{#struct_0_x6596_18983_151940934}

[[向客户端回复报文失败，原因：找不到匹配的路由]{style="font-family:宋体"}]{#struct_0_x6596_18983_x1883425575}

[[Cookie is equal to correct ACK. Changed cookie.]{lang="EN-US"}]{#struct_0_x6596_18983_1557752506}

[[cookie]{lang="EN-US"}]{#struct_0_x6596_18983_x1435568677}[序号正确，将其修改为计算得到的序号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging client-verify dns event]{lang="EN-US"}]{#struct_0_x6596_18983_x1148518245}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_207429609}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_x813924494}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_1096983927}

[[Added a trusted node:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_1016461747}[ Type DNS, Source IP *src-ip-address*, VPN instance *vpn-instance-*]{lang="EN-US" style="font-size:
  9.0pt"}*[name.]{lang="EN-US" style="font-size:9.0pt"}*

[[[添加一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_x1989505022}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址：]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[类型为]{style="font-size:9.0pt;font-family:宋体"}[DNS]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed expired trusted node: Type =DNS, ]{lang="EN-US"}]{#struct_0_x6596_18983_591084805}

[[Source IP = *src-ip-address*, ]{lang="EN-US"}]{#struct_0_x6596_18983_1394907020}

[[VPN instance = *vpn-instance-name.*]{lang="EN-US"}]{#struct_0_x6596_18983_1929694239}

[[[删除一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_x281190097}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[：类型为]{style="font-size:9.0pt;font-family:宋体"}[DNS]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[New cookie created, cookie ID is]{lang="EN-US"}]{#struct_0_x6596_18983_x1664072608}*[ cookie-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[value is *cookie-value*]{lang="EN-US"}

[[[产生新]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_1433186155}[cookie]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-id]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-size:9.0pt;
  font-family:宋体"}[cookie]{lang="EN-US" style="font-size:9.0pt"}[值是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-value]{lang="EN-US" style="font-size:9.0pt"}*

[[Cookie timed out.]{lang="EN-US"}]{#struct_0_x6596_18983_x1032284150}

[[Cookie]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1692475960}[超时]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging client-verify dns packet]{lang="EN-US"}]{#struct_0_x6596_18983_1935512903}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_209020525}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_x621675090}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x57760815}

[[The SYN packet sourced from *src-ip-address* is untrusted, and it will be verified by DNS client-verify.]{lang="EN-US"}]{#struct_0_x6596_18983_x1694409235}

[[源地址为]{style="font-family:宋体"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x510908280}[的报文不可信，需要对其进行]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}

[[The UDP DNS query packet sourced from *src-ip-address* is untrusted, dropped it and then replied with TC packet.]{lang="EN-US"}]{#struct_0_x6596_18983_237139937}

[[源地址为]{style="font-family:宋体"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x426045843}[的]{style="font-family:宋体"}[UDP DNS ]{lang="EN-US"}[查询请求报文不可信，丢弃该报文并向客户端回复]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The RST packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_x1427529057}

[[该]{style="font-family:宋体"}[RST]{lang="EN-US"}]{#struct_0_x6596_18983_1989114863}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[The ACK packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_1696599205}

[[该]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_967655062}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[Dropped SYN, and replied with SYN ACK.]{lang="EN-US"}]{#struct_0_x6596_18983_1441354381}

[[丢弃]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x6596_18983_x591826555}[报文，回复代理]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Protocol(*pro-type*) ,FLAG(*flags*)]{lang="EN-US"}]{#struct_0_x6596_18983_1665601499}

[[SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*)]{lang="EN-US"}]{#struct_0_x6596_18983_x1302018003}

[[Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)]{lang="EN-US"}]{#struct_0_x6596_18983_x856263114}

[[WinSize(*WinSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_x71527403}

[[MSS(*MssSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_x547576731}

[[设备向服务器或客户端发送的报文信息：]{style="font-family:宋体"}]{#struct_0_x6596_18983_1604408717}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pro-type]{lang="EN-US"}*]{#struct_0_x6596_18983_2099883732}[：协议类型，包括]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Other]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[Other]{lang="EN-US"}[表示除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[以外的其它协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flags]{lang="EN-US"}*]{#struct_0_x6596_18983_x1131942570}[：报文标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x270874988}[：源]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_x6596_18983_x1398155913}[：源端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x1594992777}[：目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-port]{lang="EN-US"}*]{#struct_0_x6596_18983_x1743595805}[：目的端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqSeqNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_1045893045}[：报文序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqAckNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_1756024375}[：确认序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[WinSize]{lang="EN-US"}*]{#struct_0_x6596_18983_750604971}[：窗口大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MssSize]{lang="EN-US"}*]{#struct_0_x6596_18983_533799791}[：]{lang="EN-US" style="font-family:宋体"}[MSS]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1282385216}

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x1036206435}[在入接口上使能]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证错误调试信息开关后，]{style="font-family:宋体"}[设备收到]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端发送的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的首个]{style="font-family:宋体"}[DNS]{lang="EN-US"}[查询请求报文（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文）]{style="font-family:宋体"}[，且查找路由失败时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify tcp error]{lang="EN-US"}]{#struct_0_x6596_18983_x1054517294}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/ERROR: -MDC=1;]{lang="EN-US"}[ Failed to send a reply packet to client.]{lang="EN-US"}[ Reason: No route is found.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x1651937409}*[向客户端回复报文失败，原因：找不到匹配的路由]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x588291065}[在入接口上使能]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证事件调试信息开关后，当设备对来自客户端的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名为]{style="font-family:宋体"}[KKK]{lang="EN-US"}[且目的地址为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[请求验证通过时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify dns event]{lang="EN-US"}]{#struct_0_x6596_18983_1326954716}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/EVENT: -MDC=1; Added a trusted node: Type DNS, Source IP 1.1.1.1, VPN instance kkk.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_785539150}*[添加了一个信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[，]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}[kkk]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_2023593615}[配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证受保护]{style="font-family:宋体"}[IP 6.1.1.2]{lang="EN-US"}[，并在入接口上使能]{style="font-family:宋体"}[DNS ]{lang="EN-US"}[客户端验证功能，打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证报文调试信息开关。]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[设备收到]{style="font-family:宋体"}]{#struct_0_x6596_18983_183534930}[DNS]{lang="EN-US"}[客户端发送的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的首个]{style="font-family:宋体"}[DNS]{lang="EN-US"}[查询请求报文（]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文）时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify dns packet]{lang="EN-US"}]{#struct_0_x6596_18983_x2043263621}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The UDP DNS query packet 2.2.2.2 is untrusted, drop it and then reply with TC packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1601517971}*[源地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP DNS ]{lang="EN-US"}[查询请求报文不可信，丢弃该报文并向客户端回复]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[[DNS]{lang="EN-US"}]{.ItemListCharChar}]{#struct_0_x6596_18983_x167935724}[客户端收到]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文后，按照]{style="font-family:宋体"}[TCP]{lang="EN-US"}[方式再次向服务器发起]{style="font-family:宋体"}[DNS]{lang="EN-US"}[请求。当设备收到]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端发送目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文时，输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 2.2.2.2 is untrusted, and will be verified by DNS client-verify.]{lang="EN-US"}]{#struct_0_x6596_18983_1649545038}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1058530658}*[源地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的报文不可信，需要对其进行]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:]{lang="EN-US"}]{#struct_0_x6596_18983_441394283}

[      Protocol(TCP), FLAG(SYNACK)]{lang="EN-US"}

[      SrcIP(6.1.1.2: 2200), DstIP(2.2.2.2)]{lang="EN-US"}

[      Seq(0),AckSeq(369121992)]{lang="EN-US"}

[      WinSize(0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x1161820764}*[丢弃客户端的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，设备代替服务器端向客户端回复]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_1108949215}[在入接口上使能]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验功能。打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证事件调试信息开关]{style="font-family:宋体"}[60]{lang="EN-US"}[秒后，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify dns event]{lang="EN-US"}]{#struct_0_x6596_18983_x954844105}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; New cookie created, cookie ID is]{lang="EN-US"}*[ ]{lang="EN-US"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}*[value is 517312006.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x6596_18983_1021386913}*[产生新]{style="font-family:宋体"}[cookie]{lang="EN-US"}[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[cookie]{lang="EN-US"}[值是]{style="font-family:宋体"}[517312006]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x797095218}[在入接口上使能]{style="font-family:宋体"}[DNS]{lang="EN-US"}[客户端验证功能。打开]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证错误调试信息开关后，当设备接收到客户端首次发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}*[SeqNumber]{lang="EN-US"}*[为]{style="font-family:宋体"}[517312000]{lang="EN-US"}[，且设备此时创建的]{style="font-family:宋体"}[cookie]{lang="EN-US"}[值也为]{style="font-family:宋体"}[517312001]{lang="EN-US"}[时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify dns error]{lang="EN-US"}]{#struct_0_x6596_18983_x808090862}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; ]{lang="EN-US"}[Cookie is equal to correct ACK. Changed cookie.]{lang="EN-US"}

[*[// cookie]{lang="EN-US"}*]{#struct_0_x6596_18983_x1390415748}*[序号正确，将其修改为计算得到的序号]{style="font-family:宋体"}*

::: {#-1561052350 .myid}
[]{#_Toc404793642}[]{#struct_0_x6596_18983_2085779610}

**攻击检测与防范 \-- 攻击检测与防范调试命令 \-- debugging client-verify http**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1756939628}

[**[debugging client-verify http ]{lang="EN-US"}**]{#struct_0_x6596_18983_83612178}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[**[undo debugging client-verify http ]{lang="EN-US"}**]{#struct_0_x6596_18983_x628656873}[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6596_18983_83461097}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6596_18983_1555910228}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6596_18983_1394680811}

[[network-admin]{lang="EN-US"}]{#struct_0_x6596_18983_1949194346}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6596_18983_1393783119}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6596_18983_2059926140}

[**[all]{lang="EN-US"}**]{#struct_0_x6596_18983_842881953}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x6596_18983_651323363}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6596_18983_2099677581}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6596_18983_813809921}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1109762334}

[**[debugging client-verify http]{lang="EN-US"}**]{#struct_0_x6596_18983_2000259572}[命令用来打开]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}**[undo debugging client-verify http]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[客户端验证功能的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_x191876971}[客户端验证功能的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging client-verify dns error]{lang="EN-US"}]{#struct_0_x6596_18983_1171001308}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_202664403}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_95010924}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_1293249142}

[[Failed to send a reply packet to client.]{lang="EN-US"}[ Reason: No route is found.]{lang="EN-US"}]{#struct_0_x6596_18983_x1210499200}

[[向客户端回复报文失败，原因：找不到匹配的路由]{style="font-family:宋体"}]{#struct_0_x6596_18983_345474970}

[[Cookie is equal to correct ACK. Changed cookie.]{lang="EN-US"}]{#struct_0_x6596_18983_797789423}

[[cookie]{lang="EN-US"}]{#struct_0_x6596_18983_x548868366}[序号正确，将其修改为计算得到的序号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging client-verify dns event]{lang="EN-US"}]{#struct_0_x6596_18983_2121447079}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_201693541}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_1304474439}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1569720877}

[[Added a trusted node:]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1548455757}[ Type HTTP, Source IP *src-ip-address*, VPN instance *vpn-instance* ]{lang="EN-US" style="font-size:
  9.0pt"}*[name.]{lang="EN-US" style="font-size:9.0pt"}*

[[[添加一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_2020763171}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址：]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[类型为]{style="font-size:9.0pt;font-family:宋体"}[HTTP]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[Removed expired trusted node: Type = HTTP, ]{lang="EN-US"}]{#struct_0_x6596_18983_1094550806}

[[Source IP = *src-ip-address*, ]{lang="EN-US"}]{#struct_0_x6596_18983_x1986308086}

[[VPN instance = *vpn-instance-name.*]{lang="EN-US"}]{#struct_0_x6596_18983_x272834799}

[[[删除一个信任]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_25351542}[[IP]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[地址]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}[：类型为]{style="font-size:9.0pt;font-family:宋体"}[HTTP]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[源]{style="font-size:9.0pt;font-family:宋体"}[IP]{lang="EN-US" style="font-size:9.0pt"}[地址为]{style="font-size:9.0pt;
  font-family:宋体"}*[src-ip-address]{lang="EN-US" style="font-size:9.0pt"}*[，所属的]{style="font-size:9.0pt;font-family:宋体"}[VPN]{lang="EN-US" style="font-size:9.0pt"}[实例名称为]{style="font-size:9.0pt;font-family:
  宋体"}*[vpn-instance-name]{lang="EN-US" style="font-size:9.0pt"}*

[[New cookie created, cookie ID is]{lang="EN-US"}]{#struct_0_x6596_18983_x564776304}*[ cookie-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[value is *cookie-value*]{lang="EN-US"}

[[[产生新]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}]{#struct_0_x6596_18983_x195502840}[cookie]{lang="EN-US" style="font-size:9.0pt"}[，]{style="font-size:9.0pt;font-family:
  宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-id]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-size:9.0pt;
  font-family:宋体"}[cookie]{lang="EN-US" style="font-size:9.0pt"}[值是]{style="font-size:9.0pt;font-family:宋体"}*[cookie-value]{lang="EN-US" style="font-size:9.0pt"}*

[[Cookie timed out.]{lang="EN-US"}]{#struct_0_x6596_18983_1730362580}

[[Cookie]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x6596_18983_x1739260309}[超时]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging client-verify dns packet]{lang="EN-US"}]{#struct_0_x6596_18983_91215657}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_205128627}[[字段]{style="font-family:黑体"}]{#struct_0_x6596_18983_1524549431}

[[描述]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1223930704}

[[The SYN packet soured from *src-ip-address* is untrusted, and it will be verified by HTTP client-verify.]{lang="EN-US"}]{#struct_0_x6596_18983_130449728}

[[源地址为]{style="font-family:宋体"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_x1170636481}[的报文不可信，需要对其进行]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}

[[The RST packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_1482595915}

[[该]{style="font-family:宋体"}[RST]{lang="EN-US"}]{#struct_0_x6596_18983_x754074153}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[The ACK packet is invalid and dropped.]{lang="EN-US"}]{#struct_0_x6596_18983_87301941}

[[该]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6596_18983_67908538}[报文已被验证不合法，被丢弃]{style="font-family:宋体"}

[[Received HTTP GET query packet from *src-ip-address* ,and will begin first redirect.]{lang="EN-US"}]{#struct_0_x6596_18983_1764551234}

[[收到]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}]{#struct_0_x6596_18983_838518724}[请求报文，即将进行第一次重定向]{style="font-family:宋体"}

[[Received HTTP GET query packet from *src-ip-address ,* and will begin second redirect.]{lang="EN-US"}]{#struct_0_x6596_18983_x1360531729}

[[收到]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}]{#struct_0_x6596_18983_x1435634213}[请求报文，即将进行第二次重定向]{style="font-family:宋体"}

[[Sent the redirect packet to client.]{lang="EN-US"}]{#struct_0_x6596_18983_562575476}

[[向]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_848974104}[客户端发送重定向报文]{style="font-family:宋体"}

[[Dropped SYN, and replied with SYN ACK.]{lang="EN-US"}]{#struct_0_x6596_18983_x1946810993}

[[丢弃]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x6596_18983_x1433048065}[报文，回复代理的]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Protocol(*pro-type*) ,FLAG(*flags*)]{lang="EN-US"}]{#struct_0_x6596_18983_x608938837}

[[SrcIP(*src-ip-address*:*src-port*), DstIP(*dest-ip-address*: *dest-port*),]{lang="EN-US"}]{#struct_0_x6596_18983_x1032349686}

[[Seq(*seqSeqNumber*), AckSeq(*seqAckNumber*)]{lang="EN-US"}]{#struct_0_x6596_18983_x200509063}

[[WinSize(*WinSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_x1897985352}

[[MSS(*MssSize*)]{lang="EN-US"}]{#struct_0_x6596_18983_31573695}

[[设备向服务器或客户端发送的报文信息：]{style="font-family:宋体"}]{#struct_0_x6596_18983_191251790}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pro-type]{lang="EN-US"}*]{#struct_0_x6596_18983_556169501}[：协议类型，包括]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[Other]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[Other]{lang="EN-US"}[表示除]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[以外的其它协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flags]{lang="EN-US"}*]{#struct_0_x6596_18983_1696533669}[：报文标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_945027638}[：源]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-port]{lang="EN-US"}*]{#struct_0_x6596_18983_x1620342975}[：源端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-ip-address]{lang="EN-US"}*]{#struct_0_x6596_18983_386507437}[：目的]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-port]{lang="EN-US"}*]{#struct_0_x6596_18983_784211375}[：目的端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqSeqNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_x1114131053}[：报文序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seqAckNumber]{lang="EN-US"}*]{#struct_0_x6596_18983_x688105428}[：确认序列号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[WinSize]{lang="EN-US"}*]{#struct_0_x6596_18983_x1317631121}[：窗口大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[MssSize]{lang="EN-US"}*]{#struct_0_x6596_18983_2099818196}[：]{lang="EN-US" style="font-family:宋体"}[MSS]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6596_18983_x1493850539}

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_x683744283}[配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证受保护]{style="font-family:宋体"}[IP 6.1.1.2]{lang="EN-US"}[，在入接口上使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能，并打开]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证报文调试信息开关。]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[设备收到]{style="font-family:宋体"}]{#struct_0_x6596_18983_289347456}[HTTP]{lang="EN-US"}[客户端发送的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的首个]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify http packet]{lang="EN-US"}]{#struct_0_x6596_18983_1308958490}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; The SYN packet 9.1.1.1 is untrusted, and will be verified by HTTP client-verify.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_97306532}*[源地址为]{style="font-family:宋体"}[9.1.1.1]{lang="EN-US"}[的报文不可信，需要对其进行]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证]{style="font-family:宋体"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Dropped SYN, and replied with SYN ACK:]{lang="EN-US"}]{#struct_0_x6596_18983_x1894352161}

[      Protocol(TCP), FLAG(SYNACK)]{lang="EN-US"}

[      SrcIP(6.1.1.2: 2200), DstIP(9.1.1.1: 1)]{lang="EN-US"}

[      Seq(0),AckSeq(369121992)]{lang="EN-US"}

[      WinSize(0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x1132920932}*[丢弃]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，设备代替服务器向客户端回复]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_1470857155}[客户端与设备之间的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立后，]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端首次发送]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[请求报文时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Receive HTTP GET query packet 9.1.1.1, and will begin first redirect. ]{lang="EN-US"}]{#struct_0_x6596_18983_533734255}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x224006795}*[收到]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[请求报文，即将进行第一次重定向验证处理]{style="font-family:宋体"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Sent the redirect packet to client.]{lang="EN-US"}]{#struct_0_x6596_18983_1123424053}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1988124907}*[向]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端发送重定向报文]{style="font-family:宋体"}*

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_1303792063}[客户端根据第一次的重定向结果，再次发送]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[请求报文时，设备上输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Receive HTTP GET query packet 9.1.1.1, and will begin second redirect. ]{lang="EN-US"}]{#struct_0_x6596_18983_x1030735271}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_980365585}*[收到]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[请求报文，即将进行第二次重定向验证处理]{style="font-family:宋体"}*

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Sent the redirect packet to client.]{lang="EN-US"}]{#struct_0_x6596_18983_228624466}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_1835220245}*[向]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端发送从定向报文]{style="font-family:宋体"}*

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[HTTP]{lang="EN-US"}]{#struct_0_x6596_18983_x1625549471}[客户端根据第二次的重定向结果，再次发送]{style="font-family:宋体"}[HTTP GET]{lang="EN-US"}[请求报文时，设备上输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type HTTP, Source IP 9.1.1.1, VPN instance \--.]{lang="EN-US"}]{#struct_0_x6596_18983_x391088661}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_x1306558361}*[添加一个信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：]{style="font-family:宋体"}[类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[9.1.1.1]{lang="EN-US"}[，属于公网]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_856047713}[在入接口上使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验功能。打开]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证事件调试信息开关后，当设备对来自客户端的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名为]{style="font-family:宋体"}[kkk]{lang="EN-US"}[且目的地址为受保护]{style="font-family:宋体"}[IP]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[连接请求验证通过时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify http event]{lang="EN-US"}]{#struct_0_x6596_18983_1649479502}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; Added a trusted node: Type HTTP, Source IP 1.1.1.1, VPN instance kkk.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6596_18983_639982788}*[添加一个信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：类型]{style="font-family:宋体"}[为]{style="font-family:宋体"}*[HTTP]{lang="EN-US"}*[，]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为[1.1.1.1]{lang="EN-US"}，所]{style="font-family:宋体"}[属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}[kkk]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x6596_18983_806465731}[在入接口上使能]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证功能。打开]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[客户端验证错误调试信息开关后，当设备接收到客户端首次发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文]{style="font-family:宋体"}*[SeqNumber]{lang="EN-US"}*[为]{style="font-family:宋体"}[517312000]{lang="EN-US"}[，且设备此时创建的]{style="font-family:宋体"}[cookie]{lang="EN-US"}[值也为]{style="font-family:宋体"}[517312001]{lang="EN-US"}[时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging client-verify http error]{lang="EN-US"}]{#struct_0_x6596_18983_x1282826927}

[\*Mar 5 21:08:14:237 2013 Sysname ATTACK/7/PACKET: -MDC=1; ]{lang="EN-US"}[Cookie is equal to correct ACK. Changed cookie.]{lang="EN-US"}

[*[// cookie]{lang="EN-US"}*]{#struct_0_x6596_18983_x842398821}*[序号正确，将其修改为计算得到的序号]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}
