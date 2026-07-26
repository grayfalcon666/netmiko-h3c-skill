::: {#1963437492 .myid}
[]{#_Toc404786253}[]{#struct_0_x1378_16565_x967610306}[]{#_Toc205700592}[]{#_Toc205697805}

**域名解析 \-- 域名解析调试命令 \-- debugging dns**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1378_16565_2056987014}

[**[debugging dns]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1378_16565_x942151927}

[**[undo debugging dns]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1378_16565_x1318156956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x239165826}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1378_16565_x1010984185}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x1654942081}

[[network-admin]{lang="EN-US"}]{#struct_0_x1378_16565_x1678275081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1378_16565_x608463242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1378_16565_1624341706}

[**[all]{lang="EN-US"}**]{#struct_0_x1378_16565_x967675842}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1378_16565_x1525847919}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1378_16565_x2035237365}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1378_16565_x994812057}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x1321452178}

[**[debugging dns]{lang="EN-US"}**]{#struct_0_x1378_16565_x1439737581}[命令用来打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[**[undo debugging dns]{lang="EN-US"}**]{#struct_0_x1378_16565_x204451903}[命令用来关闭]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x920164867}[服务器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging dns packet]{lang="EN-US"}]{#struct_0_x1378_16565_x105959837}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1650709824}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_x967741378}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_481400321}

[[Header:]{lang="EN-US"}]{#struct_0_x1378_16565_1813615186}

[[ ID = *id*, QR = *qr*, OpCode = *opcode*, AA = *aa*, TC = *tc*, RD = *rd* ]{lang="EN-US"}]{#struct_0_x1378_16565_x429956420}

[[ RA = *ra*, Z = *zero*, AD = *ad*, CD = *cd*, RCode = *rcode* ]{lang="EN-US"}]{#struct_0_x1378_16565_x848684923}

[[QDCount = *qdcount* ]{lang="EN-US"}]{#struct_0_x1378_16565_x1948696798}

[[ANCount = *ancount* ]{lang="EN-US"}]{#struct_0_x1378_16565_1362713756}

[[NSCount = *nscount* ]{lang="EN-US"}]{#struct_0_x1378_16565_x966758338}

[[ARCount = *arcount*]{lang="EN-US"}]{#struct_0_x1378_16565_2056289426}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x627947383}[报文头部分的内容：]{style="font-family:宋体"}

[[标识字段为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x1378_16565_x814838487}[，报文类型字段为]{style="font-family:宋体"}*[qr]{lang="EN-US"}*[，]{style="font-family:宋体"}[OpCode]{lang="EN-US"}[为]{style="font-family:宋体"}*[opcode]{lang="EN-US"}*[，授权回答字段]{style="font-family:宋体"} [为]{style="font-family:宋体"}*[aa]{lang="EN-US"}*[，可截断字段为]{style="font-family:宋体"}*[tc]{lang="EN-US"}*[，期望递归字段为]{style="font-family:宋体"}*[rd]{lang="EN-US"}*[，可用递归字段为]{style="font-family:宋体"}*[ra]{lang="EN-US"}*[，]{style="font-family:宋体"}[Z]{lang="EN-US"}[为]{style="font-family:宋体"}*[zero]{lang="EN-US"}*[，可信数据字段为]{style="font-family:宋体"}*[ad]{lang="EN-US"}*[，校验字段为]{style="font-family:宋体"}*[cd]{lang="EN-US"}*[，返回码字段为]{style="font-family:宋体"}*[rcode]{lang="EN-US"}*[，问题数为]{style="font-family:宋体"}*[qdcount]{lang="EN-US"}*[，资源记录数为]{style="font-family:宋体"} *[ancount]{lang="EN-US"}*[，授权资源记录数为]{style="font-family:宋体"}*[nscount]{lang="EN-US"}*[ ]{lang="EN-US"}[，]{style="font-family:宋体"} [额外资源记录数为]{style="font-family:宋体"}*[arcount]{lang="EN-US"}*

[[Question:]{lang="EN-US"}]{#struct_0_x1378_16565_x1382320127}

[[ QName = *host-name* ]{lang="EN-US"}]{#struct_0_x1378_16565_1582768904}

[[ QType = *query-type* (*type-number)* ]{lang="EN-US"}]{#struct_0_x1378_16565_x966823874}

[[ QClass = *class* (*class-number*)]{lang="EN-US"}]{#struct_0_x1378_16565_2062974870}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x343402393}[报文问题部分的内容：]{style="font-family:宋体"}

[[查询名为]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x1378_16565_534559}[，查询类型为]{style="font-family:宋体"}*[query-type]{lang="EN-US"}*[，类型编号为]{style="font-family:宋体"}*[type-number]{lang="EN-US"}*[，查询类为]{style="font-family:宋体"}*[class]{lang="EN-US"}*[，查询类编号为]{style="font-family:宋体"}*[class-number]{lang="EN-US"}*

[[Answer:]{lang="EN-US"}]{#struct_0_x1378_16565_x2062361604}

[[ Name = *host-name* ]{lang="EN-US"}]{#struct_0_x1378_16565_772076776}

[[ Type = *query-type* (*type-number*) ]{lang="EN-US"}]{#struct_0_x1378_16565_x967282629}

[[ Class = *class* (*class-number*) ]{lang="EN-US"}]{#struct_0_x1378_16565_513214934}

[[ TTL = *ttl*]{lang="EN-US"}]{#struct_0_x1378_16565_870724657}

[[ RDLength = *data-length* ]{lang="EN-US"}]{#struct_0_x1378_16565_x1548409109}

[[ RData = *data*]{lang="EN-US"}]{#struct_0_x1378_16565_2041353440}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x967348165}[报文资源记录部分的内容：]{style="font-family:宋体"}

[[主机名为]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_2073918481}[，查询类型为]{style="font-family:宋体"}*[query-type]{lang="EN-US"}*[，类型编号为]{style="font-family:宋体"}*[type-number]{lang="EN-US"}*[，查询类为]{style="font-family:宋体"}*[class]{lang="EN-US"}*[，查询类编号为]{style="font-family:宋体"}*[class-number]{lang="EN-US"}*[，生存时间]{style="font-family:宋体"} [为]{style="font-family:宋体"}*[ttl]{lang="EN-US"}*[，资源数据长度为]{style="font-family:宋体"}*[data-length]{lang="EN-US"}*[，资源数据为]{style="font-family:宋体"}*[data]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging dns event]{lang="EN-US"}]{#struct_0_x1378_16565_1369801309}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1645972962}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_1212598111}

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_x735794853}

[[Successfully resolved *query-name*: host name is *host-name*, address is *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_1608519756}

[[解析]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_407125172}[请求]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[成功，其主机名是]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Failed to resolve *query-name*]{lang="EN-US"}]{#struct_0_x1378_16565_x967413701}

[[解析]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_888569621}[请求]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Invalid host name *host-name*,]{lang="EN-US"}]{#struct_0_x1378_16565_1096579568}

[[主机名]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x175161711}[无效]{style="font-family:宋体"}

[[Resolving *query-name* is in process; waiting for result]{lang="EN-US"}]{#struct_0_x1378_16565_1391496546}

[[正在向服务器解析]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_1781743963}[请求]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[，等待获取查询结果]{style="font-family:宋体"}

[[Too many resolving operations are in process.]{lang="EN-US"}]{#struct_0_x1378_16565_x967479237}

[[正在处理的域名解析过多]{style="font-family:宋体"}]{#struct_0_x1378_16565_x1824722680}

[[Starting AAAA resolving for *host-name*]{lang="EN-US"}]{#struct_0_x1378_16565_x1760031413}

[[开始对主机名]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x1378_16565_834994467}[进行]{style="font-family:宋体"}[AAAA]{lang="EN-US"}[解析]{style="font-family:宋体"}

[[Starting A resolving for *host-name*]{lang="EN-US"}]{#struct_0_x1378_16565_x1979610081}

[[开始对主机名]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x1378_16565_1656938678}[进行]{style="font-family:宋体"}[A]{lang="EN-US"}[解析]{style="font-family:宋体"}

[[Starting PTR resolving for *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_x967544773}

[[开始对地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x1378_16565_x686099564}[进行]{style="font-family:宋体"}[PTR]{lang="EN-US"}[解析]{style="font-family:宋体"}

[[Trying to resolve the host name for address *ip-address* in local database]{lang="EN-US"}]{#struct_0_x1378_16565_x747564090}

[[从本地数据库解析地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_1789345481}[的主机的域名]{style="font-family:宋体"}

[[Trying to resolve *host-name* in local database]{lang="EN-US"}]{#struct_0_x1378_16565_x752501101}

[[从本地数据库解析]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x967610309}

[[Trying to resolve *host-name* in dynamic cache]{lang="EN-US"}]{#struct_0_x1378_16565_2057052550}

[[从动态缓存解析]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1799368543}

[[No DNS server is found.]{lang="EN-US"}]{#struct_0_x1378_16565_1381282811}

[[没有配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x269119875}[服务器]{style="font-family:宋体"}

[[Trying to resolve *host-name* by contacting DNS server *ip-address* through UDP]{lang="EN-US"}]{#struct_0_x1378_16565_x967675845}

[[以]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1378_16565_x1526044527}[方式向]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[解析主机]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*

[[Trying to resolve *host-name* by contacting DNS server *ip-address* through TCP]{lang="EN-US"}]{#struct_0_x1378_16565_x1166123540}

[[以]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1378_16565_x1251013608}[方式向]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[解析主机]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*

[[Connecting to server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_140749630}

[[正在连接服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_x967741381}

[[Connected to server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_481990154}

[[已连接到服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_1905293882}

[[Failed to connect to server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_1115991945}

[[连接服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_x966758341}[失败]{style="font-family:宋体"}

[[Failed to send packets to server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_2056748171}

[[发送数据给服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_x611599026}[失败]{style="font-family:宋体"}

[[Waiting *time-value* seconds for server response]{lang="EN-US"}]{#struct_0_x1378_16565_x1275985220}

[[在]{style="font-family:宋体"}*[time-value]{lang="EN-US"}*]{#struct_0_x1378_16565_x966823877}[秒时间内等待服务器应答]{style="font-family:宋体"}

[[Resolving *query-name* through DNS server *ip-address* timed out.]{lang="EN-US"}]{#struct_0_x1378_16565_2063171478}

[[向服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x1378_16565_x1156531330}[解析]{style="font-family:宋体"}[DNS]{lang="EN-US"}[请求]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[超时]{style="font-family:宋体"}

[[Received an answer: QName = *query-name*,, ID = *transaction-id*]{lang="EN-US"}]{#struct_0_x1378_16565_2122328791}

[[收到一个应答，]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x967282628}[请求为]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[t*ransaction-id*]{lang="EN-US"}

[[Expect QName = *query-name*, ID = *transaction-id.* The received request is not as expected. Discarded it.]{lang="EN-US"}]{#struct_0_x1378_16565_513149398}

[[期望收到的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x111314642}[请求为]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[，]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[t*ransaction-id*]{lang="EN-US"}[，（接收到的与期望的不符）丢弃]{style="font-family:宋体"}

[[Resolving *query-name* is canceled.]{lang="EN-US"}]{#struct_0_x1378_16565_x1025203028}

[[解析]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x967348164}[请求]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[被取消]{style="font-family:宋体"}

[[Invalid packet; discarded it.]{lang="EN-US"}]{#struct_0_x1378_16565_2073852945}

[[无效报文，丢弃]{style="font-family:宋体"}]{#struct_0_x1378_16565_x1752231752}

[[The answer is invalid.]{lang="EN-US"}]{#struct_0_x1378_16565_x1766421305}

[[无效的回答]{style="font-family:宋体"}]{#struct_0_x1378_16565_x967413700}

[[Added a dynamic DNS entry *host-name*]{lang="EN-US"}]{#struct_0_x1378_16565_888635157}

[[添加一个主机名为]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_546506232}[的动态表项]{style="font-family:宋体"}

[[Deleted a dynamic DNS entry *host-name*]{lang="EN-US"}]{#struct_0_x1378_16565_x967479236}

[[删除一个主机名为]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1824657144}[的动态表项]{style="font-family:宋体"}

[[The number of dynamic DNS entries has reached the maximum.]{lang="EN-US"}]{#struct_0_x1378_16565_5397869}

[[动态表项的数目已达到最大值]{style="font-family:宋体"}]{#struct_0_x1378_16565_x967544772}

[[Listening on IPv4 TCP port 53]{lang="EN-US"}]{#struct_0_x1378_16565_x686165100}

[[以]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1378_16565_1200065389}[方式监听]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议栈的]{style="font-family:宋体"}[53]{lang="EN-US"}[号端口]{style="font-family:宋体"}

[[Listening on IPv6 TCP port 53]{lang="EN-US"}]{#struct_0_x1378_16565_x967610308}

[[以]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1378_16565_2057118086}[方式监听]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议栈的]{style="font-family:宋体"}[53]{lang="EN-US"}[号端口]{style="font-family:宋体"}

[[Listening on IPv4 UDP port 53]{lang="EN-US"}]{#struct_0_x1378_16565_2135276815}

[[以]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1378_16565_x1117184221}[方式监听]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议栈的]{style="font-family:宋体"}[53]{lang="EN-US"}[号端口]{style="font-family:宋体"}

[[Listening on IPv6 UDP port 53]{lang="EN-US"}]{#struct_0_x1378_16565_x967675844}

[[以]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x1378_16565_x1525978991}[方式监听]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议栈的]{style="font-family:宋体"}[53]{lang="EN-US"}[号端口]{style="font-family:宋体"}

[[DNS proxy received a request for resolving *query-name.*]{lang="EN-US"}]{#struct_0_x1378_16565_650329804}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x967741380}[代理收到一个解析]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[的查询请求]{style="font-family:宋体"}

[[DNS proxy sent a reply for resolving *query-name.*]{lang="EN-US"}]{#struct_0_x1378_16565_481924618}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x2036934254}[代理发送一个解析]{style="font-family:宋体"}*[query-name]{lang="EN-US"}*[的应答]{style="font-family:宋体"}

[[No DNS server is available, answered with a spoofing address *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_x966758340}

[[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_2056813707}[服务器均不可达，以]{style="font-family:宋体"}[spoofing]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[作为应答]{style="font-family:宋体"}

[[Added a dynamic domain name *domain-name*]{lang="EN-US"}]{#struct_0_x1378_16565_589085111}

[[添加一个动态域名后缀]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x966823876}

[[Deleted a dynamic domain name *domain-name*]{lang="EN-US"}]{#struct_0_x1378_16565_2063105942}

[[删除一个动态域名后缀]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598801316}

[[Added a dynamic server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_x988352047}

[[添加一个动态]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_x1766630569}[服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Deleted a dynamic server *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_598735780}

[[删除一个动态]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1378_16565_705217634}[服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging dns error]{lang="EN-US"}]{#struct_0_x1378_16565_x319729722}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1671045283}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_1788281599}

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_x1498026937}

[[Failed to receive data]{lang="EN-US"}]{#struct_0_x1378_16565_598670244}

[[接收数据失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_x1592164901}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_x1378_16565_1456277672}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_x61410025}

[[The PTR request doesn\'t support address family *family-type.*]{lang="EN-US"}]{#struct_0_x1378_16565_480367124}

[[PTR]{lang="EN-US"}]{#struct_0_x1378_16565_x954301372}[类查询不支持地址协议族]{style="font-family:宋体"}*[family-type]{lang="EN-US"}*

[[Failed to bind socket]{lang="EN-US"}]{#struct_0_x1378_16565_242384276}

[[绑定套接字失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_598604708}

[[Failed to connect to server]{lang="EN-US"}]{#struct_0_x1378_16565_x1605974969}

[[连接失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_1472835407}

[[Failed to create socket]{lang="EN-US"}]{#struct_0_x1378_16565_x1280798256}

[[创建套接字失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_455230268}

[[Failed to set socket options]{lang="EN-US"}]{#struct_0_x1378_16565_x1581898048}

[[设置套接字选项失败]{style="font-family:宋体"}]{#struct_0_x1378_16565_598539172}

[[Listening socket hangs up]{lang="EN-US"}]{#struct_0_x1378_16565_874568494}

[[监听套接字关闭]{style="font-family:宋体"}]{#struct_0_x1378_16565_1981975244}

[[Failed to get the IP address of interface *interface-name*]{lang="EN-US"}]{#struct_0_x1378_16565_x75121322}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1120179219}[对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[The number of VPN instances has reached the maximum.]{lang="EN-US"}]{#struct_0_x1378_16565_598473636}

[[VPN]{lang="EN-US"}]{#struct_0_x1378_16565_1659457609}[实例的数目已达到最大值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x347409329}

[[\# ]{lang="EN-US"}]{#struct_0_x1378_16565_488385219}[配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1378_16565_51214282}

[System View: return to User View with Ctrl+Z.]{lang="EN-US"}

[\[Sysname\] dns server 1.0.0.1]{lang="EN-US"}

[\[Sysname\] quit]{lang="EN-US"}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x1378_16565_286115963}*[打开]{style="font-family:
宋体"}[DNS]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}*

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_x1378_16565_598408100}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> debugging dns all]{lang="EN-US"}

[// ping test.com ]{lang="EN-US"}[从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器解析到地址为]{style="font-family:宋体"}[1.0.0.2]{lang="EN-US"}

[\<Sysname\> ping test.com]{lang="EN-US"}

[Ping test.com (1.0.0.2): 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[56 bytes from 1.0.0.2: icmp_seq=0 ttl=128 time=1.000 ms]{lang="EN-US"}

[56 bytes from 1.0.0.2: icmp_seq=1 ttl=128 time=0.000 ms]{lang="EN-US"}

[56 bytes from 1.0.0.2: icmp_seq=2 ttl=128 time=0.000 ms]{lang="EN-US"}

[56 bytes from 1.0.0.2: icmp_seq=3 ttl=128 time=1.000 ms]{lang="EN-US"}

[56 bytes from 1.0.0.2: icmp_seq=4 ttl=128 time=1.000 ms]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for test.com \-\--]{lang="EN-US"}

[5 packet(s) transmitted, 5 packet(s) received, 0.0% packet loss]{lang="EN-US"}

[round-trip min/avg/max/std-dev = 0.000/0.600/1.000/0.490 ms]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1284365065}*[启动查询主机]{style="font-family:宋体"}[test.com]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[A]{lang="EN-US"}[类]{style="font-family:宋体"}[DNS]{lang="EN-US"}[查询。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Starting A resolving for test.com]{lang="EN-US"}]{#struct_0_x1378_16565_x1138508134}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1220094651}*[在本地静态配置中查询。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com in local database]{lang="EN-US"}]{#struct_0_x1378_16565_x1736704975}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_2020505032}*[在本地动态缓存中查询。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com in dynamic cache]{lang="EN-US"}]{#struct_0_x1378_16565_598342564}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_200584701}*[通过]{style="font-family:宋体"}[UDP]{lang="EN-US"}[向地址为]{style="font-family:宋体"}[1.0.0.1]{lang="EN-US"}[的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器查询。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/EVENT: -MDC=1; Trying to resolve test.com by contacting DNS server 1.0.0.1 through UDP]{lang="EN-US"}]{#struct_0_x1378_16565_359035955}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1309685329}*[发送查询报文的报文头部分的信息。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/PACKET: -MDC=1; Sent:]{lang="EN-US"}]{#struct_0_x1378_16565_73951917}

[Header:]{lang="EN-US"}

[ ID = 17767]{lang="EN-US"}

[ QR = 0, OpCode = 0, AA = 0, TC = 0, RD = 1]{lang="EN-US"}

[ RA = 0, Z = 0, AD = 0, CD = 0, RCode = 0]{lang="EN-US"}

[ QDCount = 1]{lang="EN-US"}

[ ANCount = 0]{lang="EN-US"}

[ NSCount = 0]{lang="EN-US"}

[ ARCount = 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_298046352}*[发送查询报文的问题部分的内容。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:480 2011 Sysname DNS/7/PACKET: -MDC=1; Sent:]{lang="EN-US"}]{#struct_0_x1378_16565_599325604}

[Question:]{lang="EN-US"}

[ QName  = test.com]{lang="EN-US"}

[ QType  = A (1)]{lang="EN-US"}

[ QClass = IN (1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1510355229}*[等待服务器应答，等待时长为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:482 2011 Sysname DNS/7/EVENT: -MDC=1; Waiting 2 seconds for server response]{lang="EN-US"}]{#struct_0_x1378_16565_x520658154}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1374398070}*[收到应答报文的报文头部分的内容。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:]{lang="EN-US"}]{#struct_0_x1378_16565_x283209647}

[Header:]{lang="EN-US"}

[ ID = 17767]{lang="EN-US"}

[ QR = 1, OpCode = 0, AA = 1, TC = 0, RD = 1]{lang="EN-US"}

[ RA = 0, Z = 0, AD = 0, CD = 0, RCode = 0]{lang="EN-US"}

[ QDCount = 1]{lang="EN-US"}

[ ANCount = 1]{lang="EN-US"}

[ NSCount = 2]{lang="EN-US"}

[ ARCount = 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_599260068}*[收到应答报文的问题部分的内容。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:]{lang="EN-US"}]{#struct_0_x1378_16565_x807974809}

[Question:]{lang="EN-US"}

[ QName  = test.com]{lang="EN-US"}

[ QType  = A (1)]{lang="EN-US"}

[ QClass = IN (1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1092338739}*[收到应答报文的答案部分的内容。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/PACKET: -MDC=1; Received:]{lang="EN-US"}]{#struct_0_x1378_16565_878818299}

[Answer:]{lang="EN-US"}

[ Name     = test.com]{lang="EN-US"}

[ Type     = A (1)]{lang="EN-US"}

[ Class    = IN (1)]{lang="EN-US"}

[ TTL      = 60]{lang="EN-US"}

[ RDLength = 4]{lang="EN-US"}

[ RData    = 192.168.20.177]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Received an answer: QName = test.com, ID = 17767]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1196599276}*[添加]{style="font-family:宋体"}[test.com]{lang="EN-US"}[的查询记录到本地动态缓存。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Added a dynamic DNS entry test.com]{lang="EN-US"}]{#struct_0_x1378_16565_598801317}

[*[// DNS]{lang="EN-US"}*]{#struct_0_x1378_16565_x988352048}*[查询成功。]{style="font-family:宋体"}*

[[\*Nov 16 09:56:02:484 2011 Sysname DNS/7/EVENT: -MDC=1; Successfully resolved test.com: host name is test.com, address is 1.0.0.2]{lang="EN-US"}]{#struct_0_x1378_16565_x1766958249}

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section3 style="layout-grid:15.6pt"}
:::

::: {#44608977 .myid}
[]{#_Toc404786256}[]{#struct_0_x1378_16565_x633079390}

**DDNS \-- DDNS调试命令 \-- debugging ddns**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1378_16565_312021476}

[**[debugging ddns]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1378_16565_2118146222}

[**[undo debugging ddns]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1378_16565_x1573133961}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1378_16565_598735781}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1378_16565_705217635}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x319729721}

[[network-admin]{lang="EN-US"}]{#struct_0_x1378_16565_1788478207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1378_16565_2016203285}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x1947297127}

[**[all]{lang="EN-US"}**]{#struct_0_x1378_16565_1285118358}[：表示]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1378_16565_870503040}[：表示]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1378_16565_891174258}[：表示]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1378_16565_598670245}[：表示]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1378_16565_x1592164900}

[**[debugging ddns]{lang="EN-US"}**]{#struct_0_x1378_16565_x1272605683}[命令用来打开]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ddns]{lang="EN-US"}**]{#struct_0_x1378_16565_x1569685747}[命令用来关闭]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_x1378_16565_x1673287640}[服务器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表2-1 ]{lang="EN-US"}[debugging ddns packet]{lang="EN-US"}]{#struct_0_x1378_16565_x1213989091}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1671432851}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_613251109}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_2094957101}

[[Interface = *interface-name*, Policy = *policy-name*:]{lang="EN-US"}]{#struct_0_x1378_16565_598604709}

[[Packet sent:]{lang="EN-US"}]{#struct_0_x1378_16565_x1605974970}

[*[packet-content]{lang="EN-US"}*]{#struct_0_x1378_16565_x1612343844}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1189865589}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[，发送的数据内容为：]{style="font-family:宋体"}*[packet-content]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*:]{lang="EN-US"}]{#struct_0_x1378_16565_1177585481}

[[Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_103911997}

[*[packet-content]{lang="EN-US"}*]{#struct_0_x1378_16565_x521321156}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598539173}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[，接收的数据内容为：]{style="font-family:宋体"}*[packet-content]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[debugging ddns event]{lang="EN-US"}]{#struct_0_x1378_16565_874568495}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1666243078}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_1981975243}

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_x75055786}

[[Interface = *interface-name*, Policy = *policy-name*: Starting DDNS update]{lang="EN-US"}]{#struct_0_x1378_16565_385204786}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1794894924}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：开始]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Created an update timer. The interval is *interval-value* seconds]{lang="EN-US"}]{#struct_0_x1378_16565_2061445650}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598473637}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：创建一个时间间隔为]{style="font-family:宋体"}*[interval-value]{lang="EN-US"}*[秒更新定时器]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Resolving IP address for server *server-name*]{lang="EN-US"}]{#struct_0_x1378_16565_1659457610}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x346950576}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：解析服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Server IP address is *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_x1848503890}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1398268473}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：服务器地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Connected to the server]{lang="EN-US"}]{#struct_0_x1378_16565_x1140444717}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598408101}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：已连接到服务器]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Disconnected from the server]{lang="EN-US"}]{#struct_0_x1378_16565_1284365064}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1138442598}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：与服务器失去连接]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: The update timer timed out]{lang="EN-US"}]{#struct_0_x1378_16565_x611835199}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1625804550}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：更新定时器超时]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Destroyed the update timer]{lang="EN-US"}]{#struct_0_x1378_16565_598342565}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_200584700}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：销毁更新定时器]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: DDNS update failed]{lang="EN-US"}]{#struct_0_x1378_16565_359035954}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1309685330}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Starting ODS update]{lang="EN-US"}]{#struct_0_x1378_16565_73362092}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1123928877}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：开启]{style="font-family:宋体"}[ODS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent LOGIN request]{lang="EN-US"}]{#struct_0_x1378_16565_599325605}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1510355228}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[LOGIN]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent ADDRR request]{lang="EN-US"}]{#struct_0_x1378_16565_x520592618}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1329337747}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[ADDRR]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent DELRR request]{lang="EN-US"}]{#struct_0_x1378_16565_x1474548730}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_599260069}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[DELRR]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Received response *response-code*]{lang="EN-US"}]{#struct_0_x1378_16565_x807974810}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1092797492}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：收到应答码]{style="font-family:宋体"}*[response-code]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Finished ODS update]{lang="EN-US"}]{#struct_0_x1378_16565_1230556384}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598801314}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：完成]{style="font-family:宋体"}[ODS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Stopped ODS update]{lang="EN-US"}]{#struct_0_x1378_16565_x988352049}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1767023785}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：停止]{style="font-family:宋体"}[ODS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: ODS update failed]{lang="EN-US"}]{#struct_0_x1378_16565_x455012100}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598735778}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[ODS]{lang="EN-US"}[更新失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Starting ORAY update]{lang="EN-US"}]{#struct_0_x1378_16565_x14826406}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_2043428410}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发起]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent AUTH request]{lang="EN-US"}]{#struct_0_x1378_16565_1058266290}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598670242}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[AUTH]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent username and password]{lang="EN-US"}]{#struct_0_x1378_16565_x1592164895}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x869910979}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送用户名和密码]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent REGI request]{lang="EN-US"}]{#struct_0_x1378_16565_486089124}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598604706}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[REGI]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent CNFM request]{lang="EN-US"}]{#struct_0_x1378_16565_x1605974979}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1472769871}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[CNFM]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent QUIT request]{lang="EN-US"}]{#struct_0_x1378_16565_x421389510}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598539170}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[QUIT]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Received response *reply-message*]{lang="EN-US"}]{#struct_0_x1378_16565_874568492}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1981975246}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：收到]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[应答消息]{style="font-family:宋体"}*[reply-message]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Sent a heartbeat to server, Chat ID = *chat-id*, OP Code = *op-code*, Start ID = *start-id*]{lang="EN-US"}]{#struct_0_x1378_16565_x75252394}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598473634}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送心跳报文给服务器，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[chat-id]{lang="EN-US"}*[，操作码为]{style="font-family:宋体"}*[op-code]{lang="EN-US"}*[，启动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[start-id]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Received a heartbeat from server, Chat ID = *chat-id*, OP Code = *op-code*, Start ID = *start-id*, IP = *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_1659457607}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x346753969}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：接收到服务器的心跳报文，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[chat-id]{lang="EN-US"}*[，操作码为]{style="font-family:宋体"}*[op-code]{lang="EN-US"}*[，启动]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[start-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Stopped ORAY update]{lang="EN-US"}]{#struct_0_x1378_16565_598408098}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x635214218}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：停止]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Finished ORAY update, chat ID is *chat-id*, start ID is *start-id*]{lang="EN-US"}]{#struct_0_x1378_16565_x577237115}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598342562}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[更新完成，]{style="font-family:宋体"}[chat ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[chat-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[start ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[start-id]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: ORAY update failed]{lang="EN-US"}]{#struct_0_x1378_16565_200584699}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1942880352}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[更新失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Starting GUNDIP update]{lang="EN-US"}]{#struct_0_x1378_16565_599325602}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1510355231}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发起]{style="font-family:宋体"}[GUNDIP]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Stopped GUNDIP update]{lang="EN-US"}]{#struct_0_x1378_16565_x520133867}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_599260066}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：停止]{style="font-family:宋体"}[GUNDIP]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Finished GUNDIP update]{lang="EN-US"}]{#struct_0_x1378_16565_x807974799}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_372294716}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[GUNDIP]{lang="EN-US"}[更新完成]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: GUNDIP update failed]{lang="EN-US"}]{#struct_0_x1378_16565_598801315}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x988352050}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[GUNDIP]{lang="EN-US"}[更新失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Sent GUNDIP update request]{lang="EN-US"}]{#struct_0_x1378_16565_x1766433960}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1007978769}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送]{style="font-family:宋体"}[GUNDIP]{lang="EN-US"}[更新请求]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Received response *packet*]{lang="EN-US"}]{#struct_0_x1378_16565_598735779}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x14826405}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：收到]{style="font-family:宋体"}[GNUDIP]{lang="EN-US"}[应答]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

[[Interface = *interface-name*, Policy = *policy-name*: Starting HTTP/HTTPS update]{lang="EN-US"}]{#struct_0_x1378_16565_2043428411}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598670243}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发起]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Stopped HTTP/HTTPS update]{lang="EN-US"}]{#struct_0_x1378_16565_x1592164894}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_696172962}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：停止]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[更新]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Finished HTTP/HTTPS update]{lang="EN-US"}]{#struct_0_x1378_16565_598604707}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1605974980}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[更新完成]{style="font-family:宋体"}

[[Interface *interface-name* is activated]{lang="EN-US"}]{#struct_0_x1378_16565_598539171}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_874568493}[被激活]{style="font-family:宋体"}

[[Interface *interface-name* is deactivated]{lang="EN-US"}]{#struct_0_x1378_16565_1981975245}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598473635}[去激活]{style="font-family:宋体"}

[[Interface *interface-name* is up]{lang="EN-US"}]{#struct_0_x1378_16565_1659457608}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_598408099}[变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[IP address of interface *interface-name* changed to *ip-address*]{lang="EN-US"}]{#struct_0_x1378_16565_x635214219}

[[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1378_16565_x577171579}[地址变为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表2-3 ]{lang="EN-US"}[debugging ddns error]{lang="EN-US"}]{#struct_0_x1378_16565_x527594147}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1692249749}[[字段]{style="font-family:黑体"}]{#struct_0_x1378_16565_598342563}

[[描述]{style="font-family:黑体"}]{#struct_0_x1378_16565_200584698}

[[Interface = *interface-name*, Policy = *policy-name*: The URL is invalid]{lang="EN-US"}]{#struct_0_x1378_16565_x1942880353}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1241870526}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：无效的]{style="font-family:宋体"}[URL]{lang="EN-US"}

[[Interface = *interface-name*, Policy = *policy-name*: Failed to lookup server IP address]{lang="EN-US"}]{#struct_0_x1378_16565_716849872}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_612013192}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：查找服务器失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: The interface has no IP address]{lang="EN-US"}]{#struct_0_x1378_16565_x1795323245}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_599325603}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Can't find the policy]{lang="EN-US"}]{#struct_0_x1378_16565_1510355230}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x520068331}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：找不到策略]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: The interface is not up]{lang="EN-US"}]{#struct_0_x1378_16565_1002546510}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x1844507522}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：接口没有]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[Interface = *interface-name*, Policy = *policy-name*: Failed to connect to the server]{lang="EN-US"}]{#struct_0_x1378_16565_599260067}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x807974800}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：连接服务器失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Failed to create a socket]{lang="EN-US"}]{#struct_0_x1378_16565_1092797491}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_1230490848}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：创建套接字失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Failed to receive a packet]{lang="EN-US"}]{#struct_0_x1378_16565_x1214704493}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x76722308}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：接收报文失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Failed to send a packet]{lang="EN-US"}]{#struct_0_x1378_16565_598801312}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_x988352043}[，策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：发送报文失败]{style="font-family:宋体"}

[[Interface = *interface-name*, Policy = *policy-name*: Can't create SSL context by policy *ssl-policy*]{lang="EN-US"}]{#struct_0_x1378_16565_x1766368425}

[[接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1378_16565_787517444}[，]{style="font-family:宋体"} [策略为]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[：]{style="font-family:宋体"} [通过策略]{style="font-family:宋体"}*[ssl-policy]{lang="EN-US"}*[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1378_16565_514190794}

[[\# ]{lang="EN-US"}]{#struct_0_x1378_16565_x871568704}[打开]{style="font-family:宋体"}[DNS]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor ]{lang="EN-US"}]{#struct_0_x1378_16565_598735776}

[Current terminal monitor is on.]{lang="EN-US"}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> debugging ddns all]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x14826392}*[配置]{style="font-family:宋体"}[DDNS policy]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x1378_16565_1213176847}

[\[Sysname\] ddns policy oray]{lang="EN-US"}

[\[Sysname-ddns-policy-oray\] url oray://steven:nevets@phservice2.oray.net]{lang="EN-US"}

[\[Sysname-ddns-policy-oray\] quit]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1295117888}*[接口引用]{style="font-family:宋体"}[DDNS policy]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x1378_16565_1391578401}

[\[Sysname-GigabitEthernet1/0/1\] ddns apply policy oray]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1673743566}*[开始]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Starting DDNS update]{lang="EN-US"}]{#struct_0_x1378_16565_9557154}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_598670240}*[启动周期更新定时器。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Create an update timer. The interval is 3720 seconds.]{lang="EN-US"}]{#struct_0_x1378_16565_x1592164897}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_292888435}*[解析服务器地址。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:660 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Resolving IP address for server phservice2.oray.net]{lang="EN-US"}]{#struct_0_x1378_16565_510481392}

[\*Nov 16 10:30:22:661 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Server IP address is 202.105.21.217]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x2144559899}*[开始]{style="font-family:宋体"}[ORAY]{lang="EN-US"}[更新。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:661 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Starting ORAY update]{lang="EN-US"}]{#struct_0_x1378_16565_529124468}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1590499935}*[接收到服务器的欢迎信息。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_519782072}

[220 oray.cn DDNS ServerX6 Ready.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 220 oray.cn DDNS ServerX6 Ready.]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_598604704}*[发送认证请求。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent AUTH request]{lang="EN-US"}]{#struct_0_x1378_16565_x1605974981}

[\*Nov 16 10:30:22:663 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:]{lang="EN-US"}

[auth router6]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1116736119}*[接收到服务器应答的挑战字。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_555937275}

[334 3vClhGrTEXdkTuvWsWghtQ==]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 334 3vClhGrTEXdkTuvWsWghtQ==]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1992086796}*[发送加密的用户名和密码。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent username and password]{lang="EN-US"}]{#struct_0_x1378_16565_x622253645}

[\*Nov 16 10:30:22:664 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:]{lang="EN-US"}

[aDNjZGRucyC/f8+6mZigJi6VWcZG9pw9zXBjqZf0t4E=]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1766891902}*[接收到服务器应答的认证通过消息。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_598539168}

[250 Auth passed at level \<1\>]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 Auth passed at level \<1\>]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1081746652}*[接收到服务器应答的注册域名列表。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_11773740}

[company.gicp.net]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response company.gicp.net]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x879495239}*[发送更新注册动态域名请求。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent REGI request]{lang="EN-US"}]{#struct_0_x1378_16565_x1700306863}

[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:]{lang="EN-US"}

[regi a company.gicp.net]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x2082131915}*[接收到服务器应答的注册域名列表结束标识。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_598473632}

[.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response .]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_1659457613}*[发送更新注册确认请求。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent CNFM request]{lang="EN-US"}]{#struct_0_x1378_16565_x347016112}

[\*Nov 16 10:30:22:666 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:]{lang="EN-US"}

[cnfm]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x1413851961}*[接收到服务器应答的注册域名成功消息。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:667 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_91832081}

[250 Register successfully]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:667 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 Register successfully]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x43138105}*[接收到服务器应答的注册确认成功的消息。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet received:]{lang="EN-US"}]{#struct_0_x1378_16565_598408096}

[250 6319526 155100175]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Received response 250 6319526 155100175]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1378_16565_x635214228}*[发送结束会话请求。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Sent QUIT request]{lang="EN-US"}]{#struct_0_x1378_16565_x577237118}

[\*Nov 16 10:30:22:770 2011 Sysname DDNS/7/PACKET: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Packet sent:]{lang="EN-US"}

[quit]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ORAY]{lang="EN-US"}*]{#struct_0_x1378_16565_x577025820}*[会话结束，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[6319526]{lang="EN-US"}[，心跳起始]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[155100175]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Nov 16 10:30:22:771 2011 Sysname DDNS/7/EVENT: -MDC=1; Interface = GigabitEthernet1/0/1, Policy = oray: Finished ORAY update, chat ID is 6319526, start ID is 155100175]{lang="EN-US"}]{#struct_0_x1378_16565_2134007661}

[ ]{lang="EN-US"}
