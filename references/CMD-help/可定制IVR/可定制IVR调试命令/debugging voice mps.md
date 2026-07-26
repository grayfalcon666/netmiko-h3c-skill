::: {#834488985 .myid}
[]{#_Toc404794651}[]{#struct_0_13337_x1854_x1976555846}

**可定制IVR \-- 可定制IVR调试命令 \-- debugging voice mps**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x1239686718}

[**[debugging voice mps ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_13337_x1854_1778862249}

[**[undo debugging voice mps]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_13337_x1854_1435704632}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13337_x1854_1684950305}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13337_x1854_x215583158}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x16812878}

[[network-admin]{lang="EN-US"}]{#struct_0_13337_x1854_635796449}

[[network-operator]{lang="EN-US"}]{#struct_0_13337_x1854_x1660406338}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13337_x1854_x260335211}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13337_x1854_x1155635221}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13337_x1854_31432466}

[**[all]{lang="EN-US"}**]{#struct_0_13337_x1854_721516595}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[（]{style="font-family:宋体"}[Media Play System]{lang="EN-US"}[，媒体播放系统）]{style="font-family:宋体"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13337_x1854_1951549774}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13337_x1854_458052774}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_13337_x1854_1685146913}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_13337_x1854_203645063}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_13337_x1854_x1878062815}[：表示]{style="font-family:宋体"}[MPS]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13337_x1854_880629247}

[**[debugging voice ]{lang="EN-US"}[mps]{lang="EN-US"}**]{#struct_0_13337_x1854_377836670}[命令用来打开]{style="font-family:宋体"}[MPS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice ]{lang="EN-US"}[mps]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MPS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MPS]{lang="EN-US"}]{#struct_0_13337_x1854_1043916741}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging voice mps error]{lang="EN-US"}]{#struct_0_13337_x1854_x1210022127}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1859267189}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x796064927}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1996556370}

[[Failed to start media play, media-id number is zero.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1318814694}

[[媒体放音失败，媒体文件个数为零]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1685081377}

[[Failed to create MPSCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x646058989}

[[创建放音控制块失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_436712761}

[[Failed to initialize MPSCB.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_610234020}

[[初始化放音控制块失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x116914750}

[[Failed to create *timre-type* timer.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1432967829}

[[创建定时器失败，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1126546352}*[Message-type]{lang="EN-US" style="font-size:9.0pt"}*[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_START_PLAYMEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_1315195396}[：表示媒体放音定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_PSTN_WAITDELAY]{lang="EN-US"}]{#struct_0_13337_x1854_1685277985}[：表示]{style="font-family:宋体"}[PSTN]{lang="EN-US"}[侧延时等待定时器]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_WAIT_RELEASEMSG]{lang="EN-US"}]{#struct_0_13337_x1854_x1360407172}[：表示等待释放消息定时器]{style="font-family:宋体"}

[[Failed to get MPSCB, MPSID is invalid.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1635773744}

[[无效的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_940992578}[MPSID]{lang="EN-US" style="font-size:9.0pt"}[值，不能得到]{style="font-size:9.0pt;font-family:宋体"}[MPS]{lang="EN-US" style="font-size:9.0pt"}[放音控制块]{style="font-size:9.0pt;font-family:
  宋体"}

[[Failed to get PlayCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x614430246}

[[获取播放控制块失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_486199968}

[[Cannot update MPSCB, it\'s playing now, PlayID = *media-id*,  UsrCallID = *caller-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685212449}

[[正在播放文件，不能更新放音控制块，媒体文件]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1794404735}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*[，用户]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[caller-id]{lang="EN-US" style="font-size:9.0pt"}*

[[Failed to read config, invalid DBM data type.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1849521540}

[[无效的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1192015818}[DBM]{lang="EN-US" style="font-size:9.0pt"}[数据类型，导致读取配置失败]{style="font-size:9.0pt;font-family:宋体"}

[[Fail to write DBM.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1431221885}

[[向]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1006805178}[DBM]{lang="EN-US" style="font-size:9.0pt"}[写数据失败]{style="font-size:9.0pt;font-family:宋体"}

[[CodecType is invalid.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685409057}

[[编码类型无效]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_977618605}

[[Failed to get media resource by media ID, CodecType = *codetype*, MediaID = *media-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x715518316}

[[根据媒体名称获取对应媒体资源失败，媒体编码类型为：]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x166234284}*[codetype]{lang="EN-US" style="font-size:9.0pt"}*[，媒体]{style="font-size:9.0pt;
  font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为：]{style="font-size:9.0pt;font-family:宋体"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*

[[Failed to Get default work directory.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1907290886}

[[获取当前默认工作路径失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1418320860}

[[Default working dir = *path*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685343521}

[[当前默认工作路径为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1394146569}*[path]{lang="EN-US" style="font-size:
  9.0pt"}*

[[Failed to create cache.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1989586798}

[[创建缓冲区失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1356505074}

[[Failed to read voice data.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1684884768}

[[读取语音数据失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1451341605}

[[Pointer of resource control block in read control block is null.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1704807852}

[[读取控制块中的媒体资源控制块为空]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x665011058}

[[Failed to delete cache node from cache-array.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x2068671241}

[[从缓冲区数组中删除缓冲区节点失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1684819232}

[[Failed to malloc for resource control block.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x190691793}

[[为资源控制块申请内存失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1542107603}

[[Failed to send *ack-type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1815477423}

[[发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1767536958}[ACK]{lang="EN-US" style="font-size:9.0pt"}[消息失败]{style="font-size:9.0pt;font-family:宋体"}

[*[ack-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_1685015840}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MSG_TYPE_MEDIA_PLAY_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_2128264828}[：表示回复放音请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MSG_TYPE_MEDIA_PAUSE_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_x437234513}[：表示回复暂停请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MSG_TYPE_MEDIA_UPDATE_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_637669252}[：表示回复更新请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MSG_TYPE_MEDIA_RESUM_AC]{lang="EN-US"}]{#struct_0_13337_x1854_1684950304}[K]{lang="EN-US"}[：表示回复恢复放音请求]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MSG_TYPE_MEDIA_NOTIFY_CHANGEFILE]{lang="EN-US"}]{#struct_0_13337_x1854_x215648694}[：表示切换文件]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MSG_TYPE_MEDIA_NOTIFY_OVER]{lang="EN-US"}]{#struct_0_13337_x1854_x865306690}[：表示文件播放结束]{style="font-family:宋体"}

[[Failed to handle media-request.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_763026574}

[[处理媒体放音操作失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1685146912}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging voice mps event]{lang="EN-US"}]{#struct_0_13337_x1854_203710599}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1828802282}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_491569465}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_1559675729}

[[IVR\--\>MPS :*message-type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1590436411}

[[         MPSID :*mps-id*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1845142042}

[[         Protocol : *protocol*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x2082696482}

[[         SPLID : *spl-id*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_x95542454}

[[         MSCID : *msc-id*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685081376}

[[         MediaID : *media-id*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x645993453}

[[         PlayTimes : *times*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_2094701842}

[[         PloadSize : *size*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x410069130}

[[         PlayType: *type*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_443351543}

[[         IfIndex : *ifindex*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1246673205}

[[         Codec : *codetype*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685277984}

[[IVR]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1360472708}[向]{style="font-size:9.0pt;font-family:宋体"}[MPS]{lang="EN-US" style="font-size:9.0pt"}[发送消息成功]{style="font-size:9.0pt;
  font-family:宋体"}

[*[Message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_1500765503}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PLAY_MEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_1305963151}[：开始放音消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PAUSE_MEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_x346575315}[：暂停放音消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RESUM_MEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_x1831816353}[：恢复放音消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[UPDATA_MEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_923306327}[：更新媒体消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NOTIFY_MEDIA_CHANGEFILE]{lang="EN-US"}]{#struct_0_13337_x1854_1685212448}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[媒体放音结束消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NOTIFY_MEDIA_OVER]{lang="EN-US"}]{#struct_0_13337_x1854_x1794470271}[：媒体放音结束消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UNKNOWN_MSG]{lang="EN-US"}]{#struct_0_13337_x1854_x1099359746}[：未知消息]{lang="EN-US" style="font-family:宋体"}

[*[SPLID]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_1091557072}[为业务模块]{style="font-size:9.0pt;font-family:宋体"}[ID ]{lang="EN-US" style="font-size:9.0pt"}

[*[MSCID]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_x1774859104}[为]{style="font-size:9.0pt;font-family:宋体"}[Media Stream Control]{lang="EN-US" style="font-size:9.0pt"}[模块]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}

[*[PlayTimes]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_x831011417}[为每秒发送的编码字节数]{style="font-size:9.0pt;font-family:宋体"}

[[PlayType]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685409056}[为放音的接入方式，]{style="font-size:9.0pt;font-family:宋体"}*[PloadSize]{lang="EN-US" style="font-size:9.0pt"}*[为，]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[取值为：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[PSTN ]{lang="EN-US"}]{#struct_0_13337_x1854_977684141}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VoIP]{lang="EN-US"}]{#struct_0_13337_x1854_x1899110660}

[[Codec]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1608515883}[为音频编码类型。]{style="font-size:9.0pt;font-family:宋体"}*[codetype]{lang="EN-US" style="font-size:9.0pt"}*[取值为：]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[g729r8]{lang="EN-US"}]{#struct_0_13337_x1854_131225549}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[g711alaw]{lang="EN-US"}]{#struct_0_13337_x1854_x490839249}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[g711ulaw]{lang="EN-US"}]{#struct_0_13337_x1854_1685343520}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[g723r53]{lang="EN-US"}]{#struct_0_13337_x1854_x1394081033}

[[MPS\--\>IVR :*message-type*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_954011053}

[[         MPSID :*mps-id*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_x36675137}

[[         Protocol : *protocol*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1684884771}

[[         SPLID : *spl-id*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1450882852}

[[         MSCID : *msc-id*             ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1106689936}

[[MPS]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_310455213}[向]{style="font-size:9.0pt;font-family:宋体"}[IVR]{lang="EN-US" style="font-size:9.0pt"}[发送消息成功]{style="font-size:9.0pt;font-family:
  宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_942224026}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PLAY_MEDIA_ACK ]{lang="EN-US"}]{#struct_0_13337_x1854_x457616980}[：开始放音消息确认]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[PAUSE_MEDIA_ACK ]{lang="EN-US"}]{#struct_0_13337_x1854_1684819235}[：暂停放音消息确认]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RESUM_MEDIA_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_x190757329}[：恢复放音消息确认]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UPDATA_MEDIA_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_x816342299}[：更新媒体消息确认]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NOTIFY_MEDIA_CHANGEFILE]{lang="EN-US"}]{#struct_0_13337_x1854_1269688591}[：]{lang="EN-US" style="font-family:宋体"}[媒体放音结束消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NOTIFY_MEDIA_OVER]{lang="EN-US"}]{#struct_0_13337_x1854_1685015843}[：媒体放音结束消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UNKNOWN_MSG]{lang="EN-US"}]{#struct_0_13337_x1854_2128199292}[：未知消息]{lang="EN-US" style="font-family:宋体"}

[[Start to play media, MediaID = *media-id*, UsrCallID = *user-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1251852168}

[[开始放音]{style="font-family:宋体"}]{#struct_0_13337_x1854_1266799881} [媒体文件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[media-id]{lang="EN-US"}*[，用户编号为]{style="font-family:宋体"}*[user-id]{lang="EN-US"}*

[[Delete MPSCB, MPSID = *mps-id*, UsrCallID = *user-id*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1684950307}

[[删除放音控制块，]{style="font-family:宋体"}]{#struct_0_13337_x1854_x215714230}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*[，用户名为]{style="font-family:宋体"}*[user-id]{lang="EN-US"}*

[[Resume playing media, MPSID = *mps-id*, MediaID = *media-id*, UsrCallID = *user-id*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_346268975}

[[正在恢复放音，放音控制块]{style="font-family:宋体"}]{#struct_0_13337_x1854_x1396565166}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*[，媒体文件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[media-id]{lang="EN-US"}*[，用户编号为]{style="font-family:宋体"}*[user-id]{lang="EN-US"}*

[[Pause to play media, MPSID = ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685146915}*[mps-id]{lang="EN-US" style="font-size:9.0pt"}*[, MediaID = ]{lang="EN-US" style="font-size:
  9.0pt"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*[, UsrCallID = ]{lang="EN-US" style="font-size:9.0pt"}*[user-id]{lang="EN-US" style="font-size:9.0pt"}*[.]{lang="EN-US" style="font-size:
  9.0pt"}

[[暂停放音，控制块]{style="font-family:宋体"}]{#struct_0_13337_x1854_203776135}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*[，]{style="font-family:宋体"} [媒体文件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[media-id]{lang="EN-US"}*[，用户编号为]{style="font-family:宋体"}*[user-id]{lang="EN-US"}*

[[Update media resource, MPSID = ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_892507107}*[mps-id]{lang="EN-US" style="font-size:9.0pt"}*[, MediaID = ]{lang="EN-US" style="font-size:9.0pt"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*[, UsrCallID = ]{lang="EN-US" style="font-size:
  9.0pt"}*[user-id]{lang="EN-US" style="font-size:9.0pt"}*[.]{lang="EN-US" style="font-size:9.0pt"}

[[更新媒体文件，控制块]{style="font-family:宋体"}]{#struct_0_13337_x1854_x791952889}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*[，媒体文件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[media-id ]{lang="EN-US"}*[，用户编号为]{style="font-family:宋体"}*[user-id]{lang="EN-US"}*

[[End playing media, MPSID = ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685081379}*[mps-id]{lang="EN-US" style="font-size:9.0pt"}*[, MediaID = ]{lang="EN-US" style="font-size:
  9.0pt"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*[, UsrCallID = ]{lang="EN-US" style="font-size:9.0pt"}*[user-id]{lang="EN-US" style="font-size:9.0pt"}*[.]{lang="EN-US" style="font-size:
  9.0pt"}

[[停止放音，控制块]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x646452205}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:宋体"}*[mps-id]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-size:9.0pt;
  font-family:宋体"}*[ ]{style="font-size:9.0pt"}*[媒体文件]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[media-id]{lang="EN-US" style="font-size:9.0pt"}*[，用户编号为]{style="font-size:9.0pt;font-family:宋体"}*[user-id]{lang="EN-US" style="font-size:9.0pt"}*

[[Create resource control block, CodecType = *codetype*, FileName = *file-name*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1508497385}

[[创建文件资源控制块成功，文件编码类型为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1058673107}*[codetype]{lang="EN-US" style="font-size:9.0pt"}*[，文件名为]{style="font-size:9.0pt;
  font-family:宋体"}*[file-name]{lang="EN-US" style="font-size:9.0pt"}*

[[Free resource control block, CodecType = *codetype*, FileName = *file-name*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_1685277987}

[[释放文件资源控制块成功，文件编码类型为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1360276100}*[codetype]{lang="EN-US" style="font-size:9.0pt"}*[，文件名为]{style="font-size:9.0pt;
  font-family:宋体"}*[file-name]{lang="EN-US" style="font-size:9.0pt"}*

[[Create read-control-block, CodecType = *codetype*, FileName = *file-name*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_13337_x1854_621951081}

[[创建文件读取控制块成功，文件编码类型为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_1685212451}*[codetype]{lang="EN-US" style="font-size:9.0pt"}*[，文件名为]{style="font-size:9.0pt;
  font-family:宋体"}*[file-name]{lang="EN-US" style="font-size:9.0pt"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging voice mps info]{lang="EN-US"}]{#struct_0_13337_x1854_x1794929022}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1836969363}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1486489072}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_261988207}

[[Create MPSID successfully, MPSID = *mps-id*.]{lang="EN-US"}]{#struct_0_13337_x1854_1332481534}

[[创建放音控制块成功，放音控制块]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13337_x1854_x780492803}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*

[[Init MPSCB successfully, MPSCB ID = *mps-id*.]{lang="EN-US"}]{#struct_0_13337_x1854_x1310630989}

[[初始化放音控制块成功，放音控制块]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13337_x1854_1685409059}[为]{style="font-family:宋体"}*[mps-id]{lang="EN-US"}*

[[Release  playing media successfully.]{lang="EN-US"}]{#struct_0_13337_x1854_978273965}

[[成功释放放音请求]{style="font-family:宋体"}]{#struct_0_13337_x1854_x675715850}

[[Finish reading the data of media-file.]{lang="EN-US"}]{#struct_0_13337_x1854_x1131782027}

[[读取文件数据结束]{style="font-family:宋体"}]{#struct_0_13337_x1854_x1582522500}

[[Receive data from MSC.]{lang="EN-US"}]{#struct_0_13337_x1854_2078847997}

[[接收到]{style="font-family:宋体"}[MSC]{lang="EN-US"}]{#struct_0_13337_x1854_1636396686}[模块发送的数据]{style="font-family:宋体"}

[[Change media file. MediaId = *media-id.*]{lang="EN-US"}]{#struct_0_13337_x1854_1685343523}

[[切换媒体文件，媒体文件]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13337_x1854_x1394015497}[为]{style="font-family:宋体"}*[media-id.]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging voice mps timer]{lang="EN-US"}]{#struct_0_13337_x1854_x184310672}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1833100763}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1584315248}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_283459209}

[[ Create timer, TIMERID: *timer-id*, TIMERType: *timer-type*, TIMERLEN: *timer-length.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1602358806}

[[启动定时器成功]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1579728652}

[[定时器标识为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x2113727788}*[timerid]{lang="EN-US" style="font-size:9.0pt"}*

[*[timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_1684884770}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_START_PLAYMEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_x1450817316}[：开始放音定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_PSTN_WAITDELAY]{lang="EN-US"}]{#struct_0_13337_x1854_380192680}[：]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[STN]{lang="EN-US"}[侧等待]{lang="EN-US" style="font-family:宋体"}[线路连接]{style="font-family:宋体"}[延时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_WAIT_RELEASEMSG]{lang="EN-US"}]{#struct_0_13337_x1854_366281591}[：播放结束等待]{lang="EN-US" style="font-family:宋体"}[release]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}*[timer-length]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_MEDIAPLAY_LEN]{lang="EN-US"}]{#struct_0_13337_x1854_14979305}[：正在放音状态定时器时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_WAITRELEASE_LEN]{lang="EN-US"}]{#struct_0_13337_x1854_1385580777}[：等待]{lang="EN-US" style="font-family:宋体"}[release]{lang="EN-US"}[消息定时器时长]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_PSTN_INIT_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_1767339722}[：]{lang="EN-US" style="font-family:宋体"}[WAITDELAY]{lang="EN-US"}[状态超时时间间隔]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:
  宋体"}[非]{lang="EN-US" style="font-family:宋体"}[R2]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_PSTN_R2WAITDEL_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_1684819234}[：]{lang="EN-US" style="font-family:宋体"}[WAITDELAY]{lang="EN-US"}[状态超时时间间隔]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:
  宋体"}[R2]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:
  宋体"}[）]{style="font-family:宋体"}

[[Delete timer, TIMERID: *timer-id*, TIMERType: *timer-type*, TIMERLEN: *timer-length.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x190822865}

[[成功删除定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_414924145}

[[定时器标识为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1477008459}*[timerid]{lang="EN-US" style="font-size:9.0pt"}*

[*[timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_13337_x1854_x1255931780}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_START_PLAYMEDIA]{lang="EN-US"}]{#struct_0_13337_x1854_459300985}[：开始放音定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_PSTN_WAITDELAY]{lang="EN-US"}]{#struct_0_13337_x1854_x748344783}[：]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[STN]{lang="EN-US"}[侧等待延时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS\_]{lang="EN-US"}]{#struct_0_13337_x1854_1685015842}[TIMER]{lang="EN-US"}[\_WAIT_RELEASEMSG]{lang="EN-US"}[：播放结束等待]{lang="EN-US" style="font-family:宋体"}[release]{lang="EN-US"}[消息]{lang="EN-US" style="font-family:宋体"}*[timer-length]{lang="EN-US"}*[取值为：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_MEDIAPLAY_LEN]{lang="EN-US"}]{#struct_0_13337_x1854_2128133756}[：正在放音状态定时器时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MPS_TIMER_WAITRELEASE_LEN]{lang="EN-US"}]{#struct_0_13337_x1854_1150321866}[：等待]{lang="EN-US" style="font-family:宋体"}[release]{lang="EN-US"}[消息定时器时长]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_PSTN_INIT_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_25014423}[：]{lang="EN-US" style="font-family:宋体"}[WAITDELAY]{lang="EN-US"}[状态超时时间间隔]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:
  宋体"}[非]{lang="EN-US" style="font-family:宋体"}[R2]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[MPS_TIMER_PSTN_R2WAITDEL_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_997206682}[：]{lang="EN-US" style="font-family:宋体"}[WAITDELAY]{lang="EN-US"}[状态超时时间间隔（]{lang="EN-US" style="font-family:宋体"}[R2]{lang="EN-US"}[协议）]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x1872097741}

[[\# ]{lang="EN-US"}]{#struct_0_13337_x1854_1684950306}[使用]{style="font-family:宋体"}[SIP]{lang="EN-US"}[协议进行呼叫，主叫号码为]{style="font-family:宋体"}[987]{lang="EN-US"}[，]{style="font-family:宋体"}[IVR]{lang="EN-US"}[接入号为]{style="font-family:宋体"}[177]{lang="EN-US"}[，根节点为]{style="font-family:宋体"}[service]{lang="EN-US"}[节点，配置放音操作。打开被叫侧]{style="font-family:宋体"}[MPS debug]{lang="EN-US"}[开关，输出调试信息如下：]{style="font-family:宋体"}

[[\<Sysname\> debugging voice mps all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x215779766}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_x1634925829}*[收到]{style="font-family:宋体"}[IVR]{lang="EN-US"}[侧发送的播放媒体文件请求消息]{style="font-family:宋体"}*

[[\<Sysname\>\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1709784768}

[[MPS_Event: IVR\--\>MPS : PLAY_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x470271824}

[[         MPSID : 4294967295]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x334656192}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1837234598}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1427587816}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x749420893}

[[         MediaID : 10001]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1962283350}

[[         PlayTimes : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1496035810}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685146914}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_203841671}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1905467369}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1303543499}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1552568562}

[[MPS_Event: IVR\--\>MPS : PLAY_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_342225378}

[[      ]{lang="EN-US" style="font-family:\"Courier New\""}]{#struct_0_13337_x1854_715229429}[  MPSID : 4294967295]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[       ]{lang="EN-US" style="font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1714013980}[ Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_478736924}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_637350414}

[[         MediaID : 10001]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_594602277}

[[         PlayTimes : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685081378}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x646386669}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1194415460}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x301419016}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1330574636}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_882563735}

[[MPS_Event: Start to play media, MediaID = 10001 UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_598005905}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:616 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_364459564}

[[MPS_Info: Create MpsCb successfully, MpsCb id = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x235414037}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:617 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x674426840}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1982250532}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1685277986}*[创建资源控制块]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:617 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1360341636}

[[MPS_Event: Create resource control block, CodecType = 0, FileName = cfa0:/g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1708335223}

[[/i_g729r8.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_584542993}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x79147830}*[创建读取控制块]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1127907660}

[[MPS_Event: Create read-control-block, CodecType = 0, PayloadSize = 30, MediaName]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_968867360}

[[ = cfa0:/g729r8/i_g729r8.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x881909700}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1355082478}

[[MPS_Timer: Create timer, TmrId: 0, TmrType: MPS_TIMER_PSTN_WAITDELAY, TmrLen: 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1237371188}

[[0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1141350555}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685212450}

[[MPS_Info: Init MpsCb successfully, MpsCb id = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1794994558}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1613059864}*[创建放音定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:618 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1781937511}

[[MPS_Timer: Create timer, TmrId: 1, TmrType: MPS_TIMER_START_PLAYMEDIA, TmrLen: 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1362570214}

[[0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x919706050}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:921 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_97434611}

[[MPS_Timer: Delete timer after PSTN wait delay, TmrId: 0, TmrType: MPS_TIMER_PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x90265192}

[[\_WAITDELAY, TmrLen: 300.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x756455875}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:921 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1942901880}

[[MPS_Event: Wait delay process successfully, Play state = 1, Pstn state = 2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1593563860}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:23:941 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685409058}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_978339501}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x1100882782}*[开始发送语音数据包，每]{style="font-family:宋体"}[500]{lang="EN-US"}[个包输出一次信息]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\*Dec 24 19:41:23:942 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1953955049}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1, MediaID = 1000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_766696679}

[[1, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1671624391}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:38:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_640878393}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 500, MediaID = 10]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1689161924}

[[001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1403841519}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:41:53:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1383831420}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1000, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1895951111}

[[0001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685343522}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:42:08:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1393949961}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1500, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_411044411}

[[0001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_906216211}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:42:23:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1934271764}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 2000, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1830499498}

[[0001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2142550821}

[ ]{lang="EN-US" style="font-family:\"Courier New\""}

[[\*Dec 24 19:42:38:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x52596582}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 2500, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1119706131}

[[0001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1506665425}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:42:53:911 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684884773}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 3000, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1450751780}

[[0001, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_592461442}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:42:56:101 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1566486220}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x245812371}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1240606873}*[文件数据读取结束]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1975547925}

[[MPS_Info: Finish reading the data of media-file.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_171082936}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x303287201}*[释放读取控制块]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:
8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x649048431}

[[MPS_Event: Free reading control block, CodecType = 0, MediaName = cfa0:/g729r8/i]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_247248196}

[[\_g729r8.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684819237}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x190888401}*[释放资源控制块]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1964802513}

[[MPS_Event: Free resource control block, CodecType = 0, MediaName = cfa0:/g729r8/]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x600097799}

[[i_g729r8.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x203010489}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1125773430}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_632721747}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1203151233}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1595565979}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_1937550869}*[向]{style="font-family:宋体"}[IVR]{lang="EN-US"}[发送播放当前文件成功播放结束的]{style="font-family:宋体"}[MPCP]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685015845}

[[MPS_Event: Media file has been played completely.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2128068220}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_333433913}*[发送播放结束消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_615595124}

[[MPS_Event: MPS\--\>IVR : NOTIFY_MEDIA_OVER]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1056861284}

[[         MPSID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_809366992}

[[         SPLID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1690261635}

[[         ProcResult: Success]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x978197422}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:022 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1612925185}

[[MPS_Timer: Create timer, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 10000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1757519402}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_1893486597}*[接收]{style="font-family:宋体"}[IVR]{lang="EN-US"}[发送的更新媒体文件的]{style="font-family:宋体"}[MPCP]{lang="EN-US"}[消息，]{style="font-family:宋体"}[MPS]{lang="EN-US"}[接受到消息后开始更新文件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_171196774}

[[MPS_Event: IVR\--\>MPS : UPDATE_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684950309}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x216369590}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2145452674}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x31371614}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_276610034}

[[         MediaID : 10002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1490765541}

[[         PlayTimes : 2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x92752351}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1841061643}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1789872011}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x942269855}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_995109402}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043763153}

[[MPS_Event: IVR\--\>MPS : UPDATE_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685146917}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_203907207}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x484511273}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_308590953}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x171098737}

[[         MediaID : 10002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1680170180}

[[         PlayTimes : 2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x364808374}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_390954221}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1139683992}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_59017595}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685081381}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x645927932}

[[MPS_Event: Update media resource, MpsId = 1, MediaID = 10002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x547108180}

[ ]{lang="EN-US" style="font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:023 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2000439910}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x689390485}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:024 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1311095648}

[[MPS_Event: Create resource control block, CodecType = 0, FileName = cfa0:/g729_o]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1250914080}

[[p2.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2018464134}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:024 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1778988137}

[[MPS_Event: Create read-control-block, CodecType = 0, PayloadSize = 30, MediaName]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1529326277}

[[ = cfa0:/g729_op2.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685277989}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_x1360669316}*[接收]{style="font-family:宋体"}[IVR]{lang="EN-US"}[发送的恢复放音的]{style="font-family:宋体"}[MPCP]{lang="EN-US"}[消息，]{style="font-family:宋体"}[MPS]{lang="EN-US"}[放音标志置位，开始准备放音]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_169500164}

[[MPS_Event: IVR\--\>MPS : RESUM_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1675893739}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1434952108}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1906610267}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_55482762}

[[         ResumeType : reset]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_298416117}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x693575900}

[[         MediaID : 10002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x324041770}

[[         PlayTimes : 2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_518812940}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685212453}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1795060094}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1917612129}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_696442316}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1371640730}

[[MPS_Event: IVR\--\>MPS : RESUM_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1925657794}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1147125514}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1866458599}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1643205001}

[[         ResumeType : reset]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1166780999}

[[         MSCID : 0x20100000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685409061}

[[         MediaID : 10002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_977749678}

[[         PlayTimes : 2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_875630020}

[[         PloadSize : 30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_738410234}

[[         PlayType : PSTN]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1312787309}

[[         IfIndex : 8/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1402325162}

[[         Codec : g729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1764136174}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:027 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_562734137}

[[MPS_Event: Resume playing media, MpsId = 1, MediaID = 10002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_344758162}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:051 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1753198678}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1356646862}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:07:051 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685343525}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1, MediaID = 1000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1393884425}

[[2, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1793853818}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:17:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1456575280}

[[MPS_Timer: Delete timer, TmrId: 0, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_334901171}

[[.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_725397486}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:22:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1537620486}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 500, MediaID = 10]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_808326368}

[[002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_697900202}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:37:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x746389318}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1000, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684884772}

[[0002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1450686244}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:43:52:021 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1859058716}

[[MPS_Event: Send voice packet by media-channel 9, PacketCount = 1500, MediaID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_508086760}

[[0002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_442352343}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_292453586}

[[MPS_Info: Finish reading the data of media-file.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1127298637}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1007441893}

[[MPS_Event: Free reading control block, CodecType = 0, MediaName = cfa0:/g729_op2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1641296709}

[[.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1608550517}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2008556357}

[[MPS_Event: Free resource control block, CodecType = 0, MediaName = cfa0:/g729_op]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684819236}

[[2.wav.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x190953937}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_5359800}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1742662456}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:961 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1427266078}

[[MPS_Info: No elements in array.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x112512744}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:962 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1603922252}

[[MPS_Event: Media file has been played completely.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1462814321}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_1061546517}*[向]{style="font-family:宋体"}[IVR]{lang="EN-US"}[发送]{style="font-family:宋体"}[MPCP]{lang="EN-US"}[消息，表示结束播放当前文件]{style="font-family:宋体"}*

[[\*Dec 24 19:44:06:962 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x232452404}

[[MPS_Event: MPS\--\>IVR : NOTIFY_MEDIA_OVER]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_988400585}

[[        ]{lang="EN-US" style="font-family:\"Courier New\""}]{#struct_0_13337_x1854_1685015844}[ MPSID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[         SPLID = 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2128002684}

[[         ProcResult: Success]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_379916429}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:965 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1037950338}

[[MPS_Info: Receive data from Msc.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1732462728}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:965 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1089667634}

[[MPS_Timer: Delete timer, TmrId: 1, TmrType: MPS_TIMER_START_PLAYMEDIA, TmrLen: 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_973659260}

[[0.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1331618859}

[*[// MPS]{lang="EN-US"}*]{#struct_0_13337_x1854_1008010331}*[接收]{style="font-family:宋体"}[IVR]{lang="EN-US"}[发送的释放放音消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1684950308}

[[MPS_Event: IVR\--\>MPS : RELEASE_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x216435126}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x938332048}

[[         Protocol : SPL_DISCRIM_LGS]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x962016404}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1887034370}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x596751901}

[[MPS_Event: IVR\--\>MPS : RELEASE_MEDIA]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1703457196}

[[         MPSID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1408074047}

[[         Protocol : 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1396378022}

[[         SPLID : 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1440853547}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1751043639}

[[MPS_Event: End playing media, MpsId = 1, MediaID = 10002, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_352765762}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1685146916}*[删除放音定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_203972743}

[[MPS_Timer: Delete timer, TmrId: 0, TmrType: MPS_TIMER_WAIT_RELEASEMSG, TmrLen: 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2002212181}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1100235078}*[删除放音控制块]{style="font-family:宋体"}*

[[.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1731380}

[[\*Dec 24 19:44:06:966 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x397343391}

[[MPS_Event: Delete MpsCb, MpsId = 1, UsrCallID = 1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2056402948}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x1204438961}*[释放放音请求成功，停止放音]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 19:44:06:967 2013 Sysname MPS/7/MPS_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_814571676}

[[MPS_Info: Release playing media successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x390684236}

::: {#-731988176 .myid}
[]{#_Toc404794652}[]{#struct_0_13337_x1854_1685081380}

**可定制IVR \-- 可定制IVR调试命令 \-- debugging voice ivr**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x645862396}

[**[debugging vioce ]{lang="EN-US"}[ivr ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_13337_x1854_970205348}

[**[undo debugging voice ]{lang="EN-US"}[ivr]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_13337_x1854_x128201506}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13337_x1854_371881297}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13337_x1854_x73133569}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x529294527}

[[network-admin]{lang="EN-US"}]{#struct_0_13337_x1854_x293327289}

[[network-operator]{lang="EN-US"}]{#struct_0_13337_x1854_x2017879449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13337_x1854_1480502566}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13337_x1854_2134085011}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13337_x1854_1685277988}

[**[all]{lang="EN-US"}**]{#struct_0_13337_x1854_x1360734852}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_13337_x1854_x853053672}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_13337_x1854_x1770417199}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_13337_x1854_x1205652082}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_13337_x1854_x703683281}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_13337_x1854_1069448464}[：表示]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_13337_x1854_x336810386}

[**[debugging voice ]{lang="EN-US"}[ivr]{lang="EN-US"}**]{#struct_0_13337_x1854_x653728993}[命令用来打开]{style="font-family:宋体"}[IVR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice ]{lang="EN-US"}[ivr]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IVR]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1604753290}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging voice ivr error]{lang="EN-US"}]{#struct_0_13337_x1854_752266996}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1834147341}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_1685212452}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1795125630}

[[Failed to allocate memory for]{lang="EN-US" style="font-size:
  9.0pt;font-family:\"Arial Unicode MS\",\"sans-serif\";color:black"}]{#struct_0_13337_x1854_1300226857}[ *module*.]{lang="EN-US" style="font-size:9.0pt"}

[[为]{style="font-size:9.0pt;
  font-family:宋体;color:black"}]{#struct_0_13337_x1854_x1269166747}*[module]{lang="EN-US" style="font-size:
  9.0pt"}*[分配内存失败]{style="font-size:9.0pt;font-family:宋体;
  color:black"}

[[Protocal is not supported, Protocal = *protocal*.]{lang="EN-US" style="font-size:
  9.0pt;font-family:\"Arial Unicode MS\",\"sans-serif\";color:black"}]{#struct_0_13337_x1854_1074907975}

[[不支持协议类型，该协议类型为]{style="font-size:9.0pt;
  font-family:宋体;color:black"}]{#struct_0_13337_x1854_2016115434}*[protocal.]{lang="EN-US" style="font-size:9.0pt;font-family:\"Arial Unicode MS\",\"sans-serif\";
  color:black"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging voice ivr event]{lang="EN-US"}]{#struct_0_13337_x1854_1920947729}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1839554357}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x2086355428}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_880232616}

[[CMC \--\> IVR : ACCP_CHANNEL_READY_ACK.]{lang="EN-US"}]{#struct_0_13337_x1854_1685409060}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_977815214}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Channel Ready Ack]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP_FAX_VOICE_SWITCH.]{lang="EN-US"}]{#struct_0_13337_x1854_x132498391}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x707295374}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Fax Voice Switch]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP]{lang="FR"}[\_]{lang="EN-US"}]{#struct_0_13337_x1854_x1546373183}[INFORMATION.]{lang="FR"}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x1182247443}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Information]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP]{lang="FR"}[\_]{lang="EN-US"}]{#struct_0_13337_x1854_377311705}[SERVICE.]{lang="FR"}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1685343524}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Service]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP_SERVICE_ACK.]{lang="EN-US"}]{#struct_0_13337_x1854_x1393818889}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1903428749}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Service Ack]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP_RELEASE.]{lang="EN-US"}]{#struct_0_13337_x1854_x803157958}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1023692461}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Release]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CMC \--\> IVR : ACCP_RELEASE_COMPLETE.]{lang="EN-US"}]{#struct_0_13337_x1854_2132221134}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_148018108}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Release Complete]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[IVR \--\> CMC: ACCP_SETUPACK.]{lang="EN-US"}]{#struct_0_13337_x1854_x1043998586}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x748400344}[发送]{style="font-family:宋体"}[Accp Setup Ack]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP\_ ALERT.]{lang="EN-US"}]{#struct_0_13337_x1854_1609371985}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x1152870241}[发送]{style="font-family:宋体"}[Accp Alerting]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_CONNECT.]{lang="EN-US"}]{#struct_0_13337_x1854_x144392581}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1132472255}[发送]{style="font-family:宋体"}[Accp Connect]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_INFORMATION.]{lang="EN-US"}]{#struct_0_13337_x1854_x1044064122}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x1868184238}[发送]{style="font-family:宋体"}[Accp Information]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_RELEASE.]{lang="EN-US"}]{#struct_0_13337_x1854_x1893206180}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1660034267}[发送]{style="font-family:宋体"}[Accp Release]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_RELCOMP.]{lang="EN-US"}]{#struct_0_13337_x1854_125380157}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1091874675}[发送]{style="font-family:宋体"}[Accp Release Complete]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_CHANNEL_READY.]{lang="EN-US"}]{#struct_0_13337_x1854_x1043867514}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_1380768705}[发送]{style="font-family:宋体"}[Accp Channel Ready]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_FAXVOCSWCH_ACK.]{lang="EN-US"}]{#struct_0_13337_x1854_x1798647239}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x477771947}[发送]{style="font-family:宋体"}[Accp Fax Voice Switch Ack]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_SERVICE.]{lang="EN-US"}]{#struct_0_13337_x1854_1972669955}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x1043933050}[发送]{style="font-family:宋体"}[Accp Service]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[IVR \--\> CMC: ACCP_SRVACK.]{lang="EN-US"}]{#struct_0_13337_x1854_x1080902409}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_787729896}[发送]{style="font-family:宋体"}[Accp Service Ack]{lang="EN-US"}[消息到]{style="font-family:宋体"}[CMC]{lang="EN-US"}

[[CMC \--\> IVR : ACCP_SETUP.]{lang="EN-US"}]{#struct_0_13337_x1854_851408493}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x381685478}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Accp Setup]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[IVR \--\> DPL : DPL_ROUTE_REQ.]{lang="EN-US"}]{#struct_0_13337_x1854_x1043736442}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_x307255759}[向]{style="font-family:宋体"}[DPL]{lang="EN-US"}[发送查询实体的请求]{style="font-family:宋体"}

[[IVR \--\> MPS : End playing media.]{lang="EN-US"}]{#struct_0_13337_x1854_x2035075134}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_90681234}[向]{style="font-family:宋体"}[MPS]{lang="EN-US"}[发送结束放音的请求]{style="font-family:宋体"}

[[Send synchronized-request to MPU.]{lang="EN-US"}]{#struct_0_13337_x1854_x1043801978}

[[发送主备倒换响应给主控板]{style="font-family:宋体"}]{#struct_0_13337_x1854_317866771}

[[DPL \--\> IVR : DPL_ROUTE_RSP.]{lang="EN-US"}]{#struct_0_13337_x1854_x1248103475}

[[DPL]{lang="EN-US"}]{#struct_0_13337_x1854_x1245813054}[将查询实体的结果发给]{style="font-family:宋体"}[IVR]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging voice ivr fsm]{lang="EN-US"}]{#struct_0_13337_x1854_242069073}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1845416113}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_13337_x1854_60106656}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1043605370}

[*[statusA]{lang="EN-US"}*[ \--\> *statusB*, CallId = *idA*, LocalId = *idB*.]{lang="EN-US"}]{#struct_0_13337_x1854_x560685515}

[[IVR]{lang="EN-US"}]{#struct_0_13337_x1854_422013069}[呼叫状态变迁：由]{style="font-family:宋体"}*[statusA]{lang="EN-US"}*[状态变迁到]{style="font-family:宋体"}*[statusB]{lang="EN-US"}*[状态，]{style="font-family:宋体"}[CallId]{lang="EN-US"}[为]{style="font-family:宋体"}*[idA]{lang="EN-US"}*[，]{style="font-family:宋体"}[LocalId]{lang="EN-US"}[为]{style="font-family:宋体"}*[idB]{lang="EN-US"}*

[*[state-type ]{lang="EN-US"}*]{#struct_0_13337_x1854_x2114183549}[取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVA_IDLE]{lang="EN-US"}]{#struct_0_13337_x1854_977254092}[：表示正处于空闲状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVA_INCONNECTBCH ]{lang="EN-US"}]{#struct_0_13337_x1854_338842253}[：表示正处于装配]{lang="EN-US" style="font-family:
  宋体"}[B]{lang="EN-US"}[通道的状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVA_TALK]{lang="EN-US"}]{#struct_0_13337_x1854_x833583557}[：表示正处于通话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVA_CMC_RELEASING]{lang="EN-US"}]{#struct_0_13337_x1854_x1099278572}[：表示正处于]{lang="EN-US" style="font-family:
  宋体"}[CMC]{lang="EN-US"}[拆线状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging voice ivr info]{lang="EN-US"}]{#struct_0_13337_x1854_x1043670906}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1844817984}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_1728092302}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x1229382379}

[[Cannot get entity by number, LocalId = *localId*.]{lang="EN-US"}]{#struct_0_13337_x1854_x1050160110}

[[本地呼叫]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_13337_x1854_x1639767489}[达到最大值，]{style="font-family:宋体"}[LocalId]{lang="EN-US"}[为]{style="font-family:宋体"}[localId]{lang="EN-US"}

[[Input error, RepeatTimes = *repeatTimes*, InputErrorTimes = *errorTimes*.]{lang="EN-US"}]{#struct_0_13337_x1854_x1301027499}

[[输入错误，可重试次数为]{style="font-family:宋体"}*[repeatTimes]{lang="EN-US"}*]{#struct_0_13337_x1854_1732613398}[次，输入错误次数为]{style="font-family:宋体"}*[errorTimes]{lang="EN-US"}*[次]{style="font-family:宋体"}

[[Call state is invalid, CallId = id.]{lang="EN-US"}]{#struct_0_13337_x1854_x1043474298}

[[呼叫状态是无效状态，]{style="font-family:宋体"}[CallId]{lang="EN-US"}]{#struct_0_13337_x1854_1639135245}[为]{style="font-family:宋体"}[id]{lang="EN-US"}

[[Timeout, RepeatTimes = *repeat-time*, TimeoutTimes ]{lang="EN-US"}]{#struct_0_13337_x1854_1858850296}[＝]{style="font-family:宋体"}*[error-times]{lang="EN-US"}*[.]{lang="EN-US"}

[[等待输入超时，可重复超时次数为]{style="font-family:宋体"}*[repeat-times]{lang="EN-US"}*[,]{lang="EN-US"}]{#struct_0_13337_x1854_1706501136}[，已经超时次数为]{style="font-family:宋体"}*[error-times]{lang="EN-US"}*

[[Jump configure is invalid, NodeId = id.]{lang="EN-US"}]{#struct_0_13337_x1854_392337378}

[[Jump]{lang="EN-US"}]{#struct_0_13337_x1854_x1853257514}[节点配置无效]{style="font-family:宋体"}

[[Call configure is invalid, NodeId = id.]{lang="EN-US"}]{#struct_0_13337_x1854_x2006330963}

[[Call]{lang="EN-US"}]{#struct_0_13337_x1854_x1043539834}[节点配置无效]{style="font-family:宋体"}

[[Service configure is invalid, NodeId = id.]{lang="EN-US"}]{#struct_0_13337_x1854_1700326035}

[[Service]{lang="EN-US"}]{#struct_0_13337_x1854_x24638145}[节点配置无效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging voice ivr timer]{lang="EN-US"}]{#struct_0_13337_x1854_x1271364211}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1843133072}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_1713669636}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_13337_x1854_x837667554}

[[Failed to create timer *type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x152206073}

[[创建定时器失败，该定时器类型为]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_13337_x1854_x1043998587}*[type]{lang="EN-US" style="font-size:10.0pt"}*

[*[type]{lang="EN-US" style="font-size:10.0pt"}*]{#struct_0_13337_x1854_1980483011}[的类型为：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_INVALID_TYPE]{lang="EN-US"}]{#struct_0_13337_x1854_x417070510}[：呼叫定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_CHYACK]{lang="EN-US"}]{#struct_0_13337_x1854_x1040657992}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[CHANNEL_READY]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_SRVACK]{lang="EN-US"}]{#struct_0_13337_x1854_687407895}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[SERVICE_ACK]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_RELCOM]{lang="EN-US"}]{#struct_0_13337_x1854_1387950759}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[RELEASE_COMPLATE]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_OMIT_INFORMATION]{lang="EN-US"}]{#struct_0_13337_x1854_x240355760}[：]{lang="EN-US" style="font-family:宋体"}[IVR]{lang="EN-US"}[忽略]{lang="EN-US" style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息定时器节点定时器类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_JUMP_WAIT_INPUT]{lang="EN-US"}]{#struct_0_13337_x1854_331395874}[：]{lang="EN-US" style="font-family:宋体"}[J]{lang="EN-US"}[ump]{lang="EN-US"}[节点下等待用户按键]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_FIRST_DIAL]{lang="EN-US"}]{#struct_0_13337_x1854_x1044064123}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下首次按键定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_DIAL_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_x302100297}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下按键间隙定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAIT_MPS_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_x247402280}[：等待]{lang="EN-US" style="font-family:宋体"}[MPS]{lang="EN-US"}[响应]{style="font-family:宋体"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[Start timer, TmrId = *id*, TmrType = *type*, TmrLength = *length*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1210636256}

[[启动定时器，定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x1447373746}[Id]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:宋体"}*[id]{lang="EN-US" style="font-size:9.0pt"}*[，定时器类型为]{style="font-size:9.0pt;font-family:
  宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[，]{style="font-size:9.0pt;font-family:宋体"}[定时器间隔为]{style="font-size:9.0pt;
  font-family:宋体"}*[length]{lang="EN-US" style="font-size:9.0pt"}*[ ]{lang="EN-US" style="font-size:9.0pt"}[毫秒]{style="font-size:9.0pt;
  font-family:宋体"}

[*[type]{lang="EN-US" style="font-size:10.0pt"}*]{#struct_0_13337_x1854_1184027076}[的类型为：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_INVALID_TYPE]{lang="EN-US"}]{#struct_0_13337_x1854_x1043867515}[：呼叫定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_CHYACK]{lang="EN-US"}]{#struct_0_13337_x1854_x1348114650}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[CHANNEL_READY]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_SRVACK]{lang="EN-US"}]{#struct_0_13337_x1854_1916196139}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[SERVICE_ACK]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_RELCOM]{lang="EN-US"}]{#struct_0_13337_x1854_1072754235}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[RELEASE_COMPLATE]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_OMIT_INFORMATION]{lang="EN-US"}]{#struct_0_13337_x1854_x1418066155}[：]{lang="EN-US" style="font-family:宋体"}[IVR]{lang="EN-US"}[忽略]{lang="EN-US" style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息定时器节点定时器类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_JUMP_WAIT_INPUT]{lang="EN-US"}]{#struct_0_13337_x1854_x1020335503}[：]{lang="EN-US" style="font-family:宋体"}[J]{lang="EN-US"}[ump]{lang="EN-US"}[节点下等待用户按键]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_FIRST_DIAL]{lang="EN-US"}]{#struct_0_13337_x1854_x1043933051}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下首次按键定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_DIAL_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_1647980946}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下按键间隙定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAIT_MPS_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_x783990094}[：等待]{lang="EN-US" style="font-family:宋体"}[MPS]{lang="EN-US"}[响应]{style="font-family:宋体"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[Delete timer, TmrId = *id,* TmrType = *type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_13337_x1854_x1861204651}

[[删除定时器，定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_13337_x1854_x639433240}[Id]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:宋体"}*[id]{lang="EN-US" style="font-size:9.0pt"}*[，定时器类型为]{style="font-size:9.0pt;font-family:
  宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*

[*[type]{lang="EN-US" style="font-size:10.0pt"}*]{#struct_0_13337_x1854_1051940657}[的类型为：]{style="font-size:10.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_INVALID_TYPE]{lang="EN-US"}]{#struct_0_13337_x1854_x1043736443}[：呼叫定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_CHYACK]{lang="EN-US"}]{#struct_0_13337_x1854_x1873339700}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[CHANNEL_READY]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_SRVACK]{lang="EN-US"}]{#struct_0_13337_x1854_x2087427391}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[SERVICE_ACK]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_WAIT_RELCOM]{lang="EN-US"}]{#struct_0_13337_x1854_1198004776}[：]{lang="EN-US" style="font-family:
  宋体"}[IVR]{lang="EN-US"}[等待]{lang="EN-US" style="font-family:
  宋体"}[RELEASE_COMPLATE]{lang="EN-US"}[消息定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_OMIT_INFORMATION]{lang="EN-US"}]{#struct_0_13337_x1854_x568186082}[：]{lang="EN-US" style="font-family:宋体"}[IVR]{lang="EN-US"}[忽略]{lang="EN-US" style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息定时器节点定时器类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_JUMP_WAIT_INPUT]{lang="EN-US"}]{#struct_0_13337_x1854_x1043801979}[：]{lang="EN-US" style="font-family:宋体"}[J]{lang="EN-US"}[ump]{lang="EN-US"}[节点下等待用户按键]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_FIRST_DIAL]{lang="EN-US"}]{#struct_0_13337_x1854_1883950712}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下首次按键定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IVR_TIMER_CALL_DIAL_INTERVAL]{lang="EN-US"}]{#struct_0_13337_x1854_1597535820}[：]{lang="EN-US" style="font-family:宋体"}[Call]{lang="EN-US"}[节点下按键间隙定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WAIT_MPS_ACK]{lang="EN-US"}]{#struct_0_13337_x1854_1233892828}[：等待]{lang="EN-US" style="font-family:宋体"}[MPS]{lang="EN-US"}[响应]{style="font-family:宋体"}[定时器]{lang="EN-US" style="font-family:宋体"}

*[ ]{lang="EN-US" style="color:blue"}*

[[【举例】]{style="font-family:黑体"}]{#struct_0_13337_x1854_999882059}

[[\#]{lang="EN-US"}]{#struct_0_13337_x1854_x1043605371}[ ]{lang="EN-US" style="font-family:宋体"}[用户]{style="font-family:宋体"}[0101003]{lang="EN-US"}[先]{style="font-family:宋体"}[拨打]{style="font-family:宋体"}[IVR]{lang="EN-US"}[接入号]{style="font-family:宋体"}[915]{lang="EN-US"}[，再二次呼叫号码为]{style="font-family:宋体"}[914]{lang="EN-US"}[的用户]{style="font-family:宋体"}[。]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的根节点是]{style="font-family:宋体"}[Call]{lang="EN-US"}[节点，节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[103]{lang="EN-US"}[，并配置以]{style="font-family:宋体"}[ \# ]{lang="EN-US"}[为结束符的普通二次呼叫。打开]{style="font-family:宋体"}[IVR]{lang="EN-US"}[所有调试开关]{style="font-family:宋体"}[，]{style="font-family:宋体"}[用户]{style="font-family:宋体"}[0101003]{lang="EN-US"}[拨打]{style="font-family:宋体"}[IVR]{lang="EN-US"}[接入号]{style="font-family:宋体"}[915]{lang="EN-US"}[，]{style="font-family:宋体"}[debug]{lang="EN-US"}[信息显示如下。]{style="font-family:宋体"}

[[\<Sysname\> debugging vioce ivr all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1005398426}

[[\*Dec 24 10:48:07:086 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1875560679}

[[IVR_Event: CMC \--\> IVR : ACCP_SETUP      CallID = 0x00000009 LocalID = 0xfffffff]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1432865697}

[[f]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1672151056}

[[      Called Number\...915]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1323941967}

[[      Caller Number\...0101003]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1259034794}

[[      Source IfIndex..0x00000281]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2138125153}

[[      InfoTableIndex..0x00000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043480275}

[[      DialPeer Info\...None Codec Transport]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1785161979}

[[                      Entity   Index: 915]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043670907}

[[                      DialPeer  Type: IVR]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_162008361}

[[                      Codec     Type: G729r8 G711a G711u G723-53]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1468240305}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1688687630}*[接收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[ACCP_SETUP]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1408095487}

[[IVR_Event: IVR \--\> CMC : ACCP_SETUP_ACK  CallID = 0x00000009 LocalID = 0x0000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_546466537}

[[2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1574668950}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_417894377}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_SETUP_ACK]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_716936019}

[[IVR_Event: IVR \--\> CMC : ACCP_ALERTING   CallID = 0x00000009 LocalID = 0x0000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1762903570}

[[2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_564021060}

[[      Target IfIndex..0x00000281]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1608659731}

[[      Inband info\.....Avail]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043474299}

[[      InfoTableIndex..0x00000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_73051304}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1125454696}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_ALERTING]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:087 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x911712009}

[[IVR_Event: IVR \--\> CMC : ACCP_CONNECT    CallID = 0x00000009 LocalID = 0x0000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_667871626}

[[2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x305147366}

[[      Target IfIndex..0x00000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1929490774}

[[      Inband info\.....Unavail]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1302338249}

[[      InfoTableIndex..0x00000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x333788536}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x59209839}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_CONNECT]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043539835}

[[IVR_Event: IVR \--\> CMC : ACCP_CHANNEL_READY      CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_134242094}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x393002162}

[[      DecodeProtocol..G729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_510671881}

[[      EncodeProtocol..G729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1130317722}

[[      Vad Switch\...\...Disable]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x227889598}

[[      Local Ecan\...\...Off]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_581835606}

[[      Distance Ecan\...None]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x480125568}

[[      PT Type\...\...\...None]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x241988760}

[[      PayLoadSize\.....30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1444066949}

[[      IP media DSCP\...0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_759597112}

[[      Update type\.....MEDIA_CHANNEL_CONNECT]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043998584}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_414399070}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_CHANNEL_READY]{lang="EN-US"}[消息，用来通知]{style="font-family:宋体"}[CMC]{lang="EN-US"}[，]{style="font-family:宋体"}[IVR]{lang="EN-US"}[的媒体通道已经准备完成]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2047946122}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_CHYACK, TmrLength =]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1063617944}

[[150000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1764856027}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1202969735}*[启动等待]{style="font-family:宋体"}[ACCP_CHANNEL_READY_ACK]{lang="EN-US"}[消息定时器，用来防止]{style="font-family:宋体"}[CMC]{lang="EN-US"}[无响应]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:088 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x671328861}

[[IVR_Fsm: IDLE \--\> WAIT_CHY_ACK, CallId = 9, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1613996705}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_2026462061}*[的状态由初始状态转变为等待]{style="font-family:宋体"}[ACCP_CHANNEL_READY_ACK]{lang="EN-US"}[消息状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1125323031}

[[IVR_Event: CMC \--\> IVR : ACCP_CHANNEL_READY_ACK  CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x116878889}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1044064120}

[[      DecodeProtocol..G729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x705384824}

[[      EncodeProtocol..G729r8]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_949404554}

[[      Vad Switch\...\...Disable]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1973408778}

[[      Local Ecan\...\...None]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1063022680}

[[      Distance Ecan\...None]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1192623395}

[[      PT Type\...\...\...None]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x648267582}

[[      PayLoadSize\.....30]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_690407836}

[[      IP media DSCP\...0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1709987013}

[[      DialPeer Info\...None Codec Transport]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1108545106}

[[                      Entity   Index: 915]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043867512}

[[                      DialPeer  Type: IVR]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1751399177}

[[                      Codec     Type: G729r8 G711a G711u G723-53]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x855854661}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_828055711}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送过来的]{style="font-family:宋体"}[ACCP_CHANNEL_READY_ACK ]{lang="EN-US"}[消息，]{style="font-family:宋体"}[IVR]{lang="EN-US"}[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACK]{lang="EN-US"}[，表示媒体通道准备完成]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x503189882}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_CHYACK.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1543113289}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_624283411}*[删除等待]{style="font-family:宋体"}[ACCP_CHANNEL_READY_ACK]{lang="EN-US"}[消息定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:094 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x968665874}

[[IVR_Event: IVR \--\> CMC : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1715509106}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1944316412}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1284540504}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_INFORMATION ]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:095 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043933048}

[[IVR_Fsm: WAIT_CHY_ACK \--\> ACTIVE, CallId = 9, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x724606513}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1010505828}*[的状态由等待]{style="font-family:宋体"}[ACCP_CHANNEL_READY_ACK]{lang="EN-US"}[消息状态转变为]{style="font-family:宋体"}[通话已建立]{style="font-family:宋体"}[状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:095 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1174642095}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_OMIT_INFORMATION, TmrLeng]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1728079482}

[[th = 500.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_585136205}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_300690175}*[启动忽略按键消息定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2120642847}

[[IVR_Timer: IVR_TIMER_OMIT_INFORMATION timer timed out in NODE_IDLE state.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1226365953}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1744891337}*[忽略按键消息定时器在执行流程初始状态超时]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043736440}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_OMIT_INFORMATION.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1470055173}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1788469427}*[删除忽略按键消息定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:610 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_65619634}

[[IVR_Info: The node id is not in the stack, NodeId = 103.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2101518594}

[*[//]{lang="EN-US"}*]{#struct_0_13337_x1854_1570552923}*[节点]{style="font-family:宋体"}[id]{lang="EN-US"}[不在栈中，即该节点尚未保存在临时空间里]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:611 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1390747035}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_FIRST_DIAL, TmrLengt]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1402588394}

[[h = 3000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1804744664}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1150714823}*[启动首次按键定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:07:611 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1554201337}

[[IVR_Info: NODE_IDLE \--\> CALL_WAIT_INPUT, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043801976}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1201163003}*[节点状态由初始状态转变为]{style="font-family:宋体"}[Call]{lang="EN-US"}[节点等待输入状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_2030965099}

[[IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x295845823}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1746631556}

[[      DTMF Character..9]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x578676454}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x746668441}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息，输入按键号码为]{style="font-family:宋体"}[9]{lang="EN-US"}*

[[\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_156939883}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_FIRST_DIAL.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1448259347}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_758865295}*[删除首次按键定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1328509836}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043605368}

[[ngth = 10000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x204520691}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_233959756}*[启动按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:09:665 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x413553938}

[[IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1933806420}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1866128007}*[节点状态保持]{style="font-family:宋体"}[call]{lang="EN-US"}[节点等待输入状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_76287367}

[[IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_187251234}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_268901782}

[[      DTMF Character..1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_596101311}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1043670904}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送过来的]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息，输入按键号码为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_565292888}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1138509867}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_479682739}*[删除按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:10:415 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_330544851}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x790642493}

[[ngth = 10000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_738803001}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1246929429}*[启动按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:10:416 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1227072530}

[[IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1330045673}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x917572893}*[节点状态保持]{style="font-family:宋体"}[call]{lang="EN-US"}[节点等待输入状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043474296}

[[IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1188796551}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1618501708}

[[      DTMF Character..4]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_195006438}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_109073053}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送过来的]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息，此时二次呼叫号码]{style="font-family:宋体"}[914]{lang="EN-US"}[已全部输入]{style="font-family:宋体"}*

[[\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_586438735}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x757304531}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_9314264}*[删除按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1674458946}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x157108672}

[[ngth = 10000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043539832}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_893756981}*[启动按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:11:585 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1504730779}

[[IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_INPUT, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2080693375}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_800108146}*[节点状态保持]{style="font-family:宋体"}[Call]{lang="EN-US"}[节点等待输入状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:215 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2112638448}

[[IVR_Event: CMC \--\> IVR : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_270686767}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_347501514}

[[      DTMF Character..#]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1797289390}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_1115329438}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送过来的]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息，输入按键号码为]{style="font-family:宋体"}[\#]{lang="EN-US"}*

[[\*Dec 24 10:48:15:215 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_264123784}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1255141383}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1043998585}*[删除按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1151684871}

[[IVR_Event: IVR \--\> DPL : DPL_ROUTE_REQ.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1372592517}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_861873490}*[向]{style="font-family:宋体"}[DPL]{lang="EN-US"}[发出查询实体请求]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x661262058}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL, TmrLe]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_138611156}

[[ngth = 10000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x303436816}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x223552873}*[启动按键间隔定时器，来等待]{style="font-family:宋体"}[DPL]{lang="EN-US"}[查询结果]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:216 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x296031630}

[[IVR_Info: CALL_WAIT_INPUT \--\> CALL_WAIT_ENTITY, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1901219673}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x968463571}*[状态由]{style="font-family:宋体"}[call]{lang="EN-US"}[节点等待输入状态转变为等待查询实体状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1044064121}

[[IVR_Event: DPL \--\> IVR : DPL_ROUTE_RSP.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_860699117}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_583971643}*[收到]{style="font-family:宋体"}[DPL]{lang="EN-US"}[返回的查询实体结果]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1234901899}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_CALL_DIAL_INTERVAL.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_905158498}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x941199326}*[删除按键间隔定时器]{style="font-family:宋体"}*

[[\*Dec 24 12:46:20:881 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1108093500}

[[IVR_Info: CALL_WAIT_INPUT \--\> CALL, LocalId = 5.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x532369585}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x537193850}*[节点状态由等待按键输入转变为二次呼叫状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1509971621}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_SRVACK, TmrLength =]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x797141153}

[[20000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043867513}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x185315236}*[启动等待]{style="font-family:宋体"}[SERVICE_ACK]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x40531053}

[[IVR_Event: IVR \--\> CMC : ACCP_INFORMATION        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1086328572}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_962700716}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x444343086}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:218 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_714841178}

[[IVR_Event: IVR \--\> CMC : ACCP_SERVICE    CallID = 0x00000009 LocalID = 0x0000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x298213889}

[[2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2088384598}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_2035169810}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_SERVICE]{lang="EN-US"}[消息，向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[请求语音业务]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:219 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x2119223179}

[[IVR_Fsm: ACTIVE \--\> WAIT_SERVICE_ACK, CallId = 9, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043933049}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_2004276842}*[状态由活动状态变为等待]{style="font-family:宋体"}[WAIT_SERVICE_ACK]{lang="EN-US"}[消息状态]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x391577511}

[[IVR_Event: CMC \--\> IVR : ACCP_SERVICE_ACK        CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x927294814}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_268578377}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1040845251}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[ACCP_SERVICE_ACK]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_427641090}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_SRVACK.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1380458632}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_155177495}*[删除等待]{style="font-family:宋体"}[SERVICE_ACK]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1408347586}

[[IVR_Info: Service response status is ok, CallId = 9.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043736441}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1258828182}*[语音业务请求成功]{style="font-family:宋体"}*

**[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}**

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x143341335}

[[IVR_Event: IVR \--\> CMC : ACCP_RELEASE    CallID = 0x00000009 LocalID = 0x0000000]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x269056629}

[[2]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x548742140}

[[      ReleaseCause\....Normal clearing!]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_980559934}

[*[// IVR]{lang="EN-US"}*]{#struct_0_13337_x1854_x1873978658}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_RELEASE]{lang="EN-US"}[消息，发送]{style="font-family:宋体"}[ACCP_RELEASE]{lang="EN-US"}[消息的原因是正常释放]{style="font-family:宋体"}*

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_418878500}

[[IVR_Timer: Start timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_RELCOM, TmrLength =]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x355489317}

[[6000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1110057669}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x1043801977}*[启动等待]{style="font-family:宋体"}[Accp Release Complete]{lang="EN-US"}[消息的定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 10:48:15:222 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_364920938}

[[IVR_Fsm: ACTIVE \--\> RELEASE, CallId = 9, LocalId = 2.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1772770444}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x1240845151}*[呼叫状态机由]{style="font-family:宋体"}[WAIT_SERVICE_ACK]{lang="EN-US"}[改变为]{style="font-family:宋体"}[RELEASE]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_830150621}

[[IVR_Event: CMC \--\> IVR : ACCP_RELEASE_COMPLETE   CallID = 0x00000009 LocalID = 0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1428039267}

[[x00000002]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1310700199}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_1438155970}*[接收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[模块向]{style="font-family:宋体"}[IVR]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[Accp Release Complete]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_412274168}

[[IVR_Timer: Delete timer, TmrId = 0, TmrType = IVR_TIMER_WAIT_RELCOM.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1564971989}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x2102868153}*[删除等待]{style="font-family:宋体"}[Accp Release Complete]{lang="EN-US"}[消息的定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\*Dec 24 10:48:15:225 2013 Sysname IVR/7/IVR_DEBUG:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_x1043605369}

[[IVR_Event: IVR \--\> DPL : DPL_DELETE_TABINDEX.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_13337_x1854_1361563250}

[*[// ]{lang="EN-US"}*]{#struct_0_13337_x1854_x977555209}*[IVR]{lang="EN-US"}[向]{style="font-family:宋体"}[DPL]{lang="EN-US"}[发送]{style="font-family:宋体"}[DPL_DELETE_TABINDEX]{lang="EN-US"}[消息，]{style="font-family:宋体"}[DPl]{lang="EN-US"}[可以删除临时查询表]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

*[ ]{lang="EN-US"}*
