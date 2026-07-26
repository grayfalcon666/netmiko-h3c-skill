::: {#674388250 .myid}
[]{#_Toc404796569}[]{#struct_0_x2158_x2842_398591496}[]{#_Toc131060009}

**NTP \-- NTP调试命令 \-- debugging ntp-service**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_2072592443}

[**[debugging ntp-service ]{lang="EN-US"}**[{ **acl** \| **adjustment** \| **all** \| **authentication** \| **event** \| **filter** \| **packet** \| **parameter** \| **refclock** \| **selection** \| **synchronization** \| **validity** }]{lang="EN-US"}]{#struct_0_x2158_x2842_213080437}

[**[undo debugging ntp-service ]{lang="EN-US"}**[{ **acl** \| **adjustment** \| **all** \| **authentication** \| **event** \| **filter** \| **packet** \| **parameter** \| **refclock** \| **selection** \| **synchronization** \| **validity** }]{lang="EN-US"}]{#struct_0_x2158_x2842_x106023635}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1529644060}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2158_x2842_x410409709}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x707525926}

[[network-admin]{lang="EN-US"}]{#struct_0_x2158_x2842_349911115}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2158_x2842_144169846}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1038292890}

[**[acl]{lang="EN-US"}**]{#struct_0_x2158_x2842_1819282866}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[访问控制调试信息开关。]{style="font-family:宋体"}

[**[adjustment]{lang="EN-US"}**]{#struct_0_x2158_x2842_213145973}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时钟调节调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2158_x2842_237779294}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_x2158_x2842_1477251489}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x2158_x2842_2020982950}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[filter]{lang="EN-US"}**]{#struct_0_x2158_x2842_1127026503}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时钟过滤调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x2158_x2842_583158442}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[parameter]{lang="EN-US"}**]{#struct_0_x2158_x2842_x1314180594}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时钟参数调试信息开关。]{style="font-family:宋体"}

[**[refclock]{lang="EN-US"}**]{#struct_0_x2158_x2842_244875851}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[参考时钟调试信息开关。]{style="font-family:宋体"}

[**[selection]{lang="EN-US"}**]{#struct_0_x2158_x2842_1943723021}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时钟选择调试信息开关。]{style="font-family:宋体"}

[**[synchronization]{lang="EN-US"}**]{#struct_0_x2158_x2842_1797836508}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时间同步调试信息开关。]{style="font-family:宋体"}

[**[validity]{lang="EN-US"}**]{#struct_0_x2158_x2842_212556150}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[远程主机的身份验证调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_1429445661}

[**[debugging ntp-service]{lang="EN-US"}**]{#struct_0_x2158_x2842_1101714825}[命令用来打开]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging ntp-service]{lang="EN-US"}**]{#struct_0_x2158_x2842_818869751}[命令用来关闭]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_x2158_x2842_53538443}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ntp-service acl]{lang="EN-US"}]{#struct_0_x2158_x2842_81150556}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x520701697}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1882303486}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_254554975}

[[Access restrict: *right*.]{lang="EN-US"}]{#struct_0_x2158_x2842_212621686}

[[对端设备对本地]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_x2158_x2842_1363295713}[服务的访问控制权限，]{style="font-family:宋体"}*[right]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0000]{lang="EN-US"}]{#struct_0_x2158_x2842_x1911710956}[：表示拒绝访问]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0001]{lang="EN-US"}]{#struct_0_x2158_x2842_x1415246501}[：表示具有]{style="font-family:宋体"}**[query]{lang="EN-US"}**[权限，只允许对本地]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务进行控制查询]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0002]{lang="EN-US"}]{#struct_0_x2158_x2842_670705502}[：表示具有]{style="font-family:宋体"}**[synchronization]{lang="EN-US"}**[权限，只允许对端设备与本地设备的时间同步，但不能进行控制查询]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0004]{lang="EN-US"}]{#struct_0_x2158_x2842_1149455721}[：表示具有]{style="font-family:宋体"}**[server]{lang="EN-US"}**[权限，可以对本地]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务进行时间请求和控制查询，但本地时间不会与对端设备同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x0008]{lang="EN-US"}]{#struct_0_x2158_x2842_212687222}[：表示具有]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[权限，既可以对本地]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务进行时间请求和控制查询，本地时间又可以与对端设备同步]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ntp-service adjustment]{lang="EN-US"}]{#struct_0_x2158_x2842_1301286799}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x521729948}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1688859303}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x170597294}

[[System huff size *size* min delay *delay1* huffpuff *delay2*]{lang="EN-US"}]{#struct_0_x2158_x2842_55527792}

[[huff-n\'-puff]{lang="EN-US"}]{#struct_0_x2158_x2842_x1945811692}[滤波器的阶数为]{style="font-family:宋体"}*[size]{lang="EN-US"}*[，最小延迟为]{style="font-family:宋体"}*[delay1]{lang="EN-US"}*[，过滤后的时延为]{style="font-family:宋体"}*[delay2]{lang="EN-US"}*

[[Adjust local clock]{lang="EN-US"}]{#struct_0_x2158_x2842_212752758}

[[调整本地时钟]{style="font-family:宋体"}]{#struct_0_x2158_x2842_x986271009}

[[offset: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_1530902755}

[[时钟偏移为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1959789268}

[[jitter: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x220725292}

[[时钟偏移均方根为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x945380429}

[[freq: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_212294006}

[[时钟频率为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x781572592}

[[stab: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2128454757}

[[频率稳定度为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x568578713}

[[poll: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_355564619}

[[轮询间隔为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x508403417}

[[Reset clock state]{lang="EN-US"}]{#struct_0_x2158_x2842_212359542}

[[重置时钟状态]{style="font-family:宋体"}]{#struct_0_x2158_x2842_1159580079}

[[time count difference: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2142165911}

[[时间计数差为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_2035886868}

[[state *state1*-\> *state2*]{lang="EN-US"}]{#struct_0_x2158_x2842_x913170846}

[[时钟状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_x2158_x2842_212425078}[变为]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[*[state]{lang="EN-US"}*]{#struct_0_x2158_x2842_x2089933019}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x2158_x2842_584111920}[：]{lang="EN-US" style="font-family:宋体"}[unspecified ]{lang="EN-US"}[，未定义]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x2158_x2842_x652850138}[：]{lang="EN-US" style="font-family:宋体"}[freq not set ]{lang="EN-US"}[，频率未设定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x2158_x2842_x1916800241}[：]{lang="EN-US" style="font-family:宋体"}[freq set ]{lang="EN-US"}[，频率已设定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x2158_x2842_212490614}[：]{lang="EN-US" style="font-family:宋体"}[spike detect ]{lang="EN-US"}[，检测到大的频率跳变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x2158_x2842_670711004}[：]{lang="EN-US" style="font-family:宋体"}[freq mode ]{lang="EN-US"}[，频率已确定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x2158_x2842_398591495}[：]{lang="EN-US" style="font-family:宋体"}[clock sync]{lang="EN-US"}[，时钟已同步]{lang="EN-US" style="font-family:宋体"}

[[count *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_2072592442}

[[计数器的值为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_213080438}

[[One-off system time adjustment failed. Error: *error-code*]{lang="EN-US"}]{#struct_0_x2158_x2842_x106023634}

[[一次性调整系统时钟失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1529709596}

[[Frequency error: *p1* PPM exceeds tolerance *p2* PPM]{lang="EN-US"}]{#struct_0_x2158_x2842_583118386}

[[当前时钟频率]{style="font-family:宋体"}*[p1]{lang="EN-US"}*]{#struct_0_x2158_x2842_213145974}[超出了频率阈值]{style="font-family:宋体"}*[p2]{lang="EN-US"}*

[[Failed to adjust system time]{lang="EN-US"}]{#struct_0_x2158_x2842_237779287}

[[调整系统时间失败]{style="font-family:宋体"}]{#struct_0_x2158_x2842_x479063646}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ntp-service authentication]{lang="EN-US"}]{#struct_0_x2158_x2842_x132221390}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x526364804}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_530607437}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_212556147}

[[Authentication failed]{lang="EN-US"}]{#struct_0_x2158_x2842_x526869474}

[[认证失败]{style="font-family:宋体"}]{#struct_0_x2158_x2842_x952165555}

[[auth flag *flag*]{lang="EN-US"}]{#struct_0_x2158_x2842_1557768956}

[[认证标志为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*]{#struct_0_x2158_x2842_845728130}

[[authenticate key ID *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_320391745}

[[认证密钥编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x2158_x2842_212621683}

[[packet key ID *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_1363295718}

[[收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_x2158_x2842_x1912038636}[报文中的密钥编号为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[MAC length *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2020225101}

[[MAC]{lang="EN-US"}]{#struct_0_x2158_x2842_x2107696867}[长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Received a packet at *time*, from *ip-address*, mode *mode*, key ID *id*, length *length*, authentication result *result*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1464227803}

[[在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_580877949}[，从]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[接收到带有认证信息的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，工作模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[，密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，认证结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Invalid private packet for bad length *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_212687219}

[[私有报文无效，原因：报文长度错误，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1037365354}

[[Invalid private packet, xmit/rcv timestamp delta *p1* \> *p2*]{lang="EN-US"}]{#struct_0_x2158_x2842_1251793987}

[[私有报文无效，原因：发送时间戳和接收时间戳的差值]{style="font-family:宋体"}*[p1]{lang="EN-US"}*]{#struct_0_x2158_x2842_1646249687}[大于阈值]{style="font-family:宋体"}*[p2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging ntp-service event]{lang="EN-US"}]{#struct_0_x2158_x2842_x788832894}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x532550078}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1166648256}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_212752755}

[[Clear peer at *time*]{lang="EN-US"}]{#struct_0_x2158_x2842_x986270998}

[[在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_x388611009}[清除与对端设备的连接]{style="font-family:宋体"}

[[next sent time *time*]{lang="EN-US"}]{#struct_0_x2158_x2842_1485683143}

[[下一次发送报文的时间为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_x2048458095}

[[session ID *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_x148818747}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2158_x2842_212294003}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[refid *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x781572589}

[[参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2158_x2842_x2129175652}[为]{style="font-family:宋体"}*[string]{lang="EN-US"}*

[[Sending control packet with error code *code* to *ip-address*]{lang="EN-US"}]{#struct_0_x2158_x2842_1959783698}

[[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1592277288}[发送携带错误码]{style="font-family:宋体"}*[code]{lang="EN-US"}*[的控制报文]{style="font-family:宋体"}

[[Reading status, session ID *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_1950898097}

[[读取]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2158_x2842_212359539}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[的会话的状态]{style="font-family:宋体"}

[[Event at *time*: *event*]{lang="EN-US"}]{#struct_0_x2158_x2842_1968884136}

[[在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_681387313}[发生事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Quit from the process on receiving the signal *signal*]{lang="EN-US"}]{#struct_0_x2158_x2842_362711770}

[[接收到信令]{style="font-family:宋体"}*[signal]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1589201245}[后，退出]{style="font-family:宋体"}[NTP]{lang="EN-US"}[进程]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ntp-service filter]{lang="EN-US"}]{#struct_0_x2158_x2842_x2121528316}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x530069422}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_193965438}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_212425075}

[[Clock filter: old sample, current *count1*, filter epoch *count2*, peer epoch *count3*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2089933030}

[[时钟过滤：样本太老，当前时间计数为]{style="font-family:宋体"}*[count1]{lang="EN-US"}*]{#struct_0_x2158_x2842_1793834429}[，样本时间计数为]{style="font-family:宋体"}*[count2]{lang="EN-US"}*[，参考时间计数为]{style="font-family:宋体"}*[count3]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ntp-service packet]{lang="EN-US"}]{#struct_0_x2158_x2842_x1783354862}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x535397864}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1680791438}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_490364296}

[[packet to *ip-address*]{lang="EN-US"}]{#struct_0_x2158_x2842_50669173}

[[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_212490611}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[count: *count*]{lang="EN-US"}]{#struct_0_x2158_x2842_670711007}

[[控制报文中数据的个数为]{style="font-family:宋体"}*[count]{lang="EN-US"}*]{#struct_0_x2158_x2842_398591494}

[[RMEOP: *operation*]{lang="EN-US"}]{#struct_0_x2158_x2842_2072592441}

[[控制报文中的操作码为]{style="font-family:宋体"}*[operation]{lang="EN-US"}*]{#struct_0_x2158_x2842_558174691}

[[seq: *sequence*]{lang="EN-US"}]{#struct_0_x2158_x2842_x402173879}

[[控制报文中的请求序号为]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x2158_x2842_213080435}

[[status: *status*]{lang="EN-US"}]{#struct_0_x2158_x2842_x106023637}

[[控制报文中的状态字为]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1529512988}

[[session ID: *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_845823733}

[[控制报文中的连接]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2158_x2842_1338511010}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[offset: *offset*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1210146850}

[[控制报文数据偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*]{#struct_0_x2158_x2842_213145971}

[[auth_seq: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_237779292}

[[私有报文中的消息验证码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_1477251487}

[[impl: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_2021376166}

[[私有报文中的操作码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_734346628}

[[req: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_212556148}

[[私有报文中的请求码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_x526869483}

[[err_nitems: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_x951706794}

[[私有报文的错误码或数据项的数目为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_x650627309}

[[itemsize: *size*]{lang="EN-US"}]{#struct_0_x2158_x2842_212621684}

[[每一个数据项的大小为]{style="font-family:宋体"}*[size]{lang="EN-US"}*]{#struct_0_x2158_x2842_1363295715}

[[length: *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1911842028}

[[发送报文的长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x2158_x2842_548689591}

[[leap: *leap*]{lang="EN-US"}]{#struct_0_x2158_x2842_x217797620}

[[报文中的告警信息为]{style="font-family:宋体"}*[leap]{lang="EN-US"}*]{#struct_0_x2158_x2842_212687220}

[[version: *version*]{lang="EN-US"}]{#struct_0_x2158_x2842_1301286797}

[[报文中的协议版本号为]{style="font-family:宋体"}*[version]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1688990375}

[[mode: *mode*]{lang="EN-US"}]{#struct_0_x2158_x2842_658857036}

[[报文中的工作模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*]{#struct_0_x2158_x2842_212752756}

[[vrfindex: *index*]{lang="EN-US"}]{#struct_0_x2158_x2842_x986270999}

[[收到或发送报文的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2158_x2842_x388676545}[索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[stratum: *stratum*]{lang="EN-US"}]{#struct_0_x2158_x2842_1497640550}

[[报文中的层数为]{style="font-family:宋体"}*[stratum]{lang="EN-US"}*]{#struct_0_x2158_x2842_212294004}

[[poll: *poll*]{lang="EN-US"}]{#struct_0_x2158_x2842_x781572590}

[[报文中的轮询间隔为]{style="font-family:宋体"}*[poll]{lang="EN-US"}*]{#struct_0_x2158_x2842_x2128585829}

[[precision: *precision*]{lang="EN-US"}]{#struct_0_x2158_x2842_1648146261}

[[报文中的精度为]{style="font-family:宋体"}*[precision]{lang="EN-US"}*]{#struct_0_x2158_x2842_212359540}

[[rdel: *delay*]{lang="EN-US"}]{#struct_0_x2158_x2842_1159580081}

[[报文中的根延时为]{style="font-family:宋体"}*[delay]{lang="EN-US"}*]{#struct_0_x2158_x2842_x2142690186}

[[rdsp: *disper*]{lang="EN-US"}]{#struct_0_x2158_x2842_955849714}

[[报文中的根离差为]{style="font-family:宋体"}*[disper]{lang="EN-US"}*]{#struct_0_x2158_x2842_212425076}

[[refid: *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2089933033}

[[报文中参考时钟的标识为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x2158_x2842_1390549902}

[[当参考时钟为本地时钟时，本字段的取值和本地时钟层数有关：本地时钟层数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2158_x2842_693190295}[时，为]{style="font-family:宋体"}[LOCL]{lang="EN-US"}[；本地时钟层数为其它值时，为本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[当参考时钟为网络中其它设备的时钟时，本字段为该设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2158_x2842_212490612}[地址]{style="font-family:宋体"}

[[reftime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_670711006}

[[报文中的参考时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_398591493}

[[orgtime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_213080436}

[[报文中的启始时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x106023636}

[[rectime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1529578524}

[[报文中的接收时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_1418167883}

[[xmttime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_213145972}

[[报文中的发送时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_237779293}

[[inptime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_1477251486}

[[处理报文的时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_212556145}

[[packet from *ip-address1* to *ip-address2* on *interface-name*]{lang="EN-US"}]{#struct_0_x2158_x2842_x526869472}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x2158_x2842_x951772339}[接收到源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address1]{lang="EN-US"}*[、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address2]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Invalid private packet for wrong item size, received *size1*, should be *size2* or *size3*]{lang="EN-US"}]{#struct_0_x2158_x2842_212621681}

[[私有报文无效，原因：数据项大小错误，接收到的数据项大小为]{style="font-family:宋体"}*[size1]{lang="EN-US"}*]{#struct_0_x2158_x2842_1363295720}[，应为]{style="font-family:宋体"}*[size2]{lang="EN-US"}*[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文）或]{style="font-family:宋体"}*[size3]{lang="EN-US"}*[（]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[Invalid private packet for not enough data]{lang="EN-US"}]{#struct_0_x2158_x2842_x1911514349}

[[私有报文无效，原因：数据不完整]{style="font-family:宋体"}]{#struct_0_x2158_x2842_212687217}

[[Sending request packet to *ip-address*, sequence number *number,* error code *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1037365356}

[[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_88994573}[发送请求报文，序列号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Flushing packet, *number* items]{lang="EN-US"}]{#struct_0_x2158_x2842_212752753}

[[发送]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x2158_x2842_x986271004}[个报文]{style="font-family:宋体"}

[[Failed to send packet because too many data, length *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_1531230435}

[[由于数据过多，发送报文失败，报文长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x2158_x2842_212294001}

[[Failed to set socket option, level *level*, option *option*, error code: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_x781572587}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x2158_x2842_x2128782436}[选项失败，]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项等级为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[option]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Failed to get VRF index VPN name *vpn-name*]{lang="EN-US"}]{#struct_0_x2158_x2842_212359537}

[[获取]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2158_x2842_1968884146}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[的索引失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging ntp-service parameter]{lang="EN-US"}]{#struct_0_x2158_x2842_681387316}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x510182890}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_212425073}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x2089933028}

[[Clock filter param]{lang="EN-US"}]{#struct_0_x2158_x2842_x2144968043}

[[时钟过滤参数]{style="font-family:宋体"}]{#struct_0_x2158_x2842_627184885}

[[number *number*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1344572497}

[[时间服务器的个数为]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x2158_x2842_x898210074}

[[offset *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_212490609}

[[时钟偏差为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1667941161}

[[delay *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1400140261}

[[双向延迟为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_290203286}

[[dispersion *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_1616129593}

[[离差为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_1868444985}

[[jitter *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_213080433}

[[时钟偏移均方根为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x106023639}

[[burst *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1529906204}

[[一个时钟脉冲中的数据包个数]{style="font-family:宋体"}]{#struct_0_x2158_x2842_1063032681}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging ntp-service refclock]{lang="EN-US"}]{#struct_0_x2158_x2842_1198210298}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x508012316}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x179808026}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_213145969}

[[Select PPS peer *ip-address* offset *offset*, jitter *jitter*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1718535852}

[[选取]{style="font-family:宋体"}[PPS]{lang="EN-US"}]{#struct_0_x2158_x2842_x2147226675}[类型的时钟]{style="font-family:宋体"}*[ip-address ]{lang="EN-US"}*[作为参考时钟，时钟偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[，时钟偏移量的均方根为]{style="font-family:宋体"}*[jitter]{lang="EN-US"}*

[[Reference clock sent a packet to *ip-address* at *time*]{lang="EN-US"}]{#struct_0_x2158_x2842_682965384}

[[参考时钟在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1319144702}[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[发送报文]{style="font-family:宋体"}

[[Reference clock received a packet from *ip-address* at *time*]{lang="EN-US"}]{#struct_0_x2158_x2842_1332379534}

[[参考时钟在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_212556146}[从]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[接收到报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ntp-service selection]{lang="EN-US"}]{#struct_0_x2158_x2842_x526869473}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x514507672}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x951706803}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_540686090}

[[Combine offset *offset*, jitter *jitter*]{lang="EN-US"}]{#struct_0_x2158_x2842_782897534}

[[合并时钟：系统当前时钟偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*]{#struct_0_x2158_x2842_x873939602}[，当前时钟偏移量的均方根为]{style="font-family:宋体"}*[jitter]{lang="EN-US"}*

[[Drop peer *ip-address*, select jitter *jitter2*, jitter *jitter3*]{lang="EN-US"}]{#struct_0_x2158_x2842_212621682}

[[丢弃时钟]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_1363295717}[，根据所有]{style="font-family:宋体"}[peer]{lang="EN-US"}[的]{style="font-family:宋体"}[jitter]{lang="EN-US"}[计算出的综合]{style="font-family:宋体"}[jitter]{lang="EN-US"}[为]{style="font-family:宋体"}*[jitter2]{lang="EN-US"}*[，当前]{style="font-family:宋体"}[peer]{lang="EN-US"}[连接的]{style="font-family:宋体"}[jitter]{lang="EN-US"}[为]{style="font-family:宋体"}*[jitter3]{lang="EN-US"}*

[[Survivor *ip-address*, distance *distance*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1911973100}

[[最终优选的时钟为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x681310577}[，时钟举例为]{style="font-family:宋体"}*[distance]{lang="EN-US"}*

[[endpoint *p1*, *p2*]{lang="EN-US"}]{#struct_0_x2158_x2842_x741129055}

[[时钟选择算法的终点结构体，]{style="font-family:宋体"}*[p1]{lang="EN-US"}*]{#struct_0_x2158_x2842_2117020216}[为终点偏移量，]{style="font-family:宋体"}*[p2]{lang="EN-US"}*[为步进]{style="font-family:宋体"}

[[Clock update at *time*, sample *sample*, session ID *id*, offset *offset*]{lang="EN-US"}]{#struct_0_x2158_x2842_212687218}

[[在时间]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1037365355}[更新时钟，时钟样本为]{style="font-family:宋体"}*[sample]{lang="EN-US"}*[，会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，当前时钟偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[peer *ip-address*, flash *code*, flags *flag*, reach *reach*, root distance *distance*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1477089368}

[[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_6803344}[的时间服务器的可达性，与该时间服务器连接的错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[，会话标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[，可达性为]{style="font-family:宋体"}*[reach]{lang="EN-US"}*[，根同步距离为]{style="font-family:宋体"}*[distance]{lang="EN-US"}*

[[peer *ip-address*, offset *offset*, low *low*, high *high*, flags *flag*]{lang="EN-US"}]{#struct_0_x2158_x2842_1208149425}

[[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_212752754}[的时间服务器的连接信息：时钟偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[，插值算法的最小阈值为]{style="font-family:宋体"}*[low]{lang="EN-US"}*[，插值算法的最大阈值为]{style="font-family:宋体"}*[high]{lang="EN-US"}*[，会话标识为]{style="font-family:宋体"}*[flag]{lang="EN-US"}*

[[set large distance peer *ip-address*, root distance *distance*]{lang="EN-US"}]{#struct_0_x2158_x2842_x986270997}

[[保存同步距离过大的时间服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x388545473}[，同步距离为]{style="font-family:宋体"}*[distance]{lang="EN-US"}*

[[select large distance syspeer *ip-address* ]{lang="EN-US"}]{#struct_0_x2158_x2842_x1233613867}

[[选择同步距离过大的时间服务器]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x24769560}[作为参考时钟]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging ntp-service synchronization]{lang="EN-US"}]{#struct_0_x2158_x2842_212294002}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x512031112}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x781572588}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x2129110116}

[[Synchronized to peer *address*]{lang="EN-US"}]{#struct_0_x2158_x2842_1840176419}

[[本地设备的时间与地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x577730538}[的]{style="font-family:宋体"}[peer]{lang="EN-US"}[的时间同步]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging ntp-service validity]{lang="EN-US"}]{#struct_0_x2158_x2842_x2101214562}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x513332569}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_165981859}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_212359538}

[[The packet from *ip-address string* the validity tests *result*]{lang="EN-US"}]{#struct_0_x2158_x2842_1968884137}

[[从]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_681452849}[接收到的报文通过（]{style="font-family:宋体"}[pass]{lang="EN-US"}[）或未通过（]{style="font-family:宋体"}[failed]{lang="EN-US"}[）合法性检查，检查结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1385722966}

[[\# ]{lang="EN-US"}]{#struct_0_x2158_x2842_x887247110}[网络中有两台设备]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[，]{style="font-family:宋体"}[Device A]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.19]{lang="EN-US"}[，]{style="font-family:宋体"}[Device B]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[，它们之间可以相互]{style="font-family:宋体"}[ping]{lang="EN-US"}[通。]{style="font-family:宋体"}[Device B]{lang="EN-US"}[使用本地时钟作为参考时钟，时钟层数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}[Device A]{lang="EN-US"}[通过客户端]{style="font-family:宋体"}[/]{lang="EN-US"}[服务器模式与]{style="font-family:宋体"}[Device B]{lang="EN-US"}[的时间同步时，]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打印如下调试信息。]{style="font-family:宋体"}

[[\<DeviceA\> debugging ntp-service packet]{lang="EN-US"}]{#struct_0_x2158_x2842_212425074}

[\<DeviceA\> system-view]{lang="EN-US"}

[\[DeviceA\] ntp-service unicast-server 192.168.0.13 version 3]{lang="EN-US"}

[\*Jan 25 19:58:23:206 2012 H3C NTP/7/PACKET_SEND:]{lang="EN-US"}

[ packet to 192.168.0.13, length: 48]{lang="EN-US"}

[ leap: 3, version: 3, mode: 3, vrfindex: 0]{lang="EN-US"}

[ stratum: 16, poll: 6, precision: 2\^-10]{lang="EN-US"}

[ rdel: 0.000, rdsp: 0.092, refid: INIT]{lang="EN-US"}

[ reftime: d2cadcdc.350d4fcd  Wed, Jan 25 2012 19:56:12.207]{lang="EN-US"}

[ orgtime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ rectime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ xmttime: d2cadd5f.3469b5b7  Wed, Jan 25 2012 19:58:23.204]{lang="EN-US"}

[*[// NTP]{lang="EN-US"}*]{#struct_0_x2158_x2842_x2089933031}*[模块向]{style="font-family:宋体"}[Device B]{lang="EN-US"}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时间同步报文：报文的目的地址是]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[；报文长度为]{style="font-family:宋体"}[48]{lang="EN-US"}[字节；本地时钟告警位取值为]{style="font-family:宋体"}[3]{lang="EN-US"}[；本地]{style="font-family:宋体"}[NTP]{lang="EN-US"}[协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[；工作模式为]{style="font-family:宋体"}[3]{lang="EN-US"}[；报文出端口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[（即公网）；本地时钟层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[；轮询间隔为]{style="font-family:宋体"}[64]{lang="EN-US"}[秒；时钟精度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[10]{lang="EN-US"}[次方分之一秒级别；本地根延迟为]{style="font-family:宋体"}[0.000]{lang="EN-US"}[；根离差为]{style="font-family:宋体"}[0.092]{lang="EN-US"}[；参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，表明没有参考时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳和发送时间戳]{style="font-family:宋体"}*

[[\*Jan 25 19:49:45:403 2012 H3C NTP/7/PACKET_RECV:]{lang="EN-US"}]{#struct_0_x2158_x2842_227750488}

[ packet from 192.168.0.13 to 192.168.0.19 on GigabitEthernet1/0/1]{lang="EN-US"}

[ leap: 0, version: 3, mode: 4, vrfindex: 0]{lang="EN-US"}

[ stratum:  2, poll: 6, precision: 2\^-18]{lang="EN-US"}

[ rdel: 0.000, rdsp: 10.941, refid: 127.127.1.0]{lang="EN-US"}

[ reftime: d2cadbe0.1a74d163  Wed, Jan 25 2012 19:52:00.103]{lang="EN-US"}

[ orgtime: d2cadb59.6569818c  Wed, Jan 25 2012 19:49:45.396]{lang="EN-US"}

[ rectime: d2cadc0e.f2d6a9c5  Wed, Jan 25 2012 19:52:46.948]{lang="EN-US"}

[ xmttime: d2cadc0e.f2e12620  Wed, Jan 25 2012 19:52:46.948]{lang="EN-US"}

[ inptime: 59dbcad2.f6985367  Fri, Oct 10 1947 19:15:30.963]{lang="EN-US"}

[*[// Device A]{lang="EN-US"}*]{#struct_0_x2158_x2842_912980749}*[收到]{style="font-family:宋体"}[Device B]{lang="EN-US"}[发过来的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[响应报文：对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[，本端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.19]{lang="EN-US"}[，报文入接口是]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[；对端的告警位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示处于已同步状态；对端]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[；工作模式为]{style="font-family:宋体"}[4]{lang="EN-US"}[；对端报文的出接口属于的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[；对端时钟的层数为]{style="font-family:宋体"}[2]{lang="EN-US"}[；轮询间隔为]{style="font-family:宋体"}[64]{lang="EN-US"}[秒；精度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[18]{lang="EN-US"}[次方分之一秒级别；对端的根延迟为]{style="font-family:宋体"}[0.000]{lang="EN-US"}[；根离差为]{style="font-family:宋体"}[10.941]{lang="EN-US"}[；对端的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[127.127.1.0]{lang="EN-US"}[，即本地时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳、发送时间戳和本地处理该报文的时间戳]{style="font-family:宋体"}*

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NTP%20Debug.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2158_x2842_1946148300}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[实际上，上述的报文交互过程会进行多次，此处仅给出前两个报文的信息。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x2158_x2842_212490610}
:::

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#-322447194 .myid}
[]{#_Toc404796572}[]{#struct_0_x2158_x2842_2072592446}

**SNTP \-- SNTP调试命令 \-- debugging sntp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_557978083}

[**[debugging sntp]{lang="EN-US"}**[ { **adjustment** \| **all** \| **packet** \| **selection** }]{lang="EN-US"}]{#struct_0_x2158_x2842_x1184357210}

[**[undo debugging sntp ]{lang="EN-US"}**[{ **adjustment** \| **all** \| **packet** \| **selection** }]{lang="EN-US"}]{#struct_0_x2158_x2842_1796072929}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1188204680}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2158_x2842_213080434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x106023638}

[[network-admin]{lang="EN-US"}]{#struct_0_x2158_x2842_x1529971740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2158_x2842_x2120961059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_1951368707}

[**[adjustment]{lang="EN-US"}**]{#struct_0_x2158_x2842_x1105081844}[：表示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[时钟调节调试信息开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x2158_x2842_406525059}[：表示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x2158_x2842_x1656471804}[：表示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[selection]{lang="EN-US"}**]{#struct_0_x2158_x2842_x643769021}[：表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时钟选择调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_213145970}

[**[debugging sntp]{lang="EN-US"}**]{#struct_0_x2158_x2842_237779291}[命令用来打开]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging sntp]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_x2158_x2842_1477251484}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表2-1 ]{lang="EN-US"}[debugging sntp adjustment]{lang="EN-US"}]{#struct_0_x2158_x2842_2021179558}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x518693779}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x76464020}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1889001083}

[[System huff size *size* min delay *delay1* huffpuff *delay2*]{lang="EN-US"}]{#struct_0_x2158_x2842_x414477765}

[[huff-n\'-puff]{lang="EN-US"}]{#struct_0_x2158_x2842_2134870450}[滤波器的阶数为]{style="font-family:宋体"}*[size]{lang="EN-US"}*[，最小延迟为]{style="font-family:宋体"}*[delay1]{lang="EN-US"}*[，过滤后的时延为]{style="font-family:宋体"}*[delay2]{lang="EN-US"}*

[[Adjust local clock]{lang="EN-US"}]{#struct_0_x2158_x2842_1555957655}

[[调整本地时钟]{style="font-family:宋体"}]{#struct_0_x2158_x2842_245363631}

[[offset: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x959554255}

[[时钟偏移为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_716840963}

[[jitter: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_1021708578}

[[时钟偏移量的均方根为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134935986}

[[freq: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_849854530}

[[时钟频率为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_1692258242}

[[stab: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1110068198}

[[频率稳定度为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_234623335}

[[poll: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x676806027}

[[轮询间隔为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_2135001522}

[[Reset clock state]{lang="EN-US"}]{#struct_0_x2158_x2842_1577948161}

[[重置时钟状态]{style="font-family:宋体"}]{#struct_0_x2158_x2842_x1682534643}

[[time count difference: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_953652259}

[[时间计数差为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_756620236}

[[state *state1*-\> *state2*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135067058}

[[时钟状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*]{#struct_0_x2158_x2842_1984408270}[变为]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[*[state]{lang="EN-US"}*]{#struct_0_x2158_x2842_2091438611}[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x2158_x2842_x943085607}[：]{lang="EN-US" style="font-family:宋体"}[unspecified ]{lang="EN-US"}[，未定义]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x2158_x2842_2134608306}[：]{lang="EN-US" style="font-family:宋体"}[freq not set ]{lang="EN-US"}[，频率未设定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x2158_x2842_x1180324428}[：]{lang="EN-US" style="font-family:宋体"}[freq set ]{lang="EN-US"}[，频率已设定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x2158_x2842_x125682904}[：]{lang="EN-US" style="font-family:宋体"}[spike detect ]{lang="EN-US"}[，检测到大的频率跳变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_x2158_x2842_1854728912}[：]{lang="EN-US" style="font-family:宋体"}[freq mode ]{lang="EN-US"}[，频率已确定]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_x2158_x2842_x1908749943}[：]{lang="EN-US" style="font-family:宋体"}[clock sync]{lang="EN-US"}[，时钟已同步]{lang="EN-US" style="font-family:宋体"}

[[count *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134673842}

[[计数器的值为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_1990688123}

[[One-off system time adjustment failed. Error: *error-code*]{lang="EN-US"}]{#struct_0_x2158_x2842_1303098257}

[[一次性调整系统时钟失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*]{#struct_0_x2158_x2842_105695429}

[[Frequency error: *p1* PPM exceeds tolerance *p2* PPM]{lang="EN-US"}]{#struct_0_x2158_x2842_2134739378}

[[当前时钟频率]{style="font-family:宋体"}*[p1]{lang="EN-US"}*]{#struct_0_x2158_x2842_383072445}[超出了频率阈值]{style="font-family:宋体"}*[p2]{lang="EN-US"}*

[[Failed to adjust system time.]{lang="EN-US"}]{#struct_0_x2158_x2842_x2119812523}

[[调整系统时间失败]{style="font-family:宋体"}]{#struct_0_x2158_x2842_1009531632}

[ ]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[debugging sntp packet ]{lang="EN-US"}]{#struct_0_x2158_x2842_x314927135}[命令信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x517179942}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_2134804914}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x714066649}

[[packet to *ip-address*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2113488150}

[[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_x197597530}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[count: *count*]{lang="EN-US"}]{#struct_0_x2158_x2842_x2778464}

[[控制报文中数据的个数为]{style="font-family:宋体"}*[count]{lang="EN-US"}*]{#struct_0_x2158_x2842_x479404184}

[[RMEOP: *operation*]{lang="EN-US"}]{#struct_0_x2158_x2842_1798165747}

[[控制报文中的操作码为]{style="font-family:宋体"}*[operation]{lang="EN-US"}*]{#struct_0_x2158_x2842_2135394738}

[[seq: *sequence*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1954400884}

[[控制报文中的请求序号为]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x2158_x2842_x938948595}

[[status: *status*]{lang="EN-US"}]{#struct_0_x2158_x2842_x208238631}

[[控制报文中的状态字为]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*]{#struct_0_x2158_x2842_x75197035}

[[session ID: *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1634733336}

[[控制报文中的连接]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x2158_x2842_2135460274}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*

[[offset: *offset*]{lang="EN-US"}]{#struct_0_x2158_x2842_1964247325}

[[控制报文数据偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*]{#struct_0_x2158_x2842_x994278327}

[[auth_seq: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_1438417065}

[[私有报文中的消息验证码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_1993717444}

[[impl: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134870451}

[[私有报文中的操作码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_1555892119}

[[req: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_1789541075}

[[私有报文中的请求码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_1981803366}

[[err_nitems: *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1606614571}

[[私有报文的错误码或数据项的数目为]{style="font-family:宋体"}*[code]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134935987}

[[itemsize: *size*]{lang="EN-US"}]{#struct_0_x2158_x2842_849788994}

[[每一个数据项的大小为]{style="font-family:宋体"}*[size]{lang="EN-US"}*]{#struct_0_x2158_x2842_699750863}

[[length: *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_x609315448}

[[发送报文的长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x2158_x2842_1205090339}

[[leap: *leap*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135001523}

[[报文中的告警信息为]{style="font-family:宋体"}*[leap]{lang="EN-US"}*]{#struct_0_x2158_x2842_1578013697}

[[version: *version*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1901942374}

[[报文中的协议版本号为]{style="font-family:宋体"}*[version]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1349680054}

[[mode: *mode*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135067059}

[[报文中的工作模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*]{#struct_0_x2158_x2842_1984473806}

[[vrfindex: *index*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1428815277}

[[收到或发送报文的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2158_x2842_1102203153}[索引为]{style="font-family:宋体"}*[index]{lang="EN-US"}*

[[stratum: *stratum*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134608307}

[[报文中的层数为]{style="font-family:宋体"}*[stratum]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1180258892}

[[poll: *poll*]{lang="EN-US"}]{#struct_0_x2158_x2842_1224265257}

[[报文中的轮询间隔为]{style="font-family:宋体"}*[poll]{lang="EN-US"}*]{#struct_0_x2158_x2842_x418785708}

[[precision: *precision*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134673843}

[[报文中的精度为]{style="font-family:宋体"}*[precision]{lang="EN-US"}*]{#struct_0_x2158_x2842_1990622587}

[[rdel: *delay*]{lang="EN-US"}]{#struct_0_x2158_x2842_x281120963}

[[报文中的根延时为]{style="font-family:宋体"}*[delay]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1213840287}

[[rdsp: *disper*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134739379}

[[报文中的根离差为]{style="font-family:宋体"}*[disper]{lang="EN-US"}*]{#struct_0_x2158_x2842_383006909}

[[refid: *id*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1410843427}

[[报文中参考时钟的标识为]{style="font-family:宋体"}*[id]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134804915}

[[当参考时钟为本地时钟时，本字段的取值和本地时钟层数有关：本地时钟层数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2158_x2842_x714001113}[时，为]{style="font-family:宋体"}[LOCL]{lang="EN-US"}[；本地时钟层数为其它值时，为本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[当参考时钟为网络中其它设备的时钟时，本字段为该设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2158_x2842_266034462}[地址]{style="font-family:宋体"}

[[reftime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135394739}

[[报文中的参考时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1954466420}

[[orgtime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1124591861}

[[报文中的启始时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1069313736}

[[rectime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135460275}

[[报文中的接收时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_1964312861}

[[xmttime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_x935772893}

[[报文中的发送时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134870448}

[[inptime: *string*]{lang="EN-US"}]{#struct_0_x2158_x2842_1556481942}

[[处理报文的时间戳为]{style="font-family:宋体"}*[string]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1441353747}

[[packet from *ip-address1* to *ip-address2* on *interface-name*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134935984}

[[从接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x2158_x2842_849985602}[接收到源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address1]{lang="EN-US"}*[、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address2]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Invalid private packet for wrong item size, received *size1*, should be *size2* or *size3*]{lang="EN-US"}]{#struct_0_x2158_x2842_2088197234}

[[私有报文无效，原因：数据项大小错误，接收到的数据项大小为]{style="font-family:宋体"}*[size1]{lang="EN-US"}*]{#struct_0_x2158_x2842_2135001520}[，应为]{style="font-family:宋体"}*[size2]{lang="EN-US"}*[（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文）或]{style="font-family:宋体"}*[size3]{lang="EN-US"}*[（]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文）]{style="font-family:宋体"}

[[Invalid private packet for not enough data]{lang="EN-US"}]{#struct_0_x2158_x2842_1578079233}

[[私有报文无效，原因：数据不完整]{style="font-family:宋体"}]{#struct_0_x2158_x2842_1651645334}

[[Sending request packet to *ip-address*, sequence number *number,* error code *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_2135067056}

[[向]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x2158_x2842_1985325774}[发送请求报文，序列号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Flushing packet, *number* items]{lang="EN-US"}]{#struct_0_x2158_x2842_x1109016933}

[[发送]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134608304}[个报文]{style="font-family:宋体"}

[[Failed to send packet because too many data, length *length*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1180193356}

[[由于数据过多，发送报文失败，报文长度为]{style="font-family:宋体"}*[length ]{lang="EN-US"}*]{#struct_0_x2158_x2842_x471000142}

[[Failed to set socket option, level *level*, option *option*, error code *code*]{lang="EN-US"}]{#struct_0_x2158_x2842_2134673840}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x2158_x2842_1990819195}[选项失败，]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项等级为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，]{style="font-family:宋体"}[socket]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[option]{lang="EN-US"}*[，错误码为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Failed to get VRF index, VPN name *vpn-name*]{lang="EN-US"}]{#struct_0_x2158_x2842_x1440793031}

[[获取]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x2158_x2842_2134739376}[实例]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[的索引失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表2-3 ]{lang="EN-US"}[debugging sntp selection ]{lang="EN-US"}]{#struct_0_x2158_x2842_383727805}[命令描述表]{style="font-family:黑体"}

[]{#table_struct_0_x491964976}[[字段]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x1387417302}

[[描述]{style="font-family:黑体"}]{#struct_0_x2158_x2842_464579481}

[[Select peer *ip-address*, offset *offset*]{lang="EN-US"}]{#struct_0_x2158_x2842_202988748}

[[选取]{style="font-family:宋体"}*[ip-address ]{lang="EN-US"}*]{#struct_0_x2158_x2842_2134804912}[作为参考时钟，时钟偏移量为]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2158_x2842_x714459865}

[[\# ]{lang="EN-US"}]{#struct_0_x2158_x2842_1035797215}[网络中有两台设备]{style="font-family:宋体"}[Device A]{lang="EN-US"}[和]{style="font-family:宋体"}[Device B]{lang="EN-US"}[，]{style="font-family:宋体"}[Device A]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.19]{lang="EN-US"}[，]{style="font-family:宋体"}[Device B]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[，它们之间可以相互]{style="font-family:宋体"}[ping]{lang="EN-US"}[通。]{style="font-family:宋体"}[Device B]{lang="EN-US"}[使用本地时钟作为参考时钟，时钟层数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。在]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打开]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[报文调试开关。]{style="font-family:宋体"}[Device A]{lang="EN-US"}[作为]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[客户端，通过客户端]{style="font-family:宋体"}[/]{lang="EN-US"}[服务器模式与]{style="font-family:宋体"}[Device B]{lang="EN-US"}[的时间同步时，]{style="font-family:宋体"}[Device A]{lang="EN-US"}[上打印如下调试信息。]{style="font-family:宋体"}

[[\<DeviceA\> debugging sntp all]{lang="EN-US"}]{#struct_0_x2158_x2842_x1733118230}

[\<DeviceA\> system-view]{lang="EN-US"}

[\[DeviceA\] sntp unicast-server 192.168.0.13 version 3]{lang="EN-US"}

[\*Jan 25 20:05:11:765 2012 H3C SNTP/7/PACKET_SEND:]{lang="EN-US"}

[ packet to 192.168.0.13, length: 48]{lang="EN-US"}

[ leap: 0, version: 3, mode: 3, vrfindex: 0]{lang="EN-US"}

[ stratum:  3, poll: 6, precision: 2\^-10]{lang="EN-US"}

[ rdel: 0.000, rdsp: 0.946, refid: 192.168.0.13]{lang="EN-US"}

[ reftime: d2cadeb7.c4631f0b  Wed, Jan 25 2012 20:04:07.767]{lang="EN-US"}

[ orgtime: d2cadf61.b1c7abfb  Wed, Jan 25 2012 20:06:57.694]{lang="EN-US"}

[ rectime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ xmttime: d2cadef7.c384ff1a  Wed, Jan 25 2012 20:05:11.763]{lang="EN-US"}

[*[// SNTP]{lang="EN-US"}*]{#struct_0_x2158_x2842_1924788662}*[模块向]{style="font-family:宋体"}[Device B]{lang="EN-US"}[发送]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[时间同步报文：报文的目的地址是]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[；报文长度为]{style="font-family:宋体"}[48]{lang="EN-US"}[字节；本地时钟告警位取值为]{style="font-family:宋体"}[3]{lang="EN-US"}[；本地]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[；工作模式为]{style="font-family:宋体"}[3]{lang="EN-US"}[；报文出端口所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[（即公网）；本地时钟层数为]{style="font-family:宋体"}[3]{lang="EN-US"}[；轮询间隔为]{style="font-family:宋体"}[64]{lang="EN-US"}[秒；时钟精度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[10]{lang="EN-US"}[次方分之一秒级别；本地根延迟为]{style="font-family:宋体"}[0.000]{lang="EN-US"}[；根离差为]{style="font-family:宋体"}[0.946]{lang="EN-US"}[；参考时钟的]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[，表明向]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[同步；后续的信息分别是参考时间戳、起始时间戳、接收时间戳和发送时间戳]{style="font-family:宋体"}*

[[\*Jan 25 20:05:11:770 2012 H3C SNTP/7/PACKET_RECV:]{lang="EN-US"}]{#struct_0_x2158_x2842_2135394736}

[ packet from 192.168.0.13 to 192.168.0.19 on GigabitEthernet1/0/1]{lang="EN-US"}

[ leap: 0, version: 3, mode: 4, vrfindex: 0]{lang="EN-US"}

[ stratum:  2, poll: 6, precision: 2\^-18]{lang="EN-US"}

[ rdel: 0.000, rdsp: 10.925, refid: 127.127.1.0]{lang="EN-US"}

[ reftime: d2cadfe9.1a93d102  Wed, Jan 25 2012 20:09:13.103]{lang="EN-US"}

[ orgtime: d2cadef7.c384ff1a  Wed, Jan 25 2012 20:05:11.763]{lang="EN-US"}

[ rectime: d2cae015.9b3b85e8  Wed, Jan 25 2012 20:09:57.606]{lang="EN-US"}

[ xmttime: d2cae015.9b45ae5f  Wed, Jan 25 2012 20:09:57.606]{lang="EN-US"}

[ inptime: f7decad2.7a58fac4  Sun, Oct 12 2031 15:14:26.477]{lang="EN-US"}

[*[// Device A]{lang="EN-US"}*]{#struct_0_x2158_x2842_x1954531956}*[收到]{style="font-family:宋体"}[Device B]{lang="EN-US"}[发过来的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[响应报文：对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.13]{lang="EN-US"}[，本端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}[192.168.0.19]{lang="EN-US"}[，报文入接口是]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[；对端的告警位为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示处于已同步状态；对端]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[；工作模式为]{style="font-family:宋体"}[4]{lang="EN-US"}[；对端报文的出接口属于的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[；对端时钟的层数为]{style="font-family:宋体"}[2]{lang="EN-US"}[；轮询间隔为]{style="font-family:宋体"}[64]{lang="EN-US"}[秒；精度为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[18]{lang="EN-US"}[次方分之一秒级别；对端的根延迟为]{style="font-family:宋体"}[0.000]{lang="EN-US"}[；根离差为]{style="font-family:宋体"}[10.925]{lang="EN-US"}[；对端的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[127.127.1.0]{lang="EN-US"}[，即本地时钟；后续的信息分别是参考时间戳、起始时间戳、接收时间戳、发送时间戳和本地处理该报文的时间戳]{style="font-family:宋体"}*
