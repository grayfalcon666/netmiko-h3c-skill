::: {#433753167 .myid}
[]{#_Toc404790950}[]{#struct_0_x6691_30153_180352295}

**RSVP \-- RSVP调试命令 \-- debugging rsvp all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_264780302}

[**[debugging rsvp all]{lang="EN-US"}**]{#struct_0_x6691_30153_x1633020653}

[**[undo debugging rsvp all]{lang="EN-US"}**]{#struct_0_x6691_30153_234770155}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x252859436}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_1465459531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_447030028}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_x759422995}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x234813093}

[**[debugging rsvp all]{lang="EN-US"}**]{#struct_0_x6691_30153_x699181127}[命令用来打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp authentication]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x21384952}[所有的调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_2004091744}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x1632561901}[打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp all]{lang="EN-US"}]{#struct_0_x6691_30153_x1394327695}
:::

::: {#24512083 .myid}
[]{#_Toc404790951}[]{#struct_0_x6691_30153_x1045754649}[]{#_Toc253298421}[]{#_Toc130718952}[]{#_Toc87257691}

**RSVP \-- RSVP调试命令 \-- debugging rsvp authentication**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x212157216}

[**[debugging rsvp authentication]{lang="EN-US"}**]{#struct_0_x6691_30153_x311277898}

[**[undo debugging rsvp authentication]{lang="EN-US"}**]{#struct_0_x6691_30153_x1907997043}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x134599679}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1211559244}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_1132128551}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1632627437}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_2065792052}

[**[debugging rsvp authentication]{lang="EN-US"}**]{#struct_0_x6691_30153_1070739557}[命令用来打开]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[认证调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp authentication]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[认证调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x1605756104}[认证调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x6691_30153_1276008522}[[表1-1 ]{lang="EN-US"}[debugging rsvp authentication]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_290856627}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x975597519}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_721045864}

[[Looking up SA for the incoming *message-type* message: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x184643697}

[[为接收的]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632692973}[报文查找认证关联：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Looking up SA for the outgoing *message-type* message: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_1486493374}

[[为发送的]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_x1795292592}[报文查找认证关联：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Created a receive mode SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x681981715}

[[创建接收认证关联：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x1946437144}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Created a send mode SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1947878958}

[[创建发送认证关联：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632758509}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Sent an integrity challenge message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1642422584}

[[发送]{style="font-family:宋体"}[integrity challenge]{lang="EN-US"}]{#struct_0_x6691_30153_x121043048}[消息]{style="font-family:宋体"}

[[Sent an integrity response message.]{lang="EN-US"}]{#struct_0_x6691_30153_x664969663}

[[发送]{style="font-family:宋体"}[integrity response]{lang="EN-US"}]{#struct_0_x6691_30153_1482682729}[消息]{style="font-family:宋体"}

[[Received an integrity challenge message, from *start-address* to *end-address.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1632299757}

[[收到]{style="font-family:宋体"}[integrity challenge]{lang="EN-US"}]{#struct_0_x6691_30153_106120276}[消息，起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Received an integrity response message, from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_2125217094}

[[收到]{style="font-family:宋体"}[integrity response]{lang="EN-US"}]{#struct_0_x6691_30153_1842000523}[消息，起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Challenge state is not in progress.]{lang="EN-US"}]{#struct_0_x6691_30153_1226916824}

[[Challenge]{lang="EN-US"}]{#struct_0_x6691_30153_1433880961}[状态不是正在协商]{style="font-family:宋体"}

[[Challenge object is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_x1632365293}

[[Challenge]{lang="EN-US"}]{#struct_0_x6691_30153_x754702162}[对象有效]{style="font-family:宋体"}

[[Challenge object is invalid.]{lang="EN-US"}]{#struct_0_x6691_30153_1267403127}

[[Challenge]{lang="EN-US"}]{#struct_0_x6691_30153_1605546267}[对象无效]{style="font-family:宋体"}

[[No integrity object.]{lang="EN-US"}]{#struct_0_x6691_30153_x1632824044}

[[没有]{style="font-family:宋体"}[integrity]{lang="EN-US"}]{#struct_0_x6691_30153_x1077672035}[对象]{style="font-family:宋体"}

[[No challenge object.]{lang="EN-US"}]{#struct_0_x6691_30153_1182511059}

[[没有]{style="font-family:宋体"}[challenge]{lang="EN-US"}]{#struct_0_x6691_30153_493742951}[对象]{style="font-family:宋体"}

[[Sequence *sequence* is out of the receiving window.]{lang="EN-US"}]{#struct_0_x6691_30153_1175662810}

[[序列号]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632889580}[超出接收窗口]{style="font-family:宋体"}

[[Replayed sequence *sequence*.]{lang="EN-US"}]{#struct_0_x6691_30153_105417270}

[[序列号]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x6691_30153_x2021311556}[重复]{style="font-family:宋体"}

[[Sequence *sequence* is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_x978644698}

[[序列号]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632955116}[有效]{style="font-family:宋体"}

[[MD5 digest is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_1569997051}

[[MD5]{lang="EN-US"}]{#struct_0_x6691_30153_x2096528668}[摘要有效]{style="font-family:宋体"}

[[MD5 digest is invalid.]{lang="EN-US"}]{#struct_0_x6691_30153_x1652870215}

[[MD5]{lang="EN-US"}]{#struct_0_x6691_30153_x1633020652}[摘要无效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1331313786}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x775743361}[在接口视图下配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证密钥，打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[认证调试信息开关，从接口接收到]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp authentication]{lang="EN-US"}]{#struct_0_x6691_30153_1357084478}

[\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; Looking up SA for the incoming path message: from 12.11.110.11 to 10.33.33.33.                              ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1678355798}*[为接收到的]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息查找认证关联，认证起点地址为]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; MD5 digest is valid.        ]{lang="EN-US"}]{#struct_0_x6691_30153_x1542414352}

[*[// Path]{lang="EN-US"}*]{#struct_0_x6691_30153_x1945449488}*[消息的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要有效。]{style="font-family:宋体"}*

[[\*Aug 19 08:33:11:934 2012 Sysname RSVP/7/AUTH: -MDC=1; Sequence 5778030575734489139 is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_x2140776673}

[*[// Path]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632561900}*[消息的序列号有效。]{style="font-family:宋体"}*

[[\*Aug 19 08:33:15:278 2012 Sysname RSVP/7/AUTH: -MDC=1; Looking up SA for the outgoing resv message: from 12.11.110.12 to 12.11.110.11.]{lang="EN-US"}]{#struct_0_x6691_30153_1334555660}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_284347755}*[为发送的]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息查找认证关联，认证起点地址为]{style="font-family:宋体"}[12.11.110.12]{lang="EN-US"}[，目的地址为]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:33:22:434 2012 Sysname RSVP/7/AUTH: -MDC=1; MD5 digest is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_x1904021297}

[*[// Resv]{lang="EN-US"}*]{#struct_0_x6691_30153_x216096441}*[消息的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要有效。]{style="font-family:宋体"}*

[[\*Aug 19 08:33:22:434 2012 Sysname RSVP/7/AUTH: -MDC=1; Sequence 5778030575734489140 is valid.]{lang="EN-US"}]{#struct_0_x6691_30153_x967656725}

[*[// Resv]{lang="EN-US"}*]{#struct_0_x6691_30153_478469414}*[消息的序列号有效。]{style="font-family:宋体"}*

::: {#-1825538218 .myid}
[]{#_Toc404790952}[]{#struct_0_x6691_30153_x2007353948}

**RSVP \-- RSVP调试命令 \-- debugging rsvp error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1632627436}

[**[debugging rsvp error]{lang="EN-US"}**]{#struct_0_x6691_30153_499708111}

[**[undo debugging rsvp error]{lang="EN-US"}**]{#struct_0_x6691_30153_138661648}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_86794350}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_1278444512}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_766314222}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_17113946}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1230518313}

[**[debugging rsvp error]{lang="EN-US"}**]{#struct_0_x6691_30153_x1692059406}[命令用来打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x1632692972}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging rsvp error]{lang="EN-US"}]{#struct_0_x6691_30153_x1242389981}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_285846388}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_757299163}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_845195211}

[[Failed to receive a packet from socket (*socket-fd*).]{lang="EN-US"}]{#struct_0_x6691_30153_1493587594}

[[从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x6691_30153_915131566}[（]{style="font-family:宋体"}*[socket-fd]{lang="EN-US"}*[）接收报文错误]{style="font-family:宋体"}

[[IP TTL expired.]{lang="EN-US"}]{#struct_0_x6691_30153_x379061197}

[[IP TTL]{lang="EN-US"}]{#struct_0_x6691_30153_x1632758508}[超时]{style="font-family:宋体"}

[[RSVP TTL expired.]{lang="EN-US"}]{#struct_0_x6691_30153_x76338643}

[[RSVP TTL]{lang="EN-US"}]{#struct_0_x6691_30153_x1006379871}[超时]{style="font-family:宋体"}

[[Invalid RSVP message type: *message-type*.]{lang="EN-US"}]{#struct_0_x6691_30153_1414550057}

[[无效的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_1015153791}[报文类型]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*

[[Invalid RSVP message length: *length*.]{lang="EN-US"}]{#struct_0_x6691_30153_1279108910}

[[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x1632299756}[报文长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[错误]{style="font-family:宋体"}

[[Invalid RSVP message checksum: *checksum*.]{lang="EN-US"}]{#struct_0_x6691_30153_1672204217}

[[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x1836120139}[报文校验和]{style="font-family:宋体"}*[checksum]{lang="EN-US"}*[错误]{style="font-family:宋体"}

[[Failed to decode object (class number *class-number*) in the *message-type* message.]{lang="EN-US"}]{#struct_0_x6691_30153_x176098285}

[[解码]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_507731131}[报文中类型值为]{style="font-family:宋体"}*[class-number]{lang="EN-US"}*[的对象失败]{style="font-family:宋体"}

[[Failed to decode the *message-type* message.]{lang="EN-US"}]{#struct_0_x6691_30153_342994828}

[[解码]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_x1632365292}[报文失败]{style="font-family:宋体"}

[[Failed to encode *object-type* object in the *message-type* message.]{lang="EN-US"}]{#struct_0_x6691_30153_1974181193}

[[编码]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_359776326}[报文的]{style="font-family:宋体"}*[object-type]{lang="EN-US"}*[对象失败]{style="font-family:宋体"}

[[Failed to encode the *message-type* message.]{lang="EN-US"}]{#struct_0_x6691_30153_140636802}

[[编码]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_329828583}[报文失败]{style="font-family:宋体"}

[[Failed to set socket (*socket-fd*) option.]{lang="EN-US"}]{#struct_0_x6691_30153_746185946}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x6691_30153_721750803}[（]{style="font-family:宋体"}*[socket-fd]{lang="EN-US"}*[）选项失败]{style="font-family:宋体"}

[[Failed to send packet to socket (*socket-fd*), error code *error-code*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1738764329}

[[向]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x6691_30153_x459483318}[（]{style="font-family:宋体"}*[socket-fd]{lang="EN-US"}*[）发送报文失败，错误值为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Memory alert (*alert-state*).]{lang="EN-US"}]{#struct_0_x6691_30153_746251482}

[[内存门限告警，]{style="font-family:宋体"}*[alert-state]{lang="EN-US"}*]{#struct_0_x6691_30153_x614855663}[代表内存不足的严重程度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[代表内存状态正常，值越大内存不足越严重]{style="font-family:宋体"}

[[Different service IDs in Tspec: *service-ID1 service-ID2.*]{lang="EN-US"}]{#struct_0_x6691_30153_851456239}

[[Tspec]{lang="EN-US"}]{#struct_0_x6691_30153_1602172203}[中服务]{style="font-family:宋体"}[ID]{lang="EN-US"}[不一致，分别为]{style="font-family:宋体"}*[service-ID1]{lang="EN-US"}*[和]{style="font-family:宋体"}*[service-ID2]{lang="EN-US"}*

[[Invalid service ID *service-ID* in Tspec.]{lang="EN-US"}]{#struct_0_x6691_30153_746317018}

[[Tspec]{lang="EN-US"}]{#struct_0_x6691_30153_1333541423}[中服务]{style="font-family:宋体"}[ID]{lang="EN-US"}[（]{style="font-family:宋体"}*[service-ID]{lang="EN-US"}*[）无效]{style="font-family:宋体"}

[[Failed to send HA message.]{lang="EN-US"}]{#struct_0_x6691_30153_x779903013}

[[发送]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x6691_30153_x106924163}[消息失败]{style="font-family:宋体"}

[[RSVP is not enabled on interface *interface*]{lang="EN-US"}]{#struct_0_x6691_30153_x939921298}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_x6691_30153_605580902}[未使能]{style="font-family:宋体"}[RSVP]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_421905453}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_2013840013}[打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[错误调试信息开关，收到]{style="font-family:宋体"}[IP TTL]{lang="EN-US"}[超时的]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp error]{lang="EN-US"}]{#struct_0_x6691_30153_746382554}

[\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; IP TTL expired.]{lang="EN-US"}

[*[// RSVP]{lang="EN-US"}*]{#struct_0_x6691_30153_x1448050087}*[消息的]{style="font-family:宋体"}[IP TTL]{lang="EN-US"}[超时。]{style="font-family:宋体"}*

::: {#2008648793 .myid}
[]{#_Toc404790953}[]{#struct_0_x6691_30153_1172341835}

**RSVP \-- RSVP调试命令 \-- debugging rsvp frr**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x2572142}

[**[debugging rsvp frr]{lang="EN-US"}**]{#struct_0_x6691_30153_x1333444258}

[**[undo debugging rsvp frr]{lang="EN-US"}**]{#struct_0_x6691_30153_x300991887}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_279537258}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_1239245402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_986173014}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_745923802}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1850232797}

[**[debugging rsvp frr]{lang="EN-US"}**]{#struct_0_x6691_30153_x1255603101}[命令用来打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[快速重路由调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp frr]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[快速重路由调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_512857697}[快速重路由调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging rsvp frr]{lang="EN-US"}]{#struct_0_x6691_30153_x1235535346}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_318103380}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1881287408}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_x849641036}

[[TC updated bypass *tunnel-name* info, backup bandwidth *bandwidth*, protection CT *class-type*.]{lang="EN-US"}]{#struct_0_x6691_30153_x2259416}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_745989338}[更新旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[信息，保护带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，保护带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[.]{lang="EN-US"}

[[TC deleted bypass *tunnel-name* info.]{lang="EN-US"}]{#struct_0_x6691_30153_522497722}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_743484728}[删除旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[信息]{style="font-family:宋体"}

[[Bound bypass *tunnel-name* to CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_752721604}

[[旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_x903794459}[绑定]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}*[direction]{lang="EN-US"}*]{#struct_0_x6691_30153_x393952274}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x6691_30153_x1825555121}[：表示单向隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x6691_30153_746054874}[：表示双向隧道的正向]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x6691_30153_x836987697}[：表示双向隧道的反向]{style="font-family:宋体"}[CRLSP]{lang="EN-US"}

[[Unbound bypass *tunnel-name* from CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_x952335056}

[[旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_x5723354}[取消绑定]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Got bypass *tunnel-name* info from TC: backup bandwidth *bandwidth*, protection CT *class-type*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1406041710}

[[从]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x6691_30153_746120410}[获取旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[信息：保护带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，保护带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[.]{lang="EN-US"}

[[Failed to get bypass *tunnel-name* info from TC.]{lang="EN-US"}]{#struct_0_x6691_30153_x910095248}

[[从]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x6691_30153_277360518}[获取旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*[信息失败]{style="font-family:宋体"}

[[Updated the used bandwidth of bypass *tunnel-name* from *bandwidth1* to *bandwidth2*.]{lang="EN-US"}]{#struct_0_x6691_30153_1875216016}

[[旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_926216426}[的已用带宽从]{style="font-family:宋体"}*[bandwidth1]{lang="EN-US"}*[更新为]{style="font-family:宋体"}*[bandwidth2]{lang="EN-US"}*

[[Looking up bypass tunnel for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_746710234}

[[为]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_x1651891367}[查找旁路隧道，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[The unused bandwidth *bandwidth* of bypass *tunnel-name* is insufficient for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_826593246}

[[旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_1715230648}[的未用带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，带宽不足以保护]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Optimizing bypass tunnel for all CR-LSPs.]{lang="EN-US"}]{#struct_0_x6691_30153_x1718024854}

[[正在为所有]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_x154922650}[优化旁路隧道]{style="font-family:宋体"}

[[Finished smoothing FRR configurations.]{lang="EN-US"}]{#struct_0_x6691_30153_746775770}

[[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_x1646237250}[配置平滑结束]{style="font-family:宋体"}

[[Reset bypass *tunnel-name* info.]{lang="EN-US"}]{#struct_0_x6691_30153_x38925914}

[[重置旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_x415951865}[信息]{style="font-family:宋体"}

[[Set staled flag to the bypass *tunnel-name.*]{lang="EN-US"}]{#struct_0_x6691_30153_746185947}

[[设置旁路隧道]{style="font-family:宋体"}*[tunnel-name]{lang="EN-US"}*]{#struct_0_x6691_30153_721750802}[的老化标记]{style="font-family:宋体"}

[[TC disconnected.]{lang="EN-US"}]{#struct_0_x6691_30153_x1738764330}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_750304727}[和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的连接断开]{style="font-family:宋体"}

[[Finished smoothing all CR-LSPs.]{lang="EN-US"}]{#struct_0_x6691_30153_x769038281}

[[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_746251483}[平滑结束]{style="font-family:宋体"}

[[Created CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_x614855662}

[[创建]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_851390703}[，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Deleted CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction.*]{lang="EN-US"}]{#struct_0_x6691_30153_x254176142}

[[删除]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_746317019}[，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[No tunnel available to protect CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_x851493470}

[[没有可用的]{style="font-family:宋体"}[Bypass]{lang="EN-US"}]{#struct_0_x6691_30153_x851427934}[隧道保护主]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，主]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Tunnel *bypass-tunnel-id* is the best bypass tunnel for CR-LSP (dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*).]{lang="EN-US"}]{#struct_0_x6691_30153_x26099123}

[[旁路隧道]{style="font-family:宋体"}*[bypass-tunnel-id]{lang="EN-US"}*]{#struct_0_x6691_30153_x851362398}[是可以保护主]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的最佳隧道，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Received FRR configurations on an interface from TC: ]{lang="EN-US"}]{#struct_0_x6691_30153_x1657206533}

[[interface index: *if-index*; Bypass number: *bypass-number*;]{lang="EN-US"}]{#struct_0_x6691_30153_x851296862}

[[Bypass tunnel ID: *tunnel-id1*, *tunnel-id2*, *tunnel-id3*;]{lang="EN-US"}]{#struct_0_x6691_30153_774321727}

[[Auto backup flag: *auto-backup-flag*.]{lang="EN-US"}]{#struct_0_x6691_30153_x851231326}

[[从]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x6691_30153_1085242698}[获取接口]{style="font-family:宋体"}[FRR]{lang="EN-US"}[的配置信息：接口索引为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*[；旁路隧道数目为]{style="font-family:宋体"}*[bypass-number]{lang="EN-US"}*[；旁路隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[为：]{style="font-family:宋体"}*[ tunnel-id1]{lang="EN-US"}*[，]{style="font-family:宋体"}*[tunnel-id2]{lang="EN-US"}*[，]{style="font-family:宋体"}*[tunnel-id3]{lang="EN-US"}*[；自动备份隧道标记为]{style="font-family:宋体"}*[auto-backup-flag]{lang="EN-US"}*

[[Updated CR-LSP: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_x851165790}

[[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_x2018071816}[处理]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[更新，]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[TC updated FRR configurations. FRR reoptimization time *reoptimize time*; auto backup *auto backup enable flag*; auto backup nexthop only *nexthop only flag*; auto backup removal time *remove time*; auto backup max tunnel number *max-tnlid*; auto backup min tunnel number *min-tnlid*.]{lang="EN-US"}]{#struct_0_x6691_30153_x2066153497}

[[收到]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_x6691_30153_x965814602}[处的]{style="font-family:宋体"}[FRR]{lang="EN-US"}[配置，优化定时器时间为]{style="font-family:宋体"}*[reoptimize time]{lang="EN-US"}*[；]{style="font-family:宋体"}[AUTOFRR]{lang="EN-US"}[使能标记为]{style="font-family:宋体"}*[auto backup enable flag]{lang="EN-US"}*[；下一跳的使能标记为]{style="font-family:宋体"}*[nexthop only flag]{lang="EN-US"}*[；删除定时器时间为]{style="font-family:宋体"}*[removal time]{lang="EN-US"}*[；自动隧道最大值为]{style="font-family:宋体"}*[max-tnlid]{lang="EN-US"}*[；自动隧道最小值为]{style="font-family:宋体"}*[min-tnlid]{lang="EN-US"}*[.]{lang="EN-US"}

[[Finished smoothing auto FRR configurations, protected path tables, and automatic bypass tunnels.]{lang="EN-US"}]{#struct_0_x6691_30153_x2065432601}

[[auto FRR]{lang="EN-US"}]{#struct_0_x6691_30153_x1153909445}[配置平滑，被保护路径表平滑和自动备份隧道信息平滑结束]{style="font-family:宋体"}

[[Finished smoothing all tunnels with process tunnel.]{lang="EN-US"}]{#struct_0_x6691_30153_x2065498137}

[[与]{style="font-family:宋体"}[tunnel]{lang="EN-US"}]{#struct_0_x6691_30153_x419999386}[进程的隧道平滑结束]{style="font-family:宋体"}

[[Tunnel disconnected.]{lang="EN-US"}]{#struct_0_x6691_30153_x499872945}

[[Tunnel]{lang="EN-US"}]{#struct_0_x6691_30153_x1051771537}[进程和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[进程断开连接]{style="font-family:宋体"}

[[Created an auto backup removal timer for the protected path. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;*  protected type *prot-type*; auto tunnel number *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x499938481}

[[为被保护路径表创建]{style="font-family:宋体"}[removal]{lang="EN-US"}]{#struct_0_x6691_30153_x209485382}[定时器。接口为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[，保护的地址为]{style="font-family:宋体"}*[prot-addr]{lang="EN-US"}*[，保护类型为]{style="font-family:宋体"}*[prot-type]{lang="EN-US"}*[，自动隧道编号为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[.]{lang="EN-US"}

[[Deleted the auto backup removal timer for the protected path. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;*  protected type *prot-type*; auto tunnel number *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x499741873}

[[删除被保护路径表]{style="font-family:宋体"}[removal]{lang="EN-US"}]{#struct_0_x6691_30153_x499807409}[定时器。接口为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[，保护的地址为]{style="font-family:宋体"}*[prot-addr]{lang="EN-US"}*[，保护类型为]{style="font-family:宋体"}*[prot-type]{lang="EN-US"}*[，自动隧道编号为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Auto backup removal timer for the protected path expired. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr;* protected type *prot-type*; auto tunnel number *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1412588732}

[[被保护路径表的删除定时器超时。接口为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*]{#struct_0_x6691_30153_x500135089}[，目的地址为]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[，保护的地址为]{style="font-family:宋体"}*[prot-addr]{lang="EN-US"}*[，保护类型为]{style="font-family:宋体"}*[prot-type]{lang="EN-US"}*[，自动隧道编号为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[.]{lang="EN-US"}

[[Begin to recreate automatic bypass tunnels.]{lang="EN-US"}]{#struct_0_x6691_30153_x282773539}

[[开始重新创建自动旁路隧道]{style="font-family:宋体"}]{#struct_0_x6691_30153_x500200625}

[[Reference count of the protected path updated to *ref-counter*. Interface index *if-index*; destination address *dest-addr*; protected address *prot-addr*; protected type *prot-type*.]{lang="EN-US"}]{#struct_0_x6691_30153_2107044029}

[[被保护路径表更新引用计数到]{style="font-family:宋体"}*[ref-counter]{lang="EN-US"}*]{#struct_0_x6691_30153_x500004017}*[，]{style="font-family:宋体"}*[被保护接口为]{style="font-family:宋体"}*[if-index]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[，被保护地址为]{style="font-family:宋体"}*[prot-addr]{lang="EN-US"}*[，保护类型为]{style="font-family:宋体"}*[prot-type]{lang="EN-US"}*

[[Finished smoothing all tunnel interfaces with process IF.]{lang="EN-US"}]{#struct_0_x6691_30153_1284555498}

[[与]{style="font-family:宋体"}[IF]{lang="EN-US"}]{#struct_0_x6691_30153_x500069553}[进程的隧道接口信息平滑结束]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_1333541424}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x780361765}[打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[快速重路由调试信息开关。关闭]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[隧道模式的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp frr]{lang="EN-US"}]{#struct_0_x6691_30153_746382555}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] display this]{lang="EN-US"}

[\#]{lang="EN-US"}

[interface Tunnel1 mode mpls-te]{lang="EN-US"}

[ mpls te backup bandwidth 1000]{lang="EN-US"}

[ destination 10.33.33.33]{lang="EN-US"}

[\#]{lang="EN-US"}

[return]{lang="EN-US"}

[\[Sysname-Tunnel1\] shutdown]{lang="EN-US"}

[\[Sysname-Tunnel1\]]{lang="EN-US"}

[\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; TC deleted bypass tunnel1 info.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1448050088}*[删除旁路隧道]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*

[[\*Aug 19 08:45:40:847 2012 Sysname RSVP/7/FRR: -MDC=1; Deleted CR-LSP: dst 10.33.33.33, src 10.22.22.22, tunnel ID 1, LSP ID 51011, direction 0.]{lang="EN-US"}]{#struct_0_x6691_30153_x2006880214}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_508759103}*[删除]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，该]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.22.22.22]{lang="EN-US"}[，隧道的]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[51011]{lang="EN-US"}[，该隧道为单向隧道。]{style="font-family:宋体"}*

[[\[Sysname-Tunnel1\] undo shutdown]{lang="EN-US"}]{#struct_0_x6691_30153_2011749229}

[\[Sysname-Tunnel1\]]{lang="EN-US"}

[\*Aug 19 08:45:44:148 2012 Sysname RSVP/7/FRR: -MDC=1; Created CR-LSP: dst 10.33.33.33, src 10.22.22.22, tunnel ID 1, LSP ID 51012, direction 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x455989052}*[创建]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，该]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[的目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.22.22.22]{lang="EN-US"}[，隧道的]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[51011]{lang="EN-US"}[，该隧道为单向隧道。]{style="font-family:宋体"}*

[[\*Aug 19 08:45:44:148 2012 Sysname RSVP/7/FRR: -MDC=1; TC updated bypass tunnel1 info, backup bandwidth 1000kbps, protection CT 4.]{lang="EN-US"}]{#struct_0_x6691_30153_x1168432344}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x454534991}*[更新旁路隧道]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的信息，保护带宽为]{style="font-family:宋体"}[1000kbps]{lang="EN-US"}[，保护带宽类型为]{style="font-family:宋体"}[CT 4]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\[Sysname-Tunnel1\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x6691_30153_745923803}

[\[Sysname-GigabitEthernet1/0/1\] rsvp fast-reroute bypass-tunnel tunnel1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[\*Aug 19 08:45:52:706 2012 Sysname RSVP/7/FRR: -MDC=1; Got bypass tunnel1 info from TC: backup bandwidth 1000kbps, protection CT 4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1850232798}*[从]{style="font-family:宋体"}[TC]{lang="EN-US"}[获取旁路隧道的信息，保护带宽为]{style="font-family:宋体"}[1000kbps]{lang="EN-US"}[，保护带宽类型为]{style="font-family:宋体"}[CT 4]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1288965152 .myid}
[]{#_Toc404790954}[]{#struct_0_x6691_30153_x2015117988}

**RSVP \-- RSVP调试命令 \-- debugging rsvp hello**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1042451952}

[**[debugging rsvp hello]{lang="EN-US"}**]{#struct_0_x6691_30153_951124825}

[**[undo debugging rsvp hello]{lang="EN-US"}**]{#struct_0_x6691_30153_1791346635}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x64077310}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1916560171}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x821291192}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_745989339}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_522497721}

[**[debugging rsvp hello]{lang="EN-US"}**]{#struct_0_x6691_30153_743484731}[命令用来打开]{style="font-family:宋体"}[RSVP Hello]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp hello]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP Hello]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP Hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1203593525}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging rsvp hello]{lang="EN-US"}]{#struct_0_x6691_30153_x74789081}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_314394610}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_1380585938}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1086669355}

[[Handling GR ASM, interface *interface*, peer *peer-addr*, GR state *state*, GR event *event*.]{lang="EN-US"}]{#struct_0_x6691_30153_665413569}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_746054875}[状态处理，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，邻居地址为]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，]{style="font-family:宋体"}[GR]{lang="EN-US"}[事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[GR state changed from invalid to ready.]{lang="EN-US"}]{#struct_0_x6691_30153_x836987696}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x952269520}[状态由]{style="font-family:宋体"}[invalid]{lang="EN-US"}[变更为]{style="font-family:宋体"}[ready]{lang="EN-US"}

[[GR state changed from ready to invalid.]{lang="EN-US"}]{#struct_0_x6691_30153_x55696862}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_2015008711}[状态由]{style="font-family:宋体"}[ready]{lang="EN-US"}[变更为]{style="font-family:宋体"}[invalid]{lang="EN-US"}

[[GR state changed from ready to restart.]{lang="EN-US"}]{#struct_0_x6691_30153_1242602877}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_746120411}[状态由]{style="font-family:宋体"}[ready]{lang="EN-US"}[变更为]{style="font-family:宋体"}[restart]{lang="EN-US"}

[[GR state changed from restart to recovery.]{lang="EN-US"}]{#struct_0_x6691_30153_x910095249}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_277294982}[状态由]{style="font-family:宋体"}[restart]{lang="EN-US"}[变更为]{style="font-family:宋体"}[recovery]{lang="EN-US"}

[[GR state changed from restart to invalid.]{lang="EN-US"}]{#struct_0_x6691_30153_x789967417}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1926323426}[状态由]{style="font-family:宋体"}[restart]{lang="EN-US"}[变更为]{style="font-family:宋体"}[invalid]{lang="EN-US"}

[[GR state changed from recovery to invalid.]{lang="EN-US"}]{#struct_0_x6691_30153_746710235}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1651891366}[状态由]{style="font-family:宋体"}[recovery]{lang="EN-US"}[变更为]{style="font-family:宋体"}[invalid]{lang="EN-US"}

[[GR state changed from recovery to restart.]{lang="EN-US"}]{#struct_0_x6691_30153_x739490695}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_1652417179}[状态由]{style="font-family:宋体"}[recovery]{lang="EN-US"}[变更为]{style="font-family:宋体"}[restart]{lang="EN-US"}

[[Sent a hello request message, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_448328782}

[[发送]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_822001796}[请求消息，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Replied a hello ACK message, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_746775771}

[[回应]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1646237249}[应答消息，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Handling hello ASM, interface *interface*, peer  *peer-addr*, hello state *state,* hello event *event.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1961305751}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1861016242}[状态处理，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，邻居地址为]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[hello]{lang="EN-US"}[状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，]{style="font-family:宋体"}[hello]{lang="EN-US"}[事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Hello state changed from idle to init.]{lang="EN-US"}]{#struct_0_x6691_30153_746185944}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_721750805}[状态从]{style="font-family:宋体"}[idle]{lang="EN-US"}[变更为]{style="font-family:宋体"}[init]{lang="EN-US"}

[[Hello state changed from init to up.]{lang="EN-US"}]{#struct_0_x6691_30153_x1738764327}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_347085736}[状态从]{style="font-family:宋体"}[init]{lang="EN-US"}[变更为]{style="font-family:宋体"}[up]{lang="EN-US"}

[[Hello state changed from init to idle.]{lang="EN-US"}]{#struct_0_x6691_30153_x1945406946}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_746251480}[状态从]{style="font-family:宋体"}[init]{lang="EN-US"}[变更为]{style="font-family:宋体"}[idle]{lang="EN-US"}

[[Hello state changed from up to idle.]{lang="EN-US"}]{#struct_0_x6691_30153_x614855665}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_851849455}[状态从]{style="font-family:宋体"}[up]{lang="EN-US"}[变更为]{style="font-family:宋体"}[idle]{lang="EN-US"}

[[Hello state changed from up to init.]{lang="EN-US"}]{#struct_0_x6691_30153_1246687408}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_746317016}[状态从]{style="font-family:宋体"}[up]{lang="EN-US"}[变更为]{style="font-family:宋体"}[init]{lang="EN-US"}

[[The peer *peer-addr* was lost. Hello state changed from up to init.]{lang="EN-US"}]{#struct_0_x6691_30153_1333541413}

[[邻居]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_x779903010}[丢失，]{style="font-family:宋体"}[hello]{lang="EN-US"}[状态从]{style="font-family:宋体"}[up]{lang="EN-US"}[变更为]{style="font-family:宋体"}[init]{lang="EN-US"}

[[The peer\'s hello function was disabled. Hello state changed from up to init.]{lang="EN-US"}]{#struct_0_x6691_30153_x107120771}

[[邻居关闭]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_746382552}[功能，]{style="font-family:宋体"}[hello]{lang="EN-US"}[状态从]{style="font-family:宋体"}[up]{lang="EN-US"}[变更为]{style="font-family:宋体"}[init]{lang="EN-US"}

[[Received a hello message in idle state.]{lang="EN-US"}]{#struct_0_x6691_30153_x1448050093}

[[在]{style="font-family:宋体"}[idle]{lang="EN-US"}]{#struct_0_x6691_30153_x796961097}[状态收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a hello request message in init state, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_729592309}

[[在]{style="font-family:宋体"}[init]{lang="EN-US"}]{#struct_0_x6691_30153_745923800}[状态收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[请求报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src- instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Receive a hello ACK message in init state, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1850232799}

[[在]{style="font-family:宋体"}[init]{lang="EN-US"}]{#struct_0_x6691_30153_x449034047}[状态收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[应答报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Received a hello request message in up state, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_745989336}

[[在]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x6691_30153_522497732}[状态收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[请求报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Received a hello ACK message in up state, src instance *src-instance*, dst instance *dst-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1212830408}

[[在]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x6691_30153_1047479932}[状态收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[应答报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*

[[Hello src instance *src-instance* is different from old src instance *old-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_746054872}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_x836987699}[报文中的]{style="font-family:宋体"}[src instance]{lang="EN-US"}[（]{style="font-family:宋体"}*[src-instance]{lang="EN-US"}*[）与原来的]{style="font-family:宋体"}[src instance]{lang="EN-US"}[（]{style="font-family:宋体"}*[old-instance]{lang="EN-US"}*[）不一致]{style="font-family:宋体"}

[[Hello dst instance *dst-instance* is different from old dst instance *old-instance*.]{lang="EN-US"}]{#struct_0_x6691_30153_x952990416}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_746120408}[报文中的]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[（]{style="font-family:宋体"}*[dst-instance]{lang="EN-US"}*[）与原来的]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[（]{style="font-family:宋体"}*[old-instance]{lang="EN-US"}*[）不一致]{style="font-family:宋体"}

[[Received more than *max-num* erroneous hello messages.]{lang="EN-US"}]{#struct_0_x6691_30153_1428556920}

[[接收错误的]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1294972411}[报文数大于]{style="font-family:宋体"}*[max-num]{lang="EN-US"}*

[[Received an incorrect hello message. Src instance is 0.]{lang="EN-US"}]{#struct_0_x6691_30153_746710232}

[[接收错误的]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1651891361}[报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Received an incorrect hello message. Src instance is different.]{lang="EN-US"}]{#struct_0_x6691_30153_1989392660}

[[接收错误的]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_746775768}[报文，]{style="font-family:宋体"}[src instance]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Received an incorrect hello message. Dst instance is different.]{lang="EN-US"}]{#struct_0_x6691_30153_692414902}

[[接收错误的]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1221906581}[报文，]{style="font-family:宋体"}[dst instance]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Sent *message-type* message to BFD, interface *interface*, src address *src-address*, dst address *dst-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_746185945}

[[发送]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x6691_30153_721750804}[消息给]{style="font-family:宋体"}[BFD]{lang="EN-US"}[，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[src-address]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[dst-address]{lang="EN-US"}*

[[Received BFD down message, interface *interface*, peer *peer-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1738764328}

[[收到]{style="font-family:宋体"}[BFD down]{lang="EN-US"}]{#struct_0_x6691_30153_746251481}[消息，接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，邻居地址为]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x614855664}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_851783919}[在接口视图下配置]{style="font-family:宋体"}[RSVP Hello]{lang="EN-US"}[扩展功能后，打开]{style="font-family:宋体"}[RSVP Hello]{lang="EN-US"}[调试信息开关，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp hello]{lang="EN-US"}]{#struct_0_x6691_30153_1433292777}

[\*Aug 19 08:35:12:478 2012 Sysname RSVP/7/HELLO: -MDC=1; Sent a hello request message, src instance 728, dst instance 727.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_430112404}*[发送]{style="font-family:宋体"}[Hello request]{lang="EN-US"}[消息，]{style="font-family:宋体"}[source instance]{lang="EN-US"}[为]{style="font-family:宋体"}[728]{lang="EN-US"}[，]{style="font-family:宋体"}[destination instance]{lang="EN-US"}[为]{style="font-family:宋体"}[727]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Handling hello ASM, interface GE1/0/1, peer 12.11.110.11, hello state up, hello event received message.]{lang="EN-US"}]{#struct_0_x6691_30153_x2090802962}

[*[// Hello]{lang="EN-US"}*]{#struct_0_x6691_30153_x331118884}*[状态处理，接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，邻居地址为]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[，]{style="font-family:宋体"}[hello]{lang="EN-US"}[状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[，]{style="font-family:宋体"}[hello]{lang="EN-US"}[事件为接收到消息]{style="font-family:宋体"}*

[[\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Received a hello ACK message in up state, src instance 727, dst instance 728.]{lang="EN-US"}]{#struct_0_x6691_30153_x272070944}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_839778711}*[在]{style="font-family:宋体"}[up]{lang="EN-US"}[状态接收到]{style="font-family:宋体"}[Hello ACK]{lang="EN-US"}[消息，]{style="font-family:宋体"}[source instance]{lang="EN-US"}[为]{style="font-family:宋体"}[727]{lang="EN-US"}[，]{style="font-family:宋体"}[destination instance]{lang="EN-US"}[为]{style="font-family:宋体"}[728]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:35:12:479 2012 Sysname RSVP/7/HELLO: -MDC=1; Handling GR ASM, interface GE1/0/1, peer 12.11.110.11, GR state invalid, GR event without object.]{lang="EN-US"}]{#struct_0_x6691_30153_746317017}

[*[// GR]{lang="EN-US"}*]{#struct_0_x6691_30153_1333541414}*[状态处理，接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，邻居地址为]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[，]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态为]{style="font-family:宋体"}[invalid]{lang="EN-US"}[，]{style="font-family:宋体"}[GR]{lang="EN-US"}[事件为不存在对象]{style="font-family:宋体"}*

::: {#1358900568 .myid}
[]{#_Toc404790955}[]{#struct_0_x6691_30153_x780361762}

**RSVP \-- RSVP调试命令 \-- debugging rsvp packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_976927037}

[**[debugging rsvp packet]{lang="EN-US"}**]{#struct_0_x6691_30153_x1819577960}

[**[undo debugging rsvp packet]{lang="EN-US"}**]{#struct_0_x6691_30153_x1925547142}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x422131442}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_1112241516}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x347434805}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_746382553}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1448050094}

[**[debugging rsvp packet]{lang="EN-US"}**]{#struct_0_x6691_30153_x393676570}[命令用来打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x696184930}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging rsvp packet]{lang="EN-US"}]{#struct_0_x6691_30153_x1790773234}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_304582140}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x475635679}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_1683579027}

[[Received a packet from socket *socket-fd*, length *length*, content: *content*.]{lang="EN-US"}]{#struct_0_x6691_30153_720914067}

[[从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x6691_30153_745923801}[（]{style="font-family:宋体"}*[socket-fd]{lang="EN-US"}*[）接收到报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，内容为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[[Sent a packet to socket *socket-fd*, length *length*, content: *content*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1850232800}

[[向]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x6691_30153_x1658428881}[（]{style="font-family:宋体"}*[socket-fd]{lang="EN-US"}*[）发送报文，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，内容为]{style="font-family:宋体"}*[content]{lang="EN-US"}*

[[Received *message-type* message from interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x21838739}

[[从接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_x6691_30153_x1907996960}[收到]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[消息]{style="font-family:宋体"}

[[Sent *message-type* message to interface *interface*, nexthop *nexthop-addr*, result *result*.]{lang="EN-US"}]{#struct_0_x6691_30153_1565505391}

[[向接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_x6691_30153_745989337}[发送]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[消息，下一跳地址为]{style="font-family:宋体"}*[nexthop-addr]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result  ]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}[result]{lang="EN-US"}]{#struct_0_x6691_30153_727170694}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[uccessful]{lang="EN-US"}]{#struct_0_x6691_30153_727236230}[：发送]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[消息]{lang="EN-US" style="font-family:宋体"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x6691_30153_x382073770}[：]{lang="EN-US" style="font-family:宋体"}[发送]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[消息失败]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_522497731}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x1212830405}[打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文调试信息开关，收到]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp packet]{lang="EN-US"}]{#struct_0_x6691_30153_x2131742117}

[\*Aug 19 08:37:47:978 2012 Sysname RSVP/7/PKT: -MDC=1; Sent a packet to socket 41, length 164, content: 45 C0 A4 00 00 00 00 00 FF 2E 9C F8 0C 0B 6E 0C 0C 0B 6E 0B 10 02 00 00 FF 00 00 90 00 24 04 01 01 00 00 01 02 00 00 00 50 30 A4 AC 00 00 00 38 0E EE AA E5 A9 AD 67 71 68 A8 AF A0 BD 8A 4E 91 00 10 01 07 0A 21 21 21 00 00 00 01 0A 0B 0B 0B 00 0C 03 01 0C 0B 6E 0C 00 00 00 02 00 08 05 01 00 00 27 10 00 08 08 01 00 00 00 12 00 24 09 02 00 00 00 07 05 00 00 06 7F 00 00 05 00 00 00 00 44 7A 00 00 00 00 00 00 00 00 00 00 00 00 05 DC 00 0C 0A 07 0A 0B 0B 0B 00 00 47 24 00 08 10 01 00 00 04 7B .]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x590076823}*[向]{style="font-family:宋体"}[socket 41]{lang="EN-US"}[发送]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[164]{lang="EN-US"}[字节，报文内容以十六进制形式打印。]{style="font-family:宋体"}*

[[\*Aug 19 08:37:47:978 2012 Sysname RSVP/7/PKT: -MDC=1; Sent resv message to interface GE1/0/1, nexthop 12.11.110.11, result s]{lang="EN-US"}]{#struct_0_x6691_30153_x1837625736}[uccessful]{lang="EN-US"}[.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x622659939}*[成功向接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Resv]{lang="EN-US"}[报文，下一跳地址为]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:37:51:278 2012 Sysname RSVP/7/PKT: -MDC=1; Sent a packet to socket 41, length 188, content: 46 C0 BC 00 00 00 00 00 FD 2E FF FF 0A 0B 0B 0B 0A 21 21 21 94 04 00 00 10 01 5B 0F FD 00 00 A4 00 10 01 07 0A 21 21 21 00 00 00 01 0A 0B 0B 0B 00 0C 03 01 17 0B 6E 0B 00 00 00 04 00 08 05 01 00 00 27 10 00 08 13 01 00 00 08 00 00 10 CF 07 07 07 04 07 54 75 6E 6E 65 6C 31 00 00 0C 0B 07 0A 0B 0B 0B 00 00 47 24 00 24 0C 02 00 00 00 07 01 00 00 06 7F 00 00 05 00 00 00 00 44 7A 00 00 00 00 00 00 00 00 00 00 00 00 05 DC 00 30 0D 02 00 00 00 0A 01 00 00 08 04 00 00 01 00 00 00 01 06 00 00 01 49 98 96 80 08 00 00 01 00 00 00 00 0A 00 00 01 00 00 05 DC 05 00 00 00 .]{lang="EN-US"}]{#struct_0_x6691_30153_x1382606069}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1147634949}*[向]{style="font-family:宋体"}[socket 41]{lang="EN-US"}[发送]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[188]{lang="EN-US"}[字节，报文内容以十六进制形式打印。]{style="font-family:宋体"}*

[[\*Aug 19 08:37:51:279 2012 Sysname RSVP/7/PKT: -MDC=1; Sent path message to interface GE1/0/2, nexthop 23.11.110.12, result s]{lang="EN-US"}]{#struct_0_x6691_30153_746054873}[uccessful]{lang="EN-US"}[. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x836987698}*[成功向接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[发送]{style="font-family:宋体"}[Path]{lang="EN-US"}[报文，下一跳地址为]{style="font-family:宋体"}*[23.11.110.12]{lang="EN-US"}*[。]{style="font-family:宋体"}*

::: {#-640081544 .myid}
[]{#_Toc404790956}[]{#struct_0_x6691_30153_x952924880}

**RSVP \-- RSVP调试命令 \-- debugging rsvp path**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_1191649418}

[**[debugging rsvp path]{lang="EN-US"}**[ \[ **destination** *ip-address* **source** *ip-address* **tunnel-id** *tunnel-id* \]]{lang="EN-US"}]{#struct_0_x6691_30153_29048567}

[**[undo debugging rsvp path]{lang="EN-US"}**]{#struct_0_x6691_30153_x815006470}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_206027500}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_x646869488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_746120409}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x6691_30153_1428556919}[：指定隧道的目的地址。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x6691_30153_x1295431160}[：指定隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_x6691_30153_548137948}[：指定隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x176343476}

[**[debugging rsvp path]{lang="EN-US"}**]{#struct_0_x6691_30153_x305367360}[命令用来打开]{style="font-family:宋体"}[RSVP Path]{lang="EN-US"}[相关的调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp path]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP Path]{lang="EN-US"}[相关的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP Path]{lang="EN-US"}]{#struct_0_x6691_30153_x1933685032}[相关的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging rsvp path]{lang="EN-US"}]{#struct_0_x6691_30153_x2020213657}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_331465641}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_746710233}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1651891360}

[[TC triggered to create ingress CR-LSP, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_423308719}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_x570580400}[触发创建头节点]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[TC triggered to delete ingress CR-LSP, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1371995553}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_x1070443769}[触发删除头节点]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[TC triggered to create egress CR-LSP, ingress LSR ID *lsr-id*, tunnel ID *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_746775769}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_692414903}[触发创建尾节点]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[TC triggered to delete egress CR-LSP, ingress LSR ID *lsr-id*, tunnel ID *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1221906582}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_x1779121267}[触发创建尾节点]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，头节点]{style="font-family:宋体"}[LSR ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsr-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Received a path message. Created a new PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x985257977}

[[收到]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_x662003182}[消息，新建]{style="font-family:宋体"}[PSB]{lang="EN-US"}

[[Received a path message. Updated the old PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_746185942}

[[收到]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_721750799}[消息，更新]{style="font-family:宋体"}[PSB]{lang="EN-US"}

[[PSB\'s PHOP changed from *phop-addr1* to *phop-addr2*.]{lang="EN-US"}]{#struct_0_x6691_30153_x175415392}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1344511913}[的]{style="font-family:宋体"}[PHOP]{lang="EN-US"}[从]{style="font-family:宋体"}*[phop-addr1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[phop-addr2]{lang="EN-US"}*

[[PSB incoming label *label1* is different from the recovery label *label2* in the path message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1582729505}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_746251478}[的入标签]{style="font-family:宋体"}*[label1]{lang="EN-US"}*[与]{style="font-family:宋体"}[path]{lang="EN-US"}[消息中的]{style="font-family:宋体"}[recovery label *label2*]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Allocated resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1424159721}

[[从]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_1050492782}[分配资源：接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result ]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}[result]{lang="EN-US"}]{#struct_0_x6691_30153_726908549}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[uccessful]{lang="EN-US"}]{#struct_0_x6691_30153_624656724}[：资源分配成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x6691_30153_726974085}[：资源分配失败]{style="font-family:宋体"}

[[Checked resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.]{lang="EN-US"}]{#struct_0_x6691_30153_203504479}

[[检查]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_x1733282265}[资源：接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}*[result]{lang="EN-US"}*]{#struct_0_x6691_30153_x2127152770}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[uccessful]{lang="EN-US"}]{#struct_0_x6691_30153_726777477}[：资源分配成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bandwidth unavailable]{lang="EN-US"}]{#struct_0_x6691_30153_726843013}[：带宽无效，资源分配失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no route]{lang="EN-US"}]{#struct_0_x6691_30153_x2086717089}[：亲和属性检查不通过，资源分配失败]{style="font-family:宋体"}

[[Freed resource to TRM.]{lang="EN-US"}]{#struct_0_x6691_30153_746317014}

[[释放]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_1333541411}[资源]{style="font-family:宋体"}

[[Created a reverse CR-LSP, LSP ID *lsp-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x780034082}

[[创建反向]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_x609151383}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Deleted the reverse CR-LSP, LSP ID *lsp-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_1990878577}

[[删除反向]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_746382550}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Allocated incoming label *label* for reverse LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_x1448050091}

[[为反向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x6691_30153_365838317}[分配入标签]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Allocated incoming label *label* for LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_x406405543}

[[为]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x6691_30153_745923798}[分配入标签]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Deleted MP information. PHOP is *phop-addr*.]{lang="EN-US"}]{#struct_0_x6691_30153_x643114220}

[[删除]{style="font-family:宋体"}[MP]{lang="EN-US"}]{#struct_0_x6691_30153_1098464864}[信息，]{style="font-family:宋体"}[PHOP]{lang="EN-US"}[是]{style="font-family:宋体"}*[phop-addr]{lang="EN-US"}*

[[Failed to trigger CSPF.]{lang="EN-US"}]{#struct_0_x6691_30153_x34067821}

[[触发]{style="font-family:宋体"}[CSPF]{lang="EN-US"}]{#struct_0_x6691_30153_745989334}[失败]{style="font-family:宋体"}

[[FRR bind.]{lang="EN-US"}]{#struct_0_x6691_30153_522497734}

[[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_x1212830410}[绑定]{style="font-family:宋体"}

[[FRR unbind.]{lang="EN-US"}]{#struct_0_x6691_30153_1403775828}

[[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_746054870}[取消绑定]{style="font-family:宋体"}

[[FRR inuse.]{lang="EN-US"}]{#struct_0_x6691_30153_x836987701}

[[已经进行]{style="font-family:宋体"}[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_1386186023}[切换]{style="font-family:宋体"}

[[Finished smoothing all egress CR-LSP configurations.]{lang="EN-US"}]{#struct_0_x6691_30153_x689676153}

[[尾节点]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_746120406}[配置平滑结束]{style="font-family:宋体"}

[[TC disconnected.]{lang="EN-US"}]{#struct_0_x6691_30153_1428556918}

[[TC]{lang="EN-US"}]{#struct_0_x6691_30153_x1295496696}[和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[的连接断开]{style="font-family:宋体"}

[[TRM reconnected.]{lang="EN-US"}]{#struct_0_x6691_30153_746710230}

[[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_x1651891363}[和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[重新建立连接]{style="font-family:宋体"}

[[Resource was preempted.]{lang="EN-US"}]{#struct_0_x6691_30153_x1142775222}

[[资源被抢占]{style="font-family:宋体"}]{#struct_0_x6691_30153_1059318799}

[[Deleted the PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_746775766}

[[删除]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_692414904}

[[Released the incoming label *label* for reverse LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_x1221906575}

[[释放反向]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x6691_30153_746185943}[的入标签]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Released the incoming label *label* for LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_721750798}

[[释放]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x6691_30153_x175415393}[的入标签]{style="font-family:宋体"}*[label]{lang="EN-US"}*

[[Sent a path message.]{lang="EN-US"}]{#struct_0_x6691_30153_746251479}

[[发送]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_x1424159720}[消息]{style="font-family:宋体"}

[[The path message length *length* is greater than interface MTU *mtu*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1678390573}

[[Path]{lang="EN-US"}]{#struct_0_x6691_30153_x1014652083}[消息的长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[大于接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}*[mtu]{lang="EN-US"}*

[[Started to smooth all PSBs.]{lang="EN-US"}]{#struct_0_x6691_30153_746317015}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_1333541412}[平滑开始]{style="font-family:宋体"}

[[Smoothing the PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x779968546}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_746382551}[平滑]{style="font-family:宋体"}

[[Finished smoothing all PSBs.]{lang="EN-US"}]{#struct_0_x6691_30153_x1448050092}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_769122844}[平滑结束]{style="font-family:宋体"}

[[Received interface *interface* change message.]{lang="EN-US"}]{#struct_0_x6691_30153_745923799}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_x6691_30153_x643114221}[状态变化消息]{style="font-family:宋体"}

[[Processing interface change message.]{lang="EN-US"}]{#struct_0_x6691_30153_745989335}

[[处理接口状态变化消息]{style="font-family:宋体"}]{#struct_0_x6691_30153_522497733}

[[Interface change message processing completed.]{lang="EN-US"}]{#struct_0_x6691_30153_x1212830407}

[[接口状态变化消息结束]{style="font-family:宋体"}]{#struct_0_x6691_30153_746054871}

[[Received peer *peer-addr* lost message, interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x836987700}

[[收到邻居]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_1386251559}[丢失消息，邻居所在的接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Processing peer lost message.]{lang="EN-US"}]{#struct_0_x6691_30153_746120407}

[[处理邻居丢失]{style="font-family:宋体"}]{#struct_0_x6691_30153_1428556917}

[[Peer lost message processing completed.]{lang="EN-US"}]{#struct_0_x6691_30153_x1295037944}

[[邻居丢失消息处理结束]{style="font-family:宋体"}]{#struct_0_x6691_30153_746710231}

[[GR started: Set the staled flag on the PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1651891362}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_746775767}[开始，给]{style="font-family:宋体"}[PSB]{lang="EN-US"}[打上老化标记]{style="font-family:宋体"}

[[GR disabled: Deleted the staled flag on the PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_692414905}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1221906576}[去使能，清除]{style="font-family:宋体"}[PSB]{lang="EN-US"}[老化标记]{style="font-family:宋体"}

[[GR ended: Deleted the staled PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982697409}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1919818022}[结束，删除带有老化标记的]{style="font-family:宋体"}[PSB]{lang="EN-US"}

[[Received an error notification from LSM, LSP ID *lsp-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982631873}

[[收到]{style="font-family:宋体"}[LSM]{lang="EN-US"}]{#struct_0_x6691_30153_x793737046}[错误通知，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Received a PathErr message: error code = *error-code*, error value = *error-value*, error description = *description*.]{lang="EN-US"}]{#struct_0_x6691_30153_x2144822554}

[[收到]{style="font-family:宋体"}[PathErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1982566337}[消息，错误码为]{style="font-family:宋体"}[error-code]{lang="EN-US"}[，错误值为]{style="font-family:宋体"}[error-value]{lang="EN-US"}[，错误描述信息为]{style="font-family:宋体"}[description]{lang="EN-US"}

[[Received a PathErr message. Sent a path message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1924410876}

[[收到]{style="font-family:宋体"}[PathErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1982500801}[消息，发送]{style="font-family:宋体"}[path]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Received a PathErr message. Teared the CR-LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_x214001209}

[[收到]{style="font-family:宋体"}[PathErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1960485602}[消息，拆除]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}

[[Forwarded the PathErr message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982959553}

[[转发]{style="font-family:宋体"}[PathErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1830750309}[消息]{style="font-family:宋体"}

[[Sent a PathErr message: error code = *error-code*, error value = *error-value*, error description = *description*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982894017}

[[发送]{style="font-family:宋体"}[PathErr]{lang="EN-US"}]{#struct_0_x6691_30153_709318864}[消息，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*[，错误值为]{style="font-family:宋体"}*[error-value]{lang="EN-US"}*[，错误描述信息为]{style="font-family:宋体"}*[description]{lang="EN-US"}*

[[Received a PathTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982828481}

[[收到]{style="font-family:宋体"}[PathTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1004566059}[消息]{style="font-family:宋体"}

[[Received a PathTear message. Deleted MP information for PHOP *phop-addr*.]{lang="EN-US"}]{#struct_0_x6691_30153_2047008454}

[[收到]{style="font-family:宋体"}[PathTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1982762945}[消息，删除]{style="font-family:宋体"}[MP]{lang="EN-US"}[信息，]{style="font-family:宋体"}[PHOP]{lang="EN-US"}[为]{style="font-family:宋体"}*[phop-addr]{lang="EN-US"}*

[[Received a PathTear message. Deleted the PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_676194504}

[[收到]{style="font-family:宋体"}[PathTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1982173121}[消息，删除]{style="font-family:宋体"}[PSB]{lang="EN-US"}

[[Forwarded the PathTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_69833171}

[[转发]{style="font-family:宋体"}[PathTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1982107585}[消息]{style="font-family:宋体"}

[[Sent a PathTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1862023330}

[[发送]{style="font-family:宋体"}[PathTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1982697408}[消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_809065333}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_1367741478}[打开]{style="font-family:宋体"}[RSVP Path]{lang="EN-US"}[相关的调试信息开关，收到]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp path]{lang="EN-US"}]{#struct_0_x6691_30153_1814743053}

[\*Aug 19 08:25:17:440 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a path message. Created a new PSB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x2108905736}*[接收到]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息，创建新的]{style="font-family:宋体"}[PSB]{lang="EN-US"}[。消息的目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，隧道的]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Failed to trigger CSPF.]{lang="EN-US"}]{#struct_0_x6691_30153_955968525}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1486420844}*[触发]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[计算失败。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Checked resource from TRM: interface GE1/0/1, bandwidth 0kbps, CT 0, result  successful.]{lang="EN-US"}]{#struct_0_x6691_30153_992704234}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982631872}*[检查]{style="font-family:宋体"}[TRM]{lang="EN-US"}[资源成功：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，带宽为]{style="font-family:宋体"}[0kbps]{lang="EN-US"}[，带宽类型为]{style="font-family:宋体"}[CT 0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Allocated incoming label 1148 for LSP.]{lang="EN-US"}]{#struct_0_x6691_30153_1935146309}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1044698170}*[为]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分配入标签值]{style="font-family:宋体"}[1148]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:17:441 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a path message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1535701723}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_284905443}*[发送]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a path message. Updated the old PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1522834196}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1202907356}*[接收到]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息，更新已有的]{style="font-family:宋体"}[PSB]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Failed to trigger CSPF.]{lang="EN-US"}]{#struct_0_x6691_30153_344781058}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1382431204}*[触发]{style="font-family:宋体"}[CSPF]{lang="EN-US"}[计算失败。]{style="font-family:宋体"}*

[[\*Aug 19 08:25:48:035 2012 Sysname RSVP/7/PATH: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a path message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982566336}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x358326935}*[发送]{style="font-family:宋体"}[Path]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

::: {#1168098875 .myid}
[]{#_Toc404790957}[]{#struct_0_x6691_30153_1617835657}

**RSVP \-- RSVP调试命令 \-- debugging rsvp reduction**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_370106866}

[**[debugging rsvp reduction]{lang="EN-US"}**]{#struct_0_x6691_30153_x441663431}

[**[undo debugging rsvp reduction]{lang="EN-US"}**]{#struct_0_x6691_30153_194092274}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x788113027}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_37015501}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1982500800}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_1352082732}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_885472220}

[**[debugging rsvp reduction]{lang="EN-US"}**]{#struct_0_x6691_30153_x321432223}[命令用来打开]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[摘要刷新和消息可靠传递调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp reduction]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[RSVP]{lang="EN-US"}[摘要刷新和消息可靠传递调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_1138223760}[摘要刷新和消息可靠传递调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging rsvp reduction]{lang="EN-US"}]{#struct_0_x6691_30153_1297713658}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_322930324}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x283903360}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_1762906286}

[[Created message ID *message-id* for retransmit message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982959552}

[[为重传报文分配]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_898133046}[，值为]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*

[[Added message ID *message-id* to srefresh message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1975873186}

[[为摘要刷新消息添加]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_1098949584}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a srefresh message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1100857829}

[[收到摘要刷新消息]{style="font-family:宋体"}]{#struct_0_x6691_30153_x306656384}

[[Received an ACK message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982894016}

[[收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6691_30153_x856765077}[消息]{style="font-family:宋体"}

[[Replied an ACK message.]{lang="EN-US"}]{#struct_0_x6691_30153_722054052}

[[回应]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6691_30153_591665593}[消息]{style="font-family:宋体"}

[[Replied a NACK message.]{lang="EN-US"}]{#struct_0_x6691_30153_x2049092939}

[[回应]{style="font-family:宋体"}[NACK]{lang="EN-US"}]{#struct_0_x6691_30153_x1982828480}[消息]{style="font-family:宋体"}

[[Processing ACK message ID list from *peer-addr*.]{lang="EN-US"}]{#struct_0_x6691_30153_561517882}

[[处理来自]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_488741083}[的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息的]{style="font-family:宋体"}[message ID]{lang="EN-US"}[链]{style="font-family:宋体"}

[[Reset PSB cleanup timer by message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_1331258098}

[[根据]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_1265678892}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）重置]{style="font-family:宋体"}[PSB]{lang="EN-US"}[老化定时器]{style="font-family:宋体"}

[[Reset RSB cleanup timer by message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982762944}

[[根据]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x2052688851}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）重置]{style="font-family:宋体"}[RSB]{lang="EN-US"}[老化定时器]{style="font-family:宋体"}

[[Invalid message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_1382074103}

[[无效的]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x2003613218}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Processing NACK message ID list from *peer-addr*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1414499897}

[[处理来自]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982173120}[的]{style="font-family:宋体"}[NACK]{lang="EN-US"}[消息的]{style="font-family:宋体"}[message ID]{lang="EN-US"}[链]{style="font-family:宋体"}

[[Sent a path message for message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1496250770}

[[为]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_547736337}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）发送]{style="font-family:宋体"}[path]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Sent a resv message for message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_1222482120}

[[为]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x1513546604}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）发送]{style="font-family:宋体"}[resv]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Added message ID *message-id* to the retransmit buffer.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982107584}

[[向重传缓冲区添加]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x295939389}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Deleted message ID *message-id* from the retransmit buffer.]{lang="EN-US"}]{#struct_0_x6691_30153_x550040289}

[[从重传缓冲区中删除]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x675548772}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1982697411}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_2018984450}[在接口视图下配置]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[摘要刷新和消息可靠传递功能后，打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[摘要刷新和消息可靠传递调试信息开关，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp reduction]{lang="EN-US"}]{#struct_0_x6691_30153_x591410750}

[\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Created message ID 7 for retransmit message.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_874128937}*[为重传报文分配]{style="font-family:宋体"}[message ID]{lang="EN-US"}[，值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Added message ID 6 to srefresh message.]{lang="EN-US"}]{#struct_0_x6691_30153_178878228}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1241222626}*[为摘要刷新消息添加]{style="font-family:宋体"}[message ID]{lang="EN-US"}[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:178 2012 Sysname RSVP/7/REDUC: -MDC=1; Added message ID 7 to the retransmit buffer.]{lang="EN-US"}]{#struct_0_x6691_30153_x2009507104}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1980773235}*[向重传缓冲区添加]{style="font-family:宋体"}[message ID]{lang="EN-US"}[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Received an ACK message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982631875}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1600306100}*[接收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Processing ACK message ID list from 12.11.110.11.]{lang="EN-US"}]{#struct_0_x6691_30153_x1760048688}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1830995433}*[处理来自]{style="font-family:宋体"}[12.11.110.11]{lang="EN-US"}[的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息的]{style="font-family:宋体"}[message ID]{lang="EN-US"}[链。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:179 2012 Sysname RSVP/7/REDUC: -MDC=1; Deleted message ID 7 from the retransmit buffer.]{lang="EN-US"}]{#struct_0_x6691_30153_x528691988}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1936755140}*[从重传缓冲区中删除]{style="font-family:宋体"}[message ID]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:04:334 2012 Sysname RSVP/7/REDUC: -MDC=1; Replied an ACK message.]{lang="EN-US"}]{#struct_0_x6691_30153_1898152936}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x677023913}*[应答]{style="font-family:宋体"}[ACK]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:14:134 2012 Sysname RSVP/7/REDUC: -MDC=1; Received a srefresh message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1300597194}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982566339}*[接收到]{style="font-family:宋体"}[Srefresh]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Aug 19 08:50:14:134 2012 Sysname RSVP/7/REDUC: -MDC=1; Reset PSB cleanup timer by message ID 7.]{lang="EN-US"}]{#struct_0_x6691_30153_x761611462}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_711300642}*[根据]{style="font-family:宋体"}[message ID]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）重置]{style="font-family:宋体"}[PSB]{lang="EN-US"}[老化定时器。]{style="font-family:宋体"}*

::: {#1324087602 .myid}
[]{#_Toc404790958}[]{#struct_0_x6691_30153_x770124589}

**RSVP \-- RSVP调试命令 \-- debugging rsvp resv**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1125591969}

[**[debugging rsvp resv]{lang="EN-US"}**[ \[ **destination** *ip-address* **source** *ip-address* **tunnel-id** *tunnel-id* \]]{lang="EN-US"}]{#struct_0_x6691_30153_x1425544126}

[**[undo debugging rsvp resv]{lang="EN-US"}**]{#struct_0_x6691_30153_x1665224001}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1471691838}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1917341670}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1982500803}

[**[destination]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x6691_30153_x1376800623}[：指定隧道的目的地址。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x6691_30153_961519454}[：指定隧道的源地址，即]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[消息中]{style="font-family:宋体"}[Session]{lang="EN-US"}[对象的扩展]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tunnel-id]{lang="EN-US"}**[ *tunnel-id*]{lang="EN-US"}]{#struct_0_x6691_30153_x1911753347}[：指定隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1616328150}

[**[debugging rsvp resv]{lang="EN-US"}**]{#struct_0_x6691_30153_x1671963924}[命令用来打开]{style="font-family:宋体"}[RSVP Resv]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp resv]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[RSVP Resv]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP Resv]{lang="EN-US"}]{#struct_0_x6691_30153_x1448019148}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging rsvp resv]{lang="EN-US"}]{#struct_0_x6691_30153_1948993125}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_350234193}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1982959555}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_x667950895}

[[Received a resv message. Created a new RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_1302995375}

[[收到]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_x1466537523}[消息，新建]{style="font-family:宋体"}[RSB]{lang="EN-US"}

[[Received a resv message. Updated the old RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_2107556927}

[[收到]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_1170407616}[消息，更新]{style="font-family:宋体"}[RSB]{lang="EN-US"}

[[Allocated resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982894019}

[[从]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_x2066618658}[分配资源：接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result ]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}[result]{lang="EN-US"}]{#struct_0_x6691_30153_x1289317473}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[uccessful]{lang="EN-US"}]{#struct_0_x6691_30153_x1290038369}[：资源分配成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x6691_30153_1724955354}[：资源分配失败]{style="font-family:宋体"}

[[Modified resource from TRM: interface *interface*, bandwidth *bandwidth*, CT *class-type*, result *result*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1303189755}

[[修改]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_x485624183}[资源：接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[，带宽为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[，带宽类型为]{style="font-family:宋体"}*[class-type]{lang="EN-US"}*[，返回值为]{style="font-family:宋体"}*[result ]{lang="EN-US"}*

[[其中，]{style="font-family:宋体"}[result]{lang="EN-US"}]{#struct_0_x6691_30153_x1289972833}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s]{lang="EN-US"}[uccessful]{lang="EN-US"}]{#struct_0_x6691_30153_x1289514082}[：资源修改成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x6691_30153_x2007906913}[：资源修改失败]{style="font-family:宋体"}

[[Freed resource to TRM.]{lang="EN-US"}]{#struct_0_x6691_30153_x1269426272}

[[向]{style="font-family:宋体"}[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_104089863}[释放资源]{style="font-family:宋体"}

[[Failed to get PSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982828483}

[[获取]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_158233355}[失败]{style="font-family:宋体"}

[[Created a new TCSB.]{lang="EN-US"}]{#struct_0_x6691_30153_625410812}

[[新建]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1016550399}

[[Updated the old TCSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x71385796}

[[更新旧的]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1982762947}

[[Added filterspec to TCSB.]{lang="EN-US"}]{#struct_0_x6691_30153_1838993918}

[[向]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_403146896}[添加]{style="font-family:宋体"}[filterspec]{lang="EN-US"}

[[The TCSB is blockaded.]{lang="EN-US"}]{#struct_0_x6691_30153_2027267446}

[[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1982173123}[被阻塞]{style="font-family:宋体"}

[[Merged flowdesc from TCSB. The merge flag is off.]{lang="EN-US"}]{#struct_0_x6691_30153_x1092966243}

[[根据]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_x910929900}[合并流量描述，合并标记为]{style="font-family:宋体"}[off]{lang="EN-US"}

[[Merged flowdesc from TCSB. The merge flag is on.]{lang="EN-US"}]{#struct_0_x6691_30153_x514849985}

[[根据]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_x755563675}[合并流量描述，合并标记为]{style="font-family:宋体"}[on]{lang="EN-US"}

[[Merged flowspec with LUB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982107587}

[[用]{style="font-family:宋体"}[LUB]{lang="EN-US"}]{#struct_0_x6691_30153_1270144552}[算法合并流量描述]{style="font-family:宋体"}

[[Merged flowspec with GLB.]{lang="EN-US"}]{#struct_0_x6691_30153_x635107495}

[[用]{style="font-family:宋体"}[GLB]{lang="EN-US"}]{#struct_0_x6691_30153_x1759804363}[算法合并流量描述]{style="font-family:宋体"}

[[Updated TCSB: TC_B_Police_flag *flag1*, TC_E_Police_flag *flag2,* TC_M_Police_flag *flag3*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982697410}

[[更新]{style="font-family:宋体"}[TCSB]{lang="EN-US"}]{#struct_0_x6691_30153_452900509}[，]{style="font-family:宋体"}[TC_B_Police_flag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag1]{lang="EN-US"}*[，]{style="font-family:宋体"}[TC_E_Police_flag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag2]{lang="EN-US"}[，]{style="font-family:宋体"}*[TC_M_Police_flag]{lang="EN-US"}[为]{style="font-family:宋体"}*[flag3]{lang="EN-US"}*

[[Updated CR-LSP, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_1262534930}

[[更新]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_1869817236}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Deleted CR-LSP, LSP ID *lsp-id*, direction *direction*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982631874}

[[删除]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}]{#struct_0_x6691_30153_1128577255}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*[，方向为]{style="font-family:宋体"}*[direction]{lang="EN-US"}*

[[Created request info.]{lang="EN-US"}]{#struct_0_x6691_30153_1536605855}

[[创建]{style="font-family:宋体"}[request]{lang="EN-US"}]{#struct_0_x6691_30153_x1504784946}[信息]{style="font-family:宋体"}

[[Updated request info.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982566338}

[[更新]{style="font-family:宋体"}[request]{lang="EN-US"}]{#struct_0_x6691_30153_804472479}[信息]{style="font-family:宋体"}

[[Deleted filterspec in request info.]{lang="EN-US"}]{#struct_0_x6691_30153_x186610969}

[[从]{style="font-family:宋体"}[request]{lang="EN-US"}]{#struct_0_x6691_30153_x1982500802}[信息中删除]{style="font-family:宋体"}[filterspec]{lang="EN-US"}

[[No filterspec in request info, deleted request info.]{lang="EN-US"}]{#struct_0_x6691_30153_189283318}

[[request]{lang="EN-US"}]{#struct_0_x6691_30153_x1771046436}[信息中没有]{style="font-family:宋体"}[filterspec]{lang="EN-US"}[，删除]{style="font-family:宋体"}[request]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Sent a resv message.]{lang="EN-US"}]{#struct_0_x6691_30153_503307538}

[[发送]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_x1982959554}[消息]{style="font-family:宋体"}

[[Resource was preempted.]{lang="EN-US"}]{#struct_0_x6691_30153_2060932460}

[[资源被抢占]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1000657102}

[[GR started: Set the staled flag on the RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982894018}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_662264697}[开始：给]{style="font-family:宋体"}[RSB]{lang="EN-US"}[打上老化标记]{style="font-family:宋体"}

[[GR recovered: Recovered the staled RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1336202245}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1982828482}[恢复：恢复]{style="font-family:宋体"}[RSB]{lang="EN-US"}

[[GR disabled: Deleted the staled flag on the RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_1724317296}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_247316318}[去使能：清除]{style="font-family:宋体"}[RSB]{lang="EN-US"}[中老化标记]{style="font-family:宋体"}

[[GR ended: Deleted the staled RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_1069259976}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x1982762946}[结束：删除带有老化标记的]{style="font-family:宋体"}[RSB]{lang="EN-US"}

[[Received interface *interface* change message.]{lang="EN-US"}]{#struct_0_x6691_30153_x889889437}

[[收到接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_x6691_30153_2020021554}[状态变化消息]{style="font-family:宋体"}

[[Processing interface change message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982173122}

[[处理接口状态变化消息]{style="font-family:宋体"}]{#struct_0_x6691_30153_1635917112}

[[Interface change message processing completed.]{lang="EN-US"}]{#struct_0_x6691_30153_x569985503}

[[接口状态变化消息处理结束]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1982107586}

[[Received peer *peer-addr* lost message, interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1458738803}

[[收到邻居]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982697413}[丢失消息，邻居所在的接口为]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Processing peer lost message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1113183432}

[[处理邻居丢失消息]{style="font-family:宋体"}]{#struct_0_x6691_30153_1665203571}

[[Peer lost message processing completed.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982631877}

[[处理邻居丢失消息结束]{style="font-family:宋体"}]{#struct_0_x6691_30153_1531861782}

[[Started to smooth all RSBs.]{lang="EN-US"}]{#struct_0_x6691_30153_x376856705}

[[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1982566341}[平滑开始]{style="font-family:宋体"}

[[Smoothing the RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1118169502}

[[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_1881645273}[平滑]{style="font-family:宋体"}

[[Finished smoothing all RSBs.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982500805}

[[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_1755367259}[平滑结束]{style="font-family:宋体"}

[[TRM reconnected.]{lang="EN-US"}]{#struct_0_x6691_30153_x684264199}

[[TRM]{lang="EN-US"}]{#struct_0_x6691_30153_x1982959557}[和]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[重新建立连接]{style="font-family:宋体"}

[[Received a ResvErr message: error code = *error-code*, error value = *error-value*, error description = *description.*]{lang="EN-US"}]{#struct_0_x6691_30153_494848519}

[[收到]{style="font-family:宋体"}[ResvErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1982894021}[消息，错误码为]{style="font-family:宋体"}[error-code]{lang="EN-US"}[，错误值为]{style="font-family:宋体"}*[error-value]{lang="EN-US"}*[，错误描述信息为]{style="font-family:宋体"}*[description]{lang="EN-US"}*

[[Forwarded the ResvErr message.]{lang="EN-US"}]{#struct_0_x6691_30153_1871921670}

[[转发]{style="font-family:宋体"}[ResvErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1924546744}[消息]{style="font-family:宋体"}

[[Created a new BSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982828485}

[[新建]{style="font-family:宋体"}[BSB]{lang="EN-US"}]{#struct_0_x6691_30153_964802409}

[[Updated the old BSB.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982762949}

[[更新旧的]{style="font-family:宋体"}[BSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1293173964}

[[Sent a ResvErr message: error code = *error-code*, error value = *error-value*, error description = *description.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1477510838}

[[发送]{style="font-family:宋体"}[ResvErr]{lang="EN-US"}]{#struct_0_x6691_30153_x1982173125}[消息，错误码为]{style="font-family:宋体"}[error-code]{lang="EN-US"}[，错误值为]{style="font-family:宋体"}*[error-value]{lang="EN-US"}*[，错误描述信息为]{style="font-family:宋体"}*[description]{lang="EN-US"}*

[[Received a ResvTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_2039201639}

[[收到]{style="font-family:宋体"}[ResvTear]{lang="EN-US"}]{#struct_0_x6691_30153_x1982107589}[消息]{style="font-family:宋体"}

[[Received a ResvTear message. Sent a PathTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_107345138}

[[收到]{style="font-family:宋体"}[ResvTear]{lang="EN-US"}]{#struct_0_x6691_30153_x201211920}[消息，发送]{style="font-family:宋体"}[PathTear]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Received a ResvTear message. Sent a resv message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982697412}

[[收到]{style="font-family:宋体"}[ResvTear]{lang="EN-US"}]{#struct_0_x6691_30153_1615699923}[消息，发送]{style="font-family:宋体"}[resv]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Forwarded the ResvTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982631876}

[[转发]{style="font-family:宋体"}[ResvTear]{lang="EN-US"}]{#struct_0_x6691_30153_x34222159}[消息]{style="font-family:宋体"}

[[Sent a ResvTear message.]{lang="EN-US"}]{#struct_0_x6691_30153_x1982566340}

[[发送]{style="font-family:宋体"}[ResvTear]{lang="EN-US"}]{#struct_0_x6691_30153_447914439}[消息]{style="font-family:宋体"}

[[Received a ResvConf message.]{lang="EN-US"}]{#struct_0_x6691_30153_x2108689898}

[[收到]{style="font-family:宋体"}[ResvConf]{lang="EN-US"}]{#struct_0_x6691_30153_x1982500804}[消息]{style="font-family:宋体"}

[[Sent a ResvConf message.]{lang="EN-US"}]{#struct_0_x6691_30153_x973516096}

[[发送]{style="font-family:宋体"}[ResvConf]{lang="EN-US"}]{#struct_0_x6691_30153_x1982959556}[消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1071235422}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x571467102}[打开]{style="font-family:宋体"}[RSVP Resv]{lang="EN-US"}[调试信息开关，收到]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp resv]{lang="EN-US"}]{#struct_0_x6691_30153_x1365751419}

[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a resv message. Created a new RSB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_348799664}*[接收到]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息，创建新的]{style="font-family:宋体"}[RSB]{lang="EN-US"}[。消息的目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，隧道的]{style="font-family:宋体"}[Tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.1]{lang="EN-US"}]{#struct_0_x6691_30153_x986818813}

[1.11, tunnel ID 1: TCSB param: TC_B_Police_flag 0, TC_E_Police_flag 0, TC_M_Police_flag 0.]{lang="EN-US"}

[*[// TC_B_Police_flag]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982894020}*[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[TC_E_Police_flag]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[TC_M_Police_flag]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.1]{lang="EN-US"}]{#struct_0_x6691_30153_305837729}

[1.11, tunnel ID 1: Created a new TCSB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x723325958}*[新建]{style="font-family:宋体"}[TCSB]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Allocated resource from TRM: interface GE1/0/1, bandwidth 0kbps, CT 0, result successful.]{lang="EN-US"}]{#struct_0_x6691_30153_412459840}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_596296664}*[成功从]{style="font-family:宋体"}[TRM]{lang="EN-US"}[分配资源：接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，带宽为]{style="font-family:宋体"}[0kbps]{lang="EN-US"}[，带宽类型为]{style="font-family:宋体"}[CT0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Updated CR-LSP, LSP ID 18212, direction 0.]{lang="EN-US"}]{#struct_0_x6691_30153_x2029060769}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1573248806}*[更新]{style="font-family:宋体"}[CR-LSP]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[18212]{lang="EN-US"}[，该隧道为单向隧道。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:404 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Created request info.]{lang="EN-US"}]{#struct_0_x6691_30153_x1408724880}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982828484}*[创建]{style="font-family:宋体"}[request]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:405 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Merged flowdesc from TCSB. The merge flag is off.]{lang="EN-US"}]{#struct_0_x6691_30153_x1764080946}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_955784932}*[根据]{style="font-family:宋体"}[TCSB]{lang="EN-US"}[合并流量描述，合并标记为]{style="font-family:宋体"}[off]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:13:405 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Sent a resv message.]{lang="EN-US"}]{#struct_0_x6691_30153_492794847}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_631292521}*[发送]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息。]{style="font-family:宋体"}*

[[\*Aug 19 08:30:23:967 2012 Sysname RSVP/7/RESV: -MDC=1; dst 10.33.33.33, src 10.11.11.11, tunnel ID 1: Received a resv message. Updated the old RSB.]{lang="EN-US"}]{#struct_0_x6691_30153_645350935}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_158349055}*[接收到]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息，更新已有的]{style="font-family:宋体"}[RSB]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-1257960097 .myid}
[]{#_Toc404790959}[]{#struct_0_x6691_30153_968718058}

**RSVP \-- RSVP调试命令 \-- debugging rsvp timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6691_30153_44143970}

[**[debugging rsvp timer]{lang="EN-US"}**]{#struct_0_x6691_30153_x1982762948}

[**[undo debugging rsvp timer]{lang="EN-US"}**]{#struct_0_x6691_30153_272909977}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6691_30153_1095778506}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1608273036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x823361620}

[[无]{style="font-family:宋体"}]{#struct_0_x6691_30153_x475171436}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1016165024}

[**[debugging rsvp timer]{lang="EN-US"}**]{#struct_0_x6691_30153_2071714911}[命令用来打开定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging rsvp timer]{lang="EN-US"}**[命令用来关闭定时器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RSVP]{lang="EN-US"}]{#struct_0_x6691_30153_x1982173124}[定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging rsvp timer]{lang="EN-US"}]{#struct_0_x6691_30153_473117698}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_338332676}[[字段]{style="font-family:黑体"}]{#struct_0_x6691_30153_x131918200}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6691_30153_1782613968}

[[Created cleanup timer for SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x286850418}

[[创建认证老化定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x871086739}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Reset cleanup timer of SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_1975106878}

[[重置认证老化定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x1982107588}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Cleanup timer of SA expired: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_1673429079}

[[认证老化定时器超时：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_1749752590}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Deleted cleanup timer of SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_453270085}

[[删除认证老化定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x1283784575}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Created challenge timer for SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_825075134}

[[创建认证挑战定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x416613468}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Reset challenge timer for SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1853197040}

[[重置认证挑战定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_x1223544104}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Challenge timer of SA expired: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1745133719}

[[认证挑战定时器超时：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_2059331708}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[Deleted challenge timer of SA: from *start-address* to *end-address*.]{lang="EN-US"}]{#struct_0_x6691_30153_x416547932}

[[删除认证挑战定时器：起点地址]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*]{#struct_0_x6691_30153_528107288}[，终点地址]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*

[[FRR optimize timer expired.]{lang="EN-US"}]{#struct_0_x6691_30153_x47416000}

[[FRR]{lang="EN-US"}]{#struct_0_x6691_30153_162791932}[优化定时器超时]{style="font-family:宋体"}

[[Created resend timer for HA message.]{lang="EN-US"}]{#struct_0_x6691_30153_694504493}

[[创建]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x6691_30153_x416482396}[消息重发定时器]{style="font-family:宋体"}

[[Resend timer of HA message expired.]{lang="EN-US"}]{#struct_0_x6691_30153_x1484396178}

[[HA]{lang="EN-US"}]{#struct_0_x6691_30153_x1520223223}[消息重发定时器超时]{style="font-family:宋体"}

[[Deleted the resend timer of HA message.]{lang="EN-US"}]{#struct_0_x6691_30153_x2024861293}

[[删除]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_x6691_30153_x416416860}[消息重发定时器]{style="font-family:宋体"}

[[Created GR restart timer, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_907787225}

[[创建]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x2029568816}[重启定时器，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[GR restart timer expired, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_1517613908}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_1438754577}[重启定时器超时，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Created GR recovery timer, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x416875612}

[[创建]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x6691_30153_2022256881}[恢复定时器，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[GR recovery timer expired, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_1032207855}

[[GR]{lang="EN-US"}]{#struct_0_x6691_30153_x381896817}[恢复定时器超时，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Created hello timer, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x416810076}

[[创建]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_1274729246}[定时器，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Hello timer expired, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_1136335671}

[[Hello]{lang="EN-US"}]{#struct_0_x6691_30153_1455148598}[定时器超时，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Reset hello timer.]{lang="EN-US"}]{#struct_0_x6691_30153_x416744540}

[[重置]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x6691_30153_x1875991256}[定时器]{style="font-family:宋体"}

[[Created local repair timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_615806838}

[[创建]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x416679004}[本地修复定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Local repair timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1093729508}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1585630439}[本地修复定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Deleted local repair timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1854667893}

[[删除]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x416089180}[本地修复定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Created cleanup timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_1218773486}

[[创建]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_1649845995}[老化定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Reset cleanup timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_249947397}

[[重置]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x416023644}[老化定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Deleted cleanup timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1472891932}

[[删除]{style="font-family:宋体"}[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_845357548}[老化定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Cleanup timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x416613467}

[[PSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1852214000}[老化定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Created path refresh timer for PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_2086433391}

[[创建]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_x416547931}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Reset path refresh timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_528172824}

[[重置]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_x1617640903}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Deleted path refresh timer of PSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x416482395}

[[删除]{style="font-family:宋体"}[path]{lang="EN-US"}]{#struct_0_x6691_30153_x1484330642}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Path refresh timer of PSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_1319748608}

[[path]{lang="EN-US"}]{#struct_0_x6691_30153_x416416859}[刷新定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Created srefresh timer, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_907328470}

[[创建摘要刷新定时器，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_1312171325}[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Deleted srefresh timer, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x416875611}

[[删除摘要刷新定时器，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_2022453489}[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Srefresh timer expired, peer *peer-addr,* interface *interface*.]{lang="EN-US"}]{#struct_0_x6691_30153_x1739094612}

[[摘要刷新定时器超时，邻居地址]{style="font-family:宋体"}*[peer-addr]{lang="EN-US"}*]{#struct_0_x6691_30153_x416810075}[，接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*

[[Created retransmit timer for message ID *message-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_1274663710}

[[为]{style="font-family:宋体"}[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_1454942559}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）创建重传定时器]{style="font-family:宋体"}

[[Retransmit timer of message ID *message-id* expired.]{lang="EN-US"}]{#struct_0_x6691_30153_x416744539}

[[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x1876581073}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）的重传定时器超时]{style="font-family:宋体"}

[[Reset the retransmit timer.]{lang="EN-US"}]{#struct_0_x6691_30153_x416679003}

[[重置重传定时器]{style="font-family:宋体"}]{#struct_0_x6691_30153_x1094057188}

[[The message ID *message-id* has been retransmitted more than *max-num* times, so deleted the message ID.]{lang="EN-US"}]{#struct_0_x6691_30153_912672865}

[[message ID]{lang="EN-US"}]{#struct_0_x6691_30153_x416089179}[（]{style="font-family:宋体"}*[message-id]{lang="EN-US"}*[）重传次数超过]{style="font-family:宋体"}*[max-num]{lang="EN-US"}*[次，删除该]{style="font-family:宋体"}[message ID]{lang="EN-US"}

[[Created cleanup timer for BSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_1218183667}

[[创建]{style="font-family:宋体"}[BSB]{lang="EN-US"}]{#struct_0_x6691_30153_1256498999}[老化定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Reset cleanup timer for BSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.* ]{lang="EN-US"}]{#struct_0_x6691_30153_x416023643}

[[重置]{style="font-family:宋体"}[BSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1472564252}[老化定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Cleanup timer of BSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x416613470}

[[BSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1852672753}[老化定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"} *[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID *tunnel-id*]{lang="EN-US"}

[[Created cleanup timer for RSB: src *src-addr*, LSP ID *lsp-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x927439975}

[[创建]{style="font-family:宋体"}[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_x416547934}[老化定时器，源地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Reset cleanup timer of RSB: src *src-addr*, LSP ID *lsp-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_528500504}

[[重置]{style="font-family:宋体"}[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_x416482398}[老化定时器，源地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Deleted cleanup timer of RSB: src *src-addr*, LSP ID *lsp-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1484527250}

[[删除]{style="font-family:宋体"}[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_x1895846901}[老化定时器，源地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[lsp-id]{lang="EN-US"}*

[[Cleanup timer of RSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x416416862}

[[RSB]{lang="EN-US"}]{#struct_0_x6691_30153_907918297}[老化定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Created resv refresh timer for RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id*.]{lang="EN-US"}]{#struct_0_x6691_30153_x416875614}

[[创建]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_2022650097}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Reset resv refresh timer of RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x416810078}

[[重置]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_1273811742}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Deleted resv refresh timer of RSB: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_428195688}

[[删除]{style="font-family:宋体"}[resv]{lang="EN-US"}]{#struct_0_x6691_30153_x416744542}[刷新定时器，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

[[Resv refresh timer of RSB expired: dst *dst-addr*, src *src-addr*, tunnel ID *tunnel-id.*]{lang="EN-US"}]{#struct_0_x6691_30153_x1876122328}

[[resv]{lang="EN-US"}]{#struct_0_x6691_30153_x416679006}[刷新定时器超时，目的地址]{style="font-family:宋体"}*[dst-addr]{lang="EN-US"}*[，源地址]{style="font-family:宋体"}*[src-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*

**[ ]{lang="EN-US"}**

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6691_30153_x1093860580}

[[\# ]{lang="EN-US"}]{#struct_0_x6691_30153_x1575375315}[打开]{style="font-family:宋体"}[RSVP]{lang="EN-US"}[定时器调试信息开关，第一次收到]{style="font-family:宋体"}[Path]{lang="EN-US"}[和]{style="font-family:宋体"}[Resv]{lang="EN-US"}[消息后打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rsvp timer]{lang="EN-US"}]{#struct_0_x6691_30153_x1863071193}

[\*Aug 19 08:40:42:119 2012 Sysname RSVP/7/TIMER: -MDC=1; Created path refresh timer for PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x645635102}*[为]{style="font-family:宋体"}[PSB]{lang="EN-US"}[创建路径刷新定时器，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:42:119 2012 Sysname RSVP/7/TIMER: -MDC=1; Created cleanup timer for PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.]{lang="EN-US"}]{#struct_0_x6691_30153_2143269822}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1283477636}*[创建]{style="font-family:宋体"}[PSB]{lang="EN-US"}[老化定时器，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:42:120 2012 Sysname RSVP/7/TIMER: -MDC=1; Created cleanup timer for RSB: src 10.11.11.11, LSP ID 18213.]{lang="EN-US"}]{#struct_0_x6691_30153_x416089182}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1218642414}*[创建]{style="font-family:宋体"}[RSB]{lang="EN-US"}[老化定时器，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[18213]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:42:120 2012 Sysname RSVP/7/TIMER: -MDC=1; Created resv refresh timer for RSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.]{lang="EN-US"}]{#struct_0_x6691_30153_80812972}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x1926052271}*[为]{style="font-family:宋体"}[PSB]{lang="EN-US"}[创建]{style="font-family:宋体"}[Resv]{lang="EN-US"}[刷新定时器，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:52:378 2012 Sysname RSVP/7/TIMER: -MDC=1; Path refresh timer of PSB expired: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.]{lang="EN-US"}]{#struct_0_x6691_30153_x788132020}

[*[// PSB]{lang="EN-US"}*]{#struct_0_x6691_30153_1598708530}*[的路径刷新定时器超时，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:52:734 2012 Sysname RSVP/7/TIMER: -MDC=1; Reset cleanup timer of PSB: dst 10.33.33.33, src 10.11.11.11, tunnel ID 1.]{lang="EN-US"}]{#struct_0_x6691_30153_1141683056}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_1013042932}*[重置]{style="font-family:宋体"}[PSB]{lang="EN-US"}[老化定时器，目的地址为]{style="font-family:宋体"}[10.33.33.33]{lang="EN-US"}[，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Aug 19 08:40:52:767 2012 Sysname RSVP/7/TIMER: -MDC=1; Reset cleanup timer of RSB: src 10.11.11.11, LSP ID 18213.]{lang="EN-US"}]{#struct_0_x6691_30153_1065688048}

[*[// ]{lang="EN-US"}*]{#struct_0_x6691_30153_x445862226}*[重置]{style="font-family:宋体"}[RSB]{lang="EN-US"}[老化定时器，源地址为]{style="font-family:宋体"}[10.11.11.11]{lang="EN-US"}[，]{style="font-family:宋体"}[LSP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[18213]{lang="EN-US"}[。]{style="font-family:宋体"}*

**[ ]{lang="EN-US"}**
