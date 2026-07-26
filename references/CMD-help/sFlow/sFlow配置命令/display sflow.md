::: {#-383576854 .myid}
[]{#_Toc404797359}[]{#struct_0_39861_15601_x1924499741}[]{#_Toc185927308}[]{#_Toc123026768}

**sFlow \-- sFlow配置命令 \-- display sflow**

------------------------------------------------------------------------

[**[display sflow]{lang="EN-US"}**]{#struct_0_39861_15601_2136902062}[命令用来显示]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[的配置和运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_x2062552959}

[**[display sflow]{lang="EN-US"}**]{#struct_0_39861_15601_1935624119}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_1717060204}

[[任意视图]{style="font-family:宋体"}]{#struct_0_39861_15601_1306002724}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_x2066466122}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_x1070986085}

[[network-operator]{lang="EN-US"}]{#struct_0_39861_15601_x1050020783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x1472503774}

[[mdc-operator]{lang="EN-US"}]{#struct_0_39861_15601_154272349}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_2136836526}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x1286594978}[[显示]{style="font-family:宋体"}]{#_Toc129677285}[sFlow]{lang="EN-US"}[的配置和运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display sflow]{lang="EN-US"}]{#struct_0_39861_15601_x1074451043}

[sFlow datagram version: 5]{lang="EN-US"}

[Global information:]{lang="EN-US"}

[Agent IP: 10.10.10.1(CLI)]{lang="EN-US"}

[Source address: 10.0.0.1 2001::1]{lang="EN-US"}

[Collector information:]{lang="EN-US"}

[ID    IP              Port  Aging      Size VPN-instance Description]{lang="EN-US"}

[1     22:2:20::10     6535  N/A        1400 vpn1         netserver ]{lang="EN-US"}

[2     192.168.3.5     6543  500        1400              Office ]{lang="EN-US"}

[Port information:]{lang="EN-US"}

[Interface      CID   Interval(s) FID   MaxHLen Rate       Mode      Status]{lang="EN-US"}

[GE1/0/1         1     100         1     128     1000       Random    Active]{lang="EN-US"}

[GE1/0/2         2     100         2     128     1000       Random    Active]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display sflow]{lang="EN-US"}]{#struct_0_39861_15601_1568080900}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1551977458}[[字段]{style="font-family:黑体"}]{#struct_0_39861_15601_x936815669}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_39861_15601_2136770990}

[[sFlow datagram version]{lang="EN-US"}]{#struct_0_39861_15601_1868367986}

[[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_1988789284}[报文版本号，取值只能为]{style="font-family:宋体"}[5]{lang="EN-US"}[，表示当前仅支持发送版本号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Global information]{lang="EN-US"}]{#struct_0_39861_15601_1408779980}

[[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_x1064026892}[全局信息]{style="font-family:宋体"}

[[Agent IP]{lang="EN-US"}]{#struct_0_39861_15601_x565318538}

[[sFlow Agent]{lang="EN-US"}]{#struct_0_39861_15601_1790802983}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址：]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[CLI]{lang="EN-US"}]{#struct_0_39861_15601_2136705454}[：表示手工配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[Auto]{lang="EN-US"}]{#struct_0_39861_15601_1075167607}[：表示自动查找到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Source address]{lang="EN-US"}]{#struct_0_39861_15601_x1170506769}

[[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_1687374623}[报文的源地址]{style="font-family:宋体"}

[[Collector information]{lang="EN-US"}]{#struct_0_39861_15601_62671358}

[[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_2077198896}[信息]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_39861_15601_2137688494}

[[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_1428270509}[编号]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_39861_15601_1863988258}

[[接收]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_x566972974}[报文的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_39861_15601_894634715}

[[接收]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_2137622958}[报文的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的端口号]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_39861_15601_x2083917289}

[[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_837805666}[的剩余存活时间。如果显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，则表示对应的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[不会老化]{style="font-family:宋体"}

[[Size]{lang="EN-US"}]{#struct_0_39861_15601_x989787596}

[[每次发送]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_990683879}[报文时，]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[数据部分的最大长度]{style="font-family:宋体"}

[[VPN-instance]{lang="EN-US"}]{#struct_0_39861_15601_2137164207}

[[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_x858049075}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名]{style="font-family:宋体"}

[[Description]{lang="FR"}]{#struct_0_39861_15601_x288808481}

[[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_2146476190}[的描述信息]{style="font-family:宋体"}

[[Port information]{lang="EN-US"}]{#struct_0_39861_15601_x1676968912}

[[已配置]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_2137098671}[功能的接口信息]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_39861_15601_1039248761}

[[已配置]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_288143927}[功能的接口]{style="font-family:宋体"}

[[CID]{lang="EN-US"}]{#struct_0_39861_15601_1749236535}

[[经过]{style="font-family:宋体"}[Counter]{lang="EN-US"}]{#struct_0_39861_15601_x1869903756}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。如果没有指定]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号，显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Interval(s)]{lang="EN-US"}]{#struct_0_39861_15601_2137033135}

[[Counter]{lang="EN-US"}]{#struct_0_39861_15601_x2052817608}[采样的时间间隔]{style="font-family:宋体"}

[[FID]{lang="EN-US"}]{#struct_0_39861_15601_1094182425}

[[经过]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_39861_15601_x861900970}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。如果没有指定]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号，显示为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[MaxHLen]{lang="EN-US"}]{#struct_0_39861_15601_2136967599}

[[从原始报文的头开始，允许拷贝的最大字节数]{style="font-family:宋体"}]{#struct_0_39861_15601_276605303}

[[Rate]{lang="EN-US"}]{#struct_0_39861_15601_x1644321512}

[[Flow]{lang="EN-US"}]{#struct_0_39861_15601_x1323252764}[采样的报文采样率]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_39861_15601_2136902063}

[[Flow]{lang="EN-US"}]{#struct_0_39861_15601_x2062487423}[采样的采样模式，其可能的取值如下：]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[Determine]{lang="EN-US"}]{#struct_0_39861_15601_x1648566843}[：表示固定采样]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[Random]{lang="EN-US"}]{#struct_0_39861_15601_x489084450}[：表示随机采样]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_39861_15601_2136836527}

[[接口的]{style="font-family:宋体"}[sFlow]{lang="EN-US"}]{#struct_0_39861_15601_x1286660514}[功能的启用状态，其可能的取值如下：]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[Suspended]{lang="EN-US"}]{#struct_0_39861_15601_141937452}[：表示因接口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态而挂起]{style="font-family:宋体"}

[[l[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[Active]{lang="EN-US"}]{#struct_0_39861_15601_2136770991}[：表示因接口处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态而生效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#297587724 .myid}
[]{#_Toc404797360}[]{#struct_0_39861_15601_1868302450}

**sFlow \-- sFlow配置命令 \-- sflow agent**

------------------------------------------------------------------------

[**[sflow agent]{lang="EN-US"}**]{#struct_0_39861_15601_902577442}[命令用来配置]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo sflow agent]{lang="EN-US"}**]{#struct_0_39861_15601_x1083080931}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_x941987464}

[**[sflow agent ]{lang="EN-US"}**[{ **ip** *ip-address \|* **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_39861_15601_x1547056474}

[**[undo sflow agent ]{lang="EN-US"}**[{ **ip** *\|* **ipv6** }]{lang="EN-US"}]{#struct_0_39861_15601_x297406170}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x713486496}

[[未配置]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}]{#struct_0_39861_15601_x1178027045}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。设备会定期检查是否存在]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，如果不存在，设备会自动查找一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。自动查找的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址信息不会保存在设备上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x562838192}

[[系统视图]{style="font-family:宋体"}]{#struct_0_39861_15601_2136705455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_1075233143}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_1614916072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_2026499384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_1467105614}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_39861_15601_x478307659}[：]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_39861_15601_640436522}[：]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_39861_15601_82988235}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[建议用户手工配置]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}]{#struct_0_39861_15601_1989798896}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[在设备上只能配置一个]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}]{#struct_0_39861_15601_2137688495}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，新配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址会覆盖已有的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_1428336045}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x881177911}[配置]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_x987520455}

[\[Sysname\] sflow agent ip 10.10.10.1]{lang="EN-US"}
:::

::: {#1674168959 .myid}
[]{#struct_0_39861_15601_x1173732144}[]{#_Toc404797361}[]{#_Toc313548445}

**sFlow \-- sFlow配置命令 \-- sflow collector**

------------------------------------------------------------------------

[**[sflow collector]{lang="EN-US"}**]{#struct_0_39861_15601_181426124}[命令用来配置]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的参数。]{style="font-family:宋体"}

[**[undo sflow collector]{lang="EN-US"}**]{#struct_0_39861_15601_x1331523376}[命令用来删除指定的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_589475468}

[**[sflow collector ]{lang="EN-US"}***[collector-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] { **ip** *ip-address* \| **ipv6** *ipv6-address* } \[ **port** *port-number* \] \[ **datagram-size** *size* \] \[ **time-out** *seconds  *\] \[ **description** *text* \]]{lang="EN-US"}]{#struct_0_39861_15601_2137622959}

[**[undo sflow collector ]{lang="EN-US"}***[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x2083851753}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x2047510459}

[[没有]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}]{#struct_0_39861_15601_1667622624}[的相关信息存在。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x213435203}

[[系统视图]{style="font-family:宋体"}]{#struct_0_39861_15601_884420718}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_1503205026}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_770206512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x2128588440}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_x55187578}

[*[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x591719145}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_39861_15601_x1828975400}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，不可以包含空格，区分大小写。缺省情况下，]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[不关联到任何]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，位于公网。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_39861_15601_x1789690996}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_39861_15601_1800313825}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}***[ text]{lang="EN-US"}*]{#struct_0_39861_15601_x7098508}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的描述信息。缺省情况下，]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[CLI Collector]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[datagram-size ]{lang="EN-US"}***[size]{lang="EN-US"}*]{#struct_0_39861_15601_x1547758935}[：发送]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[数据部分的最大长度，取值范围为]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[1400]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_39861_15601_x1698464616}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[6343]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time-out ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_39861_15601_x591784681}[：配置的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的参数的老化时间，当到达老化时间时，所配置的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的参数将被删除。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。缺省情况下，配置的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的参数不老化*。*]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_1226242235}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_1368989013}[配置编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[Collector]{lang="EN-US"}[，关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[3.3.3.1]{lang="EN-US"}[，端口号保持缺省值，描述信息为"]{style="font-family:宋体"}[netserver]{lang="EN-US"}["，老化时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒，]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[数据部分的最大长度为]{style="font-family:宋体"}[1000]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_2012029545}

[\[Sysname\] sflow collector 2 vpn-instance vpn1 ip 3.3.3.1 description netserver  time-out 1200 datagram-size 1000]{lang="EN-US"}
:::

::: {#-934892518 .myid}
[]{#_Toc404797362}[]{#struct_0_39861_15601_223488229}[]{#_Toc313548447}

**sFlow \-- sFlow配置命令 \-- sflow counter interval**

------------------------------------------------------------------------

[**[sflow counter interval]{lang="EN-US"}**]{#struct_0_39861_15601_1629024465}[命令用来配置]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的时间间隔，同时开启]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[**[undo sflow counter interval]{lang="EN-US"}**]{#struct_0_39861_15601_2138136953}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_75833086}

[**[sflow counter interval]{lang="EN-US"}***[ interval-time]{lang="EN-US"}*]{#struct_0_39861_15601_x591850217}

[**[undo sflow counter interval]{lang="EN-US"}**]{#struct_0_39861_15601_x308533591}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x662209359}

[[不进行]{style="font-family:宋体"}[Counter]{lang="EN-US"}]{#struct_0_39861_15601_x753733535}[采样。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x573532969}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_2056252315}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1749930215}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_x61228185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_614358364}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_x591915753}

[*[interval-time]{lang="EN-US"}*]{#struct_0_39861_15601_470910037}[：]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的时间间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_x957477244}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x238239152}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒，同时开启]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_1703285289}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow counter interval 120]{lang="EN-US"}
:::

::: {#-937808626 .myid}
[]{#_Toc404797363}[]{#struct_0_39861_15601_262368042}

**sFlow \-- sFlow配置命令 \-- sflow counter collector**

------------------------------------------------------------------------

[**[sflow counter collector]{lang="EN-US"}**]{#struct_0_39861_15601_540026786}[命令用来配置经过]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[**[undo sflow counter collector]{lang="EN-US"}**]{#struct_0_39861_15601_1532588275}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_963492172}

[**[sflow counter collector ]{lang="EN-US"}***[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x591981289}

[**[undo sflow counter collector]{lang="EN-US"}**]{#struct_0_39861_15601_1230877174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1225673145}

[[Counter]{lang="EN-US"}]{#struct_0_39861_15601_2127588895}[采样和]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[没有绑定关系，即没有指定目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1876571055}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_872500666}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_x165125064}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_480929730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x201560838}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_x592046825}

[*[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x1567289736}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1624105851}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x352954846}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置经过]{style="font-family:宋体"}[Counter]{lang="EN-US"}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_551559294}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow counter collector 2]{lang="EN-US"}
:::

::: {#-346435111 .myid}
[]{#_Toc404797364}[]{#struct_0_39861_15601_824380243}[]{#_Toc313548450}

**sFlow \-- sFlow配置命令 \-- sflow flow collector**

------------------------------------------------------------------------

[**[sflow flow collector]{lang="EN-US"}**]{#struct_0_39861_15601_x602311376}[命令用来配置经过]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[**[undo sflow flow collector]{lang="EN-US"}**]{#struct_0_39861_15601_446588340}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_x17392846}

[**[sflow flow collector ]{lang="EN-US"}***[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x592112361}

[**[undo sflow flow collector]{lang="EN-US"}**]{#struct_0_39861_15601_342047849}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1518350159}

[[Flow]{lang="EN-US"}]{#struct_0_39861_15601_x469896141}[采样和]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[没有绑定关系，即没有指定目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_1637997926}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_1211676196}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_217968160}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_x1244482515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_2051188253}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_x592177897}

[*[collector-id]{lang="EN-US"}*]{#struct_0_39861_15601_x3499469}[：]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[的编号。编号的取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_659715828}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x625371658}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置经过]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样后，]{style="font-family:宋体"}[sFlow Agent]{lang="EN-US"}[输出]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[sFlow Collector]{lang="EN-US"}[编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_x345082452}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow flow collector 2]{lang="EN-US"}
:::

::: {#2004856301 .myid}
[]{#_Toc404797365}[]{#struct_0_39861_15601_x558356689}[]{#_Toc313548452}

**sFlow \-- sFlow配置命令 \-- sflow flow max-header**

------------------------------------------------------------------------

[**[sflow flow max-header]{lang="EN-US"}**]{#struct_0_39861_15601_761280157}[命令用来配置在进行报文内容拷贝时，从原始报文的头部开始，允许拷贝的最大字节数。拷贝的内容会记录在生成的采样样本中。]{style="font-family:宋体"}

[**[undo sflow flow max-header]{lang="EN-US"}**]{#struct_0_39861_15601_x559974386}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_1903829129}

[**[sflow flow max-header ]{lang="EN-US"}***[length]{lang="EN-US"}*]{#struct_0_39861_15601_x591194857}

[**[undo sflow flow max-header]{lang="EN-US"}**]{#struct_0_39861_15601_81000456}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1342022659}

[[从原始报文的头部开始，允许拷贝的最大字节数为]{style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_39861_15601_1825346805}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1711781171}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_1603078033}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_445499588}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_x1863202890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_1194168701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_1704047542}

[*[length]{lang="EN-US"}*]{#struct_0_39861_15601_x591260393}[：从原始报文的头部开始，允许拷贝的最大字节数，取值范围为]{style="font-family:宋体"}[18]{lang="EN-US"}[～]{style="font-family:宋体"}[512]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【用户指导】]{style="font-family:黑体"}]{#struct_0_39861_15601_1658332539}

[[建议用户使用缺省配置。]{style="font-family:宋体"}]{#struct_0_39861_15601_1580088314}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1205218662}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x455949027}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置在进行报文内容拷贝时，从原始报文的头部开始，允许拷贝的最大字节数为]{style="font-family:宋体"}[60]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_x1135992023}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow flow max-header 60]{lang="EN-US"}
:::

::: {#644220321 .myid}
[]{#_Toc404797366}[]{#struct_0_39861_15601_589199943}

**sFlow \-- sFlow配置命令 \-- sflow sampling-mode**

------------------------------------------------------------------------

[**[sflow sampling-mode]{lang="EN-US"}**]{#struct_0_39861_15601_765013294}[命令用来设置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的采样模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sflow sampling-mode**]{lang="EN-US"}]{#struct_0_39861_15601_x591719144}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1828909864}

[**[sflow sampling-mode]{lang="EN-US"}**[ { **determine** \| **random** }]{lang="EN-US"}]{#struct_0_39861_15601_1118915419}

[**[undo sflow sampling-mode]{lang="EN-US"}**]{#struct_0_39861_15601_775250384}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1305563854}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_39861_15601_1343542123}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_391535099}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_x1511916469}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1500657307}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_x1424399169}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x591784680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_1226176699}

[**[determine]{lang="EN-US"}**]{#struct_0_39861_15601_x189773180}[：表示采样模式为固定采样，采样率由]{style="font-family:宋体"}**[sflow sampling-rate]{lang="EN-US"}***[ rate]{lang="EN-US"}*[命令决定。例如，在配置此模式后，设定采样率为]{style="font-family:宋体"}[4000]{lang="EN-US"}[，设备会随机在]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4000]{lang="EN-US"}[个报文中选取其中的一个报文进行采样，比如第]{style="font-family:宋体"}[10]{lang="EN-US"}[个报文，下一次设备会抽取第]{style="font-family:宋体"}[4010]{lang="EN-US"}[个报文进行采样，以此类推。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[random]{lang="EN-US"}**]{#struct_0_39861_15601_x1093808006}[：表示采样模式为随机采样，采样率由]{style="font-family:宋体"}**[sflow sampling-rate]{lang="EN-US"}***[ rate]{lang="EN-US"}*[命令决定。设备会保持平均在每]{style="font-family:宋体"}*[rate]{lang="EN-US"}*[个报文中抽取一个报文进行采样，可能从每]{style="font-family:宋体"}*[rate]{lang="EN-US"}*[个报文中随机抽取任意一个或多个报文进行采样，也可能在某段的]{style="font-family:宋体"}*[rate]{lang="EN-US"}*[个报文中不采样报文。例如，在配置此模式后，设定报文的采样率为]{style="font-family:宋体"}[4000]{lang="EN-US"}[，设备可能会在]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4000]{lang="EN-US"}[个报文中选取其中的一个报文进行采样，在]{style="font-family:宋体"}[4001]{lang="EN-US"}[～]{style="font-family:宋体"}[8000]{lang="EN-US"}[个报文中选取其中的多个报文进行采样，在]{style="font-family:宋体"}[8001]{lang="EN-US"}[～]{style="font-family:宋体"}[12000]{lang="EN-US"}[个报文中不进行任何采样，但在长期时间内的总体趋势是]{style="font-family:宋体"}[4000]{lang="EN-US"}[个报文中抽取一个进行采样。本参数的支持情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_767472892}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_473134565}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的采样模式为固定采样。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_x531449618}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow sampling-mode determine]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1981934896}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[sflow sampling-rate]{lang="EN-US"}**]{#struct_0_39861_15601_x591850216}
:::

::: {#-34667101 .myid}
[]{#_Toc404797367}[]{#struct_0_39861_15601_x308468055}

**sFlow \-- sFlow配置命令 \-- sflow sampling-rate**

------------------------------------------------------------------------

[**[sflow sampling-rate]{lang="EN-US"}**]{#struct_0_39861_15601_864327229}[命令用来配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的报文采样率，即在]{style="font-family:宋体"}*[rate]{lang="EN-US"}*[个报文中抽取一个报文进行采样，同时开启]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[**[undo sflow sampling-rate]{lang="EN-US"}**]{#struct_0_39861_15601_x2019658639}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_1076804956}

[**[sflow sampling-rate]{lang="EN-US"}***[ rate]{lang="EN-US"}*]{#struct_0_39861_15601_x445053330}

[**[undo sflow sampling-rate]{lang="EN-US"}**]{#struct_0_39861_15601_x459629616}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x591915752}

[[不进行]{style="font-family:宋体"}[Flow]{lang="EN-US"}]{#struct_0_39861_15601_470975573}[采样]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x973449647}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39861_15601_x1460672240}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_623586961}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_419899612}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x606721127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_606103069}

[*[rate]{lang="EN-US"}*]{#struct_0_39861_15601_x996067760}[：]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的报文采样率，取值范围与设备的型号相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_2022021594}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_x591981288}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样的报文采样率为]{style="font-family:宋体"}[4000]{lang="EN-US"}[，即在]{style="font-family:宋体"}[4000]{lang="EN-US"}[个报文中抽取一个报文进行采样，同时开启]{style="font-family:宋体"}[Flow]{lang="EN-US"}[采样功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_1230811638}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] sflow sampling-rate 4000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_749969273}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[sflow sampling-mode]{lang="EN-US"}**]{#struct_0_39861_15601_1310610636}
:::

::: {#-409285621 .myid}
[]{#_Toc404797368}[]{#struct_0_39861_15601_x747764512}

**sFlow \-- sFlow配置命令 \-- sflow source**

------------------------------------------------------------------------

[**[sflow source]{lang="EN-US"}**]{#struct_0_39861_15601_x1314111741}[命令用来配置]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo sflow source]{lang="EN-US"}**]{#struct_0_39861_15601_x534355949}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39861_15601_567974726}

[**[sflow source ]{lang="EN-US"}**[{ **ip** *ip-address \|* **ipv6** *ipv6-address* } \*]{lang="EN-US"}]{#struct_0_39861_15601_x1478857806}

[**[undo sflow source ]{lang="EN-US"}**[{ **ip** *\|* **ipv6** } \*]{lang="EN-US"}]{#struct_0_39861_15601_x592046824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1567355272}

[[设备使用路由决定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_39861_15601_x857714947}[地址作为]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39861_15601_x851959748}

[[系统视图]{style="font-family:宋体"}]{#struct_0_39861_15601_672867111}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39861_15601_689932750}

[[network-admin]{lang="EN-US"}]{#struct_0_39861_15601_1323020064}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39861_15601_x133090330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39861_15601_x1426464336}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_39861_15601_x592112360}[：]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_39861_15601_342113385}[：]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39861_15601_2027784469}

[[\# ]{lang="EN-US"}]{#struct_0_39861_15601_1947423962}[配置]{style="font-family:宋体"}[sFlow]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39861_15601_1524158133}

[\[Sysname\] sflow source ip 10.0.0.1]{lang="EN-US"}
:::
