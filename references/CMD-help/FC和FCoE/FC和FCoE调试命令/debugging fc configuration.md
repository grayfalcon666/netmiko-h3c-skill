::: {#-1649989733 .myid}
[]{#_Toc404797580}[]{#struct_0_x1489_93403_x742088542}[]{#_Toc235970619}[]{#_Toc233077691}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc configuration**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_467318077}

[**[debugging fc configuration]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \| **timer** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1441652831}

[**[undo debugging fc configuration]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \| **timer** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_629948126}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1384268456}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1690250529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_352034438}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x1686808424}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1972936039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x334762111}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x129905683}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_1168745460}[：]{style="font-family:宋体"}[表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_1384333992}[：]{style="font-family:宋体"}[表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_261686003}[：]{style="font-family:宋体"}[表示报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_1143469880}[：]{style="font-family:宋体"}[表示定时器调试信息开关。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1283349709}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x968997032}

[**[debugging fc configuration]{lang="EN-US"}**]{#struct_0_x1489_93403_x2058530331}[命令用来打开]{style="font-family:
宋体"}[Fabric]{lang="EN-US"}[配置模块的调试信息开关。]{style="font-family:宋体"}**[undo debugging fc configuration]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[Fabric]{lang="EN-US"}[配置模块的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x1489_93403_x1032602147}[配置模块的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging fc configuration error]{lang="EN-US"}]{#struct_0_x1489_93403_635256863}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1236770317}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1384399528}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x944224422}

[[VSAN *id* memory is not enough.]{lang="EN-US"}]{#struct_0_x1489_93403_x1845346754}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1451197417}[内存不足]{style="font-family:宋体"}

[[VSAN *id* ignored the RDI request packet received from upstream link.]{lang="EN-US"}]{#struct_0_x1489_93403_x597131295}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1291235581}[内忽略从上游收到的]{style="font-family:宋体"}[RDI]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *id* received RDI SW_ACC packet, but RDI session did not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_1384465064}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1339048461}[内收到]{style="font-family:宋体"}[RDI SW_ACC]{lang="IT"}[报文，]{style="font-family:宋体"}[但]{style="font-family:宋体"}[RDI session]{lang="IT"}[不存在]{style="font-family:宋体"}

[[VSAN *id* received RDI SW_RJT packet, but RDI session did not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_x607646988}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_975297249}[内收到]{style="font-family:宋体"}[RDI SW_RJT]{lang="IT"}[报文，]{style="font-family:宋体"}[但]{style="font-family:
  宋体"}[RDI session]{lang="IT"}[不存在]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* failed to be isolated.]{lang="EN-US"}]{#struct_0_x1489_93403_x2122097982}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1383482024}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内隔离失败]{style="font-family:宋体"}

[[VSAN *id* failed to process a RDI request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1528204730}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1055563340}[内处理]{style="font-family:宋体"}[RDI]{lang="EN-US"}[请求报文失败]{style="font-family:宋体"}

[[VSAN *id* received an error EFP packet for error record length *len*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1782504700}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1337512615}[内收到错误]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，错误记录长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[[VSAN *id* received an error EFP packet for error payload length *len*, and total packet length was *tlen*.]{lang="EN-US"}]{#struct_0_x1489_93403_1383547560}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_739431578}[内收到错误]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，错误负载长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*[，报文总长度]{style="font-family:宋体"}*[tlen]{lang="EN-US"}*

[[VSAN *id* received an error EFP packet for invalid principal switch priority *priority*.]{lang="EN-US"}]{#struct_0_x1489_93403_1513200799}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x640678561}[内收到错误]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，主交换机优先级]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[VSAN *id* received an error EFP packet for invalid principal switch name.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344877040}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1973435213}[内收到错误]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，主交换机名无效]{style="font-family:宋体"}

[[VSAN *id* received an error DIA packet for error DIA length *len.*]{lang="EN-US"}]{#struct_0_x1489_93403_x527189710}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x159835578}[内收到错误]{style="font-family:宋体"}[DIA]{lang="EN-US"}[报文，错误]{style="font-family:宋体"}[DIA]{lang="EN-US"}[长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[[VSAN *id* received an error DIA packet for invalid switch name.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811504}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x18873792}[内收到错误]{style="font-family:宋体"}[DIA]{lang="EN-US"}[报文，交换机名无效]{style="font-family:宋体"}

[[VSAN *id* received an error RDI packet for error payload length *len*, and total packet length was *tlen*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1925799200}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1958786850}[内收到错误]{style="font-family:宋体"}[RDI]{lang="EN-US"}[报文，错误负载长度]{style="font-family:宋体"}*[len]{lang="EN-US"}*[，报文总长度]{style="font-family:宋体"}*[tlen]{lang="EN-US"}*

[[VSAN *id* received an error RDI packet for invalid requesting switch name.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344745968}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x292734249}[内收到错误]{style="font-family:宋体"}[RDI]{lang="EN-US"}[报文，请求交换机名无效]{style="font-family:宋体"}

[[VSAN *id* received an error RDI packet for invalid domain ID.]{lang="EN-US"}]{#struct_0_x1489_93403_1852569776}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_529749158}[内收到错误]{style="font-family:宋体"}[RDI]{lang="EN-US"}[报文，域]{style="font-family:宋体"}[ID]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[VSAN *id* failed to allocate the domain ID, and error code was *errcode*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344680432}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x523921130}[内分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[失败，错误码为]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[。其中，]{style="font-family:宋体"}*[errcode]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[表示申请多个]{style="font-family:宋体"}[Domain ID]{lang="EN-US"}[时有已经被分出的]{style="font-family:宋体"}[Domain ID]{lang="EN-US"}[；为]{style="font-family:宋体"}[2]{lang="EN-US"}[表示]{style="font-family:宋体"}[Domain ID]{lang="EN-US"}[已经被申请完]{style="font-family:宋体"}

[[VSAN *id* failed to send RDI packet because RDI session did not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_123303512}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1709584874}[内发送]{style="font-family:宋体"}[RDI]{lang="EN-US"}[报文失败，因为]{style="font-family:宋体"}[RDI session]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[VSAN *id* ignored reconfiguration operation because the switch was isolated.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344614896}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1570825969}[内忽略重配置操作，因为交换机已经被隔离]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received packet on a wrong interface.]{lang="EN-US"}]{#struct_0_x1489_93403_x332263713}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344549360}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从错误接口收到报文]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received RCF SW_RJT packet, and isolated the interface.]{lang="EN-US"}]{#struct_0_x1489_93403_953652729}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1571083461}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内收到]{style="font-family:宋体"}[RCF]{lang="EN-US"}[拒绝报文，并隔离端口]{style="font-family:宋体"}

[[VSAN *id* received an error BF packet for error payload length *plen.*]{lang="EN-US"}]{#struct_0_x1489_93403_2140973479}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344483824}[内收到错误]{style="font-family:宋体"}[BF]{lang="EN-US"}[报文，负载长度错误]{style="font-family:宋体"}*[plen]{lang="EN-US"}*

[[VSAN *id* received an error RCF packet for error payload length *plen*.]{lang="EN-US"}]{#struct_0_x1489_93403_768115280}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x319916906}[内收到错误]{style="font-family:宋体"}[RCF]{lang="EN-US"}[报文，负载长度错误]{style="font-family:宋体"}*[plen]{lang="EN-US"}*

[[Interface *interface-name* in VSAN *id* rejected RCF packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344418288}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x417826429}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内拒绝]{style="font-family:宋体"}[RCF]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* failed to send *pkttype* packet from socket *id*, and cmdcode was *cmdcode*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1840333735}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1345401328}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket *id*]{lang="EN-US"}[发送]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[）报文失败，命令码字段为]{style="font-family:宋体"}*[cmdcode]{lang="EN-US"}*

[[Interface *interface-name* in VSAN *id* dropped packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1031991060}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1658260643}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内丢弃报文]{style="font-family:宋体"}

[[VSAN *id* failed to create socket.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345335792}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1628648007}[内创建]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* failed to add port data of *pkttype* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_560249576}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344877039}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内添加]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[）报文的端口数据失败]{style="font-family:宋体"}

[[VSAN *id* failed to bind socket *id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x51448592}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1184378991}[内绑定]{style="font-family:宋体"}[socket *id*]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *id* failed to start link up delay timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811503}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1584957733}[内创建链路]{style="font-family:宋体"}[up]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging fc configuration event]{lang="EN-US"}]{#struct_0_x1489_93403_x115787757}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1225540205}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x906541224}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x647010852}

[[VSAN *id* merged (*wwn, domain-id*) to local domain ID list.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344745967}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_917119332}[内合并报文中的]{style="font-family:宋体"}*[wwn]{lang="EN-US"}*[和]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[对到本地]{style="font-family:宋体"}

[[VSAN *id* deleted (*wwn, domain-id*) from local domain ID list.]{lang="EN-US"}]{#struct_0_x1489_93403_1235732361}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_861863414}[内从本地删除]{style="font-family:宋体"}*[wwn]{lang="EN-US"}*[和]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[对]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received EPort up event.]{lang="EN-US"}]{#struct_0_x1489_93403_2104357107}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344680431}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内收到]{style="font-family:宋体"}[E]{lang="EN-US"}[端口]{style="font-family:宋体"}[up]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received EPort down event.]{lang="EN-US"}]{#struct_0_x1489_93403_1042162811}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_747461250}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内收到]{style="font-family:宋体"}[E]{lang="EN-US"}[端口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *id* fabric name changed from *wwn1* to *wwn2*.]{lang="EN-US"}]{#struct_0_x1489_93403_131793809}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1955026721}[内]{style="font-family:宋体"}[fabric name]{lang="EN-US"}[从]{style="font-family:宋体"}*[wwn1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[wwn2]{lang="EN-US"}*

[[VSAN *id* principal switch changed to (*switch-wwn*, *priority*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1344614895}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1158057386}[内主交换机变为（]{style="font-family:宋体"}*[switch-wwn]{lang="EN-US"}*[，]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[VSAN *id* running domain ID changed from *domain-id1* to *domain-id2*.]{lang="EN-US"}]{#struct_0_x1489_93403_1404368076}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_65587428}[内运行域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}*[domain-id1]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[domain-id2]{lang="EN-US"}*

[[VSAN *id* sent EFP requests to all up ports.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344549359}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x256397460}[内向所有]{style="font-family:宋体"}[UP]{lang="EN-US"}[的接口发送]{style="font-family:宋体"}[EFP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[VSAN *id* unisolated all isolated ports.]{lang="EN-US"}]{#struct_0_x1489_93403_x322518543}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1011131925}[内去隔离所有已隔离的接口]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* was isolated because the switch was isolated.]{lang="EN-US"}]{#struct_0_x1489_93403_x765423511}

[[由于交换机被隔离，所以接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344483823}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内被隔离]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received DIA request packet from non-upstream principal link.]{lang="EN-US"}]{#struct_0_x1489_93403_x1960768075}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_488600564}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从非上游主链路收到]{style="font-family:宋体"}[DIA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[VSAN *id* received RDI RJT packet because the principal switch rejected allocating domain ID with reason code *reason-code.*]{lang="EN-US"}]{#struct_0_x1489_93403_922265970}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344418287}[内收到]{style="font-family:宋体"}[RDI]{lang="EN-US"}[拒绝报文因为主交换机拒绝分配域]{style="font-family:宋体"}[ID]{lang="EN-US"}[且原因码为]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*

[[Interface *interface-name* in VSAN *id* rejected the allocated domain ID, and isolated the interface.]{lang="EN-US"}]{#struct_0_x1489_93403_1598596206}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_682705215}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内拒绝分配的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，并隔离接口]{style="font-family:宋体"}

[[VSAN *id* accepted the allocated domain ID *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_75825038}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1345401327}[内接收分配的域]{style="font-family:宋体"}[ID *domain-id*]{lang="EN-US"}

[[VSAN *id* successfully allocated domain ID *domain-id* for the downstream switch.]{lang="EN-US"}]{#struct_0_x1489_93403_1246553601}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2041983336}[内为下游交换机成功分配域]{style="font-family:宋体"}[ID *domain-id*]{lang="EN-US"}

[[VSAN *id* started non-disruptive reconfiguration because principal switch conflicted.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345335791}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1225363480}[内发起不中断重配置因为记录的主交换机信息冲突]{style="font-family:宋体"}

[[VSAN *id* updated the local domain ID list.]{lang="EN-US"}]{#struct_0_x1489_93403_x982868680}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1819320478}[内更新本地域]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[VSAN *id* processed *event (event-id)* event in *state (state-id)* state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344877042}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x810635799}[内]{style="font-family:宋体"}*[state-id]{lang="EN-US"}*[状态下处理]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*[事件。其中，]{style="font-family:宋体"}

[*[state-id]{lang="EN-US"}*]{#struct_0_x1489_93403_2044932279}[与]{style="font-family:宋体"}*[state]{lang="EN-US"}*[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811506}[：]{lang="EN-US" style="font-family:宋体"}[INIT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1489_93403_x1181673206}[：]{lang="EN-US" style="font-family:宋体"}[BF]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="FR"}]{#struct_0_x1489_93403_x1947788862}[：]{lang="EN-US" style="font-family:
  宋体"}[RCF]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="FR"}]{#struct_0_x1489_93403_x409993997}[：]{lang="EN-US" style="font-family:
  宋体"}[EFP]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="FR"}]{#struct_0_x1489_93403_x1344745970}[：]{lang="EN-US" style="font-family:
  宋体"}[PRINCIPAL]{lang="FR"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1489_93403_x649030145}[：]{lang="EN-US" style="font-family:宋体"}[REQUEST]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1489_93403_x1688924059}[：]{lang="EN-US" style="font-family:宋体"}[SUBORDINATE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1489_93403_x1344680434}[：]{lang="EN-US" style="font-family:宋体"}[STATIC]{lang="EN-US"}

[*[event-id]{lang="EN-US"}*]{#struct_0_x1489_93403_638878284}[与]{style="font-family:宋体"}*[event]{lang="EN-US"}*[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="PT-BR"}]{#struct_0_x1489_93403_x891195476}[：]{lang="EN-US" style="font-family:宋体"}[EPort up ]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[EPort]{lang="PT-BR"}[端口]{lang="EN-US" style="font-family:宋体"}[up]{lang="PT-BR"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1489_93403_x1344614898}[：]{lang="EN-US" style="font-family:宋体"}[PSST timed out ]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1489_93403_x2021164663}[：]{lang="EN-US" style="font-family:宋体"}[DIA packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[DIA]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1489_93403_587485231}[：]{lang="EN-US" style="font-family:宋体"}[RDI packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[RDI]{lang="EN-US"}[请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1489_93403_x236647472}[：]{lang="EN-US" style="font-family:宋体"}[RDI_RJT packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[RDI]{lang="EN-US"}[请求的]{lang="EN-US" style="font-family:宋体"}[SW_RJT]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1489_93403_x1344549362}[：]{lang="EN-US" style="font-family:宋体"}[RDI_ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[RDI]{lang="EN-US"}[请求的]{lang="EN-US" style="font-family:宋体"}[SW_ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1489_93403_2116452143}[：]{lang="EN-US" style="font-family:宋体"}[FRT timed out ]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器超时]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1489_93403_x1781985298}[：]{lang="EN-US" style="font-family:宋体"}[BF packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[BF]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x1489_93403_x1344483826}[：]{lang="EN-US" style="font-family:宋体"}[RCF packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[RCF]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x1489_93403_1930914694}[：]{lang="EN-US" style="font-family:宋体"}[non-disruptive domain restart]{lang="EN-US"}[，发起]{lang="EN-US" style="font-family:宋体"}[Non-disruptive]{lang="EN-US"}[重配置事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x1489_93403_1586512273}[：]{lang="EN-US" style="font-family:宋体"}[disruptive domain restart]{lang="EN-US"}[，发起]{lang="EN-US" style="font-family:
  宋体"}[Disruptive]{lang="EN-US"}[重配置事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_x1489_93403_x1344418290}[：]{lang="EN-US" style="font-family:宋体"}[overlapped EFP packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:
  宋体"}[EFP]{lang="EN-US"}[报文且]{lang="EN-US" style="font-family:
  宋体"}[Fabric]{lang="EN-US"}[合并域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[有重叠]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[12]{lang="EN-US"}]{#struct_0_x1489_93403_x773991253}[：]{lang="EN-US" style="font-family:宋体"}[non-overlapped EFP packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:
  宋体"}[EFP]{lang="EN-US"}[报文且]{lang="EN-US" style="font-family:
  宋体"}[Fabric]{lang="EN-US"}[合并域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[不重叠且不为空]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[13]{lang="EN-US"}]{#struct_0_x1489_93403_1519816259}[：]{lang="EN-US" style="font-family:宋体"}[empty EFP packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[Domain_ID_List]{lang="EN-US"}[为空]{lang="EN-US" style="font-family:宋体"}[EFP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[14]{lang="EN-US"}]{#struct_0_x1489_93403_x1345401330}[：]{lang="EN-US" style="font-family:宋体"}[principal link down]{lang="EN-US"}[，主链路的]{lang="EN-US" style="font-family:
  宋体"}[EPort]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[15]{lang="EN-US"}]{#struct_0_x1489_93403_x675695164}[：]{lang="EN-US" style="font-family:宋体"}[fabric enable]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x1489_93403_x1345335794}[：]{lang="EN-US" style="font-family:宋体"}[fabric disable]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置功能关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[17]{lang="EN-US"}]{#struct_0_x1489_93403_x465848593}[：]{lang="EN-US" style="font-family:宋体"}[switch isolate]{lang="EN-US"}[，交换机隔离]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[18]{lang="EN-US"}]{#struct_0_x1489_93403_2014870775}[：]{lang="EN-US" style="font-family:宋体"}[switch unisolate]{lang="EN-US"}[，交换机去隔离]{lang="EN-US" style="font-family:宋体"}

[[VSAN *id* isolated the switch.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344877041}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x407351272}[内隔离交换机]{style="font-family:宋体"}

[[VSAN *id* unisolated the switch.]{lang="EN-US"}]{#struct_0_x1489_93403_x1185258077}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811505}[内去隔离交换机]{style="font-family:宋体"}

[[VSAN *id* started non-disruptive reconfiguration because local switch was principal switch.]{lang="EN-US"}]{#struct_0_x1489_93403_1547210149}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344745969}[内发起不中断重配置因为本设备是主交换机]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* was successfully isolated.]{lang="EN-US"}]{#struct_0_x1489_93403_x1858818190}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x622890092}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内隔离成功]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* was successfully unisolated.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344680433}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x2090005071}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内去隔离成功]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* was added to downstream principal link.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344614897}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x4742028}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内被添加到下游主链路]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* was deleted from downstream principal link.]{lang="EN-US"}]{#struct_0_x1489_93403_x330560266}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344549361}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从下游主链路删除]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* changed to the upstream principal link.]{lang="EN-US"}]{#struct_0_x1489_93403_x612431212}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344483825}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内变为上游主链路]{style="font-family:宋体"}

[[VSAN *id* entered Init state.]{lang="EN-US"}]{#struct_0_x1489_93403_x797968661}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1555332689}[内状态机变迁为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered BF state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344418289}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1148257512}[内状态机变迁为]{style="font-family:宋体"}[BF]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered RCF state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345401329}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1696892295}[内状态机变迁为]{style="font-family:宋体"}[RCF]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered EFP state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345335793}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x62564066}[内状态机变迁为]{style="font-family:宋体"}[EFP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered Principal state.]{lang="EN-US"}]{#struct_0_x1489_93403_1216086427}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344877044}[内状态机变迁为]{style="font-family:宋体"}[Principal]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered Request state.]{lang="EN-US"}]{#struct_0_x1489_93403_x4066745}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811508}[内状态机变迁为]{style="font-family:宋体"}[Request]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered Subordinate state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1632011900}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344745972}[内状态机变迁为]{style="font-family:宋体"}[Subordinate]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *id* entered Static state.]{lang="EN-US"}]{#struct_0_x1489_93403_513769269}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344680436}[内状态机变迁为]{style="font-family:宋体"}[Static]{lang="EN-US"}[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging fc configuration packet]{lang="EN-US"}]{#struct_0_x1489_93403_1801677698}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1249998541}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x56655488}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x284757096}

[[Interface *interface-name* in VSAN *id* received SW_RJT packet from socket *socket-id*, reason was *RJTcode*, and explanation was *RJTexplanation*.]{lang="EN-US"}]{#struct_0_x1489_93403_1987224295}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344614900}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[收到拒绝原因字段为]{style="font-family:宋体"}*[RJTcode]{lang="EN-US"}*[、解释码字段为]{style="font-family:宋体"}*[RJTexplanation]{lang="EN-US"}*[的拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received *pkttype* packet from socket *socket-id*, but the interface was isolated.]{lang="EN-US"}]{#struct_0_x1489_93403_1918031024}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x276655988}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[收到]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[、]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[）请求报文，但是接口处于隔离状态]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received RCF SW_RJT packet, and isolated the interface.]{lang="EN-US"}]{#struct_0_x1489_93403_967991450}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_890054243}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内收到]{style="font-family:宋体"}[RCF SW_RJT]{lang="EN-US"}[报文，并隔离接口]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* received *pkttype* packet from socket *socket-id*, and cmdcode was *cmdcode*.]{lang="EN-US"}]{#struct_0_x1489_93403_2102219769}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344549364}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[收到]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[、]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[）报文，命令码字段为]{style="font-family:宋体"}*[cmdcode]{lang="EN-US"}*

[[Interface *interface-name* in VSAN *id* sent *pkttype* packet from socket *socket-id*, and cmdcode was *cmdcode*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1371946099}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1517173325}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[发送]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[）报文，命令码字段为]{style="font-family:宋体"}*[cmdcode]{lang="EN-US"}*

[ ]{lang="EN-US"}

[]{#struct_0_x1489_93403_x460282058}[[表1-4 ]{lang="EN-US"}[debugging fc configuration timer]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1252029869}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x539227693}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1344483828}

[[VSAN *id* deleted the PSST timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1201253188}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1635491730}[内删除]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[VSAN *id* deleted the FRT timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1751038332}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1270756885}[内删除]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[VSAN *id* PSST timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1475995840}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1344418292}[内]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[VSAN *id* failed to start the PSST timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1936790667}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1526880694}[内启动]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[VSAN *id* successfully started the PSST timer.]{lang="EN-US"}]{#struct_0_x1489_93403_603468512}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1724534937}[内启动]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器成功]{style="font-family:宋体"}

[[VSAN *id* FRT timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345401332}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_487104250}[内]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[VSAN *id* failed to start the FRT timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x755037894}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1708310880}[内启动]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[VSAN *id* successfully started the FRT timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1345335796}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_696950821}[内启动]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器成功]{style="font-family:宋体"}

[[Interface *interface-name* in VSAN *id* failed to start the *pkttype* timer, and socket was *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1107923113}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_64073257}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内启动]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[）请求报文的定时器失败，且]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[Interface *interface-name* in VSAN *id* *pkttype* timer timed out, and socket was *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2095490484}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344877043}[在]{style="font-family:宋体"}[VSAN *id*]{lang="EN-US"}[内的]{style="font-family:宋体"}*[pkttype]{lang="EN-US"}*[（]{style="font-family:宋体"}[EFP]{lang="EN-US"}[、]{style="font-family:宋体"}[DIA]{lang="EN-US"}[、]{style="font-family:宋体"}[RDI]{lang="EN-US"}[、]{style="font-family:宋体"}[BF]{lang="EN-US"}[、]{style="font-family:宋体"}[RCF]{lang="EN-US"}[）请求报文定时器超时，且]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sock-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_755448142}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1750493687}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置模块的错误调试开关。在接口下配置拒绝]{style="font-family:宋体"}[RCF]{lang="EN-US"}[报文的情况下，当对端设备发起]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[重配置时，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc configuration error]{lang="EN-US"}]{#struct_0_x1489_93403_2094051671}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface fc 1/0/1]{lang="EN-US"}

[\[Sysname-Fc1/0/1\] fc domain rcf-reject vsan 1]{lang="EN-US"}

[\*Jun 23 15:50:40:899 2011 Sysname FCFABRIC/7/ERROR: -MDC=1; Interface Fc1/0/1 in VSAN 1 rejected RCF packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1491130264}*[接口]{style="font-family:宋体"}[fc1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内拒绝]{style="font-family:宋体"}[RCF]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x107980656}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置模块的事件调试开关。当发起]{style="font-family:宋体"}[Disruptive]{lang="EN-US"}[重配置时，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc configuration event]{lang="EN-US"}]{#struct_0_x1489_93403_x1344811507}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain restart disruptive]{lang="EN-US"}

[The command may cause traffic interruption. Continue? \[Y/N\]:y]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 processed disruptive domain restart (10) event in INIT (0) state.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_384410735}*[内]{style="font-family:宋体"}[ INIT]{lang="EN-US"}[状态下处理]{style="font-family:宋体"}[Disruptive]{lang="EN-US"}[重配置事件]{style="font-family:宋体"}*

[[\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered RCF state.]{lang="EN-US"}]{#struct_0_x1489_93403_1120859187}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_76041299}*[进入]{style="font-family:宋体"}[RCF]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 running domain ID changed from 0x1 to 0.]{lang="EN-US"}]{#struct_0_x1489_93403_x825742117}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_x195630414}*[运行域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}[1]{lang="EN-US"}[变为]{style="font-family:宋体"}[0 ]{lang="EN-US"}*

[[\*Jun 23 15:56:08:290 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 fabric name changed from 10:00:00:11:22:33:44:00 to 00:00:00:00:00:00:00:00.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344745971}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_2079853210}*[的]{style="font-family:宋体"}[fabric name]{lang="EN-US"}[从]{style="font-family:宋体"}[10:00:00:11:22:33:44:00]{lang="EN-US"}[变为]{style="font-family:宋体"}[00:00:00:00:00:00:00:00 ]{lang="EN-US"}*

[[\*Jun 23 15:56:08:291 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 unisolated all isolated ports.]{lang="EN-US"}]{#struct_0_x1489_93403_902536218}

[\*Jun 23 15:56:08:292 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Interface Fc1/0/1 in VSAN 1 was successfully unisolated.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_x700171447}*[去隔离所有隔离接口，且接口]{style="font-family:宋体"}[fc1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[内去隔离]{style="font-family:宋体"}*

[[\*Jun 23 15:56:08:294 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Interface Fc1/0/1 in VSAN 1 received EPort up event. ]{lang="EN-US"}]{#struct_0_x1489_93403_763323765}

[\*Jun 23 15:56:08:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 processed EPort up (0) event in RCF (2) state.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_1888722310}*[收到]{style="font-family:宋体"}[EPORT up]{lang="EN-US"}[事件，在]{style="font-family:宋体"}[RCF]{lang="EN-US"}[状态下处理]{style="font-family:宋体"}[EPORT up]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Jun 23 15:56:13:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered EFP state.]{lang="EN-US"}]{#struct_0_x1489_93403_399871452}

[\*Jun 23 15:56:13:325 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 sent EFP requests to all up ports.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_x1344680435}*[进入]{style="font-family:宋体"}[EFP]{lang="EN-US"}[状态，并向所有]{style="font-family:宋体"}[UP]{lang="EN-US"}[的]{style="font-family:宋体"}[EPort]{lang="EN-US"}[发送]{style="font-family:宋体"}[EFP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 entered Principal state.]{lang="EN-US"}]{#struct_0_x1489_93403_x927205657}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_301703904}*[进入]{style="font-family:宋体"}[Principal]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 running domain ID changed from 0 to 0x1.          ]{lang="EN-US"}]{#struct_0_x1489_93403_x32101156}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_x776047347}*[运行域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}[0]{lang="EN-US"}[变为]{style="font-family:宋体"}[1 ]{lang="EN-US"}*

[[\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 principal switch changed to (10:00:00:11:22:33:44:00, 2).]{lang="EN-US"}]{#struct_0_x1489_93403_x745781091}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_x1977252334}*[主交换机变为]{style="font-family:宋体"}[(10:00:00:11:22:33:44:00, 2)]{lang="EN-US"}*

[[\*Jun 23 15:56:23:326 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 1 fabric name changed from 00:00:00:00:00:00:00:00 to 10:00:00:11:22:33:44:00.  ]{lang="EN-US"}]{#struct_0_x1489_93403_x1344614899}

[*[// VSAN 1 fabric name]{lang="EN-US"}*]{#struct_0_x1489_93403_x455080722}*[从]{style="font-family:
宋体"}[00:00:00:00:00:00:00:00]{lang="EN-US"}[变为]{style="font-family:宋体"}[10:00:00:11:22:33:44:00]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_12579239}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置模块的报文调试开关。当接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc configuration packet]{lang="EN-US"}]{#struct_0_x1489_93403_968537980}

[\*Jun 23 16:24:11:854 2011 Sysname FCFABRIC/7/PACKET: -MDC=1; Interface Fc1/0/1 in VSAN 1 sent EFP packet from socket 102, and cmdcode was 0x11.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x1489_93403_x539531937}*[接口]{style="font-family:宋体"}[fc1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket 102]{lang="EN-US"}[发送]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，命令字为]{style="font-family:宋体"}[0x11]{lang="EN-US"}*

[[\*Jun 23 16:24:11:878 2011 Sysname FCFABRIC/7/PACKET: -MDC=1; Interface Fc1/0/1 in VSAN 1 received EFP packet from socket 102, and cmdcode was 0x2.]{lang="EN-US"}]{#struct_0_x1489_93403_x1374327335}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1500538809}*[接口]{style="font-family:宋体"}[fc1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[内从]{style="font-family:宋体"}[socket 102]{lang="EN-US"}[收到]{style="font-family:宋体"}[EFP]{lang="EN-US"}[报文，命令字为]{style="font-family:宋体"}[0x2]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_203293370}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[配置模块的定时器调试开关。当发起]{style="font-family:宋体"}[Disruptive]{lang="EN-US"}[重配置时，系统将输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc configuration timer]{lang="EN-US"}]{#struct_0_x1489_93403_x1344549363}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] vsan 1]{lang="EN-US"}

[\[Sysname-vsan1\] domain restart disruptive]{lang="EN-US"}

[The command may cause traffic interruption. Continue? \[Y/N\]:y]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jun 23 16:30:01:410 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 successfully started the FRT timer.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_550368202}*[内启动]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器成功]{style="font-family:宋体"}*

[[\*Jun 23 16:30:06:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 FRT timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1172166029}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_701501866}*[内]{style="font-family:宋体"}[FRT]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*

[[\*Jun 23 16:30:06:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 successfully started the PSST timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x714633095}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_1048868118}*[内启动]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器成功]{style="font-family:宋体"}*

[[\*Jun 23 16:30:16:425 2011 Sysname FCFABRIC/7/TIMER: -MDC=1; VSAN 1 PSST timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1344483827}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_364830753}*[内]{style="font-family:宋体"}[PSST]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}*

::: {#-864179399 .myid}
[]{#_Toc297193505}[]{#_Toc404797581}[]{#struct_0_x1489_93403_674427884}[]{#_Toc295486836}[]{#_Toc248720180}[]{#_Toc227722566}[]{#_Toc227642187}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc exchange**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1891027690}

[**[debugging]{lang="EN-US"}**[ **fc** **exchange** { **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1489_93403_x1655517889}

[**[undo]{lang="EN-US"}**[ **debugging** **fc** **exchange** { **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x1489_93403_x296790911}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_468395593}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x468473809}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1344418291}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_792092688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1068184069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1977211365}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_x525726197}[：]{style="font-family:宋体"}[表示错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_794826827}[：]{style="font-family:宋体"}[表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_549703403}

[**[debugging fc exchange]{lang="EN-US"}**]{#struct_0_x1489_93403_x1345401331}[命令用来打开]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fc exchange]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_2053188191}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging fc exchange error]{lang="EN-US"}]{#struct_0_x1489_93403_x754139890}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1246601933}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_473702969}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2101596069}

[[Time(s)]{lang="EN-US"}]{#struct_0_x1489_93403_x664015915}

[[时戳]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1345335795}

[[FCEXCH Input]{lang="EN-US"}]{#struct_0_x1489_93403_1100235348}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1958046519}[接收]{style="font-family:宋体"}

[[FCEXCH Output]{lang="EN-US"}]{#struct_0_x1489_93403_x40474258}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1650657367}[发送]{style="font-family:宋体"}

[[VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_221206901}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1496569630}[索引]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1489_93403_1459915873}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x1433150234}[协议号（]{style="font-family:宋体"}[0]{lang="EN-US"}[为无效值）]{style="font-family:宋体"}

[[Local]{lang="EN-US"}]{#struct_0_x1489_93403_x543885309}

[[本端]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_221272437}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}

[[Remote]{lang="EN-US"}]{#struct_0_x1489_93403_1636354806}

[[对端]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1298088657}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_x1489_93403_x1243761704}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1492961933}[的连接状态，各种取值含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PREPARE]{lang="EN-US"}]{#struct_0_x1489_93403_221337973}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[绑定成功]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[等待回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_x1489_93403_1628252223}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[监听连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_x1489_93403_932453717}[：表示连接建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS]{lang="EN-US"}]{#struct_0_x1489_93403_x1044587323}[：表示连接超时或出错后发送了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BA_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_221403509}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[并回应了]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ACC ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS_ACK]{lang="EN-US"}]{#struct_0_x1489_93403_751392366}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_x1489_93403_2101841592}[：表示连接关闭]{lang="EN-US" style="font-family:宋体"}

[[Error: Failed to receive ACK for packet]{lang="EN-US"}]{#struct_0_x1489_93403_x354448635}

[[没有收到对端]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x1489_93403_221469045}[报文]{style="font-family:宋体"}

[[Error: Failed to find exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1897724139}

[[查找]{style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1083648699}[失败]{style="font-family:宋体"}

[[Error: Failed to process link exchange]{lang="EN-US"}]{#struct_0_x1489_93403_x1216490913}

[[连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_221534581}[校验修改失败]{style="font-family:宋体"}

[[Error: Failed to accept connection]{lang="EN-US"}]{#struct_0_x1489_93403_x9087535}

[[不允许建立连接]{style="font-family:宋体"}]{#struct_0_x1489_93403_x692871667}

[[Error: Failed to create a socket for link exchange]{lang="EN-US"}]{#struct_0_x1489_93403_221600117}

[[连接]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_x1489_93403_1025737744}[创建失败]{style="font-family:宋体"}

[[Error: Failed to add link exchange]{lang="EN-US"}]{#struct_0_x1489_93403_860143336}

[[创建连接]{style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_x576534415}[失败]{style="font-family:宋体"}

[[Error: Invalid initiative]{lang="EN-US"}]{#struct_0_x1489_93403_221665653}

[[不具备发送主动权]{style="font-family:宋体"}]{#struct_0_x1489_93403_1380639259}

[[Error: Failed to make memory continuously]{lang="EN-US"}]{#struct_0_x1489_93403_x658618642}

[[报文内存连续失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_220682613}

[[Error: Failed to build packet by packet type]{lang="EN-US"}]{#struct_0_x1489_93403_x677183590}

[[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_672626317}[协议报文生成失败]{style="font-family:宋体"}

[[Error: Invalid seq ID]{lang="EN-US"}]{#struct_0_x1489_93403_1256813550}

[[发送序号错误]{style="font-family:宋体"}]{#struct_0_x1489_93403_220748149}

[[Error: Failed to reassemble all fragments]{lang="EN-US"}]{#struct_0_x1489_93403_x1452045183}

[[分片报文重组失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1076061328}

[ ]{lang="EN-US" style="background:white"}

[[表1-6 ]{lang="EN-US"}[debugging fc exchange packet]{lang="EN-US"}]{#struct_0_x1489_93403_221206902}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1245614989}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1496569629}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x912671586}

[[Time(s)]{lang="EN-US"}]{#struct_0_x1489_93403_156458572}

[[时戳]{style="font-family:宋体"}]{#struct_0_x1489_93403_2107939377}

[[FCEXCH Input]{lang="EN-US"}]{#struct_0_x1489_93403_1194274700}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_221272438}[接收]{style="font-family:宋体"}

[[FCEXCH Output]{lang="EN-US"}]{#struct_0_x1489_93403_1636354793}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_2017936072}[发送]{style="font-family:宋体"}

[[state]{lang="EN-US"}]{#struct_0_x1489_93403_x792797046}

[[FC Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_1387502310}[的连接状态，各种取值含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PREPARE]{lang="EN-US"}]{#struct_0_x1489_93403_221337974}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[绑定成功]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[等待回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LISTEN]{lang="EN-US"}]{#struct_0_x1489_93403_1628252218}[：表示协议]{lang="EN-US" style="font-family:宋体"}[Exchange]{lang="EN-US"}[监听连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ESTABLISHED]{lang="EN-US"}]{#struct_0_x1489_93403_931994968}[：表示连接建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS]{lang="EN-US"}]{#struct_0_x1489_93403_x158051253}[：表示连接超时或出错后发送了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BA_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1740669691}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS]{lang="EN-US"}[并回应了]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[ACC ACK]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABTS_ACK]{lang="EN-US"}]{#struct_0_x1489_93403_221403510}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[ABTS ACK]{lang="EN-US"}[，正在等待]{lang="EN-US" style="font-family:宋体"}[BA_ACC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CLOSED]{lang="EN-US"}]{#struct_0_x1489_93403_x1204922763}[：表示连接关闭]{lang="EN-US" style="font-family:宋体"}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1583296991}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x161521438}[索引]{style="font-family:宋体"}

[[MngID]{lang="EN-US"}]{#struct_0_x1489_93403_1149801919}

[[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_221469046}[管理器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1489_93403_1897724136}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1083583163}[协议号（]{style="font-family:宋体"}[0]{lang="EN-US"}[为无效值）]{style="font-family:宋体"}

[[src]{lang="EN-US"}]{#struct_0_x1489_93403_x2024472018}

[[源]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_221534582}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}

[[dst]{lang="EN-US"}]{#struct_0_x1489_93403_x9087532}

[[目的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1645780493}[地址及]{style="font-family:宋体"}[Exchange ID]{lang="EN-US"}

[[Seq_ID]{lang="EN-US"}]{#struct_0_x1489_93403_522404731}

[[Exchange]{lang="EN-US"}]{#struct_0_x1489_93403_221600118}[报文序号]{style="font-family:宋体"}

[[R_CTL]{lang="EN-US"}]{#struct_0_x1489_93403_1025737729}

[[路由控制字段（]{style="font-family:宋体"}[Routing Control]{lang="EN-US"}]{#struct_0_x1489_93403_859422438}[）]{style="font-family:宋体"}

[[F_CTL]{lang="EN-US"}]{#struct_0_x1489_93403_x953793301}

[[报文控制字段（]{style="font-family:宋体"}[Frame Control]{lang="EN-US"}]{#struct_0_x1489_93403_221665654}[）]{style="font-family:宋体"}

[[FC Class]{lang="EN-US"}]{#struct_0_x1489_93403_1380639264}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x659339539}[连接服务级别]{style="font-family:宋体"}

[ ]{lang="EN-US" style="background:white"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_771891841}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_220682614}[打开]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc exchange error]{lang="EN-US"}]{#struct_0_x1489_93403_x677183589}

[\*Jun 10 14:23:07:630 2011 Sysname FCEXCH/7/FCEXCH_ERR: -MDC=1;]{lang="EN-US"}

[Time(s):1307715787  FCEXCH Output:]{lang="EN-US"}

[(Error: Failed to receive ACK for packet)]{lang="EN-US"}

[VSAN ID         : (1)]{lang="EN-US"}

[Protocol        : (14)]{lang="EN-US"}

[Local           : (0x040506:26)]{lang="EN-US"}

[Remote          : (0x010203:25)]{lang="EN-US"}

[State           : (ESTABLISHED)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_672036494}*[没有收到对端的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，打印错误信息和当前]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[相关状态信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1296778063}[打开]{style="font-family:宋体"}[FC Exchange]{lang="EN-US"}[的报文调试信息开关。客户端和服务器端收发报文调试信息如下。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc exchange packet]{lang="EN-US"}]{#struct_0_x1489_93403_220748150}

[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}

[Time(s):1307717555  FCEXCH Output(state = PREPARE):]{lang="EN-US"}

[ FC Packet: src = 0x010203:35, dst = 0x040506:65535]{lang="EN-US"}

[            Seq_ID = 1, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0x02, F_CTL = 0x293000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 14, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_504269960}*[客户端发送报文，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_1842171147}

[Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x010203:35, dst = 0x040506:65535]{lang="EN-US"}

[            Seq_ID = 1, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0x02, F_CTL = 0x293000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 14, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_420853846}*[服务器端接收报文，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_308130792}

[Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x040506:36, dst = 0x010203:35]{lang="EN-US"}

[            Seq_ID = 1, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0xc1, F_CTL = 0xe80000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_221206899}*[服务器端回应]{style="font-family:宋体"}[ACK]{lang="EN-US"}[，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_2041617781}

[Time(s):1307717555  FCEXCH Input(state = PREPARE):]{lang="EN-US"}

[ FC Packet: src = 0x040506:36, dst = 0x010203:35]{lang="EN-US"}

[            Seq_ID = 1, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0xc1, F_CTL = 0xe80000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_486404232}*[客户端接收]{style="font-family:宋体"}[ACK]{lang="EN-US"}[，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_x1542772739}

[Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x040506:36, dst = 0x010203:35]{lang="EN-US"}

[            Seq_ID = 2, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0x02, F_CTL = 0xa93000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_462349073}*[服务器端回应报文，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:381 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_221272435}

[Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x040506:36, dst = 0x010203:35]{lang="EN-US"}

[            Seq_ID = 2, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0x02, F_CTL = 0xa93000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1636354804}*[客户端接收报文，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:382 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_1298219729}

[Time(s):1307717555  FCEXCH Output(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x010203:35, dst = 0x040506:36]{lang="EN-US"}

[            Seq_ID = 2, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0xc1, F_CTL = 0x680000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1619509382}*[客户端回应]{style="font-family:宋体"}[ACK]{lang="EN-US"}[，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jun 10 14:52:35:382 2011 Sysname FCEXCH/7/FCEXCH_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_1863770595}

[Time(s):1307717555  FCEXCH Input(state = ESTABLISHED):]{lang="EN-US"}

[ FC Packet: src = 0x010203:35, dst = 0x040506:36]{lang="EN-US"}

[            Seq_ID = 2, ]{lang="EN-US"}[R_CTL]{lang="PT-BR"}[ = 0xc1, F_CTL = 0x680000, FC Class = FC_CLASS_F]{lang="EN-US"}

[            Protocol = 0, MngID = 0, VSAN = 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_221337971}*[服务器端接收]{style="font-family:宋体"}[ACK]{lang="EN-US"}[，打印报文基本信息和]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[状态信息]{style="font-family:宋体"}*

::: {#1852578671 .myid}
[]{#_Toc404797582}[]{#struct_0_x1489_93403_1628252221}[]{#_Toc295486837}[]{#_Toc248720181}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc forward**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_932584789}

[**[debugging]{lang="EN-US"}**[ **fc forward** **packet**]{lang="EN-US"}]{#struct_0_x1489_93403_181525964}

[**[undo]{lang="EN-US"}**[ **debugging** **fc** **forward** **packet**]{lang="EN-US"}]{#struct_0_x1489_93403_1344550312}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1031422772}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x302187062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1050653014}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_221403507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_751392380}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_190156470}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_127661491}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x588904656}

[**[debugging fc forward]{lang="DE"}**]{#struct_0_x1489_93403_x201844811}[命令用来打开]{style="font-family:宋体"}[FC]{lang="DE"}[转发调试信息开关。]{style="font-family:宋体"}**[undo debugging fc forward]{lang="DE"}**[命令用来关闭]{style="font-family:宋体"}[FC]{lang="DE"}[转发调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_883344465}[转发调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging fc forward packet]{lang="EN-US"}]{#struct_0_x1489_93403_74669009}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1274053997}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_221469043}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1897724133}

[[S_ID]{lang="EN-US"}]{#struct_0_x1489_93403_1083255483}

[[源]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_279297715}[地址]{style="font-family:宋体"}

[[D_ID]{lang="EN-US"}]{#struct_0_x1489_93403_x598163590}

[[目的]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_221534579}[地址]{style="font-family:宋体"}

[[Seq_Cnt]{lang="EN-US"}]{#struct_0_x1489_93403_328619481}

[[分片报文编号]{style="font-family:宋体"}]{#struct_0_x1489_93403_x847625922}

[[Receiving the packet on interface *interface-name*]{lang="EN-US"}]{#struct_0_x1489_93403_562475965}

[[从指定接口接收报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1540277000}

[[Sending the local packet out of interface *interface-name*]{lang="EN-US"}]{#struct_0_x1489_93403_221600115}

[[本机报文从指定接口发送]{style="font-family:宋体"}]{#struct_0_x1489_93403_1025737742}

[[Sending the packet out of interface *interface-name*]{lang="EN-US"}]{#struct_0_x1489_93403_859750120}

[[报文从指定接口发送]{style="font-family:宋体"}]{#struct_0_x1489_93403_1290468693}

[ ]{lang="EN-US" style="background:white"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1662235480}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1555719412}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[转发报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc forward packet]{lang="EN-US"}]{#struct_0_x1489_93403_221665651}

[\*Jun 10 16:04:43:021 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;]{lang="EN-US"}

[ FC Packet: S_ID = 0x040506, D_ID = 0x010203, Seq_Cnt = 0, Receiving the packet on interface Fc1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1380639261}*[从]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口接收报文，打印报文基本信息]{style="font-family:宋体"}*

[[\*Jun 10 16:04:43:022 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_x659142931}

[ FC Packet: S_ID = 0x010203, D_ID = 0x040506, Seq_Cnt = 0, Sending the local packet out of interface Fc1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x12449584}*[本机报文从]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口发送，打印报文基本信息]{style="font-family:宋体"}*

[[\*Jun 10 16:04:43:022 2011 Sysname FCFWD/7/FCFWD_PKT: -MDC=1;]{lang="EN-US"}]{#struct_0_x1489_93403_x1650678901}

[ FC Packet: S_ID = 0x010203, D_ID = 0x040506, Seq_Cnt = 0, Sending the packet out of interface Fc1/0/1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x461728507}*[从]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口发送报文，打印报文基本信息]{style="font-family:宋体"}*

::: {#-948456085 .myid}
[]{#_Toc404797583}[]{#struct_0_x1489_93403_220682611}[]{#_Toc296953421}[]{#_Toc248640987}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc link**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x677183592}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_672757389}[交换机]{style="font-family:宋体"}[/FCF-NPV]{lang="EN-US"}[交换机：]{style="font-family:宋体"}

[**[debugging fc link]{lang="EN-US"}**[ { **all** \| **elp** \| **error** \| **esc** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_1229353823}

[**[undo debugging fc link]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **all** \| **elp** \| **error** \| **esc** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1964731946}

[[NPV]{lang="FR"}]{#struct_0_x1489_93403_2100130449}[交换机：]{style="font-family:宋体"}

[**[debugging fc link]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1522526460}

[**[undo debugging fc link]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **all** \| **error** \| **event** \| **evfp** \| **login-out** \| **packet** \| **timer** } \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x971721730}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_220748147}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1452045177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_894028036}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1152343455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x118372512}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1944459001}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_654839564}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[elp]{lang="EN-US"}**]{#struct_0_x1489_93403_x970274848}[：表示链路协商]{style="font-family:宋体"}[ELP]{lang="EN-US"}[协议调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_221206900}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[esc]{lang="EN-US"}**]{#struct_0_x1489_93403_x1496569631}[：表示交换机能力协商]{style="font-family:宋体"}[ESC]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_x1268967482}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[evfp]{lang="EN-US"}**]{#struct_0_x1489_93403_520694072}[：表示]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[参数协商]{style="font-family:宋体"}[EVFP]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}

[**[login-out]{lang="EN-US"}**]{#struct_0_x1489_93403_x705949219}[：表]{style="font-family:宋体"}[示]{style="font-family:宋体"}[FLOGI/FDISC/LOGO]{lang="EN-US"}[协议的]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x699462856}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_1154628851}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1489_93403_221272436}[：]{style="font-family:宋体"}[表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1636354807}

[**[debugging fc link]{lang="EN-US"}**]{#struct_0_x1489_93403_1298154193}[命令用来打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路调试信息开关。]{style="font-family:宋体"}**[undo debugging fc link]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_634989299}[链路调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，通过]{style="font-family:宋体"}**[interface]{lang="EN-US"}**]{#struct_0_x1489_93403_x447663052}[参数]{style="font-family:宋体"}[打开的]{style="font-family:宋体"}[指定接口的调试信息开关，只能通过在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令中指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数来关闭。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging fc link elp]{lang="EN-US"}]{#struct_0_x1489_93403_1736592618}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1273679757}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_221337972}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1628252224}

[[Interface *interface-name*: Successfully sent ELP request frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_932781397}

[[发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x810831802}[请求报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send ELP request frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1292590726}

[[发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221403508}[请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Sent ELP RJT frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_751392365}

[[发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_2101841593}[拒绝报文]{style="font-family:宋体"}

[[Interface *interface*-*name*: ELP negotiation succeeded and sent ACC frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x354383099}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_763466848}[协商成功并发送响应报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received ELP request frames with invalid length in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_221469044}

[[收到长度不合法的]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_1897724138}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received ELP request frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1083714235}

[[收到]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_706627968}[请求报文]{style="font-family:宋体"}

[[Interface *interface*-*name*: Received ELP RJT frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_221534580}

[[收到]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x9087534}[拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive ELP request ACK event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1263443469}

[[接收]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x130174697}[请求报文的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[事件失败]{style="font-family:宋体"}

[[Interface *interface-name*: Received ELP ACC frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1077612445}

[[收到]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221600116}[响应报文]{style="font-family:宋体"}

[[Interface *interface*-*name*: Received ELP ACC frames with invalid length in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1025737743}

[[收到长度不合法的]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_859815656}[响应报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received ELP RJT frames with invalid length in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1630905456}

[[收到长度不合法的]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221665652}[拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received exchange ACK event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1380639258}

[[收到]{style="font-family:宋体"}[exchange ACK]{lang="EN-US"}]{#struct_0_x1489_93403_x658553106}[事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received exchange error event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_220682612}

[[收到]{style="font-family:宋体"}[exchange error]{lang="EN-US"}]{#struct_0_x1489_93403_x677183591}[事件]{style="font-family:宋体"}

[[Interface *interface-name:* The mode of the responder is F or NP in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_672560781}

[[响应端接口模式为]{style="font-family:宋体"}[F]{lang="EN-US"}]{#struct_0_x1489_93403_x112615272}[或]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get ELP attributes in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_220748148}

[[获取]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1452045184}[接口属性失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get ELP local parameters.]{lang="EN-US"}]{#struct_0_x1489_93403_x672776801}

[[获取]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_1721155139}[本地参数信息失败]{style="font-family:宋体"}

[[Interface *interface-name*: The result of ELP parameter negotiation is *error-flag*.]{lang="EN-US"}]{#struct_0_x1489_93403_221206897}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_2041617795}[参数选择结果是]{style="font-family:宋体"}*[error-flag]{lang="EN-US"}*[，]{style="font-family:宋体"}*[error-flag]{lang="EN-US"}*[含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1489_93403_486142089}[：参数协商成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1489_93403_221272433}[：获取本端接口参数失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1489_93403_1636354802}[：流控参数协商失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1489_93403_1297826513}[：协议版本不匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1489_93403_221337969}[：对端非]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1489_93403_x328062907}[：定时器超时时间不匹配]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1489_93403_961472938}[：端口]{lang="EN-US" style="font-family:宋体"}[WWN]{lang="EN-US"}[相同]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1489_93403_450712352}[：交换机]{lang="EN-US" style="font-family:宋体"}[WWN]{lang="EN-US"}[相同]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x1489_93403_221403505}[：]{style="font-family:宋体"}[class f]{lang="EN-US"}[参数协商失败，且不可二次协商]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x1489_93403_751392378}[：]{lang="EN-US" style="font-family:宋体"}[class2\\class3]{lang="EN-US"}[参数协商失败，且不可二次协商]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x1489_93403_x236810578}[：]{lang="EN-US" style="font-family:宋体"}[class2\\class3]{lang="EN-US"}[参数协商失败，可二次协商]{lang="EN-US" style="font-family:宋体"}

[[Interface *interface-name*: ELP flow control parameters are inconsistent.]{lang="EN-US"}]{#struct_0_x1489_93403_221469041}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_1897724135}[流控参数不一致]{style="font-family:宋体"}

[[Interface *interface-name*: ELP versions are inconsistent.]{lang="EN-US"}]{#struct_0_x1489_93403_1083386555}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221534577}[版本信息不一致]{style="font-family:宋体"}

[[Interface *interface-name*: Peer ELP port is not a E_Port.]{lang="EN-US"}]{#struct_0_x1489_93403_328619471}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x127581890}[对端不为]{style="font-family:宋体"}[E]{lang="EN-US"}[端口]{style="font-family:宋体"}

[[Interface *interface-name*: R_A_TOV or E_D_TOV mismatched.]{lang="EN-US"}]{#struct_0_x1489_93403_221600113}

[[定时器不匹配]{style="font-family:宋体"}]{#struct_0_x1489_93403_1025737740}

[[Interface *interface-name*: The names of two ports are equal]{lang="EN-US"}]{#struct_0_x1489_93403_859881192}

[[两端端口名相同]{style="font-family:宋体"}]{#struct_0_x1489_93403_221665649}

[[Interface *interface-name*: The names of two switches are equal]{lang="EN-US"}]{#struct_0_x1489_93403_x958012907}

[[两端交换机名相同]{style="font-family:宋体"}]{#struct_0_x1489_93403_293537903}

[[Interface *interface-name*: Class F non-negotiable service parameters error.]{lang="EN-US"}]{#struct_0_x1489_93403_220682609}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_1279131552}[参数协商时]{style="font-family:宋体"}[CLASS F]{lang="EN-US"}[不可协商参数不一致]{style="font-family:宋体"}

[[Interface *interface-name*: Class N non-negotiable service parameters error.]{lang="EN-US"}]{#struct_0_x1489_93403_419414098}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_220748145}[参数协商时]{style="font-family:宋体"}[CLASS N]{lang="EN-US"}[不可协商参数不一致]{style="font-family:宋体"}

[[Interface *interface-name*: Class N negotiable service parameters error.]{lang="EN-US"}]{#struct_0_x1489_93403_x1452045179}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_443689342}[参数协商时]{style="font-family:宋体"}[CLASS N]{lang="EN-US"}[可协商参数不一致]{style="font-family:宋体"}

[[Interface *interface-name*: ELP negotiation succeeded in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_221206898}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_2041617780}[协商成功]{style="font-family:宋体"}

[[Interface *interface-name*: Started the second ELP negotiation in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_486338696}

[[发起]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221272434}[二次协商]{style="font-family:宋体"}

[[Interface *interface-name*: ELP negotiation launches at two ports simultaneously in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1636354805}

[[两端同时发起]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_221337970}[协商]{style="font-family:宋体"}

[[Interface *interface-name*: ELP responder started R_A_TOV in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1628252222}

[[响应端启动资源分配定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_932388181}

[[Interface *interface-name*: The receiver is waiting for ACK of SW_ACC or SW_RJT, so the receiver should drop the ELP request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_221403506}

[[当前正在等]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x1489_93403_751392379}[，丢弃第二次收到的]{style="font-family:宋体"}[ELP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

*[ ]{lang="EN-US"}*

[]{#struct_0_x1489_93403_x236810579}[[表1-9 ]{lang="EN-US"}[debugging fc link error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1266195661}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_221469042}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1897724132}

[[Interface *interface-name*: Failed to create ELP R_A_TOV in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1083321019}

[[创建]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_1489562673}[资源分配定时器失败]{style="font-family:宋体"}

[[Interface *interface-name*: ELP failed to send ACC frames in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1926984300}

[[发送响应报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_221534578}

[[Interface *interface-name*: Failed to start R_A_TOV for second negotiation in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_328619482}

[[二次协商启动资源分配定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x847625921}

[[Interface *interface-name*: Received an invalid event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_562279357}

[[收到的事件不合法]{style="font-family:宋体"}]{#struct_0_x1489_93403_164200788}

[[Interface *interface-name*: Failed to get the state of state machine in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_221600114}

[[获取状态机状态失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1025737741}

[[Interface *interface-name*: Failed to malloc memory in VSAN *vsan-id*. ]{lang="EN-US"}]{#struct_0_x1489_93403_859946728}

[[申请内存失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x465967516}

[[Interface *interface-name*: Failed to get the physical state machine.]{lang="EN-US"}]{#struct_0_x1489_93403_x5287449}

[[获取物理状态机失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_221665650}

[[Interface *interface-name*: Failed to send ESC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1380639260}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x659077395}[发送请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create ESC request timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1916812960}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_220682610}[发起端创建定时器失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create ESC responder timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x677183593}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_672691853}[响应端创建定时器失败]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP failed to get local switch WWN. ]{lang="EN-US"}]{#struct_0_x1489_93403_x1503151144}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_220748146}[获取本端交换机]{style="font-family:宋体"}[WWN]{lang="EN-US"}[值失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to add trunk list to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_x1452045178}

[[将]{style="font-family:宋体"}[trunk list]{lang="EN-US"}]{#struct_0_x1489_93403_2009773283}[下驱动失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to set tag mode to kernel.]{lang="EN-US"}]{#struct_0_x1489_93403_x721640793}

[[Tag]{lang="EN-US"}]{#struct_0_x1489_93403_2143521202}[模式下内核失败]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP failed to create a timer.]{lang="EN-US"}]{#struct_0_x1489_93403_2082909203}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_736377195}[创建定时器失败]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP failed to create link socket.]{lang="EN-US"}]{#struct_0_x1489_93403_x1833259495}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_2143586738}[创建]{style="font-family:宋体"}[link socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send EVFP request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1434616877}

[[发送]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_548423827}[请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get WWN]{lang="EN-US"}]{#struct_0_x1489_93403_2143652274}

[[获取端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_x1828499868}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to allocate memory.]{lang="EN-US"}]{#struct_0_x1489_93403_1953260546}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x46586537}

[[Interface *interface-name*: Failed to add access VSAN to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_2143717810}

[[添加端口]{style="font-family:宋体"}[ACCESS VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_1731653678}[到驱动失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to delete access VSAN from driver.]{lang="EN-US"}]{#struct_0_x1489_93403_x1339651730}

[[删除端口]{style="font-family:宋体"}[ACCESS VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_2143783346}[到驱动失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to add trunk VSAN to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_x1440169313}

[[添加端口]{style="font-family:宋体"}[Trunk VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_840117609}[到驱动失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to delete trunk VSAN from driver.]{lang="EN-US"}]{#struct_0_x1489_93403_2143848882}

[[删除端口]{style="font-family:宋体"}[Trunk VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_x1449993427}[到驱动失败]{style="font-family:宋体"}

[[Interface *interface-name*: Physical state is down, and it cannot send packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1479412380}

[[物理状态]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x1489_93403_2143914418}[，发送失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1835900001}

[[端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x119560063}[发送报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create login logical state machine in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143979954}

[[创建]{style="font-family:宋体"}[login]{lang="EN-US"}]{#struct_0_x1489_93403_x1061924998}[的逻辑状态机失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create timer in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1126848634}

[[创建定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_2142996914}

[[Interface *interface-name*: EEVFP failed to create link socket.]{lang="EN-US"}]{#struct_0_x1489_93403_540375657}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x182649662}[创建]{style="font-family:宋体"}[link socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: EEVFP failed to send request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143062450}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x670544348}[发送请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: EEVFP failed to create a timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x521612081}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_2143521203}[创建定时器失败]{style="font-family:宋体"}

[[Failed to back up in batch for HA.]{lang="EN-US"}]{#struct_0_x1489_93403_2082974739}

[[HA]{lang="EN-US"}]{#struct_0_x1489_93403_2143586739}[批备失败]{style="font-family:宋体"}

[[Failed to upgrade for HA]{lang="EN-US"}]{#struct_0_x1489_93403_x1434551341}

[[HA]{lang="EN-US"}]{#struct_0_x1489_93403_340541290}[升级失败]{style="font-family:宋体"}

[[Failed to send real-time backup data.]{lang="EN-US"}]{#struct_0_x1489_93403_2143652275}

[[发送实备数据失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1828565404}

[ ]{lang="EN-US"}

[]{#struct_0_x1489_93403_309287749}[[表1-10 ]{lang="EN-US"}[debugging fc link esc]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1290929645}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1235796821}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_2143717811}

[[Interface *interface-name*: Received ESC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1731588142}

[[收到]{style="font-family:宋体"}[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x1342785205}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received RJT frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1603209665}

[[收到拒绝报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2023217109}

[[Interface *interface-name*: Received ACK event.]{lang="EN-US"}]{#struct_0_x1489_93403_2143783347}

[[接收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x1489_93403_x1440103777}[事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received RJT frames of invalid size.]{lang="EN-US"}]{#struct_0_x1489_93403_x453574113}

[[接收到的拒绝报文大小不合法]{style="font-family:宋体"}]{#struct_0_x1489_93403_593108991}

[[Interface *interface-name*: The ESC responder switch supports VSAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x379374509}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_2143848883}[响应端支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Interface *interface-name*: The ESC responder switch doesn't support VSAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x1449927891}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_82589659}[响应端不支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive ESC ACC frames for invalid length.]{lang="EN-US"}]{#struct_0_x1489_93403_1888029}

[[收到的报文长度不合法]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1958201480}

[[Interface *interface-name*: Failed to send ESC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143914419}

[[发送]{style="font-family:宋体"}[ESC ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1835965537}[报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: The state machine is in the EIsolate state.]{lang="EN-US"}]{#struct_0_x1489_93403_3079386}

[[状态机为]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_1473568937}[隔离状态]{style="font-family:宋体"}

[[Interface *interface-name*: The ESC initiator switch doesn't support VSAN.]{lang="EN-US"}]{#struct_0_x1489_93403_2143979955}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x1061990534}[发起端不支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Interface *interface-name*: Received error ESC frames with partial descriptors.]{lang="EN-US"}]{#struct_0_x1489_93403_x1976455473}

[[收到描述符不完整的]{style="font-family:宋体"}[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x830110739}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received error ESC frames of invalid size.]{lang="EN-US"}]{#struct_0_x1489_93403_2142996915}

[[收到大小错误的]{style="font-family:宋体"}[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_540310121}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x1489_93403_x1730705565}[[表1-11 ]{lang="EN-US"}[debugging fc link event]{lang="EN-US"}]{#_Toc130718929}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1283885613}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2140506986}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_789375647}

[[Interface *interface-name*: Received the failure of negotiation in init state and transited to Isolate state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143062451}

[[Init]{lang="EN-US"}]{#struct_0_x1489_93403_x670478812}[状态下收到了协商失败的事件并转化为]{style="font-family:宋体"}[isolate]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of ELP negotiation in Init state and transited to E state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1903779239}

[[Init]{lang="EN-US"}]{#struct_0_x1489_93403_x800965377}[状态下收到]{style="font-family:宋体"}[ELP]{lang="EN-US"}[协商成功事件并转化为]{style="font-family:宋体"}[E]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Interface *interface-name*: Received logout in F state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1640220471}

[[F]{lang="EN-US"}]{#struct_0_x1489_93403_2143521200}[状态下收到了]{style="font-family:宋体"}[logout]{lang="EN-US"}[的事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received the failure of login negotiation in Init state and transited to FIsolate state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2082778131}

[[Init]{lang="EN-US"}]{#struct_0_x1489_93403_x50936325}[状态下收到]{style="font-family:宋体"}[login]{lang="EN-US"}[协商失败事件并转化为]{style="font-family:宋体"}[F]{lang="EN-US"}[隔离状态]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of login negotiation in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1192002432}

[[收到]{style="font-family:宋体"}[login]{lang="EN-US"}]{#struct_0_x1489_93403_2143586736}[协商成功事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of ESC negotiation in E state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1435010093}

[[E]{lang="EN-US"}]{#struct_0_x1489_93403_x1505987072}[状态下收到了]{style="font-family:宋体"}[ESC]{lang="EN-US"}[协商成功的事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of ESC negotiation in F/NP state.]{lang="EN-US"}]{#struct_0_x1489_93403_875287869}

[[F]{lang="EN-US"}]{#struct_0_x1489_93403_x220732304}[或]{style="font-family:宋体"}[NP]{lang="EN-US"}[状态下收到了]{style="font-family:宋体"}[ESC]{lang="EN-US"}[协商成功的事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received ELP frames in Isolate or E state and transited to Init state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143652272}

[[在]{style="font-family:宋体"}[Isolate]{lang="EN-US"}]{#struct_0_x1489_93403_x1828106652}[或]{style="font-family:宋体"}[E]{lang="EN-US"}[状态下收到了]{style="font-family:宋体"}[ELP]{lang="EN-US"}[报文并转化为]{style="font-family:宋体"}[Init]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of EVFP negotiation in E state.]{lang="EN-US"}]{#struct_0_x1489_93403_x339998989}

[[接口在]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_1833863128}[状态下收到]{style="font-family:宋体"}[EVFP]{lang="EN-US"}[协商成功的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Received the success of EEVFP negotiation in F or NP state.]{lang="EN-US"}]{#struct_0_x1489_93403_2143717808}

[[接口在]{style="font-family:宋体"}[F]{lang="EN-US"}]{#struct_0_x1489_93403_1731129391}[或]{style="font-family:宋体"}[NP]{lang="EN-US"}[状态下收到]{style="font-family:宋体"}[EEVFP]{lang="EN-US"}[协商成功的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Received VSAN up message in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_583943471}

[[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_x1888538066}[模块收到]{style="font-family:宋体"}[VSAN up]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Interface *interface-name*: Received VSAN down message in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143783344}

[[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_x1440038241}[模块收到]{style="font-family:宋体"}[VSAN down]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Interface *interface-name*: VSAN *vsan-id* does not exist or is not in trunk list.]{lang="EN-US"}]{#struct_0_x1489_93403_1155354237}

[[当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x654814517}[不存在或者这个]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[不在当前接口的]{style="font-family:宋体"}[trunk list]{lang="EN-US"}[内]{style="font-family:宋体"}

[[Interface *interface-name*: Logical state machine does not exist in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143848880}

[[当前接口当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1449862355}[的逻辑状态机不存在]{style="font-family:宋体"}

[[Interface *interface-name*: Received all VSAN down message.]{lang="EN-US"}]{#struct_0_x1489_93403_x646452654}

[[当前接口收到所有]{style="font-family:宋体"}[VSAN down]{lang="EN-US"}]{#struct_0_x1489_93403_x743888868}[的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Received getting trunk VSAN message.]{lang="EN-US"}]{#struct_0_x1489_93403_2143914416}

[[当前接口收到获取]{style="font-family:宋体"}[trunk VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1834982497}[的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Sent valid trunk VSAN message.]{lang="EN-US"}]{#struct_0_x1489_93403_115179414}

[[当前接口要发送本接口]{style="font-family:宋体"}[trunk VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2143979952}[信息]{style="font-family:宋体"}

[[Interface *interface-name*: FCoE module has not registered any event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1061793926}

[[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_766821781}[未注册任何事件]{style="font-family:宋体"}

[[Interface *interface-name*: Set to *mode* and *linkstate* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1263506879}

[[设置该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2142996912}[内端口模式和链路状态]{style="font-family:宋体"}

[[Interface *interface-name*: Isolated in VSAN *vsan-id*, reason id *reason-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_540244585}

[[端口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1327474060}[内隔离，原因码为]{style="font-family:宋体"}*[reason-id]{lang="EN-US"}*

[[Interface *interface-name*: Clear isolation info of all VSANs.]{lang="EN-US"}]{#struct_0_x1489_93403_2143062448}

[[清除所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x671068637}[内的隔离信息]{style="font-family:宋体"}

[[Interface *interface-name*: Unisolated in VSAN *vsan-id*, reason id *reason-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x458203963}

[[端口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2143521201}[内去隔离，原因码为]{style="font-family:宋体"}*[reason-id reason-id]{lang="EN-US"}*[含义如下：]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_x1489_93403_2082843667}[：]{lang="EN-US" style="font-family:宋体"}[Fabric]{lang="EN-US"}[原因导致隔离]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[1]{lang="EN-US"}]{#struct_0_x1489_93403_2143586737}[：]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[原因导致隔离]{style="font-family:宋体"}

[[Interface *interface-name:* Received the failure of EEVFP negotiation in F or NP state and transited to Isolate state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1434944557}

[[当前接口在]{style="font-family:宋体"}[F/NP]{lang="EN-US"}]{#struct_0_x1489_93403_x1076412859}[状态下收到]{style="font-family:宋体"}[EEVFP]{lang="EN-US"}[失败事件并隔离]{style="font-family:宋体"}

[[Interface *interface-name*: Received VSAN deletion event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143652273}

[[收到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1828172188}[删除事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received VSAN creation event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2086133657}

[[收到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2143717809}[创建事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received switch WWN change event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1731063855}

[[收到交换机]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_1802275258}[变化事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received timer change event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2143783345}

[[收到]{style="font-family:宋体"}[VSAN timer]{lang="EN-US"}]{#struct_0_x1489_93403_x1439972705}[变化事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received domain ID change event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1577231001}

[[收到]{style="font-family:宋体"}[domain ID]{lang="EN-US"}]{#struct_0_x1489_93403_2143848881}[变化事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received fabric name change event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1449796819}

[[收到]{style="font-family:宋体"}[Fabric name]{lang="EN-US"}]{#struct_0_x1489_93403_2143914417}[变化事件]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create LOGO request socket in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1835048033}

[[创建]{style="font-family:宋体"}[LOGO]{lang="EN-US"}]{#struct_0_x1489_93403_148381251}[请求的]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x1489_93403_2143979953}[[表1-12 ]{lang="EN-US"}[debugging fc link evfp]{lang="EN-US"}]{#_Toc130718930}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1276886669}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1061859462}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_694646808}

[[Interface *interface-name*: Launched EVFP_COMMIT negotiation.]{lang="EN-US"}]{#struct_0_x1489_93403_333957805}

[[发起]{style="font-family:宋体"}[EVFP COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_x1630621229}[阶段协商]{style="font-family:宋体"}

[[Interface *interface-name*: Encapsulated EVFP_SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1154891690}

[[封装]{style="font-family:宋体"}[EVFP SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_2142996913}[阶段的请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received EVFP_SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_540179049}

[[收到]{style="font-family:宋体"}[EVFP SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_x829877370}[阶段请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received EVFP_COMMIT request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1458343230}

[[收到]{style="font-family:宋体"}[EVFP COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_1339410278}[阶段请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received EVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143062449}

[[收到]{style="font-family:宋体"}[EVFP SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_x671003101}[阶段]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received RJT frames.]{lang="EN-US"}]{#struct_0_x1489_93403_657487413}

[[收到拒绝报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_328788722}

[[Interface *interface-name*: Successfully added trunk list to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_2143521198}

[[将]{style="font-family:宋体"}[trunk list]{lang="EN-US"}]{#struct_0_x1489_93403_125938698}[下驱动成功]{style="font-family:宋体"}

[[Interface *interface-name*: Received ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x2081592950}

[[接收到]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_524618908}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received sync ACK event.]{lang="EN-US"}]{#struct_0_x1489_93403_2143586734}

[[收到]{style="font-family:宋体"}[sync ACK]{lang="EN-US"}]{#struct_0_x1489_93403_x1434879021}[事件]{style="font-family:宋体"}

[[Interface *interface-name*: Received commit ACK event.]{lang="EN-US"}]{#struct_0_x1489_93403_1691823987}

[[收到]{style="font-family:宋体"}[commit ACK]{lang="EN-US"}]{#struct_0_x1489_93403_207682011}[事件]{style="font-family:宋体"}

[[Interface *interface-name*: Responded to EVFP_SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143652270}

[[响应]{style="font-family:宋体"}[EVFP_SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_x1828237724}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Responded to EVFP_COMMIT request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1929583765}

[[响应]{style="font-family:宋体"}[EVFP_COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_x1463316216}[请求报文]{style="font-family:宋体"}

[[The WWN of the local end is greater than that of the peer end.]{lang="EN-US"}]{#struct_0_x1489_93403_2143717806}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_1732046895}[并发时本端的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[比对端大]{style="font-family:宋体"}

[[The WWN of the local end is smaller than that of the peer end.]{lang="EN-US"}]{#struct_0_x1489_93403_1700473821}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1164005684}[并发时本端的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[比对端小]{style="font-family:宋体"}

[[The WWN of the local end equals that of the peer end.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1489_93403_2143783342}

[[EVFP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1489_93403_x1440431457}[并发时本端的]{style="font-size:9.0pt;font-family:宋体"}[WWN]{lang="EN-US" style="font-size:9.0pt"}[与对端相等]{style="font-size:9.0pt;
  font-family:宋体"}

[[Interface *interface-name*: EVFP negotiated the VSAN tagging mode as non-tagging but the two ends had different access VSAN IDs.]{lang="EN-US"}]{#struct_0_x1489_93403_x865334759}

[[两端]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_1559163732}[协商后]{style="font-family:宋体"}[trunk]{lang="EN-US"}[模式为]{style="font-family:宋体"}[non-tagging]{lang="EN-US"}[，但两端的]{style="font-family:宋体"}[access VSAN]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Interface *interface-name:* Common trunk VSAN lists on both sides are empty after EVFP negotiation.]{lang="EN-US"}]{#struct_0_x1489_93403_2143848878}

[[两端]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1449338068}[协商后公共]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[列表为空]{style="font-family:宋体"}

[[Interface *interface-name*: Local WWN is smaller than the peer WWN.]{lang="EN-US"}]{#struct_0_x1489_93403_x1931921839}

[[本端]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_2143914414}[小于对端]{style="font-family:宋体"}

[[Interface *interface-name*: Rejected frames received in incorrect phase.]{lang="EN-US"}]{#struct_0_x1489_93403_x1835113569}

[[拒绝在错误阶段收到的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1884631521}

[[Interface *interface-name*: Rejected received frames with incorrect state.]{lang="EN-US"}]{#struct_0_x1489_93403_2143979950}

[[拒绝收到的状态错误的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1061662854}

[[Interface *interface-name*: Rejected received frames with incorrect payload.]{lang="EN-US"}]{#struct_0_x1489_93403_564851973}

[[拒绝收到的负载错误的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_2142996910}

[[Interface *interface-name*: Received frames with incorrect version.]{lang="EN-US"}]{#struct_0_x1489_93403_540113513}

[[收到的报文的版本错误]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1631364659}

[[Interface *interface-name*: Received frames with incorrect switch WWN.]{lang="EN-US"}]{#struct_0_x1489_93403_2143062446}

[[收到的报文]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_x670151133}[错误]{style="font-family:宋体"}

[[Interface *interface-name*: Received frames with incorrect length.]{lang="EN-US"}]{#struct_0_x1489_93403_x900362911}

[[收到的报文长度错误]{style="font-family:宋体"}]{#struct_0_x1489_93403_2143521199}

[[Interface *interface-name*: Rejected received frames with incorrect transaction id.]{lang="EN-US"}]{#struct_0_x1489_93403_126004234}

[[拒绝]{style="font-family:宋体"}[transaction ID]{lang="EN-US"}]{#struct_0_x1489_93403_1572158726}[字段错误报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received type-unknown frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143586735}

[[接收到未知类型的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1434813485}

[[Interface *interface-name*: Rejected EVFP_COMMIT frames received before the EVFP_SYNC phase.]{lang="EN-US"}]{#struct_0_x1489_93403_x1927204411}

[[拒绝在]{style="font-family:宋体"}[EVFP_SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_2143652271}[阶段之前收到的]{style="font-family:宋体"}[EVFP_COMMIT]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name:* Discarded the EVFP reply frames received from the invalid interface.]{lang="EN-US"}]{#struct_0_x1489_93403_x1828303260}

[[丢弃从无效端口所接收到的]{style="font-family:宋体"}[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_2126978497}[回应报文]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully set tag mode to kernel.]{lang="EN-US"}]{#struct_0_x1489_93403_2143717807}

[[Tag]{lang="EN-US"}]{#struct_0_x1489_93403_1731981359}[模式下内核成功]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP negotiation succeed.]{lang="EN-US"}]{#struct_0_x1489_93403_2143783343}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1440365921}[协商成功]{style="font-family:宋体"}

[[Interface *interface-name:* Sent EEVFP SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_400496277}

[[发送]{style="font-family:宋体"}[EEVFP SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_2143848879}[阶段请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received EEVFP_SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1449272532}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x645159824}[收到]{style="font-family:宋体"}[SYNC]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name:* Responded to EEVFP_SYNC request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143914415}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1835179105}[响应]{style="font-family:宋体"}[SYNC]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name:* Received EEVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_2143979951}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1061728390}[收到]{style="font-family:宋体"}[EEVFP SYNC ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name:* EEVFP negotiated the VSAN tagging mode as non-tagging but the two ends had different access VSAN IDs.]{lang="EN-US"}]{#struct_0_x1489_93403_136577716}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_2142996911}[协商为]{style="font-family:宋体"}[non-tagging]{lang="EN-US"}[模式但是两端]{style="font-family:宋体"}[access VSAN]{lang="EN-US"}[不同]{style="font-family:宋体"}

[[Interface *interface-name:* Common trunk VSAN lists on both sides are empty after EEVFP negotiation.]{lang="EN-US"}]{#struct_0_x1489_93403_540047977}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_2143062447}[两端协商出来的]{style="font-family:宋体"}[trunk VSAN list]{lang="EN-US"}[为空]{style="font-family:宋体"}

[[Interface *interface-name:* Launched EEVFP_COMMIT negotiation.]{lang="EN-US"}]{#struct_0_x1489_93403_x670085597}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_630218596}[发起]{style="font-family:宋体"}[COMMIT]{lang="EN-US"}[协商]{style="font-family:宋体"}

[[Interface *interface-name:* Sent EEVFP COMMIT request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x585362153}

[[发送]{style="font-family:宋体"}[EEVFP COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_x655205523}[阶段请求报文]{style="font-family:宋体"}

[[Interface *interface-name:* Received EEVFP_COMMIT request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x585296617}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_826158462}[收到]{style="font-family:宋体"}[COMMIT]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name:* Rejected EEVFP_COMMIT frames received before the EEVFP_SYNC phase.]{lang="EN-US"}]{#struct_0_x1489_93403_x585231081}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_1264892122}[拒绝]{style="font-family:宋体"}[SYNC]{lang="EN-US"}[阶段之前收到的]{style="font-family:宋体"}[COMMIT]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name:* Responded to EEVFP_COMMIT request frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1812579332}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x585165545}[响应]{style="font-family:宋体"}[COMMIT]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name:* Discarded the EEVFP reply frames received from the invalid interface.]{lang="EN-US"}]{#struct_0_x1489_93403_2031389545}

[[丢弃从无效端口收到的]{style="font-family:宋体"}[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x585100009}[回应报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging fc link login-out]{lang="EN-US"}]{#struct_0_x1489_93403_x1461304218}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1303960397}[[字段]{style="font-size:9.0pt;font-family:黑体"}]{#struct_0_x1489_93403_740854589}

[[描述]{style="font-size:9.0pt;
   font-family:黑体"}]{#struct_0_x1489_93403_x1430105903}

[[Interface *interface-name*: Successfully sent FLOGI request in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585034473}

[[发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_1626150512}[请求报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI frame with wrong parameters and responded with a RJT frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1637796929}

[[收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_137417527}[报文中的参数不合法，回拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI request frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x692022596}

[[收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x584968937}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI request frame in wrong state and responded with a RJT frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1779916681}

[[收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x998384726}[请求报文时，当前本端所处的模式不正确，回拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI request frame of invalid length and responded with a RJT frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x55445454}

[[收到的]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x584903401}[请求报文的长度不合法，回拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI or FDISC ACC frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_84922547}

[[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1138287577}[或]{style="font-family:宋体"}[FDISC ]{lang="EN-US"}[报文请求端收到]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI ACC frame of invalid parameters in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1969119106}

[[端口收到的]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x585886441}[报文中的参数不合法]{style="font-family:宋体"}

[[Interface *interface-name*: Login succeeded in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_442052255}

[[端口在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1616054329}[内]{style="font-family:宋体"}[login]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Interface *interface-name*: Sent FLOGI ACC frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1891424146}

[[端口发送]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x585820905}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get FCID in VSAN *vsan-id* and sent RJT frame.]{lang="EN-US"}]{#struct_0_x1489_93403_x1030273683}

[[获取]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_x1898169809}[失败，回拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FLOGI RJT packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1372394570}

[[收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x585362152}[拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: The length of FLOGI RJT packet was invalid in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x655271059}

[[收到的]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1633190584}[拒绝报文的长度不合法]{style="font-family:宋体"}

[[Interface *interface-name*: F port was processing former login packet and rejected the FLOGI request packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x706615600}

[[F]{lang="EN-US"}]{#struct_0_x1489_93403_x585296616}[端口收到了]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[请求报文，但是当前正在处理之前的]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}

[[Interface *interface-name*: Received NP LOGO request packet in NP state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_826223998}

[[NP]{lang="EN-US"}]{#struct_0_x1489_93403_1917926754}[端口收到了]{style="font-family:宋体"}[LOGO]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully cleared FCID in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585231080}

[[清除]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_1264957658}[成功]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to clear FCID in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1294893799}

[[清除]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_x1778845221}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully sent LOGO ACC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585165544}

[[发送]{style="font-family:宋体"}[LOGO ACC]{lang="EN-US"}]{#struct_0_x1489_93403_2031324009}[报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Interface was terminated and deleted all login data in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1070320245}

[[端口终止协商且删除该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x585100008}[内所有]{style="font-family:宋体"}[login]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[Interface *interface-name*: The length of LOGO request packet is invalid in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1461369754}

[[LOGO]{lang="EN-US"}]{#struct_0_x1489_93403_1091513796}[请求报文长度不合法]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive LOGO request packet in E state in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585034472}

[[E]{lang="EN-US"}]{#struct_0_x1489_93403_1626216048}[状态下接收]{style="font-family:宋体"}[LOGO]{lang="EN-US"}[请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive LOGO request packet for invalid WWN or FCID in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1616950545}

[[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_x584968936}[或]{style="font-family:宋体"}[FCID]{lang="EN-US"}[不合法导致接收]{style="font-family:宋体"}[LOGO]{lang="EN-US"}[请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully sent LOGO request packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1779982217}

[[发送]{style="font-family:宋体"}[LOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x1426871643}[请求报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully received LOGO ACC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x584903400}

[[接收]{style="font-family:宋体"}[LOGO ACC]{lang="EN-US"}]{#struct_0_x1489_93403_84857011}[报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully received LOGO RJT packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x987505386}

[[接收]{style="font-family:宋体"}[LOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x585886440}[拒绝报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive LOGO request packet because the FC IDs are not equal in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_441986719}

[[FC ID]{lang="EN-US"}]{#struct_0_x1489_93403_x1245093042}[不一致导致接收]{style="font-family:宋体"}[LOGO]{lang="EN-US"}[请求报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Interface was not up in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585820904}

[[端口在该]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1030339219}[没有]{style="font-family:宋体"}[up]{lang="EN-US"}

[[Interface *interface-name*: Successfully sent FLOGI ACC packet in physic negotiation phase.]{lang="EN-US"}]{#struct_0_x1489_93403_x1342646807}

[[在物理协商阶段成功发送]{style="font-family:宋体"}[FLOGI ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x585362155}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FDISC request in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x655598739}

[[收到]{style="font-family:宋体"}[FDISC]{lang="EN-US"}]{#struct_0_x1489_93403_x585296619}[请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: Sent FLOGI or FDISC RJT frame in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_825765246}

[[发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x298625752}[或者]{style="font-family:宋体"}[FDISC]{lang="EN-US"}[拒绝报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[debugging fc link packet]{lang="EN-US"}]{#struct_0_x1489_93403_1068991547}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1292421869}[[字段]{style="font-size:9.0pt;
   font-family:黑体"}]{#struct_0_x1489_93403_x585231083}

[[描述]{style="font-size:9.0pt;
   font-family:黑体"}]{#struct_0_x1489_93403_1264761050}

[[Interface *interface-name*: Sent packets in VSAN *vsan-id* successfully.]{lang="EN-US"}]{#struct_0_x1489_93403_1724958731}

[[端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_2134038417}[发送]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[内的报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Received packets from VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1920904563}

[[从端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x585165547}[的]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[上接收到报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging fc link timer]{lang="EN-US"}]{#struct_0_x1489_93403_2031520617}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1295793645}[[字段]{style="font-size:9.0pt;font-family:黑体"}]{#struct_0_x1489_93403_873859260}

[[描述]{style="font-size:9.0pt;
   font-family:黑体"}]{#struct_0_x1489_93403_1267406740}

[[Interface *interface-name*: R_A_TOV timed out and started the second ELP launch in VSAN *vsan-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_54922982}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1099914346}[资源分配定时器超时并发起二次协商]{style="font-family:宋体"}

[[Interface *interface-name*: ELP E_D_TOV timed out and started R_A_TOV in VSAN *vsan-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x585100011}

[[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1461828507}[错误检测定时器超时并启动资源分配定时器]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully created E_D_TOV in VSAN *vsan-id*. ]{lang="EN-US"}]{#struct_0_x1489_93403_598233179}

[[创建错误检测定时器成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1337205979}

[[Interface *interface-name*: ESC request timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1297778131}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x585034475}[请求端的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name*: ESC reply timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1626019440}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_x899855018}[接收端的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name*: The timer waiting for EVFP SYNC ACC frames timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1293583481}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x584968939}[等待]{style="font-family:宋体"}[SYNC ACC]{lang="EN-US"}[报文的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name*: The timer waiting for EVFP COMMIT ACC frames timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1780309897}

[[EVFP]{lang="EN-US"}]{#struct_0_x1489_93403_1175412169}[等待]{style="font-family:宋体"}[COMMIT ACC]{lang="EN-US"}[报文的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP created or refreshed a timer to wait for EVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x161473097}

[[创建或刷新等待]{style="font-family:宋体"}[EVFP_SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_x1232634084}[阶段]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文定时器]{style="font-family:宋体"}

[[Interface *interface-name*: EVFP created or refreshed a timer to wait for EVFP_COMMIT ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x584903403}

[[创建或刷新等待]{style="font-family:宋体"}[EVFP_COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_84791475}[阶段]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文定时器]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully created ESC request timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x657691367}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_180518449}[发起端创建定时器成功]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully created ESC responder timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x585886443}

[[ESC]{lang="EN-US"}]{#struct_0_x1489_93403_441921183}[响应端创建定时器成功]{style="font-family:宋体"}

[[Interface *interface-name*: EEVFP created or refreshed a timer to wait for EEVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1457945548}

[[创建或刷新等待]{style="font-family:宋体"}[EEVFP_SYNC]{lang="EN-US"}]{#struct_0_x1489_93403_1935989991}[阶段]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文定时器]{style="font-family:宋体"}

[[Interface *interface-name:* The timer waiting for EEVFP SYNC ACC frames timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x585820907}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x1030142611}[等待]{style="font-family:宋体"}[SYNC ACC]{lang="EN-US"}[报文的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name:* EEVFP created or refreshed a timer to wait for EEVFP_COMMIT ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1231046910}

[[创建或刷新等待]{style="font-family:宋体"}[EEVFP_COMMIT]{lang="EN-US"}]{#struct_0_x1489_93403_x585362154}[阶段]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文定时器]{style="font-family:宋体"}

[[Interface *interface-name:* The timer waiting for EEVFP COMMIT ACC frames timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x655664275}

[[EEVFP]{lang="EN-US"}]{#struct_0_x1489_93403_x844881823}[等待]{style="font-family:宋体"}[COMMIT ACC]{lang="EN-US"}[报文的定时器超时]{style="font-family:宋体"}

[[Interface *interface-name*: The resource allocate timer timed out in VSAN *vsan-id* and a login negotiation was initiated again.]{lang="EN-US"}]{#struct_0_x1489_93403_1137542767}

[[login]{lang="EN-US"}]{#struct_0_x1489_93403_x585296618}[资源分配定时器超时，再次发起]{style="font-family:宋体"}[login]{lang="EN-US"}[协商]{style="font-family:宋体"}

[[Interface *interface-name*: The auto-load-balance timer will time out in *timeout* seconds.]{lang="EN-US"}]{#struct_0_x1489_93403_x29481300}

[[自动负载均衡定时器将在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*]{#struct_0_x1489_93403_x187119400}[秒后超时]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create auto-load-balance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1595565241}

[[创建自动负载均衡定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1581254962}

[[Interface *interface-name*: The auto-load-balance timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_757549601}

[[自动负载均衡定时器超时]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1548511074}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_825830782}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1056444092}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商]{style="font-family:宋体"}[ELP]{lang="EN-US"}[协议的调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link elp]{lang="EN-US"}]{#struct_0_x1489_93403_x1337175512}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Successfully sent ELP request frames in VSAN 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x944394743}*[发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}[请求报文成功]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Received exchange ACK event in VSAN 2.]{lang="EN-US"}]{#struct_0_x1489_93403_125910661}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x585231082}*[接收到对端]{style="font-family:宋体"}[ACK]{lang="EN-US"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ELP: -MDC=1; Interface Fc1/0/1: Received ELP ACC frames in VSAN 2.]{lang="EN-US"}]{#struct_0_x1489_93403_1264826586}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1301614190}*[接收到对端]{style="font-family:宋体"}[ELP ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x133368293}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商错误调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link error]{lang="EN-US"}]{#struct_0_x1489_93403_1287948051}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to create ELP R_A_TOV in VSAN 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1206529672}*[创建]{style="font-family:宋体"}[ELP]{lang="EN-US"}[资源分配定时器失败]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to add trunk list to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_694724281}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1123957978}*[将]{style="font-family:宋体"}[trunk list]{lang="EN-US"}[下驱动失败]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ERROR: -MDC=1; Interface Fc1/0/1: Failed to create login logical state machine in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_x585165546}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_2031455081}*[创建]{style="font-family:宋体"}[login]{lang="EN-US"}[的逻辑状态机失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_490062351}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开交换机能力协商]{style="font-family:宋体"}[ESC]{lang="EN-US"}[协议的调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link esc]{lang="EN-US"}]{#struct_0_x1489_93403_x1407214829}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ESC: -MDC=1; Interface Fc1/0/1: Received ACK event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x508183896}*[接收到]{style="font-family:宋体"}[ESC]{lang="EN-US"}[请求报文的]{style="font-family:宋体"}[ACK]{lang="EN-US"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/ESC: -MDC=1; Interface Fc1/0/1: The ESC responder switch supports VSAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x862815174}

[*[// ESC]{lang="EN-US"}*]{#struct_0_x1489_93403_x1819907892}*[响应端交换机支持]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[协议]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x585100010}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商事件调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link event]{lang="EN-US"}]{#struct_0_x1489_93403_x1461894043}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVENT: -MDC=1; Interface Fc1/0/1: Received the success of ESC negotiation in E state.]{lang="EN-US"}

[*[// E]{lang="EN-US"}*]{#struct_0_x1489_93403_1639886201}*[模式下]{style="font-family:宋体"}[ESC]{lang="EN-US"}[协商成功]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVENT: -MDC=1; Interface Fc1/0/1: Received the success of EVFP negotiation in E state.]{lang="EN-US"}]{#struct_0_x1489_93403_1429285596}

[*[// E]{lang="EN-US"}*]{#struct_0_x1489_93403_x1651845560}*[模式下]{style="font-family:宋体"}[EVFP]{lang="EN-US"}[协商成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x240117546}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[参数协商]{style="font-family:宋体"}[EVFP]{lang="EN-US"}[协议的调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link evfp]{lang="EN-US"}]{#struct_0_x1489_93403_x585034474}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Encapsulated EVFP_SYNC request frames. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1626084976}*[封装]{style="font-family:宋体"}[EVFP SYNC]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received sync ACK event. ]{lang="EN-US"}]{#struct_0_x1489_93403_x1992662662}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_653363962}*[接收到]{style="font-family:宋体"}[SYNC]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACK]{lang="EN-US"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received ACC frames. ]{lang="EN-US"}]{#struct_0_x1489_93403_x958585170}

[*[// EVFP]{lang="EN-US"}*]{#struct_0_x1489_93403_x817583258}*[接收到]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/EVFP: -MDC=1; Interface Fc1/0/1: Received EVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_x1415940942}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x584968938}*[接收到]{style="font-family:宋体"}[EVFP SYNC]{lang="EN-US"}[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1780375433}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商]{style="font-family:宋体"}[FLOGI/FDISC/LOGO]{lang="EN-US"}[协议的调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link login-out]{lang="EN-US"}]{#struct_0_x1489_93403_369427018}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Successfully sent FLOGI request in VSAN 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1475760112}*[发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[请求报文成功]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Received FLOGI request frame in wrong state and responded with a RJT frame in VSAN 2.]{lang="EN-US"}]{#struct_0_x1489_93403_x1388563289}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1462419431}*[收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[请求报文时，当前本端所处的模式不正确，回拒绝报文]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/LOGINOUT: -MDC=1; Interface Fc1/0/1: Successfully received LOGO ACC packet in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_195896076}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x584903402}*[接收]{style="font-family:宋体"}[LOGO ACC]{lang="EN-US"}[报文成功]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_84725939}[启动]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商报文调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link packet]{lang="EN-US"}]{#struct_0_x1489_93403_x989029719}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/PACKET: -MDC=1; Interface Fc1/0/1: Sent packets in VSAN 1 successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x158526520}*[端口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[内的报文成功]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/PACKET: -MDC=1; Interface Fc1/0/1: Received packets from VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_x524601658}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1970702791}*[从端口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[上接收到报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x829741841}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[链路协商定时器调试信息开关，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc link timer]{lang="EN-US"}]{#struct_0_x1489_93403_x585886442}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: Successfully created E_D_TOV in VSAN 2. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_441855647}*[创建错误检测定时器成功]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: Successfully created ESC request timer. ]{lang="EN-US"}]{#struct_0_x1489_93403_x2014717568}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1045859799}*[创建]{style="font-family:宋体"}[ESC]{lang="EN-US"}[请求报文超时检测定时器]{style="font-family:宋体"}*

[[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/TIMER: -MDC=1; Interface Fc1/0/1: EVFP created or refreshed a timer to wait for EVFP_SYNC ACC frames.]{lang="EN-US"}]{#struct_0_x1489_93403_1254866145}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x567711637}*[创建或刷新等待]{style="font-family:宋体"}[EVFP_SYNC ACC]{lang="EN-US"}[报文的定时器]{style="font-family:宋体"}*

::: {#1155138432 .myid}
[]{#_Toc297193506}[]{#_Toc252204010}[]{#_Toc404797584}[]{#struct_0_x1489_93403_1274975742}[]{#_Toc312502885}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc name-service**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x585820906}

[**[debugging fc name-service]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1489_93403_x1030208147}

[**[undo debugging fc name-service]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1489_93403_1446723549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x221655330}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1750228026}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1850500261}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x267516529}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x585362157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x655467667}

[**[all]{lang="FR"}**]{#struct_0_x1489_93403_322945617}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="FR"}**]{#struct_0_x1489_93403_1998799533}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="FR"}**]{#struct_0_x1489_93403_x786874660}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_1334515671}[：]{style="font-family:宋体"}[表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_275631468}

[**[debugging fc name-service]{lang="FR"}**]{#struct_0_x1489_93403_x824687224}[命令用来打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[名称服务调试信息开关。]{style="font-family:宋体"}**[undo debugging fc ]{lang="EN-US"}[name-service]{lang="FR"}**[命令用来关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[名称服务调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x585296621}[名称服务调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging fc name-service error]{lang="EN-US"}]{#struct_0_x1489_93403_826289531}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1325161997}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2100120219}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1162367031}

[[VSAN *id* failed to find the CT session for socket *socket-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x781273470}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585231085}[内查找]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[的]{style="font-family:宋体"}[CT]{lang="EN-US"}[会话失败]{style="font-family:宋体"}

[[VSAN *id* failed to find GMI session in domain ID *domain-id*, with source FCID *fc-id* and transaction ID *transaction-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1264629978}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2108808378}[内查找域]{style="font-family:宋体"}[ID *domain-id*]{lang="EN-US"}[，]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[，事务]{style="font-family:宋体"}[ID *transaction-id*]{lang="EN-US"}[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话失败]{style="font-family:宋体"}

[[VSAN *id* failed to get CT register information.]{lang="EN-US"}]{#struct_0_x1489_93403_1177504907}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1489369392}[内获取]{style="font-family:宋体"}[CT]{lang="EN-US"}[注册信息失败]{style="font-family:宋体"}

[[VSAN *id* failed to allocate socket or timer for sending SW_CT request in domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585165549}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_2031127401}[内发送域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内的]{style="font-family:宋体"}[SW_CT]{lang="EN-US"}[请求报文时申请]{style="font-family:宋体"}[socket]{lang="EN-US"}[或定时器失败]{style="font-family:宋体"}

[[VSAN *id* failed to allocate session for sending SW_CT request in domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_894413416}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x270497000}[内发送域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内的]{style="font-family:宋体"}[SW_CT]{lang="EN-US"}[请求报文时申请会话失败]{style="font-family:宋体"}

[[VSAN *id* failed to send SW_CT request for socket *socket-id* in domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_508971398}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585100013}[内通过]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[发送域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内的]{style="font-family:宋体"}[SW_CT]{lang="EN-US"}[请求失败]{style="font-family:宋体"}

[[VSAN *id* failed to parse the ESS packet from domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1461959579}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x845648096}[内解析从域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送的]{style="font-family:宋体"}[ESS]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[VSAN *id* received an invalid ESS packet from domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1054193263}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585034477}[内接收到从域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送的非法]{style="font-family:宋体"}[ESS]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *id* failed to negotiate ESS with domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1625888368}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1560619083}[内和域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[ ESS]{lang="EN-US"}[协商失败]{style="font-family:宋体"}

[[VSAN *id* domain *domain-id* data does not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_x1384652165}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x584968941}[内域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[相关的数据不存在]{style="font-family:宋体"}

[[VSAN *id* failed to get port WWN.]{lang="EN-US"}]{#struct_0_x1489_93403_x1779785614}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_553858566}[内获取端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *id* failed to add N port entry for the port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_x584903405}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_84660403}[内添加]{style="font-family:宋体"}[N]{lang="EN-US"}[端口]{style="font-family:宋体"}*[port-wwn]{lang="EN-US"}*[的表项失败]{style="font-family:宋体"}

[[VSAN *id* failed to create N port.]{lang="EN-US"}]{#struct_0_x1489_93403_1721058520}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_853203129}[内创建]{style="font-family:宋体"}[N]{lang="EN-US"}[端口失败]{style="font-family:宋体"}

[[VSAN *id* failed to create N node.]{lang="EN-US"}]{#struct_0_x1489_93403_x585886445}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_441790111}[内创建]{style="font-family:宋体"}[N]{lang="EN-US"}[节点失败]{style="font-family:宋体"}

[[VSAN *id* failed to add N port.]{lang="EN-US"}]{#struct_0_x1489_93403_1284667965}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585820909}[内添加]{style="font-family:宋体"}[N]{lang="EN-US"}[端口失败]{style="font-family:宋体"}

[[VSAN *id* FCID *fc-id* has no PLOGI.]{lang="EN-US"}]{#struct_0_x1489_93403_x1031060115}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1073518848}[内]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[没有]{style="font-family:宋体"}[PLOGI]{lang="EN-US"}

[[VSAN *id* name service database is empty.]{lang="EN-US"}]{#struct_0_x1489_93403_874309224}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585362156}[内名称服务数据库为空]{style="font-family:宋体"}

[[VSAN *id* rejected GET request packet with incorrect length in domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x655533203}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1873319064}[内拒绝了域]{style="font-family:宋体"}*[domain]{lang="EN-US"}*[-id]{lang="EN-US"}[内的非法长度]{style="font-family:宋体"}[GET]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *id* failed to parse entry when receiving GE_PT ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x585296620}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_826355067}[内解析]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[回应报文内的表项失败]{style="font-family:宋体"}

[[VSAN *id* failed to add GMI session for GE_PT with source FCID *src-fc-id*, transaction ID *transaction-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x110662387}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585231084}[内添加]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*

[[VSAN *id* failed to add GMI session with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1264695514}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1450796400}[内添加]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，最后]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[last-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*

[[VSAN *id* fcping timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x585165548}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_2031061865}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[VSAN *id* source FCID of the fcping request was invalid.]{lang="EN-US"}]{#struct_0_x1489_93403_1283625989}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x585100012}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[非法]{style="font-family:宋体"}

[[VSAN *id* payload length of the fcping request was incorrect, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1462025115}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_2007197448}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的负载长度非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* version of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585034476}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1625953904}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的版本非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* port tag of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_94146697}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x584968940}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的端口标签非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* port length of the fcping request was incorrect, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1779851150}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x584903404}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的端口长度非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[VSAN *id* FCID in the fcping frame was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_84594867}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_53238391}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* the fcping request was under process, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585886444}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_441724575}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求正在处理，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* WWN in the fcping frame was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x585820908}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1031125651}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* failed to send echo request, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_1408833913}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555345114}[内发送]{style="font-family:宋体"}[echo]{lang="EN-US"}[请求失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* token value of the fcping request was invalid, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x18833415}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x726264070}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[token]{lang="EN-US"}[值非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* failed to add fcping session, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_555279578}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_1140575652}[内添加]{style="font-family:宋体"}[fcping]{lang="EN-US"}[会话失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *id* does not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_555214042}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x792783889}[不存在]{style="font-family:宋体"}

[[VSAN *id* failed to receive request packet from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555148506}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x297349745}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[接收请求失败]{style="font-family:宋体"}

[[VSAN *id* failed to process response packet from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1822421931}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555607258}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[接收响应失败]{style="font-family:宋体"}

[[VSAN *id* failed to create the socket for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1844827426}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555541722}[内创建]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文的]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *id* failed to bind socket *socket-id* for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x527113131}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555476186}[内]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文的]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[绑定失败]{style="font-family:宋体"}

[[VSAN *id* failed to create *packet-type* timer for socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_280731674}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x780206088}[内]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文的]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[创建定时器失败]{style="font-family:宋体"}

[[VSAN *id* failed to send *packet-type* request/ACC/RJT packet to FCID *fc-id* with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555410650}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x154052533}[内通过]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[向]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文的（请求]{style="font-family:宋体"}[/]{lang="EN-US"}[回应]{style="font-family:宋体"}[/]{lang="EN-US"}[拒绝）失败]{style="font-family:宋体"}

[[VSAN *id* failed to check PLOGI frame parameter.]{lang="EN-US"}]{#struct_0_x1489_93403_555869402}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1248181660}[内检查]{style="font-family:宋体"}[PLOG]{lang="EN-US"}[报文参数失败]{style="font-family:宋体"}

[[VSAN *id* FCID *fc-id* has no FLOGI.]{lang="EN-US"}]{#struct_0_x1489_93403_555803866}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_308263138}[内]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[没有]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}

[[VSAN *id* failed to parse switch RSCN frame.]{lang="EN-US"}]{#struct_0_x1489_93403_555345115}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_x18833414}[内解析交换机]{style="font-family:宋体"}[RSCN]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[VSAN *id* failed to handle fabric enable event.]{lang="EN-US"}]{#struct_0_x1489_93403_x726264071}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555279579}[内处理]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[模式使能失败]{style="font-family:宋体"}

[[VSAN *id* fragment ID *frag-id* of GMI request is invalid in domain ID *domain*-*id*, with source FC ID *src*-*fc*-*id* and transaction ID *transaction*-*id*, current fragment ID is *cur*-*frag*-*id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1140575651}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555214043}[内的域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内收到分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[frag-id]{lang="EN-US"}*[的无效]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[src-fc-id]{lang="EN-US"}[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction]{lang="EN-US"}*[-*id*]{lang="EN-US"}[，当前有效分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[cur]{lang="EN-US"}*[-*frag*-*id*]{lang="EN-US"}

[[VSAN *id* received request packet from interface which negotiation mode is invalid with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x792783890}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555148507}[内从协商模式无效的接口接收到请求报文，]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *id* received response packet from interface which negotiation mode is invalid with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x297349744}

[[VSAN *id*]{lang="EN-US"}]{#struct_0_x1489_93403_555607259}[内从协商模式无效的接口接收到响应报文，]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging fc name-service event]{lang="EN-US"}]{#struct_0_x1489_93403_x1844827425}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1309297517}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2057671910}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1271878155}

[[VSAN *vsan-id* successfully deleted the GMI session in domain ID *domain-id*, with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2146864938}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555541723}[内成功删除域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，最后]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[last-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*

[[VSAN *vsan-id* successfully negotiated ESS with domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x527113130}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1810980518}[内和域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[ ESS]{lang="EN-US"}[协商通过]{style="font-family:宋体"}

[[VSAN *vsan-id* ESS timer of domain *domain-id* timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1450245121}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_91718756}[内和域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[ ESS]{lang="EN-US"}[协商定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* updated ESS capability list of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555476187}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_280731673}[内更新和域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[ ESS]{lang="EN-US"}[协商结果]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully deleted VSAN information.]{lang="EN-US"}]{#struct_0_x1489_93403_x780206083}

[[成功删除]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1761202827}[相关数据]{style="font-family:宋体"}

[[VSAN *vsan-id* received domain ID change event, which changed from *old-domain-id* to *new-domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555410651}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x154052534}[内域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}*[old-domain-id]{lang="EN-US"}*[变化为]{style="font-family:宋体"}*[new-domain-id]{lang="EN-US"}*

[[VSAN *vsan-id* received route adding event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1850079120}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2115301058}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由添加事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received route deleting event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x861109407}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555869403}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由删除事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received the FLOGI event of the port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1248181659}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x673655760}[内收到端口]{style="font-family:宋体"}*[port-ww]{lang="EN-US"}*[n]{lang="EN-US"}[的]{style="font-family:
  宋体"}[FLOGI]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received the FLOGO event of the port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_555803867}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_308263139}[内收到端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[-*wwn*]{lang="EN-US"}[的]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id* FTR timer timed out, with S_ID *fc*-*id* and token value *token*-*value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x868817980}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2006143501}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[定时器超时，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[fc]{lang="EN-US"}*[-*id*]{lang="EN-US"}[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token]{lang="EN-US"}*[-*value*]{lang="EN-US"}

[[VSAN *vsan-id* GE_ID frame timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_555345112}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x18833417}[内]{style="font-family:宋体"}[GE_ID]{lang="EN-US"}[报文定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* GE_PT frame timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x726264068}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1287138883}[内]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[报文定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* SW_CT GMI frame timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_555279576}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1140575662}[内]{style="font-family:宋体"}[SW_CT GMI]{lang="EN-US"}[报文定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully sent GMI request for GE_PT/ GMI ACC.]{lang="EN-US"}]{#struct_0_x1489_93403_x2074417828}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1338513719}[内收到]{style="font-family:宋体"}[GE_PT/GMI ACC]{lang="EN-US"}[后成功发送]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully added GMI session for GE_PT with source FCID *src*-*fc*-*id*, last FCID *last*-*fc*-*id*, and transaction ID *transaction*-*id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555214040}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x792783891}[内添加]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话成功，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，最后]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[last]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction]{lang="EN-US"}*[-*id*]{lang="EN-US"}

[[VSAN *vsan-id* successfully received the GMI request for GE_PT with last FCID *fc*-*id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1833814141}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555148504}[内成功接收]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求，上次最后]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[f]{lang="EN-US"}*[c-*id*]{lang="EN-US"}

[[VSAN *vsan-id* successfully added GMI session with source FCID *src-fc-id*, last FCID *last-fc-id*, and transaction ID *transaction-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x297349747}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1822290859}[内成功添加]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话成功，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[，最后]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[last]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction]{lang="EN-US"}*[-*id*]{lang="EN-US"}

[[VSAN *vsan-id* successfully sent GE_PT request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_555607256}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1844827436}[内成功发送]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully sent echo request frame.]{lang="EN-US"}]{#struct_0_x1489_93403_x491522433}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555541720}[内成功发送]{style="font-family:宋体"}[echo]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* received fcping request frame from source FCID *fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x527113133}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811046054}[内收到从]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送的]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* received SW_RSCN request frame from FCID *fc-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_555476184}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_280731676}[内收到从]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SW_RSCN]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* rejected SW_RSCN frame received from FCID *fc-id* for incorrect packet length.]{lang="EN-US"}]{#struct_0_x1489_93403_x780206086}

[[由于报文长度非法，]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555410648}[内拒绝从]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SW_RSCN]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[VSAN *vsan-id* received SW_RSCN response frame from FCID *fc-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_1802262611}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1338295563}[内收到从]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SW_RSCN]{lang="EN-US"}[回应]{style="font-family:宋体"}

[[VSAN *vsan-id* notified FC ZONE local/remote N port realtime FLOGI/FLOGO, FCID: *fc-id*, WWN: *port-wwn*, FWWN: *Fport-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_555869400}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1248181658}[内实时通知]{style="font-family:宋体"}[FC ZONE]{lang="EN-US"}[本地]{style="font-family:宋体"}[/]{lang="EN-US"}[远端端口的]{style="font-family:宋体"}[FLOGI/FLOGO]{lang="EN-US"}[，]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[fc]{lang="EN-US"}*[-*id*]{lang="EN-US"}[，端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[是]{style="font-family:宋体"}*[port]{lang="EN-US"}*[-*wwn*]{lang="EN-US"}[，]{style="font-family:宋体"}[F]{lang="EN-US"}[端口的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[是]{style="font-family:宋体"}*[Fport-wwn]{lang="EN-US"}*

[[VSAN *vsan-id* notified FC ZONE batch N port FLOGI *n* times.]{lang="EN-US"}]{#struct_0_x1489_93403_2055227595}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_555803864}[内第]{style="font-family:宋体"}*[n]{lang="EN-US"}*[次批量通知]{style="font-family:宋体"}[FC ZONE N]{lang="EN-US"}[端口]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}

[[VSAN *vsan-id* filtered query requests to FCID *dst*-*fc*-*id* by FC ZONE, with the request source FCID: *src*-*fc*-*id*.]{lang="EN-US"}]{#struct_0_x1489_93403_308263136}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x868817965}[内]{style="font-family:宋体"}[FC ZONE]{lang="EN-US"}[过滤了]{style="font-family:宋体"}*[src]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[对]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[的查询请求]{style="font-family:宋体"}

[[VSAN *vsan-id* filtered query requests to FCID *dst-fc-id* by FC ZONE, with the request source WWN: *src-port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_555345113}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x18833416}[内]{style="font-family:宋体"}[FC ZONE]{lang="EN-US"}[过滤了]{style="font-family:宋体"}*[src]{lang="EN-US"}*[-*port*-*wwn*]{lang="EN-US"}[对]{style="font-family:宋体"}*[dst]{lang="EN-US"}*[-*fc*-*id*]{lang="EN-US"}[的查询请求]{style="font-family:宋体"}

[[VSAN *vsan-id* received a VSAN mode change event, which changed from *old-mode* to *new-mode*.]{lang="EN-US"}]{#struct_0_x1489_93403_1883028300}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x455623869}[内收到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[模式从]{style="font-family:宋体"}*[old-mode]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[new-mode]{lang="EN-US"}*[的事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging fc name-service packet]{lang="EN-US"}]{#struct_0_x1489_93403_x726264069}[命令输出信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1335059437}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1287204419}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_555279577}

[[VSAN *vsan-id* received *packet-type* request packet from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1140575661}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2074352292}[内从]{style="font-family:宋体"}[socket *socket*-*id*]{lang="EN-US"}[接收]{style="font-family:
  宋体"}[packet-type]{lang="EN-US"}[请求报文]{style="font-family:
  宋体"}

[[VSAN *vsan-id* received *packet-type* response packet from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_213678241}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1318194768}[内从]{style="font-family:宋体"}[socket *socket*-*id*]{lang="EN-US"}[接收]{style="font-family:
  宋体"}[packet-type]{lang="EN-US"}[回应报文]{style="font-family:
  宋体"}

[[VSAN *vsan-id* successfully sent *packet-type* request/ACC/RJT packet to FCID *fc-id* with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555214041}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x792783892}[内通过]{style="font-family:宋体"}[socket *socket*-*id*]{lang="EN-US"}[向]{style="font-family:
  宋体"}*[fc]{lang="EN-US"}*[-*id*]{lang="EN-US"}[发送]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[-*type*]{lang="EN-US"}[请求]{style="font-family:宋体"}[/ACC/RJT]{lang="EN-US"}

[[VSAN *vsan-id* successfully sent fcping ACC frame.]{lang="EN-US"}]{#struct_0_x1489_93403_1833879677}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_28263509}[内成功发送]{style="font-family:宋体"}[fcping ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id* sent fcping reject frame, with source FCID *src-fc-id*, destination FCID *dst-fc-id*, and token value *token-value.*]{lang="EN-US"}]{#struct_0_x1489_93403_555148505}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x297349746}[内发送]{style="font-family:宋体"}[fcping]{lang="EN-US"}[拒绝报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1822225323}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x672682289}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[名称服务错误调试信息开关。接收分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[不合法的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[报文时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc name-service error vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_1272048638}

[\*Jan 10 18:06:11:318 2012 Sysname FCGS_LOG/7/ERROR: -MDC=1; VSAN 2 fragment ID 3 of GMI request is invalid in domain ID 1, with source FCID 010001 and transaction ID 0, current fragment ID is 2.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x710111184}*[内的域]{style="font-family:宋体"}[1]{lang="EN-US"}[内收到分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[的无效]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010001]{lang="EN-US"}[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，当前有效分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x275817098}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[名称服务事件调试信息开关。]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内有]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[或]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc name-service event vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_555607257}

[\*Jan 10 11:51:54:444 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received the FLOGI event of the port 00:02:30:30:30:30:36:39. ]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x1844827435}*[内收到端口]{style="font-family:宋体"}[00:02:30:30:30:30:36:39]{lang="EN-US"}[的]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Jan 10 11:51:54:444 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 notified FC ZONE local N port realtime FLOGI , FCID: 010000, WWN: 00:02:30:30:30:30:36:39.]{lang="EN-US"}]{#struct_0_x1489_93403_x2057606374}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x122732312}*[实时通知]{style="font-family:宋体"}[ZONE]{lang="EN-US"}[模块]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[，]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[，端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[00:02:30:30:30:30:36:39]{lang="EN-US"}*

[[\*Jan 10 11:51:54:451 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received SW_RSCN response frame from FCID fffc02.  ]{lang="EN-US"}]{#struct_0_x1489_93403_x1183126862}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_944865301}*[接收到从]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[的回应报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 10 11:51:43:230 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received the FLOGO event of the port 00:02:30:30:30:30:36:39. ]{lang="EN-US"}]{#struct_0_x1489_93403_1579609248}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_555541721}*[内收到端口]{style="font-family:宋体"}[00:02:30:30:30:30:36:39]{lang="EN-US"}[的]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Jan 10 11:51:43:231 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 notified FC ZONE local N port realtime FLOGO , FCID: 010000, WWN: 00:02:30:30:30:30:36:39.]{lang="EN-US"}]{#struct_0_x1489_93403_x527113132}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1811111590}*[实时通知]{style="font-family:宋体"}[ZONE]{lang="EN-US"}[模块]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[，]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[，端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[00:02:30:30:30:30:36:39]{lang="EN-US"}*

[[\*Jan 10 11:51:43:238 2012 Sysname FCGS_LOG/7/EVENT: -MDC=1; VSAN 2 received SW_RSCN response frame from FCID fffc02.]{lang="EN-US"}]{#struct_0_x1489_93403_507088996}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1910245670}*[接收到从]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[的回应报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x512662727}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[名称服务报文调试信息开关。]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内有]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[或]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc name-service packet vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_1337452966}

[\*Jan 10 11:58:24:988 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_RSCN request packet to FCID fffc02 with socket 23.]{lang="EN-US"}

[*[// FLOGI]{lang="EN-US"}*]{#struct_0_x1489_93403_2066939339}*[时向]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送]{style="font-family:宋体"}[N]{lang="EN-US"}[节点上线的]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[ \*Jan 10 11:58:24:992 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_RSCN response packet from socket 23. ]{lang="EN-US"}]{#struct_0_x1489_93403_555476185}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_280731675}*[接收]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[报文的回应报文]{style="font-family:宋体"}*

[[\*Jan 10 11:58:25:023 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_CT request packet from socket 26. ]{lang="EN-US"}]{#struct_0_x1489_93403_x780206089}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1760809611}*[接收]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送的获取所有名称服务数据库表项的]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan 10 11:58:25:023 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_CT ACC packet to FCID fffc02 with socket 26.]{lang="EN-US"}]{#struct_0_x1489_93403_x819867030}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1862420413}*[向]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送]{style="font-family:宋体"}[GE_PT]{lang="EN-US"}[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\*Jan 10 11:58:10:560 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent SW_RSCN request packet to FCID fffc02 with socket 23. ]{lang="EN-US"}]{#struct_0_x1489_93403_555410649}

[*[// FLOGO]{lang="EN-US"}*]{#struct_0_x1489_93403_1802262610}*[时向]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送]{style="font-family:宋体"}[N]{lang="EN-US"}[节点下线的]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan 10 11:58:10:650 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received SW_RSCN response packet from socket 23.]{lang="EN-US"}]{#struct_0_x1489_93403_x1338230027}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1499780054}*[接收]{style="font-family:宋体"}[SW RSCN]{lang="EN-US"}[报文的回应报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 10 18:05:27:415 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 received ELS_CT request packet from socket 23. ]{lang="EN-US"}]{#struct_0_x1489_93403_x1564768056}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x1834868707}*[内收到]{style="font-family:宋体"}[ELS_CT]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Jan 10 18:05:27:417 2012 Sysname FCGS_LOG/7/PACKET: -MDC=1; VSAN 2 successfully sent ELS_CT ACC packet to FCID 010001 with socket 23. ]{lang="EN-US"}]{#struct_0_x1489_93403_1482161401}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x335418386}*[内向]{style="font-family:宋体"}[010001]{lang="EN-US"}[成功发送]{style="font-family:宋体"}[ELS_CT ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#-268554433 .myid}
[]{#_Toc404797585}[]{#struct_0_x1489_93403_x1562752946}[]{#_Toc373749192}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc nport**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1504345025}

[**[debugging]{lang="EN-US"}**[ **fc** **nport** { **all** \| **error** \| **event** \| **packet** \[ **interface** *interface-type interface-number* \] } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_263351057}

[**[undo]{lang="EN-US"}**[ **debugging** **fc** **nport** { **all** \| **error** \| **event** \| **packet** \[ **interface** *interface-type interface-number* \] } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x475199297}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1776031614}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1563211697}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x121457296}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1679723716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1680582975}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1203146133}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x820835072}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_x1563277233}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_x77167222}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_1584393204}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface]{lang="EN-US"}*[-*type* *interface*-*number*]{lang="EN-US"}]{#struct_0_x1489_93403_x1083964679}[：表示指定接口的调试信息开关，]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type*]{lang="EN-US"}[只能是]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口或]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口。如果未指定本参数，表示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口、]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口和]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的调试信息开关。只有被配置为]{style="font-family:宋体"}[NP]{lang="EN-US"}[模式的接口能打印出调试信息。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_773512811}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x832135092}

[**[debugging]{lang="EN-US"}**[ **fc** **nport**]{lang="EN-US"}]{#struct_0_x1489_93403_x1563342769}[命令用来打开模拟]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[行为的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **fc** **nport**]{lang="EN-US"}[命令用来关闭模拟]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[行为的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，模拟]{style="font-family:宋体"}[N_Port]{lang="EN-US"}]{#struct_0_x1489_93403_x361871060}[行为的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_1765906017}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[表1-16 ]{lang="EN-US"}[debugging fc nport error]{lang="EN-US"}]{#struct_0_x1489_93403_x1517482427}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1247179533}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1563408305}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1919969624}

[[Received an event for an invalid VSAN ID from Fabric.]{lang="EN-US"}]{#struct_0_x1489_93403_x1563473841}

[[从]{style="font-family:宋体"}[Fabric]{lang="EN-US"}]{#struct_0_x1489_93403_x717841318}[模块收到]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}[无效的事件通知]{style="font-family:宋体"}

[[VSAN didn\'t exist. Deletion process terminated.]{lang="EN-US"}]{#struct_0_x1489_93403_x1563539377}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x756451357}[不存在，结束当前]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[删除流程]{style="font-family:宋体"}

[[Received an NPV FC ID addition event with invalid parameters.]{lang="EN-US"}]{#struct_0_x1489_93403_x1563604913}

[[收到参数无效的]{style="font-family:宋体"}[NPV FCID]{lang="EN-US"}]{#struct_0_x1489_93403_1579277068}[添加事件]{style="font-family:宋体"}

[[Received an NPV FC ID deletion event with invalid parameters.]{lang="EN-US"}]{#struct_0_x1489_93403_x1563670449}

[[收到参数无效的]{style="font-family:宋体"}[NPV FCID]{lang="EN-US"}]{#struct_0_x1489_93403_44908846}[删除事件]{style="font-family:宋体"}

[[Failed to allocate memory for port data with FC ID *fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1562687409}

[[为]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_1547068100}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[Port]{lang="EN-US"}[数据分配内存失败]{style="font-family:宋体"}

[[Failed to send a CT packet: packet type *packet-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1562752945}

[[发送类型为]{style="font-family:宋体"}*[packet-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1101060498}[的]{style="font-family:宋体"}[CT]{lang="EN-US"}[报文失败。]{style="font-family:宋体"}*[packet-name]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[RFT_ID]{lang="EN-US"}[、]{style="font-family:宋体"}[RIP_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSNN_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSPN_ID]{lang="EN-US"}[和]{style="font-family:宋体"}[GMAL]{lang="EN-US"}

[[Received a GMAL response of invalid length.]{lang="EN-US"}]{#struct_0_x1489_93403_2872247}

[[收到长度无效的]{style="font-family:宋体"}[GMAL]{lang="EN-US"}]{#struct_0_x1489_93403_x34837522}[回应报文]{style="font-family:宋体"}

[[Failed to send a PLOGI packet: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2806711}

[[发送]{style="font-family:宋体"}[Plogi]{lang="EN-US"}]{#struct_0_x1489_93403_2013431912}[请求失败，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[[PLOGI registration failed, because the MTU was not obtained.]{lang="EN-US"}]{#struct_0_x1489_93403_2741175}

[[封装]{style="font-family:宋体"}[Plogi]{lang="EN-US"}]{#struct_0_x1489_93403_x1581328922}[报文负载字段时获取]{style="font-family:宋体"}[MTU]{lang="EN-US"}[失败，]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[注册终止]{style="font-family:宋体"}

[[PLOGI registration failed, because the port WWN was not obtained.]{lang="EN-US"}]{#struct_0_x1489_93403_2675639}

[[获取接口]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_789449592}[失败，]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[注册终止]{style="font-family:宋体"}

[[Failed to allocate memory for registration resources.]{lang="EN-US"}]{#struct_0_x1489_93403_2610103}

[[申请注册资源内存失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_160208693}

[[Failed to receive a message.]{lang="EN-US"}]{#struct_0_x1489_93403_2544567}

[[接收消息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1957686452}

[[Failed to check the interface index and mode.]{lang="EN-US"}]{#struct_0_x1489_93403_2479031}

[[检查接收报文的端口索引和端口模式失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x456937394}

[[Failed to check the FC ID of interface *interface-name* .]{lang="EN-US"}]{#struct_0_x1489_93403_2413495}

[[检查接收报文端口的]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_x240823588}[失败]{style="font-family:宋体"}

[[Failed to get the VSAN ID.]{lang="EN-US"}]{#struct_0_x1489_93403_3396535}

[[获取报文中携带]{style="font-family:宋体"}[VSAN ID]{lang="EN-US"}]{#struct_0_x1489_93403_x1581668732}[失败]{style="font-family:宋体"}

[[Received an NPV FC ID event from interface *interface-name* with an invalid port mode.]{lang="EN-US"}]{#struct_0_x1489_93403_3330999}

[[从端口模式错误的接口收到]{style="font-family:宋体"}[NPV FCID]{lang="EN-US"}]{#struct_0_x1489_93403_1398617426}[事件]{style="font-family:宋体"}

[[Failed to allocate memory for VSAN data.]{lang="EN-US"}]{#struct_0_x1489_93403_2872248}

[[为]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1150582769}[数据申请内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for interface data with FC ID *fcid-value.*]{lang="EN-US"}]{#struct_0_x1489_93403_2806712}

[[为指定]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_2741176}[的接口数据申请内存失败]{style="font-family:宋体"}

[[Invalid CT response received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1178044395}

[[收到非法的]{style="font-family:宋体"}[CT]{lang="EN-US"}]{#struct_0_x1489_93403_2675640}[回应报文，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[debugging fc nport event]{lang="EN-US"}]{#struct_0_x1489_93403_x420338453}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1223868263}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1528125996}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_2610104}

[[Switch WWN successfully set to *wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_2082522994}

[[成功将全局]{style="font-family:宋体"}[WWN]{lang="EN-US"}]{#struct_0_x1489_93403_2544568}[值设置为]{style="font-family:宋体"}*[wwn]{lang="EN-US"}*

[[VSAN *vsan-id* information deleted.]{lang="EN-US"}]{#struct_0_x1489_93403_x1221535597}

[[成功删除]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1549224261}[的相关数据]{style="font-family:宋体"}

[[Received an NPV FC ID addition event from interface *interface-name*: FC ID = *fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2479032}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x860221921}[收到]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[NPV FCID]{lang="EN-US"}[添加事件]{style="font-family:宋体"}

[[Received an NPV FC ID deletion event from interface *interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_2413496}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1325260353}[收到]{style="font-family:宋体"}[NPV FCID]{lang="EN-US"}[删除事件]{style="font-family:宋体"}

[[Host name successfully set to *hostname*.]{lang="EN-US"}]{#struct_0_x1489_93403_3396536}

[[成功将主机名设置为]{style="font-family:宋体"}*[hostname]{lang="EN-US"}*]{#struct_0_x1489_93403_x15584791}

[[Local IPv4 management address successfully set to *ip-address*.]{lang="EN-US"}]{#struct_0_x1489_93403_3331000}

[[成功将本机]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1489_93403_x389216996}[管理口地址设置为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Port data of FC ID *fcid-value* added.]{lang="EN-US"}]{#struct_0_x1489_93403_2872249}

[[成功添加]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_415501172}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[Port]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[Port data of FC ID *fcid-value* deleted.]{lang="EN-US"}]{#struct_0_x1489_93403_2806713}

[[成功删除]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_850632498}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[Port]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[NPV switch started registering parameters to FCF switch.]{lang="EN-US"}]{#struct_0_x1489_93403_2741177}

[[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_1550838960}[交换机开始向]{style="font-family:宋体"}[FCF]{lang="EN-US"}[交换机进行参数注册]{style="font-family:宋体"}

[[NPV registration was completed.]{lang="EN-US"}]{#struct_0_x1489_93403_2675641}

[[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_1145745488}[交换机注册完成]{style="font-family:宋体"}

[[Resent the *packet-type* registration request, because the registration timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_2610105}

[[注册报文]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*]{#struct_0_x1489_93403_x646360361}[的]{style="font-family:宋体"}[注册请求超时，重发请求。]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[、]{style="font-family:宋体"}[RFT_ID]{lang="EN-US"}[、]{style="font-family:宋体"}[RIP_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSNN_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSPN_ID]{lang="EN-US"}[和]{style="font-family:宋体"}[GMAL]{lang="EN-US"}

[[Terminated the *packet-type* registration, because the resent registration request timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_2544569}

[[注册报文]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*]{#struct_0_x1489_93403_1507347758}[的]{style="font-family:宋体"}[注册请求重发超时，注册流程终止。]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[、]{style="font-family:宋体"}[RFT_ID]{lang="EN-US"}[、]{style="font-family:宋体"}[RIP_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSNN_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSPN_ID]{lang="EN-US"}[和]{style="font-family:宋体"}[GMAL]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[debugging fc nport packet]{lang="EN-US"}]{#struct_0_x1489_93403_960791008}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x911819519}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_2479033}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_705862020}

[[CT packet successfully sent: packet type = *packet-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_2413497}

[[成功发送类型为]{style="font-family:宋体"}*[packet-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x1403623002}[的]{style="font-family:宋体"}[CT]{lang="EN-US"}[报文。]{style="font-family:宋体"}*[packet-name]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[RFT_ID]{lang="EN-US"}[、]{style="font-family:宋体"}[RIP_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSNN_NN]{lang="EN-US"}[、]{style="font-family:宋体"}[RSPN_ID]{lang="EN-US"}[和]{style="font-family:宋体"}[GMAL]{lang="EN-US"}

[[Ready to register the FC-4 Type for FC ID *fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_3396537}

[[报文封装完成，即将为]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_1550499150}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[Port]{lang="EN-US"}[注册]{style="font-family:宋体"}[FC-4]{lang="EN-US"}[层协议类型]{style="font-family:宋体"}

[[Ready to register an IP address *ip-address* for node *node-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x356952890}

[[报文封装完成，即将为名为]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*]{#struct_0_x1489_93403_3331001}[的]{style="font-family:宋体"}[Node]{lang="EN-US"}[注册]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Ready to register a symbolic node name *node-name* for node *node-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1176866945}

[[报文封装完成，即将为名为]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*]{#struct_0_x1489_93403_2872250}[的]{style="font-family:宋体"}[Node]{lang="EN-US"}[注册描述名]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*

[[Ready to register a symbolic port name *port-name* for FC ID *fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_x794286873}

[[报文封装完成，即将为]{style="font-family:宋体"}[FCID]{lang="EN-US"}]{#struct_0_x1489_93403_2806714}[为]{style="font-family:宋体"}*[fcid-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[Port]{lang="EN-US"}[注册描述名]{style="font-family:宋体"}*[port-name]{lang="EN-US"}*

[[Ready to get a management address list of IE *ie-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1610147385}

[[报文封装完成，即将获取名为]{style="font-family:宋体"}*[ie-name]{lang="EN-US"}*]{#struct_0_x1489_93403_2741178}[的]{style="font-family:宋体"}[IE]{lang="EN-US"}[的管理口地址]{style="font-family:宋体"}

[[Management address list successfully obtained.]{lang="EN-US"}]{#struct_0_x1489_93403_x1628383089}

[[成功获取管理口地址列表]{style="font-family:宋体"}]{#struct_0_x1489_93403_2675642}

[[PLOGI packet successfully sent: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_742460961}

[[成功发送]{style="font-family:宋体"}[Plogi]{lang="EN-US"}]{#struct_0_x1489_93403_x1408355674}[请求，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[[PLOGI response successfully received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2610106}

[[接收]{style="font-family:宋体"}[Plogi]{lang="EN-US"}]{#struct_0_x1489_93403_919723580}[回应成功，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[[CT reject packet received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*, reason code = *reason-code-value*, explanation code = *reason-explanation-code-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2544570}

[[接收到]{style="font-family:宋体"}[CT]{lang="EN-US"}]{#struct_0_x1489_93403_x1577831493}[拒绝报文，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*[，拒绝原因码为]{style="font-family:宋体"}*[reason-code-value]{lang="EN-US"}*[，拒绝原因解释码为]{style="font-family:宋体"}*[reason-explanation-code-value]{lang="EN-US"}*

[[PLOGI reject packet received: source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2479034}

[[接收到]{style="font-family:宋体"}[Plogi]{lang="EN-US"}]{#struct_0_x1489_93403_302577493}[拒绝报文，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[[CT accept packet received: packet type = *packet-type*, source FC ID = *source-fcid-value*, destination FC ID = *destination-fcid-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_2413498}

[[接收到]{style="font-family:宋体"}[CT Accept]{lang="EN-US"}]{#struct_0_x1489_93403_518691299}[回应报文，报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[，源地址为]{style="font-family:宋体"}*[source-fcid-value]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination-fcid-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2051441622}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_3396538}[打开模拟]{style="font-family:宋体"}[N_Port]{lang="EN-US"}[行为的所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc nport all]{lang="EN-US"}]{#struct_0_x1489_93403_x1534614565}

[%Jun 27 08:55:44:607 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc2 changed to down.]{lang="EN-US"}

[\*Jun 27 08:55:44:625 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2: Received an NPV FC ID deletion event from interface Vfc2.]{lang="EN-US"}

[\*Jun 27 08:55:44:625 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: Port data of FC ID 0a0000 deleted.]{lang="EN-US"}

[%Jun 27 08:55:44:642 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc4 changed to down.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_643973427}*[关闭接口后，收到]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口]{style="font-family:宋体"}[NPV]{lang="EN-US"}[下]{style="font-family:宋体"}[FC ID]{lang="EN-US"}[删除事件，删除当前接口数据]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:145 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2: Received an NPV FC ID addition event from interface Vfc2: FC ID = 0a0000.]{lang="EN-US"}]{#struct_0_x1489_93403_427566112}

[\*Jun 27 08:55:47:147 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: Port data of FC ID 0a0000 added.]{lang="EN-US"}

[\*Jun 27 08:55:47:147 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: NPV switch started registering parameters to FCF switch.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_308325425}*[打开接口后，收到]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口]{style="font-family:宋体"}[NPV]{lang="EN-US"}[下]{style="font-family:宋体"}[FC ID]{lang="EN-US"}[添加事件，新增当前接口数据，触发注册流程]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:148 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI packet successfully sent: source FC ID = 0a0000, destination FC ID = fffffc.]{lang="EN-US"}]{#struct_0_x1489_93403_3331002}

[\*Jun 27 08:55:47:149 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI accept packet received: source FC ID = fffffc, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_773582418}*[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口上向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送名字服务]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[注册请求并成功接收回应报文]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:150 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register the FC-4 Type for FC ID 0a0000.]{lang="EN-US"}]{#struct_0_x1489_93403_781003304}

[\*Jun 27 08:55:47:150 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RFT_ID.]{lang="EN-US"}

[%Jun 27 08:55:47:153 2014 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Physical state on the interface Vfc4 changed to up.]{lang="EN-US"}

[\*Jun 27 08:55:47:155 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RFT_ID, source FC ID = fffffc, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1658228178}*[开始注册]{style="font-family:宋体"}[FC-4]{lang="EN-US"}[类型，]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送]{style="font-family:宋体"}[RFT_ID CT]{lang="EN-US"}[注册请求并成功接收回应]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:156 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register an IP address \"192.168.56.152\" for Node 10:00:00:03:00:00:00:00.]{lang="EN-US"}]{#struct_0_x1489_93403_x428160467}

[\*Jun 27 08:55:47:156 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RIP_NN.]{lang="EN-US"}

[\*Jun 27 08:55:47:158 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RIP_NN, source FC ID = fffffc, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x471858993}*[开始注册本机]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIP_NN CT]{lang="EN-US"}[注册请求并成功接收回应]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:158 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register a symbolic node name \"Sysname\" for node 10:00:00:03:00:00:00:00.]{lang="EN-US"}]{#struct_0_x1489_93403_2872243}

[\*Jun 27 08:55:47:159 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RSNN_NN.]{lang="EN-US"}

[\*Jun 27 08:55:47:160 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RSNN_NN, source FC ID = fffffc, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1934530946}*[开始注册本机]{style="font-family:宋体"}[Node]{lang="EN-US"}[描述名，]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送]{style="font-family:宋体"}[RSNN_NN CT]{lang="EN-US"}[注册请求并成功接收回应]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:160 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to register a symbolic port name \"Sysname:Vfc2\" for FC ID 0a0000.]{lang="EN-US"}]{#struct_0_x1489_93403_2113213556}

[\*Jun 27 08:55:47:161 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = RSPN_ID.]{lang="EN-US"}

[\*Jun 27 08:55:47:163 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = RSPN_ID, source FC ID = fffffc, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_423860878}*[开始注册本机]{style="font-family:宋体"}[NP]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Port]{lang="EN-US"}[描述名，]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送]{style="font-family:宋体"}[RSPN_ID CT]{lang="EN-US"}[注册请求并成功接收回应]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:163 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI packet successfully sent: source FC ID = 0a0000, destination FC ID = fffffa.]{lang="EN-US"}]{#struct_0_x1489_93403_x1015372370}

[\*Jun 27 08:55:47:165 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: PLOGI accept packet received: source FC ID = fffffa, destination FC ID = 0a0000.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_1878056228}*[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送管理服务]{style="font-family:宋体"}[Plogi]{lang="EN-US"}[注册请求并成功接收回应报文]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:165 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Ready to get a management address list of IE 10:00:00:01:00:00:00:00.]{lang="EN-US"}]{#struct_0_x1489_93403_2806707}

[\*Jun 27 08:55:47:166 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT packet successfully sent: packet type = GMAL.]{lang="EN-US"}

[\*Jun 27 08:55:47:168 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: CT accept packet received: packet type = GMAL, source FC ID = fffffa, destination FC ID = 0a0000.]{lang="EN-US"}

[\*Jun 27 08:55:47:168 2014 Sysname FCNPORT/7/PACKET: -MDC=1; VSAN 2 interface Vfc2: Management address list successfully obtained.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1118801506}*[开始查询对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[上的管理口地址，]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[中]{style="font-family:宋体"}[Vfc2]{lang="EN-US"}[接口向对端]{style="font-family:宋体"}[FCF]{lang="EN-US"}[发送]{style="font-family:宋体"}[GMAL CT]{lang="EN-US"}[查询请求并成功接收回应，记录查询结果]{style="font-family:宋体"}*

[[\*Jun 27 08:55:47:169 2014 Sysname FCNPORT/7/EVENT: -MDC=1; VSAN 2 interface Vfc2: NPV registration was completed.]{lang="EN-US"}]{#struct_0_x1489_93403_725675019}

[*[//]{lang="EN-US"}*]{#struct_0_x1489_93403_x1111487809}*[结束整个注册流程]{style="font-family:宋体"}*

::: {#-1772307124 .myid}
[]{#_Toc404797586}[]{#struct_0_x1489_93403_555869401}[]{#_Toc317663148}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc npv**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1248181657}

[**[debugging fc npv]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_489143654}

[**[undo debugging fc ]{lang="EN-US"}[npv]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1642320536}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_779874510}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_1704762418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1065797039}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_555803865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_308263137}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x868817966}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1489_93403_2006012419}[：]{style="font-family:宋体"}[表示指定接口的调试信息开关。如果未指定本参数，表示所有接口的调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x142725580}

[**[debugging fc npv]{lang="EN-US"}**]{#struct_0_x1489_93403_929477544}[命令用来打开]{style="font-family:宋体"}[NPV]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}**[undo debugging fc npv]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[NPV]{lang="EN-US"}[协议的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_x233319383}[协议的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，只有]{style="font-family:宋体"}[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_2675635}[交换机和]{style="font-family:宋体"}[FCF-NPV]{lang="EN-US"}[交换机（]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式）支持本命令。]{style="font-family:宋体"}

[[表1-19 ]{lang="EN-US"}[debugging fc npv]{lang="EN-US"}]{#struct_0_x1489_93403_x726264066}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1334820973}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1287269955}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_717113210}

[[Interface *interface-name*: Failed to send LOGO packet from external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x691075944}

[[上行口发送]{style="font-family:宋体"}[LOGO]{lang="EN-US"}]{#struct_0_x1489_93403_555279574}[报文失败]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully cleared NPV LOGIDB in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1140575664}

[[清除]{style="font-family:宋体"}[NPV login]{lang="EN-US"}]{#struct_0_x1489_93403_x2074548900}[数据库成功]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to clear NPV LOGIDB in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1611346721}

[[清除]{style="font-family:宋体"}[NPV login]{lang="EN-US"}]{#struct_0_x1489_93403_x435294597}[数据库失败]{style="font-family:宋体"}

[[Interface *interface-name*: NPV proxy FLOGI or FDISC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555214038}

[[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_x1602087947}[代理]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[或者]{style="font-family:宋体"}[FDISC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to find the external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1966538445}

[[查找上行口失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_111586893}

[[Interface *interface-name*: Successfully sent FDISC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555148502}

[[发送]{style="font-family:宋体"}[FDISC]{lang="EN-US"}]{#struct_0_x1489_93403_x297349749}[报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Received FDISC ACC frame of invalid parameter in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1821635499}

[[收到参数无效的]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1703559748}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received FDISC ACC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555607254}

[[收到]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1844827438}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully sent FLOGI or FDISC ACC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2010552207}

[[发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_1250773545}[或]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}[报文成功]{style="font-family:宋体"}

[[Interface *interface-name*: Successfully updated NPV LOGIDB in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2022360803}

[[更新]{style="font-family:宋体"}[NPV login]{lang="EN-US"}]{#struct_0_x1489_93403_555541718}[数据库成功]{style="font-family:宋体"}

[[Interface *interface-name*: The main board received the request from server interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1046864971}

[[主控板收到下行口发送的请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1836093337}

[[Interface *interface-name*: The external interface received the request from main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555476182}

[[上行口收到主控板发送的请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_280731670}

[[Interface *interface-name*: The main board received ACC packet from external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x780206084}

[[主控板收到上行口发送的]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1761661579}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: The main board received RJT packet from external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555410646}

[[主控板收到上行口发送的拒绝报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_1802262601}

[[Interface *interface-name*: The server interface received ACC packet from main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1338295562}

[[下行口收到主控板发送的]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x376034358}[报文]{style="font-family:宋体"}

[[Interface *interface-name*: The server interface received RJT packet from main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555869398}

[[下行口收到主控板发送的拒绝报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_1053734649}

[[Interface *interface-name*: The server interface sent request to main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x704425400}

[[下行口发送请求报文到主控板]{style="font-family:宋体"}]{#struct_0_x1489_93403_555803862}

[[Interface *interface-name*: The main board sent request to external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_308263142}

[[主控板发送请求报文到上行口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x59513905}

[[Interface *interface-name*: The external interface sent ACC to main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555345111}

[[上行口发送]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x18833418}[报文到主控板]{style="font-family:宋体"}

[[Interface *interface-name*: The main board sent ACC to server interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x726264067}

[[主控板发送]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_555279575}[报文到下行口]{style="font-family:宋体"}

[[Interface *interface-name*: The external interface sent RJT packet to main board in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1140575663}

[[上行口发送拒绝报文到主控板]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2074483364}

[[Interface *interface-name*: The main board sent RJT packet to server interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_195788955}

[[主控板发送拒绝报文到下行口]{style="font-family:宋体"}]{#struct_0_x1489_93403_555214039}

[[Interface *interface-name*: Could not find external interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1602087948}

[[找不到上行口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x406114550}

[[Interface *interface-name*: Received FDISC RJT packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555148503}

[[收到]{style="font-family:宋体"}[FDISC]{lang="EN-US"}]{#struct_0_x1489_93403_x297349748}[拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: Could not find server interface in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555607255}

[[找不到下行口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1844827437}

[[Interface *interface-name*: The length of FDISC RJT packet was invalid in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1074561508}

[[FDISC]{lang="EN-US"}]{#struct_0_x1489_93403_555541719}[拒绝报文长度不合法]{style="font-family:宋体"}

[[Interface *interface-name*: The server interface sent RJT packet to ENode in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1046864972}

[[下行口向]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x1835896729}[发送拒绝报文]{style="font-family:宋体"}

[[Interface *interface-name*: The resource allocation timer for FDISC ACC timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_555476183}

[[等待]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}]{#struct_0_x1489_93403_280731669}[报文的]{style="font-family:宋体"}[RA]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1558446083}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1915185394}[打开]{style="font-family:宋体"}[NPV]{lang="EN-US"}[协议的调试信息开关，]{style="font-family:宋体"}[NPV]{lang="EN-US"}[设备在收到登录请求时如果查找上行口失败会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc npv]{lang="EN-US"}]{#struct_0_x1489_93403_555410647}

[\*Nov  8 17:04:37:855 2011 Sysname FCLINK/7/NPV: -MDC=1; Interface FC1/0/1: Failed to find the external interface in VSAN *2*.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1802262600}*[在]{style="font-family:宋体"}[VSAN2]{lang="EN-US"}[内查找上行口失败]{style="font-family:宋体"}*

::: {#185931211 .myid}
[]{#_Toc404797587}[]{#struct_0_x1489_93403_x1338230026}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc rm**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1229103301}

[**[debugging fc rm]{lang="EN-US"}**[ { **all** \| **error** \| **fib** \| **static** \| **table** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1144745582}

[**[undo debugging fc rm]{lang="EN-US"}**[ { **all** \| **error** \| **fib** \| **static** \| **table** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_2081611239}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1606541261}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1345480737}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_555869399}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1053734650}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x703966647}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1393875704}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_1650636150}[：]{style="font-family:宋体"}[表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_x1381799639}[：]{style="font-family:宋体"}[表示错误调试信息开关。]{style="font-family:宋体"}

[**[fib]{lang="EN-US"}**]{#struct_0_x1489_93403_x168756603}[：]{style="font-family:宋体"}[表示路由变化通知调试信息开关。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_x1489_93403_2125651209}[：表示静态路由调试信息开关。]{style="font-family:宋体"}

[**[table]{lang="EN-US"}**]{#struct_0_x1489_93403_555803863}[：]{style="font-family:宋体"}[表示路由表调试信息开关。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_308263143}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x59513906}

[**[debugging fc rm]{lang="EN-US"}**]{#struct_0_x1489_93403_1050938412}[命令用来打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理调试信息开关。]{style="font-family:宋体"}**[undo debugging fc rm]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x221067069}[路由管理调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-20 ]{lang="EN-US"}[debugging fc rm error]{lang="EN-US"}]{#struct_0_x1489_93403_1375701975}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1325552237}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1422999534}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_2121429055}

[[Failed to add a domain controller route.]{lang="EN-US"}]{#struct_0_x1489_93403_x1459273389}

[[添加域控制器路由失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1751687148}

[[Failed to send a routing message to the forwarding module.]{lang="EN-US"}]{#struct_0_x1489_93403_1656663145}

[[向转发模块发送路由消息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x970864903}

[[Failed to add a node to the static routing table.]{lang="EN-US"}]{#struct_0_x1489_93403_2121363519}

[[添加静态路由节点失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_530023564}

[[This VSAN already exists.]{lang="EN-US"}]{#struct_0_x1489_93403_x1295099349}

[[指定的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_299540943}[已经存在]{style="font-family:宋体"}

[[No module has registered domain event.]{lang="EN-US"}]{#struct_0_x1489_93403_2121297983}

[[没有模块注册]{style="font-family:宋体"}[domain]{lang="EN-US"}]{#struct_0_x1489_93403_1715909258}[事件]{style="font-family:宋体"}

[[Failed to send domain-id message.]{lang="EN-US"}]{#struct_0_x1489_93403_x549702595}

[[发送]{style="font-family:宋体"}[domain ID]{lang="EN-US"}]{#struct_0_x1489_93403_608708673}[信息失败]{style="font-family:宋体"}

[[Failed to add an ENode direct route.]{lang="EN-US"}]{#struct_0_x1489_93403_2121232447}

[[添加]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_142610511}[直连路由失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-21 ]{lang="EN-US"}[debugging fc rm fib]{lang="EN-US"}]{#struct_0_x1489_93403_x1866082831}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1327896077}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_753452771}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x653025985}

[[Notified flushing routes.]{lang="EN-US"}]{#struct_0_x1489_93403_488876693}

[[通知路由下刷]{style="font-family:宋体"}]{#struct_0_x1489_93403_2121691199}

[[Successfully sent a routing message to the forwarding module.]{lang="EN-US"}]{#struct_0_x1489_93403_113482805}

[[向转发模块发送路由消息成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_1159379182}

[[Started to flush routes.]{lang="EN-US"}]{#struct_0_x1489_93403_1742361961}

[[开始路由下刷]{style="font-family:宋体"}]{#struct_0_x1489_93403_2038675605}

[[Prepared to flush route *fcid/mask-length*, with the operation type as *type*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121625663}

[[准备路由下刷，操作类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1489_93403_x228079150}[取值为：]{style="font-family:宋体"}[modify]{lang="EN-US"}[（修改）、]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[Flushed route *fcid/mask-length*, with the operation type as *type*.]{lang="EN-US"}]{#struct_0_x1489_93403_1553340898}

[[路由下刷，操作类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x1489_93403_x770824918}[取值为：]{style="font-family:宋体"}[modify]{lang="EN-US"}[（修改）、]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[ ]{lang="EN-US" style="background:white"}

[[表1-22 ]{lang="EN-US"}[debugging fc rm static]{lang="EN-US"}]{#struct_0_x1489_93403_2121560127}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1086657773}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1698899840}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1582023115}

[[Added a static route *fcid/mask-length*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1575421176}

[[添加了一条静态路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_1418912963}

[[Deleted a static route *fcid/mask-length*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121494591}

[[删除了一条静态路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1411230352}

[ ]{lang="EN-US" style="background:white"}

[[表1-23 ]{lang="EN-US"}[debugging fc rm table]{lang="EN-US"}]{#struct_0_x1489_93403_x1869167754}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1089856909}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1133044024}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1016315215}

[[Received VSAN *vsan-id* creation event.]{lang="EN-US"}]{#struct_0_x1489_93403_x794202179}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2121953343}[创建事件]{style="font-family:宋体"}

[[Received VSAN *vsan-id* deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_1666876387}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_908004973}[删除事件]{style="font-family:宋体"}

[[Received VSAN *vsan-id* domain-change event, from *domain-id* to *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1266312382}

[[接收]{style="font-family:宋体"}[VSAN domain]{lang="EN-US"}]{#struct_0_x1489_93403_x1145160419}[变化事件]{style="font-family:宋体"}

[[Got domain id list.]{lang="EN-US"}]{#struct_0_x1489_93403_2121887807}

[[获取]{style="font-family:宋体"} [domain id]{lang="EN-US"}]{#struct_0_x1489_93403_x233918020}[列表]{style="font-family:宋体"}

[[Successfully sent domain-id message.]{lang="EN-US"}]{#struct_0_x1489_93403_1739425742}

[[发送]{style="font-family:宋体"}[domain-id]{lang="EN-US"}]{#struct_0_x1489_93403_x1461334645}[信息成功]{style="font-family:宋体"}

[[Received ENode FlOGI event with FC ID *fcid* in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2121429056}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1459207853}[内]{style="font-family:宋体"}[ENode]{lang="EN-US"}[注册事件]{style="font-family:宋体"}

[[Received ENode FLOGO event with FC ID *fcid* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1903838100}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_992274117}[内]{style="font-family:宋体"}[ENode]{lang="EN-US"}[注销事件]{style="font-family:宋体"}

[ ]{lang="EN-US" style="background:white"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_492750377}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_2121363520}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理模块的路由变化通知调试信息开关，在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内添加一条静态路由，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc rm fib]{lang="EN-US"}]{#struct_0_x1489_93403_530482319}

[\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; \[VSAN 1\] Prepared to flush route 010101/24, with the operation type as modify.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x760111910}*[准备路由下刷]{style="font-family:宋体"}*

[[\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; Started to flush routes.]{lang="EN-US"}]{#struct_0_x1489_93403_1501402458}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_2111322668}*[开始路由下刷]{style="font-family:宋体"}*

[[\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; Notified flushing routes.]{lang="EN-US"}]{#struct_0_x1489_93403_x208597303}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_2121297984}*[通知路由下刷]{style="font-family:宋体"}*

[[\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; \[VSAN 1\] Flushed route 010101/24, with the operation type as modify.]{lang="EN-US"}]{#struct_0_x1489_93403_1716105866}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1008901412}*[路由下刷]{style="font-family:宋体"}*

[[\*May 11 15:44:17:548 2011 Sysname FCRM/7/fib: -MDC=1; \[VSAN 1\] Successfully sent a routing message to the forwarding module.]{lang="EN-US"}]{#struct_0_x1489_93403_624199753}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x54992914}*[成功向转发模块发送路由消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1327704865}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理模块的静态路由调试信息开关，在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内添加一条静态路由，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc rm static]{lang="EN-US"}]{#struct_0_x1489_93403_x388865767}

[\*May 11 15:50:08:596 2011 Sysname FCRM/7/static: -MDC=1; \[VSAN 1\] Added a static route 010202/24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x169463495}*[添加了一条静态路由]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_2121232448}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理模块的静态路由调试信息开关，在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内删除一条静态路由，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc rm static]{lang="EN-US"}]{#struct_0_x1489_93403_142020687}

[\*May 11 15:50:35:140 2011 Sysname FCRM/7/static: -MDC=1; \[VSAN 1\] Deleted a static route 010202/24.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x588742884}*[删除了一条静态路由]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_486427373}[打开所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[FC]{lang="EN-US"}[路由管理模块的路由表调试信息开关，在创建]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[时，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc rm table]{lang="EN-US"}]{#struct_0_x1489_93403_1948622047}

[\*May 11 15:53:04:557 2011 Sysname FCRM/7/table: -MDC=1; Received VSAN 2 creation event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x581543334}*[接收]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[创建事件]{style="font-family:宋体"}*

::: {#192716435 .myid}
[]{#_Toc257797065}[]{#_Toc248640986}[]{#_Toc207446736}[]{#_Toc207445113}[]{#_Toc207444972}[]{#_Toc404797588}[]{#struct_0_x1489_93403_1916194864}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc zone**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1631594636}

[**[debugging fc zone]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_2121691200}

[**[undo debugging fc zone]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1460954052}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1108716209}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_1111094966}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x232925289}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_227777529}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_565216815}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_2121625664}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x228537902}[：]{style="font-family:宋体"}[表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_1572441246}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_1641267171}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_455408915}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_179716165}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_370074613}

[**[debugging fc zone]{lang="EN-US"}**]{#struct_0_x1489_93403_2121560128}[命令用来打开]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fc zone]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}]{#struct_0_x1489_93403_1697916800}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-24 ]{lang="EN-US"}[debugging fc zone error]{lang="EN-US"}]{#struct_0_x1489_93403_x1427947333}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1083639501}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1816072404}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1654397935}

[[Failed to create socket for sending distribute packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x829229837}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2121494592}[内发送扩散报文时创建]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to allocate timer resource for distribute packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1411033744}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x844125016}[内扩散时分配定时器资源失败]{style="font-family:宋体"}

[[The length of packet exceeds the limit.]{lang="EN-US"}]{#struct_0_x1489_93403_320254715}

[[报文长度超出规格上限]{style="font-family:宋体"}]{#struct_0_x1489_93403_2121953344}

[[Failed to create timer for resending MRRA request frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1666548707}

[[创建]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_2121117264}[请求重发定时器失败，合并终止]{style="font-family:宋体"}

[[Failed to send MRRA request frame, because the E-Port is down or the specified VSAN doesn\'t exist on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1688777309}

[[发送]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_2121887808}[请求失败，]{style="font-family:宋体"}[E]{lang="EN-US"}[端口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态或者指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Failed to send MRRA request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x233590340}

[[发送]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x1355095432}[请求失败]{style="font-family:宋体"}

[[Failed to send MRRA request frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x798892329}

[[发送]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_2121429053}[请求报文失败，合并终止]{style="font-family:宋体"}

[[Failed to send MRRA ACC frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1458880173}

[[发送]{style="font-family:宋体"}[MRRA ACC]{lang="EN-US"}]{#struct_0_x1489_93403_1889842810}[失败]{style="font-family:宋体"}

[[Failed to receive MR request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_754683187}

[[接收]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_2121363517}[请求失败]{style="font-family:宋体"}

[[Failed to create timer for waiting for MR request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_530941068}

[[创建等待]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_899814242}[请求定时器失败]{style="font-family:宋体"}

[[Failed to receive MRRA response frame, and the merge is over on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1228109535}

[[接收]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_2121297981}[响应报文失败，合并结束]{style="font-family:宋体"}

[[Failed to receive MR response frame and the merge is over on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1715778186}

[[接收]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x559699549}[响应报文失败，合并结束]{style="font-family:宋体"}

[[Failed to receive I/O sync message from master slot.]{lang="EN-US"}]{#struct_0_x1489_93403_2121232445}

[[接收主板同步过来的消息数据失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_142741583}

[[Failed to create clock for timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1889217140}

[[为定时器创建物理时钟失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1031471396}

[[Failed to set clock for timer.]{lang="EN-US"}]{#struct_0_x1489_93403_2121691197}

[[为定时器设置物理时钟失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_113351733}

[[Failed to create walk handle for zone avl tree.]{lang="EN-US"}]{#struct_0_x1489_93403_x1004816730}

[[为]{style="font-family:宋体"}[Zone AVL Tree]{lang="EN-US"}]{#struct_0_x1489_93403_2121625661}[创建遍历句柄失败]{style="font-family:宋体"}

[[Failed to create walk handle for zone alias avl tree.]{lang="EN-US"}]{#struct_0_x1489_93403_x228210222}

[[为]{style="font-family:宋体"}[Zone Alias AVL Tree]{lang="EN-US"}]{#struct_0_x1489_93403_46399668}[创建遍历句柄失败]{style="font-family:宋体"}

[[Failed to create timer for retrying to initialize event.]{lang="EN-US"}]{#struct_0_x1489_93403_2121560125}

[[创建事件注册初始化重试定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1698768768}

[[Failed to delete ACL rule.]{lang="EN-US"}]{#struct_0_x1489_93403_838841197}

[[删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1489_93403_1059325229}[规则失败]{style="font-family:宋体"}

[[Failed to delete ACL rule from driver.]{lang="EN-US"}]{#struct_0_x1489_93403_2121494589}

[[从驱动删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1489_93403_x1410706065}[规则失败]{style="font-family:宋体"}

[[Failed to add ACLrule to driver.]{lang="EN-US"}]{#struct_0_x1489_93403_x1878714132}

[[添加]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1489_93403_2121953341}[规则到驱动失败]{style="font-family:宋体"}

[[Failed to delete ACL rule, because the specified ACLrule doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1489_93403_1666745315}

[[删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1489_93403_2121887805}[规则失败，指定规则不存在]{style="font-family:宋体"}

[[Failed to get local domain ID.]{lang="EN-US"}]{#struct_0_x1489_93403_x233786948}

[[获取本机]{style="font-family:宋体"}[domain ID]{lang="EN-US"}]{#struct_0_x1489_93403_632617340}[失败]{style="font-family:宋体"}

[[No reachable route exists.]{lang="EN-US"}]{#struct_0_x1489_93403_2121429054}

[[没有可达路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1459338925}

[[Failed to allocate timer resource for distribute request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_852077982}

[[创建等待请求报文定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_2121363518}

[[NNode already exists.]{lang="EN-US"}]{#struct_0_x1489_93403_529958028}

[[N]{lang="EN-US"}]{#struct_0_x1489_93403_1422346246}[节点已经存在]{style="font-family:宋体"}

[[Failed to delete NNode, because the WWN of specified NNode and the WWN of hash NNode don\'t match.]{lang="EN-US"}]{#struct_0_x1489_93403_2121297982}

[[删除]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1489_93403_1715974794}[节点失败，指定]{style="font-family:宋体"}[N]{lang="EN-US"}[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[与]{style="font-family:宋体"}[hash N]{lang="EN-US"}[节点的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Failed to delete NNode, because the specified NNode doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1489_93403_2121232446}

[[删除]{style="font-family:宋体"}[N]{lang="EN-US"}]{#struct_0_x1489_93403_142676047}[节点失败，指定]{style="font-family:宋体"}[N]{lang="EN-US"}[节点不存在]{style="font-family:宋体"}

[[The latter frag is not consistent with the first frag:  first's socket=*socket-id-1*, first's VSAN=*vsan-id-1*, latter's socket=*socket-id-2*, latter's VSAN=*vsan-id-2.*]{lang="EN-US"}]{#struct_0_x1489_93403_455947142}

[[后续分片与首片分片信息不一致：首片]{style="font-family:宋体"}[socket=*socket-id-1*]{lang="EN-US"}]{#struct_0_x1489_93403_2121691198}[，首片]{style="font-family:宋体"}[VSAN=*vsan-id-1*]{lang="EN-US"}[，后续]{style="font-family:宋体"}[socket=*socket-id-2*]{lang="EN-US"}[，后续]{style="font-family:宋体"}[VSAN=*vsan-id-2*]{lang="EN-US"}

[[The latter frag is not consistent with the first frag: first's IF= *interface-name-1*, latter's IF= *interface-name-2.*]{lang="EN-US"}]{#struct_0_x1489_93403_113548341}

[[后续分片与首片分片信息不一致：首片接口名称为]{style="font-family:宋体"}*[interface-name -1]{lang="EN-US"}*]{#struct_0_x1489_93403_764119345}[，后续接口名称为]{style="font-family:宋体"}*[interface-name -2]{lang="EN-US"}*

[[Failed to get the MTU of interface *interface-name.*]{lang="EN-US"}]{#struct_0_x1489_93403_2121625662}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x228144686}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get the destination interface option of socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121560126}

[[从值为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1489_93403_1698834304}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[获取目的接口选项数据失败]{style="font-family:宋体"}

[[Failed to send message to I/O slot by socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x19518960}

[[通过值为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*]{#struct_0_x1489_93403_2121494590}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[发送消息到]{style="font-family:宋体"}[I/O]{lang="EN-US"}[板失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[debugging fc zone event]{lang="EN-US"}]{#struct_0_x1489_93403_x1411164816}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1075300109}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_806778056}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1366125900}

[[\"New Neighbor Event\" happened on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121953342}

[[发现新邻居事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_1666941923}

[[\"Delete Neighbor Event\" happened on interface *interface-name* in VSAN *vsan-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1765357759}

[[发生删除邻居事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x158462829}

[[Created timer for resending MRRA request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1747257685}

[[创建]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_2121887806}[请求报文重发定时器]{style="font-family:宋体"}

[[The timer of waiting for request packet timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x233983556}

[[等待请求报文定时器超时]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1771743344}

[[Refreshed the timer for waiting for request packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1072040993}

[[刷新请求报文等待定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_2121429051}

[[The timer of waiting for ACA reply packet timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1459011245}

[[ACA]{lang="EN-US"}]{#struct_0_x1489_93403_x365052535}[应答报文等待定时器超时]{style="font-family:宋体"}

[[The timer of waiting for SFC reply packet timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x834074217}

[[SFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1205596350}[应答报文等待定时器超时]{style="font-family:宋体"}

[[The timer of waiting for UFC reply packet timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121363515}

[[UFC]{lang="EN-US"}]{#struct_0_x1489_93403_530809996}[应答报文等待定时器超时]{style="font-family:宋体"}

[[The timer of waiting for RCA reply packet timed out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1155978153}

[[RCA]{lang="EN-US"}]{#struct_0_x1489_93403_2083104823}[应答报文等待定时器超时]{style="font-family:宋体"}

[[The merge is over, because the MRRA request frame has been sent *times* times on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121297979}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1716302461}[内合并结束，]{style="font-family:宋体"}[MRRA]{lang="EN-US"}[请求报文已经被发送]{style="font-family:宋体"}*[times]{lang="EN-US"}*[次]{style="font-family:宋体"}

[[The merge is over, because the MR request frame has been sent *times* times on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_525802515}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2121232443}[内合并结束，]{style="font-family:宋体"}[MR]{lang="EN-US"}[请求报文已经被发送]{style="font-family:宋体"}*[times]{lang="EN-US"}*[次]{style="font-family:宋体"}

[[The merge is over, because the neighbor has replied busy RJT packet *times* times on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_142348367}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x102854358}[内合并结束，该邻居回复]{style="font-family:宋体"}[busy RJT]{lang="EN-US"}[报文]{style="font-family:宋体"}*[times]{lang="EN-US"}*[次，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[The size of packet is too large, and isolated the E-port on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121691195}

[[报文长度超出限制，隔离]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_113220661}[端口]{style="font-family:宋体"}

[[Failed to allocate the resource for merged zoning database.]{lang="EN-US"}]{#struct_0_x1489_93403_x246594727}

[[合并]{style="font-family:宋体"}[Zone]{lang="EN-US"}]{#struct_0_x1489_93403_691420865}[数据库时申请资源失败]{style="font-family:宋体"}

[[Finished closing the service and reclaiming the resource for FCF.]{lang="EN-US"}]{#struct_0_x1489_93403_x1014092762}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x129621003}[模式下的服务关闭和资源回收完成]{style="font-family:宋体"}

[[Finished closing the service and reclaiming the resource for NPV.]{lang="EN-US"}]{#struct_0_x1489_93403_2121625659}

[[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_x228734507}[模式下的服务关闭和资源回收完成]{style="font-family:宋体"}

[[Finished starting the service and allocating the resource for FCF.]{lang="EN-US"}]{#struct_0_x1489_93403_x318492913}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_2121560123}[模式下的服务开启和资源申请完成]{style="font-family:宋体"}

[[Failed to start the service and allocate the resource for FCF.]{lang="EN-US"}]{#struct_0_x1489_93403_1698637696}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_1575537934}[模式下的服务开启和资源申请失败]{style="font-family:宋体"}

[[Received the event notification for creating VSAN *vsan-id* from fcfabricd.]{lang="EN-US"}]{#struct_0_x1489_93403_2121494587}

[[收到]{style="font-family:宋体"}[fcfabricd]{lang="EN-US"}]{#struct_0_x1489_93403_x1410837137}[创建]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[的事件通知]{style="font-family:宋体"}

[[Received the event notification for destroying VSAN *vsan-id* from fcfabricd.]{lang="EN-US"}]{#struct_0_x1489_93403_x729478628}

[[收到]{style="font-family:宋体"}[fcfabricd]{lang="EN-US"}]{#struct_0_x1489_93403_675784241}[删除]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[的事件通知]{style="font-family:宋体"}

[[Received the event notification for changing domain ID in VSAN *vsan-id* from fcfabricd.]{lang="EN-US"}]{#struct_0_x1489_93403_2121953339}

[[收到]{style="font-family:宋体"}[fcfabricd]{lang="EN-US"}]{#struct_0_x1489_93403_1667269604}[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内]{style="font-family:宋体"}[domain id]{lang="EN-US"}[变化的事件通知]{style="font-family:宋体"}

[[Received the event notification for changing switch mode to NPV from fcfabricd.]{lang="EN-US"}]{#struct_0_x1489_93403_1005593552}

[[收到]{style="font-family:宋体"}[fcfabricd]{lang="EN-US"}]{#struct_0_x1489_93403_2121887803}[交换机变化到]{style="font-family:宋体"}[NPV]{lang="EN-US"}[模式的事件通知]{style="font-family:宋体"}

[[Received the event notification for changing switch mode to FCF from fcfabricd.]{lang="EN-US"}]{#struct_0_x1489_93403_x234180164}

[[收到]{style="font-family:宋体"}[fcfabricd]{lang="EN-US"}]{#struct_0_x1489_93403_x1104354806}[交换机变化到]{style="font-family:宋体"}[FCF]{lang="EN-US"}[模式的事件通知]{style="font-family:宋体"}

[[Registered fabric service for FCF successfully.]{lang="EN-US"}]{#struct_0_x1489_93403_2121429052}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x1458945709}[模式下注册]{style="font-family:宋体"}[fabric]{lang="EN-US"}[服务成功]{style="font-family:宋体"}

[[Finished starting the service for NPV.]{lang="EN-US"}]{#struct_0_x1489_93403_2121363516}

[[NPV]{lang="EN-US"}]{#struct_0_x1489_93403_530875532}[模式下服务开启完成]{style="font-family:宋体"}

[[Frag waiting timer is timeout, socket=*socket-id* VSAN=*vsan-id*, IF= *interface-name.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1072342378}

[[分片等待定时器超时，]{style="font-family:宋体"}[soket=*socket-id*, VSAN=*vsan-id*, IF= *interface-name*]{lang="EN-US"}]{#struct_0_x1489_93403_2121297980}

[[Isolated interface *interface-name* in VSAN *vsan-id* successfully.]{lang="EN-US"}]{#struct_0_x1489_93403_1715843722}

[[成功将接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_643212877}[在]{style="font-family:宋体"}[VSAN *vsan-id* ]{lang="EN-US"}[内隔离]{style="font-family:宋体"}

[[The isolation status of interface *interface-name* is cleared in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121232444}

[[清除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_142807119}[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内的隔离状态]{style="font-family:宋体"}

[[Failed to isolate interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1064085618}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_2121691196}[内隔离接口]{style="font-family:宋体"}*[interface-nam]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[The isolation status of interface *interface-name* is cleared in all VSANs.]{lang="EN-US"}]{#struct_0_x1489_93403_113417269}

[[清除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_2121625660}[在所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内的隔离状态]{style="font-family:宋体"}

[[The isolation status of interface *interface-name* is cleared for interface physical-layer event.]{lang="EN-US"}]{#struct_0_x1489_93403_x228275758}

[[当接口上发生物理事件的时候，将接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_2018943712}[的隔离状态清除]{style="font-family:宋体"}

[[The specified VSAN *vsan-id* doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1489_93403_2121560124}

[[指定的]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1698703232}[不存在]{style="font-family:宋体"}

[[Received message *message-type*.]{lang="EN-US"}]{#struct_0_x1489_93403_2121494588}

[[收到]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x1489_93403_x1410640529}[消息]{style="font-family:宋体"}

[[消息类型为：]{style="font-family:宋体"}]{#struct_0_x1489_93403_750635879}

[[\"FCZONE_SYNCMSG_TYPE_DEACTZNST\"]{lang="EN-US"}]{#struct_0_x1489_93403_2121953340}

[[\"FCZONE_SYNCMSG_TYPE_ACTZNST\"]{lang="EN-US"}]{#struct_0_x1489_93403_1666810851}

[[\"FCZONE_SYNCMSG_TYPE_BOARDSMOOTH\"]{lang="EN-US"}]{#struct_0_x1489_93403_2121887804}

[[\"FCZONE_SYNCMSG_TYPE_NNODE_BATCH\"]{lang="EN-US"}]{#struct_0_x1489_93403_x233852484}

[[\"FCZONE_SYNCMSG_TYPE_NNODE_LOGIN\"]{lang="EN-US"}]{#struct_0_x1489_93403_x993211307}

[[\"FCZONE_SYNCMSG_TYPE_NNODE_LOGOUT\"]{lang="EN-US"}]{#struct_0_x1489_93403_x607454300}

[[\"FCZONE_SYNCMSG_TYPE_DEFAULT_ENABLE\"]{lang="EN-US"}]{#struct_0_x1489_93403_224904141}

[[\"FCZONE_SYNCMSG_TYPE_DEFAULT_DISABLE\"]{lang="EN-US"}]{#struct_0_x1489_93403_x607519836}

[[\"FCZONE_SYNCMSG_TYPE_VSAN_DELETE\"]{lang="EN-US"}]{#struct_0_x1489_93403_930745014}

[[\"FCZONE_SYNCMSG_TYPE_DOMAIN_CHANGE\"]{lang="EN-US"}]{#struct_0_x1489_93403_x1645919990}

[[\"FCZONE_SYNCMSG_TYPE_DEBUG_SET\"]{lang="EN-US"}]{#struct_0_x1489_93403_x607585372}

[[\"FCZONE_SYNCMSG_TYPE_DEBUG_BATCH\"]{lang="EN-US"}]{#struct_0_x1489_93403_x1371260850}

[ ]{lang="EN-US"}

[[表1-26 ]{lang="EN-US"}[debugging fc zone packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1463477762}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1100062765}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1111955535}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x607650908}

[[The ACA packet has been sent three times to domain *domain-id* in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x189533789}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1468084168}[内]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文已向]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的设备发送了三次]{style="font-family:宋体"}

[[The SFC packet has been sent three times to domain *domain-id* in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_306040813}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607192156}[内]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文已向]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的设备发送了三次]{style="font-family:宋体"}

[[The UFC packet has been sent three times to domain *domain-id* in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1389561763}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x441128092}[内]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文已向]{style="font-family:宋体"}[Domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的设备发送了三次]{style="font-family:宋体"}

[[The RCA packet has been sent three times to domain *domain-id* in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x259541604}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x883589681}[内]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文已向]{style="font-family:宋体"}[Domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的设备发送了三次]{style="font-family:宋体"}

[[The ACA packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607257692}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x930132343}[内]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文已发送]{style="font-family:宋体"}

[[The SFC packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x407844030}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1204304813}[内]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文已发送]{style="font-family:宋体"}

[[The UFC packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607323228}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1802271875}[内]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文已发送]{style="font-family:宋体"}

[[The RCA packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1412602056}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x422372440}[内]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文已发送]{style="font-family:宋体"}

[[The ACA packet has been received in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607388764}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1755354610}[内接收到]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The SFC packet has been received in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x316058938}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1918339438}[内接收到]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The UFC packet has been received in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x606930012}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x167906875}[内接收到]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The RCA packet has been received in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_708238662}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1258404161}[内接收到]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The SFC packet is not sourced from the manager in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1319489217}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319423681}[内收到的]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文的地址不是管理交换机地址]{style="font-family:宋体"}

[]{#struct_0_x1489_93403_1319358145}[]{#OLE_LINK4}[[Received]{lang="EN-US"}]{#OLE_LINK3}[ SFC packet at neither ACA nor SFC phase  in VSAN *vsan-id*.]{lang="EN-US"}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_611494428}[内在非]{style="font-family:宋体"}[ACA]{lang="EN-US"}[或]{style="font-family:宋体"}[SFC]{lang="EN-US"}[阶段收到]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received malformed SFC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1319816897}

[[报文长度不合法]{style="font-family:宋体"}]{#struct_0_x1489_93403_981790042}

[[Received unknown Operation Request SFC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1319751361}

[[收到操作请求不合法报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2091544529}

[[Received conflict SFC packet in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1319292610}

[[收到的多个]{style="font-family:宋体"}[SFC]{lang="EN-US"}]{#struct_0_x1489_93403_1319227074}[报文之间冲突]{style="font-family:宋体"}

[[The RJT reply packet has been sent for fabric changed in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x606995548}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x620218167}[内]{style="font-family:宋体"}[RJT]{lang="EN-US"}[应答报文已发送，因为]{style="font-family:宋体"}[f]{lang="EN-US" style="text-transform:uppercase"}[abric]{lang="EN-US"}[网络发生了变化，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[The RJT reply packet has been sent for switch is busy in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1436525959}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607454299}[内]{style="font-family:宋体"}[RJT]{lang="EN-US"}[应答报文已发送，因为]{style="font-family:宋体"}[f]{lang="EN-US" style="text-transform:uppercase"}[abric]{lang="EN-US"}[网络正忙，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[The RJT reply packet has been sent for processing failed in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1731869738}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1454349918}[内]{style="font-family:宋体"}[RJT]{lang="EN-US"}[应答报文已发送，因为处理失败，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received RJT reply packet of *domain domain-id* for ACA packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_x680807027}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607519835}[内接收到来自]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文的拒绝回应报文，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received RJT reply packet of *domain domain-id* for SFC packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_930941622}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1467667898}[内接收到来自]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文的拒绝回应报文，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received RJT reply packet of *domain domain-id* for UFC packet in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_x607585371}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1371457458}[内接收到来自]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文的拒绝回应报文，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[The ACC reply packet for ACA packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319489218}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319423682}[内]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文已发送]{style="font-family:宋体"}

[[The ACC reply packet for SFC or UFC packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1687050536}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319358146}[内]{style="font-family:宋体"}[SFC]{lang="EN-US"}[或]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文已发送]{style="font-family:宋体"}

[[The ACC reply packet for RCA packet has been sent in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_611428892}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319816898}[内]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文已发送]{style="font-family:宋体"}

[[Received all ACC reply packet for ACA packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1204630103}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607650907}[内接收到所有]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[Received all ACC reply packet for SFC packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x188812893}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x734307265}[内接收到所有]{style="font-family:宋体"}[SFC]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[Received all ACC reply packet for UFC packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607192155}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1389758371}[内接收到所有]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[Received all ACC reply packet for RCA packet in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1531368000}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x607257691}[内接收到所有]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[The invalid ACA packet has been discarded in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1319751362}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319292607}[内丢弃无效的]{style="font-family:宋体"}[ACA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The invalid UFC packet has been discarded in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1024269361}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319227071}[内丢弃无效的]{style="font-family:宋体"}[UFC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The invalid RCA packet has been discarded in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1021082115}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319161535}[内丢弃无效的]{style="font-family:宋体"}[RCA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Sent MRRA request frame successfully on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x929935735}

[[发送]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x667835413}[请求]{style="font-family:宋体"}

[[Received MRRA request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x607323227}

[[收到]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_1801288835}[请求]{style="font-family:宋体"}

[[Sent MRRA request frame *times* times on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x421607167}

[[发送]{style="font-family:宋体"}*[times]{lang="EN-US"}*]{#struct_0_x1489_93403_x607388763}[次]{style="font-family:宋体"}[MRRA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Sent MR request frame *times* times on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1755682290}

[[发送]{style="font-family:宋体"}*[times]{lang="EN-US"}*]{#struct_0_x1489_93403_x606930011}[次]{style="font-family:宋体"}[MR]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Sent MRRA ACC response frame successfully on interface *interface-name* in VSAN *vsan-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x167972411}

[[发送]{style="font-family:宋体"}[MRRA ACC]{lang="EN-US"}]{#struct_0_x1489_93403_372509408}[成功]{style="font-family:宋体"}

[[Received MRRA ACC response frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x606995547}

[[接收到]{style="font-family:宋体"}[MRRA ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x620021559}[报文]{style="font-family:宋体"}

[[Received MRRA RJT response frame because of neighbor\'s busyness, and resent MRRA request later on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*)*.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1243319029}

[[收到]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x607454302}[报文的忙碌状态拒绝报文，稍后重发]{style="font-family:宋体"}[MRRA]{lang="EN-US"}[请求，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MRRA ACC frame, but the neighbor can't accept so large packet waiting for receiving again on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_224773069}

[[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x607519838}[协商完成，但邻居没有足够资源处理报文数据]{style="font-family:宋体"}

[[Sent MR request frame successfully on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_931662518}

[[发送]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x1157726124}[请求]{style="font-family:宋体"}

[[Received MR request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x607585374}

[[收到]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x1371654066}[请求]{style="font-family:宋体"}

[[Sent MR ACC response frame successfully on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x607650910}

[[发送]{style="font-family:宋体"}[MR ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x189009500}

[[Received MR ACC response frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1041230903}

[[收到]{style="font-family:宋体"}[MR ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x607192158}[，]{style="font-family:宋体"}[MR]{lang="EN-US"}[协商结束]{style="font-family:宋体"}

[[Sent MR RJT response frame, because the zone mode is inconsistent on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319489215}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1319423679}[响应报文，因为合并发起端的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式和本地不一致，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because the zone Merge-Control or Default-Zone does not match on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1686329651}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1319358143}[响应报文，因为合并发起端的]{style="font-family:宋体"}[merge-control]{lang="EN-US"}[或]{style="font-family:宋体"}[default zone]{lang="EN-US"}[策略等和本地的不一致，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because the Hard Zone Attribute is inconsistent on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_611101212}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1319816895}[响应报文，因为合并发起端的硬件]{style="font-family:宋体"}[Zone]{lang="EN-US"}[使能情况和本地的不一致，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because the Merge-Control setting is restrict and the adjacent zoning database is not the same as the local zoning database on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_981921114}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1319751359}[响应报文，因为]{style="font-family:宋体"}[Merge-Control]{lang="EN-US"}[为]{style="font-family:宋体"}[restrict]{lang="EN-US"}[时，合并发起端和本地的数据不完全相同，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because failed to merge the active zoneset on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_x929739127}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x1898767632}[响应报文，合并]{style="font-family:宋体"}[active zoneset]{lang="EN-US"}[失败，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because the size of the merged packet was too large on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x607323230}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1801747586}[响应报文，合并后数据超出限制，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because the number of zoning objects exceeds the limit on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x607388766}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1755485682}[响应报文，]{style="font-family:宋体"}[zoning]{lang="EN-US"}[对象个数超出限制，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Sent MR RJT response frame, because failed to merge the database on interface *interface-name* in VSAN *vsan-id* (reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x606930014}

[[发送]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x167775803}[响应报文，合并]{style="font-family:宋体"}[database]{lang="EN-US"}[失败，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame because the zone mode is inconsistent, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319161536}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1058639978}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，因为合并时两端设备]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式不一致，结束合并，并隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame because the Hard Zone Attribute is inconsistent, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319096000}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x562303397}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，因为合并时两端设备硬件]{style="font-family:宋体"}[Zone ]{lang="EN-US"}[使能情况不一致，隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame because the zone Merge-Control or Default-Zone does not match, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319554752}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2096769301}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，因为在增强]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，合并时两端设备的]{style="font-family:宋体"}[merge-control]{lang="EN-US"}[、]{style="font-family:宋体"}[default zone]{lang="EN-US"}[策略等不一致，合并失败，隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame because Merge-Control is restrict and the adjacent zoning database is not the same as the local zoning database on interface *interface-name* in VSAN *vsan-id*. (reason code=*reason-code*, reason code explanation=*code-explanation*)]{lang="EN-US"}]{#struct_0_x1489_93403_1319489216}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319423680}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，因为在增强]{style="font-family:宋体"}[zone]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[merge-control]{lang="EN-US"}[为]{style="font-family:宋体"}[restrict]{lang="EN-US"}[时，合并两端的]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据库不完全相同，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, failed to merge the active zoneset, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x606995550}

[[接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x619693880}[报文，]{style="font-family:宋体"}[active zoneset]{lang="EN-US"}[合并失败，隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, and the number of zoning objects exceeded the limit on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x607454301}

[[接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_224969677}[报文，]{style="font-family:宋体"}[Zone]{lang="EN-US"}[对象个数超出规格，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, and failed to merge database on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x607519837}

[[接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_930810550}[报文，合并]{style="font-family:宋体"}[database]{lang="EN-US"}[失败，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, and failed to merge database in Basic Zoning on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319816896}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1319751360}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，在基本]{style="font-family:宋体"}[Zone]{lang="EN-US"}[模式下，数据库合并失败，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, the size of the merged packet exceeded the limit, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1461155622}

[[接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x607585373}[报文，合并后的数据超出限制，隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Received MR RJT response frame, failed to merge the database in Enhanced Zoning, and isolated port on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1319292605}

[[VSAN vsan-id]{lang="EN-US"}]{#struct_0_x1489_93403_1319227069}[内接收到]{style="font-family:宋体"}[MR RJT]{lang="EN-US"}[报文，在增强]{style="font-family:宋体"}[zone]{lang="EN-US"}[模式下，]{style="font-family:宋体"}[Zone]{lang="EN-US"}[数据库合并失败，隔离端口，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[Discarded invalid MRRA request frame.]{lang="EN-US"}]{#struct_0_x1489_93403_x189468253}

[[丢弃无效]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x607192157}[请求报文]{style="font-family:宋体"}

[[Discarded invalid MRRA response frame.]{lang="EN-US"}]{#struct_0_x1489_93403_1389627299}

[[丢弃无效]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x607257693}[应答报文]{style="font-family:宋体"}

[[Discarded invalid MR request frame.]{lang="EN-US"}]{#struct_0_x1489_93403_x930066807}

[[丢弃无效]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x607323229}[请求报文]{style="font-family:宋体"}

[[Discarded invalid MR response frame.]{lang="EN-US"}]{#struct_0_x1489_93403_1802206339}

[[丢弃无效]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x607388765}[应答报文]{style="font-family:宋体"}

[[Failed to send MR request frame, because the E-Port is down on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1755289074}

[[发送]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x606930013}[请求报文失败，]{style="font-family:宋体"}[E]{lang="EN-US"}[端口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Failed to send MR request frame on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x167841339}

[[发送]{style="font-family:宋体"}[MR]{lang="EN-US"}]{#struct_0_x1489_93403_x606995549}[请求报文失败]{style="font-family:宋体"}

[[Received MRRA request frame again on interface *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x620152631}

[[接收到重发的]{style="font-family:宋体"}[MRRA]{lang="EN-US"}]{#struct_0_x1489_93403_x607454304}[请求]{style="font-family:宋体"}

[[Sent MRRA RJT response frame, because local switch status is in busy on interface *interface-name* in VSAN *vsan-id*(reason code=*reason-code*, reason code explanation=*code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_225166285}

[[发送]{style="font-family:宋体"}[MRRA RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x607519840}[响应报文，本地交换机处于]{style="font-family:宋体"}[busy]{lang="EN-US"}[状态，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_931138233}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1949550051}[启动两台互联的]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[错误调试信息开关。在两台设备的]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[下都进行不重复的大规模]{style="font-family:宋体"}[Zone]{lang="EN-US"}[配置，重新连接设备端口，会输出下列合并后报文长度超长的错误调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc zone error]{lang="EN-US"}]{#struct_0_x1489_93403_x289075343}

[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/ERROR: The size of packet is too large, and isolated the E-port on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_1784688948}*[内，封装]{style="font-family:宋体"}[MRRA]{lang="EN-US"}[请求向端口]{style="font-family:宋体"}[Fc1/0/1]{lang="EN-US"}[端口进行发送时，发现报文长度超出限制，隔离]{style="font-family:宋体"}[E]{lang="EN-US"}[端口]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x607585376}[启动两台互联的]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[事件调试信息开关。在其中一台]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[下进行]{style="font-family:宋体"}[Zone]{lang="EN-US"}[配置，重新连接设备端口，会输出下列链路事件以及]{style="font-family:宋体"}[MERGE]{lang="EN-US"}[流程的事件调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc zone event]{lang="EN-US"}]{#struct_0_x1489_93403_x1918774701}

[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/EVENT: \"Delete Neighbor Event\" happened on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1567199991}*[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内，端口]{style="font-family:宋体"}[Fc1/0/1]{lang="EN-US"}[上报发生删除邻居事件]{style="font-family:宋体"}*

[[\*Oct 27 11:19:53:360 2010 Sysname FCZONE/7/EVENT: \"New Neighbor Event\" happened on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_1241391974}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1784688945}*[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内，端口]{style="font-family:宋体"}[Fc1/0/1]{lang="EN-US"}[上报发现新邻居事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_546573399}[启动两台互联的]{style="font-family:宋体"}[FC]{lang="EN-US"}[设备，打开]{style="font-family:宋体"}[FC Zone]{lang="EN-US"}[报文调试信息开关。在其中一台]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[下进行]{style="font-family:宋体"}[Zone]{lang="EN-US"}[配置，重新连接设备端口，会输出下列]{style="font-family:宋体"}[MERGE]{lang="EN-US"}[流程相关的调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc zone packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1918447021}

[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Sent MRRA request frame successfully on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1784688946}*[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内，从端口]{style="font-family:宋体"}[Fc1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[MRRA]{lang="EN-US"}[请求报文成功]{style="font-family:宋体"}*

[[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Received MRRA ACC response frame on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_x1918381485}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x163805011}*[在]{style="font-family:宋体"}[VSAN1]{lang="EN-US"}[内，接收到]{style="font-family:宋体"}[MRRA ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Sent MR request frame successfully on interface Fc1/0/1 in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_209152206}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1368497381}*[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内，]{style="font-family:宋体"}[ Fc1/0/1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[MR]{lang="EN-US"}[请求报文成功]{style="font-family:宋体"}*

[[\*Oct 27 11:19:53:360 2011 Sysname FCZONE/7/PACKET: Received MR ACC response frame on interfaceFc 1/0/1 in VSAN 1.]{lang="EN-US"}]{#struct_0_x1489_93403_x171626183}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1640021611}*[在]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内，接收到]{style="font-family:宋体"}[MR ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

::: {#1985791130 .myid}
[]{#_Toc404797589}[]{#struct_0_x1489_93403_x189140572}[]{#_Toc309983710}[]{#_Toc229990375}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcoe**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_872301666}

[**[debugging fcoe]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **fcm** \| **fip** \] \[ **receive** \| **send** \] \[ **interface** *interface*-*type* *interface*-*number* \] \| **timer** }]{lang="EN-US"}]{#struct_0_x1489_93403_x1199741896}

[**[undo]{lang="EN-US"}**[ **debugging** **fcoe** { **all** \| **error** \| **event** \| **packet** \[ **fcm** \| **fip** \] \[ **receive** \| **send** \] \[ **interface** *interface*-*type* *interface*-*number* \] \| **timer** }]{lang="EN-US"}]{#struct_0_x1489_93403_x473386819}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1682260543}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1693308757}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1800716554}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x607192160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1389954982}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1065175231}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_1054055091}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_x40706559}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_x1586219140}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x961158240}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[fcm]{lang="EN-US"}**]{#struct_0_x1489_93403_x607257696}[：表示经过封装的]{style="font-family:宋体"}[FC]{lang="EN-US"}[报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[fip]{lang="EN-US"}**]{#struct_0_x1489_93403_x929870199}[：表示]{style="font-family:宋体"}[FIP]{lang="EN-US"}[协议报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1489_93403_x696122909}[：表示接收报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1489_93403_x955827093}[：表示发送报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface]{lang="EN-US"}*[-*type* *interface*-*number*]{lang="EN-US"}]{#struct_0_x1489_93403_x118701353}[：表示指定接口的调试信息开关，]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type*]{lang="EN-US"}[只能是]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口。如果未指定本参数，表示所有]{style="font-family:宋体"}[VFC]{lang="DE"}[接口的调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_1177509410}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1734286066}

[**[debugging fcoe]{lang="EN-US"}**]{#struct_0_x1489_93403_x771871704}[命令用来打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fcoe]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x607323232}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1489_93403_1801616514}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1200419619}**[fcm]{lang="EN-US"}**[和]{style="font-family:宋体"}**[fip]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，表示同时指定这两类报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1489_93403_607234785}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，表示同时指定接收和发送的报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1209209562}**[interface]{lang="EN-US"}**[参数]{style="font-family:宋体"}[打开的]{style="font-family:宋体"}[指定接口的调试信息开关，只能通过在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令中指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数来关闭。]{style="font-family:宋体"}

[[表1-27 ]{lang="EN-US"}[debugging fcoe error]{lang="EN-US"}]{#struct_0_x1489_93403_x607388768}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1121404237}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1755092466}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_488389600}

[[Failed to notify driver that FCoE is enabled for VLAN *vlan-id* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_446450237}

[[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_1973626919}[使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[通报驱动失败]{style="font-family:宋体"}

[[Failed to notify driver that FCoE is disabled for VLAN *vlan-id* in VSAN *vsan-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x606930016}

[[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x167644731}[去使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[通报驱动失败]{style="font-family:宋体"}

[[PhyIoCtl cmd *cmd* is unknown.]{lang="EN-US"}]{#struct_0_x1489_93403_x1183517713}

[[物理控制命令不存在]{style="font-family:宋体"}]{#struct_0_x1489_93403_781662772}

[[FCoE Smooth: Failed to get smooth binding data.]{lang="EN-US"}]{#struct_0_x1489_93403_x606995552}

[[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x619824952}[获取平滑的绑定信息失败]{style="font-family:宋体"}

[[FCoE Smooth: Failed to get smooth mapping data.]{lang="EN-US"}]{#struct_0_x1489_93403_x258759287}

[[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x1313463567}[获取平滑的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的映射信息失败]{style="font-family:宋体"}

[[FCoE Smooth: Failed to get smooth VFC interface state data.]{lang="EN-US"}]{#struct_0_x1489_93403_x607454303}

[[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_224838605}[获取平滑的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口状态信息失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[debugging fcoe event]{lang="EN-US"}]{#struct_0_x1489_93403_934705931}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1123435565}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_492206800}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_80724917}

[[Successfully created *Interface-name.*]{lang="EN-US"}]{#struct_0_x1489_93403_x607519839}

[[成功创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_931728054}[接口]{style="font-family:宋体"}

[[Successfully deleted *Interface-name.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1130421517}

[[成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_2023039412}[接口]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ was deleted.]{lang="EN-US"}]{#struct_0_x1489_93403_x607585375}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1371719602}[接口被删除]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ was created.]{lang="EN-US"}]{#struct_0_x1489_93403_1455960561}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x341761044}[接口被创建]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ physically went up.]{lang="EN-US"}]{#struct_0_x1489_93403_2054850056}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x607650911}[接口物理状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name* trunked the ]{lang="EN-US"}]{#struct_0_x1489_93403_x188943964}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_35639470}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_1164473347}[接口]{style="font-family:宋体"}[trunk]{lang="EN-US"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name* did not trunk the VSAN..]{lang="EN-US"}]{#struct_0_x1489_93403_x607192159}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_1389496227}[接口去]{style="font-family:宋体"}[trunk]{lang="EN-US"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}

[[Received shutdown event of *Interface-name.*]{lang="EN-US"}]{#struct_0_x1489_93403_1069834278}

[[收到]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x800905931}[接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received undo-shutdown event of *Interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x607257695}

[[收到]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x929673591}[接口]{style="font-family:宋体"}[undo shutdown]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received phyIoCtl cmd *cmd* of *Interface-name*]{lang="EN-US"}]{#struct_0_x1489_93403_x1863557262}

[[收到以太网接口的物理控制命令]{style="font-family:宋体"}]{#struct_0_x1489_93403_x607323231}

[[Notified shutdown event of *Interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1801682050}

[[通知以太网接口]{style="font-family:宋体"}[shutdown]{lang="EN-US"}]{#struct_0_x1489_93403_x411485587}[事件]{style="font-family:宋体"}

[[Notified undo-shutdown event of *Interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_2021339254}

[[通知以太网接口]{style="font-family:宋体"}[undo shutdown]{lang="EN-US"}]{#struct_0_x1489_93403_x607388767}[事件]{style="font-family:宋体"}

[[Failed to deal with *Interface-name* event.]{lang="EN-US"}]{#struct_0_x1489_93403_1755420146}

[[处理]{style="font-family:宋体"}[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1467407224}[接口事件失败]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ physically went down.]{lang="EN-US"}]{#struct_0_x1489_93403_x606930015}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x167710267}[接口物理状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Notified driver to clear *Interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x403234459}

[[通报驱动在指定]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_x606995551}[内删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口信息]{style="font-family:宋体"}

[[Notified driver to set *Interface-name* in VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x619628344}

[[通报驱动在指定]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_919697338}[内设置]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口信息]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_958629641}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x73236878}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的超时定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the advertisement timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1892579551}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_958564105}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的非请求发现通告报文定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, became up.]{lang="EN-US"}]{#struct_0_x1489_93403_1272514927}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1125316914}[接口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内变为]{style="font-family:宋体"}[up]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, became attempt.]{lang="EN-US"}]{#struct_0_x1489_93403_958498569}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1124475552}[接口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内变为]{style="font-family:宋体"}[attempt]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, became down.]{lang="EN-US"}]{#struct_0_x1489_93403_1885596854}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_958433033}[接口在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内变为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* notified FCLINK VN *FCID* down.]{lang="EN-US"}]{#struct_0_x1489_93403_x290548327}

[[通知]{style="font-family:宋体"}[FCLINK VN down]{lang="EN-US"}]{#struct_0_x1489_93403_466256172}

[[VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to change VFC state into down.]{lang="EN-US"}]{#struct_0_x1489_93403_958891785}

[[通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_x259263434}[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[VFC]{lang="EN-US"}[状态]{style="font-family:宋体"}[down]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to change VFC state into up.]{lang="EN-US"}]{#struct_0_x1489_93403_1870566419}

[[通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_958826249}[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[VFC]{lang="EN-US"}[状态]{style="font-family:宋体"}[up]{lang="EN-US"}

[[interface *Interface-name,* notified FCLINK to change VFC state into down in all vsan.]{lang="EN-US"}]{#struct_0_x1489_93403_997305358}

[[通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_x1898723534}[在所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[VFC]{lang="EN-US"}[状态]{style="font-family:宋体"}[down]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name,* notified FCLINK to smooth VFC state.]{lang="EN-US"}]{#struct_0_x1489_93403_958760713}

[[通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_355791527}[平滑]{style="font-family:宋体"}[VFC]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[VLAN *vlan-id*, received VLAN destroying event.]{lang="EN-US"}]{#struct_0_x1489_93403_958695177}

[[收到删除指定]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_x55178494}[事件，]{style="font-family:宋体"}[vlan id]{lang="EN-US" style="text-transform:uppercase"}[为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示批量事件]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, received adding port to VLAN event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1436475325}

[[收到以太网接口加入指定]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_959153929}[事件，]{style="font-family:宋体"}[vlan id]{lang="EN-US" style="text-transform:uppercase"}[为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示批量事件]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, received deleting port from VLAN event.]{lang="EN-US"}]{#struct_0_x1489_93403_897735861}

[[收到以太网接口退出指定]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_273656344}[事件，]{style="font-family:宋体"}[vlan id]{lang="EN-US" style="text-transform:uppercase"}[为]{style="font-family:宋体"}[65535]{lang="EN-US"}[时表示批量事件]{style="font-family:宋体"}

[[Received Sync Bind message.]{lang="EN-US"}]{#struct_0_x1489_93403_959088393}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_x285337234}[模块的绑定信息]{style="font-family:宋体"}

[[Received Sync VSAN message.]{lang="EN-US"}]{#struct_0_x1489_93403_958629642}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_x73236881}[模块的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Received Sync Debug message.]{lang="EN-US"}]{#struct_0_x1489_93403_x1083275480}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_958564106}[模块的]{style="font-family:宋体"}[Debug]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Received Sync Mapping message.]{lang="EN-US"}]{#struct_0_x1489_93403_1272514924}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_958498570}[模块的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的映射信息]{style="font-family:宋体"}

[[Received Sync Restart message.]{lang="EN-US"}]{#struct_0_x1489_93403_1214176617}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_958433034}[模块的重启动信息]{style="font-family:宋体"}

[[Received Sync Batch Backup Finish message]{lang="EN-US"}]{#struct_0_x1489_93403_x290548320}

[[接收]{style="font-family:宋体"}[Sync]{lang="EN-US"}]{#struct_0_x1489_93403_466452780}[模块的批备完成信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-29 ]{lang="EN-US"}[debugging fcoe packet fcm]{lang="EN-US"}]{#struct_0_x1489_93403_958891786}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1115437357}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x259263431}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1870763027}

[*[Interface-name]{lang="EN-US"}*[ sent FCoE packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1170167485}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x778401624}[接口发送]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ received FCoE packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958826250}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x959009787}[接口接收]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Failed to send packet because *Interface-name* is not up.]{lang="EN-US"}]{#struct_0_x1489_93403_1866473946}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_307474709}[接口物理状态为非]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，发送]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[FCM Send: Successfully sent packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1194816424}

[[发送]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_958760714}[报文成功]{style="font-family:宋体"}

[[FCM Send: VFC interface is not bound with Ethernet interface, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_355791524}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_138794108}[接口没有绑定到以太网接口，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Send: The Ethernet interface is not in the corresponding VLAN, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1683024622}

[[以太网接口没有在相应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_958695178}[里，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Send: Failed to encapsulate the VFT extended header, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x55178507}

[[封装]{style="font-family:宋体"}[VFT]{lang="EN-US"}]{#struct_0_x1489_93403_x297358427}[扩展头失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Send: Failed to append memory for CRC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_959153930}

[[申请添加循环冗余校验码内存失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_x1440916290}[报文]{style="font-family:宋体"}

[[FCM Send: Failed to prepend memory for SOF, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1076750808}

[[预分报文帧头内存失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_x825674586}[报文]{style="font-family:宋体"}

[[FCM Send: MAC is invalid, and the packet was discarded.]{lang="EN-US"}]{#struct_0_x1489_93403_959088394}

[[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x285337233}[地址非法，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Send: Failed to prepend memory for Eth header, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1127832995}

[[预分以太网报文头内存失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_x1762520070}[报文]{style="font-family:宋体"}

[[FCM Send: Failed to send the packet to Eth link, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958629639}

[[发送报文到以太网链路失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_1883078266}[报文]{style="font-family:宋体"}

[[FCM Send: Ethernet failed to send the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1482435936}

[[以太网发送报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_958564103}

[[FCM Send: Failed to relay the packet from master board.]{lang="EN-US"}]{#struct_0_x1489_93403_1272514929}

[[从主板透传报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1125972274}

[[FCM Receive: Successfully received FCM packet.]{lang="EN-US"}]{#struct_0_x1489_93403_38863708}

[[成功收到]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_958498567}[报文]{style="font-family:宋体"}

[[FCM Receive: VFC interface is not found by Ethernet interface and source MAC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1124475538}

[[根据以太网接口和报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x890209596}[地址没有找到匹配的]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Receive: Remote MAC does not match source MAC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958433031}

[[对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x290548325}[地址与源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不匹配，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Receive: The packet has extension header, and was discarded.]{lang="EN-US"}]{#struct_0_x1489_93403_466125100}

[[存在扩展头，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_1699918757}[报文]{style="font-family:宋体"}

[[FCM Receive: CRC is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958891783}

[[循环冗余校验码非法，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_x259263436}[报文]{style="font-family:宋体"}

[[FCM Receive: Link failed to send the packet, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1870435347}

[[链路发送报文失败，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1489_93403_958826247}[报文]{style="font-family:宋体"}

[[FCM Receive: VFC state is not up, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_997305352}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1898723540}[接口状态为非]{style="font-family:宋体"}[up]{lang="EN-US"}[状态，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Receive: VLAN is not enabled with FCoE, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958760711}

[[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_355791529}[没有使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Receive: VSAN is not up, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_138794103}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_958695175}[没有]{style="font-family:宋体"}[up]{lang="EN-US"}[，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FCM Receive: Successfully relayed the packet to master board.]{lang="EN-US"}]{#struct_0_x1489_93403_x55178496}

[[成功透传报文到主板]{style="font-family:宋体"}]{#struct_0_x1489_93403_959153927}

[[FCM Receive: Failed to relay the packet to master board.]{lang="EN-US"}]{#struct_0_x1489_93403_897735867}

[[透传报文到主板失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_273656346}

[[FCM Send: Failed to relay the packet to slot *slot-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_959088391}

[[透传报文到接口板失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x285337236}

[[FCM Send: Successfully relayed the packet to slot *slot-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1128160675}

[[成功透传报文到接口板]{style="font-family:宋体"}]{#struct_0_x1489_93403_958629640}

[[Slot *slot-id* successfully received relay packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x73236879}

[[接口板成功收到透传报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_958564104}

[[Master board successfully received relay packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1272514926}

[[主板成功收到透传报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1125382450}

[ ]{lang="EN-US"}

[[表1-30 ]{lang="EN-US"}[debugging fcoe packet fip]{lang="EN-US"}]{#struct_0_x1489_93403_x1452022037}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1137453261}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_958498568}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1124475551}

[*[Interface-name]{lang="EN-US"}*[ sent FIP packet.]{lang="EN-US"}]{#struct_0_x1489_93403_319512913}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1000065380}[接口发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[Interface-name]{lang="EN-US"}*[ received FIP packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958433032}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x290548326}[接口接收]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[FIP Receive: Ethernet *Interface-name* is not bound with VFC interface, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_466321708}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_1152479055}[接口没有绑定以太网接口，丢弃]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958891784}

[[成功接收]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x259263433}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name* ,FIP Receive: Source MAC is not equal to bound MAC, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_1870631955}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1510227931}[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不等于绑定的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Destination MAC is not equal to local MAC, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_958826248}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_997305357}[报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不等于本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to get FIP frame, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1898723537}

[[获取]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x40074657}[帧失败，丢弃]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *Interface-name*, FIP Receive-The socket head is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958760712}

[[socket]{lang="EN-US"}]{#struct_0_x1489_93403_355791526}[头非法，丢弃]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC state is down, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_138794106}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_1683024616}[接口]{style="font-family:宋体"}[down]{lang="EN-US"}[，丢弃]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id* interface *Interface-name*, FIP Receive: The VLAN is not enabled with FCoE.]{lang="EN-US"}]{#struct_0_x1489_93403_958695176}

[[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x55178493}[未使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to get local MAC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1436475332}

[[获取本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1472224179}[地址失败，丢弃]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The version of FIP header is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_959153928}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_897735862}[报文头类型非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The length of description of FIP header is invalid ,and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_273656343}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_959088392}[报文头描述符的长度非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Protocol Code and FIP Subcode are invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x285337235}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1128226211}[报文协议号和子码非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name* FIP Receive: FIP FP bit is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958629637}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_1883078260}[报文]{style="font-family:宋体"}[FP]{lang="EN-US"}[位非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id,* interface *Interface-name*, FIP Receive: VFC mode does not match the FIP F bit, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1482042720}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1999987862}[模式不匹配]{style="font-family:宋体"}[FIP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[F]{lang="EN-US"}[位，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP S bit is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958564101}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_1272514931}[报文]{style="font-family:宋体"}[S]{lang="EN-US"}[位非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Description type is unknown, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1125447985}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958498565}[报文描述符类型未指明，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Description length is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1124475540}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1246636564}[报文描述符的长度非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The count of FIP Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_958433029}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_1665766819}[报文描述符的数量非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC in FIP MAC Description does not match Remote MAC, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_1470369547}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958891781}[报文]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符中的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不匹配对端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAX_FCOE_SIZE Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x259263438}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_1871352851}[报文]{style="font-family:宋体"}[MAX FCOE SIZE]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP solicited unicast discovery advertisement packet length is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_958826245}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_997305354}[单播请求通告报文长度不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC state is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_958760709}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1600523615}[接口状态不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP A bit is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_810586814}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958695173}[报文]{style="font-family:宋体"}[A]{lang="EN-US"}[位不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC in FIP MAC Description does not match ETH-Source MAC, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x55178498}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_959153925}[报文]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符中的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不匹配源端以太口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP NameID Description is invalid, and  discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_897735865}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_273656348}[报文]{style="font-family:宋体"}[NameID]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP Fabric Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_959088389}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_1670977892}[报文]{style="font-family:宋体"}[Fabric]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP FKA ADV Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1275430163}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958629638}[报文]{style="font-family:宋体"}[FKA ADV]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP VxPort Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_1883078265}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958564102}[报文]{style="font-family:宋体"}[VxPort]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC does not trunk VSAN.]{lang="EN-US"}]{#struct_0_x1489_93403_1272514928}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1126037810}[接口没有加入到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[中]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958498566}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1124475537}[报文发送成功]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, FIP Send: Ethernet link failed to send FIP packet.]{lang="EN-US"}]{#struct_0_x1489_93403_958433030}

[[链路发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x290548324}[报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: The VFC is invalid.]{lang="EN-US"}]{#struct_0_x1489_93403_958891782}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x259263435}[报文，]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口非法]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to encapsulate packet]{lang="EN-US"}]{#struct_0_x1489_93403_1870500883}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958826246}[报文，封装报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get interface mode]{lang="EN-US"}]{#struct_0_x1489_93403_997305351}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958760710}[报文，获取接口模式失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get Ethernet interface.]{lang="EN-US"}]{#struct_0_x1489_93403_355791528}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_958695174}[报文，获取以太网接口失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get VLAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x55178495}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_959153926}[报文，获取]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_897735868}

[[发送]{style="font-family:宋体"}[Clear]{lang="EN-US"}]{#struct_0_x1489_93403_273656353}[报文成功]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, FIP Send: Successfully sent unsolicited multicast advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_959088390}

[[发送组播非请求通告报文成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_x285337237}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414023354}

[[接收]{style="font-family:宋体"}[Clear]{lang="EN-US"}]{#struct_0_x1489_93403_385997214}[报文成功]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unsolicited multicast advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414088890}

[[接收组播非请求通告报文成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1810975233}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FLOGI request packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1414154426}

[[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1417867472}[请求报文的]{style="font-family:宋体"}[FP]{lang="EN-US"}[位非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC is not F Mode, and discarded the VLINK packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1414219962}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_1022951819}[接口不是]{style="font-family:宋体"}[F]{lang="EN-US"}[模式，丢弃虚链路报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761210}

[[成功收到]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x762016834}[保活报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: The ENode failed to login, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826746}

[[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x392499187}[没有]{style="font-family:宋体"}[LOGIN]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP SW_ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413892282}

[[成功发送]{style="font-family:宋体"}[ELP SW_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_1269935517}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, bound MAC is not equal to ENode MAC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957818}

[[绑定]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x2019594419}[与]{style="font-family:宋体"}[ENode MAC]{lang="EN-US"}[不同，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to get destination MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499066}

[[获取目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_781090823}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent solicited unicast discovery advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564602}

[[成功发送单播的请求发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1414023353}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received multicast solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1180086727}

[[接收组播的发现请求报文成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1414088889}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent multicast solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_111273532}

[[成功发送组播发现请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1414154425}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received solicited unicast discovery advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1821151999}

[[成功接收单播发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1414219961}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FC-MAP in FIP FC-MAP Description does not match local FC-MAP, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761209}

[[FCMAP]{lang="EN-US"}]{#struct_0_x1489_93403_1160363003}[描述符中的]{style="font-family:宋体"}[FCMAP]{lang="EN-US"}[值与本地]{style="font-family:宋体"}[FCMAP]{lang="EN-US"}[不一致，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826745}

[[成功发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1958583128}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent FLOGO request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413892281}

[[成功发送]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}]{#struct_0_x1489_93403_866650990}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI-request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957817}

[[发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499065}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_377806296}

[[发送]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564601}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of Instantiation packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_1201477415}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1414023356}[实例化报文的第一个描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received VLAN request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x776802200}

[[成功接收]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_x1414088892}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x648175819}

[[成功接收]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1414154428}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of VLAN request packet is not MAC Description, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1414219964}

[[vlan]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_216382765}[请求报文的第一个描述符不是]{style="font-family:
  宋体"}[MAC]{lang="EN-US"}[描述符，丢弃报文]{style="font-family:
  宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP FLOGI Description is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761212}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1924816248}[报文的]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent VLAN notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826748}

[[成功发送]{style="font-family:宋体"}[vlan]{lang="EN-US" style="text-transform:
  uppercase"}]{#struct_0_x1489_93403_x1413892284}[通告报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI LS_ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_463366463}

[[成功发送]{style="font-family:宋体"}[FLOGI LS_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957820}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send:  Successfully sent FLOGO LS_ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499068}

[[成功发送]{style="font-family:宋体"}[FLOGO LS_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x25478231}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC address in MAC Description of FLOGI  packet is not zero, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564604}

[[FIP FLOGI ]{lang="EN-US"}]{#struct_0_x1489_93403_1960992302}[报文]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不是全]{style="font-family:宋体"}[0]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGO packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1414023355}

[[FIP FLOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x1414088891}[报文]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x244891292}

[[成功接收]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x1414154427}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI LS_RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414219963}

[[成功发送]{style="font-family:宋体"}[FLOGI LS_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x543132122}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGO LS_RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761211}

[[成功发送]{style="font-family:宋体"}[FLOGO LS_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826747}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP SW_RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413892283}

[[成功发送]{style="font-family:宋体"}[ELP SW_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x296148424}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent ELP request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957819}

[[成功发送]{style="font-family:宋体"}[ELP ]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499067}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received ELP request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x784993118}

[[成功接收]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564603}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive-Successfully received ELP SW_ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414023358}

[[成功接收]{style="font-family:宋体"}[ELP SW_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1227140894}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received ELP SW_RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414088894}

[[成功接收]{style="font-family:宋体"}[ELP SW_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x1414154430}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of ELP packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_2070465234}

[[FIP ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1414219966}[报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Type of Vlink instantiation packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761214}

[[虚链路实例化报文类型非法，丢弃报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_1563581994}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Command Code of FIP packet is invalid, and discarded the packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826750}

[[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1413892286}[报文的]{style="font-family:宋体"}[Command Code]{lang="EN-US"}[字段非法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: VFC is down in VSAN, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x699432951}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957822}[在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内]{style="font-family:宋体"}[down]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent ELP request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499070}

[[成功发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x381643055}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent ELP SW_ACCpacket to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564606}

[[成功发送]{style="font-family:宋体"}[ELP SW_ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1414023357}[报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive:  Successfully sent ELP SW_RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414088893}

[[成功发送]{style="font-family:宋体"}[ELP SW_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_917908122}[报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP request packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1414154429}

[[发送]{style="font-family:宋体"}[ELP]{lang="EN-US"}]{#struct_0_x1489_93403_x1414219965}[请求报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP SW_ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1349701176}

[[发送]{style="font-family:宋体"}[ELP SW_ACC ]{lang="EN-US"}]{#struct_0_x1489_93403_x1413761213}[报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send ELP SW_RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1413826749}

[[发送]{style="font-family:宋体"}[ELP SW_RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x1413892285}[报文给]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[FIP Send: Successfully output packet of *Interface-name* in VSAN *vsan-id*,]{lang="EN-US"}]{#struct_0_x1489_93403_x1102717478}

[[成功在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1413957821}[内发出]{style="font-family:宋体"}[VFC]{lang="EN-US"}[口的报文]{style="font-family:宋体"}

[[FIP Send: Failed to output packet of *Interface-name* in VSAN *vsan-id*,]{lang="EN-US"}]{#struct_0_x1489_93403_x1413499069}

[[在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1413564605}[内发出]{style="font-family:宋体"}[VFC]{lang="EN-US"}[口的报文失败]{style="font-family:宋体"}

[[FIP Receive: Failed to input packet of *Interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x767891053}

[[输入]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_152060587}[内]{style="font-family:宋体"}[VFC]{lang="EN-US"}[的报文失败]{style="font-family:宋体"}

[[FIP Receive: Successfully input packet of *Interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_151995051}

[[成功输入]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_151929515}[内]{style="font-family:宋体"}[VFC]{lang="EN-US"}[的报文]{style="font-family:宋体"}

[[Failed to send packet because *Interface-name* state is not up in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x315858116}

[[VFC]{lang="EN-US"}]{#struct_0_x1489_93403_151863979}[在]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[内不是]{style="font-family:宋体"}[up]{lang="EN-US"}[，发送报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: First Description of Fip Keep Alive packet is not MAC Description, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152322731}

[[FIP]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_x1424965753}[保活]{style="font-family:宋体;text-transform:uppercase"}[报文的第一个描述符不是]{style="font-family:宋体"}[MAC]{lang="EN-US"}[描述符，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGI request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152257195}

[[成功发送]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_152191659}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152126123}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_x1712936773}[请求报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152584875}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152519339}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FLOGO request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152060588}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FLOGO]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1842730452}[请求报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent FDISC RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_151995052}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151929516}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGI ACC packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_151863980}

[[FLOGI ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152322732}[报文]{style="font-family:
  宋体;text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:
  uppercase"}[描述符不合法，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FDISC ACC packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1424965756}

[[FDISC ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152257196}[报文]{style="font-family:
  宋体;text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:
  uppercase"}[描述符不合法，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FLOGI ACC packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152191660}

[[FLOGI ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152126124}[报文]{style="font-family:
  宋体;text-transform:uppercase"}[FP]{lang="EN-US" style="text-transform:
  uppercase"}[位不合法，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FDISC request packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1712936768}

[[FDISC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152584876}[请求报文]{style="font-family:
  宋体;text-transform:uppercase"}[FP]{lang="EN-US" style="text-transform:
  uppercase"}[位不合法，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FP bit of FDISC ACC packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152519340}

[[FDISC ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152060585}[报文]{style="font-family:
  宋体;text-transform:uppercase"}[FP]{lang="EN-US" style="text-transform:
  uppercase"}[位不合法，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_151995049}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FLOGI ACC ]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1687356420}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGI RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_151929513}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FLOGI RJT ]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151863977}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152322729}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152257193}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1804359720}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FDISC ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152191657}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FDISC RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152126121}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FDISC RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152584873}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152519337}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FLOGO ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1909297558}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received FLOGO RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152060586}

[[成功接收]{style="font-family:宋体;text-transform:uppercase"}[FLOGO RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151995050}[报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VN does not exist, discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_151929514}

[[VN]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151863978}[不存在，丢弃报文]{style="font-family:宋体;
  text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152322730}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FLOGI ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_x1424965754}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGI RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152257194}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FLOGI RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152191658}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152126122}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152584874}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152519338}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1909297545}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FDISC RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152060583}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FDISC RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151995047}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGO ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_151929511}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FLOGO ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151863975}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully sent FLOGO RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152322727}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[FLOGO RJT]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152257191}[报文给]{style="font-family:
  宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:
  uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x1804359722}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152191655}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FLOGI ACC]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGI RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152126119}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152584871}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FLOGI RJT]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152519335}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152060584}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_151995048}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_151929512}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FDISC ACC]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FDISC RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_151863976}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152322728}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FDISC RJT]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO ACC packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152257192}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_x1804359719}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FLOGO ACC]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Failed to send FLOGO RJT packet to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_152191656}

[[向]{style="font-family:宋体;text-transform:uppercase"}[FCLINK]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152126120}[发送]{style="font-family:
  宋体;text-transform:uppercase"}[FLOGO RJT]{lang="EN-US" style="text-transform:
  uppercase"}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, NPV received the empty clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_152584872}

[[NPV]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_152519336}[接收空的]{style="font-family:宋体;
  text-transform:uppercase"}[clear]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, NPV received the clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718144528}

[[NPV]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718078992}[接收]{style="font-family:宋体;text-transform:uppercase"}[clear]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to send clear packet because the mode is incorrect.]{lang="EN-US"}]{#struct_0_x1489_93403_1718013456}

[[由于模式不正确，发送]{style="font-family:宋体;text-transform:uppercase"}[clear]{lang="EN-US"}]{#struct_0_x1489_93403_1717947920}[报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Failed to Send FKA packet because the mode is incorrect.]{lang="EN-US"}]{#struct_0_x1489_93403_1718406672}

[[由于模式不正确，发送]{style="font-family:宋体;text-transform:uppercase"}[FKA]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718341136}[报文失败]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: MAC address in MAC Description of FDISC packet is not zero, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718275600}

[[FDISC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718210064}[报文]{style="font-family:宋体;text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:uppercase"}[描述符中的]{style="font-family:宋体;
  text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:
  uppercase"}[地址不为零，丢弃报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is NP, and discarded the solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718668816}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718603280}[不是]{style="font-family:宋体;text-transform:uppercase"}[NP]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃发现请求报文]{style="font-family:宋体;
  text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is F, and discarded the clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718144529}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718078993}[不是]{style="font-family:宋体;text-transform:uppercase"}[F]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[clear]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FLOGI request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718013457}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1717947921}[不是]{style="font-family:宋体;text-transform:uppercase"}[F]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FLOGI]{lang="EN-US" style="text-transform:
  uppercase"}[请求报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not NP, and discarded the FLOGI notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718406673}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718341137}[不是]{style="font-family:宋体;text-transform:uppercase"}[NP]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FLOGI]{lang="EN-US" style="text-transform:
  uppercase"}[通告报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FDISC request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718275601}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718210065}[不是]{style="font-family:宋体;text-transform:uppercase"}[F]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:
  uppercase"}[请求报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not NP, and discarded the FDISC notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718668817}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718603281}[不是]{style="font-family:宋体;text-transform:uppercase"}[NP]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FDISC]{lang="EN-US" style="text-transform:
  uppercase"}[通告报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not F, and discarded the FLOGO request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718144526}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718078990}[不是]{style="font-family:宋体;text-transform:uppercase"}[F]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FLOGO]{lang="EN-US" style="text-transform:
  uppercase"}[请求报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*,  FIP Receive: VFC mode is not NP, and discarded the FLOGO notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1717947918}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718406670}[不是]{style="font-family:宋体;text-transform:uppercase"}[NP]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FLOGO]{lang="EN-US" style="text-transform:
  uppercase"}[通告报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the ELP packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718341134}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718275598}[不是]{style="font-family:宋体;text-transform:uppercase"}[E]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[ELP]{lang="EN-US" style="text-transform:
  uppercase"}[报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: FIP MAC Description of FLOGO ACC packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718210062}

[[FLOGO ACC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718668814}[报文中]{style="font-family:宋体;text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:uppercase"}[描述符不合法，丢弃报文]{style="font-family:宋体;
  text-transform:uppercase"}

[[FIP Receive-Ethernet *Interface-nam*e, FPMA MAC does not match VFC interface, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718603278}

[[FPMA MAC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718144527}[不匹配]{style="font-family:宋体;text-transform:uppercase"}[VFC]{lang="EN-US" style="text-transform:uppercase"}[接口，丢弃报文]{style="font-family:宋体;
  text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unsolicited multicast  advertisement packet, and VFC state is attempt.]{lang="EN-US"}]{#struct_0_x1489_93403_1718078991}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718013455}[是]{style="font-family:宋体;text-transform:uppercase"}[attempt]{lang="EN-US"}[状态，成功接收组播非请求通告报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode does not match the multicast destination MAC, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718406671}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718341135}[模式不匹配组播目的]{style="font-family:宋体;text-transform:uppercase"}[MAC]{lang="EN-US" style="text-transform:uppercase"}[，丢弃报文]{style="font-family:
  宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the received VLAN request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718275599}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718210063}[不是]{style="font-family:宋体;text-transform:uppercase"}[E]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[VLAN]{lang="EN-US" style="text-transform:
  uppercase"}[请求报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: VFC mode is not E, and discarded the received Fip Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718668815}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718603279}[不是]{style="font-family:宋体;text-transform:uppercase"}[E]{lang="EN-US" style="text-transform:uppercase"}[模式，丢弃]{style="font-family:宋体;
  text-transform:uppercase"}[FIP]{lang="EN-US" style="text-transform:
  uppercase"}[保活报文]{style="font-family:宋体;text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Send: Successfully sent unicast solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718144524}

[[成功发送]{style="font-family:宋体;text-transform:uppercase"}[ ]{style="text-transform:uppercase"}]{#struct_0_x1489_93403_1718078988}[单播请求报文]{style="font-family:宋体;
  text-transform:uppercase"}

[[VSAN *vsan-id*, interface *Interface-name*, FIP Receive: Successfully received unicast solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1718013452}

[[成功接收单播请求报文]{style="font-family:宋体;text-transform:uppercase"}]{#struct_0_x1489_93403_1718406668}

[[Discarded a packet, because the port mode of VFC interface *Interface-name* in VSAN *vsan-id* is incorrect.]{lang="EN-US"}]{#struct_0_x1489_93403_1900329804}

[[VFC]{lang="EN-US" style="text-transform:uppercase"}]{#struct_0_x1489_93403_1517992775}[模式与当前]{style="font-family:宋体;text-transform:uppercase"}[VSAN]{lang="EN-US" style="text-transform:uppercase"}[模式不匹配，丢弃报文]{style="font-family:宋体;
  text-transform:uppercase"}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](FC和FCoE%20Debug.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1489_93403_1538256340}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[如果]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1489_93403_x2116801494}[FIP]{lang="EN-US"}[报文收发打印信息中的]{style="font-family:KaiTi_GB2312"}*[vsan-id]{lang="EN-US"}*[为]{style="font-family:KaiTi_GB2312"}[65535]{lang="EN-US"}[，则表示该]{style="font-family:KaiTi_GB2312"}[VSAN]{lang="EN-US"}[信息无效。例如：设备在某]{style="font-family:KaiTi_GB2312"}[VLAN]{lang="EN-US"}[中收到]{style="font-family:KaiTi_GB2312"}[vlan]{lang="EN-US" style="text-transform:uppercase"}[请求报文时，如果该]{style="font-family:
KaiTi_GB2312"}[VLAN]{lang="EN-US"}[没有对应的映射]{style="font-family:KaiTi_GB2312"}[VSAN]{lang="EN-US"}[，此时，]{style="font-family:KaiTi_GB2312"}[debug]{lang="EN-US"}[信息中的]{style="font-family:KaiTi_GB2312"}*[vsan-id]{lang="EN-US"}*[会打印为]{style="font-family:KaiTi_GB2312"}[65535]{lang="EN-US"}[，此情况属于正常。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[表1-31 ]{lang="EN-US"}[debugging fcoe timer]{lang="EN-US"}]{#struct_0_x1489_93403_1955976456}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1166261773}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x925210547}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1718341132}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the advertisement timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1123193001}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x412773998}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[非请求发现通告定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1955165432}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1718275596}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的超时定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the advertisement timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1619696848}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1999003357}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[非请求发现通告定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x63964449}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1718210060}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的超时定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1515586920}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1145967175}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口超时定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the advertisement timer.]{lang="EN-US"}]{#struct_0_x1489_93403_245890573}

[[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1718668812}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[通告定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the solicitation timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x906843717}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1293450570}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的发现请求定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the solicitation timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1718603276}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1542760204}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的发现请求定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the solicitation timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x942521484}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1411614162}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[发现请求定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the dispersion timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1718144525}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1118230387}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的离散定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the dispersion timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x390462113}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1718078989}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的离散定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the dispersion timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1433381364}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_63742113}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[离散定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the ENode dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x738676792}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1718013453}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[超时定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the ENode dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1154000728}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1054857965}[内创建]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[超时定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the ENode dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1717947917}

[[在指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x675710825}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[超时]{style="font-family:宋体"}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created VN FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x728694113}

[[成功创建]{style="font-family:宋体"}[VN FKA]{lang="EN-US"}]{#struct_0_x1489_93403_1718406669}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create VN FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1538321876}

[[创建]{style="font-family:宋体"}[VN FKA]{lang="EN-US"}]{#struct_0_x1489_93403_187539619}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted VN FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1396051771}

[[成功删除]{style="font-family:宋体"}[VN FKA]{lang="EN-US"}]{#struct_0_x1489_93403_1718341133}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created VN dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1123258537}

[[成功创建]{style="font-family:宋体"}[VN dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1218717449}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create VN dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1718275597}

[[创建]{style="font-family:宋体"}[VN dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1619762384}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, ENode FKA timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1278441593}

[[ENode FKA]{lang="EN-US"}]{#struct_0_x1489_93403_1718210061}[定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, dispersion timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1515521384}

[[离散定时器超时]{style="font-family:宋体"}]{#struct_0_x1489_93403_1718668813}

[[VSAN *vsan-id*, interface *Interface-name*, dead timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x906778181}

[[dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1056795035}[定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, VN *FCID* FKA timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1718603277}

[[VN FKA]{lang="EN-US"}]{#struct_0_x1489_93403_1542825740}[定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, VN *FCID* dead timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1026352384}

[[VN dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1010738827}[定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the NP FCF dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1043875793}

[[成功启动]{style="font-family:宋体"}[NP FCF dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1626413820}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully started the NP ENode FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804363}

[[成功启动]{style="font-family:宋体"}[NP ENode FKA]{lang="EN-US"}]{#struct_0_x1489_93403_x1326247349}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the NP FCF dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010869899}

[[创建]{style="font-family:宋体"}[NP FCF dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1745232422}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the NP ENode FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137920730}

[[创建]{style="font-family:宋体"}[NP ENode FKA]{lang="EN-US"}]{#struct_0_x1489_93403_x1010935435}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the NP FCF dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x533373281}

[[成功删除]{style="font-family:宋体"}[NP FCF dead]{lang="EN-US"}]{#struct_0_x1489_93403_x1010476683}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the NP ENode FKA timer.]{lang="EN-US"}]{#struct_0_x1489_93403_2004171311}

[[成功删除]{style="font-family:宋体"}[NP ENode FKA]{lang="EN-US"}]{#struct_0_x1489_93403_365398946}[定时器]{style="font-family:宋体"}

[[The FKA timer in VLAN *vlan-id* will time out in *timeout* seconds.]{lang="EN-US"}]{#struct_0_x1489_93403_x436159677}

[[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x436159671}[下的]{style="font-family:宋体"}[FKA]{lang="EN-US"}[定时器将在]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[秒后超时]{style="font-family:宋体"}

[[The FKA timer in VLAN *vlan-id* timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1520155463}

[[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1520155468}[下的]{style="font-family:宋体"}[FKA]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1010542219}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_83797034}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[的错误调试信息开关。当接收错误的接口控制字时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoe error]{lang="EN-US"}]{#struct_0_x1489_93403_x646931797}

[\*May 11 16:17:17:188 2011 Sysname FCOEK/7/ERROR: -MDC=1; PhyIoCtl cmd 17301526 is unknown]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1187350100}*[物理控制命令不存在]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1032681365}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[的事件调试信息开关。当关闭]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[10]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoe event]{lang="EN-US"}]{#struct_0_x1489_93403_718970936}

[\*May 11 16:17:23:616 2011 Sysname FCOE/7/EVENT: -MDC=1; Vfc10 physically went down.]{lang="EN-US"}

[*[// VFC]{lang="EN-US"}*]{#struct_0_x1489_93403_102640868}*[接口物理状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}*

[[\*May 11 16:17:18:192 2011 Sysname FCOEK/7/EVENT: -MDC=1; Successfully deleted Vfc100.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607755}

[\*May 11 16:17:18:192 2011 Sysname FCOE/7/EVENT: -MDC=1; Vfc100 was deleted.]{lang="EN-US"}

[*[// VFC]{lang="EN-US"}*]{#struct_0_x1489_93403_x640395611}*[接口被删除]{style="font-family:宋体"}*

[[\*May 11 16:17:29:616 2011 Sysname FCOEK/7/EVENT: -MDC=1; Notified driver to clear Vfc10 in VLAN 2.]{lang="EN-US"}]{#struct_0_x1489_93403_1995748154}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x2078690439}*[通知驱动删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1747544270}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[的经过封装的]{style="font-family:宋体"}[FC]{lang="EN-US"}[报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。当以太网接口没有]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[相应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[时，发送报文会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoe packet fcm]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673291}

[\*May 11 16:14:10:288 2011 Sysname FCOEK/7/PACKET: -MDC=1; FCM Send]{lang="EN-US"}[：]{style="font-family:宋体"} [The Ethernet interface is not in the corresponding VLAN, and discarded the packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_443044093}*[以太网接口没有在相应的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[里，丢弃]{style="font-family:宋体"}[FCM]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1005519003}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP]{lang="EN-US"}[协议报文调试信息开关。当]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[配置完成后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoe packet fip]{lang="EN-US"}]{#struct_0_x1489_93403_x437568326}

[\*Oct 20 14:57:45:386 2011 Sysname FCOE/7/PACKET: -MDC=1; VSAN 10, interface Vfc2, FIP Receive]{lang="EN-US"}[：]{style="font-family:宋体"}[Successfully received multicast solicitation packet.]{lang="EN-US"}

[*[// [vfc]{style="text-transform:uppercase"}]{lang="EN-US"}*]{#struct_0_x1489_93403_x581990582}*[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[下成功接收组播的发现请求报文]{style="font-family:宋体"}*

[[\*Oct 20 14:57:45:386 2011 Sysname FCOE/7/PACKET: -MDC=1; VSAN 10, interface Vfc2, FIP Send]{lang="EN-US"}]{#struct_0_x1489_93403_x827243178}[：]{style="font-family:宋体"}[Successfully sent solicited unicast discovery advertise packet.]{lang="EN-US"}

[*[// [vfc]{style="text-transform:uppercase"}]{lang="EN-US"}*]{#struct_0_x1489_93403_x1494000000}*[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[下成功发送单播的请求发现通告报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214539}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[的定时器调试信息开关。当]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口物理层]{style="font-family:宋体"}[up]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoe timer]{lang="EN-US"}]{#struct_0_x1489_93403_1760355800}

[\*Oct 20 14:57:49:849 2011 Sysname FCOE/7/TIMER: -MDC=1; VSAN 10, interface Vfc2, successfully deleted the send-solicitation timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1481808629}*[在]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[内成功删除]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[发现请求定时器]{style="font-family:宋体"}*

[[\*Oct 20 14:57:49:849 2011 Sysname FCOE/7/TIMER: -MDC=1; VSAN 10, interface Vfc2, successfully started the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1769197972}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1278837742}*[在]{style="font-family:宋体"}[VSAN 10]{lang="EN-US"}[内成功启动]{style="font-family:宋体"}[VFC]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[的超时定时器]{style="font-family:宋体"}*

::: {#935039335 .myid}
[]{#_Toc334859960}[]{#_Toc404797590}[]{#struct_0_x1489_93403_x1171162358}[]{#_Hlt12351224}[]{#_Hlt8879577}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcoemgr**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1400076701}

[**[debugging fcoemgr]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_x1489_93403_x1010280075}

[**[undo debugging fcoemgr]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_x1489_93403_2131859072}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1337116714}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x286260641}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x482982844}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x724935659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x154819610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1010738826}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x1685007562}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_242671973}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_1964916916}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_x566030776}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1896079266}

[**[debugging fcoemgr]{lang="EN-US"}**]{#struct_0_x1489_93403_x758499602}[命令用来打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[管理模块调试信息开关。]{style="font-family:宋体"}**[undo debugging fcoemgr]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[管理模块调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804362}[管理模块调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-32 ]{lang="EN-US"}[debugging fcoemgr error]{lang="EN-US"}]{#struct_0_x1489_93403_1402636006}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1159225965}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_592907486}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_843731054}

[[Failed to start the process of *process-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1326239991}

[[启动进程失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1010869898}

[[Failed to reply to synchronous message.]{lang="EN-US"}]{#struct_0_x1489_93403_983650933}

[[回复同步消息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_2126471900}

[ ]{lang="EN-US"}

[[表1-33 ]{lang="EN-US"}[debugging fcoemgr event]{lang="EN-US"}]{#struct_0_x1489_93403_x1001677698}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1158370669}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1941162013}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1010935434}

[[Received a notification about disable fcoe-mode from Master.]{lang="EN-US"}]{#struct_0_x1489_93403_1032710660}

[[收到主板去使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_359601344}[模式的通知]{style="font-family:宋体"}

[[Received a notification about the fcoe-mode enabled from Master.]{lang="EN-US"}]{#struct_0_x1489_93403_488501845}

[[收到主板使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x1010476682}[模式的通知]{style="font-family:宋体"}

[[Received a notification about start-service from Master.]{lang="EN-US"}]{#struct_0_x1489_93403_x724712044}

[[收到主板开启服务的通知]{style="font-family:宋体"}]{#struct_0_x1489_93403_226486964}

[[Received insertion slot *slot-id* event.]{lang="EN-US"}]{#struct_0_x1489_93403_1747916298}

[[收到接口板插入的事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1010542218}

[[Start to enable the processes concerning the current fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1482286907}

[[开启与当前]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_1880357971}[模式关联的进程]{style="font-family:宋体"}

[[Notify all the boards to start the services concerning fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1386949275}

[[通知所有板开启与当前]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607754}[模式关联的进程]{style="font-family:宋体"}

[[Notify all the boards to enable fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_2088487744}

[[通知所有板使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x113456830}[模式]{style="font-family:宋体"}

[[Start to enable fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673290}

[[使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_2009128034}[模式]{style="font-family:宋体"}

[[Start to disable current fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_1992145885}

[[去使能当前]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_1926805079}[模式]{style="font-family:宋体"}

[[Notify all the processes to disable fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214538}

[[通知所有进程]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_x968527555}[模式去使能]{style="font-family:宋体"}

[[Received all the replys about disable fcoe-mode from the boards notified.]{lang="EN-US"}]{#struct_0_x1489_93403_x499887769}

[[收到所有板]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_901421890}[模式去使能的通知]{style="font-family:宋体"}

[[Received all the replys to enabling fcoe-mode from boards notified.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010280074}

[[收到所有板]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_565775131}[模式使能的通知]{style="font-family:宋体"}

[[Received all the replys to starting service from boards notified.]{lang="EN-US"}]{#struct_0_x1489_93403_205758487}

[[收到所有板开启服务的通知]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1010738829}

[[Notify all the boards to disable fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1732061729}

[[通知所有板]{style="font-family:宋体"}[FCoE]{lang="EN-US"}]{#struct_0_x1489_93403_220648988}[模式去使能]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1650471256}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804365}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[管理模块的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcoemgr error]{lang="EN-US"}]{#struct_0_x1489_93403_x519678295}

[\*Nov 9 06:16:10:111 2012 Sysname FCOEMGR/7/ERROR: -MDC=1; Failed to reply to synchronous message.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1100908609}*[回复同步消息失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x462307397}[打开]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[管理模块的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping event]{lang="EN-US"}]{#struct_0_x1489_93403_x1062252247}

[\*Nov 9 06:16:12:647 2012 Sysname FCOEMGR/7/EVENT: -MDC=1; Received insertion slot 3 event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x892414516}*[收到接口板]{style="font-family:宋体"}[3]{lang="EN-US"}[插入的事件]{style="font-family:宋体"}*

[[\*Nov 9 06:16:14:861 2012 Sysname FCOEMGR/7/EVENT: -MDC=1-Slot=3; Start to enable fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010869901}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x2102052607}*[使能]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式]{style="font-family:宋体"}*

[[\*Nov 9 06:16:14:862 2012 Sysname FCOEMGR/7/EVENT: -MDC=1-Slot=3; Start to enable the processes concerning the current fcoe-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1074189250}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1118065416}*[开启与当前]{style="font-family:宋体"}[FCoE]{lang="EN-US"}[模式关联的进程]{style="font-family:宋体"}*

::: {#-1159485342 .myid}
[]{#_Toc211338642}[]{#_Toc204610073}[]{#_Toc29974884}[]{#_Toc25576880}[]{#_Toc15724192}[]{#_Toc240800233}[]{#_Toc316646603}[]{#_Toc404797591}[]{#struct_0_x1489_93403_x558288585}[]{#_Toc383781786}[]{#_Toc379646548}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fc-port-security**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1288530250}

[**[debugging fc-port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **notify** }]{lang="EN-US"}]{#struct_0_x1489_93403_305523840}

[**[undo debugging fc-port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **notify** }]{lang="EN-US"}]{#struct_0_x1489_93403_x558288584}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1288595786}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_1924547743}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x21053794}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x558288587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x1288661322}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x798456050}

[**[all]{lang="FR"}**]{#struct_0_x1489_93403_x558288586}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="FR"}**]{#struct_0_x1489_93403_x1288726858}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="FR"}**]{#struct_0_x1489_93403_x1951721229}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[notify]{lang="EN-US"}**]{#struct_0_x1489_93403_x1284935549}[：]{style="font-family:宋体"}[表示通知调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x558288589}

[**[debugging fc-port-security]{lang="EN-US"}**]{#struct_0_x1489_93403_x1288792394}[命令用来打开]{style="font-family:
宋体"}[FC]{lang="EN-US"}[端口安全]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging fc-port-security]{lang="EN-US"}**[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全]{style="font-family:宋体"}[调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_632118125}[端口安全]{style="font-family:宋体"}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-34 ]{lang="EN-US"}[debugging fc-port-security error]{lang="EN-US"}]{#struct_0_x1489_93403_x558288588}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1128096818}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x558288590}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1780363578}

[[Failed to back up data in batch.]{lang="EN-US"}]{#struct_0_x1489_93403_1780363576}

[[批备数据失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1780363574}

[[Failed to change the standby MPU to the active state.]{lang="EN-US"}]{#struct_0_x1489_93403_1780363569}

[[备用主控板倒换为主用主控板失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x175951559}

[[Failed to send a message for clearing violation entries.]{lang="EN-US"}]{#struct_0_x1489_93403_x175951561}

[[发送清除非法登录的信息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x175951563}

[[Failed to back up violation entries in batch in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x175951565}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x175951567}[内批备非法登录信息失败]{style="font-family:宋体"}

[[Failed to back up statistics in batch in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2132266695}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2132266696}[内批备统计信息失败]{style="font-family:宋体"}

[[Failed to send a check reply message.]{lang="EN-US"}]{#struct_0_x1489_93403_x2132266698}

[[发送登录权限检查回应信息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2132266700}

[[Failed to send a notification message to FCLINK.]{lang="EN-US"}]{#struct_0_x1489_93403_x2132266702}

[[向]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_206385466}[发送通知消息失败]{style="font-family:宋体"}

[[Failed to create an event re-initialization timer.]{lang="EN-US"}]{#struct_0_x1489_93403_206385461}

[[创建重新初始化事件定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_206385459}

[[Failed to create a smooth aging timer.]{lang="EN-US"}]{#struct_0_x1489_93403_206385457}

[[创建平滑老化定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1395863865}

[[Failed to create a login database in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1395863863}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1395863861}[内创建登录数据库失败]{style="font-family:宋体"}

[[Failed to add a node to the login database in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1395863859}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1395863858}[内将节点加入登录数据库失败]{style="font-family:宋体"}

[[Failed to add a switch to the login database in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x560451270}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x560451272}[内将交换机加入登录数据库失败]{style="font-family:宋体"}

[[Failed to add a policy in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x560451274}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x560451279}[内添加策略失败]{style="font-family:宋体"}

[[Failed to allocate an index for a new policy in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1778200889}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1778200887}[内为新的策略申请索引失败]{style="font-family:宋体"}

[[Failed to create a policy database in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1778200885}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1778200884}[内创建策略数据库失败]{style="font-family:宋体"}

[[Failed to find a matched violation entry and to add a new violation entry in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1778200882}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x178114246}[内没有找到非法登录表项且添加表项失败]{style="font-family:宋体"}

[[Failed to get violation info by index (index = *index*-*id*) in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x178114251}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x178114253}[内通过索引获取非法登录信息失败]{style="font-family:宋体"}

[[Failed to find a matched violation entry and to add a new violation entry on the standby MPU in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x178114255}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2134429383}[内备板上没有找到非法登录表项且添加表项失败]{style="font-family:宋体"}

[[Failed to add check result *result-id* to the queue in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2134429384}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2134429386}[内将权限检查的结果加入到队列失败]{style="font-family:宋体"}

[[Failed to add a switch violation entry (*interface-name,* sWWN *swwn*) to the queue in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2134429388}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2134429390}[内将交换机的非法登录信息]{style="font-family:宋体"}[(]{lang="EN-US"}[接口，]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[)]{lang="EN-US"}[加入到队列失败]{style="font-family:宋体"}

[[Failed to add a node violation entry (*interface-name,* pWWN *pwwn*, nWWN nwwn) to the queue in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_204222775}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_204222773}[内将节点的非法登录信息]{style="font-family:宋体"}[(]{lang="EN-US"}[接口，]{style="font-family:宋体"}*[pwwn nwwn]{lang="EN-US"}*[)]{lang="EN-US"}[加入到队列失败]{style="font-family:宋体"}

[[Failed to create a statistics and violation database in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_204222771}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_204222770}[内创建统计和非法登录数据库失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-35 ]{lang="EN-US"}[debugging fc-port-security event]{lang="EN-US"}]{#struct_0_x1489_93403_347009036}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1079950780}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1393701178}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1393701176}

[[Received an event for creating VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1393701174}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1393701169}[创建事件]{style="font-family:宋体"}

[[Received an event for deleting VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x562613959}

[[接收]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x562613961}[删除事件]{style="font-family:宋体"}

[[Received a port activation event.]{lang="EN-US"}]{#struct_0_x1489_93403_x562613963}

[[收到端口激活事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x562613965}

[[Received a port deactivation event.]{lang="EN-US"}]{#struct_0_x1489_93403_x562613967}

[[收到端口去激活事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_1776038202}

[[Received an event for a port joining an aggregate interface.]{lang="EN-US"}]{#struct_0_x1489_93403_1776038200}

[[收到端口加入聚合口事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_1776038198}

[[Received a smooth start message.]{lang="EN-US"}]{#struct_0_x1489_93403_1776038196}

[[收到平滑开始消息]{style="font-family:宋体"}]{#struct_0_x1489_93403_x180276935}

[[Received a smooth end message.]{lang="EN-US"}]{#struct_0_x1489_93403_x180276937}

[[收到平滑结束消息]{style="font-family:宋体"}]{#struct_0_x1489_93403_x180276939}

[[Finished policy aging.]{lang="EN-US"}]{#struct_0_x1489_93403_x180276941}

[[策略老化结束]{style="font-family:宋体"}]{#struct_0_x1489_93403_x180276943}

[[The node with pWWN *pwwn* (nWWN *nwwn*) is logging in through *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136592070}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2136592072}[内节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[正在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The node with pWWN *pwwn* (nWWN *nwwn*) has logged out from *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136592074}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2136592076}[内节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上下线]{style="font-family:宋体"}

[[Link is up because the switch with sWWN *swwn* is logging in through *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136592078}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_202060090}[内由于交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[正在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录，链路状态]{style="font-family:宋体"}[up]{lang="EN-US"}

[[Link is down because the switch with sWWN *swwn* has logged out from *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_202060085}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_202060083}[内由于交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上下线，链路状态]{style="font-family:宋体"}[down]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-36 ]{lang="EN-US"}[debugging fc-port-security notify]{lang="EN-US"}]{#struct_0_x1489_93403_1934698400}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1312956576}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_202060081}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1413165338}

[[The node with pWWN *pwwn* (nWWN *nwwn*) was allowed to log in through *interface-name* in VSAN *vsan-id* when a FLOGI event was received.]{lang="EN-US"}]{#struct_0_x1489_93403_1413165336}

[[当收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_1413165334}[事件时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内允许节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The node with pWWN *pwwn* (nWWN *nwwn*) was refused to log in through *interface-name* in VSAN *vsan-id* when a FLOGI event was received.]{lang="EN-US"}]{#struct_0_x1489_93403_1413165332}

[[当收到]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_1413165330}[事件时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内拒绝节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The switch with sWWN *swwn* was allowed to log in through *interface-name* in VSAN *vsan-id* when a link up event was received.]{lang="EN-US"}]{#struct_0_x1489_93403_x543149799}

[[当收到链路]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1489_93403_x543149801}[事件时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内允许交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The switch with sWWN *swwn* was refused to log in through *interface-name* in VSAN *vsan-id* when a link up event was received.]{lang="EN-US"}]{#struct_0_x1489_93403_x543149803}

[[当收到链路]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1489_93403_x543149805}[事件时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内拒绝交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The node with pWWN *pwwn* (nWWN *nwwn*) was allowed to log in through *interface-name* in VSAN *vsan-id* when a check request was received.]{lang="EN-US"}]{#struct_0_x1489_93403_x543149807}

[[当收到权限检查请求时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1795502361}[内允许节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The node with pWWN *pwwn* (nWWN *nwwn*) was refused to log in through *interface-name* in VSAN *vsan-id* when a check request was received.]{lang="EN-US"}]{#struct_0_x1489_93403_1795502358}

[[当收到权限检查请求时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1795502356}[内拒绝节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The switch with sWWN *swwn* was allowed to log in through *interface-name* in VSAN *vsan-id* when a check request was received.]{lang="EN-US"}]{#struct_0_x1489_93403_1795502354}

[[当收到权限检查请求时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x160812774}[内允许交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[The switch with sWWN *swwn* was refused to log in through *interface-name* in VSAN *vsan-id* when a check request was received.]{lang="EN-US"}]{#struct_0_x1489_93403_x160812776}

[[当收到权限检查请求时，在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x160812778}[内拒绝交换机]{style="font-family:宋体"}*[swwn]{lang="EN-US"}*[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[上登录]{style="font-family:宋体"}

[[Notify FCLINK to force the node with pWWN *pwwn* (nWWN *nwwn*) to log out from *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x160812781}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x160812783}[内通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[将]{style="font-family:宋体;color:black"}[节点]{style="font-family:宋体"}*[pwwn]{lang="EN-US"}*[(*nwwn*)]{lang="EN-US"}[从接口]{style="font-family:宋体;color:black"}*[interface-name]{lang="EN-US"}*[下线]{style="font-family:宋体;color:black"}

[[Notify FCLINK to isolate *interface-name* in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2117127911}

[[通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}]{#struct_0_x1489_93403_x2117127913}[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内将接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[隔离]{style="font-family:宋体"}

[[Notify FCLINK to force all logged-in devices to log out in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2117127915}

[[在]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2117127917}[内通知]{style="font-family:宋体"}[FCLINK]{lang="EN-US"}[将所有已登录的设备下线]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2117127918}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_907820092}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc-port-security error]{lang="EN-US"}]{#struct_0_x1489_93403_882856655}

[\*Dec 25 09:21:56:925 2013 Sysname FCPS/7/ERROR: -MDC=1; Failed to back up violation entries in batch in VSAN 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1470456809}*[批备非法登录信息失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x2117127919}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[端口安全的事件调试信息开关和通知调试信息开关，当交换机登录时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fc-port-security event]{lang="EN-US"}]{#struct_0_x1489_93403_x658263849}

[\<Sysname\> debugging fc-port-security notify]{lang="EN-US"}

[[\*Mar 28 03:09:55:468 2014 Sysname]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1489_93403_x1182886895}[FCPS/7/NOTIFY: -MDC=1; The switch with sWWN 10:00:00:e0:02:00:00:00 was allowed to log in through Fc1/0/5 in VSAN 2]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\""}[ ]{lang="EN-US"}[when a check request was received.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1237022581}*[收到权限检查请求时，交换机]{style="font-family:宋体"}[10:00:00:e0:02:00:00:00]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内通过权限检查，允许其在接口]{style="font-family:宋体"}[FC1/0/5]{lang="EN-US"}[上登录]{style="font-family:宋体"}*

[[\*Mar 28 03:09:55:471 2014 Sysname]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1489_93403_221524250}[FCPS/7/EVENT: -MDC=1; Link is up because the switch with sWWN 10:00:00:e0:02:00:00:00 is logging in through Fc1/0/5 in VSAN 2.]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x813232340}*[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内由于交换机]{style="font-family:宋体"}[10:00:00:e0:02:00:00:00]{lang="EN-US"}[在接口]{style="font-family:宋体"}[FC1/0/5]{lang="EN-US"}[上登录，链路状态]{style="font-family:宋体"}[up]{lang="EN-US"}*

[[\*Mar 28 03:09:55:473 2014 Sysname]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[ ]{lang="EN-US"}]{#struct_0_x1489_93403_x1576015679}[FCPS/7/NOTIFY: -MDC=1; The switch with sWWN 10:00:00:e0:02:00:00:00 was allowed to log in through Fc1/0/5 in VSAN 2 when a link up event was received.]{lang="EN-US" style="font-size:8.5pt;font-family:
\"Courier New\""}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_221524249}*[收到链路]{style="font-family:宋体"}[up]{lang="EN-US"}[事件时，交换机]{style="font-family:宋体"}[10:00:00:e0:02:00:00:00]{lang="EN-US"}[在]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内通过权限检查，允许其在接口]{style="font-family:宋体"}[FC1/0/5]{lang="EN-US"}[上登录]{style="font-family:宋体"}*

::: {#1992279166 .myid}
[]{#_Toc404797592}[]{#struct_0_x1489_93403_778265333}[]{#_Toc351468644}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fcs**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1616701485}

[**[debugging fcs ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1010935437}

[**[undo debugging fcs ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_629426133}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1369455030}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_1025124797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1265525070}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_548248107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_404544402}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1010476685}

[**[all]{lang="FR"}**]{#struct_0_x1489_93403_x1127996571}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="FR"}**]{#struct_0_x1489_93403_x675835568}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="FR"}**]{#struct_0_x1489_93403_x1172610863}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x764951223}[：]{style="font-family:宋体"}[表示报文调试信息开关。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_838571589}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2094278666}

[**[debugging fcs]{lang="FR"}**]{#struct_0_x1489_93403_x656107284}[命令用来打开]{style="font-family:宋体"}[FCS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fc]{lang="EN-US"}[s]{lang="FR"}**[命令用来关闭]{style="font-family:宋体"}[FCS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FCS]{lang="EN-US"}]{#struct_0_x1489_93403_x1010542221}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-37 ]{lang="EN-US"}[debugging fcs error]{lang="EN-US"}]{#struct_0_x1489_93403_440224002}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1187459277}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x557641941}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_2051440179}

[[VSAN *vsan-id*: invalid source FCID for FC ping request]{lang="EN-US"}]{#struct_0_x1489_93403_x1368975085}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607757}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[非法]{style="font-family:宋体"}

[]{#struct_0_x1489_93403_522403803}[]{#OLE_LINK2}[[VSAN *[vsan-id]{style="color:black"}*:*[ ]{style="color:black"}*[invalid payload length for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{style="color:black"}]{lang="EN-US"}]{#OLE_LINK1}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x75380811}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的负载长度非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid version for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673293}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1605843507}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的版本非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid port tag for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_346992198}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1875329338}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的端口标签非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid port length for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214541}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1403666688}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的端口长度非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid FCID for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_1769802982}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_508640257}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* was processing the FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010280077}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1000308810}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求正在处理，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid WWN for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_688037287}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010738828}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[WWN]{lang="EN-US"}[非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* failed to send echo request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x165977788}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_437866990}[内发送]{style="font-family:宋体"}[echo]{lang="EN-US"}[请求失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid token value for FC ping request (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_1744504663}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804364}[内]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求的]{style="font-family:宋体"}[token]{lang="EN-US"}[值非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* failed to add FC ping session (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x2085762236}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x525798714}[内添加]{style="font-family:宋体"}[fcping]{lang="EN-US"}[会话失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid source FCID for FTR request.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010869900}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_626830748}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求报文中的源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid payload length for FTR request (source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_1020749289}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1866812650}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求的负载长度错误，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id:* invalid version for FTR request (source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010935436}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2099457222}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求的版本无效，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid port for FTR request (source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_165151847}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010476684}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求的端口无效，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id*: invalid token value for FTR request (source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_438087370}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_118025324}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求的]{style="font-family:宋体"}[token]{lang="EN-US"}[值无效，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* was processing the FTR request (source FCID = *src-fc-id,* token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010542220}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1125859939}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求正在被处理，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值为]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id*: source FCID and destination FCID of FTR request were not in the same zone.]{lang="EN-US"}]{#struct_0_x1489_93403_207998038}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607756}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求报文中的源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[和目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[不在一个]{style="font-family:宋体"}[zone]{lang="EN-US"}[内。]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to add port when *interface-name* was link/physically up.]{lang="EN-US"}]{#struct_0_x1489_93403_x1043680138}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1377027789}[内当接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[链路]{style="font-family:宋体"}[/]{lang="EN-US"}[物理]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，添加端口失败]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid payload length.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673292}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1123039848}[内报文负载长度非法]{style="font-family:宋体"}

[[VSAN *vsan-id:* The max size in packet was less than minimum length of ACC payload.]{lang="EN-US"}]{#struct_0_x1489_93403_218978940}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214540}[内报文中的]{style="font-family:宋体"}[max size]{lang="EN-US"}[小于]{style="font-family:宋体"}[ACC]{lang="EN-US"}[负载的最小长度]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to send *packet-type* ACC frame to domain *domain-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1325216667}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_560768079}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}*[packet-type ]{lang="EN-US"}*[ACC]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to send *packet-type* request to domain *domain-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010280076}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1728574545}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求失败]{style="font-family:宋体"}

[[VSAN *vsan-id*: IE WWN in the frame did not match local IE WWN]{lang="EN-US"}]{#struct_0_x1489_93403_x1010738831}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2088357625}[内报文中的]{style="font-family:宋体"}[IE WWN]{lang="EN-US"}[与本地]{style="font-family:宋体"}[IE WWN]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to get CT register information.]{lang="EN-US"}]{#struct_0_x1489_93403_x2031209277}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804367}[内获取]{style="font-family:宋体"}[CT]{lang="EN-US"}[注册信息失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to parse CT header.]{lang="EN-US"}]{#struct_0_x1489_93403_643121119}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_201163458}[内解析报文]{style="font-family:宋体"}[CT]{lang="EN-US"}[头部失败]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid GMI request with fragment ID *fragment-id* in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*, expected fragment ID = *fragment-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010869903}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1030115275}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*[，预期的分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to find GMI session in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010935439}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2146511389}[中域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内，查找]{style="font-family:宋体"}[GMI session]{lang="EN-US"}[失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to send *packet-type* packet (socket = *socket-id*, destination FCID = *dst-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1010476687}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_34802843}[内发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文失败，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[是]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to receive response packet with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1584085469}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010542223}[内接收回应报文失败，]{style="font-family:宋体"}[socket]{lang="EN-US"}[是]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to create the socket for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1603023416}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607759}[内为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文创建]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to bind socket *socket-id* for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2041433577}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1869495491}[内为]{style="font-family:宋体"}*[packet-typ]{lang="EN-US"}*[报文绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败，]{style="font-family:宋体"}[socket]{lang="EN-US"}[是]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to receive request packet with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673295}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1526324375}[内从]{style="font-family:宋体"}[socket]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[接收请求报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to create *packet-type* timer for socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214543}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_240867274}[内为]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[的]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文创建定时器失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-38 ]{lang="EN-US"}[debugging fcs event]{lang="EN-US"}]{#struct_0_x1489_93403_602680953}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1181837965}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1010280079}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x193739756}

[[VSAN *vsan-id* successfully sent *count-value* FCS requests to domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x888599342}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x331541358}[内成功发送]{style="font-family:宋体"}*[count-value]{lang="EN-US"}*[个]{style="font-family:宋体"}[FCS]{lang="EN-US"}[请求到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*

[[VSAN *vsan-id* received *receiverespcount-value* responses in total for *sentreqcount-value* requests in domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010738830}

[[在域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x522273684}[内，]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[在发送请求]{style="font-family:宋体"}*[sentreqcount-value]{lang="EN-US"}*[个数中接收到的响应个数]{style="font-family:宋体"}*[receiverespcount-value]{lang="EN-US"}*

[[VSAN *vsan-id*: Topology discovery aging timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x1834000770}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1661788864}[内拓扑发现老化定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* processed *event* (*event-id*) event in *topostatus* (*topostatus-id*) state.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010804366}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x922962822}[内处理当前]{style="font-family:宋体"}*[topostatus-id]{lang="EN-US"}*[拓扑发现状态下有关的]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[*[topostatus-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x645076239}[与]{style="font-family:宋体"}*[topostatus]{lang="EN-US"}*[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1489_93403_980636874}[：]{lang="EN-US" style="font-family:宋体"}[inProgress]{lang="EN-US"}[，拓扑发现进行中状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1489_93403_x1010869902}[：]{lang="EN-US" style="font-family:宋体"}[completed]{lang="EN-US"}[，拓扑发现完成状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1489_93403_x535968666}[：]{style="font-family:宋体"}[localOnly]{lang="EN-US"}[，拓扑发现未开始状态]{style="font-family:宋体"}

[*[event-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x1478391859}[与]{style="font-family:宋体"}*[event]{lang="EN-US"}*[取值及含义：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1489_93403_x348963690}[：]{lang="EN-US" style="font-family:宋体"}[discovery start]{lang="EN-US"}[，拓扑发现开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x1489_93403_x1010935438}[：]{lang="EN-US" style="font-family:宋体"}[discovery stop]{lang="EN-US"}[，拓扑发现停止]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x1489_93403_x580427448}[：]{lang="EN-US" style="font-family:宋体"}[GIEIL ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GIEIL ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x1489_93403_349348542}[：]{lang="EN-US" style="font-family:宋体"}[GFN ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GFN ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x1489_93403_125021822}[：]{lang="EN-US" style="font-family:宋体"}[GIELN ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[ GIELN ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x1489_93403_x1010476686}[：]{lang="EN-US" style="font-family:宋体"}[GMAL ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GMAL ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x1489_93403_1600886784}[：]{lang="EN-US" style="font-family:宋体"}[GPPN ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GPPN ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x1489_93403_1356925983}[：]{lang="EN-US" style="font-family:宋体"}[GPSC ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GPSC ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x1489_93403_x1010542222}[：]{lang="EN-US" style="font-family:宋体"}[GPS ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GPS ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x1489_93403_36939475}[：]{lang="EN-US" style="font-family:宋体"}[GAPNL ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GAPNL ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x1489_93403_809286978}[：]{lang="EN-US" style="font-family:宋体"}[GPL ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GPL ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_x1489_93403_x1859364413}[：]{lang="EN-US" style="font-family:宋体"}[GSES ACC packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[GSES ACC]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[12]{lang="EN-US"}]{#struct_0_x1489_93403_x1010607758}[：]{lang="EN-US" style="font-family:宋体"}[RJT packet]{lang="EN-US"}[，收到]{lang="EN-US" style="font-family:宋体"}[RJT]{lang="EN-US"}[拒绝报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[13]{lang="EN-US"}]{#struct_0_x1489_93403_475349636}[：]{lang="EN-US" style="font-family:宋体"}[packet sending failure]{lang="EN-US"}[，报文发送失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[14]{lang="EN-US"}]{#struct_0_x1489_93403_x1294773003}[：]{lang="EN-US" style="font-family:宋体"}[route deletion]{lang="EN-US"}[，路由删除事件]{lang="EN-US" style="font-family:宋体"}

[[VSAN *vsan-id* successfully added port *Interfacename* when it was physically/link up.]{lang="EN-US"}]{#struct_0_x1489_93403_x1010673294}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_39759566}[内当接口]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[物理]{style="font-family:宋体"}[/]{lang="EN-US"}[链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，成功添加端口]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully deleted port *Interfacename* when it was physically/link down.]{lang="EN-US"}]{#struct_0_x1489_93403_1177608355}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010214542}[内当接口]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[物理]{style="font-family:宋体"}[/]{lang="EN-US"}[链路]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[时，成功删除端口]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully updated link attributes when *Interfacename* is link *up/down*.]{lang="EN-US"}]{#struct_0_x1489_93403_1806951215}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x432367777}[内，当接口]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[链路]{style="font-family:宋体"}[up/down]{lang="EN-US"}[时成功更新链路属性]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully deleted attached port *portname* of *Interfacename*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1472232344}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1010280078}[内成功删除接口]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[的附属连接端口]{style="font-family:宋体"}*[portname]{lang="EN-US"}*

[[VSAN *vsan-id* successfully added attached port *portname* of *Interfacename*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1759823697}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1510594557}[内成功添加接口]{style="font-family:宋体"}*[Interfacename]{lang="EN-US"}*[的附属连接端口]{style="font-family:宋体"}*[portname]{lang="EN-US"}*

[[VSAN *vsan-id* successfully added management address *managmentaddr-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_911575474}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1306659524}[内成功添加管理地址]{style="font-family:宋体"}*[managmentaddr-value]{lang="EN-US"}*

[[VSAN *vsan-id* successfully deleted management address *managmentaddr-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_911509938}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811698418}[内成功删除管理地址]{style="font-family:宋体"}*[managmentaddr-value]{lang="EN-US"}*

[[VSAN *vsan-id* successfully updated WWN of local IE to *switchWWN-value*.]{lang="EN-US"}]{#struct_0_x1489_93403_1652664762}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911444402}[内成功更新本地]{style="font-family:宋体"}[IE]{lang="EN-US"}[的]{style="font-family:宋体"}[WWN *switchWWN-value*]{lang="EN-US"}

[[VSAN *vsan-id*: The *frame-value* frame timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x896863049}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_708364500}[内]{style="font-family:宋体"}*[frame-value]{lang="EN-US"}*[帧定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*: FTR timer timed out (source FCID = *src-fc-id,* token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_911378866}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1976318038}[内]{style="font-family:宋体"}[FTR]{lang="EN-US"}[定时器超时，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* received FC ping request frame from source FCID *fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1798293280}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911837618}[内收到从]{style="font-family:宋体"}[FCID *fc-id*]{lang="EN-US"}[发送的]{style="font-family:宋体"}[fcping]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id* received domain ID change event, which changed from *domain-id1* to *domain-id2.*]{lang="EN-US"}]{#struct_0_x1489_93403_1147014286}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911772082}[内收到域]{style="font-family:宋体"}[ID]{lang="EN-US"}[变化事件，域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}*[domain-id1]{lang="EN-US"}*[变到]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[2]{lang="EN-US"}

[[VSAN *vsan-id* received switch WWN change event, which changed from *wwn1* to *wwn2.*]{lang="EN-US"}]{#struct_0_x1489_93403_x628350258}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x230817519}[内收到交换机]{style="font-family:宋体"}[WWN]{lang="EN-US"}[变化事件，从]{style="font-family:宋体"}*[wwn1 ]{lang="EN-US"}*[变到]{style="font-family:宋体"}*[wwn2]{lang="EN-US"}*

[[VSAN *vsan-id* received route adding event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911706546}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_960659588}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由添加事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received route deleting event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911641010}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x609541559}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由删除事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received FLOGI event of port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_845374944}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_912099762}[内收到端口]{style="font-family:宋体"}*[port-wwn]{lang="EN-US"}*[的]{style="font-family:宋体"}[flogin]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received FLOGO event of port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_x641081804}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_912034226}[内收到端口]{style="font-family:宋体"}*[port-wwn]{lang="EN-US"}*[的]{style="font-family:宋体"}[flogout]{lang="EN-US"}[事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-39 ]{lang="EN-US"}[debugging fcs packet]{lang="EN-US"}]{#struct_0_x1489_93403_x268879041}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1176829357}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2062356089}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1412712384}

[[VSAN *vsan-id* received *packet-type* RJT frame from domain *domain-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1997726842}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911575475}[内从域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[拒绝报文]{style="font-family:宋体"}

[[VSAN *vsan-id* received *packet-type* ACC frame from domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1306659523}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x429697231}[内从域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[接收到]{style="font-family:宋体"}*[packet-type ]{lang="EN-US"}*[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id* received *packet-type* request from domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1293644548}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x550686247}[内从域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id* sent *packet-type* RJT frame to domain *domain-id* (reason code = *reason-code*, reason code explanation = *code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_911509939}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811698417}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[拒绝报文，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[VSAN *vsan-id* sent *packet-type* ACC frame to domain *domain-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_1653123514}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x349190369}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}*[packet-type ]{lang="EN-US"}*[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id* sent *packet-type* request to domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911444403}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x896863050}[内向域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully sent FC ping ACC frame.]{lang="EN-US"}]{#struct_0_x1489_93403_708954323}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_911378867}[内成功发送]{style="font-family:宋体"}[fcping ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id* sent FC ping reject frame (source FCID = *src-fc-id*, destination FCID = *dst-fc-id*, token = *token-value*)*.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1976318037}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_1395008753}[内发送]{style="font-family:宋体"}[fcping]{lang="EN-US"}[拒绝报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* sent FTR ACC frame (destination FCID = *dst-fc-id*, token = *token-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1562856488}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_911837619}[内发送]{style="font-family:宋体"}[FTR ACC]{lang="EN-US"}[报文，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[token]{lang="EN-US"}[值是]{style="font-family:宋体"}*[token-value]{lang="EN-US"}*

[[VSAN *vsan-id* sent FTR RJT frame (destination FCID = *dst-fc-id*, reason code = *reason-code*, reason code explanation = *code-explanation*).]{lang="EN-US"}]{#struct_0_x1489_93403_1147014287}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_1848471906}[内发送]{style="font-family:宋体"}[FTR RJT]{lang="EN-US"}[报文，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，原因码是]{style="font-family:宋体"}*[reason-code]{lang="EN-US"}*[，解释码是]{style="font-family:宋体"}*[code-explanation]{lang="EN-US"}*

[[VSAN *vsan-id* received FTR request frame (source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1211189267}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_911772083}[内接收]{style="font-family:宋体"}[FTR]{lang="EN-US"}[请求报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* request packet (socket = *socket-id*, source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x628350257}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x230096623}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* response packet (socket =*socket-id*, source FCID = *src-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_911706547}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_960659587}[内从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[回应报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* successfully sent *packet-type* packet (socket =*socket-id*, destination FCID = *dst-fc-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x958429070}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x487382325}[内发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文成功，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}[，]{style="font-family:宋体"}*[socket]{lang="EN-US"}[是]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* request from FCID *src-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911641011}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x609541560}[内接收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求报文，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_845964771}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_912099763}[打开]{style="font-family:宋体"}[FCS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcs error vsan 1]{lang="EN-US"}]{#struct_0_x1489_93403_x641081803}

[\*Aug 23 11:17:17:522 2012 Sysname FCGS/7/ERROR: -MDC=1; VSAN 1 failed to get CT register information.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_421692676}*[内获取]{style="font-family:宋体"}[CT]{lang="EN-US"}[注册信息失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1773787149}[打开]{style="font-family:宋体"}[FCS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcs event vsan 1]{lang="EN-US"}]{#struct_0_x1489_93403_x1236960344}

[\*Aug 23 11:05:42:640 2012 Sysname FCGS/7/EVENT: -MDC=1; VSAN 1 successfully added management address snmp://111.111.111.111.]{lang="EN-US"}

[*[// VSAN 1]{lang="EN-US"}*]{#struct_0_x1489_93403_1469762342}*[内成功添加管理地址]{style="font-family:宋体"}[snmp://111.111.111.111]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x281527131}[打开]{style="font-family:宋体"}[FCS]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}[VSAN 1]{lang="EN-US"}[内发起拓扑发现时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fcs packet vsan 1]{lang="EN-US"}]{#struct_0_x1489_93403_912034227}

[\*Aug 26 09:35:44:853 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 25, destination FCID = fffc02).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x268879040}*[拓扑发现开始时向]{style="font-family:宋体"}[fffc02]{lang="EN-US"}[发送]{style="font-family:宋体"}[CT]{lang="EN-US"}[请求报文以区分以下要发送的报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:853 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GFN request to domain 2]{lang="EN-US"}]{#struct_0_x1489_93403_x2062421625}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x596400961}*[拓扑发现开始时向域]{style="font-family:宋体"}[2]{lang="EN-US"}[发送]{style="font-family:宋体"}[GFN]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:854 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 26, destination FCID = fffc02).]{lang="EN-US"}]{#struct_0_x1489_93403_135210538}

[\*Aug 26 09:35:44:854 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GIELN request to domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_2067455459}*[向域]{style="font-family:宋体"}[2]{lang="EN-US"}[发送]{style="font-family:宋体"}[GIELN]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:856 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 27, destination FCID = fffc02).   ]{lang="EN-US"}]{#struct_0_x1489_93403_911575472}

[\*Aug 26 09:35:44:856 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GMAL request to domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1306659526}*[向域]{style="font-family:宋体"}[2]{lang="EN-US"}[发送]{style="font-family:宋体"}[GMAL]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:858 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 28, destination FCID = fffc02).   ]{lang="EN-US"}]{#struct_0_x1489_93403_329817656}

[\*Aug 26 09:35:44:858 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GIEIL request to domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1287046840}*[向域]{style="font-family:宋体"}[2]{lang="EN-US"}[发送]{style="font-family:宋体"}[GIEIL]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:862 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 successfully sent request packet (socket = 29, destination FCID = fffc02).   ]{lang="EN-US"}]{#struct_0_x1489_93403_x737243768}

[\*Aug 26 09:35:44:862 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 sent GPL request to domain 2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_660625029}*[向域]{style="font-family:宋体"}[2]{lang="EN-US"}[发送]{style="font-family:宋体"}[GPL]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:869 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 25, source FCID = fffc02). ]{lang="EN-US"}]{#struct_0_x1489_93403_219678249}

[\*Aug 26 09:35:44:870 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GFN ACC frame from domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_911509936}*[从域]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[GFN ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:871 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 26, source FCID = fffc02). ]{lang="EN-US"}]{#struct_0_x1489_93403_1811698416}

[\*Aug 26 09:35:44:871 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GIELN ACC frame from domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1653057978}*[从域]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[GIELN ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:872 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 27, source FCID = fffc02). ]{lang="EN-US"}]{#struct_0_x1489_93403_x671812390}

[\*Aug 26 09:35:44:872 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GMAL ACC frame from domain 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x528225215}*[从域]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[GMAL ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:873 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 28, source FCID = fffc02). ]{lang="EN-US"}]{#struct_0_x1489_93403_911444400}

[\*Aug 26 09:35:44:873 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GIEIL ACC frame from domain 2. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x896863051}*[从域]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[GIEIL ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Aug 26 09:35:44:874 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received FCS response packet  (socket = 29, source FCID = fffc02). ]{lang="EN-US"}]{#struct_0_x1489_93403_708888787}

[\*Aug 26 09:35:44:874 2012 Sysname FCGS/7/PACKET: -MDC=1; VSAN 1 received GPL ACC frame from domain 2. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_220839110}*[从域]{style="font-family:宋体"}[2]{lang="EN-US"}[接收]{style="font-family:宋体"}[GPL ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

::: {#-1116748644 .myid}
[]{#_Toc404797593}[]{#struct_0_x1489_93403_1467517793}[]{#_Toc351468645}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fdmi**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1655733393}

[**[debugging fdmi ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x845864944}

[**[undo debugging fdmi ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_911378864}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1976318040}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2139984904}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_401544456}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x1477065964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_928132728}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1664683146}

[**[all]{lang="FR"}**]{#struct_0_x1489_93403_911837616}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="FR"}**]{#struct_0_x1489_93403_1147014276}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="FR"}**]{#struct_0_x1489_93403_1848537455}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x735052759}[：]{style="font-family:宋体"}[表示报文调试信息开关。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1115409121}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1452029152}

[**[debugging fdmi]{lang="FR"}**]{#struct_0_x1489_93403_137975121}[命令用来打开]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fdmi]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FDMI]{lang="EN-US"}]{#struct_0_x1489_93403_911772080}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-40 ]{lang="EN-US"}[debugging fdmi error]{lang="EN-US"}]{#struct_0_x1489_93403_x628350260}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1206197709}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x230293232}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1634445687}

[[VSAN *vsan-id* failed to get CT register information.]{lang="EN-US"}]{#struct_0_x1489_93403_x813909398}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911706544}[内查找]{style="font-family:宋体"}[CT]{lang="EN-US"}[注册信息失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to parse CT header.]{lang="EN-US"}]{#struct_0_x1489_93403_960659586}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x958429069}[内解析报文]{style="font-family:宋体"}[CT]{lang="EN-US"}[头部失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to receive request packet with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x486792500}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911641008}[内接收]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[的请求报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to receive response packet with socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1346773569}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x287453472}[内接收]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[的回应报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to create the socket for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x50999212}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_912099760}[内为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文创建]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to bind socket *socket-id* for *packet-type* packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x641081802}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_421758212}[内为]{style="font-family:宋体"}*[packet-typ]{lang="EN-US"}*[报文绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to create *packet-type* timer for socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1318779119}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_912034224}[内为]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[的]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文创建定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to send *packet-type* packet with socket *socket-id* to FCID *dst-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x268879043}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2062225017}[内向]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}[发送报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[、目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[的报文失败]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid GMI request with fragment ID *fragment-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*, expected fragment ID = *fragment-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_43617787}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911575473}[内分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[GMI]{lang="EN-US"}[请求非法，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*[，当前的分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to find GMI session in domain *domain-id* (source FCID = *src-fc-id*, transaction ID = *transaction-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1306659525}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1236266285}[中域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[内，查找]{style="font-family:宋体"}[GMI session]{lang="EN-US"}[失败，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*

[[VSAN *vsan-id* failed to get CT register information.]{lang="EN-US"}]{#struct_0_x1489_93403_911509937}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811698415}[内查找]{style="font-family:宋体"}[CT]{lang="EN-US"}[注册信息失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to parse FDMI header.]{lang="EN-US"}]{#struct_0_x1489_93403_1652992442}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_x1911407945}[内解析]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[报文头失败]{style="font-family:宋体"}

[[VSAN *vsan-id*: invalid command code *command-code* in HBA request.]{lang="EN-US"}]{#struct_0_x1489_93403_911444401}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x896863052}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[请求中命令码不合法]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to get switch WWN of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_709085395}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911378865}[内获取域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的交换机]{style="font-family:宋体"}[WWN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id* failed to add GMI session (source FCID = *src-fc-id*, transaction ID = *transaction-id*, fragment ID = *fragment-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1976318039}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_232209339}[内添加]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话失败，报文源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*[，分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-41 ]{lang="EN-US"}[debugging fdmi event]{lang="EN-US"}]{#struct_0_x1489_93403_1382581545}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1202180173}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_911837617}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1147014277}

[[VSAN *vsan-id*: GMI frame timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1848471919}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1211254804}[内]{style="font-family:宋体"}[GMI]{lang="EN-US"}[报文定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* received FLOGO event of port *port-wwn*.]{lang="EN-US"}]{#struct_0_x1489_93403_911772081}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x628350259}[内收到端口]{style="font-family:宋体"}*[port-wwn]{lang="EN-US"}*[的]{style="font-family:宋体"}[flogout]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received domain ID change event, which changed from *domain-id1* to *domain-id2*.]{lang="EN-US"}]{#struct_0_x1489_93403_x230751983}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1596887517}[内收到域]{style="font-family:宋体"}[ID]{lang="EN-US"}[变化事件，域]{style="font-family:宋体"}[ID]{lang="EN-US"}[从]{style="font-family:宋体"}*[domain-id1]{lang="EN-US"}*[变到]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[2]{lang="EN-US"}

[[VSAN *vsan-id* received route adding event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911706545}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_960659585}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由添加事件]{style="font-family:宋体"}

[[VSAN *vsan-id* received route deleting event of domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x958429072}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x487251253}[内收到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[的路由删除事件]{style="font-family:宋体"}

[[VSAN *vsan-id*: FETCH timer of domain *domain-id* timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_911641009}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1346773568}[内域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[下]{style="font-family:宋体"}[FETCH]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id*: *packet-name* frame timer of domain *domain-id* timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x287387936}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2071092643}[内域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[下]{style="font-family:宋体"}*[packet-name]{lang="EN-US"}*[报文定时器超时]{style="font-family:宋体"}

[[VSAN *vsan-id* successfully added GMI session (source FCID = *src-fc-id*, transaction ID = *transaction-id*, fragment ID = *fragment-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_912099761}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x641081801}[内添加]{style="font-family:宋体"}[GMI]{lang="EN-US"}[会话成功，报文源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[，事务]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[transaction-id]{lang="EN-US"}*[，分片]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[fragment-id]{lang="EN-US"}*

[[VSAN *vsan-id* successfully deleted HBA *hba-id* in domain *domain-id* for principal switch conflict.]{lang="EN-US"}]{#struct_0_x1489_93403_421561604}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_912034225}[内处理主管理交换机冲突，域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[中删除]{style="font-family:宋体"}[HBA]{lang="EN-US"}[为]{style="font-family:宋体"}*[hba-id]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-42 ]{lang="EN-US"}[debugging fdmi packet]{lang="EN-US"}]{#struct_0_x1489_93403_x268879042}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1196135405}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2062290553}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_847586121}

[[VSAN *vsan-id*: The HBAPKT module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1399727362}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911575470}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的拒绝报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The HBAREG module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1306659528}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x476751398}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[注册报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的拒绝报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The FORWPKT module sent *packet-type (original-pkt-name)* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_427593232}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_298190835}[内转发报文处理模块发送]{style="font-family:宋体"}*[packet-type1(original-pkt-name)]{lang="EN-US"}*[的拒绝报文到目的]{style="font-family:
  宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The HBAREG module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_911509934}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811698414}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[注册报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The FORWPKT module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_1652926906}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1653237831}[内转发报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* request packet with socket *socket-id* from FCID *src-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911444398}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x2009873296}[内成功收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[请求报文，]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* response packet with socket *socket-id* from FCID *src-fc-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_1422891337}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911378862}[内成功收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[回应报文，]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*[，源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*

[[VSAN *vsan-id* successfully sent *packet-type* packet with socket *socket-id* to FCID *dst-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1976318042}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_992182978}[内成功发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，]{style="font-family:宋体"}[socket ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-id]{lang="EN-US"}*

[[VSAN *vsan-id*: The HBAGET module sent *packet-type* ACC frame to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_613510107}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911837614}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The HBAGET module sent *packet-type* RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_1147014274}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1848406383}[内]{style="font-family:宋体"}[HBA]{lang="EN-US"}[报文处理模块发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的拒绝报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* request from FCID *src-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_911772078}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1348394284}[内收到源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[的报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的请求报文]{style="font-family:宋体"}

[[VSAN *vsan-id* received *packet-type* ACC frame from FCID *src-fc-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1535098213}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x1462369199}[内收到源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}*[src-fc-id]{lang="EN-US"}*[的报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*: The NOTIPKT module sent *notify-pkt-name*(*original-pkt-name*) ACC frame to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_911706542}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_960659584}[内通知报文处理模块发送]{style="font-family:宋体"}*[notify-pkt-name]{lang="EN-US"}*[(*original-pkt-name*)]{lang="EN-US"}[的]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The NOTIPKT module sent *notify-pkt-name*(*original-pkt-name*) RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x958429071}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911641006}[内通知报文处理模块发送]{style="font-family:宋体"}*[notify-pkt-name]{lang="EN-US"}*[(*original-pkt-name*)]{lang="EN-US"}[的]{style="font-family:宋体"}[RJT]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* received *packet-type* RJT frame from FCID *src-fc-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1346773575}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_912099758}[内收到源]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[src-fc-id]{lang="EN-US"}[的报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的拒绝报文]{style="font-family:宋体"}

[[VSAN *id*: The NOTIPKT module sent *packet-type* request to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_2079907374}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_900427325}[内通知报文处理模块发送报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的通知报文，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，返回值是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN vsan-*id*: The FORWPKT module sent *packet-type* request to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_912034222}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x268879037}[内转发报文处理模块发送报文类型为]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的转发报文，目的]{style="font-family:宋体"}[FCID]{lang="EN-US"}[是]{style="font-family:宋体"}*[dst-fc-id]{lang="EN-US"}*[，返回值是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The FORWPKT module sent RJT frame to FCID *dst-fc-id* (reason code = *reason-code*, reason code explanation = *code-explanation*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x2061962868}

[[VSAN *vsan-id* ]{lang="EN-US"}]{#struct_0_x1489_93403_911575471}[内转发报文处理模块发送拒绝报文，错误原因码是]{style="font-family:宋体"}*[reasoncode-id]{lang="EN-US"}*[，错误原因解释码是]{style="font-family:宋体"}*[explain-id]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，返回值是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id*: The FORWPKT module sent ACC frame to FCID *dst-fc-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1306659527}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1895901597}[内转发报文处理模块发送]{style="font-family:宋体"}[ACC]{lang="EN-US"}[报文到目的]{style="font-family:宋体"}[FCID *dst-fc-id*]{lang="EN-US"}[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* send FETCH request to domain *domain-id* (return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_911509935}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1811698413}[内发送]{style="font-family:宋体"}[FETCH]{lang="EN-US"}[请求到域]{style="font-family:宋体"}*[ domain-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* send GHAT request to domain *domain-id* (HBA ID = *hba-id,* return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_1653385658}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_911444399}[内发送]{style="font-family:宋体"}[GHAT]{lang="EN-US"}[请求报文到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[HBA]{lang="EN-US"}[为]{style="font-family:宋体"}*[hba-id]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[[VSAN *vsan-id* send GPAT request to domain *domain-id* (port name = *port-wwn*, return value = *return-value*).]{lang="EN-US"}]{#struct_0_x1489_93403_x2009873297}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x143192604}[内发送]{style="font-family:宋体"}[GPAT]{lang="EN-US"}[请求报文到域]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[，端口名为]{style="font-family:宋体"}*[port-wwn]{lang="EN-US"}*[，处理结果是]{style="font-family:宋体"}*[return-value]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1071962219}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_911378863}[打开]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fdmi error vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x1976318041}

[\*Dec 25 09:21:56:925 2012 Sysname FDMI/7/ERROR: -MDC=1; VSAN 2: invalid command code 0x0220 in HBA request.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_588898451}*[内，]{style="font-family:宋体"}[HBA]{lang="EN-US"}[请求中的命令码]{style="font-family:宋体"}[0x0220]{lang="EN-US"}[不合法]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x764266540}[打开]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fdmi event vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_782621759}

[\*Dec 25 09:12:54:991 2012 Sysname FDMI/7/EVENT: -MDC=1; VSAN 2 received FLOGO event of port e2:01:00:11:22:00:03:01.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_850765188}*[内，收到端口]{style="font-family:宋体"}[WWN]{lang="EN-US"}[为]{style="font-family:宋体"}[e2:01:00:11:22:00:03:01]{lang="EN-US"}[的端口的]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_911837615}[打开]{style="font-family:宋体"}[FDMI]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fdmi packet vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_1147014275}

[\*Dec 25 09:03:47:325 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 received HBA request packet with socket 13 from FCID 010000.]{lang="EN-US"}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_1848340847}*[内，从]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的节点收到]{style="font-family:宋体"}[HBA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Dec 25 09:03:47:325 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 received RHBA request from FCID 010000.]{lang="EN-US"}]{#struct_0_x1489_93403_x1985854475}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_1078976861}*[内，从]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的节点收到]{style="font-family:宋体"}[RHBA]{lang="EN-US"}[请求报文]{style="font-family:宋体"}*

[[\*Dec 25 09:03:47:330 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2 successfully sent ACC packet with socket 13 to FCID 010000.]{lang="EN-US"}]{#struct_0_x1489_93403_2020798340}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_1465437212}*[内，成功向]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的节点发送]{style="font-family:宋体"}[ACC]{lang="EN-US"}[回应报文]{style="font-family:宋体"}*

[[\*Dec 25 09:03:47:330 2012 Sysname FDMI/7/PACKET: -MDC=1; VSAN 2: The HBAREG module sent RHBA ACC frame to FCID 010000 (return value = 0).]{lang="EN-US"}]{#struct_0_x1489_93403_911772079}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x1348394283}*[内，成功向]{style="font-family:宋体"}[FCID]{lang="EN-US"}[为]{style="font-family:宋体"}[010000]{lang="EN-US"}[的节点发送]{style="font-family:宋体"}[RHBA ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

::: {#984508903 .myid}
[]{#_Toc404797594}[]{#struct_0_x1489_93403_1193785142}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fip-snooping**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1395373601}

[**[debugging fip-snooping]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **receive** \| **send** \] \| **rule** \| **session** \| **timer** }]{lang="EN-US"}[ \[ **vlan** *vlan-id* \| **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_1533016831}

[**[undo debugging fip-snooping]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **receive** \| **send** \] \| **rule** \| **session** \| **timer** } \[ **vlan** *vlan-id* \| **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1665848345}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_911706543}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_960659583}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x958429066}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x487513396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x2140876743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1207077071}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_986792140}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_911641007}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_1346773574}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x286601503}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1489_93403_x88294969}[：表示接收报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1489_93403_461837595}[：表示发送报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[rule]{lang="EN-US"}**]{#struct_0_x1489_93403_913460688}[：表示规则调试信息开关。]{style="font-family:宋体"}

[**[session]{lang="EN-US"}**]{#struct_0_x1489_93403_x1893316285}[：表示会话调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_912099759}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_x1489_93403_2079907375}[：表示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface]{lang="EN-US"}*[-*type* *interface*-*number*]{lang="EN-US"}]{#struct_0_x1489_93403_900361789}[：表示指定接口的调试信息开关，]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*type*]{lang="EN-US"}[只能是二层以太网接口或二层聚合接口。如果未指定本参数，表示所有二层以太网接口和二层聚合接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1427267816}

[**[debugging fip-snooping]{lang="EN-US"}**]{#struct_0_x1489_93403_560297342}[命令用来打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fip-snooping]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}]{#struct_0_x1489_93403_107519301}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1489_93403_x353261180}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1489_93403_912034223}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，表示同时指定接收和发送的报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1489_93403_x46410147}**[interface]{lang="EN-US"}**[参数]{style="font-family:宋体"}[打开的]{style="font-family:宋体"}[指定接口的调试信息开关，只能通过在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令中指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数来关闭。]{style="font-family:宋体"}

[[表1-43 ]{lang="EN-US"}[debugging fip-snooping error]{lang="EN-US"}]{#struct_0_x1489_93403_x2062028404}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1195321101}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2111754202}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x307048816}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for receiving interface mode was FCF.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817307881}

[[丢弃源接口模式是]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_56404171}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received VLAN Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_53669010}

[[接收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_1726658591}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for receiving interface mode was ENode.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817373417}

[[丢弃源接口模式是]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x525751448}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received a packet with incorrect length.]{lang="EN-US"}]{#struct_0_x1489_93403_x803113447}

[[接收到错误长度的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x956138432}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for relevant VLAN was not enabled with FIP Snooping.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817438953}

[[该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_336481405}[的]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[功能没有开启，丢弃报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to send the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1110907977}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x207849316}

[[VLAN *vlan-id*, Failed to send the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817504489}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x177863705}

[[VLAN *vlan-id*, interface *Interface-name*,  Discarded a Discovery Advertisement for the FCF-MAC had been saved under interface *Interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_528316318}

[[丢弃]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}]{#struct_0_x1489_93403_2137780668}[已经被接口储存的发现通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from FCF for the source and destination MAC addresses were both FCF-MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045737}

[[丢弃源和目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_1825501424}[都是]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for FC-MAP value was  different from that locally configured.]{lang="EN-US"}]{#struct_0_x1489_93403_186099670}

[[丢弃]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111273}[值和现有配置不同的发现通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP Name_Identifier descriptor length.]{lang="EN-US"}]{#struct_0_x1489_93403_1089112576}

[[该发现通告报文有长度不正确的]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x74084832}[名称描述符]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP Fabric descriptor length.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176809}

[[该发现通告报文有长度不正确的]{style="font-family:宋体"}[FIP Fabric]{lang="EN-US"}]{#struct_0_x1489_93403_1034458282}[描述符]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, The Discovery Advertisement had incorrect FIP FKA_ADV_Period descriptor length.]{lang="EN-US"}]{#struct_0_x1489_93403_975092087}

[[该发现通告报文有长度不正确的]{style="font-family:宋体"}[FKA_ADV_Period]{lang="EN-US"}]{#struct_0_x1489_93403_x1980939258}[描述符]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, The sum of the FIP Descriptor lengths of the packets was longer than FIP Descriptor List Length.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242345}

[[这些报文的]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x270399554}[描述符长度和长于]{style="font-family:宋体"}[FIP]{lang="EN-US"}[描述符表长度]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, The FIP Descriptor length of the packet is zero.]{lang="EN-US"}]{#struct_0_x1489_93403_x1761417040}

[[报文的]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783593}[描述符长度是零]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Invalid FKA_ADV_PERIOD in Discovery Advertisement.]{lang="EN-US"}]{#struct_0_x1489_93403_1805275715}

[[发现通告报文有无效的]{style="font-family:宋体"}[FKA_ADV_PERIOD]{lang="EN-US"}]{#struct_0_x1489_93403_832727858}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to create FCF maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1816849129}

[[创建]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x788473275}[维护定时器失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from ENode for the source MAC was FCF-MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_x356593579}

[[丢弃从]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x1817307880}[端口来的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[是]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for its version was not supported.]{lang="EN-US"}]{#struct_0_x1489_93403_x1509679770}

[[丢弃版本不支持的发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1817373416}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for the D bit was set to 1 in FIP FKA_ADV_Period descriptor.]{lang="EN-US"}]{#struct_0_x1489_93403_1040332493}

[[丢弃]{style="font-family:宋体"}[FIP FKA_ADV_Period ]{lang="EN-US"}]{#struct_0_x1489_93403_1250974396}[描述符]{style="font-family:宋体"}[D]{lang="EN-US"}[比特位设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[的发现通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a Discovery Advertisement for the number of FCF sessions had reached maximum.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817438952}

[[丢弃]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_1902565346}[会话到达最大数目的发现通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP Name_Identifier descriptor.]{lang="EN-US"}]{#struct_0_x1489_93403_x810390966}

[[获取]{style="font-family:宋体"}[FIP Name_Identifier]{lang="EN-US"}]{#struct_0_x1489_93403_x1817504488}[描述符失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP Fabric descriptor.]{lang="EN-US"}]{#struct_0_x1489_93403_x1743947646}

[[获取]{style="font-family:宋体"}[FIP Fabric]{lang="EN-US"}]{#struct_0_x1489_93403_491808931}[描述符失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP FKA_ADV_Period descriptor.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045736}

[[获取]{style="font-family:宋体"}[FIP FKA_ADV_Period]{lang="EN-US"}]{#struct_0_x1489_93403_259417483}[描述符失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet from ENode for the destination MAC was not All-FCF-MACs or FCF-MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111272}

[[丢弃从]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x1639770779}[端口来的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不是]{style="font-family:宋体"}[ALL-FCF-MACs]{lang="EN-US"}[或]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded the packet from FCF for the destination MAC was not All-ENode-MACs and the source MAC was not FCF-MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_1298640837}

[[丢弃从]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176808}[端口来的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不是]{style="font-family:宋体"}[ALL-ENode-MACs]{lang="EN-US"}[和源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不是]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to get FIP MAC address descriptor.]{lang="EN-US"}]{#struct_0_x1489_93403_x1694425073}

[[获取]{style="font-family:宋体"}[FIP MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242344}[地址描述符失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a FLOGI or FDISC ACC for the VN_Port MAC mismatched the FC-MAP configured.]{lang="EN-US"}]{#struct_0_x1489_93403_x1836483495}

[[丢弃]{style="font-family:宋体"}[ VN_Port MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783592}[与]{style="font-family:宋体"}[FC-MAP]{lang="EN-US"}[配置不符的]{style="font-family:宋体"}[FLOGI ]{lang="EN-US"}[或]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to get ENode WWN.]{lang="EN-US"}]{#struct_0_x1489_93403_239191774}

[[获取]{style="font-family:宋体"}[ENode WWN]{lang="EN-US"}]{#struct_0_x1489_93403_x548159622}[失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for the session had been saved under interface *Interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1816849128}

[[会话已经被其它接口保存，丢弃此虚链路实例化请求]{style="font-family:宋体"}]{#struct_0_x1489_93403_1940410080}

[[VLAN *vlan-id*, interface *Interface-name*, Unknown type of Virtual Link Instantiation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817307883}

[[虚链路实例化报文的类型是未知的]{style="font-family:宋体"}]{#struct_0_x1489_93403_1219203585}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Reply for the destination MAC was All-ENode-MACs.]{lang="EN-US"}]{#struct_0_x1489_93403_101361550}

[[丢弃目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817373419}[是]{style="font-family:宋体"}[ALL-ENode-MACs]{lang="EN-US"}[的虚链路实例化回应]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for the destination MAC was All-FCF-MACs.]{lang="EN-US"}]{#struct_0_x1489_93403_637047966}

[[丢弃目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817438955}[是]{style="font-family:宋体"}[ALL-FCF-MACs]{lang="EN-US"}[的虚链路实例化请求]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded FIP Keep Alive for the destination MAC was All-FCF-MACs.]{lang="EN-US"}]{#struct_0_x1489_93403_1143050459}

[[丢弃目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817504491}[是]{style="font-family:宋体"}[ALL-FCF-MACs]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP]{lang="EN-US"}[保活报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to create ENode maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_178301119}

[[创建]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045739}[维护定时器失败]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded Discovery Solicitation for source MAC was FPMA.]{lang="EN-US"}]{#struct_0_x1489_93403_x1306666458}

[[丢弃源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_411192076}[是]{style="font-family:宋体"}[FPMA]{lang="EN-US"}[的请求发现报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded Virtual Link Instantiation Request for source MAC was FPMA.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111275}

[[丢弃源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x73686838}[是]{style="font-family:宋体"}[FPMA]{lang="EN-US"}[的虚链路实例化请求]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded the packet for the number of FLOGI sessions had reached maximum.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176811}

[[丢弃]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_678162386}[会话达到最大值的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded FIP VN Keep Alive packet for session was not found.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242347}

[[丢弃会话未找到的]{style="font-family:宋体"}[FIP VN]{lang="EN-US"}]{#struct_0_x1489_93403_892399860}[保活报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to find outgoing interface for the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783595}

[[未找到报文转发出接口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1683122527}

[ ]{lang="EN-US"}

[[表1-44 ]{lang="EN-US"}[debugging fip-snooping event]{lang="EN-US"}]{#struct_0_x1489_93403_1118403710}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1480685709}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1816849131}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1144638099}

[[Sent VLAN Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2134251974}

[[发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_711637074}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, Received deleting VLAN event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817307882}

[[接收]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x346880356}[删除事件]{style="font-family:宋体"}

[[Interface *Interface-name*, Received VLAN events for deleting the interface from the VLANs.]{lang="EN-US"}]{#struct_0_x1489_93403_2044793293}

[[接收批量的端口离开]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_590070418}[事件]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received a VLAN event for deleting the interface from the VLAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817373418}

[[接收端口离开某个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x2091835389}[事件]{style="font-family:宋体"}

[[Interface *Interface-name*, Received interface link down event.]{lang="EN-US"}]{#struct_0_x1489_93403_1224595015}

[[接收到接口链路连接断开事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1817438954}

[[Interface *Interface-name*, Received interface inactive event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1585832896}

[[接收到接口不活跃事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_1579751344}

[[Interface *Interface-name*, Received interface joining aggregation group event.]{lang="EN-US"}]{#struct_0_x1489_93403_1214038022}

[[接收到接口加入聚合组事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1817504490}

[[Interface *Interface-name*, Received deleting interface event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1387782822}

[[接收到删除接口事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1754162883}

[[Interface *Interface-name*, The packet had incorrect FIP MAC address descriptor length.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045738}

[[报文包含不正确的]{style="font-family:宋体"}[FIP MAC]{lang="EN-US"}]{#struct_0_x1489_93403_1422216897}[地址描述符长度]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-45 ]{lang="EN-US"}[debugging fip-snooping packet]{lang="EN-US"}]{#struct_0_x1489_93403_755780323}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1483337965}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1303752384}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_567556683}

[[Received a packet with invalid socket header and discarded it.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111274}

[[接收到并抛弃]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1489_93403_1492397103}[头无效的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received VLAN Notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x246493845}

[[接收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x431776585}[通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received packet of unknown type.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176810}

[[接收到未知类型的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2050720969}

[[VLAN *vlan-id*, interface *Interface-name*, Received a packet with incorrect length]{lang="EN-US"}]{#struct_0_x1489_93403_2077498302}

[[接收到长度错误的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1597537230}

[[VLAN *vlan-id*, Sent the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242346}

[[发送报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x673684081}

[[VLAN *vlan-id*, Sent VLAN Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1457924812}

[[发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1918760443}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*,  Sent VLAN Notification packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783594}

[[发送]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1489_93403_1045760828}[通告报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received unsolicited multicast Discovery Advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1332329609}

[[接收到组播非请求发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1816849130}

[[VLAN *vlan-id*, Sent Discovery Advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1584245256}

[[发送发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1859928385}

[[VLAN *vlan-id*, interface *Interface-name*, Received multicast Discovery Solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1247665037}

[[收到组播发现请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1817307885}

[[VLAN *vlan-id*, Sent multicast Discovery Solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2025772639}

[[发送组播发现请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1507782537}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded a packet for the source interface state was invalid.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817373421}

[[丢弃源接口状态无效的报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_280752070}

[[VLAN *vlan-id*, interface *Interface-name*, Sent unicast Discovery Solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1949493364}

[[发送单播发现请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1817438957}

[[VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1989117423}

[[发送虚链路实例化请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_2050518039}

[[VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817504493}

[[发送虚链路实例化]{style="font-family:宋体"}[ACC]{lang="EN-US"}]{#struct_0_x1489_93403_1341100533}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGI ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_513229750}

[[接收到]{style="font-family:宋体"}[FLOGI ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1806129528}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Sent FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045741}

[[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1662569138}[保活报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received ENode FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111277}

[[接收到]{style="font-family:宋体"}[ENode FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1236486252}[保活报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received a packet with invalid source MAC and discarded it.]{lang="EN-US"}]{#struct_0_x1489_93403_967705643}

[[接收并丢弃源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176813}[无效的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received a packet with invalid destination MAC and discarded it.]{lang="EN-US"}]{#struct_0_x1489_93403_1840961800}

[[接收并丢弃目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_574011210}[无效的报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, Sent Virtual Link Instantiation Reply packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242349}

[[发送虚链路实例化应答报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_2055199274}

[[VLAN *vlan-id*, interface *Interface-name*, Sent Virtual Link Instantiation Reply packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783597}

[[发送虚链路实例化应答报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x520323113}

[[VLAN *vlan-id*, interface *Interface-name*, Received VN_Port FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_616849126}

[[接收到]{style="font-family:宋体"}[VN_Port FIP]{lang="EN-US"}]{#struct_0_x1489_93403_x1816849133}[保活报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received unicast Discovery Solicitation packet.]{lang="EN-US"}]{#struct_0_x1489_93403_18161315}

[[接收单播发现请求报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_1548976334}

[[VLAN *vlan-id*, interface *Interface-name*, Received solicited unicast Discovery Advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817307884}

[[接收单播请求的发现通告报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_459688698}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGI Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817373420}

[[接收]{style="font-family:宋体"}[FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_1846836011}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FDISC Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_997361451}

[[接收]{style="font-family:宋体"}[FDISC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817438956}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGO Request packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x423033482}

[[接收]{style="font-family:宋体"}[FLOGO]{lang="EN-US"}]{#struct_0_x1489_93403_x1817504492}[请求报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FDISC ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x224983408}

[[接收]{style="font-family:宋体"}[FDISC ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x90349682}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGI RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817045740}

[[接收]{style="font-family:宋体"}[FLOGI RJT]{lang="EN-US"}]{#struct_0_x1489_93403_1066314217}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FDISC RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1817111276}

[[接收]{style="font-family:宋体"}[FDISC RJT]{lang="EN-US"}]{#struct_0_x1489_93403_329597689}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGO ACC packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x177260477}

[[接收]{style="font-family:宋体"}[FLOGO ACC]{lang="EN-US"}]{#struct_0_x1489_93403_x1817176812}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FLOGO RJT packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x887921555}

[[接收]{style="font-family:宋体"}[FLOGO RJT]{lang="EN-US"}]{#struct_0_x1489_93403_x1817242348}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Discarded FIP Clear packet for the destination MAC was All-ENode-MACs]{lang="EN-US"}]{#struct_0_x1489_93403_489115333}

[[丢弃目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_x1816783596}[是]{style="font-family:宋体"}[ALL-ENode-MAC]{lang="EN-US"}[的]{style="font-family:宋体"}[FIP Clear]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Received FIP Clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2086407054}

[[接收]{style="font-family:宋体"}[FIP Clear]{lang="EN-US"}]{#struct_0_x1489_93403_x1816849132}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, Sent FIP Clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1547922626}

[[发送]{style="font-family:宋体"}[FIP Clear]{lang="EN-US"}]{#struct_0_x1489_93403_x1539870617}[报文]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Sent FIP Clear packet.]{lang="EN-US"}]{#struct_0_x1489_93403_561702106}

[[发送]{style="font-family:宋体"}[FIP Clear]{lang="EN-US"}]{#struct_0_x1489_93403_x810057853}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-46 ]{lang="EN-US"}[debugging fip-snooping rule]{lang="EN-US"}]{#struct_0_x1489_93403_561767642}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1503022349}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1967202790}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1275239059}

[[VLAN *vlan-id*, interface *Interface-name*, Prepared to add rule {SA: mac-*address* / *mask length*; DA: *mac-address* / *mask length*}]{lang="EN-US"}]{#struct_0_x1489_93403_x1994908711}

[[准备添加规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1191404938}

[[VLAN *vlan-id*, interface *Interface-name*, Prepared to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_561833178}

[[准备删除规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_197820336}

[[VLAN *vlan-id*, interface *Interface-name*, Began to add rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_1992010214}

[[开始添加规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_x44148564}

[[VLAN *vlan-id*, interface *Interface-name*, Began to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_561898714}

[[开始删除规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1811126352}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to add rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_1767318411}

[[添加规则失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_561439962}

[[VLAN *vlan-id*, interface *Interface-name*, Successfully added rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_x1142741890}

[[成功添加规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_x515062160}

[[VLAN *vlan-id*, interface *Interface-name*, Successfully deleted rule {SA: *mac-address* / *mask length*, DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_x1905661824}

[[成功删除规则]{style="font-family:宋体"}]{#struct_0_x1489_93403_561505498}

[[VLAN *vlan-id*, interface *Interface-name*, Failed to delete rule {SA: *mac-address* / *mask length*; DA: *mac-address* / *mask length*}.]{lang="EN-US"}]{#struct_0_x1489_93403_115132052}

[[删除规则失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1960912182}

[[Received terminal event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1898103837}

[[收到终端事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_561571034}

[ ]{lang="EN-US"}

[[表1-47 ]{lang="EN-US"}[debugging fip-snooping session]{lang="EN-US"}]{#struct_0_x1489_93403_x307432245}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1504058509}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x866777040}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_561636570}

[[VLAN *vlan-id*, interface *Interface-name*, Added MAC *mac-address* to {FCFs}.]{lang="EN-US"}]{#struct_0_x1489_93403_x69119468}

[[添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1489_93403_1298528261}[到]{style="font-family:宋体"}[{FCFs}]{lang="EN-US"}

[[VLAN *vlan-id*, interface *Interface-name*, Deleted MAC *mac-address* from {FCFs}.]{lang="EN-US"}]{#struct_0_x1489_93403_x457854164}

[[从]{style="font-family:宋体"}[{FCFs}]{lang="EN-US"}]{#struct_0_x1489_93403_562226394}[删除]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[VLAN *vlan-id*, interface *Interface-name*, Refreshed ENode temp session with exchange *exchange-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x572358422}

[[刷新]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x1434428061}[临时会话，]{style="font-family:宋体"}[exchange]{lang="EN-US"}[为]{style="font-family:宋体"}*[exchange-id]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Added ENode temp session with exchange *exchange-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_1425160046}

[[添加]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_562291930}[临时会话，]{style="font-family:宋体"}[exchange]{lang="EN-US"}[为]{style="font-family:宋体"}*[exchange-id]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Deleted ENode temp session with exchange *exchange-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_521943879}

[[删除]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_439785844}[临时会话，]{style="font-family:宋体"}[exchange]{lang="EN-US"}[为]{style="font-family:宋体"}*[exchange-id]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Refreshed ENode FLOGI session with VN_Port MAC *mac-address*.]{lang="EN-US"}]{#struct_0_x1489_93403_561702107}

[[刷新]{style="font-family:宋体"}[ENode FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x810057852}[会话，]{style="font-family:宋体"}[VN_Port MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Added ENode FLOGI session with VN_Port MAC *mac-address.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1843640753}

[[添加]{style="font-family:宋体"}[ENode FLOGI ]{lang="EN-US"}]{#struct_0_x1489_93403_561767643}[会话，]{style="font-family:宋体"}[VN_Port MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Deleted ENode FLOGI session with VN_Port MAC *mac-address.*]{lang="EN-US"}]{#struct_0_x1489_93403_x1967202789}

[[删除]{style="font-family:宋体"}[ENode FLOGI]{lang="EN-US"}]{#struct_0_x1489_93403_x1809940192}[会话，]{style="font-family:宋体"}[VN_Port MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Refreshed FCF session with FCF-MAC *mac-address.*]{lang="EN-US"}]{#struct_0_x1489_93403_561833179}

[[刷新]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_197820335}[会话，]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Refreshed ]{lang="EN-US"}]{#struct_0_x1489_93403_1992010215}[]{#OLE_LINK22}[[to-be-reflushed ]{lang="EN-US"}]{#OLE_LINK21}[ENode rule with []{#OLE_LINK20}[VN_Port MAC]{#OLE_LINK19} *mac-address.*]{lang="EN-US"}

[[刷新]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x44214100}[正在下刷的规则，]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[[VLAN *vlan-id*, interface *Interface-name*, Refreshed to-be-reflushed FCF rule with FCF-MAC *mac-address.*]{lang="EN-US"}]{#struct_0_x1489_93403_561898715}

[[刷新]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x1811126353}[正在下刷的规则，]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-48 ]{lang="EN-US"}[debugging fip-snooping timer]{lang="EN-US"}]{#struct_0_x1489_93403_x961564944}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1501208781}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_561439963}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1142741891}

[[VLAN *vlan-id*, interface *Interface-name*, Created FCF maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x2081146101}

[[创建]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_491080034}[维护定时器]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Deleted FCF maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_561505499}

[[删除]{style="font-family:宋体"}[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_115132053}[维护定时器]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, FCF maintenance timer timed out with FCF-MAC *mac-address*.]{lang="EN-US"}]{#struct_0_x1489_93403_1960912183}

[[FCF]{lang="EN-US"}]{#struct_0_x1489_93403_x1898169373}[维护定时器超时]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Age timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_561571035}

[[Age]{lang="EN-US"}]{#struct_0_x1489_93403_x307432246}[定时器超时]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Created ENode maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x866580432}

[[创建]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_688202020}[维护定时器]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, Deleted ENode maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_561636571}

[[删除]{style="font-family:宋体"}[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_x69119469}[维护定时器]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, ENode maintenance timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_1298528260}

[[ENode]{lang="EN-US"}]{#struct_0_x1489_93403_562226395}[维护定时器超时]{style="font-family:宋体"}

[[VLAN *vlan-id*, interface *Interface-name*, VN maintenance timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x572358421}

[[VN]{lang="EN-US"}]{#struct_0_x1489_93403_x1434624669}[维护定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_179821644}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_562291931}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[的错误调试信息开关。当]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[接口时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping error]{lang="EN-US"}]{#struct_0_x1489_93403_521943878}

[\*Aug 15 14:30:08:413 2012 Sysname FIPS/7/ERROR: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Failed to find outgoing interface for the packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_439785845}*[未找到报文转发出接口]{style="font-family:宋体"}*

[[\*Aug 15 14:30:08:419 2012 Sysname FIPS/7/ERROR: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Discarded a packet from FCF for the source and destination MAC addresses were both FCF-MAC.]{lang="EN-US"}]{#struct_0_x1489_93403_x864969369}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x338890394}*[丢弃]{style="font-family:宋体"}[FCF]{lang="EN-US"}[端口收到的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[为]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[的报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x835394786}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[的事件调试信息开关。当删除]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping event]{lang="EN-US"}]{#struct_0_x1489_93403_561702104}

[\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, interface GigabitEthernet1/0/1, Received a VLAN event for deleting the interface from the VLAN.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x810057855}*[接收接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[离开]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, interface GigabitEthernet1/0/2, Received a VLAN event for deleting the interface from the VLAN.]{lang="EN-US"}]{#struct_0_x1489_93403_x1843444145}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x159971528}*[接收接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[离开]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Aug 15 14:21:06:778 2012 Sysname FIPS/7/EVENT: -MDC=1; VLAN 3, Received deleting VLAN event.]{lang="EN-US"}]{#struct_0_x1489_93403_622100049}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x954329500}*[接收删除]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_561767640}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[报文调试信息开关。当]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[内]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[下规则成功后会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping packet]{lang="EN-US"}]{#struct_0_x1489_93403_x1967202788}

[\*Aug 15 14:42:33:108 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Received unsolicited multicast Discovery Advertisement packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_918943163}*[接收到组播非请求发现通告报文]{style="font-family:宋体"}*

[[\*Aug 15 14:42:33:108 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, Sent Discovery Advertisement packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2035026226}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1011359590}*[发送发现通告报文]{style="font-family:宋体"}*

[[\*Aug 15 14:42:33:188 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Received ENode FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_350827902}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x841468774}*[收到]{style="font-family:宋体"}[ENode FIP]{lang="EN-US"}[保活报文]{style="font-family:宋体"}*

[[\*Aug 15 14:42:33:188 2012 Sysname FIPS/7/PACKET: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Sent FIP Keep Alive packet.]{lang="EN-US"}]{#struct_0_x1489_93403_561833176}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_197820322}*[发送]{style="font-family:宋体"}[FIP]{lang="EN-US"}[保活报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x346641950}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[的规则调试信息开关。当]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[配置完成后]{style="font-family:宋体"}[shutdown ENode]{lang="EN-US"}[模式的接口会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping rule]{lang="EN-US"}]{#struct_0_x1489_93403_x1407416786}

[\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Prepared to delete rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1462840302}*[准备删除规则]{style="font-family:宋体"}*

[[\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Began to delete rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.]{lang="EN-US"}]{#struct_0_x1489_93403_1019291347}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_561898712}*[开始删除规则]{style="font-family:宋体"}*

[[\*Aug 15 14:38:10:785 2012 Sysname FIPS/7/RULE: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Successfully deleted rule {SA:0efc-0001-0001/48; DA:0000-1234-0a01/48}.]{lang="EN-US"}]{#struct_0_x1489_93403_x1811126346}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x201984521}*[成功删除规则]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x699284431}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[会话调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。当]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[下]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[下规则成功会一直输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping sessions]{lang="EN-US"}]{#struct_0_x1489_93403_x1982728211}

[[\*Aug 15 14:35:34:510 2012 Sysname FIPS/7/SESSION: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Refreshed FCF session with FCF-MAC 0000-1234-0a01.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1489_93403_x998536745}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1229123776}*[以]{style="font-family:宋体"}[FCF-MAC]{lang="EN-US"}[刷新]{style="font-family:宋体"}[FCF]{lang="EN-US"}[会话]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_561439960}[打开]{style="font-family:宋体"}[FIP Snooping]{lang="EN-US"}[的定时器调试信息开关。当端口物理连接]{style="font-family:宋体"}[down]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging fip-snooping timer]{lang="EN-US"}]{#struct_0_x1489_93403_x1142741888}

[\*Aug 15 14:09:07:591 2012 Sysname FIPS/7/TIMER: -MDC=1; VLAN 10, interface GigabitEthernet1/0/2, Deleted ENode maintenance timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x871226984}*[删除接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的]{style="font-family:宋体"}[ENode]{lang="EN-US"}[维护定时器]{style="font-family:宋体"}*

[[\*Aug 15 14:09:07:592 2012 Sysname FIPS/7/TIMER: -MDC=1; VLAN 10, interface GigabitEthernet1/0/1, Deleted FCF maintenance timer.]{lang="EN-US"}]{#struct_0_x1489_93403_807320951}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_596063584}*[删除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[FCF]{lang="EN-US"}[维护定时器]{style="font-family:宋体"}*

::: {#-1072839551 .myid}
[]{#_Toc404797595}[]{#struct_0_x1489_93403_x1871279463}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging fspf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_561505496}

[**[debugging fspf]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **flood \| ha \| lsr** \| **packet \| spf \| timer** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_115132042}

[**[undo debugging fspf]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **flood \| ha \| lsr** \| **packet \| spf \| timer** } \[ **vsan** *vsan-id* \]]{lang="EN-US"}]{#struct_0_x1489_93403_4597046}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_114438531}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_1554834985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1284484700}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1587080486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_561571032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x307432251}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x866514897}[：]{style="font-family:宋体"}[表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_708899738}[：]{style="font-family:宋体"}[表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_649968798}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[flood]{lang="EN-US"}**]{#struct_0_x1489_93403_x1478119787}[：表示]{style="font-family:宋体"}[LSR]{lang="EN-US"}[泛洪调试信息开关。]{style="font-family:宋体"}

[**[ha]{lang="EN-US"}**]{#struct_0_x1489_93403_1935660145}[：表示高可靠性调试信息开关。]{style="font-family:宋体"}

[**[lsr]{lang="EN-US"}**]{#struct_0_x1489_93403_561636568}[：表示]{style="font-family:宋体"}[LSR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_1887195676}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_x1489_93403_x567361955}**[：]{style="font-family:宋体"}**[表示路由计算调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x1489_93403_1632015768}[：表示定时器调试信息开关。]{style="font-family:宋体"}

[**[vsan]{lang="EN-US"}**[ *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1511050777}[：表示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[vsan-id]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3839]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1671101141}

[**[debugging fspf]{lang="EN-US"}**]{#struct_0_x1489_93403_562226392}[命令用来打开]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging fspf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x572358420}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-49 ]{lang="EN-US"}[debugging fspf error]{lang="EN-US"}]{#struct_0_x1489_93403_x1434559133}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1493206733}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_249189938}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1248448071}

[[Failed to create VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_562291928}

[[创建]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x1816708289}[失败]{style="font-family:宋体"}

[[Failed to process domain-change event because VSAN *vsan-id* does not exist.]{lang="EN-US"}]{#struct_0_x1489_93403_362021896}

[[由于]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x91435023}[不存在，处理]{style="font-family:宋体"}[domain]{lang="EN-US"}[变化事件失败]{style="font-family:宋体"}

[[The checksum of the LSR is incorrect, and it should be *number* instead of *number.*]{lang="EN-US"}]{#struct_0_x1489_93403_561702105}

[[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x810057854}[校验和不正确]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to process link-up event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1843509681}

[[处理链路]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x1489_93403_971221061}[事件失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-50 ]{lang="EN-US"}[debugging fspf event]{lang="EN-US"}]{#struct_0_x1489_93403_664303}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1497022701}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_561767641}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1967202787}

[[VSAN *vsan-id*, successfully flushed LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x647140778}

[[刷新]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_866455751}[成功]{style="font-family:宋体"}

[[VSAN *vsan-id*, the flag for generating LSR is cleaned up.]{lang="EN-US"}]{#struct_0_x1489_93403_561833177}

[[清除生成]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_197820321}[的标记]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to generate a new LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x346641949}

[[生成新的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1407875537}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to flush LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_561898713}

[[刷新]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1811126347}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, successfully generated a new LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_1364099420}

[[生成新的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_1906385809}[成功]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to generate a new LSR because the interval is less than Min_Ls_Interval.]{lang="EN-US"}]{#struct_0_x1489_93403_561439961}

[[由于时间间隔小于最小时间间隔，生成新的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1142741889}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id,* set up the flag for generating LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_1857656371}

[[设置生成]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_561505497}[的标记]{style="font-family:宋体"}

[[VSAN *vsan-id*, successfully installed the LSR which is the same as local LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_115132043}

[[成功安装与本地相同的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_4597047}

[[VSAN *vsan-id*, successfully installed the LSR and calculated route.]{lang="EN-US"}]{#struct_0_x1489_93403_1680522472}

[[成功安装]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_561571033}[，并且触发路由计算]{style="font-family:宋体"}

[[VSAN *vsan-id*, the incarnation reaches the maximal number and the LSR will be flushed.]{lang="EN-US"}]{#struct_0_x1489_93403_x307432252}

[[incarnation]{lang="EN-US"}]{#struct_0_x1489_93403_x866318289}[达到最大值，刷新该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[Received VSAN *vsan-id* creation event.]{lang="EN-US"}]{#struct_0_x1489_93403_561636569}

[[收到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_1887195675}[创建事件]{style="font-family:宋体"}

[[Received VSAN *vsan-id* deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_x567427491}

[[收到]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_562226393}[删除事件]{style="font-family:宋体"}

[[VSAN *vsan-id*, received domain-change event from *domain-id1* to *domain-id2*.]{lang="EN-US"}]{#struct_0_x1489_93403_x572358419}

[[收到]{style="font-family:宋体"}[domain]{lang="EN-US"}]{#struct_0_x1489_93403_x1435148956}[变化事件]{style="font-family:宋体"}

[[VSAN *vsan-id*, changed domain from *domain-id1* to *domain-id2*.]{lang="EN-US"}]{#struct_0_x1489_93403_562291929}

[[Domain]{lang="EN-US"}]{#struct_0_x1489_93403_x1816708290}[从一个值变到另一个值]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, received link-up event in E-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x847897221}

[[接口]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_561702102}[模式下收到链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, received link-down event in E-mode.]{lang="EN-US"}]{#struct_0_x1489_93403_x810057849}

[[接口]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_x1843182000}[模式下收到链路]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, received *event-type* event in *state* state.]{lang="EN-US"}]{#struct_0_x1489_93403_561767638}

[[在某种状态下收到某种事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_371449364}

[[VSAN *vsan-id*, interface *Interface-name*, the neighbor entered *state* state.]{lang="EN-US"}]{#struct_0_x1489_93403_1453694809}

[[邻居进入某种状态]{style="font-family:宋体"}]{#struct_0_x1489_93403_561833174}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created the new interface.]{lang="EN-US"}]{#struct_0_x1489_93403_197820324}

[[成功创建新的接口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x346641944}

[[VSAN *vsan-id*, interface *Interface-name*, successfully deleted the interface.]{lang="EN-US"}]{#struct_0_x1489_93403_561898710}

[[成功删除接口]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1811126348}

[[VSAN *vsan-id*, interface *Interface-name*, reset the neighbor and initialized the neighbor structure.]{lang="EN-US"}]{#struct_0_x1489_93403_x1721014295}

[[重启邻居并且初始化邻居结构]{style="font-family:宋体"}]{#struct_0_x1489_93403_561439958}

[[Interface *Interface-name*, received the baud rate change event.]{lang="EN-US"}]{#struct_0_x1489_93403_1578247304}

[[收到波特率变化事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_561505494}

[[Interface *Interface-name*, received interface deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_115132040}

[[收到接口删除事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_4597044}

[[Interface *Interface-name*, received interface deactivation event.]{lang="EN-US"}]{#struct_0_x1489_93403_561571030}

[[收到接口去激活事件]{style="font-family:宋体"}]{#struct_0_x1489_93403_x307432249}

[[VSAN *vsan-id*, failed to enable FSPF.]{lang="EN-US"}]{#struct_0_x1489_93403_561636566}

[[使能]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_1887195662}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, terminated new LSR generation because of Graceful Restart.]{lang="EN-US"}]{#struct_0_x1489_93403_x567099812}

[[由于平滑重启，终止新的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_562226390}[生成]{style="font-family:宋体"}

[ ]{lang="EN-US" style="background:white"}

[[表1-51 ]{lang="EN-US"}[debugging fspf flood]{lang="EN-US"}]{#struct_0_x1489_93403_x572358418}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1518762957}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1435083420}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_2061678044}

[[VSAN *vsan-id*, flooded the LSR with domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_562291926}

[[泛洪]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1816708283}

[ ]{lang="EN-US" style="background:white"}

[[表1-52 ]{lang="EN-US"}[debugging fspf ha]{lang="EN-US"}]{#struct_0_x1489_93403_1881051670}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1521929325}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1337519122}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_561702103}

[[VSAN *vsan-id*, interface *Interface-name*, cleared the flag for Restarter.]{lang="EN-US"}]{#struct_0_x1489_93403_x810057848}

[[清除]{style="font-family:宋体"}[Restarter]{lang="EN-US"}]{#struct_0_x1489_93403_x1843247536}[标志]{style="font-family:宋体"}

[[VSAN *vsan-id*, entered GR Restarter role.]{lang="EN-US"}]{#struct_0_x1489_93403_x415931123}

[[进入]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}]{#struct_0_x1489_93403_561767639}[角色]{style="font-family:宋体"}

[[VSAN *vsan-id*, exited from GR Restarter role.]{lang="EN-US"}]{#struct_0_x1489_93403_371449365}

[[退出]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}]{#struct_0_x1489_93403_1453694810}[角色]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, originating Domain_ID field of FSPF header is different from the locally saved one, and failed to enter GR Helper role.]{lang="EN-US"}]{#struct_0_x1489_93403_1380864610}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_561833175}[头中]{style="font-family:宋体"}[originating Domain_ID]{lang="EN-US"}[字段和本地保存不一致，不能进入]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[角色]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, set up the flag for Restarter.]{lang="EN-US"}]{#struct_0_x1489_93403_197820323}

[[设置]{style="font-family:宋体"}[Restarter]{lang="EN-US"}]{#struct_0_x1489_93403_x346641951}[标志]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, cleared the flag for Helper.]{lang="EN-US"}]{#struct_0_x1489_93403_x1407351250}

[[清除]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_x1489_93403_561898711}[标志]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, set up the flag for Helper.]{lang="EN-US"}]{#struct_0_x1489_93403_x1811126349}

[[设置]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_x1489_93403_x154930354}[标志]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, neighbor state was not full, and failed to enter GR Helper role.]{lang="EN-US"}]{#struct_0_x1489_93403_561439959}

[[邻居状态非]{style="font-family:宋体"}[full]{lang="EN-US"}]{#struct_0_x1489_93403_1578247303}[，不能进入]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[角色]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, already in GR Helper role.]{lang="EN-US"}]{#struct_0_x1489_93403_x752845745}

[[已经是]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_x1489_93403_1012116481}[角色]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, GR Helper was not enabled, and failed to enter GR Helper role.]{lang="EN-US"}]{#struct_0_x1489_93403_561505495}

[[GR Helper]{lang="EN-US"}]{#struct_0_x1489_93403_115132041}[没有使能，不能进入]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[角色]{style="font-family:宋体"}

[ ]{lang="EN-US" style="background:white"}

[[表1-53 ]{lang="EN-US"}[debugging fspf lsr]{lang="EN-US"}]{#struct_0_x1489_93403_4597045}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1514437005}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1451645410}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_561571031}

[[VSAN *vsan-id*, cleared all LSR in LSDB.]{lang="EN-US"}]{#struct_0_x1489_93403_x307432250}

[[清除链路状态数据库中所有的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x866449361}

[[VSAN *vsan-id*, added a LSR to LSDB: Link State Identifier is *domain-id*, Number of Links is *number.*]{lang="EN-US"}]{#struct_0_x1489_93403_698413325}

[[向链路状态数据库中添加一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_561636567}[，链路状态标识符为]{style="font-family:宋体"}[LSR]{lang="EN-US"}[所属交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，链路数量为]{style="font-family:宋体"}[LSR]{lang="EN-US"}[中包含]{style="font-family:宋体"}[link]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[[VSAN *vsan-id*, Link ID is *number*, Output Port is *Interface-name*, Neighbor Port is *Interface-name*, Link Cost is n*umber*.]{lang="EN-US"}]{#struct_0_x1489_93403_1887195661}

[[Link ID]{lang="EN-US"}]{#struct_0_x1489_93403_x567165348}[为对端交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[Output Port]{lang="EN-US"}[为源接口索引，]{style="font-family:宋体"}[Neighbor port]{lang="EN-US"}[为目的端接口索引，]{style="font-family:宋体"}[Link Cost]{lang="EN-US"}[为链路的开销]{style="font-family:宋体"}

[[VSAN *vsan-id*, deleted a LSR from LSDB: Link State Identifier is *domain-id*, Number of Links is *number.*]{lang="EN-US"}]{#struct_0_x1489_93403_2045601731}

[[从链路状态数据库中删除一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_562226391}[，链路状态标识符为]{style="font-family:宋体"}[LSR]{lang="EN-US"}[所属交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[，链路数量为]{style="font-family:宋体"}[LSR]{lang="EN-US"}[中包含]{style="font-family:宋体"}[link]{lang="EN-US"}[的个数]{style="font-family:宋体"}

[[VSAN *vsan-id*, the LSR not in LSDB: Link State Identifier is *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x572358417}

[[链路状态数据库中不存在该]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1434231452}[，链路状态标识符为]{style="font-family:宋体"}[LSR]{lang="EN-US"}[所属交换机的域]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully added a LSR to acklist with domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_562291927}

[[成功向]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x1489_93403_x1816708284}[列表中添加一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully added a LSR to retrlist with domain *domain-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1121536783}

[[成功向重传列表添加一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127786047}

[ ]{lang="EN-US"}

[[表1-54 ]{lang="EN-US"}[debugging fspf packet]{lang="EN-US"}]{#struct_0_x1489_93403_x630112754}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1516468333}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1894855872}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_192389588}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Failed to find FSPF interface by VSAN and interface index, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x598092529}

[[根据]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2127851583}[和接口索引查找不到]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[接口信息，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name, packet-type* Receive: Neighbor state is down, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_160406266}

[[邻居状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1489_93403_x1208730951}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: SID field of FC header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x258514656}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_2127917119}[头的]{style="font-family:宋体"}[SID]{lang="EN-US"}[字段错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: DID field of FC header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x229723782}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x1905172652}[头的]{style="font-family:宋体"}[DID]{lang="EN-US"}[字段错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of FSPF header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1527374402}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_2127982655}[头长度错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Command field of FSPF header is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_548605767}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x1016937412}[头的命令字段不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Version field of FSPF header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127523903}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x658274989}[头的版本字段错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Authentication Type field of FSPF header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1575018638}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x913132795}[头的认证类型错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127589439}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x1441447694}[头的源]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[字段不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header conflicts with local Domain_ID, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_783337758}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_2127654975}[头的源]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[和本地]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[有冲突，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Originating Domain_ID field of FSPF header is different from the locally saved one, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1694520632}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x488351734}[头的源]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[和本地保存的]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[不同，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Authentication field of FSPF header is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127720511}

[[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_1745823551}[头的认证字段错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of hello packet is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x440676809}

[[Hello]{lang="EN-US"}]{#struct_0_x1489_93403_2128310335}[报文长度错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Recipient Domain_ID field of 2-way hello packet is invalid, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1980946755}

[[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_916912258}[报文的]{style="font-family:宋体"}[Recipient Domain_ID]{lang="EN-US"}[字段不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Hello_Interval field of hello packet mismatches the local Hello_Interval, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2128375871}

[[Hello]{lang="EN-US"}]{#struct_0_x1489_93403_x2009216792}[报文的]{style="font-family:宋体"}[Hello_Interval]{lang="EN-US"}[不匹配本地的]{style="font-family:宋体"}[Hello_Interval]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Dead_Interval field of hello packet mismatches the local Dead_Interval, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2039014520}

[[Hello]{lang="EN-US"}]{#struct_0_x1489_93403_2127786048}[报文的]{style="font-family:宋体"}[Dead_Interval]{lang="EN-US"}[不匹配本地的]{style="font-family:宋体"}[Dead_Interval]{lang="EN-US"}[，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name, packet-type* Receive: Originating Domain_ID field of 2-way hello is different from the locally save one, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x629785074}

[[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_1308861354}[报文的源]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[和本地保存的]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[不相等，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Originating Port Index field of 2-way hello is different from the locally saved one, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127851584}

[[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_160078586}[报文的源端口索引和本地保存的不相等，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Recipient Domain_ID field of 2-way hello is different from local Domain_ID, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127917120}

[[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_x229133959}[报文的]{style="font-family:宋体"}[Recipient Domain_ID]{lang="EN-US"}[和本地的]{style="font-family:宋体"}[ Domain_ID]{lang="EN-US"}[不相等，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of LSU packet is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_4152995}

[[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_2127982656}[报文的长度错误，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Flags filed of LSU packet mismatches the Number of LSRs field, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_548409159}

[[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x517154032}[报文的]{style="font-family:宋体"}[flags]{lang="EN-US"}[标记不匹配]{style="font-family:宋体"}[LSR]{lang="EN-US"}[的数量，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: The length of LSA packet is incorrect, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127523904}

[[LSA]{lang="EN-US"}]{#struct_0_x1489_93403_x658733741}[报文的长度不合法，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name,* *packet-type* Receive: Flags filed of LSA packet mismatches the Number of LSRs field, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127589440}

[[LSA]{lang="EN-US"}]{#struct_0_x1489_93403_x1442037511}[报文的]{style="font-family:宋体"}[flags]{lang="EN-US"}[标记不匹配]{style="font-family:宋体"}[LSR]{lang="EN-US"}[数量，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Neighbor state was init, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x317632840}

[[邻居状态是]{style="font-family:宋体"}[init]{lang="EN-US"}]{#struct_0_x1489_93403_2127654976}[状态，丢弃报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Memory was not enough to complete the operation.]{lang="EN-US"}]{#struct_0_x1489_93403_1694717240}

[[没有足够的内存去完成操作]{style="font-family:宋体"}]{#struct_0_x1489_93403_2127720512}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 1-way Hello packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1745889087}

[[成功收到]{style="font-family:宋体"}[1-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_x1621140408}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 1-way hello packet with GR flag.]{lang="EN-US"}]{#struct_0_x1489_93403_2128310336}

[[成功收到带有]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1489_93403_x1980750147}[标志的]{style="font-family:宋体"}[1-way hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received initialized LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2128375872}

[[成功收到初始化的]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x2009282328}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received LSA with LSR headers packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1527498249}

[[成功收到带有]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127786045}[头的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Packet Receive: The input interface index is invalid.]{lang="EN-US"}]{#struct_0_x1489_93403_x629981682}

[[入接口索引无效]{style="font-family:宋体"}]{#struct_0_x1489_93403_2127851581}

[[Packet Receive: VSAN ID is invalid.]{lang="EN-US"}]{#struct_0_x1489_93403_160275194}

[[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_2127917117}[无效]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 1-way hello packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x228806278}

[[成功发送]{style="font-family:宋体"}[1-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_2127982653}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 1-way hello packet with GR flag.]{lang="EN-US"}]{#struct_0_x1489_93403_548212551}

[[成功发送带有]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1489_93403_22130007}[标志的]{style="font-family:宋体"}[1-way hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to create socket.]{lang="EN-US"}]{#struct_0_x1489_93403_2127523901}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1489_93403_x658406061}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to bind the socket.]{lang="EN-US"}]{#struct_0_x1489_93403_2127589437}

[[绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1489_93403_x1441840910}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to add to epoll.]{lang="EN-US"}]{#struct_0_x1489_93403_2127654973}

[[加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x1489_93403_1694913848}[失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 2-way hello packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127720509}

[[成功发送]{style="font-family:宋体"}[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_1745299264}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent 2-way hello packet with GR flag.]{lang="EN-US"}]{#struct_0_x1489_93403_2128310333}

[[成功发送带有]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1489_93403_x1981077827}[标志的]{style="font-family:宋体"}[2-way hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Failed to send the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2128375869}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2008692503}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 2-way hello packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127786046}

[[成功接收]{style="font-family:宋体"}[2-way hello]{lang="EN-US"}]{#struct_0_x1489_93403_x630178290}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received 2-way hello packet with GR flag.]{lang="EN-US"}]{#struct_0_x1489_93403_2127851582}

[[成功接收带有]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x1489_93403_2127917118}[标志的]{style="font-family:宋体"}[2-way hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received empty LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x229658246}

[[成功接收空]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_2127982654}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received update LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_548540231}

[[成功接收更新]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_2127523902}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully checked a received LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x658340525}

[[检查接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127589438}[成功]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, Length field of a received LSR is invalid, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x1441513230}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127654974}[长度不合法，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Checksum field of a received LSR is incorrect, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_1694586168}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127720510}[校验和错误，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, LSR type field of a received LSR is incorrect, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_1745758015}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2128310334}[类型错误，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR is invalid, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x1980881219}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2128375870}[链路状态字段不合法，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Advertising Domain_ID field of a received LSR is invalid, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x2009151256}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127786043}[通告]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[不合法，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR does not equal Advertising Domain_ID field, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x630374898}

[[接收]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127851579}[的链路状态字段不等于通告]{style="font-family:宋体"}[Domain_ID]{lang="EN-US"}[，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, LSR Age field of a received LSR is invalid, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_160799481}

[[接收的]{style="font-family:宋体"}[LSR age]{lang="EN-US"}]{#struct_0_x1489_93403_2127917115}[字段不合法，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Incarnation Number field of a received LSR is invalid, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x228937350}

[[接收的]{style="font-family:宋体"}[LSR Incarnation Numbe ]{lang="EN-US"}]{#struct_0_x1489_93403_2127982651}[字段不合法，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Number of LSR links of a received LSR mismatches LSR Length field, and discarded the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_2127523899}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_1679721802}[数量不匹配]{style="font-family:宋体"}[LSR]{lang="EN-US"}[长度，丢弃该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent initialized LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127589435}

[[成功发送初始化的]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x1441709838}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent empty LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127654971}

[[成功发送空的]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_2127720507}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent updated LSU packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1745692480}

[[成功发送更新的]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_2128310331}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent LSA with LSR headers packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x1981208899}

[[成功发送带有]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2128375867}[头的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Send: Successfully sent empty LSA packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2009610007}

[[成功发送空的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x1489_93403_2127786044}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, *packet-type* Receive: Successfully received empty LSA packet.]{lang="EN-US"}]{#struct_0_x1489_93403_2127851580}

[[成功接收空的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x1489_93403_160340730}[报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully checked a received LSR header.]{lang="EN-US"}]{#struct_0_x1489_93403_2127917116}

[[成功检查接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x228740742}[头]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, LSR type field of a received LSR header is incorrect, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_2127982652}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127523900}[头中]{style="font-family:宋体"}[LSR]{lang="EN-US"}[类型不正确，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR header is invalid, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x658471597}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127589436}[头中]{style="font-family:宋体"}[Link State Identifier]{lang="EN-US"}[字段不合法，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Advertising Domain_ID field of a received LSR header is invalid, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x1441906446}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2127654972}[头中]{style="font-family:宋体"}[Advertising Domain_ID]{lang="EN-US"}[字段不正确，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Link State Identifier field of a received LSR header does not equal Advertising Domain_ID field, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_2127720508}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2128310332}[头中]{style="font-family:宋体"}[Link State Identifier]{lang="EN-US"}[字段和]{style="font-family:宋体"}[Advertising Domain_ID]{lang="EN-US"}[字段不相等，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, LSR Age field of a received LSR header is invalid, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x1981012291}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_2128375868}[头中]{style="font-family:宋体"}[LSR Age]{lang="EN-US"}[字段不合法，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, Incarnation Number field of a received LSR header is invalid, and ignored the LSR.]{lang="EN-US"}]{#struct_0_x1489_93403_x601097308}

[[接收的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_1727942222}[头中]{style="font-family:宋体"}[Incarnation Number]{lang="EN-US"}[字段不合法，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}

[[VSAN *vsan-id*, interface *Interface-name*, packet-type Receive: Received empty LSA without having sent empty LSU, and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x601031772}

[[没有发送空]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x179346153}[报文却接收空]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文，丢弃该报文]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, the LSR is ignored because the interval is less than Min_LS_Arrival]{lang="EN-US"}]{#struct_0_x1489_93403_x600966236}

[[接收间隔值没有达到最小间隔值，忽略该]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x600900700}

[ ]{lang="EN-US" style="background:white"}

[[表1-55 ]{lang="EN-US"}[debugging fspf spf]{lang="EN-US"}]{#struct_0_x1489_93403_217969094}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1535099949}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1055271116}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_725463223}

[[VSAN *vsan-id*, interface *Interface-name*, *operate-type* a route: domain *domain-id.*]{lang="EN-US"}]{#struct_0_x1489_93403_x601359452}

[[改变路由，操作类型取值为：]{style="font-family:宋体"}[add]{lang="EN-US"}]{#struct_0_x1489_93403_2137262734}[（添加）、]{style="font-family:宋体"}[modify]{lang="EN-US"}[（修改）、]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to notify FSPF route.]{lang="EN-US"}]{#struct_0_x1489_93403_x473173619}

[[通知]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x504072552}[路由失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, the hold timer timed out and calculated route.]{lang="EN-US"}]{#struct_0_x1489_93403_x601293916}

[[路由计算间隔定时器超时，计算路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_1785756709}

[[VSAN *vsan-id*, successfully calculated the route.]{lang="EN-US"}]{#struct_0_x1489_93403_x1646960570}

[[成功计算路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_1336718588}

[[VSAN *vsan-id*, the age of local LSR is MAX_AGE, terminated the route calculation.]{lang="EN-US"}]{#struct_0_x1489_93403_x601228380}

[[本地]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x1785424497}[的]{style="font-family:宋体"}[age]{lang="EN-US"}[是最大]{style="font-family:宋体"}[age]{lang="EN-US"}[，结束路由计算]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to alloc memory, terminated the route calculation.]{lang="EN-US"}]{#struct_0_x1489_93403_302619684}

[[申请内存失败，停止路由计算]{style="font-family:宋体"}]{#struct_0_x1489_93403_1560101389}

[[VSAN *vsan-id*, the age of relevant LSR (domain *domain-id*) is MAX_AGE, ignored the Link Descriptor (domain *domain-id)*.]{lang="EN-US"}]{#struct_0_x1489_93403_x601162844}

[[相关]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_1426392996}[的]{style="font-family:宋体"}[age]{lang="EN-US"}[是最大]{style="font-family:宋体"}[age]{lang="EN-US"}[，忽略该链路描述符]{style="font-family:宋体"}

[[VSAN *vsan-id*, the relevant LSR (domain *domain-id*) is nonexistent, ignored the Link Descriptor (domain *domain-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_1643257138}

[[相关]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x600573020}[不存在，忽略该链路描述符]{style="font-family:宋体"}

[[VSAN *vsan-id*, the relevant LSR (domain *domain-id*) has no peer Link Descriptor, ignored the Link Descriptor (domain *domain-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_603356329}

[[相关]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_x436573341}[不存在对称的链路描述符，忽略该链路描述符]{style="font-family:宋体"}

[[VSAN *vsan-id*, the type of peer Link Descriptor (domain *domain-id*) is invalid, ignored the Link Descriptor (domain *domain-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x600507484}

[[对称链路描述符的类型不合法，忽略该链路描述符]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2141892837}

[[VSAN *vsan-id*, the interface index of peer Link Descriptor (domain *domain-id*) is invalid, ignored the Link Descriptor (domain *domain-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x1518688401}

[[对称链路描述符的接口索引不合法，忽略该链路描述符]{style="font-family:宋体"}]{#struct_0_x1489_93403_995111853}

[[VSAN *vsan-id*, the relevant LSR (domain *domain-id*) has been in the spf-list, ignored the Link Descriptor (domain *domain-id*).]{lang="EN-US"}]{#struct_0_x1489_93403_x601097307}

[[相关]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x1489_93403_1728138830}[存在路由计算列表，忽略该链路描述符]{style="font-family:宋体"}

[[VSAN *vsan-id*, immediately calculated the route because the interval reached the hold-time.]{lang="EN-US"}]{#struct_0_x1489_93403_1810552985}

[[间隔时间达到路由计算间隔，计算路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_x601031771}

[[VSAN *vsan-id* , successfully created the hold timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x179411689}

[[成功创建路由计算间隔定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1230991892}

[[VSAN *vsan-id*, failed to create the hold timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x600966235}

[[创建路由计算间隔定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x180036867}

[[VSAN *vsan-id*, terminated the route calculation because of Graceful Restart.]{lang="EN-US"}]{#struct_0_x1489_93403_1430465850}

[[由于平滑重启，终止路由计算]{style="font-family:宋体"}]{#struct_0_x1489_93403_x600900699}

[[VSAN *vsan-id*, calculated a fspf route: domain *domain-id*, interface *Interface-name*, cost *number*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2120224307}

[[计算]{style="font-family:宋体"}[FSPF]{lang="EN-US"}]{#struct_0_x1489_93403_x601359451}[路由]{style="font-family:宋体"}

[[VSAN vsan-id, immediately calculated the route because the interval reached the hold-time.]{lang="EN-US"}]{#struct_0_x1489_93403_2137459342}

[[间隔时间达到路由计算间隔，计算路由]{style="font-family:宋体"}]{#struct_0_x1489_93403_1040202071}

[[VSAN vsan-id , successfully created the hold timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601293915}

[[成功创建路由计算间隔定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_1785953317}

[[VSAN vsan-id, failed to create the hold timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x2008219218}

[[创建路由计算间隔定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x601228379}

[ ]{lang="EN-US" style="background:white"}

[[表1-56 ]{lang="EN-US"}[debugging fspf timer]{lang="EN-US"}]{#struct_0_x1489_93403_x1784965742}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1557214445}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x834743263}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x447981745}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created the retransfer timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601162843}

[[成功创建重传定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_1425934244}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created the hello timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1743560623}

[[成功创建]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x1489_93403_x1302640548}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x600573019}

[[成功创建]{style="font-family:宋体"}[dead]{lang="EN-US"}]{#struct_0_x1489_93403_602897574}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, successfully created the empty LSU timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x2140358347}

[[成功创建]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x600507483}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the retransfer timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x2141565157}

[[创建重传定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1220404959}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the hello timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1807573227}

[[创建]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x1489_93403_x601097310}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1728466511}

[[创建]{style="font-family:宋体"}[dead]{lang="EN-US"}]{#struct_0_x1489_93403_327633446}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, failed to create the empty LSU timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601031774}

[[创建空]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x179215081}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, deleted the retransfer timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1477468070}

[[删除重传定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_x600966238}

[[VSAN *vsan-id*, interface *Interface-name*, deleted the hello timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x180757763}

[[删除]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x1489_93403_x1722572068}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, deleted the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x1441058099}

[[删除]{style="font-family:宋体"}[dead]{lang="EN-US"}]{#struct_0_x1489_93403_x600900702}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, deleted the empty LSU timer.]{lang="EN-US"}]{#struct_0_x1489_93403_218100166}

[[创建空]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_631431058}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, refreshed the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601359454}

[[刷新]{style="font-family:宋体"}[dead]{lang="EN-US"}]{#struct_0_x1489_93403_2137655950}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, successfully created the age timer.]{lang="EN-US"}]{#struct_0_x1489_93403_269926874}

[[成功创建]{style="font-family:宋体"}[age]{lang="EN-US"}]{#struct_0_x1489_93403_x601293918}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, failed to create the age timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1785625637}

[[创建]{style="font-family:宋体"}[age]{lang="EN-US"}]{#struct_0_x1489_93403_297778741}[定时器失败]{style="font-family:宋体"}

[[VSAN *vsan-id*, deleted the age timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601228382}

[[删除]{style="font-family:宋体"}[age]{lang="EN-US"}]{#struct_0_x1489_93403_x1785555569}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, interface *Interface-name*, refreshed the hello timer.]{lang="EN-US"}]{#struct_0_x1489_93403_544733300}

[[刷新]{style="font-family:宋体"}[hello]{lang="EN-US"}]{#struct_0_x1489_93403_x601162846}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, successfully created the restarter timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1426261924}

[[成功创建重启定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_x600573022}

[[VSAN *vsan-id*, failed to create the restarter timer.]{lang="EN-US"}]{#struct_0_x1489_93403_603487401}

[[创建重启定时器失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1327815117}

[[VSAN *vsan-id*, the restarter timer timed out.]{lang="EN-US"}]{#struct_0_x1489_93403_x600507486}

[[重启定时器超时]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2141761765}

[[VSAN *vsan-id*, interface *Interface-name*, refreshed the empty LSU timer.]{lang="EN-US"}]{#struct_0_x1489_93403_598080931}

[[刷新空]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x1489_93403_x601097309}[定时器]{style="font-family:宋体"}

[[VSAN *vsan-id*, deleted the restarter timer.]{lang="EN-US"}]{#struct_0_x1489_93403_1728007758}

[[删除重启定时器]{style="font-family:宋体"}]{#struct_0_x1489_93403_x601031773}

[ ]{lang="EN-US" style="background:white"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x179280617}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1487733212}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf error vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_192938615}

[\*Nov 28 18:46:34:074 2011 Sysname FSPF/7/ERROR: -MDC=1; VSAN 2, interface Vfc2 failed to process link-up event.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1837675830}*[处理链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x600966237}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的]{style="font-family:宋体"}[事件调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf event vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x180167939}

[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/EVENT: -MDC=1; VSAN 2, successfully generated a new LSR.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x2094751177}*[成功生成一个新]{style="font-family:宋体"}[LSR]{lang="EN-US"}*

[[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/EVENT: -MDC=1; VSAN 2, successfully installed the LSR and calculated route.]{lang="EN-US"}]{#struct_0_x1489_93403_659507978}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x132046404}*[成功安装]{style="font-family:宋体"}[LSR]{lang="EN-US"}[，并且计算路由]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1402210183}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[泛洪调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf flood vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x600900701}

[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/FLOOD: -MDC=1; VSAN 2, flooded the LSR with domain 1.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x1489_93403_217903558}*[泛洪]{style="font-family:宋体"}[LSR]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x1620408753}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的高可靠性调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf ha vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x848991235}

[\*Nov 28 18:42:34:629 2011 Sysname FSPF/7/HA: -MDC=1; VSAN 2, interface Fc1/0/1, cleared the flag for Restarter.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1138194867}*[清除]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[标志]{style="font-family:宋体"}*

[[\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/HA: -MDC=1; VSAN 2, interface Fc1/0/1, GR Helper was not enabled, and failed to enter GR Helper role.]{lang="EN-US"}]{#struct_0_x1489_93403_1772791942}

[*[// GR Helper]{lang="EN-US"}*]{#struct_0_x1489_93403_x601359453}*[没有使能，不能进入]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[角色]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_2137328270}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf lsr vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_1831972044}

[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/LSR: -MDC=1; VSAN 2, deleted a LSR from LSDB: Link State Identifier is 1, Number of Links is 1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1381302994}*[从]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中删除一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}[，链路描述符为]{style="font-family:宋体"}[1]{lang="EN-US"}[，链路个数是]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/LSR: -MDC=1; VSAN 2, added a LSR to LSDB: Link State Identifier is 1, Number of Links is 1.]{lang="EN-US"}]{#struct_0_x1489_93403_566331334}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_400859319}*[向]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中添加一条]{style="font-family:宋体"}[LSR]{lang="EN-US"}[，链路描述符为]{style="font-family:宋体"}[1]{lang="EN-US"}[，链路个数是]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_447453798}[配置]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[接口]{style="font-family:宋体"}[up]{lang="EN-US"}[，打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的]{style="font-family:宋体"}[报文调试信息]{style="font-family:宋体"}[开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf packet vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x601293917}

[\*Nov 28 18:10:29:453 2011 Sysname FSPF/7/PACKET: -MDC=1; VSAN 2, interface Fc1/0/1, Hello Send: Successfully sent 1-way hello packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1785822245}*[成功发送]{style="font-family:宋体"}[1-way hello]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov 28 18:10:51:486 2011 Sysname FSPF/7/PACKET: -MDC=1; VSAN 2, interface Fc1/0/1, Hello Receive: Dead_Interval field of hello packet mismatches the local Dead_Interval,and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_1905888567}

[*[// Hello]{lang="EN-US"}*]{#struct_0_x1489_93403_x140458048}*[报文的]{style="font-family:宋体"}[Dead_Interval]{lang="EN-US"}[值不等于本地]{style="font-family:宋体"}[Dead_Interval]{lang="EN-US"}[值，丢弃报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x978143702}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的路由计算调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf spf vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x601228381}

[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/SPF: -MDC=1; VSAN 2, immediately calculated the route because the interval reached the hold-time.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x1785490033}*[时间间隔到达路由计算间隔值，触发路由计算]{style="font-family:宋体"}*

[[\*Nov 28 18:11:42:352 2011 Sysname FSPF/7/SPF: -MDC=1; VSAN 2, successfully calculated the route.]{lang="EN-US"}]{#struct_0_x1489_93403_1036866637}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1250568926}*[成功计算路由]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1211943236}[打开]{style="font-family:宋体"}[VSAN 2 ]{lang="EN-US"}[内]{style="font-family:宋体"}[FSPF]{lang="EN-US"}[模块的定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging fspf timer vsan 2]{lang="EN-US"}]{#struct_0_x1489_93403_x2118343124}

[\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/TIMER: -MDC=1; VSAN 2, interface Fc1/0/1, deleted the retransfer timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1499044361}*[删除重传定时器]{style="font-family:宋体"}*

[[\*Nov 28 18:42:51:486 2011 Sysname FSPF/7/TIMER: -MDC=1; VSAN 2, interface Fc1/0/1, refreshed the dead timer.]{lang="EN-US"}]{#struct_0_x1489_93403_x601162845}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_1426327460}*[刷新]{style="font-family:宋体"}[dead]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

::: {#1028409160 .myid}
[]{#_Toc404797596}[]{#struct_0_x1489_93403_x1371245446}[]{#_Toc350354013}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging san-aggregation**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1371442054}

[**[debugging san-aggregation]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **selection** \| **packet** \[ **receive** \| **send** \] }]{lang="EN-US"}[ \[ **interface** **san-aggregation** *interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1371376518}

[**[undo debugging san-aggregation]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **selection** \| **packet** \[ **receive** \| **send** \] } \[ **interface** **san-aggregation** *interface-number* \]]{lang="EN-US"}]{#struct_0_x1489_93403_x1370983302}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1371179910}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_x1371114374}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x1371835270}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x968026450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x967960914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x968157522}

[**[all]{lang="EN-US"}**]{#struct_0_x1489_93403_x968091986}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1489_93403_x967764306}[：表示]{style="font-family:宋体"}[错误调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1489_93403_x967895378}[：表示]{style="font-family:宋体"}[事件调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[selection]{lang="EN-US"}**]{#struct_0_x1489_93403_x967829842}[：表示成员接口选中调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1489_93403_x968550738}[：表示]{style="font-family:宋体"}[报文调试信息开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x1489_93403_x968485202}[：表示接收报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_x1489_93403_x968026451}[：表示发送报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[interface san-aggregation ]{lang="EN-US"}***[interface]{lang="EN-US"}*[-*number*]{lang="EN-US"}]{#struct_0_x1489_93403_x968157523}[：表示指定]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的调试信息开关。]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[-*number*]{lang="EN-US"}[表示]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的编号。如果未指定本参数，表示所有]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x968091987}

[**[debugging san-aggregation]{lang="EN-US"}**]{#struct_0_x1489_93403_x967764307}[命令用来打开]{style="font-family:
宋体"}[FC]{lang="EN-US"}[聚合组调试信息开关。]{style="font-family:宋体"}**[undo debugging san-aggregation]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[FC]{lang="EN-US"}[聚合组调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x967698771}[聚合组调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1489_93403_x967829843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1489_93403_x968485203}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，表示同时指定接收和发送的报文。]{style="font-family:宋体"}[]{#_Toc85816095}[]{#_Toc85816096}[]{#_Toc85816097}[]{#_Toc85816098}[]{#_Toc85816099}[]{#_Toc85816100}[]{#_Toc85816101}[]{#_Toc85816102}[]{#_Toc85816103}[]{#_Toc85816104}[]{#_Toc85816105}[]{#_Toc85816106}[]{#_Toc85816107}[]{#_Toc85816108}[]{#_Toc85816109}[]{#_Toc85816110}[]{#_Toc85816111}[]{#_Toc85816112}[]{#_Toc85816113}[]{#_Toc85816114}[]{#_Toc85816115}[]{#_Toc85816116}[]{#_Toc85816117}[]{#_Toc85816118}[]{#_Toc85816119}[]{#_Toc85816120}[]{#_Toc85816121}[]{#_Toc85816122}[]{#_Toc85816123}[]{#_Toc85816124}[]{#_Toc85816125}[]{#_Toc85816126}[]{#_Toc37747171}[]{#_Hlt23321500}[]{#_Hlt9334992}[]{#_Toc85816127}[]{#_Toc85816129}[]{#_Toc85816130}[]{#_Toc85816131}[]{#_Toc85816138}[]{#_Toc85816139}[]{#_Toc85816140}[]{#_Toc85816141}[]{#_Toc85816142}[]{#_Toc85816156}[]{#_Toc85816157}[]{#_Toc85816158}[]{#_Toc85816159}[]{#_Toc85816166}[]{#_Toc85816167}[]{#_Toc85816168}[]{#_Toc85816169}[]{#_Toc85816182}[]{#_Toc85816183}[]{#_Toc85816204}[]{#_Toc85816205}[]{#_Toc85816206}[]{#_Toc85816207}[]{#_Toc85816208}[]{#_Toc85816209}[]{#_Toc85816210}[]{#_Toc85816211}[]{#_Toc85816212}[]{#_Toc85816213}[]{#_Toc85816214}[]{#_Toc85816227}[]{#_Toc85816228}[]{#_Toc85816229}[]{#_Toc85816230}[]{#_Toc85816231}[]{#_Toc85816232}[]{#_Toc85816233}[]{#_Toc85816240}[]{#_Toc85816241}[]{#_Toc85816242}[]{#_Toc85816243}[]{#_Toc85816244}[]{#_Toc85816245}[]{#_Toc85816246}[]{#_Toc85816247}[]{#_Toc85816248}[]{#_Toc85816249}[]{#_Toc85816250}[]{#_Toc85816251}[]{#_Toc85816252}[]{#_Toc85816253}[]{#_Toc85816254}[]{#_Toc85816255}[]{#_Toc85816256}[]{#_Toc85816257}[]{#_Toc85816258}[]{#_Toc85816268}[]{#_Toc85816269}[]{#_Toc85816270}[]{#_Toc85816271}[]{#_Toc85816272}[]{#_Toc85816273}[]{#_Toc85816274}[]{#_Toc85816281}[]{#_Toc85816282}[]{#_Toc85816283}[]{#_Toc85816284}[]{#_Toc85816306}[]{#_Toc85816307}[]{#_Toc85816308}[]{#_Toc85816309}[]{#_Toc85816337}[]{#_Toc85816338}[]{#_Toc85816340}[]{#_Toc85816341}[]{#_Toc85816342}[]{#_Toc85816352}[]{#_Toc85816353}[]{#_Toc85816354}[]{#_Toc85816355}[]{#_Toc85816356}[]{#_Toc85816357}[]{#_Toc85816358}[]{#_Toc85816359}[]{#_Toc85816360}[]{#_Toc85816361}[]{#_Toc85816362}[]{#_Toc85816363}[]{#_Toc85816364}[]{#_Toc85816365}[]{#_Toc85816366}[]{#_Toc85816367}[]{#_Toc85816368}[]{#_Toc85816399}[]{#_Toc85816400}[]{#_Toc85816401}[]{#_Toc85816403}[]{#_Toc85816408}[]{#_Toc85816409}[]{#_Toc85816410}[]{#_Toc85816411}[]{#_Toc85816412}[]{#_Toc85816413}[]{#_Toc85816423}[]{#_Toc85816424}[]{#_Toc85816425}[]{#_Toc85816426}[]{#_Toc85816427}[]{#_Toc85816455}[]{#_Toc85816456}[]{#_Toc85816457}[]{#_Hlt15267207}[]{#_Toc85816458}[]{#_Toc85816459}[]{#_Toc85816460}[]{#_Toc85816461}[]{#_Toc85816462}[]{#_Toc85816463}[]{#_Toc85816464}[]{#_Toc85816465}[]{#_Toc85816467}[]{#_Toc85816468}[]{#_Toc85816469}[]{#_Toc85816470}[]{#_Toc85816471}[]{#_Toc85816472}[]{#_Toc85816473}[]{#_Toc85816474}[]{#_Toc85816475}[]{#_Toc85816476}[]{#_Toc85816477}[]{#_Toc85816478}[]{#_Toc85816479}[]{#_Toc85816480}[]{#_Toc85816481}[]{#_Toc85816482}[]{#_Toc85816483}[]{#_Toc85816484}[]{#_Toc85816485}[]{#_Toc85816645}[]{#_Toc85816646}[]{#_Toc85816647}[]{#_Toc85816648}[]{#_Toc85816649}[]{#_Toc85816650}[]{#_Toc85816651}[]{#_Toc85816652}[]{#_Toc85816653}[]{#_Toc85816654}[]{#_Toc85816655}[]{#_Toc85816656}[]{#_Toc85816657}[]{#_Toc85816658}[]{#_Toc85816659}[]{#_Toc85816675}[]{#_Toc85816676}[]{#_Toc85816677}[]{#_Toc85816678}[]{#_Toc85816680}[]{#_Toc85816683}[]{#_Toc85816685}[]{#_Toc85816686}[]{#_Toc85816687}[]{#_Toc85816689}[]{#_Toc85816694}[]{#_Toc85816695}[]{#_Toc85816696}[]{#_Toc85816699}[]{#_Toc85816702}[]{#_Toc85816703}[]{#_Hlt15796603}[]{#_Toc85816704}[]{#_Toc85816705}[]{#_Toc85816706}[]{#_Toc85816707}[]{#_Toc85816708}[]{#_Toc85816709}[]{#_Toc85816710}[]{#_Toc85816713}[]{#_Toc85816714}[]{#_Toc85816715}[]{#_Toc85816716}[]{#_Toc85816717}[]{#_Toc85816718}[]{#_Toc85816719}[]{#_Toc85816720}[]{#_Toc85816721}[]{#_Toc85816722}[]{#_Toc85816723}[]{#_Toc85816742}[]{#_Toc85816743}[]{#_Toc85816744}[]{#_Toc85816745}[]{#_Toc85816752}[]{#_Toc85816753}[]{#_Toc85816754}[]{#_Toc85816755}[]{#_Toc85816774}[]{#_Toc85816775}[]{#_Toc85816776}[]{#_Toc85816777}[]{#_Toc85816787}[]{#_Toc85816788}[]{#_Toc85816789}[]{#_Toc85816790}[]{#_Toc85816791}[]{#_Toc85816792}[]{#_Toc85816793}[]{#_Toc85816794}[]{#_Toc85816795}[]{#_Toc85816796}[]{#_Toc85816797}[]{#_Toc85816816}[]{#_Hlt24806861}[]{#_Toc85816817}[]{#_Toc85816818}[]{#_Toc85816819}[]{#_Toc85816820}[]{#_Toc85816851}[]{#_Toc85816852}[]{#_Toc85816853}[]{#_Toc85816854}[]{#_Toc85816861}[]{#_Toc37747192}[]{#_Toc37747193}[]{#_Toc37747194}[]{#_Toc37747195}[]{#_Toc37747202}[]{#_Toc85816862}[]{#_Toc85816863}[]{#_Toc85816864}[]{#_Toc85816865}[]{#_Toc85816872}[]{#_Toc85816873}[]{#_Toc85816874}[]{#_Toc85816875}[]{#_Toc85816878}[]{#_Toc85816881}[]{#_Toc85816883}[]{#_Toc85816884}[]{#_Hlt23751682}[]{#_Hlt12087209}[]{#_Toc85816885}[]{#_Toc85816886}[]{#_Toc85816887}[]{#_Toc85816888}[]{#_Toc85816889}[]{#_Toc85816890}[]{#_Toc85816891}[]{#_Toc85816892}[]{#_Toc85816893}[]{#_Toc85816894}[]{#_Toc85816895}[]{#_Toc85816896}[]{#_Toc85816897}[]{#_Toc85816898}[]{#_Toc85816899}[]{#_Toc85816909}[]{#_Toc85816910}[]{#_Toc85816911}[]{#_Toc85816912}[]{#_Toc85816913}[]{#_Toc85816914}[]{#_Toc85816930}[]{#_Toc85816931}[]{#_Toc85816932}[]{#_Toc85816933}[]{#_Toc85816935}[]{#_Toc85816937}[]{#_Toc85816939}[]{#_Toc85816940}[]{#_Toc85816941}[]{#_Toc85816942}[]{#_Toc85816943}[]{#_Toc85816944}[]{#_Toc85816945}[]{#_Toc85816955}[]{#_Toc85816956}[]{#_Toc85816957}[]{#_Toc85816958}[]{#_Toc85816959}[]{#_Toc85816960}[]{#_Toc85816970}[]{#_Toc85816971}[]{#_Toc85816972}[]{#_Toc85816973}[]{#_Toc85816983}[]{#_Toc85816984}[]{#_Hlt25036508}[]{#_Toc85816985}[]{#_Toc85816986}[]{#_Hlt25036644}[]{#_Toc85816987}[]{#_Toc85816988}[]{#_Hlt24620344}[]{#_Hlt24620750}[]{#_Toc85816989}[]{#_Toc85816990}[]{#_Toc85816991}[]{#_Toc85816992}[]{#_Toc85816993}[]{#_Toc85816994}[]{#_Toc85816995}[]{#_Toc85816996}[]{#_Toc85816997}[]{#_Toc85816998}[]{#_Toc85816999}[]{#_Toc85817000}[]{#_Hlt24621022}[]{#_Toc85817001}[]{#_Toc85817009}[]{#_Toc85817010}[]{#_Toc85817011}[]{#_Toc85817012}[]{#_Toc85817022}[]{#_Toc85817029}[]{#_Toc85817030}[]{#_Toc85817031}[]{#_Hlt24797856}[]{#_Toc85817032}[]{#_Toc85817033}[]{#_Toc85817034}[]{#_Toc85817035}[]{#_Toc85817036}[]{#_Toc85817037}[]{#_Toc85817038}[]{#_Toc85817039}[]{#_Toc85817040}[]{#_Toc85817041}[]{#_Toc85817051}[]{#_Toc85817052}[]{#_Toc85817053}[]{#_Toc85817054}[]{#_Toc85817055}[]{#_Toc85817056}[]{#_Toc85817057}[]{#_Toc85817058}[]{#_Toc85817065}[]{#_Toc85817066}[]{#_Toc85817067}[]{#_Toc85817068}[]{#_Toc85817069}[]{#_Toc85817079}[]{#_Toc85817080}[]{#_Toc85817081}[]{#_Toc85817082}[]{#_Toc85817083}[]{#_Toc85817084}[]{#_Toc85817085}[]{#_Toc85817086}[]{#_Toc85817087}[]{#_Toc85817088}[]{#_Toc85817089}[]{#_Toc85817090}[]{#_Toc85817091}[]{#_Toc85817092}[]{#_Toc85817105}[]{#_Toc85817106}[]{#_Toc85817107}[]{#_Toc85817108}[]{#_Toc85817109}[]{#_Toc85817110}[]{#_Toc85817111}[]{#_Toc85817112}[]{#_Toc85817119}[]{#_Toc85817120}[]{#_Toc85817121}[]{#_Toc85817122}[]{#_Toc85817123}[]{#_Toc85817124}[]{#_Toc85817125}[]{#_Toc85817126}[]{#_Toc85817127}[]{#_Toc85817128}[]{#_Toc85817129}[]{#_Toc85817136}[]{#_Toc85817137}[]{#_Toc85817138}[]{#_Toc85817139}[]{#_Toc85817140}[]{#_Toc85817141}[]{#_Toc85817142}[]{#_Toc85817143}[]{#_Toc85817144}[]{#_Toc85817149}[]{#_Toc85817150}[]{#_Toc85817151}[]{#_Toc85817152}[]{#_Toc85817153}[]{#_Toc85817154}[]{#_Toc85817155}[]{#_Toc85817156}[]{#_Toc85817157}[]{#_Toc85817158}[]{#_Toc85817159}[]{#_Toc85817160}[]{#_Toc85817161}[]{#_Toc85817163}[]{#_Toc85817164}[]{#_Toc85817165}[]{#_Toc85817166}[]{#_Toc85817167}[]{#_Toc85817168}[]{#_Toc85817169}[]{#_Toc85817170}[]{#_Toc85817171}[]{#_Toc85817172}[]{#_Toc85817173}[]{#_Toc85817174}[]{#_Toc85817175}[]{#_Toc85817176}[]{#_Toc85817177}[]{#_Toc85817178}[]{#_Toc85817179}[]{#_Toc85817180}[]{#_Toc85817181}[]{#_Toc85817182}[]{#_Toc85817183}[]{#_Toc85817184}[]{#_Toc85817185}[]{#_Toc85817186}[]{#_Toc85817187}[]{#_Toc85817188}[]{#_Toc85817189}[]{#_Toc85817190}[]{#_Toc85817191}[]{#_Toc85817192}[]{#_Toc85817193}[]{#_Toc85817194}[]{#_Toc85817195}[]{#_Toc85817196}[]{#_Toc85817203}[]{#_Toc85817204}[]{#_Toc85817207}[]{#_Toc85817208}[]{#_Toc85817209}[]{#_Toc85817210}[]{#_Toc85817211}[]{#_Toc85817212}[]{#_Toc85817213}[]{#_Toc85817214}[]{#_Toc85817215}[]{#_Toc85817216}[]{#_Toc85817217}[]{#_Toc85817227}[]{#_Toc85817228}[]{#_Toc85817239}[]{#_Toc85817240}[]{#_Toc85817241}[]{#_Toc85817251}[]{#_Toc85817252}[]{#_Toc85817253}[]{#_Toc85817254}[]{#_Toc85817255}[]{#_Toc85817256}[]{#_Toc85817257}[]{#_Toc85817258}[]{#_Toc85817268}[]{#_Toc85817269}[]{#_Toc85817270}[]{#_Toc85817271}[]{#_Toc85817272}[]{#_Toc85817273}[]{#_Toc85817274}[]{#_Toc85817275}[]{#_Toc85817276}[]{#_Toc85817277}[]{#_Toc85817287}[]{#_Toc85817288}[]{#_Toc85817289}[]{#_Toc85817290}[]{#_Toc85817300}[]{#_Toc85817301}[]{#_Toc85817302}[]{#_Toc85817303}[]{#_Toc85817304}[]{#_Toc85817305}[]{#_Toc85817306}[]{#_Toc85817316}[]{#_Toc85817317}[]{#_Toc85817318}[]{#_Toc85817319}[]{#_Toc85817320}[]{#_Toc85817321}[]{#_Toc85817324}[]{#_Toc85817326}[]{#_Toc85817327}[]{#_Toc85817337}[]{#_Toc85817338}[]{#_Toc85817339}[]{#_Toc85817340}[]{#_Toc85817341}[]{#_Toc85817348}[]{#_Toc85817352}[]{#_Toc85817353}[]{#_Toc85817354}[]{#_Toc85817364}[]{#_Toc85817365}[]{#_Toc85817366}[]{#_Toc85817367}[]{#_Toc85817368}[]{#_Toc85817369}[]{#_Toc85817379}[]{#_Toc85817380}[]{#_Toc85817381}[]{#_Toc85817382}[]{#_Toc85817383}[]{#_Toc85817405}[]{#_Toc85817406}[]{#_Toc85817408}[]{#_Toc85817409}[]{#_Toc85817410}[]{#_Toc85817411}[]{#_Toc85817418}[]{#_Toc85817419}[]{#_Toc85817420}[]{#_Toc85817421}[]{#_Toc85817422}[]{#_Toc85817423}[]{#_Toc85817424}[]{#_Toc85817425}[]{#_Toc85817426}[]{#_Toc85817427}[]{#_Toc85817428}[]{#_Toc85817429}[]{#_Toc85817430}[]{#_Toc85817431}[]{#_Toc85817441}[]{#_Toc85817442}[]{#_Toc85817443}[]{#_Toc85817444}[]{#_Toc85817445}[]{#_Toc85817447}[]{#_Toc85817448}[]{#_Toc85817449}[]{#_Toc85817450}[]{#_Toc85817451}[]{#_Toc85817461}[]{#_Toc85817462}[]{#_Toc85817463}[]{#_Toc85817464}[]{#_Toc85817465}[]{#_Toc85817466}[]{#_Toc85817476}[]{#_Toc85817477}[]{#_Toc85817478}[]{#_Toc85817479}[]{#_Toc85817480}[]{#_Toc85817487}[]{#_Toc85817488}[]{#_Toc85817489}[]{#_Toc85817490}[]{#_Toc85817497}[]{#_Toc85817498}[]{#_Toc85817499}[]{#_Toc85817500}[]{#_Toc85817501}[]{#_Toc85817502}[]{#_Toc85817503}[]{#_Toc85817504}[]{#_Toc85817505}[]{#_Toc85817506}[]{#_Toc85817507}[]{#_Toc85817508}[]{#_Toc85817509}[]{#_Toc85817510}[]{#_Toc85817511}[]{#_Toc85817512}[]{#_Toc85817513}[]{#_Toc85817514}[]{#_Toc85817515}[]{#_Toc85817516}[]{#_Toc85817537}[]{#_Toc85817538}[]{#_Toc85817539}[]{#_Toc85817540}[]{#_Toc85817541}[]{#_Toc85817542}[]{#_Toc85817543}[]{#_Toc85817544}[]{#_Toc85817545}[]{#_Toc85817546}[]{#_Toc85817547}[]{#_Toc85817548}[]{#_Toc85817549}[]{#_Toc85817550}[]{#_Toc85817551}[]{#_Toc85817552}[]{#_Toc85817553}[]{#_Toc85817554}[]{#_Toc85817555}[]{#_Toc85817556}[]{#_Toc85817566}[]{#_Toc85817567}[]{#_Toc85817568}[]{#_Toc85817569}[]{#_Toc85817570}[]{#_Toc85817571}[]{#_Toc85817572}[]{#_Toc85817573}[]{#_Toc85817574}[]{#_Toc85817575}[]{#_Toc85817585}[]{#_Toc85817586}[]{#_Toc85817587}[]{#_Toc85817588}[]{#_Toc85817589}[]{#_Toc85817590}[]{#_Toc85817600}[]{#_Toc85817601}[]{#_Toc85817602}[]{#_Toc85817603}[]{#_Toc85817604}[]{#_Toc85817605}[]{#_Toc85817606}[]{#_Toc85817607}[]{#_Toc85817617}[]{#_Toc85817618}[]{#_Toc85817619}[]{#_Toc85817620}[]{#_Toc85817622}[]{#_Toc85817623}[]{#_Toc85817624}[]{#_Toc85817625}[]{#_Toc85817626}[]{#_Toc85817636}[]{#_Toc85817637}[]{#_Toc85817638}[]{#_Toc85817639}[]{#_Toc85817640}[]{#_Toc85817641}[]{#_Toc85817642}[]{#_Toc85817643}[]{#_Toc85817644}[]{#_Toc85817657}[]{#_Toc85817658}[]{#_Toc85817659}[]{#_Toc85817660}[]{#_Toc85817661}[]{#_Toc85817662}[]{#_Toc85817663}[]{#_Toc85817664}[]{#_Toc85817665}[]{#_Toc85817666}[]{#_Toc85817667}[]{#_Toc85817671}[]{#_Toc85817672}[]{#_Hlt21938307}[]{#_Toc85817673}[]{#_Toc85817674}[]{#_Toc85817675}[]{#_Toc85817676}[]{#_Toc85817677}[]{#_Toc85817678}[]{#_Toc85817679}[]{#_Toc85817680}[]{#_Toc85817681}[]{#_Toc85817682}[]{#_Toc85817683}[]{#_Toc85817684}[]{#_Toc85817685}[]{#_Toc85817686}[]{#_Toc85817687}[]{#_Toc85817688}[]{#_Toc85817689}[]{#_Toc85817690}[]{#_Toc85817691}[]{#_Toc85817692}[]{#_Toc85817693}[]{#_Toc85817694}[]{#_Toc85817695}[]{#_Toc85817696}[]{#_Toc85817697}[]{#_Toc85817698}[]{#_Toc85817699}[]{#_Toc85817700}[]{#_Toc85817701}[]{#_Toc85817702}[]{#_Toc85817703}[]{#_Hlt15977823}[]{#_Toc85817704}[]{#_Toc85817705}[]{#_Toc85817706}[]{#_Toc85817707}[]{#_Toc85817708}[]{#_Toc85817709}[]{#_Toc85817710}[]{#_Toc85817711}[]{#_Toc85817712}[]{#_Toc85817713}[]{#_Toc85817714}[]{#_Toc85817715}[]{#_Toc85817725}[]{#_Toc85817726}[]{#_Toc85817727}[]{#_Toc85817728}[]{#_Toc85817729}[]{#_Toc85817730}[]{#_Toc85817740}[]{#_Toc85817741}[]{#_Hlt23405451}[]{#_Toc85817742}[]{#_Toc85817743}[]{#_Toc85817744}[]{#_Toc85817745}[]{#_Toc85817755}[]{#_Toc85817756}[]{#_Toc85817757}[]{#_Toc85817758}[]{#_Toc85817759}[]{#_Toc85817760}[]{#_Toc85817770}[]{#_Toc85817771}[]{#_Toc85817772}[]{#_Toc85817773}[]{#_Toc85817774}[]{#_Toc85817784}[]{#_Toc85817785}[]{#_Toc85817786}[]{#_Toc85817787}[]{#_Toc85817788}[]{#_Toc85817789}[]{#_Toc85817790}[]{#_Toc85817800}[]{#_Toc85817801}[]{#_Toc56323509}[]{#_Toc56323510}[]{#_Toc56323511}[]{#_Toc56323512}[]{#_Toc56323522}[]{#_Toc56323523}[]{#_Toc85817802}[]{#_Toc85817803}[]{#_Toc85817804}[]{#_Toc85817805}[]{#_Toc85817815}[]{#_Toc85817816}[]{#_Toc85817817}[]{#_Toc85817818}[]{#_Toc85817819}[]{#_Toc85817829}[]{#_Toc85817830}[]{#_Toc85817831}[]{#_Toc85817832}[]{#_Toc85817833}[]{#_Toc85817834}[]{#_Toc85817844}[]{#_Toc85817845}[]{#_Toc85817846}[]{#_Toc85817847}[]{#_Toc85817848}[]{#_Toc85817849}[]{#_Toc85817859}[]{#_Toc85817860}[]{#_Toc85817861}[]{#_Hlt25378447}[]{#_Toc85817863}[]{#_Toc85817864}[]{#_Toc85817874}[]{#_Toc85817875}[]{#_Toc85817876}[]{#_Toc85817877}[]{#_Toc85817878}[]{#_Toc85817879}[]{#_Toc85817889}[]{#_Toc85817890}[]{#_Toc56323530}[]{#_Toc56323531}[]{#_Toc56323532}[]{#_Toc56323533}[]{#_Toc56323543}[]{#_Toc56323544}[]{#_Toc85817891}[]{#_Toc85817892}[]{#_Toc85817893}[]{#_Toc85817894}[]{#_Toc85817904}[]{#_Toc85817905}[]{#_Toc85817906}[]{#_Toc85817907}[]{#_Toc85817908}[]{#_Toc85817909}[]{#_Toc85817910}[]{#_Toc85817911}[]{#_Toc85817912}[]{#_Toc85817913}[]{#_Toc85817923}[]{#_Toc85817924}[]{#_Toc85817925}[]{#_Toc85817926}[]{#_Toc85817927}[]{#_Toc85817928}[]{#_Toc85817944}[]{#_Toc85817945}[]{#_Toc85817946}[]{#_Toc85817947}[]{#_Toc85817948}[]{#_Toc85817949}[]{#_Toc85817950}[]{#_Toc85817951}[]{#_Toc85817952}[]{#_Toc85817954}[]{#_Toc85817956}[]{#_Toc85817957}[]{#_Toc85817959}[]{#_Toc85817961}[]{#_Toc85817963}[]{#_Toc85817964}[]{#_Toc85817966}[]{#_Toc85817969}[]{#_Toc85817975}[]{#_Toc85817976}[]{#_Toc85817981}[]{#_Toc85817982}[]{#_Toc85817983}[]{#_Toc85817984}[]{#_Toc85817985}[]{#_Toc85817986}[]{#_Toc85817987}[]{#_Toc85817989}[]{#_Toc85817991}[]{#_Toc85817992}[]{#_Toc85817994}[]{#_Toc85817998}[]{#_Toc85817999}[]{#_Toc85818001}[]{#_Toc85818003}[]{#_Toc85818005}[]{#_Toc85818006}[]{#_Toc85818012}[]{#_Toc85818013}[]{#_Toc85818018}[]{#_Toc85818019}[]{#_Toc85818020}[]{#_Toc85818021}[]{#_Toc85818022}[]{#_Toc85818023}[]{#_Toc85818024}[]{#_Toc85818026}[]{#_Toc85818028}[]{#_Toc85818030}[]{#_Toc85818032}[]{#_Toc85818035}[]{#_Toc85818041}[]{#_Toc85818043}[]{#_Toc85818046}[]{#_Toc85818047}[]{#_Toc85818053}[]{#_Toc85818054}[]{#_Toc85818059}[]{#_Toc85818060}[]{#_Toc85818061}[]{#_Toc85818062}[]{#_Toc85818063}[]{#_Toc85818064}[]{#_Toc85818065}[]{#_Toc85818067}[]{#_Toc85818069}[]{#_Toc85818071}[]{#_Toc85818073}[]{#_Toc85818075}[]{#_Toc85818076}[]{#_Toc85818077}[]{#_Toc85818079}[]{#_Toc85818082}[]{#_Toc85818083}[]{#_Toc85818084}[]{#_Toc85818086}[]{#_Toc85818088}[]{#_Toc85818089}[]{#_Toc85818091}[]{#_Toc85818092}[]{#_Toc85818093}[]{#_Toc85818094}[]{#_Toc85818095}[]{#_Toc85818098}[]{#_Toc85818100}[]{#_Toc85818101}[]{#_Toc85818103}[]{#_Toc85818104}[]{#_Toc85818105}[]{#_Toc85818107}[]{#_Toc85818108}[]{#_Toc85818109}[]{#_Toc85818110}[]{#_Toc85818111}[]{#_Toc85818112}[]{#_Toc85818113}[]{#_Toc85818114}[]{#_Toc85818116}[]{#_Toc85818118}[]{#_Toc85818120}[]{#_Toc85818122}[]{#_Toc85818125}[]{#_Toc85818127}[]{#_Toc85818132}[]{#_Toc85818134}[]{#_Toc85818136}[]{#_Toc85818138}[]{#_Toc85818139}[]{#_Toc85818145}[]{#_Toc85818146}[]{#_Toc85818151}[]{#_Toc85818152}[]{#_Toc85818153}[]{#_Toc85818154}[]{#_Toc85818155}[]{#_Toc85818156}[]{#_Toc85818157}[]{#_Toc85818159}[]{#_Toc85818161}[]{#_Toc85818164}[]{#_Toc85818166}[]{#_Toc85818168}[]{#_Toc85818170}[]{#_Toc85818172}[]{#_Toc85818173}[]{#_Toc85818174}[]{#_Toc85818175}[]{#_Toc85818177}[]{#_Toc85818179}[]{#_Toc85818181}[]{#_Toc85818187}[]{#_Toc85818188}[]{#_Toc85818189}[]{#_Toc85818190}[]{#_Toc85818191}[]{#_Toc85818192}[]{#_Toc85818193}[]{#_Toc85818195}[]{#_Toc85818196}[]{#_Toc85818197}[]{#_Toc85818198}[]{#_Toc85818199}[]{#_Toc85818209}[]{#_Toc85818213}[]{#_Toc85818217}[]{#_Toc85818221}[]{#_Toc85818225}[]{#_Toc85818229}[]{#_Toc85818233}[]{#_Toc85818237}[]{#_Toc85818241}[]{#_Toc85818245}[]{#_Toc85818249}[]{#_Toc85818253}[]{#_Toc85818257}[]{#_Toc85818261}[]{#_Toc85818269}[]{#_Toc85818273}[]{#_Toc85818277}[]{#_Toc85818281}[]{#_Toc85818285}[]{#_Toc85818286}[]{#_Toc85818287}[]{#_Toc85818288}[]{#_Toc85818289}[]{#_Toc85818290}[]{#_Toc85818291}[]{#_Toc85818292}[]{#_Toc85818293}[]{#_Toc85818294}[]{#_Toc85818295}[]{#_Toc85818296}[]{#_Hlt9156368}[]{#_Toc85818297}[]{#_Toc85818298}[]{#_Toc85818299}[]{#_Toc85818300}[]{#_Toc85818301}[]{#_Toc85818302}[]{#_Toc85818303}[]{#_Toc85818304}[]{#_Toc85818305}[]{#_Toc85818306}[]{#_Toc85818316}[]{#_Toc85818317}[]{#_Toc85818318}[]{#_Toc85818319}[]{#_Toc85818320}[]{#_Toc85818330}[]{#_Toc85818331}[]{#_Toc85818332}[]{#_Toc85818334}[]{#_Toc85818336}[]{#_Toc85818337}[]{#_Toc85818338}[]{#_Toc85818339}[]{#_Toc85818349}[]{#_Toc85818350}[]{#_Toc85818351}[]{#_Toc85818352}[]{#_Toc85818353}[]{#_Toc85818354}[]{#_Toc85818355}[]{#_Toc85818356}[]{#_Toc85818357}[]{#_Toc85818358}[]{#_Toc85818370}[]{#_Toc85818371}[]{#_Toc85818372}[]{#_Toc85818373}[]{#_Toc85818374}[]{#_Toc85818386}[]{#_Toc85818387}[]{#_Toc85818389}[]{#_Toc85818390}[]{#_Toc85818391}[]{#_Toc85818392}[]{#_Toc85818402}[]{#_Toc85818404}[]{#_Toc85818405}[]{#_Toc85818406}[]{#_Toc85818407}[]{#_Toc85818417}[]{#_Toc85818418}[]{#_Toc85818419}[]{#_Hlt23324581}[]{#_Toc85818420}[]{#_Toc85818421}[]{#_Hlt23741538}[]{#_Toc85818422}[]{#_Toc85818433}[]{#_Toc85818434}[]{#_Toc85818435}[]{#_Toc85818436}[]{#_Toc85818446}[]{#_Toc85818447}[]{#_Toc85818448}[]{#_Toc85818449}[]{#_Toc85818450}[]{#_Toc85818451}[]{#_Toc85818452}[]{#_Toc85818462}[]{#_Toc85818463}[]{#_Toc85818465}[]{#_Toc85818466}[]{#_Toc85818467}[]{#_Toc85818468}[]{#_Toc85818478}[]{#_Toc85818479}[]{#_Toc85818481}[]{#_Toc85818482}[]{#_Toc85818483}[]{#_Toc85818484}[]{#_Toc85818494}[]{#_Toc85818495}[]{#_Toc85818497}[]{#_Toc85818498}[]{#_Toc85818499}[]{#_Toc85818500}[]{#_Toc85818510}[]{#_Toc85818511}[]{#_Toc85818512}[]{#_Toc85818514}[]{#_Toc85818516}[]{#_Toc85818527}[]{#_Toc85818528}[]{#_Toc85818530}[]{#_Toc85818531}[]{#_Toc85818532}[]{#_Toc85818543}[]{#_Toc85818544}[]{#_Toc85818545}[]{#_Toc85818547}[]{#_Toc85818548}[]{#_Toc85818549}[]{#_Toc85818550}[]{#_Toc85818584}[]{#_Toc85818585}[]{#_Toc85818586}[]{#_Toc85818587}[]{#_Toc85818588}[]{#_Toc85818589}[]{#_Toc85818590}[]{#_Toc85818591}[]{#_Toc85818592}[]{#_Toc85818594}[]{#_Toc85818595}[]{#_Toc85818596}[]{#_Toc85818597}[]{#_Toc85818598}[]{#_Toc85818599}[]{#_Toc85818602}[]{#_Toc85818604}[]{#_Toc85818606}[]{#_Toc85818607}[]{#_Toc85818608}[]{#_Toc85818609}[]{#_Toc85818610}[]{#_Toc85818616}[]{#_Hlt25146204}[]{#_Hlt12271448}[]{#_Toc85818617}[]{#_Toc85818618}[]{#_Toc85818619}[]{#_Toc85818620}[]{#_Toc85818621}[]{#_Toc85818622}[]{#_Toc85818623}[]{#_Toc85818624}[]{#_Toc85818625}[]{#_Toc85818626}[]{#_Toc85818627}[]{#_Toc85818628}[]{#_Toc85818656}[]{#_Toc85818657}[]{#_Toc85818658}[]{#_Toc85818659}[]{#_Toc85818660}[]{#_Toc85818661}[]{#_Toc85818662}[]{#_Toc85818663}[]{#_Toc85818664}[]{#_Toc85818665}[]{#_Toc85818690}[]{#_Toc85818691}[]{#_Toc85818692}[]{#_Hlt15375565}[]{#_Toc85818693}[]{#_Toc85818694}[]{#_Toc85818695}[]{#_Toc85818696}[]{#_Toc85818697}[]{#_Toc85818698}[]{#_Toc85818699}[]{#_Toc85818700}[]{#_Toc85818701}[]{#_Toc85818702}[]{#_Toc85818703}[]{#_Toc85818704}[]{#_Toc85818717}[]{#_Toc85818718}[]{#_Toc85818719}[]{#_Toc85818720}[]{#_Toc85818721}[]{#_Toc85818722}[]{#_Toc85818723}[]{#_Toc85818733}[]{#_Toc85818734}[]{#_Toc85818738}[]{#_Toc85818739}[]{#_Toc85818740}[]{#_Toc85818741}[]{#_Toc85818742}[]{#_Toc85818743}[]{#_Toc85818744}[]{#_Toc85818745}[]{#_Toc85818746}[]{#_Toc85818747}[]{#_Toc85818748}[]{#_Toc85818764}[]{#_Toc85818765}[]{#_Toc85818766}[]{#_Toc85818767}[]{#_Toc85818768}[]{#_Toc85818769}[]{#_Toc85818770}[]{#_Toc85818774}[]{#_Toc85818777}[]{#_Hlt23410930}[]{#_Toc85818778}[]{#_Toc85818779}[]{#_Toc85818780}[]{#_Toc85818781}[]{#_Toc85818782}[]{#_Toc85818801}[]{#_Toc85818802}[]{#_Hlt23410927}[]{#_Toc85818803}[]{#_Toc85818804}[]{#_Toc85818805}[]{#_Toc85818806}[]{#_Toc85818807}[]{#_Toc85818808}[]{#_Toc85818809}[]{#_Toc85818810}[]{#_Toc85818811}[]{#_Toc85818812}[]{#_Toc85818813}[]{#_Toc85818814}[]{#_Toc85818815}[]{#_Toc85818816}[]{#_Toc85818817}[]{#_Toc85818818}[]{#_Toc85818819}[]{#_Toc323805920}[]{#_Toc323805921}[]{#_Toc323805922}[]{#_Toc323805923}[]{#_Toc323805924}[]{#_Toc323805925}[]{#_Toc323805926}[]{#_Toc323805927}[]{#_Toc323805928}[]{#_Toc323805929}[]{#_Toc323805930}[]{#_Toc323805931}[]{#_Toc323805932}[]{#_Toc323805933}[]{#_Toc323805934}[]{#_Toc323805935}[]{#_Toc323805936}[]{#_Toc323805937}[]{#_Toc323805938}[]{#_Toc323805939}[]{#_Toc323805942}[]{#_Toc323805943}[]{#_Toc323805944}[]{#_Toc323805946}[]{#_Toc323805947}[]{#_Toc323805948}[]{#_Toc323805949}[]{#_Toc323805951}[]{#_Toc323805954}[]{#_Toc323805955}[]{#_Toc323805956}[]{#_Toc323805957}[]{#_Toc323805958}[]{#_Toc323805959}[]{#_Toc323805960}[]{#_Toc323805961}[]{#_Toc323805962}[]{#_Toc323805963}[]{#_Toc323805964}[]{#_Toc323805965}[]{#_Toc323805966}[]{#_Toc323805967}[]{#_Toc323805968}[]{#_Toc323805969}[]{#_Toc323805970}[]{#_Toc323805971}[]{#_Toc323805973}[]{#_Toc323805974}[]{#_Toc323805975}[]{#_Toc323805976}[]{#_Toc323805977}[]{#_Toc323805978}[]{#_Toc323805979}[]{#_Toc323805980}[]{#_Toc323805981}[]{#_Toc323805982}[]{#_Toc323805983}[]{#_Toc323805984}[]{#_Toc323805988}[]{#_Toc323805991}[]{#_Toc323805992}[]{#_Toc323805993}[]{#_Toc323805994}[]{#_Toc323805995}[]{#_Toc323805996}[]{#_Toc323805997}[]{#_Toc323805998}[]{#_Toc323805999}[]{#_Toc323806000}[]{#_Toc323806001}[]{#_Toc323806002}[]{#_Toc323806003}[]{#_Toc323806004}[]{#_Toc323806008}[]{#_Toc323806009}[]{#_Toc323806010}[]{#_Toc323806011}[]{#_Toc323806012}[]{#_Toc323806013}[]{#_Toc323806014}[]{#_Toc323806016}[]{#_Toc323806017}[]{#_Toc323806018}[]{#_Toc323806019}[]{#_Toc323806020}[]{#_Toc323806021}[]{#_Toc323806022}[]{#_Toc323806023}[]{#_Toc323806024}[]{#_Toc323806025}[]{#_Toc323806026}[]{#_Toc323806027}[]{#_Toc323806028}[]{#_Toc323806031}[]{#_Toc323806032}[]{#_Toc323806033}[]{#_Toc323806035}[]{#_Toc323806036}[]{#_Toc323806037}[]{#_Toc323806039}[]{#_Toc323806040}[]{#_Toc323806041}[]{#_Toc323806042}[]{#_Toc323806043}[]{#_Toc323806044}[]{#_Toc323806045}[]{#_Toc323806046}[]{#_Toc323806047}[]{#_Toc323806048}[]{#_Toc323806049}[]{#_Toc323806050}[]{#_Toc323806051}[]{#_Toc323806052}[]{#_Toc323806053}[]{#_Toc323806056}[]{#_Toc323806057}[]{#_Toc323806058}[]{#_Toc323806059}[]{#_Toc323806060}[]{#_Toc323806061}[]{#_Toc323806062}[]{#_Toc323806063}[]{#_Toc323806064}[]{#_Toc323806065}[]{#_Toc323806066}[]{#_Toc323806067}[]{#_Toc323806068}[]{#_Toc323806069}[]{#_Toc323806071}[]{#_Toc323806072}[]{#_Toc323806073}[]{#_Toc323806074}[]{#_Toc323806075}[]{#_Toc323806078}[]{#_Toc323806079}[]{#_Toc323806080}[]{#_Toc323806082}[]{#_Toc323806083}[]{#_Toc323806084}[]{#_Toc323806085}[]{#_Toc323806086}[]{#_Toc323806087}[]{#_Toc323806088}[]{#_Toc323806089}[]{#_Toc323806090}[]{#_Toc323806091}[]{#_Toc323806092}[]{#_Toc323806093}[]{#_Toc323806094}[]{#_Toc323806095}

[[·[              ]{style="font:7.0pt "}]{lang="DE" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1489_93403_1116127128}**[interface]{lang="EN-US"}**[参数]{style="font-family:宋体"}[打开的]{style="font-family:宋体"}[指定接口的调试信息开关，只能通过在]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令中指定]{style="font-family:宋体"}**[interface]{lang="EN-US"}**[参数来关闭。]{style="font-family:宋体"}

[[表1-57 ]{lang="EN-US"}[debugging san-aggregation error]{lang="EN-US"}]{#struct_0_x1489_93403_x968157524}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2070819530}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x967764308}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x967895380}

[[PhyIoCtl event *event-id* is unknown.]{lang="EN-US"}]{#struct_0_x1489_93403_x968485204}

[[物理控制事件]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x967960917}[未知]{style="font-family:宋体"}

[[Failed to add interface *fc*-*interface-name* to SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x968091989}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x967895381}[接口]{style="font-family:宋体"}*[fc]{lang="EN-US"}*[-*interface-name*]{lang="EN-US"}[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to create SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x968550741}

[[创建]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x968026454}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to deal with interface event for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x968091990}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x967698774}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[处理接口事件失败]{style="font-family:宋体"}

[[Failed to notify driver to block interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x968550742}

[[通知驱动阻塞成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x968026455}[失败]{style="font-family:宋体"}

[[Failed to notify driver to unblock interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x968157527}

[[通知驱动解除阻塞成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x967698775}[失败]{style="font-family:宋体"}

[[Failed to notify driver to create SAN aggregation group of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x967829847}

[[通知驱动创建]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x968485207}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to notify driver to change Selected ports for  interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1760725833}

[[通知驱动]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1761119049}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[选中端口变化失败]{style="font-family:宋体"}

[[Failed to notify driver to delete SAN aggregation group for  interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1761053513}

[[通知驱动删除]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1760398153}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to notify driver to set local-first load sharing mode.]{lang="EN-US"}]{#struct_0_x1489_93403_1760725832}

[[通知驱动设置本地转发优先模式失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1761184584}

[[Notifying driver to set local-first load sharing mode is not supported.]{lang="EN-US"}]{#struct_0_x1489_93403_1761053512}

[[不支持通知驱动设置本地转发优先模式]{style="font-family:宋体"}]{#struct_0_x1489_93403_1760398152}

[[Failed to notify the physical state of  interface *sagg-interface-name* to become up.]{lang="EN-US"}]{#struct_0_x1489_93403_1760725831}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1761119047}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[物理]{style="font-family:宋体"}[UP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to notify the physical state of  interface *sagg-interface-name* to become down.]{lang="EN-US"}]{#struct_0_x1489_93403_1761053511}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1760398151}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[物理]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to notify the speed of  interface *sagg-interface-name* to be changed.]{lang="EN-US"}]{#struct_0_x1489_93403_1760922438}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1761119046}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[速率变化失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-58 ]{lang="EN-US"}[debugging san-aggregation event]{lang="EN-US"}]{#struct_0_x1489_93403_1761184582}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2121824673}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_1761053510}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1760856901}

[[Received an event for creating SAN aggregation group for  interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1760725829}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1761119045}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[创建事件]{style="font-family:宋体"}

[[Received an event for deleting SAN aggregation group for  interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1761053509}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1760398149}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[删除事件]{style="font-family:宋体"}

[[Received shutdown notification for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1760922436}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1761119044}[聚合组]{style="font-family:宋体"}*[sagg-interface-name ]{lang="EN-US"}*[shutdown]{lang="EN-US"}[通知]{style="font-family:宋体"}

[[Received undo-shutdown notification for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1760987972}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1760332612}[聚合组]{style="font-family:宋体"}*[sagg-interface-name ]{lang="EN-US"}*[undo-shutdown]{lang="EN-US"}[通知]{style="font-family:宋体"}

[[Notified interface *fc-interface-name* of interface *sagg-interface-name* to join the SAN aggregation group.]{lang="EN-US"}]{#struct_0_x1489_93403_1807976608}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1807845536}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*

[[Notified interface *fc-interface-name* of interface *sagg-interface-name* to leave the SAN aggregation group.]{lang="EN-US"}]{#struct_0_x1489_93403_1808238752}

[[通知成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_1807386784}[离开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}

[[Received a link up event for interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1807911071}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1807779999}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received a link down event for interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1808238751}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1808107679}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[链路]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received an active event for interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1807452319}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1807779998}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[激活事件]{style="font-family:宋体"}

[[Received a deactive event for interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1808173214}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1808042142}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[取消激活事件]{style="font-family:宋体"}

[[Received an event for deleting  interface *fc-interface-name* of interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_1807452318}

[[收到]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1807976605}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[删除事件]{style="font-family:宋体"}

[[The physical state of interface *sagg-interface-name* became up with *fc-mode* mode.]{lang="EN-US"}]{#struct_0_x1489_93403_1807845533}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1808042141}[聚合组]{style="font-family:宋体"}*[sagg-interface-name fc-mode]{lang="EN-US"}*[模式物理状态]{style="font-family:
  宋体"}[UP]{lang="EN-US"}

[[The physical state of interface *sagg-interface-name* became down.]{lang="EN-US"}]{#struct_0_x1489_93403_1807386781}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1807911068}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[物理状态]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[The speed of interface *sagg-interface-name* changed to *speed-number* Gbps.]{lang="EN-US"}]{#struct_0_x1489_93403_1807845532}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_1808238748}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[速率变为]{style="font-family:宋体"}*[speed-number Gbps]{lang="EN-US"}*

[[Created a retransmission timer and retransmission began.]{lang="EN-US"}]{#struct_0_x1489_93403_1807386780}

[[创建重传定时器并且开始重传]{style="font-family:宋体"}]{#struct_0_x1489_93403_1807911067}

[[Deleted the retransmission timer and retransmission finished.]{lang="EN-US"}]{#struct_0_x1489_93403_1807779995}

[[删除重传定时器并且结束重传]{style="font-family:宋体"}]{#struct_0_x1489_93403_1808238747}

[[Successfully set local-first load sharing mode.]{lang="EN-US"}]{#struct_0_x1489_93403_1808107675}

[[设置本地转发优先模式成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_1807452315}

[[Interface *fc-interface-name* joined the SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_241696059}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_242089275}[接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}*[sagg-interface-number]{lang="EN-US"}*

[[Interface *fc-interface-name* leaved the SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_242023739}

[[成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_241368379}[离开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*

[[Successfully notified the physical state of interface sagg-interface-name to become up.]{lang="EN-US"}]{#struct_0_x1489_93403_241892666}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_242089274}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[物理]{style="font-family:宋体"}[UP]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Successfully notified the physical state of interface *sagg-interface-name* to become down.]{lang="EN-US"}]{#struct_0_x1489_93403_241958202}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241368378}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[物理]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Successfully notified the speed of interface *sagg-interface-name* to be changed.]{lang="EN-US"}]{#struct_0_x1489_93403_241892665}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241761593}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[速率变化成功]{style="font-family:宋体"}

[[Successfully notified shutdown event for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_241958201}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241302841}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[ shutdown]{lang="EN-US"}[事件成功]{style="font-family:宋体"}

[[Successfully notified undo-shutdown event for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_241892664}

[[通知]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241761592}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[ undo-shutdown]{lang="EN-US"}[事件成功]{style="font-family:宋体"}

[[Received phyIoCtl event *event-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_242154808}

[[收到物理控制事件]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*]{#struct_0_x1489_93403_241302840}

[[Successfully created the SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_241827127}

[[创建]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241761591}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[[Successfully deleted the SAN aggregation group for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_242154807}

[[删除]{style="font-family:宋体"}[FC]{lang="EN-US"}]{#struct_0_x1489_93403_242023735}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-59 ]{lang="EN-US"}[debugging san-aggregation selection]{lang="EN-US"}]{#struct_0_x1489_93403_241368375}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1920094806}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_241892662}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_241761590}

[[Began to determine Selected ports for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_242154806}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_241302838}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[开始进行成员接口选择]{style="font-family:宋体"}

[[Interface *fc-interface-name* became Selected in interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137182856}

[[成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x2137051784}[变为选中口]{style="font-family:宋体"}

[[Interface *fc-interface-name* became Unselected in interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136986248}

[[成员接口]{style="font-family:宋体"}*[fc-interface-name]{lang="EN-US"}*]{#struct_0_x1489_93403_x2136855176}[变为非选中口]{style="font-family:宋体"}

[[Notified Selected port change for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137772680}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x2137248393}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[通知选中口变化]{style="font-family:宋体"}

[[Selected ports did not change for interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136920713}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x2136789641}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[选中口没有变化]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-60 ]{lang="EN-US"}[debugging san-aggregation packet]{lang="EN-US"}]{#struct_0_x1489_93403_x2136855177}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1930160691}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2137772681}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2137051786}

[[Interface *sagg-interface-name* sent a packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136920714}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x2136789642}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[发送报文]{style="font-family:宋体"}

[[Interface *sagg-interface-name* received a packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137707146}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x2137248395}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[接收报文]{style="font-family:宋体"}

[[The SAN aggregation group for interface *sagg-interface-name* had no selected member and discarded the packet.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137117323}

[[FC]{lang="EN-US"}]{#struct_0_x1489_93403_x2136986251}[聚合组]{style="font-family:宋体"}*[sagg-interface-name]{lang="EN-US"}*[没有选中口，因此丢弃该报文]{style="font-family:宋体"}

[[Successfully relayed the packet from interface *sagg-interface-name* to the active MPU.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136855179}

[[透传报文到主板成功]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2137182860}

[[Failed to relay the packet from interface *sagg-interface-name* to the active MPU.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137051788}

[[透传报文到主板失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2136920716}

[[Received the packet from interface *sagg-interface-name* on slot *slot-number*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136855180}

[*[slot-number]{lang="EN-US"}*]{#struct_0_x1489_93403_x2137772684}[板收到报文]{style="font-family:宋体"}

[[The active MPU successfully received relayed packet from interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2137248397}

[[主板成功收到透传报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2137117325}

[[The active MPU discarded the relayed packet from interface *sagg-interface-name*.]{lang="EN-US"}]{#struct_0_x1489_93403_x2136789645}

[[主板丢弃透传报文]{style="font-family:宋体"}]{#struct_0_x1489_93403_x2137707149}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2137772685}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_591700499}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的错误调试信息开关。当]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组失败时会输出下列调试信息。]{style="font-family:宋体"}

[[\<sysname\> debugging san-aggregation error]{lang="EN-US"}]{#struct_0_x1489_93403_591897107}

[\*Feb  3 07:38:14:512 2013 Sysname FCAGG/7/ERROR: -MDC=1; Failed to add interface fc1/0/1 to SAN aggregation group for interface SAN-Aggregation1.]{lang="EN-US"}

[*[// FC]{lang="EN-US"}*]{#struct_0_x1489_93403_591110675}*[接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}[1]{lang="EN-US"}[失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_592093714}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的事件调试信息开关。当配置]{style="font-family:宋体"}[FC]{lang="EN-US"}[接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}[1]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<sysname\> debugging san-aggregation event]{lang="EN-US"}]{#struct_0_x1489_93403_591634961}

[\*Feb  3 07:44:10:356 2013 Sysname FCAGG/7/EVENT: -MDC=1; Interface fc1/0/1 joined the SAN aggregation group for interface SAN-Aggregation1.]{lang="EN-US"}

[*[// FC]{lang="EN-US"}*]{#struct_0_x1489_93403_591897105}*[接口]{style="font-family:宋体"}[FC1/0/1]{lang="EN-US"}[加入]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_592093713}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的成员接口选中调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。当]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组内成员接口链路]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging san-aggregation selection]{lang="EN-US"}]{#struct_0_x1489_93403_591176209}

[\*Feb  3 07:57:38:487 2013 Sysname FCAGG/7/SELECTION: -MDC=1; Began to determine Selected ports for interface SAN-Aggregation2.]{lang="EN-US"}

[*[// FC]{lang="EN-US"}*]{#struct_0_x1489_93403_591110673}*[聚合组]{style="font-family:宋体"}[2]{lang="EN-US"}[开始进行成员接口选择]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_591700496}[打开]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组的报文调试信息]{style="font-family:宋体"}[开关]{style="font-family:宋体"}[。当]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组]{style="font-family:宋体"}[2]{lang="EN-US"}[和对端]{style="font-family:宋体"}[FC]{lang="EN-US"}[聚合组链路协商时，会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging san-aggregation packet]{lang="EN-US"}]{#struct_0_x1489_93403_591634960}

[\*Feb  3 07:57:38:488 2013 Sysname FCAGGK/7/PACKET: -MDC=1; Interface SAN-Aggregation2 sent a packet.]{lang="EN-US"}

[*[// FC]{lang="EN-US"}*]{#struct_0_x1489_93403_591766032}*[聚合组]{style="font-family:宋体"}[2]{lang="EN-US"}[发送协商报文]{style="font-family:宋体"}*

::: {#-1784775968 .myid}
[]{#_Toc404797597}[]{#struct_0_x1489_93403_2016526182}

**FC和FCoE \-- FC和FCoE调试命令 \-- debugging vsan**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1489_93403_764142069}

[**[debugging vsan]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1489_93403_x1135466140}

[**[undo debugging vsan]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x1489_93403_x509692154}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x600573021}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1489_93403_603421865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1489_93403_1749326897}

[[network-admin]{lang="EN-US"}]{#struct_0_x1489_93403_x1525839795}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1489_93403_1927646278}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x506967455}

[**[all]{lang="FR"}**]{#struct_0_x1489_93403_136794002}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="FR"}**]{#struct_0_x1489_93403_x600507485}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="FR"}**]{#struct_0_x1489_93403_x2141958373}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1489_93403_x2121967114}

[**[debugging vsan]{lang="FR"}**]{#struct_0_x1489_93403_x2123134706}[命令用来打开]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[vsan]{lang="FR"}**[命令用来关闭]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_688627417}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-61 ]{lang="EN-US"}[debugging vsan error]{lang="EN-US"}]{#struct_0_x1489_93403_x625791974}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1552514253}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_x601097312}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1728335439}

[[Failed to add event *eventtype* notify node of module *module-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x435956178}

[[为模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x1985087043}[添加事件]{style="font-family:宋体"}*[eventtype]{lang="EN-US"}*[通知结点失败]{style="font-family:宋体"}

[[Failed to push *event* event in VSAN *vsan-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_x601031776}

[[推送]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x179084009}[内的]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件失败]{style="font-family:宋体"}

[[Failed to notify module *module-id* of *event* event with priority *priority* in VSAN *vsan-id* in user space.]{lang="EN-US"}]{#struct_0_x1489_93403_x98905081}

[[向用户态模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_x1489_93403_1706574853}[通知]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内的优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to notify the driver of the VSAN *vsan-id* creation event, and error code *err-code*.]{lang="EN-US"}]{#struct_0_x1489_93403_x600966240}

[[通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x180233480}[创建事件失败，且错误码为]{style="font-family:宋体"}*[err-code]{lang="EN-US"}*

[[Failed to notify the driver of the VSAN *vsan-id* deletion event, and error code *err-code*.]{lang="EN-US"}]{#struct_0_x1489_93403_x1696608347}

[[通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x600900704}[删除事件失败，且错误码为]{style="font-family:宋体"}*[err-code]{lang="EN-US"}*

[[Failed to receive FC response message from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_217706950}

[[从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x611840237}[接收]{style="font-family:宋体"}[FC]{lang="EN-US"}[响应消息失败]{style="font-family:宋体"}

[[Failed to receive FC request message from socket *socket-id*.]{lang="EN-US"}]{#struct_0_x1489_93403_1505612579}

[[从]{style="font-family:宋体"}[socket *socket-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x601359456}[接收]{style="font-family:宋体"}[FC]{lang="EN-US"}[请求消息失败]{style="font-family:宋体"}

[[Failed to reply to synchronous message.]{lang="EN-US"}]{#struct_0_x1489_93403_2137524878}

[[回应同步消息失败]{style="font-family:宋体"}]{#struct_0_x1489_93403_1061303890}

[[Failed to synchronize VSAN to IO board.]{lang="EN-US"}]{#struct_0_x1489_93403_x601293920}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1489_93403_1786149922}[板同步]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[配置失败]{style="font-family:宋体"}

[[Failed to synchronize VSAN debug to IO board.]{lang="EN-US"}]{#struct_0_x1489_93403_1052591895}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1489_93403_x601228384}[板同步]{style="font-family:宋体"}[VSAN debug]{lang="EN-US"}[配置失败]{style="font-family:宋体"}

[[Failed to synchronize fabric debug to IO board.]{lang="EN-US"}]{#struct_0_x1489_93403_x1785686641}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1489_93403_1179453430}[板同步]{style="font-family:宋体"}[Fabric debug]{lang="EN-US"}[配置失败]{style="font-family:宋体"}

[[Failed to synchronize timer configuration to IO board.]{lang="EN-US"}]{#struct_0_x1489_93403_x601162848}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1489_93403_1425606564}[板同步定时器配置失败]{style="font-family:宋体"}

[[Failed to synchronize the VSAN mode to the IO board.]{lang="EN-US"}]{#struct_0_x1489_93403_311212941}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1489_93403_1878702985}[板同步]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[模式失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-62 ]{lang="EN-US"}[debugging vsan event]{lang="EN-US"}]{#struct_0_x1489_93403_1764248162}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1549323341}[[字段]{style="font-family:黑体"}]{#struct_0_x1489_93403_479047479}

[[描述]{style="font-family:黑体"}]{#struct_0_x1489_93403_1878726288}

[[VSAN *vsan-id* was successfully created]{lang="EN-US"}]{#struct_0_x1489_93403_x600573024}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_603094185}[被成功创建]{style="font-family:宋体"}

[[VSAN *vsan-id* was successfully deleted]{lang="EN-US"}]{#struct_0_x1489_93403_501121957}

[[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x600507488}[被成功删除]{style="font-family:宋体"}

[[Successfully notified the driver of the VSAN *vsan-id* creation event.]{lang="EN-US"}]{#struct_0_x1489_93403_x2141106405}

[[通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_394217686}[创建事件成功]{style="font-family:宋体"}

[[Notifying the driver of the VSAN creation event was not supported.]{lang="EN-US"}]{#struct_0_x1489_93403_x1282768999}

[[不支持通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x601097311}[创建事件]{style="font-family:宋体"}

[[Successfully notified the driver of the VSAN *vsan-id* deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_1728532047}

[[通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1088101486}[删除事件成功]{style="font-family:宋体"}

[[Notifying the driver of the VSAN deletion event was not supported.]{lang="EN-US"}]{#struct_0_x1489_93403_1079569382}

[[不支持通知驱动]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_x601031775}[删除事件]{style="font-family:宋体"}

[[Notified module *module-id* of *event* event with priority *priority* in VSAN *vsan-id* in user space]{lang="EN-US"}]{#struct_0_x1489_93403_x179149545}

[[向用户态模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x15144827}[通知]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内的优先级为]{style="font-family:宋体"}*[priority]{lang="EN-US"}*[的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01]{lang="EN-US"}]{#struct_0_x1489_93403_x600966239}[：]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}[创建事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02]{lang="EN-US"}]{#struct_0_x1489_93403_x180823299}[：]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}[删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x04]{lang="EN-US"}]{#struct_0_x1489_93403_x1308372774}[：域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x08]{lang="EN-US"}]{#struct_0_x1489_93403_x600900703}[：]{lang="EN-US" style="font-family:宋体"}[fabric name]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[Created kernel VSAN data in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_218034630}

[[创建]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_611341188}[的内核数据]{style="font-family:宋体"}

[[Destroyed kernel VSAN data in VSAN *vsan-id*]{lang="EN-US"}]{#struct_0_x1489_93403_1631941257}

[[删除]{style="font-family:宋体"}[VSAN]{lang="EN-US"}]{#struct_0_x1489_93403_x601359455}[的内核数据]{style="font-family:宋体"}

[[Notified the kernel module *module-id* of the VSAN *vsan-id* event *event*.]{lang="EN-US"}]{#struct_0_x1489_93403_2137721486}

[[向内核模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_x1489_93403_x1635609640}[通知]{style="font-family:宋体"}[VSAN *vsan-id*]{lang="EN-US"}[内的事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[.]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01]{lang="EN-US"}]{#struct_0_x1489_93403_x601293919}[：]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}[创建事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02]{lang="EN-US"}]{#struct_0_x1489_93403_1785691173}[：]{lang="EN-US" style="font-family:宋体"}[VSAN]{lang="EN-US"}[删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x04]{lang="EN-US"}]{#struct_0_x1489_93403_x1203639355}[：域]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x08]{lang="EN-US"}]{#struct_0_x1489_93403_x601228383}[：]{lang="EN-US" style="font-family:宋体"}[fabric name]{lang="EN-US"}[变化事件]{lang="EN-US" style="font-family:宋体"}

[[Received EPort deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_x1785621105}

[[收到]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_799704407}[端口删除事件]{style="font-family:宋体"}

[[Received EPort active event.]{lang="EN-US"}]{#struct_0_x1489_93403_x601162847}

[[收到]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_1426196388}[端口激活事件]{style="font-family:宋体"}

[[Received EPort deactive event.]{lang="EN-US"}]{#struct_0_x1489_93403_1229474435}

[[收到]{style="font-family:宋体"}[E]{lang="EN-US"}]{#struct_0_x1489_93403_x600573023}[端口去激活事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1489_93403_603552937}

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_1754277639}[打开]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[错误调试信息开关。创建]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[失败时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vsan error]{lang="EN-US"}]{#struct_0_x1489_93403_x1466370796}

[\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/ERROR: -MDC=1; Failed to notify module 134348800 of VSAN deletion event with priority 64 in VSAN 2 in user space.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x600507487}*[向用户态模块]{style="font-family:宋体"}[134348800]{lang="EN-US"}[通知]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[删除事件失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1489_93403_x2141827301}[打开]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[事件调试信息开关。删除]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[时会输出下列调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging vsan event]{lang="EN-US"}]{#struct_0_x1489_93403_x1441985713}

[\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Notified module 134348800 of VSAN deletion event with priority 64 in VSAN 2 in user space.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x1489_93403_x454743542}*[向用户态模块]{style="font-family:宋体"}[134348800]{lang="EN-US"}[通知]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[内的优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[的]{style="font-family:宋体"}[VSAN]{lang="EN-US"}[删除事件]{style="font-family:宋体"}*

[[\*Jun 23 16:42:36:222 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; Successfully notified the driver of the VSAN 2 deletion event.]{lang="EN-US"}]{#struct_0_x1489_93403_x335899433}

[*[// ]{lang="EN-US"}*]{#struct_0_x1489_93403_x186510507}*[通知驱动]{style="font-family:宋体"}[VSAN 2]{lang="EN-US"}[被删除]{style="font-family:宋体"}*

[[\*Jun 23 16:42:36:224 2011 Sysname FCFABRIC/7/EVENT: -MDC=1; VSAN 2 was successfully deleted.]{lang="EN-US"}]{#struct_0_x1489_93403_964986633}

[*[// VSAN 2]{lang="EN-US"}*]{#struct_0_x1489_93403_x492788026}*[被成功删除]{style="font-family:宋体"}*
