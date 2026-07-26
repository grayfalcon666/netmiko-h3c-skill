::: {#1634015212 .myid}
[]{#_Toc404785217}[]{#struct_0_x1371_13203_996236627}[]{#_Toc327384574}[]{#_Toc205700592}[]{#_Toc205697805}

**Modem管理 \-- Modem管理调试命令 \-- debugging modem**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1371_13203_x1264374376}

[**[debugging modem]{lang="EN-US"}**[ { **all** \| **error** \| **event** } \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1371_13203_x2123725049}

[**[undo debugging modem]{lang="EN-US"}**[ { **all** \| **error** \| **event** } \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1371_13203_x518016950}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1371_13203_x1900823829}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1371_13203_841278647}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1371_13203_1118504922}

[[network-admin]{lang="EN-US"}]{#struct_0_x1371_13203_x446310676}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1371_13203_553128180}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1371_13203_781225917}

[**[all]{lang="EN-US"}**]{#struct_0_x1371_13203_1484397471}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1371_13203_x1693985435}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1371_13203_x2123659513}[：表示事件调试信息开关。]{style="font-family:宋体"}

[]{#struct_0_x1371_13203_1807047198}[]{#OLE_LINK14}[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#OLE_LINK13}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[指定接口的调试信息开关，不指定该参数时，表示所有接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1371_13203_x1211661902}

[**[debugging modem ]{lang="EN-US"}**]{#struct_0_x1371_13203_569345535}[命令用来打开]{style="font-family:宋体"}[Modem]{lang="EN-US"}[管理的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging modem]{lang="EN-US"}**]{#struct_0_x1371_13203_819701250}[命令用来关闭]{style="font-family:宋体"}[Modem]{lang="EN-US"}[管理的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1371_13203_418875648}[管理的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging modem error]{lang="EN-US"}]{#struct_0_x1371_13203_x710390782}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_132901082}[[字段]{style="font-family:黑体"}]{#struct_0_x1371_13203_1322963539}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1371_13203_262049929}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_x1371_13203_x2123593977}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_x1371_13203_1866246050}

[[Failed to send message to IO board]{lang="EN-US"}]{#struct_0_x1371_13203_x906752077}

[[向]{style="font-family:宋体"}[IO]{lang="EN-US"}]{#struct_0_x1371_13203_x623966130}[板发送消息失败]{style="font-family:宋体"}

[[Failed to create timer]{lang="EN-US"}]{#struct_0_x1371_13203_602282119}

[[创建定时器失败]{style="font-family:宋体"}]{#struct_0_x1371_13203_205097975}

[[Failed to connect to dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x2123528441}

[[连接]{style="font-family:宋体"}[dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x209646730}[失败]{style="font-family:宋体"}

[[Failed to connect to TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x69608745}

[[连接]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x1428973096}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get TTY name]{lang="EN-US"}]{#struct_0_x1371_13203_380228134}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1393135549}[的接口获取]{style="font-family:宋体"}[TTY]{lang="EN-US"}[名称失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to open TTY *tty-name*]{lang="EN-US"}]{#struct_0_x1371_13203_x2123462905}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_214695379}[的接口打开名字为]{style="font-family:宋体"}*[tty-name]{lang="EN-US"}*[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send message *message-name* to TTY]{lang="EN-US"}]{#struct_0_x1371_13203_226279784}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x892700819}[的接口向]{style="font-family:宋体"}[TTY]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send message *message-name* to dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x1747900855}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1606847062}[的接口向]{style="font-family:宋体"}[dialer]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息失败]{style="font-family:宋体"}

[[Interface *interface-name*: Call-in is not enabled]{lang="EN-US"}]{#struct_0_x1371_13203_x2123397369}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1073419270}[的接口没有启用呼入功能]{style="font-family:宋体"}

[[Interface *interface-name*: Call-out is not enabled]{lang="EN-US"}]{#struct_0_x1371_13203_658260362}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1333074899}[的接口没有启用呼出功能]{style="font-family:宋体"}

[[Interface *interface-name*: A call is active now on this interface]{lang="EN-US"}]{#struct_0_x1371_13203_x2123331833}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x735815725}[的接口已经存在一路呼叫]{style="font-family:宋体"}

[[Interface *interface-name*: Interface has been shut down]{lang="EN-US"}]{#struct_0_x1371_13203_x799564783}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_150468729}[的接口已经被关闭]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is not working in protocol mode]{lang="EN-US"}]{#struct_0_x1371_13203_x1311211135}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123266297}[的接口没有工作在协议模式]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is not working in flow mode]{lang="EN-US"}]{#struct_0_x1371_13203_1925441282}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x412964865}[的接口没有工作在流模式]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to create asynchronous modem]{lang="EN-US"}]{#struct_0_x1371_13203_1541580136}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1110983475}[的接口创建异步]{style="font-family:宋体"}[modem]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to delete asynchronous modem]{lang="EN-US"}]{#struct_0_x1371_13203_x2124249337}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x12638996}[的接口删除异步]{style="font-family:宋体"}[modem]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to enable modem]{lang="EN-US"}]{#struct_0_x1371_13203_x655222160}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1883048106}[的接口启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to disable modem]{lang="EN-US"}]{#struct_0_x1371_13203_x2124183801}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1209818025}[的接口关闭]{style="font-family:宋体"}[modem]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send AT command *at-string* to modem]{lang="EN-US"}]{#struct_0_x1371_13203_1851770812}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x60676943}[的接口向]{style="font-family:宋体"}[modem]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[at-string]{lang="EN-US"}*[的]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to configure modem to work in flow mode]{lang="EN-US"}]{#struct_0_x1371_13203_x2123725048}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1048066991}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[为流模式失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to configure modem to work in protocol mode]{lang="EN-US"}]{#struct_0_x1371_13203_657885227}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1601503680}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[为协议模式失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to configure modem to work in AT mode]{lang="EN-US"}]{#struct_0_x1371_13203_x2123659512}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_240963257}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[为]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令模式失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to set modem country code to *country-name*]{lang="EN-US"}]{#struct_0_x1371_13203_1378037368}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x628851692}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[的国家码为]{style="font-family:宋体"}*[country-name]{lang="EN-US"}*[国家失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to enable modem caller number resolving]{lang="EN-US"}]{#struct_0_x1371_13203_x2123593976}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_300162109}[的接口启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[获取终端主叫号码功能失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to disable modem caller number resolving]{lang="EN-US"}]{#struct_0_x1371_13203_x1334996932}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123528440}[的接口关闭]{style="font-family:宋体"}[modem]{lang="EN-US"}[获取终端主叫号码功能失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging modem event]{lang="EN-US"}]{#struct_0_x1371_13203_1356437211}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_125724202}[[字段]{style="font-family:黑体"}]{#struct_0_x1371_13203_x906038193}

[[描述]{style="font-family:黑体"}]{#struct_0_x1371_13203_x1050372787}

[[Interface *interface-name*: Enabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_1564514303}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1371462252}[的接口启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Interface *interface-name*: Disabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_1923494094}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123462904}[的接口关闭]{style="font-family:宋体"}[modem]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Interface *interface-name*: Created asynchronous modem]{lang="EN-US"}]{#struct_0_x1371_13203_1780779320}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1387546321}[的接口创建异步]{style="font-family:宋体"}[modem]{lang="EN-US"}

[[Interface *interface-name*: Deleted asynchronous modem]{lang="EN-US"}]{#struct_0_x1371_13203_1694130179}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1465604242}[的接口删除异步]{style="font-family:宋体"}[modem]{lang="EN-US"}

[[Interface *interface-name*: Configured modem to work in flow mode]{lang="EN-US"}]{#struct_0_x1371_13203_x1945491982}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1995136925}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[的工作模式为流模式]{style="font-family:宋体"}

[[Interface *interface-name*: Configured modem to work in protocol mode]{lang="EN-US"}]{#struct_0_x1371_13203_x2123397368}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1655464085}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[的工作模式为协议模式]{style="font-family:宋体"}

[[Interface *interface-name*: Configured modem to work in AT mode]{lang="EN-US"}]{#struct_0_x1371_13203_x1227206104}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1380506369}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[的工作模式为]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令模式]{style="font-family:宋体"}

[[Interface *interface-name*: Set modem country code to *country-name*]{lang="EN-US"}]{#struct_0_x1371_13203_479944703}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123331832}[的接口设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[的国家码为]{style="font-family:宋体"}*[country-name]{lang="EN-US"}*[国家]{style="font-family:宋体"}

[[Interface *interface-name*: Enabled modem caller number resolving]{lang="EN-US"}]{#struct_0_x1371_13203_1993067630}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x832844471}[的接口启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[获取终端主叫号码功能]{style="font-family:宋体"}

[[Interface *interface-name*: Disabled modem caller number resolving]{lang="EN-US"}]{#struct_0_x1371_13203_x1857482584}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x158498894}[的接口关闭]{style="font-family:宋体"}[modem]{lang="EN-US"}[获取终端主叫号码功能]{style="font-family:宋体"}

[[Interface *interface-name*: Sent AT command *at-string* to modem]{lang="EN-US"}]{#struct_0_x1371_13203_x2123266296}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x803442073}[的接口向]{style="font-family:宋体"}[modem]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[at-string]{lang="EN-US"}*[的]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令]{style="font-family:宋体"}

[[Interface *interface-name*: Started call-in processing]{lang="EN-US"}]{#struct_0_x1371_13203_x167770063}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x25747099}[的接口开始呼入处理]{style="font-family:宋体"}

[[Interface *interface-name*: Started call-out processing]{lang="EN-US"}]{#struct_0_x1371_13203_823849616}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2124249336}[的接口开始呼出处理]{style="font-family:宋体"}

[[Interface *interface-name*: Started baud rate negotiation]{lang="EN-US"}]{#struct_0_x1371_13203_1553444945}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1139256804}[的接口开始波特率协商]{style="font-family:宋体"}

[[Interface *interface-name*: Stopped baud rate negotiation]{lang="EN-US"}]{#struct_0_x1371_13203_242858168}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1849596949}[的接口停止波特率协商]{style="font-family:宋体"}

[[Interface *interface-name*: Waiting to resolve caller number for *time-interval* ms]{lang="EN-US"}]{#struct_0_x1371_13203_x2124183800}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1519065330}[的接口等待]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[毫秒以获取终端主叫号码]{style="font-family:宋体"}

[[Interface *interface-name*: Waiting carrier detection for *time-interval* ms]{lang="EN-US"}]{#struct_0_x1371_13203_x134703844}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_2001753933}[的接口等待]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[毫秒以进行载波检测]{style="font-family:宋体"}

[[Interface *interface-name*: Resolved caller number]{lang="EN-US"}]{#struct_0_x1371_13203_x2123725051}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x874181774}[的接口获取到终端主叫号码]{style="font-family:宋体"}

[[Interface *interface-name*: Waiting for resolving caller number timed out]{lang="EN-US"}]{#struct_0_x1371_13203_952208732}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1083581234}[的接口获取终端主叫号码超时]{style="font-family:宋体"}

[[Interface *interface-name*: Waiting for carrier detection timed out]{lang="EN-US"}]{#struct_0_x1371_13203_x2123659515}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1325120684}[的接口载波检测超时]{style="font-family:宋体"}

[[Interface *interface-name*: Modem would be restarted in *time-interval* ms]{lang="EN-US"}]{#struct_0_x1371_13203_1256495145}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1880367742}[的接口将于]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[毫秒后重启]{style="font-family:宋体"}[modem]{lang="EN-US"}

[[Interface *interface-name*: FSM state changed from *pre-state* to *next-state*]{lang="EN-US"}]{#struct_0_x1371_13203_x2123593979}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1622152192}[的接口状态机从]{style="font-family:宋体"}*[pre-state]{lang="EN-US"}*[状态迁移到]{style="font-family:宋体"}*[next-state]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[[Interface *interface-name*: Interface has been shut down]{lang="EN-US"}]{#struct_0_x1371_13203_x707367281}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x400929047}[的接口已经被关闭]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is turned on]{lang="EN-US"}]{#struct_0_x1371_13203_x2123528443}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_953152684}[的接口被启用]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is shut down]{lang="EN-US"}]{#struct_0_x1371_13203_x1926018715}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_214610007}[的接口被关闭]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is deleted]{lang="EN-US"}]{#struct_0_x1371_13203_x2123462907}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1377494793}[的接口被删除]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is deactivated]{lang="EN-US"}]{#struct_0_x1371_13203_x35453194}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123397371}[的接口被去激活]{style="font-family:宋体"}

[[Interface *interface-name*: Interface is activated]{lang="EN-US"}]{#struct_0_x1371_13203_x717123374}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x613911483}[的接口被激活]{style="font-family:宋体"}

[[Interface *interface-name*: Interface physical mode is changed to asynchronous mode]{lang="EN-US"}]{#struct_0_x1371_13203_x2123331835}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1542384779}[的接口物理模式被切换为异步模式]{style="font-family:宋体"}

[[Interface *interface-name*: Interface physical mode is changed to synchronous mode]{lang="EN-US"}]{#struct_0_x1371_13203_138205020}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1985251470}[的接口物理模式被切换为同步模式]{style="font-family:宋体"}

[[Interface *interface-name*: Discarded message *at-string* from modem]{lang="EN-US"}]{#struct_0_x1371_13203_x2123266299}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x1919187320}[的接口丢弃了来自]{style="font-family:宋体"}[modem]{lang="EN-US"}[的]{style="font-family:宋体"}[AT]{lang="EN-US"}[消息，消息内容为]{style="font-family:宋体"}*[at-string]{lang="EN-US"}*

[[Interface *interface-name*: Received message *at-string* from modem]{lang="EN-US"}]{#struct_0_x1371_13203_x302979486}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2124249339}[的接口接收到来自]{style="font-family:宋体"}[modem]{lang="EN-US"}[的]{style="font-family:宋体"}[AT]{lang="EN-US"}[消息，消息内容为]{style="font-family:宋体"}*[at-string]{lang="EN-US"}*

[[Interface *interface-name*: Opened TTY *tty-name*]{lang="EN-US"}]{#struct_0_x1371_13203_x1531668770}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_509973552}[的接口打开了名字为]{style="font-family:宋体"}*[tty-name]{lang="EN-US"}*[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}

[[Interface *interface-name*: Closed TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x2124183803}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_47018611}[的接口关闭了]{style="font-family:宋体"}

[[Interface *interface-name*: Received message *message-name* from TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x2123725050}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_691902167}[的接口收到了来自]{style="font-family:宋体"}[TTY]{lang="EN-US"}[内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Sent message *message-name* to TTY]{lang="EN-US"}]{#struct_0_x1371_13203_125858564}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123659514}[的接口向]{style="font-family:宋体"}[TTY]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Received message *message-name* from dialer]{lang="EN-US"}]{#struct_0_x1371_13203_1403762671}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_x555337126}[的接口收到了来自]{style="font-family:宋体"}[dialer]{lang="EN-US"}[内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[[Interface *interface-name*: Sent message *message-name* to dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x2123593978}

[[接口名为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x1371_13203_1106731163}[的接口向]{style="font-family:宋体"}[dialer]{lang="EN-US"}[发送内容为]{style="font-family:宋体"}*[message-name]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1371_13203_818452522}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_x1582049345}[配置]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x1371_13203_x2123528442}

[\[Sysname\] dialer-group 1 rule ip permit ]{lang="EN-US"}

[\[Sysname\] interface dialer 1]{lang="EN-US"}

[\[Sysname-Dialer1\] ip address 1.0.0.1 24]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer circular enable ]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer-group 1]{lang="EN-US"}

[\[Sysname-Dialer1\] dialer number 123456]{lang="EN-US"}

[\[Sysname-Dialer1\] quit ]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/2]{lang="EN-US"}

[\[Sysname-Serial2/1/2\] physical-mode async]{lang="EN-US"}

[\[Sysname-Serial2/1/2\] dialer circular enable]{lang="EN-US"}

[\[Sysname-Serial2/1/2\] dialer circular-group 1]{lang="EN-US"}

[\[Sysname-Serial2/1/2\] return]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_x1775730671}[打开]{style="font-family:宋体"}[Modem]{lang="EN-US"}[管理的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging modem event]{lang="EN-US"}]{#struct_0_x1371_13203_x2072057052}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_881489917}[启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[呼出功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x1371_13203_1778143222}

[\[Sysname\] line tty 2]{lang="EN-US"}

[\[Sysname-line-tty2\] modem enable call-out]{lang="EN-US"}

[\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message MODEM_ENABLED to TTY]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x1281971836}*[通知]{style="font-family:宋体"}[TTY]{lang="EN-US"}[启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[功能]{style="font-family:宋体"}*

[[\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message GET_TTY to TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x2123462906}

[\*Jun 13 09:39:27:799 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message TTY_READY from TTY]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x1351388562}*[向]{style="font-family:宋体"}[TTY]{lang="EN-US"}[获取]{style="font-family:宋体"}[TTY]{lang="EN-US"}[控制权限]{style="font-family:宋体"}*

[[\*Jun 13 09:39:27:800 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Open TTY /dev/tty6]{lang="EN-US"}]{#struct_0_x1371_13203_x914223833}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_458191911}*[打开]{style="font-family:宋体"}[TTY]{lang="EN-US"}*

[[\*Jun 13 09:39:27:800 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Created asynchronous modem]{lang="EN-US"}]{#struct_0_x1371_13203_x1968754455}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1348812745}*[创建异步]{style="font-family:宋体"}[modem]{lang="EN-US"}*

[[\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Set modem to AT mode]{lang="EN-US"}]{#struct_0_x1371_13203_x39036516}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_601785243}*[设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[工作在]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令模式]{style="font-family:宋体"}*

[[\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from INVALID to DISCONNECT]{lang="EN-US"}]{#struct_0_x1371_13203_408747893}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x2123397370}*[进入]{style="font-family:宋体"}[DISCONNECT]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jun 13 09:39:27:801 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Disabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_2011759981}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x413783878}*[关闭]{style="font-family:宋体"}[modem ]{lang="EN-US"}*

[[\*Jun 13 09:39:27:802 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Modem would be restarted in 2000 ms]{lang="EN-US"}]{#struct_0_x1371_13203_374633710}

[*[// 2]{lang="EN-US"}*]{#struct_0_x1371_13203_624751595}*[秒后重新启用]{style="font-family:宋体"}[modem ]{lang="EN-US"}*

[[\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Enabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_x72497226}

[\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from DISCONNECT to IDLE]{lang="EN-US"}

[\*Jun 13 09:39:30:803 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started baud rate negotiation]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x168039696}*[进入]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态，开始波特率协商]{style="font-family:宋体"}*

[[\[Sysname-line-tty2\] return]{lang="EN-US"}]{#struct_0_x1371_13203_x2123331834}

[\*Jun 13 09:39:36:809 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem]{lang="EN-US"}

[\*Jun 13 09:39:41:804 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1186498576}*[发送]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令进行波特率协商]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_1031197203}[通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[命令触发]{style="font-family:宋体"}[DDR]{lang="EN-US"}[进行拨号。]{style="font-family:宋体"}

[[\<Sysname\> ping -c 1 1.0.0.2]{lang="EN-US"}]{#struct_0_x1371_13203_2026682155}

[Ping 1.0.0.2 (1.0.0.2): 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message DDR_DIALPRIM_CONN_REQ from dialer]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x835055396}*[收到]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号请求]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Stopped baud rate negotiation]{lang="EN-US"}]{#struct_0_x1371_13203_x426534241}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_2035494609}*[停止波特率协商]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started call-out processing]{lang="EN-US"}]{#struct_0_x1371_13203_598423218}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x283804286}*[开始呼出处理]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:949 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command ATDT123456 to modem]{lang="EN-US"}]{#struct_0_x1371_13203_x2123266298}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x353103379}*[发送拨号指令]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:951 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from IDLE to CONNECT]{lang="EN-US"}]{#struct_0_x1371_13203_x1425042384}

[\*Jun 13 09:39:52:951 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Waiting carrier detection for 60000 ms]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_677955975}*[进入]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[状态，等待检测载波信号]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:952 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message CD UP from modem]{lang="EN-US"}]{#struct_0_x1371_13203_x66126522}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_115042214}*[收到]{style="font-family:宋体"}[CD UP]{lang="EN-US"}[消息，链路建立成功]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:952 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Set modem to protocol mode]{lang="EN-US"}]{#struct_0_x1371_13203_1161116499}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1898581832}*[设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[工作在协议模式]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Close TTY]{lang="EN-US"}]{#struct_0_x1371_13203_x2124249338}

[\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message PUT_TTY to TTY]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_34415171}*[关闭]{style="font-family:宋体"}[TTY]{lang="EN-US"}[，释放]{style="font-family:宋体"}[TTY]{lang="EN-US"}[权限]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from CONNECT to ACTIVE]{lang="EN-US"}]{#struct_0_x1371_13203_459664597}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x262626751}*[进入]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jun 13 09:39:52:953 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message DDR_DIALPRIM_CONN_IND to dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x113386197}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_407550843}*[通知]{style="font-family:宋体"}[DDR]{lang="EN-US"}[拨号完成]{style="font-family:宋体"}*

[[%Jun 13 09:39:52:954 2012 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Serial2/1/2 link status is UP.]{lang="EN-US"}]{#struct_0_x1371_13203_1636399952}

[Request time out]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for 1.0.0.2 \-\--]{lang="EN-US"}

[1 packet(s) transmitted, 0 packet(s) received, 100.0% packet loss]{lang="EN-US"}

[%Jun 13 09:39:56:050 2012 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface Serial2/1/2 is UP.]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Jun 13 09:40:33:158 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message CD DOWN from modem]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x2124183802}*[收到]{style="font-family:宋体"}[CD DOWN]{lang="EN-US"}[消息，对端拆链]{style="font-family:宋体"}*

[[\*Jun 13 09:40:33:158 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message GET_TTY to TTY]{lang="EN-US"}]{#struct_0_x1371_13203_1613102552}

[\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Received message TTY_READY from TTY]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x1354556462}*[向]{style="font-family:宋体"}[TTY]{lang="EN-US"}[获取]{style="font-family:宋体"}[TTY]{lang="EN-US"}[控制权限]{style="font-family:宋体"}*

[[\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Open TTY /dev/tty6]{lang="EN-US"}]{#struct_0_x1371_13203_1903235730}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x398431440}*[打开]{style="font-family:宋体"}[TTY]{lang="EN-US"}*

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_857387406}*[设置]{style="font-family:宋体"}[modem]{lang="EN-US"}[工作在]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令模式]{style="font-family:宋体"}*

[[\*Jun 13 09:40:33:159 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command +++ to modem]{lang="EN-US"}]{#struct_0_x1371_13203_x1493622263}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1979010521}*[向]{style="font-family:宋体"}[modem]{lang="EN-US"}[发送拆链指令]{style="font-family:宋体"}[+++]{lang="EN-US"}*

[[\*Jun 13 09:40:33:160 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent message DDR_DIALPRIM_DISCONN_IND to dialer]{lang="EN-US"}]{#struct_0_x1371_13203_x718719735}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_x201410746}*[通知]{style="font-family:宋体"}[DDR]{lang="EN-US"}[连接断开]{style="font-family:宋体"}*

[[%Jun 13 09:40:33:161 2012 Sysname IFNET/3/PHY_UPDOWN: -MDC=1; Serial2/1/2 link status is DOWN.]{lang="EN-US"}]{#struct_0_x1371_13203_1667887462}

[%Jun 13 09:40:33:161 2012 Sysname IFNET/5/LINK_UPDOWN: -MDC=1; Line protocol on the interface Serial2/1/2 is DOWN.]{lang="EN-US"}

[\*Jun 13 09:40:33:161 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from ACTIVE to DISCONNECT]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_900891398}*[进入]{style="font-family:宋体"}[DISCONNECT]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jun 13 09:40:33:161 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Disabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_1994116664}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1386430918}*[关闭]{style="font-family:宋体"}[modem]{lang="EN-US"}*

[[\*Jun 13 09:40:33:162 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Modem would be restarted in 2000 ms]{lang="EN-US"}]{#struct_0_x1371_13203_x1036224787}

[*[// 2]{lang="EN-US"}*]{#struct_0_x1371_13203_x1847262341}*[秒后重新启用]{style="font-family:宋体"}[modem]{lang="EN-US"}*

[[\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Enabled modem]{lang="EN-US"}]{#struct_0_x1371_13203_x201345210}

[\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: FSM state changed from DISCONNECT to IDLE]{lang="EN-US"}

[\*Jun 13 09:40:36:163 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Started baud rate negotiation]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1229010953}*[进入]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态，开始波特率协商]{style="font-family:宋体"}*

[[\*Jun 13 09:40:42:164 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem]{lang="EN-US"}]{#struct_0_x1371_13203_403518435}

[\*Jun 13 09:40:47:164 2012 Sysname MODEM/7/EVENT: -MDC=1; Interface Serial2/1/2: Sent AT command AT to modem]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1371_13203_1788357958}*[发送]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令进行波特率协商]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_1928516968}[打开]{style="font-family:宋体"}[Modem]{lang="EN-US"}[管理的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging modem error ]{lang="EN-US"}]{#struct_0_x1371_13203_x727889407}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_x1835721906}[启用]{style="font-family:宋体"}[modem]{lang="EN-US"}[呼入功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x1371_13203_x93653403}

[\[Sysname\] line tty 2]{lang="EN-US"}

[\[Sysname-line-tty2\] modem enable call-in ]{lang="EN-US"}

[\[Sysname-line-tty2\] return]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1371_13203_x755101689}[通过]{style="font-family:宋体"}[ping]{lang="EN-US"}[命令触发]{style="font-family:宋体"}[DDR]{lang="EN-US"}[进行拨号。]{style="font-family:宋体"}

[[\<Sysname\> ping -c 1 1.0.0.2]{lang="EN-US"}]{#struct_0_x1371_13203_x201279674}

[Ping 1.0.0.2 (1.0.0.2): 56 data bytes, press CTRL_C to break]{lang="EN-US"}

[\*Jun 19 09:44:44:288 2012 Sysname MODEM/7/ERROR: -MDC=1; Interface Serial2/1/2: Call-out is not enabled]{lang="EN-US"}

[*[// Modem]{lang="EN-US"}*]{#struct_0_x1371_13203_x1502475732}*[呼出功能未启用]{style="font-family:宋体"}*

[[Request time out]{lang="EN-US"}]{#struct_0_x1371_13203_1314638238}

[ ]{lang="EN-US"}

[\-\-- Ping statistics for 1.0.0.2 \-\--]{lang="EN-US"}

[1 packet(s) transmitted, 0 packet(s) received, 100.0% packet loss]{lang="EN-US"}

[]{#_Toc288816810}[]{#_Toc288816811}[]{#_Toc288816813}[]{#_Toc288816817}[]{#_Toc288816820}[]{#_Toc288816833}[]{#_Toc288816846}[]{#_Toc288816849}[]{#_Toc288816852}[]{#_Toc288816854}[]{#_Toc288816868}[]{#_Toc288816869}[ ]{lang="EN-US"}
