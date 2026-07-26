::: {#-1384994826 .myid}
[]{#_Toc404797000}[]{#struct_0_12109_70365_x418932927}

**NETCONF \-- NETCONF配置命令 \-- xml**

------------------------------------------------------------------------

[**[xml]{lang="EN-US"}**]{#struct_0_12109_70365_277998026}[命令用来进入]{style="font-family:宋体"}[X]{lang="EN-US"}[ML]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12109_70365_1855465270}

[**[xml]{lang="EN-US"}**]{#struct_0_12109_70365_1620827523}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12109_70365_1888206398}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12109_70365_x1564647199}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1034204795}

[[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_1781392602}

[[network-operator]{lang="EN-US"}]{#struct_0_12109_70365_620465758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12109_70365_x1757191416}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12109_70365_x365347391}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12109_70365_x450670295}

[[进入]{style="font-family:宋体"}[XML]{lang="EN-US"}]{#struct_0_12109_70365_x471338286}[视图后可以输入]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令来配置或者获取系统数据。用户登录时使用的角色不同，可执行的]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[操作也不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_429415758}[和]{lang="EN-US" style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[可执行全部操作。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[network-operator]{lang="EN-US"}]{#struct_0_12109_70365_938194924}[和]{lang="EN-US" style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[可执行]{lang="EN-US" style="font-family:宋体"}[get]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[get-bulk]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[get-config]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[get-bulk-config]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[get-sessions]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[close-session]{lang="EN-US"}[操作。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_12109_70365_905799210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户输入的]{style="font-family:宋体"}]{#struct_0_12109_70365_1780933851}[NETCONF]{lang="EN-US"}[指令必须符合]{style="font-family:宋体"}[XML]{lang="EN-US"}[语言格式要求和《]{style="font-family:宋体"}[NETCONF XML API ]{lang="EN-US"}[手册》中的语法、语义要求。建议使用第三方软件来协助生成]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令，命令行手工输入方式通常用于研发和测试环境。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[退出]{style="font-family:宋体"}]{#struct_0_12109_70365_1396769202}[XML]{lang="EN-US"}[视图时需要使用相关的]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令]{style="font-family:宋体"}[，不能使用]{style="font-family:宋体"}**[quit]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_12109_70365_x595364348}[XML]{lang="EN-US"}[模式下终止当前任务的快捷键有重置缓存的功能，快捷键之前的内容都会被清除掉。如果在用户线]{style="font-family:宋体"}[/]{lang="EN-US"}[用户线类视图下使用]{style="font-family:宋体"}**[escape-key]{lang="EN-US"}**[命令配置了终止当前任务的快捷键（默认为]{style="font-family:宋体"}[Ctrl+C]{lang="EN-US"}[），可能会影响]{style="font-family:宋体"}[XML]{lang="EN-US"}[视图下相关配置。例如：在用户线视图下配置了]{style="font-family:宋体"}**[escape-key ]{lang="EN-US"}**[a]{lang="EN-US"}[，当]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令中含有字符']{style="font-family:宋体"}[a]{lang="EN-US"}['时，其实只有]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令最后一个']{style="font-family:宋体"}[a]{lang="EN-US"}['之后的内容能够得到处理；当]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令中不含有字符']{style="font-family:宋体"}[a]{lang="EN-US"}['时，则对]{style="font-family:宋体"}[XML]{lang="EN-US"}[视图下的配置没有影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12109_70365_1064976089}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_x1677849009}[进入]{style="font-family:宋体"}[XML]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> xml]{lang="EN-US"}]{#struct_0_12109_70365_x1738853646}

[\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>\<hello xmlns=\"urn:ietf:params:xml:ns:netconf:base:1.0\"\>\<capabilities\>\<capability\>urn:ietf:params:netconf:base:1.1\</capability\>\<capability\>urn:ietf:params:netconf:writable-running\</capability\>\<capability\>urn:ietf:params:netconf:capability:notification:1.0\</capability\>\<capability\>urn:ietf:params:netconf:capability:validate:1.1\</capability\>\<capability\>urn:ietf:params:netconf:capability:interleave:1.0\</capability\>\<capability\>urn:h3c:params:netconf:capability:h3c-netconf-ext:1.0\</capability\>\</capabilities\>\<session-id\>1\</session-id\>\</hello\>\]\]\>\]\]\>]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_1486509793}[退出]{style="font-family:宋体"}[XML]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<rpc message-id=\"101\" xmlns=\"urn:ietf:params:xml:ns:netconf:base:1.0\"\>]{lang="EN-US"}]{#struct_0_12109_70365_x205175141}

[  \<close-session\>]{lang="EN-US"}

[  \</close-session\>]{lang="EN-US"}

[\</rpc\>\]\]\>\]\]\>]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}
:::

::: {#343253621 .myid}
[]{#_Toc404797001}[]{#struct_0_12109_70365_x954058782}

**NETCONF \-- NETCONF配置命令 \-- netconf soap http enable**

------------------------------------------------------------------------

[**[netconf soap http enable]{lang="EN-US"}**]{#struct_0_12109_70365_1780868315}[命令用来开启基于]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1343565422}

[**[netconf soap http enable]{lang="EN-US"}**]{#struct_0_12109_70365_x2097890213}

[**[undo netconf soap http enable]{lang="EN-US"}**]{#struct_0_12109_70365_1918867632}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12109_70365_x271681351}

[[基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_12109_70365_145198633}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12109_70365_x477796281}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12109_70365_5226060}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1017502817}

[[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_1780802779}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12109_70365_1400212794}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12109_70365_x803849491}

[[FIPS]{lang="EN-US"}]{#struct_0_12109_70365_549981024}[模式下，不支持本命令。]{style="font-family:宋体"}

[[配置该命令后，表示设备能够解析这样的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_12109_70365_1299072573}[报文，报文中的数据为]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[封装过的]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12109_70365_1083142012}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_1888980510}[开启基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12109_70365_1201960524}

[\[Sysname\] netconf soap http enable]{lang="EN-US"}
:::

::: {#-12797788 .myid}
[]{#_Toc404797002}[]{#struct_0_12109_70365_1282876097}

**NETCONF \-- NETCONF配置命令 \-- netconf soap https enable**

------------------------------------------------------------------------

[**[netconf soap https enable]{lang="EN-US"}**]{#struct_0_12109_70365_1780737243}[命令用来开启基于]{style="font-family:
宋体"}[HTTPS]{lang="EN-US"}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12109_70365_574543069}

[**[netconf soap https enable]{lang="EN-US"}**]{#struct_0_12109_70365_708850510}

[**[undo netconf soap https enable]{lang="EN-US"}**]{#struct_0_12109_70365_x2084723632}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12109_70365_x2064407187}

[[基于]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_12109_70365_1450495014}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12109_70365_x870195835}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12109_70365_x1502191668}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1100336121}

[[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_1780671707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12109_70365_x595429884}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12109_70365_978906058}

[[配置该命令后，表示设备能够解析这样的]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_12109_70365_436770049}[报文，报文中的数据为]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[封装过的]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[指令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12109_70365_x925417691}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_x802452284}[开启基于]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的]{style="font-family:宋体"}[SOAP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12109_70365_x564721612}

[\[Sysname\] netconf soap https enable]{lang="EN-US"}
:::

::: {#-2032328180 .myid}
[]{#_Toc404797003}[]{#struct_0_12109_70365_710827521}

**NETCONF \-- NETCONF配置命令 \-- netconf ssh server enable**

------------------------------------------------------------------------

[**[netconf]{lang="EN-US"}**[ **ssh** **server** **enable**]{lang="EN-US"}]{#struct_0_12109_70365_1013731624}[命令用来开启]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}[的接入方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **netconf** **ssh** **server** **enable**]{lang="EN-US"}]{#struct_0_12109_70365_x542339029}[命令用来关闭]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}[的接入方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12109_70365_1745955453}

[**[netconf]{lang="EN-US"}**[ **ssh** **server** **enable**]{lang="EN-US"}]{#struct_0_12109_70365_726328544}

[**[undo]{lang="EN-US"}**[ **netconf** **ssh** **server** **enable**]{lang="EN-US"}]{#struct_0_12109_70365_1020363023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1243967018}

[[未开启]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}]{#struct_0_12109_70365_x400997942}[的接入方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12109_70365_x444117100}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12109_70365_711679489}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12109_70365_2125708607}

[[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_1785449496}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12109_70365_1524451001}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12109_70365_1943644150}

[[用户配置该命令后，可以利用]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_12109_70365_x148475613}[客户端通过]{style="font-family:宋体"}[SSH]{lang="EN-US"}[子系统的方式接入设备的]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[系统，然后直接进入]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[配置模式，而不用手工输入]{style="font-family:宋体"}[XML]{lang="EN-US"}[命令。]{style="font-family:宋体"}

[[使能该命令前必须在设备上把]{style="font-family:宋体"}[SSH]{lang="EN-US"}]{#struct_0_12109_70365_x673074308}[连接终端的认证方式设置为]{style="font-family:宋体"}[scheme]{lang="EN-US"}[，支持]{style="font-family:宋体"}[NETCONF over SSH]{lang="EN-US"}[的客户端才能连接到]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}[系统，目前只支持用]{style="font-family:宋体"}[urn:ietf:params:netconf:base:1.0]{lang="EN-US"}[（设备与终端共同支持的能力集）连接系统。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12109_70365_150131718}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_1291026901}[开启]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}[的接入方式。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_12109_70365_1253065187}

[\[Sysname\] netconf ssh server enable]{lang="EN-US"}
:::

::: {#1900569941 .myid}
[]{#struct_0_12109_70365_x2000036350}[]{#_Toc404797004}

**NETCONF \-- NETCONF配置命令 \-- netconf ssh server port**

------------------------------------------------------------------------

[**[netconf]{lang="EN-US"}**[ **ssh** **server port**]{lang="EN-US"}]{#struct_0_12109_70365_x814367627}[命令用来设置]{style="font-family:宋体"}[ NETCONF Over SSH]{lang="EN-US"}[接入方式的监听端口号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **netconf** **ssh** **server** **port**]{lang="EN-US"}]{#struct_0_12109_70365_594691801}[命令用来把端口号恢复成默认的]{style="font-family:宋体"}[830]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12109_70365_711745025}

[**[netconf]{lang="EN-US"}**[ **ssh** **server** **port** *port-number*]{lang="EN-US"}]{#struct_0_12109_70365_1739778742}

[**[undo]{lang="EN-US"}**[ **netconf ssh** **server** **port**]{lang="EN-US"}]{#struct_0_12109_70365_x358237811}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12109_70365_839041449}

[[基于]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}]{#struct_0_12109_70365_220873783}[的接入方式的监听端口是]{style="font-family:宋体"}[830]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12109_70365_1842640156}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12109_70365_1984840591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12109_70365_1631876721}

[[network-admin]{lang="EN-US"}]{#struct_0_12109_70365_1254173406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12109_70365_1748682529}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12109_70365_81353307}

[*[port-number]{lang="EN-US"}*]{#struct_0_12109_70365_195364392}[：基于]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}[的接入方式的监听端口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[830]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12109_70365_x1938897156}

[[用户可以在必要时使用此命令来重新配置一个端口作为]{style="font-family:宋体"}[NETCONF]{lang="EN-US"}]{#struct_0_12109_70365_711155200}[子系统的监听端口，但由于]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务使用共享端口的方式来分配监听端口，为了正常使用，必须保证分配的端口不和其他使用的端口冲突。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12109_70365_155976134}

[[\# ]{lang="EN-US"}]{#struct_0_12109_70365_1503637520}[把基于]{style="font-family:宋体"}[NETCONF Over SSH]{lang="EN-US"}[的接入方式的监听端口设置为]{style="font-family:宋体"}[800]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> system]{lang="EN-US"}]{#struct_0_12109_70365_x1968209546}

[\[sysname\] netconf ssh server port 800]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
