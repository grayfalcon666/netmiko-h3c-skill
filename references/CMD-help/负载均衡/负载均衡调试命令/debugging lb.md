::: {#1689273160 .myid}
[]{#_Toc404796287}[]{#struct_0_x4398_19848_x1356891751}[]{#_Toc320977758}[]{#_Toc320977705}[]{#_Toc320977672}[]{#_Toc320977658}[]{#_Toc320956813}

**负载均衡 \-- 负载均衡调试命令 \-- debugging lb**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4398_19848_1285843610}

[**[debugging]{lang="EN-US"}**[ **lb** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_x4398_19848_1595081166}

[**[undo]{lang="EN-US"}**[ **debugging** **lb** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_x4398_19848_x954473449}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4398_19848_x2112711492}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4398_19848_x144527741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4398_19848_206133621}

[[network-admin]{lang="EN-US"}]{#struct_0_x4398_19848_x1037958583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4398_19848_431388863}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4398_19848_x2119068783}

[**[all]{lang="EN-US"}**]{#struct_0_x4398_19848_254547285}[：表示负载均衡所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x4398_19848_1324699301}[：]{style="font-family:宋体"}[表示负载均衡错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x4398_19848_80104721}[：]{style="font-family:宋体"}[表示负载均衡事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x4398_19848_x1903820752}[：]{style="font-family:宋体"}[表示负载均衡状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x4398_19848_1531579639}[：]{style="font-family:宋体"}[表示负载均衡报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4398_19848_x1984019275}

[**[debugging]{lang="EN-US"}**[ **lb**]{lang="EN-US"}]{#struct_0_x4398_19848_989048854}[命令用来打开负载均衡调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **lb**]{lang="EN-US"}[命令用来关闭负载均衡调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，负载均衡调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4398_19848_206068085}

[[表1-1 ]{lang="EN-US"}[debugging lb error]{lang="FR"}]{#struct_0_x4398_19848_1352746898}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1979915808}[[字段]{style="font-family:黑体"}]{#struct_0_x4398_19848_x605525753}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4398_19848_x82102196}

[[Failed to delete virtual server (*name*) instance from kernel.]{lang="FR"}]{#struct_0_x4398_19848_x688622323}

[[从内核删除虚服务]{style="font-family:宋体"}]{#struct_0_x4398_19848_x515351565}*[name]{lang="FR"}*[的实例失败]{style="font-family:宋体"}

 

[[F]{lang="FR"}[ailed to add virtual server (*name*) instance to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_1577409978}

[[向内核添加虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_206002549}[的实例失败]{style="font-family:宋体"}

 

[[Failed to switch server farm (*name1*) of the virtual server to master/backup server farm (*name2*).]{lang="EN-US"}]{#struct_0_x4398_19848_x1405055413}

[[虚服务下的实服务组]{style="font-family:宋体"}*[name1]{lang="EN-US"}*]{#struct_0_x4398_19848_x888383976}[转为主用]{style="font-family:宋体"}[/]{lang="EN-US"}[备份实服务组]{style="font-family:宋体"}*[name2]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to modify the IPv4/IPv6 address of virtual server (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_767217653}

[[修改虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_530503424}[的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

 

[[Failed to instantiate virtual server (*name*) by *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1175067314}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_206461301}[，导致虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*[实例化失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4/IPv6 address change]{lang="EN-US"}]{#struct_0_x4398_19848_x1261132449}[：]{lang="EN-US" style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[port change]{lang="EN-US"}]{#struct_0_x4398_19848_1428899483}[：端口变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[default or backup server farm change]{lang="EN-US"}]{#struct_0_x4398_19848_x1705489325}[：]{lang="EN-US" style="font-family:宋体"}[默认]{style="font-family:宋体"}[或备份实服务组变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabling the server]{lang="EN-US"}]{#struct_0_x4398_19848_x19253881}[：使能虚服务]{lang="EN-US" style="font-family:
  宋体"}

 

[[Failed to modify virtual server (*name*) by *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_1484161327}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_206395765}[，导致虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*[的配置修改失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabling UDP forced LB]{lang="EN-US"}]{#struct_0_x4398_19848_1954379322}[：使能]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[connection limit change]{lang="EN-US"}]{#struct_0_x4398_19848_598431091}[：连接数限制变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[rate limit change]{lang="EN-US"}]{#struct_0_x4398_19848_x654678382}[：连接速率变化]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bandwidth change]{lang="EN-US"}]{#struct_0_x4398_19848_x1670146134}[：连接带宽变化]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ssl-server-policy change]{lang="EN-US"}]{#struct_0_x4398_19848_x1904213968}[：]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器策略]{style="font-family:宋体"}[变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ssl-client-policy change]{lang="EN-US"}]{#struct_0_x4398_19848_x1904148432}[：]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[redirect change]{lang="EN-US"}]{#struct_0_x4398_19848_x1904082896}[：重定向内容变化]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[return code change]{lang="EN-US"}]{#struct_0_x4398_19848_273033828}[：重定向返回码变化]{lang="EN-US" style="font-family:
  宋体"}

 

[[Failed to add/delete/modify an instance of the virtual server.]{lang="EN-US"}]{#struct_0_x4398_19848_206330229}

[[添加]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_436678629}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[修改虚服务器实例失败]{style="font-family:宋体"}

 

[[Failed to add the server farm due to insufficient memory in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x1386284345}

[[由于内核中内存不足，导致添加实服务组失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1874790622}

 

[[Failed to modify online state of the server farm due to failure to modify the predictor algorithm.]{lang="EN-US"}]{#struct_0_x4398_19848_x1474803191}

[[由于修改调度算法失败，导致修改实服务组的在线状态失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_206264693}

 

[[Failed to modify the NAT of server farm *name*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1133706450}

[[修改实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x229464367}[的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能失败]{style="font-family:宋体"}

 

[[Failed to instantiate server farm *name* due to *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_1223175922}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_905303534}[，导致实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*[实例化失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insufficient memory]{lang="EN-US"}]{#struct_0_x4398_19848_206723445}[：内存]{lang="EN-US" style="font-family:
  宋体"}[不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ID conflict]{lang="EN-US"}]{#struct_0_x4398_19848_1750538610}[：编号冲突]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to add server farm *name* instance to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x1245591228}

[[向内核添加实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x252236493}[的数据失败]{style="font-family:宋体"}

 

[[Failed to create instance for real server *name1* associated with server farm *name2*.]{lang="EN-US"}]{#struct_0_x4398_19848_206657909}

[[被实服务组]{style="font-family:宋体"}*[name2]{lang="EN-US"}*]{#struct_0_x4398_19848_1769609000}[引用的实服务器]{style="font-family:宋体"}*[name1]{lang="EN-US"}*[实例化失败]{style="font-family:宋体"}

 

[[Failed to modify the predictor algorithm of server farm *name* instance.]{lang="EN-US"}]{#struct_0_x4398_19848_x1767300276}

[[修改实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x175743270}[实例的调度算法失败]{style="font-family:宋体"}

 

[[Failed to modify the fail-action of server farm *name* instance.]{lang="EN-US"}]{#struct_0_x4398_19848_206199158}

[[修改实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1001145707}[实例的故障处理失败]{style="font-family:宋体"}

 

[[Failed to modify the active real server number of server farm *name*.]{lang="EN-US"}]{#struct_0_x4398_19848_209192190}

[[修改实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1787352648}[的活动实服务器数失败]{style="font-family:宋体"}

 

[[Failed to modify the SNAT of server farm *name*.]{lang="EN-US"}]{#struct_0_x4398_19848_206133622}

[[修改实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1037958580}[的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[功能失败]{style="font-family:宋体"}

 

[[Not enough memory to create server farm (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_x1903755217}

[[创建实服务组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1904213969}[时内存不足]{style="font-family:宋体"}

 

[[Failed to add the real server (*name*) instance in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_1352746895}

[[向内核添加实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x605198073}[实例失败]{style="font-family:宋体"}

 

[[Not enough memory to create real server (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_684823987}

[[创建实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_206002550}[时内存不足]{style="font-family:宋体"}

 

[[Failed to delete/modify the real server instance in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_933596754}

[[在内核中删除]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_273733183}[修改实服务器实例失败]{style="font-family:宋体"}

 

[[Failed to write real server (*name*) to DBM.]{lang="EN-US"}]{#struct_0_x4398_19848_206461302}

[[向实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1261132452}[写]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Not enough memory to create instance for real server (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_x943819048}

[[在用户态中创建实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_206395766}[实例时内存不足]{style="font-family:宋体"}

 

[[Failed to send real server instance to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_1954379321}

[[向内核发送实服务器实例失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_598496627}

 

[[Not enough memory to initialize sticky method in sticky group (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_206330230}

[[初始化持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1901973538}[的持续性方法时内存不足]{style="font-family:宋体"}

 

[[Failed to modify sticky group (*name1*) in real server farm (*name2*) instance to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x872128077}

[[修改实服务组]{style="font-family:宋体"}*[name2]{lang="EN-US"}*]{#struct_0_x4398_19848_206264694}[实例中的持续性组]{style="font-family:宋体"}*[name1]{lang="EN-US"}*[下发内核失败]{style="font-family:宋体"}

 

[[Failed to delete sticky group (*name*) instance from kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x1133706445}

[[从内核删除持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_173885696}[实例失败]{style="font-family:宋体"}

 

[[Failed to create instance for sticky group (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_206723446}

[[为持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1750538607}[创建实例失败]{style="font-family:宋体"}

 

[[Not enough memory to add sticky group (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_x186706127}

[[添加持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1809002053}[时内存不足]{style="font-family:宋体"}

 

[[Failed to recover DBM of sticky group (*name)*.]{lang="EN-US"}]{#struct_0_x4398_19848_206199155}

[[恢复持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1001145704}[的]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to add sticky group (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_1775276131}

[[添加持续性组]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_206133619}[失败]{style="font-family:宋体"}

 

[[Not enough memory to allocate memory for sticky entries.]{lang="EN-US"}]{#struct_0_x4398_19848_206002547}

[[为持续性表项申请内存时内存不足]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1405055399}

 

[[Failed to get sticky entry due to improper sticky group configuration.]{lang="EN-US"}]{#struct_0_x4398_19848_206461299}

[[由于持续性组的配置原因，导致获取持续性表项失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_1114255548}

 

[[Not enough memory to add sticky group to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x525114564}

[[向内核添加持续性组时内存不足]{style="font-family:宋体"}]{#struct_0_x4398_19848_206395763}

 

[[Failed to get real server by sticky entry.]{lang="EN-US"}]{#struct_0_x4398_19848_206330227}

[[根据持续性表项查找实服务器失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_436678619}

 

[[Failed to get valid real server by sticky entry.]{lang="EN-US"}]{#struct_0_x4398_19848_206264691}

[[根据持续性表项查找可用的实服务器失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1133706448}

 

[[Not enough memory to generate sticky entries.]{lang="EN-US"}]{#struct_0_x4398_19848_206723443}

[[生成持续性表项时内存不足]{style="font-family:宋体"}]{#struct_0_x4398_19848_1750538612}

 

[[Failed to add policy due to *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1245460156}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_206657907}[，导致添加策略数据失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insufficient memory in kernel]{lang="EN-US"}]{#struct_0_x4398_19848_1769609010}[：内核中内存]{lang="EN-US" style="font-family:宋体"}[不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ID conflict in kernel]{lang="EN-US"}]{#struct_0_x4398_19848_206199156}[：]{style="font-family:宋体"}[内核中编号冲突]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to add rule node for policy *policy* due to *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1001145705}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_206133620}[，导致策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*[添加规则节点失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failure to instantiate action *action*]{lang="EN-US"}]{#struct_0_x4398_19848_x1037958582}[：动作]{lang="EN-US" style="font-family:宋体"}*[action]{lang="EN-US"}*[实例化失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insufficient memory]{lang="EN-US"}]{#struct_0_x4398_19848_1997472804}[：]{style="font-family:宋体"}[内存]{lang="EN-US" style="font-family:宋体"}[不足]{style="font-family:宋体"}

 

[[Failed to modify policy *policy* to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206068084}

[[在内核中修改策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*]{#struct_0_x4398_19848_1352746897}[数据失败]{style="font-family:宋体"}

 

[[Failed to add policy *policy* due to insufficient memory.]{lang="EN-US"}]{#struct_0_x4398_19848_206002548}

[[由于内存不足，导致添加策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*]{#struct_0_x4398_19848_x1405055414}[失败]{style="font-family:宋体"}

 

[[Failed to recover policy *policy* from DBM due to insufficient memory.]{lang="EN-US"}]{#struct_0_x4398_19848_206461300}

[[由于内存不足，导致策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*]{#struct_0_x4398_19848_x1261132450}[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}[中恢复失败]{style="font-family:宋体"}

 

[[Failed to instantiate policy *policy* due to *reason*.]{lang="EN-US"}]{#struct_0_x4398_19848_206330228}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x4398_19848_436678630}[，导致策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*[实例化失败。]{style="font-family:宋体"}*[reason]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insufficient memory]{lang="EN-US"}]{#struct_0_x4398_19848_206264692}[：内存]{lang="EN-US" style="font-family:
  宋体"}[不足]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid ID]{lang="EN-US"}]{#struct_0_x4398_19848_x1133706451}[：]{style="font-family:宋体"}[编号无效]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to add policy *policy* to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206723444}

[[向内核添加策略]{style="font-family:宋体"}*[policy]{lang="EN-US"}*]{#struct_0_x4398_19848_1750538609}[失败]{style="font-family:宋体"}

 

[[Not enough memory to create class *class*.]{lang="EN-US"}]{#struct_0_x4398_19848_206657908}

[[创建类]{style="font-family:宋体"}*[class]{lang="EN-US"}*]{#struct_0_x4398_19848_1769609001}[时内存不足]{style="font-family:宋体"}

 

[[Not enough memory to add match rule of the class.]{lang="EN-US"}]{#struct_0_x4398_19848_206199153}

[[为类添加匹配规则时内存不足]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1001145702}

 

[[Failed to add match rule of the class to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206133617}

[[向内核添加类的匹配规则失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_536019527}

 

[[Failed to add class (*class*) to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206068081}

[[向内核添加类]{style="font-family:宋体"}*[class]{lang="EN-US"}*]{#struct_0_x4398_19848_1352746894}[失败]{style="font-family:宋体"}

 

[[Failed to add class to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206002545}

[[向内核添加类失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1405055401}

 

[[Failed to delete class (*class*) from kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206461297}

[[从内核删除类]{style="font-family:宋体"}*[class]{lang="EN-US"}*]{#struct_0_x4398_19848_1114255558}[失败]{style="font-family:宋体"}

 

[[Failed to write class (*class*) to DBM.]{lang="EN-US"}]{#struct_0_x4398_19848_206264689}

[[写类]{style="font-family:宋体"}*[class]{lang="EN-US"}*]{#struct_0_x4398_19848_206723441}[到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Not enough memory to add action (*action*).]{lang="EN-US"}]{#struct_0_x4398_19848_1750538614}

[[创建动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206657905}[时内存不足]{style="font-family:宋体"}

 

[[Not enough memory to create action (*action*) instance.]{lang="EN-US"}]{#struct_0_x4398_19848_1769609012}

[[创建动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206199154}[实例时内存不足]{style="font-family:宋体"}

 

[[Failed to modify/instantiate server farm of action (*action*).]{lang="EN-US"}]{#struct_0_x4398_19848_x1001145703}

[[修改]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_206133618}[实例化动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*[引用的实服务组失败]{style="font-family:宋体"}

 

[[Failed to reference action (*action*) sticky group.]{lang="EN-US"}]{#struct_0_x4398_19848_536019538}

[[动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206068082}[引用持续性组失败]{style="font-family:宋体"}

 

[[Failed to add action (*action*) instance to kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206002546}

[[向内核添加动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_x1405055400}[实例失败]{style="font-family:宋体"}

 

[[Failed to delete action (*action*) instance from kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206461298}

[[从内核删除动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_1114255547}[实例失败]{style="font-family:宋体"}

 

[[Failed to modify action (*action*) instance in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_206395762}

[[在内核中修改动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206330226}[实例失败]{style="font-family:宋体"}

 

[[Failed to modify action (*action*) instance.]{lang="EN-US"}]{#struct_0_x4398_19848_x91654960}

[[修改动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_x91589424}[实例失败]{style="font-family:宋体"}

 

[[Failed to resume master server farm (*name*) of action (*action*).]{lang="EN-US"}]{#struct_0_x4398_19848_436678620}

[[恢复动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206264690}[引用的主用实服务组为在线实服务组失败]{style="font-family:宋体"}

 

[[Failed to switch backup server farm (*action*) of action (*action*).]{lang="EN-US"}]{#struct_0_x4398_19848_x1133706449}

[[切换动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206723442}[引用的备份实服务组为在线实服务组失败]{style="font-family:宋体"}

 

[[Failed to write action (*action*) to DBM.]{lang="EN-US"}]{#struct_0_x4398_19848_1750538611}

[[写动作]{style="font-family:宋体"}*[action]{lang="EN-US"}*]{#struct_0_x4398_19848_206657906}[到]{style="font-family:宋体"}[DBM]{lang="EN-US"}[失败]{style="font-family:宋体"}

 

[[Failed to add parameter profile (*profile*).]{lang="EN-US"}]{#struct_0_x4398_19848_2128513458}

[[添加参数模板]{style="font-family:宋体"}*[profile]{lang="EN-US"}*]{#struct_0_x4398_19848_x810973866}[失败]{style="font-family:宋体"}

 

[[Failed to delete the parameter profile (*profile*) from kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_2128447922}

[[从内核删除参数模板]{style="font-family:宋体"}*[profile]{lang="EN-US"}*]{#struct_0_x4398_19848_1494201162}[失败]{style="font-family:宋体"}

 

[[Failed to modify the parameter profile (*profile*).]{lang="EN-US"}]{#struct_0_x4398_19848_724057473}

[[修改参数模板]{style="font-family:宋体"}*[profile]{lang="EN-US"}*]{#struct_0_x4398_19848_2128775602}[失败]{style="font-family:宋体"}

 

[[Failed to reference parameter profile (*profile*) by virtual server (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_2128710066}

[[虚服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_357902150}[引用参数模板]{style="font-family:宋体"}*[profile]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to cancel the reference of parameter profile by virtual server (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_2128644530}

[[虚服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x396405452}[解除引用参数模板]{style="font-family:宋体"}*[profile]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to add SNAT pool (*name*) instance.]{lang="EN-US"}]{#struct_0_x4398_19848_2128578994}

[[添加]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_2129037746}[地址池]{style="font-family:宋体"}*[name]{lang="EN-US"}*[实例失败]{style="font-family:宋体"}

 

[[Failed to add new SNAT pool (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_2128972210}

[[添加新的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_1133645643}[地址池]{style="font-family:宋体"}*[name]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[SNAT pool (*name*) does not exist.]{lang="EN-US"}]{#struct_0_x4398_19848_2128513459}

[[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_x811039402}[地址池]{style="font-family:宋体"}*[name]{lang="EN-US"}*[不存在]{style="font-family:宋体"}

 

[[Failed to delete/modify SNAT pool (*name*) instance.]{lang="EN-US"}]{#struct_0_x4398_19848_2128447923}

[[删除]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_2128382387}[修改]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池]{style="font-family:宋体"}*[name]{lang="EN-US"}*[实例失败]{style="font-family:宋体"}

 

[[Pro=*protocol*, Src=*sip*/*sport*, Dst=*dip*/*dport*, ID=*id*]{lang="EN-US"}]{#struct_0_x4398_19848_x829091846}

[[收到的报文信息，其中报文协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4398_19848_2128316851}[，源]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}*[sip]{lang="EN-US"}*[/*sport*]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}*[dip]{lang="EN-US"}*[/*dport*]{lang="EN-US"}[，编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

 

[[Failed to process first/subsequent packet with NAT disabled.]{lang="EN-US"}]{#struct_0_x4398_19848_2128710067}

[[NAT]{lang="EN-US"}]{#struct_0_x4398_19848_2128644531}[未使能时处理首个]{style="font-family:宋体"}[/]{lang="EN-US"}[后续报文失败]{style="font-family:宋体"}

 

[[Not enough memory to create control information when enabling SNAT.]{lang="EN-US"}]{#struct_0_x4398_19848_2128578995}

[[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_282119249}[使能时，由于内存耗尽而无法创建控制信息]{style="font-family:宋体"}

 

[[Failed to process first packet with SNAT enabled.]{lang="EN-US"}]{#struct_0_x4398_19848_2129037747}

[[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_2128972211}[使能时处理首报文失败]{style="font-family:宋体"}

 

[[Failed to disconnect the TCP connection to the client.]{lang="EN-US"}]{#struct_0_x4398_19848_1133580107}

[[实服务器故障且选择断开连接方式处理故障时，由于发送报文失败而未与客户端断开]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4398_19848_2128513456}[连接]{style="font-family:宋体"}

 

[[Failed to start NQA job *job* of real server *name* by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_2128447920}

[[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_2128382384}[开启]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to stop NQA job (handle: *num*) of real server *name*.]{lang="EN-US"}]{#struct_0_x4398_19848_x829026310}

[[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_2128316848}[停止健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to refresh start NQA job *job* of real server *name* by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_2128775600}

[[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x390542993}[刷新开启]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[失败]{style="font-family:宋体"}

 

[[Failed to add action SSL rewrite data.]{lang="EN-US"}]{#struct_0_x4398_19848_1987534337}

[[添加]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_1987665409}[重写数据的动作失败]{style="font-family:宋体"}

 

[[Failed to modify action (*name*) instance.]{lang="EN-US"}]{#struct_0_x4398_19848_1988320769}

[[修改动作]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1987730944}[实例失败]{style="font-family:宋体"}

 

[[Failed to modify server farm of action (*name*).]{lang="EN-US"}]{#struct_0_x4398_19848_1987862016}

[[修改动作]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1987927552}[的实服务组配置失败]{style="font-family:宋体"}

 

[[Failed to delete match rule of the class from kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_1987534336}

[[从内核中删除类匹配规则失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_1987665408}

 

[[Failed to add policy due to insufficient memory in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_1988255232}

[[由于内核中内存不足，导致添加策略失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x741152406}

 

[[Failed to add policy due to ID conflict in kernel.]{lang="EN-US"}]{#struct_0_x4398_19848_x741086870}

[[由于内核中编号冲突，导致添加策略失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x740955798}

 

[[Not enough memory to create *info* information.]{lang="EN-US"}]{#struct_0_x4398_19848_x741414550}

[[由于内存不足，导致创建]{style="font-family:宋体"}*[info]{lang="EN-US"}*]{#struct_0_x4398_19848_x741283478}[信息失败。]{style="font-family:宋体"}*[info]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[session control]{lang="EN-US"}]{#struct_0_x4398_19848_x740628118}[：会话扩展]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP per-packet contro]{lang="EN-US"}]{#struct_0_x4398_19848_x741152407}[l]{lang="EN-US"}[：]{style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡扩展]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sticky control]{lang="EN-US"}]{#struct_0_x4398_19848_x741086871}[：]{style="font-family:宋体"}[持续性扩展]{lang="EN-US" style="font-family:宋体"}

 

[[Failed to accept SSL server connection \[*id*\].]{lang="EN-US"}]{#struct_0_x4398_19848_x740955799}

[[与服务器端确立建立编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741349015}[的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接失败]{style="font-family:宋体"}

 

[[Failed to distribute packet: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x741283479}

[[上送报文]{style="font-family:宋体"}*[packet]{lang="EN-US"}*]{#struct_0_x4398_19848_x740628119}[失败]{style="font-family:宋体"}

 

[[Transaction \[*id*\] failed to receive request: Return value=\[*value*\], Event=User-Input/Server-Output.]{lang="EN-US"}]{#struct_0_x4398_19848_x740562583}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741086868}[的事务接收请求失败，返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*[，事件为]{style="font-family:宋体"}[User-Input/Server-Output]{lang="EN-US"}

 

[[Transaction \[*id*\] failed to receive response: Return value=\[*value*\], Event=User-Output/Server-Input.]{lang="EN-US"}]{#struct_0_x4398_19848_x740955796}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741414548}[的事务接收应答失败，返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*[，事件为]{style="font-family:宋体"}[User-Output/Server-Input]{lang="EN-US"}

 

[[Transaction \[*id*\]: Direction=Request/Response, Parse result=Failed, Parse length=*length*.]{lang="EN-US"}]{#struct_0_x4398_19848_x741283476}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741217940}[的事务，方向为请求]{style="font-family:宋体"}[/]{lang="EN-US"}[应答方向，解析结果为失败，解析长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

 

[[Transaction \[*id*\] binding failed.]{lang="EN-US"}]{#struct_0_x4398_19848_x740562580}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741086869}[的事务绑定失败]{style="font-family:宋体"}

 

[[Transaction \[*id*\] failed to be connected to the real server.]{lang="EN-US"}]{#struct_0_x4398_19848_x740955797}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741414549}[的事务连接实服务器失败]{style="font-family:宋体"}

 

[[The real server selected by Transaction \[*id*\] doesn't existed.]{lang="EN-US"}]{#struct_0_x4398_19848_x741283477}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x740628117}[的事务所选择的实服务器不存在]{style="font-family:宋体"}

 

[[The real server selected by Transaction \[*id*\] was invalid.]{lang="EN-US"}]{#struct_0_x4398_19848_x741152410}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741021338}[的事务所选择的实服务器不可用]{style="font-family:宋体"}

 

[[Transaction \[*id*\] failed to re-create send-request queue.]{lang="EN-US"}]{#struct_0_x4398_19848_x741414554}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x741283482}[的事务重新创建发送队列失败]{style="font-family:宋体"}

 

[[Failed to merge *length* data to one data information.]{lang="EN-US"}]{#struct_0_x4398_19848_x740628122}

[[长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x4398_19848_x740562586}[的数据信息合并失败]{style="font-family:宋体"}

 

[[Failed to combine *length1* data with the previous *length2* data.]{lang="EN-US"}]{#struct_0_x4398_19848_x741086875}

[[将当前数据（长度为]{style="font-family:宋体"}*[length1]{lang="EN-US"}*]{#struct_0_x4398_19848_x740955803}[）与之前数据（长度为]{style="font-family:宋体"}*[length2]{lang="EN-US"}*[）合并失败]{style="font-family:宋体"}

 

[[Failed to create SSL server connection \[*connection* \].]{lang="EN-US"}]{#struct_0_x4398_19848_x741414555}

[[与服务器建立]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x741283483}[连接失败（连接信息为]{style="font-family:宋体"}*[connection]{lang="EN-US"}*[）]{style="font-family:宋体"}

 

[[Local=*address1*/*port1,* Peer=*address2*/*port2*]{lang="EN-US"}]{#struct_0_x4398_19848_x740628123}

[[建立的连接信息，源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4398_19848_x740562587}[为]{style="font-family:宋体"}*[address1]{lang="EN-US"}*[，源端口为]{style="font-family:宋体"}*[port1]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[address2]{lang="EN-US"}*[，目的端口为]{style="font-family:宋体"}*[port2]{lang="EN-US"}*

 

[[Transaction \[*id*\] failed to create a handle for connecting the real server.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144371397}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144240325}[的事务创建连接实服务器的句柄失败]{style="font-family:宋体"}

 

[[Virtual server *name* failed to create handle.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144699077}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144568005}[创建句柄失败]{style="font-family:宋体"}

 

[[Virtual server *name* failed to bind handle.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144502469}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1143847109}[绑定句柄失败]{style="font-family:宋体"}

 

[[Virtual server *name* failed to listen to handle.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144436934}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144305862}[监听句柄失败]{style="font-family:宋体"}

 

[[Virtual server *name* failed to accept a new handle.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144699078}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144633542}[接收新句柄失败]{style="font-family:宋体"}

 

[[Virtual server *name* failed to create a new SSL connection.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144502470}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1143912646}[创建新的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接失败]{style="font-family:宋体"}

 

[[Not enough memory to create session tack information.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144436931}

[[内存不足导致创建会话附加信息失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1144371395}

 

[[Not enough memory to create session sticky information.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144240323}

[[内存不足导致创建会话持续性信息失败]{style="font-family:宋体"}]{#struct_0_x4398_19848_x1144699075}

 

[[Failed to search FIB information: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144568003}

[[查找]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_x4398_19848_x1144502467}[信息失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Failed to create a TCP SYN packet: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1143847107}

[[创建]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}]{#struct_0_x4398_19848_x1144436932}[报文失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Dropped an error packet \[TCP ACK\] from client: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144305860}

[[丢弃客户端回的]{style="font-family:宋体"}[TCP ACK]{lang="EN-US"}]{#struct_0_x4398_19848_x1144240324}[错误报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Failed to create a TCP RST packet: *connection*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144633540}

[[创建]{style="font-family:宋体"}[TCP RST]{lang="EN-US"}]{#struct_0_x4398_19848_x1144568004}[报文失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Failed to process first packet when SNAT was enabled: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144502468}

[[SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_x1143847108}[使能时处理首报文失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Failed to select real server according to predictor: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1144436937}

[[根据调度算法选择实服务器失败，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144305865}

 

[[Failed to send the data of SSL policy *SSLPolicy*, error code *errorcode*, total length *totallen*, sent length *sentlen*, sending length *sendinglen*.]{lang="EN-US"}]{#struct_0_x4398_19848_x91523887}

[[发送]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x91458351}[策略]{style="font-family:宋体"}*[SSLPolicy]{lang="EN-US"}*[的数据失败，错误码为]{style="font-family:宋体"}*[errorcode]{lang="EN-US"}*[，总数据长度为]{style="font-family:宋体"}*[totallen]{lang="EN-US"}*[，已发送数据长度为]{style="font-family:宋体"}*[sentlen]{lang="EN-US"}*[，本次发送数据长度为]{style="font-family:宋体"}*[sendinglen]{lang="EN-US"}*

 

[[Failed to create the data of SSL policy *SSLPolicy*.]{lang="EN-US"}]{#struct_0_x4398_19848_x91392815}

[[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x91327279}[策略]{style="font-family:宋体"}*[SSLPolicy]{lang="EN-US"}*[的数据失败]{style="font-family:宋体"}

 

[[Failed to create SSL policy *SSLPolicy* context.]{lang="EN-US"}]{#struct_0_x4398_19848_x91261743}

[[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x91196207}[策略]{style="font-family:宋体"}*[SSLPolicy]{lang="EN-US"}*[的上下文失败]{style="font-family:宋体"}

 

[[Failed to sync instance (type: *type*).]{lang="EN-US"}]{#struct_0_x4398_19848_x1144240329}

[[类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x4398_19848_x1144633545}[的实例化信息同步失败。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x4398_19848_x1144568009}[：添加虚服务器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x4398_19848_x1143912649}[：删除虚服务器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x4398_19848_x1143847113}[：修改虚服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x4398_19848_x1144371402}[：添加实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x4398_19848_x1144305866}[：删除实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x4398_19848_x1144699082}[：修改虚服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_x4398_19848_x1144633546}[：添加实服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_x4398_19848_x1144502474}[：删除实服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[8]{lang="EN-US"}]{#struct_0_x4398_19848_x1143847114}[：修改虚服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[9]{lang="EN-US"}]{#struct_0_x4398_19848_421647008}[：设置]{style="font-family:宋体"}[debug]{lang="EN-US"}[开关]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_x4398_19848_421778080}[：]{style="font-family:宋体"}[虚服务器统计]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_x4398_19848_421843616}[：]{style="font-family:宋体"}[实服务器统计]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[12]{lang="EN-US"}]{#struct_0_x4398_19848_421450400}[：添加持续性组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[13]{lang="EN-US"}]{#struct_0_x4398_19848_421515936}[：删除持续性组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[14]{lang="EN-US"}]{#struct_0_x4398_19848_422171296}[：修改持续性组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[15]{lang="EN-US"}]{#struct_0_x4398_19848_421647007}[：]{style="font-family:宋体"}[添加]{lang="EN-US" style="font-family:宋体"}[类]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x4398_19848_421712543}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[类]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[17]{lang="EN-US"}]{#struct_0_x4398_19848_421843615}[：]{style="font-family:宋体"}[添加]{lang="EN-US" style="font-family:宋体"}[匹配规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[18]{lang="EN-US"}]{#struct_0_x4398_19848_421384863}[：删除匹配规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[19]{lang="EN-US"}]{#struct_0_x4398_19848_421515935}[：添加动作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[20]{lang="EN-US"}]{#struct_0_x4398_19848_421581471}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[动作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[21]{lang="EN-US"}]{#struct_0_x4398_19848_422236831}[：]{style="font-family:宋体"}[修改]{lang="EN-US" style="font-family:宋体"}[动作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[22]{lang="EN-US"}]{#struct_0_x4398_19848_421647010}[：]{style="font-family:宋体"}[添加]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[23]{lang="EN-US"}]{#struct_0_x4398_19848_421778082}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[24]{lang="EN-US"}]{#struct_0_x4398_19848_421843618}[：]{style="font-family:宋体"}[修改]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[25]{lang="EN-US"}]{#struct_0_x4398_19848_421450402}[：]{style="font-family:宋体"}[添加]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[26]{lang="EN-US"}]{#struct_0_x4398_19848_421515938}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[27]{lang="EN-US"}]{#struct_0_x4398_19848_422171298}[：]{style="font-family:宋体"}[修改]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[28]{lang="EN-US"}]{#struct_0_x4398_19848_422236834}[：添加]{style="font-family:宋体"}[SNAT]{lang="EN-US"}

 

[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[29]{lang="EN-US"}]{#struct_0_x4398_19848_421712545}[：]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[SNAT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[30]{lang="EN-US"}]{#struct_0_x4398_19848_421843617}[：]{style="font-family:宋体"}[修改]{lang="EN-US" style="font-family:宋体"}[SNAT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[31]{lang="EN-US"}]{#struct_0_x4398_19848_421384865}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[参数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x4398_19848_421515937}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[33]{lang="EN-US"}]{#struct_0_x4398_19848_421581473}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[持续性组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[34]{lang="EN-US"}]{#struct_0_x4398_19848_422236833}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[类]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[35]{lang="EN-US"}]{#struct_0_x4398_19848_421712540}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[SNAT]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[36]{lang="EN-US"}]{#struct_0_x4398_19848_421778076}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[动作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[37]{lang="EN-US"}]{#struct_0_x4398_19848_421384860}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[38]{lang="EN-US"}]{#struct_0_x4398_19848_421450396}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[实服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[39]{lang="EN-US"}]{#struct_0_x4398_19848_421581468}[：]{style="font-family:宋体"}[平滑]{lang="EN-US" style="font-family:宋体"}[虚服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[40]{lang="EN-US"}]{#struct_0_x4398_19848_422171292}[：策略]{style="font-family:宋体"}[下]{lang="EN-US" style="font-family:宋体"}[的规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[41]{lang="EN-US"}]{#struct_0_x4398_19848_421647003}[：动作]{style="font-family:宋体"}[下]{lang="EN-US" style="font-family:宋体"}[的规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[42]{lang="EN-US"}]{#struct_0_x4398_19848_421712539}[：]{lang="EN-US" style="font-family:宋体"}[实服务组统计信息]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging lb event]{lang="EN-US"}]{#struct_0_x4398_19848_x395881165}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2000514690}[[字段]{style="font-family:黑体"}]{#struct_0_x4398_19848_x804736500}

[[描述]{style="font-family:黑体"}]{#struct_0_x4398_19848_458742459}

[[Not enough memory resource.]{lang="EN-US"}]{#struct_0_x4398_19848_x1970653867}

[[内存资源不足]{style="font-family:宋体"}]{#struct_0_x4398_19848_2128578992}

 

[[Memory resource is restored.]{lang="EN-US"}]{#struct_0_x4398_19848_282315857}

[[内存资源恢复]{style="font-family:宋体"}]{#struct_0_x4398_19848_x501625905}

 

[[Received NQA notify health *job* *result* of real server *name* by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_934426794}

[[收到实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x876078435}[下的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[通知的结果]{style="font-family:宋体"}*[result]{lang="EN-US"}*[。]{style="font-family:宋体"}*[result]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_x4398_19848_1614044356}[：失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}]{#struct_0_x4398_19848_2129037744}[：非法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[succe]{lang="EN-US"}]{#struct_0_x4398_19848_x8801592}[eded]{lang="EN-US"}[：成功]{lang="EN-US" style="font-family:宋体"}

 

[[Succeeded in starting NQA job *job* (handle: *num*) of real server *name* by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_x683330067}

[[开启实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1659878238}[下的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[成功]{style="font-family:宋体"}

 

[[Add the start NQA job *job* of real server *name* to refresh list by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_x1684623416}

[[将开启实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x579604103}[下的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}*[job]{lang="EN-US"}*[添加到重刷链中]{style="font-family:宋体"}

 

[[Stop the NQA job (handle: *num*) of real server *name*.]{lang="EN-US"}]{#struct_0_x4398_19848_2128972208}

[[停止实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1134169932}[下的健康检测]{style="font-family:宋体"}

 

[[Succeeded in refreshing start NQA job *job* (handle: *num*) of real server *name* by IPv4/IPv6.]{lang="EN-US"}]{#struct_0_x4398_19848_x765573832}

[[成功刷新开启实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1634369270}[下]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[健康检测]{style="font-family:宋体"}

 

[[LB started in slot *slotid*.]{lang="EN-US"}]{#struct_0_x4398_19848_421581467}

[[负载均衡特性在槽位]{style="font-family:宋体"}*[slotid]{lang="EN-US"}*]{#struct_0_x4398_19848_422171291}[上启动]{style="font-family:宋体"}

 

[[Connection \[ *connection* \] state is changed to idle.]{lang="EN-US"}]{#struct_0_x4398_19848_422236827}

[[连接]{style="font-family:宋体"}*[connection]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498701213}[的状态变为空闲状态]{style="font-family:宋体"}

 

[[Transaction \[*id*\] received request successfully: Event=User-Input.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498766749}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498832285}[的事务接收请求数据成功，事件为]{style="font-family:宋体"}[User-Input]{lang="EN-US"}

 

[[Transaction \[*id*\] received response successfully: Event=User-Output.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498373533}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498504605}[的事务接收应答数据成功，事件为]{style="font-family:宋体"}[User-Output]{lang="EN-US"}

 

[[Transaction \[*id*\]: Event=*event*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498570141}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498176925}[的事务，事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User-Age]{lang="EN-US"}]{#struct_0_x4398_19848_x1498635678}[：用户超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User-Error]{lang="EN-US"}]{#struct_0_x4398_19848_x1498766750}[：用户错误]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server-OutPut]{lang="EN-US"}]{#struct_0_x4398_19848_x1498832286}[：服务器输出]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server-Age]{lang="EN-US"}]{#struct_0_x4398_19848_x1498373534}[：服务器超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server-Error]{lang="EN-US"}]{#struct_0_x4398_19848_x1498504606}[：服务器错误]{style="font-family:宋体"}

 

[[Transaction \[*id*\] received response data successfully: Event=Server-Input.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498570142}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498111390}[的事务接收应答数据成功，事件为]{style="font-family:宋体"}[Server-Input]{lang="EN-US"}

 

[[Transaction \[*id*\] got an idle connection successfully.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498176926}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498701211}[的事务获取空闲连接成功]{style="font-family:宋体"}

 

[[Transaction \[*id*\] created a new connection \[*connection*\] successfully.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498766747}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498832283}[的事务创建连接]{style="font-family:宋体"}*[connection]{lang="EN-US"}*[成功]{style="font-family:宋体"}

 

[[Transaction \[*id*\] selected real server \[ID: *id*\] by predictor.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498373531}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498504603}[的事务根据调度算法选择编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的实服务器成功]{style="font-family:宋体"}

 

[[Transaction \[*id*\] selected real server in \[*state*\] state by sticky.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498570139}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498111387}[的事务根据持续性选择的实服务器状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OK]{lang="EN-US"}]{#struct_0_x4398_19848_x1498635676}[：实服务器可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OVERLOAD]{lang="EN-US"}]{#struct_0_x4398_19848_x1498701212}[：]{lang="EN-US" style="font-family:宋体"}[实服务器超载]{style="font-family:宋体"}

 

[[Transaction \[*id*\] used the previous real server.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498766748}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498373532}[的事务使用上次的实服务器]{style="font-family:宋体"}

 

[[Transaction \[*id*\] forwarding method is *type*.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498439068}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498504604}[的事务转发方法为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x4398_19848_x1498570140}[：默认]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_x4398_19848_x1498176924}[：丢包]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forward]{lang="EN-US"}]{#struct_0_x4398_19848_x1498635681}[：转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Server-farm]{lang="EN-US"}]{#struct_0_x4398_19848_x1498701217}[：由实服务组处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x4398_19848_x1498832289}[：]{lang="EN-US" style="font-family:宋体"}[未知]{style="font-family:宋体"}

 

[[Transaction \[*id*\] needs to select another real server.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498373537}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498439073}[的事务需要重新选择一个实服务器]{style="font-family:宋体"}

 

[[Transaction \[*id*\] needs to send redirect response.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498504609}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498111393}[的事务需要发送重定向报文]{style="font-family:宋体"}

 

[[Transaction \[*id*\] has been deleted.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498176929}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498635682}[的事务已被删除]{style="font-family:宋体"}

 

[[Transaction \[*id*\] sent request/response successfully \[*connection*\].]{lang="EN-US"}]{#struct_0_x4398_19848_x1498766754}

[[编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498832290}[的事务发送请求]{style="font-family:宋体"}[/]{lang="EN-US"}[应答成功，连接信息为]{style="font-family:宋体"}*[connection]{lang="EN-US"}*

 

[[Virtual server *name* created a new transaction \[*id*\]: \[*connection*\].]{lang="EN-US"}]{#struct_0_x4398_19848_x1498373538}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1498439074}[成功创建一个编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的事务，连接信息为]{style="font-family:宋体"}*[connection]{lang="EN-US"}*

 

[[SSL client connection \[*connection*\] accepted successfully.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498570146}

[[接收]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x1498111394}[客户端连接]{style="font-family:宋体"}*[connection]{lang="EN-US"}*[成功]{style="font-family:宋体"}

 

[[Virtual server *name* created a new SSL connection.]{lang="EN-US"}]{#struct_0_x4398_19848_x1498176930}

[[虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_67382728}[创建了一个]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接]{style="font-family:宋体"}

 

[[SSL server connection \[ *connection* \] established successfully.]{lang="EN-US"}]{#struct_0_x4398_19848_67317192}

[[与]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_67251656}[服务器端建立连接]{style="font-family:宋体"}*[connection]{lang="EN-US"}*[成功]{style="font-family:宋体"}

 

[[SSL client/server connection \[ *connection* \] was not ready.]{lang="EN-US"}]{#struct_0_x4398_19848_67644872}

[[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_67579336}[客户端]{style="font-family:宋体"}[/]{lang="EN-US"}[服务器端连接]{style="font-family:宋体"}*[connection]{lang="EN-US"}*[尚未就绪]{style="font-family:宋体"}

 

[[Local=*address1*/*port1,* Peer=*address2*/*port2*]{lang="EN-US"}]{#struct_0_x4398_19848_67513800}

[[建立的连接信息，源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4398_19848_67907016}[为]{style="font-family:宋体"}*[address1]{lang="EN-US"}*[，源端口为]{style="font-family:宋体"}*[port1]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[address2]{lang="EN-US"}*[，目的端口为]{style="font-family:宋体"}*[port2]{lang="EN-US"}*

 

[[Succeed to receive the data of ssl policy *SSLpolicy*, total length *totallen*, received length *recevlen*, receiving length *receivinglen*.]{lang="EN-US"}]{#struct_0_x4398_19848_x91130678}

[[接收]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_273136506}[策略]{style="font-family:宋体"}*[SSLpolicy]{lang="EN-US"}*[的数据成功，总长度]{style="font-family:宋体"}*[totallen]{lang="EN-US"}*[，已接收数据长度]{style="font-family:宋体"}*[recevlen]{lang="EN-US"}*[，本次接收数据长度]{style="font-family:宋体"}*[receivinglen]{lang="EN-US"}*

 

[[Succeeded to create the data of SSL policy *SSLpolicy*, total length *totallen*.]{lang="EN-US"}]{#struct_0_x4398_19848_x153435923}

[[创建]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x4398_19848_x91065142}[策略]{style="font-family:宋体"}*[SSLpolicy]{lang="EN-US"}*[的数据成功，总长度为]{style="font-family:宋体"}*[totallen]{lang="EN-US"}*

 

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging lb fsm]{lang="EN-US"}]{#struct_0_x4398_19848_x984951959}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1692165273}[[字段]{style="font-family:黑体"}]{#struct_0_x4398_19848_67448263}

[[描述]{style="font-family:黑体"}]{#struct_0_x4398_19848_1766422426}

[[Transaction \[*id*\]: State=*state1* -\> *state2*, Direction=Request/Response.]{lang="EN-US"}]{#struct_0_x4398_19848_67382727}

[[在请求]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_67317191}[应答方向上，编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的事务状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITING]{lang="EN-US"}]{#struct_0_x4398_19848_421999791}[：等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONNECTING]{lang="EN-US"}]{#struct_0_x4398_19848_67251655}[：连接状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TRANSMITTING]{lang="EN-US"}]{#struct_0_x4398_19848_67710407}[：转发状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FINISH]{lang="EN-US"}]{#struct_0_x4398_19848_1847469157}[：应答数据接收完成状态]{lang="EN-US" style="font-family:宋体"}

 

[[Transaction \[*id*\] reset: State=*state* -\> WAITING.]{lang="EN-US"}]{#struct_0_x4398_19848_67644871}

[[重置编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x1312132253}[的事务，其状态由]{style="font-family:宋体"}*[state]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}[WAITING]{lang="EN-US"}[。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAITING]{lang="EN-US"}]{#struct_0_x4398_19848_67579335}[：等待状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONNECTING]{lang="EN-US"}]{#struct_0_x4398_19848_67513799}[：连接状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TRANSMITTING]{lang="EN-US"}]{#struct_0_x4398_19848_x1390066519}[：转发状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FINISH]{lang="EN-US"}]{#struct_0_x4398_19848_67972551}[：应答数据接收完成状态]{lang="EN-US" style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging lb packet]{lang="EN-US"}]{#struct_0_x4398_19848_2136491387}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1998311324}[[字段]{style="font-family:黑体"}]{#struct_0_x4398_19848_1038521467}

[[描述]{style="font-family:黑体"}]{#struct_0_x4398_19848_2128513457}

[[Pro=*protocol*, Src=*sip*/*sport*, Dst=*dip*/*dport*, ID=*id*]{lang="EN-US"}]{#struct_0_x4398_19848_x810121898}

[[收到的报文信息，其中报文协议号为]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4398_19848_1286888824}[，源]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}*[sip]{lang="EN-US"}*[/*sport*]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}*[dip]{lang="EN-US"}*[/*dport*]{lang="EN-US"}[，编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

 

[[Input packet matched virtual server *name*]{lang="EN-US"}]{#struct_0_x4398_19848_766759316}

[[收到匹配虚服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1301452685}[的报文]{style="font-family:宋体"}

 

[[Server farm/Forwarding/Dropping is selected according to default server farm/policy]{lang="EN-US"}]{#struct_0_x4398_19848_x1656604104}

[[根据虚服务器配置的缺省实服务组]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_x2101908187}[策略来选择实服务组]{style="font-family:宋体"}[/]{lang="EN-US"}[转发]{style="font-family:宋体"}[/]{lang="EN-US"}[丢弃]{style="font-family:宋体"}

 

[[Real server *name* is selected according to sticky method]{lang="EN-US"}]{#struct_0_x4398_19848_2128447921}

[[根据持续性方式获取实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_1494397770}

 

[[Real server *name* is selected according to predictor]{lang="EN-US"}]{#struct_0_x4398_19848_403426666}

[[根据调度算法获取实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_215160618}

 

[[Succeeded in processing first/subsequent packet with NAT/SNAT enabled: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x767140568}

[[NAT/SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_740434110}[使能时首个]{style="font-family:宋体"}[/]{lang="EN-US"}[后续报文处理成功，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Succeeded in processing first/subsequent packet with NAT disabled: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_2128382385}

[[NAT]{lang="EN-US"}]{#struct_0_x4398_19848_x828960774}[未使能时首个]{style="font-family:宋体"}[/]{lang="EN-US"}[后续报文处理成功，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Succeeded in processing reverse packet with NAT/SNAT enabled: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x2045378120}

[[NAT/SNAT]{lang="EN-US"}]{#struct_0_x4398_19848_x615391962}[使能时反向报文处理成功，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Virtual/Real server (*name*) is not available now.]{lang="EN-US"}]{#struct_0_x4398_19848_x669426246}

[[虚]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_2128316849}[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*[当前不可用或已失效]{style="font-family:宋体"}

 

[[Session conflict, try to use source port *port*.]{lang="EN-US"}]{#struct_0_x4398_19848_723467650}

[[由于会话冲突，尝试选择源端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*]{#struct_0_x4398_19848_x1490742983}

 

[[Session conflict, try to use ID *id*.]{lang="EN-US"}]{#struct_0_x4398_19848_285740993}

[[由于会话冲突，尝试选择编号]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x4398_19848_x902149804}

 

[[TTL or hop limit of the packet expires.]{lang="EN-US"}]{#struct_0_x4398_19848_2128775601}

[[报文中的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_x4398_19848_x390608529}[或]{style="font-family:宋体"}[Hop Limit]{lang="EN-US"}[值超时]{style="font-family:宋体"}

 

[[Real server *(name)* is in fault, use KEEP/RESCHEDULE/RESET processing.]{lang="EN-US"}]{#struct_0_x4398_19848_x117472883}

[[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x1803228817}[故障，使用保持已有连接]{style="font-family:宋体"}[/]{lang="EN-US"}[重定向连接]{style="font-family:宋体"}[/]{lang="EN-US"}[断开已有连接的方式处理报文]{style="font-family:宋体"}

 

[[Real server *name1* is rescheduled while real server *name2* is in fault.]{lang="EN-US"}]{#struct_0_x4398_19848_2128710065}

[[实服务器]{style="font-family:宋体"}*[name2]{lang="EN-US"}*]{#struct_0_x4398_19848_357705542}[故障，实服务器]{style="font-family:宋体"}*[name1]{lang="EN-US"}*[被重定向连接]{style="font-family:宋体"}

 

[[Can't find any other real server to reschedule while real server *name* is in fault.]{lang="EN-US"}]{#struct_0_x4398_19848_x160986541}

[[实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x852042425}[故障，无法找到其它实服务器参与重定向连接]{style="font-family:宋体"}

 

[[The UDP/TCP/ICMP connection to the client was disconnected.]{lang="EN-US"}]{#struct_0_x4398_19848_x977270671}

[[某实服务器故障，且选择断开连接方式处理故障，与客户端的]{style="font-family:宋体"}[UDP/TCP/ICMP]{lang="EN-US"}]{#struct_0_x4398_19848_2128644529}[连接被断开]{style="font-family:宋体"}

 

[[The received packet exceeded MSS, dropped it.]{lang="EN-US"}]{#struct_0_x4398_19848_67710409}

[[收到的报文超出了]{style="font-family:宋体"}[TCP MSS]{lang="EN-US"}]{#struct_0_x4398_19848_67579337}[，将其丢弃]{style="font-family:宋体"}

 

[[Real server *name* is *state* according to *method*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_67513801}

[[根据]{style="font-family:宋体"}*[method]{lang="EN-US"}*]{#struct_0_x4398_19848_67907017}[找到的实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*[的状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_x4398_19848_67448260}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[selected]{lang="EN-US"}]{#struct_0_x4398_19848_67382724}[：可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overload]{lang="EN-US"}]{#struct_0_x4398_19848_67251652}[：超载]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[not found]{lang="EN-US"}]{#struct_0_x4398_19848_67710404}[：未找到]{style="font-family:宋体"}

[*[method]{lang="EN-US"}*]{#struct_0_x4398_19848_67644868}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sticky method]{lang="EN-US"}]{#struct_0_x4398_19848_67513796}[：持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[predictor]{lang="EN-US"}]{#struct_0_x4398_19848_67972548}[：]{lang="EN-US" style="font-family:宋体"}[调度算法]{style="font-family:宋体"}

 

[[Real server is *state* according to *method*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_67907012}

[[根据]{style="font-family:宋体"}*[method]{lang="EN-US"}*]{#struct_0_x4398_19848_67382723}[找到的实服务器的状态为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[state]{lang="EN-US"}*]{#struct_0_x4398_19848_67317187}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[selected]{lang="EN-US"}]{#struct_0_x4398_19848_67251651}[：可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overload]{lang="EN-US"}]{#struct_0_x4398_19848_67644867}[：超载]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[not found]{lang="EN-US"}]{#struct_0_x4398_19848_67579331}[：未找到]{style="font-family:宋体"}

[*[method]{lang="EN-US"}*]{#struct_0_x4398_19848_67513795}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sticky method]{lang="EN-US"}]{#struct_0_x4398_19848_67907011}[：持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[predictor]{lang="EN-US"}]{#struct_0_x4398_19848_x335836263}[：]{lang="EN-US" style="font-family:宋体"}[调度算法]{style="font-family:宋体"}

 

[[Server farm is not found according to *type*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335967335}

[[根据类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x4398_19848_x336032871}[未找到实服务组，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[default server farm]{lang="EN-US"}]{#struct_0_x4398_19848_x335574119}[：默认实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[policy]{lang="EN-US"}]{#struct_0_x4398_19848_x335705191}[：]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

 

[[Server farm is selected according to *type*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335770727}

[[根据类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x4398_19848_x335377511}[找到实服务组，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[default server farm]{lang="EN-US"}]{#struct_0_x4398_19848_x335836264}[：默认实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[policy]{lang="EN-US"}]{#struct_0_x4398_19848_x335901800}[：]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

 

[[Server farm is changed by *type*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x336032872}

[[根据类型]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x4398_19848_x335574120}[找到实服务组已经改变，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[default server farm]{lang="EN-US"}]{#struct_0_x4398_19848_x335705192}[：默认实服务组]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[policy]{lang="EN-US"}]{#struct_0_x4398_19848_x335770728}[：]{lang="EN-US" style="font-family:宋体"}[策略]{style="font-family:宋体"}

 

[[Inserted a cookie \[*cookie*\] with length \[*length*: *timeout*: *insert-length*\]: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335311976}

[[插入一个]{style="font-family:宋体"}[cookie]{lang="EN-US"}]{#struct_0_x4398_19848_x335836261}[，字符内容为]{style="font-family:宋体"}*[cookie]{lang="EN-US"}*[，字符长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，超时长度为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[，插入长度为]{style="font-family:宋体"}*[insert-length]{lang="EN-US"}*[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Sent a packet \[TCP SYN/TCP RST/HTTP\] to real server *name*, result \[*result*\]: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335901797}

[[发送一个]{style="font-family:宋体"}[TCP SYN/TCP RST/HTTP]{lang="EN-US"}]{#struct_0_x4398_19848_x336032869}[报文到实服务器]{style="font-family:宋体"}*[name]{lang="EN-US"}*[，结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Sent a packet \[HTTP\] to real server, result \[*result*\]: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x91196213}

[[发送一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x4398_19848_x1674450485}[报文到实服务器，结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a packet \[TCP SYN\] from client and sent a packet \[SYN ACK\] to client: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335574117}

[[从客户端收到一个]{style="font-family:宋体"}[TCP SYN]{lang="EN-US"}]{#struct_0_x4398_19848_x335639653}[报文，并回一个]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}[报文给客户端，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Successfully created a packet \[TCP SYN/TCP RST\]: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335770725}

[[创建]{style="font-family:宋体"}[TCP SYN/TCP RST]{lang="EN-US"}]{#struct_0_x4398_19848_x335311973}[报文成功，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a packet \[TCP ACK\] from client: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335377509}

[[从客户端收到一个]{style="font-family:宋体"}[TCP ACK]{lang="EN-US"}]{#struct_0_x4398_19848_x335901798}[报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a packet \[HTTP\] from client: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335967334}

[[从客户端收到一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x4398_19848_x335574118}[报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a duplicate packet \[HTTP\] form client: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335639654}

[[从客户端收到一个重复的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x4398_19848_x335705190}[报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a packet \[TCP\] from real server: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335836267}

[[从实服务器收到一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4398_19848_x335967339}[报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Received a packet \[SYN ACK\] from real server: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x336032875}

[[从实服务器收到一个]{style="font-family:宋体"}[SYN ACK]{lang="EN-US"}]{#struct_0_x4398_19848_x335639659}[报文，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Rewrote a cookie \[*value*\] with length \[*length*\]: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335705195}

[[重写了一个值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*]{#struct_0_x4398_19848_x335770731}[、长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[cookie]{lang="EN-US"}[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Inserted a header \[*name*: *value*\]: *packet*]{lang="EN-US"}]{#struct_0_x4398_19848_x335377515}

[[插入了一个名为]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x335836268}[、值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的头部，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Input packet matched virtual server *name*: *packet*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335967340}

[[输入报文匹配上虚服务]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_x4398_19848_x336032876}[，报文信息为]{style="font-family:宋体"}*[packet]{lang="EN-US"}*

 

[[Transaction \[*id*\]: Direction=Request/Response, State=*state1* -\> *state2*, Parse Length=*length*.]{lang="EN-US"}]{#struct_0_x4398_19848_x335639660}

[[在请求]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4398_19848_x335705196}[应答方向上，编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的事务解析状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[，解析长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Request_line]{lang="EN-US"}]{#struct_0_x4398_19848_x335311980}[：请求行]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Headers]{lang="EN-US"}]{#struct_0_x4398_19848_x335377516}[：报文头部]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Body]{lang="EN-US"}]{#struct_0_x4398_19848_1230247678}[：报文体]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Chunked]{lang="EN-US"}]{#struct_0_x4398_19848_1230116606}[：报文体为]{style="font-family:宋体"}[Chunked]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Done]{lang="EN-US"}]{#struct_0_x4398_19848_1230051070}[：]{lang="EN-US" style="font-family:宋体"}[解析完成]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4398_19848_x395815629}

[[\# ]{lang="EN-US"}]{#struct_0_x4398_19848_722633852}[打开负载均衡错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lb error]{lang="EN-US"}]{#struct_0_x4398_19848_x999244081}

[\*Aug 29 00:09:45:746 2012 Sysname LB/7/ERROR: -MDC=1; Failed to process first packet with NAT disabled: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.]{lang="EN-US"}

[*[// NAT]{lang="EN-US"}*]{#struct_0_x4398_19848_x487000089}*[未使能时处理首报文失败：报文协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[，源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.1/0]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.2/0]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[10850]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x4398_19848_x983874562}[打开负载均衡事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lb event]{lang="EN-US"}]{#struct_0_x4398_19848_x197453864}

[\*Aug 29 00:13:58:003 2012 Sysname LB/7/EVENT: -MDC=1; Received NQA notify health n failed of real server rs by IPv4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4398_19848_2128578993}*[收到实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[下的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[健康检测]{style="font-family:宋体"}[n]{lang="EN-US"}[通知的失败结果]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x4398_19848_1230182141}[打开负载均衡状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lb fsm]{lang="EN-US"}]{#struct_0_x4398_19848_1230116605}

[\*Jan 18 03:24:59:671 2014 Sysname LB/7/FSM: -MDC=1; Transaction \[6\]: State=CONNECTING -\> TRANSMITTING, Direction=Request.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4398_19848_1230051069}*[在请求方向上，编号为]{style="font-family:宋体"}[6]{lang="EN-US"}[的事务的状态由]{style="font-family:宋体"}[CONNECTING]{lang="EN-US"}[迁移到]{style="font-family:宋体"}[TRANSMITTING]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x4398_19848_282250321}[打开负载均衡报文调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging lb packet]{lang="EN-US"}]{#struct_0_x4398_19848_x82344622}

[\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Input packet matched virtual server vs: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4398_19848_x831186908}*[收到匹配虚服务器]{style="font-family:宋体"}[vs]{lang="EN-US"}[的报文：报文协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[，源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.1/0]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.2/0]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[10850]{lang="EN-US"}*

[[\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Server farm is selected according to default server farm: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.]{lang="EN-US"}]{#struct_0_x4398_19848_1036581082}

[*[// ]{lang="EN-US"}*]{#struct_0_x4398_19848_x1466785819}*[根据虚服务器配置的缺省实服务组来选择实服务组：报文协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.1/0]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.2/0]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[10850]{lang="EN-US"}*

[[\*Aug 29 00:09:45:746 2012 Sysname LB/7/PACKET: -MDC=1; Real server rs is selected according to predictor: Pro=6, Src=2.2.2.1/0, Dst=2.2.2.2/0, ID=10850.]{lang="EN-US"}]{#struct_0_x4398_19848_x1404812209}

[*[// ]{lang="EN-US"}*]{#struct_0_x4398_19848_x797721985}*[根据调度算法获取实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[：报文协议号为]{style="font-family:宋体"}[6]{lang="EN-US"}[，源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.1/0]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和端口号为]{style="font-family:宋体"}[2.2.2.2/0]{lang="EN-US"}[，编号为]{style="font-family:宋体"}[10850]{lang="EN-US"}*
