::: {#36427591 .myid}
[]{#_Toc404793066}[]{#struct_0_x7538_x3345_953078156}[]{#_Toc123629825}

**IPsec \-- IPsec调试命令 \-- debugging ipsec**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x1194410432}

[**[debugging ipsec]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ { **policy** \| **ipv6-policy** } *policy-name* \[ *seq-number* \] \| **profile** *profile-name* \| **spi** { *ipv4-address \|* **ipv6** *ipv6-address* } { **ah** \| **esp** *spi-number* } \| **remote-address** { *ipv4-address \|* **ipv6** *ipv6-address* } }]{lang="EN-US"}]{#struct_0_x7538_x3345_x1345081555}

[**[undo]{lang="EN-US"}**[ **debugging ipsec** { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x7538_x3345_1132133281}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x651654769}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x195813280}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_906807520}

[[network-admin]{lang="EN-US"}]{#struct_0_x7538_x3345_372226139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7538_x3345_x59203649}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x812577169}

[**[all]{lang="EN-US"}**]{#struct_0_x7538_x3345_x2005645541}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x7538_x3345_1084574154}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x7538_x3345_1132198817}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x7538_x3345_x662259243}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x7538_x3345_1208676448}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x7538_x3345_1104481498}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1037854712}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x7538_x3345_396690470}[：表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6553]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_1216027791}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[spi]{lang="EN-US"}**]{#struct_0_x7538_x3345_x952010313}[：指定]{style="font-family:宋体"}[SPI]{lang="EN-US"}[的三元组信息（]{style="font-family:宋体"}[SPI]{lang="EN-US"}[、安全协议、]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端地址）。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x7538_x3345_x824577628}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_x7538_x3345_1132264353}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ah]{lang="EN-US"}**]{#struct_0_x7538_x3345_925450996}[：指定]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[esp]{lang="EN-US"}**]{#struct_0_x7538_x3345_x979799347}[：指定]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[*[spi-number]{lang="EN-US"}*]{#struct_0_x7538_x3345_1655826731}[：表示]{style="font-family:宋体"}[SPI]{lang="EN-US"}[的序号，取值范围为]{style="font-family:宋体"}[256]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[remote-address]{lang="EN-US"}**]{#struct_0_x7538_x3345_704407657}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x7538_x3345_x973574481}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_x7538_x3345_44029140}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1636885997}

[**[debugging ipsec]{lang="EN-US"}**]{#struct_0_x7538_x3345_877317396}[命令用来打开]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging ipsec]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1131805601}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipsec error]{lang="EN-US"}]{#struct_0_x7538_x3345_x91370228}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x310985060}[[字段]{style="font-family:黑体"}]{#struct_0_x7538_x3345_553970066}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1780876479}

[[Failed to allocate memory.]{lang="EN-US"}]{#struct_0_x7538_x3345_1751080870}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1172167401}

[[Failed to set an IPv6 header variable to 0.]{lang="EN-US"}]{#struct_0_x7538_x3345_1131871137}

[[将]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_266706809}[头可变部分置零时出错]{style="font-family:宋体"}

[[Failed to add SP entry in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x579689863}

[[向内核添加]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_22276431}[（]{style="font-family:宋体"}[Security Policy]{lang="EN-US"}[，安全策略）]{style="font-family:宋体"} [entry]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to find SP entry in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1905557909}

[[在内核中查找]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_1078362392}[失败]{style="font-family:宋体"}

[[The SP doesn\'t exist in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1131936673}

[[内核中不存在]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x496948543}

[[The IPsec tunnel doesn\'t exist in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2003795538}

[[内核中不存在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1304717298}[隧道]{style="font-family:宋体"}

[[The DPD doesn\'t exist in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1153859245}

[[内核中不存在]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1132002209}[（]{style="font-family:宋体"}[Dead Peer Detection]{lang="EN-US"}[，对等体存活检测）]{style="font-family:宋体"}

[[Failed to require CCFJOB structure.]{lang="EN-US"}]{#struct_0_x7538_x3345_2078867025}

[[申请]{style="font-family:宋体"}[CCF JOB]{lang="EN-US"}]{#struct_0_x7538_x3345_2059169415}[结构失败]{style="font-family:宋体"}

[[Failed to encrypt CCF.]{lang="EN-US"}]{#struct_0_x7538_x3345_x771340181}

[[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_2005271093}[加密失败]{style="font-family:宋体"}

[[The SA doesn\'t exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_1132592033}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1673395629}[不存在]{style="font-family:宋体"}

[[Failed to decrypt CCF.]{lang="EN-US"}]{#struct_0_x7538_x3345_496472824}

[[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_x1302291878}[解密失败]{style="font-family:宋体"}

[[Failed to create CCF session.]{lang="EN-US"}]{#struct_0_x7538_x3345_1132657569}

[[创建]{style="font-family:宋体"}[CCF session]{lang="EN-US"}]{#struct_0_x7538_x3345_x1798064382}[失败]{style="font-family:宋体"}

[[The packet hash values don't match.]{lang="EN-US"}]{#struct_0_x7538_x3345_x575548255}

[[解封装后的报文哈希值不匹配]{style="font-family:宋体"}]{#struct_0_x7538_x3345_770923914}

[[No SA in IPsec tunnel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1738810264}

[[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815607}[隧道中没有]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Can\'t find next SA in AH-ESP mode. ]{lang="EN-US"}]{#struct_0_x7538_x3345_1753885354}

[[AH-ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_1439161606}[模式下，下一个]{style="font-family:宋体"}[SA]{lang="EN-US"}[找不到]{style="font-family:宋体"}

[[IPsec tunnel has been deleted or updated when fast forwarding is performed.]{lang="EN-US"}]{#struct_0_x7538_x3345_x730357663}

[[快转时]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750071}[隧道已经被删除或更新]{style="font-family:宋体"}

[[Packet should have been encrypted by IPsec.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1833152742}

[[报文本应该被]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1046258034}[保护]{style="font-family:宋体"}

[[SA has been deleted or updated when fast forwarding is performed.]{lang="EN-US"}]{#struct_0_x7538_x3345_39053549}

[[快转时]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596684535}[已经被删除或更新]{style="font-family:宋体"}

[[In transport mode, SA address doesn't match packet address.]{lang="EN-US"}]{#struct_0_x7538_x3345_1787626974}

[[传输模式下，报文中的地址与]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x987406240}[中的不一致]{style="font-family:宋体"}

[[The packet is too big: size = *size.*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596618999}

[[报文过大，报文大小为]{style="font-family:宋体"}*[size]{lang="EN-US"}*]{#struct_0_x7538_x3345_476170805}

[[Failed to add outer IP header.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1605789094}

[[添加外部]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7538_x3345_1820548394}[头失败]{style="font-family:宋体"}

[[The packet is not an IPsec packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077751}

[[非]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1137688828}[报文]{style="font-family:宋体"}

[[Can\'t find SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x369278375}

[[找不到]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012215}

[[Can\'t find SA by SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x328777387}

[[根据]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x553153304}[查找不到对应的]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Failed to add node to invalid SPI hash table.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946679}

[[向无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_1245429349}[哈希表添加节点失败]{style="font-family:宋体"}

[[Failed to add SA to IPsec tunnel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1199267009}

[[向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x577450614}[隧道添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to connect to the IPsec daemon.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881143}

[[连接]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2115352008}[用户态守护进程失败]{style="font-family:宋体"}

[[The block-flow-table doesn\'t exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_1674199272}

[[阻流表不存在]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1596291319}

[[The ACL mode is wrong.]{lang="EN-US"}]{#struct_0_x7538_x3345_x151404461}

[[ACL]{lang="EN-US"}]{#struct_0_x7538_x3345_1972838435}[模式错误]{style="font-family:宋体"}

[[Received replayed packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596225783}

[[收到了重放包]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2096491848}

[[Can't find SA when processing ICMP too big packet: SPI = *spi.*]{lang="EN-US"}]{#struct_0_x7538_x3345_138897560}

[[在处理]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815606}[过大报文过程中找不到]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SPI]{lang="EN-US"}[值为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*

[[No SA in IPsec tunnel.]{lang="EN-US"}]{#struct_0_x7538_x3345_187801413}

[[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2111961228}[隧道没有任何]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Invalid IPsec profile index.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750070}

[[无效的]{style="font-family:宋体"}[IPsec profile]{lang="EN-US"}]{#struct_0_x7538_x3345_895730613}[索引]{style="font-family:宋体"}

[[Failed to get IPsec profile name.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596684534}

[[获取]{style="font-family:宋体"}[IPsec profile]{lang="EN-US"}]{#struct_0_x7538_x3345_x941256381}[名称失败]{style="font-family:宋体"}

[[After decryption, source address check failed.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1194765054}

[[解封装后源地址检查失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1596618998}

[[Failed to create lipc socket.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1089913136}

[[创建]{style="font-family:宋体"}[lipc socket]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077750}[失败]{style="font-family:宋体"}

[[The SP already exists.]{lang="EN-US"}]{#struct_0_x7538_x3345_1591194527}

[[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1492964613}[已经存在]{style="font-family:宋体"}

[[Failed to add SP in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012214}

[[向内核添加]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1894861328}[失败]{style="font-family:宋体"}

[[Failed to add profile SP in kernel]{lang="EN-US"}]{#struct_0_x7538_x3345_866355290}

[[向内核添加]{style="font-family:宋体"}[profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946678}[失败]{style="font-family:宋体"}

[[Failed to add SA in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1483454006}

[[向内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881142}[失败]{style="font-family:宋体"}

[[Failed to delete SA in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x549268067}

[[删除内核中的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_949204349}[失败]{style="font-family:宋体"}

[[Failed to add IPsec tunnel in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596291318}

[[向内核添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1717488402}[隧道失败]{style="font-family:宋体"}

[[Failed to delete tunnel in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596225782}

[[删除内核中的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x530407907}[隧道失败]{style="font-family:宋体"}

[[Failed to add DPD in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815609}

[[向内核添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x2090743248}[失败]{style="font-family:宋体"}

[[Failed to delete DPD in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_2024872133}

[[删除内核中的]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750073}[失败]{style="font-family:宋体"}

[[The SP entry doesn\'t exist in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x670353328}

[[内核]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596684537}[不存在]{style="font-family:宋体"}

[[Number of SAs exceeded the limit.]{lang="EN-US"}]{#struct_0_x7538_x3345_624827560}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596619001}[数量超过最大值]{style="font-family:宋体"}

[[Failed to create IPsec IF-CB.]{lang="EN-US"}]{#struct_0_x7538_x3345_966749958}

[[创建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x982237014}[接口控制块失败]{style="font-family:宋体"}

[[Failed to set IPsec IF-CB to interface]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077753}

[[(ifIndex = *ifindex*)]{lang="EN-US"}]{#struct_0_x7538_x3345_1994479054}

[[向接口上设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012217}[接口控制块失败，其接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[Failed to change the aging timer for block-flow-table.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946681}

[[修改阻流表的老化时间失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_889395597}

[[Failed to create policy/template.]{lang="EN-US"}]{#struct_0_x7538_x3345_585355571}

[[由命令行创建策略]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881145}[模板失败]{style="font-family:宋体"}

[[Failed to create policy/template group.]{lang="EN-US"}]{#struct_0_x7538_x3345_1373046234}

[[由命令行创建策略组]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596291321}[模板组失败]{style="font-family:宋体"}

[[Failed to initialize policy hash table.]{lang="EN-US"}]{#struct_0_x7538_x3345_x507569285}

[[策略哈希表初始化失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1596225785}

[[Failed to recover policy/template.]{lang="EN-US"}]{#struct_0_x7538_x3345_x933692434}

[[恢复策略]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815608}[模板失败]{style="font-family:宋体"}

[[Failed to recover policy/template group.]{lang="EN-US"}]{#struct_0_x7538_x3345_638140107}

[[恢复策略组]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750072}[模板组失败]{style="font-family:宋体"}

[[Failed to recover transform reference.]{lang="EN-US"}]{#struct_0_x7538_x3345_2058530027}

[[恢复提议的引用关系失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1596684536}

[[Failed to save policy/template/profile info to DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2104055795}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596619000}[中保存策略]{style="font-family:宋体"}[/]{lang="EN-US"}[模板]{style="font-family:宋体"}[/profile]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Failed to delete policy/template/profile info from DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x599333983}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077752}[中删除策略]{style="font-family:宋体"}[/]{lang="EN-US"}[模板]{style="font-family:宋体"}[/profile]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Failed to save system configuration to DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_428395113}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012216}[中保存系统配置失败]{style="font-family:宋体"}

[[Failed to save transform configuration to DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x732061914}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946680}[中保存提议配置失败]{style="font-family:宋体"}

[[Failed to get system configuration from DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1839487758}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881144}[中读取系统配置失败]{style="font-family:宋体"}

[[Failed to save source interface configuration to DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1355837121}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596291320}[中保存源接口配置失败]{style="font-family:宋体"}[                ]{lang="EN-US"}

[[Failed to save interface configuration to DBM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596225784}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x7538_x3345_632391507}[中保存接口配置失败]{style="font-family:宋体"}

[[Failed to get interface name by ifIndex.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815611}

[[通过接口索引获取接口名称失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1734447352}

[[Failed to start IPsec daemon.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750075}

[[启动]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_136215726}[进程失败]{style="font-family:宋体"}

[[Failed to alloc SP index.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596684539}

[[分配]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x181741494}[索引失败]{style="font-family:宋体"}

[[Failed to malloc SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596619003}

[[分配]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_2129549372}[资源失败]{style="font-family:宋体"}

[[Failed to malloc SP entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077755}

[[分配]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012219}[资源失败]{style="font-family:宋体"}

[[Failed to update kernel SP entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_1284360721}

[[更新内核的]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946683}[失败]{style="font-family:宋体"}

[[Failed to find SP entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_x273403817}

[[查找]{style="font-family:宋体"}[SP entry ]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881147}[失败]{style="font-family:宋体"}

[[Failed to add SP to array.]{lang="EN-US"}]{#struct_0_x7538_x3345_210246820}

[[将]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596291323}[加入数组失败]{style="font-family:宋体"}

[[Failed to find template group.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596225787}

[[查找模板组失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_229106980}

[[Failed to add policy SP to kernel ]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596815610}

[[向内核添加]{style="font-family:宋体"}[policy SP]{lang="EN-US"}]{#struct_0_x7538_x3345_994436003}[失败]{style="font-family:宋体"}

[[Failed to find policy SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596750074}

[[查找]{style="font-family:宋体"}[policy SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596684538}[失败]{style="font-family:宋体"}

[[Failed to add profile SP to kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1384342447}

[[向内核添加]{style="font-family:宋体"}[profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596619002}[失败]{style="font-family:宋体"}

[[Failed to get SP when filling ISAKMP SA data.]{lang="EN-US"}]{#struct_0_x7538_x3345_563465431}

[[填充]{style="font-family:宋体"}[ISAKMP SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597077754}[数据时获取]{style="font-family:宋体"}[SP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to get DPD when filling ISAKMP SA data.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1597012218}

[[填充]{style="font-family:宋体"}[ISAKMP SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x281723220}[数据时获取]{style="font-family:宋体"}[DPD]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add IPsec tunnel when adding manual SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596946682}

[[添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596881146}[时添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道失败]{style="font-family:宋体"}

[[Failed to add IPsec tunnel during ISSU update process.]{lang="EN-US"}]{#struct_0_x7538_x3345_1776330761}

[[进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596291322}[升级时，添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道失败]{style="font-family:宋体"}

[[Failed to add SA when adding manual SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x910853812}

[[添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1596225786}[时添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to fill SA when adding ISAKMP SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_325498694}

[[添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_x2112856118}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[时填充]{style="font-family:宋体"}[SA]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add IPsec tunnel when adding ISAKMP SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_325564230}

[[添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_325629766}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[时添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道失败]{style="font-family:宋体"}

[[Failed to add timer when adding ISAKMP SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_60877838}

[[添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_325695302}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[时添加定时器失败]{style="font-family:宋体"}

[[Failed to alloc SPI.]{lang="EN-US"}]{#struct_0_x7538_x3345_325236550}

[[分配]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_1125897511}[失败]{style="font-family:宋体"}

[[Failed to alloc new SPI for ISAKMP SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_325302086}

[[分配]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_325367622}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[的新]{style="font-family:宋体"}[SPI]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to alloc larva SA index when adding larva SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_1521836337}

[[添加临时]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_325433158}[时分配临时]{style="font-family:宋体"}[SA]{lang="EN-US"}[索引失败]{style="font-family:宋体"}

[[Failed to add larval SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_326022982}

[[添加临时]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x690677043}[失败]{style="font-family:宋体"}

[[Failed to alloc SA index.]{lang="EN-US"}]{#struct_0_x7538_x3345_326088518}

[[分配]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_325498695}[索引失败]{style="font-family:宋体"}

[[Failed to alloc ISAKMP SA index.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2112856117}

[[分配]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_325564231}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引失败]{style="font-family:宋体"}

[[Failed to alloc manual SA index.]{lang="EN-US"}]{#struct_0_x7538_x3345_325629767}

[[分配手工方式]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_60877837}[的索引失败]{style="font-family:宋体"}

[[Failed to add SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_325695303}

[[添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_325236551}[失败]{style="font-family:宋体"}

[[Failed to add SA to kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_1125897512}

[[向内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_325302087}[失败]{style="font-family:宋体"}

[[Failed to add SA to kernel during ISSU update process.]{lang="EN-US"}]{#struct_0_x7538_x3345_325367623}

[[当进行]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x7538_x3345_325433159}[升级时向内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to alloc DPD Index.]{lang="EN-US"}]{#struct_0_x7538_x3345_964470684}

[[分配]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_326022983}[索引失败]{style="font-family:宋体"}

[[Failed to add DPD timer.]{lang="EN-US"}]{#struct_0_x7538_x3345_326088519}

[[添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1542557920}[定时器失败]{style="font-family:宋体"}

[[Failed to add DPD to kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_325498692}

[[向内核添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_325564228}[失败]{style="font-family:宋体"}

[[Failed to add DPD timer during smooth processing with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_325629764}

[[和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_60877836}[进行平滑处理时添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to add DPD to kernel during smooth processing with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_325695300}

[[和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_325236548}[进行平滑处理时向内核添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[The same outbound profile SA has existed. SPI: *spi* Protocol: *protocol*.]{lang="EN-US"}]{#struct_0_x7538_x3345_325302084}

[[已存在相同的出方向]{style="font-family:宋体"}[profile SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x425255797}[（]{style="font-family:宋体"}[IPsec profile]{lang="EN-US"}[生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[）。]{style="font-family:宋体"}[SPI]{lang="EN-US"}[值为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*[，协议类型为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*

[[The same outbound policy SA has existed. SPI: *spi*, Remote address: *remote-addr*, Protocol: *protocol*.]{lang="EN-US"}]{#struct_0_x7538_x3345_325367620}

[[已存在相同出方向的]{style="font-family:宋体"}[policy SA]{lang="EN-US"}]{#struct_0_x7538_x3345_325433156}[（]{style="font-family:宋体"}[IPsec policy]{lang="EN-US"}[生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[）。]{style="font-family:宋体"}[SPI]{lang="EN-US"}[值为]{style="font-family:宋体"}*[SPI]{lang="EN-US"}*[，对端地址为]{style="font-family:宋体"}*[remote-addr]{lang="EN-US"}*[，协议类型为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*

[[Failed to generate static route.]{lang="EN-US"}]{#struct_0_x7538_x3345_326022980}

[[新建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x690677045}[隧道时，生成路由信息失败]{style="font-family:宋体"}

[[Failed to add static route.]{lang="EN-US"}]{#struct_0_x7538_x3345_326088516}

[[新建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_325498693}[隧道时，路由模块添加静态路由失败]{style="font-family:宋体"}

[[Failed to delete static route.]{lang="EN-US"}]{#struct_0_x7538_x3345_325564229}

[[删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_578433938}[隧道时，路由模块删除静态路由失败]{style="font-family:宋体"}

[[Failed to notify route module of starting to smooth IPv4 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_325629765}

[[和路由模块平滑路由过程中通知路由模块开始平滑]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_325695301}[路由，通知失败]{style="font-family:宋体"}

[[Failed to notify route module of starting to smooth IPv6 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_325236549}

[[和路由模块平滑路由过程中通知路由模块开始平滑]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_325302085}[路由，通知失败]{style="font-family:宋体"}

[[Failed to subscribe service events.]{lang="EN-US"}]{#struct_0_x7538_x3345_325367621}

[[订阅服务事件失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1521836334}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ipsec event]{lang="EN-US"}]{#struct_0_x7538_x3345_634538404}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x283905156}[[字段]{style="font-family:黑体"}]{#struct_0_x7538_x3345_325433157}

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_964470670}

[[The IPsec IF-CB(ifIndex = *ifindex*) will be deleted in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1773296134}

[[内核中的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x600943604}[的接口控制快（接口序号为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*[）将要被删除掉]{style="font-family:宋体"}

[[Can\'t find block-flow-table.]{lang="EN-US"}]{#struct_0_x7538_x3345_x545686229}

[[找不到阻流表]{style="font-family:宋体"}]{#struct_0_x7538_x3345_879056363}

[[Can\'t find an IPsec tunnel to match the flow.]{lang="EN-US"}]{#struct_0_x7538_x3345_326022981}

[[找不到匹配流的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x690677046}[隧道]{style="font-family:宋体"}

[[IPsec daemon successfully connected.]{lang="EN-US"}]{#struct_0_x7538_x3345_1329240837}

[[成功连接到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1751895009}[用户态守护进程]{style="font-family:宋体"}

[[IPsec daemon disconnected.]{lang="EN-US"}]{#struct_0_x7538_x3345_x958840888}

[[与用户态守护进程失去连接]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x891751659}

[[Sent SA-Acquire message: SP ID = *ID.*]{lang="EN-US"}]{#struct_0_x7538_x3345_326088517}

[[发送]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1542557922}[协商请求，对应]{style="font-family:宋体"}[SP]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[ID]{lang="EN-US"}*

[[Sent SA-Expire message: SP ID = *SPID*, tunnel ID = *TNLID.*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1285358547}

[[发送]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1661028195}[重协商请求，对应]{style="font-family:宋体"}[SP]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[SPID]{lang="EN-US"}[，]{style="font-family:宋体"}*[Tunnel ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[TNLID]{lang="EN-US"}*

[[Sent Invalid-SPI message: SPI = *spi.*]{lang="EN-US"}]{#struct_0_x7538_x3345_567455468}

[[发送]{style="font-family:宋体"}[Invalid-SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_325498690}[消息，]{style="font-family:宋体"} [SPI]{lang="EN-US"}[值为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*

[[Sent DPD-Request message: DPD ID = *DPDID*]{lang="EN-US"}]{#struct_0_x7538_x3345_x2112856122}

[[发送]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x585642382}[探测请求消息，]{style="font-family:宋体"} [DPD ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[DPDID]{lang="EN-US"}*

[[Updated outbound SA of IPsec tunnel: SA ID = *saindex.*]{lang="EN-US"}]{#struct_0_x7538_x3345_x277521411}

[[更新]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2133160506}[隧道出方向的]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[序号为]{style="font-family:宋体"}*[saindex]{lang="EN-US"}*

[[Received an interface event message for interface *interface-type interface-num*, event: *event*.]{lang="EN-US"}]{#struct_0_x7538_x3345_325564226}

[[收到响应接口事件消息，接口名称为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x7538_x3345_578433953}[，接口事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Received interface network layer event message.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1217251760}

[[收到响应接口网络层事件消息]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1888895942}

[[Received an event message for slot *slot-id*, event: *event*.]{lang="EN-US"}]{#struct_0_x7538_x3345_325629762}

[[收到响应接口板事件消息，板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*]{#struct_0_x7538_x3345_60877842}[，消息类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Received an ACL message for ACL *acl-number*, event: *event*.]{lang="EN-US"}]{#struct_0_x7538_x3345_841431349}

[[收到]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x7538_x3345_325695298}[消息，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号为]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[，消息类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Received an address message for interface *interface-type interface-num*, event: *event*.]{lang="EN-US"}]{#struct_0_x7538_x3345_491336250}

[[收到地址消息，接口名称为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x7538_x3345_x641988915}[，消息类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Sent notify message to kernel: slot *slot-id*, event: *event*.]{lang="EN-US"}]{#struct_0_x7538_x3345_4961929}

[[发送]{style="font-family:宋体"}[notify]{lang="EN-US"}]{#struct_0_x7538_x3345_325236546}[消息给内核，板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[，消息类型为]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Sent *msg* to kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1212754655}

[[向内核发送消息]{style="font-family:宋体"}*[msg]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1099145825}[，]{style="font-family:宋体"}[msg]{lang="EN-US"}[是消息类型，包括以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x1580983107}[：添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_325302082}[：更新]{style="font-family:宋体"}[SP entry]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x425255795}[：删除]{style="font-family:宋体"}[SP entry]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add source-if SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x575626532}[：添加源接口]{style="font-family:宋体"}[SP entry]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete source-if SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_325367618}[：删除源接口]{style="font-family:宋体"}[SP entry]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x434478809}[：添加]{style="font-family:宋体"}[SP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x445020309}[：更新]{style="font-family:宋体"}[SP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x2036199318}[：删除]{style="font-family:宋体"}[SP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_325433154}[：添加]{style="font-family:宋体"}[profile SP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_964470671}[：删除]{style="font-family:宋体"}[profile SP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1773296135}[：更新]{style="font-family:宋体"}[profile SP]{lang="EN-US"}

[[Added SA to kernel successfully .]{lang="EN-US"}]{#struct_0_x7538_x3345_326022978}

[[向内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_2030312147}[成功]{style="font-family:宋体"}

[[SA successfully added in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x319426263}

[[内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x162808871}[成功]{style="font-family:宋体"}

[[SA successfully deleted in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_326088514}

[[删除内核中的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1542557925}[成功]{style="font-family:宋体"}

[[Added outbound SA to IPsec tunnel(SA ID = *sa-index*)]{lang="EN-US"}]{#struct_0_x7538_x3345_x1285293011}

[[向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_325498691}[隧道添加出方向]{style="font-family:宋体"}[SA(SA]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[sa-index]{lang="EN-US"}*[)]{lang="EN-US"}

[[Added tunnel to kernel successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2112856121}

[[向内核添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x182357855}[隧道成功]{style="font-family:宋体"}

[[IPsec tunnel successfully added in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_325564227}

[[内核添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_578433952}[隧道成功]{style="font-family:宋体"}

[[IPsec tunnel successfully deleted in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1217251759}

[[删除内核中的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_325629763}[隧道成功]{style="font-family:宋体"}

[[IPsec tunnel successfully added to list.]{lang="EN-US"}]{#struct_0_x7538_x3345_60877841}

[[向链表添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1114883787}[隧道成功]{style="font-family:宋体"}

[[IPsec tunnel added to aggregation-hash]{lang="EN-US"}]{#struct_0_x7538_x3345_325695299}

[[向聚合哈希表中添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_491336251}[隧道成功]{style="font-family:宋体"}

[[Added SP entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_x641988916}

[[添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_325236547}

[[Added SP by policy.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1212754654}

[[根据策略添加]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_466938116}

[[SP entry successfully added in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_325302083}

[[内核成功添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x425255796}

[[SP successfully added in kernel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x575560996}

[[内核成功添加]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_325367619}

[[Added policy SA by manual SP, SP index: *index*, SP sequence number: *sp-seq*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x434478810}

[[成功根据手工]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_325433155}[添加策略]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SP]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[sp-index]{lang="EN-US"}*[，]{style="font-family:宋体"}[SP]{lang="EN-US"}[序号为]{style="font-family:宋体"}*[sp-seq]{lang="EN-US"}*

[[Successfully added an IPsec tunnel during ISSU update process.]{lang="EN-US"}]{#struct_0_x7538_x3345_964470672}

[[在]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x7538_x3345_x1773296136}[升级时成功添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Added an IPsec tunnel when adding manual SA: tunnel index = *tunnel-id*, tunnel sequence number = *tunnel_seq*.]{lang="EN-US"}]{#struct_0_x7538_x3345_326022979}

[[添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_2030312146}[过程中成功添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道索引是]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道序号是]{style="font-family:宋体"}*[tunnel_seq]{lang="EN-US"}*

[[Added manual SAs. Number of SAs added is *number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_326088515}

[[成功添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1542557924}[。添加的]{style="font-family:宋体"}[SA]{lang="EN-US"}[的个数]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[No. *ordinal-number* SA: index = *sa-id,* sequence number = *sa-seq*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1285227475}

[[第]{style="font-family:宋体"}*[ordinal-number]{lang="EN-US"}*]{#struct_0_x7538_x3345_1891582635}[个]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引是]{style="font-family:宋体"}*[sa-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的序列号是]{style="font-family:宋体"}*[sa-seq]{lang="EN-US"}*

[[Added SA context to SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1230410029}

[[成功向]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_19049187}[中添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[内容]{style="font-family:宋体"}

[[Added an IPsec tunnel when adding ISAKMP SA: tunnel index = *tunnel-id*, tunnel sequence number = *tunnel_seq*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648171}

[[添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_1890694028}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[过程中成功添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道索引是]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道序号是]{style="font-family:宋体"}*[tunnel_seq]{lang="EN-US"}*

[[Added ISAKMP SAs. Number of SAs added is *number*. No. *ordinal-number* SA: index = *sa-id,* sequence number = *sa-seq*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713707}

[[成功添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_x2014184837}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[。添加的]{style="font-family:宋体"}[SA]{lang="EN-US"}[的个数]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，第]{style="font-family:宋体"}*[ordinal-number]{lang="EN-US"}*[个的]{style="font-family:宋体"}[SA]{lang="EN-US"}[索引是]{style="font-family:宋体"}*[sa-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[序号是]{style="font-family:宋体"}*[sa-seq]{lang="EN-US"}*

[[Added SA context to IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779243}

[[向]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1884831453}[发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[内容]{style="font-family:宋体"}

[[Timer successfully added when adding ISAKMP SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320491}

[[添加]{style="font-family:宋体"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_x471836471}[方式]{style="font-family:宋体"}[SA]{lang="EN-US"}[时添加定时器成功]{style="font-family:宋体"}

[[Started to smoothly process SA with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1167475038}

[[开始和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1891386027}[进行平滑]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Finished smooth processing SA with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_1477394952}

[[结束和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451563}[平滑]{style="font-family:宋体"}[SA ]{lang="EN-US"}

[[Started to smoothly process IPsec tunnel with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242111092}

[[开始和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517099}[进行平滑]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Finished smooth processing IPsec tunnel with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1261908818}

[[结束和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106923}[平滑]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Started to smoothly process DPD with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_1752908226}

[[开始和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_562088131}[进行平滑]{style="font-family:宋体"}[DPD]{lang="EN-US"}

[[Finished smooth processing DPD with IKE.]{lang="EN-US"}]{#struct_0_x7538_x3345_1892172459}

[[结束和]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_2143514461}[平滑]{style="font-family:宋体"}[DPD]{lang="EN-US"}

[[Sent *msg* message to slot:*slot-id*, message type is *type-id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891582636}

[[向]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1230475565}[号接口板发送]{style="font-family:宋体"}*[msg]{lang="EN-US"}*[消息，消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}*[type-id]{lang="EN-US"}*

[[消息类型和其对应的类型]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648172}[如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[debug]{lang="EN-US"}]{#struct_0_x7538_x3345_1890628492}[：调试，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[anti-replay check]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713708}[：抗重放检查]{lang="EN-US" style="font-family:
  宋体"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[4]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[decryption check]{lang="EN-US"}]{#struct_0_x7538_x3345_x2013595013}[：解封装后检查]{lang="EN-US" style="font-family:
  宋体"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[log switch]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779244}[：]{lang="EN-US" style="font-family:宋体"}[log]{lang="EN-US"}[开关]{lang="EN-US" style="font-family:宋体"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[6]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[idle]{lang="EN-US"}]{#struct_0_x7538_x3345_1884634845}[：空闲，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[7]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[global df-bit]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320492}[：全局]{lang="EN-US" style="font-family:宋体"}[df-bit]{lang="EN-US"}[设置]{lang="EN-US" style="font-family:宋体"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[8]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[df-bit]{lang="EN-US"}]{#struct_0_x7538_x3345_x471639863}[：接口]{lang="EN-US" style="font-family:宋体"}[df-bit]{lang="EN-US"}[设置，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[9]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[all global configuration]{lang="EN-US"}]{#struct_0_x7538_x3345_1891386028}[：所有全局配置]{lang="EN-US" style="font-family:宋体"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_1476805128}[：添加]{lang="EN-US" style="font-family:宋体"}[SP entry]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[11]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451564}[：更新]{lang="EN-US" style="font-family:
  宋体"}[SP entry]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[12]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete SP entry]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242045556}[：删除]{lang="EN-US" style="font-family:
  宋体"}[SP entry]{lang="EN-US"}[/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[13]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add SP]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517100}[：添加]{lang="EN-US" style="font-family:宋体"}[SP]{lang="EN-US"}[/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[14]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update SP]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106924}[：更新]{lang="EN-US" style="font-family:宋体"}[SP]{lang="EN-US"}[/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[15]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete SP]{lang="EN-US"}]{#struct_0_x7538_x3345_1753366978}[：删除]{lang="EN-US" style="font-family:宋体"}[SP]{lang="EN-US"}[/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_1892172460}[：添加]{lang="EN-US" style="font-family:宋体"}[profile SP]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_2143973210}[：更新]{style="font-family:宋体"}[profile SP]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[18]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete profile SP]{lang="EN-US"}]{#struct_0_x7538_x3345_1891582633}[：删除]{style="font-family:宋体"}[profile SP]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[19]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add tunne]{lang="EN-US"}]{#struct_0_x7538_x3345_x1230803245}[l]{lang="EN-US"}[：添加]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete tunnel]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648169}[：删除]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[21]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1890169741}[：添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[22]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713705}[：删除]{style="font-family:宋体"}[SA]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[23]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update MTU]{lang="EN-US"}]{#struct_0_x7538_x3345_x2014315909}[：更新]{style="font-family:宋体"}[MTU]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[24]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[switch SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779241}[：切换]{style="font-family:宋体"}[SA]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[25]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete block-flow table]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320489}[：删除阻流表]{style="font-family:宋体"}[/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[26]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[add DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x471312184}[：添加]{style="font-family:宋体"}[DPD/]{lang="EN-US"}[类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[27]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1891386025}[：更新]{style="font-family:宋体"}[DPD]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[28]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1477526024}[：删除]{style="font-family:宋体"}[DPD]{lang="EN-US"}[，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[29]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[update DPD index of SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451561}[：更新]{style="font-family:宋体"}[SA]{lang="EN-US"}[的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[索引，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[30]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reset statistics]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242242164}[：重置统计计数，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[31]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[idle report]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517097}[：]{style="font-family:宋体"}[idle]{lang="EN-US"}[报告，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[32]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth start]{lang="EN-US"}]{#struct_0_x7538_x3345_x1262564178}[：平滑开始，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[32]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth end]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106921}[：平滑结束，类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[34]{lang="EN-US"}

[[Adding route: Dest/Mask: *ip-address*/*mask-length*, Next hop: *ip-address* , Source vpn instance: *vpn-name*, Destination vpn instance: *vpn-name*, Tag: *tag-value*, Preference: *preference-num*]{lang="EN-US"}]{#struct_0_x7538_x3345_1753039298}

[[新建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1892172457}[隧道时，即将添加一条静态路由信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dest/Mask]{lang="EN-US"}]{#struct_0_x7538_x3345_1891582634}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[掩码长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Next hop]{lang="EN-US"}]{#struct_0_x7538_x3345_x1230344493}[：下一跳]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source vpn instance]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648170}[：路由目的地址所属的]{lang="EN-US" style="font-family:
  宋体"}[VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination vpn instance]{lang="EN-US"}]{#struct_0_x7538_x3345_1890759564}[：路由下一跳地址所属的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tag]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713706}[：路由标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Preference]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779242}[：路由优先级]{lang="EN-US" style="font-family:宋体"}

[[Deleting route: Dest/Mask: *ip-address*/*mask-length*, Next hop: *ip-address*, Source vpn instance: *vpn-name*, Destination vpn instance: *vpn-name*, Tag: *tag-value*, Preference: *preference-num*]{lang="EN-US"}]{#struct_0_x7538_x3345_1884765917}

[[删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320490}[隧道时，即将删除一条静态路由信息]{style="font-family:宋体"}

[[Successfully added a static route.]{lang="EN-US"}]{#struct_0_x7538_x3345_x471770935}

[[新建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1891386026}[隧道时，路由模块添加静态路由成功]{style="font-family:宋体"}

[[Only increased the reference count of the static route but didn\'t add it.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451562}

[[新建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242176628}[隧道时，发现已经向路由模块添加过相同的静态路由，则不再通知路由模块添加此路由仅增加该路由的引用计数]{style="font-family:宋体"}

[[Successfully deleted a static route.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517098}

[[删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1261974354}[隧道时，路由模块删除静态路由成功]{style="font-family:宋体"}

[[Only reduced the reference count of the static route but didn\'t delete it.]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106922}

[[删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1892172458}[隧道时，发现两个以上]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对应同一条静态路由，则不通知路由模块删除该静态路由仅减少该路由的引用计数]{style="font-family:宋体"}

[[Started to smoothly process the IPv4 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_2143448925}

[[开始对]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_1891582631}[静态路由进行平滑处理]{style="font-family:宋体"}

[[Started to smoothly process the IPv6 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648167}

[[开始对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_1890300813}[静态路由进行平滑处理]{style="font-family:宋体"}

[[Finished smooth processing of the IPv4 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713703}

[[结束对]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_x2013922693}[静态路由的平滑处理]{style="font-family:宋体"}

[[Finished smooth processing of the IPv6 static routes.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779239}

[[结束对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320487}[静态路由的平滑处理]{style="font-family:宋体"}

[[Successfully subscribed service events.]{lang="EN-US"}]{#struct_0_x7538_x3345_x471443256}

[[成功订阅所有的服务事件]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1891386023}

[[Received a service event: the status of IPv4 route service is up.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451559}

[[接收到一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_x1241717879}[路由服务]{style="font-family:宋体"}[up]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received a service event: the status of IPv4route service is down.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517095}

[[接收到一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106919}[路由服务]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received a service event: the status of IPv6 route service is up.]{lang="EN-US"}]{#struct_0_x7538_x3345_1753563589}

[[接收到一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_1892172455}[路由服务]{style="font-family:宋体"}[up]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Received a service event: the status of IPv6 route service is down.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891582632}

[[接收到一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_x1230737709}[路由服务]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ipsec packet]{lang="EN-US"}]{#struct_0_x7538_x3345_1891648168}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x505782756}[]{#struct_0_x7538_x3345_1890235277}[]{#_Toc277669731}[]{#_Toc277669732}[]{#_Toc277669735}[]{#_Toc277669736}[]{#_Toc277669737}[]{#_Toc277669738}[]{#_Toc277669739}[]{#_Toc277669740}[]{#_Toc277669741}[]{#_Toc277669742}[]{#_Toc277669743}[]{#_Toc277669744}[]{#_Toc277669745}[]{#_Toc277669746}[]{#_Toc277669795}[]{#_Toc277669796}[]{#_Toc277669824}[]{#_Toc277669825}[]{#_Toc277669845}[]{#_Toc277669846}[]{#_Toc277669865}[]{#_Toc277669866}[]{#_Toc277669867}[]{#_Toc277669868}[]{#_Toc277669869}[]{#_Toc277669871}[]{#_Toc277669872}[]{#_Toc277669873}[]{#_Toc277669874}[]{#_Toc277669879}[]{#_Toc277669883}[]{#_Toc277669887}[]{#_Toc277669888}[]{#_Toc277669891}[]{#_Toc277669892}[]{#_Toc277669894}[]{#_Toc277669899}[]{#_Toc277669900}[]{#_Toc277669901}[]{#_Toc277669902}[]{#_Toc277669903}[]{#_Toc277669904}[]{#_Toc277669905}[]{#_Toc277669906}[]{#_Toc277669907}[]{#_Toc277669908}[]{#_Toc277669910}[]{#_Toc277669912}[]{#_Toc277669916}[]{#_Toc277669920}[]{#_Toc277669921}[]{#_Toc277669924}[]{#_Toc277669925}[]{#_Toc277669926}[]{#_Toc277669927}[]{#_Toc277669930}[]{#_Toc277669931}[]{#_Toc277669932}[]{#_Toc277669933}[]{#_Toc277669934}[]{#_Toc277669935}[]{#_Toc277669936}[]{#_Toc277669937}[]{#_Toc277669938}[]{#_Toc277669939}[]{#_Toc277669940}[]{#_Toc277669941}[]{#_Toc277669990}[]{#_Toc277669991}[]{#_Toc277670043}[]{#_Toc277670044}[]{#_Toc277670067}[]{#_Toc277670068}[]{#_Toc277670087}[]{#_Toc277670088}[]{#_Toc277670089}[]{#_Toc277670090}[]{#_Toc277670091}[]{#_Toc277670092}[]{#_Toc277670095}[]{#_Toc277670097}[]{#_Toc277670098}[]{#_Toc277670099}[]{#_Toc277670100}[]{#_Toc277670105}[]{#_Toc277670109}[]{#_Toc277670115}[]{#_Toc277670119}[]{#_Toc277670122}[]{#_Toc277670127}[]{#_Toc277670128}[]{#_Toc277670129}[]{#_Toc277670131}[]{#_Toc277670133}[]{#_Toc277670134}[]{#_Toc277670138}[]{#_Toc277670139}[]{#_Toc277670140}[]{#_Toc277670141}[]{#_Toc277670142}[]{#_Toc277670143}[]{#_Toc277670144}[]{#_Toc277670145}[]{#_Toc277670149}[]{#_Toc277670150}[]{#_Toc277670153}[]{#_Toc277670157}[]{#_Toc277670161}[]{#_Toc277670162}[字段]{style="font-family:黑体"}

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x1270171967}

[[Packet will be sent to CCF for sync-encryption.]{lang="EN-US"}]{#struct_0_x7538_x3345_x634384513}

[[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_1337724900}[执行同步加密操作]{style="font-family:宋体"}

[[Packet will be sent to CCF for sync-decryption]{lang="EN-US"}]{#struct_0_x7538_x3345_x1428209074}

[[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_1679331055}[执行同步解密操作]{style="font-family:宋体"}

[[Packet will be sent to CCF for asyn-encryption.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891713704}

[[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_x2014381445}[执行异步加密操作]{style="font-family:宋体"}

[[Packet will be sent to CCF for asyn-decryption.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1964402840}

[[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}]{#struct_0_x7538_x3345_1262459513}[执行异步解密操作]{style="font-family:宋体"}

[[Found SA with SPI *spi*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1626463478}

[[已经找到]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_1891779240}[为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Packet matches SP *spid*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1884896989}

[[报文匹配]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_740122536}[，]{style="font-family:宋体"}[SP ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[spid]{lang="EN-US"}*[.]{lang="EN-US"}

[[Packet has been encrypted by SA whose SPI is *spi*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1251192529}

[[报文已经被]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_x275043122}[为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[加密]{style="font-family:宋体"}

[[Packet has been decrypted by SA whose SPI is *spi*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1891320488}

[[报文已经被]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_x471246648}[为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[解密]{style="font-family:宋体"}

[[ESP auth algorithm: *auth*, ESP encp algorithm: *encp*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x770720389}

[[ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_1226113705}[采用的认证算法为]{style="font-family:宋体"}*[auth]{lang="EN-US"}*[，加密算法为]{style="font-family:宋体"}*[encp]{lang="EN-US"}*

[[AH auth algorithm: *auth*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1381461614}

[[AH]{lang="EN-US"}]{#struct_0_x7538_x3345_1891386024}[采用的认证算法为]{style="font-family:宋体"}*[auth]{lang="EN-US"}*

[[Src : *src* Dst : *dst* SPI : *spi*]{lang="EN-US"}]{#struct_0_x7538_x3345_1477591560}

[[报文的源地址为，目的地址为，]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_x343162941}[值为]{style="font-family:宋体"}*[spi]{lang="EN-US"}*

[[Received IPsec(AH) packet]{lang="EN-US"}]{#struct_0_x7538_x3345_x1142282351}

[[入方向收到]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x7538_x3345_2065193724}[报文]{style="font-family:宋体"}

[[Received IPsec(ESP) packet]{lang="EN-US"}]{#struct_0_x7538_x3345_1891451560}

[[入方向收到]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242307700}[报文]{style="font-family:宋体"}

[[Received IPSec packet from fast forwarding]{lang="EN-US"}]{#struct_0_x7538_x3345_x1017860960}

[[快转入方向收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1891517096}[报文]{style="font-family:宋体"}

[[Sent routing protocol packet by IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1262629714}

[[路由协议报文经由]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1042809757}[发送]{style="font-family:宋体"}

[[Sent IPsec packet]{lang="EN-US"}]{#struct_0_x7538_x3345_x95790012}

[[报文经由]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1892106920}[发送]{style="font-family:宋体"}

[[Sent packet by IPsec fast forwarding]{lang="EN-US"}]{#struct_0_x7538_x3345_1753104834}

[[报文经由]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1047417478}[快转发送]{style="font-family:宋体"}

[[Added IP fast forwarding entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1049494456}

[[添加快转表项]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1892172456}

[[Added IPv6 fast forwarding entry.]{lang="EN-US"}]{#struct_0_x7538_x3345_2143579997}

[[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_x1062121246}[快转表项]{style="font-family:宋体"}

[[Failed to find SA by SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_2067863902}

[[根据]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300720}[找不到对应的]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[The packet is too big, mtu = *mtu*, packet len = *len*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x926686668}

[[报文过大，]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x7538_x3345_262215782}[值为]{style="font-family:宋体"}*[mtu]{lang="EN-US"}*[，长度为]{style="font-family:宋体"}*[len]{lang="EN-US"}*

[[The reason of dropping packet is *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837235184}

[[报文被丢弃的原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x7538_x3345_x536896798}[，包括以下几种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet too long]{lang="EN-US"}]{#struct_0_x7538_x3345_x1209927191}[：报文太长]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_822233354}[：无效]{lang="EN-US" style="font-family:宋体"}[SPI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No available SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x837169648}[：找不到]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No available IPsec tunnel]{lang="EN-US"}]{#struct_0_x7538_x3345_x972090807}[：找不到]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Encryption failed]{lang="EN-US"}]{#struct_0_x7538_x3345_x1044708965}[：加密失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Decryption failed]{lang="EN-US"}]{#struct_0_x7538_x3345_x837104112}[：解密失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loop too many times]{lang="EN-US"}]{#struct_0_x7538_x3345_x2105405531}[：本机循环次数过多]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL check failed]{lang="EN-US"}]{#struct_0_x7538_x3345_x1405871185}[：]{lang="EN-US" style="font-family:
  宋体"}[ACL]{lang="EN-US"}[检查失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Address does not match with SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1973705961}[：报文地址与]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[中的地址不匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Anti-replay sequence number reached the max]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562864}[：抗重放序号达到最大值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[The encapsulation mode does not match]{lang="EN-US"}]{#struct_0_x7538_x3345_945015724}[：封装类型不匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receive a ESP dummy packet]{lang="EN-US"}]{#struct_0_x7538_x3345_1906381505}[：收到]{lang="EN-US" style="font-family:宋体"}[ESP]{lang="EN-US"}[保活报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Memory alloc failed]{lang="EN-US"}]{#struct_0_x7538_x3345_x837497328}[：内存分配失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet length wrong]{lang="EN-US"}]{#struct_0_x7538_x3345_264406212}[：长度长度错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Replayed packet]{lang="EN-US"}]{#struct_0_x7538_x3345_182930972}[：重放报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authentication failed]{lang="EN-US"}]{#struct_0_x7538_x3345_x837431792}[：认证失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Security protocol set of SA does not match]{lang="EN-US"}]{#struct_0_x7538_x3345_641297919}[：]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[的安全协议组合与对端不匹配]{lang="EN-US" style="font-family:宋体"}

[[Inbound IPsec AH processing: Authentication succeeded.]{lang="EN-US"}]{#struct_0_x7538_x3345_710154363}

[[入方向]{style="font-family:宋体"}[IPsec AH]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366256}[处理：认证成功]{style="font-family:宋体"}

[[Outbound IPsec AH processing: Authentication finished, anti-replay SN is *sn* .]{lang="EN-US"}]{#struct_0_x7538_x3345_1002830081}

[[出方向]{style="font-family:宋体"}[IPsec AH]{lang="EN-US"}]{#struct_0_x7538_x3345_x283958550}[处理：认证完成，抗重放序号为]{style="font-family:宋体"}*[sn]{lang="EN-US"}*

[[Inbound IPsec ESP processing: Decryption succeeded.]{lang="EN-US"}]{#struct_0_x7538_x3345_x836776432}

[[入方向]{style="font-family:宋体"}[IPsec ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_1372191107}[处理：解密成功]{style="font-family:宋体"}

[[Outbound IPsec ESP processing: Encryption succeeded, anti-replay SN is *sn*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x836710896}

[[出方向]{style="font-family:宋体"}[IPsec ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_251847359}[处理：加密成功，抗重放序号为]{style="font-family:宋体"}*[sn]{lang="EN-US"}*

[[Outbound IPsec processing: Sent packet back to IP forwarding.]{lang="EN-US"}]{#struct_0_x7538_x3345_x645358771}

[[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300719}[处理：将报文重新发送给]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发]{style="font-family:宋体"}

[[Inbound IPsec processing: Sent packet back to IP forwarding.]{lang="EN-US"}]{#struct_0_x7538_x3345_x926227917}

[[入方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1654092774}[处理：将报文重新发送给]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发]{style="font-family:宋体"}

[[Outbound IPsec processing: Sent packet back to IP forwarding for following process.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837235183}

[[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x537224478}[处理：将报文返回转发继续处理后续业务]{style="font-family:宋体"}

[[IPsec processing: Tunnel mode]{lang="EN-US"}]{#struct_0_x7538_x3345_x837169647}

[[采用隧道模式]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x971763127}

[[IPsec processing: Transport mode]{lang="EN-US"}]{#struct_0_x7538_x3345_1367570239}

[[采用传输模式]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x837104111}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x2105339995}

[[\# ]{lang="EN-US"}]{#struct_0_x7538_x3345_x718728264}[设备上已存在满配的]{style="font-family:宋体"}[SP]{lang="EN-US"}[，配置手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[错误调试信息开关。当将策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[应用于接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的时候，输出如下]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[错误调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipsec error]{lang="EN-US"}]{#struct_0_x7538_x3345_1491761049}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipsec policy mypolicy]{lang="EN-US"}

[\*Jul 14 16:45:16:157 2012 Sysname IPSEC/7/ERROR: -MDC=1;]{lang="EN-US"}

[Failed to alloc SP index.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1086120885}*[分配]{style="font-family:宋体"}[SP]{lang="EN-US"}[索引失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562863}[在设备上配置手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[，并打开]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[事件调试开关。当将策略]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[应用于接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上时，会生成]{style="font-family:宋体"}[SP]{lang="EN-US"}[和]{style="font-family:宋体"}[SA]{lang="EN-US"}[，输出如下]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[事件调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipsec event]{lang="EN-US"}]{#struct_0_x7538_x3345_945343404}

[\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/event:]{lang="EN-US"}

[SP entry successfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1370722363}*[内核成功添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}*

[[\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1372267583}

[Sent add SP entry message to kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x123290607}*[向内核发送]{style="font-family:宋体"}[添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}[的消息]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:020 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_373227702}

[Added SP entry.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_490974855}*[添加]{style="font-family:宋体"}[SP entry]{lang="EN-US"}*

[[\*Jul 18 15:28:55:022 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_x837497327}

[SP successfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_264864964}*[内核成功添加]{style="font-family:宋体"}[SP]{lang="EN-US"}*

[[\*Jul 18 15:28:55:022 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_1806717197}

[Sent add SP message to kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1599962797}*[向内核发送添加]{style="font-family:宋体"}[SP]{lang="EN-US"}[的消息]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:023 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_x526704515}

[Added SP by policy.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_257830669}*[根据策略添加]{style="font-family:宋体"}[SP]{lang="EN-US"}*

[[\*Jul 18 15:28:55:024 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1139022963}

[Added policy SA by manual SP, SP index is 0, SP sequence number is 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_196277623}*[成功根据手工]{style="font-family:宋体"}[SP]{lang="EN-US"}[添加策略]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SP]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[SP]{lang="EN-US"}[序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_x837431791}

[IPsec tunnel added to aggregation-hash.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_641494527}*[向聚合哈希表中添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道成功]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_228476441}

[IPsec tunnel successfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1189428541}*[内核添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道成功]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:026 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_529256978}

[Added tunnel to kernel successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1993462125}*[向内核添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道成功]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:026 2012 HP IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366255}

[Added an IPsec tunnel when adding manual SA: tunnel index = 0, tunnel sequence number = 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1002633473}*[添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}[过程中添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道，隧道索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，隧道序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_517320454}

[SA succussfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1502017197}*[内核成功添加]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_1155891635}

[SA succussfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x301682833}*[内核成功添加]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_1471744107}

[Added outbound SA to IPsec tunnel(SA ID = 1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_405735186}*[成功向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道添加出方向]{style="font-family:宋体"}[SA]{lang="EN-US"}[（]{style="font-family:宋体"}[SA]{lang="EN-US"}[索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_x836776431}

[SA succussfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1372387715}*[内核成功添加]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/event:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1769309134}

[SA succussfully added in kernel.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x401574427}*[内核成功添加]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_1516487597}

[Added SA to kernel successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1715046076}*[成功向内核添加]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_793667807}

[Added manual SAs. Number of SAs added is 4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x836710895}*[成功添加手工]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的个数为]{style="font-family:宋体"}[4]{lang="EN-US"}*

[[\*Jul 18 15:28:55:027 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_251781823}

[No.1 SA: index = 3, sequence number = 2.]{lang="EN-US"}

[\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}

[No.2 SA: index = 2, sequence number = 2.]{lang="EN-US"}

[\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}

[No.3 SA: index = 1, sequence number = 2.]{lang="EN-US"}

[\*Jul 18 15:28:55:028 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}

[No.4 SA: index = 0, sequence number = 2.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1819188240}*[第一个]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x99702302}*[第二个]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1301530482}*[第三个]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x889183409}*[第四个]{style="font-family:宋体"}[SA]{lang="EN-US"}[的索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[SA]{lang="EN-US"}[的序号为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Jul 18 15:28:55:029 2012 Sysname IPSEC/7/ERROR:]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300722}

[Added SA context to SP.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x926817740}*[成功向]{style="font-family:宋体"}[SP]{lang="EN-US"}[添加]{style="font-family:宋体"}[SA]{lang="EN-US"}[上下文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x7538_x3345_1020038461}[在设备上配置手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，应用于接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上，并打开]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的报文调试信息开关。当从本机]{style="font-family:宋体"}[ping]{lang="EN-US"}[对端的时候，输出如下]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipsec packet]{lang="EN-US"}]{#struct_0_x7538_x3345_x1242507074}

[\<Sysname\> ping -c 1 10.10.10.2]{lang="EN-US"}

[PING 10.10.10.2 (10.10.10.2): 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}

[\-\-- Sent IPsec packet \-\--]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_938334779}*[出方向发送]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理的报文]{style="font-family:宋体"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_353956727}

[Added IP fast forwarding entry.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x837235186}*[添加快转表项]{style="font-family:宋体"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x537027870}

[Outbound IPsec processing: Src : 10.10.10.1 Dst : 10.10.10.2 SPI : 1114]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x789740580}*[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理：源地址：]{style="font-family:宋体"}[10.10.10.1]{lang="EN-US"}[，目的地址：]{style="font-family:宋体"}[10.10.10.2]{lang="EN-US"}[，]{style="font-family:宋体"}[SPI: 1114]{lang="EN-US"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_444220692}

[Outbound IPsec processing: ESP auth algorithm: SHA1, ESP encp algorithm: DES-CBC.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_484930421}*[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理：]{style="font-family:宋体"}[ESP]{lang="EN-US"}[认证算法为]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[，]{style="font-family:宋体"}[ESP]{lang="EN-US"}[加密算法为]{style="font-family:宋体"}[DES-CBC]{lang="EN-US"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x369337273}

[Packet will be sent to CCF for sync-encryption.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1560456921}*[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}[执行同步加密操作]{style="font-family:宋体"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x837169650}

[Outbound IPsec ESP processing: Encryption succeeded, anti-replay SN is 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x971566518}*[出方向]{style="font-family:宋体"}[IPsec ESP]{lang="EN-US"}[处理：加密完成，抗重放序号为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_1362476547}

[Outbound IPsec processing: AH auth algorithm: MD5.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x711455002}*[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理：]{style="font-family:宋体"}[AH]{lang="EN-US"}[认证算法为]{style="font-family:宋体"}[MD5]{lang="EN-US"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_488190061}

[Packet will be sent to CCF for sync-encryption.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1385930459}*[报文将被发送到]{style="font-family:宋体"}[CCF]{lang="EN-US"}[执行同步加密操作]{style="font-family:宋体"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_1870646033}

[Outbound IPsec AH processing: Authentication finished, anti-replay SN is 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x406327196}*[出方向]{style="font-family:宋体"}[IPsec AH]{lang="EN-US"}[处理：认证完成，抗重放序号为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Jul 14 16:55:10:211 2012 Sysname IPSEC/7/packet: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x837104114}

[Outbound IPsec processing: Sent packet back to IP forwarding.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2105012315}*[出方向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理：将报文重新发送给]{style="font-family:宋体"}[IP]{lang="EN-US"}[转发]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#-370055485 .myid}
[]{#_Toc404793069}[]{#struct_0_x7538_x3345_1980657241}[]{#_Toc333265151}[]{#_Toc130718952}[]{#_Toc87257691}

**IKE \-- IKE调试命令 \-- debugging ike**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1504236797}

[**[debugging ike ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x7538_x3345_x918811302}

[**[undo debugging ike ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_945146796}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x801762826}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x1969158063}

[[network-admin]{lang="EN-US"}]{#struct_0_x7538_x3345_x527858676}

[[vd-admin]{lang="EN-US"}]{#struct_0_x7538_x3345_x523786574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1263081541}

[**[all]{lang="EN-US"}**]{#struct_0_x7538_x3345_654166123}[：表示所有]{style="font-family:宋体"}[IKE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x7538_x3345_x1995269690}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x7538_x3345_x837497330}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x7538_x3345_264930499}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1804035150}

[**[debugging ike ]{lang="EN-US"}**]{#struct_0_x7538_x3345_x709203212}[命令用来打开]{style="font-family:宋体"}[IKE]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}**[undo debugging ike]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IKE]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1344439259}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_x7538_x3345_18860846}[[表2-1 ]{lang="EN-US"}[debugging ike error]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x514265028}[[字段]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1603025441}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x837431794}

[[Failed to verify the peer signature.]{lang="EN-US"}]{#struct_0_x7538_x3345_641691135}

[[对端签名验证失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1267495855}

[[HASH payload is missing.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1972921782}

[[未在]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1097501944}[报文中找到]{style="font-family:宋体"}[HASH]{lang="EN-US"}[载荷]{style="font-family:宋体"}

[[Failed to verify the peer HASH.]{lang="EN-US"}]{#struct_0_x7538_x3345_811715667}

[[对端]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366258}[验证失败]{style="font-family:宋体"}

[[Signature payload is missing.]{lang="EN-US"}]{#struct_0_x7538_x3345_1002436865}

[[未在]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_x836776434}[报文中找到签名载荷]{style="font-family:宋体"}

[[Invalid SPI length (*length*) in DPD packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_1372060035}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x168545016}[报文中的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Invalid I-Cookie in DPD packet: *I-Cookie*]{lang="EN-US"}]{#struct_0_x7538_x3345_549677101}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1105056694}[报文中的]{style="font-family:宋体"}[I-Cookie]{lang="EN-US"}[无效，]{style="font-family:宋体"}[I-Cookie]{lang="EN-US"}[的值为]{style="font-family:宋体"}*[I-Cookie]{lang="EN-US"}*

[[Invalid R-Cookie in DPD packet: *R-Cookie*]{lang="EN-US"}]{#struct_0_x7538_x3345_x836710898}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_252502719}[报文：]{style="font-family:宋体"}[R-Cookie]{lang="EN-US"}[无效，]{style="font-family:宋体"}[R-Cookie]{lang="EN-US"}[的值为]{style="font-family:宋体"}*[R-Cookie]{lang="EN-US"}*

[[The length (*length*) of DPD sequence number is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_x774851894}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x167342480}[序列号的长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Invalid DPD sequence number (*number*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300721}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x926752204}[序列号无效，序列号的值为]{style="font-family:宋体"}*[number]{lang="EN-US"}*

[[DPD packet retransmission timed out.]{lang="EN-US"}]{#struct_0_x7538_x3345_1801579185}

[[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1475755202}[报文的重传已超时]{style="font-family:宋体"}

[[Invalid IPv4 address length (*length*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x837235185}

[[无效的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_x536831262}[地址长度，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Invalid IPv6 address length (*length*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x1564447111}

[[无效的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_x1394236243}[地址长度，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Invalid ID of IPv4 address type: *ID-IPv4*]{lang="EN-US"}]{#struct_0_x7538_x3345_x837169649}

[[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_x972156343}[地址类型的身份无效，身份的值为]{style="font-family:宋体"}*[ID-IPv4]{lang="EN-US"}*

[[Invalid ID of IPv6 address type: *ID-IPv6*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1920025190}

[[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_x999811845}[地址类型的身份无效，身份的值为]{style="font-family:宋体"}*[ID-IPv6]{lang="EN-US"}*

[[Invalid FQDN ID length (*length*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x837104113}

[[FQDN]{lang="EN-US"}]{#struct_0_x7538_x3345_x2105471067}[类型的身份长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Invalid user FQDN ID length (*length*).]{lang="EN-US"}]{#struct_0_x7538_x3345_410822029}

[[User FQDN]{lang="EN-US"}]{#struct_0_x7538_x3345_265031458}[类型的长度身份无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Failed to get DN because the certificate doesn\'t exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562865}

[[获取]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x7538_x3345_944950188}[失败，因为证书不存在]{style="font-family:宋体"}

[[Failed to get ID data for constructing ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_749983214}

[[构造]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1705924349}[载荷时获取]{style="font-family:宋体"}[ID]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Invalid ID payload with protocol *protocol-number* and port *port-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837497329}

[[无效的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_264471748}[载荷，]{style="font-family:宋体"}[ID]{lang="EN-US"}[载荷中的协议号为]{style="font-family:宋体"}*[protocol-number]{lang="EN-US"}*[，端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*

[[Invalid ID type (*ID-type*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x998576090}

[[身份类型无效，身份类型值为]{style="font-family:宋体"}*[ID-type]{lang="EN-US"}*]{#struct_0_x7538_x3345_1867452229}

[[Failed to find proposal *proposal-number* in profile *profile-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837431793}

[[在名称为]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_641363455}[的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中没有找到编号为]{style="font-family:宋体"}*[proposal-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[proposal]{lang="EN-US"}

[[Failed to verify HASH for informational exchange.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2023835421}

[[验证]{style="font-family:宋体"}[informational exchange]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366257}[报文中的]{style="font-family:宋体"}[HASH]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to construct delete payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1002764545}

[[构造]{style="font-family:宋体"}[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x686361095}[载荷失败]{style="font-family:宋体"}

[[Invalid SPI length.]{lang="EN-US"}]{#struct_0_x7538_x3345_x836776433}

[[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_1372256643}[长度无效]{style="font-family:宋体"}

[[Protocol ID (*ID*) in delete payload is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1360006929}

[[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x836710897}[载荷中的协议]{style="font-family:宋体"}[ID]{lang="EN-US"}[无效，协议号为]{style="font-family:宋体"}*[ID]{lang="EN-US"}*

[[KE payload doesn't exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_251912895}

[[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_1996791063}[载荷不存在]{style="font-family:宋体"}

[[Invalid KE payload length (*length*).]{lang="EN-US"}]{#struct_0_x7538_x3345_1692263351}

[[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300724}[载荷的长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Failed to construct notification payload for keepalive.]{lang="EN-US"}]{#struct_0_x7538_x3345_x926424524}

[[发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_1043017454}[报文时构造]{style="font-family:宋体"}[notification]{lang="EN-US"}[载荷失败]{style="font-family:宋体"}

[[Length (*length*) of the sequence number in keepalive packet is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837235188}

[[Keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x536634654}[报文中的序列号长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Length (*length*) of the HASH payload in keepalive packet is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837169652}

[[Keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x971435446}[报文中的]{style="font-family:宋体"}[HASH]{lang="EN-US"}[载荷长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Failed to calculate HASH for verification of keepalive packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x180264876}

[[验证]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x837104116}[报文时，本端计算]{style="font-family:宋体"}[HASH]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add sequence number to keepalive packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2105143387}

[[构造]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x1069472565}[报文时，添加序列号失败]{style="font-family:宋体"}

[[Failed to calculate HASH for keepalive.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562868}

[[构造]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_944753580}[报文时，计算]{style="font-family:宋体"}[HASH]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to float port.]{lang="EN-US"}]{#struct_0_x7538_x3345_2119107466}

[[切换端口失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x837497332}

[[Length (*length*) of the nonce payload is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_265061571}

[[Nonce]{lang="EN-US"}]{#struct_0_x7538_x3345_x837431796}[载荷的长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Failed to parse the certificate request payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_641560063}

[[解析证书请求载荷失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1358502279}

[[No available proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366260}

[[没有找到可用的]{style="font-family:宋体"}[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_1002961154}

[[Failed to get certificate.]{lang="EN-US"}]{#struct_0_x7538_x3345_481662819}

[[获取证书失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x836776436}

[[Failed to get private key.]{lang="EN-US"}]{#struct_0_x7538_x3345_1371928963}

[[获取私钥失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x836710900}

[[Failed to construct ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1704336714}

[[构造]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1295962204}[身份载荷失败]{style="font-family:宋体"}

[[Failed to calculate *hash-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837300723}

[[计算]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x926883276}[失败，]{style="font-family:宋体"}[HASH]{lang="EN-US"}[名称为]{style="font-family:宋体"}*[hash-name]{lang="EN-US"}*

[[Failed to validate *hash-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_257712042}

[[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x837235187}[失败，]{style="font-family:宋体"}[HASH]{lang="EN-US"}[名称为]{style="font-family:宋体"}*[hash-name]{lang="EN-US"}*

[[Failed to compute key material.]{lang="EN-US"}]{#struct_0_x7538_x3345_x536962334}

[[计算密钥材料失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x837169651}

[[Failed to install IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x971632054}

[[安装]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x837104115}[失败]{style="font-family:宋体"}

[[The nonce payload doesn\'t exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2105077851}

[[Nonce]{lang="EN-US"}]{#struct_0_x7538_x3345_416571703}[载荷不存在]{style="font-family:宋体"}

[[The KE payload doesn\'t exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837562867}

[[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_945081260}[载荷不存在]{style="font-family:宋体"}

[[No valid DH group description in SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837497331}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_264996035}[载荷中没有有效的]{style="font-family:宋体"}[DH group]{lang="EN-US"}

[[There are too many KE payloads.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837431795}

[[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_641756671}[载荷太多，]{style="font-family:宋体"}

[[The length of the KE payload does\'t match the DH group description.]{lang="EN-US"}]{#struct_0_x7538_x3345_x837366259}

[[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_1002371329}[载荷的长度和用于]{style="font-family:宋体"}[PFS]{lang="EN-US"}[的]{style="font-family:宋体"}[DH group]{lang="EN-US"}[描述不匹配]{style="font-family:宋体"}

[[Failed to construct NAT-OA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x836776435}

[[构造]{style="font-family:宋体"}[NAT-OA]{lang="EN-US"}]{#struct_0_x7538_x3345_1372125571}[载荷失败]{style="font-family:宋体"}

[[Failed to construct RESPONDER_LIFETIME payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x836710899}

[[构造]{style="font-family:宋体"}[RESPONDER_LIFETIME]{lang="EN-US"}]{#struct_0_x7538_x3345_252568255}[载荷失败]{style="font-family:宋体"}

[[Failed to construct KE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x435089191}

[[构造]{style="font-family:宋体"}[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_728783221}[载荷失败]{style="font-family:宋体"}

[[Failed to pad for encryption.]{lang="EN-US"}]{#struct_0_x7538_x3345_1911584189}

[[加密报文前的填充失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_728848757}

[[Failed to send data. Reason: *error-reason.*]{lang="EN-US"}]{#struct_0_x7538_x3345_122731218}

[[发送报文失败，错误原因为]{style="font-family:宋体"}*[error-reason]{lang="EN-US"}*]{#struct_0_x7538_x3345_728914293}

[[No enough space in the packet for Non-ESP marker.]{lang="EN-US"}]{#struct_0_x7538_x3345_2067559578}

[[报文超大，不能添加]{style="font-family:宋体"}[Non-ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_728979829}[标记]{style="font-family:宋体"}

[[Failed to decrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x235685816}

[[解密报文失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_728521077}

[[Non-zero message ID (*Message-ID*) in phase 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_1992973743}

[[一阶段的]{style="font-family:宋体"}[Message ID]{lang="EN-US"}]{#struct_0_x7538_x3345_728586613}[不为]{style="font-family:宋体"}[0]{lang="EN-US"}[，其值为]{style="font-family:宋体"}*[Message-ID]{lang="EN-US"}*

[[I-Cookie must not be zero.]{lang="EN-US"}]{#struct_0_x7538_x3345_2002274343}

[[I-Cookie]{lang="EN-US"}]{#struct_0_x7538_x3345_728652149}[不能为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[The first packet of phase 1 is invalid: Encryption bit is set.]{lang="EN-US"}]{#struct_0_x7538_x3345_1869140461}

[[一阶段的第一条报文无效：报文的加密标识为已使能]{style="font-family:宋体"}]{#struct_0_x7538_x3345_728717685}

[[The first packet of phase 1 is invalid: Non-zero R-Cookie.]{lang="EN-US"}]{#struct_0_x7538_x3345_729307509}

[[一阶段的第一条报文无效：报文的]{style="font-family:宋体"}[R-Cookie]{lang="EN-US"}]{#struct_0_x7538_x3345_x481780481}[不为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Failed to parse phase 1 packet. Reason *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_729373045}

[[解析一阶段的]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_694828639}[报文失败，原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[，可能的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_PAYLOAD_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_728783222}[：载荷类型无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOI_NOT_SUPPORTED]{lang="EN-US"}]{#struct_0_x7538_x3345_1911584188}[：不支持的]{lang="EN-US" style="font-family:
  宋体"}[DOI]{lang="EN-US"}[字段]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SITUATION_NOT_SUPPORTED]{lang="EN-US"}]{#struct_0_x7538_x3345_728848758}[：不支持的]{lang="EN-US" style="font-family:宋体"}[situation]{lang="EN-US"}[字段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_COOKIE]{lang="EN-US"}]{#struct_0_x7538_x3345_122731217}[：]{lang="EN-US" style="font-family:宋体"}[cookie]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_MAJOR_VERSION]{lang="EN-US"}]{#struct_0_x7538_x3345_728914294}[：主版本号无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_MINOR_VERSION]{lang="EN-US"}]{#struct_0_x7538_x3345_2067559571}[：次版本号无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_EXCHANGE_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_728979830}[：交换类型无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_FLAGS]{lang="EN-US"}]{#struct_0_x7538_x3345_728521078}[：标识无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_MESSAGE_ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1992973746}[：]{lang="EN-US" style="font-family:
  宋体"}[message ID]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_PROTOCOL_ID]{lang="EN-US"}]{#struct_0_x7538_x3345_728586614}[：提议号无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_2002274350}[：]{lang="EN-US" style="font-family:宋体"}[SPI]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_TRANSFORM_ID]{lang="EN-US"}]{#struct_0_x7538_x3345_728652150}[：]{lang="EN-US" style="font-family:
  宋体"}[transform ID]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATTRIBUTES_NOT_SUPPORTED]{lang="EN-US"}]{#struct_0_x7538_x3345_x87174684}[：不支持的属性]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NO_PROPOSAL_CHOSEN]{lang="EN-US"}]{#struct_0_x7538_x3345_728717686}[：没有匹配的提议]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BAD_PROPOSAL_SYNTAX]{lang="EN-US"}]{#struct_0_x7538_x3345_729307510}[：提议语法错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PAYLOAD_MALFORMED]{lang="EN-US"}]{#struct_0_x7538_x3345_1474534648}[：载荷格式错误]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_KEY_INFORMATION]{lang="EN-US"}]{#struct_0_x7538_x3345_729373046}[：密钥信息无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_ID_INFORMATION]{lang="EN-US"}]{#struct_0_x7538_x3345_694828636}[：身份无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_CERT_ENCODING]{lang="EN-US"}]{#struct_0_x7538_x3345_728783219}[：证书编码无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_CERTIFICATE]{lang="EN-US"}]{#struct_0_x7538_x3345_728848755}[：证书无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CERT_TYPE_UNSUPPORTED]{lang="EN-US"}]{#struct_0_x7538_x3345_122731220}[：不支持的证书类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_CERT_AUTHORITY]{lang="EN-US"}]{#struct_0_x7538_x3345_728914291}[：证书认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_HASH_INFORMATION]{lang="EN-US"}]{#struct_0_x7538_x3345_2067559576}[：]{lang="EN-US" style="font-family:宋体"}[HASH]{lang="EN-US"}[无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTHENTICATION_FAILED]{lang="EN-US"}]{#struct_0_x7538_x3345_728979827}[：认证失败]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INVALID_SIGNATURE]{lang="EN-US"}]{#struct_0_x7538_x3345_728521075}[：签名无效]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADDRESS_NOTIFICATION]{lang="EN-US"}]{#struct_0_x7538_x3345_1992973741}[：地址通知]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NOTIFY_SA_LIFETIME]{lang="EN-US"}]{#struct_0_x7538_x3345_728586611}[：]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}[生命周期通知]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CERTIFICATE_UNAVAILABLE]{lang="EN-US"}]{#struct_0_x7538_x3345_2002274345}[：证书不可用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNSUPPORTED_EXCHANGE_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_728652147}[：不支持的交换类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNEQUAL_PAYLOAD_LENGTHS]{lang="EN-US"}]{#struct_0_x7538_x3345_728717683}[：载荷长度不相等]{lang="EN-US" style="font-family:宋体"}

[[The packet is dropped because of not being encrypted]{lang="EN-US"}]{#struct_0_x7538_x3345_1845249798}

[[丢弃报文，因为报文没有加密]{style="font-family:宋体"}]{#struct_0_x7538_x3345_729307507}

[[Failed to parse informational exchange packet. Reason *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_729373043}

[[解析]{style="font-family:宋体"}[informational exchange]{lang="EN-US"}]{#struct_0_x7538_x3345_694828641}[报文失败，原因是]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[*[reason]{lang="EN-US"}*]{#struct_0_x7538_x3345_728783220}[取值同上]{style="font-family:宋体"}

[[Failed to parse keepalive packet because of *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728848756}

[[解析]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_122731219}[报文失败，原因是]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[*[reason]{lang="EN-US"}*]{#struct_0_x7538_x3345_728914292}[取值同上]{style="font-family:宋体"}

[[Unsupported exchange type (*type*) in packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_2067559577}

[[不支持的交换类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x7538_x3345_728979828}[，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x7538_x3345_728521076}[：不存在的交换类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Base]{lang="EN-US"}]{#struct_0_x7538_x3345_1992973744}[：基础交换类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_x7538_x3345_728586612}[：主模式交换类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x7538_x3345_728652148}[O]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Authenticaton Only]{lang="EN-US"}[交换类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Aggressive]{lang="EN-US"}]{#struct_0_x7538_x3345_1869140460}[：野蛮模式交换类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Info]{lang="EN-US"}]{#struct_0_x7538_x3345_728717684}[：]{lang="EN-US" style="font-family:宋体"}[infomational exchange]{lang="EN-US"}[交换类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mode cfg]{lang="EN-US"}]{#struct_0_x7538_x3345_729307508}[：配置模式交换类型]{lang="EN-US" style="font-family:宋体"}

[[Invalid Non-ESP marker: *marker*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x481780480}

[[无效的]{style="font-family:宋体"}[Non-ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_729373044}[标识：]{style="font-family:宋体"}*[marker]{lang="EN-US"}*

[[The received packet is too short, which is *length* bytes.]{lang="EN-US"}]{#struct_0_x7538_x3345_728783217}

[[收到报文的长度太小，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x7538_x3345_x44730945}

[[Failed to receive packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_728848753}

[[接收报文失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_728914289}

[[Failed to bind UDP port *port-number*. Reason: *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_111244448}

[[绑定]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_728979825}[端口失败，端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[，错误原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[[Failed to set UDP port *port-number*. Reason: *reason*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728521073}

[[设置]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_1992973739}[端口失败，端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[，错误原因为]{style="font-family:宋体"}*[reason]{lang="EN-US"}*

[[Failed to add UDP port *port-number* to epoll.]{lang="EN-US"}]{#struct_0_x7538_x3345_728586609}

[[添加]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_728652145}[端口到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败，端口号为：]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*

[[Failed to initiate UDP port *port-number*. Error code: *error-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728717681}

[[初始化]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_1845249796}[端口失败，端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[error-number]{lang="EN-US"}*

[*[byte-number]{lang="EN-US"}*[th byte of the structure *struct-name* must be 0.]{lang="EN-US"}]{#struct_0_x7538_x3345_729307505}

[[结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_729373041}[的第]{style="font-family:宋体"}*[byte-number]{lang="EN-US"}*[个字节必须为]{style="font-family:宋体"}[0 ]{lang="EN-US"}

[*[Field-name]{lang="EN-US"}*[ of *struct-name* has an unknown value: *value*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728783218}

[[结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_x44730954}[的域]{style="font-family:宋体"}*[field-name]{lang="EN-US"}*[的值]{style="font-family:宋体"}*[value]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[*[field-name]{lang="EN-US"}*[ of *struct-name* has unknown members.]{lang="EN-US"}]{#struct_0_x7538_x3345_728848754}

[[结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_728914290}[的域]{style="font-family:宋体"}*[field-name]{lang="EN-US"}*[包含未知的成员]{style="font-family:宋体"}

[[No enough bytes to get *data2* from *data1*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728979826}

[[没有足够的空间来保存从数据]{style="font-family:宋体"}*[data1]{lang="EN-US"}*]{#struct_0_x7538_x3345_x235685815}[中获取的数据]{style="font-family:宋体"}*[data2]{lang="EN-US"}*

[[No enough space in output packet for *struct-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728521074}

[[报文中没有足够的空间用于保存结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_728586610}

[[No enough space to place *length* bytes of *data-name* in *struct-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_728652146}

[[结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_1869140458}[中没有足够的空间用于保存]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[No enough space to place *data-name* in *struct-name.*]{lang="EN-US"}]{#struct_0_x7538_x3345_728717682}

[[结构]{style="font-family:宋体"}*[struct-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_729307506}[中没有足够的空间保存数据]{style="font-family:宋体"}*[data-name]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Failed to add the HASH payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_729373042}

[[添加]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869774}[载荷失败]{style="font-family:宋体"}

[[Ignored the certificate request of type *type-id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_310806217}

[[忽略证书请求，证书请求的类型为]{style="font-family:宋体"}*[type-id]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1643804238}

[[Failed to get the certificate and key by certificate request.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738702}

[[根据证书请求获取证书和密钥失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1643673166}

[[Failed to verify the peer certificate. Reason: *error-string*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131918}

[[验证对端证书失败，错误原因为]{style="font-family:宋体"}*[error-string]{lang="EN-US"}*]{#struct_0_x7538_x3345_x137927531}

[[Failed to find keychain *keychain-name* in profile *profile-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066382}

[[在]{style="font-family:宋体"}[IKE profile *profile-name*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644000846}[中查找]{style="font-family:宋体"}[keychain *keychain-name*]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to create IKE SA with core data.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935310}

[[根据核心数据创建一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345486}[失败]{style="font-family:宋体"}

[[Failed to create IPsec SA with core data.]{lang="EN-US"}]{#struct_0_x7538_x3345_1797140130}

[[根据核心数据创建二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279950}[失败]{style="font-family:宋体"}

[[Failed to receive smooth SA ACK from IPsec.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869773}

[[从]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643804237}[接收]{style="font-family:宋体"}[SA]{lang="EN-US"}[平滑处理的应答失败]{style="font-family:宋体"}

[[Number of negotiating IKE SAs exceeded the limit.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738701}

[[正在协商的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643673165}[的数目超出限制]{style="font-family:宋体"}

[[Number of established IKE SAs exceeded the limit.]{lang="EN-US"}]{#struct_0_x7538_x3345_x741483367}

[[已经建立的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131917}[的数目超出限制]{style="font-family:宋体"}

[[Attribute *attribute-name* is repeated.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066381}

[[属性重复，属性名称为]{style="font-family:宋体"}*[attribute-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1644000845}

[[Failed to construct situation.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935309}

[[构造]{style="font-family:宋体"}[situaton]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345485}[字段失败]{style="font-family:宋体"}

[[Failed to construct proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279949}

[[构造]{style="font-family:宋体"}[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869776}[载荷失败]{style="font-family:宋体"}

[[Failed to construct transform payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1473605631}

[[构造]{style="font-family:宋体"}[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643804240}[载荷失败]{style="font-family:宋体"}

[[Failed to construct attributes.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738704}

[[构造属性失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1643673168}

[[Unsupported DOI *doi*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131920}

[[不支持的]{style="font-family:宋体"}[DOI *doi*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066384}

[[Proposal payload must be the last payload in SA payload, but *payload-name* payload is found following proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644000848}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935312}[载荷必须是]{style="font-family:宋体"}[SA]{lang="EN-US"}[载荷中的最后一个载荷，但在]{style="font-family:宋体"}[proposal]{lang="EN-US"}[载荷之后还有]{style="font-family:宋体"}*[payload-name]{lang="EN-US"}*[载荷]{style="font-family:宋体"}

[[Unexpected protocol ID (*ID-type*) found in proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345488}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279952}[载荷中的协议]{style="font-family:宋体"}[ID]{lang="EN-US"}[无效，协议]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}*[ID-type]{lang="EN-US"}*

[[Invalid SPI length (*SPI-length*) in proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869775}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643804239}[载荷中的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[长度无效]{style="font-family:宋体"}

[[No transform payload in proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1410813725}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738703}[载荷中没有]{style="font-family:宋体"}[transform]{lang="EN-US"}[载荷]{style="font-family:宋体"}

[[Transform number is not monotonically increasing.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643673167}

[[Transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131919}[号不是单调递增的]{style="font-family:宋体"}

[[Invalid transform ID: *id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066383}

[[无效的]{style="font-family:宋体"}[transform ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644000847}[：]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[No acceptable transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935311}

[[没有可以接受的]{style="font-family:宋体"}[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345487}

[[Unexpected *payload-name* payload in proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279951}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869778}[载荷中有不期望出现的载荷]{style="font-family:宋体"}*[payload-name]{lang="EN-US"}*

[[Only one transform is permitted in one proposal, but *trans-count* transforms are found.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643804242}

[[在选中的]{style="font-family:宋体"}[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738706}[载荷中只允许有一个]{style="font-family:宋体"}[transform]{lang="EN-US"}[，但实际有]{style="font-family:宋体"}*[trans-count]{lang="EN-US"}*[个]{style="font-family:宋体"}

[[Failed to parse the IKE SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643673170}

[[解析]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1500932718}[载荷失败]{style="font-family:宋体"}

[[Proposal payload has more transforms than specified in the proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131922}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066386}[载荷中的]{style="font-family:宋体"}[transform]{lang="EN-US"}[载荷数量比]{style="font-family:宋体"}[proposal]{lang="EN-US"}[载荷中指定的数量多]{style="font-family:宋体"}

[[Proposal payload has fewer transforms than specified in the proposal payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644000850}

[[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935314}[载荷中的]{style="font-family:宋体"}[transform]{lang="EN-US"}[载荷数量比]{style="font-family:宋体"}[proposal]{lang="EN-US"}[载荷中指定的数量少]{style="font-family:宋体"}

[[Invalid next payload (*payload-type*) in transform payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345490}

[[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279954}[载荷中的]{style="font-family:宋体"}[next payload]{lang="EN-US"}[字段无效，载荷类型为]{style="font-family:宋体"}*[payload-type]{lang="EN-US"}*

[[SA_LIFE_TYPE attribute must be in front of the SA_LIFE_DURATION attribute.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643869777}

[[SA_LIFE_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643804241}[属性必须在]{style="font-family:宋体"}[SA_LIFE_DURATION]{lang="EN-US"}[属性前面]{style="font-family:宋体"}

[[Attribute *attribute-type* is repeated in IPsec transform *trans-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643738705}

[[属性类型为的]{style="font-family:宋体"}*[attribute-type]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1643673169}[属性在]{style="font-family:宋体"}[IPsec transform]{lang="EN-US"}[中重复，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*

[[SA_LIFE_TYPE attribute is repeated in packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644131921}

[[属性]{style="font-family:宋体"}[SA_LIFE_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644066385}[在报文中重复]{style="font-family:宋体"}

[[Unsupported IPsec attribute *attribute*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1644000849}

[[不支持的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643935313}[属性]{style="font-family:宋体"}*[attribute]{lang="EN-US"}*

[[SA_LIFE_TYPE IPsec attribute not followed by SA_LIFE_DURATION attribute in message.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643345489}

[[报文中的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643279953}[属性]{style="font-family:宋体"}[SA_LIFE_TYPE]{lang="EN-US"}[后面没有]{style="font-family:宋体"}[SA_LIFE_DURATION]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Encapsulation mode must be specified in IPsec transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785833}

[[IPsec transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x77720297}[中必须指定封装模式]{style="font-family:宋体"}

[[AUTH_ALGORITHM attribute is missing in AH transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77654761}

[[在]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x7538_x3345_x77589225}[协议的]{style="font-family:宋体"}[transform]{lang="EN-US"}[中没有]{style="font-family:宋体"}[AUTH_ALGORITHM]{lang="EN-US"}[属性]{style="font-family:宋体"}

[[Transform ID (*id*) in transform *trans-number* doesn\'t match authentication algorithm *auth-algo-name* (*auth-algo-value*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047977}

[[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x77982441}[中的]{style="font-family:宋体"}[transform ID]{lang="EN-US"}[和认证算法不匹配，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[transform ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，认证算法为]{style="font-family:宋体"}*[auth-algo-name]{lang="EN-US"}*[，其值为]{style="font-family:宋体"}*[auth-algo-value]{lang="EN-US"}*

[[Neither encryption algorithm nor authentication algorithm is specified in ESP proposal, which is not permitted.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916905}

[[ESP proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851369}[中既没有加密算法也没有认证算法，这是不允许的]{style="font-family:宋体"}

[[Unsupported ESP transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77261545}

[[不支持的]{style="font-family:宋体"}[ESP transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196009}

[[Unsupported ESP authentication algorithm.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785832}

[[不支持的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x7538_x3345_x77720296}[认证算法]{style="font-family:宋体"}

[[IPsec proposal with improper SPI size (*size*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x77654760}

[[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77589224}[中的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[大小错误，]{style="font-family:宋体"}[SPI]{lang="EN-US"}[大小为]{style="font-family:宋体"}*[size]{lang="EN-US"}*

[[IPsec proposal contains invalid SPI (*SPI*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047976}

[[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916904}[中的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[无效，其值为]{style="font-family:宋体"}*[SPI]{lang="EN-US"}*

[[Failed to get SPI from IPsec proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851368}

[[从]{style="font-family:宋体"}[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77261544}[中获取]{style="font-family:宋体"}[SPI]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[No transform in IPsec proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196008}

[[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785835}[中没有]{style="font-family:宋体"}[transform]{lang="EN-US"}

[[SA payload contains more than one AH proposal with the same proposal number.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77720299}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x77654763}[载荷中有多个]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议的]{style="font-family:宋体"}[proposal]{lang="EN-US"}[对应同一个]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号]{style="font-family:宋体"}

[[SA payload contains more than one ESP proposal with the same proposal number.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77589227}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047979}[载荷中有多个]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[proposal]{lang="EN-US"}[对应同一个]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Invalid next payload (*payload-type-num*) in proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77982443}

[[Proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916907}[载荷中的]{style="font-family:宋体"}[next payload]{lang="EN-US"}[字段无效，其类型值为]{style="font-family:宋体"}*[payload-type-num]{lang="EN-US"}*

[[Unsupported IPsec DOI situation (*situation-num*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851371}

[[不支持的]{style="font-family:宋体"}[IPsec DOI situation]{lang="EN-US"}]{#struct_0_x7538_x3345_x77261547}[，其类型值为]{style="font-family:宋体"}*[situation-num]{lang="EN-US"}*

[[Invalid IPsec proposal *proposal-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196011}

[[无效的]{style="font-family:宋体"}[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785834}[，]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号为]{style="font-family:宋体"}*[proposal-number]{lang="EN-US"}*

[[Failed to get IPsec policy when renegotiating IPsec SA. Delete IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77720298}

[[在重协商]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x77589226}[时获取]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[策略失败，删除]{style="font-family:宋体"}[ IPsec SA]{lang="EN-US"}

[[Failed to get IPsec policy for phase 2 responder. Delete IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047978}

[[作为二阶段协商的响应方时，获取]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x77982442}[策略失败，删除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}

[[No HASH in notification payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916906}

[[在]{style="font-family:宋体"}[notification]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851370}[载荷中没有]{style="font-family:宋体"}[HASH]{lang="EN-US"}

[[Failed to send message to IPsec when getting SPI.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77261546}

[[获取]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196010}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when adding SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785837}

[[添加]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x77720301}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when deleting SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77654765}

[[删除]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047981}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when getting SP.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77982445}

[[获取]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916909}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when adding DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851373}

[[添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x77261549}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when updating DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196013}

[[升级]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x77785836}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when deleting DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77654764}

[[删除]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_x77589228}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to send message to IPsec when switching SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x78047980}

[[切换]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x77982444}[时向]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[发消息失败]{style="font-family:宋体"}

[[Failed to negotiate IKE SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77916908}

[[协商]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x77851372}[失败]{style="font-family:宋体"}

[[Failed to negotiate IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x77196012}

[[协商]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010782502}[失败]{style="font-family:宋体"}

[*[Errstring]{lang="EN-US"}*[. Attribute *attribute-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010848038}

[[错误原因为]{style="font-family:宋体"}*[errstring]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2010651430}[。相关的属性名称为]{style="font-family:宋体"}*[attribute-name]{lang="EN-US"}*

[*[Errstring]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2010716966}[的内容包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported encryption algorithm: enc-alg]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520358}[：不支持的加密算法]{lang="EN-US" style="font-family:宋体"}[enc-alg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported HASH algorithm: hash-alg]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010389286}[：不支持的]{lang="EN-US" style="font-family:宋体"}[HASH]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}[hash-alg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported authentication method: auth-meth]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010454822}[：不支持的认证方法]{lang="EN-US" style="font-family:宋体"}[auth-meth]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported DH group: group-name]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010258214}[：不支持的]{lang="EN-US" style="font-family:宋体"}[DH group group-name]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported lifetime type: lifetime-type]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010323750}[：不支持的生命周期类型]{lang="EN-US" style="font-family:宋体"}[lifetime-type]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAKLEY_LIFE_DURATION attribute not preceded by OAKLEY_LIFE_TYPE attribute.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010782501}[：]{lang="EN-US" style="font-family:宋体"}[OAKLEY_LIFE_DURATION]{lang="EN-US"}[属性没有在]{lang="EN-US" style="font-family:
  宋体"}[OAKLEY_LIFE_TYPE]{lang="EN-US"}[属性之前]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAKLEY_KEY_LENGTH attribute not preceded by OAKLEY_ENCRYPTION_ALGORITHM attribute]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010651429}[：]{lang="EN-US" style="font-family:宋体"}[OAKLEY_KEY_LENGTH]{lang="EN-US"}[属性没有在]{lang="EN-US" style="font-family:宋体"}[OAKLEY_ENCRYPTION_ALGORITHM]{lang="EN-US"}[属性之前]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAKLEY_KEY_LENGTH attribute not match OAKLEY_ENCRYPTION_ALGORITHM.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010716965}[：]{lang="EN-US" style="font-family:宋体"}[OAKLEY_KEY_LENGTH]{lang="EN-US"}[属性和]{lang="EN-US" style="font-family:宋体"}[OAKLEY_ENCRYPTION_ALGORITHM]{lang="EN-US"}[属性不匹配]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed to get encryption algorithm]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520357}[：获取加密算法失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsupported OAKLEY attribute attribute]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010585893}[：不支持的]{lang="EN-US" style="font-family:宋体"}[OAKLEY]{lang="EN-US"}[属性]{lang="EN-US" style="font-family:宋体"}[attribute]{lang="EN-US"}

[[Failed to match the proposal.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010389285}

[[匹配]{style="font-family:宋体"}[proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010258213}[失败]{style="font-family:宋体"}

[]{#_Toc130718927}[[Received invalid SPI message from IPsec, but no IKE SA exists.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010323749}

[[收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010782504}[的]{style="font-family:宋体"}[invalid SPI]{lang="EN-US"}[消息，但是没有]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}

[[Failed to get subject name from certificate.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010848040}

[[从证书中获取主题名失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2010651432}

[[Failed to get local certificate.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520360}

[[获取本地证书失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2010585896}

[[Failed to send notification packet for deleting IPsec SA, because of no corresponding IKE SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010389288}

[[删除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010454824}[时发送]{style="font-family:宋体"}[notification]{lang="EN-US"}[报文失败，因为没有找到对应的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}

[[Failed to construct certificate request payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010323752}

[[构造证书请求载荷失败]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2010782503}

[[Unsupported attribute *attribute-type*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010848039}

[[不支持的属性，属性类型为]{style="font-family:宋体"}*[attribute-type]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2010651431}

[[Invalid major version(*version*).]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520359}

[[主版本号无效，主版本号为]{style="font-family:宋体"}*[version]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2010585895}

[ ]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[debugging ike event]{lang="EN-US"}]{#struct_0_x7538_x3345_x1440967048}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x459309956}[[字段]{style="font-family:黑体"}]{#struct_0_x7538_x3345_x562810863}

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1139417541}

[[Signature verification succeeded.]{lang="EN-US"}]{#struct_0_x7538_x3345_x254626110}

[[验证签名成功]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2010389287}

[[HASH verification succeeded.]{lang="EN-US"}]{#struct_0_x7538_x3345_269254584}

[[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_1225173539}[成功]{style="font-family:宋体"}

[[Delete IPsec SAs.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1635020399}

[[删除]{style="font-family:宋体"}[IPsecSA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1285045992}

[[Delete IKE SA with connection ID *id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010454823}

[[删除]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x269322317}[，]{style="font-family:宋体"}[connection ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Update DPD configuration in IKE SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x138868198}

[[更新一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_62883830}[中的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[Notify IPsec to add DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_274002482}

[[通知]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010258215}[添加]{style="font-family:宋体"}[DPD]{lang="EN-US"}

[[Notify IPsec to delete DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_x527551649}

[[通知]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_1847883223}[删除]{style="font-family:宋体"}[DPD]{lang="EN-US"}

[[Notify IPsec to update DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2121413067}

[[通知]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1297193057}[更新]{style="font-family:宋体"}[DPD]{lang="EN-US"}

[[Process interface *interface-type interface-num* active event.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010323751}

[[处理接口激活事件，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x7538_x3345_1505106203}

[[Process interface *interface-name* deactive event.]{lang="EN-US"}]{#struct_0_x7538_x3345_1823935744}

[[处理接口去激活事件，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x7538_x3345_x831269652}

[[Process interface *interface-name* delete event.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010782506}

[[处理接口删除事件，接口名为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*]{#struct_0_x7538_x3345_1517220940}

[[The board chassis *chassis-num* slot *slot-num* is inserted.]{lang="EN-US"}]{#struct_0_x7538_x3345_1045628266}

[[单板插入]{style="font-family:宋体"}*[chassic-number]{lang="EN-US"}*]{#struct_0_x7538_x3345_944105574}[号成员设备的]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[号槽位中]{style="font-family:宋体"}

[[Protocol/port in phase 1 ID payload is *protocol-number*/*port-number*, which is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010848042}

[[一阶段]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1440720593}[载荷中的协议号]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号为]{style="font-family:宋体"}*[protocol-number]{lang="EN-US"}*[/*port-number*]{lang="EN-US"}[，它们是可接受的]{style="font-family:宋体"}

[[Begin to construct IPsec SA delete packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_174146414}

[[开始构造二阶段]{style="font-family:宋体"}[SA delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010651434}[报文]{style="font-family:宋体"}

[[Delete IKE SA with connection ID *id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_92520126}

[[删除一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1490211578}[，]{style="font-family:宋体"}[connection ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Received IPsec SA delete packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x239254279}

[[收到二阶段]{style="font-family:宋体"}[SA delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010716970}[报文]{style="font-family:宋体"}

[[Process delete payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1535914911}

[[处理]{style="font-family:宋体"}[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x1701417298}[载荷]{style="font-family:宋体"}

[[Ignore delete payload: packet not encrypted or IKE SA not established.]{lang="EN-US"}]{#struct_0_x7538_x3345_815877304}

[[忽略]{style="font-family:宋体"}[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520362}[载荷：报文没有加密或者一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[没有建立]{style="font-family:宋体"}

[[Received SA acquire message from IPsec.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1103059836}

[[收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x2037931736}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求消息]{style="font-family:宋体"}

[[Received IPsec capability.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010585898}

[[收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_x1037682521}[规格]{style="font-family:宋体"}

[[Received smooth IPsec SA ACK.]{lang="EN-US"}]{#struct_0_x7538_x3345_668625392}

[[收到平滑]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_471983377}[的应答]{style="font-family:宋体"}

[[IKE keepalive timed out. Delete IKE SA with connection ID *id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010389290}

[[IKE Keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x133964407}[定时器超时，删除一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[，]{style="font-family:宋体"}[connection ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Reset IKE keepalive timeout timer. New time value is *time*]{lang="EN-US"}]{#struct_0_x7538_x3345_x246607732}

[[重置]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010454826}[超时定时器，新的时间值为]{style="font-family:宋体"}*[time]{lang="EN-US"}*

[[I am behind NAT.]{lang="EN-US"}]{#struct_0_x7538_x3345_x672606844}

[[我在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7538_x3345_1709882982}[设备之后]{style="font-family:宋体"}

[[Peer is behind NAT.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010258218}

[[对端在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7538_x3345_x1643296896}[设备之后]{style="font-family:宋体"}

[[No need to float port.]{lang="EN-US"}]{#struct_0_x7538_x3345_343527433}

[[不需要切换端口]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x2010323754}

[[Float port to local port *local-port* and remote port *remote-port*]{lang="EN-US"}]{#struct_0_x7538_x3345_x2030346206}

[[切换端口，本端端口为]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1601406657}[，对端端口为]{style="font-family:宋体"}*[remote-port]{lang="EN-US"}*

[[Sending DPD packet of type *type* with sequence number *seq-no*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010782505}

[[发送]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x7538_x3345_1920505467}[类型的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文，序列号为]{style="font-family:宋体"}*[seq-no]{lang="EN-US"}*

[[Delete IKE SA by received notification.]{lang="EN-US"}]{#struct_0_x7538_x3345_x903293594}

[[根据错误通知报文删除一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010848041}

[[INITIAL-CONTACT message is dropped because of not being encrypted.]{lang="EN-US"}]{#struct_0_x7538_x3345_1844005120}

[[INITIAL-CONTACT]{lang="EN-US"}]{#struct_0_x7538_x3345_x1632115193}[未加密，丢弃它]{style="font-family:宋体"}

[[Delete redundant SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010651433}

[[删除多余的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010716969}

[[Length (*length*) of notification packet is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_1549133268}

[[notification]{lang="EN-US"}]{#struct_0_x7538_x3345_x1767977183}[报文的长度无效，长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Protocol-ID (*ID*) of notification packet is unsupported.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010520361}

[[不支持]{style="font-family:宋体"}[notification]{lang="EN-US"}]{#struct_0_x7538_x3345_1625823519}[报文中的协议号：]{style="font-family:宋体"}*[ID]{lang="EN-US"}*

[[Notification *notification-name* is received.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1908895575}

[[收到通知报文]{style="font-family:宋体"}*[notification-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2010585897}

[[Inbound flow: *dst-addr-\>src-addr*]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010389289}

[[入方向流量：目的地址]{style="font-family:宋体"}[-\>]{lang="EN-US"}]{#struct_0_x7538_x3345_1075823638}[源地址]{style="font-family:宋体"}

[[Outbound flow: *src-addr-\>dst-addr*]{lang="EN-US"}]{#struct_0_x7538_x3345_807184539}

[[出方向流量：源地址]{style="font-family:宋体"}[-\>]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010454825}[目的地址]{style="font-family:宋体"}

[[Validated *hash-name* successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010258217}

[[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x1690351063}[成功，]{style="font-family:宋体"}[HASH]{lang="EN-US"}[名称为]{style="font-family:宋体"}*[hash-name]{lang="EN-US"}*

[[Getting IPsec message timed out. Delete IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2010323753}

[[获取]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x7538_x3345_342306789}[消息超时，删除二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}

[[Protocol: *protocol*]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698561}

[[安全协议为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1714702742}[（]{style="font-family:宋体"}[AH]{lang="EN-US"}[或]{style="font-family:宋体"}[ESP]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Inbound SPI: *in-spi*]{lang="EN-US"}]{#struct_0_x7538_x3345_x444764097}

[[入方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_1113997070}[值为]{style="font-family:宋体"}*[in-spi]{lang="EN-US"}*

[[Outbound SPI: *out-spi*]{lang="EN-US"}]{#struct_0_x7538_x3345_10778780}

[[出方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x7538_x3345_x444567489}[值为]{style="font-family:宋体"}*[out-spi]{lang="EN-US"}*

[[Install IPsec SAs.]{lang="EN-US"}]{#struct_0_x7538_x3345_x851129808}

[[下发]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444633025}

[[Lifetime in seconds: *seconds*]{lang="EN-US"}]{#struct_0_x7538_x3345_699505907}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444436417}[的生命周期为]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Lifetime in kilobytes: *bytes*]{lang="EN-US"}]{#struct_0_x7538_x3345_704533931}

[[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1332953955}[的生命周期为]{style="font-family:宋体"}*[bytes]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Phase 2 Exchange chooses role: Local is initiator.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444501953}

[[二阶段协商选择角色：本端为发起方]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1617001009}

[[Phase 2 Exchange chooses role: Local is responder.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305345}

[[二阶段协商选择角色：本端为响应方]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1499247392}

[[Begin Quick mode exchange.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370881}

[[开始进行快速模式协商过程]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1907953909}

[[No enough space to send packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174273}

[[没有足够的空间来发送报文]{style="font-family:宋体"}]{#struct_0_x7538_x3345_729235034}

[[Retransmittion of phase 1 packet timed out.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239809}

[[重传一阶段报文超时]{style="font-family:宋体"}]{#struct_0_x7538_x3345_689973791}

[[Ignore phase 1 packet retransmit timeout event.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698560}

[[忽略一阶段报文重传超时事件]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1714768278}

[[Retransmittion of  phase 2 packet timed out.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1828822484}

[[重传二阶段报文超时]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x444764096}

[[Ignore phase 2 packet retransmit timeout event.]{lang="EN-US"}]{#struct_0_x7538_x3345_1114062606}

[[忽略二阶段报文重传超时事件]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x444567488}

[[Phase 1 Exchange chooses role: Local is initiator.]{lang="EN-US"}]{#struct_0_x7538_x3345_x851064272}

[[一阶段协商选择角色：本端为发起方]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x444633024}

[[Phase 1 Exchange chooses role: Local is responder.]{lang="EN-US"}]{#struct_0_x7538_x3345_699440371}

[[一阶段协商选择角色：本端为响应方]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x444436416}

[[Phase 1 packet is malformed: Not starting with an SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444501952}

[[一阶段报文格式错误：没有以]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1616935473}[载荷开始]{style="font-family:宋体"}

[[Phase2 packet is malformed: Not starting with an HASH payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305344}

[[二阶段报文格式错误：没有以]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_1499312928}[载荷开始]{style="font-family:宋体"}

[[Quick mode packet is received, but IKE SA does not exist.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370880}

[[收到快速模式的报文，但一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1907888373}[不存在]{style="font-family:宋体"}

[[Quick mode packet is received, but IKE SA is incomplete.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174272}

[[收到快速模式的报文，但一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_729169498}[不完整]{style="font-family:宋体"}

[[Ignored delete SA payload because the IKE SA is not established.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239808}

[[忽略删除]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698563}[的报文，因为]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Ignored delete SA payload because the packet is not encrypted.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1714571670}

[[忽略删除]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444764099}[的报文，因为报文没有加密]{style="font-family:宋体"}

[[Received informational exchange packet, but IKE SA is inexistent or incomplete.]{lang="EN-US"}]{#struct_0_x7538_x3345_1113079566}

[[收到]{style="font-family:宋体"}[information exchange]{lang="EN-US"}]{#struct_0_x7538_x3345_x444567491}[报文，但是一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[不存在或者不完整]{style="font-family:宋体"}

[[Received keepalive packet, but IKE SA is not existed.]{lang="EN-US"}]{#struct_0_x7538_x3345_x850605519}

[[收到]{style="font-family:宋体"}[IKE keepaclive]{lang="EN-US"}]{#struct_0_x7538_x3345_x444633027}[报文，但是一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Received keepalive packet, but it is not encrypted.]{lang="EN-US"}]{#struct_0_x7538_x3345_699374835}

[[收到]{style="font-family:宋体"}[IKE keepaclive]{lang="EN-US"}]{#struct_0_x7538_x3345_x444436419}[报文，但是它没有加密]{style="font-family:宋体"}

[[Received keepalive packet, but IKE SA is incomplete.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444501955}

[[收到]{style="font-family:宋体"}[IKE keepaclive]{lang="EN-US"}]{#struct_0_x7538_x3345_x1617132081}[报文，但是一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[不完整]{style="font-family:宋体"}

[[Ignore NAT keepalive packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305347}

[[忽略]{style="font-family:宋体"}[NAT keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_1499116320}[报文]{style="font-family:宋体"}

[[Initialize UDP port.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370883}

[[初始化]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_1907822837}[端口]{style="font-family:宋体"}

[[PKI data had been changed.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174275}

[[PKI]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239811}[数据已经有所变化]{style="font-family:宋体"}

[[Found pre-shared key that matches address *address* in keychain *keychain-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_689449502}

[[在]{style="font-family:宋体"}[keychain *keychain-name*]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698562}[中找到了预共享密钥，该预共享密钥与地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*[匹配]{style="font-family:宋体"}

[[Pre-shared key matching address *address* not found.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1714637206}

[[根据地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x7538_x3345_x444764098}[无法找到匹配的预共享密钥]{style="font-family:宋体"}

[[Found keychain *keychain-name* in profile *profile-name* successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444567490}

[[成功在]{style="font-family:宋体"}[IKE profile *profile-name*]{lang="EN-US"}]{#struct_0_x7538_x3345_x850539983}[中找到]{style="font-family:宋体"}[keychain *keychain-name*]{lang="EN-US"}

[[Get profile *profile-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444633026}

[[获取]{style="font-family:宋体"}[IKE profile *profile-name*]{lang="EN-US"}]{#struct_0_x7538_x3345_699309299}

[[Initiator created an SA for peer *address*, local port *local-port*, remote port *remote-port*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444436418}

[[发起方创建]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444501954}[，对端地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[，本端端口为]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*[，对端端口为]{style="font-family:宋体"}*[remote-port]{lang="EN-US"}*

[[Set IKE SA state to *state-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1617066545}

[[设置一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305346}[状态为]{style="font-family:宋体"}*[state-name]{lang="EN-US"}*

[[IKE SA state changed from *state1* to *state2*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1499181856}

[[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370882}[状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[转换到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[Set IPsec SA state to *state-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174274}

[[设置二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_729562714}[状态为]{style="font-family:宋体"}*[state-name]{lang="EN-US"}*

[[IPsec SA state changed from *state1* to *state2*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239810}

[[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698565}[状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[转换到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[Responder created an SA for peer *address*, local port *local-port*, remote port *remote-port*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1714440598}

[[发起方创建]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444764101}[，对端地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*[，本端端口为]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*[，对端端口为]{style="font-family:宋体"}*[remote-port]{lang="EN-US"}*

[[Delete IPsec SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444567493}

[[删除二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x850474447}

[[Oakley transform *trans-number* is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444633029}

[[Oakley transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x444436421}[是可接受的，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*

[[Begin *mode* mode exchange.]{lang="EN-US"}]{#struct_0_x7538_x3345_704927150}

[[开始]{style="font-family:宋体"}*[mode]{lang="EN-US"}*]{#struct_0_x7538_x3345_x444501957}[模式的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商]{style="font-family:宋体"}

[[IKE SA not found. Initiate IKE SA negotiation.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305349}

[[没有一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1500033824}[，发起一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[的协商]{style="font-family:宋体"}

[[IKE SA is prepared for renegotiation.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370885}

[[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174277}[已经准备好进行重协商]{style="font-family:宋体"}

[[IKE SA is expired.]{lang="EN-US"}]{#struct_0_x7538_x3345_729497178}

[[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239813}[生命周期到达]{style="font-family:宋体"}

[[Renegotiation has already started for this IKE SA.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444698564}

[[该]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1714506134}[的重协商已经开始]{style="font-family:宋体"}

[[IKE SA with connection ID *connection-id* has expired, and it will be deleted.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444764100}

[[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444567492}[生命周期到达，将其删除，]{style="font-family:宋体"}[connection ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[connection-id]{lang="EN-US"}*

[[IPsec SA is being negotiated.]{lang="EN-US"}]{#struct_0_x7538_x3345_x850408911}

[[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444633028}[正在协商]{style="font-family:宋体"}

[[IPsec SA has expired and will be deleted.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444436420}

[[生命周期到达，删除二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x444501956}

[[IKE thread *thread-id* processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1617197617}

[[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_x444305348}[线程]{style="font-family:宋体"}*[thread-id]{lang="EN-US"}*[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}

[[IKE thread *thread-id* processes a CTL-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444370884}

[[IKE]{lang="EN-US"}]{#struct_0_x7538_x3345_1908150517}[线程]{style="font-family:宋体"}*[thread-id]{lang="EN-US"}*[处理一个控制队列消息]{style="font-family:宋体"}

[[Vendor ID *verdor-id* is matched.]{lang="EN-US"}]{#struct_0_x7538_x3345_x444174276}

[[匹配上]{style="font-family:宋体"}[vendor ID *verdor-id*]{lang="EN-US"}]{#struct_0_x7538_x3345_x444239812}

[[No vendor ID is matched.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385380}

[[没有匹配的]{style="font-family:宋体"}[verdor ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1823877590}

[[ ]{lang="EN-US"}]{#_Toc130718928}

[[表2-3 ]{lang="EN-US"}[debugging pki packet]{lang="EN-US"}]{#struct_0_x7538_x3345_x2050524496}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x451737092}[[字段]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1121319844}

[[描述]{style="font-family:黑体"}]{#struct_0_x7538_x3345_1296125298}

[[Construct authentication data by pre-shared key.]{lang="EN-US"}]{#struct_0_x7538_x3345_x338774440}

[[根据预共享密钥生成认证数据]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1567223738}

[[Verify ]{lang="EN-US"}]{#struct_0_x7538_x3345_1244759177}[[HASH]{lang="EN-US" style="font-size:10.5pt"}]{.MsoCommentReference}[ payload.]{lang="EN-US"}

[[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_400514287}[载荷]{style="font-family:宋体"}

[[Construct authentication data by private key.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516452}

[[根据私钥生成认证数据]{style="font-family:宋体"}]{#struct_0_x7538_x3345_2107722244}

[[Verify signature payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x708956648}

[[验证签名载荷]{style="font-family:宋体"}]{#struct_0_x7538_x3345_220322552}

[[DPD packet with sequence number *sequence-number* is received.]{lang="EN-US"}]{#struct_0_x7538_x3345_x449683924}

[[收到]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450916}[报文，序列号为：]{style="font-family:宋体"}*[sequence-number]{lang="EN-US"}*

[[Retransmit DPD packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_158282587}

[[重传]{style="font-family:宋体"}[DPD]{lang="EN-US"}]{#struct_0_x7538_x3345_1012645239}[报文]{style="font-family:宋体"}

[[Peer ID value: address *address*.]{lang="EN-US"}]{#struct_0_x7538_x3345_997155505}

[[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1121647524}[值：地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Peer ID value: FQDN *fqdn*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1799700735}

[[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1311798751}[值：]{style="font-family:宋体"}[FQDN *fqdn*]{lang="EN-US"}

[[Peer ID value: User FQDN *user-fqdn*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1196381791}

[[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_535649252}[值：]{style="font-family:宋体"}[User FQDN *user-fqdn*]{lang="EN-US"}

[[Peer ID value: DN *DN-value*]{lang="EN-US"}]{#struct_0_x7538_x3345_1121581988}

[[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1409439776}[值：]{style="font-family:宋体"}[DN]{lang="EN-US"}[，]{style="font-family:宋体"}[DN]{lang="EN-US"}[的内容为]{style="font-family:宋体"}*[DN-value]{lang="EN-US"}*

[[Peer ID type: *ID-type* (*value*).]{lang="EN-US"}]{#struct_0_x7538_x3345_1278121670}

[[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1593622608}[类型：]{style="font-family:宋体"}*[ID-type]{lang="EN-US"}*[，类型的值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Local ID type: *ID-type* (*value*).]{lang="EN-US"}]{#struct_0_x7538_x3345_1121778596}

[[本端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1283250256}[类型：]{style="font-family:宋体"}*[ID-type]{lang="EN-US"}*[，类型的值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Local ID value: *ID-value*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1770555465}

[[本端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1121713060}[值：]{style="font-family:宋体"}*[ID-value]{lang="EN-US"}*

[[Construct ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x663187114}

[[构造]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1209052932}[载荷]{style="font-family:宋体"}

[[The profile *profile-name* is matched.]{lang="EN-US"}]{#struct_0_x7538_x3345_x698899012}

[[匹配到]{style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_x7538_x3345_1121909668}[为]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*

[[No profile is matched.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1846260690}

[[没有匹配到]{style="font-family:宋体"}[profile]{lang="EN-US"}]{#struct_0_x7538_x3345_x1796067979}

[[Process ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x755771634}

[[处理]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1121844132}[载荷]{style="font-family:宋体"}

[[Construct notification packet: *notification-type*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x631611283}

[[构造]{style="font-family:宋体"}[notification]{lang="EN-US"}]{#struct_0_x7538_x3345_x1516671423}[报文：]{style="font-family:宋体"}*[notification-type]{lang="EN-US"}*

[[Construct delete payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385381}

[[构造]{style="font-family:宋体"}[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_x1823812054}[载荷]{style="font-family:宋体"}

[[The phase 1 delete packet is received.]{lang="EN-US"}]{#struct_0_x7538_x3345_1224158121}

[[收到一阶段]{style="font-family:宋体"}[delete]{lang="EN-US"}]{#struct_0_x7538_x3345_1121319845}[报文]{style="font-family:宋体"}

[[The cookies\' length (*length*) is invalid.]{lang="EN-US"}]{#struct_0_x7538_x3345_1296059762}

[[Cookies]{lang="EN-US"}]{#struct_0_x7538_x3345_68108096}[的长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[无效]{style="font-family:宋体"}

[[Construct KE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1146561736}

[[构造]{style="font-family:宋体"}[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516453}[载荷]{style="font-family:宋体"}

[[Process KE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_2107656708}

[[处理]{style="font-family:宋体"}[KE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1505230623}[载荷]{style="font-family:宋体"}

[[Send keepalive packet with sequence number *sequence-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450917}

[[发送]{style="font-family:宋体"}[IKE keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_158217051}[报文，序列号为]{style="font-family:宋体"}*[sequence-number]{lang="EN-US"}*

[[Process keepalive packet with sequence number *sequence-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x932022447}

[[处理]{style="font-family:宋体"}[IKE keepalive]{lang="EN-US"}]{#struct_0_x7538_x3345_1121647525}[报文，序列号为]{style="font-family:宋体"}*[sequence-number]{lang="EN-US"}*

[[Construct NAT-D payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1799635199}

[[构造]{style="font-family:宋体"}[NAT-D]{lang="EN-US"}]{#struct_0_x7538_x3345_1207625982}[载荷]{style="font-family:宋体"}

[[Received *count* NAT-D payloads.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121581989}

[[收到]{style="font-family:宋体"}[NAT-D]{lang="EN-US"}]{#struct_0_x7538_x3345_x1409374240}[载荷，数量为]{style="font-family:宋体"}*[count]{lang="EN-US"}*

[[Construct NONCE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2040087749}

[[构造]{style="font-family:宋体"}[NONCE]{lang="EN-US"}]{#struct_0_x7538_x3345_1121778597}[载荷]{style="font-family:宋体"}

[[Process NONCE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1283184720}

[[处理]{style="font-family:宋体"}[NONCE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1025160771}[载荷]{style="font-family:宋体"}

[[Construct INITIAL-CONTACT payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121713061}

[[构造]{style="font-family:宋体"}[INITIAL-CONTACT]{lang="EN-US"}]{#struct_0_x7538_x3345_x663252650}[载荷]{style="font-family:宋体"}

[[Construct SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_782895572}

[[构造]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_x7538_x3345_1121909669}[载荷]{style="font-family:宋体"}

[[Construct IPsec ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1846195154}

[[构造]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1121844133}[载荷]{style="font-family:宋体"}

[[Process HASH payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x631545747}

[[处理]{style="font-family:宋体"}[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_1655413616}[载荷]{style="font-family:宋体"}

[[Construct IPsec SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385378}

[[构造]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1823353295}[载荷]{style="font-family:宋体"}

[[Construct HASH(3) payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2094804566}

[[构造]{style="font-family:宋体"}[HASH(3)]{lang="EN-US"}]{#struct_0_x7538_x3345_1121319842}[载荷]{style="font-family:宋体"}

[[Process IPsec ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1295994226}

[[处理]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516450}[载荷]{style="font-family:宋体"}

[[Construct NAT-OA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_2107591172}

[[构造]{style="font-family:宋体"}[NAT-OA]{lang="EN-US"}]{#struct_0_x7538_x3345_1198820392}[载荷]{style="font-family:宋体"}

[[Process NAT-OA payload: *address*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450914}

[[处理]{style="font-family:宋体"}[NAT-OA]{lang="EN-US"}]{#struct_0_x7538_x3345_158151515}[载荷，地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*

[[Received *count* NAT-OA payloads.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121647522}

[[收到]{style="font-family:宋体"}[NAT-OA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1799569663}[载荷，数量为]{style="font-family:宋体"}*[count]{lang="EN-US"}*

[[Construct IPsec RESPONDER_LIFETIME payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_665930006}

[[构造]{style="font-family:宋体"}[IPsec RESPONDER_LIFETIME]{lang="EN-US"}]{#struct_0_x7538_x3345_1121581986}[载荷]{style="font-family:宋体"}

[[Construct HASH(1) payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1409832992}

[[构造]{style="font-family:宋体"}[HASH(1)]{lang="EN-US"}]{#struct_0_x7538_x3345_1121778594}[载荷]{style="font-family:宋体"}

[[Collision of phase 2 negotiation is found.]{lang="EN-US"}]{#struct_0_x7538_x3345_1283381328}

[[二阶段协商发生碰撞]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121713058}

[[Construct HASH(2) payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x663711403}

[[构造]{style="font-family:宋体"}[HASH(2)]{lang="EN-US"}]{#struct_0_x7538_x3345_x1572366847}[载荷]{style="font-family:宋体"}

[[I-Cookie: *icookie*]{lang="EN-US"}]{#struct_0_x7538_x3345_1121909666}

[[R-Cookie: *rcookie*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1845605330}

[[next payload: *next-payload*]{lang="EN-US"}]{#struct_0_x7538_x3345_1121844130}

[[version: *version*]{lang="EN-US"}]{#struct_0_x7538_x3345_x631480211}

[[exchange mode: *mode*]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385379}

[[flags: \[*flag*\]]{lang="EN-US"}]{#struct_0_x7538_x3345_x1823287759}

[[message ID: *mid*]{lang="EN-US"}]{#struct_0_x7538_x3345_1121319843}

[[length: *length*]{lang="EN-US"}]{#struct_0_x7538_x3345_1295928690}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发起方]{lang="EN-US" style="font-family:宋体"}[cookie]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516451}[：]{lang="EN-US" style="font-family:宋体"}[icookie]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[响应方]{lang="EN-US" style="font-family:宋体"}[cookie]{lang="EN-US"}]{#struct_0_x7538_x3345_2107525636}[：]{lang="EN-US" style="font-family:宋体"}[rcookie]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[下一个载荷：]{lang="EN-US" style="font-family:宋体"}[next-payload]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450915}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISAKMP]{lang="EN-US"}]{#struct_0_x7538_x3345_158085979}[版本：]{lang="EN-US" style="font-family:宋体"}[version]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协商模式：]{lang="EN-US" style="font-family:宋体"}[mode]{lang="EN-US"}]{#struct_0_x7538_x3345_786187829}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标识为：]{lang="EN-US" style="font-family:宋体"}[flag]{lang="EN-US"}]{#struct_0_x7538_x3345_1121647523}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Message ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1799504127}[：]{lang="EN-US" style="font-family:宋体"}[mid]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121581987}[长度：]{lang="EN-US" style="font-family:宋体"}[length]{lang="EN-US"}

[[Encrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1409767456}

[[对报文进行加密]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121778595}

[[Received *payload-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1283315792}

[[收到载荷]{style="font-family:宋体"}*[payload-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_1121713059}

[[Sending packet to *address*, remote port *remote-port*, local port *local-port*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x663776939}

[[发送报文到地址]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x7538_x3345_1121909667}[，对端端口号为]{style="font-family:宋体"}*[remote-port]{lang="EN-US"}*[，本端端口号为]{style="font-family:宋体"}*[local-port]{lang="EN-US"}*

[[Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1845539794}

[[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7538_x3345_1121844131}[报文]{style="font-family:宋体"}

[[Sending an IPv6 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x631414675}

[[发送一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385376}[报文]{style="font-family:宋体"}

[[Retransmit phase 1 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121319840}

[[重传一阶段报文]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1295863154}

[[Retransmit phase 2 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516448}

[[重传二阶段报文]{style="font-family:宋体"}]{#struct_0_x7538_x3345_2107066883}

[[Retransmit in response to duplicate packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450912}

[[针对对端重发的报文，重传对应的响应报文]{style="font-family:宋体"}]{#struct_0_x7538_x3345_158544731}

[[Discard duplicate packet because of exhausted retransmission.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121647520}

[[本端重传次数已达到最大，不再响应该重复的报文，将其丢弃]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1799438591}

[[Discard duplicate packet with no response.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121581984}

[[丢弃对端重复发送的报文，不进行响应]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1409701920}

[[Collision of phase 1 negotiation is found.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121778592}

[[一阶段协商发生碰撞]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121713056}

[[Decrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x662793899}

[[对报文进行解密]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121909664}

[[Begin a new phase 1 negotiation as responder.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1845474258}

[[做为响应方，开始加入一个新的一阶段协商过程]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121844128}

[[Parse informational exchange packet successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_x630955922}

[[成功解析]{style="font-family:宋体"}[informational exchange]{lang="EN-US"}]{#struct_0_x7538_x3345_1121385377}[报文]{style="font-family:宋体"}

[[Received packet from *address* source port *source-port* destination port *des-port*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121319841}

[[收到的来自]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x7538_x3345_1295797618}[的报文，源端口为]{style="font-family:宋体"}*[source-port]{lang="EN-US"}*[，目的端口为]{style="font-family:宋体"}*[des-port]{lang="EN-US"}*

[[Skipping *length* raw bytes of *name1* to get *name2*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121516449}

[[跳过载荷]{style="font-family:宋体"}[name1]{lang="EN-US"}]{#struct_0_x7538_x3345_2107001347}[的]{style="font-family:宋体"}*[length]{lang="EN-US"}*[字节，去获取下一个载荷]{style="font-family:宋体"}*[name2]{lang="EN-US"}*

[[Add certificate request payload *subjectname*.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121450913}

[[添加证书请求载荷，主题名为]{style="font-family:宋体"}*[subjectname]{lang="EN-US"}*]{#struct_0_x7538_x3345_1121647521}

[[Construct certificate request payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1799373055}

[[构造证书请求载荷]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1121581985}

[[Received certificate request payload that contains issuer name *issuer-name*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1409636384}

[[收到证书请求载荷，签发者名为]{style="font-family:宋体"}*[issuer-name]{lang="EN-US"}*]{#struct_0_x7538_x3345_1121778593}

[[Process certificate request payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121713057}

[[处理证书请求载荷]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x662859435}

[[The certificate request payload is empty.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121909665}

[[证书请求载荷是空的]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1845408722}

[[Construct certificate payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1121844129}

[[构造证书载荷]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1607497975}

[[The profile *profile-name is matched* by remote certificate.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1954587661}

[[通过对端证书匹配到一个]{style="font-family:宋体"}[IKE profile *profile-name*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563511}

[[Process certificate payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607366903}

[[处理证书载荷]{style="font-family:宋体"}]{#struct_0_x7538_x3345_101656958}

[[Encryption algorithm is *enc-algo*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607432439}

[[加密算法为]{style="font-family:宋体"}*[enc-algo]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1798252216}

[[HASH algorithm is *hash-algo*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235831}

[[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607301367}[算法为]{style="font-family:宋体"}*[hash-algo]{lang="EN-US"}*

[[Authentication method is *auth-method*.]{lang="EN-US"}]{#struct_0_x7538_x3345_31735670}

[[认证方法为]{style="font-family:宋体"}*[auth-method]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1607104759}

[[DH group is *group*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170295}

[[DH group]{lang="EN-US"}]{#struct_0_x7538_x3345_x1372005090}[为]{style="font-family:宋体"}*[group]{lang="EN-US"}*

[[Lifetime type is *type*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1606973687}

[[生命周期类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1607039223}[，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in seconds]{lang="EN-US"}]{#struct_0_x7538_x3345_x1926785808}[：时间生命周期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in kilobyte]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607497974}[s]{lang="EN-US"}[：字节生命周期]{lang="EN-US" style="font-family:宋体"}

[[Life duration is *value*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563510}

[[生命周期为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x7538_x3345_985248983}

[[Key length is *length* bytes.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607366902}

[[密钥长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1607432438}[字节]{style="font-family:宋体"}

[[Check ISAKMP transform *trans-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x232168275}

[[检查]{style="font-family:宋体"}[ISAKMP transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235830}[，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*

[[Attributes is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607301366}

[[属性是可接受的]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1534348271}

[[Construct transfrom payload for transform *trans-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607104758}

[[构造]{style="font-family:宋体"}[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170294}[载荷，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*

[[Encapsulation mode is *mode*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1606973686}

[[封装模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*]{#struct_0_x7538_x3345_x851017876}[，]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607039222}[：隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transport]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607497977}[：传输模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel-UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_x791788247}[：]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的隧道模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Transport-UDP]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563513}[：]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[封装的传输模式]{lang="EN-US" style="font-family:宋体"}

[[Set attributes according to phase 2 transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607366905}

[[根据二阶段]{style="font-family:宋体"}[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607432441}[设置属性]{style="font-family:宋体"}

[[Transform ID is *id*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1442218464}

[[Transform ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235833}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[Construct transform 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607301369}

[[构造]{style="font-family:宋体"}[transform 1]{lang="EN-US"}]{#struct_0_x7538_x3345_x1487294104}

[[Construct IPsec proposal *proposal-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607104761}

[[构造]{style="font-family:宋体"}[IPsec proposal]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170297}[，]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号为]{style="font-family:宋体"}*[proposal-number]{lang="EN-US"}*

[[Parse transform *trans-number*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1606973689}

[[解析]{style="font-family:宋体"}[transform]{lang="EN-US"}]{#struct_0_x7538_x3345_1071296425}[，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[trans-number]{lang="EN-US"}*

[[The SA_LIFE_TYPE attribute is repeated in packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607039225}

[[SA_LIFE_TYPE]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607497976}[属性在报文中重复]{style="font-family:宋体"}

[[Number of key rounds is *round*.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563512}

[[密钥轮数为]{style="font-family:宋体"}*[round]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1607366904}

[[Process IPsec SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x301627569}

[[处理]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607432440}[载荷]{style="font-family:宋体"}

[[The attributes are unacceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235832}

[[属性不可接受]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1607301368}

[[Construct *vid-name* vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1241589251}

[[构造]{style="font-family:宋体"}[vendor id]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607104760}[载荷，]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[名称为]{style="font-family:宋体"}*[vid-name]{lang="EN-US"}*

[[Process vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170296}

[[处理]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1606973688}[载荷]{style="font-family:宋体"}

[[HASH:*value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607039224}

[[HASH]{lang="EN-US"}]{#struct_0_x7538_x3345_x1523501281}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[SKEYID:*value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607497979}

[[SKEYID]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563515}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Extended Skeyid_e:*value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607366907}

[[扩展的]{style="font-family:宋体"}[Skeyid_e]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607432443}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Local generated new IV: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_1689949418}

[[本地新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235835}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[SKEYID_a: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607301371}

[[SKEYID_a]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607104763}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[SKEYID_d: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170299}

[[SKEYID_d]{lang="EN-US"}]{#struct_0_x7538_x3345_953593738}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[SKEYID_e: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1606973691}

[[SKEYID_e]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607039227}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Encrypt IV: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607497978}

[[加密]{style="font-family:宋体"}[IV]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607563514}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Encryption generated new IV: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607366906}

[[加密新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}]{#struct_0_x7538_x3345_861171845}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Decrypt IV: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607432442}

[[解密]{style="font-family:宋体"}[IV]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607235834}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Remote new IV: *value*]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607301370}

[[对端新]{style="font-family:宋体"}[IV]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607104762}[为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[The proposal is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607170298}

[[提议是可以接受的]{style="font-family:宋体"}]{#struct_0_x7538_x3345_x1606973690}

[[The proposal is unacceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1607039226}

[[提议是不能接受的]{style="font-family:宋体"}]{#struct_0_x7538_x3345_1608666601}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7538_x3345_456461533}

[[\#]{lang="EN-US"}]{#struct_0_x7538_x3345_314816326}[在两个安全网关上配置了]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商类型的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[策略，在一阶段]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商过程中，若未找到匹配的]{style="font-family:宋体"}[IKE proposal]{lang="EN-US"}[，则打开]{style="font-family:宋体"}[IKE]{lang="EN-US"}[错误调试信息开关后将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ike error]{lang="EN-US"}]{#struct_0_x7538_x3345_1257817760}

[\*Aug 20 19:19:44:543 2012 Sysname IKE/7/ERROR: -MDC=1; No acceptable transform.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_523432914}*[没有可以接受的]{style="font-family:宋体"}[transform]{lang="EN-US"}*

[[\*Aug 20 19:19:44:543 2012 Sysname IKE/7/ERROR: -MDC=1; Failed to parse the IKE SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_836187259}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1392531340}*[解析]{style="font-family:宋体"}[SA]{lang="EN-US"}[载荷失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x7538_x3345_x1085545621}[在两个安全网关上配置了]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商类型的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[策略，若配置一阶段协商模式为主模式，认证方法为预共享密钥认证，则当有流量触发协商时，打开]{style="font-family:宋体"}[IKE]{lang="EN-US"}[事件调试信息开关后将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ike event]{lang="EN-US"}]{#struct_0_x7538_x3345_9521607}

[\<Sysname\> ping -c 1 192.168.222.5 ]{lang="EN-US"}

[PING 192.168.222.5 (192.168.222.5): 56 data bytes, press CTRL_C to break ]{lang="EN-US"}

[\*Aug 20 19:10:37:509 2012 Sysname IKE/7/EVENT: -MDC=1; Received SA acquire message from IPsec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314750790}*[收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Set IPsec SA state to IKE_P2_STA]{lang="EN-US"}]{#struct_0_x7538_x3345_x1304496974}

[TE_INIT.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x696237540}*[设置二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态为]{style="font-family:宋体"}[IKE_P2_STATE_INIT]{lang="EN-US"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; No IKE SA found, initiate IKE SA negotiation.]{lang="EN-US"}]{#struct_0_x7538_x3345_932420121}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1698678340}*[没有一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[，发起一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[的协商]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Get profile profile1.]{lang="EN-US"}]{#struct_0_x7538_x3345_1602007950}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x299859521}*[获取]{style="font-family:宋体"}[profile profile1]{lang="EN-US"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Initiator create a SA for peer 192.168.222.5, local port 500, remote port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_314947398}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1612695349}*[发起方创建]{style="font-family:宋体"}[SA]{lang="EN-US"}[，对端地址为]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，本端端口为]{style="font-family:宋体"}[500]{lang="EN-US"}[，对端端口为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Set IKE SA state to IKE_P1_STATE_INIT.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1396874577}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2021890265}*[设置一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态为]{style="font-family:宋体"}[IKE_P1_STATE_INIT]{lang="EN-US"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3083549648 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_1898622672}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1399361746}*[线程]{style="font-family:宋体"}[3083549648]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:510 2012 Sysname IKE/7/EVENT: -MDC=1; Begin Main mode exchange.]{lang="EN-US"}]{#struct_0_x7538_x3345_x700978516}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_729388701}*[开始主模式协商]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:511 2012 Sysname IKE/7/EVENT: -MDC=1; Found pre-shared key that matches address 192.168.222.5 in keychain keychain1. ]{lang="EN-US"}]{#struct_0_x7538_x3345_x1659718455}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314881862}*[在]{style="font-family:宋体"}[keychain keychain1]{lang="EN-US"}[中找到了预共享密钥，预共享密钥匹配地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}*

[[\*Aug 20 19:10:37:511 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_INIT to IKE_P1_STATE_SEND1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x714547518}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2109782249}*[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P1_STATE_INIT]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P1_STATE_SEND1]{lang="EN-US"}*

[[\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3008052176 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_1272166188}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_1564864642}*[线程]{style="font-family:宋体"}[3008052176]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; Oakley transform 1 is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_1368925491}

[*[// Oakley transform]{lang="EN-US"}*]{#struct_0_x7538_x3345_x352937547}*[是可接受的，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:10:37:520 2012 Sysname IKE/7/EVENT: -MDC=1; Match the vendor ID NAT-T rfc3947.]{lang="EN-US"}]{#struct_0_x7538_x3345_x250101075}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315078470}*[匹配上]{style="font-family:宋体"}[vendor ID NAT-T rfc3947]{lang="EN-US"}*

[[\*Aug 20 19:10:37:533 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND1 to IKE_P1_STATE_SEND3.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1170322874}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1494366331}*[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P1_STATE_SEND1]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P1_STATE_SEND3]{lang="EN-US"}*

[[\*Aug 20 19:10:37:533 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1903738359}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2086548140}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:566 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3083549648 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_1336590016}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_905057401}*[线程]{style="font-family:宋体"}[3083549648]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; Match the vendor ID DPD.]{lang="EN-US"}]{#struct_0_x7538_x3345_315012934}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x431076175}*[匹配上]{style="font-family:宋体"}[vendor ID DPD]{lang="EN-US"}*

[[\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND3 to IKE_P1_STATE_SEND5.]{lang="EN-US"}]{#struct_0_x7538_x3345_1770846326}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_415035298}*[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P1_STATE_SEND3]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P1_STATE_SEND5]{lang="EN-US"}*

[[\*Aug 20 19:10:37:580 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_x383375679}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x447706217}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:584 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3075161040 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_615536080}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x233175319}*[线程]{style="font-family:宋体"}[3075161040]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:584 2012 Sysname IKE/7/EVENT: -MDC=1; Verify HASH successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2102093046}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315209542}*[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}[成功]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; IKE SA state changed from IKE_P1_STATE_SEND5 to IKE_P1_STATE_ESTABLISHED.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1294936698}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_311641896}*[一阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P1_STATE_SEND5]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P1_STATE_ESTABLISHED]{lang="EN-US"}*

[[\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3075161040 process]{lang="EN-US"}]{#struct_0_x7538_x3345_x1782668799}

[es a job.]{lang="EN-US"}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_1958991388}*[线程]{style="font-family:宋体"}[3075161040]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:585 2012 Sysname IKE/7/EVENT: -MDC=1; Begin Quick mode exchange.]{lang="EN-US"}]{#struct_0_x7538_x3345_1127198551}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2073942174}*[开始快速模式协商]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_x221441940}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_315144006}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_INIT to IKE_P2_STATE_GETSPI.]{lang="EN-US"}]{#struct_0_x7538_x3345_756292885}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_790664793}*[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P2_STATE_INIT]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P2_STATE_GETSPI]{lang="EN-US"}*

[[\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_944072464}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x580677867}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3066772432 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_x412441858}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_785669637}*[线程]{style="font-family:宋体"}[3066772432]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:586 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_GETSPI to IKE_P2_STATE_SEND1.]{lang="EN-US"}]{#struct_0_x7538_x3345_747851456}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315340614}*[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P2_STATE_GETSPI]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P2_STATE_SEND1]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_x499359371}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_177933400}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3033218000 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_x520026219}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_1430656830}*[线程]{style="font-family:宋体"}[3033218000]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; Validate HASH(2) successfully.]{lang="EN-US"}]{#struct_0_x7538_x3345_1800154016}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2021263816}*[验证]{style="font-family:宋体"}[HASH(2)]{lang="EN-US"}[成功]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; Install IPsec SAs.]{lang="EN-US"}]{#struct_0_x7538_x3345_315275078}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2100749142}*[下发]{style="font-family:宋体"}[IPsecSA]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   inbound flow: 192.168.222.5/32-\>192.168.222.71/32]{lang="EN-US"}]{#struct_0_x7538_x3345_x1029186305}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1761568824}*[入流量为]{style="font-family:宋体"}[192.168.222.5/32-\>192.168.222.71/32]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   outbound flow: 192.168.222.]{lang="EN-US"}]{#struct_0_x7538_x3345_x791280690}

[71/32-\>192.168.222.5/32]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1201265285}*[出流量为]{style="font-family:宋体"}[192.168.222.71/32-\>192.168.222.5/32]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   Lifetime second: 3600]{lang="EN-US"}]{#struct_0_x7538_x3345_x1179494969}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x557233513}*[生命周期为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   Lifetime kilobytes: 1843200]{lang="EN-US"}]{#struct_0_x7538_x3345_314816327}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1257817761}*[生命周期为]{style="font-family:宋体"}[1843200]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1;   protocol: 51]{lang="EN-US"}]{#struct_0_x7538_x3345_523498450}

[  inbound SPI: 54e4913]{lang="EN-US"}

[   outbound SPI: 44213487]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1626288292}*[协议为]{style="font-family:宋体"}[51]{lang="EN-US"}[，入方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}[为：]{style="font-family:宋体"}[54e4913]{lang="EN-US"}[，出方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}[为：]{style="font-family:宋体"}[44213487]{lang="EN-US"}*

[[\*Aug 20 19:10:37:592 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_SEND1 to IKE_P2_STATE_SA_CREATED.]{lang="EN-US"}]{#struct_0_x7538_x3345_262461682}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_881409644}*[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P2_STATE_SEND1]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P2_STATE_SA_CREATED]{lang="EN-US"}*

[[\*Aug 20 19:10:37:593 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3087980192 processes a Control-Queue msg.]{lang="EN-US"}]{#struct_0_x7538_x3345_314750791}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1304496973}*[线程]{style="font-family:宋体"}[3087980192]{lang="EN-US"}[处理一个控制队列消息]{style="font-family:宋体"}*

[[\*Aug 20 19:10:37:594 2012 Sysname IKE/7/EVENT: -MDC=1; IKE thread 3041606608 processes a job.]{lang="EN-US"}]{#struct_0_x7538_x3345_2032645815}

[*[// IKE]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1553874474}*[线程]{style="font-family:宋体"}[3041606608]{lang="EN-US"}[处理一个]{style="font-family:宋体"}[job]{lang="EN-US"}*

[[\*Aug 20 19:10:37:594 2012 Sysname IKE/7/EVENT: -MDC=1; IPsec SA state changed from IKE_P2_STATE_SA_CREATED to IKE_P2_STATE_ESTABLISHED.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1763814065}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x464385922}*[二阶段]{style="font-family:宋体"}[SA]{lang="EN-US"}[状态从]{style="font-family:宋体"}[IKE_P2_STATE_SA_CREATED]{lang="EN-US"}[到]{style="font-family:宋体"}[IKE_P2_STATE_ESTABLISHED]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x7538_x3345_402745324}[在两个安全网关上配置了]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商类型的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[策略，若配置一阶段协商模式为主模式，认证方法为预共享密钥认证，则当有流量触发协商时，打开]{style="font-family:宋体"}[IKE]{lang="EN-US"}[报文调试信息开关后将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging ike packet]{lang="EN-US"}]{#struct_0_x7538_x3345_314947399}

[\<Sysname\> ping -c 1  192.168.222.5]{lang="EN-US"}

[PING 192.168.222.5 (192.168.222.5): 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Encryption algorithm is 3DES-CBC.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1612695348}*[加密算法为]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Hash algorithm is HMAC-MD5.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1396940113}

[*[// HASH]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1784351734}*[算法为]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   DH group 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_781598618}

[*[// DH group]{lang="EN-US"}*]{#struct_0_x7538_x3345_1418122678}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication method is Pre-shared key.]{lang="EN-US"}]{#struct_0_x7538_x3345_x439149613}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x370404786}*[认证方法为]{style="font-family:宋体"}[Pre-shared key]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.]{lang="EN-US"}]{#struct_0_x7538_x3345_314881863}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x714547519}*[生命周期类型为]{style="font-family:宋体"}[Life type in seconds]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 86400.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2109716713}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1989098222}*[生命周期为]{style="font-family:宋体"}[86400]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct transform payload 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_230478492}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1542919752}*[构造]{style="font-family:宋体"}[transform]{lang="EN-US"}[载荷，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x487273492}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x180760668}*[构造]{style="font-family:宋体"}[SA]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T rfc3947 vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_315078471}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1170322873}*[构造]{style="font-family:宋体"}[vendor id]{lang="EN-US"}[载荷，]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[名称为]{style="font-family:宋体"}[NAT-T rfc3947]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft3 vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2041086078}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1573308144}*[构造]{style="font-family:宋体"}[vendor id]{lang="EN-US"}[载荷，]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[名称为]{style="font-family:宋体"}[NAT-T draft3]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft2 vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1224012991}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_13389990}*[构造]{style="font-family:宋体"}[vendor id]{lang="EN-US"}[载荷，]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[名称为]{style="font-family:宋体"}[NAT-T draft2]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-T draft1 vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x908773996}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315012935}*[构造]{style="font-family:宋体"}[vendor id]{lang="EN-US"}[载荷，]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[名称为]{style="font-family:宋体"}[NAT-T draft1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5 local port 500, remote port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_x431076174}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1770780790}*[发送报文到地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，本端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}[，对端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_482489516}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 0000000000000000]{lang="EN-US"}

[  next payload: SA]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ \]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 164]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1327186018}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1311812393}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[0000000000000000]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315209543}*[下一个载荷为：]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1294936699}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1254442045}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1386568665}*[标识为：]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_1869891681}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x636237977}*[长度为：]{style="font-family:宋体"}[164]{lang="EN-US"}*

[[\*Aug 20 19:18:34:125 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_2066646042}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315144007}*[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.]{lang="EN-US"}]{#struct_0_x7538_x3345_756292884}

[222.5 source port 500 destination port 500.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_790664794}*[收到的]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[报文，源端口为]{style="font-family:宋体"}[500]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_944072459}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: SA]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ \]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 104]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2140311322}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x935875761}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315340615}*[下一个载荷为：]{style="font-family:宋体"}[SA]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x499359372}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_177998936}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_726669938}*[标识为：]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_48564443}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1005077065}*[长度为：]{style="font-family:宋体"}[104]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received IKE Security Association Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_355631553}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315275079}*[收到]{style="font-family:宋体"}[SA]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Vendor ID Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2100749141}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1432470832}*[收到]{style="font-family:宋体"}[Vendor ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Process SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1070554268}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1204010011}*[处理]{style="font-family:宋体"}[SA]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Check ISAKMP transform 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x154590231}

[检查]{style="font-family:宋体"}[ISAKMP transform]{lang="EN-US"}[，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}*[1]{lang="EN-US"}*

[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Encryption algorithm is 3DES-CBC.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_113570409}*[加密算法为]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   HASH algorithm is HMAC-MD5.]{lang="EN-US"}]{#struct_0_x7538_x3345_314816324}

[*[// HASH]{lang="EN-US"}*]{#struct_0_x7538_x3345_1257817758}*[算法为]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   DH group is 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_522908623}

[*[// DH group]{lang="EN-US"}*]{#struct_0_x7538_x3345_414005671}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication method is Pre-shared key.]{lang="EN-US"}]{#struct_0_x7538_x3345_664367922}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2066727265}*[认证方法为]{style="font-family:宋体"}[Pre-shared key]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1397185113}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1483214289}*[生命周期类型为]{style="font-family:宋体"}[Life type in seconds]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 86400.]{lang="EN-US"}]{#struct_0_x7538_x3345_314750788}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1034155178}*[生命周期为]{style="font-family:宋体"}[86400]{lang="EN-US"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Attribuites is acceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1715286536}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2139051480}*[属性是可接受的]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:127 2012 Sysname IKE/7/PACKET: -MDC=1; Process vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1618876864}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_554068202}*[处理]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct KE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1506363999}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2144424088}*[构造]{style="font-family:宋体"}[IKE]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NONCE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_314947396}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1612695359}*[构造]{style="font-family:宋体"}[NONCE]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:137 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NAT-D payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1396874576}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_706993090}*[构造]{style="font-family:宋体"}[NAT-D]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Construct DPD vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x21611729}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_234374830}*[构造]{style="font-family:宋体"}[DPD vendor ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.22]{lang="EN-US"}]{#struct_0_x7538_x3345_1524882446}

[2.5 , remote port 500 ,local port 500.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314881860}*[发送报文到地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，对端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}[，本端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x714547516}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: KE]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ \]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 208]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2109913321}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_143675836}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x216024680}*[下一个载荷为：]{style="font-family:宋体"}[KE]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_601072669}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315078468}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_785992254}*[标识为：]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1392565446}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x178919002}*[长度为：]{style="font-family:宋体"}[208]{lang="EN-US"}*

[[\*Aug 20 19:18:34:138 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1988171407}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_608491348}*[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.222.5 source port 500 destination port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_579134961}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315012932}*[收到的]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[报文，源端口为]{style="font-family:宋体"}[500]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x431076177}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: KE]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ \]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 208]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1770715254}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1518169487}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1960124573}*[下一个载荷为：]{style="font-family:宋体"}[KE]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1497618916}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315209540}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1294936696}*[标识为：]{style="font-family:宋体"}[\[ \]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_1830671670}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1386192951}*[长度为：]{style="font-family:宋体"}[208]{lang="EN-US"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Key ExchangePayload.]{lang="EN-US"}]{#struct_0_x7538_x3345_2084474402}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1324498401}*[收到]{style="font-family:宋体"}[ISAKMP Key Exchange]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Nonce Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_454547508}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_125161853}*[收到]{style="font-family:宋体"}[ISAKMP Nonce]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP NAT-D Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_315144004}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_756292887}*[收到]{style="font-family:宋体"}[ISAKMP NAT-D]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP NAT-D Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_790664791}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_944072462}*[收到]{style="font-family:宋体"}[ISAKMP NAT-D]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Vendor ID Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x580677869}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x413097218}*[收到]{style="font-family:宋体"}[ISAKMP Vendor ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Process KE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x442415533}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_847623038}*[处理]{style="font-family:宋体"}[KE]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:171 2012 Sysname IKE/7/PACKET: -MDC=1; Process NONCE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_315340612}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x499359377}*[处理]{style="font-family:宋体"}[NONCE]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID:]{lang="EN-US"}]{#struct_0_x7538_x3345_177802328}

[ 989e79e1 620ff603 a76bb9b9 7d88a19c]{lang="EN-US"}

[*[// SKEYID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1280923239}*[为]{style="font-family:宋体"}[989e79e1 620ff603 a76bb9b9 7d88a19c]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_d:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1067670806}

[ 6fd7bd8f faf8480a af6c4813 4011cadd]{lang="EN-US"}

[*[// SKEYID_d]{lang="EN-US"}*]{#struct_0_x7538_x3345_408817068}*[为]{style="font-family:宋体"}[6fd7bd8f faf8480a af6c4813 4011cadd]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_a:]{lang="EN-US"}]{#struct_0_x7538_x3345_x2045746666}

[ cd0aeaf8 6bb94aa3 3ad50fe4 7fb0464f]{lang="EN-US"}

[*[// SKEYID_a]{lang="EN-US"}*]{#struct_0_x7538_x3345_315275076}*[为]{style="font-family:宋体"}[cd0aeaf8 6bb94aa3 3ad50fe4 7fb0464f]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; SKEYID_e:]{lang="EN-US"}]{#struct_0_x7538_x3345_x2100749132}

[ 795d3765 91083053 65cacc69 000ffe09]{lang="EN-US"}

[*[// SKEYID_e]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1029251841}*[为]{style="font-family:宋体"}[795d3765 91083053 65cacc69 000ffe09]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Extended SKEYID_e:]{lang="EN-US"}]{#struct_0_x7538_x3345_313942594}

[ d554084f a2a9237a 9c141dac a41c86e9 8aa14807 14db45be]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_884196890}*[扩展的]{style="font-family:宋体"}[SKEYID_e]{lang="EN-US"}[为]{style="font-family:宋体"}[d554084f a2a9237a 9c141dac a41c86e9 8aa14807 14db45be]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local generated new IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_942736222}

[ add7096a 4b961742]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1255750467}*[本地新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[add7096a 4b961742]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Received 2 NAT-D payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_314816325}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1257817759}*[收到]{style="font-family:宋体"}[NAT-D]{lang="EN-US"}[载荷，数量为]{style="font-family:宋体"}[2]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local ID type: IPV4_ADDR.]{lang="EN-US"}]{#struct_0_x7538_x3345_522974159}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_828676119}*[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[类型为：]{style="font-family:宋体"}[IPV4_ADDR]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Local ID value: 192.168.222.]{lang="EN-US"}]{#struct_0_x7538_x3345_x860486262}

[71.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2068718356}*[本端]{style="font-family:宋体"}[ID]{lang="EN-US"}[值为：]{style="font-family:宋体"}[192.168.222.71]{lang="EN-US"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Construct ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_314750789}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1034155179}*[构造]{style="font-family:宋体"}[ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Hash:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1715221000}

[ c5d733fa e6d1a6af ded56c05 de989aad]{lang="EN-US"}

[// HASH]{lang="EN-US"}[为]{style="font-family:
宋体"}[c5d733fa e6d1a6af ded56c05 de989aad]{lang="EN-US"}

[\*Aug 20 19:18:34:184 2012 Sysname IKE/7/PACKET: -MDC=1; Construct authentication by pre-shared key.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1773003559}*[根据预共享密钥生成认证数据]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Construct INITIAL-CONTACT payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1480829350}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1752974896}*[构造]{style="font-family:宋体"}[INITIAL-CONTACT]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_246305156}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314947397}*[加密报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_1612695358}

[ add7096a 4b961742]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1396940112}*[加密]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[add7096a 4b961742]{lang="EN-US"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Encryption generated New IV: ae230a1d 7cb77287]{lang="EN-US"}]{#struct_0_x7538_x3345_x218267793}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1638221453}*[加密时新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[ae230a1d 7cb77287]{lang="EN-US"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Process vendor ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2040028986}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1599572250}*[处理]{style="font-family:宋体"}[vendor ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5, remote port 500, local port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_314881861}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x714547517}*[发送报文到地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，对端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}[，本端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_x2109847785}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: ID]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ENCRYPT\]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 92]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_614665857}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1365915138}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_89367630}*[下一个载荷为：]{style="font-family:宋体"}[ID]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315078469}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_785992255}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1392565445}*[标识为：]{style="font-family:宋体"}[\[ENCRYPT\]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x582203529}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_626970538}*[长度为：]{style="font-family:宋体"}[92]{lang="EN-US"}*

[[\*Aug 20 19:18:34:185 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x549684161}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_187252517}*[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.]{lang="EN-US"}]{#struct_0_x7538_x3345_315012933}

[222.5, source port 500 destination port 500.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x431076176}*[收到的]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[报文，源端口为]{style="font-family:宋体"}[500]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_1770649718}

[  I-cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: ID]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Main]{lang="EN-US"}

[  flags: \[ENCRYPT\]]{lang="EN-US"}

[  message ID: 0]{lang="EN-US"}

[  length: 60]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1666915154}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2078579118}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_552013621}*[下一个载荷为：]{style="font-family:宋体"}[ID]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315209541}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1294936697}*[协商模式为：]{style="font-family:宋体"}[Main]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_264587729}*[标识为：]{style="font-family:宋体"}[\[ENCRYPT\]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x583930148}*[为：]{style="font-family:宋体"}[0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_225133898}*[长度为：]{style="font-family:宋体"}[60]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_1621671117}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x70866887}*[解密报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_315144005}

[ ae230a1d 7cb77287]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_756292886}*[解密]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[ae230a1d 7cb77287]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Remote New IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_790664792}

[ 4c788f75 c7ad88ab]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_944072465}*[对端新]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[4c788f75 c7ad88ab]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x580677866}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x412376322}*[收到]{style="font-family:宋体"}[ISAKMP Identification]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Hash Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_331791220}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315340613}*[收到]{style="font-family:宋体"}[ISAKMP Hash]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Process ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x499359378}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_177343576}*[处理]{style="font-family:宋体"}[ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Peer ID type: IPV4_ADDR.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2043899311}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1112834403}*[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPV4_ADDR]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Peer ID value: address 192.168.222.5.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1919756663}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_754579617}*[对端]{style="font-family:宋体"}[ID]{lang="EN-US"}[值为]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; Verify HASH payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_315275077}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2100749131}*[验证]{style="font-family:宋体"}[HASH]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:188 2012 Sysname IKE/7/PACKET: -MDC=1; HASH:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1432536368}

[ f510f1f8 1d205e1c 9aa31c42 00b3ab9a]{lang="EN-US"}

[*[// HASH]{lang="EN-US"}*]{#struct_0_x7538_x3345_866530631}*[为]{style="font-family:宋体"}[f510f1f8 1d205e1c 9aa31c42 00b3ab9a]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Set attributes by phase 2 transform.]{lang="EN-US"}]{#struct_0_x7538_x3345_1027877208}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1928838717}*[根据二阶段]{style="font-family:宋体"}[transform]{lang="EN-US"}[设置属性]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Encapsulation mode is Tunnel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1881352273}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1862658590}*[封装模式为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life type in seconds]{lang="EN-US"}]{#struct_0_x7538_x3345_314816322}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1257817756}*[生命周期类型为]{style="font-family:宋体"}[Life type in seconds]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 3600.]{lang="EN-US"}]{#struct_0_x7538_x3345_523563983}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2049324311}*[生命周期为]{style="font-family:宋体"}[3600]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life type in kilobytes]{lang="EN-US"}]{#struct_0_x7538_x3345_1083991109}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x862917914}*[生命周期类型为]{style="font-family:宋体"}[Life type in kilobytes]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 1843200.]{lang="EN-US"}]{#struct_0_x7538_x3345_2108510695}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314750786}*[生命周期为]{style="font-family:宋体"}[1843200]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication algorithm is HMAC-SHA1]{lang="EN-US"}]{#struct_0_x7538_x3345_1034155184}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1714500115}*[认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;   Transform ID is HMAC-SHA1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1989642882}

[*[// Transform ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1522349671}*[为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct transform 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1572857695}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1892230763}*[构造]{style="font-family:宋体"}[transform 1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec proposal 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_314947394}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1612695361}*[构造]{style="font-family:宋体"}[IPsec proposal]{lang="EN-US"}[，]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1396350291}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1097842590}*[构造]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct NONCE payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2125414753}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1965439602}*[构造]{style="font-family:宋体"}[NONCE]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x556260597}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x676793889}*[构造]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct IPsec ID payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_314881858}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2006441660}*[构造]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Construct HASH(1) payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x169833338}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1778942054}*[构造]{style="font-family:宋体"}[HASH(1)]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1218448153}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1024864271}*[加密报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_1281777777}

[ 836eddd9 ed30acf7]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315078466}*[加密]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[836eddd9 ed30acf7]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypted Generate New IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_785992264}

[ 3b143591 5c647ff2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1328423738}*[加密时新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[3b143591 5c647ff2]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.22]{lang="EN-US"}]{#struct_0_x7538_x3345_1005687086}

[2.5, remote port 500, local port 500.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_353665409}*[发送报文到地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，对端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}[，本端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_315012930}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: HASH]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Quick]{lang="EN-US"}

[  flags: \[ENCRYPT\]]{lang="EN-US"}

[  message ID: 8a9c07c1]{lang="EN-US"}

[  length: 156]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x431076179}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1770059894}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1059120244}*[下一个载荷为：]{style="font-family:宋体"}[HASH]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_894578991}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x267290930}*[协商模式为：]{style="font-family:宋体"}[Quick]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x776462177}*[标识为：]{style="font-family:宋体"}[\[ENCRYPT\]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_315209538}*[为：]{style="font-family:宋体"}[8a9c07c1]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2104240752}*[长度为：]{style="font-family:宋体"}[156]{lang="EN-US"}*

[[\*Aug 20 19:18:34:189 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1955799575}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1412550131}*[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received packet from 192.168.222.5 source port 500 destination port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1208810367}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x788919098}*[收到的]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[报文，源端口为]{style="font-family:宋体"}[500]{lang="EN-US"}[，目的端口为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_315144002}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: HASH]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Quick]{lang="EN-US"}

[  flags: \[ENCRYPT\]]{lang="EN-US"}

[  message ID: 8a9c07c1]{lang="EN-US"}

[  length: 156]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_756292881}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_790664789}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1394579706}*[下一个载荷为：]{style="font-family:宋体"}[HASH]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x763700350}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_595337577}*[协商模式为：]{style="font-family:宋体"}[Quick]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1187853008}*[标识为：]{style="font-family:宋体"}[\[ENCRYPT\]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_315340610}*[为：]{style="font-family:宋体"}[8a9c07c1]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x499359375}*[长度为：]{style="font-family:宋体"}[156]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_177671256}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_42737109}*[加密报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Decrypt IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_983573676}

[ 3b143591 5c647ff2]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x62240366}*[解密]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[3b143591 5c647ff2]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Remote New IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_x1776984274}

[ 4914de5c 11d57f5c]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315275074}*[对端新]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[4914de5c 11d57f5c]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Hash Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x2100749130}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_133547573}*[收到]{style="font-family:宋体"}[ISAKMP Hash ]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Security Asso]{lang="EN-US"}]{#struct_0_x7538_x3345_x508899951}

[ciation Payload.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1297740971}*[收到]{style="font-family:宋体"}[ISAKMP Security Association]{lang="EN-US"}[载荷]{style="font-family:
宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Nonce Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_116529390}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x281562657}*[收到]{style="font-family:宋体"}[ISAKMP Nonce]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload (IPsec DOI).]{lang="EN-US"}]{#struct_0_x7538_x3345_314816323}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1257817757}*[收到]{style="font-family:宋体"}[ISAKMP Identificatio]{lang="EN-US"}[载荷]{style="font-family:宋体"}[(IPsec DOI)]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Received ISAKMP Identification Payload (IPsec DOI).]{lang="EN-US"}]{#struct_0_x7538_x3345_523629519}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1597325991}*[收到]{style="font-family:宋体"}[ISAKMP Identificatio]{lang="EN-US"}[载荷]{style="font-family:宋体"}[(IPsec DOI)]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process HASH payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1029253483}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_179212779}*[处理]{style="font-family:宋体"}[HASH]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec SA payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x969683681}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_310411103}*[处理]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Check IPsec proposal 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_314750787}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1034155185}*[检查]{style="font-family:宋体"}[IPsec proposal]{lang="EN-US"}[，]{style="font-family:宋体"}[proposal]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Parse transform 1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1714434579}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2067261595}*[解析]{style="font-family:宋体"}[transform]{lang="EN-US"}[，]{style="font-family:宋体"}[transform]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Encapsulation mode is Tunnel.]{lang="EN-US"}]{#struct_0_x7538_x3345_x192824403}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_641202453}*[封装模式为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in seconds.]{lang="EN-US"}]{#struct_0_x7538_x3345_337951247}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_2137265695}*[生命周期类型为]{style="font-family:宋体"}[Life type in seconds]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 3600.]{lang="EN-US"}]{#struct_0_x7538_x3345_314947395}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1612695360}*[生命周期为]{style="font-family:宋体"}[3600]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Lifetime type is Life type in kilobytes.]{lang="EN-US"}]{#struct_0_x7538_x3345_x1396415827}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x192633674}*[生命周期类型为]{style="font-family:宋体"}[Life type in kilobytes]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Life duration is 1843200.]{lang="EN-US"}]{#struct_0_x7538_x3345_x905066345}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_262265264}*[生命周期为]{style="font-family:宋体"}[1843200]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Authentication algorithm is HMAC-SHA1.]{lang="EN-US"}]{#struct_0_x7538_x3345_x200077094}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_314881859}*[认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1;   Transform ID is HMAC-SHA1.]{lang="EN-US"}]{#struct_0_x7538_x3345_2006441659}

[*[// Transform ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x169374587}*[为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; The attributes are unacceptable.]{lang="EN-US"}]{#struct_0_x7538_x3345_x205655209}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1763129515}*[属性是可接受的]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec ID Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_x183950482}

[*[//  ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x694401705}*[处理]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:193 2012 Sysname IKE/7/PACKET: -MDC=1; Process IPsec ID Payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_315078467}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_785992265}*[处理]{style="font-family:宋体"}[IPsec ID]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Construct HASH(3) payload.]{lang="EN-US"}]{#struct_0_x7538_x3345_1328423739}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1005752622}*[构造]{style="font-family:宋体"}[HASH(3)]{lang="EN-US"}[载荷]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt the packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_747780693}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x405612504}*[加密报文]{style="font-family:宋体"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypt IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_2045053038}

[ 4914de5c 11d57f5c]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1764344509}*[加密]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[4914de5c 11d57f5c]{lang="EN-US"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Encrypted Generate New IV:]{lang="EN-US"}]{#struct_0_x7538_x3345_315012931}

[ ecfa444e ed72ab05]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x431076178}*[加密时新生成的]{style="font-family:宋体"}[IV]{lang="EN-US"}[为]{style="font-family:宋体"}[ecfa444e ed72ab05]{lang="EN-US"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Sending packet to 192.168.222.5, remote port 500, local port 500.]{lang="EN-US"}]{#struct_0_x7538_x3345_1769994358}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_534717715}*[发送报文到地址]{style="font-family:宋体"}[192.168.222.5]{lang="EN-US"}[，对端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}[，本端端口号为]{style="font-family:宋体"}[500]{lang="EN-US"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_x7538_x3345_315209539}

[  I-Cookie: 3519bdda65bfeaaa]{lang="EN-US"}

[  R-Cookie: 078711749a32520c]{lang="EN-US"}

[  next payload: HASH]{lang="EN-US"}

[  version: ISAKMP Version 1.0]{lang="EN-US"}

[  exchange mode: Quick]{lang="EN-US"}

[  flags: \[ENCRYPT\]]{lang="EN-US"}

[  message ID: 8a9c07c1]{lang="EN-US"}

[  length: 52]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x2104240753}*[发起方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[3519bdda65bfeaaa]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_773083780}*[响应方]{style="font-family:宋体"}[cookie]{lang="EN-US"}[为：]{style="font-family:宋体"}[078711749a32520c]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1297506613}*[下一个载荷为：]{style="font-family:宋体"}[HASH]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1347072103}*[版本为：]{style="font-family:宋体"}[ISAKMP Version 1.0]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_1441937778}*[协商模式为：]{style="font-family:宋体"}[Quick]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_197065643}*[标识为：]{style="font-family:宋体"}[\[ENCRYPT\]]{lang="EN-US"}*

[*[// Message ID]{lang="EN-US"}*]{#struct_0_x7538_x3345_x1381699484}*[为：]{style="font-family:宋体"}[8a9c07c1]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_315144003}*[长度为：]{style="font-family:宋体"}[52]{lang="EN-US"}*

[[\*Aug 20 19:18:34:194 2012 Sysname IKE/7/PACKET: -MDC=1; Sending an IPv4 packet.]{lang="EN-US"}]{#struct_0_x7538_x3345_756292880}

[*[// ]{lang="EN-US"}*]{#struct_0_x7538_x3345_790664790}*[发送一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
