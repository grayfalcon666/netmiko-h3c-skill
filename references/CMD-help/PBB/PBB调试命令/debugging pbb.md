::: {#-1483065727 .myid}
[]{#_Toc404784315}[]{#struct_0_32539_x9819_x2092755736}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**PBB \-- PBB调试命令 \-- debugging pbb**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1534077497}

[**[debugging pbb ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_32539_x9819_733292572}

[**[undo debugging pbb ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_32539_x9819_1580774777}

[[【视图】]{style="font-family:黑体"}]{#struct_0_32539_x9819_742476149}

[[用户视图]{style="font-family:宋体"}]{#struct_0_32539_x9819_x1377923543}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1250698044}

[[network-admin]{lang="EN-US"}]{#struct_0_32539_x9819_1754850522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_32539_x9819_x1113250806}

[[【参数】]{style="font-family:黑体"}]{#struct_0_32539_x9819_1426628904}

[**[all]{lang="EN-US"}**]{#struct_0_32539_x9819_851040374}[：表示]{style="font-family:宋体"}[PBB]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_32539_x9819_1855045748}[：表示]{style="font-family:宋体"}[PBB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_32539_x9819_50650638}[：表示]{style="font-family:宋体"}[PBB]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_32539_x9819_1886626140}[：表示]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1785241502}

[**[debugging pbb]{lang="EN-US"}**]{#struct_0_32539_x9819_1265342072}[命令用来打开]{style="font-family:宋体"}[PBB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging pbb]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[PBB]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_32539_x9819_938687780}[的所有调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging pbb error]{lang="EN-US"}]{#struct_0_32539_x9819_1754916058}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2089646902}[[字段]{style="font-family:黑体"}]{#struct_0_32539_x9819_892168266}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_32539_x9819_1042822755}

[[Failed to get VSI block.]{lang="EN-US"}]{#struct_0_32539_x9819_x52930149}

[[获取]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_x1471515224}[控制块失败]{style="font-family:宋体"}

[[The interface *interface-name* isn\'t enabled to receive PBB packet.]{lang="EN-US"}]{#struct_0_32539_x9819_x1163906756}

[[该]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_x1145806899}[的接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[没有使能接收]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The Unicast Pseudo Wire entry has already been learned.]{lang="EN-US"}]{#struct_0_32539_x9819_1755243738}

[[已经学习该单播表项]{style="font-family:宋体"}]{#struct_0_32539_x9819_78956416}

[[The number of Unicast Pseudo Wire entries in this VSI (VsiIndex *n*) has reached the upper limit.]{lang="EN-US"}]{#struct_0_32539_x9819_x1632054391}

[[已达到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_699857394}[索引为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[表项个数的上限]{style="font-family:宋体"}

[[The total number of Unicast Pseudo Wire entries has reached the upper limit.]{lang="EN-US"}]{#struct_0_32539_x9819_677829774}

[[已达到设备可以学习的最大的单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_x1656857014}[表项个数上限]{style="font-family:宋体"}

[[Failed to learn the Unicast Pseudo Wire entry.]{lang="EN-US"}]{#struct_0_32539_x9819_x1173369531}

[[学习单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_1755309274}[表项失败]{style="font-family:宋体"}

[[The STG state of interface *interface-name* is not forwarding.]{lang="EN-US"}]{#struct_0_32539_x9819_x1115138703}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_248928272}[的]{style="font-family:宋体"}[STG]{lang="EN-US"}[状态为非转发状态]{style="font-family:宋体"}

[[Failed to add Multicast Pseudo Wire entries to driver.]{lang="EN-US"}]{#struct_0_32539_x9819_4489591}

[[添加组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_x1492264016}[表项到驱动失败]{style="font-family:宋体"}

[[Failed to add Multicast Pseudo Wire port to driver.]{lang="EN-US"}]{#struct_0_32539_x9819_1755112666}

[[添加组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_853425089}[表项中的出端口到驱动失败]{style="font-family:宋体"}

[[Failed to delete Multicast Pseudo Wire entries from driver.]{lang="EN-US"}]{#struct_0_32539_x9819_x1009504532}

[[从驱动删除组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_1302431787}[表项失败]{style="font-family:宋体"}

[[Failed to delete Multicast Pseudo Wire port from driver.]{lang="EN-US"}]{#struct_0_32539_x9819_x250832887}

[[从驱动删除组播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_1656162783}[表项中的出端口失败]{style="font-family:宋体"}

[[Failed to add Unicast Pseudo Wire entries to driver.]{lang="EN-US"}]{#struct_0_32539_x9819_1755178202}

[[添加单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_1596901833}[表项到驱动失败]{style="font-family:宋体"}

[[Failed to delete Unicast Pseudo Wire entries from driver.]{lang="EN-US"}]{#struct_0_32539_x9819_x637476117}

[[从驱动删除单播]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_32539_x9819_x1855260323}[表项失败]{style="font-family:宋体"}

[[Failed to enable the interface PBB mode.]{lang="EN-US"}]{#struct_0_32539_x9819_x792368099}

[[使能接口]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_32539_x9819_1755505882}[模式失败]{style="font-family:宋体"}

[[Failed to disable the interface PBB mode.]{lang="EN-US"}]{#struct_0_32539_x9819_x1413292690}

[[关闭接口]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_32539_x9819_x1841588521}[模式失败]{style="font-family:宋体"}

[[The I-SID of this PBB packet is not the same as configured.]{lang="EN-US"}]{#struct_0_32539_x9819_x2060949438}

[[PBB]{lang="EN-US"}]{#struct_0_32539_x9819_1755571418}[报文的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和配置值不符]{style="font-family:宋体"}

[[The B-VLAN of this PBB packet is not the same as configured.]{lang="EN-US"}]{#struct_0_32539_x9819_x1106530351}

[[PBB]{lang="EN-US"}]{#struct_0_32539_x9819_229196193}[报文的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[和配置值不符]{style="font-family:宋体"}

[[Failed to learn PBB packet because the VSI is administratively down.]{lang="EN-US"}]{#struct_0_32539_x9819_1644615237}

[[由于]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_x984160831}[被手工关闭导致学习]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[Failed to allocate memory for VLAN map on interface *interface-name.*]{lang="EN-US"}]{#struct_0_32539_x9819_1754981595}

[[为接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_482979669}[上的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[位图分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for control block on interface *interface-name.*]{lang="EN-US"}]{#struct_0_32539_x9819_330577411}

[[为接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_407563768}[上的控制块分配内存失败]{style="font-family:宋体"}

[[Failed to set private data on interface *interface-name.*]{lang="EN-US"}]{#struct_0_32539_x9819_1755047131}

[[设置接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_900854998}[上的控制块失败]{style="font-family:宋体"}

[[Failed to allocate memory for Multicast Pseudo Wire entry with VsiIndex *vsi-index*, I-SID *i-sid*, B-VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_32539_x9819_x792634662}

[[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_580253908}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的组播表项分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for Unicast Pseudo Wire interface control block on interface *interface-name.*]{lang="EN-US"}]{#struct_0_32539_x9819_1754850523}

[[为接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_x1113316342}[上的单播表项接口控制块分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for Unicast Pseudo Wire entry with VsiIndex *vsi-index,* I-SID *i-sid,* B-VLAN *vlan-id*, B-MAC *mac-address* on interface *interface-name.*]{lang="EN-US"}]{#struct_0_32539_x9819_x72634677}

[[为接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_1648629721}[上的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}[为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[的单播表项分配内存失败]{style="font-family:宋体"}

[[Failed to recognize an invalid TLV. Keep on processing the next one.]{lang="EN-US"}]{#struct_0_32539_x9819_1754916059}

[[识别无效的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_32539_x9819_892102730}[失败。继续处理下一个]{style="font-family:宋体"}[TLV]{lang="EN-US"}

[[Failed to allocate memory for control block on VSI (VsiIndex *vsi-index*).]{lang="EN-US"}]{#struct_0_32539_x9819_x140846898}

[[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_x2050795977}[（]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[）的控制块分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for uplink node for VSI (VsiIndex *vsi-index*).]{lang="EN-US"}]{#struct_0_32539_x9819_1755243739}

[[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_79021952}[（]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[）的上行口节点分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for hash node for VSI (VsiIndex *vsi-index*).]{lang="EN-US"}]{#struct_0_32539_x9819_471030383}

[[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_x1008692688}[（]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[vsi-index]{lang="EN-US"}*[）的]{style="font-family:宋体"}[hash]{lang="EN-US"}[节点分配内存失败]{style="font-family:宋体"}

[[Failed to set ethernet type.]{lang="EN-US"}]{#struct_0_32539_x9819_159543234}

[[设置报文封装模式失败]{style="font-family:宋体"}]{#struct_0_32539_x9819_1016950510}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging pbb event]{lang="EN-US"}]{#struct_0_32539_x9819_455124366}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2032335400}[[字段]{style="font-family:黑体"}]{#struct_0_32539_x9819_509063800}

[[描述]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1343773801}

[[Receive event: *event* on the interface *interface-name*.]{lang="EN-US"}]{#struct_0_32539_x9819_1755112667}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_853359553}[收到事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[。]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[为接口名，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[nterface]{lang="EN-US"}]{#struct_0_32539_x9819_x1323374758}[\_]{lang="EN-US"}[active]{lang="EN-US"}[：接口激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[nterface]{lang="EN-US"}]{#struct_0_32539_x9819_x911578831}[\_d]{lang="EN-US"}[eactive]{lang="EN-US"}[：接口去激活事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[i]{lang="EN-US"}[nterface]{lang="EN-US"}]{#struct_0_32539_x9819_654800725}[\_d]{lang="EN-US"}[elete]{lang="EN-US"}[：接口删除事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[nterface]{lang="EN-US"}]{#struct_0_32539_x9819_x1348935860}[\_u]{lang="EN-US"}[p]{lang="EN-US"}[：接口链路]{lang="EN-US" style="font-family:宋体"}[UP]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[i]{lang="EN-US"}[nterface]{lang="EN-US"}]{#struct_0_32539_x9819_1482876203}[\_d]{lang="EN-US"}[own]{lang="EN-US"}[：接口链路]{lang="EN-US" style="font-family:宋体"}[DOWN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[Receive the event that interface *interface-name1* *event* the aggregate interface *interface-name2*.]{lang="EN-US"}]{#struct_0_32539_x9819_1755178203}

[[收到接口]{style="font-family:宋体"}*[interface-name1]{lang="EN-US"}*]{#struct_0_32539_x9819_1596836297}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[退出聚合接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[2]{lang="EN-US"}[事件。]{style="font-family:宋体"}*[interface-name1]{lang="EN-US"}*[为接口名，]{style="font-family:宋体"}*[interface-name2]{lang="EN-US"}*[为聚合接口名，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[j]{lang="EN-US"}[oin]{lang="EN-US"}]{#struct_0_32539_x9819_868499683}[ ]{lang="EN-US"}[in]{lang="EN-US"}[：接口加入聚合]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[eave]{lang="EN-US"}]{#struct_0_32539_x9819_1731296090}[ ]{lang="EN-US"}[from]{lang="EN-US"}[：]{style="font-family:宋体"}[接口离开聚合]{lang="EN-US" style="font-family:宋体"}

[[Receive vsi_add event: VsiIndex *vsiindex*, VsiName *vsiname*, PBB I-SID *pbbisid*, ShutdownFlag *flag*.]{lang="EN-US"}]{#struct_0_32539_x9819_x529650657}

[[收到]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_32539_x9819_482673054}[添加事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[vsiindex]{lang="EN-US"}*]{#struct_0_32539_x9819_1755505883}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}*[vsiname]{lang="EN-US"}*]{#struct_0_32539_x9819_x1413227154}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}*[pbbisid]{lang="EN-US"}*]{#struct_0_32539_x9819_925358397}[：]{style="font-family:宋体"}[PBB I-SID ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[flag]{lang="EN-US"}*]{#struct_0_32539_x9819_1912726720}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[是否]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}

[[Receive *event* event: VsiIndex *vsiindex*, VsiName *vsiname*.]{lang="EN-US"}]{#struct_0_32539_x9819_140439036}

[[收到]{style="font-family:宋体"}[VSI UP/DOWN/Delete]{lang="EN-US"}]{#struct_0_32539_x9819_1755571419}[事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[event]{lang="EN-US"}*]{#struct_0_32539_x9819_x1106595887}[：]{lang="EN-US" style="font-family:宋体"}[v]{lang="EN-US"}[si\_]{lang="EN-US"}[u]{lang="EN-US"}[p]{lang="EN-US"}[、]{style="font-family:宋体"}[v]{lang="EN-US"}[si\_]{lang="EN-US"}[d]{lang="EN-US"}[own]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[v]{lang="EN-US"}[si\_]{lang="EN-US"}[d]{lang="EN-US"}[el]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsiindex]{lang="EN-US"}*]{#struct_0_32539_x9819_x1942706108}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsiname]{lang="EN-US"}*]{#struct_0_32539_x9819_x2071232421}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名字]{lang="EN-US" style="font-family:宋体"}

[[Receive vsi_modify_pbb_i-sid event: VsiIndex *vsiindex*, VsiName *vsiname*, PBB I-SID *pbbisid.*]{lang="EN-US"}]{#struct_0_32539_x9819_x503071535}

[[收到]{style="font-family:宋体"}[VSI PBB]{lang="EN-US"}]{#struct_0_32539_x9819_1172792603}[模式改变事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsiindex]{lang="EN-US"}*]{#struct_0_32539_x9819_1754981592}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[vsiname]{lang="EN-US"}*]{#struct_0_32539_x9819_483307349}[：]{lang="EN-US" style="font-family:宋体"}[VSI]{lang="EN-US"}[名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pbbisid]{lang="EN-US"}*]{#struct_0_32539_x9819_1214346428}[：]{lang="EN-US" style="font-family:宋体"}[PBB I-SID]{lang="EN-US"}

[[Receive *event* event.]{lang="EN-US"}]{#struct_0_32539_x9819_x1224282496}

[[收到]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_32539_x9819_x1447612029}[事件，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[2vpn\_]{lang="EN-US"}]{#struct_0_32539_x9819_1755047128}[d]{lang="EN-US"}[isable]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[2vpn\_]{lang="EN-US"}]{#struct_0_32539_x9819_901313749}[b]{lang="EN-US"}[atch\_]{lang="EN-US"}[b]{lang="EN-US"}[egin]{lang="EN-US"}[：批备开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[l]{lang="EN-US"}[2vpn\_]{lang="EN-US"}]{#struct_0_32539_x9819_1003591602}[b]{lang="EN-US"}[atch\_]{lang="EN-US"}[e]{lang="EN-US"}[nd]{lang="EN-US"}[：批备结束事件]{lang="EN-US" style="font-family:宋体"}

[[Receive slot *slot-id* insert event.]{lang="EN-US"}]{#struct_0_32539_x9819_x696608798}

[[收到单板]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_32539_x9819_x1772125801}[插入事件。]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*[为单板所在的槽位号]{style="font-family:宋体"}

[[Receive slot *slot-id* remove event.]{lang="EN-US"}]{#struct_0_32539_x9819_1754850520}

[[收到单板]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_32539_x9819_x1113119734}[拔出事件。]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*[为单板所在的槽位号]{style="font-family:宋体"}

[[Slot *slot-id* does not support PBB.]{lang="EN-US"}]{#struct_0_32539_x9819_1666642733}

[[单板]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_32539_x9819_x655082306}[不支持]{style="font-family:宋体"}[PBB]{lang="EN-US"}[。]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*[为单板所在的槽位号]{style="font-family:宋体"}

[[Receive event: interface *interface-name* *event* VLAN *vlan-id.*]{lang="EN-US"}]{#struct_0_32539_x9819_1754916056}

[[收到事件：接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_891775050}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[退出]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[（单个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）。]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[为端口名，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN-ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[added to]{lang="EN-US"}]{#struct_0_32539_x9819_x479453525}[：端口加入]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleted from]{lang="EN-US"}]{#struct_0_32539_x9819_1443460892}[：端口退出]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Receive event: interface *interface-name* *event* VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_1755243736}

[[VLANs number: *vlan-number*]{lang="EN-US"}]{#struct_0_32539_x9819_78825344}

[[VLANs:*start* to *end.*]{lang="EN-US"}]{#struct_0_32539_x9819_x844809896}

[[收到事件：端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_1476799308}[加入]{style="font-family:宋体"}[/]{lang="EN-US"}[退出]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（批量]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[）。]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[为端口名，]{style="font-family:宋体"}*[vlan-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[个数，]{style="font-family:宋体"}*[start]{lang="EN-US"}*[为开始的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[值，]{style="font-family:宋体"}*[end]{lang="EN-US"}*[为结束的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[值，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[added]{lang="EN-US"}]{#struct_0_32539_x9819_1755309272}[ ]{lang="EN-US"}[to]{lang="EN-US"}[：端口加入]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deleted]{lang="EN-US"}]{#struct_0_32539_x9819_x1114745487}[ ]{lang="EN-US"}[from]{lang="EN-US"}[：端口退出]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Receive NoHardResource event with Unicast Pseudo Wire number *n*.]{lang="EN-US"}]{#struct_0_32539_x9819_x506125073}

[[No.   SlotId   VSIIndex  I-SID   B-MAC    B-VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_1755112664}

[*[number  SlotId  VsiIndex I-sid]{lang="EN-US"}*[ * mac-address    vlan-id*]{lang="EN-US"}]{#struct_0_32539_x9819_853556161}

[[收到硬件资源不足消息，]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_32539_x9819_x271533628}[为单播]{style="font-family:宋体"}[PW]{lang="EN-US"}[表项个数]{style="font-family:宋体"}

[[Receive *event* event from slot *slot-id* with VsiIndex *vsiindex*, I-SID *i-sid*, Unicast Pseudo Wire number *n.*]{lang="EN-US"}]{#struct_0_32539_x9819_x1393854727}

[[No.              B-MAC                B-VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_1755178200}

[*[number      mac-address        vlan-id]{lang="EN-US"}*]{#struct_0_32539_x9819_1596770761}

[[收到老化事件。]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_32539_x9819_x1476896699}[为板号，]{style="font-family:宋体"}*[vsiindex]{lang="EN-US"}*[为]{style="font-family:宋体"}*[VSI]{lang="EN-US"}*[索引，]{style="font-family:宋体"}*[i-sid]{lang="EN-US"}*[为]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为单播表项个数，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[为事件类型，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ged]{lang="EN-US"}]{#struct_0_32539_x9819_1755505880}[：老化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[c]{lang="EN-US"}[ancelled_aged]{lang="EN-US"}]{#struct_0_32539_x9819_x1413423762}[：不老化]{lang="EN-US" style="font-family:宋体"}

[[Receive TC event with all interfaces and all VLANs.]{lang="EN-US"}]{#struct_0_32539_x9819_1539424889}

[[收到所有接口和所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_1373979186}[的]{style="font-family:宋体"}[TC]{lang="EN-US"}[（]{style="font-family:宋体"}[Topology Change]{lang="EN-US"}[）事件]{style="font-family:宋体"}

[[Receive TC event]{lang="EN-US"}]{#struct_0_32539_x9819_562762225}

[[Interfaces number: *interface-number*]{lang="EN-US"}]{#struct_0_32539_x9819_1113001180}

[[Interfaces:]{lang="EN-US"}]{#struct_0_32539_x9819_827953282}

[*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_354760579}

[[VLANs number: *vlan-number*]{lang="EN-US"}]{#struct_0_32539_x9819_1191435709}

[[VLANs:]{lang="EN-US"}]{#struct_0_32539_x9819_760067578}

[*[start ]{lang="EN-US"}*[to *end*]{lang="EN-US"}]{#struct_0_32539_x9819_x1003321716}

[[收到指定接口和指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_928151417}[的]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface-number]{lang="EN-US"}]{#struct_0_32539_x9819_x1658951842}[：为接口个数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface-name]{lang="EN-US"}]{#struct_0_32539_x9819_1725561639}[：接口名字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[vlan-number]{lang="EN-US"}]{#struct_0_32539_x9819_x584996904}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[start]{lang="EN-US"}]{#struct_0_32539_x9819_159477698}[：开始的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[end]{lang="EN-US"}]{#struct_0_32539_x9819_1037844873}[：结束的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[值]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging pbb packet]{lang="EN-US"}]{#struct_0_32539_x9819_x900122213}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1711505416}[[字段]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1800403030}

[[描述]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1886053289}

[[Receive PBB frame from *interface-name*]{lang="EN-US"}]{#struct_0_32539_x9819_x476076875}

[[从端口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_32539_x9819_1754850521}[收到]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[B-DA]{lang="EN-US"}]{#struct_0_32539_x9819_x1113185270}

[[目的]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}]{#struct_0_32539_x9819_x663361881}[地址]{style="font-family:宋体"}

[[B-SA]{lang="EN-US"}]{#struct_0_32539_x9819_443585941}

[[源]{style="font-family:宋体"}[B-MAC]{lang="EN-US"}]{#struct_0_32539_x9819_x90034450}[地址]{style="font-family:宋体"}

[[B-Tag TPID]{lang="EN-US"}]{#struct_0_32539_x9819_x660683923}

[[B-Tag]{lang="EN-US"}]{#struct_0_32539_x9819_x1438154924}[类型]{style="font-family:宋体"}

[[B-VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_1754916057}

[[B-VLAN]{lang="EN-US"}]{#struct_0_32539_x9819_891709514}[值]{style="font-family:宋体"}

[[I-Tag TPID]{lang="EN-US"}]{#struct_0_32539_x9819_x92111741}

[[I-Tag]{lang="EN-US"}]{#struct_0_32539_x9819_1044286523}[类型]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_32539_x9819_x977106828}

[[I-SID]{lang="EN-US"}]{#struct_0_32539_x9819_x1787118180}[值]{style="font-family:宋体"}

[[C-DA]{lang="EN-US"}]{#struct_0_32539_x9819_1755243737}

[[目的]{style="font-family:宋体"}[C-MAC]{lang="EN-US"}]{#struct_0_32539_x9819_78890880}[地址]{style="font-family:宋体"}

[[C-SA]{lang="EN-US"}]{#struct_0_32539_x9819_x1406606243}

[[源]{style="font-family:宋体"}[C-MAC]{lang="EN-US"}]{#struct_0_32539_x9819_1693593818}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_32539_x9819_x1899038754}

[[\# ]{lang="EN-US"}]{#struct_0_32539_x9819_x421651340}[配置好]{style="font-family:宋体"}[PBB]{lang="EN-US"}[功能，并打开]{style="font-family:宋体"}[PBB]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pbb error]{lang="EN-US"}]{#struct_0_32539_x9819_1755309273}

[\*Oct 24 14:23:58:531 2012 Sysname PBB/7/Error: The B-VLAN of this PBB packet is not the same as configured.]{lang="EN-US"}

[*[// PBB]{lang="EN-US"}*]{#struct_0_32539_x9819_x1114679951}*[报文所携带的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[与配置不相符，单播表项学习失败]{style="font-family:宋体"}*

[[\*Oct 24 14:27:16:968 2012 Sysname PBB/7/Error: The I-SID of this PBB packet is not the same as configured.]{lang="EN-US"}]{#struct_0_32539_x9819_983327061}

[*[// PBB]{lang="EN-US"}*]{#struct_0_32539_x9819_x1896860956}*[报文所携带的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[与配置不相符，单播表项学习失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_32539_x9819_1895723480}[配置好]{style="font-family:宋体"}[PBB]{lang="EN-US"}[功能，并打开]{style="font-family:宋体"}[PBB]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pbb event]{lang="EN-US"}]{#struct_0_32539_x9819_1996421747}

[\*Oct 24 14:36:35:312 2012 Sysname PBB/7/Event: Receive vsi_add event: VsiIndex 0, VsiName aaa, PBB I-SID 1, ShutdownFlag 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_32539_x9819_867820426}*[处理]{style="font-family:宋体"}[VSI]{lang="EN-US"}[添加事件成功（即创建]{style="font-family:宋体"}[VSI]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Oct 24 14:36:35:312 2009 Sysname PBB/7/Event: Receive slot 9 insert event.]{lang="EN-US"}]{#struct_0_32539_x9819_x1470095041}

[*[// ]{lang="EN-US"}*]{#struct_0_32539_x9819_x167537074}*[处理板插入事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_32539_x9819_1755112665}[配置好]{style="font-family:宋体"}[PBB]{lang="EN-US"}[功能，并打开]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging pbb packet]{lang="EN-US"}]{#struct_0_32539_x9819_853490625}

[\*Oct 24 11:20:41:453 2012 Sysname PBB/7/Packet:]{lang="EN-US"}

[ Receive PBB frame from GigabitEthernet1/0/1]{lang="EN-US"}

[ B-DA: 0102-0304-0506]{lang="EN-US"}

[ B-SA: 0605-0403-0206]{lang="EN-US"}

[ B-Tag TPID: 0x8100]{lang="EN-US"}

[ B-VLAN: 20]{lang="EN-US"}

[ I-Tag TPID: 0x88e7]{lang="EN-US"}

[ I-SID: 111]{lang="EN-US"}

[ C-DA: 0101-0101-0101]{lang="EN-US"}

[ C-SA: 0202-0202-0202]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_32539_x9819_x1031780711}*[从上行口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的]{style="font-family:宋体"}[PBB]{lang="EN-US"}[报文]{style="font-family:宋体"}[头的具体内容]{style="font-family:宋体"}*
