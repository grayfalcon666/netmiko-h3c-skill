::: {#229615355 .myid}
[]{#_Toc382494448}[]{#_Toc404797453}[]{#struct_0_18273_17671_1047699415}[]{#_Toc388540174}

**Packet Capture \-- Packet Capture配置命令 \-- packet-capture interface**

------------------------------------------------------------------------

[**[packet-capture interface]{lang="EN-US"}**]{#struct_0_18273_17671_x1516806906}[命令用来开启指定接口的入方向报文捕获功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18273_17671_x237785575}

[[捕获并保存报文到文件：]{style="font-family:宋体"}]{#struct_0_18273_17671_x1213403866}

[**[packet-capture interface]{lang="EN-US"}**[ *interface-type* *interface-number* \[ **capture-filter** *capt-expression* \| **limit-captured-frames** *limit* \| **limit-frame-size** *bytes* \| **autostop filesize** *kilobytes* \| **autostop duration** *seconds* \| **autostop files** *numbers* \| **capture-ring-buffer filesize** *kilobytes* \| **capture-ring-buffer duration** *seconds* \| **capture-ring-buffer files** *numbers* \] \* **write** *filepath* \[ **raw** \| { **brief** \| **verbose** } \] \*]{lang="EN-US"}]{#struct_0_18273_17671_223013530}

[[捕获并显示报文内容：]{style="font-family:宋体"}]{#struct_0_18273_17671_x341708466}

[**[packet-capture interface]{lang="EN-US"}**[ *interface-type* *interface-number* \[ **capture-filter** *capt-expression* \| **display-filter** *disp-expression* \| **limit-captured-frames** *limit* \| **limit-frame-size** *bytes* \| **autostop duration** *seconds* \] \* \[ **raw** \| { **brief** \| **verbose** } \] \* ]{lang="EN-US"}]{#struct_0_18273_17671_1533591858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18273_17671_198690934}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18273_17671_x395360750}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18273_17671_x1202510391}

[[network-admin]{lang="EN-US"}]{#struct_0_18273_17671_20271098}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_18273_17671_676609332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18273_17671_1102615573}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_18273_17671_1839753896}[：指定捕获报文的二层以太网接口]{style="font-family:宋体"}[/]{lang="EN-US"}[三层以太网接口。]{style="font-family:宋体"}

[**[capture-filter]{lang="EN-US"}***[ capt-expression]{lang="EN-US"}*]{#struct_0_18273_17671_x1176532658}[：指定用来捕获报文的过滤规则，]{style="font-family:宋体"}*[capt-expression]{lang="EN-US"}*[为捕获过滤表达式。设备根据此参数指定的过滤规则对报文进行过滤并捕获匹配过滤规则的报文。捕获过滤语法规则请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[Packet Capture]{lang="EN-US"}["。如果不指定此参数，则捕获该接口的所有入方向的报文。]{style="font-family:宋体"}

[**[display-filter]{lang="EN-US"}***[ disp-expression]{lang="EN-US"}*]{#struct_0_18273_17671_x1436102732}[：指定用来显示报文的过滤规则。]{style="font-family:宋体"}*[disp-expression]{lang="EN-US"}*[为显示过滤表达式。设备对已捕获的报文匹配参数指定的显示过滤规则，并将匹配的报文内容进行显示。与捕获过滤不同的是，显示过滤支持报文内容过滤，捕获过滤语法规则请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[Packet Capture]{lang="EN-US"}["。如果不指定此参数，则显示所有捕获到的报文信息。]{style="font-family:宋体"}

[**[limit-captured-frames]{lang="EN-US"}***[ limit]{lang="EN-US"}*]{#struct_0_18273_17671_x61037192}[：指定捕获报文的最大个数，]{style="font-family:宋体"}*[limit]{lang="EN-US"}*[为报文的最大个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[。当达到捕获报文的最大个数时，则停止捕获报文，若指定报文最大个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则表示没有限制。如果没有指定此参数，表示捕获报文的最大个数为]{style="font-family:宋体"}[10]{lang="EN-US"}[个。]{style="font-family:宋体"}

[**[limit-frame-size]{lang="EN-US"}***[ bytes]{lang="EN-US"}*]{#struct_0_18273_17671_223013529}[：指定捕获报文的最大长度，]{style="font-family:宋体"}*[bytes]{lang="EN-US"}*[为报文的最大长度，取值范围为]{style="font-family:宋体"}[64]{lang="EN-US"}[～]{style="font-family:宋体"}[8000]{lang="EN-US"}[，单位为字节。当捕获到的报文超过此长度，会对报文进行截断。如果未指定本参数，表示能够捕获的报文的最大长度为]{style="font-family:宋体"}[8000]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[**[autostop filesize]{lang="EN-US"}**[ *kilobytes*]{lang="EN-US"}]{#struct_0_18273_17671_x805060295}[：指定存储报文文件大小，]{style="font-family:宋体"}*[kilobytes]{lang="EN-US"}*[为文件长度最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65536]{lang="EN-US"}[，单位为千字节。当报文文件大小达到最大值时，捕获报文自动停止。如果没有指定本参数，表示对报文文件大小没有限制。]{style="font-family:宋体"}

[**[autostop]{lang="EN-US"}**[ **duration** *seconds*]{lang="EN-US"}]{#struct_0_18273_17671_1640689781}[：指定捕获报文时长，]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[为时长最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。当捕获报文时长达到最大值时，捕获报文自动停止。如果没有指定本参数，表示不对捕获报文的时长进行限制。]{style="font-family:宋体"}

[**[autostop]{lang="EN-US"}**[ **files** *numbers*]{lang="EN-US"}]{#struct_0_18273_17671_x1580180210}[：指定切换存储报文文件次数，]{style="font-family:宋体"}*[numbers]{lang="EN-US"}*[为文件切换次数最大值，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。当指定本参数时，报文将被保存到文件名为扩展文件名的文件中，扩展文件名由]{style="font-family:宋体"}**[write]{lang="EN-US"}**[参数指定的文件名称、文件生成序号和写入时间组成，当切换到新文件时，新生成的扩展报文文件序号按序递增，例如，指定的文件名称为]{style="font-family:宋体"}[a.pcap]{lang="EN-US"}[，则扩展名称为]{style="font-family:宋体"}[a_00001_20140211034151.pcap]{lang="EN-US"}[，当达到切换写文件条件时，则将报文信息写入新生成]{style="font-family:宋体"}[a_00002_20140211034207.pcap]{lang="EN-US"}[文件中，依次类推。当切换文件次数达到最大值时，捕获报文自动停止。如果没有指定本参数，表示不对报文文件切换的次数进行限制。]{style="font-family:宋体"}

[**[capture-ring-buffer]{lang="EN-US"}**[ **filesize** *kilobytes*]{lang="EN-US"}]{#struct_0_18273_17671_387825072}[：指定切换存储报文文件大小，]{style="font-family:宋体"}*[kilobytes]{lang="EN-US"}*[为报文文件长度最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65536]{lang="EN-US"}[，单位为千字节。当报文文件大小达到最大值时，切换到下一个文件来存储捕获报文。如果没有指定本参数，表示不以文件大小为限制切换报文文件。]{style="font-family:宋体"}

[**[capture-ring-buffer]{lang="EN-US"}**[ **duration** *seconds*]{lang="EN-US"}]{#struct_0_18273_17671_x1298256827}[：指定切换存储报文文件时长，]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[为时长最大值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。当捕获报文时长达到最大值时，切换到下一个文件来存储捕获报文。如果没有本参数，表示不以时长为限制切换报文文件。]{style="font-family:宋体"}

[**[capture-ring-buffer]{lang="EN-US"}**[ **files** *numbers*]{lang="EN-US"}]{#struct_0_18273_17671_x1186379767}[：指定存储报文文件最大存在个数，]{style="font-family:宋体"}*[numbers]{lang="EN-US"}*[为报文文件个数最大值，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[；当指定本参数时，报文将被保存到文件名为扩展文件名的文件中，扩展文件名由]{style="font-family:宋体"}**[write]{lang="EN-US"}**[参数指定的文件名称、文件生成序号和写入时间组成，当切换到新文件时，新生成的扩展报文文件序号按序递增，例如，指定的文件名称为]{style="font-family:宋体"}[a.pcap]{lang="EN-US"}[，则扩展名称为]{style="font-family:宋体"}[a_00001_20140211034151.pcap]{lang="EN-US"}[，当达到切换写文件条件时，则将报文信息写入新生成]{style="font-family:宋体"}[a_00002_20140211034207.pcap]{lang="EN-US"}[文件中，依次类推。当文件个数达到最大个数时，删除捕获报文过程中生成的最老文件，将捕获的报文写入新生成的扩展文件中。如果没有指定本参数，表示报文文件的最大存在个数没有限制。]{style="font-family:宋体"}

[**[write]{lang="EN-US"}***[ filepath]{lang="EN-US"}*]{#struct_0_18273_17671_x1718180369}[：指定保存捕获报文的文件完整路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[字符的字符串，区分大小写。文件名命名规则的详细介绍，请参见"基础配置指导"中的"文件系统管理"。只支持以]{style="font-family:宋体"}[pcap]{lang="EN-US"}[格式的文件保存报文信息，保存到用户指定位置。如果没有指定此参数，将不会保存捕获的报文。]{style="font-family:宋体"}

[**[raw]{lang="EN-US"}**]{#struct_0_18273_17671_1830595952}**[：]{style="font-family:宋体"}**[将报文内容以十六进制格式显示。如果不指定此参数则不将报文文件内容用十六进制格式显示。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18273_17671_1045220718}[：显示捕获报文的详细信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_18273_17671_x987020265}[：显示捕获报文的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18273_17671_x791395324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启指定接口的报文捕获功能，设备会实时显示捕获报文的信息，如果用户希望停止捕获，直接输入]{style="font-family:宋体"}]{#struct_0_18273_17671_1110344626}[Ctrl+C]{lang="EN-US"}[停止捕获报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定]{lang="EN-US" style="font-family:宋体"}**[autostop files]{lang="EN-US"}**]{#struct_0_18273_17671_1533591852}[参数或者]{lang="EN-US" style="font-family:
宋体"}**[capture-ring-buffer]{lang="EN-US"}**[ **files**]{lang="EN-US"}[参数时，如果同时指定]{lang="EN-US" style="font-family:宋体"}**[autostop filesize]{lang="EN-US"}**[参数，则]{lang="EN-US" style="font-family:
宋体"}**[autostop filesize]{lang="EN-US"}**[参数为切换条件属性参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定]{lang="EN-US" style="font-family:宋体"}**[autostop files]{lang="EN-US"}**]{#struct_0_18273_17671_x472318778}[参数或者]{lang="EN-US" style="font-family:
宋体"}**[capture-ring-buffer]{lang="EN-US"}**[ **files**]{lang="EN-US"}[参数时，则需指定一个具有切换捕获报文存文件条件属性的参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当同时指定]{lang="EN-US" style="font-family:宋体"}**[autostop filesize]{lang="EN-US"}**]{#struct_0_18273_17671_1491361101}[和]{lang="EN-US" style="font-family:
宋体"}**[capture-ring-buffer filesize]{lang="EN-US"}**[时，]{lang="EN-US" style="font-family:宋体"}**[autostop filesize]{lang="EN-US"}**[停止条件参数属性失效，]{lang="EN-US" style="font-family:宋体"}**[capture-ring-buffer filesize]{lang="EN-US"}**[的切换条件参数属性生效，且以后指定参数的]{lang="EN-US" style="font-family:宋体"}*[kilobytes]{lang="EN-US"}*[为切换条件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于文件系统对文件个数有限制，所以保存捕获报文文件的最大个数同样会有限制，具体数目与设备使用的文件系统有关。当达到文件系统的最大个数时，将退出捕获。]{style="font-family:宋体"}]{#struct_0_18273_17671_1714281079}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当不指定]{style="font-family:宋体"}]{#struct_0_18273_17671_1163639719}**[raw]{lang="EN-US"}**[、]{style="font-family:宋体"}**[brief]{lang="EN-US"}**[和]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**[中的任何一个参数时，指定]{style="font-family:宋体"}**[write]{lang="EN-US"}**[参数，显示捕获的报文个数；当不指定]{style="font-family:宋体"}**[raw]{lang="EN-US"}**[、]{style="font-family:宋体"}**[brief]{lang="EN-US"}**[、]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**[和]{style="font-family:宋体"}**[write]{lang="EN-US"}**[中的任何一个参数时，显示报文的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18273_17671_x136699060}

[[\# ]{lang="EN-US"}]{#struct_0_18273_17671_223013535}[开启接口]{style="font-family:宋体"}[Gigabitehernet1/0/1]{lang="EN-US"}[报文捕获功能。]{style="font-family:宋体"}

[[\<Sysname\> packet-capture interface Gigabitehernet1/0/1]{lang="EN-US"}]{#struct_0_18273_17671_1533591853}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18273_17671_1047961559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet-capture read]{lang="EN-US"}**]{#struct_0_18273_17671_90289999}
:::

::: {#-447274429 .myid}
[]{#_Toc382494460}[]{#_Toc404797454}[]{#struct_0_18273_17671_x1466089849}[]{#_Toc388540175}[]{#_Toc382494289}[]{#_Toc382494389}[]{#_Toc382494449}[]{#_Toc382494299}[]{#_Toc382494399}[]{#_Toc382494459}

**Packet Capture \-- Packet Capture配置命令 \-- packet-capture read**

------------------------------------------------------------------------

[**[packet-capture read]{lang="EN-US"}**]{#struct_0_18273_17671_212878415}[命令用来开启解析并显示保存的数据包文件的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18273_17671_356472023}

[**[packet-capture read ]{lang="EN-US"}***[filepath ]{lang="EN-US"}*[\[ **verbose** \] \[ **display-filter** *disp-expression* \] \[ **raw** \| { **brief** \| **verbose** } \] \*]{lang="EN-US"}]{#struct_0_18273_17671_x1733276819}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18273_17671_1398228454}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18273_17671_x1058819046}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18273_17671_223013534}

[[network-admin]{lang="EN-US"}]{#struct_0_18273_17671_1533591854}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_18273_17671_1047633879}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18273_17671_x729100558}

[**[read]{lang="EN-US"}***[ filepath]{lang="EN-US"}*]{#struct_0_18273_17671_1911816399}[：]{style="font-family:宋体"}[指定读取的文件的完整路径，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。文件名命名规则的详细介绍，请参见"基础配置指导"中的"文件系统管理"。读取指定路径上的]{style="font-family:宋体"}[pcap]{lang="EN-US"}[或]{style="font-family:宋体"}[pcapng]{lang="EN-US"}[格式文件。]{style="font-family:宋体"}

[**[display-filter]{lang="EN-US"}***[ disp-expression]{lang="EN-US"}*]{#struct_0_18273_17671_1037167962}[：指定用来显示报文的过滤规则。]{style="font-family:宋体"}*[disp-expression]{lang="EN-US"}*[为显示报文的过滤规则。设备报文文件内容匹配参数指定的显示过滤规则，并将匹配的报文内容进行显示。显示过滤语法规则参见]{style="font-family:宋体"}[Packet Capture]{lang="EN-US"}[配置手册。如果不指定此参数，则显示报文文件所的报文信息。]{style="font-family:宋体"}

[**[raw]{lang="EN-US"}**]{#struct_0_18273_17671_1644672813}[：]{style="font-family:宋体"}[将报文文件内容用十六进制格式显示。如果不指定此参数，则不将报文文件内容用十六进制格式显示。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_18273_17671_611211870}[：显示报文文件的简要信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18273_17671_x1171223529}[：显示报文文件的详细信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18273_17671_1587624842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启解析并显示报文文件内容功能，]{style="font-family:宋体"}]{#struct_0_18273_17671_x1629664873}[Packet Capture]{lang="EN-US"}[终端显示从指定文件中读取解析的报文信息，如果用户希望退出此过程，可以直接输入]{style="font-family:宋体"}[Ctrl+C]{lang="EN-US"}[退出解析过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet Capture]{lang="EN-US"}]{#struct_0_18273_17671_78850495}[支持解析]{lang="EN-US" style="font-family:宋体"}[pcap]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[pcapng]{lang="EN-US"}[格式的报文文件。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[未指定]{style="font-family:宋体"}]{#struct_0_18273_17671_x555469134}**[raw]{lang="EN-US"}**[、]{style="font-family:宋体"}**[brief]{lang="EN-US"}**[、]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**[参数时，则显示简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18273_17671_614539976}

[[\# ]{lang="EN-US"}]{#struct_0_18273_17671_223013533}[解析]{style="font-family:宋体"}[flash:/test]{lang="EN-US"}[目录下的报文文件]{style="font-family:宋体"}**[aaaa.pcap]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> packet-capture read flash:/test/aaaa.pcap]{lang="EN-US"}]{#struct_0_18273_17671_1533591855}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18273_17671_1047568343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet-capture interface]{lang="EN-US"}**]{#struct_0_18273_17671_x1900419065}
:::
