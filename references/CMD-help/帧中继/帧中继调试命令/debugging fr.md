::: {#2118975210 .myid}
[]{#_Toc404785783}[]{#struct_0_x6265_25298_2129563616}

**帧中继 \-- 帧中继调试命令 \-- debugging fr**

------------------------------------------------------------------------

[**[debugging]{lang="EN-US"}**[ **fr**]{lang="EN-US"}]{#struct_0_x6265_25298_200021758}[命令用来打开帧中继调试信息开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **debugging** **fr**]{lang="EN-US"}]{#struct_0_x6265_25298_624260352}[命令用来关闭帧中继调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6265_25298_x2143113074}

[**[debugging fr]{lang="EN-US"}**[ { **all** \[ **interface** *interface-type* *interface-number* \] \| **event** \| **inarp** \[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number* \] \] \| **lmi** \[ **interface** *interface-type* *interface-number* \] \| **packet** \[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number* \] \] \| **packet-hex** \[ **interface** *interface-type* *interface-number* \] }]{lang="EN-US"}]{#struct_0_x6265_25298_1058206502}

[**[undo debugging fr]{lang="EN-US"}**[ { **all** \[ **interface** *interface-type* *interface-number* \] \| **event** \| **inarp** \[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number* \] \] \| **lmi** \[ **interface** *interface-type* *interface-number* \] \| **packet** \[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number*\] \] \| **packet-hex** \[ **interface** *interface-type* *interface-number* \] }]{lang="EN-US"}]{#struct_0_x6265_25298_x319264335}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6265_25298_x1329617820}

[[帧中继所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x6265_25298_x1954163434}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6265_25298_1872947575}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6265_25298_x1293583638}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6265_25298_657541102}

