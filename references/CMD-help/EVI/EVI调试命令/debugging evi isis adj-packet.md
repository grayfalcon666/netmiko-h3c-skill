::: {#-704754029 .myid}
[]{#_Toc404798217}[]{#struct_0_17822_17521_1234633496}[]{#_Toc312864690}

**EVI \-- EVI调试命令 \-- debugging evi isis adj-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_69765499}

[**[debugging evi isis adj-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **verbose** \]]{lang="EN-US"}[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1954805011}

[**[undo debugging ]{lang="EN-US"}[evi isis adj-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1753012778}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1083129474}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_18178220}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x605488219}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1060279866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x564517933}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_1373196642}

[**[receive]{lang="EN-US"}**]{#struct_0_17822_17521_164884622}[：]{style="font-family:宋体"}[打开接收]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_17822_17521_292849453}[：]{style="font-family:宋体"}[打开发送]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17822_17521_125982074}[：表示显示详细信息，对报文来说显示报文内容。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x483253235}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x605160539}

[**[debugging evi isis adj-packet]{lang="EN-US"}**]{#struct_0_17822_17521_x1215696673}[命令用来打开]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:
宋体"}**[undo debugging ]{lang="EN-US"}[evi isis adj-packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x990255568}[进程的邻居报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17822_17521_469074766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_17822_17521_176928939}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则同时显示打开接收和发送]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定进程号，则表示打开所有进程的邻居报文调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_585507785}

[[表1-1 ]{lang="EN-US"}[debugging evi isis adj-packet]{lang="EN-US"}]{#struct_0_17822_17521_x1450449973}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1771209480}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_522165030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_2142512034}

[[Receive a LAN IIH *String* error. IIH discarded]{lang="EN-US"}]{#struct_0_17822_17521_x605095003}

[[收到]{style="font-family:宋体"}]{#struct_0_17822_17521_1088108420}[Hello]{lang="EN-US"}[报文解析]{style="font-family:宋体"}[TLV]{lang="EN-US"}[时发生错误，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了错误原因]{style="font-family:宋体"}

[[IIH *String* with circuit(*PortName*) mismatch]{lang="EN-US"}]{#struct_0_17822_17521_x2005675399}

[[收到的]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_17822_17521_587902183}[Hello]{lang="EN-US"}[报文的特征与接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*[的特征不匹配，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文与接口不匹配的特征]{lang="EN-US" style="font-family:宋体"}

[[IIH has the same SNPA with a NBR, but different System ID. The NBR will be down]{lang="EN-US"}]{#struct_0_17822_17521_1391701865}

[[收到的]{style="font-family:宋体"}]{#struct_0_17822_17521_x513678409}[Hello]{lang="EN-US"}[报文与已有邻居有相同的]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[地址，但是系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[不同，将这个邻居置]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IIH has the same System ID with a NBR, but different SNPA. The IIH will be discarded]{lang="EN-US"}]{#struct_0_17822_17521_x605291611}

[[收到的]{style="font-family:宋体"}]{#struct_0_17822_17521_x90348197}[Hello]{lang="EN-US"}[报文与已有邻居有相同的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[，但是]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[地址不同，丢弃该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Level-*Number* NBR(*Address*) two way *String*]{lang="EN-US"}]{#struct_0_17822_17521_x326670846}

[[Level-*Number* ]{lang="EN-US"}]{#struct_0_17822_17521_x1907949154}[的邻居]{lang="EN-US" style="font-family:宋体"}[2-Way]{lang="EN-US"}[检查的结果，]{lang="EN-US" style="font-family:宋体"}*[Address]{lang="EN-US"}*[描述了邻居的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了检查结果，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_17822_17521_x680360718}[：通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="EN-US"}]{#struct_0_17822_17521_x605226075}[：不通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[pend]{lang="EN-US"}]{#struct_0_17822_17521_1512692208}[：邻居信息没有收集完整，需要继续等待]{style="font-family:宋体"}

[[System is under disable state, ADJ packet discarded]{lang="EN-US"}]{#struct_0_17822_17521_x271508564}

[[系统处于去使能状态，丢弃]{style="font-family:宋体"}]{#struct_0_17822_17521_1388469642}[ADJ]{lang="EN-US"}[模块收到的报文]{style="font-family:宋体"}

[[Circuit state is not up, ADJ packet discarded]{lang="EN-US"}]{#struct_0_17822_17521_x7453011}

[[接口处于非]{style="font-family:宋体"}]{#struct_0_17822_17521_x604898395}[up]{lang="EN-US"}[状态，丢弃]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块收到的报文]{style="font-family:宋体"}

[[Receive a packet from self, ADJ packet discarded]{lang="EN-US"}]{#struct_0_17822_17521_1857001158}

[[收到的是本设备自己的报文，丢弃]{style="font-family:宋体"}]{#struct_0_17822_17521_1504620665}[ADJ]{lang="EN-US"}[模块收到的报文]{style="font-family:宋体"}

[[Failed to get source MAC address]{lang="EN-US"}]{#struct_0_17822_17521_x118152287}

[[获取源]{style="font-family:宋体"}]{#struct_0_17822_17521_389802204}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Receive a *String* packet from(*Address*) on circuit(*PortName*)]{lang="EN-US"}]{#struct_0_17822_17521_x604832859}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_1166543020}[上从地址]{lang="EN-US" style="font-family:宋体"}*[Address]{lang="EN-US"}*[收到了]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[类型报文，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lan L1 Hello]{lang="EN-US"}]{#struct_0_17822_17521_x1210797832}[：]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Receive unsupport packet *Number*, ADJ packet discarded]{lang="EN-US"}]{#struct_0_17822_17521_702705862}

[[收到了不支持的报文，丢弃]{style="font-family:宋体"}]{#struct_0_17822_17521_x605422686}[ADJ]{lang="EN-US"}[模块收到的报文，]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[描述了报文的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型值]{style="font-family:宋体"}

[[No enough PDU space for *String*]{lang="EN-US"}]{#struct_0_17822_17521_334039091}

[[PDU]{lang="EN-US"}]{#struct_0_17822_17521_x675923212}[长度已经达到最大值，无法继续编码，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了]{style="font-family:宋体"}[PDU]{lang="EN-US"}[达到最大值的时机]{style="font-family:宋体"}

[[Failed to get ADJ pointer failed for *String*]{lang="EN-US"}]{#struct_0_17822_17521_x376670339}

[[获取邻居维护的接口下数据指针失败，]{style="font-family:宋体"}]{#struct_0_17822_17521_x605357150}*[String]{lang="EN-US"}*[描述了失败的时机]{style="font-family:宋体"}

[[No extend VLAN to fill the extend VLAN TLV]{lang="EN-US"}]{#struct_0_17822_17521_1905544940}

[[没有任何扩展]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x489163345}[，所以无法对]{lang="EN-US" style="font-family:宋体"}[Extend-VLAN TLV]{lang="EN-US"}[进行编码]{lang="EN-US" style="font-family:宋体"}

[[No need to set AVF VLAN if not DED]{lang="EN-US"}]{#struct_0_17822_17521_x771960888}

[[不是]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_17822_17521_x605553758}[，无需携带]{style="font-family:宋体"}[AVF VLAN]{lang="EN-US"}[子]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[*[String]{lang="EN-US"}*[ send a hello on circuit(*PortName*) in VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_726432938}

[[DED]{lang="EN-US"}]{#struct_0_17822_17521_x964425296}[在接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}[VLAN *Number*]{lang="EN-US"}[上发送了]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x189831086}[的取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DED]{lang="EN-US"}]{#struct_0_17822_17521_x605488222}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ED]{lang="EN-US"}]{#struct_0_17822_17521_1061000763}

[[DED send hello failed on circuit(*PortName*) in VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_965366738}

[[DED]{lang="EN-US"}]{#struct_0_17822_17521_478941745}[在接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}[VLAN *Number*]{lang="EN-US"}[上发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to get circuit data for Multiport Capability TLV.]{lang="EN-US"}]{#struct_0_17822_17521_309389601}

[[无法获取邻居接口数据，封装多端口能力集]{style="font-family:宋体"}]{#struct_0_17822_17521_1214068728}[TLV]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1912028986}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x605160542}[打开所有进程的接收]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis adj-packet]{lang="EN-US"}]{#struct_0_17822_17521_x1215237926}

[\*Dec 19 11:39:36:066 2011 ]{lang="EN-US"}[Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-0-ADJ: Level-1 NBR(0011.2200.0201) two way pass.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_17822_17521_x1305029350}*[的邻居]{style="font-family:宋体"}[(0011.2200.0201)]{lang="EN-US"}[双向连接检查通过]{style="font-family:宋体"}*

::: {#-1525054557 .myid}
[]{#_Toc404798218}[]{#struct_0_17822_17521_x371472966}[]{#_Toc312864691}

**EVI \-- EVI调试命令 \-- debugging evi isis all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1931144123}

[**[debugging evi isis]{lang="EN-US"}**[ **all** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1169965710}

[**[undo debugging evi isis all ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x605095006}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_1087780740}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_93157141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_1651820731}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_2127897611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_945140157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x847983209}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x2121818856}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x605291614}

[**[debugging evi isis all]{lang="EN-US"}**]{#struct_0_17822_17521_x90675877}[命令用来打开所有与]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程相关的调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis all]{lang="EN-US"}**[命令用来关闭所有与]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程相关的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有与]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_82810460}[进程相关的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的所有调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x746434124}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x942129437}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_1768041021}[打开所有进程的]{style="font-family:宋体"}[所有与]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程相关的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis all]{lang="EN-US"}]{#struct_0_17822_17521_2091305064}
:::

::: {#-116444641 .myid}
[]{#_Toc127096845}[]{#_Toc65310809}[]{#_Toc36367100}[]{#_Toc34185794}[]{#_Toc307924335}[]{#_Ref146536023}[]{#_Toc404798219}[]{#struct_0_17822_17521_x601249448}[]{#_Toc312864692}

**EVI \-- EVI调试命令 \-- debugging evi isis error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_x605226078}

[**[debugging evi isis]{lang="EN-US"}**[ **error** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1513544176}

[**[undo debugging evi isis error ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1310775018}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_17822_17521_156310}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x520960590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_263913923}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_246429812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_821797423}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x153882046}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x604898398}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_1856673478}

[**[debugging evi isis]{lang="EN-US"}[ error]{lang="EN-US"}**]{#struct_0_17822_17521_x1639397641}[命令用来打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程错误调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis]{lang="EN-US"}[ error]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程错误调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x75878766}[进程的错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的错误调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x2097888656}

[[表1-2 ]{lang="EN-US"}[debugging evi isis error]{lang="EN-US"}]{#struct_0_17822_17521_x294587050}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1766509288}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_2122160806}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1991911166}

[[Failed to create *Type* bitmap when *String*]{lang="EN-US"}]{#struct_0_17822_17521_x604832862}

[[创建]{lang="EN-US" style="font-family:
  宋体"}[bitmap]{lang="EN-US"}]{#struct_0_17822_17521_1167132845}[资源失败，]{lang="EN-US" style="font-family:宋体"}*[ String]{lang="EN-US"}*[描述了失败的时机，]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[描述了]{lang="EN-US" style="font-family:宋体"}[bitmap]{lang="EN-US"}[资源的类型，]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值可以如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_17822_17521_x1619510041}[：不活动的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[note]{lang="EN-US"}]{#struct_0_17822_17521_x1331597712}[：记录的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_17822_17521_x127522109}[：添加的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_x622204305}[：删除的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[saved]{lang="EN-US"}]{#struct_0_17822_17521_x605422685}[：保存的]{lang="EN-US" style="font-family:宋体"}

[[Failed to get mac by vlan, ADJ system data is NULL]{lang="EN-US"}]{#struct_0_17822_17521_334104627}

[[通过]{style="font-family:宋体"}]{#struct_0_17822_17521_515801003}[vlan]{lang="EN-US"}[获取]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败，邻居维护的系统数据为空]{style="font-family:宋体"}

[[Failed to add local mac entry, ADJ system data is NULL]{lang="EN-US"}]{#struct_0_17822_17521_1380193294}

[[添加本地]{style="font-family:宋体"}]{#struct_0_17822_17521_x1476787535}[MAC]{lang="EN-US"}[地址失败，邻居维护的系统数据为空]{style="font-family:宋体"}

[[Failed to get local MAC of VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x605357149}

[[获取]{lang="EN-US" style="font-family:
  宋体"}[VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_1905086189}[的本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to create new LAV node]{lang="EN-US"}]{#struct_0_17822_17521_x99218152}

[[创建新的]{style="font-family:宋体"}]{#struct_0_17822_17521_x1563250427}[LAV]{lang="EN-US"}[结点失败]{style="font-family:宋体"}

[[Failed to create bitmap to operate *String*]{lang="EN-US"}]{#struct_0_17822_17521_221442218}

[[创建一个操作类型为]{style="font-family:宋体"}]{#struct_0_17822_17521_x605553757}*[String]{lang="EN-US"}*[的位图失败]{style="font-family:宋体"}

[[Failed to get extend VLAN]{lang="EN-US"}]{#struct_0_17822_17521_727153834}

[[获取扩展]{style="font-family:宋体"}]{#struct_0_17822_17521_x1756400118}[VLAN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Invalid NULL parameter in getting all AVF information]{lang="EN-US"}]{#struct_0_17822_17521_479830868}

[[获取所有]{style="font-family:宋体"}]{#struct_0_17822_17521_x1725194566}[AVF]{lang="EN-US"}[信息时无效的]{style="font-family:宋体"}[NULL]{lang="EN-US"}[参数]{style="font-family:宋体"}

[[Failed to get current LAV when GR finished]{lang="EN-US"}]{#struct_0_17822_17521_x605488221}

[[获取当前]{style="font-family:宋体"}]{#struct_0_17822_17521_1060804155}[LAV]{lang="EN-US"}[失败，当]{style="font-family:宋体"}[GR]{lang="EN-US"}[完成时]{style="font-family:宋体"}

[[Failed to alloc r-mac head while *String*]{lang="EN-US"}]{#struct_0_17822_17521_x1022941901}

[[分配]{lang="EN-US" style="font-family:
  宋体"}[r-mac]{lang="EN-US"}]{#struct_0_17822_17521_709708089}[头空间失败，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了失败的时机]{lang="EN-US" style="font-family:宋体"}

[[Failed to add r-mac vlan entry, vlan: *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x605160541}

[[添加]{lang="EN-US" style="font-family:
  宋体"}[r-mac]{lang="EN-US"}]{#struct_0_17822_17521_x1215172390}[表项失败，]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[Number]{lang="EN-US"}*

[[Failed to create r-mac attribute]{lang="EN-US"}]{#struct_0_17822_17521_1710935022}

[[创建]{style="font-family:宋体"}]{#struct_0_17822_17521_x293314096}[r-mac]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[Failed to notify r-mac message]{lang="EN-US"}]{#struct_0_17822_17521_x605095005}

[[通知]{lang="EN-US" style="font-family:
  宋体"}[r-mac]{lang="EN-US"}]{#struct_0_17822_17521_1087977348}[信息失败]{lang="EN-US" style="font-family:宋体"}

[[LAN ADJ number has arrived max]{lang="EN-US"}]{#struct_0_17822_17521_457364512}

[[LAN ADJ]{lang="EN-US"}]{#struct_0_17822_17521_2026602136}[数据已达最大值]{lang="EN-US" style="font-family:宋体"}

[[Failed to get ADJ pointer when starting hello timer]{lang="EN-US"}]{#struct_0_17822_17521_x605291613}

[[当启动]{style="font-family:宋体"}]{#struct_0_17822_17521_x90479269}[Hello]{lang="EN-US"}[定时间器时，获取]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[维护数据失败]{style="font-family:宋体"}

[[Failed to start Level-*Number* Hello timer ]{lang="EN-US"}]{#struct_0_17822_17521_x486406056}

[[启动]{lang="EN-US" style="font-family:
  宋体"}[Level *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x605226077}[的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to start hold timer]{lang="EN-US"}]{#struct_0_17822_17521_1512561136}

[[启动]{style="font-family:宋体"}]{#struct_0_17822_17521_153653223}[Hold]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to get circuit(*PortName*)\'s priority]{lang="EN-US"}]{#struct_0_17822_17521_x1966539346}

[[获取接口]{style="font-family:宋体"}]{#struct_0_17822_17521_x604898397}*[PortName]{lang="EN-US"}*[优先级失败]{style="font-family:宋体"}

[[Failed to get system\'s area address when encoding AREA]{lang="EN-US"}]{#struct_0_17822_17521_1856870086}

[[获取区域地址失败]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_17822_17521_1487741969}

[[Failed to get circuit(*PortName*)\'s MTU]{lang="EN-US"}]{#struct_0_17822_17521_943319986}

[[获取接口]{lang="EN-US" style="font-family:
  宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_x604832861}[的]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[失败]{lang="EN-US" style="font-family:宋体"}

[*[Type]{lang="EN-US"}*[ send hello failed on circuit(*PortName*) in VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_1167067309}

[[设备类型为]{lang="EN-US" style="font-family:
  宋体"}*[Type]{lang="EN-US"}*]{#struct_0_17822_17521_x818314231}[的设备在接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN *Number*]{lang="EN-US"}[上发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值可以如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DED]{lang="EN-US"}]{#struct_0_17822_17521_x605422688}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ED]{lang="EN-US"}]{#struct_0_17822_17521_334956595}

[[Failed to send hello packet on circuit(*PortName*)]{lang="EN-US"}]{#struct_0_17822_17521_317971941}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_x605357152}[上发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to create hello timer  on circuit(*PortName*)]{lang="EN-US"}]{#struct_0_17822_17521_1905413868}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_1099083465}[上创建]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[定时器失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to notify LAV change message]{lang="EN-US"}]{#struct_0_17822_17521_824703714}

[[通知]{style="font-family:宋体"}]{#struct_0_17822_17521_x605553760}[LAV]{lang="EN-US"}[改变消息失败]{style="font-family:宋体"}

[[Processing interface MTU change error.]{lang="EN-US"}]{#struct_0_17822_17521_726957229}

[[处理接口]{style="font-family:宋体"}]{#struct_0_17822_17521_x2104876318}[MTU]{lang="EN-US"}[变化事件错误]{style="font-family:宋体"}

[[Failed to active the interface(*interface index*).]{lang="EN-US"}]{#struct_0_17822_17521_x605488224}

[[激活接口]{lang="EN-US" style="font-family:宋体"}[(*interface index*)]{lang="EN-US"}]{#struct_0_17822_17521_1060607547}[失败]{lang="EN-US" style="font-family:宋体"}

[[Notify interface delete error on interface: *interface index*]{lang="EN-US"}]{#struct_0_17822_17521_2103935939}

[[通知接口]{lang="EN-US" style="font-family:宋体"}*[interface index]{lang="EN-US"}*]{#struct_0_17822_17521_x605160544}[删除事件错误]{lang="EN-US" style="font-family:宋体"}

[[Invalid phase *phase-number*, ignore event.]{lang="EN-US"}]{#struct_0_17822_17521_x1214844710}

[[无效的]{style="font-family:宋体"}]{#struct_0_17822_17521_77630818}[reset]{lang="EN-US"}[阶段，忽略该事件]{style="font-family:宋体"}

[[Failed to create LSP change notify message.]{lang="EN-US"}]{#struct_0_17822_17521_x605095008}

[[创建]{style="font-family:宋体"}]{#struct_0_17822_17521_1087649668}[LSP]{lang="EN-US"}[变化通知消息失败]{style="font-family:宋体"}

[[PDU level(]{lang="EN-US"}[1) mismatch with circuit level(*CirLevel*).]{lang="EN-US"}]{#struct_0_17822_17521_x605291616}

[[PDU]{lang="EN-US"}]{#struct_0_17822_17521_x90806949}[报文中的]{lang="EN-US" style="font-family:宋体"}[level(1)]{lang="EN-US"}[与接口]{lang="EN-US" style="font-family:宋体"}[level(*CirLevel*)]{lang="EN-US"}[不匹配]{lang="EN-US" style="font-family:宋体"}

[[Failed to set updt socket option.]{lang="EN-US"}]{#struct_0_17822_17521_x834074136}

[[设置]{style="font-family:宋体"}]{#struct_0_17822_17521_x605226080}[updt]{lang="EN-US"}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项失败]{style="font-family:宋体"}

[[Failed to start *Type* timer on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_1513019885}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_1701328217}[上启动定时器失败，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:
  宋体"}*[Type]{lang="EN-US"}*[描述了定时器类型]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x604898400}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_17822_17521_665556669}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x604832864}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP flooding]{lang="EN-US"}]{#struct_0_17822_17521_1167263917}

[[Failed to stop LSP  flood timer on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_x1231310370}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x605422687}[上停止]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[泛洪定时器失败，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{lang="EN-US" style="font-family:宋体"}

[[Failed to stop level-1 timer on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_333973555}

[[在接口]{lang="EN-US" style="font-family:
  宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x605357151}[上停止]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[ever-1]{lang="EN-US"}[定时器失败，]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{lang="EN-US" style="font-family:宋体"}

[[Failed to insert mac to list]{lang="EN-US"}]{#struct_0_17822_17521_1905610476}

[[向链表中添加]{style="font-family:宋体"}]{#struct_0_17822_17521_1826890657}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to update LSP information]{lang="EN-US"}]{#struct_0_17822_17521_x605553759}

[[更新]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_726498474}[信息失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to insert LSP information]{lang="EN-US"}]{#struct_0_17822_17521_x605488223}

[[添加]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1060935227}[信息失败]{lang="EN-US" style="font-family:宋体"}

[[Circuit(*PortName*) is not operationally on, ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_x1021404758}

[[接口]{lang="EN-US" style="font-family:
  宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_x605160543}[处于不可操作状态，忽略]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Failed to obtain IF net index]{lang="EN-US"}]{#struct_0_17822_17521_x1215303462}

[[获取]{lang="EN-US" style="font-family:
  宋体"}[IF net ]{lang="EN-US"}]{#struct_0_17822_17521_x605095007}[索引失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to send PDU, returns *ReturnLength*, buffer length is *Length*.]{lang="EN-US"}]{#struct_0_17822_17521_1087846276}

[[发送报文失败，发送缓冲区大小为]{lang="EN-US" style="font-family:
  宋体"}*[Length]{lang="EN-US"}*]{#struct_0_17822_17521_x605291615}[，返回值为]{lang="EN-US" style="font-family:宋体"}*[ReturnLength]{lang="EN-US"}*[ ]{lang="EN-US"}

[[LSP size(*LspSize*) is larger than circuit MTU(*CirMtu*).]{lang="EN-US"}]{#struct_0_17822_17521_x90610341}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1417511867}[的大小]{lang="EN-US" style="font-family:宋体"}[(*LspSize*)]{lang="EN-US"}[大于接口的]{lang="EN-US" style="font-family:宋体"}[MTU(*CirMtu*) ]{lang="EN-US"}

[[Failed to send LSP]{lang="EN-US"}]{#struct_0_17822_17521_x605226079}

[[发送]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1513478640}[报文失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to send level-*Number*  *Type* PDU]{lang="EN-US"}]{#struct_0_17822_17521_x604898399}

[[发送]{lang="EN-US" style="font-family:
  宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_1856739014}[的]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[类型报文失败]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值可以如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x604832863}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_17822_17521_1167198381}

[[Failed to install LSP with sequence number zero]{lang="EN-US"}]{#struct_0_17822_17521_960661257}

[[安装序号为]{style="font-family:宋体"}]{#struct_0_17822_17521_1769232404}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to *Type*  level-*Number* area address *String*]{lang="EN-US"}]{#struct_0_17822_17521_960726793}

[[操作]{lang="EN-US" style="font-family:
  宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_x589062269}[区域地址]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[失败]{lang="EN-US" style="font-family:宋体"}[,]{lang="EN-US"}[操作类型为]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[，]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值可以如下]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_17822_17521_x1363977523}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_960530185}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Failed to *Type* level- *Number* protocol support *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_17822_17521_1542305458}

[[操作]{lang="EN-US" style="font-family:
  宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_960595721}[的支持的协议类型]{lang="EN-US" style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[(*ProString*)]{lang="EN-US"}[失败，操作类型为]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[ProString]{lang="EN-US"}*]{#struct_0_17822_17521_332636330}[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVI-ISIS]{lang="EN-US"}]{#struct_0_17822_17521_960923401}[：]{style="font-family:宋体"}[EVI]{lang="EN-US"}[ ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown]{lang="EN-US"}]{#struct_0_17822_17521_x754248672}[：]{style="font-family:宋体"}[其它协议]{lang="EN-US" style="font-family:宋体"}

[*[Type]{lang="EN-US"}*]{#struct_0_17822_17521_960988937}[的具体取值可以如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_17822_17521_x1974838285}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_960792329}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Failed to add level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_1798622774}

[[添加]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_960857865}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to delete level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_x351017407}

[[删除]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_961185545}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to modify level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_x45973110}

[[更新]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_961251081}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to add level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_960661258}

[[添加]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_1769232401}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[由]{lang="EN-US" style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的伪节点邻居信息失败]{lang="EN-US" style="font-family:宋体"}

[[Failed to delete level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID.*]{lang="EN-US"}]{#struct_0_17822_17521_960726794}

[[删除]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x589062264}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[由]{lang="EN-US" style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的伪节点邻居信息失败]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1363780915}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_879067632}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis error]{lang="EN-US"}]{#struct_0_17822_17521_960530186}

[\*Mar 18 14:28:41:744 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-101-ERR: Failed to send level-1 CSNP PDU.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_1542305457}*[发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文失败]{style="font-family:宋体"}*

::: {#-534665538 .myid}
[]{#_Toc404798220}[]{#struct_0_17822_17521_x1699289558}[]{#_Toc312864693}

**EVI \-- EVI调试命令 \-- debugging evi isis event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1390751767}

[**[debugging evi isis]{lang="EN-US"}**[ **event** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1425335223}

[**[undo debugging evi isis]{lang="EN-US"}**[ **event** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_985519668}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x309885088}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_2030188789}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_960595722}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_332636333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1941932237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x814458504}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_952072053}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_252137891}

[**[debugging evi isis event]{lang="EN-US"}**]{#struct_0_17822_17521_251841428}[命令用来打开]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程事件调试信息开关。]{style="font-family:
宋体"}**[undo debugging evi isis event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x692335733}[进程的事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的事件调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_412844977}

[[表1-3 ]{lang="EN-US"}[debugging evi isis event]{lang="EN-US"}]{#struct_0_17822_17521_960923402}[命令输出的信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1782764008}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x754248675}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_821663417}

[[Failed to get local MAC of VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_1791750367}

[[在]{style="font-family:宋体"}[VLAN *Number*]{lang="EN-US"}]{#struct_0_17822_17521_1489066053}[上获取本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Clear all AVF in circuit *PortName*]{lang="EN-US"}]{#struct_0_17822_17521_780951723}

[[清除接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_2119788437}[上所有]{style="font-family:宋体"} [的]{style="font-family:宋体"}[AVF]{lang="EN-US"}

[[DED changed on *PortName*: old DED: *String*, new DED: *String*]{lang="EN-US"}]{#struct_0_17822_17521_960988938}

[[接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_x1974838300}[所属网段的]{style="font-family:宋体"}[DED]{lang="EN-US"}[发生改变，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了以前的]{style="font-family:宋体"}[DED]{lang="EN-US"}[和新的]{style="font-family:宋体"}[DED]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[System\'s state is disable]{lang="EN-US"}]{#struct_0_17822_17521_x1873191999}

[[系统处于去使能状态]{style="font-family:宋体"}]{#struct_0_17822_17521_1748067102}

[[Update proccess(*Number*) configuration to DBM]{lang="EN-US"}]{#struct_0_17822_17521_1213070542}

[[更新进程]{style="font-family:宋体"}[(*Number*)]{lang="EN-US"}]{#struct_0_17822_17521_960792330}[的配置数据到]{style="font-family:宋体"}[DBM]{lang="EN-US"}

[[Notify extended VLAN configuration]{lang="EN-US"}]{#struct_0_17822_17521_x540029377}

[[通知配置扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x854119973}

[[Evilink Interface is deleted successfully]{lang="EN-US"}]{#struct_0_17822_17521_x331931074}

[[EVI-Link]{lang="EN-US"}]{#struct_0_17822_17521_x1832161704}[接口删除成功]{style="font-family:宋体"}

[[Notifing the tunnel interface state changed]{lang="EN-US"}]{#struct_0_17822_17521_960857866}

[[通知]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_17822_17521_x351017404}[接口状态改变]{style="font-family:宋体"}

[[Notifing the evi-link interface state changed]{lang="EN-US"}]{#struct_0_17822_17521_x2068266648}

[[通知]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_17822_17521_1718058702}[接口状态改变]{style="font-family:宋体"}

[[Refresh the interface parameter on interface: *interface-index*]{lang="EN-US"}]{#struct_0_17822_17521_x1238193668}

[[刷新]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_961185546}[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[下保存的接口的各种参数]{style="font-family:宋体"}

[[Interface *Portname* is created successfully]{lang="EN-US"}]{#struct_0_17822_17521_x45973109}

[[接口]{style="font-family:宋体"}*[Portname]{lang="EN-US"}*]{#struct_0_17822_17521_x640385510}[创建成功]{style="font-family:宋体"}

[[Interface *Portname* is deleted successfully]{lang="EN-US"}]{#struct_0_17822_17521_415347514}

[[接口]{style="font-family:宋体"}*[Portname]{lang="EN-US"}*]{#struct_0_17822_17521_961251082}[删除成功]{style="font-family:宋体"}

[[LSP MTU change from *value1* to *value2*, notify UPDT MTU change.]{lang="EN-US"}]{#struct_0_17822_17521_x932240725}

[[通知]{style="font-family:宋体"}[UPDT]{lang="EN-US"}]{#struct_0_17822_17521_x1315773969}[模块]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文发送的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大小由]{style="font-family:宋体"}*[value1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[value2]{lang="EN-US"}*

[[Delete interface *interface-index* data from DBM *bActive*]{lang="EN-US"}]{#struct_0_17822_17521_x168561446}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_17822_17521_960661255}[删除接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[下的参数，接口的状态为]{style="font-family:宋体"}*[bActive]{lang="EN-US"}*

[[Receive Delete circuit ack event, flag is *bDel*]{lang="EN-US"}]{#struct_0_17822_17521_1769232406}

[[收到一个删除接口应答事件，标志为]{style="font-family:宋体"}[bDel]{lang="EN-US"}]{#struct_0_17822_17521_542850371}

[[Reset finished, process with reset code *reason-code.*]{lang="EN-US"}]{#struct_0_17822_17521_1073381651}

[[复位完成，处理原因码]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*]{#struct_0_17822_17521_960726791}[引起的复位。目前存在如下原因码：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_x589062267}[：]{lang="EN-US" style="font-family:宋体"}[reset evi isis]{lang="EN-US"}[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_x1363584307}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_1502047008}[：]{lang="EN-US" style="font-family:宋体"}[EVI]{lang="EN-US"}[ ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_17822_17521_960530183}[：协议进程降级引起的复位]{style="font-family:宋体"}

[[Receive *string* event on interface: *interface-index.*]{lang="EN-US"}]{#struct_0_17822_17521_1542305452}

[[在接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_17822_17521_x1699092950}[上收到如下事件：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[board insert  event]{lang="EN-US"}]{#struct_0_17822_17521_113883654}[：板插入事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[board remove event]{lang="EN-US"}]{#struct_0_17822_17521_960595719}[：板拔出事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface add event]{lang="EN-US"}]{#struct_0_17822_17521_1906614434}[：接口添加事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface delete event]{lang="EN-US"}]{#struct_0_17822_17521_x658835951}[：接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN \--\> UP event]{lang="EN-US"}]{#struct_0_17822_17521_960923399}[：接口]{lang="EN-US" style="font-family:
  宋体"}[UP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP \--\> DOWN event]{lang="EN-US"}]{#struct_0_17822_17521_1971899681}[：接口]{lang="EN-US" style="font-family:
  宋体"}[DOWN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[speed change event]{lang="EN-US"}]{#struct_0_17822_17521_1828002452}[：接口速率变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MTU change event]{lang="EN-US"}]{#struct_0_17822_17521_960988935}[：]{lang="EN-US" style="font-family:
  宋体"}[MTU]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN add event]{lang="EN-US"}]{#struct_0_17822_17521_x1974838287}[：接口加入]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN delete event]{lang="EN-US"}]{#struct_0_17822_17521_x306583769}[：接口离开]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AVF VLAN change event]{lang="EN-US"}]{#struct_0_17822_17521_645430442}[：接口的]{lang="EN-US" style="font-family:
  宋体"}[AVF]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[designated VLAN change event]{lang="EN-US"}]{#struct_0_17822_17521_960792327}[：接口的指定]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[Reset change into phase *phase-code*.]{lang="EN-US"}]{#struct_0_17822_17521_1798622788}

[[复位进入]{style="font-family:宋体"}*[phase-code]{lang="EN-US"}*]{#struct_0_17822_17521_x193761476}[阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_960857863}[：]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_x351017401}[：]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_x2068070040}[：]{lang="EN-US" style="font-family:宋体"}[FINAL]{lang="EN-US"}

[[Reset processing with backinfo: module *module-number*, event *event-number*, phase *phase-code*.]{lang="EN-US"}]{#struct_0_17822_17521_961185543}

[[处理其他模块回复的]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_17822_17521_x45973112}[完成事件。]{style="font-family:宋体"}

[*[module-number]{lang="EN-US"}*]{#struct_0_17822_17521_1315929619}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_961251079}[：]{lang="EN-US" style="font-family:宋体"}[ADJ]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_x1741544800}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_1172876497}[：]{lang="EN-US" style="font-family:宋体"}[DEC]{lang="EN-US"}[模块]{lang="EN-US" style="font-family:宋体"}

[*[event-number]{lang="EN-US"}*]{#struct_0_17822_17521_960661256}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_1769232403}[：]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_960726792}[：]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_x589062270}[：]{lang="EN-US" style="font-family:宋体"}[ENABLE]{lang="EN-US"}

[*[phase-code]{lang="EN-US"}*]{#struct_0_17822_17521_x1363518770}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_960530184}[：]{lang="EN-US" style="font-family:宋体"}[STOP WORK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_1542305459}[：]{lang="EN-US" style="font-family:宋体"}[DISABLE]{lang="EN-US"}

[[Reset processing receive event *event-type*.]{lang="EN-US"}]{#struct_0_17822_17521_x1698372054}

[[收到复位事件，事件类型码为]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*]{#struct_0_17822_17521_960595720}[。目前存在如下复位类型码：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_332636331}[：]{lang="EN-US" style="font-family:宋体"}[reset ]{lang="EN-US"}[evi isis all]{lang="EN-US"}[命令引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_1941932239}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号翻转引起的复位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_960923400}[：]{lang="EN-US" style="font-family:宋体"}[EVI]{lang="EN-US"}[ ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址变化引起的复位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_17822_17521_x754248673}[：协议进程降级引起的复位]{style="font-family:宋体"}

[[VLAN config change notify]{lang="EN-US"}]{#struct_0_17822_17521_960988936}

[[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1974838286}[配置改变]{style="font-family:宋体"}

[[Reset start up.]{lang="EN-US"}]{#struct_0_17822_17521_1259500172}

[[复位开始]{style="font-family:宋体"}]{#struct_0_17822_17521_960792328}

[[Flushed Delete_Map event { *interface-name* Remote VLAN *IDR* \--\> Local VLAN *IDL* } to driver]{lang="EN-US"}]{#struct_0_17822_17521_309455135}

[[下刷驱动删除接口上的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1228874766}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_309389599}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDR]{lang="EN-US"}*]{#struct_0_17822_17521_74951819}[：远端]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDL]{lang="EN-US"}*]{#struct_0_17822_17521_1918751632}[：本地]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Flushed Add_Map event { *interface-name* Remote VLAN *IDR* \--\> Local VLAN *IDL* } to driver]{lang="EN-US"}]{#struct_0_17822_17521_309324063}

[[下刷驱动添加接口上的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_440094698}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_309258527}[：接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDR]{lang="EN-US"}*]{#struct_0_17822_17521_x755847584}[：远端]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDL]{lang="EN-US"}*]{#struct_0_17822_17521_309717279}[：本地]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Associated with a track entry]{lang="EN-US"}]{#struct_0_17822_17521_237659855}

[[关联了]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_17822_17521_309651743}

[[Static MAC filtering policy changed]{lang="EN-US"}]{#struct_0_17822_17521_x981285586}

[[本地静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17822_17521_752061255}[地址的过滤规则发生改变]{style="font-family:宋体"}

[[Dynamic MAC filtering policy changed]{lang="EN-US"}]{#struct_0_17822_17521_309586207}

[[本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17822_17521_x841587322}[地址的过滤规则发生改变]{style="font-family:宋体"}

[[Updated VLAN mapping data to DBM.]{lang="EN-US"}]{#struct_0_17822_17521_309520671}

[[更新]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_305346846}[映射数据到]{style="font-family:宋体"}[DBM]{lang="EN-US"}

[[Updated RMAC {SiteID *IDS* Remote VLAN *IDR* \--\> Local VLAN *IDL*}]{lang="EN-US"}]{#struct_0_17822_17521_309979423}

[[根据]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x402120007}[映射更新远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDS]{lang="EN-US"}*]{#struct_0_17822_17521_309913887}[：站点]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDR]{lang="EN-US"}*]{#struct_0_17822_17521_x1923962053}[：远端]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IDL]{lang="EN-US"}*]{#struct_0_17822_17521_209846236}[：本地]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Notified other modules of preferred VLAN configuration change.]{lang="EN-US"}]{#struct_0_17822_17521_309455132}

[[通知]{style="font-family:宋体"}[AEF]{lang="EN-US"}]{#struct_0_17822_17521_x1228874761}[优先级配置变化]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_1798622775}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x193958097}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis event]{lang="EN-US"}]{#struct_0_17822_17521_x511671877}

[\*Jun  8 08:29:44:658 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-101-EVT: Notifing the tunnel interface state changed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_1090674246}*[通知]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口状态改变]{style="font-family:宋体"}*

::: {#-120743162 .myid}
[]{#_Toc404798221}[]{#struct_0_17822_17521_945629907}[]{#_Toc312864694}

**EVI \-- EVI调试命令 \-- debugging evi isis graceful-restart**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_960857864}

[**[debugging evi isis graceful-restart ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x351017406}

[**[undo debugging evi isis graceful-restart ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x2068397720}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x495025598}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1929215223}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1257018343}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_136168800}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1337610574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x15924643}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_961185544}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x45973111}

[**[debugging evi isis graceful-restart]{lang="EN-US"}**]{#struct_0_17822_17521_1315929618}[命令用来打开进程的平滑重启调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis graceful-restart]{lang="EN-US"}**[命令用来关闭进程的平滑重启调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_496120892}[进程的平滑重启调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的平滑重启调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x248866251}

[[表1-4 ]{lang="EN-US"}[debugging evi isis graceful-restart]{lang="EN-US"}]{#struct_0_17822_17521_568415787}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1809455272}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_191153180}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_961251080}

[[Graceful-restart complete]{lang="EN-US"}]{#struct_0_17822_17521_x932240727}

[[平滑重启完成]{style="font-family:宋体"}]{#struct_0_17822_17521_x1315905041}

[[T3 timer is stoped]{lang="EN-US"}]{#struct_0_17822_17521_x1844303264}

[[T3]{lang="EN-US"}]{#struct_0_17822_17521_583748305}[定时器停止]{style="font-family:宋体"}

[[T3 timer expired before T2 timer]{lang="EN-US"}]{#struct_0_17822_17521_1013348665}

[[T3]{lang="EN-US"}]{#struct_0_17822_17521_960661253}[定时器在]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器之前失效]{style="font-family:宋体"}

[[Level-*Number* T2 timer expired]{lang="EN-US"}]{#struct_0_17822_17521_1769232408}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_542981443}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器失效]{style="font-family:宋体"}

[[Graceful-restart enter *Type*]{lang="EN-US"}]{#struct_0_17822_17521_x2019078391}

[[平滑重启进入]{style="font-family:宋体"}*[Type]{lang="EN-US"}*]{#struct_0_17822_17521_1719292483}[阶段，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[指示了类型可以取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starting]{lang="EN-US"}]{#struct_0_17822_17521_389225512}[：启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[restarting]{lang="EN-US"}]{#struct_0_17822_17521_960726789}[：重启]{lang="EN-US" style="font-family:宋体"}

[[Recieve T2 timer cancel event]{lang="EN-US"}]{#struct_0_17822_17521_1749589901}

[[收到]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_17822_17521_x1564451675}[定时器取消事件]{style="font-family:宋体"}

[[Level-*Number* T2 timer is stopped]{lang="EN-US"}]{#struct_0_17822_17521_1236916803}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_x1557452098}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器停止]{style="font-family:宋体"}

[[Receive module(*Mid*) phase(*Phase*), current phase(*GrPhase*)]{lang="EN-US"}]{#struct_0_17822_17521_960530181}

[[收到模块]{style="font-family:宋体"}*[Mid]{lang="EN-US"}*]{#struct_0_17822_17521_1542305454}[的状态]{style="font-family:宋体"}*[Phase]{lang="EN-US"}*[，当前]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态是]{style="font-family:宋体"}*[GrPhase]{lang="EN-US"}*

[[Stop level-*Number* T1 timer]{lang="EN-US"}]{#struct_0_17822_17521_x1699224022}

[[停止]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_x2036153274}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[Recieve hello with *Type* bit set from circuit: *PortName* Level- *Number*]{lang="EN-US"}]{#struct_0_17822_17521_960595717}

[[从接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_1906614448}[收到]{style="font-family:宋体"}[hello]{lang="EN-US"}[报文中]{style="font-family:宋体"}[level- *Number*]{lang="EN-US"}[的]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[位置位，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[位可以取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RR]{lang="EN-US"}]{#struct_0_17822_17521_x658573808}[：重启请求位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RA]{lang="EN-US"}]{#struct_0_17822_17521_x1184852840}[：重启抑制位]{lang="EN-US" style="font-family:宋体"}

[[Failed to purge level-*Number* LSP]{lang="EN-US"}]{#struct_0_17822_17521_960923397}

[[清除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_1971899675}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Begin to purge local level-*Number* LSP]{lang="EN-US"}]{#struct_0_17822_17521_1828264593}

[[开始清除本地的]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_306667949}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Purge level-*Number* LSP *PseudoId*-*LspNum*]{lang="EN-US"}]{#struct_0_17822_17521_x1760683194}

[[清除]{style="font-family:宋体"}[level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_960988933}[的]{style="font-family:宋体"}[LSP *PseudoId*-*LspNum*]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[End to purge local level-*Number* LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1974838289}

[[结束清除本地的]{style="font-family:宋体"}[level-*Number* LSP]{lang="EN-US"}]{#struct_0_17822_17521_499985285}[报文]{style="font-family:宋体"}

[[Level-*Number* LSDB synchronization is complete]{lang="EN-US"}]{#struct_0_17822_17521_960792325}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_1798622786}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[Level-*Number* CSNP set synchronization is complete on circuit *PortName*]{lang="EN-US"}]{#struct_0_17822_17521_x194154692}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_2036594695}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[设置同步完成在接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[上]{style="font-family:宋体"}

[[Level-*Number* LSDB synchronization is complete]{lang="EN-US"}]{#struct_0_17822_17521_960857861}

[[Level-*Number*]{lang="EN-US"}]{#struct_0_17822_17521_x351017403}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}

[[EVIISIS-*Number*-GR: Interface(*interface-index*) level-*Number* T1 timer expired count: *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x2068201112}

[[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_17822_17521_1862937211}[下，]{style="font-family:宋体"}[Level-*Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[次]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_961185541}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x45973114}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的平滑重启调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis graceful-restart]{lang="EN-US"}]{#struct_0_17822_17521_1315929613}

[\*Mar 17 14:25:11:744 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-101-GR: Level- 1  LSDB synchronization is complete.]{lang="EN-US"}

[*[// Level-1]{lang="EN-US"}*]{#struct_0_17822_17521_495531068}*[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步完成]{style="font-family:宋体"}*

::: {#-1958575208 .myid}
[]{#_Toc404798222}[]{#struct_0_17822_17521_x1347874825}[]{#_Toc312864695}

**EVI \-- EVI调试命令 \-- debugging evi isis ha**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1427733975}

[**[debugging evi isis ha]{lang="EN-US"}**]{#struct_0_17822_17521_x745041577}

[**[undo debugging evi isis ha]{lang="EN-US"}**]{#struct_0_17822_17521_961251077}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1741544794}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x796033216}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x41564304}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x2093583086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_649589972}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_51782335}

[**[debugging evi isis ha]{lang="EN-US"}**]{#struct_0_17822_17521_912103779}[命令用来打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis ha]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议]{style="font-family:宋体"}[HA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS HA]{lang="EN-US"}]{#struct_0_17822_17521_960661254}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging evi isis ha]{lang="EN-US"}]{#struct_0_17822_17521_1769232405}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1807473160}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_542653763}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x1897091419}

[[Failed to initialize the PUBLISH when HA]{lang="EN-US"}]{#struct_0_17822_17521_x1549150160}

[[初始化发布事件失败，当]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x2005154855}[时]{style="font-family:宋体"}

[[Real time backup *string.*]{lang="EN-US"}]{#struct_0_17822_17521_x1171508182}

[[实时备份]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_960726790}[的各种配置和属性信息。]{style="font-family:宋体"}*[String]{lang="EN-US"}*[列表：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[eviisis(*Number*) process debugging information]{lang="EN-US"}]{#struct_0_17822_17521_x589062268}[：进程调试信息，]{lang="EN-US" style="font-family:宋体"}*[Number]{lang="EN-US"}*[：为进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[eviisis system debugging information]{lang="EN-US"}]{#struct_0_17822_17521_x1364043059}[：系统调试信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process(*Number*)]{lang="EN-US"}]{#struct_0_17822_17521_233257680}[：进程配置，]{lang="EN-US" style="font-family:宋体"}*[Number]{lang="EN-US"}*[：为进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface]{lang="EN-US"}]{#struct_0_17822_17521_1993285511}[：接口配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process view]{lang="EN-US"}]{#struct_0_17822_17521_960530182}[：进程视图]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[process enable]{lang="EN-US"}]{#struct_0_17822_17521_1542305453}[：]{lang="EN-US" style="font-family:宋体"}[EVI]{lang="EN-US"}[ ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[进程使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[designated vlan]{lang="EN-US"}]{#struct_0_17822_17521_x1699027414}[：指定]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[graceful-restart]{lang="EN-US"}]{#struct_0_17822_17521_x1367865184}[：平滑重启]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[graceful-restart Interval]{lang="EN-US"}]{#struct_0_17822_17521_x286898111}[：平滑重启时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP life time]{lang="EN-US"}]{#struct_0_17822_17521_960595718}[：]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[生命周期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP refresh interval]{lang="EN-US"}]{#struct_0_17822_17521_1906614435}[：]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[刷新间隔]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log peer change]{lang="EN-US"}]{#struct_0_17822_17521_x658901487}[：邻居状态显示信息]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extend vlan]{lang="EN-US"}]{#struct_0_17822_17521_1968275034}[：扩展]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DED priority]{lang="EN-US"}]{#struct_0_17822_17521_1053727506}[：]{lang="EN-US" style="font-family:宋体"}[DED]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[hello  time interval]{lang="EN-US"}]{#struct_0_17822_17521_960923398}[：]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP interval]{lang="EN-US"}]{#struct_0_17822_17521_1971899680}[：发送]{lang="EN-US" style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello lapse number]{lang="EN-US"}]{#struct_0_17822_17521_1828067988}[：邻居的]{lang="EN-US" style="font-family:
  宋体"}[Hello]{lang="EN-US"}[报文失效数目]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP throttle time and LSP throttle count]{lang="EN-US"}]{#struct_0_17822_17521_x2098151619}[：发送链路状态报文的最小时间间隔和一次最多发送的链路状态报文的数目]{lang="EN-US" style="font-family:宋体"}

[[Receive HA *string* event.]{lang="EN-US"}]{#struct_0_17822_17521_x855589505}

[[收到]{style="font-family:宋体"}[HA *string*]{lang="EN-US"}]{#struct_0_17822_17521_960988934}[通知事件，事件列表：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EPOLLUP]{lang="EN-US"}]{#struct_0_17822_17521_x1974838288}[：]{lang="EN-US" style="font-family:宋体"}[epoll HUP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[batch backup]{lang="EN-US"}]{#struct_0_17822_17521_2066069226}[：批量备份事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stop]{lang="EN-US"}]{#struct_0_17822_17521_x2142169328}[：进程停止事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[degrade]{lang="EN-US"}]{#struct_0_17822_17521_960792326}[：降级事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[upgrade]{lang="EN-US"}]{#struct_0_17822_17521_1798622789}[：升级事件]{lang="EN-US" style="font-family:宋体"}

[[Reconnecting to HA daemon, Please wait\...]{lang="EN-US"}]{#struct_0_17822_17521_x193695940}

[[重新连接]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x140213188}[模块，请等待]{style="font-family:宋体"}[...]{lang="EN-US"}

[[Receive EVI-ISIS real-time backup data.]{lang="EN-US"}]{#struct_0_17822_17521_960857862}

[[收到]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x351017400}[实备数据]{style="font-family:宋体"}

[[Receive EVI-ISIS batch backup data.]{lang="EN-US"}]{#struct_0_17822_17521_x2068004504}

[[收到]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_294207809}[批量备份数据]{style="font-family:宋体"}

[[Send batch backup data to slave board.]{lang="EN-US"}]{#struct_0_17822_17521_961185542}

[[发送批量备份数据到备板]{style="font-family:宋体"}]{#struct_0_17822_17521_x45973113}

[[External Deinit]{lang="EN-US"}]{#struct_0_17822_17521_1315929620}

[[去初始化]{style="font-family:宋体"}]{#struct_0_17822_17521_495596601}

[[Notifying thread to stop work.]{lang="EN-US"}]{#struct_0_17822_17521_961251078}

[[通知线程停止工作]{style="font-family:宋体"}]{#struct_0_17822_17521_x1741544799}

[[Processing the HA upgrade.]{lang="EN-US"}]{#struct_0_17822_17521_x36518329}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x1411991738}[升级事件]{style="font-family:宋体"}

[[HA smooth end]{lang="EN-US"}]{#struct_0_17822_17521_x1111147646}

[[HA]{lang="EN-US"}]{#struct_0_17822_17521_796241863}[平滑结束]{style="font-family:宋体"}

[[HA smooth start]{lang="EN-US"}]{#struct_0_17822_17521_x1411926202}

[[HA]{lang="EN-US"}]{#struct_0_17822_17521_1926480462}[平滑开始]{style="font-family:宋体"}

[[No process found. HA smooth ended]{lang="EN-US"}]{#struct_0_17822_17521_1043084122}

[[不存在任何进程实例，]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x445025940}[平滑结束]{style="font-family:宋体"}

[[External init when HA]{lang="EN-US"}]{#struct_0_17822_17521_x1412122810}

[[初始化]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x1724011681}[时]{style="font-family:宋体"}

[[Notifying thread to start work.]{lang="EN-US"}]{#struct_0_17822_17521_x2105770624}

[[通知线程开始工作]{style="font-family:宋体"}]{#struct_0_17822_17521_x1412057274}

[[Start up EVI-ISIS protocol process when HA upgrade.]{lang="EN-US"}]{#struct_0_17822_17521_x382535746}

[[开始启动]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_334072790}[协议进程当]{style="font-family:宋体"}[HA]{lang="EN-US"}[升级时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1420299152}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1411729594}[打开]{style="font-family:宋体"}[EVI IS-IS HA]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis ha]{lang="EN-US"}]{#struct_0_17822_17521_1714346263}

[\*Jun  3 09:56:15:006 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-101-HA: Receive HA upgrade event.]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_17822_17521_1428090495}*[收到]{style="font-family:宋体"}[HA]{lang="EN-US"}[升级事件]{style="font-family:宋体"}*

::: {#915469014 .myid}
[]{#_Toc312864696}[]{#_Toc404798223}[]{#struct_0_17822_17521_x495504425}

**EVI \-- EVI调试命令 \-- debugging evi isis local-mac**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1153173392}

[**[debugging evi isis local-mac]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1834273956}

[**[undo debugging evi isis local-mac]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1828927157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_674872867}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1411664058}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_17822_17521_2633842}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1039330859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x110815941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_948318446}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_1549952969}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1390323330}

[**[debugging evi isis local-mac]{lang="EN-US"}**]{#struct_0_17822_17521_1954530551}[命令用来打开]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程的本地]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址信息调试信息开关。用于调试驱动上报的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息使用。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging evi isis local-mac**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x1411860666}[进程的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17822_17521_260469962}[地址信息调试信息开关。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging evi isis local-mac]{lang="EN-US"}]{#struct_0_17822_17521_x1283903201}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1796312968}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x429180849}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x1717632815}

[[Receive local MAC, Operation type:O*pType*, MAC type:*MacType*, ifIndex:*ifIndex*, VLAN: *Number*, MAC: *MacAddr*.]{lang="FR"}]{#struct_0_17822_17521_x700728529}

[[收到本地]{style="font-family:宋体"}]{#struct_0_17822_17521_743020122}[MAC]{lang="FR"}[地址信息，]{style="font-family:宋体"}[VLAN]{lang="FR"}[为]{style="font-family:宋体"}*[Number]{lang="FR"}*[，]{style="font-family:宋体"}[MAC]{lang="FR"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="FR"}*[，操作类型为]{style="font-family:宋体"}*[OpType]{lang="FR"}*[，]{style="font-family:宋体"}*[OpType]{lang="FR"}*[的取值可以如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="FR"}]{#struct_0_17822_17521_x1411795130}[：添加]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_17822_17521_x919103824}[：删除]{lang="EN-US" style="font-family:宋体"}

[[MAC]{lang="EN-US"}]{#struct_0_17822_17521_867529799}[地址类型为]{style="font-family:宋体"}*[MacType]{lang="EN-US"}*[，]{style="font-family:宋体"}*[MacType]{lang="EN-US"}*[的取值可以如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_17822_17521_1971099103}[：动态]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[static]{lang="EN-US"}]{#struct_0_17822_17521_x128181356}[：静态]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nonadvertised]{lang="EN-US"}]{#struct_0_17822_17521_736916845}[：非发布]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1411467450}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x492336234}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis local-mac]{lang="EN-US"}]{#struct_0_17822_17521_538578685}

[\*Jun  3 09:56:15:911 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1; ]{lang="EN-US"}

[Receive local MAC, Operation type:add, MAC type:dynamic, ifIndex:0x1111, VLAN: 2, MAC: aa-bb-cc.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1706143672}*[收到本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[，操作类型为]{style="font-family:宋体"}[add]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[类型为]{style="font-family:宋体"}[dynamic]{lang="EN-US"}[，]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}[为]{style="font-family:宋体"}[0x1111]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[aa-bb-cc]{lang="EN-US"}*

::: {#1393998550 .myid}
[]{#_Toc404798224}[]{#struct_0_17822_17521_x1774479658}

**EVI \-- EVI调试命令 \-- debugging evi isis misc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1220716560}

[**[debugging evi isis misc]{lang="EN-US"}**]{#struct_0_17822_17521_x561362353}

[**[undo debugging evi isis misc]{lang="EN-US"}**]{#struct_0_17822_17521_x1411401914}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_718769633}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_1805534717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1889208908}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x137004847}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1057689407}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1373350644}

[**[debugging evi isis misc]{lang="EN-US"}**]{#struct_0_17822_17521_x521644399}[命令用来打开与进程无关的其它调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis misc]{lang="EN-US"}**[命令用来关闭与进程无关的其它调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x517787850}[的与进程无关的其它调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging evi isis misc]{lang="EN-US"}]{#struct_0_17822_17521_x1411991737}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1795486344}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1870662533}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x286364844}

[[Failed to receive local mac message]{lang="EN-US"}]{#struct_0_17822_17521_x833939719}

[[接收本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17822_17521_1992037174}[消息失败]{style="font-family:宋体"}

[[Failed to create bitmap for publishing LAV]{lang="EN-US"}]{#struct_0_17822_17521_350408013}

[[发布]{style="font-family:宋体"}[LAV]{lang="EN-US"}]{#struct_0_17822_17521_x1411926201}[时创建位图资源失败]{style="font-family:宋体"}

[[Publish batch Lav info]{lang="EN-US"}]{#struct_0_17822_17521_360396521}

[[批量下发]{style="font-family:宋体"}[LAV]{lang="EN-US"}]{#struct_0_17822_17521_465133926}[信息]{style="font-family:宋体"}

[[Send Lav notify message, event: *EventType*, tunnel index: ]{lang="EN-US"}*[TunnelIndex]{lang="EN-US"}*]{#struct_0_17822_17521_x1437319131}

[[发送]{style="font-family:宋体"}[LAV]{lang="EN-US"}]{#struct_0_17822_17521_860053369}[通知事件消息，事件类型为]{style="font-family:宋体"}*[EventType]{lang="EN-US"}*[，]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[接口索引为]{style="font-family:宋体"}*[TunnelIndex]{lang="EN-US"}*[，]{style="font-family:宋体"}*[EventType]{lang="EN-US"}*[的取值可以如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADD]{lang="EN-US"}]{#struct_0_17822_17521_x1412122809}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEL]{lang="EN-US"}]{#struct_0_17822_17521_198368156}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Failed to *Opt* VLAN on port, error: ]{lang="EN-US"}*[ErrorCode]{lang="EN-US"}*[, EVI link index:]{lang="EN-US"}*[ IfIndex]{lang="EN-US"}*]{#struct_0_17822_17521_226618309}

[[在接口上操作]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1155554110}[失败，错误码为]{style="font-family:宋体"}*[ErrorCode]{lang="EN-US"}*[，]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[IfIndex]{lang="EN-US"}*[，操作类型为]{style="font-family:宋体"}*[Opt]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Opt]{lang="EN-US"}*[的取值可以如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_17822_17521_605772380}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_x1412057273}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Process(*PorcId*) is created successfully]{lang="EN-US"}]{#struct_0_17822_17521_x785820273}

[[进程]{style="font-family:宋体"}[(]{lang="EN-US"}]{#struct_0_17822_17521_x1226685076}*[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}*[)]{lang="EN-US"}[创建成功]{style="font-family:宋体"}

[[Update EVI-ISIS Designated Vlan  to DBM]{lang="EN-US"}]{#struct_0_17822_17521_x785894975}

[[更新指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1411729593}[数据到]{style="font-family:宋体"}[DBM]{lang="EN-US"}

[[Failed to create bitmap]{lang="EN-US"}]{#struct_0_17822_17521_148262322}

[[创建]{style="font-family:宋体"}[bitmap]{lang="EN-US"}]{#struct_0_17822_17521_x362937709}[资源失败]{style="font-family:宋体"}

[[Failed to connect to *String* ]{lang="EN-US"}]{#struct_0_17822_17521_x1903734298}

[[连接]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_107561454}[模块失败，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了模块的类型]{style="font-family:宋体"}

[[Send HA response(*String*) error]{lang="EN-US"}]{#struct_0_17822_17521_x1411664057}

[[发送]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_x1919680459}[应答错误，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[指示了应答的内容]{style="font-family:宋体"}

[[Starting HA upgrade waiting timer for reset complete]{lang="EN-US"}]{#struct_0_17822_17521_x1912274990}

[[启动]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17822_17521_15664742}[升级等待定时器为了重启完成]{style="font-family:宋体"}

[[External init error when HA]{lang="EN-US"}]{#struct_0_17822_17521_x1411860665}

[[HA]{lang="EN-US"}]{#struct_0_17822_17521_x1305613979}[时外部初始化错误]{style="font-family:宋体"}

[*[Type ]{lang="EN-US"}*[ the global packet up to CPU]{lang="EN-US"}]{#struct_0_17822_17521_x278330160}

[[操作全局的报文是否允许发送到]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_17822_17521_x783810012}[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[描述了操作的类型，]{style="font-family:宋体"}[Type]{lang="EN-US"}[的取值可以如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enable]{lang="EN-US"}]{#struct_0_17822_17521_x1411795129}[：允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disable]{lang="EN-US"}]{#struct_0_17822_17521_x2128891869}[：不允许]{lang="EN-US" style="font-family:宋体"}

[[Receive IFM EPOLLHUP event]{lang="EN-US"}]{#struct_0_17822_17521_x1360270108}

[[收到接口管理的]{style="font-family:宋体"}[EPOLLHUP]{lang="EN-US"}]{#struct_0_17822_17521_1781521729}[事件]{style="font-family:宋体"}

[[Receive SIGKILL signal from SCM]{lang="EN-US"}]{#struct_0_17822_17521_x1411467449}

[[从]{style="font-family:宋体"}[SCM]{lang="EN-US"}]{#struct_0_17822_17521_1429912531}[收到]{style="font-family:宋体"}[SIGKILL]{lang="EN-US"}[信号]{style="font-family:宋体"}

[[Process is deleted successfully]{lang="EN-US"}]{#struct_0_17822_17521_x870310930}

[[进程删除成功]{style="font-family:宋体"}]{#struct_0_17822_17521_x1411401913}

[[Tunnel is deleted successfully]{lang="EN-US"}]{#struct_0_17822_17521_1122054160}

[[Tunnel]{lang="EN-US"}]{#struct_0_17822_17521_x771726982}[接口删除成功]{style="font-family:宋体"}

[[Failed to get system node *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x326517173}

[[获取系统结点失败，]{style="font-family:宋体"}*[Number]{lang="EN-US"}*]{#struct_0_17822_17521_x1411991740}[为系统索引]{style="font-family:宋体"}

[[Receive DEV EPOLLHUP event]{lang="EN-US"}]{#struct_0_17822_17521_x1467181398}

[[收到设备模块发送过来的]{style="font-family:宋体"}[EPOLLHUP]{lang="EN-US"}]{#struct_0_17822_17521_700632976}[事件]{style="font-family:宋体"}

[[Reconnecting to *String*, please wait\...]{lang="EN-US"}]{#struct_0_17822_17521_x1411926204}

[[重新连接]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_763681048}[模块，请等待，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[描述了要连接的模块]{style="font-family:宋体"}

[[Receive VLAN *Type*  event]{lang="EN-US"}]{#struct_0_17822_17521_1615002772}

[[收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x704439307}[事件。]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[描述了事件的类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create ]{lang="EN-US"}]{#struct_0_17822_17521_x1412122812}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_1408156201}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EPOLLHUP]{lang="EN-US"}]{#struct_0_17822_17521_1357647105}

[[External connection of system index *SysINDEX* failed, connectivity set to false.]{lang="EN-US"}]{#struct_0_17822_17521_309913885}

[[系统实例索引为]{style="font-family:宋体"}*[SysINDEX]{lang="EN-US"}*]{#struct_0_17822_17521_1875539077}[的外部连接断开，]{style="font-family:宋体"}[连通性检查失败]{style="font-family:宋体"}

[[Connectivity test passed, connectivity set to true.]{lang="EN-US"}]{#struct_0_17822_17521_x1356326164}

[[连通性检查成功]{style="font-family:宋体"}]{#struct_0_17822_17521_1875473541}

[[Neighbor count optType is *type*, current value is *value*.]{lang="EN-US"}]{#struct_0_17822_17521_x1417959142}

[[邻居计数的操作类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_17822_17521_1875408005}[，当前邻居个数为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[*[type]{lang="EN-US"}*]{#struct_0_17822_17521_1370525611}[的取值可以如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_1875342469}[：计数加操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_x648077730}[：计数减操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_1875801221}[：统计清零]{lang="EN-US" style="font-family:宋体"}

[[The callback track entry doesn\'t match local configuration.]{lang="EN-US"}]{#struct_0_17822_17521_x620052634}

[[Track]{lang="EN-US"}]{#struct_0_17822_17521_1875735685}[模块回调通知的]{style="font-family:宋体"}[Entry]{lang="EN-US"}[同配置中保存的不一致]{style="font-family:宋体"}

[[Track status: *state*.]{lang="EN-US"}]{#struct_0_17822_17521_x1822322065}

[[Track]{lang="EN-US"}]{#struct_0_17822_17521_1875670149}[的连通状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[的取值可以如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_17822_17521_1875604613}[：监测结果未就绪]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Negative]{lang="EN-US"}]{#struct_0_17822_17521_904005424}[：监测对象工作异常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Positive]{lang="EN-US"}]{#struct_0_17822_17521_1876063365}[：监测对象工作正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_17822_17521_x1940936280}[：未识别状态]{style="font-family:宋体"}

[[Transport-side connectivity of the intra-site neighbor changed to *value.*]{lang="EN-US"}]{#struct_0_17822_17521_1875997829}

[[邻居公网侧连通性改变]{style="font-family:宋体"}]{#struct_0_17822_17521_979925733}

[*[value]{lang="EN-US"}*]{#struct_0_17822_17521_1875539078}[的取值可以如下]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_x1355998484}[：邻居公网侧连通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_17822_17521_1875473542}[：邻居公网侧不连通]{lang="EN-US" style="font-family:宋体"}

[[Failed to initialize the TRACK ]{lang="EN-US"}[while HA was being performed.]{lang="EN-US"}]{#struct_0_17822_17521_x1418155750}

[[HA]{lang="EN-US"}]{#struct_0_17822_17521_1875408006}[的时候]{style="font-family:宋体"}[Track]{lang="EN-US"}[初始化失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1412057276}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1545335160}[打开接收]{style="font-family:宋体"}[EVI IS-IS ]{lang="EN-US"}[其它错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis misc]{lang="EN-US"}]{#struct_0_17822_17521_1342100299}

[\*Dec 20 12:24:03:012 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-MISC: Receive VLAN create event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x812956752}*[收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[创建事件]{style="font-family:宋体"}*

::: {#833331557 .myid}
[]{#_Toc404798225}[]{#struct_0_17822_17521_343718965}[]{#_Toc312864697}

**EVI \-- EVI调试命令 \-- debugging evi isis route**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1762050884}

[**[debugging evi isis route]{lang="EN-US"}**[ \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_20563198}

[**[undo debugging evi isis route ]{lang="EN-US"}**[\[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1411729596}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_551546849}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1581409931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1236059989}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1785539116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1142757559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x252183437}

[**[verbose]{lang="EN-US"}**]{#struct_0_17822_17521_x59468748}[：打开路由详细调试信息开关。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x1411664060}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x353530982}

[**[debugging evi isis route]{lang="EN-US"}**]{#struct_0_17822_17521_1309536882}[命令用来打开]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程的路由计算调试信息开关。]{style="font-family:
宋体"}**[undo]{lang="EN-US"}**[ **debugging evi isis route**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的路由计算调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x325907323}[进程路由计算调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的路由计算调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x250770144}

[[表1-8 ]{lang="EN-US"}[debugging evi isis route]{lang="EN-US"}]{#struct_0_17822_17521_x1911295320}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1821528008}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_1561769663}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_899818279}

[[Flush r-mac, vlan: *Number*, mac: *MacAddr*, action: *Type*]{lang="FR"}]{#struct_0_17822_17521_x1411860668}

[[下刷]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_17822_17521_x546099092}[MAC]{lang="FR"}[表项，]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="FR"}[为]{lang="EN-US" style="font-family:
  宋体"}*[Number]{lang="FR"}*[，]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="FR"}[地址为]{lang="EN-US" style="font-family:宋体"}*[MacAddr]{lang="FR"}*[，操作类型为]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="FR"}*[，]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="FR"}*[的取值可以如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_17822_17521_x2033309227}[：无]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add]{lang="EN-US"}]{#struct_0_17822_17521_1646018659}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_17822_17521_766830770}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update]{lang="EN-US"}]{#struct_0_17822_17521_x1603376607}[：更新]{lang="EN-US" style="font-family:宋体"}

[[Failed to flush r-mac, vlan: *Number*, mac: *MacAddr*, error: *ErrorId*]{lang="FR"}]{#struct_0_17822_17521_x1411795132}

[[下刷]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_17822_17521_x2081903238}[MAC]{lang="FR"}[表项失败，]{lang="EN-US" style="font-family:
  宋体"}[MAC]{lang="FR"}[地址为]{lang="EN-US" style="font-family:
  宋体"}*[MacAddr]{lang="FR"}*[，错误]{lang="EN-US" style="font-family:宋体"}[ID]{lang="FR"}[为]{lang="EN-US" style="font-family:宋体"}*[ErrorId]{lang="FR"}*

[*[Type]{lang="FR"}*]{#struct_0_17822_17521_x840940826}[  r-mac entry, vlan: *Number*, mac: *MacAddr*]{lang="FR"}

[[操作]{lang="EN-US" style="font-family:
  宋体"}]{#struct_0_17822_17521_2144014769}[r-mac]{lang="FR"}[表项，操作类型为]{lang="EN-US" style="font-family:
  宋体"}*[Type]{lang="FR"}*[，具体取值如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_17822_17521_x395877137}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_17822_17521_x1411467452}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Update]{lang="EN-US"}]{#struct_0_17822_17521_x1655135648}[：更新]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Query]{lang="EN-US"}]{#struct_0_17822_17521_x1869031156}[：查询]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_1748007499}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1870267193}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis route]{lang="EN-US"}]{#struct_0_17822_17521_391080792}

[\*Jun  3 09:56:15:911 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1; ]{lang="EN-US"}

[EVIISIS-101- ROUTE: Update]{lang="EN-US"}[  ]{lang="EN-US"}[r-mac entry, vlan: ]{lang="FR"}[5]{lang="EN-US"}[, mac: ]{lang="FR"}[aa-bb-cc.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1411401916}*[更新]{style="font-family:宋体"}[r-mac]{lang="EN-US"}[表项，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[aa-bb-cc]{lang="EN-US"}*

::: {#604082899 .myid}
[]{#_Toc404798226}[]{#struct_0_17822_17521_1881569047}[]{#_Toc312864698}

**EVI \-- EVI调试命令 \-- debugging evi isis self-originate-update**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1354843790}

[**[debugging evi isis self-originate-update ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x785136065}

[**[undo]{lang="EN-US"}**[ **debugging evi isis self-originate-update** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x452317798}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_207602164}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x874466321}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_2081340963}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1411991739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1617735709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1969462636}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x1251159288}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1545087738}

[**[debugging evi isis self-originate-update]{lang="EN-US"}**]{#struct_0_17822_17521_1840079694}[命令用来打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的本地更新调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis self-originate-update]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的本地更新调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_1318673728}[进程的本地更新调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的本地更新调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x895178992}

[[表1-9 ]{lang="EN-US"}[debugging evi isis self-originate-update]{lang="EN-US"}]{#struct_0_17822_17521_x1411926203}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1821149672}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x802402893}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1820395571}

[[Purging level-*Number* LSP \[*LSPId*.*PseudoId* -*LspNum*\].]{lang="EN-US"}]{#struct_0_17822_17521_1668666929}

[[清除]{style="font-family:宋体"}[level- *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x1640362199}[的]{style="font-family:宋体"}[LSP\[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{style="font-family:宋体"}[\]]{lang="EN-US"}

[[EVI-ISIS(*ProcID*) level- *Number* LSP overflow.]{lang="EN-US"}]{#struct_0_17822_17521_x747445233}

[[EVI]{lang="EN-US"}]{#struct_0_17822_17521_x1412122811}[ ]{lang="EN-US"}[IS]{lang="EN-US"}[-]{lang="EN-US"}[IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}*[ProcID]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[leve]{lang="EN-US"}[l]{lang="EN-US"}[- *Number* LSP]{lang="EN-US"}[已满]{lang="EN-US" style="font-family:宋体"}

[[The remaining space of level- *Number* fragment 0 LSP is shortage while adding area or protocol support.]{lang="EN-US"}]{#struct_0_17822_17521_x157927740}

[[当添加区域地址或协议支持时]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_462733997}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[的零分片]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[中剩余空间不足]{lang="EN-US" style="font-family:宋体"}

[[Rebuilding all level- *Number* LSPs Start.]{lang="EN-US"}]{#struct_0_17822_17521_x1684457429}

[[开始对]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_905813875}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[的所有]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[进行]{lang="EN-US" style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[Rebuilding all level-*Number* LSPs end.]{lang="EN-US"}]{#struct_0_17822_17521_x1412057275}

[[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1948619687}[l]{lang="EN-US"}[-*Number*]{lang="EN-US"}[所有]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作结束]{lang="EN-US" style="font-family:宋体"}

[[MTU change triggers rebuild.]{lang="EN-US"}]{#struct_0_17822_17521_1485412812}

[[MTU]{lang="EN-US"}]{#struct_0_17822_17521_348818871}[改变触发]{lang="EN-US" style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[Attempting to exceed max sequence number.]{lang="EN-US"}]{#struct_0_17822_17521_x355284486}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1411729595}[的序列号超过最大值（需要反转）]{style="font-family:宋体"}

[[Generating level- *Number* LSP \[*LSPId*.*PseudoId* -*LspNum*\], Seq *SeqNum*, length *LspLen*.]{lang="EN-US"}]{#struct_0_17822_17521_x1014537092}

[[生成序列号为]{lang="EN-US" style="font-family:
  宋体"}*[SeqNum]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_17822_17521_x32594290}[长度为]{lang="EN-US" style="font-family:宋体"}*[LspLen]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[leve]{lang="EN-US"}[l]{lang="EN-US"}[- *Number* LSP\[LSPID.]{lang="EN-US"}[伪节点]{lang="EN-US" style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{lang="EN-US" style="font-family:宋体"}[\]]{lang="EN-US"}

[[TLV handle triggers rebuild.]{lang="EN-US"}]{#struct_0_17822_17521_1734535923}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_412929394}[处理触发]{lang="EN-US" style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[[LSP lifetime change triggers rebuild.]{lang="EN-US"}]{#struct_0_17822_17521_x1411664059}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1568717783}[生存时间触发]{lang="EN-US" style="font-family:宋体"}[Rebuild]{lang="EN-US"}[操作]{lang="EN-US" style="font-family:宋体"}

[*[Type ]{lang="EN-US"}*[ level- *Number* area address *String*.]{lang="EN-US"}]{#struct_0_17822_17521_x1673559121}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1951496804}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[操作区域地址，操作类型为]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*

[*[Type]{lang="EN-US"}*]{#struct_0_17822_17521_x1411860667}[的取值如下：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17822_17521_1826553903}[：]{lang="EN-US" style="font-family:宋体"}[Added]{lang="EN-US"}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17822_17521_874942734}[：]{lang="EN-US" style="font-family:宋体"}[Deleted]{lang="EN-US"}[：删除]{lang="EN-US" style="font-family:宋体"}

[[Added level- *Number* protocol support *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_17822_17521_2009011695}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1411795131}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[添加支持的协议类型]{lang="EN-US" style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[(*ProString*)]{lang="EN-US"}

[[Deleted level- *Number* protocol support *ProNumber*(*ProString*).]{lang="EN-US"}]{#struct_0_17822_17521_1809779531}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_2112765183}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[删除支持的协议类型]{lang="EN-US" style="font-family:宋体"}*[ProNumber]{lang="EN-US"}*[(*ProString*)]{lang="EN-US"}

[[Added level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_x1547217330}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1411467451}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[添加由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息]{lang="EN-US" style="font-family:宋体"}

[[Deleted level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_1073747707}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x242582611}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[删除由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息]{lang="EN-US" style="font-family:宋体"}

[[Modified level- *Number* neighbour: system *systemID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_1747396602}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1411401915}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[更新由]{lang="EN-US" style="font-family:宋体"}*[systemID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的邻居信息]{lang="EN-US" style="font-family:宋体"}

[[Added level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_x2010113722}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_1198318385}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[添加由]{lang="EN-US" style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的伪节点邻居信息]{lang="EN-US" style="font-family:宋体"}

[[Deleted level- *Number* pseudo neighbour: pseudo *pseudoID* =\> neighbour *neighbourID*.]{lang="EN-US"}]{#struct_0_17822_17521_1803334640}

[[为]{lang="EN-US" style="font-family:
  宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x1411991742}[l]{lang="EN-US"}[- *Number*]{lang="EN-US"}[删除由]{lang="EN-US" style="font-family:宋体"}*[pseudoID]{lang="EN-US"}*[到]{lang="EN-US" style="font-family:宋体"}*[neighbourID]{lang="EN-US"}*[的伪节点邻居信息]{lang="EN-US" style="font-family:宋体"}

[[Failed to add mac address for vlan *Number*]{lang="EN-US"}]{#struct_0_17822_17521_1664986484}

[[添加]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1350824370}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Delete mac address for vlan *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x1411926206}

[[删除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x399118366}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Delete all mac address for vlan *Number*]{lang="EN-US"}]{#struct_0_17822_17521_x1468628796}

[[删除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x2118132537}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[所有的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1412122814}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_245356787}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[本地更新调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis self-originate-update]{lang="EN-US"}]{#struct_0_17822_17521_1804658807}

[\*May 27 15:46:13:289 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1; ]{lang="EN-US"}

[EVIISIS-101-ORG: Generating level-1 LSP \[0011.2233.4401.00-00\], Seq 0x00000001, length 71.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x689387392}*[生成序列号为]{style="font-family:宋体"}[0x00000001]{lang="EN-US"}[，长度为]{style="font-family:宋体"}[71]{lang="EN-US"}[的]{style="font-family:宋体"}[L1 LSP\[0011.2233.4401.00-00\]]{lang="EN-US"}*

::: {#-1045538911 .myid}
[]{#_Toc404798227}[]{#struct_0_17822_17521_1382916720}[]{#_Toc312864699}

**EVI \-- EVI调试命令 \-- debugging evi isis snp-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_741826431}

[**[debugging evi isis snp-packet ]{lang="EN-US"}**[\[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1862581704}

[**[undo debugging evi isis snp-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x221395004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1412057278}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1995673854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_309998734}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1955316643}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x540186226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1205119702}

[**[receive]{lang="EN-US"}**]{#struct_0_17822_17521_x600390370}[：]{style="font-family:宋体"}[打开接收]{style="font-family:宋体"}[EVI IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_17822_17521_965407001}[：]{style="font-family:宋体"}[打开发送]{style="font-family:宋体"}[EVI IS-IS SNP]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17822_17521_313213593}[：表示显示详细信息，对报文来说显示报文内容。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_x1411729598}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_101208155}

[**[debugging evi isis snp-packet]{lang="EN-US"}**]{#struct_0_17822_17521_x149057395}[命令用来打开]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:
宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging evi isis snp-packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x1865627302}[进程的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17822_17521_1961650934}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_17822_17521_99439495}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则同时显示打开接收和发送]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定进程号，则表示打开所有进程的]{style="font-family:宋体"}]{#struct_0_17822_17521_1058950781}[SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging evi isis snp-packet]{lang="EN-US"}]{#struct_0_17822_17521_x1518656526}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1813184520}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1411664062}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x1516330396}

[[Receive *PduName* from *SourceId* on circuit *CirName*.]{lang="EN-US"}]{#struct_0_17822_17521_x1868752890}

[[在接口]{style="font-family:宋体"}[CirName]{lang="EN-US"}]{#struct_0_17822_17521_494469161}[上]{style="font-family:宋体"}[收到来自于]{style="font-family:宋体"}[SourceId ]{lang="EN-US"}[的]{style="font-family:宋体"}[PduName]{lang="EN-US"}[，]{style="font-family:宋体"}[PduName]{lang="EN-US"}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1454332875}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1411860670}

[[Receive *PduName* from *SourceId* on circuit *CirName* range from * StartLSPId*.*StartPseudoId* -*StartLspNum* to *EndLSPId*.*EndPseudoId* -*EndLspNum.*]{lang="EN-US"}]{#struct_0_17822_17521_x902263916}

[[在接口]{style="font-family:宋体"}*[CirName]{lang="EN-US"}*]{#struct_0_17822_17521_x1915519964}[上]{style="font-family:宋体"}[收到来自于]{style="font-family:宋体"}*[SourceId]{lang="EN-US"}*[ ]{lang="EN-US"}[的]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[，范围为起始]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号，结束]{style="font-family:宋体"}[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{style="font-family:宋体"}

[*[PduName]{lang="EN-US"}*]{#struct_0_17822_17521_x1377164135}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1697852506}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_17822_17521_465781182}

[[Failed  to process SNP PDU.]{lang="EN-US"}]{#struct_0_17822_17521_x1411795134}

[[处理]{style="font-family:宋体"}[SNP ]{lang="EN-US"}]{#struct_0_17822_17521_1406495004}[报文失败]{style="font-family:宋体"}

[[Not  find current  LSP entry to build CSNP.]{lang="EN-US"}]{#struct_0_17822_17521_712862317}

[[没有找到当前的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1994557694}[摘要来创建]{style="font-family:宋体"}[CSNP]{lang="EN-US"}

[[Level-*Number* CSNP  timer expired on a not DED circuit(*String*).]{lang="EN-US"}]{#struct_0_17822_17521_x1411467454}

[[非]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_17822_17521_1833262594}[的接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*[上]{style="font-family:宋体"}[lever- *Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{style="font-family:宋体"}

[[Send *PduName* on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_1601109642}

[[在接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x1781711551}[上发送]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{style="font-family:宋体"}

[*[PduName]{lang="EN-US"}*]{#struct_0_17822_17521_934182132}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1411401918}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1963059555}

[[Level-*Number* PSNP timer expired on a DED circuit(*String*).]{lang="EN-US"}]{#struct_0_17822_17521_x1462026515}

[[DED]{lang="EN-US"}]{#struct_0_17822_17521_1873307396}[接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*[上]{style="font-family:宋体"}[lever- *Number*]{lang="EN-US"}[的]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{style="font-family:宋体"}

[[Invalid LSPID  reported in SNP.]{lang="EN-US"}]{#struct_0_17822_17521_x1411991741}

[[SNP]{lang="EN-US"}]{#struct_0_17822_17521_1261701957}[中包含无效的]{style="font-family:宋体"}[LSPID]{lang="EN-US"}

[[Wrong LSP entry TLV length(*TlvLen*) in SNP.]{lang="EN-US"}]{#struct_0_17822_17521_x1889941493}

[[SNP]{lang="EN-US"}]{#struct_0_17822_17521_1868242627}[中携带错误的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[SNP contain too much LSP entry.]{lang="EN-US"}]{#struct_0_17822_17521_x1411926205}

[[SNP]{lang="EN-US"}]{#struct_0_17822_17521_x1965202307}[中包含]{style="font-family:宋体"}[LSP]{lang="EN-US"}[摘要的个数超过限制]{style="font-family:宋体"}

[[Wrong TLV length in SNP.]{lang="EN-US"}]{#struct_0_17822_17521_x646616556}

[[SNP]{lang="EN-US"}]{#struct_0_17822_17521_x1122478606}[中携带错误的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Invalid TLV in SNP.]{lang="EN-US"}]{#struct_0_17822_17521_x1412122813}

[[SNP]{lang="EN-US"}]{#struct_0_17822_17521_x1320727154}[中携带无效的]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[LSP entry *LSPId*.*PseudoId* -*LspNum* processed, older than LSDB copy.]{lang="EN-US"}]{#struct_0_17822_17521_1386256225}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x287743768}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId* --*LspNum*]{lang="EN-US"}[，比]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的旧]{style="font-family:宋体"}

[[LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, newer than LSDB  copy.]{lang="EN-US"}]{#struct_0_17822_17521_x1412057277}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1183548195}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId* --*LspNum*]{lang="EN-US"}[，比]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的新]{style="font-family:宋体"}

[[LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, same as LSDB copy.]{lang="EN-US"}]{#struct_0_17822_17521_147051008}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x374918036}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId* --*LspNum*]{lang="EN-US"}[，与]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中保存的新旧相同]{style="font-family:宋体"}

[[LSP  entry *LSPId*.*PseudoId* -*LspNum* processed, not exist in LSDB.]{lang="EN-US"}]{#struct_0_17822_17521_x1411729597}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_2117630790}[摘要]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId* --*LspNum*]{lang="EN-US"}[，在]{style="font-family:
  宋体"}[LSDB]{lang="EN-US"}[中不存在]{style="font-family:宋体"}

[[PSNP not processed, current ED is not DED.]{lang="EN-US"}]{#struct_0_17822_17521_x1351616289}

[[当前]{style="font-family:宋体"}[ED]{lang="EN-US"}]{#struct_0_17822_17521_x1411664061}[不是]{style="font-family:宋体"}[DED]{lang="EN-US"}[，不处理]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[SNPType ]{lang="EN-US"}*[not processed before DED election.]{lang="EN-US"}]{#struct_0_17822_17521_1212552959}

[[在]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_17822_17521_519969609}[选举前不处理]{style="font-family:宋体"}*[SNPType]{lang="EN-US"}*[报文，]{style="font-family:宋体"}*[SNPType]{lang="EN-US"}*[的]{style="font-family:宋体"}[具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1411860669}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSNP]{lang="EN-US"}]{#struct_0_17822_17521_1019984849}

[[Lsp entry *LSPId*.*PseudoId* -*LspNum* is not loaded in CSNP.]{lang="EN-US"}]{#struct_0_17822_17521_x1807886738}

[[在]{style="font-family:宋体"}[CSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1411795133}[中没有]{style="font-family:宋体"}[LSP *LSPId*.*PseudoId* --*LspNum*]{lang="EN-US"}[的摘要]{style="font-family:宋体"}

[[CSNP not processed on DED.]{lang="EN-US"}]{#struct_0_17822_17521_646980117}

[[DED]{lang="EN-US"}]{#struct_0_17822_17521_894610409}[上不处理]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Invalid type of SNP PDU.]{lang="EN-US"}]{#struct_0_17822_17521_1951435545}

[[无效的]{style="font-family:宋体"}[SNP PDU]{lang="EN-US"}]{#struct_0_17822_17521_x1411467453}[类型]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x89051707}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x2047567196}[打开接收]{style="font-family:宋体"}[EVI IS-IS SNP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis snp-packet receive]{lang="EN-US"}]{#struct_0_17822_17521_292156171}

[\*Dec 19 15:40:51:337 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-0-SNP: Send L1 CSNP on circuit Evi-Link0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_248618012}*[在]{style="font-family:宋体"}[EVI-Link0]{lang="EN-US"}[上发送]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#877426296 .myid}
[]{#_Toc404798228}[]{#struct_0_17822_17521_549874318}[]{#_Toc312864700}

**EVI \-- EVI调试命令 \-- debugging evi isis timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1413813641}

[**[debugging evi isis]{lang="EN-US"}**[ **timer** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1411401917}

[**[undo debugging evi isis timer ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x847314308}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_227950209}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1181085226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1218827553}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1825911385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1765975900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_458398123}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_154092203}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_1527994745}

[**[debugging evi isis]{lang="EN-US"}[ timer]{lang="EN-US"}**]{#struct_0_17822_17521_x1273864112}[命令用来打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging evi isis]{lang="EN-US"}[ timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[进程的定时器调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_2101815384}[进程的定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，如果未指定进程号，则表示打开所有进程的定时器调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_x1174119056}

[[表1-11 ]{lang="EN-US"}[debugging evi isis timer]{lang="EN-US"}]{#struct_0_17822_17521_1831042796}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1845410536}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_190512712}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x1674673766}

[[Start *Type* timer, value is *value*]{lang="EN-US"}]{#struct_0_17822_17521_154157739}

[[启动]{style="font-family:宋体"}]{#struct_0_17822_17521_765459506}*[Type]{lang="EN-US"}*[定时器，时间为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值可以如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T2]{lang="EN-US"}]{#struct_0_17822_17521_x476593158}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T3]{lang="EN-US"}]{#struct_0_17822_17521_1183151872}

[[Reset *Type* timer, value is *value*]{lang="EN-US"}]{#struct_0_17822_17521_x259527695}

[[重置]{lang="EN-US" style="font-family:宋体"}*[Type]{lang="EN-US"}*]{#struct_0_17822_17521_x63585738}[定时器，时间为]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的取值可以如下]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T2]{lang="EN-US"}]{#struct_0_17822_17521_153961131}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T3]{lang="EN-US"}]{#struct_0_17822_17521_1770823742}

[[Level-*Number* adjacency hold SystemId timer expired on the circuit *PortName*]{lang="EN-US"}]{#struct_0_17822_17521_x1105352547}

[[接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_x1143001908}[下的]{lang="EN-US" style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[的邻居定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Level-*Number*  hello timer expired on the circuit *PortName*]{lang="EN-US"}]{#struct_0_17822_17521_416041902}

[[接口]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_154026667}[下的]{lang="EN-US" style="font-family:宋体"}[level-*Number*]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[H]{lang="EN-US"}[ello]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Starting waiting timer for max sequence num exceed, time value is *value* ms.]{lang="EN-US"}]{#struct_0_17822_17521_x1935964040}

[[启动]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_447849037}[序列号达到最大值的翻转等待定时器，定时器时长为]{style="font-family:宋体"}[value]{lang="EN-US"}[毫秒]{style="font-family:宋体"}

[[Level-*Number* CSNP * *timer expired on the circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_x1329454965}

[[接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x1395977476}[下的]{style="font-family:宋体"}[level- *Number* CSNP]{lang="EN-US"}[定时器超时，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{style="font-family:宋体"}

[[Level- *Number* flood timer expired on the circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_154354347}

[[接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_1782697620}[下的]{style="font-family:宋体"}[level-]{lang="EN-US"}*[ Number]{lang="EN-US"}*[泛洪定时器超时，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名]{style="font-family:宋体"}

[[Level- *Number* LSP \[*LSPId*.*PseudoId* -*LspNum*\] gen timer expired.]{lang="EN-US"}]{#struct_0_17822_17521_863884542}

[[leve]{lang="EN-US"}]{#struct_0_17822_17521_x69277530}[l]{lang="EN-US"}[-]{lang="EN-US"}*[ Number]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[LSP\[LSPID.]{lang="EN-US"}[伪节点]{lang="EN-US" style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{lang="EN-US" style="font-family:宋体"}[\]]{lang="EN-US"}[生成定时器超时]{lang="EN-US" style="font-family:宋体"}

[[Start level- *Number* LSP \[*LSPId*.*PseudoId* -*LspNum*\] gen timer, time vlaue is *TimeValue*(ms).]{lang="EN-US"}]{#struct_0_17822_17521_154419883}

[[启动]{style="font-family:宋体"}[level-]{lang="EN-US"}*[ Number ]{lang="EN-US"}*]{#struct_0_17822_17521_2029447311}[的]{style="font-family:宋体"}[LSP\[LSPID.]{lang="EN-US"}[伪节点]{style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{style="font-family:宋体"}[\]]{lang="EN-US"}[生成定时器，定时器时长为]{style="font-family:宋体"}*[TimeValue]{lang="EN-US"}*[(]{lang="EN-US"}[单位毫秒]{style="font-family:宋体"}[)]{lang="EN-US"}

[[Stop level- *Number* LSP \[*LSPId*.*PseudoId* -*LspNum*\] gen timer.]{lang="EN-US"}]{#struct_0_17822_17521_958706505}

[[停止]{lang="EN-US" style="font-family:宋体"}[leve]{lang="EN-US"}]{#struct_0_17822_17521_x424748027}[l]{lang="EN-US"}[-]{lang="EN-US"}*[ Number]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[LSP\[LSPID.]{lang="EN-US"}[伪节点]{lang="EN-US" style="font-family:宋体"}[ID-]{lang="EN-US"}[分片号]{lang="EN-US" style="font-family:宋体"}[\]]{lang="EN-US"}[生成定时器]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x212752811}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1819219573}[打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis timer]{lang="EN-US"}]{#struct_0_17822_17521_154223275}

[\*Dec 20 10:18:29:955 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1;]{lang="EN-US"}

[EVIISIS-0-TMR: Level-1 hello timer expired on the circuit Evi-Link0.]{lang="EN-US"}

[*[// EVI-Link0]{lang="EN-US"}*]{#struct_0_17822_17521_x545039642}*[上的]{style="font-family:宋体"}[Lever-1 Hello]{lang="EN-US"}[报文发送定时器超时]{style="font-family:宋体"}*

::: {#-1939460375 .myid}
[]{#_Toc404798229}[]{#struct_0_17822_17521_x350803496}[]{#_Toc312864701}

**EVI \-- EVI调试命令 \-- debugging evi isis update-packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_x519662269}

[**[debugging evi isis update-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ **verbose** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_1680730538}

[**[undo debugging evi isis update-packet]{lang="EN-US"}**[ \[ **receive** \| **send** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17822_17521_x1138657523}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_771513081}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x98899074}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_154288811}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1336862630}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1053819574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_219967265}

[**[receive]{lang="EN-US"}**]{#struct_0_17822_17521_x561355971}[：]{style="font-family:宋体"}[打开接收]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[更新模块报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_17822_17521_85026818}[：]{style="font-family:宋体"}[打开发送]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[更新模块报文的调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17822_17521_503875983}[：表示显示详细信息，对报文来说显示报文内容。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_17822_17521_1024668926}[：要打开的调试信息开关的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_860215412}

[**[debugging evi isis update-packet]{lang="EN-US"}**]{#struct_0_17822_17521_154616491}[命令用来打开]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的更新模块报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging evi isis update-packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的更新模块报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_1986490697}[进程的更新模块报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17822_17521_x30509323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_17822_17521_x1947567132}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则同时打开接收和发送]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程更新模块报文调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定进程，则表示打开所有进程的更新模块报文调试信息开关。]{style="font-family:宋体"}]{#struct_0_17822_17521_1897368518}

[[表1-12 ]{lang="EN-US"}[debugging evi isis update-packet]{lang="EN-US"}]{#struct_0_17822_17521_1924576249}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1840603528}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1552463357}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_154682027}

[[Flooding *PduName* *LSPId*.*PseudoId* -*LspNum* on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_x418495788}

[[在接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_x1650970506}[上泛洪]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[（]{style="font-family:宋体"}*[LSPId]{lang="EN-US"}*[.*PseudoId* -*LspNum*]{lang="EN-US"}[），]{style="font-family:
  宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名，]{style="font-family:
  宋体"}*[PduName]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1955466534}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 CSNP]{lang="EN-US"}]{#struct_0_17822_17521_1201072473}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 PSNP]{lang="EN-US"}]{#struct_0_17822_17521_x1837811015}

[*[Type]{lang="EN-US"}*[ *PduName* lspid= *LSPId*.*PseudoId* -*LspNum* seq=*Sequence* ht=*HoldTime* from snpa *SnpaAddr* on circuit *String*.]{lang="EN-US"}]{#struct_0_17822_17521_154092204}

[[在接口]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_17822_17521_1527994748}[上从地址]{style="font-family:宋体"}*[SnpaAddr]{lang="EN-US"}*[ *type*]{lang="EN-US"}[序列号为]{style="font-family:宋体"}*[Sequence]{lang="EN-US"}*[，时间为]{style="font-family:宋体"}*[HoldTime]{lang="EN-US"}*[的]{style="font-family:宋体"}*[PduName]{lang="EN-US"}*[，]{style="font-family:宋体"}[lspid= *LSPId*.*PseudoId* -*LspNum* seq]{lang="EN-US"}[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：接口名，]{style="font-family:宋体"}

[*[type]{lang="EN-US"}*]{#struct_0_17822_17521_x1274060720}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receive]{lang="EN-US"}]{#struct_0_17822_17521_x1548807693}[：接收]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Send]{lang="EN-US"}]{#struct_0_17822_17521_x112177023}[：发送]{lang="EN-US" style="font-family:宋体"}

[*[PduName]{lang="EN-US"}*]{#struct_0_17822_17521_154157740}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1 LSP]{lang="EN-US"}]{#struct_0_17822_17521_1957100587}

[*[Type remot]{lang="EN-US"}*[e address*(*vlan *Number:* MAC *MacAddr)*]{lang="EN-US"}]{#struct_0_17822_17521_x1036245782}

[[对远程地址操作，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_17822_17521_168536056}[为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[MacAddr]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[可以取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_17822_17521_1335981974}[：添加]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_17822_17521_153961132}[：删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modify]{lang="EN-US"}]{#struct_0_17822_17521_1770823739}[：修改]{lang="EN-US" style="font-family:宋体"}

[[LSP\'s sequence number is 0]{lang="EN-US"}]{#struct_0_17822_17521_x1104631652}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1672727757}[报文的序列号为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Illegal is-type in level-1 LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1824162905}

[[无效的类型在]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_17822_17521_154026668}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Check sum is zero]{lang="EN-US"}]{#struct_0_17822_17521_x1935964051}

[[校验和为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17822_17521_x1118300440}

[[Check sum error]{lang="EN-US"}]{#struct_0_17822_17521_x199252050}

[[校验和错误]{style="font-family:宋体"}]{#struct_0_17822_17521_154354348}

[[Invalid extended is reachability TLV]{lang="EN-US"}]{#struct_0_17822_17521_1782697631}

[[不支持的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_17822_17521_863819007}

[[Support protocol mismatch]{lang="EN-US"}]{#struct_0_17822_17521_1431121609}

[[支持的协议不匹配]{style="font-family:宋体"}]{#struct_0_17822_17521_154419884}

[[LSP with more than *Count* area addr(es)]{lang="EN-US"}]{#struct_0_17822_17521_2029447314}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_958509897}[中区域地址数量超过最大值]{style="font-family:宋体"}

[[LSP with wrong area addr length *Length*]{lang="EN-US"}]{#struct_0_17822_17521_x1413746648}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_154223276}[中区域地址长度错误，长度为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*

[[Lsp with wrong area addr *AreaAddr*]{lang="EN-US"}]{#struct_0_17822_17521_x545039645}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x351000104}[中区域地址错误，地址为]{style="font-family:宋体"}*[AreaAddr]{lang="EN-US"}*

[[Invalid mac reachability TLV]{lang="EN-US"}]{#struct_0_17822_17521_154288812}

[[无效的]{style="font-family:宋体"}[mac TLV]{lang="EN-US"}]{#struct_0_17822_17521_1336862631}

[[Wrong encoding of area address TLV in LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1053754038}

[[错误的区域地址]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_17822_17521_x109658980}[在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文中]{style="font-family:宋体"}

[[Bad TLV length in the received LSP]{lang="EN-US"}]{#struct_0_17822_17521_154616492}

[[收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1986490700}[报文中错误的]{style="font-family:宋体"}[TLV]{lang="EN-US"}[长度]{style="font-family:宋体"}

[[Own LSP *LSP ID*-*LSP Seq* processed, newer than LSDB copy]{lang="EN-US"}]{#struct_0_17822_17521_x1987152146}

[[处理本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_154682028}[报文序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中新]{style="font-family:宋体"}

[[Other LSP *LSP ID*-*LSP Seq*  processed, newer than LSDB copy]{lang="EN-US"}]{#struct_0_17822_17521_x418495787}

[[处理非本地的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1651036042}[报文]{style="font-family:宋体"}[,]{lang="EN-US"}[序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中新]{style="font-family:宋体"}

[[LSP  *LSP ID*-*LSP Seq* processed, older than LSDB copy]{lang="EN-US"}]{#struct_0_17822_17521_154092201}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_1527994743}[报文，序列号比]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中旧]{style="font-family:宋体"}

[[LSP *LSP ID*-*LSP Seq*  processed, same as LSDB copy]{lang="EN-US"}]{#struct_0_17822_17521_x1273470896}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_154157737}[报文，序列号与]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中相同]{style="font-family:宋体"}

[*[String ]{lang="EN-US"}*[ LSP *LSP ID*-*LSP Seq* processed, no exist in LSDB]{lang="EN-US"}]{#struct_0_17822_17521_765459496}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_x1233373035}[报文，]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中不存在，报文类型为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Sting]{lang="EN-US"}*[的取值可以为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[other]{lang="EN-US"}]{#struct_0_17822_17521_153961129}[：非本地的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[own]{lang="EN-US"}]{#struct_0_17822_17521_x185491386}[：本地的]{lang="EN-US" style="font-family:宋体"}

[[PDU size(*Size*) is greater than receive buffer size(*SizeBuf*),ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_x427116147}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_154026665}[大小]{style="font-family:宋体"}[(*Size*)]{lang="EN-US"}[大于接收缓冲区大小]{style="font-family:宋体"}[(*SizeBuf*)]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[PDU size(*Size*) is less than common PDU header size(*Len*),ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_x1935964038}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_803882789}[大小]{style="font-family:宋体"}[(*Size*)]{lang="EN-US"}[小于]{style="font-family:宋体"}[PDU]{lang="EN-US"}[正常的报文头长度]{style="font-family:宋体"}[(*Length)*]{lang="EN-US"}[，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[PDU size *Size*) is less than fixed PDU header size(*Len*),ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_154354345}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_1782697618}[大小]{style="font-family:宋体"}[(*Size*)]{lang="EN-US"}[小于]{style="font-family:宋体"}[PDU]{lang="EN-US"}[填充的报文头长度]{style="font-family:宋体"}[(*Length)*]{lang="EN-US"}[，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[PDU length mismatch: recvLen = *RecvLength*, encodeLen = *EncodeLenght*,ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_863360257}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_154419881}[长度]{style="font-family:宋体"}*[RecvLength]{lang="EN-US"}*[与报文中指示的长度]{style="font-family:宋体"}*[EncodeLenght]{lang="EN-US"}*[不匹配，丢弃报文]{style="font-family:宋体"}

[[SNPA address of PDU is the same as the local circuit(*PortName*), ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_2029447309}

[[在接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*]{#struct_0_17822_17521_959230792}[上收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文中]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[的地址与本地一样，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[EVI-ISIS process is under disable, ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_154223273}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_17822_17521_x545039648}[进程处于]{style="font-family:宋体"}[disable]{lang="EN-US"}[状态，丢弃]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Failed to Check received packet]{lang="EN-US"}]{#struct_0_17822_17521_x350148136}

[[检测接收到的报文失败]{style="font-family:宋体"}]{#struct_0_17822_17521_154288809}

[[LSP or SNP PDU common header error, ignoring  PDU]{lang="EN-US"}]{#struct_0_17822_17521_x1001789522}

[[LSP]{lang="EN-US"}]{#struct_0_17822_17521_154616489}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[通用报文头错误，丢弃报文]{style="font-family:宋体"}

[[Received PDU level mismatch]{lang="EN-US"}]{#struct_0_17822_17521_x352161471}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_914914662}[报文级别不匹配]{style="font-family:宋体"}

[[No active neighbour with such snpa(*SnpaAddr*) on the cicuit(*PortName*), ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_154682025}

[[没有激活的邻居地址是]{style="font-family:宋体"}*[SnpaAddr]{lang="EN-US"}*]{#struct_0_17822_17521_x418495790}[在接口]{style="font-family:宋体"}*[PortName]{lang="EN-US"}*[上，丢弃报文]{style="font-family:宋体"}

[[Failed to processLSP PDU]{lang="EN-US"}]{#struct_0_17822_17521_x1651494795}

[[处理]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_17822_17521_154092202}[报文失败]{style="font-family:宋体"}

[[Received PDU is not LSP or SNP, ignoring PDU]{lang="EN-US"}]{#struct_0_17822_17521_1527994746}

[[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_17822_17521_154157738}[报文不是]{style="font-family:宋体"}[LSP]{lang="EN-US"}[或]{style="font-family:宋体"}[SNP]{lang="EN-US"}[报文，丢弃报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_765459507}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x476593159}[打开接收]{style="font-family:宋体"}[EVI IS-IS ]{lang="EN-US"}[更新模块报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi isis update-packet receive]{lang="EN-US"}]{#struct_0_17822_17521_1183217408}

[\*Jun  8 08:31:21:994 2011 Sysname EVIISIS/7/EVIISIS DBG: -MDC=1; ]{lang="EN-US"}

[EVIISIS-101-UPDT: Received PDU level mismatch.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1089677947}*[收到的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文级别不匹配]{style="font-family:宋体"}*

::: {#155479855 .myid}
[]{#_Toc404798230}[]{#struct_0_17822_17521_x659616273}[]{#_Toc309053976}[]{#_Toc303421794}

**EVI \-- EVI调试命令 \-- debugging evi mac-address**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_153961130}

[**[debugging evi mac-address]{lang="EN-US"}**]{#struct_0_17822_17521_1770823741}[ { **info** \| **isis** }]{lang="EN-US"}

[**[undo debugging evi mac-address]{lang="EN-US"}**]{#struct_0_17822_17521_x1105155939}[ { **info** \| **isis** }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_x563295146}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_1858234276}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_x615034136}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_1639490599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x887614305}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x592636008}

[**[info]{lang="EN-US"}**]{#struct_0_17822_17521_154026666}[：表示下驱动调试信息开关。]{style="font-family:宋体"}

[**[isis]{lang="EN-US"}**]{#struct_0_17822_17521_x1935964041}[：表示来自]{style="font-family:宋体"}[EVI ]{lang="EN-US"}[IS-IS]{lang="EN-US"}[模块消息的调试信息开关。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1118234904}

[**[debugging evi ]{lang="EN-US"}**]{#struct_0_17822_17521_1646364916}**[mac-address]{lang="EN-US"}**[命令用来打开]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}**[undo debugging evi ]{lang="EN-US"}[mac-address]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}]{#struct_0_17822_17521_2056810891}[的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表1-13 ]{lang="EN-US"}[debugging evi mac-address info]{lang="EN-US"}]{#struct_0_17822_17521_x534112367}[命令]{style="font-family:黑体"}[输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1859601160}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x665924797}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_154354346}

[*[interface-name]{lang="EN-US"}*[: Set selective-flooding MAC address *mac-address* successfully.]{lang="EN-US"}]{#struct_0_17822_17521_1782697621}

[[设置隧道接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_863819006}[的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[信息成功]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[: Failed to set selective-flooding MAC address *mac-address*.]{lang="EN-US"}]{#struct_0_17822_17521_1431121608}

[[设置隧道接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_x2140299167}[的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[: Failed to set selective-flooding MAC address *mac-address* due to insufficient hardware resources.]{lang="EN-US"}]{#struct_0_17822_17521_x827545835}

[[由于硬件资源不足，设置隧道接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_154419882}[的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[: Set *type* information successfully.]{lang="EN-US"}]{#struct_0_17822_17521_2029447312}

[[设置隧道接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ *type*]{lang="EN-US"}]{#struct_0_17822_17521_958640969}[信息成功，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extern VLAN]{lang="EN-US"}]{#struct_0_17822_17521_1538417745}[：扩展]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1324370239}[：激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive VLAN]{lang="EN-US"}]{#struct_0_17822_17521_154223274}[：非激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC request]{lang="EN-US"}]{#struct_0_17822_17521_x545039643}[：本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址请求]{lang="EN-US" style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[: Failed to set *type* information.]{lang="EN-US"}]{#struct_0_17822_17521_x350869032}

[[设置隧道接口]{style="font-family:宋体"}*[interface-name type]{lang="EN-US"}*]{#struct_0_17822_17521_1767842635}[信息失败，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extern VLAN]{lang="EN-US"}]{#struct_0_17822_17521_154288810}[：扩展]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active VLAN]{lang="EN-US"}]{#struct_0_17822_17521_1336862629}[：激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1054278325}[：非激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC request]{lang="EN-US"}]{#struct_0_17822_17521_1747627953}[：本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址请求]{lang="EN-US" style="font-family:宋体"}

[*[interface-name]{lang="EN-US"}*[: Failed to set *type* information due to insufficient hardware resources.]{lang="EN-US"}]{#struct_0_17822_17521_x1733952375}

[[由于硬件资源不足，设置隧道接口]{style="font-family:宋体"}*[interface-name type]{lang="EN-US"}*]{#struct_0_17822_17521_154616490}[信息失败，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extern VLAN]{lang="EN-US"}]{#struct_0_17822_17521_1986490698}[：扩展]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x31361291}[：激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive VLAN]{lang="EN-US"}]{#struct_0_17822_17521_716630440}[：非激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC request]{lang="EN-US"}]{#struct_0_17822_17521_154682026}[：本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址请求]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[debugging evi mac-address isis]{lang="EN-US"}]{#struct_0_17822_17521_x418495789}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1860328904}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1650904970}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_204684899}

[*[interface-name]{lang="EN-US"}*[: Received a(an) *type* message from ISIS.]{lang="EN-US"}]{#struct_0_17822_17521_846977838}

[[隧道接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17822_17521_x1801664398}[从]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[接收到]{style="font-family:宋体"}*[type]{lang="EN-US"}*[消息，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的取值以及含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[extern VLAN]{lang="EN-US"}]{#struct_0_17822_17521_154092199}[：扩展]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active VLAN]{lang="EN-US"}]{#struct_0_17822_17521_1934014288}[：激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive VLAN]{lang="EN-US"}]{#struct_0_17822_17521_x1407958361}[：非激活]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC request]{lang="EN-US"}]{#struct_0_17822_17521_920534927}[：本地]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址请求]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x207922297}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x641595238}[打开]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}[模块]{style="font-family:宋体"}[来自]{style="font-family:宋体"}[EVI ]{lang="EN-US"}[IS-IS]{lang="EN-US"}[模块消息的调试信息开关]{style="font-family:
宋体"}[，如果接收到激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息，则会打印如下信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging evi mac-address isis]{lang="EN-US"}]{#struct_0_17822_17521_154157735}

[\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/ISIS: -MDC=1; Tunnel101: Received an active VLAN message from ISIS.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_765459494}*[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[从]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[接收到激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1233373033}[打开]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}[模块]{style="font-family:宋体"}[下驱动调试信息开关]{style="font-family:宋体"}[，配置泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[时会打印如下驱动信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging evi mac-address info]{lang="EN-US"}]{#struct_0_17822_17521_x96970990}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] evi selective-flooding mac-address 1113-1113-1113 vlan 1]{lang="EN-US"}

[\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/INFO: -MDC=1; Tunnel101: Set selective-flooding MAC address 1113-1113-1113 successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1649807062}*[设置隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[的泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[信息成功]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_645587428}[打开]{style="font-family:宋体"}[EVI MAC]{lang="EN-US"}[模块]{style="font-family:宋体"}[下驱动调试信息开关]{style="font-family:宋体"}[，如果激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的信息下发驱动，则会打印如下信息：]{style="font-family:宋体"}

[[\<Sysname\> debugging evi mac-address info]{lang="EN-US"}]{#struct_0_17822_17521_153961127}

[\*Feb 24 10:50:19:644 2011 Sysname EVIMAC/7/INFO: -MDC=1; Tunnel101: Set an active VLAN information successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x185491400}*[设置隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息成功]{style="font-family:宋体"}*

::: {#-2058376723 .myid}
[]{#_Toc404798231}[]{#struct_0_17822_17521_x2001487483}

**EVI \-- EVI调试命令 \-- debugging evi neighbor-discovery client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_1946964607}

[**[debugging evi neighbor-discovery client]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17822_17521_x1203539901}

[**[undo debugging evi neighbor-discovery client]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17822_17521_674717757}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_253091563}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x1930903480}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_154026663}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1935964044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1521519431}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x322277827}

[**[all]{lang="EN-US"}**]{#struct_0_17822_17521_x877491175}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_17822_17521_1245220329}[：表示表项调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17822_17521_x1885846506}[：表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17822_17521_x724081329}[：表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_17822_17521_x523143920}[：表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_154354343}

[**[debugging evi neighbor-discovery client]{lang="EN-US"}**]{#struct_0_17822_17521_1782697624}[命令用来打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging evi neighbor-discovery client ]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_17822_17521_864146686}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-15 ]{lang="EN-US"}[debugging evi neighbor-discovery client entry]{lang="EN-US"}]{#struct_0_17822_17521_x1467244202}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1855275208}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_505358237}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1636379455}

[[Failed to find the server node.]{lang="EN-US"}]{#struct_0_17822_17521_x745912963}

[[查找服务器节点失败]{style="font-family:宋体"}]{#struct_0_17822_17521_154419879}

[*[operate-name]{lang="EN-US"}*[: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*]{lang="EN-US"}]{#struct_0_17822_17521_1984817285}

[[操作表项信息，接口为]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_2046612547}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[*[operate-name]{lang="EN-US"}*]{#struct_0_17822_17521_1631669861}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Added neighbor]{lang="EN-US"}]{#struct_0_17822_17521_1237861647}[：添加邻居节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted neighbor]{lang="EN-US"}]{#struct_0_17822_17521_154223271}[：删除邻居节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[Added server node]{lang="NO-BOK"}]{#struct_0_17822_17521_x545039646}[：]{lang="EN-US" style="font-family:
  宋体"}[添加]{lang="EN-US" style="font-family:宋体"}[服务器节点]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted server node]{lang="EN-US"}]{#struct_0_17822_17521_x351065640}[：删除服务器节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Added dummy]{lang="EN-US"}]{#struct_0_17822_17521_x512185702}[：添加]{lang="EN-US" style="font-family:宋体"}[Dummy]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deleted dummy]{lang="EN-US"}]{#struct_0_17822_17521_2060333034}[：删除]{lang="EN-US" style="font-family:宋体"}[Dummy]{lang="EN-US"}[节点]{lang="EN-US" style="font-family:宋体"}

[[Added tunnel: interface= *if-name*, peer address= *ipaddr-value.*]{lang="EN-US"}]{#struct_0_17822_17521_154288807}

[[添加隧道：接口为]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_x1001789524}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[[Deleted tunnel: interface= *if-name*, peer address= *ipaddr-value.*]{lang="EN-US"}]{#struct_0_17822_17521_1385499513}

[[删除隧道：接口为]{style="font-family:宋体"}*[ii-name]{lang="EN-US"}*]{#struct_0_17822_17521_x542226768}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[debugging evi neighbor-discovery client error]{lang="EN-US"}]{#struct_0_17822_17521_1429099779}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1857310632}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_1417563480}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_154616487}

[[Failed to create run info.]{lang="EN-US"}]{#struct_0_17822_17521_x352161457}

[[创建运行信息失败]{style="font-family:宋体"}]{#struct_0_17822_17521_915045736}

[[Failed to create hash.]{lang="EN-US"}]{#struct_0_17822_17521_4133366}

[[创建]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_17822_17521_x1280042106}[失败]{style="font-family:宋体"}

[[Failed to start ENDP service.]{lang="EN-US"}]{#struct_0_17822_17521_x110266962}

[[启动]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_17822_17521_154682023}[服务失败]{style="font-family:宋体"}

[[Failed to create tunnel connection.]{lang="EN-US"}]{#struct_0_17822_17521_x418495792}

[[创建与隧道的连接失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x1651363723}

[ ]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[debugging evi neighbor-discovery client event]{lang="EN-US"}]{#struct_0_17822_17521_1326429231}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1850953352}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1208726320}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x597574204}

[[Created *timer-name* timer: timer interval= *time-value*; timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_17822_17521_154092200}

[[创建]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_17822_17521_1527994744}[定时器，时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*[，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

[*[timer-name]{lang="EN-US"}*]{#struct_0_17822_17521_x1273798576}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register]{lang="EN-US"}]{#struct_0_17822_17521_729593949}[：注册定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIPC reconnect]{lang="EN-US"}]{#struct_0_17822_17521_x2122504554}[：]{lang="EN-US" style="font-family:宋体"}[LIPC]{lang="EN-US"}[重连定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[neighbor ]{lang="EN-US"}]{#struct_0_17822_17521_x1786981349}[aging]{lang="EN-US"}[：邻居老化定时器]{lang="EN-US" style="font-family:宋体"}

[[Modified register timer: timer interval= *time-value.*]{lang="EN-US"}]{#struct_0_17822_17521_154157736}

[[修改注册定时器的时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_17822_17521_765459497}

[[Deleted *timer-name* timer: timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_17822_17521_x1233373036}

[[删除]{style="font-family:宋体"}*[timer-name]{lang="EN-US"}*]{#struct_0_17822_17521_x856485877}[定时器，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

[*[timer-name]{lang="EN-US"}*]{#struct_0_17822_17521_x778851449}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[register]{lang="EN-US"}]{#struct_0_17822_17521_153961128}[：注册定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIPC reconnect]{lang="EN-US"}]{#struct_0_17822_17521_x185491387}[：]{lang="EN-US" style="font-family:宋体"}[LIPC]{lang="EN-US"}[重连定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[neighbor ]{lang="EN-US"}]{#struct_0_17822_17521_x427181683}[aging]{lang="EN-US"}[：邻居老化定时器]{lang="EN-US" style="font-family:宋体"}

[[Received EVI tunnel restart event.]{lang="EN-US"}]{#struct_0_17822_17521_2032170344}

[[收到]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_17822_17521_x845281227}[隧道重启事件]{style="font-family:宋体"}

[[Started ENDP service.]{lang="EN-US"}]{#struct_0_17822_17521_154026664}

[[启动]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_17822_17521_x1935964039}[服务]{style="font-family:宋体"}

[[Started smoothing neighbor information.]{lang="EN-US"}]{#struct_0_17822_17521_x762201152}

[[开始平滑邻居信息]{style="font-family:宋体"}]{#struct_0_17822_17521_x989948615}

[[Finished smoothing neighbor information.]{lang="EN-US"}]{#struct_0_17822_17521_154354344}

[[邻居信息平滑结束]{style="font-family:宋体"}]{#struct_0_17822_17521_1782697619}

[[Stopped ENDP service.]{lang="EN-US"}]{#struct_0_17822_17521_863294721}

[[停止]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_17822_17521_1106891258}[服务]{style="font-family:宋体"}

[*[if-name]{lang="EN-US"}*[ received interface *event-name*.]{lang="EN-US"}]{#struct_0_17822_17521_x1158768768}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_154419880}[收到接口事件，事件类型为]{style="font-family:宋体"}*[event-name]{lang="EN-US"}*

[*[event-name]{lang="EN-US"}*]{#struct_0_17822_17521_2029447310}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up event]{lang="EN-US"}]{#struct_0_17822_17521_958772041}[：接口]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[p]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down event]{lang="EN-US"}]{#struct_0_17822_17521_154223272}[：接口]{lang="EN-US" style="font-family:宋体"}[d]{lang="EN-US"}[own]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create event]{lang="EN-US"}]{#struct_0_17822_17521_x545039649}[：接口创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete event]{lang="EN-US"}]{#struct_0_17822_17521_x350213672}[：接口删除]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[debugging evi neighbor-discovery client packet]{lang="EN-US"}]{#struct_0_17822_17521_x908880881}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1852470568}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x1606618642}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_154288808}

[[Interface *if-name* received a packet: packet type= *type-value*, networkID= *netid-value*, server address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_x1001789523}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_2145014400}[收到一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_17822_17521_x1567595287}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_1065378408}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_17822_17521_321105687}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_17822_17521_154616488}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_x352161470}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Interface *if-name* Sent a packet: packet type= *type-value*, networkID= *netid-value*, server address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_914849126}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_x1889479277}[发送一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_17822_17521_1591061420}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_154682024}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_17822_17521_x418495791}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_17822_17521_x1651429259}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_x244900220}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Peer info: IP address= *ipaddr-value*, system ID= *macaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_x1099624015}

[[对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17822_17521_1720176144}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*

[[Invalid peer info: IP address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_x307410290}

[[失效的对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17822_17521_300675433}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[[Packet failed header check.]{lang="EN-US"}]{#struct_0_17822_17521_999878134}

[[报文头检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x47251011}

[[Packet failed fixed header check.]{lang="EN-US"}]{#struct_0_17822_17521_1720241680}

[[报文固定头检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_107456692}

[[Packet failed required content check.]{lang="EN-US"}]{#struct_0_17822_17521_433713156}

[[报文强制部分检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_164137754}

[[Packet failed extended content check.]{lang="EN-US"}]{#struct_0_17822_17521_1720045072}

[[报文扩展部分检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x1071000043}

[[Transaction ID mismatch.]{lang="EN-US"}]{#struct_0_17822_17521_462134800}

[[事务]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17822_17521_x110247019}[不相等]{style="font-family:宋体"}

[[Packet failed authentication.]{lang="EN-US"}]{#struct_0_17822_17521_1720110608}

[[认证失败]{style="font-family:宋体"}]{#struct_0_17822_17521_1676358592}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1254715320}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_218386592}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[表项调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery client entry]{lang="EN-US"}]{#struct_0_17822_17521_x265178894}

[\*Sep  6 17:14:34:243 2011 Sysname ENDC/7/ENTRY: -MDC=1; Add neighbor: interface= Tunnel1, network ID= 1, IP address= 1.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x2107278366}*[添加邻居节点，接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[[\*Sep  6 17:14:34:246 2011 Sysname ENDC/7/ENTRY: -MDC=1; Added Tunnel: interface= Tunnel1, peer address= 1.1.1.1.]{lang="EN-US"}]{#struct_0_17822_17521_1720438288}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1502029765}*[添加隧道，接口为]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[，对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_225704706}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[事件调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[发送注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery client event]{lang="EN-US"}]{#struct_0_17822_17521_x295638951}

[\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created register timer: time interval= 15s, timer ID= 10.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_267682194}*[创建注册定时器，时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_x1631735170}[使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[报文调试信息开关，当]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery client packet]{lang="EN-US"}]{#struct_0_17822_17521_1720503824}

[\*Sep  6 17:22:10:772 2011 Sysname ENDC/7/PACKET: -MDC=1; Interface Tunnel1 received a packet: packet type= 4, network ID= 1, server address= 1.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_896307471}*[接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[收到一个报文，报文类型为注册应答报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}*

[[\*Sep  6 17:22:10:773 2011 Sysname ENDC/7/PACKET: -MDC=1; Peer info: IP address= 1.1.1.1, system ID= 0011-2200-0101.]{lang="EN-US"}]{#struct_0_17822_17521_310984642}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_1816527668}*[对端信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0011-2200-0101]{lang="EN-US"}*

::: {#742196963 .myid}
[]{#_Toc404798232}[]{#struct_0_17822_17521_1634433303}[]{#_Toc287608520}[]{#_Toc205804228}

**EVI \-- EVI调试命令 \-- debugging evi neighbor-discovery server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17822_17521_976259377}

[**[debugging evi neighbor-discovery server]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17822_17521_x197603554}

[**[undo debugging evi neighbor-discovery server]{lang="EN-US"}**[ { **all** \| **entry** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17822_17521_1990510745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17822_17521_1720307216}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17822_17521_x282149018}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17822_17521_203363371}

[[network-admin]{lang="EN-US"}]{#struct_0_17822_17521_x1999733384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17822_17521_1224718837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1609901990}

[**[all]{lang="EN-US"}**]{#struct_0_17822_17521_1576520483}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_17822_17521_988820587}[：表示表项调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17822_17521_1720372752}[：表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17822_17521_871570747}[：表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_17822_17521_635540288}[：表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1534386726}

[**[debugging evi neighbor-discovery server]{lang="EN-US"}**]{#struct_0_17822_17521_x1660901427}[命令用来打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging evi neighbor-discovery server]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_17822_17521_x1978349107}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-19 ]{lang="EN-US"}[debugging evi neighbor-discovery server entry]{lang="EN-US"}]{#struct_0_17822_17521_1441635355}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1848144616}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_2123818430}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1720700432}

[[Added client: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*]{lang="EN-US"}]{#struct_0_17822_17521_2064659323}

[[增加客户，接口为]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_x833349810}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Deleted client: interface= *if-name*, network ID= *netid-value*, IP address= *ipaddr-value.*]{lang="EN-US"}]{#struct_0_17822_17521_x1885138320}

[[删除客户，接口为]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_1794960992}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[debugging evi neighbor-discovery server error]{lang="EN-US"}]{#struct_0_17822_17521_x294758516}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1876649448}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_1720765968}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_x272968281}

[[Failed to create run info.]{lang="EN-US"}]{#struct_0_17822_17521_58285588}

[[创建运行信息失败]{style="font-family:宋体"}]{#struct_0_17822_17521_2071775356}

[ ]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[debugging evi neighbor-discovery server event]{lang="EN-US"}]{#struct_0_17822_17521_x1679456709}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1875790056}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_151530292}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1720176145}

[[Created aging timer: timer interval= *time-value*, timer ID= *id-value*.]{lang="EN-US"}]{#struct_0_17822_17521_x307475826}

[[创建老化定时器，时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_17822_17521_x1318373269}[，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*

[[Modified aging timer: timer interval= *time-value*]{lang="EN-US"}]{#struct_0_17822_17521_x159386250}

[[修改老化定时器的时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_17822_17521_x953862517}

[[Deleted aging timer: timer id= *id-value*.]{lang="EN-US"}]{#struct_0_17822_17521_1720241681}

[[删除]{style="font-family:宋体"}]{#struct_0_17822_17521_107522228}[ID]{lang="NO-BOK"}[为]{style="font-family:宋体"}*[id-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[老化]{style="font-family:宋体"}[定时器]{style="font-family:宋体"}

[*[if-name]{lang="EN-US"}*[ received interface *event-name*.]{lang="EN-US"}]{#struct_0_17822_17521_x1526194569}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_1382006873}[收到接口事件，事件类型为]{style="font-family:宋体"}*[event-name]{lang="EN-US"}*

[*[event-name]{lang="EN-US"}*]{#struct_0_17822_17521_1557684397}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up event]{lang="EN-US"}]{#struct_0_17822_17521_510415467}[：接口]{lang="EN-US" style="font-family:宋体"}[u]{lang="EN-US"}[p]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down event]{lang="EN-US"}]{#struct_0_17822_17521_1720045073}[：接口]{lang="EN-US" style="font-family:宋体"}[d]{lang="EN-US"}[own]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create event]{lang="EN-US"}]{#struct_0_17822_17521_x1070934507}[：接口创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete event]{lang="EN-US"}]{#struct_0_17822_17521_x1492987079}[：接口删除]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-22 ]{lang="EN-US"}[debugging evi neighbor-discovery server packet]{lang="EN-US"}]{#struct_0_17822_17521_x1578703470}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1877825480}[[字段]{style="font-family:黑体"}]{#struct_0_17822_17521_x2086192715}

[[描述]{style="font-family:黑体"}]{#struct_0_17822_17521_1720110609}

[[Packet failed authentication.]{lang="EN-US"}]{#struct_0_17822_17521_1676293056}

[[认证失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x1297045016}

[[Interface *if-name* received a packet: packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_393901750}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_248229576}[收到一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户端服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_17822_17521_393654704}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_1720438289}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_17822_17521_x1502095301}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_17822_17521_651041431}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_244889894}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Interface *if-name s*ent a packet: ]{lang="EN-US"}]{#struct_0_17822_17521_x83174615}

[[packet type= *type-value*, network ID= *netid-value*, client address= *ipaddr-value*.]{lang="EN-US"}]{#struct_0_17822_17521_1720503825}

[[接口]{style="font-family:宋体"}*[if-name]{lang="EN-US"}*]{#struct_0_17822_17521_896373007}[发送一个报文：报文类型为]{style="font-family:宋体"}*[type-value]{lang="EN-US"}*[，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[netid-value]{lang="EN-US"}*[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*

[*[type-value]{lang="EN-US"}*]{#struct_0_17822_17521_x49648309}[的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17822_17521_x81541029}[：注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_17822_17521_x1333800284}[：注册应答报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_17822_17521_1720307217}[：注销报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17822_17521_x282083482}[：错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Client info: IP address= *ipaddr-value*, system ID= *macaddr-value*, register interval= *time-value*]{lang="EN-US"}]{#struct_0_17822_17521_x1376923805}

[[报文中携带的客户信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17822_17521_x2057529200}[地址为]{style="font-family:宋体"}*[ipaddr-value]{lang="EN-US"}*[，桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[macaddr-value]{lang="EN-US"}*[，注册时间间隔为]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*

[[Packet failed validity check.]{lang="EN-US"}]{#struct_0_17822_17521_192676701}

[[合法性检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_1720372753}

[[Packet failed header check.]{lang="EN-US"}]{#struct_0_17822_17521_871505211}

[[报文头检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x2075314826}

[[Packet failed fixed header check.]{lang="EN-US"}]{#struct_0_17822_17521_1720700433}

[[报文固定头检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_2064724859}

[[Packet failed required content check.]{lang="EN-US"}]{#struct_0_17822_17521_x65529445}

[[报文强制部分检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x494002313}

[[Packet failed extended content check.]{lang="EN-US"}]{#struct_0_17822_17521_1720765969}

[[报文扩展部分检测失败]{style="font-family:宋体"}]{#struct_0_17822_17521_x272902745}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17822_17521_x1139086314}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_621679870}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[表项调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery server entry]{lang="EN-US"}]{#struct_0_17822_17521_947751793}

[\*Sep  6 16:49:49:180 2011 Sysname ENDS/7/ENTRY: -MDC=1; Added client: interface= Tunnel0, network ID= 1, IP address= 1.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_1162647954}*[增加客户，接口为]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[，网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_1388282818}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[事件调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery server event]{lang="EN-US"}]{#struct_0_17822_17521_1720176142}

[\*Sep  8 15:21:38:814 2011 Sysname ENDS/7/EVENT: -MDC=1; Created aging timer: time interval= 75s, timer ID= 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x307017074}*[创建老化定时器，时间间隔为]{style="font-family:宋体"}[75]{lang="EN-US"}[秒，定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17822_17521_279465548}[使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能，打开]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[报文调试信息开关，当]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[收到]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的注册报文后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging evi neighbor-discovery server packet]{lang="EN-US"}]{#struct_0_17822_17521_x737236426}

[\*Sep  6 16:58:30:600 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 received a packet: packet type= 3, network ID= 1, client address= 1.1.1.2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x512231240}*[接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[收到一个报文：报文类型为注册报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*

[[\*Sep  6 17:01:02:276 2011 Sysname ENDS/7/PACKET: -MDC=1; Client info: IP address= 1.1.1.2, system ID= 0011-2200-0101, register interval= 5s.]{lang="EN-US"}]{#struct_0_17822_17521_x1817551525}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_x1715875287}*[报文中携带的客户信息：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0011-2200-0101]{lang="EN-US"}[，注册时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Sep  6 16:58:30:604 2011 Sysname ENDS/7/PACKET: -MDC=1; Interface Tunnel0 sent a packet: packet type= 4, network ID= 1, client address= 1.1.1.2.]{lang="EN-US"}]{#struct_0_17822_17521_x246557315}

[*[// ]{lang="EN-US"}*]{#struct_0_17822_17521_1720241678}*[接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[发送一个报文：报文类型为注册应答报文，对应的网络]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}*
