::: {#729839134 .myid}
[]{#_Toc404792425}[]{#struct_0_19508_69870_x1617554155}[]{#_Toc233198545}

**802.1X \-- 802.1X调试命令 \-- debugging dot1x**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_19508_69870_x460075737}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_19508_69870_275736424}

[**[debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_19508_69870_x1580841604}

[**[undo debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_19508_69870_x368389796}

[[分布式设备：]{style="font-family:宋体"}]{#struct_0_19508_69870_x1091112785}

[**[debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_19508_69870_1561030389}

[**[undo debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_19508_69870_1233408963}

[[分布式]{style="font-family:宋体"}]{#struct_0_19508_69870_x2126464659}[IRF]{lang="SV"}[设备：]{style="font-family:宋体"}

[**[debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ ]{lang="EN-US"}]{#struct_0_19508_69870_x1664121045}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[**[undo debugging dot1x]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** } \[ ]{lang="EN-US"}]{#struct_0_19508_69870_x1617488619}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19508_69870_1655225147}

[[用户视图]{style="font-family:宋体"}]{#struct_0_19508_69870_x2009080241}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19508_69870_123103795}

[[network-admin]{lang="EN-US"}]{#struct_0_19508_69870_1951053645}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19508_69870_1279641412}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19508_69870_x1547845591}

[**[all]{lang="EN-US"}**]{#struct_0_19508_69870_1347492201}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_19508_69870_x1442031076}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_19508_69870_x1617423083}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_19508_69870_x154382487}[：表示报文调试信息开关。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_19508_69870_104401146}[：表示指定单板的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_19508_69870_x1376929673}[：表示指定成员设备的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_19508_69870_1890144340}[：表示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_19508_69870_1705434344}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示成员设备上指定单板的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_19508_69870_x506385666}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示指定单板的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_19508_69870_494990797}

[]{#OLE_LINK1}[**[debugging dot1x]{lang="EN-US"}**]{#struct_0_19508_69870_x204675456}[命令用来打开]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging dot1x]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_19508_69870_1365588142}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_19508_69870_1157541453}[[表1-1 ]{lang="EN-US"}[debugging dot1x error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_99100285}[[字段]{style="font-family:黑体"}]{#struct_0_19508_69870_x1617357547}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19508_69870_582399577}

[[Failed to set unknown source MAC action on *interface-type interface-num.*]{lang="EN-US"}]{#struct_0_19508_69870_x810957825}

[[在接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_19508_69870_x1843443813}[上设置未知源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址动作失败]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving authenticate response.]{lang="EN-US"}]{#struct_0_19508_69870_x652993015}

[[收到认证回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_419271963}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving authorization response.]{lang="EN-US"}]{#struct_0_19508_69870_x1618340587}

[[收到授权回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_x653477149}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving accounting response.]{lang="EN-US"}]{#struct_0_19508_69870_861913679}

[[收到计费回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_960890891}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to set enable protocol packet to CPU.]{lang="EN-US"}]{#struct_0_19508_69870_353888177}

[[设置使能协议报文上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_19508_69870_x175335792}[失败]{style="font-family:宋体"}

[[Failed to open packet socket.]{lang="EN-US"}]{#struct_0_19508_69870_x1618275051}

[[打开报文]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_19508_69870_1380322065}[失败]{style="font-family:宋体"}

[[Failed to set LogicState on *if_name*,*error_code*]{lang="EN-US"}]{#struct_0_19508_69870_488935005}

[[在]{style="font-family:宋体"}]{#struct_0_19508_69870_391340619}[接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[上]{style="font-family:
  宋体"}[设置接口逻辑状态失败，错误码为]{style="font-family:宋体"}*[error_code]{lang="EN-US"}*

[[Failed to allocate memory for EAP challenge request.]{lang="EN-US"}]{#struct_0_19508_69870_923264596}

[[为]{style="font-family:宋体"}[EAP challenge]{lang="EN-US"}]{#struct_0_19508_69870_x1617816298}[请求分配内存失败]{style="font-family:宋体"}

[[Invalid password length.]{lang="EN-US"}]{#struct_0_19508_69870_144594109}

[[密码长度无效]{style="font-family:宋体"}]{#struct_0_19508_69870_x1636583597}

[[Failed to allocate memory for EAP Identifier request.]{lang="EN-US"}]{#struct_0_19508_69870_2033188797}

[[为]{style="font-family:宋体"}[EAP Identity]{lang="EN-US"}]{#struct_0_19508_69870_x89346792}[请求分配内存失败]{style="font-family:宋体"}

[[PAE entering Abort for BE process failed.]{lang="EN-US"}]{#struct_0_19508_69870_x1617750762}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_x588091564}[进程失败，]{style="font-family:宋体"}[PAE]{lang="EN-US"}[异常退出]{style="font-family:宋体"}

[[Failed to process message for the message type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_x1393968994}

[[消息类型无效，处理失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x764619990}

[[Failed to accept connection on the global known port.]{lang="EN-US"}]{#struct_0_19508_69870_1680732497}

[[在全局知名端口接收连接失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x1617685226}

[[Failed to process the Set request message for the data type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_498431032}

[[处理]{style="font-family:宋体"}[Set]{lang="EN-US"}]{#struct_0_19508_69870_492331598}[请求消息失败，数据类型无效]{style="font-family:宋体"}

[[Failed to process the Get request message for the data type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_1340915957}

[[处理]{style="font-family:宋体"}[Get]{lang="EN-US"}]{#struct_0_19508_69870_x256842525}[请求消息失败，数据类型无效]{style="font-family:宋体"}

[[Failed to process the Getnext request message for the data type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_x1617619690}

[[处理]{style="font-family:宋体"}[Getnext]{lang="EN-US"}]{#struct_0_19508_69870_1449982353}[请求消息失败，数据类型无效]{style="font-family:宋体"}

[[Failed to process the Getbulk request message for the data type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_1941920126}

[[处理]{style="font-family:宋体"}[Getbulk]{lang="EN-US"}]{#struct_0_19508_69870_1920090797}[请求消息失败，数据类型无效]{style="font-family:宋体"}

[[Failed to process the request message for the operation type is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_x1617554154}

[[处理请求消息失败，操作类型无效]{style="font-family:宋体"}]{#struct_0_19508_69870_1106008204}

[[Failed to connect to master.]{lang="EN-US"}]{#struct_0_19508_69870_786942146}

[[连接到主控板失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x1043485193}

[[Failed to add socket to LPU connection table.]{lang="EN-US"}]{#struct_0_19508_69870_x1617488618}

[[将]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_19508_69870_89141206}[加入长连接链表失败]{style="font-family:宋体"}

[[The data type of Pull message is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_1282930224}

[[Pull]{lang="EN-US"}]{#struct_0_19508_69870_x1776781751}[消息数据类型无效]{style="font-family:宋体"}

[[The interface is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_x1617423082}

[[接口无效]{style="font-family:宋体"}]{#struct_0_19508_69870_x1720466428}

[[Failed to get interface link status.]{lang="EN-US"}]{#struct_0_19508_69870_1809539394}

[[获取接口连接状态失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x1617357546}

[[The identifier is unmatched.]{lang="EN-US"}]{#struct_0_19508_69870_x2146483778}

[[认证报文不匹配]{style="font-family:宋体"}]{#struct_0_19508_69870_x1099742607}

[[Dropped received EAP packet for the packet length is invalid.]{lang="EN-US"}]{#struct_0_19508_69870_x1359870491}

[[丢弃接收到的]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_19508_69870_x1618340586}[报文，报文长度无效]{style="font-family:宋体"}

[[Dropped received EAP packet for the packet is empty.]{lang="EN-US"}]{#struct_0_19508_69870_2075406206}

[[丢弃接收到的]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_19508_69870_807003308}[报文，报文内容为空]{style="font-family:宋体"}

[[Failed to get statistics.]{lang="EN-US"}]{#struct_0_19508_69870_x1618275050}

[[获取统计信息失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x1348561290}

[[Invalid protocol version ID.]{lang="EN-US"}]{#struct_0_19508_69870_x399202700}

[[无效的协议版本]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19508_69870_1261845581}

[[There is no EAP request  from authentication server.]{lang="EN-US"}]{#struct_0_19508_69870_x1617816301}

[[没有来自于认证服务器的]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_19508_69870_x1065849295}[请求]{style="font-family:宋体"}

[[Failed to create a user timer.]{lang="EN-US"}]{#struct_0_19508_69870_x1617750765}

[[创建用户定时器失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x991376091}

[[User Failed to start acct-update period timer when receiving acct-start response terminate user session]{lang="EN-US"}]{#struct_0_19508_69870_1249971971}

[[当用户正在接收计费开始回应结束用户会话时，用户不能启动计费更新周期定时器]{style="font-family:宋体"}]{#struct_0_19508_69870_x1449085107}

[[Invalid server string length *length.*]{lang="EN-US"}]{#struct_0_19508_69870_654488127}

[[服务器下发的]{style="font-family:宋体"}[String]{lang="EN-US"}]{#struct_0_19508_69870_654029374}[属性信息长度非法，为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Dropped received logoff packet for VLAN is not match, packet VLAN is *vlan-id*, user VLAN is *vlan-id*.]{lang="EN-US"}]{#struct_0_19508_69870_1129754999}

[[丢弃]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_19508_69870_653963838}[不匹配的]{style="font-family:宋体"}[logoff]{lang="EN-US"}[报文，报文所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，用户所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Failed to allocate memory for EAP Notification request.]{lang="EN-US"}]{#struct_0_19508_69870_565287743}

[[为]{style="font-family:宋体"}[EAP Notification]{lang="EN-US"}]{#struct_0_19508_69870_1653400170}[请求报文分配内存失败]{style="font-family:宋体"}

[[Failed to check smarton packet because of invalid prefix.]{lang="EN-US"}]{#struct_0_19508_69870_653898302}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_x204182315}[报文失败，原因是前缀不合法]{style="font-family:宋体"}

[[Failed to check smarton packet because of unmatched MD5 digest.]{lang="EN-US"}]{#struct_0_19508_69870_623773610}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_653832766}[报文失败，原因是]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要不匹配]{style="font-family:宋体"}

[[Failed to check smarton packet because of no switch ID information.]{lang="EN-US"}]{#struct_0_19508_69870_639801639}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_x1114495897}[报文失败，原因是报文中未携带设备]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Failed to check smarton packet because of unmatched switch ID length.]{lang="EN-US"}]{#struct_0_19508_69870_653767230}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_17751973}[报文失败，原因是设备]{style="font-family:宋体"}[ID]{lang="EN-US"}[长度不匹配]{style="font-family:宋体"}

[[Failed to check smarton packet because of unmatched switch ID.]{lang="EN-US"}]{#struct_0_19508_69870_x387027886}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_653701694}[报文失败，原因是设备]{style="font-family:宋体"}[ID]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Failed to check smarton packet because of no ID or Password information.]{lang="EN-US"}]{#struct_0_19508_69870_x409137565}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_2136297130}[报文失败，原因是报文中未携带设备]{style="font-family:宋体"}[ID]{lang="EN-US"}[或密码]{style="font-family:宋体"}

[[Failed to check smarton packet bacause of invalid MD5 digest length.]{lang="EN-US"}]{#struct_0_19508_69870_653636158}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_1168540255}[报文失败，原因是]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要长度不匹配]{style="font-family:宋体"}

[[Failed to check hash information.]{lang="EN-US"}]{#struct_0_19508_69870_x591965402}

[[检查]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_19508_69870_653570622}[信息失败]{style="font-family:宋体"}

[[Failed to check smarton packet because of no device switch-ID or MD5 digest.]{lang="EN-US"}]{#struct_0_19508_69870_516885850}

[[检查]{style="font-family:宋体"}[smarton]{lang="EN-US"}]{#struct_0_19508_69870_1003003016}[报文失败，原因是设备上未配置]{style="font-family:宋体"}[Swich ID]{lang="EN-US"}[或未生成]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_19508_69870_x1617685229}[[表1-2 ]{lang="EN-US"}[debugging dot1x event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_91588925}[[字段]{style="font-family:黑体"}]{#struct_0_19508_69870_1257945919}

[[描述]{style="font-family:黑体"}]{#struct_0_19508_69870_61463780}

[[Got accounting-stop response by *mac* and *interface-type interface-num*[, ]{style="color:black"}RespCode=*RespCode.*]{lang="EN-US"}]{#struct_0_19508_69870_x359540727}

[[通过]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_x685641112}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[获取停止计费信息，响应码为]{style="font-family:宋体"}*[RespCode ]{lang="EN-US"}*

[*[Interface-type interface-num]{lang="EN-US"}*[ is redundant.]{lang="EN-US"}]{#struct_0_19508_69870_x995837497}

[[接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_19508_69870_x171992245}[多余]{style="font-family:宋体"}

[[Received EAP Request packet.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1617619693}

[[接收到]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_1046697826}[请求消息的报文]{style="font-family:宋体;color:black"}

[[Received EAP Success packet.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_1679883403}

[[接收到]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x685528935}[成功消息的报文]{style="font-family:宋体;color:black"}

[[Received EAP Failure packet.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1320116237}

[[接收到]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_550282122}[失败消息的报文]{style="font-family:宋体;color:black"}

[[Received EAP packet of unknown type.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1617554157}

[[接收未知类型的报文]{style="font-family:宋体;color:black"}]{#struct_0_19508_69870_702723677}

[[Sending EAP Packet (identifier *identifier*, type *type*)]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_400765159}

[[正在发送]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_657818689}[报文（匹配标识为]{style="font-family:宋体;color:black"}*[identifier]{lang="EN-US" style="color:black"}*[，]{style="font-family:
  宋体;color:black"}[ ]{style="color:black"}[类型为]{style="font-family:宋体;color:black"}*[type]{lang="EN-US" style="color:black"}*[）]{style="font-family:宋体;color:black"}

[[Processing If_Delete event:]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_1520030411}

[[正在处理删除接口事件]{style="font-family:宋体"}]{#struct_0_19508_69870_x2089798688}

[[Processing If_Deactive event:]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1617488621}

[[正在处理接口去激活事件]{style="font-family:宋体"}]{#struct_0_19508_69870_1298798179}

[[Processing If_Active event:]{lang="EN-US"}]{#struct_0_19508_69870_x2054835333}

[[正在处理接口激活事件]{style="font-family:宋体"}]{#struct_0_19508_69870_x277961073}

[[Processing If_Down event:]{lang="EN-US"}]{#struct_0_19508_69870_x1377268156}

[[正在处理接口]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_19508_69870_x1617423085}[事件]{style="font-family:宋体"}

[[Processing If_Up event:]{lang="EN-US"}]{#struct_0_19508_69870_654488126}

[[正在处理接口]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_19508_69870_654029373}[事件]{style="font-family:宋体"}

[[Multicasted Identity Request packets on interface *interface-type interface-num* of VLAN vlan-id.]{lang="EN-US"}]{#struct_0_19508_69870_652186567}

[[在]{style="font-family:宋体"}]{#struct_0_19508_69870_x508249710}[处于]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[中的接]{style="font-family:宋体"}[口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[上组播]{style="font-family:宋体"}[发送]{style="font-family:宋体"}[EAP Identity]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Multicasted Identity Request packets on interface *interface-type interface-num.*]{lang="EN-US"}]{#struct_0_19508_69870_351144499}

[[在接]{style="font-family:宋体"}]{#struct_0_19508_69870_x489631861}[口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[上组播]{style="font-family:
  宋体"}[发送]{style="font-family:宋体"}[EAP Identity]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[PORT_SM\[*interface-type interface-num*\] entering init state\...]{lang="EN-US"}]{#struct_0_19508_69870_x1617357549}

[[端口状态机进入初始状态]{style="font-family:宋体"}]{#struct_0_19508_69870_1745198991}

[[PORT_SM\[*interface-type interface-num*\] entering author-force state\...]{lang="EN-US"}]{#struct_0_19508_69870_365553797}

[[端口状态机进入强制授权状态]{style="font-family:宋体"}]{#struct_0_19508_69870_x406786889}

[[PORT_SM\[*interface-type interface-num*\] entering unauthor-force state\....]{lang="EN-US"}]{#struct_0_19508_69870_x418325821}

[[端口状态机进入非强制授权状态]{style="font-family:宋体"}]{#struct_0_19508_69870_x1618340589}

[[PORT_SM\[*interface-type interface-num*\] entering disconnected state\....]{lang="EN-US"}]{#struct_0_19508_69870_x1816276563}

[[端口状态机进入断开连接状态]{style="font-family:宋体"}]{#struct_0_19508_69870_1851578658}

[[PORT_SM\[*interface-type interface-num*\] entering disconnected state\....]{lang="EN-US"}]{#struct_0_19508_69870_1442171203}

[[端口状态机进入断开连接状态]{style="font-family:宋体"}]{#struct_0_19508_69870_x1618275053}

[[PORT_SM\[*interface-type interface-num*\] entering authenticating state\....]{lang="EN-US"}]{#struct_0_19508_69870_217522651}

[[端口状态机进入正在认证状态]{style="font-family:宋体"}]{#struct_0_19508_69870_x1358044185}

[[PORT_SM\[*interface-type interface-num*\] entering authored state\....]{lang="EN-US"}]{#struct_0_19508_69870_1567278095}

[[端口状态机进入已经授权的状态]{style="font-family:宋体"}]{#struct_0_19508_69870_x649744594}

[[PORT_SM\[*interface-type interface-num*\] received *event* event *t*]{lang="EN-US"}]{#struct_0_19508_69870_x1617816300}

[[端口状态机接收事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_19508_69870_500234646}

[[Global switch or interface switch is off.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_108657733}

[[未打开全局或接口开关]{style="font-family:宋体;color:black"}]{#struct_0_19508_69870_820892831}

[[Processing HA UPGRADE event.]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1617750764}

[[正在处理]{style="font-family:宋体;color:black"}[HA]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_574707850}[升级事件]{style="font-family:宋体;color:black"}

[[Processing HA DEGRADE event .]{lang="SV" style="color:black"}]{#struct_0_19508_69870_1368840105}

[[正在处理]{style="font-family:宋体;color:black"}[HA]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1617685228}[降级事件]{style="font-family:宋体;color:black"}

[[Failed to find the specified unauthor user.]{lang="SV" style="color:black"}]{#struct_0_19508_69870_x308138022}

[[查找指定非授权用户失败]{style="font-family:宋体;color:black"}]{#struct_0_19508_69870_849122741}

[[Reconnect timer timeout, reconnecting to mpu ]{lang="EN-US"}]{#struct_0_19508_69870_x1617619692}

[[重连定时器超时，向]{style="font-family:宋体"}[mpu]{lang="EN-US"}]{#struct_0_19508_69870_x1682185529}[重新发起连接]{style="font-family:宋体"}

[[Successfully connected to master, closed reconnect timer.]{lang="EN-US"}]{#struct_0_19508_69870_x112018829}

[[成功连接到主控板，关闭重连接定时器]{style="font-family:宋体"}]{#struct_0_19508_69870_x363563373}

[[Processing the event of IFEVENT.]{lang="EN-US"}]{#struct_0_19508_69870_x1617554156}

[[正在处理接口事件]{style="font-family:宋体"}]{#struct_0_19508_69870_x2026159678}

[[Create reconnect timer successfully]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x1638905690}

[[成功创建重连接定时器]{style="font-family:宋体"}]{#struct_0_19508_69870_x1617488620}

[[Failed to create reconnect timer]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x267285762}

[[创建重连接定时器失败]{style="font-family:宋体"}]{#struct_0_19508_69870_1603823523}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed authentication request and returned Processing.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x1617423084}

[[对于用户（]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_x913897374}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[，所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[，接入端口为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[），]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求并返回正在处理的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed ]{style="color:black"}authorization [request and returned Processing.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_2123450297}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x1617357548}[处理授权请求并返回正在处理的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed ]{style="color:black"}accounting [request and returned Processing.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x983684364}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x1326573670}[处理计费请求并返回正在处理的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed authentication request and returned Success.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x1618340588}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_912606792}[处理认证请求并返回成功的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed ]{style="color:black"}authorization [request and returned Success.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_2133712079}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x1618275052}[处理授权请求并返回成功的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed ]{style="color:black"}accounting [request and returned Success.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_1783606592}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_2011521134}[处理计费请求并返回成功的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed authentication request and returned Failure code *code*.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x2006457126}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x641149263}[处理认证请求并返回失败的结果，错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed authentication request and returned Continuing.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_653570620}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_516885848}[处理认证请求并返回继续认证的结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] [AAA processed ]{style="color:black"}authorization [request and returned Failure.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x1573115333}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x2006522662}[处理授权请求并返回失败的结果]{style="font-family:宋体"}

[[\[*mac*:VLANvlan: *interface-type interface-num*\] [AAA processed ]{style="color:black"}accounting-update [request and returned Failure.]{style="color:black"}]{lang="EN-US"}]{#struct_0_19508_69870_x937712213}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x1163211795}[处理计费更新请求并返回失败的结果]{style="font-family:宋体"}

[[Succeeding in notifying port-mode to 8021x thread.]{lang="EN-US"}]{#struct_0_19508_69870_x2006588198}

[[端口模式下设置]{style="font-family:宋体;color:black"}[802.1X]{lang="EN-US" style="color:black"}]{#struct_0_19508_69870_x738444844}[线程成功]{style="font-family:宋体;color:black"}

[[BE is in Idle state]{lang="EN-US"}]{#struct_0_19508_69870_434966570}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_x2006653734}[进入闲置状态]{style="font-family:宋体"}

[[BE is in Initialize state]{lang="EN-US"}]{#struct_0_19508_69870_x9912343}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_x2006194982}[进入初始化状态]{style="font-family:宋体"}

[[BE is in request state]{lang="EN-US"}]{#struct_0_19508_69870_635642937}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_985544524}[进入请求状态]{style="font-family:宋体"}

[[BE is in Response state]{lang="EN-US"}]{#struct_0_19508_69870_x2006260518}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_x235777114}[进入回应状态]{style="font-family:宋体"}

[[BE is in Fail state]{lang="EN-US"}]{#struct_0_19508_69870_x288455450}

[[BE]{lang="EN-US"}]{#struct_0_19508_69870_x2006326054}[进入失败状态]{style="font-family:宋体"}

[[User sent authentication request]{lang="EN-US"}]{#struct_0_19508_69870_x1195548341}

[[用户发出认证请求]{style="font-family:宋体"}]{#struct_0_19508_69870_x2006391590}

[[User sent authorization request]{lang="EN-US"}]{#struct_0_19508_69870_1133383019}

[[用户发出授权请求]{style="font-family:宋体"}]{#struct_0_19508_69870_x264599078}

[[User sent accounting-start request]{lang="EN-US"}]{#struct_0_19508_69870_x2005932838}

[[用户发出开始计费请求]{style="font-family:宋体"}]{#struct_0_19508_69870_x1013292519}

[[User sent accounting-stop request]{lang="EN-US"}]{#struct_0_19508_69870_x2005998374}

[[用户发出停止计费请求]{style="font-family:宋体"}]{#struct_0_19508_69870_x8176998}

[[User sent accounting-update request]{lang="EN-US"}]{#struct_0_19508_69870_x2006457125}

[[用户发出更新计费请求]{style="font-family:宋体"}]{#struct_0_19508_69870_x1044433790}

[[Server timed out]{lang="EN-US"}]{#struct_0_19508_69870_x1065501347}

[[服务器超时]{style="font-family:宋体"}]{#struct_0_19508_69870_x2006522661}

[[PAE is in Initialize state]{lang="EN-US"}]{#struct_0_19508_69870_1791171142}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006588197}[处于初始化状态]{style="font-family:宋体"}

[[PAE is in Disconnect state]{lang="EN-US"}]{#struct_0_19508_69870_21070043}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006653733}[处于断开连接状态]{style="font-family:宋体"}

[[PAE is in Connecting state]{lang="EN-US"}]{#struct_0_19508_69870_x769427230}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006194981}[处于连接状态]{style="font-family:宋体"}

[[PAE is in Authenticating state]{lang="EN-US"}]{#struct_0_19508_69870_232358410}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006260517}[进入正在认证状态]{style="font-family:宋体"}

[[PAE is in Authenticated state]{lang="EN-US"}]{#struct_0_19508_69870_1780645521}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006326053}[进入认证状态]{style="font-family:宋体"}

[[PAE is in Aborting state]{lang="EN-US"}]{#struct_0_19508_69870_1177104654}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2006391589}[进入丢弃状态]{style="font-family:宋体"}

[[PAE is in Held state]{lang="EN-US"}]{#struct_0_19508_69870_x788996818}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2005932837}[进入]{style="font-family:宋体"}[Held]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[PAE is in Restart state]{lang="EN-US"}]{#struct_0_19508_69870_196561062}

[[PAE]{lang="EN-US"}]{#struct_0_19508_69870_x2005998373}[进入重启状态]{style="font-family:宋体"}

[[Failed to create server timeout timer]{lang="EN-US"}]{#struct_0_19508_69870_x411461525}

[[创建服务器超时定时器失败]{style="font-family:宋体"}]{#struct_0_19508_69870_x275685884}

[[Create server timeout timer successfully]{lang="EN-US"}]{#struct_0_19508_69870_x2006457128}

[[创建服务器超时定时器成功]{style="font-family:宋体"}]{#struct_0_19508_69870_2134788259}

[[Processing new mac event]{lang="EN-US"}]{#struct_0_19508_69870_x2006522664}

[[处理新]{style="font-family:宋体"}[mac]{lang="EN-US"}]{#struct_0_19508_69870_x1744281267}[事件]{style="font-family:宋体"}

[[Notified Portsec of new mac result:]{lang="EN-US"}]{#struct_0_19508_69870_x2006588200}

[[通知端口安全新]{style="font-family:宋体"}[mac]{lang="EN-US"}]{#struct_0_19508_69870_x382804309}[的结果]{style="font-family:宋体"}

[[Processing the event of unauthor]{lang="EN-US"}]{#struct_0_19508_69870_x2006653736}

[[处理]{style="font-family:宋体"}[unauthor]{lang="EN-US"}]{#struct_0_19508_69870_x1172711757}[事件]{style="font-family:宋体"}

[[Processing the event of IfVlanDel]{lang="EN-US"}]{#struct_0_19508_69870_x2006194984}

[[处理]{style="font-family:宋体"}[ifvlanDel]{lang="EN-US"}]{#struct_0_19508_69870_x2006260520}[事件]{style="font-family:宋体"}

[[Processing the event of AuthenFail]{lang="EN-US"}]{#struct_0_19508_69870_x592073010}

[[处理认证失败事件]{style="font-family:宋体"}]{#struct_0_19508_69870_x2006326056}

[[Notified PortSec of AuthenFail result:]{lang="EN-US"}]{#struct_0_19508_69870_1936619541}

[[通知端口安全认证失败结果]{style="font-family:宋体"}]{#struct_0_19508_69870_x2006391592}

[[The maximum number of accounting attempts has been reached]{lang="EN-US"}]{#struct_0_19508_69870_x29416395}

[[达到最大计费尝试次数]{style="font-family:宋体"}]{#struct_0_19508_69870_x2005932840}

[[AAA processed accounting-update request and returned processing]{lang="EN-US"}]{#struct_0_19508_69870_x1369195199}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x2005998376}[处理计费更新请求并返回正在处理]{style="font-family:宋体"}

[[AAA processed accounting-update request and returned success]{lang="EN-US"}]{#struct_0_19508_69870_x1170976412}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x2006457127}[处理计费更新请求并返回成功]{style="font-family:宋体"}

[[AAA processed accounting-update request and returned fail]{lang="EN-US"}]{#struct_0_19508_69870_2087734092}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x2006522663}[处理计费更新请求并返回失败]{style="font-family:宋体"}

[[User received authentication response]{lang="EN-US"}]{#struct_0_19508_69870_628371728}

[[用户收到认证回应]{style="font-family:宋体"}]{#struct_0_19508_69870_x2006588199}

[[AAA processed authorization request and returned processing]{lang="EN-US"}]{#struct_0_19508_69870_x2006653735}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x1575996284}[处理授权请求并返回正在处理]{style="font-family:宋体"}

[[AAA processed authorization request and returned sucess]{lang="EN-US"}]{#struct_0_19508_69870_x2006194983}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_x930441004}[处理授权请求并返回成功]{style="font-family:宋体"}

[[AAA processed authorization request and returned fail]{lang="EN-US"}]{#struct_0_19508_69870_x2006260519}

[[AAA]{lang="EN-US"}]{#struct_0_19508_69870_1330306827}[处理授权请求并返回失败]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Delete User from critical vlan *c-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_653570618}

[[用户（]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_654553658}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[，所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[，接入端口为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[）退出]{style="font-family:宋体"}[Critical VLAN *c-vlan*]{lang="EN-US"}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Succeeded to add User to critical vlan *c-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_654488122}

[[用户成功加入]{style="font-family:宋体"}[Critical VLAN *c-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2074853980}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Failed to add User to critical *c-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_1491755484}

[[用户加入]{style="font-family:宋体"}[Critical VLAN *c-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2074919516}[失败]{style="font-family:宋体"}

[[Receive Unknown IP type.]{lang="EN-US"}]{#struct_0_19508_69870_x2074985052}

[[收到不能识别的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19508_69870_x2075050588}[类型]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Delete User from auth-fail vlan *a-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_x2075116124}

[[用户退出]{style="font-family:宋体"}[Auth-Fail VLAN *a-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2075181660}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num* \] Succeeded to add User to auth-fail vlan *a-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_x2075247196}

[[用户成功加入]{style="font-family:宋体"}[Auth-Fail VLAN *a-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2075312732}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Failed to add User to auth-fail vlan *a-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_778983575}

[[用户加入]{style="font-family:宋体"}[Auth-Fail VLAN *a-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2074329692}[失败]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Delete User from guest vlan *a-vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_x2074395228}

[[用户退出]{style="font-family:宋体"}[Guest VLAN *a-vlan*]{lang="EN-US"}]{#struct_0_19508_69870_x2074853981}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Succeeded to add User to guest vlan *vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_x2074919517}

[[用户成功加入]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_19508_69870_x2074985053}

[[\[*mac*:VLAN*vlan*: *interface-type interface-num*\] Failed to add User to guest vlan *vlan*.]{lang="EN-US"}]{#struct_0_19508_69870_x2075050589}

[[用户加入]{style="font-family:宋体"}[Guest VLAN]{lang="EN-US"}]{#struct_0_19508_69870_x2075116125}[失败]{style="font-family:宋体"}

[[Succeed to get hash information from server.]{lang="EN-US"}]{#struct_0_19508_69870_x2075181661}

[[成功从服务器获取]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_19508_69870_694404996}[信息]{style="font-family:宋体"}

[[Succeeded to send smarton notification-request packet.]{lang="EN-US"}]{#struct_0_19508_69870_x2075247197}

[[成功发送]{style="font-family:宋体"}[SmartOn notification-request]{lang="EN-US"}]{#struct_0_19508_69870_x2075312733}[报文]{style="font-family:宋体"}

[[Succeeded to check smarton notification-response.]{lang="EN-US"}]{#struct_0_19508_69870_x2074329693}

[[成功检查]{style="font-family:宋体"}[SmartOn notification-response]{lang="EN-US"}]{#struct_0_19508_69870_x2074395229}[报文]{style="font-family:宋体"}

[[\[*interface-type interface-num*\]EAP-REQ/ID Multicast timed out.]{lang="EN-US"}]{#struct_0_19508_69870_x2074853982}

[[组播发送]{style="font-family:宋体"}[EAP-REQ/ID]{lang="EN-US"}]{#struct_0_19508_69870_x2074919518}[报文超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging dot1x packet]{lang="EN-US"}]{#struct_0_19508_69870_1726950410}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_108154237}[[字段]{style="font-family:黑体"}]{#struct_0_19508_69870_x2006326055}

[[描述]{style="font-family:黑体"}]{#struct_0_19508_69870_370535600}

[[Received a packet on interface *interface-type interface-num*]{lang="EN-US"}]{#struct_0_19508_69870_1284965436}

[[\-\--Verbose information of the packet\-\--]{lang="EN-US"}]{#struct_0_19508_69870_x373899951}

[[Destination Mac Address: *dst-mac*]{lang="EN-US"}]{#struct_0_19508_69870_x2068977269}

[[Source Mac Address: *src-mac*]{lang="EN-US"}]{#struct_0_19508_69870_1540176114}

[[Mac Frame Type: *fram-type*]{lang="EN-US"}]{#struct_0_19508_69870_1546749971}

[[Protocol Version ID: *version-id*]{lang="EN-US"}]{#struct_0_19508_69870_x2006391591}

[[Packet Type: *type-num*]{lang="EN-US"}]{#struct_0_19508_69870_x432700922}

[[Packet Length: *length*]{lang="EN-US"}]{#struct_0_19508_69870_1267655352}

[[接收来自接口]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_19508_69870_x1920099700}[的报文，包括如下信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_1969469020}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_x847961331}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_19508_69870_969639501}[帧类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协议版本号]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19508_69870_x2005932839}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文类型]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19508_69870_1715590836}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文长度]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19508_69870_x78183294}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19508_69870_1409309747}

[[\# ]{lang="EN-US"}]{#struct_0_19508_69870_1718173052}[在一台启动了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[功能的设备上，打开]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[所有调试功能。当有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户上线时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging dot1x all]{lang="EN-US"}]{#struct_0_19508_69870_x2005998375}

[\*Jan  1 02:44:12:154 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}

[Received a packet on interface GE1/0/1/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 0180-c200-0003]{lang="EN-US"}

[Source Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 1]{lang="EN-US"}

[Packet Length: 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1574260939}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0]{lang="EN-US"}[接收了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:156 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_297089431}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] PAE is in Disconnect state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_202439147}*[进入断开连接状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:157 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x1111909548}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Initialize state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_1340361600}*[进入初始状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:158 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2006457130}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] PAE is in Restart state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_x1804014213}*[进入重启状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:159 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1394444765}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Idle state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_x39114093}*[进入]{style="font-family:宋体"}[Idle]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:160 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x118282847}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] PAE is in Connecting state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_x1995380543}*[进入连接状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:161 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x131829431}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] PAE is in Authenticating state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_x2082532523}*[进入认证状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:162 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2006522666}

[PORT_SM\[GE1/0/1\] received event DOT1X_PSM_E_START_AUTH.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1387886615}*[接口接收到]{style="font-family:宋体"}[DOT1X_PSM_E_START_AUTH]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:163 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x1052549217}

[PORT_SM\[GE1/0/1\] entering authenticating state\...]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1129017273}*[接口进入认证状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:166 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1505901297}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Request state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_x905210012}*[进入请求状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:166 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1061941439}

[Sending EAP Packet (identifier 1, type 1)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1347602239}*[正在发送]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}[报文（匹配标识为]{style="font-family:宋体;
color:black"}[1]{lang="EN-US" style="color:black"}[，类型为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[）]{style="font-family:宋体;color:black"}*

[[\*Jan  1 02:44:12:170 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}]{#struct_0_19508_69870_x2006588202}

[Transmitted a packet on interface GE1/0/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Source Mac Address: 00e0-fc00-5830]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 0]{lang="EN-US"}

[Packet Length: 5]{lang="EN-US"}

[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}

[Code: 1]{lang="EN-US"}

[Identifier: 1]{lang="EN-US"}

[Length: 5]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_779995105}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0]{lang="EN-US"}[发送了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:174 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}]{#struct_0_19508_69870_x2006653738}

[Received a packet on interface GE1/0/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 0180-c200-0003]{lang="EN-US"}

[Source Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 0]{lang="EN-US"}

[Packet Length: 16]{lang="EN-US"}

[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}

[Code: 2 ]{lang="EN-US"}

[Identifier: 1]{lang="EN-US"}

[Length: 16]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1603225765}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0]{lang="EN-US"}[接收了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:175 2011 Sysname 802.1X/7/EVENT: ]{lang="EN-US"}]{#struct_0_19508_69870_x1114674380}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Response state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_x1253059094}*[进入响应状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:176 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_74472934}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Create server timeout timer successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_867090102}*[成功创建服务器超时定时器]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:178 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1046272797}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Request state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_2000771801}*[进入请求状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:178 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2006194986}

[Sending EAP Packet (identifier 2, type 4)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1689955891}*[正在发送]{style="font-family:宋体;color:black"}[EAP]{lang="EN-US" style="color:black"}[报文（匹配标识为]{style="font-family:宋体;
color:black"}[2]{lang="EN-US" style="color:black"}[，类型为]{style="font-family:宋体;color:black"}[4]{lang="EN-US" style="color:black"}[）]{style="font-family:宋体;color:black"}*

[[\*Jan  1 02:44:12:183 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}]{#struct_0_19508_69870_267385604}

[Transmitted a packet on interface GE1/0/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Source Mac Address: 00e0-fc00-5830]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 0]{lang="EN-US"}

[Packet Length: 22]{lang="EN-US"}

[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}

[Code: 1]{lang="EN-US"}

[Identifier: 2]{lang="EN-US"}

[Length: 22]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x263789893}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0/1]{lang="EN-US"}[发送了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:185 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}]{#struct_0_19508_69870_x2006260522}

[Received a packet on interface GE1/0/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 0180-c200-0003]{lang="EN-US"}

[Source Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 0]{lang="EN-US"}

[Packet Length: 33]{lang="EN-US"}

[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}

[Code: 2]{lang="EN-US"}

[Identifier: 2]{lang="EN-US"}

[Length: 33]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1754872424}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0/1]{lang="EN-US"}[接收了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:186 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x690825822}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Response state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_956073083}*[进入响应状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:187 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_876966287}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Create server timeout timer successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1463921055}*[成功创建服务器超时定时器]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:190 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2006326058}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] User sent authentication request.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1130050487}*[用户发送认证请求]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:191 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x513469165}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] AAA processed authentication request and returned Processing.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_19508_69870_911475423}*[处理认证请求并返回正在处理的结果]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:205 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x1281362629}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] User received authentication response, RespCode=0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_364760327}*[用户收到认证响应，响应码为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Jan  1 02:44:12:206 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1229637377}

[\[1cbd-b9e3-b0ed:VLAN1: GE1/0/1\] BE is in Success state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_826916604}*[进入成功状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:211 2011 Sysname 802.1X/7/PACKET:]{lang="EN-US"}]{#struct_0_19508_69870_x2006391594}

[Transmitted a packet on interface GE1/0/1.]{lang="EN-US"}

[\-\--Verbose information of the packet\-\--]{lang="EN-US"}

[Destination Mac Address: 1cbd-b9e3-b0ed]{lang="EN-US"}

[Source Mac Address: 00e0-fc00-5830]{lang="EN-US"}

[Mac Frame Type: 888e]{lang="EN-US"}

[Protocol Version ID: 1]{lang="EN-US"}

[Packet Type: 0]{lang="EN-US"}

[Packet Length: 4]{lang="EN-US"}

[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}

[Code: 3]{lang="EN-US"}

[Identifier: 3]{lang="EN-US"}

[Length: 4]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x1192215809}*[接口]{style="font-family:宋体"}[Gigabitethernet1/0/1]{lang="EN-US"}[发送了一个报文]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:212 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_96925062}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] PAE is inAuthenticated state.]{lang="EN-US"}

[*[// PAE]{lang="EN-US"}*]{#struct_0_19508_69870_415249163}*[进入认证状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:213 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1412996086}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] User sent authorization request.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1884679484}*[用户发送授权请求]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:214 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2005932842}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] AAA processed authorization request and returned Success.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_19508_69870_x206395785}*[处理授权请求并返回成功的结果]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:216 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_46348304}

[PORT_SM\[GE1/0/1\] received event DOT1X_PSM_E_USER_AUTHORED.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1361183923}*[接口接收到]{style="font-family:宋体"}[DOT1X_PSM_E_USER_AUTHORED]{lang="EN-US"}[事件]{style="font-family:
宋体"}*

[[\*Jan  1 02:44:12:219 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x954355332}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] User sent accounting-start request.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_x2087474396}*[用户发送计费开始请求]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:220 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_835492108}

[PORT_SM\[GE1/0/1\] received event DOT1X_PSM_E_END_AUTH.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1935526686}*[接口接收到]{style="font-family:宋体"}[DOT1X_PSM_E_END_AUTH]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:222 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_x2005998378}

[PORT_SM\[GE1/0/1\] entering disconnected state\...]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_19508_69870_1961191470}*[接口进入断开连接状态]{style="font-family:宋体"}*

[[\*Jan  1 02:44:12:583 2011 Sysname 802.1X/7/EVENT:]{lang="EN-US"}]{#struct_0_19508_69870_1660799051}

[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] BE is in Idle state.]{lang="EN-US"}

[*[// BE]{lang="EN-US"}*]{#struct_0_19508_69870_534848296}*[进入]{style="font-family:宋体"}[Idle]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

*[ ]{lang="EN-US"}*