[[network-admin]{lang="EN-US"}]{#struct_0_x6265_25298_x1998347776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6265_25298_1042455577}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6265_25298_199825150}

[**[all]{lang="EN-US"}**]{#struct_0_x6265_25298_x457710508}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x6265_25298_x1610157396}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[inarp]{lang="EN-US"}**]{#struct_0_x6265_25298_2143305915}[：表示逆向地址解析协议调试信息开关。]{style="font-family:宋体"}

[**[lmi]{lang="EN-US"}**]{#struct_0_x6265_25298_562485472}[：表示]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x6265_25298_x317370615}[：表示数据报文调试信息开关。]{style="font-family:宋体"}

[**[packet-hex]{lang="EN-US"}**]{#struct_0_x6265_25298_844485181}[：表示十六进制报文调试信息开关，包括数据报文和协商报文。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6265_25298_347198211}[：表示指定接口的调试信息开关。如果不指定接口，则表示所有接口的调试信息开关。指定的接口只能是主接口，不能是子接口。指定主接口后，将打开主接口及其子接口的调试信息开关。]{style="font-family:宋体"}

[**[dlci ]{lang="EN-US"}***[dlci-number]{lang="EN-US"}*]{#struct_0_x6265_25298_x786230123}[：表示指定虚电路的调试信息开关。]{style="font-family:宋体"}*[dlci-number]{lang="EN-US"}*[表示虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[，范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[1008]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[的虚电路为帧中继协议保留，供特殊使用。如果不指定本参数，则表示所有虚电路的调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6265_25298_207176773}

[]{#struct_0_x6265_25298_199890686}[[表1-1 ]{lang="EN-US"}[debugging fr event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_13050017}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_x894811970}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_x1864453621}

[[Added IP address on interface *interface-name.*]{lang="EN-US"}]{#struct_0_x6265_25298_1928104712}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x274767530}[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Deleted IP address on interface *interface-name.*]{lang="EN-US"}]{#struct_0_x6265_25298_x132101716}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x238260874}[删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Modified IP address on interface *interface-name.*]{lang="EN-US"}]{#struct_0_x6265_25298_199694078}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x708028530}[修改]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Keepalive changed on interface *interface-name.*]{lang="EN-US"}]{#struct_0_x6265_25298_2143851864}

[[接口]{style="font-family:宋体"}*[interface-name ]{lang="EN-US"}*[keep alive]{lang="EN-US"}]{#struct_0_x6265_25298_916171502}[变化]{style="font-family:宋体"}

[[Failed to create a MAP for exceeding the MAP number limit on the DLCI.]{lang="EN-US"}]{#struct_0_x6265_25298_x63981444}

[[创建]{style="font-family:宋体"}[MAP]{lang="EN-US"}]{#struct_0_x6265_25298_x857861978}[失败，超过了]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上允许的最大]{style="font-family:宋体"}[MAP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Failed to create a MAP for exceeding the MAP number limit in the system.]{lang="EN-US"}]{#struct_0_x6265_25298_x1272938897}

[[创建]{style="font-family:宋体"}[MAP]{lang="EN-US"}]{#struct_0_x6265_25298_199759614}[失败，超过了系统允许的最大]{style="font-family:宋体"}[MAP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Failed to create a MAP for exceeding the MAP number limit on the interface.]{lang="EN-US"}]{#struct_0_x6265_25298_x266780356}

[[创建]{style="font-family:宋体"}[MAP]{lang="EN-US"}]{#struct_0_x6265_25298_1972248932}[失败，超过了接口允许的最大]{style="font-family:宋体"}[MAP]{lang="EN-US"}[个数]{style="font-family:宋体"}

[[Failed to create a PVC for exceeding the PVC number limit in the system.]{lang="EN-US"}]{#struct_0_x6265_25298_911380590}

[[超出系统允许创建的]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_x6265_25298_1621066118}[个数上限，创建]{style="font-family:宋体"}[PVC]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name*, because the PVC state is down.]{lang="EN-US"}]{#struct_0_x6265_25298_333990570}

[[PVC]{lang="EN-US"}]{#struct_0_x6265_25298_200611582}[状态为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发送报文失败]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name*, because of the packet encapsulation error.]{lang="EN-US"}]{#struct_0_x6265_25298_x512926195}

[[报文封装错误，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x257835970}[发送报文失败]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name*, because the PVC does not exist.]{lang="EN-US"}]{#struct_0_x6265_25298_71937027}

[[PVC]{lang="EN-US"}]{#struct_0_x6265_25298_836591343}[不存在，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发送报文失败]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name*, because there is no matched MAP.]{lang="EN-US"}]{#struct_0_x6265_25298_x69284786}

[[没有匹配的]{style="font-family:宋体"}[MAP]{lang="EN-US"}]{#struct_0_x6265_25298_200677118}[，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发送报文失败]{style="font-family:宋体"}

[[Failed to send a packet on interface *interface-name*, because the packet type is unknown.]{lang="EN-US"}]{#struct_0_x6265_25298_1016499165}

[[报文类型错误，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1508324572}[发送报文失败]{style="font-family:宋体"}

[[Failed to received a packet on interface *interface-name*, because the packet length error.]{lang="EN-US"}]{#struct_0_x6265_25298_x30214535}

[[报文长度错误，接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1439156253}[接收报文失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x6265_25298_x1214818666}[[表1-2 ]{lang="EN-US"}[debugging fr inarp]{lang="EN-US"}]{#_Toc130718930}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_9218613}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_200087293}

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_x912904914}

[[Sent an InARP *packet-type* packet on interface *interface-name* DLCI *DLCI*:]{lang="EN-US"}]{#struct_0_x6265_25298_152151407}

[[  hard length=*hard length*, hard=*hard*]{lang="EN-US"}]{#struct_0_x6265_25298_1425039565}

[[  protocol length=*protocol length*, protocol=*protocol*]{lang="EN-US"}]{#struct_0_x6265_25298_1710902617}

[[  source IP=*source IP*, target IP=*target IP*]{lang="EN-US"}]{#struct_0_x6265_25298_2105612998}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x178377106}[下]{style="font-family:宋体"}[DCLI]{lang="EN-US"}[为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[上发送]{style="font-family:宋体"}[InARP *packet-type*]{lang="EN-US"}[报文：硬件地址长度为]{style="font-family:宋体"}*[hard length]{lang="EN-US"}*[，硬件地址类型为]{style="font-family:宋体"}*[hard]{lang="EN-US"}*[（]{style="font-family:宋体"}*[hard]{lang="EN-US"}*[值为]{style="font-family:宋体"}[0x000f]{lang="EN-US"}[，表示帧中继），协议地址长度为]{style="font-family:宋体"}*[protocol length]{lang="EN-US"}*[，协议地址类型为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[（]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[值为]{style="font-family:宋体"}[0x0800]{lang="EN-US"}[，表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议），源协议地址为]{style="font-family:宋体"}*[source IP]{lang="EN-US"}*[，目的协议地址为]{style="font-family:宋体"}*[target IP]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_x6265_25298_200152829}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_x6265_25298_969653339}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[[Received an InARP *packet-type* packet on interface *interface-name* DLCI *DLCI*:]{lang="EN-US"}]{#struct_0_x6265_25298_x1774446505}

[[  hard length=*hard length*, hard=*hard*]{lang="EN-US"}]{#struct_0_x6265_25298_898006987}

[[  protocol length=*protocol length*, protocol=*protocol*]{lang="EN-US"}]{#struct_0_x6265_25298_x1158389567}

[[  source *IP*=*source IP*, target *IP*=*target IP*]{lang="EN-US"}]{#struct_0_x6265_25298_1176513507}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_2036312319}[下]{style="font-family:宋体"}[DCLI]{lang="EN-US"}[为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[上收到]{style="font-family:宋体"}[InARP *packet-type*]{lang="EN-US"}[报文：硬件地址长度为]{style="font-family:宋体"}*[hard length]{lang="EN-US"}*[，硬件地址类型为]{style="font-family:宋体"}*[hard]{lang="EN-US"}*[（]{style="font-family:宋体"}*[hard]{lang="EN-US"}*[值为]{style="font-family:宋体"}[0x000f]{lang="EN-US"}[，表示帧中继），协议地址长度为]{style="font-family:宋体"}*[protocol length]{lang="EN-US"}*[，协议地址类型为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[（]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[值为]{style="font-family:宋体"}[0x0800]{lang="EN-US"}[，表示]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议），源协议地址为]{style="font-family:宋体"}*[source IP]{lang="EN-US"}*[，目的协议地址为]{style="font-family:宋体"}*[target IP]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_x6265_25298_199956221}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_x6265_25298_707227349}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Protocol not supported.]{lang="EN-US"}]{#struct_0_x6265_25298_2129563617}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_358384978}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[协议类型不支持]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Frame length error.]{lang="EN-US"}]{#struct_0_x6265_25298_x1307820734}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_999200872}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[帧长度错误]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Field length error.]{lang="EN-US"}]{#struct_0_x6265_25298_200021757}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_624260339}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[域长度错误]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Hardware type error.]{lang="EN-US"}]{#struct_0_x6265_25298_x996102007}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1055835028}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[硬件类型错误]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: IP address length error.]{lang="EN-US"}]{#struct_0_x6265_25298_1577113260}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199825149}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[协议地址长度错误]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Operation code error.]{lang="EN-US"}]{#struct_0_x6265_25298_1498604619}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1312762582}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[报文操作码不合法]{style="font-family:宋体"}

[[Received an InARP packet on interface *interface-name*: Operation code not supported.]{lang="EN-US"}]{#struct_0_x6265_25298_1089149830}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x502380779}[收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文：]{style="font-family:宋体"}[报文操作码不支持]{style="font-family:宋体"}

[[Create dynamic MAP failed on interface *interface-name* : No IP address.]{lang="EN-US"}]{#struct_0_x6265_25298_199890685}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x894811967}[创建动态]{style="font-family:宋体"}[MAP]{lang="EN-US"}[失败：没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Create dynamic MAP failed on interface *interface-name* : Cannot create MAP on P2P interface.]{lang="EN-US"}]{#struct_0_x6265_25298_x1864519156}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_195540846}[创建动态]{style="font-family:宋体"}[MAP]{lang="EN-US"}[失败：]{style="font-family:宋体"}[P2P]{lang="EN-US"}[子接口不能创建]{style="font-family:宋体"}[MAP]{lang="EN-US"}

[[Create dynamic MAP failed on interface *interface-name* : Static or default MAP exist.]{lang="EN-US"}]{#struct_0_x6265_25298_x1371813533}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199694077}[创建动态]{style="font-family:宋体"}[MAP]{lang="EN-US"}[失败：已经存在静态或缺省]{style="font-family:宋体"}[MAP]{lang="EN-US"}

[[Interface *interface-name*: Failed to send a packet.]{lang="EN-US"}]{#struct_0_x6265_25298_x708028535}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_2144179544}[：报文发送失败]{style="font-family:宋体"}

[[Interface *interface-name*: Unknown error.]{lang="EN-US"}]{#struct_0_x6265_25298_1098207331}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_809356679}[：未知错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc127787932}[]{#_Toc96758239}[[表1-3 ]{lang="EN-US"}[debugging fr lmi]{lang="EN-US"}]{#struct_0_x6265_25298_199759613}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_7623497}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_x266780353}

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_1971921252}

[[Sent a LMI *packet-type message-type* packet on interface *interface-name*:]{lang="EN-US"}]{#struct_0_x6265_25298_x1360871606}

[[  ssn=*ssn*, rsn=*rsn*]{lang="EN-US"}]{#struct_0_x6265_25298_2076343494}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x95445883}[上发送]{style="font-family:宋体"}[LMI *packet-type message-type*]{lang="EN-US"}[报文：发送报文序列号为]{style="font-family:宋体"}*[ssn]{lang="EN-US"}*[，接收报文序列号为]{style="font-family:宋体"}*[rsn]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x6265_25298_x165701790}[：全状态报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIV]{lang="EN-US"}]{#struct_0_x6265_25298_200611581}[：链路完整性验证报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[asyn]{lang="EN-US"}]{#struct_0_x6265_25298_x512926194}[：异步]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态报文]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*]{#struct_0_x6265_25298_x257901506}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status]{lang="EN-US"}]{#struct_0_x6265_25298_101613139}[：状态消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status enquiry]{lang="EN-US"}]{#struct_0_x6265_25298_1548652644}[：状态请求消息]{lang="EN-US" style="font-family:宋体"}

[[Received a LMI *packet-type message-type* packet on interface *interface-name*:]{lang="EN-US"}]{#struct_0_x6265_25298_1783781977}

[[  ssn=*ssn*, rsn=*rsn*]{lang="EN-US"}]{#struct_0_x6265_25298_200677117}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1016499178}[上收到]{style="font-family:宋体"}[LMI *packet-type message-type*]{lang="EN-US"}[报文：发送报文序列号为]{style="font-family:宋体"}*[ssn]{lang="EN-US"}*[，接收报文序列号为]{style="font-family:宋体"}*[rsn]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x6265_25298_1509045467}[：全状态报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIV]{lang="EN-US"}]{#struct_0_x6265_25298_1148414710}[：链路完整性验证报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[asyn]{lang="EN-US"}]{#struct_0_x6265_25298_x1058770715}[：异步]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态报文]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*]{#struct_0_x6265_25298_661303345}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status]{lang="EN-US"}]{#struct_0_x6265_25298_200087296}[：状态消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status enquiry]{lang="EN-US"}]{#struct_0_x6265_25298_x912904911}[：状态请求消息]{lang="EN-US" style="font-family:宋体"}

[[Sent a LMI *packet-type message-type* packet on interface *interface-name*:]{lang="EN-US"}]{#struct_0_x6265_25298_151954799}

[[  ssn=*ssn*, rsn=*rsn*]{lang="EN-US"}]{#struct_0_x6265_25298_78805283}

[*[  ]{lang="EN-US"}*[PVCs=*num*]{lang="EN-US"}]{#struct_0_x6265_25298_x1073495532}

[*[  ]{lang="EN-US"}*[DLCI=*DLCI*, *active*, new=*new*]{lang="EN-US"}]{#struct_0_x6265_25298_200152832}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1368998814}[上发送]{style="font-family:宋体"}[LMI *packet-type message-type*]{lang="EN-US"}[报文：发送报文序列号为]{style="font-family:宋体"}*[ssn]{lang="EN-US"}*[，接收报文序列号为]{style="font-family:宋体"}*[rsn]{lang="EN-US"}*[，虚链路号为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的状态为]{style="font-family:宋体"}*[act]{lang="EN-US"}*[，是否新建标志为]{style="font-family:宋体"}*[new]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[个数为]{style="font-family:宋体"}*[num]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"} [类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x6265_25298_1957415092}[：全状态报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIV]{lang="EN-US"}]{#struct_0_x6265_25298_1309531533}[：链路完整性验证报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[asyn]{lang="EN-US"}]{#struct_0_x6265_25298_902404065}[：异步]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态报文]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*]{#struct_0_x6265_25298_199956224}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status]{lang="EN-US"}]{#struct_0_x6265_25298_707227344}[：状态消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status enquiry]{lang="EN-US"}]{#struct_0_x6265_25298_2129563614}[：状态请求消息]{lang="EN-US" style="font-family:宋体"}

[*[active]{lang="EN-US"}*]{#struct_0_x6265_25298_358188370}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_x6265_25298_1122171116}[：表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[处于非激活状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_x6265_25298_200021760}[：表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[处于激活状态]{style="font-family:宋体"}

[*[new]{lang="EN-US"}*]{#struct_0_x6265_25298_x2096728840}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x6265_25298_x2004119833}[：表示不是新创建的]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x6265_25298_600987835}[：表示新创建的]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[Received a LMI *packet-type message-type* packet on interface *interface-name*:]{lang="EN-US"}]{#struct_0_x6265_25298_25930818}

[[  ssn=*ssn*, rsn=*rsn*]{lang="EN-US"}]{#struct_0_x6265_25298_199825152}

[*[  ]{lang="EN-US"}*[PVCs=*num*]{lang="EN-US"}]{#struct_0_x6265_25298_x457710510}

[[  DLCI=*DLCI*, *active*, new=*new*]{lang="EN-US"}]{#struct_0_x6265_25298_x1609633107}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x764951867}[上收到]{style="font-family:宋体"}[LMI *packet-type message-type*]{lang="EN-US"}[报文：发送报文序列号为]{style="font-family:宋体"}*[ssn]{lang="EN-US"}*[，接收报文序列号为]{style="font-family:宋体"}*[rsn]{lang="EN-US"}*[，虚链路号为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的状态为]{style="font-family:宋体"}*[act]{lang="EN-US"}*[，是否新建标志为]{style="font-family:宋体"}*[new]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[个数为]{style="font-family:宋体"}*[num]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[的]{style="font-family:宋体"} [类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x6265_25298_199890688}[：全状态报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LIV]{lang="EN-US"}]{#struct_0_x6265_25298_x894811964}[：链路完整性验证报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[asyn]{lang="EN-US"}]{#struct_0_x6265_25298_x1864715764}[：异步]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态报文]{style="font-family:宋体"}

[*[message-type]{lang="EN-US"}*]{#struct_0_x6265_25298_x244080470}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status]{lang="EN-US"}]{#struct_0_x6265_25298_30085223}[：状态消息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[status enquiry]{lang="EN-US"}]{#struct_0_x6265_25298_199694080}[：状态请求消息]{lang="EN-US" style="font-family:宋体"}

[*[active]{lang="EN-US"}*]{#struct_0_x6265_25298_x1428072570}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_x6265_25298_1700313943}[：表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[处于非激活状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_x6265_25298_199759616}[：表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[处于激活状态]{style="font-family:宋体"}

[*[new]{lang="EN-US"}*]{#struct_0_x6265_25298_x266780358}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x6265_25298_1972380004}[：表示不是新创建的]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x6265_25298_482555178}[：表示新创建的]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[Timeout on interface *interface-name* (interface type=*interface type*, state=*state*).]{lang="EN-US"}]{#struct_0_x6265_25298_200611584}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x512926197}[上超时，此接口类型为]{style="font-family:宋体"}*[interface type]{lang="EN-US"}*[，状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[interface type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DTE]{lang="EN-US"}]{#struct_0_x6265_25298_x257704898}[：数据终端设备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_x6265_25298_841687113}[：数据电路终接设备]{style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_x6265_25298_200677120}[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_x6265_25298_x939815963}[：链路连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_x6265_25298_1380555790}[：]{lang="EN-US" style="font-family:宋体"}[链路]{style="font-family:宋体"}[断开]{lang="EN-US" style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Packet length error.]{lang="EN-US"}]{#struct_0_x6265_25298_200087295}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x912904912}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[报文长度错误]{style="font-family:宋体"}

[[Interface *interface-name*: DTE received illegal LMI status enquiry packet.]{lang="EN-US"}]{#struct_0_x6265_25298_151758191}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1708027931}[：]{style="font-family:宋体"}[DTE]{lang="EN-US"}[端收到非法状态请求报文]{style="font-family:宋体"}

[[Interface *interface-name*: DCE received illegal LMI status packet.]{lang="EN-US"}]{#struct_0_x6265_25298_200152831}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1368998813}[：]{style="font-family:宋体"}[DCE]{lang="EN-US"}[端收到非法状态应答报文]{style="font-family:宋体"}

[[Interface *interface-name*: Received LMI type different from the configured type.]{lang="EN-US"}]{#struct_0_x6265_25298_x771468263}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199956223}[：]{style="font-family:宋体"}[接收]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文封装类型与端口配置类型不一致]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Packet format error.]{lang="EN-US"}]{#struct_0_x6265_25298_707227347}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_2129563615}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[报文格式错误]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Call reference information unit content error.]{lang="EN-US"}]{#struct_0_x6265_25298_200021759}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_624260353}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Call reference]{lang="EN-US"}[信息单元内容错误]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Message type value is illegal.]{lang="EN-US"}]{#struct_0_x6265_25298_x2143113073}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199825151}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Message type]{lang="EN-US"}[取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Locking Shift information unit value is illegal.]{lang="EN-US"}]{#struct_0_x6265_25298_x457710509}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1610091860}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[类型]{style="font-family:宋体"}[Locking Shift]{lang="EN-US"}[信息单元内容取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: ANSI message type is illegal.]{lang="EN-US"}]{#struct_0_x6265_25298_1513076908}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199890687}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[异步状态报文的消息类型非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Report type ID error.]{lang="EN-US"}]{#struct_0_x6265_25298_x894811969}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199694079}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Report type]{lang="EN-US"}[信息单元标识取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Report type length error.]{lang="EN-US"}]{#struct_0_x6265_25298_x708028529}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_2144441687}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Report type]{lang="EN-US"}[信息单元长度取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Report type error.]{lang="EN-US"}]{#struct_0_x6265_25298_x1977045908}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_199759615}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Report]{lang="EN-US"}[类型不合法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: LIV ID error.]{lang="EN-US"}]{#struct_0_x6265_25298_x266780355}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_200611583}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Link integrity verification]{lang="EN-US"}[信息单元标识取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: LIV length error.]{lang="EN-US"}]{#struct_0_x6265_25298_x512926196}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x257770434}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[Link integrity verification]{lang="EN-US"}[信息单元长度取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: PVC status error in LIV.]{lang="EN-US"}]{#struct_0_x6265_25298_200677119}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1016499164}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态字段取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: PVC status unit length error.]{lang="EN-US"}]{#struct_0_x6265_25298_1508259036}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_200087290}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态信息单元长度取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: PVC ID error.]{lang="EN-US"}]{#struct_0_x6265_25298_x912904917}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_152085871}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态信息单元标识取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: PVC length error.]{lang="EN-US"}]{#struct_0_x6265_25298_200152826}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_969653350}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态信息单元长度取值非法]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Exceeding the upper limit for the PVC count.]{lang="EN-US"}]{#struct_0_x6265_25298_199956218}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x2013761828}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[个数超出最大限制]{style="font-family:宋体"}

[[Received a LMI packet on interface *interface-name*: Illegal DLCI.]{lang="EN-US"}]{#struct_0_x6265_25298_x9940216}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_200021754}[收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[报文：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态信息单元]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[取值非法]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send a packet.]{lang="EN-US"}]{#struct_0_x6265_25298_624260340}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x186797936}[：报文发送失败]{style="font-family:宋体"}

[[Interface *interface-name*: Unknown error.]{lang="EN-US"}]{#struct_0_x6265_25298_199825146}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1498604630}[：]{style="font-family:宋体"}[未知错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging fr packet]{lang="EN-US"}]{#struct_0_x6265_25298_1312303828}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_32683755}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_x452810887}

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_199890682}

[[Sent a *packet-type* packet on interface *interface-name* DLCI *DLCI*, packet length is *length.*]{lang="EN-US"}]{#struct_0_x6265_25298_x894811974}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x1864715765}[下虚电路号为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[上发送]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet type]{lang="EN-US"}*[的类型有：]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}

[[Received a *packet-type* packet on interface *interface-name* DLCI *DLCI*, packet length is *length.*]{lang="EN-US"}]{#struct_0_x6265_25298_1322003471}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_x2080403018}[下虚电路号为]{style="font-family:宋体"}*[DLCI]{lang="EN-US"}*[上收到]{style="font-family:宋体"}*[packet-type]{lang="EN-US"}*[报文，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[packet type]{lang="EN-US"}*[的类型有：]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[ISIS]{lang="EN-US"}[、]{style="font-family:宋体"}[MPLS]{lang="EN-US"}

[[Interface *interface-name* DLCI *DLCI*: DLCI reserved]{lang="EN-US"}]{#struct_0_x6265_25298_x830258553}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ DLCI *DLCI*]{lang="EN-US"}]{#struct_0_x6265_25298_199694074}[：]{style="font-family:宋体"}[保留虚链路号]{style="font-family:宋体"}

[[Interface *interface-name* DLCI *DLCI*: Type unrecognized]{lang="EN-US"}]{#struct_0_x6265_25298_x708028534}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ DLCI *DLCI*]{lang="EN-US"}]{#struct_0_x6265_25298_2144114008}[：]{style="font-family:宋体"}[非法协议类型]{style="font-family:宋体"}

[[Interface *interface-name* DLCI *DLCI*: PVC unavailable]{lang="EN-US"}]{#struct_0_x6265_25298_1178166408}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ DLCI *DLCI*]{lang="EN-US"}]{#struct_0_x6265_25298_x472911734}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[没有配置或非激活]{style="font-family:宋体"}

[[Interface *interface-name* DLCI *DLCI*: MAP unavailable]{lang="EN-US"}]{#struct_0_x6265_25298_x880505272}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ DLCI *DLCI*]{lang="EN-US"}]{#struct_0_x6265_25298_x1413706795}[：]{style="font-family:宋体"}[MAP]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Interface *interface-name* DLCI *DLCI*: Unknown reason]{lang="EN-US"}]{#struct_0_x6265_25298_199759610}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ DLCI *DLCI*]{lang="EN-US"}]{#struct_0_x6265_25298_x266780352}[：]{style="font-family:宋体"}[未知的原因]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging fr packet-hex]{lang="EN-US"}]{#struct_0_x6265_25298_1971986788}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_26290835}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_1765404554}

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_40510896}

[[Sent a packet on interface *interface-name*, packet length is *length.*]{lang="EN-US"}]{#struct_0_x6265_25298_2114864366}

[[The packet content in hex format:]{lang="EN-US"}]{#struct_0_x6265_25298_1067305486}

[*[  hex sequence]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x6265_25298_189897454}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_200611578}[上发送报文，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}[。]{style="font-family:宋体"}*[十六进制显示报文内容：*十六进制序列*]{style="font-family:宋体"}

[[Received a packet on interface *interface-name*, packet length is *length.*]{lang="EN-US"}]{#struct_0_x6265_25298_207117847}

[[The packet content in hex format:]{lang="EN-US"}]{#struct_0_x6265_25298_x439319738}

[*[  hex sequence]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x6265_25298_1574900338}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_1908683744}[上收到报文，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}[。]{style="font-family:宋体"}*[十六进制显示报文内容：*十六进制序列*]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6265_25298_x378032375}

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x226432306}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口连接，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，两端配置好]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[DTE]{lang="EN-US"}[接口关闭]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能，]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的]{style="font-family:宋体"}[DCE]{lang="EN-US"}[接口使能]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x576198002}

[[\<RouterA\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_200677114}

[\[RouterA\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterA]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterA-Serial2/1/0\] undo fr inarp ip 200]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] ip address 2.2.2.1 255.255.255.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_x6265_25298_1016499177}

[[\<RouterB\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_1508455643}

[\[RouterB\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterB]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterB-Serial2/1/0\] fr inarp ip 200]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] ip address 2.2.2.2 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6265_25298_x24417688}[打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的帧中继事件调试信息开关。将]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口进行]{style="font-family:宋体"}**[undo ip address]{lang="EN-US"}**[操作时，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上可以看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterA\> debugging fr event]{lang="EN-US"}]{#struct_0_x6265_25298_200087289}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/EVENT:]{lang="EN-US"}

[Deleted IP address on interface Serial2/1/0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_1043410228}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x443202732}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口连接，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，接口或虚链路使能]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能（缺省使能），两端配置好]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_x6265_25298_831924083}

[[\<RouterA\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_x168681741}

[\[RouterA\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterA]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterA-Serial2/1/0\] ip address 2.2.2.1 255.255.255.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_x6265_25298_x592472539}

[[\<RouterB\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_200152825}

[\[RouterB\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterB]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterB-Serial2/1/0\] ip address 2.2.2.2 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6265_25298_969653351}[打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的帧中继逆向地址解析协议调试信息开关。将]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口进行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[、]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作时，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上可以看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterA\> debugging fr inarp]{lang="EN-US"}]{#struct_0_x6265_25298_x1392109473}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/INARP:]{lang="EN-US"}

[Sent an InARP request packet on interface serial2/1/0 DLCI 200:]{lang="EN-US"}

[  hard length=2, hard=0x000F]{lang="EN-US"}

[  protocol length=4, protocol=0x0800]{lang="EN-US"}

[  source IP=2.2.2.1, target IP=0.0.0.0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_1026429711}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的虚链路]{style="font-family:宋体"}[200]{lang="EN-US"}[上发送]{style="font-family:宋体"}[InARP]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}*

[[\*Sep 10 09:36:30:715 2013 RouterA FR/7/INARP:]{lang="EN-US"}]{#struct_0_x6265_25298_199956217}

[Received an InARP reply packet on interface serial2/1/0 DLCI 200:]{lang="EN-US"}

[  hard length=2, hard=0x000F]{lang="EN-US"}

[  protocol length=4, protocol=0x0800]{lang="EN-US"}

[  source IP=2.2.2.2, target IP=0.0.0.0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x2013761841}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的虚链路]{style="font-family:宋体"}[200]{lang="EN-US"}[上收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[响应报文。]{style="font-family:宋体"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_1200044437}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口相连，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，接口或虚链路使能]{style="font-family:宋体"}[LMI]{lang="EN-US"}[（缺省使能）。两端配置好接口类型，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x1650577469}

[[\<RouterA\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_x1856882206}

[\[RouterA\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_x6265_25298_x1330473316}

[[\<RouterB\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_200021753}

[\[RouterB\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6265_25298_624260343}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[端打开帧中继]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议调试信息开关。将]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口进行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[、]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作时，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上可以看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterA\> debugging fr lmi]{lang="EN-US"}]{#struct_0_x6265_25298_x186797937}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/LMI:]{lang="EN-US"}

[Sent a LMI full status enquiry packet on interface serial2/1/0:]{lang="EN-US"}

[  ssn=1, rsn=0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x1309957407}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的虚链路上发送]{style="font-family:宋体"}[LMI]{lang="EN-US"}[全状态请求报文，包含收发序号。]{style="font-family:宋体"}*

[[\*Sep 10 09:36:30:715 2013[ RouterA FR/7/LMI:]{.TerminalDisplayChar}]{lang="EN-US"}]{#struct_0_x6265_25298_1608657337}

[Received a LMI full status packet on interface serial2/1/0:]{lang="EN-US"}

[  ssn=1, rsn=1]{lang="EN-US"}

[  PVCs=2]{lang="EN-US"}

[  DLCI=100, active, new=1]{lang="EN-US"}

[  DLCI=200, active, new=1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_1987608951}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的虚链路上收到]{style="font-family:宋体"}[LMI]{lang="EN-US"}[全状态响应报文，包含收发序号以及]{style="font-family:宋体"}[PVC]{lang="EN-US"}[信息。]{style="font-family:宋体"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_199825145}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口连接，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，接口或虚链路使能]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能（缺省使能），两端配置好]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_x6265_25298_1498604631}

[[\<RouterA\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_1312238292}

[\[RouterA\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[RouterA-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterA]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterA-Serial2/1/0\] ip address 2.2.2.1 255.255.255.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_x6265_25298_1401793078}

[[\<RouterB\> system-view]{lang="EN-US"}]{#struct_0_x6265_25298_199890681}

[\[RouterB\] interface serial 2/1/0]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[RouterB-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[]{lang="NO-BOK"}[RouterB]{lang="EN-US"}[-Serial2/1/0-fr-dlci-200\] quit]{lang="NO-BOK"}

[\[RouterB-Serial2/1/0\] ip address 2.2.2.2 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6265_25298_x894811971}[打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的帧中继数据报文调试信息开关和十六进制报文调试信息开关。将]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口进行]{style="font-family:宋体"}[ping -c 1 2.2.2.2]{lang="EN-US"}[操作时，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[上可以看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterA\> debugging fr packet]{lang="EN-US"}]{#struct_0_x6265_25298_x1864388085}

[\<RouterA\> debugging fr packet-hex]{lang="EN-US"}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET:]{lang="EN-US"}

[Sent an IP packet on interface serial2/1/0 DLCI 200, packet length is 88.]{lang="EN-US"}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET-HEX:]{lang="EN-US"}

[Sent a packet on interface serial2/1/0, packet length is 88.]{lang="EN-US"}

[The packet content in hex format:]{lang="EN-US"}

[  30 81 03 cc 45 00 00 54 06 35 00 00 ff 01 ad 6d]{lang="EN-US"}

[  02 02 02 01 02 02 02 02 08 00 2c 2a 19 01 00 00]{lang="EN-US"}

[  52 3f 25 33 00 08 50 57 08 09 0a 0b 0c 0d 0e 0f]{lang="EN-US"}

[  10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x235736019}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[DLCI 200]{lang="EN-US"}[上发送]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文，长度为]{style="font-family:宋体"}[88]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET:]{lang="EN-US"}]{#struct_0_x6265_25298_199694073}

[Received an IP packet on interface serial2/1/0 DLCI 200, packet length is 88.]{lang="EN-US"}

[\*Sep 10 09:36:30:715 2013 RouterA FR/7/PACKET-HEX:]{lang="EN-US"}

[Received a packet on interface serial2/1/0, packet length is 88.]{lang="EN-US"}

[The packet content in hex format:]{lang="EN-US"}

[  30 81 03 cc 45 00 00 54 00 10 00 00 ff 01 b3 92]{lang="EN-US"}

[  02 02 02 02 02 02 02 01 00 00 34 2a 19 01 00 00]{lang="EN-US"}

[  52 3f 25 33 00 08 50 57 08 09 0a 0b 0c 0d 0e 0f]{lang="EN-US"}

[  10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x708028539}*[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[DLCI 200]{lang="EN-US"}[上收到]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文，长度为]{style="font-family:宋体"}[88]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#1655594421 .myid}
[]{#_Toc404785784}[]{#struct_0_x6265_25298_585069774}[]{#_Toc383418934}[]{#_Toc381342142}

**帧中继 \-- 帧中继调试命令 \-- debugging fr compression iphc**

------------------------------------------------------------------------

[**[debugging fr compression iphc]{lang="EN-US"}**]{#struct_0_x6265_25298_x18750310}[命令用来打开帧中继]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩调试信息开关。]{style="font-family:宋体"}

[**[undo debugging fr compression iphc]{lang="EN-US"}**]{#struct_0_x6265_25298_x1684352976}[命令用来关闭帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6265_25298_914244005}

[**[debugging fr compression iphc]{lang="EN-US"}**[ { **rtp** \| **tcp** }]{lang="EN-US"}]{#struct_0_x6265_25298_x1063886603}

[**[undo debugging fr compression iphc]{lang="EN-US"}**[ { **rtp** \| **tcp** }]{lang="EN-US"}]{#struct_0_x6265_25298_x1590501872}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6265_25298_585266382}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_x178800896}[压缩的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6265_25298_x1662319862}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x6265_25298_1419794071}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6265_25298_669833015}

[[network-admin]{lang="EN-US"}]{#struct_0_x6265_25298_x1962001783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6265_25298_1808022519}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6265_25298_585200846}

[**[rtp]{lang="EN-US"}**]{#struct_0_x6265_25298_551794915}[：表示]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩调试信息开关。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x6265_25298_1439769425}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6265_25298_x756660999}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_1148777171}[压缩调试信息包括：]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商信息和压缩]{style="font-family:宋体"}[/]{lang="EN-US"}[解压缩信息。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging fr compression iphc]{lang="EN-US"}]{#struct_0_x6265_25298_1649933429}[命令输出信息描述表（]{style="font-family:黑体"}[IPHC]{lang="EN-US"}[协商信息）]{style="font-family:黑体"}

[]{#table_struct_0_370606285}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_585921742}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_193061904}

[[Received IPHC negotiation info on interface *interface-name* DLCI *dlci-number*.]{lang="EN-US"}]{#struct_0_x6265_25298_x1609808622}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x6265_25298_585856206}[，]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[dlci-number]{lang="EN-US"}*[上收到]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商信息]{style="font-family:宋体"}

[[Received an active event in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_918104894}

[[IPHC negotiation started.]{lang="EN-US"}]{#struct_0_x6265_25298_x1653018586}

[[Sent a config REQ (F = 1) packet, FSM state changed to I1.]{lang="EN-US"}]{#struct_0_x6265_25298_585397455}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_2128822423}[状态机在去使能状态收到了激活事件]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_766513039}[开始协商]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}]{#struct_0_x6265_25298_585331919}[报文，状态机进入]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config REQ (F = \*) packet in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_1330070630}

[[Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.]{lang="EN-US"}]{#struct_0_x6265_25298_x1025370852}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_585528527}[状态机在去使能状态下收到]{style="font-family:宋体"}[REQ (F =\*)]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6265_25298_1652149569}[报文和]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，状态机进去]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Error: Received a config ACK packet in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_x757181132}

[[状态机收到错误事件：去使能状态下收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x6265_25298_585462991}[报文]{style="font-family:宋体"}

[[Error: Received a negotiation timer timeout event in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_x339655409}

[[状态机收到错误事件：去使能状态下收到协商定时器超时事件]{style="font-family:宋体"}]{#struct_0_x6265_25298_786602958}

[[Error: Received an illegal event in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_585135311}

[[状态机收到错误事件：去使能状态下收到非法事件]{style="font-family:宋体"}]{#struct_0_x6265_25298_x465389984}

[[Error: Received an active event in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585069775}

[[状态机收到错误事件：]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_x18750311}[状态收到激活事件]{style="font-family:宋体"}

[[Received a config REQ (F = \*) packet in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1684352975}

[[Sent a config ACK packet, FSM state changed to I3.]{lang="EN-US"}]{#struct_0_x6265_25298_585266383}

[[状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_x178800897}[阶段收到]{style="font-family:宋体"}[REQ (F = \*)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，状态机进入]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config ACK packet in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1662254326}

[[FSM state changed to I2.]{lang="EN-US"}]{#struct_0_x6265_25298_585200847}

[[状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_551794914}[阶段收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[进入]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_1439769426}[状态]{style="font-family:宋体"}

[[Received a negotiation timer timeout (+) event in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585921743}

[[Sent a config REQ (F = 1) packet.]{lang="EN-US"}]{#struct_0_x6265_25298_193061903}

[[状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_x1609808621}[状态收到协商定时器超时]{style="font-family:宋体"}[(+)]{lang="EN-US"}[事件，并发送]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a negotiation timer timeout (-) event in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585856207}

[[IPHC negotiation stopped.]{lang="EN-US"}]{#struct_0_x6265_25298_918104895}

[[状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_585397456}[状态收到协商定时器超时]{style="font-family:宋体"}[(-)]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_2128822420}[协商停止]{style="font-family:宋体"}

[[Error: Received an illegal event in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_766316431}

[[状态机收到错误事件：]{style="font-family:宋体"}[I1]{lang="EN-US"}]{#struct_0_x6265_25298_585331920}[状态收到非法事件]{style="font-family:宋体"}

[[Error: Received an active event in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1008581523}

[[状态机收到错误事件：]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_1069831045}[状态收到激活事件]{style="font-family:宋体"}

[[Received a config REQ (F = 1) packet in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585528528}

[[Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.]{lang="EN-US"}]{#struct_0_x6265_25298_1652149584}

[[状态机在]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_585462992}[状态下收到]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文和]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，状态机进入]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config REQ (F = 0) packet in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x339655410}

[[Sent a config ACK packet, FSM state changed to Operational.]{lang="EN-US"}]{#struct_0_x6265_25298_787192781}

[[IPHC negotiation done.]{lang="EN-US"}]{#struct_0_x6265_25298_585135312}

[[状态机在]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_x465389983}[阶段收到]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，状态机进入]{style="font-family:宋体"}[Operational]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_x1877479250}[协商完成]{style="font-family:宋体"}

[[Error: Received a config ACK packet in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585069776}

[[状态机收到错误事件：在]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_x18750312}[状态收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Received a negotiation timer timeout (+) event in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585266384}

[[Sent a config REQ (F = 1) packet, FSM state changed to I1.]{lang="EN-US"}]{#struct_0_x6265_25298_x178800890}

[[状态机在]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_585200848}[阶段收到协商定时器超时]{style="font-family:宋体"}[(+)]{lang="EN-US"}[事件，并发送]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文，状态机进入]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a negotiation timer timeout (-) event in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_551794925}

[[IPHC negotiation stopped.]{lang="EN-US"}]{#struct_0_x6265_25298_x898882735}

[[状态机在]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_585921744}[状态收到协商定时器超时]{style="font-family:宋体"}[(-)]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_193061902}[协商停止]{style="font-family:宋体"}

[[Error: Received an illegal event in I2 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1609808620}

[[状态机收到错误事件：]{style="font-family:宋体"}[I2]{lang="EN-US"}]{#struct_0_x6265_25298_585856208}[状态下收到非法事件]{style="font-family:宋体"}

[[Error: Received an active event in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_918104884}

[[状态机收到错误事件：]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_585397457}[状态下收到激活事件]{style="font-family:宋体"}

[[Received a config REQ (F = 1) packet in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_2128822421}

[[Sent config ACK and config REQ (F = 0) packets, FSM state remains in I3.]{lang="EN-US"}]{#struct_0_x6265_25298_766381967}

[[状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_585331921}[状态下收到]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文和]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，状态机保持在]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config REQ (F = 0) packet in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1008581522}

[[Sent a config ACK packet, FSM state remains in I3.]{lang="EN-US"}]{#struct_0_x6265_25298_585528529}

[[状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_1652149583}[状态下收到]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，状态机保持在]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config ACK packet in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x756525786}

[[FSM state changed to Operational.]{lang="EN-US"}]{#struct_0_x6265_25298_585462993}

[[IPHC negotiation done.]{lang="EN-US"}]{#struct_0_x6265_25298_x339655411}

[[状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_585135313}[状态收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，并进入]{style="font-family:宋体"}[Operational]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_x465389982}[协商完成]{style="font-family:宋体"}

[[Received a negotiation timer timeout (+) event in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1877413714}

[[Sent a config REQ (F = 0) packet, FSM state remains in I3.]{lang="EN-US"}]{#struct_0_x6265_25298_585069777}

[[状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_x18750313}[状态收到协商定时器超时]{style="font-family:宋体"}[(+)]{lang="EN-US"}[事件，并发送]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，状态机保持在]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a negotiation timer timeout (-) event in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_585266385}

[[IPHC negotiation stopped.]{lang="EN-US"}]{#struct_0_x6265_25298_x178800891}

[[状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_x1662385398}[状态收到协商定时器超时]{style="font-family:宋体"}[(-)]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_585200849}[协商停止]{style="font-family:宋体"}

[[Error: Received an illegal event in I3 state.]{lang="EN-US"}]{#struct_0_x6265_25298_551794924}

[[状态机收到错误事件：]{style="font-family:宋体"}[I3]{lang="EN-US"}]{#struct_0_x6265_25298_585921745}[状态收到非法事件]{style="font-family:宋体"}

[[Error: Received an active event in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_193061901}

[[状态机收到错误事件：]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_585856209}[状态收到激活事件]{style="font-family:宋体"}

[[Error: Received a negotiation timer timeout event in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_918104885}

[[状态机收到错误事件：]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_585397450}[状态收到协商定时器超时事件]{style="font-family:宋体"}

[[Received a config REQ (F = 1) packet in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_2128822426}

[[Sent config ACK and config REQ (F = 0) packets, FSM state changed to I3.]{lang="EN-US"}]{#struct_0_x6265_25298_766185359}

[[状态机在]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_585331914}[状态收到]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文和]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，状态机进入]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config REQ (F = 0) packet in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_1330070641}

[[Sent a config ACK packet, FSM state remains in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_585528522}

[[状态机在]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_1652149574}[状态收到]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，状态机保持]{style="font-family:宋体"}[Operational]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Received a config ACK packet in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_585462986}

[[状态机收到错误事件：]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_1616659730}[状态收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Error: Received an illegal event in Operational state.]{lang="EN-US"}]{#struct_0_x6265_25298_x2041694946}

[[状态机收到错误事件：]{style="font-family:宋体"}[Operational]{lang="EN-US"}]{#struct_0_x6265_25298_585135306}[状态收到非法事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_1873262181}[状态机相关说明：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x6265_25298_271982199}[：协商激活事件，状态机只在]{style="font-family:宋体"}[Disable]{lang="EN-US"}[状态时收到该事件。收到该事件后开始协商。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQ (F = 1)]{lang="EN-US"}]{#struct_0_x6265_25298_x1239711081}[：请求报文]{style="font-family:
宋体"}[(F = 1)]{lang="EN-US"}[，表示收到此报文后需要回复]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文和]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文。在]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态时只需回复]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQ (F = 0)]{lang="EN-US"}]{#struct_0_x6265_25298_507793668}[：请求报文]{style="font-family:
宋体"}[(F = 0)]{lang="EN-US"}[，表示收到此报文后，需要回复]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文。在]{style="font-family:宋体"}[Disable]{lang="EN-US"}[状态时，需同时回复]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQ (F = \*)]{lang="EN-US"}]{#struct_0_x6265_25298_x460005738}[：表示不区别]{style="font-family:
宋体"}[F = 1]{lang="EN-US"}[还是]{style="font-family:宋体"}[F = 0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACK]{lang="EN-US"}]{#struct_0_x6265_25298_585069770}[：应答报文，接收到对端]{style="font-family:宋体"}[REQ (F = \*)]{lang="EN-US"}[报文后，回复此报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[timeout (+)]{lang="EN-US"}]{#struct_0_x6265_25298_x18750314}[：定时器超时]{style="font-family:
宋体"}[(+)]{lang="EN-US"}[事件。发送]{style="font-family:宋体"}[REQ (F = \*)]{lang="EN-US"}[报文后，在规定时间内没有收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文且定时器超时次数没有超过最大值时收到此事件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[timeout (-)]{lang="EN-US"}]{#struct_0_x6265_25298_x1684352972}[：定时器超时]{style="font-family:
宋体"}[(-)]{lang="EN-US"}[事件。发送]{style="font-family:宋体"}[REQ (F = \*)]{lang="EN-US"}[报文后，在规定时间内没有收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文且定时器超时次数超过了到最大值时收到此事件。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x6265_25298_x1411354823}[：表示在某状态下收到某个事件是错误的，不作动作，状态不改变。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging fr compression iphc]{lang="EN-US"}]{#struct_0_x6265_25298_x654289496}[命令输出信息描述表（]{style="font-family:黑体"}[IPHC]{lang="EN-US"}[压缩]{style="font-family:黑体"}[/]{lang="EN-US"}[解压缩信息）]{style="font-family:黑体"}

[]{#table_struct_0_691889689}[[字段]{style="font-family:黑体"}]{#struct_0_x6265_25298_x1330503140}

[[描述]{style="font-family:黑体"}]{#struct_0_x6265_25298_585266378}

[[RHC]{lang="EN-US"}]{#struct_0_x6265_25298_x988104966}

[[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_1299650253}[头压缩信息]{style="font-family:宋体"}

[[THC]{lang="EN-US"}]{#struct_0_x6265_25298_585200842}

[[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_551794919}[头压缩信息]{style="font-family:宋体"}

[[FULL_HEADER]{lang="EN-US"}]{#struct_0_x6265_25298_1439769421}

[[未压缩的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x756923143}[或者]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文，解压端根据这个报文为解压后续的压缩报文创建或更新解压表项]{style="font-family:宋体"}

[[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_x6265_25298_585921738}

[[一种由解压端发送给压缩端的特殊报文，用来传输已经或者可能已经失去同步的压缩和解压表项的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x6265_25298_x998579174}[号来通知压缩端发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文来同步压缩和解压缩表项]{style="font-family:宋体"}

[[COMPRESSED_NON_TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x42070890}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_585856202}[报文。接口下配置]{style="font-family:宋体"}**[fr compression iphc enable]{lang="EN-US"}**[ **nonstandard**]{lang="EN-US"}[命令后，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该格式的报文]{style="font-family:宋体"}

[[COMPRESSED_TCP]{lang="EN-US"}]{#struct_0_x6265_25298_918104890}

[[压缩的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x1653018590}[报文。成功压缩时，压缩端会将]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文压缩成该格式的报文]{style="font-family:宋体"}

[[COMPRESSED_RTP_8]{lang="EN-US"}]{#struct_0_x6265_25298_585397451}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_2128822427}[报文。当接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数小于等于]{style="font-family:宋体"}[256]{lang="EN-US"}[时，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该种格式的报文]{style="font-family:宋体"}

[[COMPRESSED_RTP_16]{lang="EN-US"}]{#struct_0_x6265_25298_766250895}

[[压缩的]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_585331915}[报文。当接口上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数大于]{style="font-family:宋体"}[256]{lang="EN-US"}[时，成功压缩时，压缩端会将]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文压缩成该种格式的报文]{style="font-family:宋体"}

[[ERROR]{lang="EN-US"}]{#struct_0_x6265_25298_1330070642}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_x1025239777}[压缩]{style="font-family:宋体"}[/]{lang="EN-US"}[解压缩过程的错误信息]{style="font-family:宋体"}

[[WARNING]{lang="EN-US"}]{#struct_0_x6265_25298_585528523}

[[IPHC]{lang="EN-US"}]{#struct_0_x6265_25298_1652149573}[压缩]{style="font-family:宋体"}[/]{lang="EN-US"}[解压缩过程的提示信息]{style="font-family:宋体"}

[[received]{lang="EN-US"}]{#struct_0_x6265_25298_x756525773}

[[接收报文]{style="font-family:宋体"}]{#struct_0_x6265_25298_585462987}

[[sent]{lang="EN-US"}]{#struct_0_x6265_25298_1616659729}

[[发送报文]{style="font-family:宋体"}]{#struct_0_x6265_25298_x2042153699}

[[connect ID]{lang="EN-US"}]{#struct_0_x6265_25298_585135307}

[[报文流标识，表示压缩]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6265_25298_1873262182}[解压缩的某条流。压缩端和解压端根据这个]{style="font-family:宋体"}[ID]{lang="EN-US"}[号来查找压缩和解压缩表项]{style="font-family:宋体"}

[[checksum]{lang="EN-US"}]{#struct_0_x6265_25298_272178807}

[[校验和]{style="font-family:宋体"}]{#struct_0_x6265_25298_585069771}

[[seq]{lang="EN-US"}]{#struct_0_x6265_25298_x18750315}

[[Sequence Number]{lang="EN-US"}]{#struct_0_x6265_25298_x1684352971}[，报文的序列号]{style="font-family:宋体"}

[[gen]{lang="EN-US"}]{#struct_0_x6265_25298_585266379}

[[Generation Number]{lang="EN-US"}]{#struct_0_x6265_25298_x988104967}[字段用来检测]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文压缩和解压缩的一致性]{style="font-family:宋体"}

[[Sent uncompressed packets]{lang="EN-US"}]{#struct_0_x6265_25298_1299715789}

[[发送了没有压缩的报文。压缩过程中，当检测到压缩表项为空，不能对报文进行压缩，为保证报文传输，会发送没有经过压缩的报文，并打印该条信息]{style="font-family:宋体"}]{#struct_0_x6265_25298_585200843}

[[The compression context of TCP is invalid]{lang="EN-US"}]{#struct_0_x6265_25298_551794918}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_1439769422}[报文过程中检测到压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[IP header mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_585921739}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x998579175}[报文过程中检测到]{style="font-family:宋体"}[IP]{lang="EN-US"}[头与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[TCP header mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_585856203}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_918104891}[报文过程中检测到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_URG code error]{lang="EN-US"}]{#struct_0_x6265_25298_x1653018591}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143485901}[报文过程中检测到]{style="font-family:宋体"}[Delta URG]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[th_URG mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_1182227273}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_2050348422}[报文过程中检测到]{style="font-family:宋体"}[URG]{lang="EN-US"}[字段与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_win code error]{lang="EN-US"}]{#struct_0_x6265_25298_x2143551437}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x992990071}[报文过程中检测到]{style="font-family:宋体"}[Delta Window]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_ACK code error]{lang="EN-US"}]{#struct_0_x6265_25298_x409524603}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143354829}[报文过程中检测到]{style="font-family:宋体"}[Delta Acknowledgment Number]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta th_seq code error]{lang="EN-US"}]{#struct_0_x6265_25298_x931148781}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143420365}[报文过程中检测到]{style="font-family:宋体"}[Delta Sequence]{lang="EN-US"}[字段编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The flag bits of th_URG, th_seq, and th_win are set]{lang="EN-US"}]{#struct_0_x6265_25298_937572617}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_2020871767}[报文过程中检测到]{style="font-family:宋体"}[URG]{lang="EN-US"}[字段、]{style="font-family:宋体"}[Sequence Number]{lang="EN-US"}[字段和]{style="font-family:宋体"}[Window]{lang="EN-US"}[字段的标识位被置为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Delta IP ID code error]{lang="EN-US"}]{#struct_0_x6265_25298_x2143748045}

[[压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x6265_25298_1520635328}[报文过程中检测到]{style="font-family:宋体"}[Delta IP ID]{lang="EN-US"}[编码错误。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The compression context of NON_TCP is invalid]{lang="EN-US"}]{#struct_0_x6265_25298_x2143813581}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_639979772}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文过程中检测到]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[的压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[UDP checksum mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_835956414}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143616973}[报文过程中检测到]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头的]{style="font-family:宋体"}[Checksum]{lang="EN-US"}[字段与压缩表项中的不匹配。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The number of compressed NON_TCP packets is out of range]{lang="EN-US"}]{#struct_0_x6265_25298_1413102134}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_x1976886321}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[过程中检测到在两个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文之间，发送的]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文的数量超出了规定的范围]{style="font-family:宋体"}

[[The time for compressing NON_TCP packet is lawless]{lang="EN-US"}]{#struct_0_x6265_25298_x2143682509}

[[将]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_1767552621}[报文压缩成]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[报文的过程中检测到压缩的报文的时间段非法。这时压缩端会发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文来同步压缩端和解压端（在每发送一个]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文后的一段时间内压缩的]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}[压缩报文是合法的，不在这个时间段内对报文进行压缩是非法的）]{style="font-family:宋体"}

[[The delta values of timestamp,sequence number, or IP ID are lawless]{lang="EN-US"}]{#struct_0_x6265_25298_x2142961613}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_x578022323}[报文的过程中检测到时间戳的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值、报文序列号的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值或者]{style="font-family:宋体"}[IP ID]{lang="EN-US"}[的]{style="font-family:宋体"}[delta]{lang="EN-US"}[值非法。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The compression context of RTP is invalid]{lang="EN-US"}]{#struct_0_x6265_25298_x353637678}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143027149}[报文的过程中检测到]{style="font-family:宋体"}[RTP]{lang="EN-US"}[的压缩表项无效。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[The delta value of the IP ID is lawless]{lang="EN-US"}]{#struct_0_x6265_25298_x1068191669}

[[压缩]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x6265_25298_x2143485900}[报文的过程中检测到]{style="font-family:宋体"}[IP]{lang="EN-US"}[头]{style="font-family:宋体"}[Delta ID]{lang="EN-US"}[值非法。这时压缩端会发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，同时更新压缩表项]{style="font-family:宋体"}

[[Connect ID xx out of range]{lang="EN-US"}]{#struct_0_x6265_25298_x1546656082}

[[解压过程中检测到报文流标识号]{style="font-family:宋体"}[xx]{lang="EN-US"}]{#struct_0_x6265_25298_x1109021461}[超出合法范围]{style="font-family:宋体"}

[[the decompression context is null]{lang="EN-US"}]{#struct_0_x6265_25298_x2143551436}

[[解压过程中检测到解压缩表项为空。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_x6265_25298_1735893284}[报文]{style="font-family:宋体"}

[[the decompression context is  invalid]{lang="EN-US"}]{#struct_0_x6265_25298_x2143354828}

[[解压过程中检测到解压缩表项无效。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}]{#struct_0_x6265_25298_1797734574}[报文]{style="font-family:宋体"}

[[the TCP checksum is error]{lang="EN-US"}]{#struct_0_x6265_25298_x821024080}

[[解压过程中检测到]{style="font-family:宋体"}[TCP Checksum]{lang="EN-US"}]{#struct_0_x6265_25298_x2143420364}[字段错误。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the generation number is mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_x1791310738}

[[解压缩过程中检测到]{style="font-family:宋体"}[Generation Number]{lang="EN-US"}]{#struct_0_x6265_25298_x743027531}[字段不匹配。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the time for receiving the packet is lawless]{lang="EN-US"}]{#struct_0_x6265_25298_x2143748044}

[[解压过程中检测到接收]{style="font-family:宋体"}[COMPRESSED_NON_TCP]{lang="EN-US"}]{#struct_0_x6265_25298_x1208248027}[报文的时间非法。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[the sequence number is mismatched]{lang="EN-US"}]{#struct_0_x6265_25298_x2143813580}

[[解压过程中检测到]{style="font-family:宋体"}[Sequence Number]{lang="EN-US"}]{#struct_0_x6265_25298_x926104169}[字段与解压表想中的不匹配。这时解压端会向压缩端发送一个]{style="font-family:宋体"}[CONTEXT_STATE]{lang="EN-US"}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6265_25298_274869859}

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x2143616972}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口连接，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，两端都开启]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能，并配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的帧中继]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩调试信息开关，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[接口执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[/**undo shutdown**]{lang="EN-US"}[，在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上可以看到如下调试信息：]{style="font-family:宋体"}

[[\<RouterA\> debugging fr compression iphc tcp]{lang="EN-US"}]{#struct_0_x6265_25298_x152981807}

[\<RouterB\> debugging fr compression iphc tcp]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_x6265_25298_271482451}

[[\*Mar 25 02:15:54:481 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_1782565286}

[[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}]{#struct_0_x6265_25298_x1534214691}

[[  Received an active event in Disable state.]{lang="EN-US"}]{#struct_0_x6265_25298_x1673826614}

[[  IPHC negotiation started.]{lang="EN-US"}]{#struct_0_x6265_25298_x811434881}

[[  Sent a config REQ (F = 1) packet, FSM state changed to I1.]{lang="EN-US"}]{#struct_0_x6265_25298_x1458658031}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x1193161902}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[ 100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[Disable]{lang="EN-US"}[状态收到激活事件，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[开始协商，发送]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[报文，进入]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 25 02:15:54:496 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2143682508}

[[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}]{#struct_0_x6265_25298_x961330734}

[[  Received a config REQ (F = \*) packet in I1 state.]{lang="EN-US"}]{#struct_0_x6265_25298_1257840870}

[[  Sent a config ACK packet, FSM state changed to I3.]{lang="EN-US"}]{#struct_0_x6265_25298_x1135795186}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_336403575}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[REQ (F = \*)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，进入]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 25 02:15:57:578 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2033479092}

[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}

[  Received a negotiation timer timeout (+) event in I3 state.]{lang="EN-US"}

[  Sent a config REQ (F = 0) packet, FSM state remains in I3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_526304793}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态收到协商定时器超时]{style="font-family:宋体"}[(+)]{lang="EN-US"}[事件，并发送]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，保持]{style="font-family:宋体"}[I3]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 25 02:15:57:580 2014 RouterA FR/7/IPHC: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2142961612}

[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}

[  Received a config ACK packet in I3 state.]{lang="EN-US"}

[  FSM state changed to Operational.]{lang="EN-US"}

[  IPHC negotiation done.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_988061618}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[I3]{lang="EN-US"}[阶段收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，进入]{style="font-family:宋体"}[Operational]{lang="EN-US"}[状态，协商完成]{style="font-family:宋体"}*

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_x6265_25298_1716026886}

[[\*Mar 25 02:15:54:495 2014 RouterB FR/7/IPHC: -MDC=1;]{lang="EN-US"}]{#struct_0_x6265_25298_553119314}

[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}

[  Received an active event in Disable state.]{lang="EN-US"}

[  IPHC negotiation started.]{lang="EN-US"}

[  Sent a config REQ (F = 1) packet, FSM state changed to I1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_1132558478}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[Disable]{lang="EN-US"}[状态收到激活事件，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[开始协商，发送]{style="font-family:宋体"}[REQ (F = 1)]{lang="EN-US"}[，进入]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 25 02:15:54:496 2014 RouterB FR/7/IPHC: -MDC=1;]{lang="EN-US"}]{#struct_0_x6265_25298_111262027}

[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}

[  Received a config ACK packet in I1 state.]{lang="EN-US"}

[  FSM state changed to I2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_1200030940}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商状态机在]{style="font-family:宋体"}[I1]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，进入]{style="font-family:宋体"}[I2]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 25 02:15:57:580 2014 RouterB FR/7/IPHC: -MDC=1;]{lang="EN-US"}]{#struct_0_x6265_25298_x2143027148}

[Received IPHC negotiation info on interface Serial2/1/0 DLCI 16:]{lang="EN-US"}

[  Received a config REQ (F = 0) packet in I2 state.]{lang="EN-US"}

[  Sent a config ACK packet, FSM state changed to Operational.]{lang="EN-US"}

[  IPHC negotiation done.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_497892272}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[状态机在]{style="font-family:宋体"}[I2]{lang="EN-US"}[状态收到]{style="font-family:宋体"}[REQ (F = 0)]{lang="EN-US"}[报文，并发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文，进入]{style="font-family:宋体"}[Operational]{lang="EN-US"}[状态，协商完成]{style="font-family:宋体"}*

[[\# Router A]{lang="EN-US"}]{#struct_0_x6265_25298_x334428173}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过串口连接，链路层协议配置为]{style="font-family:宋体"}[FR]{lang="EN-US"}[，两端都开启]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能，并配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。打开]{style="font-family:宋体"}[Router B]{lang="EN-US"}[的帧中继]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩调试信息开关。当]{style="font-family:宋体"}[Router A]{lang="EN-US"}[以]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[方式登录]{style="font-family:宋体"}[Router B]{lang="EN-US"}[时，]{style="font-family:宋体"}[Router B]{lang="EN-US"}[上]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩解压缩调试信息如下：]{style="font-family:宋体"}

[[\<RouterB\> debugging fr compression iphc tcp]{lang="EN-US"}]{#struct_0_x6265_25298_x945256592}

[\*Mar 14 05:51:29:849 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}

[Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x276671231}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[16]{lang="EN-US"}[接收到]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Mar 14 05:51:29:851 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x1780707805}

[ THC: received FULL_HEADER, connect ID 0, checksum 0xd572, seq 734446218]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_1879012499}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，接收到]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0xd572]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[734446218]{lang="EN-US"}*

[[\*Mar 14 05:51:29:852 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2143485899}

[Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 38.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_826455664}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[16]{lang="EN-US"}[接收到]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[38]{lang="EN-US"}*

[[\*Mar 14 05:51:29:853 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x1433458514}

[ THC: received COMPRESSED_TCP, connect ID 0, checksum 0x9623, seq 734446218]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_524941318}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，接收到]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x9623]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[734446218]{lang="EN-US"}*

[[\*Mar 14 05:51:29:854 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_159039155}

[ THC: sent FULL_HEADER, connect ID 0, checksum 0xd55a, seq 513970195]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_1639965751}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0xd55a]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[513970195]{lang="EN-US"}*

[[\*Mar 14 05:51:29:854 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x1234187025}

[Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.]{lang="EN-US"}

[*[ // ]{lang="EN-US"}*]{#struct_0_x6265_25298_1507501594}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路为]{style="font-family:宋体"}[16]{lang="EN-US"}[收到]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Mar 14 05:51:29:872 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2143551435}

[ THC: sent COMPRESSED_TCP, connect ID 0, checksum 0x820e, seq 513970195]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_2139177811}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，发送]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0x820e]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[513970195]{lang="EN-US"}*

[[\*Mar 14 05:51:29:872 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_78752359}

[Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 41.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_867467859}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚链路]{style="font-family:宋体"}[16]{lang="EN-US"}[，发送]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度]{style="font-family:宋体"}[41]{lang="EN-US"}*

[[\*Mar 14 05:51:29:873 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x1516983924}

[Received an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 36.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x6265_25298_x632385209}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚链路]{style="font-family:宋体"}[16]{lang="EN-US"}[收到]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[[\*Mar 14 05:51:29:874 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x85615798}

[ THC: received COMPRESSED_TCP, connect ID 0, checksum 0xb78f, seq 734446200]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_376291777}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，接收到]{style="font-family:宋体"}[COMPRESSED_TCP]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0xb78f]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[734446200]{lang="EN-US"}*

[[\*Mar 14 05:51:29:874 2014 RouterB IPHC/7/EVENT: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x2143354827}

[ THC ERROR: Delta th_win code error, connect ID 0]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_x1381487475}*[报文压缩错误信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，在压缩]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文过程中]{style="font-family:宋体"}[Delta Window]{lang="EN-US"}[字段编码错误]{style="font-family:宋体"}*

[[\*Mar 14 05:51:29:875 2014 RouterB IPHC/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x1753942436}

[ THC: sent FULL_HEADER, connect ID 0, checksum 0xd4fa, seq 513970159]{lang="EN-US"}

[*[// TCP]{lang="EN-US"}*]{#struct_0_x6265_25298_x838148804}*[报文压缩信息：报文流]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，发送]{style="font-family:宋体"}[FULL_HEADER]{lang="EN-US"}[报文，校验和为]{style="font-family:宋体"}[0xd4fa]{lang="EN-US"}[，序列号为]{style="font-family:宋体"}[513970159]{lang="EN-US"}*

[[\*Mar 14 05:51:29:875 2014 RouterB FR/7/PACKET: -MDC=1-Slot=2;]{lang="EN-US"}]{#struct_0_x6265_25298_x43153688}

[Sent an IPHC packet on interface Serial2/1/0 DLCI 16, packet length is 56.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x6265_25298_x1722746554}*[串口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[，虚电路]{style="font-family:宋体"}[16]{lang="EN-US"}[发送]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[报文，报文长度为]{style="font-family:宋体"}[56]{lang="EN-US"}*

[ ]{lang="EN-US"}
