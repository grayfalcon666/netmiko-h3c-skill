::: {#-1131994522 .myid}
[]{#_Toc404795433}[]{#struct_0_78412_18415_1641951566}

**CFD \-- CFD调试命令 \-- debugging cfd**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_78412_18415_x1121994929}

[**[debugging cfd]{lang="EN-US"}**[ { ]{lang="EN-US"}**[ais-track]{lang="EN-US"}**[ **link-status** **packet** \[ **level** *level-value* \] \| **all** \| **event** \| **fsm** \[ **ais** \| { **cci** \| **fng** \| **lbi** \| **mcc** \| **mme** \| **rmep** } \[ **interface** *interface-type interface-number* \] \| **packet** \[ **receive** \| **send** \] \[ **interface** *interface-type interface-number* \] \| **timer** }]{lang="EN-US"}]{#struct_0_78412_18415_x764482610}

[**[undo debugging cfd]{lang="EN-US"}**[ { ]{lang="EN-US"}**[ais-track]{lang="EN-US"}**[ **link-status** **packet** \[ **level** *level-value* \] \| **all** \| **event** \| **fsm** \[ **ais** \| { **cci** \| **fng** \| **lbi** \| **mcc** \| **mme** \| **rmep** } \[ **interface** *interface-type interface-number* \] \| **packet** \[ **receive** \| **send** \] \[ **interface** *interface-type interface-number* \] \| **timer** }]{lang="EN-US"}]{#struct_0_78412_18415_67570298}

[[【视图】]{style="font-family:黑体"}]{#struct_0_78412_18415_515982508}

[[用户视图]{style="font-family:宋体"}]{#struct_0_78412_18415_x1004316302}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_78412_18415_1966203929}

[[network-admin]{lang="EN-US"}]{#struct_0_78412_18415_103199197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_78412_18415_x1060004004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_78412_18415_227164126}

[**[ais-track]{lang="EN-US"}**[ **link-status** **packet**]{lang="EN-US"}]{#struct_0_78412_18415_x1082988256}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[以太网告警指示信号报文调试信息开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[level]{lang="EN-US"}**[ *level-value*]{lang="EN-US"}]{#struct_0_78412_18415_x470420335}[：表示指定级别]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的调试信息开关，]{style="font-family:宋体"}*[level-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。如果未指定本参数，表示所有级别]{style="font-family:
宋体"}[EAIS]{lang="EN-US"}[报文的调试信息开关。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_78412_18415_x1805536209}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_78412_18415_x1558921694}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_78412_18415_x4916179}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[ais]{lang="EN-US"}**]{#struct_0_78412_18415_x1082922720}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[告警指示信号状态机调试信息开关。]{style="font-family:宋体"}

[**[cci]{lang="EN-US"}**]{#struct_0_78412_18415_x1748386811}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连通性检测状态机调试信息开关。]{style="font-family:宋体"}

[**[fng]{lang="EN-US"}**]{#struct_0_78412_18415_1601636511}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[错误报警状态机]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[lbi]{lang="EN-US"}**]{#struct_0_78412_18415_x1004250766}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[环回状态机]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[mcc]{lang="EN-US"}**]{#struct_0_78412_18415_x1364928907}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}[状态机]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[mme]{lang="EN-US"}**]{#struct_0_78412_18415_1641656087}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[rmep]{lang="EN-US"}**]{#struct_0_78412_18415_59082745}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}[状态机]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_78412_18415_66774551}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_78412_18415_x1658158542}[：表示接收的]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_78412_18415_x584457140}[：表示发送的]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_78412_18415_x308239682}[：表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_78412_18415_x1863972309}[：表示]{style="font-family:宋体"}[CFD]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_78412_18415_x1004185230}

[]{#OLE_LINK1}[**[debugging cfd]{lang="EN-US"}**]{#struct_0_78412_18415_x1114907027}[命令用来打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging cfd]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[CFD]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[CFD]{lang="EN-US"}]{#struct_0_78412_18415_x578854873}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_78412_18415_380032365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当未指定]{style="font-family:宋体"}]{#struct_0_78412_18415_367896169}**[send]{lang="EN-US"}**[和]{style="font-family:宋体"}**[receive]{lang="EN-US"}**[参数时，表示同时打开或关闭]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文的发送和接收调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定了]{style="font-family:宋体"}]{#struct_0_78412_18415_1313650393}**[fsm]{lang="EN-US"}**[参数而未指定]{style="font-family:宋体"}**[ais]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cci]{lang="EN-US"}**[、]{style="font-family:宋体"}**[fng]{lang="EN-US"}**[、]{style="font-family:宋体"}**[lbi]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mcc]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mme]{lang="EN-US"}**[和]{style="font-family:宋体"}**[rmep]{lang="EN-US"}**[参数时，表示打开或关闭]{style="font-family:宋体"}[CFD]{lang="EN-US"}[所有的状态机调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口上配置的是内向]{style="font-family:宋体"}]{#struct_0_78412_18415_x1261107990}[MEP]{lang="EN-US"}[，由于内向]{style="font-family:宋体"}[MEP]{lang="EN-US"}[对报文处理的特殊性，在打开接口上发送]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文的调试信息开关时，只会输出]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文，而不会输出]{style="font-family:宋体"}[LT]{lang="EN-US"}[和]{style="font-family:宋体"}[LB]{lang="EN-US"}[报文；打开接口上接收]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文调试信息开关时，]{style="font-family:宋体"}[CCM]{lang="EN-US"}[、]{style="font-family:宋体"}[LT]{lang="EN-US"}[和]{style="font-family:宋体"}[LB]{lang="EN-US"}[报文都不会输出，如果想看到所有报文，可以打开所有接口收发]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于开启了硬件检测功能的]{style="font-family:宋体"}]{#struct_0_78412_18415_x1082201824}[MEP]{lang="EN-US"}[，打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文调试信息开关后，不会输出其]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文的调试信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设备上有辅助]{style="font-family:宋体"}]{#struct_0_78412_18415_461228925}[CPU]{lang="EN-US"}[，所有发送的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文调试信息都不会输出，接收的高速]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文会抽样输出，接收的低速]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文则正常输出。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging cfd ais-track link-status packet]{lang="EN-US"}]{#struct_0_78412_18415_x1412685669}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2092385758}[[字段]{style="font-family:黑体"}]{#struct_0_78412_18415_x1082136288}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_78412_18415_x1529978484}

[[Send EAIS Packet]{lang="EN-US"}]{#struct_0_78412_18415_1409910346}

[[发送]{style="font-family:宋体"}[EAIS]{lang="EN-US"}]{#struct_0_78412_18415_x603446585}[报文]{style="font-family:宋体"}

[[Packet Length]{lang="EN-US"}]{#struct_0_78412_18415_x1082726111}

[[报文长度]{style="font-family:宋体"}]{#struct_0_78412_18415_1262295391}

[[Level]{lang="EN-US"}]{#struct_0_78412_18415_x2101110004}

[[EAIS]{lang="EN-US"}]{#struct_0_78412_18415_430502660}[报文的发送级别]{style="font-family:宋体"}

[[Period]{lang="EN-US"}]{#struct_0_78412_18415_x1082660575}

[[EAIS]{lang="EN-US"}]{#struct_0_78412_18415_1870554843}[报文的发送周期]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging cfd event]{lang="EN-US"}]{#struct_0_78412_18415_1417355610}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1843533386}[[字段]{style="font-family:黑体"}]{#struct_0_78412_18415_x1004643982}

[[描述]{style="font-family:黑体"}]{#struct_0_78412_18415_346204092}

[[CFD processes create/delete port ]{lang="EN-US"}]{#struct_0_78412_18415_x595309752}*[port-name]{lang="FR"}*[ event]{lang="EN-US"}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_x139850645}[响应创建]{style="font-family:宋体"}[/]{lang="EN-US"}[删除接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[的事件]{style="font-family:宋体"}

[[CFD processes port *port-name* up/down event]{lang="EN-US"}]{#struct_0_78412_18415_2054152979}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_364785394}[响应接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[的]{style="font-family:宋体"}[up/down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[CFD processes port *port-name* active/deactive event]{lang="FR"}]{#struct_0_78412_18415_813483340}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_x1004578446}[响应接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[的激活]{style="font-family:宋体"}[/]{lang="EN-US"}[去激活事件]{style="font-family:宋体"}

[[CFD processes port ]{lang="EN-US"}]{#struct_0_78412_18415_x2000316182}*[port-name]{lang="FR"}*[ aggregation(leave) event]{lang="EN-US"}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_2037048115}[响应接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[的加入（退出）聚合组事件]{style="font-family:宋体"}

[[CFD responds to add port *port-name* to vlan 1]{lang="EN-US"}]{#struct_0_78412_18415_72134003}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_x1317473122}[响应接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[加入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[CFD responds to delete port *port-name* from vlan 1]{lang="EN-US"}]{#struct_0_78412_18415_x1004512910}

[[CFD]{lang="EN-US"}]{#struct_0_78412_18415_x1714565803}[响应接口]{style="font-family:宋体"}*[port-name]{lang="FR"}*[退出]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging cfd fsm]{lang="EN-US"}]{#struct_0_78412_18415_x1024505665}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1837176076}[[字段]{style="font-family:黑体"}]{#struct_0_78412_18415_x507160686}

[[描述]{style="font-family:黑体"}]{#struct_0_78412_18415_x587534122}

[[AIS]{lang="EN-US"}]{#struct_0_78412_18415_x1209329864}

[[告警指示信号状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_1870827544}

[[CCI]{lang="EN-US"}]{#struct_0_78412_18415_x1004447374}

[[连通性检测状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_2040434924}

[[FNG]{lang="EN-US"}]{#struct_0_78412_18415_1662477679}

[[错误报警状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_x2391165}

[[LBI]{lang="EN-US"}]{#struct_0_78412_18415_x2011227491}

[[环回状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_2042304891}

[[MCC]{lang="EN-US"}]{#struct_0_78412_18415_x1003857550}

[[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_78412_18415_x1879446306}[状态机]{style="font-family:宋体"}

[[MME]{lang="EN-US"}]{#struct_0_78412_18415_1528432636}

[[错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_78412_18415_91757716}[状态机]{style="font-family:宋体"}

[[RMEP]{lang="EN-US"}]{#struct_0_78412_18415_x759778922}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_78412_18415_x1003792014}[状态机]{style="font-family:宋体"}

[[FSM]{lang="EN-US"}]{#struct_0_78412_18415_x870172071}

[[状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_1565322029}

[[Port]{lang="EN-US"}]{#struct_0_78412_18415_598555938}

[[MEP]{lang="EN-US"}]{#struct_0_78412_18415_x272288114}[所在的接口]{style="font-family:宋体"}

[[SI]{lang="FR"}]{#struct_0_78412_18415_917932466}

[[MEP]{lang="EN-US"}]{#struct_0_78412_18415_x463329892}[所在的服务实例]{style="font-family:宋体"}

[[MEP]{lang="FR"}]{#struct_0_78412_18415_212988079}

[[配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_78412_18415_x1593563552}

[[State machine:*State-machine*]{lang="EN-US"}]{#struct_0_78412_18415_x788234862}

[[当前状态机为]{style="font-family:宋体"}*[State-machine]{lang="EN-US"}*]{#struct_0_78412_18415_917998002}

[[Prestate:*State-machine*]{lang="EN-US"}]{#struct_0_78412_18415_1866748918}

[[状态机变迁前的状态为]{style="font-family:宋体"}*[State-machine]{lang="EN-US"}*]{#struct_0_78412_18415_352366228}

[[Curstate:*State-machine*]{lang="EN-US"}]{#struct_0_78412_18415_519050445}

[[状态机的当前状态为]{style="font-family:宋体"}*[State-machine]{lang="EN-US"}*]{#struct_0_78412_18415_918063538}

[ ]{lang="EN-US"}

[]{#struct_0_78412_18415_218880983}[[表1-4 ]{lang="EN-US"}[debugging cfd packet]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1834326304}[[字段]{style="font-family:黑体"}]{#struct_0_78412_18415_x1490667089}

[[描述]{style="font-family:黑体"}]{#struct_0_78412_18415_436255606}

[*[port-name]{lang="FR"}*]{#struct_0_78412_18415_2014575252}[/*port-index* send/recv]{lang="FR"}

[[设备通过接口]{style="font-family:宋体"}]{#struct_0_78412_18415_493311643}*[port-name]{lang="FR"}*[/*port-index*]{lang="FR"}[发送]{style="font-family:宋体"}[/]{lang="EN-US"}[接收了一个]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Pkt length]{lang="EN-US"}]{#struct_0_78412_18415_1416500866}

[[报文长度]{style="font-family:宋体"}]{#struct_0_78412_18415_918129074}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging cfd timer]{lang="EN-US"}]{#struct_0_78412_18415_x160590528}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1833162580}[[字段]{style="font-family:黑体"}]{#struct_0_78412_18415_x51371741}

[[描述]{style="font-family:黑体"}]{#struct_0_78412_18415_508315481}

[[Service-instance]{lang="FR"}]{#struct_0_78412_18415_x447792964}

[[MEP]{lang="EN-US"}]{#struct_0_78412_18415_x1799411655}[所在的服务实例]{style="font-family:宋体"}

[[MEP]{lang="FR"}]{#struct_0_78412_18415_x662810555}

[[配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_78412_18415_917670322}

[[Operation]{lang="FR"}]{#struct_0_78412_18415_x681785525}

[[定时器的操作，包括]{style="font-family:宋体"}[create]{lang="EN-US"}]{#struct_0_78412_18415_x3175407}[、]{style="font-family:宋体"}[delete]{lang="EN-US"}[和]{style="font-family:宋体"}[refresh]{lang="EN-US"}

[[FNG]{lang="EN-US"}]{#struct_0_78412_18415_x1552682015}

[[错误报警状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_x253390756}

[[LBI]{lang="EN-US"}]{#struct_0_78412_18415_x872615379}

[[环回状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_917735858}

[[Xcon Ccm]{lang="EN-US"}]{#struct_0_78412_18415_2110565986}

[[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_78412_18415_950818448}[状态机]{style="font-family:宋体"}

[[Err Ccm]{lang="EN-US"}]{#struct_0_78412_18415_1901204550}

[[错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}]{#struct_0_78412_18415_x253495653}[状态机]{style="font-family:宋体"}

[[RMEP]{lang="EN-US"}]{#struct_0_78412_18415_706325381}

[[远端]{style="font-family:宋体"}[MEP]{lang="EN-US"}]{#struct_0_78412_18415_917801394}[状态机]{style="font-family:宋体"}

[[LTM]{lang="EN-US"}]{#struct_0_78412_18415_x895170770}

[[链路跟踪状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_x363387491}

[[AutoLtm]{lang="EN-US"}]{#struct_0_78412_18415_1976586537}

[[自动发送链路跟踪报文状态机]{style="font-family:宋体"}]{#struct_0_78412_18415_x980160507}

[[AIS]{lang="EN-US"}]{#struct_0_78412_18415_x1083053791}

[[告警指示信号]{style="font-family:宋体"}]{#struct_0_78412_18415_x667328133}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_78412_18415_917866930}

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x1082201823}[打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[以太网告警指示信号报文调试信息开关，使能端口状态与]{style="font-family:宋体"}[AIS]{lang="EN-US"}[联动功能并配置好]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文的发送级别和周期。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd ais-track link-status packet]{lang="EN-US"}]{#struct_0_78412_18415_1220743812}

[\*Feb  2 14:55:27:492 2013 Sysname EAIS/7/PACKET: -MDC=1;]{lang="EN-US"}

[Send EAIS Packet:]{lang="EN-US"}

[20 21 04 00 00]{lang="EN-US"}

[Packet Length: 5    Level: 1    Period: 1s]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78412_18415_1383305553}*[发送一个级别为]{style="font-family:宋体"}[1]{lang="EN-US"}[、周期为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒的]{style="font-family:宋体"}[EAIS]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_1893777049}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、服务实例和]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[告警指示信号状态机调试信息开关，使能告警抑制功能并配置相应的级别和周期。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm ais]{lang="EN-US"}]{#struct_0_78412_18415_x1082136287}

[\*Jul  3 10:26:51:743 2013 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[AIS: Service instance: 1,MEP: 1, PreState: IDLE, CurState: NO_RECEIVE]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_x320124903}*[中的]{style="font-family:宋体"}[AIS]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[NO_RECEIVE]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x33081094}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[连通性检测状态机调试信息开关。使能配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[，并使能该]{style="font-family:宋体"}[MEP]{lang="EN-US"}[的]{style="font-family:宋体"}[CC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm cci]{lang="EN-US"}]{#struct_0_78412_18415_927654675}

[\*Mar 29 09:20:54:037 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[CCI: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate:CCI_IDLE Curstate:CCI_WAITING]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_x1055519189}*[中的]{style="font-family:宋体"}[CCI]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[CCI_IDLE]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[CCI_WAITING]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_175534600}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}[状态机调试信息开关。该设备上的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[收到了其它设备发来的错误]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm mme]{lang="EN-US"}]{#struct_0_78412_18415_1670211985}

[\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[MME: GigabitEthernet1/0/1 Service-instance:1 mep:1]{lang="EN-US"}

[Prestate:ERRCCM_NO_DEFECT Curstate:ERRCCM_DEFECT]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_1856487589}*[中的]{style="font-family:宋体"}[MME]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[ERRCCM_NO_DEFECT]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[ERRCCM_DEFECT]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x1604586408}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}[状态机调试信息开关。该设备上的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[收到了其它设备发来的]{style="font-family:宋体"}[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm mcc]{lang="EN-US"}]{#struct_0_78412_18415_918456754}

[\*Mar 29 15:30:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[MCC: GigabitEthernet1/0/1 Service-instance:1 mep:1]{lang="EN-US"}

[Prestate:XCON_NO_DEFECT Curstate:XCON_DEFECT]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_732164804}*[中的]{style="font-family:宋体"}[MME]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[XCON_NO_DEFECT]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[XCON_DEFECT]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x34554360}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}[状态机调试信息开关。该设备上的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[收到了其它设备发来的交叉连接]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm mcc]{lang="EN-US"}]{#struct_0_78412_18415_x1719427948}

[\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[MCC: GigabitEthernet1/0/1 Service-instance:2 mep:3]{lang="EN-US"}

[Prestate:XCON_NO_DEFECT Curstate:XCON_DEFECT]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_1671315164}*[中的]{style="font-family:宋体"}[MME]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[XCON_NO_DEFECT]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[XCON_DEFECT]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_1818071804}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[ RMEP]{lang="EN-US"}[状态机调试信息开关。该设备上的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[在]{style="font-family:宋体"}[3.5]{lang="EN-US"}[个报文周期内没有收到了远端设备发来的]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm rmep]{lang="EN-US"}]{#struct_0_78412_18415_918522290}

[\*Mar 29 15:40:45:967 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[RMEP: GigabitEthernet1/0/1 Service-instance:2 mep:3]{lang="EN-US"}

[Prestate: RMEP_OK Curstate: RMEP_FAILED]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_x1911051258}*[中的]{style="font-family:宋体"}[RMEP]{lang="EN-US"}[状态机发生迁移，该状态机前一状态为]{style="font-family:宋体"}[RMEP_OK]{lang="EN-US"}[，当前状态为]{style="font-family:宋体"}[RMEP_FAILED]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x1740560390}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[错误报警状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm mme]{lang="EN-US"}]{#struct_0_78412_18415_1426570351}

[\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate: FNG_RESET Curstate: FNG_DEFECT]{lang="EN-US"}

[\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate:FNG_DEFECT Curstate: FNG_DEFECT_REPORT]{lang="EN-US"}

[\*Mar 29 09:20:56:056 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[FNG: GigabitEthernet1/0/1 Service-instance:1 mep:1 Prestate: FNG_DEFECT_REPORT Curstate: FNG_DEFECT_REPORTED]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_x1881525446}*[中的]{style="font-family:宋体"}[FNG]{lang="EN-US"}[状态机发生迁移]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_x1177422348}[在设备上启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[功能并配置相应]{style="font-family:宋体"}[MD]{lang="EN-US"}[、]{style="font-family:宋体"}[MA]{lang="EN-US"}[、]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD LBI]{lang="EN-US"}[报文状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd fsm lbi]{lang="EN-US"}]{#struct_0_78412_18415_917932467}

[\*Mar 29 15:30:56:161 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_IDLE Curstate: LBI_STARTING]{lang="EN-US"}

[\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_STARTING Curstate: LBI_TRANSMITTING]{lang="EN-US"}

[\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMITTING Curstate: LBI_TRANSMIT]{lang="EN-US"}

[\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM: -MDC=1;]{lang="EN-US"}

[LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMIT Curstate: LBI_TRANSMITTING]{lang="EN-US"}

[\*Mar 29 15:30:56:162 2011 Sysname CFD/7/FSM:]{lang="EN-US"}

[LBI: GigabitEthernet1/0/1 Service-instance 1 mep 1 Prestate: LBI_TRANSMITTING Curstate: LBI_WAITING]{lang="EN-US"}

[*[// CFD]{lang="EN-US"}*]{#struct_0_78412_18415_x463329891}*[中的]{style="font-family:宋体"}[LBI]{lang="EN-US"}[状态机发生迁移]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_78412_18415_212791471}[在设备上配置等级为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[MD]{lang="EN-US"}[和服务实例，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[MEP ID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的外向]{style="font-family:宋体"}[MEP]{lang="EN-US"}[。打开]{style="font-family:宋体"}[CFD]{lang="EN-US"}[协议报文的调试信息开关。启动]{style="font-family:宋体"}[CFD]{lang="EN-US"}[服务和]{style="font-family:宋体"}[CCM]{lang="EN-US"}[发送，并通过命令向远端配置的]{style="font-family:宋体"}[MEP]{lang="EN-US"}[发送]{style="font-family:宋体"}[LTM]{lang="EN-US"}[和]{style="font-family:宋体"}[LBM]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> debugging cfd packet]{lang="EN-US"}]{#struct_0_78412_18415_x971811927}

[\*Mar 29 15:38:32:663 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="EN-US"}

[20 01 05 36 00 00 00 3a 00 02 04 03 6d 64 31 02]{lang="EN-US"}

[03 6d 61 31 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 01 00 02 00 00 02]{lang="EN-US"}

[00 01 02 04 00 01 01 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00]{lang="EN-US"}

[Pkt length: 83]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78412_18415_917998003}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文，由该报文开头的]{style="font-family:宋体"}[01]{lang="EN-US"}[可知是一个]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 29 15:38:32:630 2011 Sysname CCM/7/PACKET: -MDC=1; Interface 148 recv:]{lang="EN-US"}]{#struct_0_78412_18415_x1082201826}

[20 01 05 36 00 00 00 3a 00 02 04 03 6d 64 31 02]{lang="EN-US"}

[03 6d 61 31 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00 01 00 02 00 00 02]{lang="EN-US"}

[00 01 02 04 00 01 01 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00]{lang="EN-US"}

[Pkt length: 83]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78412_18415_1624028339}*[通过索引号为]{style="font-family:宋体"}[148]{lang="EN-US"}[的接口发送了一个]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文，由该报文开头的]{style="font-family:宋体"}[01]{lang="EN-US"}[可知是一个]{style="font-family:宋体"}[CCM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 29 15:50:40:575 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 recv:]{lang="EN-US"}]{#struct_0_78412_18415_1866748919}

[20 05 00 11 00 02 00 01 09 00 11 22 33 44 01 00]{lang="EN-US"}

[11 22 33 44 01 07 00 08 00 00 00 11 22 33 44 01]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[Pkt length: 42]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_78412_18415_352300692}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到了一个]{style="font-family:宋体"}[CFD]{lang="EN-US"}[报文，由该报文开头的]{style="font-family:宋体"}[05]{lang="EN-US"}[可知是一个]{style="font-family:宋体"}[LTM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 29 15:42:14:245 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="EN-US"}]{#struct_0_78412_18415_x1010220507}

[20 04 00 06 00 02 00 00 07 01 08 00 10 00 00 00]{lang="EN-US"}

[11 22 33 44 01 00 00 00 00 00 00 00 00 05 00 0a]{lang="EN-US"}

[01 00 11 22 33 44 01 00 00 00 06 00 0a 01 00 11]{lang="EN-US"}

[22 33 44 01 00 00 00 01 00 02 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00]{lang="SV"}

[Pkt length: 72]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1557986737}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[由该报文开头的]{style="font-family:宋体"}[04]{lang="SV"}[可知是一个]{style="font-family:宋体"}[LTR]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Mar 29 09:37:28:452 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_918063539}

[20 03 00 04 00 02 00 00 01 00 02 00 00 03 00 02]{lang="SV"}

[00 00 1f 00 05 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00]{lang="SV"}

[Pkt length: 40]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_218880982}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[由该报文开头的]{style="font-family:宋体"}[03]{lang="SV"}[可知是一个]{style="font-family:宋体"}[LBM]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Mar 29 15:33:35:563 2011 Sysname CCM/7/PACKET: -MDC=1; GigabitEthernet1/0/1 recv:]{lang="SV"}]{#struct_0_78412_18415_x1490667090}

[20 02 00 04 00 01 00 01 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 ]{lang="SV"}

[Pkt length: 42]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1485993159}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[接收了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[由该报文开头的]{style="font-family:宋体"}[02]{lang="SV"}[可知是一个]{style="font-family:宋体"}[LBR]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 15:56:30:370 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_x1082660577}

[20 21 04 00 00]{lang="SV"}

[Pkt length]{lang="SV"}[：]{style="font-family:
宋体"}[5]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1082857185}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[21]{lang="SV"}[可知是一个]{style="font-family:宋体"}[AIS]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 15:50:19:800 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_x2117454946}

[20 2d 00 10 51 4b 3b 15 09 64 e0 70 00 00 00 00]{lang="SV"}

[00 00 00 00 00]{lang="SV"}

[Pkt length: 21]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_2015994285}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[2d]{lang="SV"}[可知是一个]{style="font-family:宋体"}[1DM]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 15:50:30:370 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_x1082791649}

[20 2f 00 20 51 4b 3b b9 2d 28 26 70 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00]{lang="SV"}

[Pkt length: 37]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1866474431}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[2f]{lang="SV"}[可知是一个]{style="font-family:宋体"}[DMM]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 15:51:30:450 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 receive:]{lang="SV"}]{#struct_0_78412_18415_x1082988257}

[20 2e 00 20 51 4b 3d b3 2d 28 26 70 51 48 70 d5]{lang="SV"}

[0f a9 43 18 51 48 70 d5 0f a9 43 18 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[Pkt length: 42]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_1095663606}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[接收了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[2e]{lang="SV"}[可知是一个]{style="font-family:宋体"}[DMR]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 15:52:30:830 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_1874524826}

[20 25 00 04 00 00 00 09 20 00 41 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[Pkt length: 77]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1082922721}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[25]{lang="SV"}[可知是一个]{style="font-family:宋体"}[TST]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 16:07:33:830 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 send:]{lang="SV"}]{#struct_0_78412_18415_713955673}

[20 2b 00 0c 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00]{lang="SV"}

[Pkt length: 17]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_x1083119329}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[2b]{lang="SV"}[可知是一个]{style="font-family:宋体"}[LMM]{lang="SV"}[报文]{style="font-family:宋体"}*

[[\*Feb  2 16:07:34:450 2013 Sysname CFD/7/PACKET: -MDC=1; GigabitEthernet1/0/1 receive:]{lang="SV"}]{#struct_0_78412_18415_x1091115421}

[20 2a 00 0c 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[00 00 00 00 00 00 00 00 00 00]{lang="SV"}

[Pkt length: 42]{lang="SV"}

[*[// ]{lang="SV"}*]{#struct_0_78412_18415_529547618}*[通过接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[发送了一个]{style="font-family:宋体"}[CFD]{lang="SV"}[报文，由该]{style="font-family:宋体"}[报文]{style="font-family:宋体"}[开头的]{style="font-family:宋体"}[2a]{lang="SV"}[可知是一个]{style="font-family:宋体"}[LMR]{lang="SV"}[报文]{style="font-family:宋体"}*
