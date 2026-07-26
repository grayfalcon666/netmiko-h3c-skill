::: {#-451464956 .myid}
[]{#_Toc404785258}[]{#struct_0_13902_55743_1745730021}[]{#_Toc327384577}

**3G/4G Modem管理 \-- 3G/4G Modem管理调试命令 \-- debugging cellular**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13902_55743_x439270542}

[**[debugging cellular]{lang="EN-US"}**[ { **error** \| **event** }]{lang="EN-US"}]{#struct_0_13902_55743_x725032467}

[**[undo debugging cellular]{lang="EN-US"}**[ { **error** \| **event** }]{lang="EN-US"}]{#struct_0_13902_55743_2115471795}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13902_55743_x2063235962}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13902_55743_x1945756975}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13902_55743_1772937570}

[[network-admin]{lang="EN-US"}]{#struct_0_13902_55743_1864137451}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13902_55743_x1967291409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13902_55743_x1379646096}

[**[error]{lang="EN-US"}**]{#struct_0_13902_55743_x365584836}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13902_55743_353956752}[：表示事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13902_55743_x523849942}

[**[debugging cellular]{lang="EN-US"}**]{#struct_0_13902_55743_2116061619}[命令用来打开]{style="font-family:宋体"}[cellular]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[**[undo debugging cellular]{lang="EN-US"}**]{#struct_0_13902_55743_x234585078}[命令用来关闭]{style="font-family:宋体"}[cellular]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[cellular]{lang="EN-US"}]{#struct_0_13902_55743_92707696}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging cellular error]{lang="EN-US"}]{#struct_0_13902_55743_x432534338}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_584768534}[[字段]{style="font-family:黑体"}]{#struct_0_13902_55743_848039943}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13902_55743_x981966564}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_13902_55743_1133850239}

[[分配内存失败]{style="font-family:宋体"}]{#struct_0_13902_55743_921310228}

[[Controller *controller-name*: No device plug-in found]{lang="EN-US"}]{#struct_0_13902_55743_119290336}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2116127155}[的控制器接口没有找到对应的设备插件]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to get device major number]{lang="EN-US"}]{#struct_0_13902_55743_2128768217}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_333892631}[的控制器接口获取设备主设备号失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to initialize device]{lang="EN-US"}]{#struct_0_13902_55743_x1983831491}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_356217389}[的控制器接口初始化设备失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to initialize device, error code is *error-code*]{lang="EN-US"}]{#struct_0_13902_55743_750102786}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2115537328}[的控制器接口初始化设备失败，返回错误码]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Controller *controller-name*: Failed to open device *device-name*]{lang="EN-US"}]{#struct_0_13902_55743_x1656656544}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x1294086840}[的控制器接口打开名为]{style="font-family:宋体"}*[device-name]{lang="EN-US"}*[的设备失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to read data from device]{lang="EN-US"}]{#struct_0_13902_55743_1430646057}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x963368034}[的控制器接口从设备读取数据失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to write data to device]{lang="EN-US"}]{#struct_0_13902_55743_x415269874}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2115602864}[的控制器接口向设备写入数据失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to send IOCTL command *command* to device]{lang="EN-US"}]{#struct_0_13902_55743_x823586894}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x1955129332}[的控制器接口向设备下发]{style="font-family:宋体"}[IOCTL]{lang="EN-US"}[命令字]{style="font-family:宋体"}*[command]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to reboot device]{lang="EN-US"}]{#struct_0_13902_55743_x256347247}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x694369809}[的控制器接口重启设备失败]{style="font-family:宋体"}

[[Controller *controller-name*: Failed to send command \"*command-name*\" to device plug-in, error code is *error-code*]{lang="EN-US"}]{#struct_0_13902_55743_x1182004112}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2115668400}[的控制器接口向设备插件下发命令]{style="font-family:宋体"}*[command-name]{lang="EN-US"}*[失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Controller *controller-name*: Failed to complete command \"*command-name*\", error code is *error-code*]{lang="EN-US"}]{#struct_0_13902_55743_x1310089794}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1456374113}[的控制器接口执行名为]{style="font-family:宋体"}*[command-name]{lang="EN-US"}*[的命令失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Controller *controller-name*: Failed to read data from device plug-in, error code is *error-code*]{lang="EN-US"}]{#struct_0_13902_55743_727012041}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x994698397}[的控制器接口从设备插件读取数据失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Controller *controller-name*: Failed to write data to device plug-in, error code is error-code]{lang="EN-US"}]{#struct_0_13902_55743_2115733936}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x1598317899}[的控制器接口向设备插件写数据失败，错误码为]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*

[[Interface *interface-name*: Failed to send a link message.]{lang="EN-US"}]{#struct_0_13902_55743_x822874361}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_326381422}[发送链路消息失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send a dialer message.]{lang="EN-US"}]{#struct_0_13902_55743_1458904140}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_1322865026}[发送拨号消息失败]{style="font-family:宋体"}

[[Interface *interface-index*: Invalid index in dialer message.]{lang="EN-US"}]{#struct_0_13902_55743_1906008994}

[[拨号消息中的接口索引]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_13902_55743_1709361337}[非法]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to add new DNS address*.*]{lang="EN-US"}]{#struct_0_13902_55743_1754962084}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_339925053}[添加新]{style="font-family:宋体"}[DNS]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to add new IP address*.*]{lang="EN-US"}]{#struct_0_13902_55743_2045661162}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_586853428}[添加新]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to get interface information.]{lang="EN-US"}]{#struct_0_13902_55743_x1846274671}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_x1226158888}[获取接口信息失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging cellular event]{lang="EN-US"}]{#struct_0_13902_55743_1951124088}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_580615029}[[字段]{style="font-family:黑体"}]{#struct_0_13902_55743_x1057205634}

[[描述]{style="font-family:黑体"}]{#struct_0_13902_55743_221200611}

[[Controller *controller-name*: Controller is activated]{lang="EN-US"}]{#struct_0_13902_55743_86893019}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1403378970}[的控制器接口被激活]{style="font-family:宋体"}

[[Controller *controller-name*: Controller is deactivated]{lang="EN-US"}]{#struct_0_13902_55743_1006356708}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2115275184}[的控制器接口被去激活]{style="font-family:宋体"}

[[Controller *controller-name*: Controller is deleted]{lang="EN-US"}]{#struct_0_13902_55743_x884582853}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_364731290}[的控制器接口被删除]{style="font-family:宋体"}

[[Controller *controller-name*: Opened device *device-name*]{lang="EN-US"}]{#struct_0_13902_55743_x1924050500}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x2086632534}[的控制器接口打开了设备名为]{style="font-family:宋体"}*[device-name]{lang="EN-US"}*[的设备]{style="font-family:宋体"}

[[Controller *controller-name*: Closed device]{lang="EN-US"}]{#struct_0_13902_55743_x382997711}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x839539935}[的控制器接口关闭了设备]{style="font-family:宋体"}

[[Controller *controller-name*: Device major No. is *major-number*]{lang="EN-US"}]{#struct_0_13902_55743_2115340720}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_668006403}[的控制器接口的设备的主设备号为]{style="font-family:宋体"}*[major-number]{lang="EN-US"}*

[[Controller *controller-name*: Initializing device]{lang="EN-US"}]{#struct_0_13902_55743_x378983339}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1333950334}[的控制器接口正在初始化设备]{style="font-family:宋体"}

[[Controller *controller-name*: Device initialization completed]{lang="EN-US"}]{#struct_0_13902_55743_x1542974477}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_453126002}[的控制器接口的设备初始化完成]{style="font-family:宋体"}

[[Controller *controller-name*: Device removing completed]{lang="EN-US"}]{#struct_0_13902_55743_2115406256}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x881401253}[的控制器接口的设备拔出完成]{style="font-family:宋体"}

[[Controller *controller-name*: Device is rebooted]{lang="EN-US"}]{#struct_0_13902_55743_2104277384}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1322415360}[的控制器接口的设备被重启]{style="font-family:宋体"}

[[Controller *controller-name*: Read *byte-counts* bytes of data from device]{lang="EN-US"}]{#struct_0_13902_55743_x2089560695}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1931372513}[的控制器接从设备读取了]{style="font-family:宋体"}*[byte-counts]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[Controller *controller-name*: Wrote *byte-counts* bytes of data to device]{lang="EN-US"}]{#struct_0_13902_55743_2115471792}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x2063039354}[的控制器接口向设备写了]{style="font-family:宋体"}*[byte-counts]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[Controller *controller-name*: Sent IOCTL command *command-value* to device]{lang="EN-US"}]{#struct_0_13902_55743_463232809}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_673162457}[的控制器接口向设备发送值为]{style="font-family:宋体"}*[command-value]{lang="EN-US"}*[的]{style="font-family:宋体"}[IOCTL]{lang="EN-US"}[命令字]{style="font-family:宋体"}

[[Controller *controller-name*: Read data from device plug-in]{lang="EN-US"}]{#struct_0_13902_55743_x519232512}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2116061616}[的控制器接口从设备插件读取了数据]{style="font-family:宋体"}

[[Controller *controller-name*: Wrote *byte-counts* bytes of data to device plug-in]{lang="EN-US"}]{#struct_0_13902_55743_x233733110}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1777751890}[的控制器接口向设备插件写了]{style="font-family:宋体"}*[byte-counts]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[Sent command *command-name* to device plug-in (major No. *major-number*)]{lang="EN-US"}]{#struct_0_13902_55743_x351551471}

[[向主设备号为]{style="font-family:宋体"}*[major-number]{lang="EN-US"}*]{#struct_0_13902_55743_1428979154}[的设备插件发送名为]{style="font-family:宋体"}*[command-name]{lang="EN-US"}*[的命令]{style="font-family:宋体"}

[[Controller *controller-name*: Sent command *command-name* to device plug-in]{lang="EN-US"}]{#struct_0_13902_55743_2116127152}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_2129095897}[的控制器接口向设备插件发送名为]{style="font-family:宋体"}*[command-name]{lang="EN-US"}*[的命令字]{style="font-family:宋体"}

[[Controller *controller-name*: Command *command-name* completed]{lang="EN-US"}]{#struct_0_13902_55743_x1237792377}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_1574877407}[的控制器接口名为]{style="font-family:宋体"}*[command-name]{lang="EN-US"}*[的命令处理完成]{style="font-family:宋体"}

[[Added timer *timer-id*, whose interval is *time-interval* seconds]{lang="EN-US"}]{#struct_0_13902_55743_2115537329}

[[创建]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13902_55743_x1656722080}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器，超时时间为]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Controller *controller-name*: Added timer *timer-id*, whose interval is *time-interval* seconds]{lang="EN-US"}]{#struct_0_13902_55743_203313032}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_x1198323657}[的控制器接口创建]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器，超时时间为]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Timer timed out]{lang="EN-US"}]{#struct_0_13902_55743_2115602865}

[[定时器超时]{style="font-family:宋体"}]{#struct_0_13902_55743_x823521358}

[[Controller *controller-name*: Timer timed out]{lang="EN-US"}]{#struct_0_13902_55743_723547609}

[[接口名为]{style="font-family:宋体"}*[controller-name]{lang="EN-US"}*]{#struct_0_13902_55743_484905330}[的控制器接口下定时器超时]{style="font-family:宋体"}

[[Suspended timer *timer-id*]{lang="EN-US"}]{#struct_0_13902_55743_2115668401}

[[ID]{lang="EN-US"}]{#struct_0_13902_55743_x1310024258}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器被挂起]{style="font-family:宋体"}

[[Activated timer *timer-id*]{lang="EN-US"}]{#struct_0_13902_55743_x1026940896}

[[ID]{lang="EN-US"}]{#struct_0_13902_55743_x1528595861}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器被激活]{style="font-family:宋体"}

[[Refreshed timer *timer-id*\'s interval to *time-interval* seconds]{lang="EN-US"}]{#struct_0_13902_55743_2115733937}

[[修改]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13902_55743_x1598383435}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器超时时间，超时时间为]{style="font-family:宋体"}*[time-interval]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Deleted timer *timer-id*]{lang="EN-US"}]{#struct_0_13902_55743_1120077337}

[[ID]{lang="EN-US"}]{#struct_0_13902_55743_x1821262010}[为]{style="font-family:宋体"}*[timer-id]{lang="EN-US"}*[的定时器被删除]{style="font-family:宋体"}

[[Interface *interface-name*: Received event up.]{lang="EN-US"}]{#struct_0_13902_55743_x1629443415}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ up]{lang="EN-US"}]{#struct_0_13902_55743_386979220}

[[Interface *interface-name*: Received event down.]{lang="EN-US"}]{#struct_0_13902_55743_x1438763869}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ down]{lang="EN-US"}]{#struct_0_13902_55743_1674558694}

[[Interface *interface-name*: Received event deactivated.]{lang="EN-US"}]{#struct_0_13902_55743_x1179104721}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_13902_55743_1072277390}[去激活]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13902_55743_1984834734}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_x706721577}[打开]{style="font-family:宋体"}[cellular]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging cellular event]{lang="EN-US"}]{#struct_0_13902_55743_2115275185}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_x884648389}[重启]{style="font-family:宋体"}[cellular]{lang="EN-US"}[控制器上的]{style="font-family:宋体"}[3G modem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13902_55743_337748060}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] modem reboot]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\]]{lang="EN-US"}

[\*Jun 19 16:56:02:074 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device is rebooted]{lang="EN-US"}

[*[// 3G Modem]{lang="EN-US"}*]{#struct_0_13902_55743_x21091063}*[被重启]{style="font-family:宋体"}*

[[%Jun 19 16:56:02:075 2012 Sysname CELLULAR/4/DEV_REMOVED: -MDC=1; Controller Cellular2/4/0: 3G Modem device is removed.]{lang="EN-US"}]{#struct_0_13902_55743_x532229375}

[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Sent IOCTL command 4302 to device]{lang="EN-US"}

[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device removing completed]{lang="EN-US"}

[*[// 3G Modem]{lang="EN-US"}*]{#struct_0_13902_55743_601690664}*[被移除]{style="font-family:宋体"}*

[[%Jun 19 16:56:02:075 2012 Sysname CELLULAR/4/DEV_INSERTED: -MDC=1; Controller Cellular2/4/0: 3G Modem device is inserted.]{lang="EN-US"}]{#struct_0_13902_55743_x426454655}

[*[// 3G Modem]{lang="EN-US"}*]{#struct_0_13902_55743_x1482084625}*[被插入]{style="font-family:宋体"}*

[[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Sent IOCTL command 80044300 to device]{lang="EN-US"}]{#struct_0_13902_55743_2115340721}

[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device major No. is 1]{lang="EN-US"}

[*[// 3G Modem]{lang="EN-US"}*]{#struct_0_13902_55743_668071939}*[主设备号为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Initializing device]{lang="EN-US"}]{#struct_0_13902_55743_1613572257}

[*[// ]{lang="EN-US"}*]{#struct_0_13902_55743_x152167610}*[初始化]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}*

[[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Added timer 0, interval is 30 seconds]{lang="EN-US"}]{#struct_0_13902_55743_x2057125430}

[\*Jun 19 16:56:02:075 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Added timer 1, interval is 3 seconds]{lang="EN-US"}

[\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Timer timed out]{lang="EN-US"}

[\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Controller Cellular2/4/0: Device initialization completed]{lang="EN-US"}

[\*Jun 19 16:56:05:484 2012 Sysname CELLULAR/7/EVENT: -MDC=1; Deleted timer 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13902_55743_x1405418665}*[初始化]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[完成]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_743144044}[以太网通道接口拨号成功。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13902_55743_215546541}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] interface eth-channel 0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer circular enable]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer number 1 autodial]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer timer autodial 10]{lang="EN-US"}

[\*Aug 20 20:34:36:543 2013 Sysname LTE/7/EVENT: -MDC=1; Interface Echannel2/4/0:0: Received event up.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13902_55743_x822939897}*[以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[接口]{style="font-family:宋体"}[up]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_x1599262300}[打开]{style="font-family:宋体"}[cellular]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging cellular error]{lang="EN-US"}]{#struct_0_13902_55743_x2065263332}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_x656667590}[在]{style="font-family:宋体"}[SIM]{lang="EN-US"}[卡被锁的]{style="font-family:宋体"}[3G Modem]{lang="EN-US"}[上启用]{style="font-family:宋体"}[PIN]{lang="EN-US"}[码认证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13902_55743_2115406257}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] pin verification enable 666666]{lang="EN-US"}

[SIM card has been locked. Please verify PIN first.]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\]]{lang="EN-US"}

[\*Jun 19 17:16:34:574 2012 Sysname CELLULAR/7/ERROR: -MDC=1; Controller Cellular2/4/0: Failed to complete command \"pin verification enable\", error code is 23670002]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13902_55743_x881335717}*[下发命令行]{style="font-family:宋体"}[pin verification enable]{lang="EN-US"}[失败，错误码为]{style="font-family:宋体"}[23670002]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13902_55743_1493441337}[以太网通道接口添加新]{style="font-family:宋体"}[DNS]{lang="EN-US"}[地址失败。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13902_55743_x1362107505}

[\[Sysname\] controller cellular 2/4/0]{lang="EN-US"}

[\[Sysname-Cellular2/4/0\] interface eth-channel 0]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer circular enable]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer number 1 autodial]{lang="EN-US"}

[\[Sysname-Eth-channel2/4/0:0\] dialer timer autodial 10]{lang="EN-US"}

[\*Aug 20 20:34:36:543 2013 Sysname LTE/7/ERROR: -MDC=1; Interface Echannel2/4/0:0: Failed to add new DNS address.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_13902_55743_1905943458}*[以太网通道接口]{style="font-family:宋体"}[Eth-channel2/4/0:0]{lang="EN-US"}[接口添加新]{style="font-family:宋体"}[DNS]{lang="EN-US"}[地址失败]{style="font-family:宋体"}*

::: {#1516915984 .myid}
[]{#_Toc404785259}[]{#struct_0_13902_55743_1328974737}

**3G/4G Modem管理 \-- 3G/4G Modem管理调试命令 \-- debugging cellular plugin**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13902_55743_x914530228}

[**[debugging cellular plugin]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13902_55743_1204277884}

[**[undo debugging cellular plugin]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_13902_55743_x2091351563}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13902_55743_x1658030055}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13902_55743_x1864222850}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13902_55743_2115471793}

[[network-admin]{lang="EN-US"}]{#struct_0_13902_55743_x2063104890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13902_55743_x1677651243}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13902_55743_293236567}

[**[all]{lang="EN-US"}**]{#struct_0_13902_55743_x113393427}[：表示所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13902_55743_x1549831059}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13902_55743_x510065653}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_13902_55743_x1273876602}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13902_55743_783243032}

[**[debugging cellular plugin]{lang="EN-US"}**]{#struct_0_13902_55743_x333579601}[命令用来打开插件的调试信息开关。]{style="font-family:
宋体"}

[**[undo debugging cellular plugin]{lang="EN-US"}**]{#struct_0_13902_55743_x816966991}[命令用来关闭插件的调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，插件的调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_13902_55743_2116061617}

[[该命令的调试信息由]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}]{#struct_0_13902_55743_x233667574}[产品插件输出，不同的]{style="font-family:宋体"}[3G/4G Modem]{lang="EN-US"}[插件输出信息不同。]{style="font-family:宋体"}

[ ]{lang="EN-US"}
:::
