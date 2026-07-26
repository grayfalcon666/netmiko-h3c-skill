::: {#194034419 .myid}
[]{#_Toc404793754}[]{#struct_0_18704_x2318_1114601996}

**IP Source Guard \-- IP Source Guard调试命令 \-- debugging source binding**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_18704_x2318_x835153841}

[**[debugging ]{lang="EN-US"}**[{ **ip** \| **ipv6** } **source binding** { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_18704_x2318_x806463833}

[**[undo debugging ]{lang="EN-US"}**[{ **ip** \| **ipv6** } **source binding** { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_18704_x2318_779254984}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18704_x2318_x1683741396}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18704_x2318_833695393}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18704_x2318_173581415}

[[network-admin]{lang="EN-US"}]{#struct_0_18704_x2318_783172011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18704_x2318_x584189231}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18704_x2318_x2103933177}

[**[ip]{lang="EN-US"}**]{#struct_0_18704_x2318_1589127736}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[绑定功能的调试信息开关。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_18704_x2318_579392804}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[绑定功能的调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_18704_x2318_x932142651}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_18704_x2318_1803602755}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_18704_x2318_x2117125523}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_18704_x2318_415888681}

[]{#OLE_LINK1}[**[debugging source binding]{lang="EN-US"}**]{#struct_0_18704_x2318_x593997051}[命令用来打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[绑定功能的调试信息开关。]{style="font-family:宋体"}**[undo debugging source binding]{lang="EN-US"}**[命令用来关闭指定的绑定功能调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，端口绑定功能的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_18704_x2318_x2013422817}

[]{#struct_0_18704_x2318_x1771765025}[[表1-1 ]{lang="EN-US"}[debugging source binding error]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x202072334}[[字段]{style="font-family:黑体"}]{#struct_0_18704_x2318_x2104916217}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18704_x2318_x349476828}

[[Failed to assign binding info message.]{lang="EN-US"}]{#struct_0_18704_x2318_x1238805074}

[[下发绑定信息相关的消息失败]{style="font-family:宋体"}]{#struct_0_18704_x2318_792058721}

[[Failed to assign request for getting large data.]{lang="EN-US"}]{#struct_0_18704_x2318_662086941}

[[下发获取大量数据的请求消息失败]{style="font-family:宋体"}]{#struct_0_18704_x2318_1074278612}

[[ ]{lang="EN-US"}]{#_Toc130718927}

[[表1-2 ]{lang="EN-US"}[debugging source binding event]{lang="EN-US"}]{#struct_0_18704_x2318_458068080}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x203243342}[[字段]{style="font-family:黑体"}]{#struct_0_18704_x2318_x2104850681}

[[描述]{style="font-family:黑体"}]{#struct_0_18704_x2318_x552177334}

[[The module *module* has associated with IPCIM successfully.]{lang="EN-US"}]{#struct_0_18704_x2318_771932617}

[*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_1122620536}[模块与]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}[关联成功]{style="font-family:宋体"}

[[The module *module* has been disassociated.]{lang="EN-US"}]{#struct_0_18704_x2318_808399771}

[*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_682684402}[模块成功去关联]{style="font-family:宋体"}

[[Received addEntry message.]{lang="EN-US"}]{#struct_0_18704_x2318_x1860090631}

[[接收到添加表项的消息]{style="font-family:宋体"}]{#struct_0_18704_x2318_1162395064}

[[Received deleteEntry message.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104391928}

[[接收到删除表项的消息]{style="font-family:宋体"}]{#struct_0_18704_x2318_1141137658}

[[Received updateEntry message.]{lang="EN-US"}]{#struct_0_18704_x2318_x1680278347}

[[接收到更新表项的消息]{style="font-family:宋体"}]{#struct_0_18704_x2318_x297667872}

[[Received deleteEntryByKeyword message.]{lang="EN-US"}]{#struct_0_18704_x2318_421174019}

[[接收到根据关键字删除表项的消息]{style="font-family:宋体"}]{#struct_0_18704_x2318_x950669186}

[[Start smoothing process for module *module*.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104326392}

[[开始对]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_2017427567}[模块进行平滑处理]{style="font-family:宋体"}

[[The smoothing process for module *module* ended.]{lang="EN-US"}]{#struct_0_18704_x2318_1967418817}

[*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_1656073839}[模块平滑处理结束]{style="font-family:宋体"}

[[Received message to delete interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_18704_x2318_x546584766}

[[接收到删除接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104260856}[的消息]{style="font-family:宋体"}

[[Received message to activate interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_18704_x2318_x1317244210}

[[接收到激活接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18704_x2318_180327965}[的消息]{style="font-family:宋体"}

[[Received message to deactivate interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_18704_x2318_166608290}

[[接收到去激活接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_18704_x2318_934362369}[的消息]{style="font-family:宋体"}

[[Deleted the specified binding entries, VPN = v*pn-instance-name*.]{lang="EN-US"}]{#struct_0_18704_x2318_1530129560}

[[删除属于]{style="font-family:宋体"}[VPN *vpn-instance-name*]{lang="EN-US"}]{#struct_0_18704_x2318_x2104195320}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, ifIndex = *ifindex*.]{lang="EN-US"}]{#struct_0_18704_x2318_2028340684}

[[删除接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x582277436}[的接口上的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, portIndex = *portindex*.]{lang="EN-US"}]{#struct_0_18704_x2318_620077591}

[[删除端口索引为]{style="font-family:宋体"}*[portindex]{lang="EN-US"}*]{#struct_0_18704_x2318_875318372}[的端口上的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, ]{lang="EN-US"}]{#struct_0_18704_x2318_x2104129784}

[[clientVLAN = *client-vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_x1341471535}

[[删除属于]{style="font-family:宋体"}[clientVLAN *client-vlan-id*]{lang="EN-US"}]{#struct_0_18704_x2318_1838120230}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, secondVLAN = *second-vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_1986401531}

[[删除属于]{style="font-family:宋体"}[secondVLAN *second-vlan-id*]{lang="EN-US"}]{#struct_0_18704_x2318_x2104064248}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, serviceVLAN = *service-vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_x335605170}

[[删除属于]{style="font-family:宋体"}[serviceVLAN *service-vlan-id*]{lang="EN-US"}]{#struct_0_18704_x2318_x1654940721}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, privatetype = *privatetype.*]{lang="EN-US"}]{#struct_0_18704_x2318_x1410888196}

[[删除私有类型为]{style="font-family:宋体"}*[privatetype]{lang="EN-US"}*]{#struct_0_18704_x2318_x2103998712}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, MAC = *mac-address*.]{lang="EN-US"}]{#struct_0_18704_x2318_x451481945}

[[删除]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18704_x2318_x1633452558}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[.]{lang="EN-US"}[的绑定表项]{style="font-family:宋体"}

[[Deleted the specified binding entries, IP = *ip-address*, VPN = v*pn-instance-name*.]{lang="EN-US"}]{#struct_0_18704_x2318_x877843848}

[[删除指定的绑定表项，]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18704_x2318_x2103933176}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，且属于]{style="font-family:宋体"}[VPN *vpn-instance-name*]{lang="EN-US"}

[[Deleted the specified binding entries, source module = *module*.]{lang="EN-US"}]{#struct_0_18704_x2318_23043795}

[[删除来源模块为]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_1470508348}[的绑定表项]{style="font-family:宋体"}

[[Found a binding entry: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_1226674056}

[[查找到一条绑定表项：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104916216}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Binding entry not found: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_x1915560769}

[[查找绑定表项失败：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104850680}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[vlan]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Added a rule for driver: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, gatewayMAC = *gw-mac-address*, VLAN = *vlan-id,* drvContext\[0\] *= drvcontext\[0\]*, drvContext\[1\] = *drvcontext\[1\]*, returnCode = *return-code*.]{lang="EN-US"}]{#struct_0_18704_x2318_x2118261275}

[[添加驱动规则：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104391931}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，用户侧网关]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[gw-mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[drvContext\[0\]]{lang="EN-US"}[为]{style="font-family:宋体"}*[drvcontext\[0\]]{lang="EN-US"}*[，]{style="font-family:宋体"}[drvContext\[1\]]{lang="EN-US"}[为]{style="font-family:宋体"}*[drvcontext\[1\]]{lang="EN-US"}*[，处理结果代码为]{style="font-family:宋体"}*[return-code]{lang="EN-US"}*

[[Deleted a rule for driver: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, gatewayMAC = *gw-mac-address*, VLAN = *vlan-id*, drvContext\[0\] *= drvcontext\[0\]*, drvContext\[1\] = *drvcontext\[1\]*, returnCode = *return-code*.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104326395}

[[删除驱动规则：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104260859}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，用户侧网关]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[gw-mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[ vlan]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[drvContext\[0\]]{lang="EN-US"}[为]{style="font-family:宋体"}*[drvcontext\[0\]]{lang="EN-US"}*[，]{style="font-family:宋体"}[drvContext\[1\]]{lang="EN-US"}[为]{style="font-family:宋体"}*[drvcontext\[1\]]{lang="EN-US"}*[，处理结果代码为]{style="font-family:宋体"}*[return-code]{lang="EN-US"}*

[[Added a default rule for driver, returnCode = *returnvalue*.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104195323}

[[为驱动添加一条缺省规则，下驱动结果为]{style="font-family:宋体"}*[returnvalue]{lang="EN-US"}*]{#struct_0_18704_x2318_462256743}

[[Deleted a default rule for driver, returnCode = *returnvalue*.]{lang="EN-US"}]{#struct_0_18704_x2318_x176969113}

[[为驱动删除一条缺省规则，下驱动结果为]{style="font-family:宋体"}*[returnvalue]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104129787}

[[Added a binding entry: module = *module*, ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_x1744756062}

[[添加一条绑定表项：来源模块为]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104064251}[，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Deleted a binding entry: module = *module*, ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*.]{lang="EN-US"}]{#struct_0_18704_x2318_x1545524287}

[[删除一条绑定表项：来源模块为]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_x2103998715}[，接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Updated a binding entry (module = *module*): ]{lang="EN-US"}]{#struct_0_18704_x2318_1921171050}

[[Old info: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*,]{lang="EN-US"}]{#struct_0_18704_x2318_x2103933179}

[[VPN *=* v*pn-index.*]{lang="EN-US"}]{#struct_0_18704_x2318_782558682}

[[New info: ifIndex = *ifindex*, IP = *ip-address*, MAC = *mac-address*, VLAN = *vlan-id*, ]{lang="EN-US"}]{#struct_0_18704_x2318_x1684459389}

[[VPN *=* v*pn-index.*]{lang="EN-US"}]{#struct_0_18704_x2318_x2104916219}

[[更新来源模块为]{style="font-family:宋体"}*[module]{lang="EN-US"}*]{#struct_0_18704_x2318_1169552946}[的绑定表项：]{style="font-family:宋体"}

[[老的表项信息：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104850683}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[vlan]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[v*pn-index*]{lang="EN-US"}

[[新的表项信息：接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*]{#struct_0_18704_x2318_x2104391930}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[，]{style="font-family:宋体"}[vlan]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[v*pn-index*]{lang="EN-US"}

[[Number of driver assignments has reached the maximum.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104326394}

[[驱动下发的次数达到最大值]{style="font-family:宋体;color:black"}]{#struct_0_18704_x2318_x1470970675}

[[Deleted binding entries using the reset command.]{lang="EN-US"}]{#struct_0_18704_x2318_x2104260858}

[[使用]{style="font-family:宋体"}[reset]{lang="EN-US"}]{#struct_0_18704_x2318_x866905516}[命令删除了绑定表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18704_x2318_x525637455}

[[\# ]{lang="EN-US"}]{#struct_0_18704_x2318_x1970041597}[在设备上打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[绑定功能的错误调试信息开关，并通过命令行添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，当表项下发失败时，可能输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ip source binding error]{lang="EN-US"}]{#struct_0_18704_x2318_x2104195322}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001]{lang="EN-US"}

[\*Apr 28 18:27:30:866 2011 sysname IPSG/7/ERROR: -MDC=1; Failed to assign binding info message.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18704_x2318_x1103827198}*[表项下发内核失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18704_x2318_991378352}[在设备上打开]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[绑定功能的事件调试信息开关，并通过命令行添加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ip source binding event]{lang="EN-US"}]{#struct_0_18704_x2318_945734909}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001]{lang="EN-US"}

[\*Apr 28 18:37:30:866 2011 sysname IPSG/7/EVENT: -MDC=1; Added a rule for driver: ifIndex = 0x34, IP = 192.168.0.1, MAC = 0001-0001-0001, gatewayMAC = ffff-ffff-ffff,]{lang="EN-US"}

[ VLAN = 0xffff, drvContext\[0\] = 0x4, drvContext\[1\] = 0x4, returnCode = 0x0.]{lang="EN-US"}

[\*Apr 28 18:37:30:866 2011 sysname IPSG/7/EVENT: -MDC=1; Added a binding entry: module = Static, ifIndex = 0x1, IP = 192.168.0.1, MAC = 0001-0001-0001, VLAN = 65536.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18704_x2318_x871402622}*[成功添加一条静态绑定表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_18704_x2318_1971317687}[删除一条]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态绑定表项，输出如下调试信息。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0/1\] undo ip source binding ip-address 192.168.0.1 mac-address 0001-0001-0001]{lang="EN-US"}]{#struct_0_18704_x2318_x2104129786}

[\*Apr 28 18:40:48:812 2011 sysname IPSG/7/EVENT: -MDC=1; Deleted a rule for driver: if]{lang="EN-US"}

[Index = 0x34, IP = 192.168.0.1, MAC = 0001-0001-0001, gatewayMac = ffff-ffff-fff]{lang="EN-US"}

[f, VLAN = 0xffff, drvContext\[0\] = 0x4, drvContext\[1\] = 0x4, returnCode = 0x0.]{lang="EN-US"}

[\*Apr 28 18:40:48:812 2011 sysname IPSG/7/EVENT: -MDC=1; Deleted a binding entry: module = Static, ifIndex = 0x1, IP = 192.168.0.1, MAC = 0001-0001-0001, VLAN = 65536.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_18704_x2318_x178672121}*[成功删除一条静态绑定表项]{style="font-family:宋体"}*
