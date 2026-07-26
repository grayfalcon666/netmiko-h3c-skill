::: {#1201504155 .myid}
[]{#_Toc118791469}[]{#_Toc404787067}[]{#struct_0_x3544_x1778_x500398486}[]{#_Toc277670163}[]{#_Toc123629827}

**隧道 \-- 隧道调试命令 \-- debugging tunnel**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1470851600}

[**[debugging tunnel]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ **interface tunnel** *interface-number* \]]{lang="EN-US"}]{#struct_0_x3544_x1778_832126595}

[**[undo debugging tunne]{lang="EN-US"}**[l { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x3544_x1778_435154903}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1741799313}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1236591834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1154457564}

[[network-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_1685386318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_2082496713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1081562284}

[**[all]{lang="EN-US"}**]{#struct_0_x3544_x1778_1999080865}[：表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x3544_x1778_x1259120461}[：表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x3544_x1778_362784470}[：表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x3544_x1778_x1179428983}[：表示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块报文调试信息开关。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x3544_x1778_908820700}[：表示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口进行调试。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1236526298}

[**[debugging tunnel]{lang="EN-US"}**]{#struct_0_x3544_x1778_360131403}[命令用来打开]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}**[undo debugging tunnel]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[模块的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_2134961523}[模块的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging tunnel error]{lang="EN-US"}]{#struct_0_x3544_x1778_1172279988}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x181736945}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1978538958}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_822316937}

[[Failed to send data to slot *num*.]{lang="EN-US"}]{#struct_0_x3544_x1778_437937920}

[[发送数据到槽位号为]{style="font-family:宋体"}*[num]{lang="EN-US"}*]{#struct_0_x3544_x1778_x959314318}[的接口板失败]{style="font-family:宋体"}

[[Tunnel ICMP error: Can't get the corresponding tunnel interface in up state.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236985050}

[[收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x3544_x1778_359976178}[差错报文后，找不到对应的处于]{style="font-family:宋体"}[up]{lang="EN-US"}[状态的隧道接口]{style="font-family:宋体"}

[[Tunnel ICMP error: Failed to update the ICMP soft state.]{lang="EN-US"}]{#struct_0_x3544_x1778_x437134422}

[[更新]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x3544_x1778_x1318711390}[软状态失败]{style="font-family:宋体"}

[[Failed to create Tunnel*num*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x2104568530}

[[创建接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_545175335}[失败]{style="font-family:宋体"}

[[Failed to delete Tunnel*num*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236919514}

[[删除接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1865696306}[失败]{style="font-family:宋体"}

[[The EVI-Link interface already exists.]{lang="EN-US"}]{#struct_0_x3544_x1778_1978208044}

[[此]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_1242665077}[接口已经存在]{style="font-family:宋体"}

[[The number of the EVI-Link interfaces has reached the maximum.]{lang="EN-US"}]{#struct_0_x3544_x1778_x586553924}

[[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_399822897}[接口数量已经达到最大值]{style="font-family:宋体"}

[[The EVI-Link interface doesn\'t exist.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236853978}

[[此]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_369854643}[接口不存在]{style="font-family:宋体"}

[[Failed to find the tunnel interface with the EVI-Link interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_394607042}

[[根据]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_740244306}[接口查找]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口失败]{style="font-family:宋体"}

[[Failed to create the EVI-link interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_1008440543}

[[创建]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_1236788442}[接口失败]{style="font-family:宋体"}

[[Failed to delete the EVI-Link interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_x2054440554}

[[删除]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_467993993}[接口失败]{style="font-family:宋体"}

[[Failed to find the EVI-Link interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_2072642890}

[[查找]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_x195882505}[接口失败]{style="font-family:宋体"}

[[Failed to find the output interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_1237247194}

[[查找出接口失败]{style="font-family:宋体"}]{#struct_0_x3544_x1778_x23480445}

[[Failed to get the tunnel mode.]{lang="EN-US"}]{#struct_0_x3544_x1778_x695070554}

[[获取隧道模式失败]{style="font-family:宋体"}]{#struct_0_x3544_x1778_x1654184643}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging tunnel event]{lang="EN-US"}]{#struct_0_x3544_x1778_947936591}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x151201303}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_600092932}

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1237181658}

[[Tunnel*num* can\'t come up because *reason*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1971871642}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1494691591}[不能]{style="font-family:宋体"}[up]{lang="EN-US"}[的原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[，]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[t]{lang="EN-US"}[he source address has been changed]{lang="EN-US"}]{#struct_0_x3544_x1778_282594256}[：隧道源接口地址已经改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[t]{lang="EN-US"}[he tunnel interface is shut]{lang="EN-US"}]{#struct_0_x3544_x1778_570560326}[ ]{lang="EN-US"}[down]{lang="EN-US"}[：接口处于]{lang="EN-US" style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}[ode check failed]{lang="EN-US"}]{#struct_0_x3544_x1778_2081398546}[：隧道模式检查失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[t]{lang="EN-US"}[here is no]{lang="EN-US"}]{#struct_0_x3544_x1778_x686242446}[t]{lang="EN-US"}[ enough hardware resource]{lang="EN-US"}[：硬件资源不足]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[the tunnel source and destination belong to different VRFs]{lang="EN-US"}]{#struct_0_x3544_x1778_612704000}[：隧道源地址和目的地址属于不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[Tunnel*num*: No keepalive packet received from the peer.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236722907}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1181680144}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，没有收到对端返回的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Tunnel ICMP event: The ICMP error message has been sent to ICMP module.]{lang="EN-US"}]{#struct_0_x3544_x1778_x461630440}

[[ICMP]{lang="EN-US"}]{#struct_0_x3544_x1778_x1664933494}[差错信息已经发送到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[Tunnel ICMP event: The ICMPv6 error message has been sent to ICMP6 module.]{lang="EN-US"}]{#struct_0_x3544_x1778_583838617}

[[ICMP6]{lang="EN-US"}]{#struct_0_x3544_x1778_x725607669}[差错信息已经发送到]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[模块]{style="font-family:宋体"}

[[Received an ADJ change message (flag = *flag*).]{lang="EN-US"}]{#struct_0_x3544_x1778_1236657371}

[[收到一个]{style="font-family:宋体"}[ADJ]{lang="EN-US"}]{#struct_0_x3544_x1778_x44517631}[变化的消息，标记为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[Received a VN change message.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1222421206}

[[收到一个]{style="font-family:宋体"}[VN]{lang="EN-US"}]{#struct_0_x3544_x1778_x2092402627}[变化的消息]{style="font-family:宋体"}

[[Event registered: SocketFd = *fd,* tunnelMode = *mode*, event = *event*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1082245094}

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_1236591835}[事件注册：套接字为]{style="font-family:宋体"}*[fd]{lang="EN-US"}*[，隧道模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[，事件类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Recovered interface (ifType = *type*) configuration during ISSU.]{lang="EN-US"}]{#struct_0_x3544_x1778_1154523100}

[[ISSU]{lang="EN-US"}]{#struct_0_x3544_x1778_x1029060963}[期间添加节点，接口类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Configuration of Tunnel*num* has already been synchronized.]{lang="EN-US"}]{#struct_0_x3544_x1778_x13086426}

[[接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1845956777}[的配置已经同步]{style="font-family:宋体"}

[[Synchronization count is *number*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236526299}

[[同步次数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x3544_x1778_360065867}

[[Received EVI-Link creating message.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1756774264}

[[收到创建]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_x952248866}[接口消息]{style="font-family:宋体"}

[[Received EVI-Link deleting message.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236985051}

[[收到删除]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_x3544_x1778_359910642}[接口消息]{style="font-family:宋体"}

[[Tunnel*num* adjusted link MTU to *mtusize*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1102919999}

[[接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x894944193}[调整]{style="font-family:宋体"}[MTU]{lang="EN-US"}[为]{style="font-family:宋体"}*[mtusize]{lang="EN-US"}*

[[EVI-Link*num*: No keepalive packet received from the peer.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236919515}

[[EVI-Link*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1865761842}[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，没有收到对端返回的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[RIB updated message: IfIndex = *index*, ifType = *type*, nextHop = *addr*, count = *cnt*, VNID = *vnid*, outIfIndex = *indexout*, rtFlag = *flag*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1611384842}

[[路由刷新消息：接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x3544_x1778_1887098807}[，接口类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，下一跳地址为]{style="font-family:宋体"}*[addr]{lang="EN-US"}*[，路由个数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*[，]{style="font-family:宋体"}[VN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vnid]{lang="EN-US"}*[，出接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*[，路由标记]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[RIB deleted message: IfIndex = *index*, ifType = *type*, nextHop = *addr*,]{lang="EN-US"}]{#struct_0_x3544_x1778_1236853979}

[[路由删除消息：接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x3544_x1778_369920179}[，接口类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，下一跳地址为]{style="font-family:宋体"}*[addr]{lang="EN-US"}*

[[Registered RIB: IfIndex = *index*, ifType = *type*, dstAddr = *addr*, vrfIndex = *vrfindex*]{lang="EN-US"}]{#struct_0_x3544_x1778_x383067306}

[[向路由表中注册：接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x3544_x1778_x411786793}[，接口类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，目的地址我]{style="font-family:宋体"}*[addr]{lang="EN-US"}[，]{style="font-family:宋体"}*[VPN]{lang="EN-US"}[实例索引为]{style="font-family:宋体"}*[vrfindex]{lang="EN-US"}*

[[Deregistered RIB: IfIndex = *index*, ifType = *type*, dstAddr = *addr*, vrfIndex = *vrfindex*]{lang="EN-US"}]{#struct_0_x3544_x1778_1236788443}

[[从路由表中解除注册：接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_x3544_x1778_x2054506090}[，接口类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[addr]{lang="EN-US"}[，]{style="font-family:宋体"}*[VPN]{lang="EN-US"}[实例索引为]{style="font-family:宋体"}*[vrfindex]{lang="EN-US"}*

[[Synchronized tunnel configurations on Tunnel*num* (ifIndex = *ifindex*).]{lang="EN-US"}]{#struct_0_x3544_x1778_x2097409234}

[[接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x185676724}[同步隧道的相关配置，接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[Number of synchronization messages sent: *cnt*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236657368}

[[同步发送个数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_x3544_x1778_x44058878}

[[Number of synchronization message received: *cnt*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236591832}

[[同步接收个数为]{style="font-family:宋体"}*[cnt]{lang="EN-US"}*]{#struct_0_x3544_x1778_1154064348}

[[Synchronization started.]{lang="EN-US"}]{#struct_0_x3544_x1778_145511081}

[[同步开始]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1236526296}

[[Synchronized DS-Lite switch on interface (ifIndex = *ifindex*)*.*]{lang="EN-US"}]{#struct_0_x3544_x1778_360786763}

[[接口同步]{style="font-family:宋体"}[DS-Lite]{lang="EN-US"}]{#struct_0_x3544_x1778_x926779441}[开关的配置，接口索引为]{style="font-family:宋体"}[if*index*]{lang="EN-US"}

[*[IfName]{lang="EN-US"}*[ failed to get information about operation *id*.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236985048}

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_360500465}[接口或]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[获取操作]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的信息失败]{style="font-family:宋体"}

[[Processing result of operation *id* for *IfName*: *result*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x479597104}

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_1236919512}[接口或]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[下发的操作]{style="font-family:宋体"}*[id]{lang="EN-US"}[，]{style="font-family:宋体"}*[处理结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[succeeded]{lang="EN-US"}]{#struct_0_x3544_x1778_1865303090}[：处理该操作成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[not supported]{lang="EN-US"}]{#struct_0_x3544_x1778_19313081}[：不能处理该操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[resources not enough]{lang="EN-US"}]{#struct_0_x3544_x1778_1236853976}[：没有足够的资源处理该操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[resources ]{lang="EN-US"}[not ready]{lang="EN-US"}]{#struct_0_x3544_x1778_368937139}[：未准备好处理该操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x3544_x1778_1236788440}[：处理该操作失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processed already]{lang="EN-US"}]{#struct_0_x3544_x1778_x2054571626}[：相同的操作已经处理]{style="font-family:宋体"}

[*[IfName]{lang="EN-US"}*[ notifies driver: Operation = *id*]{lang="EN-US"}]{#struct_0_x3544_x1778_458886535}

[[TunnelIfIndex = *tunnelifindex*, EvilinkIfIndex = *evilinkifindex*]{lang="EN-US"}]{#struct_0_x3544_x1778_1237247192}

[[VRFIndex = *vrfindex*, DstVRFIndex = *dstvrfindex*]{lang="EN-US"}]{#struct_0_x3544_x1778_x23087229}

[[TunnelMode = *mode*, TransPro = *pro*]{lang="EN-US"}]{#struct_0_x3544_x1778_1108593748}

[[TunnelSrc = *srcaddr*]{lang="EN-US"}]{#struct_0_x3544_x1778_1237181656}

[[TunnelDst = *dstaddr*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1972002714}

[[TTL = *ttl*, ToS = *tos*, DFBit = *dfbit*]{lang="EN-US"}]{#struct_0_x3544_x1778_1236722905}

[[MTU = *mtu*, IPv6MTU = *ipv6mtu*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1181549072}

[[DrvContext\[0\] = *context0*, DrvContext\[1\] = *context1*]{lang="EN-US"}]{#struct_0_x3544_x1778_49667425}

[[VNHandle = *vnhandle*, ADJIndex = *adjindex*]{lang="EN-US"}]{#struct_0_x3544_x1778_1236657369}

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_x43993342}[接口或]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口]{style="font-family:宋体"}*[IfName]{lang="EN-US"}*[通知驱动进行操作]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_40064913}[接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[，]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口索引为]{style="font-family:宋体"}*[evilinkifindex]{lang="EN-US"}*

[[Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_1236591833}[接口所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vrfindex]{lang="EN-US"}*[，隧道目的端地址所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}*[dstvrfindex]{lang="EN-US"}*

[[隧道模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*]{#struct_0_x3544_x1778_1154129884}[，隧道传输协议为]{style="font-family:宋体"}*[pro]{lang="EN-US"}*

[[隧道源端地址为]{style="font-family:宋体"}*[srcaddr]{lang="EN-US"}*]{#struct_0_x3544_x1778_1236526297}

[[隧道目的端地址为]{style="font-family:宋体"}*[dstaddr]{lang="EN-US"}*]{#struct_0_x3544_x1778_360721227}

[[TTL]{lang="EN-US"}]{#struct_0_x3544_x1778_x932433426}[为]{style="font-family:宋体"}*[ttl]{lang="EN-US"}*[，]{style="font-family:宋体"}[TOS]{lang="EN-US"}[为]{style="font-family:宋体"}*[tos]{lang="EN-US"}*[，]{style="font-family:宋体"}[DF]{lang="EN-US"}[标志为]{style="font-family:宋体"}*[dfbit]{lang="EN-US"}*

[[MTU]{lang="EN-US"}]{#struct_0_x3544_x1778_1236985049}[为]{style="font-family:宋体"}*[mtu]{lang="EN-US"}*[，]{style="font-family:宋体"}[IPv6MTU]{lang="EN-US"}[为]{style="font-family:宋体"}*[ipv6mtu]{lang="EN-US"}*

[[隧道驱动上下文信息为]{style="font-family:宋体"}*[context0]{lang="EN-US"}*]{#struct_0_x3544_x1778_360434929}[、]{style="font-family:宋体"}*[context1]{lang="EN-US"}*

[[VN]{lang="EN-US"}]{#struct_0_x3544_x1778_1236919513}[句柄为]{style="font-family:宋体"}*[vnhandle]{lang="EN-US"}*[，]{style="font-family:宋体"}[ADJ]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[adjindex]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging tunnel packet]{lang="EN-US"}]{#struct_0_x3544_x1778_1865368626}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x161571989}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1202368281}

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_313772253}

[[IPv6 tunnel packet: The length of extension header is *length*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x85592591}

[[隧道通过]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_1675144168}[快转转发出隧道报文时，解析出]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文扩展头长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[The protocol number *number* of the packet from driver is unknown. Dropped the packet]{lang="EN-US"}]{#struct_0_x3544_x1778_797968217}

[[驱动发送给隧道接口的报文，协议号为未知的数值]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x3544_x1778_1236853977}[，丢弃该报文]{style="font-family:宋体"}

[[Sent an ICMPv6 parameter problem message to the source, when the encapsulation limit is reached.]{lang="EN-US"}]{#struct_0_x3544_x1778_369002675}

[[IPv6 over IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_945174877}[隧道报文超过允许的最大嵌套封装次数后，不允许该报文再进入隧道进行封装。此时，隧道向源节点发送]{style="font-family:宋体"}[ICMP6]{lang="EN-US"}[参数错误报文]{style="font-family:宋体"}

[[Tunnel packet: Received an inner ICMP message (type = *type*, code = *code*).]{lang="EN-US"}]{#struct_0_x3544_x1778_x1666848873}

[[接收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x3544_x1778_973830007}[差错报文，差错类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[和差错码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Received a packet to be de-encapsulated.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236480838}

[[收到一个需要解封装的报文]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1236788441}

[[Received a GRE over IPv4 packet with upper layer protocol *id*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x2054637162}

[[收到一个]{style="font-family:宋体"}[GRE over IPv4]{lang="EN-US"}]{#struct_0_x3544_x1778_x2099307736}[报文，上层协议为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Received an IPv4 over IPv4 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1967868483}

[[收到一个]{style="font-family:宋体"}[IPv4 over IPv4]{lang="EN-US"}]{#struct_0_x3544_x1778_x679834687}[报文]{style="font-family:宋体"}

[[Received an IPv6 over IPv4 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_1237247193}

[[收到一个]{style="font-family:宋体"}[IPv6 over IPv4]{lang="EN-US"}]{#struct_0_x3544_x1778_x23152765}[报文]{style="font-family:宋体"}

[[Received a de-encapsulated packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_1139573928}

[[收到一个已经解封装的报文]{style="font-family:宋体"}]{#struct_0_x3544_x1778_66291985}

[[Received a GRE over IPv6 packet with upper layer protocol *id*.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1805334507}

[[收到一个]{style="font-family:宋体"}[GRE over IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_1237181657}[报文，上层协议为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Received an IPv4 over IPv6 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1972068250}

[[收到一个]{style="font-family:宋体"}[IPv4 over IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_x1136454045}[报文]{style="font-family:宋体"}

[[Received an IPv6 over IPv6 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_1527923698}

[[收到一个]{style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_x1282174832}[报文]{style="font-family:宋体"}

[[Received a too big packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236722902}

[[收到一个过大报文]{style="font-family:宋体"}]{#struct_0_x3544_x1778_x1181876752}

[[Received a packet (family = *family*, length = *length*).]{lang="EN-US"}]{#struct_0_x3544_x1778_1034611755}

[[收到一个报文，协议族为]{style="font-family:宋体"}*[family]{lang="EN-US"}*]{#struct_0_x3544_x1778_1001627705}[，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Received a message to trigger ARP.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236657366}

[[收到一个触发]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x3544_x1778_x44976382}[的消息]{style="font-family:宋体"}

[[Received a message to trigger ND.]{lang="EN-US"}]{#struct_0_x3544_x1778_x408511272}

[[收到一个触发]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_x3544_x1778_x1379834399}[的消息]{style="font-family:宋体"}

[[Received a message to resend interface information for Tunnel*num* (ifindex = *ifindex*).]{lang="EN-US"}]{#struct_0_x3544_x1778_1236591830}

[[收到一个重发接口]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1154195420}[（接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[）信息的消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_501145065}

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_1150547112}[打开]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[错误调试信息开关。在分布式环境下配置隧道相关命令时插拔接口板，设备上将出现如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel error]{lang="NO-BOK"}]{#struct_0_x3544_x1778_391640114}

[\*Nov 17 09:16:07:928 2010 Sysname TUNNEL/7/error: -MDC=1;]{lang="NO-BOK"}

[ ]{lang="NO-BOK"}[Failed to send data to slot1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_1460439184}*[发送数据到]{style="font-family:宋体"}[1]{lang="EN-US"}[号接口板失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_1236526294}[打开]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[事件调试信息开关。创建隧道接口，配置隧道接口参数使隧道接口]{style="font-family:宋体"}[up]{lang="EN-US"}[后，]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[隧道接口，设备上将出现如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel event]{lang="DA"}]{#struct_0_x3544_x1778_360917835}

[\*Sep  6 11:59:59:183 2011 Sysname TUNNEL/7/event: -MDC=1;]{lang="NO-BOK"}

[ Tunnel0 can\'t come up because the tunnel interface is shutdown.  ]{lang="NO-BOK"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x376324069}*[由于接口处于]{style="font-family:宋体"}[shutdown]{lang="EN-US"}[状态，隧道]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[不能]{style="font-family:宋体"}[up]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_x1610754928}[打开]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[报文调试信息开关。设备接收到不支持的协议报文时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel packet]{lang="NO-BOK"}]{#struct_0_x3544_x1778_x858838553}

[\*Nov 17 09:16:07:928 2010 Sysname TUNNEL/7/debug: ]{lang="EN-US"}[-MDC=1;]{lang="NO-BOK"}

[ The protocol number 4 of the packet is unknown. ]{lang="EN-US"}[Dropped the packet]{lang="NO-BOK"}

[*[// ]{lang="NO-BOK"}*]{#struct_0_x3544_x1778_x272066592}*[隧道接收到不支持的协议报文（协议号为]{style="font-family:宋体"}[4]{lang="NO-BOK"}[），丢弃该报文]{style="font-family:宋体"}*

::: {#-1159857400 .myid}
[]{#_Toc404787068}[]{#struct_0_x3544_x1778_799522100}[]{#_Toc123629825}

**隧道 \-- 隧道调试命令 \-- debugging tunnel4**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1236985046}

[**[debugging tunnel4]{lang="EN-US"}**[ { **all** \| **error** \| **packet** } \[ **interface tunnel** *interface-number* \]]{lang="EN-US"}]{#struct_0_x3544_x1778_360369393}

[**[undo debugging tunnel4]{lang="EN-US"}**[ { **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x3544_x1778_2052892433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1484968363}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1618554445}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x995371287}

[[network-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_x1724206799}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_410821400}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1328488043}

[**[all]{lang="EN-US"}**]{#struct_0_x3544_x1778_x1270477263}[：表示]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x3544_x1778_1236919510}[：表示]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x3544_x1778_1865434162}[：表示]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x3544_x1778_411444658}[：表示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口进行调试。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1043651028}

[**[debugging tunnel4]{lang="EN-US"}**]{#struct_0_x3544_x1778_x1635600339}[命令用来打开]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging tunnel4]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_x1006391006}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[IPv4 Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_1869042118}[指的是外层传输协议为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议的隧道。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging tunnel4 error]{lang="EN-US"}]{#struct_0_x3544_x1778_105528577}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x167683437}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1236853974}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_369068211}

[[Tunnel*num* status check: Source address is not set.]{lang="EN-US"}]{#struct_0_x3544_x1778_x255039689}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_146874842}[状态检查：源地址没有配置]{style="font-family:宋体"}

[[Tunnel*num* status check: Destination address is not set.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1391874411}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x859222127}[状态检查：目的地址没有配置]{style="font-family:宋体"}

[[Tunnel*num* status check: Source address is not the address of a local interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236788438}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x2054047339}[状态检查：源地址不是本设备接口的地址]{style="font-family:宋体"}

[[Tunnel*num* status check: Failed to get FIB information of the source address.]{lang="EN-US"}]{#struct_0_x3544_x1778_x145358114}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1998015034}[状态检查：获取源地址]{style="font-family:宋体"}[FIB]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Tunnel*num* status check: Destination address should not be the address of a local interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_1399596339}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_35012927}[状态检查：目的地址不能是本设备接口的地址]{style="font-family:宋体"}

[[Tunnel*num* status check: Failed to get FIB information of the destination address.]{lang="EN-US"}]{#struct_0_x3544_x1778_1237247190}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x23218301}[状态检查：获取目的地址]{style="font-family:宋体"}[FIB]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[The protocol state of Tunnel*num* is not up. Dropped the packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x985311572}

[[待解封装报文出隧道时发现相应隧道接口协议状态不是]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x3544_x1778_476100907}[的，报文被丢弃]{style="font-family:宋体"}

[[Tunnel*num*: The information obtained from the adjacency table is invalid.]{lang="EN-US"}]{#struct_0_x3544_x1778_1123094152}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1237181654}[：获取的邻接表信息非法]{style="font-family:宋体"}

[[Tunnel*num*: The passenger protocol number *number* is not supported.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1972133786}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1552780831}[：不支持乘客协议]{style="font-family:宋体"}*[protocol-number]{lang="IT"}*

[[The IPv4 address embedded in the source IPv6 address is invalid.]{lang="EN-US"}]{#struct_0_x3544_x1778_1977138664}

[[自动隧道中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_287936530}[源地址里内嵌的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址非法，丢弃报文]{style="font-family:宋体"}

[[The IPv4 address embedded in the destination IPv6 address is invalid.]{lang="EN-US"}]{#struct_0_x3544_x1778_1236722903}

[[自动隧道中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_x1181942288}[目的地址里内嵌的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址非法，丢弃报文]{style="font-family:宋体"}

[[IPv6 destination address is not a 6to4 address.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1973870147}

[[6to4]{lang="EN-US"}]{#struct_0_x3544_x1778_x869066711}[隧道加封装时获取的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[目的地址前缀不是]{style="font-family:宋体"}[2002::]{lang="EN-US"}

[[IPv6 destination address is not an IPv4-compatible IPv6 address]{lang="EN-US"}]{#struct_0_x3544_x1778_1236657367}

[[IPv4]{lang="EN-US"}]{#struct_0_x3544_x1778_x44910846}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[自动隧道加封装时获取到的目的地址不是兼容地址]{style="font-family:宋体"}

[[Failed to forward the IPv4 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_378254749}

[[加封装后的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x3544_x1778_458804508}[报文发送失败]{style="font-family:宋体"}

[[No tunnel in the physical state of up was found for the packet. Dropped the packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x615011971}

[[出隧道报文解封装时找不到对应的、物理状态]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x3544_x1778_1236591831}[的隧道接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging tunnel4 packet]{lang="EN-US"}]{#struct_0_x3544_x1778_1154260956}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x135254395}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1325016406}

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x265598294}

[[Tunnel*num* packet: Before encapsulation according to adjacency table,]{lang="EN-US"}]{#struct_0_x3544_x1778_x208569258}

[*[source]{lang="EN-US"}*[-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x882767173}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1236526295}[：根据邻接表加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_360852299}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1160826227}[：加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before encapsulation according to fast-forwarding table, ]{lang="EN-US"}]{#struct_0_x3544_x1778_x1260737248}

[*[source]{lang="EN-US"}*[-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x811484453}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x678976244}[：根据快转表加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: After encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_1236985047}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_360303857}[：加封装后，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Fast forwarded the encapsulated packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1136279494}

[[快速转发加封装后的报文]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1641284547}

[[Failed to fast forward the encapsulated packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1912049233}

[[快转加封装后的报文失败]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1236919511}

[[Before de-encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_1865499698}

[[解封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_x3544_x1778_x329571566}[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before de-encapsulation according to fast-forwarding table, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_629044694}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_835331038}[：根据快转表解封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: After de-encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_1236853975}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_369133747}[：解封装后，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Discarded compatible address packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_1341113441}

[[丢弃]{style="font-family:宋体"}]{#struct_0_x3544_x1778_116379424}[含有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1370236379}

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_698544364}[打开本端的]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[错误调试信息开关。创建隧道接口，但没有配置源地址时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel4 error]{lang="EN-US"}]{#struct_0_x3544_x1778_1236788439}

[\*Mar 29 09:16:07:928 2011 Sysname TUNNEL4/7/error: ]{lang="EN-US"}[-MDC=1;]{lang="NO-BOK"}

[ Tunnel1 status check: Source address is not set.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x2054112875}*[隧道]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[状态检查：没有配置源地址]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_395573994}[打开本端的]{style="font-family:宋体"}[IPv4 Tunnel]{lang="EN-US"}[报文调试信息开关。在两台设备之间建立]{style="font-family:宋体"}[IPv4 over IPv4]{lang="EN-US"}[隧道，并分别配置参数使隧道接口]{style="font-family:宋体"}[up]{lang="EN-US"}[。在本端设备上]{style="font-family:宋体"}[ping]{lang="EN-US"}[对端设备，本端设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel4 packet]{lang="EN-US"}]{#struct_0_x3544_x1778_x141275917}

[\<Sysname\> ping -c 1 -a 10.1.1.1 10.1.3.1]{lang="EN-US"}

[PING 10.1.3.1 (10.1.3.1) from 10.1.1.1: 56 data bytes]{lang="EN-US"}

[56 bytes from 10.1.3.1: icmp_seq=0 ttl=255 time=1.000 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 10.1.3.1 ping statistics \-\--]{lang="EN-US"}

[1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss]{lang="EN-US"}

[round-trip min/avg/max/stddev = 1.000/1.000/1.000/0.000 ms]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;]{lang="EN-US"}

[ Tunnel0 packet: Before encapsulation according to adjacency table,]{lang="EN-US"}

[   10.1.1.1-\>10.1.3.1 (length = 84)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_283226842}*[根据邻接表加封装前，报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.3.1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[84]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_1237247191}

[ Tunnel0 packet: After encapsulation,]{lang="EN-US"}

[   1.1.1.1-\>1.1.1.2 (length = 104)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x23283837}*[加封装后，报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[104]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 11:56:35:242 2011 Sysname TUNNEL4/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_x613185556}

[ Tunnel0 packet: Fast forwarded the encapsulated packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x618909723}*[根据快转表项快速转发封装后的报文]{style="font-family:宋体"}*

[[\*Sep  6 11:56:35:243 2011 Sysname TUNNEL4/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_550765376}

[ Tunnel0 packet: Before de-encapsulation according to fast-forwarding table,]{lang="EN-US"}

[   1.1.1.2-\>1.1.1.1 (length = 104)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x1369596142}*[接收到的报文根据快转表项解封装前，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[104]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 11:56:35:243 2011 Sysname TUNNEL4/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_1237181655}

[ Tunnel0 packet: After de-encapsulation,]{lang="EN-US"}

[   10.1.3.1-\>10.1.1.1 (length = 84)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x1972199322}*[接收到的报文解封装后，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.3.1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[84]{lang="EN-US"}[字节]{style="font-family:宋体"}*

::: {#-1159857402 .myid}
[]{#_Toc404787069}[]{#struct_0_x3544_x1778_x2044050941}[]{#_Toc123629826}[]{#_Toc277669731}[]{#_Toc277669732}[]{#_Toc277669735}[]{#_Toc277669736}[]{#_Toc277669737}[]{#_Toc277669738}[]{#_Toc277669739}[]{#_Toc277669740}[]{#_Toc277669741}[]{#_Toc277669742}[]{#_Toc277669743}[]{#_Toc277669744}[]{#_Toc277669745}[]{#_Toc277669746}[]{#_Toc277669795}[]{#_Toc277669796}[]{#_Toc277669824}[]{#_Toc277669825}[]{#_Toc277669845}[]{#_Toc277669846}[]{#_Toc277669865}[]{#_Toc277669866}[]{#_Toc277669867}[]{#_Toc277669868}[]{#_Toc277669869}[]{#_Toc277669871}[]{#_Toc277669872}[]{#_Toc277669873}[]{#_Toc277669874}[]{#_Toc277669879}[]{#_Toc277669883}[]{#_Toc277669887}[]{#_Toc277669888}[]{#_Toc277669891}[]{#_Toc277669892}[]{#_Toc277669894}[]{#_Toc277669899}[]{#_Toc277669900}[]{#_Toc277669901}[]{#_Toc277669902}[]{#_Toc277669903}[]{#_Toc277669904}[]{#_Toc277669905}[]{#_Toc277669906}[]{#_Toc277669907}[]{#_Toc277669908}[]{#_Toc277669910}[]{#_Toc277669912}[]{#_Toc277669916}[]{#_Toc277669920}[]{#_Toc277669921}[]{#_Toc277669924}[]{#_Toc277669925}[]{#_Toc277669926}[]{#_Toc277669927}[]{#_Toc277669930}[]{#_Toc277669931}[]{#_Toc277669932}[]{#_Toc277669933}[]{#_Toc277669934}[]{#_Toc277669935}[]{#_Toc277669936}[]{#_Toc277669937}[]{#_Toc277669938}[]{#_Toc277669939}[]{#_Toc277669940}[]{#_Toc277669941}[]{#_Toc277669990}[]{#_Toc277669991}[]{#_Toc277670043}[]{#_Toc277670044}[]{#_Toc277670067}[]{#_Toc277670068}[]{#_Toc277670087}[]{#_Toc277670088}[]{#_Toc277670089}[]{#_Toc277670090}[]{#_Toc277670091}[]{#_Toc277670092}[]{#_Toc277670095}[]{#_Toc277670097}[]{#_Toc277670098}[]{#_Toc277670099}[]{#_Toc277670100}[]{#_Toc277670105}[]{#_Toc277670109}[]{#_Toc277670115}[]{#_Toc277670119}[]{#_Toc277670122}[]{#_Toc277670127}[]{#_Toc277670128}[]{#_Toc277670129}[]{#_Toc277670131}[]{#_Toc277670133}[]{#_Toc277670134}[]{#_Toc277670138}[]{#_Toc277670139}[]{#_Toc277670140}[]{#_Toc277670141}[]{#_Toc277670142}[]{#_Toc277670143}[]{#_Toc277670144}[]{#_Toc277670145}[]{#_Toc277670149}[]{#_Toc277670150}[]{#_Toc277670153}[]{#_Toc277670157}[]{#_Toc277670161}[]{#_Toc277670162}

**隧道 \-- 隧道调试命令 \-- debugging tunnel6**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_757883356}

[**[debugging tunnel6]{lang="EN-US"}**[ { **all** \| **error** \| **packet** } \[ **interface tunnel** *interface-number* \]]{lang="EN-US"}]{#struct_0_x3544_x1778_824611109}

[**[undo debugging tunnel6]{lang="EN-US"}**[ { **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x3544_x1778_x2016554464}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_487636972}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x3544_x1778_1601046128}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1357378271}

[[network-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492160449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x3544_x1778_33340340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1727188304}

[**[all]{lang="EN-US"}**]{#struct_0_x3544_x1778_1929953586}[：表示]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x3544_x1778_x1867935598}[：表示]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x3544_x1778_1995488867}[：表示]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1245072561}[：表示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口进行调试。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_1078673551}

[**[debugging tunnel6]{lang="EN-US"}**]{#struct_0_x3544_x1778_1305913691}[命令用来打开]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging tunnel6]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492225985}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[IPv6 Tunnel]{lang="EN-US"}]{#struct_0_x3544_x1778_1761174615}[指的是外层传输协议为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议的隧道。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging tunnel6 error]{lang="EN-US"}]{#struct_0_x3544_x1778_679290391}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x142467473}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x143008258}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x294734531}

[[Tunnel*num* status check: Source address is not set.]{lang="EN-US"}]{#struct_0_x3544_x1778_546896055}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1298678206}[状态检查：源地址没有配置]{style="font-family:宋体"}

[[Tunnel*num* status check: Destination address is not set.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492291521}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_291834662}[状态检查：目的地址没有配置]{style="font-family:宋体"}

[[Tunnel*num* status check: Source address is not the address of a local interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1839079111}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1868689421}[状态检查：源地址不是本设备接口的地址]{style="font-family:宋体"}

[[Tunnel*num* status check: Failed to get FIB information of the source address.]{lang="EN-US"}]{#struct_0_x3544_x1778_2129666891}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1510162020}[状态检查：获取源地址]{style="font-family:宋体"}[FIB]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Tunnel*num* status check: Destination address should not be the address of a local interface.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492357057}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_183796517}[状态检查：目的地址不能是本设备接口的地址]{style="font-family:宋体"}

[[Tunnel*num* status check: Failed to get FIB information of the destination address.]{lang="EN-US"}]{#struct_0_x3544_x1778_x549008144}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1402620611}[状态检查：获取目的地址]{style="font-family:宋体"}[FIB]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[The protocol state of Tunnel*num* is not up. Dropped the packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_9582278}

[[待解封装报文出隧道时发现相应隧道接口协议状态不是]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x3544_x1778_x1491898305}[的，报文被丢弃]{style="font-family:宋体"}

[[Tunnel*num*: The information obtained from the adjacency table is invalid.]{lang="EN-US"}]{#struct_0_x3544_x1778_1390665141}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_605009464}[：邻接表信息非法]{style="font-family:宋体"}

[[Tunnel*num*: The passenger protocol number *number* is not supported.]{lang="EN-US"}]{#struct_0_x3544_x1778_997930268}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1128711056}[：不支持乘客协议]{style="font-family:宋体"}*[protocol-number]{lang="IT"}*

[[Failed to forward the IPv6 packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1491963841}

[[加封装后的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x3544_x1778_x474081545}[报文发送失败]{style="font-family:宋体"}

[[No tunnel in the physical state of up was found for the packet. Dropped the packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_512134396}

[[出隧道报文解封装时找不到对应的、物理状态]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x3544_x1778_x241663786}[的隧道接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging tunnel6 packet]{lang="EN-US"}]{#struct_0_x3544_x1778_x1628463875}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x145486391}[[字段]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1492029377}

[[描述]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1011909849}

[[Tunnel*num* packet: Before encapsulation according to adjacency table,]{lang="EN-US"}]{#struct_0_x3544_x1778_x1469591995}

[*[source]{lang="EN-US"}*[-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_1237477900}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1508423366}[：根据邻接表加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x407130424}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x14880547}[：加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before encapsulation according to fast-forwarding table, ]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492094913}

[*[source]{lang="EN-US"}*[-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x473685524}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1323278192}[：根据快转表加封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: After encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_436252041}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_2045656811}[：加封装后，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Fast forwarded the encapsulated packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1491636161}

[[快速转发加封装后的报文]{style="font-family:宋体"}]{#struct_0_x3544_x1778_x1041084707}

[[Failed to fast forward the encapsulated packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x1148944366}

[[快转加封装后的报文失败]{style="font-family:宋体"}]{#struct_0_x3544_x1778_233025749}

[[Before de-encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x234378608}

[[解封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_x3544_x1778_1600685834}[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: Before de-encapsulation according to fast-forwarding table, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_x1491701697}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_x1846672771}[：根据快转表解封装前，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Tunnel*num* packet: After de-encapsulation, *source*-\>*destination* (length = *length*)]{lang="EN-US"}]{#struct_0_x3544_x1778_1071902698}

[[隧道]{style="font-family:宋体"}[Tunnel*num*]{lang="EN-US"}]{#struct_0_x3544_x1778_1475484959}[：解封装后，报文头源地址为]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，目的地址为]{style="font-family:宋体"}*[destination]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Discarded compatible address packet.]{lang="EN-US"}]{#struct_0_x3544_x1778_x620951830}

[[丢弃]{style="font-family:宋体"}]{#struct_0_x3544_x1778_x1492160448}[含有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[兼容]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x3544_x1778_x1532743601}

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_x2014701407}[打开本端的]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[错误调试信息开关。创建隧道接口，但没有配置源地址时，打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel6 error]{lang="EN-US"}]{#struct_0_x3544_x1778_319307974}

[\*Mar 29 09:17:07:928 2011 Sysname TUNNEL6/7/error: ]{lang="EN-US"}[-MDC=1;]{lang="NO-BOK"}

[ Tunnel1 status check: Source address is not set.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x896321868}*[隧道]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[状态检查：没有配置源地址]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x3544_x1778_349483311}[打开本端的]{style="font-family:宋体"}[IPv6 Tunnel]{lang="EN-US"}[报文调试信息开关。在两台设备之间建立]{style="font-family:宋体"}[IPv6 over IPv6]{lang="EN-US"}[隧道，并分别配置参数使隧道接口]{style="font-family:宋体"}[up]{lang="EN-US"}[。在本端设备上]{style="font-family:宋体"}[ping]{lang="EN-US"}[对端设备，本端设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging tunnel6 packet]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492225984}

[\<Sysname\> ping ipv6 -c 1 -a 3::1 5::1]{lang="EN-US"}

[PING6(56 data bytes) 3::1 \--\> 5::1]{lang="EN-US"}

[56 bytes from 5::1, icmp_seq=0 hlim=64 time=2.000 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- 5::1 ping6 statistics \-\--]{lang="EN-US"}

[1 packet(s) transmitted, 1 packet(s) received, 0.0% packet loss]{lang="EN-US"}

[round-trip min/avg/max/std-dev = 2.000/2.000/2.000/0.000 ms]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;]{lang="EN-US"}

[ Tunnel1 packet: Before encapsulation,]{lang="EN-US"}

[   3::1-\>5::1 (length = 104)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_195090674}*[报文加封装前，源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3::1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5::1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[104]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_x1814075316}

[ Tunnel1 packet: After encapsulation,]{lang="EN-US"}

[   1::1-\>1::2 (length = 144)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_1845835439}*[报文加封装后，源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::2]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[144]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 12:05:12:296 2011 Sysname TUNNEL6/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_1875502334}

[ Tunnel1 packet: Failed to fast forward the encapsulated packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_933305753}*[没有找到封装后报文对应的快转表项，快转失败]{style="font-family:宋体"}*

[[\*Sep  6 12:05:12:297 2011 Sysname TUNNEL6/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_x1492291520}

[ Tunnel1 packet: Before de-encapsulation according to fast-forwarding table,]{lang="EN-US"}

[   1::2-\>1::1 (length = 144)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_1857918603}*[根据快转表项解封装前，报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::2]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[144]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Sep  6 12:05:12:297 2011 Sysname TUNNEL6/7/packet: -MDC=1;]{lang="EN-US"}]{#struct_0_x3544_x1778_1492437186}

[ Tunnel1 packet: After de-encapsulation,]{lang="EN-US"}

[   5::1-\>3::1 (length = 104)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x3544_x1778_x234107700}*[报文解封装后，源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5::1]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[3::1]{lang="EN-US"}[，报文长度为]{style="font-family:宋体"}[104]{lang="EN-US"}[字节]{style="font-family:宋体"}*
