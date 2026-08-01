<!-- CMD-INDEX
  packet-capture interface            | 用户视图             | L6
  packet-capture read                 | 用户视图             | L88
-->

**Packet Capture \-- Packet Capture配置命令 \-- packet-capture interface**

------------------------------------------------------------------------

**[packet-capture interface**]命令用来开启指定接口的入方向报文捕获功能。

【命令】

捕获并保存报文到文件：

**[packet-capture interface**[ *interface-type* *interface-number* [ **capture-filter** *capt-expression* \| **limit-captured-frames** *limit* \| **limit-frame-size** *bytes* \| **autostop filesize** *kilobytes* \| **autostop duration** *seconds* \| **autostop files** *numbers* \| **capture-ring-buffer filesize** *kilobytes* \| **capture-ring-buffer duration** *seconds* \| **capture-ring-buffer files** *numbers* ] \* **write** *filepath* [ **raw** \| { **brief** \| **verbose** } ] \*]]

捕获并显示报文内容：

**[packet-capture interface**[ *interface-type* *interface-number* [ **capture-filter** *capt-expression* \| **display-filter** *disp-expression* \| **limit-captured-frames** *limit* \| **limit-frame-size** *bytes* \| **autostop duration** *seconds* ] \* [ **raw** \| { **brief** \| **verbose** } ] \* ]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[interface** *interface-type interface-number*]：指定捕获报文的二层以太网接口/三层以太网接口。

**[capture-filter*** capt-expression*]：指定用来捕获报文的过滤规则，*capt-expression*为捕获过滤表达式。设备根据此参数指定的过滤规则对报文进行过滤并捕获匹配过滤规则的报文。捕获过滤语法规则请参见"网络管理和监控配置指导"中的"Packet Capture"。如果不指定此参数，则捕获该接口的所有入方向的报文。

**[display-filter*** disp-expression*]：指定用来显示报文的过滤规则。*disp-expression*为显示过滤表达式。设备对已捕获的报文匹配参数指定的显示过滤规则，并将匹配的报文内容进行显示。与捕获过滤不同的是，显示过滤支持报文内容过滤，捕获过滤语法规则请参见"网络管理和监控配置指导"中的"Packet Capture"。如果不指定此参数，则显示所有捕获到的报文信息。

**[limit-captured-frames*** limit*]：指定捕获报文的最大个数，*limit*为报文的最大个数，取值范围为0～2147483647。当达到捕获报文的最大个数时，则停止捕获报文，若指定报文最大个数为0，则表示没有限制。如果没有指定此参数，表示捕获报文的最大个数为10个。

**[limit-frame-size*** bytes*]：指定捕获报文的最大长度，*bytes*为报文的最大长度，取值范围为64～8000，单位为字节。当捕获到的报文超过此长度，会对报文进行截断。如果未指定本参数，表示能够捕获的报文的最大长度为8000字节。

**[autostop filesize** *kilobytes*]：指定存储报文文件大小，*kilobytes*为文件长度最大值，取值范围为1～65536，单位为千字节。当报文文件大小达到最大值时，捕获报文自动停止。如果没有指定本参数，表示对报文文件大小没有限制。

**[autostop** **duration** *seconds*]：指定捕获报文时长，*seconds*为时长最大值，取值范围为1～2147483647，单位为秒。当捕获报文时长达到最大值时，捕获报文自动停止。如果没有指定本参数，表示不对捕获报文的时长进行限制。

**[autostop** **files** *numbers*]：指定切换存储报文文件次数，*numbers*为文件切换次数最大值，取值范围为2～64。当指定本参数时，报文将被保存到文件名为扩展文件名的文件中，扩展文件名由**write**参数指定的文件名称、文件生成序号和写入时间组成，当切换到新文件时，新生成的扩展报文文件序号按序递增，例如，指定的文件名称为a.pcap，则扩展名称为a_00001_20140211034151.pcap，当达到切换写文件条件时，则将报文信息写入新生成a_00002_20140211034207.pcap文件中，依次类推。当切换文件次数达到最大值时，捕获报文自动停止。如果没有指定本参数，表示不对报文文件切换的次数进行限制。

**[capture-ring-buffer** **filesize** *kilobytes*]：指定切换存储报文文件大小，*kilobytes*为报文文件长度最大值，取值范围为1～65536，单位为千字节。当报文文件大小达到最大值时，切换到下一个文件来存储捕获报文。如果没有指定本参数，表示不以文件大小为限制切换报文文件。

**[capture-ring-buffer** **duration** *seconds*]：指定切换存储报文文件时长，*seconds*为时长最大值，取值范围为1～2147483647，单位为秒。当捕获报文时长达到最大值时，切换到下一个文件来存储捕获报文。如果没有本参数，表示不以时长为限制切换报文文件。

**[capture-ring-buffer** **files** *numbers*]：指定存储报文文件最大存在个数，*numbers*为报文文件个数最大值，取值范围为2～64；当指定本参数时，报文将被保存到文件名为扩展文件名的文件中，扩展文件名由**write**参数指定的文件名称、文件生成序号和写入时间组成，当切换到新文件时，新生成的扩展报文文件序号按序递增，例如，指定的文件名称为a.pcap，则扩展名称为a_00001_20140211034151.pcap，当达到切换写文件条件时，则将报文信息写入新生成a_00002_20140211034207.pcap文件中，依次类推。当文件个数达到最大个数时，删除捕获报文过程中生成的最老文件，将捕获的报文写入新生成的扩展文件中。如果没有指定本参数，表示报文文件的最大存在个数没有限制。

**[write*** filepath*]：指定保存捕获报文的文件完整路径，为1～64字符的字符串，区分大小写。文件名命名规则的详细介绍，请参见"基础配置指导"中的"文件系统管理"。只支持以pcap格式的文件保存报文信息，保存到用户指定位置。如果没有指定此参数，将不会保存捕获的报文。

**[raw**]**：**将报文内容以十六进制格式显示。如果不指定此参数则不将报文文件内容用十六进制格式显示。

**[verbose**]：显示捕获报文的详细信息。

**[brief**]：显示捕获报文的简要信息。

【使用指导】

·开启指定接口的报文捕获功能，设备会实时显示捕获报文的信息，如果用户希望停止捕获，直接输入Ctrl+C停止捕获报文。

·当指定**autostop files**参数或者**capture-ring-buffer** **files**参数时，如果同时指定**autostop filesize**参数，则**autostop filesize**参数为切换条件属性参数。

·当指定**autostop files**参数或者**capture-ring-buffer** **files**参数时，则需指定一个具有切换捕获报文存文件条件属性的参数。

·当同时指定**autostop filesize**和**capture-ring-buffer filesize**时，**autostop filesize**停止条件参数属性失效，**capture-ring-buffer filesize**的切换条件参数属性生效，且以后指定参数的*kilobytes*为切换条件。

·由于文件系统对文件个数有限制，所以保存捕获报文文件的最大个数同样会有限制，具体数目与设备使用的文件系统有关。当达到文件系统的最大个数时，将退出捕获。

·当不指定**raw**、**brief**和**verbose**中的任何一个参数时，指定**write**参数，显示捕获的报文个数；当不指定**raw**、**brief**、**verbose**和**write**中的任何一个参数时，显示报文的简要信息。

【举例】

\# 开启接口Gigabitehernet1/0/1报文捕获功能。

\<Sysname\> packet-capture interface Gigabitehernet1/0/1

【相关命令】

·**packet-capture read**

**Packet Capture \-- Packet Capture配置命令 \-- packet-capture read**

------------------------------------------------------------------------

**[packet-capture read**]命令用来开启解析并显示保存的数据包文件的功能。

【命令】

**[packet-capture read ***filepath *[ **verbose**   **display-filter** *disp-expression*  [ **raw** \| { **brief** \| **verbose** } ] \*]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[read*** filepath*]：指定读取的文件的完整路径，为1～64个字符的字符串，区分大小写。文件名命名规则的详细介绍，请参见"基础配置指导"中的"文件系统管理"。读取指定路径上的pcap或pcapng格式文件。

**[display-filter*** disp-expression*]：指定用来显示报文的过滤规则。*disp-expression*为显示报文的过滤规则。设备报文文件内容匹配参数指定的显示过滤规则，并将匹配的报文内容进行显示。显示过滤语法规则参见Packet Capture配置手册。如果不指定此参数，则显示报文文件所的报文信息。

**[raw**]：将报文文件内容用十六进制格式显示。如果不指定此参数，则不将报文文件内容用十六进制格式显示。

**[brief**]：显示报文文件的简要信息。

**[verbose**]：显示报文文件的详细信息。

【使用指导】

·开启解析并显示报文文件内容功能，Packet Capture终端显示从指定文件中读取解析的报文信息，如果用户希望退出此过程，可以直接输入Ctrl+C退出解析过程。

·Packet Capture支持解析pcap和pcapng格式的报文文件。

·未指定**raw**、**brief**、**verbose**参数时，则显示简要信息。

【举例】

\# 解析flash:/test目录下的报文文件**aaaa.pcap**。

\<Sysname\> packet-capture read flash:/test/aaaa.pcap

【相关命令】

·**packet-capture interface**
