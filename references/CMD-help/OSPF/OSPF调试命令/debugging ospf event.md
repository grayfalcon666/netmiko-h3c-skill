::: {#-1910963938 .myid}
[]{#_Toc404787732}[]{#struct_0_78893_x1682_1618434633}[]{#_Toc300065252}[]{#_Toc148240883}

**OSPF \-- OSPF调试命令 \-- debugging ospf event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x717375676}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **event** \[ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** \]]{lang="EN-US"}]{#struct_0_78893_x1682_140193829}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **event** \[ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** \]]{lang="EN-US"}]{#struct_0_78893_x1682_686344100}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1416779170}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1277576423}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1943215369}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_694345034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_1793664465}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1792595248}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x717310140}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bfd]{lang="EN-US"}**]{#struct_0_78893_x1682_x637152681}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[联动调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_78893_x1682_1657785149}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[错误事件调试信息开关。]{style="font-family:宋体"}

[**[graceful]{lang="EN-US"}**[-restart]{lang="EN-US"}]{#struct_0_78893_x1682_x1769349724}[：表示平滑重启调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_78893_x1682_x630131517}[：表示接口事件调试信息开关。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}**]{#struct_0_78893_x1682_x1104188045}[：表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_39094581}

[**[debugging ospf event]{lang="EN-US"}**]{#struct_0_78893_x1682_x736380729}[命令用来打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x150937009}[事件调试信息开关处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x717244604}[进程的事件调试信息。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ospf event bfd]{lang="EN-US"}]{#struct_0_78893_x1682_x1416911770}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1664362609}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_1087105789}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_869383762}

[[BFD service connected, smooth all session]{lang="EN-US"}]{#struct_0_78893_x1682_x1539053606}

[[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_1390271132}[进程连接，开始平滑会话]{style="font-family:宋体"}

[[BFD service disconnected, clear all session]{lang="EN-US"}]{#struct_0_78893_x1682_x1726880687}

[[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_x717179068}[进程断开连接，清除本地保存的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Receive BFD event *bfd-event*]{lang="EN-US"}]{#struct_0_78893_x1682_x682556844}

[[接受到]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_1488662020}[进程发送的事件：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bfd-event]{lang="EN-US"}*]{#struct_0_78893_x1682_1966247416}[：]{style="font-family:宋体"}[BFD]{lang="EN-US"}[事件类型]{style="font-family:宋体"}

[[Notify BFD smooth stop]{lang="EN-US"}]{#struct_0_78893_x1682_x1918335926}

[[通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_1870975206}[进程会话平滑结束]{style="font-family:宋体"}

[[Create BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*]{lang="EN-US"}]{#struct_0_78893_x1682_x718162108}

[[通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_x1616975645}[进程创建会话：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*[-id]{lang="EN-US"}]{#struct_0_78893_x1682_x616571587}[：进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface]{lang="EN-US"}*[-name]{lang="EN-US"}]{#struct_0_78893_x1682_1518951914}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1488613535}[：邻居的路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_765669952}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话源地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_x718096572}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话目的地址]{lang="EN-US" style="font-family:
  宋体"}

[[Delete BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*]{lang="EN-US"}]{#struct_0_78893_x1682_x25445651}

[[通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_191968998}[进程删除会话：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*[-id]{lang="EN-US"}]{#struct_0_78893_x1682_68105512}[：进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface]{lang="EN-US"}*[-name]{lang="EN-US"}]{#struct_0_78893_x1682_1554808803}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x717637819}[：邻居的路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_1660897146}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话源地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_x1872264444}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话目的地址]{lang="EN-US" style="font-family:
  宋体"}

[[Disable BFD session for OSPF *process-id*, *interface-name*, nbr *nbr-id*, src *src-ip-address*, dst *dst-ip-address*]{lang="EN-US"}]{#struct_0_78893_x1682_x1576476622}

[[通知]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_x717572283}[进程去使能会话：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*[-id]{lang="EN-US"}]{#struct_0_78893_x1682_145549647}[：进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface]{lang="EN-US"}*[-name]{lang="EN-US"}]{#struct_0_78893_x1682_x1514051352}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1093358422}[：邻居的路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_x1368325209}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话源地址]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_x717506747}[：]{lang="EN-US" style="font-family:
  宋体"}[BFD]{lang="EN-US"}[会话目的地址]{lang="EN-US" style="font-family:
  宋体"}

[[Total *num* OSPF process under GR]{lang="EN-US"}]{#struct_0_78893_x1682_x615072841}

[[BFD]{lang="EN-US"}]{#struct_0_78893_x1682_x1031280514}[进程连接时收集正在进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_812714873}[：正在进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程数量]{style="font-family:宋体"}

[[OSPF *process-id* exit GR, reserved *num* OSPF process under GR]{lang="EN-US"}]{#struct_0_78893_x1682_x717441211}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1411949054}[进程退出]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1983432996}[：进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_x1678078529}[：正在进行]{style="font-family:宋体"}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ospf event error]{lang="EN-US"}]{#struct_0_78893_x1682_x1996735671}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1667997924}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x717375675}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_139997221}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_69234257}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1722497687}[进程号]{style="font-family:宋体"}

[[OSPF received packet having conflicted Router ID : *rt-id*]{lang="EN-US"}]{#struct_0_78893_x1682_446506544}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1167033804}[收到了]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[冲突的报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1109438877}[：邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[Received short IP packet  (*ip-pkt-len* bytes)]{lang="EN-US"}]{#struct_0_78893_x1682_x717310139}

[[收到包长不正确的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_78893_x1682_x636693928}[包：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_76765037}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[包长]{lang="EN-US" style="font-family:宋体"}

[[Received short Hello/DD/REQ/UPDATE packet (*ospf-pkt-len* bytes)]{lang="EN-US"}]{#struct_0_78893_x1682_x2075944676}

[[收到包长不正确的]{style="font-family:宋体"}[Hello/DD/REQ/UPDATE]{lang="EN-US"}]{#struct_0_78893_x1682_77405235}[包：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ospf-pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_1608040117}[：]{lang="EN-US" style="font-family:
  宋体"}[OSPF]{lang="EN-US"}[包长]{lang="EN-US" style="font-family:
  宋体"}

[[Received short UPDATE/ACK packet (*ospf-pkt-len* bytes with *ls-count*  LSAs)]{lang="EN-US"}]{#struct_0_78893_x1682_x717244603}

[[收到包长不正确的]{style="font-family:宋体"}[UPDATE/ACK]{lang="EN-US"}]{#struct_0_78893_x1682_x1416977306}[包：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ospf-pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_1038733793}[：]{lang="EN-US" style="font-family:
  宋体"}[OSPF]{lang="EN-US"}[包长]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-count]{lang="EN-US"}*]{#struct_0_78893_x1682_1496746318}[：包含的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[个数]{lang="EN-US" style="font-family:宋体"}

[[Received short IP packet(*ip-pkt-len* bytes) containing *ospf-pkt-len* bytes OSPF data field (type *pkt-type*)]{lang="EN-US"}]{#struct_0_78893_x1682_x867417725}

[[收到包长不正确的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_78893_x1682_x717179067}[包，并说明其中]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[包长：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x682229164}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[包长]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ospf-pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x2026236924}[：]{lang="EN-US" style="font-family:
  宋体"}[OSPF]{lang="EN-US"}[包长]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pkt-type]{lang="EN-US"}*]{#struct_0_78893_x1682_870247221}[：包的类型，取值为]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[REQ]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[UPDATE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}

[[Received error packet *pkt-type* from interface *interface-type interface-number*]{lang="EN-US"}]{#struct_0_78893_x1682_x1714400297}

[[收到错误包：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x718162107}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pkt-type]{lang="EN-US"}*]{#struct_0_78893_x1682_x1616779037}[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[包类型，取值为]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[REQ]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[UPDATE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Interface-type interface-number]{lang="EN-US"}*]{#struct_0_78893_x1682_x1231293435}[：接口类型和编号]{lang="EN-US" style="font-family:宋体"}

[[OSPF received packet having bad authentication type : *auth-type*]{lang="EN-US"}]{#struct_0_78893_x1682_561630972}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x2051464066}[收到包含错误认证类型的包：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[auth-type]{lang="EN-US"}*]{#struct_0_78893_x1682_x718096571}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[包认证类型，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示无认证、为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示认证方式为]{style="font-family:宋体"}[Simple]{lang="EN-US"}[认证、为]{style="font-family:宋体"}[2]{lang="EN-US"}[表示认证方式为]{style="font-family:宋体"}[MD5]{lang="EN-US"}

[[OSPF received packet having bad authentication key]{lang="EN-US"}]{#struct_0_78893_x1682_x25380115}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_327188077}[收到错误认证码的包]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ospf event graceful-restart]{lang="EN-US"}]{#struct_0_78893_x1682_2106338070}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1665970063}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_402307995}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x717637822}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1660569463}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x199875863}[进程号]{style="font-family:宋体"}

[[nonstandard GR started for OSPF router]{lang="EN-US"}]{#struct_0_78893_x1682_2108589176}

[[开始执行非标准]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_1757819136}

[[IETF GR started for OSPF router]{lang="EN-US"}]{#struct_0_78893_x1682_720655432}

[[开始执行]{style="font-family:宋体"}[IETF GR]{lang="EN-US"}]{#struct_0_78893_x1682_857136175}

[[created GR interval timer,timeout interval is *num*(s)]{lang="EN-US"}]{#struct_0_78893_x1682_x717572286}

[[创建]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_145353039}[间隔定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_x1766120329}[：定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[deleted GR interval timer]{lang="EN-US"}]{#struct_0_78893_x1682_1910324909}

[[删除]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x110962764}[间隔定时器]{style="font-family:宋体"}

[[GR interval timer fired]{lang="EN-US"}]{#struct_0_78893_x1682_573499846}

[[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x717506750}[间隔定时器超时]{style="font-family:宋体"}

[[created GR wait timer,timeout interval is *num*(s)]{lang="EN-US"}]{#struct_0_78893_x1682_x615007306}

[[创建]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x1872673197}[等待定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_x1981336053}[：定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[deleted GR wait timer]{lang="EN-US"}]{#struct_0_78893_x1682_145524945}

[[删除]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x717441214}[等待定时器]{style="font-family:宋体"}

[[GR wait timer fired]{lang="EN-US"}]{#struct_0_78893_x1682_x1411752446}

[[GR]{lang="EN-US"}]{#struct_0_78893_x1682_2069040805}[等待定时器超时]{style="font-family:宋体"}

[[generate LSAs start]{lang="EN-US"}]{#struct_0_78893_x1682_x1981593781}

[[开始生成]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_1473200672}

[[generate LSAs end]{lang="EN-US"}]{#struct_0_78893_x1682_x717375678}

[[生成]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_139800613}[结束]{style="font-family:宋体"}

[[Flush stale area LSAs]{lang="EN-US"}]{#struct_0_78893_x1682_x729988636}

[[老化]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_710715029}[内部]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[Flush stale ASE and NSSA LSAs]{lang="EN-US"}]{#struct_0_78893_x1682_435817038}

[[老化]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x717310142}[外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[*[(vlink) ]{lang="EN-US"}*[neighbor : *nbr-id*,exit Restart reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x637283753}

[[邻居退出]{style="font-family:宋体"}]{#struct_0_78893_x1682_855004808}[GR Restart]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_60351353}[：邻居]{style="font-family:宋体"}[neighbor]{lang="EN-US"}[ ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x717244606}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[interface: *if-name*,DR or BDR change : old DR:*ip-address*,old BDR: *ip-address*,new DR: *ip-address*,new BDR: *ip-address*.]{lang="EN-US"}]{#struct_0_78893_x1682_x1416780698}

[[DR,BDR]{lang="EN-US"}]{#struct_0_78893_x1682_1759337235}[变化：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_78893_x1682_190838003}[：]{lang="EN-US" style="font-family:宋体"}[接口名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_x717179070}[：接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[interface : *if-name*,exit Restart reason : *reason*.]{lang="EN-US"}]{#struct_0_78893_x1682_x682032557}

[[接口退出]{style="font-family:宋体"}]{#struct_0_78893_x1682_x2032706868}[Restart]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_117785281}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[area:area-id vlink peer: *nbr-id* exit Restart reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x718162110}

[[vlink]{lang="EN-US"}]{#struct_0_78893_x1682_x1616451358}[退出]{style="font-family:宋体"}[Restart]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1258542317}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x229929502}[：区域号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x718096574}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[exit Restart reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x25052435}

[[退出]{style="font-family:宋体"}[GR Restart]{lang="EN-US"}]{#struct_0_78893_x1682_x316989437}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x415497410}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*]{#struct_0_78893_x1682_x717637821}[）]{style="font-family:宋体"}[neighbor : *nbr-id*,exit Helper reason : *reason*]{lang="EN-US"}

[[vlink]{lang="EN-US"}]{#struct_0_78893_x1682_1660372855}[退出]{style="font-family:宋体"}[Helper]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_2118532391}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x717572285}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[exit Helper Reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_145156431}

[[退出]{style="font-family:宋体"}]{#struct_0_78893_x1682_706630147}[GR Helper]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x717506749}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[Exit Restart,Reason : *reason*,for neighbor : *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x614417481}

[[退出]{style="font-family:宋体"}[GR Restart]{lang="EN-US"}]{#struct_0_78893_x1682_62474047}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x1445830460}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x717441213}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Exit Restart,Reason : *reason*,for interface : *if-name*]{lang="EN-US"}]{#struct_0_78893_x1682_x1411817982}

[[退出]{style="font-family:宋体"}[GR Restart]{lang="EN-US"}]{#struct_0_78893_x1682_198639866}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x717375677}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_78893_x1682_140128293}[：]{lang="EN-US" style="font-family:宋体"}[接口名]{style="font-family:宋体"}

[[Exit Restart,Reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x803194125}

[[退出]{style="font-family:宋体"}[GR Restart]{lang="EN-US"}]{#struct_0_78893_x1682_x717310141}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x637218217}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[Exit Helper,Reason : *reason*,for neighbor : *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1606846153}

[[退出]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_78893_x1682_x717244605}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x1416846234}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1052297703}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Exit Helper,Reason : *reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x717179069}

[[退出]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_78893_x1682_x682622380}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_x884122627}[：退出原因]{lang="EN-US" style="font-family:宋体"}

[[received new grace LSA from neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x718162109}

[[接受到邻居发送的]{style="font-family:宋体"}[GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_x1616910109}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x718096573}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[received MaxAge grace LSA from neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x25511187}

[[接受到邻居发送的]{style="font-family:宋体"}[MaxAge GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_1406434662}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_848446123}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[exit IETF GR helper mode for ]{lang="EN-US"}]{#struct_0_78893_x1682_311625009}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[neighbor *nbr-id*]{lang="EN-US"}

[[退出]{style="font-family:宋体"}[IETF GR Helper]{lang="EN-US"}]{#struct_0_78893_x1682_1338113128}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_848511659}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[generated grace LSA for ]{lang="EN-US"}]{#struct_0_78893_x1682_x1664255401}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[interface *if-name*]{lang="EN-US"}

[[生成]{style="font-family:宋体"}[GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_x1766947328}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_78893_x1682_848577195}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[flush MaxAge grace LSA for ]{lang="EN-US"}]{#struct_0_78893_x1682_1907099022}[（]{style="font-family:
  宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:
  宋体"}[interface *if-name*]{lang="EN-US"}

[[洪泛]{style="font-family:宋体"}[GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_848642731}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_78893_x1682_541912681}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[created GR send grace lsa timer,timeout interval is *num*(s)]{lang="EN-US"}]{#struct_0_78893_x1682_1048173881}

[[创建]{style="font-family:宋体"}[IETF GR GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_848708267}[发送定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_980395976}[：定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[deleted GR send grace lsa timer]{lang="EN-US"}]{#struct_0_78893_x1682_848773803}

[[删除]{style="font-family:宋体"}[IETF GR GraceLsa]{lang="EN-US"}]{#struct_0_78893_x1682_x1345852387}[发送定时器]{style="font-family:宋体"}

[[created Grace Period timer for ]{lang="EN-US"}]{#struct_0_78893_x1682_848839339}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[neighbor *nbr-id*,timeout interval is *num*(s)]{lang="EN-US"}

[[创建]{style="font-family:宋体"}[IETF GR]{lang="EN-US"}]{#struct_0_78893_x1682_x1961091896}[周期定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_631992241}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[num]{lang="EN-US"}*]{#struct_0_78893_x1682_848904875}[：定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[deleted Grace Period timer for ]{lang="EN-US"}]{#struct_0_78893_x1682_837020712}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[neighbor *nbr-id*]{lang="EN-US"}

[[删除]{style="font-family:宋体"}[IETF GR]{lang="EN-US"}]{#struct_0_78893_x1682_847921835}[周期定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x502027785}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[created OOB Progress timer for ]{lang="EN-US"}]{#struct_0_78893_x1682_847987371}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[neighbor *nbr-id*]{lang="EN-US"}

[[创建非标准]{style="font-family:宋体"}[GR OOB]{lang="EN-US"}]{#struct_0_78893_x1682_1822737460}[定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_738901738}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[deleted OOB Progress timer for ]{lang="EN-US"}]{#struct_0_78893_x1682_848446124}[（]{style="font-family:宋体"}*[vlink]{lang="EN-US"}*[）]{style="font-family:宋体"}[neighbor *nbr-id*]{lang="EN-US"}

[[删除非标准]{style="font-family:宋体"}[GR OOB]{lang="EN-US"}]{#struct_0_78893_x1682_311625006}[定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_848511660}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[created Resync timer for neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1056733776}

[[创建非标准]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_848577196}[同步定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1907099021}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[deleted Resync timer for neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_136985951}

[[删除非标准]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_78893_x1682_848642732}[同步定时器：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_541912678}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[exit nonstandard GR helper mode for neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_848708268}

[[退出非标准]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_78893_x1682_980395981}[模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_848773804}[：邻居路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[GR all helpers completed for OSPF router]{lang="EN-US"}]{#struct_0_78893_x1682_x1345852388}

[[与所有]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_78893_x1682_848839340}[同步完成]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ospf event interface]{lang="EN-US"}]{#struct_0_78893_x1682_x387113791}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1677022849}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_1317588933}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_1523165529}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1429416463}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1349224832}[进程号]{style="font-family:宋体"}

[[Interface *intf-ip* received *intf-event* and its state from *pre-state* -\> *cur-state*]{lang="EN-US"}]{#struct_0_78893_x1682_848904876}

[[接口状态变化的详细信息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_837020709}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[intf-ip]{lang="EN-US"}*]{#struct_0_78893_x1682_315397602}[：接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[intf-event]{lang="EN-US"}*]{#struct_0_78893_x1682_1832804296}[：引起接口状态变化的事件，取值为]{lang="EN-US" style="font-family:宋体"}[InterfaceUp]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[WaitTimer]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LoopInd]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[BackupSeen]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NeighborChange]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[UnloopInd]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[InterfaceDown]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pre-state]{lang="EN-US"}*[/*cur-state*]{lang="EN-US"}]{#struct_0_78893_x1682_x703708754}[：接口状态，取值为]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}[表示接口处于]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[、取值为]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[表示接口是回环状态、]{lang="EN-US" style="font-family:宋体"}[Waiting]{lang="EN-US"}[表示接口处于]{lang="EN-US" style="font-family:宋体"}[waiting]{lang="EN-US"}[状态、]{lang="EN-US" style="font-family:宋体"}[Point-to-point]{lang="EN-US"}[接口连接点到点网络或者通过虚连接、]{lang="EN-US" style="font-family:宋体"}[DR]{lang="EN-US"}[表示路由器是]{lang="EN-US" style="font-family:宋体"}[DR]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Backup]{lang="EN-US"}[表示路由器是]{lang="EN-US" style="font-family:宋体"}[BDR]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[DROther]{lang="EN-US"}[表示路由器非]{lang="EN-US" style="font-family:宋体"}[DR]{lang="EN-US"}[且非]{lang="EN-US" style="font-family:宋体"}[BDR]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ospf event neighbor]{lang="EN-US"}]{#struct_0_78893_x1682_x1732012449}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1673995463}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_847921836}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x502027784}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_784682566}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1737805193}[进程号]{style="font-family:宋体"}

[[Neighbor *nbr-ip* received *nbr-event* and its state from *original-state* -\> *current-state*]{lang="EN-US"}]{#struct_0_78893_x1682_x1672426220}

[[邻居状态变化的详细信息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1522618018}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-ip]{lang="EN-US"}*]{#struct_0_78893_x1682_x704849802}[：邻居接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-event]{lang="EN-US"}*]{#struct_0_78893_x1682_847987372}[：引起邻居状态变化的事件，取值为]{lang="EN-US" style="font-family:宋体"}[HelloReceived]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Start]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2WayReceived]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NegotiationDone]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ExchangeDone]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[BadLSReq]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LoadingDone]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[AdjOK?]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[1-Way]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[KillNbr]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Inactivity Timer]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[LLDown]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[original-state]{lang="EN-US"}*[/*current-state*]{lang="EN-US"}]{#struct_0_78893_x1682_1822737457}[：邻居状态，取值为]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Attempt]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Init]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ExStart]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Loading]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Full]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_739098345}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_x1716592068}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口事件调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf event interface]{lang="EN-US"}]{#struct_0_78893_x1682_1815762775}

[%Nov  1 10:15:33:767 2012 RouterA IFNET/5/LINK_UPDOWN: -MDC=1;]{lang="EN-US"}

[Line protocol on the interface GigabitEthernet1/0/1 is UP]{lang="EN-US"}

[\*Nov  1 10:15:38:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1: Interface 150.1.1.1 received InterfaceUp and its state from Down -\> Waiting.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_207887253}*[接口状态由]{style="font-family:宋体"}[Down]{lang="EN-US"}[变为]{style="font-family:宋体"}[Waiting]{lang="EN-US"}*

[[\*Nov  1 10:16:18:811 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_848446121}

[OSPF 1: Interface 150.1.1.1 received BackupSeen and its state from Waiting -\> BackupDR.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_311625011}*[接口状态由]{style="font-family:宋体"}[Waiting]{lang="EN-US"}[变为]{style="font-family:宋体"}[BackupDR]{lang="EN-US"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_x618202016}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开邻居事件调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf event neighbor]{lang="EN-US"}]{#struct_0_78893_x1682_568780997}

[\*Nov  1 10:14:18:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received KillNbr and its state from Full -\> Down.]{lang="EN-US"}

[\*Nov  1 10:15:48:098 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received HelloReceived and its state from Down -\> Init.]{lang="EN-US"}

[\*Nov  1 10:15:48:098 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received 2WayReceived and its state from Init -\> 2Way.]{lang="EN-US"}

[\*Nov  1 10:16:13:811 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received AdjOk? and its state from 2Way -\> ExStart.]{lang="EN-US"}

[\*Nov  1 10:16:18:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received NegotiationDone and its state from ExStart -\> Exchange.]{lang="EN-US"}

[\*Nov  1 10:16:18:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received ExchangeDone and its state from Exchange -\> Loading.]{lang="EN-US"}

[\*Nov  1 10:16:18:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1: Neighbor 150.1.1.2 received LoadingDone and its state from Loading -\> Full.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_433140935}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[与邻居]{style="font-family:宋体"}[150.1.1.2]{lang="EN-US"}[建立邻接关系的全过程]{style="font-family:宋体"}*

::: {#-305748851 .myid}
[]{#_Toc404787733}[]{#struct_0_78893_x1682_848511657}[]{#_Toc300065253}[]{#_Toc148240884}

**OSPF \-- OSPF调试命令 \-- debugging ospf lsa**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1664255403}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **lsa** \[ { **generate** \| **install** } \[ **filter** { **ase** \| **opaque-as** \| \[ **area** *area-id* \] { **asbr** \| **network** \| **nssa** \| **opaque-area** \| **opaque-link** \| **router** \| **summary** }  \[ *link-state-id* \] } \] \] ]{lang="EN-US"}]{#struct_0_78893_x1682_x604147914}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **lsa** \[ { **generate** \| **install** } \[ **filter** \] \]]{lang="EN-US"}]{#struct_0_78893_x1682_x23179602}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x63637118}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_473066926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1362047260}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_836142095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x541430546}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_848577193}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1907099024}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_78893_x1682_137313631}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成调试信息开关。]{style="font-family:宋体"}

[**[install]{lang="EN-US"}**]{#struct_0_78893_x1682_1368584331}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[安装到]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[库中的调试信息开关。]{style="font-family:宋体"}

[**[filter]{lang="EN-US"}**]{#struct_0_78893_x1682_1987796480}[：表示打开过滤]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**[ *area-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1987862016}[：]{style="font-family:宋体"}[表示数据库中指定区域的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将打开所有区域的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_78893_x1682_x1579905741}[：表示]{style="font-family:宋体"}[ASBR Summary LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[ase]{lang="EN-US"}**]{#struct_0_78893_x1682_x264583942}[：表示]{style="font-family:宋体"}[AS External LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**]{#struct_0_78893_x1682_x610763014}[：表示]{style="font-family:宋体"}[Network LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[nssa]{lang="EN-US"}**]{#struct_0_78893_x1682_746812653}[：表示]{style="font-family:宋体"}[NSSA External LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[opaque-area]{lang="EN-US"}**]{#struct_0_78893_x1682_483456460}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Opaque-area LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[opaque-as]{lang="EN-US"}**]{#struct_0_78893_x1682_x445895217}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Opaque-AS LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[opaque-link]{lang="EN-US"}**]{#struct_0_78893_x1682_1987927552}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Opaque-link LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[router]{lang="EN-US"}**]{#struct_0_78893_x1682_379638817}[：表示]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_78893_x1682_1179691758}[：表示]{style="font-family:宋体"}[Network Summary LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[*[link-state-id]{lang="EN-US"}*]{#struct_0_78893_x1682_709148709}[：]{style="font-family:宋体"}[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x373807724}

[**[debugging ospf lsa]{lang="EN-US"}**]{#struct_0_78893_x1682_x585741812}[命令用来打开]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf lsa]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x253838938}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1887868902}[进程的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging ospf lsa]{lang="EN-US"}]{#struct_0_78893_x1682_x1379675758}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1675162381}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_848642729}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1796739487}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1210997632}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_689991884}[进程号]{style="font-family:宋体"}

[*[op-type]{lang="NO-BOK"}*]{#struct_0_78893_x1682_x1417898245}[ LSA at x ms]{lang="NO-BOK"}

[[对]{style="font-family:宋体"}]{#struct_0_78893_x1682_235920990}[LSA]{lang="NO-BOK"}[进行操作：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}*[op-type]{lang="NO-BOK"}*]{#struct_0_78893_x1682_848708265}[：]{lang="EN-US" style="font-family:宋体"}[表示对]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="NO-BOK"}[进行何种操作]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:宋体"}[Generate]{lang="NO-BOK"}[表示生成]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="NO-BOK"}[，]{lang="EN-US" style="font-family:宋体"}[Install]{lang="NO-BOK"}[表示安装]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="NO-BOK"}

[[LSA type: *ls-type* Link state ID: *link-state-id*]{lang="EN-US"}]{#struct_0_78893_x1682_980395978}

[[Advertising router*: rt-id*]{lang="EN-US"}]{#struct_0_78893_x1682_2127256646}

[[LSA ]{lang="EN-US"}]{#struct_0_78893_x1682_x1775157789}[头部信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-type]{lang="EN-US"}*]{#struct_0_78893_x1682_1813384339}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[类型，]{lang="EN-US" style="font-family:宋体"}*[LSA-type]{lang="EN-US"}*[的取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[Router LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[network LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[net-summary LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[ASBR-summary LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[AS-external --LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[NSSA LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[9/10/11]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[l]{lang="EN-US"}[ink-state-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1927075767}[：]{lang="EN-US" style="font-family:宋体"}[LSA ]{lang="EN-US"}[标识]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_848773801}[：生成]{lang="EN-US" style="font-family:宋体"}[LSA ]{lang="EN-US"}[的路由器的标识]{lang="EN-US" style="font-family:宋体"}

[[LSA age: *age*  Options : External routing: *ON/OFF*]{lang="EN-US"}]{#struct_0_78893_x1682_x1345852385}

[[LSA ]{lang="EN-US"}]{#struct_0_78893_x1682_x1424682386}[头部信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[age]{lang="EN-US"}*]{#struct_0_78893_x1682_478507418}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[年龄字段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ON/OFF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1635961630}[：表示支持或不支持外部路由]{lang="EN-US" style="font-family:宋体"}

[[Length: *ls-len * Sequence number: *seq-num* Checksum:*checksum*]{lang="EN-US"}]{#struct_0_78893_x1682_848839337}

[[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x1961091902}[头部信息；]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Ls-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1336917474}[：]{lang="EN-US" style="font-family:宋体"}[LS]{lang="EN-US"}[长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Seq-num]{lang="EN-US"}*]{#struct_0_78893_x1682_x169278845}[：]{lang="EN-US" style="font-family:宋体"}[LS]{lang="EN-US"}[序列号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Checksum]{lang="EN-US"}*]{#struct_0_78893_x1682_1745320902}[：除]{lang="EN-US" style="font-family:宋体"}[LSA age]{lang="EN-US"}[字段外整个]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的校验和]{lang="EN-US" style="font-family:宋体"}

[[Capabilities: VBit: EBit: BBit: NtBit: Link count: *link-count* TOS# *tos-num*  Metric *cost*]{lang="EN-US"}]{#struct_0_78893_x1682_848904873}

[[Router LSA]{lang="EN-US"}]{#struct_0_78893_x1682_837020706}[的内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[VBit]{lang="EN-US"}*]{#struct_0_78893_x1682_315397591}[：]{lang="EN-US" style="font-family:宋体"}[0x40]{lang="EN-US"}[，表示]{lang="EN-US" style="font-family:宋体"}[virtual link]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[EBit]{lang="EN-US"}*]{#struct_0_78893_x1682_693687394}[：]{lang="EN-US" style="font-family:宋体"}[0x200]{lang="EN-US"}[，表示]{lang="EN-US" style="font-family:宋体"}[Exteranl LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[BBit]{lang="EN-US"}*]{#struct_0_78893_x1682_805072181}[：]{lang="EN-US" style="font-family:宋体"}[0x100]{lang="EN-US"}[，表示]{lang="EN-US" style="font-family:宋体"}[ABR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[NtBit]{lang="PT-BR"}]{#struct_0_78893_x1682_847921833}[：]{lang="EN-US" style="font-family:宋体"}[0x1000]{lang="PT-BR"}[，表示该路由器无条件进行了]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="PT-BR"}[到]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="PT-BR"}[的转换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Link-count]{lang="EN-US"}*]{#struct_0_78893_x1682_x502027779}[：]{lang="EN-US" style="font-family:宋体"}[Router LSA]{lang="EN-US"}[描述的链路数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tos-num]{lang="EN-US"}*]{#struct_0_78893_x1682_783961677}[：]{lang="EN-US" style="font-family:宋体"}[Router LSA]{lang="EN-US"}[中的]{lang="EN-US" style="font-family:宋体"}[TOS]{lang="EN-US"}[数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_x721415882}[：链路代价]{lang="EN-US" style="font-family:宋体"}

[[Network mask: *net-mask* Neighbor router: *rt-id*]{lang="EN-US"}]{#struct_0_78893_x1682_847987369}

[[Network LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x133577684}[内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[net-mask]{lang="EN-US"}*]{#struct_0_78893_x1682_2092860587}[：网段掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_846351148}[：路由器发现的邻居的标识符]{style="font-family:宋体"}

[[Network mask: *net-mask* Metric: *cost*]{lang="EN-US"}]{#struct_0_78893_x1682_848446122}

[[Summary, ASBR-Summary LSA]{lang="EN-US"}]{#struct_0_78893_x1682_311625008}[内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[net-mask]{lang="EN-US"}*]{#struct_0_78893_x1682_1338113129}[：网段掩码]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_x2003203691}[：链路代价]{lang="EN-US" style="font-family:宋体"}

[[Network mask: *net-mask* TOS: *tos* Metric: *cost* Forwarding address: *fwd-addr* External route tag: *rt-tag*]{lang="EN-US"}]{#struct_0_78893_x1682_848511658}

[[AS_External LSA, NSSA LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x1664255400}[内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[net-mask]{lang="EN-US"}*]{#struct_0_78893_x1682_961936027}[：网段掩码]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tos]{lang="EN-US"}*]{#struct_0_78893_x1682_x1387060400}[：服务类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_848577194}[：链路代价]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[fwd-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1907099023}[：转发地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-tag]{lang="EN-US"}*]{#struct_0_78893_x1682_137117023}[：外部路由标志]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_724382951}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_848642730}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[LSA]{lang="EN-US"}[安装到]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[库中的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf lsa install]{lang="SV"}]{#struct_0_78893_x1682_541912680}

[\<RouterA\>]{lang="SV"}

[\*Sep  8 17:51:02:234 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4796222 ms:]{lang="SV"}

[\*Sep  8 17:51:02:244 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="SV"}

[\*Sep  8 17:51:02:244 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 201.1.1.1.]{lang="SV"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.]{lang="SV"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000008 CheckSum: 60445.]{lang="EN-US"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 0 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.2 55.0 LinkType: 3.]{lang="EN-US"}

[\*Sep  8 17:51:02:254 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// OSPF]{lang="PT-BR"}*]{#struct_0_78893_x1682_1048173880}*[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[安装由自己生成的]{style="font-family:宋体"}[Router-LSA]{lang="PT-BR"}*

[[\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4800748 ms:]{lang="PT-BR"}]{#struct_0_78893_x1682_848708266}

[\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="PT-BR"}

[\*Sep  8 17:51:06:766 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 202.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 202.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 5 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000001 CheckSum: 5373.]{lang="EN-US"}

[\*Sep  8 17:51:06:776 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 256 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.255.0 LinkType: 3.]{lang="EN-US"}

[\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// OSPF]{lang="PT-BR"}*]{#struct_0_78893_x1682_980395975}*[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[安装由对端生成的]{style="font-family:宋体"}[Router-LSA]{lang="PT-BR"}*

[[\*Sep  8 17:51:06:786 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4800748 ms:]{lang="PT-BR"}]{#struct_0_78893_x1682_2127256659}

[\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 2.]{lang="PT-BR"}

[\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 150.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:06:806 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Length: 32 Seq# 80000001 CheckSum: 2890.]{lang="EN-US"}

[\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0.]{lang="EN-US"}

[\*Sep  8 17:51:06:816 2006 RouterA OSPF/6/OSPFDEBUG:Neighbor router: 202.1.1.1.]{lang="EN-US"}

[\*Sep  8 17:51:06:826 2006 RouterA OSPF/6/OSPFDEBUG:Neighbor router: 201.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_x1774567964}*[由于本端是]{style="font-family:宋体"}[DR]{lang="EN-US"}[，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[安装由自己生成的]{style="font-family:宋体"}[Network-LSA]{lang="EN-US"}*

[[\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4801229 ms:]{lang="EN-US"}]{#struct_0_78893_x1682_848773802}

[\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="EN-US"}

[\*Sep  8 17:51:07:238 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 201.1.1.1.]{lang="EN-US"}

[\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.]{lang="EN-US"}

[\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 17:51:07:248 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000009 CheckSum: 34281.]{lang="EN-US"}

[\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 0 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.1 LinkData: 150.1.1.1 LinkType: 2.]{lang="EN-US"}

[\*Sep  8 17:51:07:258 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// OSPF]{lang="PT-BR"}*]{#struct_0_78893_x1682_x1345852386}*[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[安装由自己生成的]{style="font-family:宋体"}[Router-LSA]{lang="PT-BR"}[。其中的]{style="font-family:宋体"}[stub link]{lang="PT-BR"}[变为]{style="font-family:宋体"}[transit link]{lang="PT-BR"}*

[[\*Sep  8 17:51:11:710 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 4805705 ms:]{lang="PT-BR"}]{#struct_0_78893_x1682_141401555}

[\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="PT-BR"}

[\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 202.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 202.1.1.1.]{lang="PT-BR"}

[\*Sep  8 17:51:11:720 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 1 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000002 CheckSum: 47803.]{lang="EN-US"}

[\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 512 BBit: 256 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Sep  8 17:51:11:731 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.1 LinkData: 150.1.1.2 LinkType: 2.]{lang="EN-US"}

[\*Sep  8 17:51:11:741 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// OSPF]{lang="PT-BR"}*]{#struct_0_78893_x1682_x587308295}*[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[安装对端的]{style="font-family:宋体"}[Router-LSA]{lang="PT-BR"}[。其中的]{style="font-family:宋体"}[stub link]{lang="PT-BR"}[变为]{style="font-family:宋体"}[transit link]{lang="PT-BR"}*

[[\*Sep  8 18:00:27:660 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Install LSA at 5361645 ms:]{lang="PT-BR"}]{#struct_0_78893_x1682_848839338}

[\*Sep  8 18:00:27:660 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 5.]{lang="PT-BR"}

[\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 123.1.1.0.]{lang="PT-BR"}

[\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 201.1.1.1.]{lang="PT-BR"}

[\*Sep  8 18:00:27:670 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 80000001 CheckSum: 25377.]{lang="EN-US"}

[\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0.]{lang="EN-US"}

[\*Sep  8 18:00:27:680 2006 RouterA OSPF/6/OSPFDEBUG:TOS: 128 Metric: 001 Forwarding address  0.0.0.0 External route tag 0.0.0.1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1961091895}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[安装]{style="font-family:宋体"}[5]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}[，对应引入路由为]{style="font-family:宋体"}[123.1.1.0 255.255.255.0]{lang="EN-US"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_228707714}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1(150.1.1.1/24)]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1(150.1.1.2/24)]{lang="EN-US"}[相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf lsa generate]{lang="EN-US"}]{#struct_0_78893_x1682_706136262}

[\<RouterA\>]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Generate LSA at 6352610 ms:]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 1.1.1.1.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 1.1.1.1.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 8000002c CheckSum:  3185.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 0 BBit: 0 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.0 LinkData: 255.255.255.0 LinkType: 3.]{lang="EN-US"}

[\*Dec 12 11:07:33:610 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_155919129}*[生成]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}*

[[%Dec 12 11:07:33:708 2006 RouterA RM/3/RMLOG:OSPF-NBRCHANGE: Process 1, Neighbour 150.1.1.2(GigabitEthernet1/0/1) from Loading to Full]{lang="EN-US"}]{#struct_0_78893_x1682_848904874}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Generate LSA at 6357625 ms:]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LSA type: 1.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LinkStateId: 1.1.1.1.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Advertising Rtr: 1.1.1.1.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LSA Age: 0 Options: ExRouting:ON.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Length: 36 Seq# 8000002d CheckSum: 44595.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:Capabilities: VBit:0 EBit: 0 BBit:  0 NtBit: 0 Link count: 1.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:LinkID: 150.1.1.2 LinkData: 150.1.1.1 LinkType: 2.]{lang="EN-US"}

[\*Dec 12 11:07:38:630 2006 RouterA OSPF/6/OSPFDEBUG:TOS# 0 Metric 10.]{lang="PT-BR"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_837020711}*[邻居]{style="font-family:宋体"}[FULL]{lang="EN-US"}[之后生成]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}*

::: {#1452028164 .myid}
[]{#_Toc148240885}[]{#_Toc300065254}[]{#_Toc404787734}[]{#struct_0_78893_x1682_x1640917542}[]{#_Toc343678075}

**OSPF \-- OSPF调试命令 \-- debugging ospf non-stop-routing**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1378673085}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **non-stop-routing**]{lang="EN-US"}]{#struct_0_78893_x1682_x607475352}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **non-stop-routing**]{lang="EN-US"}]{#struct_0_78893_x1682_x1336723347}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x972348438}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_x663003831}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_847921834}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x502027786}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_784813638}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x744329577}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_676801144}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1329900261}

[**[debugging ospf non-stop-routing]{lang="EN-US"}**]{#struct_0_78893_x1682_1387541179}[命令用来打开]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf non-stop-routing]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}]{#struct_0_78893_x1682_x652940443}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x722537751}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging ospf non-stop-routing]{lang="EN-US"}]{#struct_0_78893_x1682_847987370}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1647654654}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_1822737459}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_739491561}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x825451038}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x580618764}[进程号]{style="font-family:宋体"}

[[begin to backup configuration data\...]{lang="EN-US"}]{#struct_0_78893_x1682_x1952669611}

[[开始批备配置数据]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1840602684}

[[begin to backup running data\...]{lang="EN-US"}]{#struct_0_78893_x1682_848446119}

[[开始批备运行数据]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1262353109}

[[begin to backup lsa data\...]{lang="EN-US"}]{#struct_0_78893_x1682_x1436458931}

[[开始批备]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_1284325298}[数据]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1512391019}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_839827314}[开始进行主备倒换，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf non-stop-routing]{lang="SV"}]{#struct_0_78893_x1682_848511655}

[\<RouterA\>]{lang="SV"}

[\*Dec 13 04:47:30:586 2012 RouterA  OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup configuration data\...]{lang="SV"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1664255405}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[开始批备配置数据]{style="font-family:宋体"}*

[[\*Dec 13 04:47:30:590 2012 RouterA OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup running data\...]{lang="SV"}]{#struct_0_78893_x1682_558651500}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1223905831}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[开始批备运行数据]{style="font-family:宋体"}*

[[\*Dec 13 04:47:30:590 2012 RouterA OSPF/7/DEBUG: -MDC=1; OSPF 1 begin to backup lsa data\...]{lang="SV"}]{#struct_0_78893_x1682_1083193429}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_1077609142}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[开始批备]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数据]{style="font-family:宋体"}*

::: {#740484893 .myid}
[]{#_Toc404787735}[]{#struct_0_78893_x1682_369957710}

**OSPF \-- OSPF调试命令 \-- debugging ospf packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1177208106}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **packet** \[ **ack** \| **dd** \| **filter** { **interface** *interface-type interface-number* \| { **source** \| **destination** } { **acl** *acl-num* \| **prefix-list** *prefix-list-name* } } \* \| **hello** \| **request** \| **update** \]]{lang="EN-US"}]{#struct_0_78893_x1682_x1405644687}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **packet** \[ **ack** \| **dd** \| **filter** \| **hello** \| **request** \| **update** \]]{lang="EN-US"}]{#struct_0_78893_x1682_848577191}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1907099026}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_137444703}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_859601803}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x1035678370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x833102556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1612368707}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1371297249}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ack]{lang="EN-US"}**]{#struct_0_78893_x1682_848642727}[：表示]{style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[dd]{lang="EN-US"}**]{#struct_0_78893_x1682_x1796739485}[：表示]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[filter]{lang="EN-US"}**]{#struct_0_78893_x1682_x985357799}[：表示打开过滤报文的开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_78893_x1682_2013962851}[：接口类型和编号]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_78893_x1682_x894890464}[：指定报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_78893_x1682_x985423335}[：指定报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_78893_x1682_x1067069360}[：指定用于过滤的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[号，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_78893_x1682_x551607478}[：指定用于过滤的地址前缀列表名称，]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[hello]{lang="EN-US"}**]{#struct_0_78893_x1682_1921170250}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[request]{lang="EN-US"}**]{#struct_0_78893_x1682_624047046}[：表示]{style="font-family:宋体"}[LSR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[update]{lang="EN-US"}**]{#struct_0_78893_x1682_x2022824493}[：表示]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1137192998}

[**[debugging ospf packet]{lang="EN-US"}**]{#struct_0_78893_x1682_x2110849493}[命令用来打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging ospf packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_2059162007}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1203318521}[进程的报文调试信息。]{style="font-family:宋体"}

[[如果未指定任何参数，则表示打开所有报文的调试信息开关。]{style="font-family:宋体"}]{#struct_0_78893_x1682_x985554407}

[]{#_Toc130718927}[[表1-8 ]{lang="EN-US"}[debugging ospf packet]{lang="EN-US"}]{#struct_0_78893_x1682_848708263}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1644288454}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_980395972}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_2127256652}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1774895644}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x756394894}[进程号]{style="font-family:宋体"}

[[Sending packets]{lang="EN-US"}]{#struct_0_78893_x1682_810426322}

[[发送]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_956614940}[报文]{style="font-family:宋体"}

[[Receiving packets]{lang="EN-US"}]{#struct_0_78893_x1682_848773799}

[[接收]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_2092756672}[报文]{style="font-family:宋体"}

[[Source address: *src-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_55457096}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x270840561}[报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Destination address: *dst-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_1334051585}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1036165240}[报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Version *ver*, Type*: pkt-type*, Length: *pkt-len*]{lang="NO-BOK"}]{#struct_0_78893_x1682_848839335}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1961091900}[报文头信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ver]{lang="EN-US"}*]{#struct_0_78893_x1682_x174118060}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议版本，当前为]{style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pkt-type]{lang="EN-US"}*]{#struct_0_78893_x1682_x125280994}[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文类型，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[LSR]{lang="EN-US"}[报文、]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文、取值为]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pkt-len]{lang="EN-US"}*]{#struct_0_78893_x1682_691929261}[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文长度]{lang="EN-US" style="font-family:宋体"}

[[Router: *rt-id*, Area: *area-id*, Checksum: *chksum*]{lang="EN-US"}]{#struct_0_78893_x1682_848904871}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_837020708}[报文头信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_315397601}[：生成]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文的路由器标识]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1832804295}[：发送报文的接口所属的区域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[chksum]{lang="EN-US"}*]{#struct_0_78893_x1682_x703643218}[：从]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文头开始，除了]{style="font-family:宋体"}[64]{lang="EN-US"}[位的认证域外，整个报文的校验和]{style="font-family:宋体"}

[[Authentication type: *auth-type*, Key(ASCII): *key*]{lang="EN-US"}]{#struct_0_78893_x1682_847921831}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x502027781}[报文头信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[au-type]{lang="EN-US"}*]{#struct_0_78893_x1682_784485958}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文认证类型，取值为]{style="font-family:宋体"}[00]{lang="EN-US"}[表示无认证，为]{style="font-family:宋体"}[01]{lang="EN-US"}[表示简单认证，为]{style="font-family:宋体"}[02]{lang="EN-US"}[表示]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[key]{lang="EN-US"}*]{#struct_0_78893_x1682_1811039427}[：认证码]{lang="EN-US" style="font-family:宋体"}

[[Network mask: *net-mask*]{lang="EN-US"}]{#struct_0_78893_x1682_847987367}*[，]{style="font-family:宋体"}*[Hello interval: *hello-interval*]{lang="EN-US"}*[，]{style="font-family:宋体"}*[Option: *opt*]{lang="EN-US"}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_x133577674}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[net-mask]{lang="EN-US"}*]{#struct_0_78893_x1682_2092860582}[：发送报文的接口的网络掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[hello-interval]{lang="EN-US"}*]{#struct_0_78893_x1682_846678828}[：发送报文的时间间隔，单位为秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[opt]{lang="EN-US"}*]{#struct_0_78893_x1682_x868890510}[：路由器支持的可选能力、]{lang="EN-US" style="font-family:宋体"}[E bit]{lang="EN-US"}[为支持外部路由、]{lang="EN-US" style="font-family:宋体"}[N/P bit ]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[能力、]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[表示支持]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[转]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L bit]{lang="EN-US"}[表示报文后带有扩展与]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[有关的扩展数据]{lang="EN-US" style="font-family:宋体"}

[[Router priority: *rt-pri,* Dead Interval: *dead-interval,* DR: *ip-addr, * BDR: *ip-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_848446120}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_311625010}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-pri]{lang="EN-US"}*]{#struct_0_78893_x1682_x618202015}[：路由器的优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dead-interval]{lang="EN-US"}*]{#struct_0_78893_x1682_568584389}[：邻居失效的时间间隔，单位为秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_848511656}[：接口网段上]{lang="EN-US" style="font-family:宋体"}[DR]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[BDR]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Neighbor ID: *rt-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1664255402}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_2124735441}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_663865715}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[已发现的邻居的路由器标识符]{style="font-family:宋体"}

[[Hello: hello timer mismatch]{lang="EN-US"}]{#struct_0_78893_x1682_848577192}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_1907099025}[报文信息：路由器与邻居]{style="font-family:宋体"}[Hello interval]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Hello: dead timer mismatch]{lang="EN-US"}]{#struct_0_78893_x1682_137248095}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_615658622}[报文信息：路由器与邻居]{style="font-family:宋体"}[Dead interval]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Hello: netmask mismatch]{lang="EN-US"}]{#struct_0_78893_x1682_848642728}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_x1796739488}[报文信息：路由器与邻居网段掩码不一致]{style="font-family:宋体"}

[[Hello: option mismatch]{lang="EN-US"}]{#struct_0_78893_x1682_x1970512519}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_1558264464}[报文信息：路由器与邻居对可选能力的支持不一致]{style="font-family:宋体"}

[[Extended options(LLS data): *option*]{lang="EN-US"}]{#struct_0_78893_x1682_848708264}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_78893_x1682_980395977}[、]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_78893_x1682_2127256657}[：与]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[有关的选项、]{lang="EN-US" style="font-family:宋体"}[LR]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[OOB]{lang="EN-US"}[协商、]{lang="EN-US" style="font-family:宋体"}[RS]{lang="EN-US"}[通知邻居进入]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[Graceful  Restart]{lang="EN-US"}[）。]{lang="EN-US" style="font-family:
  宋体"}

[[MTU:*mtu-val,* Option:  *option,* R_I_M_MS Bit: *bits*]{lang="SV"}]{#struct_0_78893_x1682_848773800}

[[OSPF DD]{lang="EN-US"}]{#struct_0_78893_x1682_x1345852384}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mtu-val]{lang="EN-US"}*]{#struct_0_78893_x1682_1304200969}[：接口不分片而能发送的最大]{style="font-family:宋体"}[IP]{lang="EN-US"}[包字节大小。如果接口没有配置]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文中]{style="font-family:宋体"}[MTU]{lang="EN-US"}[域的值为发送该报文接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}[,]{lang="EN-US"}[该值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_78893_x1682_848839336}[：路由器支持的可选能力，取值]{lang="EN-US" style="font-family:宋体"}[E bit]{lang="EN-US"}[表示支持外部路由]{lang="EN-US" style="font-family:宋体"}[N/P bti ]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[能力、]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[表示支持]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[转]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[L bit]{lang="EN-US"}[表示报文后带有扩展与]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[有关的扩展数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bits]{lang="EN-US"}*]{#struct_0_78893_x1682_x1961091901}[：]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文协商标志位，取值]{lang="EN-US" style="font-family:宋体"}[I bit]{lang="EN-US"}[表示协商开始、]{lang="EN-US" style="font-family:宋体"}[M bit]{lang="EN-US"}[表示还有]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[包要交互、]{lang="EN-US" style="font-family:宋体"}[MS bit]{lang="EN-US"}[表示自己是]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[R bit]{lang="EN-US"}[表示开始进行]{lang="EN-US" style="font-family:宋体"}[OOB]{lang="EN-US"}[，可以是这几个值的组合]{lang="EN-US" style="font-family:宋体"}

[[DD Sequence number: *seq-num*]{lang="PT-BR"}]{#struct_0_78893_x1682_x1740202001}

[[OSPF DD]{lang="EN-US"}]{#struct_0_78893_x1682_848904872}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seq-num]{lang="EN-US"}*]{#struct_0_78893_x1682_837020705}[：]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文的序号]{lang="EN-US" style="font-family:宋体"}

[[LSA type: *ls-type,* Link state ID: *ls-id,* Advertising router: *rt-id*]{lang="EN-US"}]{#struct_0_78893_x1682_315397590}

[[OSPF DD]{lang="EN-US"}]{#struct_0_78893_x1682_847921832}[、]{style="font-family:宋体"}[LSR]{lang="EN-US"}[、]{style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文信息]{style="font-family:宋体"}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x502027780}[报文中描述的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-type]{lang="EN-US"}*]{#struct_0_78893_x1682_784420422}[：]{lang="EN-US" style="font-family:宋体"}*[ ]{lang="EN-US"}*[LSA]{lang="EN-US"}[的类型，取值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[Router LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[network LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[net-summary LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[ASBR-summary LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[AS-external --LSA]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[NSSA LSA]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[9]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[10]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[11]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-id]{lang="EN-US"}*]{#struct_0_78893_x1682_847987368}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[rt-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x133577685}[：]{lang="EN-US" style="font-family:宋体"}*[ ]{lang="EN-US"}*[通告]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的路由器的标识符]{lang="EN-US" style="font-family:宋体"}

[[LSA age: *ls-age, * Options: External routing:ON/OFF]{lang="EN-US"}]{#struct_0_78893_x1682_2092795051}

[[OSPF DD]{lang="EN-US"}]{#struct_0_78893_x1682_x1880437232}[、]{style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ls-age]{lang="EN-US"}]{#struct_0_78893_x1682_400873172}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[age]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ON/OFF]{lang="EN-US"}]{#struct_0_78893_x1682_476218341}[：路由器外部路由能力的支持]{lang="EN-US" style="font-family:宋体"}

[[Length: *ls-len*, Sequence number: *seq-num,*  Checksum: *checksum*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880371696}

[[OSPF DD]{lang="EN-US"}]{#struct_0_78893_x1682_x60344888}[、]{style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1089497535}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的字节长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seq-num]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880306160}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的序列号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[checksum]{lang="EN-US"}*]{#struct_0_78893_x1682_2087459926}[：]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[中的校验和]{lang="EN-US" style="font-family:宋体"}

[[LSA count: *ls-count*]{lang="EN-US"}]{#struct_0_78893_x1682_854211386}

[[OSPF LSU]{lang="EN-US"}]{#struct_0_78893_x1682_x1880240624}[报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-count]{lang="EN-US"}*]{#struct_0_78893_x1682_1626504013}[：]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文中包含的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[数]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1516789967}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_x520669958}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF HELLO]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf packet hello]{lang="EN-US"}]{#struct_0_78893_x1682_x1880175088}

[\<RouterA\>]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 39833.]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68908828 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR: 0.0.0.0.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_1633754880}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。目前为止，没有发现任何邻居]{style="font-family:宋体"}*

[[\*0.68913955 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}]{#struct_0_78893_x1682_1546404437}

[\*0.68913955 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 12700.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 0.0.0.0, BDR: 0.0.0.0.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_1931702504}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[收到对方]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。目前为止，对方也是没有发现任何邻居]{style="font-family:宋体"}*

[[\*0.68918832 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.]{lang="EN-US"}]{#struct_0_78893_x1682_x1880109552}

[\*0.68918832 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1]{lang="EN-US"}

[\*0.68918832 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 53394.]{lang="EN-US"}

[\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68918842 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68918852 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[0.0.0.0.]{lang="EN-US"}

[\*0.68918852 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 202.1.1.1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_1237648776}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。已经发现邻居]{style="font-family:宋体"}[202.1.1.1]{lang="EN-US"}*

[[\*0.68924260 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}]{#struct_0_78893_x1682_x1217414742}

[\*0.68924260 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[150.1.1.2.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x902183588}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[收到对方的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。选举]{style="font-family:宋体"}[150.1.1.1]{lang="EN-US"}[为]{style="font-family:宋体"}[DR]{lang="EN-US"}[，]{style="font-family:宋体"}[150.1.1.2]{lang="EN-US"}[为]{style="font-family:宋体"}[BDR]{lang="EN-US"}*

[[\*0.68928827 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Sending packets.]{lang="EN-US"}]{#struct_0_78893_x1682_x1880044016}

[\*0.68928827 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.1]{lang="EN-US"}

[\*0.68928827 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Router: 201.1.1.1, Area: 0.0.0.0, Checksum: 14735.]{lang="EN-US"}

[\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68928837 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68928847 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[150.1.1.2.]{lang="EN-US"}

[\*0.68928847 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 202.1.1.1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x974494587}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发送保持邻居关系的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}]{#struct_0_78893_x1682_1886377203}

[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[150.1.1.2.]{lang="EN-US"}

[\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1012935322}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[收到对方为保持邻居关系发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_78893_x1682_x985095657}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的报文过滤调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf packet filter source prefix-list pl1]{lang="EN-US"}]{#struct_0_78893_x1682_x985685480}

[\<RouterA\> system-view]{lang="EN-US"}

[\[RouterA\] ip prefix-list pl1 index 1 permit 150.1.1.2 32]{lang="EN-US"}

[\[RouterA\]]{lang="EN-US"}

[\*0.68913955 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}

[\*0.68913955 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 44.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 12700.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68913965 RouterA OSPF/6/OSPFDEBUG: Router priority: 1, Dead Interval: 40, DR: 0.0.0.0, BDR: 0.0.0.0.]{lang="EN-US"}

[\*0.68924260 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}

[\*0.68924260 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68924270 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[150.1.1.2.]{lang="EN-US"}

[\*0.68924280 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.]{lang="EN-US"}

[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:OSPF 1: Receiving packets.]{lang="EN-US"}

[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Source address: 150.1.1.2]{lang="EN-US"}

[\*0.68934274 RouterA OSPF/6/OSPFDEBUG:Destination address: 224.0.0.5]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Version 2, Type: 1, Length: 48.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Router: 202.1.1.1, Area: 0.0.0.0, Checksum: 14735.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Authentication type: 00, Key(ASCII): 0 0 0 0 0 0 0 0.]{lang="EN-US"}

[\*0.68934284 RouterA OSPF/6/OSPFDEBUG:Network mask: 255.255.255.0, Hello interval: 10, Option: \_E\_.]{lang="EN-US"}

[\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Router priority: 1, Dead Interval: 40, DR: 150.1.1.1, BDR:]{lang="EN-US"}

[150.1.1.2.]{lang="EN-US"}

[\*0.68934294 RouterA OSPF/6/OSPFDEBUG:Neighbor ID: 201.1.1.1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_860523579}*[指定报文源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[150.1.1.2]{lang="EN-US"}[，通过地址前缀列表]{style="font-family:宋体"}[pl1]{lang="EN-US"}[过滤的报文信息]{style="font-family:宋体"}*

::: {#-11862230 .myid}
[]{#_Toc300065255}[]{#_Toc404787736}[]{#struct_0_78893_x1682_x1879978480}[]{#_Toc348020480}[]{#_Toc340741957}

**OSPF \-- OSPF调试命令 \-- debugging ospf policy**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_62976008}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **redistribute** \| **spf** }]{lang="EN-US"}]{#struct_0_78893_x1682_1727678469}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **redistribute** \| **spf** }]{lang="EN-US"}]{#struct_0_78893_x1682_x304686993}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1592580833}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_1532254218}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1692777743}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x1063051090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_803037556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1880961520}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_846277704}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[abr-filter]{lang="EN-US"}**]{#struct_0_78893_x1682_515546507}[：打开]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[过策略的调试开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_78893_x1682_536661391}[：打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[所有策略的调试开关。]{style="font-family:宋体"}

[**[default-route]{lang="EN-US"}**]{#struct_0_78893_x1682_x540892834}[：打开默认路由过策略的调试开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_78893_x1682_x24368994}[：打开策略事件的调试开关。]{style="font-family:宋体"}

[**[redistribute]{lang="EN-US"}**]{#struct_0_78893_x1682_x1004393721}[：打开引入路由过策略的调试开关。]{style="font-family:宋体"}

[**[spf]{lang="EN-US" style="color:black"}**]{#struct_0_78893_x1682_x235961914}[：打开路由过策略的调试开关。]{style="font-family:宋体;
color:black"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x653496738}

[**[debugging ospf policy]{lang="EN-US"}**]{#struct_0_78893_x1682_x1880895984}[命令用来打开]{style="font-family:宋体"}[过]{style="font-family:宋体"}[策略的调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf policy]{lang="EN-US"}**[用来关闭]{style="font-family:宋体"}[过]{style="font-family:宋体"}[策略的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}]{#struct_0_78893_x1682_1778576197}[过]{style="font-family:宋体"}[策略的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x2105348084}[进程的]{style="font-family:宋体"}[过策略]{style="font-family:宋体"}[调试信息。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging ospf policy]{lang="EN-US"}]{#struct_0_78893_x1682_x1694000793}**[ ]{lang="EN-US"}**[abr-filter]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1655275977}[[字段]{style="font-family:黑体;
   color:#0096d6"}]{#struct_0_78893_x1682_1241148649}
:::

[[含义]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_x503125869}

[[OSPF *process-id* area *area-id* checked abr-filter *type*, dest: *address*, mask: *mask*, result: *result*, cost:*cost*]{lang="EN-US"}]{#struct_0_78893_x1682_x754894877}

[[Type-3 LSA]{lang="EN-US"}]{#struct_0_78893_x1682_542449823}[过策略结果]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880437231}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area]{lang="EN-US"}[-]{lang="EN-US"}*]{#struct_0_78893_x1682_1966957113}*[id]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x341867805}[：策略类型，]{style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:宋体"}[import]{lang="EN-US"}[表示向本区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过策略，]{style="font-family:宋体"}[export]{lang="EN-US"}[表示向其它区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[address]{lang="EN-US"}*]{#struct_0_78893_x1682_1332136651}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_78893_x1682_x1164432437}[：掩码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_x857623039}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880371695}[：表示过策略后的开销]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging ospf policy]{lang="EN-US"}]{#struct_0_78893_x1682_1505739053}[ ]{lang="EN-US"}[default-route]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1656442895}[[字段]{style="font-family:黑体;
   color:#0096d6"}]{#struct_0_78893_x1682_x933217034}

[[含义]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_x2075753443}

[[OSPF *process-id* registered default-route policy: *policy-name*, result: *result*]{lang="EN-US"}]{#struct_0_78893_x1682_1905722345}

[[注册默认路由策略]{style="font-family:宋体"}]{#struct_0_78893_x1682_x2055194025}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880306159}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[policy-name]{lang="EN-US"}*]{#struct_0_78893_x1682_x997588253}[：]{lang="EN-US" style="font-family:
  宋体"}[策略名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_169443635}[：返回结果，]{style="font-family:宋体"}[success]{lang="EN-US"}[表示注册成功，]{style="font-family:宋体"}[fail]{lang="EN-US"}[表示注册失败]{style="font-family:宋体"}

[[OSPF *process-id* deregistered default-route policy: *policy-name*, result: *result*]{lang="EN-US"}]{#struct_0_78893_x1682_x2047393445}

[[注销默认路由策略]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1996705932}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_965295337}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[policy-name]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880240623}[：]{lang="EN-US" style="font-family:
  宋体"}[策略名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_2029788540}[：返回结果，]{style="font-family:宋体"}[success]{lang="EN-US"}[表示注销成功，]{style="font-family:宋体"}[fail]{lang="EN-US"}[表示注销失败]{style="font-family:宋体"}

[[OSPF *process-id* received default-route policy message, result: *result*, flag: *flag*, cost type: *type*, cost: *cost*, tag: *tag*, policy-name: *name*]{lang="EN-US"}]{#struct_0_78893_x1682_x1406743524}

[[接收到默认路由过策略消息]{style="font-family:宋体"}]{#struct_0_78893_x1682_822528492}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1570014399}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880175087}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x1095128475}[：标志位，]{style="font-family:宋体"}[0x0]{lang="EN-US"}[表示无应用，]{style="font-family:宋体"}[0x1]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost]{lang="EN-US"}[，]{style="font-family:宋体"}[0x2]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost type]{lang="EN-US"}[，]{style="font-family:宋体"}[0x8]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[tag]{lang="EN-US"}[，若存在多个应用，该标志位为或的关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_1820585043}[：默认路由类型，]{style="font-family:宋体"}[type-1]{lang="EN-US"}[表示一类外部路由，]{style="font-family:宋体"}[type-2]{lang="EN-US"}[表示二类外部路由，]{style="font-family:宋体"}[unknown]{lang="EN-US"}[表示未知类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_88069480}[：默认路由开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tag]{lang="EN-US"}*]{#struct_0_78893_x1682_226605525}[：标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880109551}[：]{lang="EN-US" style="font-family:宋体"}[策略名]{style="font-family:宋体"}

[[OSPF *process-id* checked default-route policy, result: permit, flag: *flag*, cost type: *type*, cost: *cost*, tag: *tag*]{lang="EN-US"}]{#struct_0_78893_x1682_1640933303}

[[默认路由过策略通过后的结果]{style="font-family:宋体"}]{#struct_0_78893_x1682_1986579987}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_1984120474}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x696223914}[：标志位，]{style="font-family:宋体"}[0x0]{lang="EN-US"}[表示无应用，]{style="font-family:宋体"}[0x1]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost]{lang="EN-US"}[，]{style="font-family:宋体"}[0x2]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost type]{lang="EN-US"}[，]{style="font-family:宋体"}[0x8]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[tag]{lang="EN-US"}[，若存在多个应用，该标志位为或的关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880044015}[：默认路由类型，]{style="font-family:宋体"}[type-1]{lang="EN-US"}[表示一类外部路由，]{style="font-family:宋体"}[type-2]{lang="EN-US"}[表示二类外部路由，]{style="font-family:宋体"}[unknown]{lang="EN-US"}[表示未知类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_78893_x1682_x571210060}[：默认路由开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tag]{lang="EN-US"}*]{#struct_0_78893_x1682_193921494}[：标签]{style="font-family:宋体"}

[[OSPF *process-id* checked default-route policy,result: deny]{lang="EN-US"}]{#struct_0_78893_x1682_x186629387}

[[默认路由过策略不通过]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1879978479}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_1985093701}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging ospf policy]{lang="EN-US"}]{#struct_0_78893_x1682_x287243561}**[ ]{lang="EN-US"}**[event]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1652934074}[[字段]{style="font-family:黑体;
   color:#0096d6"}]{#struct_0_78893_x1682_1907412903}

[[含义]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_x642434512}

[[OSPF received acl *number* change event]{lang="EN-US"}]{#struct_0_78893_x1682_x2019737886}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1880961519}[收到]{style="font-family:宋体"}[ACL]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[number]{lang="EN-US"}*]{#struct_0_78893_x1682_2055934677}[：]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[号]{style="font-family:宋体"}

[[OSPF received ip prefix-list *name* change event]{lang="EN-US"}]{#struct_0_78893_x1682_328680660}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_681072318}[收到]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀列表变化事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_78893_x1682_x300250944}[：]{lang="EN-US" style="font-family:宋体"}[前缀列表名]{style="font-family:宋体"}

[[OSPF received route policy *name* change event]{lang="EN-US"}]{#struct_0_78893_x1682_x86118212}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1880895983}[收到路由策略变化事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_78893_x1682_1375291670}[：路由策略名]{style="font-family:宋体"}

[[OSPF *process-id* received policy change event (Import count: *importcnt*, calculate count: *calccnt*)]{lang="EN-US"}]{#struct_0_78893_x1682_x724844369}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1307562131}[进程收到过策略变化事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x2057626963}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[importcnt]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880437234}[：]{lang="EN-US" style="font-family:宋体"}[该策略在路由引入中被引用次数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[calccnt]{lang="EN-US"}*]{#struct_0_78893_x1682_1207442226}[：该策略在路由计算中被引用次数]{style="font-family:宋体"}

[[OSPF *process-id* GR end trigger import]{lang="EN-US"}]{#struct_0_78893_x1682_x654755278}

[[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x834557019}[结束触发路由引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_1908769956}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPF *process-id* GR end trigger calculation]{lang="EN-US"}]{#struct_0_78893_x1682_x1880371698}

[[GR]{lang="EN-US"}]{#struct_0_78893_x1682_1102454526}[结束触发路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x897976876}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPF *process-id* GR end trigger calculating priority]{lang="EN-US"}]{#struct_0_78893_x1682_x507179077}

[[GR]{lang="EN-US"}]{#struct_0_78893_x1682_x656537010}[结束触发路由收敛优先级计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1351040469}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging ospf policy]{lang="EN-US"}]{#struct_0_78893_x1682_x1880306162}**[ ]{lang="EN-US"}**[redistribute]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1659604963}[[字段]{style="font-family:黑体;
   color:#0096d6"}]{#struct_0_78893_x1682_x1044707956}

[[含义]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_x1462848156}

[[OSPF *process-id* checked export policy, dest: *dest*, mask: *mask*, protocol ID: *protocol-id*, process ID: *process-id*, result: *result*]{lang="EN-US"}]{#struct_0_78893_x1682_x234859415}

[[引入路由过策略结果]{style="font-family:宋体"}]{#struct_0_78893_x1682_x749857965}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1144730936}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*]{#struct_0_78893_x1682_323985210}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880240626}[：掩码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1505663869}[：]{lang="EN-US" style="font-family:
  宋体"}[引入路由协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1986417132}[：]{lang="EN-US" style="font-family:宋体"}[引入路由的进程号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_481943698}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging ospf policy]{lang="EN-US"}]{#struct_0_78893_x1682_x501098028}**[ ]{lang="EN-US"}**[spf]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1660943242}[[字段]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_77436247}

[[含义]{style="font-family:黑体;color:#0096d6"}]{#struct_0_78893_x1682_x467181343}

[[OSPF *process-id* checked preference policy, dest: *dest*, result: *result*, new preference: *preference*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880175090}

[[路由优先级过策略的结果]{style="font-family:宋体"}]{#struct_0_78893_x1682_1277458984}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_179670963}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*]{#struct_0_78893_x1682_1536835285}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_404737299}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[preference]{lang="EN-US"}*]{#struct_0_78893_x1682_x1508817531}[：路由优先级数值]{style="font-family:宋体"}

[[OSPF *process-id* checked prefix-priority policy, dest: *dest*, result: *result*, priority: *priority*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880109554}

[[前缀优先收敛过策略的结果]{style="font-family:宋体"}]{#struct_0_78893_x1682_2044217830}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_1429532683}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*]{#struct_0_78893_x1682_1846221947}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_x572081993}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[priority]{lang="EN-US"}*]{#struct_0_78893_x1682_2035780856}[：路由收敛优先级名，优先级从高到低取值为]{style="font-family:宋体"}[critical]{lang="EN-US"}[、]{style="font-family:宋体"}[high]{lang="EN-US"}[、]{style="font-family:宋体"}[medium]{lang="EN-US"}[和]{style="font-family:宋体"}[low]{lang="EN-US"}

[[OSPF *process-id* checked fast reroute policy, dest: *dest*, result: *result*, ifindex: *ifindex*, nexthop: *nexthop*, bkifindex: *bkifindex*, bknexthop: *bknexthop*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880044018}

[[FRR]{lang="EN-US"}]{#struct_0_78893_x1682_188304827}[过策略结果]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1483025761}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*]{#struct_0_78893_x1682_x582076652}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_x1726730952}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifindex]{lang="EN-US"}*]{#struct_0_78893_x1682_1626991498}[：出接口索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_78893_x1682_x1879978482}[：]{lang="EN-US" style="font-family:宋体"}[下一跳地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bkifindex]{lang="EN-US"}*]{#struct_0_78893_x1682_1225775422}[：备份出接口索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bknexthop]{lang="EN-US"}*]{#struct_0_78893_x1682_1510790576}[：]{lang="EN-US" style="font-family:宋体"}[备份下一跳地址]{style="font-family:宋体"}

[[OSPF *process-id* checked import policy, dest: *dest*, mask: *mask*, nexthop: *nexthop*, ifindex: *ifindex*, subprotocol: *protocol-id*, metric: *metric*, tag: *tag*, result: *result*]{lang="EN-US"}]{#struct_0_78893_x1682_1815545020}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x2131271087}[向路由管理下发路由过策略的结果]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880961522}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*]{#struct_0_78893_x1682_x316521710}[：]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask]{lang="EN-US"}*]{#struct_0_78893_x1682_1961778660}[：掩码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_78893_x1682_x1061507431}[：]{lang="EN-US" style="font-family:宋体"}[下一跳地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifindex]{lang="EN-US"}*]{#struct_0_78893_x1682_570066754}[：出接口索引]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880895986}[：子协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_615776783}[：花销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tag]{lang="EN-US"}*]{#struct_0_78893_x1682_1170986569}[：标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_78893_x1682_452456324}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1563263788}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_x1773818415}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；配置默认路由策略，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开默认路由过策略的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf policy default-route]{lang="EN-US"}]{#struct_0_78893_x1682_x1880437233}

[\*Nov  5 10:10:01:326 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 registered default-route policy r1, result: success.]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_78893_x1682_x1165210769}*[默认路由策略注册成功]{style="font-family:宋体"}*

[[\*Nov  5 10:10:02:776 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_659772389}

[OSPF 1 received default-route policy message, result: permit, flag: 0x8, cost type: type-1, cost: 0, tag: 333, policy-name: r1.]{lang="EN-US"}

[\*Nov  5 10:10:02:777 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 checked default-route policy, result: permit, flag: 0x8, cost type: type-1, cost: 0, tag: 333.]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_78893_x1682_2043665480}*[默认路由过策略成功]{style="font-family:宋体"}*

[[\# Router A]{lang="PT-BR"}]{#struct_0_78893_x1682_1096669630}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="PT-BR"}[）与]{style="font-family:宋体"}[Router B]{lang="PT-BR"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="PT-BR"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="PT-BR"}[，在]{style="font-family:宋体"}[Router A]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[OSPF]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[，在]{style="font-family:宋体"}[OSPF]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[中创建区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[OSPF]{lang="PT-BR"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[，配置静态路由]{style="font-family:宋体"}[3.3.3.3/32]{lang="PT-BR"}[，引入静态路由；在]{style="font-family:宋体"}[Router B]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[OSPF]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[OSPF]{lang="PT-BR"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[；在]{style="font-family:宋体"}[Router A]{lang="PT-BR"}[上打开路由过策略的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf policy spf]{lang="EN-US"}]{#struct_0_78893_x1682_x2129969419}

[\*Nov  5 10:10:03:777 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 checked import policy, dest: 3.3.3.3, mask: 32, nexthop: 150.1.1.1, ifindex: 0x2, subprotocol: 1, metric: 1, tag: 333, result: permit.]{lang="EN-US"}

[*[// OSPF]{lang="PT-BR"}*]{#struct_0_78893_x1682_x1272740024}*[向路由管理下发路由过策略成功]{style="font-family:宋体"}*

::: {#738394654 .myid}
[]{#_Toc404787737}[]{#struct_0_78893_x1682_x1880371697}[]{#_Toc348020481}[]{#_Toc340741958}[]{#_Toc338927731}

**OSPF \-- OSPF调试命令 \-- debugging ospf redistribute**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1626428829}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **redistribute** { **event** \| **prefix** \[ *ip-address* *mask-length* \] }]{lang="EN-US"}]{#struct_0_78893_x1682_x324681342}

[**[undo]{lang="EN-US"}**[ **debugging** **ospf** \[ *process-id* \] **redistribute** { **event** \| **prefix** }]{lang="EN-US"}]{#struct_0_78893_x1682_x271681991}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1766486483}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_x259228428}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1831900861}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_226235382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_x1880306161}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x641423429}

[*[ip-address]{lang="EN-US"}*]{#struct_0_78893_x1682_51879092}[：路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_78893_x1682_882652909}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**]{#struct_0_78893_x1682_x740006258}[：表示引入前缀调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_78893_x1682_x1323346748}[：表示引入事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_406993526}

[**[debugging ospf redistribute]{lang="EN-US"}**]{#struct_0_78893_x1682_1929544837}[命令用来打开]{style="font-family:
宋体"}[OSPF ]{lang="EN-US"}[路由引入调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf redistribute]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[OSPF ]{lang="EN-US"}[路由引入调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF ]{lang="EN-US"}]{#struct_0_78893_x1682_840196304}[路由引入调试信息开关处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1880240625}[进程的路由引入调试信息。]{style="font-family:宋体"}

[[表1-14 ]{lang="EN-US"}[debugging ospf redistribute event]{lang="EN-US"}]{#struct_0_78893_x1682_x1102379342}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1657258836}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x2113541106}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_590917616}

[[OSPF *process-id* triggered redistributed type *type*]{lang="EN-US"}]{#struct_0_78893_x1682_746454007}

[[触发路由引入，其中：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1136838230}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880175089}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_67670939}[：引入类型，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示从]{style="font-family:宋体"}[RIB]{lang="EN-US"}[表引入，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示从自身的引入表引入]{style="font-family:宋体"}

[[OSPF received rib smooth start message]{lang="EN-US"}]{#struct_0_78893_x1682_x1438998277}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x686361207}[收到平滑开始消息]{style="font-family:宋体"}

[[OSPF received rib smooth end message]{lang="EN-US"}]{#struct_0_78893_x1682_1213184323}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1254938480}[收到平滑结束消息]{style="font-family:宋体"}

[[OSPF received rib batch start message, instance: *instance-id* , user data: *data*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880109553}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1491234579}[实例收到批量上报开始消息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1121342975}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_x127988329}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[OSPF received rib batch end message, instance: *instance-id* , user data: *data*]{lang="EN-US"}]{#struct_0_78893_x1682_x1831688557}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_937721612}[实例收到批量上报开始消息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880044017}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_591589354}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[OSPF received ECA *attr-id* change event:*event*]{lang="EN-US"}]{#struct_0_78893_x1682_1211340004}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1390871880}[实例收到处理扩展团体属性变化消息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1300045038}[：扩展团体属性]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event]{lang="EN-US"}*]{#struct_0_78893_x1682_x1879978481}[：事件，取值为]{lang="EN-US" style="font-family:宋体"}[add]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[delete]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging ospf redistribute prefix]{lang="EN-US"}]{#struct_0_78893_x1682_1629059949}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_x1657809694}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1083552426}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x2113939949}

[[OSPF *process-id* process redistributed entry, ifindex: *ifindex*, nexthop: *nexthop,* tag: *tag*, flag: *flag,* process ID: *process-id2,* attribute ID: *attr-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1956177378}

[[处理引入前缀的路由信息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_2080830648}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880961521}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ifindex]{lang="EN-US"}*]{#struct_0_78893_x1682_x1882605651}[：出接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_78893_x1682_x1045190664}[：下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[tag]{lang="EN-US"}*]{#struct_0_78893_x1682_x639550819}[：标签]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x526065038}[：路由标志，取值为：]{style="font-family:宋体"}[0x00000001]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000002]{lang="EN-US"}[、]{style="font-family:宋体"}[ 0x00000004]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000008]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000010]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000040]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000080]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000100]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000200]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00000400]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00010000]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00040000]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00080000]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00100000]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00200000]{lang="EN-US"}[、]{style="font-family:宋体"}[0x00400000]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880895985}*[2]{lang="EN-US"}*[：引入路由的进程号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-id]{lang="EN-US"}*]{#struct_0_78893_x1682_212492256}[：扩展团体属性]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPF *process-id* process route:]{lang="EN-US"}]{#struct_0_78893_x1682_x529658042}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest]{lang="EN-US"}*[/*mask-len*, redistributed type: *type,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count,* option: *option*, old option: *option*]{lang="EN-US"}

[[查找该前缀原来是否被引入：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1221043829}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x2127326797}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*[/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_2131960511}[：目的地址和掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880437236}[：引入类型，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示从自身引入表引入，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示从]{style="font-family:宋体"}[RIB]{lang="EN-US"}[引入]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_x1924725656}[：开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_2121804976}[：协议号，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示直连路由，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示静态路由，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示]{style="font-family:宋体"}[rip]{lang="EN-US"}[，]{style="font-family:宋体"}[4]{lang="EN-US"}[表示]{style="font-family:宋体"}[ospf]{lang="EN-US"}[，]{style="font-family:宋体"}[5]{lang="EN-US"}[表示]{style="font-family:宋体"}[isis]{lang="EN-US"}[，]{style="font-family:宋体"}[6]{lang="EN-US"}[表示]{style="font-family:宋体"}[bgp]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subprotocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_2142917618}[：子协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880371700}[：下一跳个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_78893_x1682_746813989}[：引入前缀属性，]{lang="EN-US" style="font-family:宋体"}[0x01]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[类]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[源自]{lang="EN-US" style="font-family:宋体"}[MBGP]{lang="EN-US"}[还原]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[0x02]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合，]{lang="EN-US" style="font-family:宋体"}[0x04]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[5/7]{lang="EN-US"}[类]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[源自引入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[0x08]{lang="EN-US"}[表示]{lang="EN-US" style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合]{lang="EN-US" style="font-family:宋体"}[(VPN)]{lang="EN-US"}

[[OSPF received prefix refresh message:]{lang="EN-US"}]{#struct_0_78893_x1682_x674756109}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest]{lang="EN-US"}*[/*mask-len*, instance: *instance-id*, user data: *data,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*]{lang="EN-US"}

[[收到前缀路由刷新消息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1557118531}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*[/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x1467561526}[：目的地址和掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880306164}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_x238138902}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_1666549480}[：开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_2128683763}[：协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subprotocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880240628}[：子协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_78893_x1682_x342864455}[：下一跳个数]{style="font-family:宋体"}

[[OSPF received prefix delete message:]{lang="EN-US"}]{#struct_0_78893_x1682_14499681}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest]{lang="EN-US"}*[/*mask-len*, instance: *instance-id*, user data: *data*, table ID: *table-id*, old protocol ID: *protocol-id*]{lang="EN-US"}

[[收到前缀路由删除消息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1318070038}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*[/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x1880175092}[：目的地址和掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1854708898}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_2018372870}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[table-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1783492920}[：路由所属路由表]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880109556}[：]{style="font-family:宋体"}[上次上报的协议类型]{lang="EN-US" style="font-family:宋体"}

[[OSPF received rib refresh message:]{lang="EN-US"}]{#struct_0_78893_x1682_x1087950052}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest]{lang="EN-US"}*[/*mask-len*, instance: *instance-id*, user data: *data,* metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*]{lang="EN-US"}

[[收到激活路由刷新消息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x420936665}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*[/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_865343617}[：目的地址和掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880044020}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_x168122141}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_x989918733}[：开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1404739702}[：协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subprotocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1879978484}[：子协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_78893_x1682_x1906392460}[：下一跳个数]{style="font-family:宋体"}

[[OSPF received rib delete message:]{lang="EN-US"}]{#struct_0_78893_x1682_1051309961}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest]{lang="EN-US"}*[/*mask-len*, instance: *instance-id*, user data: *data*, table ID: *table-id*, old protocol ID: *protocol-id*]{lang="EN-US"}

[[收到激活路由删除消息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1880961524}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest]{lang="EN-US"}*[/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x1479321124}[：目的地址和掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_181859190}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[data]{lang="EN-US"}*]{#struct_0_78893_x1682_x477851673}[：协议注册时携带的私有数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[table-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880895988}[：路由所属路由表]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_165438089}[：]{style="font-family:宋体"}[上次上报的协议类型]{lang="EN-US" style="font-family:宋体"}

[[OSPF *process-id* added prefix: *dest*/*mask-len*, metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*]{lang="EN-US"}]{#struct_0_78893_x1682_x1248582358}

[[将前缀添加到引入路由表，其中：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1880437235}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x358641715}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[d]{lang="EN-US"}[est]{lang="EN-US"}*]{#struct_0_78893_x1682_x286032337}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880371699}[：掩码长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_x463629415}[：开销]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1788415672}[：协议号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subprotocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1257109151}[：子协议号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880306163}[：下一跳个数]{lang="EN-US" style="font-family:宋体"}

[[OSPF *process-id* deleted prefix: *dest*/*mask-len*, metric: *metric*, protocol ID: *protocol-id*, subprotocol ID: *subprotocol-id*, nexthop count: *count*]{lang="EN-US"}]{#struct_0_78893_x1682_521375985}

[[将前缀从引入路由表删除，其中：]{style="font-family:宋体"}]{#struct_0_78893_x1682_2050893058}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880240627}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[d]{lang="EN-US"}[est]{lang="EN-US"}*]{#struct_0_78893_x1682_60420072}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880175091}[：掩码长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_78893_x1682_x288624957}[：开销]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_875501467}[：协议号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[subprotocol-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880109555}[：子协议号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_78893_x1682_x684665525}[：下一跳个数]{lang="EN-US" style="font-family:宋体"}

[[OSPF aged default route, instance: *instance-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1697156144}

[[老化默认路由：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1880044019}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[instance-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1754388768}[：路由所在]{lang="EN-US" style="font-family:
  宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}

[[OSPF *process-id* aged redistributed route *dest-addr*/*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x1109538291}

[[老化引入路由：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1879978483}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1503107933}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_475746215}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1880961523}[：掩码]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1249562231}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_147741180}[通过]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开引入事件调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf redistribute event]{lang="EN-US"}]{#struct_0_78893_x1682_x1880895987}

[\*Nov  1 08:58:54:157 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 triggered redistributed type 2.]{lang="EN-US"}

[\*Nov  1 08:58:54:158 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 triggered redistributed type 2.]{lang="EN-US"}

[\*Nov  1 08:58:54:158 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 triggered redistributed type 2.]{lang="EN-US"}

[\*Nov  1 08:58:55:280 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 triggered redistributed type 2.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x950307158}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[通过查找自身的引入表进行路由引入]{style="font-family:宋体"}*

[[\*Nov  1 08:58:57:109 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_896385520}

[OSPF received rib smooth start message.]{lang="EN-US"}

[\*Nov  1 08:58:57:112 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received rib smooth end message.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_314553700}*[进程收到平滑消息]{style="font-family:宋体"}*

[[\*Nov  1 08:58:57:124 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x760810318}

[OSPF received rib batch start message, instance: 0, user data: 0x0.]{lang="EN-US"}

[\*Nov  1 08:58:57:126 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received rib batch end message, instance: 0, user data: 0x0.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x79945272}*[实例收到批量上报消息]{style="font-family:宋体"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_962411760}[通过]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的进程]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置引入静态路由，打开引入前缀调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf redistribute prefix]{lang="EN-US"}]{#struct_0_78893_x1682_x314353291}

[\<RouterA\> system-view]{lang="EN-US"}

[\[RouterA\] ip route-static 2.1.1.1 24 null0]{lang="EN-US"}

[\[RouterA\]\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received rib refresh message:2.1.1.0/24, instance: 0, user data: 0x0,]{lang="EN-US"}

[metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.]{lang="EN-US"}

[\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 process redistributed entry, ifindex: 0x14c1, nexthop: 0x0,]{lang="EN-US"}

[tag: 0, flag: 0x10000, process ID: 0, attribute ID: 0xffffffff.]{lang="EN-US"}

[\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 process route:2.1.1.0/24, redistribute type:2]{lang="EN-US"}

[metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count:1,]{lang="EN-US"}

[option: 0x04, old option: 0x00.]{lang="EN-US"}

[\*Nov  5 08:18:32:128 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 added prefix: 2.1.1.0/24, metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_964719732}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[引入激活路由]{style="font-family:宋体"}*

[[\[RouterA\] undo ip route-static 2.1.1.1 24]{lang="EN-US"}]{#struct_0_78893_x1682_845224633}

[\[RouterA\]\*Nov  5 08:19:13:752 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received rib delete message: 2.1.1.0/24, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 2.]{lang="EN-US"}

[\*Nov  5 08:19:13:752 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF 1 deleted prefix: 2.1.1.0/24, metric:0, protocol ID: 2, sub protocol ID: 1, nexthop count: 1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x585727171}*[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[删除激活路由]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\[RouterA\] ip route-static 0.0.0.0 0 null0]{lang="EN-US"}]{#struct_0_78893_x1682_x314287755}

[\[RouterA\]\*Nov  5 08:19:31:558 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received prefix refresh message: 0.0.0.0/0, instance: 0, user data: 0x0,]{lang="EN-US"}

[metric: 0, protocol ID: 2, subprotocol ID: 1, nexthop count: 1.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_2079475345}*[进程引入默认路由]{style="font-family:宋体"}*

[[\[RouterA\] undo ip route-static 0.0.0.0 0]{lang="EN-US"}]{#struct_0_78893_x1682_x277838121}

[\[RouterA\]\*Nov  5 08:19:56:656 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF received prefix delete message: 0.0.0.0/0, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 0.]{lang="EN-US"}

[\*Nov  5 08:19:56:656 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[OSPF receive rib delete message: 0.0.0.0/0, instance: 0, user data: 0x0, table ID: 2, old protocol ID: 2.]{lang="EN-US"}

[*[// OSPF]{lang="EN-US"}*]{#struct_0_78893_x1682_x1336386003}*[进程删除默认路由]{style="font-family:宋体"}*

::: {#-821910390 .myid}
[]{#_Toc404787738}[]{#struct_0_78893_x1682_1794903535}

**OSPF \-- OSPF调试命令 \-- debugging ospf spf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1873217099}

[**[debugging ospf]{lang="EN-US"}**[ \[ *process-id* \] **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **topology** \| **tree** }]{lang="EN-US"}]{#struct_0_78893_x1682_x314222219}

[**[undo debugging ospf]{lang="EN-US"}**[ \[ *process-id* \] **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **topology** \| **tree** }]{lang="EN-US"}]{#struct_0_78893_x1682_x607328060}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_974231026}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1103273470}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1748052596}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_1513576158}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_145288626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1344628845}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x2104694680}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_78893_x1682_x314156683}[：表示所有]{style="font-family:宋体"}[SPF]{lang="EN-US"}[调度与计算的调试信息开关。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_78893_x1682_x1806189752}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_78893_x1682_1211942620}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[的]{style="font-family:宋体"}[job]{lang="EN-US"}[调度调试信息开关。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_78893_x1682_x154002746}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算]{style="font-family:宋体"}[External AS]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_78893_x1682_2077952107}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算]{style="font-family:宋体"}[Internal AS]{lang="EN-US"}[路由的调试信息开关。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**]{#struct_0_78893_x1682_312807539}[：表示]{style="font-family:宋体"}[SPF node]{lang="EN-US"}[和]{style="font-family:宋体"}[link]{lang="EN-US"}[变化的调试信息开关。]{style="font-family:宋体"}

[**[tree]{lang="EN-US"}**]{#struct_0_78893_x1682_x1581134444}**[：]{style="font-family:宋体"}**[表示生成树计算调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1274019722}

[**[debugging ospf spf]{lang="EN-US"}**]{#struct_0_78893_x1682_1103116762}[命令用来打开]{style="font-family:宋体"}[OSPF SPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf spf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPF SPF]{lang="EN-US"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x314091147}[调试信息开关处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_529292570}[进程的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[调试信息。]{style="font-family:宋体"}

[[表1-16 ]{lang="EN-US"}[debugging ospf spf brief]{lang="EN-US"}]{#struct_0_78893_x1682_697017459}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1628029294}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x201528940}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_883332639}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1861532202}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x370586676}[进程号]{style="font-family:宋体"}

[[Schedule event: *schedule-event* at *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x314025611}

[[引起]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_916336521}[调度的事件：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[schedule-event]{lang="EN-US"}*]{#struct_0_78893_x1682_x180700929}[：产生调度的事件类型，取值为]{lang="EN-US" style="font-family:
  宋体"}[0x80000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x40000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ 0x10000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[ 0x00008000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00004000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000010]{lang="EN-US"}

[[Schedule flag: *schedule-flag*, SPF is scheduled]{lang="EN-US"}]{#struct_0_78893_x1682_x1687141105}

[[显示]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x728521794}[调度标志位：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[schedule-flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x442862118}[：调度标志，取值为]{lang="EN-US" style="font-family:
  宋体"}[0x80000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x40000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x20000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x10000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x08000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00008000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00004000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00002000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00001000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000080]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000010]{lang="EN-US"}

[[Schedule flag: *schedule-flag*, SPF is stopped]{lang="EN-US"}]{#struct_0_78893_x1682_x313960075}

[[显示停止]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_1462424317}[调度的标志位：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[schedule-flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x663018061}[：调度标志，取值为]{lang="EN-US" style="font-family:
  宋体"}[0x80000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x40000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x20000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x10000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x08000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00008000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00004000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00002000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00001000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000080]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000010]{lang="EN-US"}

[[Pre Proc: Schedule: *schedule-flag*]{lang="EN-US"}]{#struct_0_78893_x1682_x1127056507}

[[当前]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x894423802}[调度标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[schedule--flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x313894539}[：调度标志，取值为]{lang="EN-US" style="font-family:
  宋体"}[0x80000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x40000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x20000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x10000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x08000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00008000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00004000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00002000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00001000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000080]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000010]{lang="EN-US"}

[[Pre Proc: Running: *running-flag*]{lang="EN-US"}]{#struct_0_78893_x1682_x2107726450}

[[当前]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_846763863}[计算标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[running-flag]{lang="EN-US"}*]{#struct_0_78893_x1682_x1599092674}[：运行标志，取值为]{lang="EN-US" style="font-family:
  宋体"}[0x80000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x40000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x20000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x10000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x08000000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00008000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00004000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00002000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00001000]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000080]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000040]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000020]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000008]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[0x00000004]{lang="EN-US"}[，或者其中某些值的组合]{lang="EN-US" style="font-family:宋体"}

[[SPF building SPT begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x153984350}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x314877579}[最短路径树计算开始]{style="font-family:宋体"}

[[Build SPT for area *area-id* at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x1818802247}

[[计算区域号为]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1790328848}[区域的最短路径树]{style="font-family:宋体"}

[[SPF building SPT ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x792052350}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_192822279}[最短路径树计算结束]{style="font-family:宋体"}

[[Router route calculation begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x314812043}

[[Router]{lang="EN-US"}]{#struct_0_78893_x1682_x227808793}[类型路由计算开始]{style="font-family:宋体"}

[[Router route calculation ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_1782425275}

[[Router]{lang="EN-US"}]{#struct_0_78893_x1682_x1518551565}[类型路由计算结束]{style="font-family:宋体"}

[[Type-7 to Type-5 LSA translator begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x314353290}

[[七转五角色计算开始]{style="font-family:宋体"}]{#struct_0_78893_x1682_964785268}

[[Type-7 to Type-5 LSA translator ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_2041870631}

[[七转五角色计算结束]{style="font-family:宋体"}]{#struct_0_78893_x1682_x723372464}

[[Internal route calculation begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_1495984710}

[[开始计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x314287754}[内部路由]{style="font-family:宋体"}

[[SPF starts(full internal routes)]{lang="EN-US"}]{#struct_0_78893_x1682_2079409809}

[[开始全部计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_540610455}[内部路由]{style="font-family:宋体"}

[[SPF ends(full internal routes)]{lang="EN-US"}]{#struct_0_78893_x1682_1103226160}

[[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x314222218}[内部路由全部计算结束]{style="font-family:宋体"}

[[SPF starts(incremental internal routes)]{lang="EN-US"}]{#struct_0_78893_x1682_x607393596}

[[开始增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x941196164}[内部路由]{style="font-family:宋体"}

[[SPF ends(incremental internal routes)]{lang="EN-US"}]{#struct_0_78893_x1682_x314156682}

[[增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x1806124216}[内部路由结束]{style="font-family:宋体"}

[[Internal route calculation ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x36964677}

[[AS]{lang="EN-US"}]{#struct_0_78893_x1682_1213390121}[内部路由计算结束]{style="font-family:宋体"}

[[Forwarding address calculation begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x314091146}

[[开始计算转发地址]{style="font-family:宋体"}]{#struct_0_78893_x1682_529358106}

[[Forwarding address calculation ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_1472451445}

[[计算转发地址结束]{style="font-family:宋体"}]{#struct_0_78893_x1682_701677540}

[[External route calculation begins at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x314025610}

[[开始计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_916270985}[外部路由]{style="font-family:宋体"}

[[SPF starts(full external routes)]{lang="EN-US"}]{#struct_0_78893_x1682_x313960074}

[[开始全部计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_1462358781}[外部路由]{style="font-family:宋体"}

[[SPF ends(full external routes)]{lang="EN-US"}]{#struct_0_78893_x1682_196652815}

[[AS]{lang="EN-US"}]{#struct_0_78893_x1682_1686482510}[外部路由全部计算结束]{style="font-family:宋体"}

[[SPF starts(incremental external routes)]{lang="EN-US"}]{#struct_0_78893_x1682_x313894538}

[[开始增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x2107660914}[外部路由]{style="font-family:宋体"}

[[SPF ends(incremental external routes)]{lang="EN-US"}]{#struct_0_78893_x1682_1806010812}

[[增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x314877578}[外部路由结束]{style="font-family:宋体"}

[[External route calculation ends at x ms]{lang="EN-US"}]{#struct_0_78893_x1682_x1818736711}

[[AS]{lang="EN-US"}]{#struct_0_78893_x1682_x1631558756}[外部路由计算结束]{style="font-family:宋体"}

[[LFA nbr collect  begins]{lang="EN-US"}]{#struct_0_78893_x1682_x314812042}

[[FRR ]{lang="EN-US"}]{#struct_0_78893_x1682_x227743257}[邻居信息收集开始]{style="font-family:宋体"}

[[LFA nbr collect end]{lang="EN-US"}]{#struct_0_78893_x1682_x177643703}

[[FRR]{lang="EN-US"}]{#struct_0_78893_x1682_x314353293}[邻居信息收集结束]{style="font-family:宋体"}

[[LFA nbr SPF calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_964588660}

[[FRR]{lang="EN-US"}]{#struct_0_78893_x1682_1714398915}[邻居]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算开始]{style="font-family:宋体"}

[[LFA nbr SPF calculation end]{lang="EN-US"}]{#struct_0_78893_x1682_x314287757}

[[FRR]{lang="EN-US"}]{#struct_0_78893_x1682_2079606417}[邻居]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算结束]{style="font-family:宋体"}

[[LFA nbr IntraRt cost calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_525788267}

[[FRR ]{lang="EN-US"}]{#struct_0_78893_x1682_x314222221}[邻居]{style="font-family:宋体"}[intra]{lang="EN-US"}[路由]{style="font-family:宋体"}[cost]{lang="EN-US"}[计算开始]{style="font-family:宋体"}

[[LFA nbr IntraRt cost calculation end]{lang="EN-US"}]{#struct_0_78893_x1682_x607852349}

[[FRR ]{lang="EN-US"}]{#struct_0_78893_x1682_x314156685}[邻居]{style="font-family:宋体"}[intra]{lang="EN-US"}[路由]{style="font-family:宋体"}[cost]{lang="EN-US"}[计算结束]{style="font-family:宋体"}

[[LFA nbr ASBR cost calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x1805796536}

[[FRR ]{lang="EN-US"}]{#struct_0_78893_x1682_2021065442}[邻居]{style="font-family:宋体"}[ASBR cost]{lang="EN-US"}[计算开始]{style="font-family:宋体"}

[[LFA nbr ASBR cost calculation end]{lang="EN-US"}]{#struct_0_78893_x1682_x314091149}

[[FRR ]{lang="EN-US"}]{#struct_0_78893_x1682_529161498}[邻居]{style="font-family:宋体"}[ASBR cost]{lang="EN-US"}[计算结束]{style="font-family:宋体"}

[[LFA SPF BkNextHop calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x1884349741}

[[FRR SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x314025613}[备份下一跳计算开始]{style="font-family:宋体"}

[[LFA SPF BkNextHop calculation end]{lang="EN-US"}]{#struct_0_78893_x1682_916205449}

[[FRR SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x313960077}[备份下一跳计算结束]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[debugging ospf spf asbr]{lang="EN-US"}]{#struct_0_78893_x1682_1462293245}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1639428958}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1450069533}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1155965536}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1510860615}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x870972387}[进程号]{style="font-family:宋体"}

[[Full ASBR routes calculation begins at bucket x]{lang="EN-US"}]{#struct_0_78893_x1682_x773723102}

[[全部]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_78893_x1682_x313894541}[路由计算开始]{style="font-family:宋体"}

[[Full ASBR stops at bucket x]{lang="EN-US"}]{#struct_0_78893_x1682_x2107202167}

[[全部]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_78893_x1682_x720150453}[路由计算本次结束]{style="font-family:宋体"}

[[SPF calculating route to ASBR, Destination ID *dest-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_2051408079}

[[计算到达]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1333509611}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x814791498}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[Incremental ASBR routes calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x314877581}

[[开始增量计算]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_78893_x1682_x1818277948}[路由]{style="font-family:宋体"}

[[Incremental ASBR routes calculation ends]{lang="FR"}]{#struct_0_78893_x1682_x1550114705}

[[增量]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_78893_x1682_485072410}[路由计算结束]{style="font-family:宋体"}

[[Begin Calc Asbr LFA Dest:*Router-id* PriNexthop:*ipaddr* ]{lang="FR"}]{#struct_0_78893_x1682_701185543}

[[开始计算]{style="font-family:宋体"}[Asbr]{lang="EN-US"}]{#struct_0_78893_x1682_x314812045}[备份下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Router-id]{lang="FR"}*]{#struct_0_78893_x1682_x227939865}[：]{lang="EN-US" style="font-family:宋体"}[Asbr]{lang="EN-US"}[的]{style="font-family:宋体"}[Routerid]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Ipaddr]{lang="FR"}*]{#struct_0_78893_x1682_938416938}[：主下一跳]{style="font-family:宋体"}[ip]{lang="FR"}[地址]{style="font-family:宋体"}

[[Succeed Calc Asbr LFA Dest: *Router-id*, PriNexthop: *ipaddr*, LFANexthopAddr: *Bkipaddr*]{lang="FR"}]{#struct_0_78893_x1682_x2067962586}

[[成功计算出]{style="font-family:宋体"}[Asbr]{lang="EN-US"}]{#struct_0_78893_x1682_1779883750}[备份下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Bkipaddr]{lang="FR"}*]{#struct_0_78893_x1682_x314353292}[：]{lang="EN-US" style="font-family:宋体"}[备份下一跳]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[debugging ospf spf internal]{lang="EN-US"}]{#struct_0_78893_x1682_964654196}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1637397065}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1486236173}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_563034326}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1894942514}

[[OSPF ]{lang="EN-US"}]{#struct_0_78893_x1682_1432976438}[进程号]{style="font-family:宋体"}

[[Full internal routes calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x314287756}

[[全部]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_2079540881}[内部路由计算开始]{style="font-family:宋体"}

[[Full internal routes calculation ends]{lang="EN-US"}]{#struct_0_78893_x1682_x677369695}

[[全部]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_78893_x1682_1146677441}[内部路由计算本次结束]{style="font-family:宋体"}

[[SPF calculating route to internal route *dest-addr* /*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x522126199}

[[计算到达]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[/*msk-lenr*]{lang="EN-US"}]{#struct_0_78893_x1682_x314222220}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x607917885}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_1737510815}[：掩码]{lang="EN-US" style="font-family:宋体"}

[[Advertising source *dest-id*, *src-type*, cost x]{lang="EN-US"}]{#struct_0_78893_x1682_x1346235274}

[[路由发布源信息，包括发布者，发布源类型，]{style="font-family:宋体"}[cost]{lang="EN-US"}]{#struct_0_78893_x1682_x458967221}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x990592337}[：路由发布者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[src-type]{lang="EN-US"}*]{#struct_0_78893_x1682_x314156684}[：发布源类型，取值]{lang="EN-US" style="font-family:宋体"}[stub]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[network]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[inter]{lang="EN-US"}

[[Old route has no valid nexthop]{lang="EN-US"}]{#struct_0_78893_x1682_x1805731000}

[[计算之前，没有到达此路由的有效路径]{style="font-family:宋体"}]{#struct_0_78893_x1682_x569512351}

[[Old route for *dest-addr*/*mask-len*, cost x]{lang="EN-US"}]{#struct_0_78893_x1682_x502199715}

[[计算之前到达]{style="font-family:宋体"}*[dest-addr]{lang="EN-US"}*[ /*mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x48362928}[的]{style="font-family:宋体"}[cost]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x314091148}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_529227034}[：掩码]{lang="EN-US" style="font-family:宋体"}

[[stub route, nexthop *dest-addr*, Entry ID *entry-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1858488295}

[[计算之前路由的下一跳，]{style="font-family:宋体"}[Entry ID]{lang="EN-US"}]{#struct_0_78893_x1682_2082130284}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x314025612}[：下一跳]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="NO-BOK"}*]{#struct_0_78893_x1682_916139913}[：]{lang="EN-US" style="font-family:宋体"}[在路由表中的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="NO-BOK"}

[[Cannot find valid nexthop for current advertising source]{lang="EN-US"}]{#struct_0_78893_x1682_x806796867}

[[不能查找到当前发布源的下一跳]{style="font-family:宋体"}]{#struct_0_78893_x1682_410376889}

[[Add new route. Outgoing interface: x, Nexthop: *dest-addr, %s NbrId ID 0x%*]{lang="EN-US"}]{#struct_0_78893_x1682_x884034533}

[[增加一条新路由，包括出接口，下一跳地址，邻居类型和]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_78893_x1682_x313960076}[号：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1462227709}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Delete old route. Outgoing interface: x, Nexthop: d*est-addr, %s NbrId ID 0x%*]{lang="EN-US"}]{#struct_0_78893_x1682_x1830321077}

[[删除路由，路由出接口，下一跳地址，邻居类型和]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_78893_x1682_1481146620}[号：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x313894540}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Update old route. Outgoing interface: x, Nexthop: *dest-addr, %s NbrId ID 0x%*]{lang="EN-US"}]{#struct_0_78893_x1682_x2107136631}

[[更新路由出接口，下一跳地址，邻居类型和]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_78893_x1682_1112818051}[号：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1166321912}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[No advertising source]{lang="EN-US"}]{#struct_0_78893_x1682_x314877580}

[[无发布源]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1818212412}

[[Incremental internal route calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x2031020608}

[[开始增量计算]{style="font-family:宋体"}]{#struct_0_78893_x1682_673854188}

[[Incremental internal route calculation ends]{lang="EN-US"}]{#struct_0_78893_x1682_x314812044}

[[增量计算结束]{style="font-family:宋体"}]{#struct_0_78893_x1682_x227874329}

[[Begin Calc One IntraRt BNH, Dest: *dest-ip*, PNH: *dest-addr*,]{lang="EN-US"}]{#struct_0_78893_x1682_x141611150}

[[开始计算一条]{style="font-family:宋体"}[intra]{lang="EN-US"}]{#struct_0_78893_x1682_x314353295}[路由备份下一跳：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-ip]{lang="EN-US"}*]{#struct_0_78893_x1682_964981876}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x1718614205}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Succeed Calc One IntraRt BNH, Dest: *dest-ip*, PNH:]{lang="EN-US"}]{#struct_0_78893_x1682_741101676}*[ ]{lang="EN-US" style="font-size:10.5pt"}[dest-addr]{lang="EN-US"}*[. BNP: *dest-addr*,]{lang="EN-US"}

[[成功计算出一条]{style="font-family:宋体"}[intra]{lang="EN-US"}]{#struct_0_78893_x1682_x314287759}[路由备份下一跳：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-ip]{lang="EN-US"}*]{#struct_0_78893_x1682_2079737489}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_2084990822}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[debugging ospf spf external]{lang="EN-US"}]{#struct_0_78893_x1682_995781030}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1641240392}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x653114463}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x314222223}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x607983421}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1391426861}[进程号]{style="font-family:宋体"}

[[Full SPF ASE routes calculation begins]{lang="EN-US"}]{#struct_0_78893_x1682_x921550499}

[[开始完全]{style="font-family:宋体"}[ASE SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x527892158}[计算]{style="font-family:宋体"}

[[Full SPF ASE routes calculation stops]{lang="EN-US"}]{#struct_0_78893_x1682_x933631218}

[[结束完全]{style="font-family:宋体"}[ASE SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x314156687}[计算]{style="font-family:宋体"}

[[SPF calculating external route *dest-addr/mask-len*]{lang="EN-US"}]{#struct_0_78893_x1682_x1805927608}

[[计算到达]{style="font-family:宋体"}*[dest-addr/msk-lenr]{lang="EN-US"}*]{#struct_0_78893_x1682_x1439340464}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1046792712}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_1996905024}[：掩码]{lang="EN-US" style="font-family:宋体"}

[[Advertising source *dest-id*, *src-type* src, Cost: x]{lang="EN-US"}]{#struct_0_78893_x1682_x314091151}

[[路由发布源信息，包括发布者，发布源类型，]{style="font-family:宋体"}[cost]{lang="EN-US"}]{#struct_0_78893_x1682_529685785}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_78893_x1682_868268759}[：路由发布者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[s*rc-type*]{lang="EN-US"}]{#struct_0_78893_x1682_x1296372064}[：发布源类型，取值]{lang="EN-US" style="font-family:
  宋体"}[ASE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}

[[Old route has no valid nexthop]{lang="EN-US"}]{#struct_0_78893_x1682_x314025615}

[[计算之前，没有到达此路由的有效路径]{style="font-family:宋体"}]{#struct_0_78893_x1682_916074377}

[[Old route for *dest-addr/mask-len*, cost x]{lang="EN-US"}]{#struct_0_78893_x1682_x825634997}

[[计算之前到达]{style="font-family:宋体"}*[dest-addr/mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x909168843}[的]{style="font-family:宋体"}[cost]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x487877197}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x313960079}[：掩码]{lang="EN-US" style="font-family:宋体"}

[[Cannot find ASBR route]{lang="EN-US"}]{#struct_0_78893_x1682_1461637885}

[[不能查找到到达]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_78893_x1682_x507477041}[的路由]{style="font-family:宋体"}

[[Begin Calc ExternalASRt Alt DestIpAddr:*dest-addr*, PriNextHopAddr:*ip-addr* ]{lang="EN-US"}]{#struct_0_78893_x1682_149901110}

[[开始计算外部路由备份下一跳]{style="font-family:宋体"}]{#struct_0_78893_x1682_x313894543}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x2107333239}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_804185695}[：主下一跳地址]{style="font-family:宋体"}

[[Succeed Calc ExternalASRt Alt DestIpAddr: *dest-addr* PriNextHopAddr: *ip-addr*, LFANexthopAddr:*bk-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_897819338}

[[成功计算外部路由备份下一跳]{style="font-family:宋体"}]{#struct_0_78893_x1682_x314877583}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x1818146876}[：目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ip-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x148216331}[：主下一跳地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[bk-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x1456974585}[：备份下一跳地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[debugging ospf spf topology]{lang="EN-US"}]{#struct_0_78893_x1682_x567154511}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1610843868}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x314812047}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x228070937}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1965963}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x999477089}[进程号]{style="font-family:宋体"}

[[SPF node added, type: *type* , advertising source: *adv-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_x78013752}

[[增加]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1763139015}[节点：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x314353294}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_965047412}[：发布源]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_x209293366}[：发布源]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[[SPF node updated, type: *type*, advertising source: *adv-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_1087798303}

[[更新]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_499765817}[节点：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x314287758}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_2079671953}[：发布源]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_x1456294862}[：发布源]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[[SPF node deleted, type: *type*, advertising source: *adv-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_x49339679}

[[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1027731709}[节点：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x314222222}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x608048957}[：发布源]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_365991250}[：发布源]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[[SPF link added, type:*type*, link ID: *link-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_1978937937}

[[增加]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_1937603302}[链路：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x314156686}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1805862072}[：]{lang="EN-US" style="font-family:宋体"}[link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_1089291228}[：发布源的]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[[SPF link updated, type:*type*, link ID: *link-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_x1303319475}

[[更新]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x314091150}[链路：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_529751321}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_78893_x1682_482339390}[：]{lang="EN-US" style="font-family:宋体"}[link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_765754511}[：发布源的]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[[SPF link deleted, type:*type*, link ID: *link-id*, LsId: *lsid*]{lang="EN-US"}]{#struct_0_78893_x1682_x314025614}

[[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_916008841}[链路：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_1551420539}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1678124175}[：]{lang="EN-US" style="font-family:宋体"}[link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_78893_x1682_x313960078}[：发布源的]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[s]{lang="EN-US"}[I]{lang="EN-US"}[d]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[debugging ospf spf tree]{lang="EN-US"}]{#struct_0_78893_x1682_1461572349}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1618991753}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1685570469}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x52318390}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x268018011}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x491947129}[进程号]{style="font-family:宋体"}

[[No delete flag on node.]{lang="EN-US"}]{#struct_0_78893_x1682_x313894542}

[[节点上无删除标志]{style="font-family:宋体"}]{#struct_0_78893_x1682_x2107267703}

[[Set direct flag on node.]{lang="EN-US"}]{#struct_0_78893_x1682_x244706025}

[[为节点打上直连标志]{style="font-family:宋体"}]{#struct_0_78893_x1682_89478609}

[[Delete node.]{lang="EN-US"}]{#struct_0_78893_x1682_x725797654}

[[删除节点]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1716876062}

[[Delete non-existent node.]{lang="EN-US"}]{#struct_0_78893_x1682_x314877582}

[[删除不存在的节点]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1818081340}

[[Set RMT flag on node.]{lang="EN-US"}]{#struct_0_78893_x1682_x645341720}

[[为节点打上]{style="font-family:宋体"}[RMT]{lang="EN-US"}]{#struct_0_78893_x1682_1327138213}[标志]{style="font-family:宋体"}

[[Set RMT flag on destination node.]{lang="EN-US"}]{#struct_0_78893_x1682_370333850}

[[为目的节点打上]{style="font-family:宋体"}[RMT]{lang="EN-US"}]{#struct_0_78893_x1682_x314812046}[标志]{style="font-family:宋体"}

[[Set direct flag on destination node.]{lang="EN-US"}]{#struct_0_78893_x1682_x228005401}

[[为目的节点打上直连标志]{style="font-family:宋体"}]{#struct_0_78893_x1682_69444259}

[[Cost is decreased. Destination node is deleted. 2-way check failed.]{lang="EN-US"}]{#struct_0_78893_x1682_244569439}

[[目的节点已删除，]{style="font-family:宋体"}[2-way]{lang="EN-US"}]{#struct_0_78893_x1682_x81238748}[检查失败]{style="font-family:宋体"}

[[Link (new path)]{lang="EN-US"}]{#struct_0_78893_x1682_1607961010}

[[增加新链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x939419812}

[[Link (involved)]{lang="EN-US"}]{#struct_0_78893_x1682_2106135247}

[[本次变化涉及此链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_1187995147}

[[Resume link]{lang="EN-US"}]{#struct_0_78893_x1682_1608026546}

[[恢复被删除的链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1126494941}

[[Delete link]{lang="EN-US"}]{#struct_0_78893_x1682_x393637511}

[[删除链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_861182721}

[[Backward link involved]{lang="EN-US"}]{#struct_0_78893_x1682_1608092082}

[[回指链路变化]{style="font-family:宋体"}]{#struct_0_78893_x1682_x752403797}

[[Create existing link]{lang="EN-US"}]{#struct_0_78893_x1682_x2111793984}

[[创建已存在的链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x735104299}

[[Create new link]{lang="EN-US"}]{#struct_0_78893_x1682_1608157618}

[[创建新链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1116438118}

[[Delete link when deleting node]{lang="EN-US"}]{#struct_0_78893_x1682_199645974}

[[删除节点时删除链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_499662514}

[[Cost is increased. Link has no effect on any node.]{lang="EN-US"}]{#struct_0_78893_x1682_1608223154}

[[新增链路不影响任何节点]{style="font-family:宋体"}]{#struct_0_78893_x1682_41594773}

[[Cost is decreased. Backward link is deleted. 2-way check failed.]{lang="EN-US"}]{#struct_0_78893_x1682_x1908349832}

[[回指链路被删除，]{style="font-family:宋体"}[2-way]{lang="EN-US"}]{#struct_0_78893_x1682_147442104}[检查失败]{style="font-family:宋体"}

[[Cost is decreased The cost of backward link is out of range. 2-way check failed.]{lang="EN-US"}]{#struct_0_78893_x1682_1608288690}

[[回指链路]{style="font-family:宋体"}[cost]{lang="EN-US"}]{#struct_0_78893_x1682_x386610948}[超大，]{style="font-family:宋体"}[2-way]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

[[Add root to candidate list of area *area-id*]{lang="EN-US"}]{#struct_0_78893_x1682_x1031912144}

[[区域最短路径树计算：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1608354226}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1917192586}[：区域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Destination node *dest-id*, Advertising source *adv-id*, Non-stub link count x]{lang="EN-US"}]{#struct_0_78893_x1682_x549597651}

[[当前处理的节点信息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x583415254}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608419762}[：目的节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_407387350}[：发布源]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[*[type]{lang="EN-US"}*[ Link *link-id*, Data *link-data*, Cost x]{lang="EN-US"}]{#struct_0_78893_x1682_2104267575}

[[当前处理的链路信息：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1607436722}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="NO-BOK"}*]{#struct_0_78893_x1682_x1706750819}[：]{lang="EN-US" style="font-family:宋体"}[TransNet]{lang="NO-BOK"}[、]{lang="EN-US" style="font-family:宋体"}[p-2-p]{lang="NO-BOK"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1145174232}[：链路对应的]{lang="EN-US" style="font-family:宋体"}[link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-data]{lang="EN-US"}*]{#struct_0_78893_x1682_1607502258}[：链路对应的]{lang="EN-US" style="font-family:宋体"}[data]{lang="EN-US"}

[[SPF node TENT: neighbor node found]{lang="EN-US"}]{#struct_0_78893_x1682_x930924021}

[[找到目的节点]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1559359350}

[[SPF node TENT: neighbor node not found]{lang="EN-US"}]{#struct_0_78893_x1682_1607961011}

[[没找到目的节点]{style="font-family:宋体"}]{#struct_0_78893_x1682_x939485348}

[[Add vertex: *type* *dest-id*, Cost to root x, Nexthop: *dest-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_248224656}

[[加入候选节点：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1608026547}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x1126560477}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="FR"}*]{#struct_0_78893_x1682_1571678119}[：]{lang="EN-US" style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1608092083}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Get vertex: *type* *dest-id*, Cost to root x, Nexthop: *dest-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_x752338261}

[[加入候选节点：]{style="font-family:宋体"}]{#struct_0_78893_x1682_551458585}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_1608157619}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="FR"}*]{#struct_0_78893_x1682_x1116372582}[：]{lang="EN-US" style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1608223155}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Net-node *dest-id*, Advertising source *adv-id*, Router count x]{lang="EN-US"}]{#struct_0_78893_x1682_41529237}

[[网段节点信息以及包含的目的节点数：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1882409257}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608288691}[：目的节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x386676484}[：发布源]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Attach router *dest-id*]{lang="EN-US"}]{#struct_0_78893_x1682_90320490}

[[网段节点中包含的目的节点：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1608354227}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1917127050}[：目的节点]{lang="EN-US" style="font-family:宋体"}

[[Remove vertex:*type* *dest-id*, Cost to root x, Nexthop: *dest-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_1608419763}

[[从候选链上移除候选节点：]{style="font-family:宋体"}]{#struct_0_78893_x1682_407452886}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_x1445954731}[：取值]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="FR"}*]{#struct_0_78893_x1682_1607436723}[：]{lang="EN-US" style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x1706685283}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[[Candidate list empty, SPF area *area-id* finished.]{lang="EN-US"}]{#struct_0_78893_x1682_x1357450871}

[[区域完成最短路径树计算：]{style="font-family:宋体"}]{#struct_0_78893_x1682_1607502259}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x930989557}[：当前计算的区域]{lang="EN-US" style="font-family:宋体"}

[[Delete SPF link]{lang="NL"}]{#struct_0_78893_x1682_1607961008}

[[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x939944099}[链路]{style="font-family:宋体"}

[[SPF link: Nexthop is changed\...]{lang="EN-US"}]{#struct_0_78893_x1682_1608026544}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1126363869}[链路下一跳变化]{style="font-family:宋体"}

[[SPF link: Cost is increased\...]{lang="EN-US"}]{#struct_0_78893_x1682_1633650481}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_1608092080}[链路的]{style="font-family:宋体"}[cost]{lang="EN-US"}[增大]{style="font-family:宋体"}

[[SPF link: Cost is decreased\...]{lang="EN-US"}]{#struct_0_78893_x1682_x752272725}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_1608157616}[链路的]{style="font-family:宋体"}[cost]{lang="EN-US"}[减小]{style="font-family:宋体"}

[[SPF link: Cost is decreased, and backward link is found.]{lang="EN-US"}]{#struct_0_78893_x1682_x1115782758}

[[找到回指链路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1961803246}

[[SPF link Type: *type*,Link ID: link-id, LS ID: *ls_id* Neighbors:x  *Ingore2way*  whereTree(Back) change-type Incr(Decr) del NHop Involved NewPath]{lang="EN-US"}]{#struct_0_78893_x1682_1608223152}

[[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_41725845}[链路描述信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_1608288688}[：类型取值]{lang="EN-US" style="font-family:宋体"}[transit]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[p-2-p]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[link-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x387135237}[：链路对应的]{lang="EN-US" style="font-family:宋体"}[link ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls_id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608354224}[：发布源]{lang="EN-US" style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Ingore2way]{lang="EN-US"}*]{#struct_0_78893_x1682_x1917061514}[：忽略]{lang="EN-US" style="font-family:宋体"}[2-way]{lang="EN-US"}[检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[where]{lang="EN-US"}*]{#struct_0_78893_x1682_1608419760}[：状态，取值]{lang="EN-US" style="font-family:宋体"}[tree]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[back]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[init]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[change-type]{lang="EN-US"}*]{#struct_0_78893_x1682_407518422}[：链路变化类型，取值]{lang="EN-US" style="font-family:
  宋体"}[del]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[nhop]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[involved newpath]{lang="EN-US"}

[[Rebuilding Nbr *adv-id* Spf Tree for Area area-id]{lang="EN-US"}]{#struct_0_78893_x1682_1607436720}

[[开始邻居]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1706881891}[树计算：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[adv-id]{lang="EN-US"}*]{#struct_0_78893_x1682_1607502256}[：邻居]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x931579381}[：区域号]{lang="EN-US" style="font-family:宋体"}

[[Add Node to Nbr htSpfHashTbl:Node *ls_id*, Mask *mask-len*, Cost to root *x*]{lang="EN-US"}]{#struct_0_78893_x1682_1607961009}

[[将普通]{style="font-family:宋体"}[Rtr]{lang="EN-US"}]{#struct_0_78893_x1682_x940009635}[节点加入到邻居节点哈希表：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[ls_id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608026545}[：发布源]{lang="EN-US" style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1126429405}[：掩码长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[x]{lang="EN-US"}]{#struct_0_78893_x1682_1561082285}[：开销]{lang="EN-US" style="font-family:宋体"}

[[Add PnNode to Nbr PseudoNodeTbl:PnNode *ls_id*, Mask *mask-len*, Cost to root *x*]{lang="EN-US"}]{#struct_0_78893_x1682_1608092081}

[[将网段节点加入到邻居网段哈希表：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x752207189}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls_id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608157617}[：发布源]{lang="EN-US" style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[mask-len]{lang="EN-US"}*]{#struct_0_78893_x1682_x1115717222}[：掩码长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[x]{lang="EN-US"}]{#struct_0_78893_x1682_1608223153}[：开销]{lang="EN-US" style="font-family:宋体"}

[[LFA nbr SPF calculation error *x*]{lang="EN-US"}]{#struct_0_78893_x1682_41660309}

[[FRR]{lang="EN-US"}]{#struct_0_78893_x1682_1608288689}[邻居]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算错误码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[x]{lang="EN-US"}]{#struct_0_78893_x1682_x387200773}[：]{style="font-family:宋体"}[错误码]{lang="EN-US" style="font-family:宋体"}

[[Area:*area-id* Begin Calc SPFNode LFA Lsid: *ls_id* Type:*type* ]{lang="EN-US"}]{#struct_0_78893_x1682_1608354225}

[[开始计算]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1916995978}[节点的备份下一跳：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls_id]{lang="EN-US"}*]{#struct_0_78893_x1682_1608419761}[：发布源]{lang="EN-US" style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_78893_x1682_407583958}[：]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[为]{style="font-family:宋体"}[RtrNode]{lang="EN-US"}[，]{style="font-family:宋体"}[2]{lang="EN-US"}[为]{style="font-family:宋体"}[TransitNode]{lang="EN-US"}

[[Area: *area-id* Succeed Calc SPFNode LFA Lsid: *ls_id* Type:*type* PriNexthop:*Nexthop-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_1607436721}[，]{style="font-family:宋体"}[LFANexthop: *BkNexthop-addr*]{lang="EN-US"}

[[成功计算出]{style="font-family:宋体"}[SPFNode]{lang="EN-US"}]{#struct_0_78893_x1682_1607502257}[备份下一跳：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls_id]{lang="EN-US"}*]{#struct_0_78893_x1682_x931644917}[：发布源]{lang="EN-US" style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Nexthop-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_1607961006}[：下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[BkNexthop-addr]{lang="EN-US"}*]{#struct_0_78893_x1682_x939288739}[：备份下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[CandNexthopN: *Nexthop-addr* S2AltN: *cost* AltN2D:*cost* N2S: *cost* N2D: *cost* N2E: *cost* S2N: *cost* S2D: *cost*]{lang="EN-US"}]{#struct_0_78893_x1682_1608026542}

[[候选节点的]{style="font-family:宋体"}[cost]{lang="EN-US"}]{#struct_0_78893_x1682_x1126232797}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S2AltN]{lang="EN-US"}]{#struct_0_78893_x1682_1608092078}[：源节点到当前最优下一跳的距离]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AltN2D]{lang="EN-US"}]{#struct_0_78893_x1682_x752796998}[：当前最优下一跳到目的节点的距离]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N2S]{lang="EN-US"}]{#struct_0_78893_x1682_1608157614}[：备份下一跳到源节点的距离]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N2D]{lang="EN-US"}]{#struct_0_78893_x1682_x1115651686}[：备份下一跳到目的节点的距离]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S2D]{lang="EN-US"}]{#struct_0_78893_x1682_1608223150}[：源节点到目的节点的距离]{style="font-family:宋体"}

[[CandNexthopN: *Nexthop-addr*  is PriNexthop]{lang="EN-US"}]{#struct_0_78893_x1682_1608288686}

[[候选备下一跳是主下一跳]{style="font-family:宋体"}]{#struct_0_78893_x1682_x386742021}

[[CandNexthopN: *Nexthop-addr*  not Loop Free]{lang="EN-US"}]{#struct_0_78893_x1682_1608354222}

[[候选备下一跳有环路]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1917454730}

[[CandNexthopN: *Nexthop-addr* ExitIndex is PriExitIndex]{lang="EN-US"}]{#struct_0_78893_x1682_1608419758}

[[候选备下一跳出接口与主下一跳出接口相同]{style="font-family:宋体"}]{#struct_0_78893_x1682_1607436718}

[[CurrNexthopN: *Nexthop-addr* Node protect, CandNexthopN: *Nexthop-addr* Not]{lang="EN-US"}]{#struct_0_78893_x1682_x1707406180}

[[当前最优备下一跳为节点保护，但候选备下一跳不为节点保护]{style="font-family:宋体"}]{#struct_0_78893_x1682_1607502254}

[[CurrNexthopN: *Nexthop-addr* Link protect, CandNexthopN: *Nexthop-addr* Not]{lang="EN-US"}]{#struct_0_78893_x1682_x931710453}

[[当前最优备下一跳为链路保护，但候选备下一跳不为链路保护]{style="font-family:宋体"}]{#struct_0_78893_x1682_1607961007}

[[Update SPF Node LFANexthop: *Nexthop-addr* Reason:*reason*]{lang="EN-US"}]{#struct_0_78893_x1682_x939354275}

[[更新备选下一跳，]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_78893_x1682_1608026543}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Node Protect]{lang="EN-US"}]{#struct_0_78893_x1682_1608092079}[：备份下一跳节点保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Link Protect]{lang="EN-US"}]{#struct_0_78893_x1682_x752731462}[：备份下一跳链路保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Downstream alternate]{lang="EN-US"}]{#struct_0_78893_x1682_1608157615}[：备份下一跳下游保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Cost]{lang="EN-US"}]{#struct_0_78893_x1682_x1115586150}[：备份下一跳]{style="font-family:宋体"}[S2N+N2D]{lang="EN-US"}[更小]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Different PriExitIndex]{lang="EN-US"}]{#struct_0_78893_x1682_1608223151}[：备份下一跳]{style="font-family:宋体"} [出接口与主下一跳不同]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nexthop IpAddr]{lang="EN-US"}]{#struct_0_78893_x1682_1608288687}[：备份下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址更小]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NULL CurrNode]{lang="EN-US"}]{#struct_0_78893_x1682_x386807557}[：当前最优备份下一跳为]{lang="EN-US" style="font-family:宋体"}[NULL]{lang="EN-US"}[，]{style="font-family:宋体"}[直接更新]{lang="EN-US" style="font-family:宋体"}

[[Rtr-node *dest-id*, Tunnel found, SPF cost x, TE cost x, Nexthop: *dest-addr*]{lang="EN-US"}]{#struct_0_78893_x1682_x126188373}

[[从候选链上新发现隧道：]{style="font-family:宋体"}]{#struct_0_78893_x1682_x126253909}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[dest-id]{lang="FR"}*]{#struct_0_78893_x1682_x126319445}[：]{lang="EN-US" style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[节点]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[dest-addr]{lang="FR"}*]{#struct_0_78893_x1682_x125926229}[：下一跳地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1608354223}

[[\# Router]{lang="EN-US"}]{#struct_0_78893_x1682_x1917389194}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[192.168.171.2/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[192.168.171.10/24]{lang="EN-US"}[）在]{style="font-family:宋体"}[Area 0]{lang="EN-US"}[相连，接口类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，打开调试开关并重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging ospf spf all]{lang="EN-US"}]{#struct_0_78893_x1682_1608419759}

[\<Sysname\> reset ospf 1 process]{lang="EN-US"}

[Reset OSPF process? \[Y/N\]:y]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF Stop Schedule for process reset]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000000 SPF is stopped, at 803994745 ms]{lang="EN-US"}

[  OSPF 1 SPF link Delete SPF link]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  SPF link Type:2, Link ID:192.168.171.10, LS ID:22.22.22.22 Neighbors:1 Back]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link Delete SPF link]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  SPF link Type:2, Link ID:192.168.171.10, LS ID:192.168.171.2 Neighbors:1 Tree]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link Delete SPF link]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  SPF link Type:3, Link ID:192.168.171.2, LS ID:192.168.171.10 Neighbors:1 Back]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link Delete SPF link]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  SPF link Type:3, Link ID:22.22.22.22, LS ID:192.168.171.10 Neighbors:1 Tree]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_408108245}*[停止]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算，删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}[链路]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_844855606}

[  OSPF 1 SPF node added, Type:1, Advertising source:192.168.171.2, LS ID:192.168.171.2]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Add New Node.]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000001 at 803994819 ms.]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule flag : 0x00000001 SPF is scheduled.]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000080 at 803994821 ms.]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF Initial running flag]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Schedule: 0x00000001.]{lang="EN-US"}

[\*Nov  1 10:10:51:338 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Running : 0x000006CD.]{lang="EN-US"}

[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF building SPT begins at 804000440 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_820093302}*[创建新的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点，]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算开始]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_1607436719}

[  OSPF 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.0, at 804000440 ms. \*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF building SPT ends at 804000440 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_x1707340644}*[重建]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树，]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算结束]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_1607502255}

[  OSPF 1 Router route calculation begins at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation ends at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:339 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation begins at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full ASBR routes calculation begins at bucket 0]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full ASBR stops at bucket 11]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation ends at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Type-7 to Type-5 LSA translator begins at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Type-7 to Type-5 LSA translator ends at 804000440 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Internal route calculation begins at 804000440 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_x931775989}*[各种类型路由计算开始或结束]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:340 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_1212521399}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(full internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full internal routes calculation begins]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF calculating route to internal route 192.168.171.0/24]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Advertising source 192.168.171.2, Stub src, cost:1]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Old route has no valid nexthop]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Add new route. Outgoing interface:5, Nexthop:192.168.171.2, Normal NbrId ID ]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[0x130003f2]{lang="EN-US"}

[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full internal routes calculation ends]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_879398896}*[开始全部计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:341 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1120922345}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(full internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Internal route calculation ends at 804000441 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Forwarding address calculation begins at 804000441 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Forwarding address calculation ends at 804000441 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 External route calculation begins at 804000441 ms]{lang="EN-US"}

[*[// AS]{lang="EN-US"}*]{#struct_0_78893_x1682_341325956}*[内部路由全部计算结束]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_1880829084}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(full external routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full SPF ASE routes calculation begins]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full SPF ASE routes calculation stops]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_577848885}*[开始全部计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1120856809}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(full external routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:342 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 External route calculation ends at 804000443 ms]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000080 at 804000450 ms.]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule flag : 0x00000080 SPF is scheduled.]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF Initial running flag]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Schedule: 0x00000080.]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Running : 0x00000300.]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Internal route calculation begins at 804000667 ms]{lang="EN-US"}

[*[// AS]{lang="EN-US"}*]{#struct_0_78893_x1682_x461386880}*[外部路由全部计算结束]{style="font-family:宋体"}*

[[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1120791273}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF starts(incremental internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Incremental internal route calculation begins]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF calculating route to internal route 120.1.1.0/24]{lang="EN-US"}

[\*Nov  1 10:10:51:343 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Advertising source 192.168.171.2, Stub src, cost:10]{lang="EN-US"}

[\*Nov  1 10:10:51:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Old route has no valid nexthop]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Add new route. Outgoing interface:6, Nexthop:120.1.1.1]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Incremental internal route calculation ends]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_97483140}*[开始增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}*

[[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1120660201}

[  OSPF 1 \*\*\*\*\*\*\*\*\* SPF ends(incremental internal routes)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Internal route calculation ends at 804000798 ms]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Forwarding address calculation begins at 804000798 ms]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Forwarding address calculation ends at 804000798 ms]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF node added, Type:1, Advertising source:22.22.22.22, LS ID:22.22.22.22]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Add New Node.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link added, Type:2, Link ID:192.168.171.10, LS ID:192.168.171.2]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Create new link]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x0000028C at 804002088 ms.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule flag : 0x0000028C SPF is scheduled.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000001 at 804002211 ms.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF node added, Type:2, Advertising source:22.22.22.22, LS ID:192.168.171.10]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Add New Node.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Set direct flag on node.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link added, Type:3, Link ID:192.168.171.2, LS ID:192.168.171.10]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Create new link]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link added, Type:3, Link ID:22.22.22.22, LS ID:192.168.171.10]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Create new link]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Schedule event: 0x00000002 at 804002406 ms.]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF link added, Type:2, Link ID:192.168.171.10, LS ID:22.22.22.22]{lang="EN-US"}

[\*Nov  1 10:10:53:344 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Create new link]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF Initial running flag]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Schedule: 0x00000001.]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Pre Proc : Running : 0x000006CD.]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF building SPT begins at 804007439 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_x1905841443}*[增量计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由结束]{style="font-family:宋体"}*

[[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1120594665}

[  OSPF 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.0, at 804007439 ms. \*\*\*\*]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF building SPT ends at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation begins at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation ends at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation begins at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full ASBR routes calculation begins at bucket 0]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 SPF calculating route to ASBR, Destiantion ID 22.22.22.22]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Full ASBR stops at bucket 11]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Router route calculation ends at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Type-7 to Type-5 LSA translator begins at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Type-7 to Type-5 LSA translator ends at 804007439 ms]{lang="EN-US"}

[\*Nov  1 10:10:57: 345 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPF 1 Internal route calculation begins at 804007439 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_1569504734}*[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[重建]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树，各种类型路由计算开始或结束]{style="font-family:宋体"}*

::: {#-954513376 .myid}
[]{#_Toc404787739}[]{#struct_0_78893_x1682_x97901163}[]{#_Toc300065256}[]{#_Toc148240886}

**OSPF \-- OSPF调试命令 \-- debugging ospf timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x727610111}

[**[debugging]{lang="EN-US"}**[ **ospf** \[ *process-id* \] **timer** \[ **lsa-generate** \| **spf** \]]{lang="EN-US"}]{#struct_0_78893_x1682_2071462298}

[**[undo debugging ospf ]{lang="EN-US"}**[\[ *process-id* \] **timer** \[ **lsa-generate** \| **spf** \]]{lang="EN-US"}]{#struct_0_78893_x1682_x2066738631}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78893_x1682_187481500}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78893_x1682_x1120529129}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x58282042}

[[network-admin]{lang="EN-US"}]{#struct_0_78893_x1682_1017791855}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78893_x1682_1126797358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x265240855}

[*[process-id]{lang="EN-US"}*]{#struct_0_78893_x1682_x1753931619}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsa-generate]{lang="EN-US"}**]{#struct_0_78893_x1682_1741178382}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器调试信息开关。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_78893_x1682_1713694854}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78893_x1682_1979766603}

[**[debugging ospf timer]{lang="EN-US"}**]{#struct_0_78893_x1682_x1120463593}[命令用来打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging ospf  timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1148447732}[定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1944134043}[进程的定时器调试信息。]{style="font-family:宋体"}

[[表1-22 ]{lang="EN-US"}[debugging ospf timer lsa-generate]{lang="EN-US"}]{#struct_0_78893_x1682_293701972}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1865912925}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_786839769}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_1302358571}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1302251748}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1121446633}[进程号]{style="font-family:宋体"}

[[Create LS timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_1207390710}

[[创建]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_1689134094}[生成定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Delete LS timer]{lang="EN-US"}]{#struct_0_78893_x1682_1799178677}

[[删除]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x190794822}[生成定时器]{style="font-family:宋体"}

[[Restart LS timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x1121381097}

[[启动]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_x2078433412}[生成定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Reset LS timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x785376343}

[[重置]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_78893_x1682_1879649754}[生成定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[debugging ospf timer spf]{lang="EN-US"}]{#struct_0_78893_x1682_1074469709}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1863881036}[[字段]{style="font-family:黑体"}]{#struct_0_78893_x1682_70458128}

[[描述]{style="font-family:黑体"}]{#struct_0_78893_x1682_x1120922344}

[[OSPF *process-id*]{lang="EN-US"}]{#struct_0_78893_x1682_1907409897}

[[OSPF]{lang="EN-US"}]{#struct_0_78893_x1682_1647262944}[进程号]{style="font-family:宋体"}

[[Create SPF timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x1909826843}

[[创建]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1264815074}[计算定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Delete SPF timer]{lang="EN-US"}]{#struct_0_78893_x1682_x1880677621}

[[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x1120856808}[计算定时器]{style="font-family:宋体"}

[[Restart SPF timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x2027470821}

[[启动]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_784617994}[计算定时器，超时时间]{style="font-family:宋体"}[x]{lang="EN-US"}[毫秒]{style="font-family:宋体"}

[[Reset SPF timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_78893_x1682_x219528288}

[[重置]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_78893_x1682_x751405218}[计算定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78893_x1682_x36787326}

[[\# Router A]{lang="EN-US"}]{#struct_0_78893_x1682_x1120791272}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.1/24]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[150.1.1.2/24]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[定时器调试信息开关并重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospf timer]{lang="EN-US"}]{#struct_0_78893_x1682_x1468600801}

[\<RouterA\> reset ospf 1 process]{lang="EN-US"}

[Reset OSPF process? \[Y/N\]:y]{lang="EN-US"}

[%Nov  1 10:51:04:589 2012 RouterA OSPF/5/OSPF_NBR_CHG: -MDC=1; OSPF 1 Neighbour 150.1.1.2 (GigabitEthernet1/0/1) from Full to Down]{lang="EN-US"}

[         \*Nov  1 10:51:04:598 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}

[           OSPF 1 Reset SPF timer,timeout value is 5000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_64333249}*[重置]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器，超时时间]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[         \*Nov  1 10:51:04:634 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x781897206}

[           OSPF 1 Delete SPF timer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_2144903998}*[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器]{style="font-family:宋体"}*

[[         \*Nov  1 10:51:06:068 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_1590542696}

[           OSPF 1 Create SPF timer,timeout value is 5000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_x1120725736}*[创建]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器，超时时间]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[         \*Nov  1 10:51:11:553 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x542790373}

[OSPF 1 Create LS timer,timeout value is 5000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_1361908081}*[创建]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器，超时时间]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[         \*Nov  1 10:51:13:082 2012 RouterA OSPF/7/DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_78893_x1682_x1317098027}

[           OSPF 1 Reset LS timer,timeout value is 714 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78893_x1682_86107239}*[重置]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器，超时时间]{style="font-family:宋体"}[714]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
