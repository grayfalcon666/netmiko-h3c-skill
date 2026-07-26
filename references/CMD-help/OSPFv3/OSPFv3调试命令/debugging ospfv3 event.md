::: {#293194319 .myid}
[]{#_Toc404788844}[]{#struct_0_35947_29584_1823658999}[]{#_Toc301773753}[]{#_Toc161563938}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_1500960893}

[**[debugging ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **event** \[ **bfd** \| **error** \| **graceful-restart** \| **interface** \| **neighbor** \]]{lang="EN-US"}]{#struct_0_35947_29584_1738089161}

[**[undo debugging ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **event** \[ **bfd** \| **error** \| **graceful-restart** **interface** \| **neighbor** \]]{lang="EN-US"}]{#struct_0_35947_29584_1222985053}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_852837036}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_2042383819}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_x822427114}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_x458847044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_x603602228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1466496917}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x588808015}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bfd]{lang="EN-US"}**]{#struct_0_35947_29584_x1736466282}[：表示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_35947_29584_x141962148}[：表示错误事件调试信息开关。]{style="font-family:宋体"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_35947_29584_853295788}[：表示]{style="font-family:宋体"}[GR]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_35947_29584_x873999887}[：表示接口事件调试信息开关。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}**]{#struct_0_35947_29584_1162865017}[：表示邻居事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_x578774582}

[**[debugging ospfv3 event]{lang="EN-US"}**]{#struct_0_35947_29584_428791061}[命令用来打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging ospfv3 ]{lang="DA"}[event]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1989582555}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1142847345}[进程的事件调试信息开关。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ospfv3 event bfd]{lang="EN-US"}]{#struct_0_35947_29584_x30143108}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_287992501}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x1689688571}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_853230252}

[[Receive bfd event (*number*)]{lang="NO-BOK"}]{#struct_0_35947_29584_x1312614344}

[[接收到]{style="font-family:宋体"}]{#struct_0_35947_29584_272630168}[BFD]{lang="PT-BR"}[事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:
  10.0pt;font-family:Symbol"}*[number]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1084646562}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="NO-BOK"}[事件类型]{lang="EN-US" style="font-family:宋体"}

[*[Notify bfd smooth stop]{lang="EN-US"}*]{#struct_0_35947_29584_18851768}

[[通知]{style="font-family:宋体"}]{#struct_0_35947_29584_x1720758036}[BFD]{lang="PT-BR"}[平滑停止]{style="font-family:宋体"}

[[Bfd session create for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).]{lang="NO-BOK"}]{#struct_0_35947_29584_2059687291}

[[创建]{style="font-family:宋体"}]{#struct_0_35947_29584_852771497}[BFD]{lang="NO-BOK"}[会话]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_1419082484}[：]{lang="EN-US" style="font-family:宋体"}[指定进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="NO-BOK"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_707140583}[：]{lang="EN-US" style="font-family:宋体"}[指定接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}[x.x.x.x]{lang="NO-BOK"}]{#struct_0_35947_29584_x1240237973}[：]{lang="EN-US" style="font-family:宋体"}[指定邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="NO-BOK"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[address1]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1314097550}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="NO-BOK"}[会话的源地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[address2]{lang="NO-BOK"}*]{#struct_0_35947_29584_1339430020}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="NO-BOK"}[会话的目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[number3]{lang="NO-BOK"}*]{#struct_0_35947_29584_852705961}[：]{lang="EN-US" style="font-family:宋体"}[调用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="NO-BOK"}[接口的返回值]{lang="EN-US" style="font-family:宋体"}

[[Bfd session delete for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).]{lang="NO-BOK"}]{#struct_0_35947_29584_x2089195814}

[[删除]{style="font-family:宋体"}]{#struct_0_35947_29584_x1658176729}[BFD]{lang="NO-BOK"}[会话]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1981858997}[：]{lang="EN-US" style="font-family:宋体"}[指定进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_635488804}[：指定接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_852640425}[：邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[address1]{lang="NO-BOK"}*]{#struct_0_35947_29584_1828878995}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的源地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[address2]{lang="NO-BOK"}*]{#struct_0_35947_29584_993646519}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[number3]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1151800529}[：调用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[接口的返回值]{lang="EN-US" style="font-family:宋体"}

[[Bfd session disable for process (*number1*), (*number2*), nbr (*x.x.x.x*), src (*address1*), dst (*address2*), RetVal: (*number3*).]{lang="NO-BOK"}]{#struct_0_35947_29584_634932096}

[[去使能]{style="font-family:宋体"}]{#struct_0_35947_29584_852574889}[BFD]{lang="NO-BOK"}[会话]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1171066314}[：]{lang="EN-US" style="font-family:宋体"}[指定进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_1823538599}[：指定接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_x495658978}[：邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[address1]{lang="NO-BOK"}*]{#struct_0_35947_29584_128680336}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的源地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[address2]{lang="NO-BOK"}*]{#struct_0_35947_29584_853033641}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的目的地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[number3]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1947515441}[：调用]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[接口的返回值]{lang="EN-US" style="font-family:宋体"}

[[Bfd smooth, ]{lang="NO-BOK"}[collect Gr process (]{lang="EN-US"}]{#struct_0_35947_29584_1031111327}*[number]{lang="NO-BOK"}*[).]{lang="EN-US"}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_867868767}[平滑，收集正在做]{style="font-family:宋体"}[GR]{lang="EN-US"}[的进程]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number]{lang="NO-BOK"}*]{#struct_0_35947_29584_476812653}[：进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Bfd smooth, no Gr process, Notify bfd smooth stop.]{lang="EN-US"}]{#struct_0_35947_29584_852968105}

[[BFD]{lang="PT-BR"}]{#struct_0_35947_29584_x724123172}[平滑，没有处于]{style="font-family:宋体"}[GR]{lang="PT-BR"}[的进程，通知]{style="font-family:宋体"}[BFD]{lang="PT-BR"}[平滑停止]{style="font-family:宋体"}

[[Bfd smooth, process (]{lang="EN-US"}]{#struct_0_35947_29584_1000693410}*[number1]{lang="NO-BOK"}*[) Gr completed or deleted, bfd Gr Process list count: (]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[).]{lang="EN-US"}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_236629772}[平滑，指定进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[过程完成或者删除]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_852902569}[：指定进程的]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_884535198}[：当前处于]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态的进程计数]{style="font-family:宋体"}

[[Bfd connected, process all session.]{lang="EN-US"}]{#struct_0_35947_29584_x437530013}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_1771627125}[连接成功，处理所有的会话]{style="font-family:宋体"}

[[Bfd disconnect, clear all session.]{lang="EN-US"}]{#struct_0_35947_29584_852837033}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_2042383816}[失去连接，清除所有的会话]{style="font-family:宋体"}

[[Bfd session add radix nbr for process (]{lang="EN-US"}]{#struct_0_35947_29584_x822754794}*[number1]{lang="NO-BOK"}*[), (]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[), nbr (]{lang="EN-US"}*[x.x.x.x)]{lang="NO-BOK"}*[, instanceId (]{lang="EN-US"}*[number3]{lang="NO-BOK"}*[), Count: (]{lang="EN-US"}*[number4]{lang="NO-BOK"}*[), src (]{lang="EN-US"}*[address1]{lang="NO-BOK"}*[), dst (]{lang="EN-US"}*[address2]{lang="NO-BOK"}*[).]{lang="EN-US"}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_x435867880}[会话添加新节点到]{style="font-family:宋体"}[Radix]{lang="EN-US"}[树中]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_853295785}[：指定]{lang="EN-US" style="font-family:宋体"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_x873999874}[：指定接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_1162668396}[：邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number3]{lang="NO-BOK"}*]{#struct_0_35947_29584_853230249}[：实例]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number4]{lang="NO-BOK"}*]{#struct_0_35947_29584_643700803}[：当前节点个数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[address1]{lang="NO-BOK"}*]{#struct_0_35947_29584_2131139697}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的源地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:
  10.0pt;font-family:Symbol"}*[address2]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1706542979}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的目的地址]{lang="EN-US" style="font-family:宋体"}

[[Bfd session delete radix nbr for process (]{lang="EN-US"}]{#struct_0_35947_29584_852771498}*[number1]{lang="NO-BOK"}*[), (]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[), nbr (]{lang="EN-US"}*[x.x.x.x]{lang="NO-BOK"}*[), instanceId (]{lang="EN-US"}*[number3]{lang="NO-BOK"}*[), Count: (]{lang="EN-US"}*[number4]{lang="NO-BOK"}*[), src (]{lang="EN-US"}*[address1]{lang="NO-BOK"}*[), dst (]{lang="EN-US"}*[address2]{lang="NO-BOK"}*[).]{lang="EN-US"}

[[BFD]{lang="EN-US"}]{#struct_0_35947_29584_1419082481}[会话删除]{style="font-family:宋体"}[Radix]{lang="EN-US"}[树中指定节点]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_707337191}[：指定]{lang="EN-US" style="font-family:宋体"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_852705962}[：指定接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_x2089195811}[：邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number3]{lang="NO-BOK"}*]{#struct_0_35947_29584_x898661842}[：实例]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number4]{lang="NO-BOK"}*]{#struct_0_35947_29584_852640426}[：当前节点个数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[address1]{lang="NO-BOK"}*]{#struct_0_35947_29584_1828878998}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的源地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[address2]{lang="NO-BOK"}*]{#struct_0_35947_29584_993318839}[：]{lang="EN-US" style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的目的地址]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ospfv3 event error]{lang="EN-US"}]{#struct_0_35947_29584_x530655259}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_318389001}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_852574890}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_785248829}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_1716105078}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_521102043}[进程号]{style="font-family:宋体"}

[[Neighbor *nbr-id*]{lang="EN-US"}]{#struct_0_35947_29584_636285986}

[[邻居的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_35947_29584_x630520048}

[[OSPFv3 *process-id* Gen Dbsummary list fail]{lang="EN-US"}]{#struct_0_35947_29584_52814455}

[[生产]{style="font-family:宋体"}[DD summary]{lang="EN-US"}]{#struct_0_35947_29584_853033642}[列表失败]{style="font-family:宋体"}

[[joining the multicastgroup *goupname*, Failed: *value*, IfNetIndex: *if-index(if-name)*.]{lang="EN-US"}]{#struct_0_35947_29584_x1947515444}

[[加入组播组失败]{style="font-family:宋体"}]{#struct_0_35947_29584_1434395854}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[goupname]{lang="EN-US"}*]{#struct_0_35947_29584_x1581658572}[：组播组名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_35947_29584_892251171}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-index]{lang="EN-US"}*]{#struct_0_35947_29584_116900286}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_35947_29584_852968106}[：接口名称]{lang="EN-US" style="font-family:宋体"}

[[leaving the multicastgroup *goupname*, Failed: *value*, IfNetIndex: *if-index(if-name)*.]{lang="EN-US"}]{#struct_0_35947_29584_x724123173}

[[离开组播组失败]{style="font-family:宋体"}]{#struct_0_35947_29584_1000758946}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[goupname]{lang="EN-US"}*]{#struct_0_35947_29584_609798245}[：组播组名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_35947_29584_x1342811492}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-index]{lang="EN-US"}*]{#struct_0_35947_29584_1144515277}[：接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_35947_29584_852902570}[：接口名称]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ospfv3 event graceful-restart]{lang="EN-US"}]{#struct_0_35947_29584_x1454116969}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_311546707}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_304629225}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1105505833}

[[OSPFv3 \[*number*\]]{lang="EN-US"}]{#struct_0_35947_29584_1652896380}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x751212434}[进程号]{style="font-family:宋体"}

[[create grace LSA send timer, timeout value is *number* (ms)]{lang="EN-US"}]{#struct_0_35947_29584_x1593702225}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_852837034}[创建发送]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number]{lang="EN-US"}*]{#struct_0_35947_29584_2042383821}[：表示定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[delete grace LSA send timer]{lang="EN-US"}]{#struct_0_35947_29584_x822951399}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_1088648801}[端删除发送]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[create GR waiting timer, timeout value is *number* (ms)]{lang="EN-US"}]{#struct_0_35947_29584_279630424}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_1887903216}[创建等待定时器，用来发现]{style="font-family:宋体"}[Helper]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number]{lang="EN-US"}*]{#struct_0_35947_29584_853295786}[：表示定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[delete GR waiting timer]{lang="EN-US"}]{#struct_0_35947_29584_x873999873}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_1163127148}[端删除等待定时器]{style="font-family:宋体"}

[[GR waiting timer expired]{lang="EN-US"}]{#struct_0_35947_29584_842798278}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_842994886}[端等待定时器超时]{style="font-family:宋体"}

[[create GR period timer, timeout value is *number* (ms)]{lang="EN-US"}]{#struct_0_35947_29584_x962952210}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_701631200}[端创建平滑重启时间定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number]{lang="EN-US"}*]{#struct_0_35947_29584_398066184}[：表示定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[delete GR period timer]{lang="EN-US"}]{#struct_0_35947_29584_853230250}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_x1312614342}[端删除平滑重启时间间隔定时器]{style="font-family:宋体"}

[[GR period timer expired]{lang="EN-US"}]{#struct_0_35947_29584_842601670}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_842536134}[端平滑重启时间间隔定时器超时]{style="font-family:宋体"}

[[received newer grace LSA from neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_1435429582}*[x.x.x.x]{lang="NO-BOK"}*

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1854424284}[端从邻居收到新的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1487121879}[：表示邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[received maximum age grace LSA from neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_852771495}*[x.x.x.x]{lang="NO-BOK"}*

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1419082486}[端从邻居收到新的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[并且]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[age=3600]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_707009511}[：表示邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[received maximum age grace LSA, no neighbor  ]{lang="EN-US"}]{#struct_0_35947_29584_1828616529}*[x.x.x.x]{lang="NO-BOK"}*

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_852705959}[端收到新的]{style="font-family:宋体"}[age=3600]{lang="EN-US"}[的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，发现发送该]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的路由器不是自己的邻居]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_249456354}[：]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[received grace LSA, GR helper is not enabled]{lang="EN-US"}]{#struct_0_35947_29584_x1519325566}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_x1507757912}[端收到]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但是未使能]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[not enter helper mode, support planned GR only]{lang="EN-US"}]{#struct_0_35947_29584_842863811}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_842798275}[端不进入]{style="font-family:宋体"}[helper]{lang="EN-US"}[模式，只支持计划性]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[received grace LSA, age ]{lang="EN-US"}]{#struct_0_35947_29584_852640423}*[number1]{lang="NO-BOK"}*[ larger than GR period ]{lang="EN-US"}*[number2]{lang="NO-BOK"}*

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1828879001}[端收到]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但是收到的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[age]{lang="EN-US"}[大于]{style="font-family:宋体"}[GR interval]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_x145208245}[：]{lang="EN-US" style="font-family:宋体"}[LS age]{lang="EN-US"}[字段]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_738571648}[：]{lang="EN-US" style="font-family:宋体"}[GR interval]{lang="EN-US"}[字段]{lang="EN-US" style="font-family:宋体"}

[[not enter helper mode, neighbor is neither full nor 2-way.]{lang="EN-US"}]{#struct_0_35947_29584_852574887}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_x1171066312}[端不进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式，因为邻居不是]{style="font-family:宋体"}[full]{lang="EN-US"}[状态或者]{style="font-family:宋体"}[2-way]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[already enter helper mode, neighbor is neither full nor 2-way.]{lang="EN-US"}]{#struct_0_35947_29584_660739185}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_558660193}[端已经进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式，邻居不是]{style="font-family:宋体"}[full]{lang="EN-US"}[或者]{style="font-family:宋体"}[2-way]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[not enter helper mode, LSA in retransmit-list content is changed]{lang="EN-US"}]{#struct_0_35947_29584_842536131}

[[不进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_35947_29584_842732739}[模式，因为重传链中的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[发生变化]{style="font-family:宋体"}

[[received invalid grace LSA]{lang="EN-US"}]{#struct_0_35947_29584_853033639}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_773473751}[端收到无效的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}

[[received grace LSA, but GR period ]{lang="EN-US"}]{#struct_0_35947_29584_x424239875}*[number]{lang="NO-BOK"}*[ invalid.]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_971512354}[端收到]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但是收到的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[period]{lang="EN-US"}[字段无效]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number]{lang="NO-BOK"}*]{#struct_0_35947_29584_852968103}[：]{lang="EN-US" style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[中指定的]{lang="EN-US" style="font-family:宋体"}[period]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[received grace LSA, but GR reason invalid]{lang="EN-US"}]{#struct_0_35947_29584_842994884}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_842929348}[端收到]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但是收到的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[GR reason]{lang="EN-US"}[字段无效]{style="font-family:宋体"}

[[received grace LSA, but no neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_x724123170}*[x.x.x.x]{lang="NO-BOK"}*

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1000824482}[端收到]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但是邻居列表中没有通告的邻居]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_1011283286}[：]{lang="EN-US" style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[中通告的邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[not enter helper mode, router is restarter.]{lang="EN-US"}]{#struct_0_35947_29584_852902567}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_884535196}[端不进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式，因为正在作为]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[端平滑重启]{style="font-family:宋体"}

[[create GR period timer ]{lang="EN-US"}]{#struct_0_35947_29584_x437530019}*[number1]{lang="NO-BOK"}*[ for neighbor ]{lang="EN-US"}*[x.x.x.x]{lang="NO-BOK"}*[, timeout interval is ]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[ ]{lang="NO-BOK"}[(s)]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_852837031}[端为指定的邻居创建平滑间隔定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_2042383818}[：定时器标编号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_x822361578}[：指定的邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_x68061799}[：定时器间隔]{lang="EN-US" style="font-family:宋体"}

[[delete GR period timer for neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_853295783}*[x.x.x.x]{lang="NO-BOK"}*[.]{lang="EN-US"}

[[删除对指定邻居创建的平滑间隔定时器]{style="font-family:宋体"}]{#struct_0_35947_29584_x873999876}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_1162799468}[：指定邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[restart GR period timer, return value: ]{lang="EN-US"}]{#struct_0_35947_29584_853230247}*[number1]{lang="NO-BOK"}*[ for neighbor ]{lang="EN-US"}*[x.x.x.x]{lang="NO-BOK"}*[, timeout interval is ]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[ ]{lang="NO-BOK"}[(s).]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_643700797}[端为指定邻居重置平滑间隔定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_1368889796}[：重置平滑间隔定时器后返回值，查看是否重置成功，]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[表示成功。]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_852771496}[：指定邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_1419082483}[：定时器间隔设定值]{lang="EN-US" style="font-family:宋体"}

[[enter helper mode for neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_707206119}*[x.x.x.x]{lang="NO-BOK"}*[ of *interface*. Neighbor count in IETF GR restart is ]{lang="EN-US"}*[number]{lang="NO-BOK"}*[.]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_852705960}[端为指定邻居进入]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_x2089195813}[：指定邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[interface]{lang="EN-US"}*]{#struct_0_35947_29584_439579285}[：]{lang="EN-US" style="font-family:宋体"}[邻居所在的接口]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number]{lang="NO-BOK"}*]{#struct_0_35947_29584_x2061461256}[：此时本]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}[端对应的]{lang="EN-US" style="font-family:宋体"}[Restarter]{lang="EN-US"}[个数]{lang="EN-US" style="font-family:宋体"}

[[exit helper mode for neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_852640424}*[x.x.x.x]{lang="NO-BOK"}*[ of *interface, exitreason*. Neighbor count in IETF GR restart is ]{lang="EN-US"}*[number]{lang="NO-BOK"}*[.]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1828878996}[端为指定邻居离开]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_993449911}[：指定的邻居]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[interface]{lang="EN-US"}*]{#struct_0_35947_29584_439382677}[：]{lang="EN-US" style="font-family:宋体"}[邻居所在的接口]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[exitreason]{lang="EN-US"}*]{#struct_0_35947_29584_440103573}[：]{lang="EN-US" style="font-family:宋体"}[退出原因]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[number]{lang="NO-BOK"}*]{#struct_0_35947_29584_852574888}[：此时本]{lang="EN-US" style="font-family:宋体"}[Helper]{lang="EN-US"}[端对应的]{lang="EN-US" style="font-family:宋体"}[Restarter]{lang="EN-US"}[个数]{lang="EN-US" style="font-family:宋体"}

[[received maximum age grace LSA from ]{lang="EN-US"}]{#struct_0_35947_29584_x1947515442}*[x.x.x.x]{lang="NO-BOK"}*[, not helper mode for the neighbor.]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_852968104}[端接收到指定邻居发来的]{style="font-family:宋体"}[age]{lang="EN-US"}[为]{style="font-family:宋体"}[3600]{lang="EN-US"}[的]{style="font-family:宋体"}[Grace LSA]{lang="EN-US"}[，但本]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端不作为指定邻居的]{style="font-family:宋体"}[Helper]{lang="EN-US"}

[[process exit all helper mode.]{lang="EN-US"}]{#struct_0_35947_29584_x724123171}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_1000890018}[端不再做任何邻居的]{style="font-family:宋体"}[Helper]{lang="EN-US"}

[[process exit helper mode abnormally, LSA check failed. LSA type: 0x]{lang="EN-US"}]{#struct_0_35947_29584_853295784}*[number1]{lang="NO-BOK"}*[, Lsid: ]{lang="EN-US"}*[number2]{lang="NO-BOK"}*[, Adv: ]{lang="EN-US"}*[x.x.x.x]{lang="NO-BOK"}*[.]{lang="EN-US"}

[[Helper]{lang="EN-US"}]{#struct_0_35947_29584_x873999875}[端退出]{style="font-family:宋体"}[Helper]{lang="EN-US"}[模式，因为]{style="font-family:宋体"}[LSA]{lang="EN-US"}[严格检查失败。]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="NO-BOK"}*]{#struct_0_35947_29584_1162733932}[：严格检查失败的]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的类型]{lang="EN-US" style="font-family:宋体"}

[[(1)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x2001]{lang="EN-US"}]{#struct_0_35947_29584_853230248}[表示]{style="font-family:宋体"}[Router -LSA]{lang="EN-US"}

[[(2)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x2002]{lang="EN-US"}]{#struct_0_35947_29584_643700802}[表示]{style="font-family:宋体"}[Network-LSA]{lang="EN-US"}

[[(3)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x2003]{lang="EN-US"}]{#struct_0_35947_29584_2131139696}[表示]{style="font-family:宋体"}[Inter-Area-Prefix-LSA]{lang="EN-US"}

[[(4)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x2004]{lang="EN-US"}]{#struct_0_35947_29584_x1876111856}[表示]{style="font-family:宋体"}[Inter-Area-Router-LSA]{lang="EN-US"}

[[(5)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x4005]{lang="EN-US"}]{#struct_0_35947_29584_x496191559}[表示]{style="font-family:宋体"}[AS-External-LSA]{lang="EN-US"}

[[(6)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x0008]{lang="EN-US"}]{#struct_0_35947_29584_x1876177392}[表示]{style="font-family:宋体"}[Link-LSA]{lang="EN-US"}

[[(7)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x2009]{lang="EN-US"}]{#struct_0_35947_29584_x1044653796}[表示]{style="font-family:宋体"}[Intra-Area-Prefix-LSA]{lang="EN-US"}

[[(8)[    ]{style="font:7.0pt "}]{lang="EN-US"}[0x000b]{lang="EN-US"}]{#struct_0_35947_29584_x746400139}[表示]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1876242928}[：该]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Link State ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_199410563}[：该]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的通告路由器]{style="font-family:宋体"}

[[DR/BDR is confilicting with helper.]{lang="EN-US"}]{#struct_0_35947_29584_439317147}

[[当前]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}]{#struct_0_35947_29584_439251611}[与]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端发来的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中通告的]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[DR/BDR recovered from DBM: x.x.x.x/x.x.x.x, helper\'s DR/BDR: x.x.x.x/x.x.x.x.]{lang="EN-US"}]{#struct_0_35947_29584_439448219}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_35947_29584_439382683}[里恢复的]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[和]{style="font-family:宋体"}[helper]{lang="EN-US"}[带过来的]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_2005597691}[：被选为]{style="font-family:宋体"}[DR]{lang="NO-BOK"}[或者]{style="font-family:宋体"}[BDR]{lang="NO-BOK"}[的]{style="font-family:宋体"}[Router ID]{lang="NO-BOK"}

[[local DR/BDR: x.x.x.x/x.x.x.x, helper\'s DR/BDR: x.x.x.x/x.x.x.x.]{lang="EN-US"}]{#struct_0_35947_29584_2005794299}

[[本地的]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}]{#struct_0_35947_29584_x831657555}[和]{style="font-family:宋体"}[helper]{lang="EN-US"}[带过来的]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[x.x.x.x]{lang="NO-BOK"}*]{#struct_0_35947_29584_2005335547}[：被选为]{style="font-family:宋体"}[DR]{lang="NO-BOK"}[或者]{style="font-family:宋体"}[BDR]{lang="NO-BOK"}[的]{style="font-family:宋体"}[Router ID]{lang="NO-BOK"}

[[exit restarter mode for interface *interface*, *exitreason*.]{lang="EN-US"}]{#struct_0_35947_29584_2005532155}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_2005466619}[端某个接口退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[i]{lang="EN-US"}[nterface]{lang="EN-US"}*]{#struct_0_35947_29584_2006187515}[：退出]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[exitreason]{lang="EN-US"}*]{#struct_0_35947_29584_2006121979}[：]{lang="EN-US" style="font-family:宋体"}[接口退出原因]{style="font-family:宋体"}

[[process exit restarter mode, all neighbors have been done.]{lang="EN-US"}]{#struct_0_35947_29584_x1875849712}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_1748645136}[端的所有邻居都平滑重启完成]{style="font-family:宋体"}

[[process exit restarter mode abnormally, interface changed.]{lang="EN-US"}]{#struct_0_35947_29584_374152865}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_x1875587568}[端退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[模式，因为接口发生改变]{style="font-family:宋体"}

[[process exit restarter mode abnormally, neighbor changed.]{lang="EN-US"}]{#struct_0_35947_29584_2006121980}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_2005663225}[端退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[模式，因为邻居发生改变]{style="font-family:宋体"}

[[process exit restarter mode abnormally, GR period timer expired.]{lang="EN-US"}]{#struct_0_35947_29584_x1876177391}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_x641369269}[端退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[模式，因为超过了平滑重启时间]{style="font-family:宋体"}

[[process exit restarter mode, no interface up.]{lang="EN-US"}]{#struct_0_35947_29584_2006187513}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_2005663226}[端退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[模式，因为没有接口]{style="font-family:宋体"}[up]{lang="EN-US"}

[[graceful restart is finished]{lang="EN-US"}]{#struct_0_35947_29584_x1876242927}

[[Restarter]{lang="EN-US"}]{#struct_0_35947_29584_x560104324}[端完成了平滑重启]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ospfv3 event interface]{lang="EN-US"}]{#struct_0_35947_29584_x1876308463}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_302040207}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_2053578113}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x751846006}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_1138177898}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x704661724}[进程号]{style="font-family:宋体"}

[[Interface *if-name* received *event* and its state from *pre-state* -\> *cur-state*.]{lang="EN-US"}]{#struct_0_35947_29584_487482940}

[[接口状态变化]{style="font-family:宋体"}]{#struct_0_35947_29584_x1379072727}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_35947_29584_x1875849711}[：接口名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event]{lang="EN-US"}*]{#struct_0_35947_29584_1345360609}[：接口状态机事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pre-state/cur-state]{lang="EN-US"}*]{#struct_0_35947_29584_1007830009}[：接口状态机状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ospfv3 event neighbor]{lang="EN-US"}]{#struct_0_35947_29584_1035084514}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_305239030}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x2120858962}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_362335784}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1875915247}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1588216499}[进程号]{style="font-family:宋体"}

[[Neighbor *nbr-id* (*if-name*) received *event* and its state from *pre-state* -\> *cur-state*.]{lang="EN-US"}]{#struct_0_35947_29584_x987799326}

[[邻居状态变化]{style="font-family:宋体"}]{#struct_0_35947_29584_x741796654}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-id]{lang="EN-US"}*]{#struct_0_35947_29584_x528656943}[：邻居的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[if-name]{lang="EN-US"}*]{#struct_0_35947_29584_x1509025689}[：接口名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event]{lang="EN-US"}*]{#struct_0_35947_29584_1302627526}[：邻居状态机事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pre-state/cur-state]{lang="EN-US"}*]{#struct_0_35947_29584_x1875980783}[：邻居状态机状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_x62202553}[]{#_Toc133749756}[]{#_Toc93984826}[]{#_Toc81478692}[]{#_Toc58333153}[]{#_Toc58294808}[]{#_Toc29710726}[]{#_Hlt19607792}

[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_990225061}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::1/64]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::2/64]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开邻居事件调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 event neighbor]{lang="EN-US"}]{#struct_0_35947_29584_x381992525}

[\*Apr 20 15:44:55:319 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor 2.2.2.2(GigabitEthernet1/0/2) received HelloReceived and its state from Down -\> Init.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1847763945}*[邻居状态由]{style="font-family:宋体"}[Down]{lang="EN-US"}[变为]{style="font-family:宋体"}[Init]{lang="EN-US"}*

[[\*Apr 20 15:44:55:319 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_1858463318}[2.2.2]{lang="EN-US"}[.2(GigabitEthernet1/0/2) received 2WayReceived and its state from Init -\> ExStart.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_143967931}*[邻居状态由]{style="font-family:宋体"}[Init]{lang="EN-US"}[变为]{style="font-family:宋体"}[Exstart]{lang="EN-US"}*

[[\*Apr 20 15:45:24:276 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_x1876046319}[2.2.2]{lang="EN-US"}[.2(GigabitEthernet1/0/2) received NegotiationDone and its state from ExStart -\> Exc]{lang="EN-US"}

[hange.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x835504108}*[邻居状态由]{style="font-family:宋体"}[Exstart]{lang="EN-US"}[变为]{style="font-family:宋体"}[Exchange]{lang="EN-US"}*

[[\*Apr 20 15:45:24:286 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_1922437128}[2.2.2]{lang="EN-US"}[.2(GigabitEthernet1/0/2) received ExchangeDone and its state from Exchange -\> Loadi]{lang="EN-US"}

[ng.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x657670461}*[邻居状态由]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[变为]{style="font-family:宋体"}[Loading]{lang="EN-US"}*

[[\*Apr 20 15:45:24:286 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 : Neighbor ]{lang="EN-US"}]{#struct_0_35947_29584_599323340}[2.2.2]{lang="EN-US"}[.2(GigabitEthernet1/0/2) received LoadingDone and its state from Loading -\> Full.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_1528490522}*[邻居状态由]{style="font-family:宋体"}[Loading]{lang="EN-US"}[变为]{style="font-family:宋体"}[Full]{lang="EN-US"}*

::: {#-7601585 .myid}
[]{#_Toc404788845}[]{#struct_0_35947_29584_1630942045}[]{#_Toc301773754}[]{#_Toc161563940}[]{#_Toc133749757}[]{#_Toc93984827}[]{#_Toc81478693}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 lsa**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_1219624237}

[**[debugging ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **lsa** { **generate** \| **install** \| **receive** }]{lang="EN-US"}]{#struct_0_35947_29584_x1875587567}

[**[undo debugging ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **lsa** { **generate** \| **install** \| **receive** }]{lang="EN-US"}]{#struct_0_35947_29584_x1442575651}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_x36163893}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_x899842901}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_x280085133}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_651987726}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_1272601924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1882734552}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_264689423}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_35947_29584_x1875653103}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成调试信息开关。]{style="font-family:宋体"}

[**[install]{lang="EN-US"}**]{#struct_0_35947_29584_1675534766}[：表示将]{style="font-family:宋体"}[LSA]{lang="EN-US"}[导入到]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中的调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_35947_29584_1939539661}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[接收调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_198591663}

[**[debugging ospfv3 lsa]{lang="EN-US"}**]{#struct_0_35947_29584_1629839232}[命令用来打开]{style="font-family:宋体"}[LSA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ospfv3 lsa]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LSA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_104352845}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1055123464}[进程的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging ospfv3 lsa]{lang="EN-US"}]{#struct_0_35947_29584_x1617639645}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_304382206}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_1571662774}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1876111858}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1658990973}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1282825383}[进程号]{style="font-family:宋体"}

[[LS Age = *lsa-age*]{lang="NO-BOK"}]{#struct_0_35947_29584_725954869}

[[LSA]{lang="NO-BOK"}]{#struct_0_35947_29584_x2096320567}[的生存时间]{style="font-family:宋体"}

[[LS Type = *lsa-type*]{lang="NO-BOK"}]{#struct_0_35947_29584_1804141437}

[*[lsa-type]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1876177394}[：]{style="font-family:宋体"}[LSA]{lang="NO-BOK"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x2001]{lang="NO-BOK"}]{#struct_0_35947_29584_118145618}[表示]{lang="EN-US" style="font-family:宋体"}[Router-LSA]{lang="NO-BOK"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x2002]{lang="NO-BOK"}]{#struct_0_35947_29584_1393188908}[表示]{lang="EN-US" style="font-family:宋体"}[Network-LSA]{lang="NO-BOK"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x2003]{lang="NO-BOK"}]{#struct_0_35947_29584_x229002314}[表示]{lang="EN-US" style="font-family:宋体"}[Inter-area-prefix-LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2004]{lang="EN-US"}]{#struct_0_35947_29584_421652905}[表示]{lang="EN-US" style="font-family:宋体"}[Inter-area-router-LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x4005]{lang="NO-BOK"}]{#struct_0_35947_29584_x952360827}[表示]{lang="EN-US" style="font-family:宋体"}[AS-External-LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x2007]{lang="NO-BOK"}]{#struct_0_35947_29584_x1876242930}[表示]{lang="EN-US" style="font-family:宋体"}[NSSA-LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}[0x0008]{lang="NO-BOK"}]{#struct_0_35947_29584_x156754261}[表示]{lang="EN-US" style="font-family:宋体"}[Link-LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[0x2009]{lang="PT-BR"}]{#struct_0_35947_29584_x1170923458}[表示]{lang="EN-US" style="font-family:宋体"}[Intra-Area-Prefix-LSA]{lang="EN-US"}

[[LS ID = *ls-id*]{lang="NO-BOK"}]{#struct_0_35947_29584_x6377533}

[[LSA]{lang="NO-BOK"}]{#struct_0_35947_29584_1656322164}[的链路状态]{style="font-family:宋体"}[ID]{lang="NO-BOK"}

[[Adv ID = *adv-id*]{lang="NO-BOK"}]{#struct_0_35947_29584_x1876308466}

[[发布]{style="font-family:宋体"}]{#struct_0_35947_29584_1294063226}[LSA]{lang="NO-BOK"}[的]{style="font-family:宋体"}[Router ID]{lang="NO-BOK"}

[[Seq Number = *seqnum*]{lang="NO-BOK"}]{#struct_0_35947_29584_x573179170}

[[LSA]{lang="NO-BOK"}]{#struct_0_35947_29584_x654120827}[序列号]{style="font-family:宋体"}

[[Cksum = *chksum*]{lang="NO-BOK"}]{#struct_0_35947_29584_x1224281593}

[[LSA]{lang="NO-BOK"}]{#struct_0_35947_29584_x1875849714}[校验和]{style="font-family:宋体"}

[[Length = *length*]{lang="NO-BOK"}]{#struct_0_35947_29584_942076082}

[[LSA]{lang="NO-BOK"}]{#struct_0_35947_29584_1653559689}[长度]{style="font-family:宋体"}

[[Generate LSA at *time-stamp* ms.]{lang="NO-BOK"}]{#struct_0_35947_29584_x1166715726}

[[生成]{style="font-family:宋体"}]{#struct_0_35947_29584_1991737135}[LSA]{lang="NO-BOK"}[的时间]{style="font-family:宋体"}

[[Install LSA at ]{lang="EN-US"}]{#struct_0_35947_29584_x1875915250}*[time-stamp]{lang="NO-BOK"}*[ ms.]{lang="EN-US"}

[[安装]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_x784502032}[的时间]{style="font-family:宋体"}

[[Receive LSA at *time-stamp* ms.]{lang="EN-US"}]{#struct_0_35947_29584_743660437}

[[接收]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_1386293248}[的时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_90964765}

[]{#_Toc133749758}[]{#_Toc93984828}[]{#_Toc81478694}[[\# Router A]{lang="FR"}]{#struct_0_35947_29584_x1875980786}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="FR"}[（]{style="font-family:宋体"}[1001::1/64]{lang="FR"}[）]{style="font-family:宋体"}[与]{style="font-family:宋体"}[Router B]{lang="FR"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[（]{style="font-family:宋体"}[1001::2/64]{lang="FR"}[）]{style="font-family:宋体"}[相连]{style="font-family:宋体"}[，]{style="font-family:宋体"}[网络类型为]{style="font-family:宋体"}[Broadcast]{lang="FR"}[，]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Router A]{lang="FR"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程]{style="font-family:宋体"}[1]{lang="FR"}[，]{style="font-family:
宋体"}[在]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程]{style="font-family:宋体"}[1]{lang="FR"}[中创建区域]{style="font-family:
宋体"}[1]{lang="FR"}[，]{style="font-family:宋体"}[在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="FR"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="FR"}[；]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Router B]{lang="FR"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[进程]{style="font-family:宋体"}[1]{lang="FR"}[，]{style="font-family:
宋体"}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="FR"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="FR"}[。]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Router A]{lang="FR"}[上打开]{style="font-family:宋体"}[LSA]{lang="FR"}[生成调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 lsa generate]{lang="NO-BOK"}]{#struct_0_35947_29584_x821717440}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402163 ms.]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2001]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.0]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001]{lang="NO-BOK"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x101e]{lang="EN-US"}

[\*Apr 20 16:06:29:163 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 24]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_1259441372}*[生成]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}*

[[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402164 ms.]{lang="EN-US"}]{#struct_0_35947_29584_1837805551}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x0008]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.3]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0xfee]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 56]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1303917297}*[生成]{style="font-family:宋体"}[Link LSA]{lang="EN-US"}*

[[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2402164 ms.]{lang="EN-US"}]{#struct_0_35947_29584_x1876046322}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2009]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.1]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000001]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x4368]{lang="EN-US"}

[\*Apr 20 16:06:29:164 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 44]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x788646549}*[生成]{style="font-family:宋体"}[Intra-Area-Prefix-LSA]{lang="EN-US"}*

[[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1 Generate LSA at 2410239 ms.]{lang="EN-US"}]{#struct_0_35947_29584_1205939813}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;   OSPFv3 LSA Header:]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Age = 0]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS Type = 0x2001]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     LS ID = 0.0.0.0]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Adv ID = 1.1.1.1]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Seq Number = 0x80000007]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Cksum = 0x8c66]{lang="EN-US"}

[\*Apr 20 16:06:37:239 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;     Length = 40]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x2105328585}*[重新生成]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}*

::: {#-69666850 .myid}
[]{#_Toc404788846}[]{#struct_0_35947_29584_x1875587570}[]{#_Toc301773755}[]{#_Toc161563942}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_x683126300}

[**[debugging ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **packet** \[ **ack** \| **dd** \| **hello** \| **request** \| **update** \]]{lang="EN-US"}]{#struct_0_35947_29584_1078472092}

[**[undo debugging ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **packet** \[ **ack** \| **dd** \| **hello** \| **request** \| **update** \]]{lang="EN-US"}]{#struct_0_35947_29584_x1834345024}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1729790925}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_1472729212}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_1481841460}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_185199371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_x821770726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1875653106}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1859917643}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ack]{lang="EN-US"}**]{#struct_0_35947_29584_x1966860897}[：表示]{style="font-family:宋体"}[LSAck]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[dd]{lang="EN-US"}**]{#struct_0_35947_29584_574709336}[：表示]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[hello]{lang="EN-US"}**]{#struct_0_35947_29584_x1303658956}[：表示]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[request]{lang="EN-US"}**]{#struct_0_35947_29584_463904155}[：表示]{style="font-family:宋体"}[LSR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[update]{lang="EN-US"}**]{#struct_0_35947_29584_701664119}[：表示]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_1159820757}

[**[debugging ospfv3 packet]{lang="EN-US"}**]{#struct_0_35947_29584_x547216372}[命令用来打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo debugging ospfv3 packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[OSPFv3]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1938664188}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1876111857}[进程的报文调试信息开关。]{style="font-family:宋体"}

[]{#struct_0_35947_29584_1069892382}[[表1-7 ]{lang="EN-US"}[debugging ospfv3 packet]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_334640049}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x19710974}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1883632597}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_406419849}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x466708073}[进程号]{style="font-family:宋体"}

[[Interface id: *interface-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1230996338}

[[接口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_35947_29584_x1876177393}

[[Router Priority: *router-pri*]{lang="EN-US"}]{#struct_0_35947_29584_521430145}

[[路由器优先级]{style="font-family:宋体"}]{#struct_0_35947_29584_x816021586}

[[Option: *option*]{lang="EN-US"}]{#struct_0_35947_29584_x1867162346}

[[选项字段]{style="font-family:宋体"}]{#struct_0_35947_29584_x1329608140}

[[Hello Interval: *interval*]{lang="EN-US"}]{#struct_0_35947_29584_287159882}

[[Hello]{lang="EN-US"}]{#struct_0_35947_29584_x1876242929}[报文时间间隔]{style="font-family:宋体"}

[[Dead Interval: *interval*]{lang="EN-US"}]{#struct_0_35947_29584_x1366673378}

[[超时时长]{style="font-family:宋体"}]{#struct_0_35947_29584_1371659877}

[[DR: *router-id*]{lang="EN-US"}]{#struct_0_35947_29584_25893707}

[[DR]{lang="EN-US"}]{#struct_0_35947_29584_1056073553}[的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[BDR: *router-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1876308465}

[[BDR]{lang="EN-US"}]{#struct_0_35947_29584_890778699}[的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[MTU: *value*]{lang="EN-US"}]{#struct_0_35947_29584_1701521053}

[[MTU]{lang="EN-US"}]{#struct_0_35947_29584_x1969907748}[值]{style="font-family:宋体"}

[[R_I_M_MS Bit: *value*]{lang="EN-US"}]{#struct_0_35947_29584_222295545}

[[DD]{lang="EN-US"}]{#struct_0_35947_29584_x1875849713}[报文]{style="font-family:宋体"}[R_I_M_MS]{lang="EN-US"}[字段值]{style="font-family:宋体"}

[[DD Sequence number: *seq-value*]{lang="EN-US"}]{#struct_0_35947_29584_182561195}

[[DD]{lang="EN-US"}]{#struct_0_35947_29584_x146560972}[报文序列号]{style="font-family:宋体"}

[[LSA type: *lsa-type*]{lang="EN-US"}]{#struct_0_35947_29584_288559410}

[[LSA]{lang="EN-US"}]{#struct_0_35947_29584_x461619840}[类型]{style="font-family:宋体"}

[[LinkStateId: *ls-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1875915249}

[[LSA]{lang="EN-US"}]{#struct_0_35947_29584_425417085}[的]{style="font-family:宋体"}[LS ID]{lang="EN-US"}

[[Advertising Rtr: *router-id*]{lang="EN-US"}]{#struct_0_35947_29584_x947974232}

[[发布路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_35947_29584_x1945354426}

[[LSA age: *lsa-age*]{lang="EN-US"}]{#struct_0_35947_29584_x1875980785}

[[LSA]{lang="EN-US"}]{#struct_0_35947_29584_x1225001967}[年龄]{style="font-family:宋体"}

[[Length: *value*]{lang="EN-US"}]{#struct_0_35947_29584_1377926390}

[[长度]{style="font-family:宋体"}]{#struct_0_35947_29584_1909452683}

[[Checksum: *value*]{lang="EN-US"}]{#struct_0_35947_29584_x1876046321}

[[校验和]{style="font-family:宋体"}]{#struct_0_35947_29584_x1191931076}

[[LSA count: *value*]{lang="EN-US"}]{#struct_0_35947_29584_x943481168}

[[LSU]{lang="EN-US"}]{#struct_0_35947_29584_634357231}[报文保护的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Version *value*]{lang="EN-US"}]{#struct_0_35947_29584_x1875587569}

[[版本号]{style="font-family:宋体"}]{#struct_0_35947_29584_x1892914345}

[[Source address: *src-addr*]{lang="EN-US"}]{#struct_0_35947_29584_x687104000}

[[源地址]{style="font-family:宋体"}]{#struct_0_35947_29584_1198528210}

[[Destination address: *dst-addr*]{lang="EN-US"}]{#struct_0_35947_29584_x1875653105}

[[目的地址]{style="font-family:宋体"}]{#struct_0_35947_29584_868965712}

[[Receiving packets]{lang="EN-US"}]{#struct_0_35947_29584_1031728807}

[[收到报文]{style="font-family:宋体"}]{#struct_0_35947_29584_x1876111860}

[[OSPFv3 received packet having bad type :*value*]{lang="EN-US"}]{#struct_0_35947_29584_x1302564005}

[[收到错误的类型报文]{style="font-family:宋体"}]{#struct_0_35947_29584_179455867}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_35947_29584_x1072516306}[：报文类型]{lang="EN-US" style="font-family:宋体"}

[[Sending packets]{lang="EN-US"}]{#struct_0_35947_29584_x1876177396}

[[发送报文]{style="font-family:宋体"}]{#struct_0_35947_29584_1280945032}

[[OSPFv3 received packet with invalid destination]{lang="EN-US"}]{#struct_0_35947_29584_x1677935279}

[[收到错误的目的地址报文]{style="font-family:宋体"}]{#struct_0_35947_29584_x1876242932}

[[OSPFv3 received packet having conflicted Router ID :*router-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1319553675}

[[收到重复的]{style="font-family:宋体"}[Router-ID]{lang="EN-US"}]{#struct_0_35947_29584_2079003373}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[router-id]{lang="FR"}*]{#struct_0_35947_29584_x1876308468}[：]{lang="EN-US" style="font-family:宋体"}[路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="FR"}

[[OSPFv3 received packet with mismatch AREA]{lang="EN-US"}]{#struct_0_35947_29584_131263812}

[[收到区域不匹配的报文]{style="font-family:宋体"}]{#struct_0_35947_29584_x935941703}

[[Ignored the packet on interface *interface-type interface-number* due to IPsec profile mismatch.]{lang="EN-US"}]{#struct_0_35947_29584_x1845727651}

[[IPsec]{lang="EN-US"}]{#struct_0_35947_29584_x1875849716}[安全框架不匹配，忽略该报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_35947_29584_x220723332}[：接]{style="font-family:宋体"}[口类型和编号，从该接口收到]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_586702671}

[]{#_Toc133749760}[]{#_Toc93984830}[]{#_Toc81478696}[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_691928681}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::1/64]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::2/64]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 packet dd]{lang="EN-US"}]{#struct_0_35947_29584_x1875915252}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]{lang="EN-US"}

[\*Apr 20 17:57:31:545 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00002368.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1947301446}*[发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.]{lang="EN-US"}]{#struct_0_35947_29584_x765629869}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 41302, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003782.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_128708938}*[接收]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.]{lang="EN-US"}]{#struct_0_35947_29584_x1875980788}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 88.]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:547 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|-.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003782.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 0008.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.3.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 56 Sequence number: 80000001 Checksum: 0fee.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2001.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.0.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 24 Sequence number: 80000001 Checksum: 101e.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2009.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.1.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 1.1.1.1.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 6.]{lang="EN-US"}

[\*Apr 20 17:57:31:548 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 44 Sequence number: 80000001 Checksum: 4368.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1272056134}*[发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.]{lang="EN-US"}]{#struct_0_35947_29584_x1876046324}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 88.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 35496, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|MS.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003783.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 0008.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.15.0.8.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 214.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 56 Sequence number: 80000001 Checksum: 04d4.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2001.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.0.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 167.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 24 Sequence number: 80000003 Checksum: ed3a.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA type: 2009.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LinkStateId: 0.0.0.1.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Advertising Rtr: 2.2.2.2.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; LSA age: 166.]{lang="EN-US"}

[\*Apr 20 17:57:31:554 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Length: 44 Sequence number: 80000002 Checksum: 554d.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1595215603}*[接收]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.]{lang="EN-US"}]{#struct_0_35947_29584_x1875587572}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.]{lang="EN-US"}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: I\|M\|-.]{lang="EN-US"}

[\*Apr 20 17:57:31:555 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003783.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1845925714}*[发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Receiving packets.]{lang="EN-US"}]{#struct_0_35947_29584_397139861}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 2.2.2.2, Area: 0.0.0.1, Checksum: 41306, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: -\|-\|MS.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003784.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_260933453}*[接收]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; OSPFv3 1: Sending packets.]{lang="EN-US"}]{#struct_0_35947_29584_x1875653108}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Source address: fe80::20c:29ff:fe85:9205]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Destination address: fe80::200:5eff:fe00:100]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Version 3, Type: 2, Length: 28.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; Router: 1.1.1.1, Area: 0.0.0.1, Checksum: 0, Instance: 0.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; MTU: 1500, Option: -\|R\|-\|-\|E\|V6, R_I_M_MS Bit: -\|-\|-.]{lang="EN-US"}

[\*Apr 20 17:57:31:566 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1; DD Sequence number: 00003784.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_1628480599}*[发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-434549209 .myid}
[]{#_Toc301773756}[]{#_Toc161563943}[]{#_Toc404788847}[]{#struct_0_35947_29584_1695232868}[]{#_Toc348020504}[]{#_Toc340742739}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 policy**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_1513713594}

[**[debugging]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **export** \| **import** \| **preference** }]{lang="EN-US"}]{#struct_0_35947_29584_137733881}

[**[undo]{lang="EN-US"}**[ **debugging** **ospfv3** \[ *process-id* \] **policy** { **abr-filter** \| **all** \| **default-route** \| **event** \| **export** \| **import** \| **preference** }]{lang="EN-US"}]{#struct_0_35947_29584_x1985114029}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_397598089}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_7875431}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_1173598181}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_x1965060204}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_x1876111859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x92907032}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x316342154}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[abr-filter]{lang="EN-US"}**]{#struct_0_35947_29584_x1901401845}[：打开]{style="font-family:宋体"}[3]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}[过策略调试开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_35947_29584_x1669675142}[：打开所有路由过策略的调试开关。]{style="font-family:宋体"}

[**[default-route]{lang="EN-US"}**]{#struct_0_35947_29584_x491576899}[：打开默认路由过策略的调试开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_35947_29584_x848425147}[：打开策略事件的调试开关。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_35947_29584_x770264191}[：打开引入路由过策略的调试开关。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_35947_29584_x1876177395}[：打开下路由过策略的调试开关。]{style="font-family:宋体"}

[**[preference]{lang="EN-US"}**]{#struct_0_35947_29584_1684229559}[：打开优先级过策略的调试开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_x993048709}

[**[debugging]{lang="EN-US"}**[ **ospfv3** **policy**]{lang="EN-US"}]{#struct_0_35947_29584_x1964343191}[命令用来打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由过策略调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging]{lang="DA"}**[ **ospfv3** ]{lang="DA"}**[policy]{lang="EN-US"}**[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[路由过策略调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_711373409}[路由过策略调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x369836737}[进程的路由过策略调试信息开关。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging ospfv3 policy abr-filter]{lang="EN-US"}]{#struct_0_35947_29584_1197006187}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_325027423}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x780320293}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_984040607}

[[OSPFv3 *process-id* checked abr-filter policy, area *area-id*, abr-filter type: *abr-filter-type,* flag: *flag*, policy type: *policy-type*, policy name: *name,* check address: *check-addr,* mask length: *length*]{lang="EN-US"}]{#struct_0_35947_29584_x1876242931}

[[Type-3 LSA]{lang="EN-US"}]{#struct_0_35947_29584_x1722838202}[过策略相关信息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1603147107}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[v3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[area-id]{lang="EN-US"}*]{#struct_0_35947_29584_x90260988}[：]{lang="EN-US" style="font-family:宋体"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[abr-filter-type]{lang="EN-US"}*]{#struct_0_35947_29584_1566903071}[：]{lang="EN-US" style="font-family:宋体"}[ABR]{lang="EN-US"}[策略]{lang="EN-US" style="font-family:宋体"}[类型，]{style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:宋体"}[import]{lang="EN-US"}[表示对向本区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过策略，]{style="font-family:宋体"}[export]{lang="EN-US"}[表示对向其它区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_35947_29584_x1487556486}[：标志位，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示对下一跳过策略，取值为]{style="font-family:宋体"}[2]{lang="EN-US"}[表示对前缀过策略]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[policy-]{lang="EN-US"}[type]{lang="EN-US"}*]{#struct_0_35947_29584_2036469579}[：]{lang="EN-US" style="font-family:宋体"}[过]{style="font-family:宋体"}[策略类型]{lang="EN-US" style="font-family:宋体"}[，包括]{style="font-family:宋体"}[acl]{lang="EN-US"}[，]{style="font-family:宋体"}[prefix-list]{lang="EN-US"}[和]{style="font-family:宋体"}[route-policy]{lang="EN-US"}[三种类型]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_35947_29584_x1876308467}[：策略名]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[check-addr]{lang="EN-US"}*]{#struct_0_35947_29584_x272020715}[：过策略的前缀]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[len]{lang="EN-US"}*]{#struct_0_35947_29584_1997406618}*[gth]{lang="EN-US"}*[：前缀掩码长度]{style="font-family:宋体"}

[[OSPFv3 ]{lang="PT-BR"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_907100510}[ ]{lang="EN-US"}[checked ]{lang="PT-BR"}[abr-filter]{lang="EN-US"}[ ]{lang="EN-US"}[policy result]{lang="PT-BR"}[: *result,* cost: *cost*]{lang="EN-US"}

[[Type-3 LSA]{lang="EN-US"}]{#struct_0_35947_29584_x2049527712}[过策略结果]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1113086521}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[v3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_x1875849715}[：过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x624007859}[：过策略后的开销]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ospfv3 policy default-route]{lang="EN-US"}]{#struct_0_35947_29584_x683242539}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_326300455}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x96380144}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x853240225}

[[OSPFv3 *process-id* received default-route policy message, result: *result*, flag: *flag*, cost type: *type*, cost: *cost*]{lang="EN-US"}]{#struct_0_35947_29584_1351872997}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1875915251}[收到默认路由过策略消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_781581909}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_206183643}[：]{lang="EN-US" style="font-family:宋体"}[过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_35947_29584_2109997544}[：标志位，]{style="font-family:
  宋体"}[0x0]{lang="EN-US"}[表示无应用，]{style="font-family:宋体"}[0x1]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost]{lang="EN-US"}[，]{style="font-family:宋体"}[0x2]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost type]{lang="EN-US"}[，]{style="font-family:宋体"}[0x8]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[tag]{lang="EN-US"}[，若存在多个应用，该标志位为或的关系]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_35947_29584_x2099809299}[：默认路由类型，]{style="font-family:
  宋体"}[type-1]{lang="EN-US"}[表示一类外部路由，]{style="font-family:
  宋体"}[type-2]{lang="EN-US"}[表示二类外部路由，]{style="font-family:
  宋体"}[unknown]{lang="EN-US"}[表示未知类型]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x240988365}[：过策略后的开销]{style="font-family:
  宋体"}

[[OSPFv3 *process-id* checked default-route policy permit, flag: *flag*, cost type: type, cost: *cost*]{lang="EN-US"}]{#struct_0_35947_29584_x1875980787}

[[默认路由过策略通过后的结果]{style="font-family:宋体"}]{#struct_0_35947_29584_1907165915}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1273785043}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_35947_29584_400069243}[：标志位，]{style="font-family:
  宋体"}[0x0]{lang="EN-US"}[表示无应用，]{style="font-family:宋体"}[0x1]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost]{lang="EN-US"}[，]{style="font-family:宋体"}[0x2]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[cost type]{lang="EN-US"}[，]{style="font-family:宋体"}[0x8]{lang="EN-US"}[表示应用]{style="font-family:宋体"}[tag]{lang="EN-US"}[，若存在多个应用，该标志位为或的关系]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_35947_29584_1803757178}[：默认路由类型，]{style="font-family:
  宋体"}[type-1]{lang="EN-US"}[表示一类外部路由，]{style="font-family:
  宋体"}[type-2]{lang="EN-US"}[表示二类外部路由，]{style="font-family:
  宋体"}[unknown]{lang="EN-US"}[表示未知类型]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x1876046323}[：过策略后的开销]{style="font-family:
  宋体"}

[[OSPFv3 *process-id* checked default-route policy deny.]{lang="EN-US"}]{#struct_0_35947_29584_1940236806}

[[默认路由过策略不通过]{style="font-family:宋体"}]{#struct_0_35947_29584_x1540716426}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_645963289}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging ospfv3 policy event]{lang="EN-US"}]{#struct_0_35947_29584_x1839915735}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_325443631}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x380002043}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1875587571}

[[OSPFv3 *process-id* received policy change event, import reference count: *number1*, calculate reference count: *number2*]{lang="EN-US"}]{#struct_0_35947_29584_2045757055}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x560402382}[进程过策略信息统计]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1231293057}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number1]{lang="EN-US"}*]{#struct_0_35947_29584_x467760645}[：本策略被进程]{lang="EN-US" style="font-family:宋体"}[引入]{style="font-family:宋体"}[过策略计数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[number2]{lang="EN-US"}*]{#struct_0_35947_29584_x1233051293}[：本策略被]{lang="EN-US" style="font-family:宋体"}[路由计算引入计数]{style="font-family:宋体"}

[[OSPFv3 *process-id* ignored policy change when process is under GR]{lang="EN-US"}]{#struct_0_35947_29584_x1875653107}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x293833702}[进程处于]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态而忽略策略变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1623799592}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPFv3 received acl number *acl-number* change event]{lang="EN-US"}]{#struct_0_35947_29584_x681729422}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x318237491}[收到]{style="font-family:宋体"}[acl]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[acl-]{lang="EN-US"}[number]{lang="EN-US"}*]{#struct_0_35947_29584_x534100339}[：访问控制列表号]{style="font-family:宋体"}

[[OSPFv3 received prefix-list *name* change event]{lang="EN-US"}]{#struct_0_35947_29584_x310027915}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x355318189}[收到前缀列表变化事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_35947_29584_x827418872}[：前缀列表名]{style="font-family:
  宋体"}

[[OSPFv3 received route-policy *name* change event ]{lang="EN-US"}]{#struct_0_35947_29584_x1147886027}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1980325854}[收到路由策略变化事件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_35947_29584_x276348280}[：路由策略名]{style="font-family:
  宋体"}

[[OSPFv3 received prefix-list batch end message]{lang="EN-US"}]{#struct_0_35947_29584_x310093451}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_22967267}[收到前缀列表批处理结束消息]{style="font-family:宋体"}

[[OSPFv3 received route-policy batch end message]{lang="EN-US"}]{#struct_0_35947_29584_x232050234}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_972612016}[收到路由过策略批处理结束消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging ospfv3 export]{lang="EN-US"}]{#struct_0_35947_29584_1668764110}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_319401118}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x310158987}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_1573877482}

[[OSPFv3 *process-id* checked export policy, address: *addr,* mask length: *length*]{lang="EN-US"}]{#struct_0_35947_29584_1998748429}

[[引入路由过策略相关信息]{style="font-family:宋体"}]{#struct_0_35947_29584_x423054474}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1616040443}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_1674939670}[：过策略的前缀]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[length]{lang="EN-US"}*]{#struct_0_35947_29584_x310224523}[：前缀掩码长]{lang="EN-US" style="font-family:宋体"}[度]{style="font-family:宋体"}

[[OSPFv3 ]{lang="PT-BR"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_6202469}[ ]{lang="EN-US"}[checked ]{lang="PT-BR"}[export]{lang="EN-US"}[ ]{lang="EN-US"}[policy result]{lang="PT-BR"}[: *result*, cost: *cost*]{lang="EN-US"}

[[引入路由过策略结果]{style="font-family:宋体"}]{#struct_0_35947_29584_1814375607}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1763730201}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_x1371712662}[：]{lang="EN-US" style="font-family:宋体"}[过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x1634389519}[：表示过策略后的开销]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging ospfv3 import]{lang="EN-US"}]{#struct_0_35947_29584_x309765771}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_322738534}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x669632373}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x426243394}

[[OSPFv3 *process-id* checked import policy, policy type: *type,* policy name: *name,* prefix: *prefix,* nexthop: *nexthop,* cost: *cost,* interface index: *if-index*]{lang="EN-US"}]{#struct_0_35947_29584_2016697982}

[[下路由过策略相关信息]{style="font-family:宋体"}]{#struct_0_35947_29584_785870201}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_931078545}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_35947_29584_x309831307}[：下路由过策略类型，包括]{style="font-family:
  宋体"}[acl]{lang="EN-US"}[，]{style="font-family:
  宋体"}[prefix-list]{lang="EN-US"}[和]{style="font-family:宋体"}[route-policy]{lang="EN-US"}[三种类型]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_35947_29584_2049140353}[：]{lang="EN-US" style="font-family:宋体"}[下路由过策略名]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[prefix]{lang="EN-US"}*]{#struct_0_35947_29584_x889833745}[：]{lang="EN-US" style="font-family:宋体"}[路由前缀]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_35947_29584_x757870385}[：下一跳地址]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x1595346156}[：下一跳开销]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[if-index]{lang="EN-US"}*]{#struct_0_35947_29584_x1011619602}[：出接口索引]{style="font-family:宋体"}

[[OSPFv3 *process-id* checked import policy result: *result*]{lang="EN-US"}]{#struct_0_35947_29584_x309896843}

[[下路由过策略结果]{style="font-family:宋体"}]{#struct_0_35947_29584_x337126632}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x603260711}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[v3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_x1865289536}[：]{lang="EN-US" style="font-family:宋体"}[过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging ospfv3 preference]{lang="EN-US"}]{#struct_0_35947_29584_40736322}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_349483440}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x309962379}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1827796852}

[[OSPFv3 *process-id* checked preference policy, preference: *pref,* policy name: *name,* prefix: *prefix,* nexthop: *nexthop,* cost: *cost,* interface index: *if-index*]{lang="EN-US"}]{#struct_0_35947_29584_x237185645}

[[路由优先级过策略相关信息]{style="font-family:宋体"}]{#struct_0_35947_29584_x2843899}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1024013807}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[v3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[pref]{lang="EN-US"}*]{#struct_0_35947_29584_2068025777}[：路由优先级]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[name]{lang="EN-US"}*]{#struct_0_35947_29584_x309503627}[：路由优先级过策略]{lang="EN-US" style="font-family:宋体"}[名]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[prefix]{lang="EN-US"}*]{#struct_0_35947_29584_x1823310682}[：]{lang="EN-US" style="font-family:宋体"}[路由前缀]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_35947_29584_x1625811739}[：下一跳地址]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[cost]{lang="EN-US"}*]{#struct_0_35947_29584_x1679439593}[：下一跳开销]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[if-index]{lang="EN-US"}*]{#struct_0_35947_29584_x1400233838}[：出接口索引]{style="font-family:宋体"}

[[OSPFv3 *process-id* checked preference policy result: *result*]{lang="EN-US"}]{#struct_0_35947_29584_938620160}

[[路由优先级过策略的调试结果]{style="font-family:宋体"}]{#struct_0_35947_29584_x309569163}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_2038172344}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[v3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_686485867}[：]{lang="EN-US" style="font-family:宋体"}[过策略结果，取值为]{style="font-family:宋体"}[permit]{lang="EN-US"}[表示通过，]{style="font-family:宋体"}[deny]{lang="EN-US"}[表示不通过]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_x338652554}

[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_x30553074}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1::1/64]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1::2/64]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；配置默认路由策略，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开默认路由过策略的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 policy default-route]{lang="EN-US"}]{#struct_0_35947_29584_x310027914}

[\*Nov  5 17:11:49:217 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 received default-route policy message, result: permit, flag: 0x1,]{lang="EN-US"}

[cost type: 2, cost: 33.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x355383725}*[接收到默认路由过策略消息]{style="font-family:宋体"}*

[[\*Nov  5 17:11:49:217 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_355570777}

[  OSPFv3 1 checked default-route policy permit, flag: 0x1, cost type: type-2,]{lang="EN-US"}

[cost: 33.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x2098926471}*[默认路由过策略通过后的结果]{style="font-family:宋体"}*

[[\# Router A]{lang="PT-BR"}]{#struct_0_35947_29584_887822978}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[（]{style="font-family:宋体"}[1::1/64]{lang="PT-BR"}[）与]{style="font-family:宋体"}[Router B]{lang="PT-BR"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[（]{style="font-family:宋体"}[1::2/64]{lang="PT-BR"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="PT-BR"}[，在]{style="font-family:宋体"}[Router A]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[中创建区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="PT-BR"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[，配置静态路由]{style="font-family:宋体"}[1::8/128]{lang="PT-BR"}[，引入静态路由；在]{style="font-family:宋体"}[Router B]{lang="PT-BR"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="PT-BR"}[进程]{style="font-family:宋体"}[1]{lang="PT-BR"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="PT-BR"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="PT-BR"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="PT-BR"}[；配置策略，在]{style="font-family:宋体"}[Router A]{lang="PT-BR"}[上打开引入路由过策略的调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 policy export]{lang="PT-BR"}]{#struct_0_35947_29584_x86231705}

[\*Nov  5 14:46:01:042 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="PT-BR"}

[  ]{lang="PT-BR"}[OSPFv3 1 checked export policy ]{lang="PT-BR" style="font-size:8.0pt;color:black"}[address: 1::8, mask Length: 128.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_35947_29584_x310093450}*[引入路由过策略相关信息]{style="font-family:宋体"}*

[[\*Nov  5 14:46:01:042 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="PT-BR"}]{#struct_0_35947_29584_23032803}

[  OSPFv3 1 checked export policy result: permit, cost: 0.]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_35947_29584_1666651082}*[引入路由过策略结果]{style="font-family:宋体"}*

::: {#1334113892 .myid}
[]{#_Toc404788848}[]{#struct_0_35947_29584_1718077484}[]{#_Toc348020505}[]{#_Toc340742740}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 redistribute**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_x826312265}

[**[debugging]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **redistribute** \[ **prefix** *ipv6-address prefix-length* \]]{lang="EN-US"}]{#struct_0_35947_29584_2022304307}

[**[undo]{lang="EN-US"}**[ **debugging** **ospfv3** \[ *process-id* \] **redistribute**]{lang="EN-US"}]{#struct_0_35947_29584_x164539312}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_x310158986}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_1573943018}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1089886087}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_x1318158081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_966738086}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_1275621880}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1129431090}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_35947_29584_x420239362}[：表示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的引入路由调试信息开关。]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀；]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_x373286365}

[**[debugging]{lang="EN-US"}**[ **ospfv3** **redistribute**]{lang="EN-US"}]{#struct_0_35947_29584_x310224522}[命令用来打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[引入路由调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging]{lang="DA"}**[ **ospfv3** ]{lang="DA"}**[redistribute]{lang="EN-US"}**[命令]{style="font-family:
宋体"}[用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[引入路由调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_6136933}[引入路由调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1281459941}[进程的引入路由调试信息开关。如果未指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀，则显示所有的引入路由调试信息。]{style="font-family:宋体"}

[[表1-14 ]{lang="EN-US"}[debugging ospfv3 redistribute]{lang="EN-US"}]{#struct_0_35947_29584_x1612173271}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_348630700}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_566823401}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_1909724534}

[[OSPFv3 received rib batch start message, instance: ]{lang="EN-US"}]{#struct_0_35947_29584_1151989240}*[instance-id]{lang="NO-BOK"}*[, ]{lang="NO-BOK"}[user data: *user-data*]{lang="EN-US"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309765770}[实例收到批处理开始的消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[instance-id]{lang="NO-BOK"}*]{#struct_0_35947_29584_x669697909}[：路由所在]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[user-data]{lang="EN-US"}*]{#struct_0_35947_29584_1460097474}[：消息中携带的用户数据值]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 received rib batch end message, instance: ]{lang="EN-US"}]{#struct_0_35947_29584_x539327474}*[instance-id]{lang="NO-BOK"}*[, ]{lang="NO-BOK"}[user data: *user-data*]{lang="EN-US"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1809548409}[实例收到批处理结束的消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[instance-id]{lang="NO-BOK"}*]{#struct_0_35947_29584_1719846943}[：路由所在]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[user-data]{lang="EN-US"}*]{#struct_0_35947_29584_x309831306}[：消息中携带的用户数据值]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 received rib smooth start message]{lang="EN-US"}]{#struct_0_35947_29584_2049205889}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1287595702}[收到平滑开始的消息]{style="font-family:宋体"}

[[OSPFv3 received rib smooth end message]{lang="EN-US"}]{#struct_0_35947_29584_x401575468}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x50317236}[收到平滑结束的消息]{style="font-family:宋体"}

[[ OSPFv3 *process-id* triggered redistributed type *type*]{lang="EN-US"}]{#struct_0_35947_29584_x309896842}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x337061096}[进程触发路由引入]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x1013420789}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_35947_29584_1917959808}[：引入类型，]{style="font-family:
  宋体"}[0x1]{lang="EN-US"}[表示从]{style="font-family:宋体"}[RIB]{lang="EN-US"}[表引入，]{style="font-family:宋体"}[0x2]{lang="EN-US"}[表示从自身的引入表引入]{style="font-family:宋体"}

[[OSPFv3 received rib refresh message, instance: ]{lang="EN-US"}]{#struct_0_35947_29584_1783182395}*[instance-id]{lang="NO-BOK"}*[,]{lang="NO-BOK"}[ address: *addr*,]{lang="EN-US"}[ ]{lang="EN-US"}[user data: *user-data*, metric: *metric*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*]{lang="EN-US"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309962378}[实例收到普通路由刷新消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[instance-id]{lang="NO-BOK"}*]{#struct_0_35947_29584_x1827862388}[：路由所在]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_1607436415}[：该条路由的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[user-data]{lang="EN-US"}*]{#struct_0_35947_29584_1014434972}[：消息中携带的用户数据]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_127522570}[：该条路由的开销]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x309503626}[：该条路由所属的协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示直连路由，]{style="font-family:宋体"}[2]{lang="EN-US"}[表示静态路由，]{style="font-family:宋体"}[3]{lang="EN-US"}[表示]{style="font-family:宋体"}[ripng]{lang="EN-US"}[，]{style="font-family:宋体"}[4]{lang="EN-US"}[表示]{style="font-family:宋体"}[ospfv3]{lang="EN-US"}[，]{style="font-family:宋体"}[5]{lang="EN-US"}[表示]{style="font-family:宋体"}[isisv6]{lang="EN-US"}[，]{style="font-family:宋体"}[6]{lang="EN-US"}[表示]{style="font-family:宋体"}[bgp4+]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[subProtocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1823376218}[：该条路由的子协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_35947_29584_x1545789563}[：该条路由的下一跳个数]{style="font-family:
  宋体"}

[[OSPFv3 received rib change message, instance: ]{lang="EN-US"}]{#struct_0_35947_29584_82856413}*[instance-id]{lang="NO-BOK"}*[,]{lang="NO-BOK"}[ address: *addr*, user data: *user-data*, table ID: *table-id*, last protocol ID: *protocol-id*]{lang="EN-US"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309569162}[实例收到普通路由删除消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[instance-id]{lang="NO-BOK"}*]{#struct_0_35947_29584_2038106808}[：路由所在]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x2051334397}[：该条路由的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[user-data]{lang="EN-US"}*]{#struct_0_35947_29584_1576588190}[：消息中携带的用户数据]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[table-id]{lang="EN-US"}*]{#struct_0_35947_29584_x310027917}[：该条路由所在的路由表]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x355449261}[：该条路由上次上报时所属协议类型]{style="font-family:宋体"}

[[OSPFv3 *process-id* scanned redistributed route, nexthop: *nexthop*, interface index: *if-index*, vrfIndex: *vrfIndex*, process ID: *process-id2*, flag: *flag*]{lang="EN-US"}]{#struct_0_35947_29584_x820698420}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x717117840}[进程扫描特定进程的引入条目]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x310093453}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[nexthop]{lang="EN-US"}*]{#struct_0_35947_29584_22836195}[：下一条地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[if]{lang="EN-US"}[-index]{lang="EN-US"}*]{#struct_0_35947_29584_x842451175}[：出接口索引]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[vrfIndex]{lang="EN-US"}*]{#struct_0_35947_29584_423724526}[：转发表索引]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id2]{lang="EN-US"}*]{#struct_0_35947_29584_x310158989}[：引入条目所在的进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_35947_29584_1573222122}[：路由标志]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* processed redistributed route, address: *addr*, type: *type*, metric: *metric*, protocol ID: *protoco-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*, option: *option*, last option: *last-option*]{lang="EN-US"}]{#struct_0_35947_29584_x703324548}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x310224525}[进程处理引入的路由]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_6071397}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x184128663}[：路由]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_35947_29584_x1929797751}[：引入类型]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_x309765773}[：路由]{lang="EN-US" style="font-family:宋体"}[开销]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[protoco-id]{lang="EN-US"}*]{#struct_0_35947_29584_x669763445}[：该路由所属协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[subProtocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x790003909}[：该路由所属子协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_35947_29584_x309831309}[：下一]{lang="EN-US" style="font-family:宋体"}[跳]{style="font-family:宋体"}[个数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_2049795713}[：当前可选项]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[last-option]{lang="EN-US"}*]{#struct_0_35947_29584_x1261512348}[：原来可选项]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* added type-5 LSA to LSDB, address: *addr*, option: *option*, metric: *metric*, EFTBits: *EFTBits*, LsID: *lsid*]{lang="EN-US"}]{#struct_0_35947_29584_x309896845}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x337257704}[进程为引入的路由添加]{style="font-family:宋体"}[5]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x1368816608}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x309962381}[：引入路由的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x1827272551}[：可选项数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_297529287}[：路由]{lang="EN-US" style="font-family:宋体"}[开销]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[EFTBits]{lang="EN-US"}*]{#struct_0_35947_29584_1168511349}[：]{lang="EN-US" style="font-family:宋体"}[EFT]{lang="EN-US"}[标志位数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_35947_29584_x309503629}[：产生的]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[类]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Link State ID]{lang="EN-US"}

[[OSPFv3 *process-id* deleted type-5 LSA from LSDB, address: *addr*, option: *option*, EFTBits: *EFTBits*, LsID: *lsid*]{lang="EN-US"}]{#struct_0_35947_29584_x1824228186}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309569165}[进程删除由引入的路由生成的]{style="font-family:宋体"}[5]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_2038565560}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x1615871560}[：引入路由的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x310027916}[：可选项数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[EFTBits]{lang="EN-US"}*]{#struct_0_35947_29584_x355514797}[：]{lang="EN-US" style="font-family:宋体"}[EFT]{lang="EN-US"}[标志位数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_35947_29584_1931812871}[：产生的]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[类]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Link State ID]{lang="EN-US"}

[[OSPFv3 *process-id* added default-route LSA, option: *option*, metric: *metric*, LsID: *lsid*]{lang="EN-US"}]{#struct_0_35947_29584_x310093452}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_22901731}[添加默认路由]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_1352854205}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x310158988}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[前缀选项]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_1573287658}[：默认路由开销]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_35947_29584_x310224524}[：链路状态]{style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[OSPFv3 *process-id* deleted default-route LSA, option: *option*, LsID: *lsid*]{lang="EN-US"}]{#struct_0_35947_29584_6005861}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1863878635}[删除默认路由]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x309765772}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x669828981}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[前缀选项]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[lsid]{lang="EN-US"}*]{#struct_0_35947_29584_x796492553}[：链路状态]{style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[OSPFv3 *process-id* added prefix to routing table, address: *addr*, metric: *metric*, option: *option*, version: *version*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*, result: *result*]{lang="EN-US"}]{#struct_0_35947_29584_x309831308}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_2049861249}[进程添加引入的路由前缀到引入路由表]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x309896844}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x337192168}[：引入路由地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_513067840}[：引入路由的度量值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x309962380}[：引入路由的可选项数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[version]{lang="EN-US"}*]{#struct_0_35947_29584_x1827338087}[：引入路由的版本号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x309503628}[：所属协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[subProtocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1824293722}[：所属的子协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_35947_29584_x309569164}[：下一]{lang="EN-US" style="font-family:宋体"}[跳]{style="font-family:宋体"}[个数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[result]{lang="EN-US"}*]{#struct_0_35947_29584_2038500024}[：]{lang="EN-US" style="font-family:宋体"}[路由前缀添加结果，取值]{style="font-family:宋体"}[success]{lang="EN-US"}[表示添加成功，取值]{style="font-family:宋体"}[fail]{lang="EN-US"}[表示添加失败]{style="font-family:宋体"}

[[OSPFv3 *process-id* deleted prefix from routing table, address: *addr*, metric: *metric*, option: *option*, version: *version*, protocol ID: *protocol-id*, subProtocol ID: *subProtocol-id*, nexthop count: *count*]{lang="EN-US"}]{#struct_0_35947_29584_1877870779}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x310027919}[进程从引入路由表中删除指定前缀]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x354531757}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[addr]{lang="EN-US"}*]{#struct_0_35947_29584_x310093455}[：引入路由地址]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[metric]{lang="EN-US"}*]{#struct_0_35947_29584_22705123}[：引入路由的度量值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[option]{lang="EN-US"}*]{#struct_0_35947_29584_x310158991}[：引入路由的可选项数值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[version]{lang="EN-US"}*]{#struct_0_35947_29584_1573746411}[：引入路由的版本号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[protocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_434892870}[：所属协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[subProtocol-id]{lang="EN-US"}*]{#struct_0_35947_29584_x310224527}[：所属的子协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[count]{lang="EN-US"}*]{#struct_0_35947_29584_5940325}[：下一]{lang="EN-US" style="font-family:宋体"}[跳]{style="font-family:宋体"}[个数]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* queried rib route, instance: ]{lang="EN-US"}]{#struct_0_35947_29584_x309765775}*[instance-id]{lang="NO-BOK"}*[, protocol ID: *protocol-id*, synRt Fd: *fd*]{lang="EN-US"}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x669370229}[进程向路由管理查询指定实例的路由]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[process]{lang="EN-US"}*]{#struct_0_35947_29584_x309831311}*[-id]{lang="NO-BOK"}*[：]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[instance-id]{lang="NO-BOK"}*]{#struct_0_35947_29584_2049271424}[：进程所在的实例]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[protocol]{lang="EN-US"}*]{#struct_0_35947_29584_x309896847}*[-id]{lang="NO-BOK"}*[：需要查询的协议]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[fd]{lang="EN-US"}*]{#struct_0_35947_29584_x337388776}[：路由管理进程的文件描述符]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1435334895}

[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_1727013300}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[（]{style="font-family:宋体"}[1::1/64]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1::2/64]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[2]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[2]{lang="EN-US"}[，；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[2]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开引入路由调试信息开关，]{style="font-family:宋体"}[配置静态路由]{style="font-family:宋体"}[1::9/128]{lang="PT-BR"}[，并引入静态路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 redistribute]{lang="NO-BOK" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_35947_29584_x898264846}

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_463599595}

[[  OSPFv3 received rib batch start message, instance: 0, user data: 0x0.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x898330382}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1980782776}*[实例收到批处理开始的消息]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x1422121524}

[[  OSPFv3 received rib refresh message, instance: 0,address: 1::9/128,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_523819254}

[[user data: 0x0, metric: 0, protocol ID: 2, subProtocol ID: 0,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897740559}

[[nexthop count: 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_35947_29584_x2009913787}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_988289811}*[实例收到普通路由刷新消息]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897806095}

[[  OSPFv3 1 scanned redistributed route, nexthop: ::, interface index: 273,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x2031415322}

[[vrfIndex: 0, process 0, flag: 0x10000.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_1170989972}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x175823032}*[进程扫描特定进程的引入条目]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897609487}

[[  OSPFv3 1 processed redistributed route, address: 1::9/128, type: 1,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_1545800956}

[[metric: 0, protocol ID: 2, subProtocol ID: 0, nexthop count: 1,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_140788434}

[[option: 0x4, last option: 0x0.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_340587858}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x309569167}*[进程处理引入的路由]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897675023}

[[  OSPFv3 1 added type-5 LSA to LSDB, address: 1::9/128, option:0x0,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_692683830}

[[metric: 1, EFTBits: 0x4, LsID: 0.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897478415}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_103000688}*[进程为引入的路由添加]{style="font-family:宋体"}[5]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x25067188}

[[  OSPFv3 1 added prefix]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_35947_29584_x897543951}[to routing table, address: 1::9/128, metric:0,]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\""}

[[option: 0x4, version: 1, protocol ID: 2, subProtocol ID: 0,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_687917114}

[[nexthop count: 1, result: success.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_35947_29584_1812177546}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x354597293}*[进程添加引入的路由前缀到引入路由表]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897347343}

[[  OSPFv3 received rib batch end message, instance: 0, user data: 0x0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_35947_29584_1101699683}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_572365739}*[实例收到批处理结束的消息]{style="font-family:宋体"}*

[[\*Nov  5 16:21:06:547 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x897412879}

[[  OSPFv3 1 triggered redistributed type 0x2.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_1474051316}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1322761680}*[进程触发路由引入]{style="font-family:宋体"}*

[[\*Nov  5 16:21:07:573 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x898264847}

[[  OSPFv3 1 scanned redistributed route, nexthop: ::, interface index: 273,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_463534059}

[[vrfIndex: 0, process Id: 0, flag: 0x10000.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x200933375}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x120618310}*[进程扫描特定进程的引入条目]{style="font-family:宋体"}*

[[\*Nov  5 16:21:07:573 2012 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x898330383}

[[  OSPFv3 1 processed redistributed route, address: 1::9/128,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x1422055988}

[[redistribute type: 2, metric: 0, protocol ID: 2, subProtocol ID: 0,]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_668343387}

[[nexthop count: 1, option: 0x4, last option: 0x4.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_35947_29584_x1622547354}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_22164086}*[进程处理引入的路由]{style="font-family:宋体"}*

::: {#1925865504 .myid}
[]{#_Toc404788849}[]{#struct_0_35947_29584_x1636656669}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 spf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_x310158990}

[**[debugging ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **tree** }]{lang="EN-US"}]{#struct_0_35947_29584_1573811947}

[**[undo debugging ospfv3]{lang="EN-US"}**[ \[ *process-id* \] **spf** { **all** \| **asbr** \| **brief** \| **external** \| **internal** \| **tree** }]{lang="EN-US"}]{#struct_0_35947_29584_x1840398489}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_774362921}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_1998996125}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_x69123910}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_x1751905265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_x339804065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x16183127}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x310224526}[：]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_35947_29584_5874789}[：表示全部]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_35947_29584_684067674}[：表示]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_35947_29584_1375889797}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算概要调试信息开关。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_35947_29584_879958675}[：表示]{style="font-family:宋体"}[AS]{lang="EN-US"}[外]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算的调试信息开关。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_35947_29584_x978822365}[：表示]{style="font-family:宋体"}[AS]{lang="EN-US"}[内]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[**[tree]{lang="EN-US"}**]{#struct_0_35947_29584_426896439}[：表示区域内]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_x154267677}

[**[debugging ospfv3 route]{lang="EN-US"}**]{#struct_0_35947_29584_x1024212573}[命令用来打开]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}**[undo debugging ospfv3 route]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_35947_29584_x309765774}[路由计算调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x669435765}[进程的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[路由计算调试信息开关。]{style="font-family:宋体"}

[[表1-15 ]{lang="EN-US"}[debugging ospfv3 spf]{lang="EN-US"}]{#struct_0_35947_29584_x1594070960}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_347190705}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_1189327748}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_863950178}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_1075362235}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1532027293}[进程号]{style="font-family:宋体"}

[[Area *area-id*]{lang="EN-US"}]{#struct_0_35947_29584_x309831310}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_35947_29584_2049336960}

[[OSPFv3 *process-id* Schedule event: *sch-event* at *time-stamp* ms.]{lang="EN-US"}]{#struct_0_35947_29584_1066236686}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x254865496}[进程计算调度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sch-event]{lang="EN-US"}*]{#struct_0_35947_29584_587115533}[：调度类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_x309896846}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Schedule flag : *sch-flag* SPF is scheduled.]{lang="EN-US"}]{#struct_0_35947_29584_x337323240}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x241740079}[进程计算调度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sch-flag]{lang="EN-US"}*]{#struct_0_35947_29584_x477032080}[：调度标记]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Schedule event: *sch-event* SPF is stopped, at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_x1925125431}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309962382}[进程计算调度停止]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sch-event]{lang="EN-US"}*]{#struct_0_35947_29584_x1827469159}[：调度类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_91493346}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Pre flag : Schedule: *sch-flag*.]{lang="EN-US"}]{#struct_0_35947_29584_x2041355624}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x312688867}[进程计算前次调度标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sch-flag]{lang="EN-US"}*]{#struct_0_35947_29584_x309503630}[：调度标记]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Now flag : Running : *sch-flag*.]{lang="SV"}]{#struct_0_35947_29584_x1823769433}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x717107453}[进程计算当前调度标记]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[sch-flag]{lang="EN-US"}*]{#struct_0_35947_29584_x622704977}[：调度标记]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* Rebuilding Spf Tree for Area *area-id*, at *time-stamp* ms. \*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_1790258959}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x309569166}[进程重新构造区域的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_2038368952}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* SPF Full Schedule]{lang="EN-US"}]{#struct_0_35947_29584_1794026698}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_456671707}[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[计算调度]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF route calculation is running, it have to be stopped]{lang="EN-US"}]{#struct_0_35947_29584_1612286386}

[[停止]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_163180180}[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF running stop for inactive process state]{lang="EN-US"}]{#struct_0_35947_29584_865574775}

[[停止]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x2023223722}[进程]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算，进程状态无效]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF Initial running flag]{lang="EN-US"}]{#struct_0_35947_29584_x1345084147}

[[初始化]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612220850}[进程运行标记]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF Stop Schedule for process reset]{lang="EN-US"}]{#struct_0_35947_29584_x926939797}

[[停止]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1751508167}[进程]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算，进程重置]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF building SPT begins at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_x1991054952}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612155314}[进程开始构造]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_x1372298539}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* SPF building SPT ends at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_705367688}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_508907195}[进程结束构造]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_1612089778}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Router route calculation begins at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_157627752}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x204833715}[进程开始路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_1612548530}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Router route calculation ends at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_x1758025382}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1002672336}[进程结束路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_1502451777}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* ASBR route calculation begins at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_1612482994}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_220732275}[进程开始]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_546844043}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* ASBR route calculation ends at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_1612417458}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1734182600}[进程结束]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_x740322434}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Internal route calculation begins at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_615327699}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612351922}[进程开始域内路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_x1315008342}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Internal route calculation ends at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_1309908730}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612810674}[进程结束域内路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_213451811}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* External route calculation begins at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_x803426924}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612745138}[进程开始域外路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_x1753390447}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* External route calculation ends at *time-stamp* ms]{lang="EN-US"}]{#struct_0_35947_29584_x2060668448}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612286387}[进程结束域外路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-stamp]{lang="EN-US"}*]{#struct_0_35947_29584_163114644}[：时间戳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF starts(incremental internal routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_1612220851}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x927005333}[进程开始域内增量路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF ends(incremental internal routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_x1272536412}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612155315}[进程结束域内增量路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF starts(incremental external routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_x1372233003}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1364139011}[进程开始域外增量路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF ends(incremental external routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_1612089779}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_157562216}[进程结束域外增量路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF starts(full internal routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_1612548531}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1758090918}[进程开始域内完全路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF ends(full internal routes)\*\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_1026280507}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612482995}[进程结束域内完全路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF starts(full external routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_220666739}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612417459}[进程开始域外完全路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* \*\*\*\* SPF ends(full external routes)\*\*\*\*]{lang="EN-US"}]{#struct_0_35947_29584_x1734117064}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1249262463}[进程结束域外完全路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* Add root to candidate list of area *area-id*]{lang="EN-US"}]{#struct_0_35947_29584_1612351923}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1314942806}[进程为区域候选列表添加根节点]{style="font-family:宋体"}

[[OSPFv3 *process-id* Candidate list empty, SPF area *area-id* finished.]{lang="EN-US"}]{#struct_0_35947_29584_1612810675}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_213517347}[进程候选列表为空，]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算结束]{style="font-family:宋体"}

[[OSPFv3 *process-id* SPF node *spf-node*, Type:*node-type*, Advertising source:*router-id*, LS ID:*ls-id*]{lang="EN-US"}]{#struct_0_35947_29584_774929613}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612745139}[进程添加]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[spf-node]{lang="EN-US"}*]{#struct_0_35947_29584_x1753455983}[：]{style="font-family:宋体"}[SPF]{lang="EN-US"}[节点号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[router-id]{lang="EN-US"}*]{#struct_0_35947_29584_1612286384}[：发布源路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-id]{lang="EN-US"}*]{#struct_0_35947_29584_163049108}[：链路状态]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPFv3 *process-id* SPF link *spf-link*, Type:*link-type*, Advertising source: *router-id*,, LS ID: *ls-id* ]{lang="EN-US"}]{#struct_0_35947_29584_1612220848}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x926415510}[进程添加]{style="font-family:宋体"}[SPF Link]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[spf-link]{lang="EN-US"}*]{#struct_0_35947_29584_x525098106}[：]{lang="EN-US" style="font-family:宋体"}[SPFLink]{lang="EN-US"}[号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[router-id]{lang="EN-US"}*]{#struct_0_35947_29584_1612155312}[：发布源路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ls-id]{lang="EN-US"}*]{#struct_0_35947_29584_x1372691755}[：链路状态]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[OSPFv3 *process-id* SPF calculating route to ASBR, Destination ID *router-id*]{lang="EN-US"}]{#struct_0_35947_29584_1612089776}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_158020968}[进程计算]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[router-id]{lang="EN-US"}*]{#struct_0_35947_29584_1612548528}[：]{lang="EN-US" style="font-family:宋体"}[目的路由器]{lang="EN-US" style="font-family:宋体"}[ID]{lang="FR"}

[[OSPFv3 *process-id* Del Asbr route,because *value*]{lang="EN-US"}]{#struct_0_35947_29584_x1758549669}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612482992}[进程删除]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[value]{lang="EN-US"}*]{#struct_0_35947_29584_221125491}[：原因码]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Incremental ASBR routes calculation begins]{lang="EN-US"}]{#struct_0_35947_29584_1612417456}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1735100104}[进程开始增量]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* Incremental ASBR routes calculation ends]{lang="EN-US"}]{#struct_0_35947_29584_1612351920}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1314877270}[进程结束增量]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[OSPFv3 *process-id* Delete old route. Outgoing interface: *interface-id*, Nexthop: *next-hop*]{lang="EN-US"}]{#struct_0_35947_29584_1612810672}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_213582883}[进程删除路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-id]{lang="EN-US"}*]{#struct_0_35947_29584_414035053}[：接口]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[next-hop]{lang="EN-US"}*]{#struct_0_35947_29584_1612745136}[：下一跳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Cannot find valid nexthop for current advertising source.]{lang="EN-US"}]{#struct_0_35947_29584_x1752472943}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612286385}[进程找不到有效下一跳]{style="font-family:宋体"}

[[OSPFv3 *process-id* No advertising sourc]{lang="EN-US"}]{#struct_0_35947_29584_1612220849}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x926481046}[进程无发布源]{style="font-family:宋体"}

[[OSPFv3 *process-id* Don\'t calculate for active internal route.]{lang="EN-US"}]{#struct_0_35947_29584_1612155313}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1372626219}[进程不计算域内路由]{style="font-family:宋体"}

[[OSPFv3 *process-id* Add new route. Outgoing interface:*interface-id*, Nexthop:*next-hop*]{lang="EN-US"}]{#struct_0_35947_29584_1612089777}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_157955432}[进程下发路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-id]{lang="EN-US"}*]{#struct_0_35947_29584_1612548529}[：接口]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[next-hop]{lang="EN-US"}*]{#struct_0_35947_29584_x1758615205}[：下一跳]{lang="EN-US" style="font-family:宋体"}

[[OSPFv3 *process-id* Update old route. Outgoing interface: *interface-id*, Nexthop: *next-hop*]{lang="EN-US"}]{#struct_0_35947_29584_1612482993}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_221059955}[进程更新路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[interface-id]{lang="EN-US"}*]{#struct_0_35947_29584_1612417457}[：接口]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[next-hop]{lang="EN-US"}*]{#struct_0_35947_29584_x1735034568}[：下一跳]{lang="EN-US" style="font-family:宋体"}

[[OSPF *process-id* Fail to add route to RM rib]{lang="EN-US"}]{#struct_0_35947_29584_1612351921}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1314811734}[进程下发路由失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_x142343614}

[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_1612810673}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::1/64]{lang="EN-US"}[）与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[（]{style="font-family:宋体"}[1001::2/64]{lang="EN-US"}[）相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[1]{lang="EN-US"}[。在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开路由计算概要调试信息开关。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 spf brief]{lang="EN-US"}]{#struct_0_35947_29584_213648419}

[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule event: 0x00000001 at 69879924 ms.]{lang="EN-US"}

[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule flag : 0x00000001 SPF is scheduled.]{lang="EN-US"}

[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 SPF Full Schedule]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1062352555}*[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[计算调度]{style="font-family:宋体"}*

[[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1601781026}

[  OSPFv3 1 SPF route calculation is running, it have to be stopped]{lang="EN-US"}

[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule event: 0x00000000 SPF is stopped, at 69879924 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1779460063}*[停止]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1612745137}

[  OSPFv3 1 Schedule event: 0x00000020 at 69879924 ms.]{lang="EN-US"}

[\*Apr 21 10:51:06:924 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule flag : 0x00000020 SPF is scheduled.]{lang="EN-US"}

[\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule event: 0x00000001 at 69879925 ms.]{lang="EN-US"}

[\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 SPF Full Schedule]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1752538479}*[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[计算调度]{style="font-family:宋体"}*

[[\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1608038973}

[  OSPFv3 1 SPF route calculation is running, it have to be stopped]{lang="EN-US"}

[\*Apr 21 10:51:06:925 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 Schedule event: 0x000000A7 SPF is stopped, at 69879925 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1792567978}*[停止]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[FULL]{lang="EN-US"}[路由计算]{style="font-family:宋体"}*

[[\...\...]{lang="NO-BOK"}]{#struct_0_35947_29584_794911103}

[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[  OSPFv3 1 SPF Initial running flag]{lang="NO-BOK"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x204103985}*[初始化]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程运行标记]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1612286382}

[  OSPFv3 1 Pre flag : Schedule: 0x00000000.]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_163442324}*[进程计算前次调度标记]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1363703507}

[  OSPFv3 1 Now flag : Running : 0x000000A7.]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1505201878}*[进程计算当前调度标记]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_2055610283}

[  OSPFv3 1 SPF building SPT begins at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1893931210}*[进程开始构造]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1750786796}

[  OSPFv3 1 \*\*\*\* Rebuilding Spf Tree for Area 0.0.0.1, at 69888240 ms. \*\*\*\*]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1612220846}*[进程重新构造区域的]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x927333014}

[  OSPFv3 1 SPF building SPT ends at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_648568521}*[进程结束构造]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x130703409}

[  OSPFv3 1 Router route calculation begins at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x2064820399}*[进程开始路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x2083971924}

[  OSPFv3 1 Router route calculation ends at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1008029864}*[进程结束路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1612155310}

[  OSPFv3 1 ASBR route calculation begins at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1372560683}*[进程开始]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1078805488}

[  OSPFv3 1 ASBR route calculation ends at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x95307642}*[进程结束]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1195756027}

[  OSPFv3 1 Internal route calculation begins at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x2047333177}*[进程开始域内路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_577915105}

[  OSPFv3 1 \*\*\*\* SPF starts(full internal routes)\*\*\*\*]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1283870909}*[进程开始域内完全路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1612089774}

[  OSPFv3 1 \*\*\*\* SPF ends(full internal routes)\*\*\*\*\*]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_157889896}*[进程结束域内完全路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_11898668}

[  OSPFv3 1 Internal route calculation ends at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x2112532253}*[进程结束域内路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1027451000}

[  OSPFv3 1 External route calculation begins at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1867312477}*[进程开始域外路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1094794532}

[  OSPFv3 1 \*\*\*\* SPF starts(full external routes)\*\*\*\*]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_1612548526}*[进程开始域外完全路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1757632165}

[  OSPFv3 1 \*\*\*\* SPF ends(full external routes)\*\*\*\*]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x610068231}*[进程结束域外完全路由计算]{style="font-family:宋体"}*

[[\*Apr 21 10:51:15:240 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_317093523}

[  OSPFv3 1 External route calculation ends at 69888240 ms]{lang="EN-US"}

[*[// OSPFv3]{lang="EN-US"}*]{#struct_0_35947_29584_x1084847822}*[进程结束域外路由计算]{style="font-family:宋体"}*

::: {#-1235957857 .myid}
[]{#_Toc404788850}[]{#struct_0_35947_29584_x128538691}[]{#_Toc303674579}[]{#_Toc303084514}

**OSPFv3 \-- OSPFv3调试命令 \-- debugging ospfv3 timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_35947_29584_x429021670}

[**[debugging]{lang="EN-US"}**[ **ospfv3** \[ *process-id* \] **timer** \[ **lsa-generate** \| **spf** \]]{lang="EN-US"}]{#struct_0_35947_29584_x880577268}

[**[undo debugging ospfv3 ]{lang="EN-US"}**[\[ *process-id* \] **timer** \[ **lsa-generate** \| **spf** \]]{lang="EN-US"}]{#struct_0_35947_29584_1612482990}

[[【视图】]{style="font-family:黑体"}]{#struct_0_35947_29584_220994419}

[[用户视图]{style="font-family:宋体"}]{#struct_0_35947_29584_1472391299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_35947_29584_1823522952}

[[network-admin]{lang="EN-US"}]{#struct_0_35947_29584_x1989927824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_35947_29584_x30260255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_35947_29584_x222164879}

[*[process-id]{lang="EN-US"}*]{#struct_0_35947_29584_x266588572}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsa-generate]{lang="EN-US"}**]{#struct_0_35947_29584_1998093392}[：表示]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器调试信息开关。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_35947_29584_1612417454}[：表示]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_35947_29584_x1734969032}

[**[debugging ospfv3 timer]{lang="EN-US"}**]{#struct_0_35947_29584_1315361820}[命令用来打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}**[undo debugging ospfv3 timer]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1766625455}[定时器调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果未指定进程号，则打开所有]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_293116557}[进程的定时器调试信息开关。]{style="font-family:宋体"}

[[表1-16 ]{lang="EN-US"}[debugging ospfv3 timer lsa-generate]{lang="EN-US"}]{#struct_0_35947_29584_1976811819}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_368052513}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_1039777635}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_x1627605268}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_1612351918}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_x1315401557}[进程号]{style="font-family:宋体"}

[[Create LS timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_35947_29584_1123083783}

[[创建]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_1932235177}[生成定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Delete LS timer]{lang="EN-US"}]{#struct_0_35947_29584_x1679765929}

[[删除]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_x408009933}[生成定时器]{style="font-family:宋体"}

[[Restart LS timer]{lang="EN-US"}]{#struct_0_35947_29584_1612810670}

[[启动]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_35947_29584_213713955}[生成定时器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[debugging ospfv3 timer spf]{lang="EN-US"}]{#struct_0_35947_29584_671758449}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_367677258}[[字段]{style="font-family:黑体"}]{#struct_0_35947_29584_x1012025025}

[[描述]{style="font-family:黑体"}]{#struct_0_35947_29584_269806540}

[[OSPFv3 *process-id*]{lang="EN-US"}]{#struct_0_35947_29584_x1167152644}

[[OSPFv3]{lang="EN-US"}]{#struct_0_35947_29584_1612745134}[进程号]{style="font-family:宋体"}

[[Create SPF timer, timeout value is *x* ms]{lang="EN-US"}]{#struct_0_35947_29584_x1752604015}

[[创建]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_35947_29584_x454688702}[计算定时器，超时时间]{style="font-family:宋体"}*[x]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Delete SPF timer]{lang="EN-US"}]{#struct_0_35947_29584_x797534301}

[[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_35947_29584_x439027599}[计算定时器]{style="font-family:宋体"}

[[Restart SPF timer]{lang="EN-US"}]{#struct_0_35947_29584_x327777323}

[[启动]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_35947_29584_1612286383}[计算定时器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_35947_29584_163376788}

[[\# Router A]{lang="EN-US"}]{#struct_0_35947_29584_x16468240}[通过]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[相连，网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中创建区域]{style="font-family:宋体"}[0]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上创建]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[功能并配置其属于区域]{style="font-family:宋体"}[0]{lang="EN-US"}[；在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[定时器调试信息开关并重启]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<RouterA\> debugging ospfv3 timer]{lang="EN-US"}]{#struct_0_35947_29584_840370876}

[\*Sep  5 20:44:36:990 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}

[OSPFv3 1 Delete SPF timer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x1382358462}*[删除]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器]{style="font-family:宋体"}*

[[\*Sep  5 20:44:36:991 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x704591135}

[OSPFv3 1 Create SPF timer,timeout value is 5000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_135816670}*[创建]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器]{style="font-family:宋体"}*

[[\*Sep  6 20:33:42:647 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_1612220847}

[OSPFv3 1 Restart SPF timer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x927398550}*[重置]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算定时器]{style="font-family:宋体"}*

[[\*Sep  5 07:33:36:990 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1682528812}

[OSPFv3 1 Delete LS timer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_530170679}*[删除]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器]{style="font-family:宋体"}*

[[\*Sep  6 07:34:40:647 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x1675297604}

[OSPFv3 1 Create LS timer,timeout value is 5000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_x830645334}*[创建]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器，超时时间]{style="font-family:宋体"}[5000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[[\*Sep  6 07:35:41:449 2011 RouterA OSPFV3/7/OSPFV3DEBUG: -MDC=1;]{lang="EN-US"}]{#struct_0_35947_29584_x2133353525}

[OSPFv3 1 Restart LS timer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_35947_29584_1612155311}*[重置]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
