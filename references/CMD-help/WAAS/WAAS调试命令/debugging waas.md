::: {#-1838545339 .myid}
[]{#_Toc404787356}[]{#struct_0_17480_x4622_410452145}[]{#_Toc320977758}[]{#_Toc320977705}[]{#_Toc320977672}[]{#_Toc320977658}[]{#_Toc320956813}

**WAAS \-- WAAS调试命令 \-- debugging waas**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17480_x4622_x1019903064}

[**[debugging]{lang="EN-US"}**[ **waas** { **all** \| **dre** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17480_x4622_1533660300}

[**[undo]{lang="EN-US"}**[ **debugging** **waas** { **all** \| **dre** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_17480_x4622_x1675291432}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17480_x4622_1854609230}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17480_x4622_2110008409}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17480_x4622_139828604}

[[network-admin]{lang="EN-US"}]{#struct_0_17480_x4622_1209025065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17480_x4622_x2033685769}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17480_x4622_x290536290}

[**[all]{lang="EN-US"}**]{#struct_0_17480_x4622_x342225083}[：表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[dre]{lang="EN-US"}**]{#struct_0_17480_x4622_x795954477}[：表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据冗余消除调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17480_x4622_x1518733070}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17480_x4622_1477235693}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_17480_x4622_x343305455}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17480_x4622_757445409}

[**[debugging]{lang="EN-US"}**[ **waas**]{lang="EN-US"}]{#struct_0_17480_x4622_x2014188287}[命令用来打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **waas**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_17480_x4622_131039388}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging waas dre]{lang="FR"}]{#struct_0_17480_x4622_x618874946}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x439426243}[[字段]{style="font-family:黑体"}]{#struct_0_17480_x4622_x653810296}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17480_x4622_432665365}

[[The matching policy action is *ability*. The TFO global switch is *cfgswitch*. IPv4/IPv6 TCP packet: src=*ip*/*port*, dst=*ip*/*port*, payload length=*len.*]{lang="FR"}]{#struct_0_17480_x4622_370113905}

[[收到匹配]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1618922314}[WAAS]{lang="FR"}[策略的报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[其中策略引用的]{style="font-family:宋体"}[class]{lang="FR"}[的优化方式为]{style="font-family:宋体"}*[ability]{lang="FR"}*[，]{style="font-family:宋体"}[配置的]{style="font-family:宋体"}[WAAS]{lang="FR"}[全局优化开关为]{style="font-family:宋体"}*[cfgswitch]{lang="FR"}*[。基于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[报文：源]{style="font-family:宋体"}[I]{lang="EN-US"}[Pv4/IPv6]{lang="FR"}[地址和端口号为]{style="font-family:宋体"}*[ip]{lang="FR"}*[/*port*]{lang="FR"}[，]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IPv4/IPv6]{lang="FR"}[地址和端口号为]{style="font-family:宋体"}*[ip]{lang="FR"}*[/*port*]{lang="FR"}[，]{style="font-family:宋体"}[载荷长度为]{style="font-family:宋体"}*[len]{lang="FR"}[。]{style="font-family:宋体"}[ability]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NONE]{lang="EN-US"}]{#struct_0_17480_x4622_x1063384892}[：无优化能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFO]{lang="EN-US"}]{#struct_0_17480_x4622_258042231}[：]{style="font-family:宋体"}[TFO]{lang="EN-US"}[传输优化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_x1986756035}[：数据冗余消除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_1352982970}[：]{lang="EN-US" style="font-family:宋体"}[LZ]{lang="EN-US"}[压缩]{lang="EN-US" style="font-family:宋体"}

[[不对报文进行优化，显示为]{style="font-family:宋体"}[NONE]{lang="EN-US"}]{#struct_0_17480_x4622_x261670217}[；对报文进行优化，]{style="font-family:宋体"}[TFO]{lang="EN-US"}[为必选，]{style="font-family:宋体"}[DRE]{lang="EN-US"}[和]{style="font-family:宋体"}[LZ]{lang="EN-US"}[可选，可取二者的组合。]{style="font-family:宋体"}

[*[cfgswitch]{lang="EN-US"}*]{#struct_0_17480_x4622_x374726267}[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_x1098990014}[：打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[消除数据冗余功能全局开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_947208995}[：打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据压缩功能全局开关]{style="font-family:宋体"}

 

[[The original data was divided into *blocknum* blocks, of which *createdictnum* new dictionary entries were created and *matchdictnum* entries were matched]{lang="FR"}[.]{lang="EN-US"}]{#struct_0_17480_x4622_1892563231}

[[原始数据进行]{style="font-family:宋体"}[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_555678264}[滑动分块处理。原始数据被切割成]{style="font-family:宋体"}*[blocknum]{lang="FR"}*[块，其中新创建的字典表项数为]{style="font-family:宋体"}*[createdictnum]{lang="FR"}*[，匹配的字典表项数为]{style="font-family:宋体"}*[matchdictnum]{lang="FR"}*

 

[[DRE compressing, transmitted ]{lang="FR"}*[orglen ]{lang="EN-US"}*[bytes]{lang="EN-US"}]{#struct_0_17480_x4622_465709953}[.]{lang="FR"}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_153698379}[压缩时，重传未确认的]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节数据]{style="font-family:宋体"}

 

[[Fast compressing compressed *orglen* bytes to *cmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_x1611560811}

[[快速压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*]{#struct_0_17480_x4622_x1775091823}[字节的数据压缩为]{style="font-family:宋体"}*[cmplen]{lang="EN-US"}*[字节。进行快速压缩的情况包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[报文过短，长度小于最小支持压缩数据大小（]{style="font-family:宋体"}]{#struct_0_17480_x4622_647267474}[64]{lang="EN-US"}[字节）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MSS]{lang="EN-US"}]{#struct_0_17480_x4622_x115873596}[（]{lang="EN-US" style="font-family:宋体"}[Maximum Segment Size]{lang="EN-US"}[，最大报文段长度）值小于能接受的最小]{lang="EN-US" style="font-family:
  宋体"}[MSS]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[285]{lang="EN-US"}[字节）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_x1781674360}[压缩失败]{style="font-family:宋体"}

 

[[DRE compressed *orglen* bytes to *cmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_2067697171}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_x240683059}[压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节的数据压缩为]{style="font-family:宋体"}*[cmplen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[LZ was not performed: Insufficient compression buffer after DRE.]{lang="EN-US"}]{#struct_0_17480_x4622_296393976}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_366679487}[压缩处理后，再进行]{style="font-family:宋体"}[LZ]{lang="EN-US"}[压缩处理时压缩缓冲区不足，放弃]{style="font-family:宋体"}[LZ]{lang="EN-US"}[压缩]{style="font-family:宋体"}

 

[[DRE and LZ compressed *orglen* bytes to *cmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_x239329827}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_1679954545}[和]{style="font-family:宋体"}[LZ]{lang="EN-US"}[压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节的数据压缩为]{style="font-family:宋体"}*[cmplen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[DRE and LZ decompressed *orglen* bytes to *decmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_897975887}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_x746870354}[和]{style="font-family:宋体"}[LZ]{lang="EN-US"}[解压处理，将长度为]{style="font-family:宋体"}[orglen]{lang="EN-US"}[字节的数据解压为]{style="font-family:宋体"}*[decmplen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[Performing fast compression after LZ failed: Insufficient compression buffer.]{lang="EN-US"}]{#struct_0_17480_x4622_496870301}

[[压缩缓冲区不足，导致]{style="font-family:宋体"}[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_x105472770}[压缩失败，尝试进行快速压缩处理]{style="font-family:宋体"}

 

[[LZ compressed *orglen* bytes to *cmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_x1800796111}

[[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_x351456684}[压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节的数据压缩为]{style="font-family:宋体"}*[cmplen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[LZ decompressed *orglen* bytes to *decmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_1052129007}

[[LZ]{lang="EN-US"}]{#struct_0_17480_x4622_x1915005649}[解压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节的数据解压为]{style="font-family:宋体"}[decmplen]{lang="EN-US"}[字节]{style="font-family:宋体"}

 

[[Compression was not performed: Data of *orglen* bytes is too short.]{lang="EN-US"}]{#struct_0_17480_x4622_1214641532}

[[长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*]{#struct_0_17480_x4622_2062954242}[字节的数据太短，放弃压缩]{style="font-family:宋体"}

 

[[DRE decompressed *orglen* bytes to *decmplen* bytes.]{lang="EN-US"}]{#struct_0_17480_x4622_1572739178}

[[DRE]{lang="EN-US"}]{#struct_0_17480_x4622_x1063904469}[解压缩处理，将长度为]{style="font-family:宋体"}*[orglen]{lang="EN-US"}*[字节的数据解压为]{style="font-family:宋体"}*[decmplen]{lang="EN-US"}*[字节]{style="font-family:宋体"}

 

[[The peer has acknowledged *len* bytes of data, synchronizing and matching *ackdictnum* dictionary entries.]{lang="EN-US"}]{#struct_0_17480_x4622_1319644228}

[[对端确认了]{style="font-family:宋体"}*[len]{lang="EN-US"}*]{#struct_0_17480_x4622_1012520781}[字节数据，这些数据匹配、创建]{style="font-family:宋体"}*[ackdictnum]{lang="EN-US"}*[个表项]{style="font-family:宋体"}

 

[ ]{lang="FR"}

[[表1-2 ]{lang="EN-US"}[debugging waas error]{lang="FR"}]{#struct_0_17480_x4622_x1316748150}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x441943463}[[字段]{style="font-family:黑体"}]{#struct_0_17480_x4622_700487225}

[[描述]{style="font-family:黑体"}]{#struct_0_17480_x4622_x1568988615}

[[Failed to delete a matching rule of the class from kernel.]{lang="FR"}]{#struct_0_17480_x4622_1210421632}

[[从内核删除]{style="font-family:宋体"}[class]{lang="EN-US"}]{#struct_0_17480_x4622_1039044615}[的]{style="font-family:宋体"}[match]{lang="EN-US"}[规则失败]{style="font-family:宋体"}

 

[[Creating class *name* failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_140705477}

[[内存不足，导致创建名为]{style="font-family:宋体"}]{#struct_0_17480_x4622_x395970981}*[name]{lang="FR"}*[的]{style="font-family:宋体"}[class]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Creating a matching rule for the class failed:Insufficient memory.]{lang="EN-US"}]{#struct_0_17480_x4622_409675410}

[[内存不足，导致创建]{style="font-family:宋体"}[class]{lang="EN-US"}]{#struct_0_17480_x4622_180754043}[的]{style="font-family:宋体"}[match]{lang="EN-US"}[规则失败]{style="font-family:宋体"}

 

[[Failed to create an instance for class]{lang="EN-US"}]{#struct_0_17480_x4622_767173446}*[ name]{lang="FR"}*[.]{lang="EN-US"}

[[实例化名为]{style="font-family:宋体"}]{#struct_0_17480_x4622_1831595301}*[name]{lang="FR"}*[的]{style="font-family:宋体"}[class]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to add a matching rule of the class to kernel.]{lang="EN-US"}]{#struct_0_17480_x4622_x936456847}

[[向内核添加]{style="font-family:宋体"}[class]{lang="EN-US"}]{#struct_0_17480_x4622_x1131677343}[的]{style="font-family:宋体"}[match]{lang="EN-US"}[规则失败]{style="font-family:宋体"}

 

[[Failed to add class ]{lang="EN-US"}]{#struct_0_17480_x4622_x1271629932}*[name]{lang="FR"}*[ to kernel.]{lang="EN-US"}

[[向内核添加名为]{style="font-family:宋体"}]{#struct_0_17480_x4622_77482010}*[name]{lang="FR"}*[的]{style="font-family:宋体"}[class]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to delete class ]{lang="EN-US"}]{#struct_0_17480_x4622_x1696552980}*[name]{lang="FR"}*[ from kernel.]{lang="EN-US"}

[[从内核删除]{style="font-family:宋体"}[class ]{lang="EN-US"}]{#struct_0_17480_x4622_1706789418}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Recovering class *name* from DBM failed: Insufficient memory.]{lang="EN-US"}]{#struct_0_17480_x4622_x808502022}

[[内存不足，导致从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_17480_x4622_188483595}[配置恢复]{style="font-family:宋体"}[class ]{lang="EN-US"}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Recovering class a matching rule from DBM failed: Insufficient memory.]{lang="EN-US"}]{#struct_0_17480_x4622_314621300}

[[内存不足，导致从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_17480_x4622_1044235895}[配置恢复]{style="font-family:宋体"}[class]{lang="EN-US"}[的]{style="font-family:宋体"}[match]{lang="EN-US"}[规则失败]{style="font-family:宋体"}

 

[[Failed to push the data of class to kernel.]{lang="EN-US"}]{#struct_0_17480_x4622_x1706629570}

[[class]{lang="EN-US"}]{#struct_0_17480_x4622_x1829248117}[数据下内核失败]{style="font-family:宋体"}

 

[[Failed to add session extension information to the session handle.]{lang="EN-US"}]{#struct_0_17480_x4622_x1918963404}

[[添加会话扩展信息到会话句柄上失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1366919848}

 

[[Failed to set up a TCP listening handle.]{lang="EN-US"}]{#struct_0_17480_x4622_x1022093937}

[[创建监听]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_283952500}[句柄失败]{style="font-family:宋体"}

 

[[Failed to modify the IPv4/IPv6 option of *option*.]{lang="EN-US"}]{#struct_0_17480_x4622_x1898593866}

[[修改]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}]{#struct_0_17480_x4622_184288136}[连接选项]{style="font-family:宋体"}*[option]{lang="EN-US"}*[失败。]{style="font-family:宋体"}*[option]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[base-congestion-window]{lang="EN-US"}]{#struct_0_17480_x4622_828487535}[：]{style="font-family:宋体"}[设置]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[获取窗口大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[receive-buffer]{lang="EN-US"}]{#struct_0_17480_x4622_817158415}[：]{style="font-family:宋体"}[设置进入慢启动的拥塞窗口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[keepalive]{lang="EN-US"}]{#struct_0_17480_x4622_452272306}[：]{style="font-family:宋体"}[设置保活定时器是否使能]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to enable WAAS forwarding.]{lang="EN-US"}]{#struct_0_17480_x4622_x1457357548}

[[使能]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_17480_x4622_543990004}[业务转发点失败]{style="font-family:宋体"}

 

[[Failed to get WAAS global status.]{lang="EN-US"}]{#struct_0_17480_x4622_x1921973492}

[[获取]{style="font-family:宋体"}[WAAS]{lang="EN-US"}]{#struct_0_17480_x4622_x1967055532}[全局统计信息失败]{style="font-family:宋体"}

 

[[Failed to add the application of the WAAS policy on interface *interface-name* to kernel.]{lang="EN-US"}]{#struct_0_17480_x4622_x696447188}

[[向内核添加接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17480_x4622_173578951}[应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略失败]{style="font-family:宋体"}

 

[[Failed to apply the WAAS policy *name* to interface *interface-name*.]{lang="EN-US"}]{#struct_0_17480_x4622_1520256245}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17480_x4622_1429293807}[应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略]{style="font-family:宋体"}*[name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to delete the application of the WAAS policy on interface *interface-name* from kernel.]{lang="EN-US"}]{#struct_0_17480_x4622_2110073945}

[[从内核删除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_17480_x4622_1750309591}[应用]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[策略失败]{style="font-family:宋体"}

 

[[Adding IPv4/IPv6 blacklist entries failed:Insufficient memory.]{lang="EN-US"}]{#struct_0_17480_x4622_x1242737305}

[[内存不足，导致添加]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}]{#struct_0_17480_x4622_x2135608740}[的黑名单表项失败]{style="font-family:宋体"}

 

[[Failed to create a new IPv4/IPv6 blacklist.]{lang="EN-US"}]{#struct_0_17480_x4622_1182902034}

[[创建新的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}]{#struct_0_17480_x4622_904236308}[黑名单表失败]{style="font-family:宋体"}

[]{#_GoBack}

 

[[Processing the REQUESTFAIL event failed: Insufficient infomation.]{lang="EN-US"}]{#struct_0_17480_x4622_707652974}

[[获取信息不足，导致响应]{style="font-family:宋体"}[REQUESTFAIL]{lang="EN-US"}]{#struct_0_17480_x4622_x618809410}[事件失败]{style="font-family:宋体"}

 

[[Failed to accept a new connection.]{lang="EN-US"}]{#struct_0_17480_x4622_x1405615266}

[[接受新连接失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1860316209}

 

[[Creating local/peer dictionary entries failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x1128441668}

[[内存不足，导致创建本端]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1116921148}[/]{lang="FR"}[对端数据字典表项失败]{style="font-family:宋体"}

 

[[Adding meta data failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_551566417}

[[内存不足，导致添加本端]{style="font-family:宋体"}]{#struct_0_17480_x4622_1579599701}[/]{lang="FR"}[对端数据字典元数据失败]{style="font-family:宋体"}

 

[[Failed to save local/peer dictionary entries.]{lang="FR"}]{#struct_0_17480_x4622_947274531}

[[保存本端]{style="font-family:宋体"}]{#struct_0_17480_x4622_x2077904768}[/]{lang="FR"}[对端数据字典表项失败]{style="font-family:宋体"}

 

[[Creating a link node for the unacknowledged dictionary entries failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x164579288}

[[内存不足，导致创建包含未确认数据字典表项信息的链表节点失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_913502448}

 

[[DRE decompress failed: The dictionary has been deleted.]{lang="FR"}]{#struct_0_17480_x4622_26239039}

[[数据字典已被释放，导致]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1781608824}[DRE]{lang="FR"}[解压缩失败]{style="font-family:宋体"}

 

[[DRE decompress failed: Insufficient decompression buffer.]{lang="FR"}]{#struct_0_17480_x4622_1711013977}

[[DRE]{lang="FR"}]{#struct_0_17480_x4622_1728489306}[解压缩缓冲区不足，导致]{style="font-family:宋体"}[DRE]{lang="FR"}[解压缩失败]{style="font-family:宋体"}

 

[[DRE decompress failed: The dictionary entry not found.]{lang="FR"}]{#struct_0_17480_x4622_699288782}

[[查找数据字典表项失败，导致]{style="font-family:宋体"}]{#struct_0_17480_x4622_791195853}[DRE]{lang="FR"}[解压缩失败]{style="font-family:宋体"}

 

[[DRE decompress failed: MD5 authentication failed.]{lang="FR"}]{#struct_0_17480_x4622_x926576285}

[[MD5]{lang="FR"}]{#struct_0_17480_x4622_496935837}[验证失败，导致]{style="font-family:宋体"}[DRE]{lang="FR"}[解压缩失败]{style="font-family:宋体"}

 

[[Failed to add new dictionary entries during DRE decompression.]{lang="EN-US"}]{#struct_0_17480_x4622_x1241540149}

[[DRE]{lang="FR"}]{#struct_0_17480_x4622_1857535256}[解压缩时，添加新的字典表项失败]{style="font-family:宋体"}

 

[[DRE compress failed: The peer was not found.]{lang="FR"}]{#struct_0_17480_x4622_1136975204}

[[从]{style="font-family:宋体"}]{#struct_0_17480_x4622_681626861}[DRE]{lang="FR"}[句柄获取]{style="font-family:宋体"}[peer]{lang="FR"}[节点失败，导致]{style="font-family:宋体"}[DRE]{lang="FR"}[压缩失败]{style="font-family:宋体"}

 

[[DRE compress failed: The dictionary has been deleted.]{lang="FR"}]{#struct_0_17480_x4622_2063019778}

[[数据字典已被释放，导致]{style="font-family:宋体"}]{#struct_0_17480_x4622_73144085}[DRE]{lang="FR"}[压缩失败]{style="font-family:宋体"}

 

[[Compress failed: The peer was not found.]{lang="FR"}]{#struct_0_17480_x4622_45521270}

[[获取]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1878006669}[peer]{lang="FR"}[节点失败，导致压缩失败]{style="font-family:宋体"}

 

[[Decompress failed: The peer was not found.]{lang="FR"}]{#struct_0_17480_x4622_441672219}

[[获取]{style="font-family:宋体"}]{#struct_0_17480_x4622_140771013}[peer]{lang="FR"}[节点失败，导致解压缩失败]{style="font-family:宋体"}

 

[[Decompression failed: MD5 message error or empty package.]{lang="EN-US"}]{#struct_0_17480_x4622_x1583209588}

[[MD5]{lang="FR"}]{#struct_0_17480_x4622_x13688986}[信息错误或解压缩数据为空，导致解压缩失败。]{style="font-family:宋体"}

 

[[Failed to add peer *peer-id.*]{lang="EN-US"}]{#struct_0_17480_x4622_1442255698}

[[添加]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1100749250}[peer]{lang="FR"}[节点]{style="font-family:宋体"}*[peer-id]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[LZ decompression failed.]{lang="FR"}]{#struct_0_17480_x4622_1706854954}

[[LZ]{lang="FR"}]{#struct_0_17480_x4622_x1553337006}[解压缩失败]{style="font-family:宋体"}

 

[[Creating the peer dictionary failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x928251067}

[[内存不足，导致创建]{style="font-family:宋体"}]{#struct_0_17480_x4622_x711494325}[peer]{lang="FR"}[数据字典失败]{style="font-family:宋体"}

 

[[Failed to create WAAS license reconnecting timer.]{lang="FR"}]{#struct_0_17480_x4622_x1022028401}

[[创建]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1509615268}[WAAS license]{lang="FR"}[重连定时器失败]{style="font-family:宋体"}

 

[[Failed to create WAAS license checking timer.]{lang="FR"}]{#struct_0_17480_x4622_1279016682}

[[创建]{style="font-family:宋体"}]{#struct_0_17480_x4622_763162785}[WAAS license]{lang="FR"}[检查定时器失败]{style="font-family:宋体"}

 

[[Failed to push the data of policy to kernel.]{lang="FR"}]{#struct_0_17480_x4622_x292905830}

[[策略数据下内核失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_544055540}

 

[[Failed to push the data of LocalID to kernel.]{lang="FR"}]{#struct_0_17480_x4622_x1749297818}

[[LocalID]{lang="FR"}]{#struct_0_17480_x4622_2092586882}[数据下内核失败]{style="font-family:宋体"}

 

[[Failed to push the data of TFO to kernel.]{lang="FR"}]{#struct_0_17480_x4622_x1098435203}

[[TFO]{lang="FR"}]{#struct_0_17480_x4622_2110139481}[数据下内核失败]{style="font-family:宋体"}

 

[[Failed to create blacklist aging timer.]{lang="FR"}]{#struct_0_17480_x4622_1704274056}

[[创建黑名单老化定时器失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_1660352156}

 

[[Failed to reset the blacklist aging timer.]{lang="FR"}]{#struct_0_17480_x4622_1687567655}

[[重置黑名单老化定时器失败]{style="font-family:宋体"}]{#struct_0_17480_x4622_x618743874}

 

[[Failed to synchronize instance (type: ]{lang="EN-US"}]{#struct_0_17480_x4622_x621710097}*[type]{lang="FR"}*[) message.]{lang="EN-US"}

[[同步类型为]{style="font-family:宋体"}]{#struct_0_17480_x4622_x474349183}*[type]{lang="FR"}*[的实例化信息失败。]{style="font-family:宋体"}*[type]{lang="FR"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_17480_x4622_x576395085}[：设置]{style="font-family:宋体"}[debug]{lang="EN-US"}[调试开关状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_17480_x4622_947340067}[：添加]{lang="EN-US" style="font-family:宋体"}[class]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_17480_x4622_1057051176}[：删除]{lang="EN-US" style="font-family:宋体"}[class]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_17480_x4622_998355067}[：添加]{lang="EN-US" style="font-family:宋体"}[match]{lang="EN-US"}[规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_17480_x4622_x574057230}[：删除]{lang="EN-US" style="font-family:宋体"}[match]{lang="EN-US"}[规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_17480_x4622_x1781543288}[：添加策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_17480_x4622_707744175}[：删除策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_17480_x4622_x432495107}[：修改策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_17480_x4622_2018745228}[：策略添加]{lang="EN-US" style="font-family:宋体"}[match]{lang="EN-US"}[规则]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_17480_x4622_497001373}[：策略删除]{style="font-family:宋体"}[match]{lang="EN-US"}[规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_17480_x4622_x176253794}[：设置接口应用策略]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[12]{lang="EN-US"}]{#struct_0_17480_x4622_x1885571473}[：设置全局优化开关状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[13]{lang="EN-US"}]{#struct_0_17480_x4622_330356930}[：修改策略优化方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[14]{lang="EN-US"}]{#struct_0_17480_x4622_2063085314}[：设置]{style="font-family:宋体"}[TFO]{lang="EN-US"}[保活开关状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[15]{lang="EN-US"}]{#struct_0_17480_x4622_1975815763}[：设置]{style="font-family:宋体"}[TFO]{lang="EN-US"}[拥塞窗口大小]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_17480_x4622_x76049962}[：设置]{style="font-family:宋体"}[TFO]{lang="EN-US"}[接收缓冲区长度]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[17]{lang="EN-US"}]{#struct_0_17480_x4622_140836549}[：设置自动发现黑名单开关状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[18]{lang="EN-US"}]{#struct_0_17480_x4622_566520589}[：设置]{lang="EN-US" style="font-family:宋体"}[LocalID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[19]{lang="EN-US"}]{#struct_0_17480_x4622_x1274050023}[：配置恢复，]{lang="EN-US" style="font-family:宋体"}[class]{lang="EN-US"}[下内核]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20]{lang="EN-US"}]{#struct_0_17480_x4622_x123886258}[：设置版本号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[21]{lang="EN-US"}]{#struct_0_17480_x4622_1706920490}[：设置黑名单老化时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[22]{lang="EN-US"}]{#struct_0_17480_x4622_380248777}[：添加黑名单]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[23]{lang="EN-US"}]{#struct_0_17480_x4622_1791261118}[：删除黑名单]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[24]{lang="EN-US"}]{#struct_0_17480_x4622_x1021962865}[：清除]{lang="EN-US" style="font-family:宋体"}[DRE]{lang="EN-US"}[缓存]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[25]{lang="EN-US"}]{#struct_0_17480_x4622_x1467062537}[：清除]{lang="EN-US" style="font-family:宋体"}[DRE]{lang="EN-US"}[统计信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[26]{lang="EN-US"}]{#struct_0_17480_x4622_x515011523}[：清除黑名单]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to modify policy *name* action on kernel.]{lang="FR"}]{#struct_0_17480_x4622_544121076}

[[修改内核策略]{style="font-family:宋体"}]{#struct_0_17480_x4622_961426190}*[name]{lang="FR"}*[的优化方式失败]{style="font-family:宋体"}

 

[[Creating an instance for policy *name* failed: Invalid ID.]{lang="FR"}]{#struct_0_17480_x4622_x1043878317}

[[无效的]{style="font-family:宋体"}]{#struct_0_17480_x4622_1220218147}[ID]{lang="FR"}[编号，导致实例化]{style="font-family:宋体"}[WAAS]{lang="FR"}[策略]{style="font-family:宋体"}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Failed to add policy *name* to kernel.]{lang="FR"}]{#struct_0_17480_x4622_2110205017}

[[向内核添加策略]{style="font-family:宋体"}]{#struct_0_17480_x4622_145643060}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Failed to delete policy *name* from kernel.]{lang="FR"}]{#struct_0_17480_x4622_1853432973}

[[删除内核策略]{style="font-family:宋体"}]{#struct_0_17480_x4622_x618678338}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Failed to add/delete match *ID* on kernel.]{lang="FR"}]{#struct_0_17480_x4622_x240289867}

[[添加]{style="font-family:宋体"}]{#struct_0_17480_x4622_947405603}[/]{lang="FR"}[删除内核]{style="font-family:宋体"}[ID]{lang="FR"}[为]{style="font-family:宋体"}*[ID]{lang="FR"}*[ ]{lang="FR"}[的]{style="font-family:宋体"}[match]{lang="FR"}[规则失败]{style="font-family:宋体"}

 

[[Adding a matching rule failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x637268430}

[[内存不足，导致]{style="font-family:宋体"}]{#struct_0_17480_x4622_1239844551}[class]{lang="FR"}[添加]{style="font-family:宋体"}[match]{lang="FR"}[规则失败]{style="font-family:宋体"}

 

[[Adding policy *name* failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x1781477752}

[[内存不足，导致添加策略]{style="font-family:宋体"}]{#struct_0_17480_x4622_x935495867}*[name]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Recovering policy *name* from DBM failed: Insufficient memory.]{lang="FR"}]{#struct_0_17480_x4622_x187786350}

[[内存不足，导致从]{style="font-family:宋体"}]{#struct_0_17480_x4622_497066909}[DBM]{lang="FR"}[恢复策略]{style="font-family:宋体"}*[name]{lang="FR"}*[数据失败]{style="font-family:宋体"}

 

[ ]{lang="FR"}

[[表1-3 ]{lang="EN-US"}[debugging waas event]{lang="FR"}]{#struct_0_17480_x4622_1405880144}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x430298165}[[字段]{style="font-family:黑体"}]{#struct_0_17480_x4622_x1873861914}

[[描述]{style="font-family:黑体"}]{#struct_0_17480_x4622_x1999445888}

[[State of Memory-alert-gate is minor.]{lang="FR"}]{#struct_0_17480_x4622_497506215}

[[内存门限一级告警]{style="font-family:宋体"}]{#struct_0_17480_x4622_339740983}

 

[[State of Memory-alert-gate is severe.]{lang="FR"}]{#struct_0_17480_x4622_x1306314951}

[[内存门限二级告警]{style="font-family:宋体"}]{#struct_0_17480_x4622_x230858665}

 

[[State of Memory-alert-gate is critical.]{lang="EN-US"}]{#struct_0_17480_x4622_x468219923}

[[内存门限三级告警]{style="font-family:宋体"}]{#struct_0_17480_x4622_1667362915}

 

[[State of Memory-alert-gate changed to severe.]{lang="EN-US"}]{#struct_0_17480_x4622_133381411}

[[内存门限变为二级告警]{style="font-family:宋体"}]{#struct_0_17480_x4622_800866726}

 

[[State of Memory-alert-gate changed to ]{lang="EN-US"}]{#struct_0_17480_x4622_2063150850}[minor]{lang="FR"}[.]{lang="EN-US"}

[[内存门限变为一级告警]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1880668443}

 

[[State of Memory-alert-gate changed to normal.]{lang="EN-US"}]{#struct_0_17480_x4622_331796088}

[[内存门限恢复正常]{style="font-family:宋体"}]{#struct_0_17480_x4622_x771097724}

 

[[WAAS processes ifevent\[*ifevent*\].]{lang="EN-US"}]{#struct_0_17480_x4622_x1892726621}

[[WAAS]{lang="EN-US"}]{#struct_0_17480_x4622_x801138686}[处理接口事件]{style="font-family:宋体"}*[ifevent]{lang="EN-US"}[。]{style="font-family:宋体"}[ifevent]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17480_x4622_710055343}[：接口批量激活]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[deactive]{lang="EN-US"}]{#struct_0_17480_x4622_32216361}[：接口批量去激活]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_17480_x4622_343161517}[：接口批量删除]{style="font-family:宋体"}

 

[[The ifindex\[*index*\] ifevent\[*ifevent*\] failed.]{lang="EN-US"}]{#struct_0_17480_x4622_140902085}

[[接口索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*]{#struct_0_17480_x4622_x1418583059}[的接口处理接口事件]{style="font-family:宋体"}[i*fevent*]{lang="EN-US"}[失败。]{style="font-family:宋体"}*[ifevent]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_17480_x4622_x1108547912}[：接口激活]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[deactive]{lang="EN-US"}]{#struct_0_17480_x4622_x1372987793}[：接口去激活]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="FR"}]{#struct_0_17480_x4622_743479401}[：接口删除]{style="font-family:宋体"}

 

[[Connection\[*info*\] received event *event* while the focusing event is e*vent*.]{lang="FR"}]{#struct_0_17480_x4622_x1617614747}

[[收到]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1947630345}[TCP]{lang="FR"}[连接事件，连接信息为]{style="font-family:宋体"}*[info]{lang="FR"}[。]{style="font-family:宋体"}*[TCP]{lang="FR"}[句柄收到事件]{style="font-family:宋体"}*[event]{lang="FR"}*[，监听事件是]{style="font-family:宋体"}*[event]{lang="FR"}*[。]{style="font-family:宋体"}*[info]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}*[。]{style="font-family:宋体"}[event]{lang="FR"}*[取以下值或以下值的组合：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DATAREADY]{lang="EN-US"}]{#struct_0_17480_x4622_24724764}[，数据到达事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WRITESPACE]{lang="EN-US"}]{#struct_0_17480_x4622_x1802837873}[，数据可写事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ERRORREPORT]{lang="EN-US"}]{#struct_0_17480_x4622_1706986026}[，连接关闭事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUESTFAIL]{lang="EN-US"}]{#struct_0_17480_x4622_799869946}[，连接建立失败事件]{lang="EN-US" style="font-family:宋体"}

 

[[Processing REQUESTFAIL event.]{lang="EN-US"}]{#struct_0_17480_x4622_1168319628}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_1017979828}[连接建立失败事件]{style="font-family:宋体"}

 

[[Processing ERRORREPORT event on connection\[*info*\].]{lang="FR"}]{#struct_0_17480_x4622_1488073785}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_1590100687}[连接关闭事件，连接信息为]{style="font-family:宋体"}*[info]{lang="FR"}[。]{style="font-family:宋体"}[info]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Accepted a new connection\[*info*\].]{lang="FR"}]{#struct_0_17480_x4622_1670142085}

[[接受一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_x1021897329}[新连接，连接信息为]{style="font-family:宋体"}*[info]{lang="FR"}[。]{style="font-family:宋体"}[info]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Processing DATAREADY event on connection\[*info*\].]{lang="FR"}]{#struct_0_17480_x4622_x360653723}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_x954499243}[连接上的数据到达事件，连接信息为]{style="font-family:宋体"}*[info]{lang="FR"}[。]{style="font-family:宋体"}[inf]{lang="FR"}*[o]{lang="EN-US"}[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Processing WRITESPACE event on connection\[*info*\].]{lang="FR"}]{#struct_0_17480_x4622_x1720507702}

[[处理]{style="font-family:宋体"}]{#struct_0_17480_x4622_x951796833}[TCP]{lang="FR"}[连接可写事件，连接信息为]{style="font-family:宋体"}[info]{lang="FR"}*[。]{style="font-family:宋体"}[info]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[ ]{lang="FR"}

[[表1-4 ]{lang="EN-US"}[debugging waas packet]{lang="FR"}]{#struct_0_17480_x4622_560150285}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x436031161}[[字段]{style="font-family:黑体"}]{#struct_0_17480_x4622_1410017815}

[[描述]{style="font-family:黑体"}]{#struct_0_17480_x4622_1670871487}

[[Failed to send *packetnum* packet(s) while processing DATAREADY event on connection\[*packet*\].]{lang="FR"}]{#struct_0_17480_x4622_295616363}

[[处理]{style="font-family:宋体"}]{#struct_0_17480_x4622_x1462977957}[TCP]{lang="FR"}[数据到达事件时，发送]{style="font-family:宋体"}*[packetnum]{lang="FR"}*[个数据包失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="FR"}[。]{style="font-family:宋体"}[packet]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Sent *packetnum* packet(s) while processing DATAREADY event on connection\[*packet*\].]{lang="FR"}]{#struct_0_17480_x4622_544186612}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_x2142472758}[数据到达事件时，成功发送]{style="font-family:宋体"}*[packetnum]{lang="FR"}*[个数据包，报文信息为]{style="font-family:宋体"}*[packet]{lang="FR"}[。]{style="font-family:宋体"}[packet]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Failed to send *packetnum* packet(s) while processing WRITESPACE event on connection\[*packet*\].]{lang="FR"}]{#struct_0_17480_x4622_x710510056}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_114283136}[连接可写事件，发送]{style="font-family:宋体"}*[packetnum]{lang="FR"}*[个数据包失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="FR"}[。]{style="font-family:宋体"}[packet]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[[Sent *packetnum* packet(s) while processing WRITESPACE event on connection\[*packet*\].]{lang="FR"}]{#struct_0_17480_x4622_101824367}

[[处理]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_17480_x4622_1404413847}[连接可写事件，成功发送]{style="font-family:宋体"}*[packetnum]{lang="FR"}*[个数据包，报文信息为]{style="font-family:宋体"}*[packet]{lang="FR"}[。]{style="font-family:宋体"}[packet]{lang="FR"}*[形式为]{style="font-family:宋体"}[srcaddr/srcport -\> dstaddr/dstport]{lang="FR"}

 

[ ]{lang="FR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17480_x4622_x260198713}

[[\# ]{lang="EN-US"}]{#struct_0_17480_x4622_x719160342}[打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[错误调试信息开关。添加]{style="font-family:宋体"}[peer]{lang="EN-US"}[字典表项，内存不足时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging waas error]{lang="EN-US"}]{#struct_0_17480_x4622_330224149}

[\*Sep 19 09:55:52:338 2014 Sysname WAAS/7/ERROR: Adding peer dictionary entries failed : Insufficient memory]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17480_x4622_1339527112}*[添加]{style="font-family:宋体"}[peer]{lang="EN-US"}[字典表项失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17480_x4622_369276584}[打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[事件调试信息开关。内存进入二级门限时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging waas event]{lang="EN-US"}]{#struct_0_17480_x4622_1229499938}

[\*Aug 14 01:10:08:790 2014 Sysname WAAS/7/EVENT: -MDC=1; State of Memory-alert-gate is severe.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17480_x4622_x823046960}*[达到内存门限二级告警]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17480_x4622_x22931652}[打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[数据冗余消除调试信息开关。]{style="font-family:宋体"}[DRE]{lang="EN-US"}[解压缩处理时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging waas dre]{lang="EN-US"}]{#struct_0_17480_x4622_2110270553}

[\*Aug 14 01:10:08:790 2014 Sysname WAAS/7/DRE: -MDC=1; DRE decompressed 306 bytes to 280 bytes.]{lang="EN-US"}

[*[// DRE]{lang="EN-US"}*]{#struct_0_17480_x4622_2111830111}*[解压缩时]{style="font-family:宋体"}[,]{lang="EN-US"}[将]{style="font-family:宋体"}[306]{lang="EN-US"}[字节解压成]{style="font-family:宋体"}[280]{lang="EN-US"}[字节]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17480_x4622_x1008011363}[打开]{style="font-family:宋体"}[WAAS]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接上收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging waas packet]{lang="EN-US"}]{#struct_0_17480_x4622_x534947528}

[\*Aug 14 01:10:08:660 2014 Sysname WAAS/7/PACKET: -MDC=1; Sent 1 packet(s) while processing DATAREADY event on connection\[192.168.27.1/80 -\> 192.168.17.1/2900\]. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17480_x4622_x263748312}*[收到]{style="font-family:宋体"}[DATAREADY]{lang="EN-US"}[事件，在源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[192.168.27.1/80]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[192.168.10.1/2900]{lang="EN-US"}[的连接上，成功发送一个报文]{style="font-family:宋体"}*

[[\*Aug 14 01:10:08:792 2014 Sysname WAAS/7/PACKET: -MDC=1; Connection\[192.168.27.1/80 -\> 192.168.17.1/2901\] received event \[DATAREADY\] while the focusing event is \[DATAREADY\]\[ERRORREPORT\].]{lang="EN-US"}]{#struct_0_17480_x4622_725843088}

[*[// ]{lang="EN-US"}*]{#struct_0_17480_x4622_x1309734241}*[收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听事件，在源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[192.168.27.1/80]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[192.168.17.1/2901]{lang="EN-US"}[的连接上监听]{style="font-family:宋体"}[DATAREADY]{lang="EN-US"}[和]{style="font-family:宋体"}[ERRORREPORT]{lang="EN-US"}[事件时，收到]{style="font-family:宋体"}[DATAREADY]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
