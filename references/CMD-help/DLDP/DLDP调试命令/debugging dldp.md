::: {#1573760459 .myid}
[]{#_Toc404795511}[]{#struct_0_x1118_13379_566964011}

**DLDP \-- DLDP调试命令 \-- debugging dldp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1968356466}

[**[debugging dldp]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **timer** \| { **fsm** \| **packet** } \[ **interface** *interface-type* *interface-number* \] }]{lang="EN-US"}]{#struct_0_x1118_13379_1493426680}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1118_13379_1324892519}**[debugging dldp]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **all** \| **error** \| **event** \| **timer** \| { **fsm** \| **packet** } \[ **interface** *interface-type* *interface-number* \] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1118_13379_x695722995}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1118_13379_x822723304}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1634760269}

[[network-admin]{lang="EN-US"}]{#struct_0_x1118_13379_x1168055050}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1118_13379_631659262}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1118_13379_1170931107}

[**[all]{lang="EN-US"}**]{#struct_0_x1118_13379_x690438331}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1118_13379_191988047}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[错误报文调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1118_13379_x1809578974}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1118_13379_967003622}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x1118_13379_x1702228430}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1118_13379_x1686969696}[：表示]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x1118_13379_x1635743309}[：表示指定接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[调试信息开关，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。如果未指定本参数，则表示所有接口的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1175924466}

[**[debugging dldp]{lang="EN-US"}**]{#struct_0_x1118_13379_x1391320446}[命令用来打开]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging dldp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DLDP]{lang="EN-US"}]{#struct_0_x1118_13379_x1043288439}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging dldp error]{lang="EN-US"}]{#struct_0_x1118_13379_1268827291}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1329930815}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_13379_1410499336}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_13379_37762271}

[[Port *port-name* received an error packet]{lang="EN-US"}]{#struct_0_x1118_13379_x903844851}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_1581761613}[收到了一个错误报文]{style="font-family:宋体"}

[[Reason types of the error packet]{lang="EN-US"}]{#struct_0_x1118_13379_x1635677773}

[[报文的错误类型：]{style="font-family:宋体"}]{#struct_0_x1118_13379_x347004613}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LENGTH ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_947273213}[：表示报文长度错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DLDP NOT ENABLE]{lang="EN-US"}]{#struct_0_x1118_13379_x904971289}[：表示]{lang="EN-US" style="font-family:
  宋体"}[DLDP]{lang="EN-US"}[未使能]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CURRENT STATE CAN\'T RECEIVE PACKET]{lang="EN-US"}]{#struct_0_x1118_13379_x1673435542}[：表示]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[当前状态]{lang="EN-US" style="font-family:宋体"}[下]{style="font-family:宋体"}[不能接收报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROTOCOL ID ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x1360489361}[：表示报文协议号错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VERSION ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x507597063}[：表示报文版本号错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INTERVAL ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x1635219024}[：表示报文中通告时间间隔错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTHTYPE ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x619567387}[：表示报文的认证类型错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PASSWORD ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x993638624}[：表示报文的认证密码错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LOOP PACKET]{lang="EN-US"}]{#struct_0_x1118_13379_387940749}[：表示是自环报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PACKET TYPE ERROR]{lang="EN-US"}]{#struct_0_x1118_13379_x1704561657}[：表示报文类型错误]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging dldp event]{lang="EN-US"}]{#struct_0_x1118_13379_394992425}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1333444037}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_13379_x574789690}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1635153488}

[[Port *port-name* down/up]{lang="EN-US"}]{#struct_0_x1118_13379_x741987655}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_x2088842586}[发生物理]{style="font-family:宋体"}[down/up]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging dldp timer]{lang="EN-US"}]{#struct_0_x1118_13379_1863088800}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1332415967}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1713459468}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_13379_888237260}

[[Port *port-name* created a delaydown/recover-probe timer]{lang="EN-US"}]{#struct_0_x1118_13379_1219209254}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_811152807}[上建立了]{style="font-family:宋体"}[delaydown/recover-probe]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[Port *port-name* created an advertisement timer]{lang="EN-US"}]{#struct_0_x1118_13379_x1635087952}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_1915789713}[上建立了]{style="font-family:宋体"}[advertisement]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[The advertisement/delaydown/recover-probe timer of port *port-name* timed out]{lang="EN-US"}]{#struct_0_x1118_13379_x1183304446}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_42724143}[下的]{style="font-family:宋体"}[advertisement/delaydown/recover-probe]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[Neighbor BridgeMAC]{lang="EN-US"}]{#struct_0_x1118_13379_524220183}

[[邻居桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1118_13379_211330988}[地址]{style="font-family:宋体"}

[[Neighbor PortIndex]{lang="EN-US"}]{#struct_0_x1118_13379_1990338630}

[[邻居接口索引]{style="font-family:宋体"}]{#struct_0_x1118_13379_2101523451}

[[The neighbor of port *port-name* created a probe timer]{lang="EN-US"}]{#struct_0_x1118_13379_x1635022416}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_905572698}[下的邻居建立了]{style="font-family:宋体"}[probe]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[The neighbor of port *port-name* created an aged/echo timer]{lang="EN-US"}]{#struct_0_x1118_13379_x1555462370}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_2141653299}[下的邻居建立了]{style="font-family:宋体"}[aged/echo]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[The neighbor's aged/echo/probe timer of port *port-name* timed out]{lang="EN-US"}]{#struct_0_x1118_13379_1397998325}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_1448456876}[下邻居的]{style="font-family:宋体"}[aged/echo/probe]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging dldp fsm]{lang="EN-US"}]{#struct_0_x1118_13379_x1634956880}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1326369721}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1783921148}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_13379_21118478}

[[Port *port-name* added/deleted a neighbor]{lang="EN-US"}]{#struct_0_x1118_13379_x1961989734}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_1256490917}[增加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除了一个邻居]{style="font-family:宋体"}

[[A state transition occurred to the neighbor of port *port-name*]{lang="EN-US"}]{#struct_0_x1118_13379_1644635276}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_x979114563}[上有邻居进行状态迁移]{style="font-family:宋体"}

[[Neighbor BridgeMAC]{lang="EN-US"}]{#struct_0_x1118_13379_1606997090}

[[邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1118_13379_x1634891344}[地址]{style="font-family:宋体"}

[[Neighbor PortIndex]{lang="EN-US"}]{#struct_0_x1118_13379_x582883539}

[[邻居的接口索引]{style="font-family:宋体"}]{#struct_0_x1118_13379_602329301}

[[Neighbor state]{lang="EN-US"}]{#struct_0_x1118_13379_x197561365}

[[邻居的状态：]{style="font-family:宋体"}]{#struct_0_x1118_13379_x763580051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNCONFIRMED]{lang="EN-US"}]{#struct_0_x1118_13379_x961273561}[：表示未确认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONFIRMED]{lang="EN-US"}]{#struct_0_x1118_13379_x1634825808}[：表示确认状态]{lang="EN-US" style="font-family:宋体"}

[[Neighbor state transition: *state1* \--\> *state2*]{lang="EN-US"}]{#struct_0_x1118_13379_1025324507}

[[邻居的状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_x1118_13379_883188119}[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，状态包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNCONFIRMED]{lang="EN-US"}]{#struct_0_x1118_13379_1003535114}[：表示未确认状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONFIRMED]{lang="EN-US"}]{#struct_0_x1118_13379_x1078891953}[：表示确认状态]{lang="EN-US" style="font-family:宋体"}

[[Port *port-name* state transition: *state1* \--\> *state2*]{lang="EN-US"}]{#struct_0_x1118_13379_x1634760272}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_x1927635473}[的状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，状态包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INITIAL]{lang="EN-US"}]{#struct_0_x1118_13379_986351987}[：表示初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INACTIVE]{lang="EN-US"}]{#struct_0_x1118_13379_1003438351}[：表示非活动状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNIDIRECTIONAL]{lang="EN-US"}]{#struct_0_x1118_13379_x1864710087}[：表示单通状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BIDIRECTIONAL]{lang="EN-US"}]{#struct_0_x1118_13379_829571796}[：表示双通状态]{lang="EN-US" style="font-family:宋体"}

[[Stimulation]{lang="EN-US"}]{#struct_0_x1118_13379_x1635743312}

[[激励条件：]{style="font-family:宋体"}]{#struct_0_x1118_13379_746324299}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DLDP enable]{lang="EN-US"}]{#struct_0_x1118_13379_969155393}[：表示使能]{lang="EN-US" style="font-family:宋体"}[DLDP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DLDP disable]{lang="EN-US"}]{#struct_0_x1118_13379_211490913}[：表示关闭]{lang="EN-US" style="font-family:宋体"}[DLDP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port down]{lang="EN-US"}]{#struct_0_x1118_13379_x1635677776}[：表示接口物理]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Port up]{lang="EN-US"}]{#struct_0_x1118_13379_x750289140}[：表示接口物理]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No confirmed neighbor]{lang="EN-US"}]{#struct_0_x1118_13379_x460840417}[：表示没有确认邻居]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confirmed neighbor]{lang="EN-US"}]{#struct_0_x1118_13379_1861099975}[：表示有确认邻居]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging dldp packet]{lang="EN-US"}]{#struct_0_x1118_13379_x1584847980}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1088017109}[[字段]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1533893451}

[[描述]{style="font-family:黑体"}]{#struct_0_x1118_13379_x1635219023}

[[Port *port-name* sent/received a DLDP packet]{lang="EN-US"}]{#struct_0_x1118_13379_1302746914}

[[接口]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*]{#struct_0_x1118_13379_1350307008}[发送]{style="font-family:宋体"}[/]{lang="EN-US"}[收到了一个]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Following is the content of the packet]{lang="EN-US"}]{#struct_0_x1118_13379_x2081491721}

[[该报文的具体内容如下]{style="font-family:宋体"}]{#struct_0_x1118_13379_x1440775879}

[[DLDP ID]{lang="EN-US"}]{#struct_0_x1118_13379_324260703}

[[报文中携带的协议号]{style="font-family:宋体"}]{#struct_0_x1118_13379_x1747716976}

[[DLDP version ID]{lang="EN-US"}]{#struct_0_x1118_13379_x1635153487}

[[报文中携带的版本号]{style="font-family:宋体"}]{#struct_0_x1118_13379_824096286}

[[DLDP packet type]{lang="EN-US"}]{#struct_0_x1118_13379_342521174}

[[报文类型：]{style="font-family:宋体"}]{#struct_0_x1118_13379_1742577587}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADVERTISEMENT]{lang="EN-US"}]{#struct_0_x1118_13379_x683279309}[：表示]{lang="EN-US" style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PROBE]{lang="EN-US"}]{#struct_0_x1118_13379_x2000481270}[：表示]{lang="EN-US" style="font-family:宋体"}[Probe]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ECHO]{lang="EN-US"}]{#struct_0_x1118_13379_x1635087951}[：表示]{lang="EN-US" style="font-family:宋体"}[Echo]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADVERTISEMENT-RSY]{lang="EN-US"}]{#struct_0_x1118_13379_349705772}[：表示]{lang="EN-US" style="font-family:
  宋体"}[RSY]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADVERTISEMENT-FLUSH]{lang="EN-US"}]{#struct_0_x1118_13379_x429472572}[：表示]{lang="EN-US" style="font-family:
  宋体"}[Flush]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DISABLE]{lang="EN-US"}]{#struct_0_x1118_13379_x866194797}[：表示]{lang="EN-US" style="font-family:宋体"}[Disable]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LINKDOWN]{lang="EN-US"}]{#struct_0_x1118_13379_1446245158}[：表示]{lang="EN-US" style="font-family:宋体"}[LinkDown]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECOVER-PROBE]{lang="EN-US"}]{#struct_0_x1118_13379_x1635022415}[：表示]{lang="EN-US" style="font-family:宋体"}[RecoverProbe]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECOVER-ECHO]{lang="EN-US"}]{#struct_0_x1118_13379_1308857225}[：表示]{lang="EN-US" style="font-family:宋体"}[RecoverEcho]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ILLEGAL]{lang="EN-US"}]{#struct_0_x1118_13379_x279674699}[：表示非法报文]{lang="EN-US" style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x1118_13379_x404302540}

[[报文]{style="font-family:宋体"}[RSY]{lang="EN-US"}]{#struct_0_x1118_13379_1645152207}[标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO-RSY]{lang="EN-US"}]{#struct_0_x1118_13379_x1634956879}[：表示该报文是普通]{lang="EN-US" style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSY]{lang="EN-US"}]{#struct_0_x1118_13379_1300995959}[：表示该报文是]{style="font-family:宋体"}[RSY]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FLUSH]{lang="EN-US"}]{#struct_0_x1118_13379_648702415}[：表示该报文是]{lang="EN-US" style="font-family:宋体"}[Flush]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO-FLAG]{lang="EN-US"}]{#struct_0_x1118_13379_x1004852138}[：表示当前的报文类型不关心]{lang="EN-US" style="font-family:宋体"}[Flag]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ILLEGAL]{lang="EN-US"}]{#struct_0_x1118_13379_1657227361}[：表示非法标记]{lang="EN-US" style="font-family:宋体"}

[[Authentication mode]{lang="EN-US"}]{#struct_0_x1118_13379_1008923927}

[[报文认证方式：]{style="font-family:宋体"}]{#struct_0_x1118_13379_x1634891343}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_x1118_13379_1339430762}[：表示不认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SIMPLE]{lang="EN-US"}]{#struct_0_x1118_13379_x422439787}[：表示明文认证方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x1118_13379_x105702701}[：表示]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ILLEGAL]{lang="EN-US"}]{#struct_0_x1118_13379_x1790048177}[：标识非法的认证模式]{lang="EN-US" style="font-family:宋体"}

[[Authentication password]{lang="EN-US"}]{#struct_0_x1118_13379_x1634825807}

[[报文认证密码]{style="font-family:宋体"}]{#struct_0_x1118_13379_1784839394}

[[Interval of sending Advertisement packet]{lang="EN-US"}]{#struct_0_x1118_13379_1929922101}

[[报文中携带的发送]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}]{#struct_0_x1118_13379_471866351}[报文时间间隔（单位为秒）]{style="font-family:宋体"}

[[HostBridgeMAC]{lang="EN-US"}]{#struct_0_x1118_13379_x1634760271}

[[报文中携带的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1118_13379_x1524350946}[地址]{style="font-family:宋体"}

[[HostPortIndex]{lang="EN-US"}]{#struct_0_x1118_13379_884398660}

[[报文中携带的接口索引]{style="font-family:宋体"}]{#struct_0_x1118_13379_1646502628}

[[Neighbor information]{lang="EN-US"}]{#struct_0_x1118_13379_x750233090}

[[是否携带邻居信息：]{style="font-family:宋体"}]{#struct_0_x1118_13379_x1635743311}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Carried]{lang="EN-US"}]{#struct_0_x1118_13379_x819759642}[：表示携带]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not carried]{lang="EN-US"}]{#struct_0_x1118_13379_682230521}[：表示未携带]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1118_13379_724219878}

[[\# ]{lang="EN-US"}]{#struct_0_x1118_13379_1309200145}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上都全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能，并分别在其各自的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能；配置]{style="font-family:宋体"}[Device A]{lang="EN-US"}[的]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文发送时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒；在]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上打开]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[错误报文调试信息开关，并配置其]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<DeviceB\> debugging dldp error]{lang="EN-US"}]{#struct_0_x1118_13379_x1635677775}

[\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/ERROR: -MDC=1; Port GigabitEthernet1/0/1 received an error packet. Reason types of the error packet: INTERVAL ERROR.]{lang="EN-US"}

[*[// Device B]{lang="EN-US"}*]{#struct_0_x1118_13379_x1153573667}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到了一个错误报文，报文的错误类型为"报文中通告时间间隔错误"]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1118_13379_x1082951066}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上都全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能，并分别在其各自的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能；在]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上打开]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[事件调试信息开关，拔掉其接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的光纤。]{style="font-family:宋体"}

[[\<DeviceB\> debugging dldp event]{lang="EN-US"}]{#struct_0_x1118_13379_1770968526}

[\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/EVENT: -MDC=1; Port GigabitEthernet1/0/1 down.]{lang="FR"}

[*[// Device B]{lang="FR"}*]{#struct_0_x1118_13379_471633673}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[发生物理]{style="font-family:宋体"}[down]{lang="FR"}*

[[\# ]{lang="FR"}]{#struct_0_x1118_13379_1267718455}[在]{style="font-family:宋体"}[Device A]{lang="FR"}[和]{style="font-family:宋体"}[Device B]{lang="FR"}[上都全局使能]{style="font-family:宋体"}[DLDP]{lang="FR"}[功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在]{style="font-family:宋体"}[Device A]{lang="FR"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[DLDP]{lang="FR"}[功能]{style="font-family:宋体"}[；]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Device A]{lang="FR"}[和]{style="font-family:宋体"}[Device B]{lang="FR"}[上都打开]{style="font-family:宋体"}[DLDP]{lang="FR"}[定时器调试信息开关]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并在]{style="font-family:宋体"}[Device B]{lang="FR"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[上使能]{style="font-family:宋体"}[DLDP]{lang="FR"}[功能。]{style="font-family:宋体"}

[[\<DeviceB\> debugging dldp timer]{lang="EN-US"}]{#struct_0_x1118_13379_x1070420328}

[\*Apr 26 12:05:54:962 2011 DeviceB DLDP/7/TIMER: -MDC=1; Port GigabitEthernet1/0/1 created a recover-probe timer.]{lang="EN-US"}

[*[// Device B]{lang="EN-US"}*]{#struct_0_x1118_13379_x474437843}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上建立了一个]{style="font-family:宋体"}[recover-probe]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\<DeviceA\> debugging dldp timer]{lang="EN-US"}]{#struct_0_x1118_13379_x614643318}

[\*Apr 26 12:05:54:962 2011 DeviceA DLDP/7/TIMER:]{lang="EN-US"}

[The neighbor of port GigabitEthernet1/0/1 created a probe timer.]{lang="EN-US"}

[Neighbor BridgeMAC: 00e0-fc00-3331]{lang="EN-US"}

[Neighbor PortIndex: 9]{lang="EN-US"}

[*[// Device A]{lang="EN-US"}*]{#struct_0_x1118_13379_x1635219026}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下的邻居建立了一个]{style="font-family:宋体"}[probe]{lang="EN-US"}[定时器，该邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-3331]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[9]{lang="EN-US"}*

[[\*Apr 26 12:05:54:962 2011 DeviceA DLDP/7/TIMER: -MDC=1; The neighbor\'s probe timer of port GigabitEthernet1/0/1 timed out.]{lang="EN-US"}]{#struct_0_x1118_13379_543232027}

[Neighbor BridgeMAC: 00e0-fc00-3331]{lang="EN-US"}

[Neighbor PortIndex: 9]{lang="EN-US"}

[*[// Device A]{lang="EN-US"}*]{#struct_0_x1118_13379_833356865}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下邻居的]{style="font-family:宋体"}[probe]{lang="EN-US"}[定时器超时，该邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-3331]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[9]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1118_13379_1915212594}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上都全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能，并分别在其各自的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能；在]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上打开]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[\<DeviceB\> debugging dldp fsm]{lang="EN-US"}]{#struct_0_x1118_13379_x370729944}

[\*Apr 26 12:07:07:731 2011 DeviceB DLDP/7/FSM: -MDC=1; Port GigabitEthernet1/0/1 added a neighbor.]{lang="EN-US"}

[ Neighbor BridgeMAC: 00e0-fc00-3333]{lang="EN-US"}

[ Neighbor PortIndex: 35]{lang="EN-US"}

[ Neighbor state: UNCONFIRMED]{lang="EN-US"}

[*[// Device B]{lang="EN-US"}*]{#struct_0_x1118_13379_1573579051}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[增加了一个邻居，该邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-3333]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[35]{lang="EN-US"}[，处于未确认状态]{style="font-family:宋体"}*

[[\*Apr 26 12:07:09:731 2011 DeviceB DLDP/7/FSM: -MDC=1; A state transition occurred to the neighbor of port GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x1118_13379_1684478699}

[ Neighbor BridgeMAC: 00e0-fc00-3333]{lang="EN-US"}

[ Neighbor PortIndex: 35]{lang="EN-US"}

[ Neighbor state transition: UNCONFIRMED \--\> CONFIRMED]{lang="EN-US"}

[*[// Device B]{lang="EN-US"}*]{#struct_0_x1118_13379_x1635153490}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上有邻居进行状态迁移，该邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-3333]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[35]{lang="EN-US"}[，由未确认状态迁移到确认状态]{style="font-family:宋体"}*

[[\*Apr 26 12:12:22:653 2011 DeviceB DLDP/7/FSM: -MDC=1; Port GigabitEthernet1/0/1 state transition: UNIDIRECTIONAL \--\> BIDIRECTIONAL]{lang="EN-US"}]{#struct_0_x1118_13379_x1098283551}

[ Stimulation: Confirmed neighbor]{lang="EN-US"}

[*[// Device B]{lang="EN-US"}*]{#struct_0_x1118_13379_x969250225}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发生了状态迁移，由单通状态迁移到双通状态，激励条件为有确定邻居]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1118_13379_1456152736}[在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[上都全局使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能，并分别在其各自的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[功能；在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打开接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<DeviceA\> debugging dldp packet interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1118_13379_x1253884997}

[\*Apr 26 12:10:18:523 2011 DeviceA DLDP/7/PKT: -MDC=1; Port GigabitEthernet1/0/1 received a DLDP packet. Following is the content of the packet:]{lang="EN-US"}

[ DLDP ID: 0x0001]{lang="EN-US"}

[ DLDP version ID: 0x01]{lang="EN-US"}

[ DLDP packet type: ADVERTISEMENT]{lang="EN-US"}

[ Flags: NO-RSY]{lang="EN-US"}

[ Authentication mode: NONE]{lang="EN-US"}

[ Authentication password:]{lang="EN-US"}

[ Interval of sending Advertisement packet: 5 seconds]{lang="EN-US"}

[ HostBridgeMAC: 00e0-fc00-3331]{lang="EN-US"}

[ HostPortIndex: 9]{lang="EN-US"}

[ Neighbor information: Not carried]{lang="EN-US"}

[*[// Device A]{lang="EN-US"}*]{#struct_0_x1118_13379_x1857270847}*[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到了一个]{style="font-family:宋体"}[DLDP]{lang="EN-US"}[报文，其具体内容如下：协议号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，版本号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，报文类型为]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文，]{style="font-family:宋体"}[RSY]{lang="EN-US"}[标志为]{style="font-family:宋体"}[0]{lang="EN-US"}[（表示普通]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文），认证方式为不认证，无认证密码，发送]{style="font-family:宋体"}[Advertisement]{lang="EN-US"}[报文时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[00E0-FC00-3331]{lang="EN-US"}[，接口索引为]{style="font-family:宋体"}[9]{lang="EN-US"}[，未携带邻居信息]{style="font-family:宋体"}*
