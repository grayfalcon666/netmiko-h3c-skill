::: {#835078810 .myid}
[]{#_Toc404794182}[]{#struct_0_17473_x5816_1639886201}

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice lgs**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17473_x5816_1429285596}

[**[debugging voice lgs ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x1651845560}

[**[undo debugging voice lgs]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x240117546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x440284736}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17473_x5816_1741438525}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17473_x5816_573302827}

[[network-admin]{lang="EN-US"}]{#struct_0_17473_x5816_x585034474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17473_x5816_x1992662662}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x958585170}

[**[all]{lang="EN-US"}**]{#struct_0_17473_x5816_x817583258}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17473_x5816_x1415940942}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17473_x5816_x28080845}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17473_x5816_741974161}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_17473_x5816_x584968938}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_17473_x5816_x1780375433}[：表示]{style="font-family:宋体"}[LGS]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17473_x5816_369427018}

[**[debugging voice lgs]{lang="EN-US"}**]{#struct_0_17473_x5816_1475760112}[命令用来打开]{style="font-family:宋体"}[LGS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice lgs]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[LGS]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[LGS]{lang="EN-US"}]{#struct_0_17473_x5816_x1388563289}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging voice lgs error]{lang="EN-US"}]{#struct_0_17473_x5816_1462419431}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x583307827}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_195896076}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1223547924}

[[Failed to send *Type* message to CMC.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2146672783}

[[向]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x584903402}[CMC]{lang="EN-US" style="font-size:9.0pt"}[发送]{style="font-size:9.0pt;font-family:宋体"}*[Type]{lang="EN-US" style="font-size:9.0pt"}*[消息失败]{style="font-size:9.0pt;
  font-family:宋体"}

[*[Type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_84725939}[为]{style="font-size:9.0pt;font-family:宋体"}[LGS]{lang="EN-US" style="font-size:9.0pt"}[发给驱动消息的类型，取值为：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x1086366773}[：表示被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫的信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x1086301237}[：表示主叫对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x1111539454}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_17473_x5816_x1998813214}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫发送完成拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_x1085449269}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_x1947556629}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_17473_x5816_x1085383733}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被发送媒体通道准备就绪信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_352539370}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫发送]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[Failed to send the *Type* command to driver.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x989029719}

[[LGS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x158526520}[向驱动下发]{style="font-size:9.0pt;font-family:宋体"}*[Type]{lang="EN-US" style="font-size:9.0pt"}*[命令失败]{style="font-size:
  9.0pt;font-family:宋体"}

[*[Type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x524601658}[为下发驱动的命令字类型]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_INSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_x1085973558}[：表示下发接口占用命令字]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_DTMF_DETECT_ON]{lang="EN-US"}]{#struct_0_17473_x5816_x1085908022}[：表示下发]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测命令字]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_DTMF_DETECT_OFF]{lang="EN-US"}]{#struct_0_17473_x5816_x1310554198}[：表示下发关闭]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测命令字]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_NTE_ON]{lang="EN-US"}]{#struct_0_17473_x5816_x1086104630}[：表示下发]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[NTE]{lang="EN-US"}[命令字]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_FXS_ALERT_ON]{lang="EN-US"}]{#struct_0_17473_x5816_x849436969}[：表示下发开始振铃命令字]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_FXS_ALERT_OFF]{lang="EN-US"}]{#struct_0_17473_x5816_x1086039094}[：表示下发关闭振铃命令字]{lang="EN-US" style="font-family:宋体"}

[[Failed to allocate memory for CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1970702791}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x585886442}[CCB]{lang="EN-US" style="font-size:9.0pt"}[分配内存失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get LGS private data from interface *interface*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_441855647}

[[从接口获取私有数据失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x2014717568}

[[Failed to deal with the install command.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1045859799}

[[处理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1254866145}[install]{lang="EN-US" style="font-size:9.0pt"}[命令字失败]{style="font-size:9.0pt;font-family:宋体"}

[[No local call index is available.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x567711637}

[[没有空闲的本地呼叫索引]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x585820906}

[[Cannot find the CCB to be deleted.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1030208147}

[[找不到删除的]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1446723549}[CCB]{lang="EN-US" style="font-size:9.0pt"}

[[Received an unexpected message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x221655330}

[[收到一个不是预期的消息]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1750228026}

[[Failed to check ACCP message which received from CMC.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_322945617}

[[从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1998799533}[CMC]{lang="EN-US" style="font-size:9.0pt"}[收到]{style="font-size:9.0pt;font-family:宋体"}[ACCP]{lang="EN-US" style="font-size:9.0pt"}[消息检查失败]{style="font-size:9.0pt;font-family:
  宋体"}

[[The call with call ID *call-id* already exist.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x786874660}

[[Call ID]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x585296621}[为]{style="font-size:9.0pt;font-family:宋体"}[call-id]{lang="EN-US" style="font-size:9.0pt"}[的呼叫已经存在]{style="font-size:9.0pt;
  font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging voice lgs event]{lang="EN-US"}]{#struct_0_17473_x5816_826289531}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x554387763}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x2100120219}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1162367031}

[[ LGS \--\> CMC : *Message-type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x781273470}

[[LGS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1356017753}[进程向]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[进程成功发送]{style="font-size:9.0pt;
  font-family:宋体"}*[Message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[Type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1085449270}[为]{style="font-size:9.0pt;font-family:宋体"}[LGS]{lang="EN-US" style="font-size:9.0pt"}[发给驱动消息的类型，取值为：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x1085383734}[：表示被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫的信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x406975517}[：表示主叫对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x1085973551}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_17473_x5816_x408006203}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫发送完成拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_1350752692}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_x1085908015}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_17473_x5816_1061902189}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被发送媒体通道准备就绪信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_x1086104623}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫发送]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[CMC\--\> LGS : *Message-type*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_x78141608}

[[LGS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x585231085}[进程收到]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[进程发送的]{style="font-size:9.0pt;
  font-family:宋体"}*[Message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[[LGS \--\> DRV: *Command-type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1264629978}

[[向驱动下发]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x2108808378}*[Command-type]{lang="EN-US" style="font-size:9.0pt"}*[命令]{style="font-size:9.0pt;font-family:宋体"}

[[DRV \--\> LGS: *Event-type* ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1177504907}

[[LGS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1489369392}[收到驱动上报的]{style="font-size:9.0pt;font-family:宋体"}*[Event-type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;font-family:宋体"}

[[Send DTMF characters *number* to driver.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_x60775605}

[[发送]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1784142525}[DTMF]{lang="EN-US" style="font-size:9.0pt"}[号码给驱动]{style="font-size:9.0pt;font-family:宋体"}

[[Caller number is null or exceeds the length limit.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x585165549}

[[主叫号码为空或超出长度限制]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_2031127401}

[[Caller name is null or exceeds the length limit.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_894413416}

[[主机名为空或超出长度限制]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x270497000}

[[Send call number to CMC in *state* state.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_508971398}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x585100013}*[state]{lang="EN-US" style="font-size:9.0pt"}*[ e]{lang="EN-US" style="font-size:9.0pt"}[状态向]{style="font-size:9.0pt;
  font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[发送号码，]{style="font-size:9.0pt;font-family:宋体"}*[state]{lang="EN-US" style="font-size:9.0pt"}*[表示当前呼叫的状态]{style="font-size:9.0pt;
  font-family:宋体"}

[[Begin to receive called number.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1461959579}

[[开始接收被叫号码]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x845648096}

[[Received Event-type event from interface *index*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1054193263}

[[从接口]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_731236131}*[index]{lang="EN-US" style="font-size:9.0pt"}*[收到驱动上报的事件类型]{style="font-size:9.0pt;font-family:宋体"}

[[Inband information is unavailable. Play ring-back tone in two seconds.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x585034477}

[[带内信息不可用，两秒钟后播放回铃音]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1625888368}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging voice lgs fsm]{lang="EN-US"}]{#struct_0_17473_x5816_x1560619083}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x561291923}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1384652165}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1391792781}

[[State changes from *state1* to *state2*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x161190130}

[[呼叫状态从]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1114448064}*[state1]{lang="EN-US" style="font-size:9.0pt"}*[切换到]{style="font-size:9.0pt;font-family:宋体"}*[state2]{lang="EN-US" style="font-size:9.0pt"}*[.]{lang="EN-US" style="font-size:
  9.0pt"}

[*[state1]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1086170159}*[和]{style="font-size:9.0pt;font-family:宋体"}[state2]{lang="EN-US" style="font-size:9.0pt"}[的]{style="font-size:9.0pt;font-family:宋体"}*[取值为：]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[LGS_IDLE]{lang="EN-US"}]{#struct_0_17473_x5816_x880825016}[：]{lang="EN-US" style="font-family:宋体"}[LGS]{lang="EN-US"}[初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLER_INSTALLING]{lang="EN-US"}]{#struct_0_17473_x5816_x1086366767}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在占用接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLER_NUM_RCVING]{lang="EN-US"}]{#struct_0_17473_x5816_1513062031}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[收号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLER_CONNECTING]{lang="EN-US"}]{#struct_0_17473_x5816_x1086301231}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在连接]{lang="EN-US" style="font-family:宋体"}[呼叫]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[FXS_CALLER_RING_BACK]{lang="EN-US"}]{#struct_0_17473_x5816_51259960}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[播放回铃音]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLER_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_x1085449263}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线正在]{style="font-family:宋体"}[通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLED_INSTALLING]{lang="EN-US"}]{#struct_0_17473_x5816_x428526855}[：]{lang="EN-US" style="font-family:宋体"}[被叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在占用接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLED_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_x1085383727}[：]{lang="EN-US" style="font-family:宋体"}[被叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[振铃]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXS_CALLED_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_x1085973552}[：]{lang="EN-US" style="font-family:宋体"}[被叫使用的]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXO_CALLER_INSTALLING]{lang="EN-US"}]{#struct_0_17473_x5816_x1974090144}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在占用接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXO_CALLER_NUM_RCVING]{lang="EN-US"}]{#struct_0_17473_x5816_x1085908016}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[收号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[FXO_CALLER_CONNECTING]{lang="EN-US"}]{#struct_0_17473_x5816_658617662}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在连接呼叫]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXO_CALLER_RING_BACK]{lang="EN-US"}]{#struct_0_17473_x5816_x1086104624}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[播放回铃音]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXO_CALLER_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_1119997035}[：]{lang="EN-US" style="font-family:宋体"}[主叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线正在]{style="font-family:宋体"}[通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[FXO_CALLED_INSTALLING]{lang="EN-US"}]{#struct_0_17473_x5816_x1086039088}[：]{lang="EN-US" style="font-family:宋体"}[被叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[正在占用接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[FXO_CALLED_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_762995314}[：]{lang="EN-US" style="font-family:宋体"}[被叫使用的]{style="font-family:宋体"}[FXO]{lang="EN-US"}[语音用户线在]{style="font-family:宋体"}[通话]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging voice lgs info]{lang="EN-US"}]{#struct_0_17473_x5816_x584968941}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x558092787}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1779785614}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_553858566}

[[ Reconnecting to HA daemon, Please wait\...]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x544621190}

[[重连]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x292911565}[HA]{lang="EN-US" style="font-size:9.0pt"}

[[Failed to connect to HA daemon.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2013810199}

[[连]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1270474337}[[接]{style="font-size:
  9.0pt;font-family:宋体"}]{.TableTextChar}[[HA]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[[失败]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging voice lgs timer]{lang="EN-US"}]{#struct_0_17473_x5816_x584903405}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x564622707}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_84660403}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1721058520}

[[ Submodel *name* init timed out, TimerID = *timerid* duration = *time-length* ms.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_853203129}

[[LGS]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2098808305}[子模块]{style="font-size:9.0pt;font-family:宋体"}[ *[name]{lang="EN-US"}*]{style="font-size:9.0pt"}[初始化超时，定时器]{style="font-size:9.0pt;font-family:宋体"}[ID]{lang="EN-US" style="font-size:9.0pt"}[为]{style="font-size:9.0pt;font-family:
  宋体"}*[timerID]{lang="EN-US" style="font-size:9.0pt"}*[，持续时间为]{style="font-size:9.0pt;font-family:宋体"}*[TimerLen]{lang="EN-US" style="font-size:9.0pt"}*[毫秒]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to get timer *Timer-name length*, state:State-type.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1237800977}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1111823384}*[State-type]{lang="EN-US" style="font-size:9.0pt"}*[呼叫的状态，获取定时器时长失败]{style="font-size:9.0pt;font-family:宋体"}

[[Succeed in starting the *Timer-name* timer, state: *State-typ*e, time length:*Timelengh*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x585886445}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_441790111}*[State-type]{lang="EN-US" style="font-size:9.0pt"}*[呼叫的状态，创建定时器]{style="font-size:9.0pt;font-family:宋体"}*[Timer-name]{lang="EN-US" style="font-size:9.0pt"}*[，持续时间为]{style="font-size:9.0pt;
  font-family:宋体"}*[TimerLen]{lang="EN-US" style="font-size:9.0pt"}*[毫秒]{style="font-size:9.0pt;font-family:宋体"}

[*[State-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1086170160}[取值同表]{style="font-size:9.0pt;font-family:
  宋体"}[1-3]{lang="EN-US" style="font-size:9.0pt"}

[[Succeed in stopping the *Timer-name* timer,state:*State-type.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1284667965}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1492003589}*[State-type]{lang="EN-US" style="font-size:9.0pt"}*[呼叫的状态，]{style="font-size:9.0pt;font-family:宋体"}[LGS ]{lang="EN-US" style="font-size:9.0pt"}[删除定时器]{style="font-size:9.0pt;font-family:
  宋体"}*[Timer-name]{lang="EN-US" style="font-size:9.0pt"}*

[*[State-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1086366768}[取值同表]{style="font-size:9.0pt;font-family:
  宋体"}[1-3]{lang="EN-US" style="font-size:9.0pt"}

[*[Timer-name]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1654414875}[ timer timed out in State-type state.]{lang="EN-US" style="font-size:9.0pt"}

[[LGS *Timer-name*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2126764276}[定时器在]{style="font-size:9.0pt;
  font-family:宋体"}*[State-type]{lang="EN-US" style="font-size:9.0pt"}*[状态下超时]{style="font-size:9.0pt;font-family:宋体"}

[*[State-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1086301232}[取值同表]{style="font-size:9.0pt;font-family:
  宋体"}[1-3]{lang="EN-US" style="font-size:9.0pt"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x585820909}

[[\# ]{lang="EN-US"}]{#struct_0_17473_x5816_x1031060115}[打开主叫侧]{style="font-family:宋体"}[LGS]{lang="EN-US"}[所有类型的调试信息输出开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging voice lgs all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_17473_x5816_x1073518848}

[[\<Sysname\>\*Jan 20 08:59:33:731 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_874309224}

[LGS_Event: DRV \--\> LGS:  VOICE_EVENT_FXS_OFF_HOOK ]{lang="EN-US"}

[*[// LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_2065527852}*[收到驱动上报的摘机事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:732 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_315914158}

[LGS_Event: \[0x000005a3\] Find CCB for driver message VOICE_EVENT_FXS_OFF_HOOK ]{lang="EN-US"}

[in LGS_IDLE state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_620472269}*[根据事件找到相应的]{style="font-family:宋体"}[CCB]{lang="EN-US"}[，这时候]{style="font-family:宋体"}[LGS]{lang="EN-US"}[在初始]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:732 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x585362156}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICE_COM_INSTALL]{lang="EN-US"}

[*[// LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_x655533203}*[向驱动下发占用命令]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:733 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1873319064}

[LGS_Timer: \[0x000005a3\] Succeed in starting Wait_Install_ACK timer,]{lang="EN-US"}

[state:LGS_IDLE, time length:3000ms.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1620239435}*[创建等待]{style="font-family:宋体"}[install_ACK]{lang="EN-US"}[的定时器，这时候状态是]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[，定时器时长是]{style="font-family:宋体"}[3000ms]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:733 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1456843437}

[LGS_Fsm: \[0x000005a3\] State changes from LGS_IDLE to FXS_CALLER_INSTALLING]{lang="EN-US"}

[*[//LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_1888405049}*[状态从]{style="font-family:宋体"}[LGS_IDLE]{lang="EN-US"}[转到]{style="font-family:宋体"}[FXS_CALLER_INSTALLING]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_370654705}

[LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_INSTALL_ACK:  Success ]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_17473_x5816_x585296620}*[收到驱动上报的]{style="font-family:宋体"}[INSTALL_ACK]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_826355067}

[LGS_Event: \[0x000005a3\] Find CCB for driver message VOICE_EVENT_COM_INSTALL_ACK ]{lang="EN-US"}

[in FXS_CALLER_INSTALLING state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: \[0x000005a3\] Succeed in stopping Wait_Install_ACK timer,]{lang="EN-US"}

[state:FXS_CALLER_INSTALLING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:33:761 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] Send play Dial tone command to driver in ]{lang="EN-US"}

[FXS_CALLER_INSTALLING state.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_17473_x5816_x110662387}*[向驱动发送播放拨号音的命令，在]{style="font-family:宋体"}[FXS_CALLER_INSTALLING]{lang="EN-US"}[状态下]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x585231084}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICEL_COM_TONE_GEN_ON]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: \[0x000005a3\] Succeed in starting First Dial timer,]{lang="EN-US"}

[state:FXS_CALLER_INSTALLING, time length:10000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICE_COM_DTMF_DETECT_ON]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:33:762 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Fsm: \[0x000005a3\] State changes from FXS_CALLER_INSTALLING to FXS_CALLER_NUM_RCVING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_DTMF_IND:  1 ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] Find CCB for driver message VOICE_EVENT_COM_DTMF_IND ]{lang="EN-US"}

[in FXS_CALLER_NUM_RCVING state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:021 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: \[0x000005a3\] Succeed in stopping First Dial timer,]{lang="EN-US"}

[state:FXS_CALLER_NUM_RCVING]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1264695514}*[停止]{style="font-family:宋体"}[First Dial]{lang="EN-US"}[定时器，状态是]{style="font-family:宋体"}[FXS_CALLER_NUM_RCVING]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:35:022 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1450796400}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICE_COM_TONE_GEN_OFF]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:022 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: LGS \--\> CMC : ACCP_SETUP]{lang="EN-US"}

[*[// LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_830802661}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_SETUP]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:35:023 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x585165548}

[LGS_Timer: \[0x000005a3\] Succeed in starting Dial_Interval timer,]{lang="EN-US"}

[state:FXS_CALLER_NUM_RCVING, time length:10000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:024 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Fsm: \[0x000005a3\] State changes from FXS_CALLER_NUM_RCVING to FXS_CALLER_PREPARE]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: DRV \--\> LGS:  VOICE_EVENT_COM_DTMF_IND:  0 ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] Find CCB for driver message VOICE_EVENT_COM_DTMF_IND ]{lang="EN-US"}

[in FXS_CALLER_PREPARE state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:681 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] Send call number to CMC in FXS_CALLER_PREPARE state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_2031061865}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送被叫号码，在]{style="font-family:宋体"}[FXS_CALLER_PREPARE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:35:682 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1283625989}

[LGS_Event: LGS \--\> CMC : ACCP_INFORMATION]{lang="EN-US"}

[*[// LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_x186925505}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_INFORMATION]{lang="EN-US"}[消息]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x2120643498}

[LGS_Event: CMC \--\> LGS : ACCP_SETUP_ACK]{lang="EN-US"}

[*[// LGS]{lang="EN-US"}*]{#struct_0_17473_x5816_x1312480934}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的]{style="font-family:宋体"}[ACCP_SETUP_ACK]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x585100012}

[LGS_Timer: \[0x000005a3\] Succeed in stopping Dial_Interval timer,]{lang="EN-US"}

[state:FXS_CALLER_PREPARE]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICE_COM_DTMF_DETECT_OFF]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:684 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: \[0x000005a3\] Succeed in starting Wait_ACCP_ALERTING timer,]{lang="EN-US"}

[state:FXS_CALLER_PREPARE, time length:35000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:685 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Fsm: \[0x000005a3\] State changes from FXS_CALLER_PREPARE to FXS_CALLER_CONNECTING]{lang="EN-US"}

[\*Jan 20 08:59:35:716 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: CMC \--\> LGS : ACCP_ALERTING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:716 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: \[0x000005a3\] Delete timer Wait ACCP_ALERTING success,]{lang="EN-US"}

[state:FXS_CALLER_CONNECTING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: Inband information is unavailable. Play ring-back tone in two seconds.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1462025115}*[带内消息不可用，两秒钟后播放回铃音]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"Courier New\""}

[[\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x585034476}

[LGS_Timer: \[0x000005a3\] Create timer Delay Ring Back,]{lang="EN-US"}

[state:FXS_CALLER_CONNECTING, time length:2000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:35:717 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Fsm: \[0x000005a3\] State changes from FXS_CALLER_CONNECTING to FXS_CALLER_RING_BACK]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Timer: Delay ring back timer timed out in FXS_CALLER_RING_BACK state. ]{lang="EN-US"}

[*[// Delay ring back]{lang="EN-US"}*]{#struct_0_17473_x5816_1625953904}*[定时器在]{style="font-family:宋体"}[FXS_CALLER_RING_BACK]{lang="EN-US"}[状态下超时]{style="font-family:宋体"}*

[[\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_94146697}

[LGS_Event: \[0x000005a3\] Send play RingBack tone command to driver in ]{lang="EN-US"}

[FXS_CALLER_RING_BACK state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan 20 08:59:37:758 2012 Sysname LGS/7/LGS_DEBUG: ]{lang="EN-US"}

[LGS_Event: \[0x000005a3\] LGS \--\> DRV: VOICE_COM_TONE_GEN_ON]{lang="EN-US"}

::: {#919985566 .myid}
[]{#_Toc404794183}[]{#struct_0_17473_x5816_1231431307}

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice em**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17473_x5816_729456636}

[**[debugging vioce em ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x1772738624}

[**[undo debugging voice em]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_392602514}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1284321911}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17473_x5816_x584968940}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1779851150}

[[network-admin]{lang="EN-US"}]{#struct_0_17473_x5816_x2085162078}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17473_x5816_2146036794}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x126967135}

[**[all]{lang="EN-US"}**]{#struct_0_17473_x5816_x628454111}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17473_x5816_165162732}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17473_x5816_x584903404}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17473_x5816_84594867}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_17473_x5816_53238391}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_17473_x5816_557137162}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17473_x5816_1391701896}

[**[debugging voice em]{lang="EN-US"}**]{#struct_0_17473_x5816_x513612886}[命令用来打开]{style="font-family:宋体"}[EM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice em]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[EM]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[EM]{lang="EN-US"}]{#struct_0_17473_x5816_x1383601744}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging voice em error]{lang="EN-US"}]{#struct_0_17473_x5816_163219446}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x562591379}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1502167701}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x585886444}

[[ Received unknown driver message!]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_441724575}

[[收到]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1823060422}[EM]{lang="EN-US" style="font-size:9.0pt"}[不支持的驱动消息]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to wait message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1085293470}

[[等待消息超时]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1344799514}

[[Failed to get EM private data from interface *index*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_944594153}

[[获取]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x585820908}[EM]{lang="EN-US" style="font-size:9.0pt"}[接口]{style="font-size:9.0pt;font-family:宋体"}*[index]{lang="EN-US" style="font-size:9.0pt"}*[下配置失败]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to send message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1031125651}

[[发送消息失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1408833913}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging voice em event]{lang="EN-US"}]{#struct_0_17473_x5816_1703194182}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x563105491}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x133892562}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_883477579}

[[ Succeed in sending message-type  to CMC.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x833951855}

[[EM]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555345114}[模块给]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[模块发送]{style="font-size:9.0pt;font-family:
  宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x18833415}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x726264070}[：表示被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫的信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_1287663172}[：表示主叫对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x1618607474}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_17473_x5816_264478113}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送完成拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_555279578}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_1140575652}[：表示主叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_17473_x5816_x2074417825}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送媒体通道准备就绪信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CHANNEL_UPDATE]{lang="EN-US"}]{#struct_0_17473_x5816_480175921}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的媒体通道更新信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_1840708330}[：表示主]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[被叫给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[EM \--\> DRV: *command-type*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1697900624}

[[EM ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555214042}[模块给驱动下发命令字：]{style="font-size:9.0pt;font-family:宋体"}

[*[command-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x792783889}[ ]{lang="EN-US" style="font-size:9.0pt"}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_INSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_1833289854}[：表示给驱动下发发起呼叫的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_UNINSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_x1861007971}[：表示给驱动下发拆除呼叫的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_AEM_SEIZE]{lang="EN-US"}]{#struct_0_17473_x5816_x1045035545}[：表示给驱动下发占用信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_AEM_IDLE]{lang="EN-US"}]{#struct_0_17473_x5816_x1457234067}[：表示给驱动下发示闲信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_DTMF_GEN]{lang="EN-US"}]{#struct_0_17473_x5816_555148506}[：表示给驱动下发发送号码的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_TONE_GEN_ON]{lang="EN-US"}]{#struct_0_17473_x5816_x297349745}[：表示给驱动下发播放提示音的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_TONE_GEN_OFF]{lang="EN-US"}]{#struct_0_17473_x5816_x1822421931}[：表示给驱动下发停止播放提示音的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_DTMF_DETECT_ON]{lang="EN-US"}]{#struct_0_17473_x5816_x58615809}[：表示给驱动下发打开]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_DTMF_DETECT_OFF]{lang="EN-US"}]{#struct_0_17473_x5816_1963958149}[：表示给驱动下发关闭]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[检测的命令]{lang="EN-US" style="font-family:宋体"}

[[Received *message-type* message from CMC in state *call-state*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555607258}

[[EM]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1844827426}[在]{style="font-size:9.0pt;font-family:宋体"}*[call-state]{lang="EN-US" style="font-size:9.0pt"}*[状态下收到]{style="font-size:9.0pt;font-family:宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;
  font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x491587969}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x1647011165}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给主叫发送的建立新呼叫的消息]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_555541722}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给被叫发送的建立新呼叫应答消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x527113131}[：表示收到了]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[拆除呼叫的消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_17473_x5816_1810914982}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[对]{lang="EN-US" style="font-family:宋体"}[E&M]{lang="EN-US"}[发送的拆除呼叫请求的应答]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_100390514}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[连接建立的消息]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_555476186}[：表示被叫端已经开始振铃]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_17473_x5816_280731674}[：表示主叫端收到]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[，已经准备好媒体通道的消息]{lang="EN-US" style="font-family:宋体"}

[[Received *event-type* from DRV in * call-state*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x780206088}

[[EM]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1760875147}[在]{style="font-size:9.0pt;font-family:宋体"}*[call-state]{lang="EN-US" style="font-size:9.0pt"}*[状态下收到驱动发的]{style="font-size:9.0pt;font-family:宋体"}*[event-type]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;
  font-family:宋体"}

[*[event-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_555410650}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_EVENT_COM_INSTALL_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x154052533}[：表示驱动给]{lang="EN-US" style="font-family:宋体"}[EM]{lang="EN-US"}[上报呼叫初始化的处理结果的事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_EVENT_COM_DTMF_IND]{lang="EN-US"}]{#struct_0_17473_x5816_x1849751440}[：表示驱动给]{lang="EN-US" style="font-family:宋体"}[EM]{lang="EN-US"}[上报收到了]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[被叫号码的应答事件]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging voice em fsm]{lang="EN-US"}]{#struct_0_17473_x5816_1946913635}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x569631315}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1600729581}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_555869402}

[[ State changed from *current-state* to *next-state*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1248181660}

[[呼叫状态从当前状态]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1883312733}*[current-state]{lang="EN-US" style="font-size:
  9.0pt"}*[切换到下一个状态]{style="font-size:9.0pt;font-family:宋体"}*[next-state]{lang="EN-US" style="font-size:9.0pt"}*

[*[current-state]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_126650753}[和]{style="font-size:9.0pt;font-family:
  宋体"}*[next-state]{lang="EN-US" style="font-size:9.0pt"}*[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EM_IDLE ]{lang="EN-US"}]{#struct_0_17473_x5816_x4291739}[：表示通道空闲]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLER_WAIT_INSTALL_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x265846679}[：表示正在等待驱动建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLER_WAIT_OCCUPY]{lang="EN-US"}]{#struct_0_17473_x5816_116645223}[：表示等待占用信号的上升沿]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLER_WAIT_SEND_NUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_555803866}[：表示等待发送被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLER_SENDING_NUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_308263138}[：表示主叫端正在发送被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLER_RINGING]{lang="EN-US"}]{#struct_0_17473_x5816_x868817979}[：表示主叫端正在听回铃音]{lang="EN-US" style="font-family:宋体"}[,]{lang="EN-US"}[即等待被叫应答]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLER_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_2006733314}[：表示主叫正在通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLER_ONHOOK]{lang="EN-US"}]{#struct_0_17473_x5816_243901102}[：表示主叫先挂机]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLED_WAIT_SEND_OCCUPY]{lang="EN-US"}]{#struct_0_17473_x5816_555345115}[：表示等待发送占用信号上升沿]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLED_WAIT_RECEIVE_NUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_x18833414}[：表示等待接收被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLED_RECEIVING_NUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_x726264071}[：表示被叫端正在接收被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLED_WAIT_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_1287728708}[：表示等待呼叫初始化完成]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLED_RINGING]{lang="EN-US"}]{#struct_0_17473_x5816_x384708039}[：表示被叫正在振铃]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[EMCALLED_TALKING]{lang="EN-US"}]{#struct_0_17473_x5816_555279579}[：表示被叫正在通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLED_ONHOOK]{lang="EN-US"}]{#struct_0_17473_x5816_1140575651}[：表示被叫先挂机]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[EMCALLED_BUSYTONE]{lang="EN-US"}]{#struct_0_17473_x5816_x2074352289}[：表示被叫正在播放忙音]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging voice em info]{lang="EN-US"}]{#struct_0_17473_x5816_x1708701596}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x566604819}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_507767449}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1249118420}

[[The current interface index\[*index*\] has been occupied.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555214043}

[[当前的语音接口]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x792783890}*[index]{lang="EN-US" style="font-size:9.0pt"}*[被占用]{style="font-size:9.0pt;font-family:宋体"}

[[Succeed in creating E&M CCB\[*id*\]]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1833748605}

[[成功创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1539851886}[[CCB]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[(]{lang="EN-US" style="font-size:
  9.0pt;font-family:宋体"}[呼叫控制块[)]{lang="EN-US"}，]{style="font-size:9.0pt;font-family:宋体"}[*[id]{lang="EN-US" style="font-size:9.0pt"}*]{.TableTextChar}[为呼叫控制块的标识]{style="font-size:9.0pt;
  font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging voice em timer]{lang="EN-US"}]{#struct_0_17473_x5816_1105713834}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x567427347}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_594980593}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_958124954}

[[Deleted TimerId \[timer-id\]]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555148507}

[[删除特定的定时器]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x297349744}

[*[timer-id]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1822356395}[为定时器的唯一标示]{style="font-size:9.0pt;font-family:宋体"}

[[Created message-waiting confirmation timer \[timer-id\]]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1425354396}[，]{style="font-size:9.0pt;font-family:宋体"}[ [length is 50 ms]{lang="EN-US"}]{style="font-size:9.0pt"}

[[创建示闲信号确认定时器，时长为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1269887220}*[time-length]{lang="EN-US" style="font-size:9.0pt"}*[毫秒]{style="font-size:9.0pt;
  font-family:宋体"}

[[Created message-occupied confirmation timer \[timer-id\]]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_257367103}[，]{style="font-size:9.0pt;font-family:宋体"}[ [length is 50 ms.]{lang="EN-US"}]{style="font-size:9.0pt"}

[[创建占用信号确认定时器，时长为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_555607259}*[time-length]{lang="EN-US" style="font-size:9.0pt"}*[毫秒]{style="font-size:9.0pt;
  font-family:宋体"}

*[ ]{lang="EN-US" style="color:blue"}*

[[【举例】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1844827425}

[[\# E&M]{lang="EN-US"}]{#struct_0_17473_x5816_x2057671910}[语音用户线]{style="font-family:宋体"}[5/0]{lang="EN-US"}[为主叫，]{style="font-family:宋体"}[E&M]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[5/3]{lang="EN-US"}[为被叫，被叫号码为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging vioce em all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_17473_x5816_1271878155}

[[\*Feb 10 11:41:47:756 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2146864938}

[EM_Event: CMC \--\> EM : ACCP_SETUP]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x2037685276}*[主叫端]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发来建立呼叫消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:47:757 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1631712602}

[EM_Info: \[subscriber-line5/0\]: Succeed in creating EM CCB\[0\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_555541723}*[创建呼叫控制块，控制块]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:47:757 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x527113130}

[EM_Event: \[subscriber-line5/0\]: Received ACCP_SETUP message from CMC on state EM_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[0\] to wait install ack, length is 1000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_INSTALL]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:758 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EM_IDLE to EMCALLER_WAIT_INSTALL_ACK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Received VOICE_EVENT_COM_INSTALL_ACK from DRV on state EMCALLER_WAIT_INSTALL_ACK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[0\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:790 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[0\] to dialout delay, length is 300ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:791 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending ACCP_SETUP_ACK to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:791 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_AEM_SEIZE.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1810980518}*[主叫端向驱动下发占用信号命令]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:47:792 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555476187}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending low-to-high level.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:792 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending ACCP_ALERTING to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:793 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EMCALLER_WAIT_INSTALL_ACK to EMCALLER_WAIT_SEND_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:880 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Info: \[subscriber-line5/3\]: Succeed in creating EM CCB\[1\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_280731673}*[被叫端创建呼叫控制块，控制块]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:47:880 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x780206083}

[EM_Event: \[subscriber-line5/3\]: Received VOICE_EVENT_AEM_SEIZE from DRV on state EM_IDLE.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1761202827}*[被叫端在空闲状态收到驱动上报的占用信号，准备建立呼叫]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:47:881 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555410651}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to seize confirm, length is 50ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received EM_TIMER_SIGNAL_CONFIRM on state EM_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:925 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to wait install ack, length is 1000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:926 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_INSTALL]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:926 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EM_IDLE to EMCALLED_WAIT_RECEIVE_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received VOICE_EVENT_COM_INSTALL_ACK from DRV on state EMCALLED_WAIT_RECEIVE_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:970 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to wait dtmf ind, length is 5000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:971 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_DTMF_DETECT_ON.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:47:971 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EMCALLED_WAIT_RECEIVE_NUMBER to EMCALLED_RECEIVING_NUMBER.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x154052534}*[被叫端呼叫状态从等待收号到进行收号]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1850079120}

[EM_Event: \[subscriber-line5/0\]: Received EM_TIMER_SIGNAL_WAIT on state EMCALLER_WAIT_SEND_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[0\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_2115301058}*[删除定时器标示为]{style="font-family:宋体"}[1]{lang="EN-US"}[的定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:48:125 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555803867}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_DTMF_GEN]{lang="EN-US"}

[DTMF Number is 20]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:126 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[0\] to wait dtmf ack, length is 60000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:126 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EMCALLER_WAIT_SEND_NUMBER to EMCALLER_SENDING_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received VOICE_EVENT_COM_DTMF_IND from DRV on state EMCALLED_RECEIVING_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending ACCP_SETUP to CMC, Number is 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:260 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Begin to receive next called number.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:261 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to inter digit, length is 10000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:261 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EMCALLED_RECEIVING_NUMBER to EMCALLED_RECEIVING_NUMBER_PREPARE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received VOICE_EVENT_COM_DTMF_IND from DRV on state EMCALLED_RECEIVING_NUMBER_PREPARE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[0x00000694\]: Send call number to CMC in EMCALLED_RECEIVING_NUMBER_PREPARE state.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending ACCP_INFORMATION to CMC]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:530 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: DTMF Character 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:533 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_SETUP_ACK]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:533 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received ACCP_SETUP_ACK message from CMC on state EMCALLED_RECEIVING_NUMBER_PREPARE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_308263139}*[被叫端结束收号，向驱动下发停止收号命令]{style="font-family:宋体"}*

*[ ]{lang="EN-US" style="font-size:9.0pt"}*

[[\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555345112}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to wait alerting, length is 40000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:534 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EMCALLED_RECEIVING_NUMBER_PREPARE to EMCALLED_RINGING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:586 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_ALERTING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:586 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received ACCP_ALERTING message from CMC on state EMCALLED_RINGING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending ACCP_CHANNEL_READY to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:587 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to wait connect, length is 60000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:588 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_TONE_GEN_ON.]{lang="EN-US"}

[Succeed in sending ringing to Driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Received VOICE_EVENT_COM_DTMF_ACK from DRV on state EMCALLER_SENDING_NUMBER.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[0\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:680 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[0\] to seize signal, length is 60000ms.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x18833417}*[主叫端创建等待被叫端占用信号的定时器，时长为]{style="font-family:宋体"}[60000]{lang="EN-US"}[毫秒]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555279576}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending ACCP_CHANNEL_READY to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EMCALLER_SENDING_NUMBER to EMCALLER_RINGING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:48:684 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_CHANNEL_READY_ACK]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:788 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_CHANNEL_READY_ACK]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:888 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_CONNECT]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1140575662}*[被叫端收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[连接建立的消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:50:888 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555214040}

[EM_Event: \[subscriber-line5/3\]: Received ACCP_CONNECT message from CMC on state EMCALLED_RINGING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_TONE_GEN_OFF]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in stopping ringing.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:889 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_AEM_SEIZE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:890 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending low-to-high level.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:890 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EMCALLED_RINGING to EMCALLED_TALKING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:970 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Received VOICE_EVENT_AEM_SEIZE from DRV on state EMCALLER_RINGING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:970 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending ACCP_CONNECT to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:971 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[0\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:50:971 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EMCALLER_RINGING to EMCALLER_TALKING.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x792783891}*[主叫端从播放回铃音的状态切换到通话的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1833814141}

[EM_Event: CMC \--\> EM : ACCP_RELEASE]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Received ACCP_RELEASE message from CMC on state EMCALLER_TALKING.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1660567979}*[主叫端在通话状态下从]{style="font-family:宋体"}[CMC]{lang="EN-US"}[收到挂机信号]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:55:597 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_923370338}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[0\] to busy tone end, length is 60000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:598 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_DTMF_DETECT_OFF.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:598 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_AEM_IDLE.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1389995877}*[主叫端向驱动下发示闲信令，准备拆除呼叫]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555148504}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending high-to-low level.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_TONE_GEN_ON.]{lang="EN-US"}

[Succeed in sending busytone to Driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/0\]: State changed from EMCALLER_TALKING to EMCALLER_CALLER_ONHOOK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:599 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending ACCP_RELEASE_COMPLETE to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:680 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received VOICE_EVENT_AEM_IDLE from DRV on state EMCALLED_TALKING.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x297349747}*[被叫端在通话状态下收到主叫端的示闲信号，准备拆除呼叫]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:55:680 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555607256}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to idle confirm, length is 50ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received EM_TIMER_SIGNAL_CONFIRM on state EMCALLED_TALKING.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_AEM_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:725 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending high-to-low level.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in sending ACCP_RELEASE to CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Created message wait timer\[1\] to wait release complete, length is 3000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:726 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Fsm: \[subscriber-line5/3\]: State changed from EMCALLED_TALKING to EMCALLED_CALLED_ONHOOK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: CMC \--\> EM : ACCP_RELEASE_COMPLETE]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Received ACCP_RELEASE_COMPLETE message from CMC on state EMCALLED_CALLED_ONHOOK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:729 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: EM \--\> DRV: VOICE_COM_UNINSTALL.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/3\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:730 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/3\]: Succeed in deleting EMCCB\[1\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1844827436}*[被叫端删除控制块，表明已经拆除此路呼叫]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:55:800 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555541720}

[EM_Event: \[subscriber-line5/0\]: Received VOICE_EVENT_AEM_IDLE from DRV on state EMCALLER_CALLER_ONHOOK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:800 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Created message wait timer\[1\] to idle confirm, length is 50ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Received EM_TIMER_SIGNAL_CONFIRM on state EMCALLER_CALLER_ONHOOK.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_TONE_GEN_OFF]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:825 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in stopping busytone.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[0\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_AEM_IDLE.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:826 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in sending high-to-low level.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: EM \--\> DRV: VOICE_COM_UNINSTALL.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x527113133}*[主叫端向驱动下发拆除呼叫命令，通知驱动拆线]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_555476184}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Timer: \[subscriber-line5/0\]: Deleted TimerId \[-1\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Feb 10 11:41:55:827 2012 Sysname EM/7/EM_DEBUG: ]{lang="EN-US"}

[EM_Event: \[subscriber-line5/0\]: Succeed in deleting EMCCB\[0\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_280731676}*[主叫端删除控制块，表明呼叫完全拆除]{style="font-family:宋体"}*

::: {#922803593 .myid}
[]{#_Toc404794184}[]{#struct_0_17473_x5816_x780206086}

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice r2**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1761530507}

[**[debugging voice r2 ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x1371787495}

[**[undo debugging voice r2 ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_1919254977}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17473_x5816_555410648}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17473_x5816_1802262611}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1338295563}

[[network-admin]{lang="EN-US"}]{#struct_0_17473_x5816_1190049583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17473_x5816_x2120154450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1923314502}

[**[all]{lang="EN-US"}**]{#struct_0_17473_x5816_1599266805}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17473_x5816_555869400}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17473_x5816_x1248181658}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17473_x5816_2055227595}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_17473_x5816_x1986992102}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_17473_x5816_1194631354}[：表示]{style="font-family:宋体"}[R2]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1430789173}

[**[debugging voice r2]{lang="EN-US"}**]{#struct_0_17473_x5816_1287924141}[命令用来打开]{style="font-family:宋体"}[R2]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice r2]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[R2]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[R2]{lang="EN-US"}]{#struct_0_17473_x5816_x850376517}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-11 ]{lang="EN-US"}[debugging voice r2 error]{lang="EN-US"}]{#struct_0_17473_x5816_x1229965689}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x540711251}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_555803864}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_308263136}

[[Failed to send *message-type* to cmc.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x868817965}

[[R2]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2005946883}[向]{style="font-size:9.0pt;font-family:宋体"}[CMC ]{lang="EN-US" style="font-size:9.0pt"}[模块发送消息失败]{style="font-size:9.0pt;
  font-family:宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_398720846}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x1530934828}[：表示入局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_555345113}[：表示出局端对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_x18833416}[：表示出局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_x726264069}[：表示出局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[Failed to send *command-type* to driver.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1287204419}

[[R2]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_718752287}[向驱动下发命令字失败]{style="font-size:9.0pt;font-family:宋体"}

[*[command-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x540904422}[命令字类型取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_INSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_555279577}[：表示出局端给驱动下发安装呼叫准备工作的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_DTMF_GEN]{lang="EN-US"}]{#struct_0_17473_x5816_1140575661}[：表示出局端通过]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式给驱动下发被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_CAS_LINESIG]{lang="EN-US"}]{#struct_0_17473_x5816_x2074352292}[：表示出局端给驱动下发线路信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_MFC_GEN_ON]{lang="EN-US"}]{#struct_0_17473_x5816_213678241}[：表示出局端给驱动下发]{lang="EN-US" style="font-family:宋体"}[MFC]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[Failed to send VOICE \_CAS_LINESIG *lineSig-type* to driver.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1318194768}

[[R2]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1110798378}[向驱动下发线路信令失败，其中线路信令值为]{style="font-size:9.0pt;font-family:宋体"}*[lineSig-type ]{lang="EN-US" style="font-size:9.0pt"}*[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_17473_x5816_555214041}[：表示当前线路处于空闲状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BLOCK]{lang="EN-US"}]{#struct_0_17473_x5816_x792783892}[：表示当前线路处于被阻塞状态]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SEIZURE]{lang="EN-US"}]{#struct_0_17473_x5816_1833879677}[：表示当前线路处于被占用状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CLEARFORWARD]{lang="EN-US"}]{#struct_0_17473_x5816_28263509}[：表示当前线路处于前向拆线状态]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[SEIZUREACK]{lang="EN-US"}]{#struct_0_17473_x5816_397419455}[：表示当前线路处于占用应答状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ANSWER]{lang="EN-US"}]{#struct_0_17473_x5816_555148505}[：表示当前线路处于接通回应状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CLEARBACK]{lang="EN-US"}]{#struct_0_17473_x5816_x297349746}[：表示当前线路处于后向拆线状态]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RELEASEGUARD]{lang="EN-US"}]{#struct_0_17473_x5816_x1822225323}[：表示当前线路处于后向释放监控状态]{lang="EN-US" style="font-family:宋体"}

[[Invalid register signal.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x672682289}

[[记发器信令无效]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_555607257}

[[Failed to allocate memory to R2 CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1844827435}

[[给]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x2057606374}[R2]{lang="EN-US" style="font-size:9.0pt"}[控制块分配内存失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to initialize R2 CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x122732312}

[[初始化]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1183126862}[R2]{lang="EN-US" style="font-size:9.0pt"}[控制块数据失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get free time slot.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555541721}

[[获取空闲线路时隙失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x527113132}

[[Received an unexpected message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1811111590}

[[收到了无效的消息]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_555476185}

[[Called number length exceed length limit.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_280731675}

[[被叫号码长度超过了长度限制]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x780206089}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging voice r2 event]{lang="EN-US"}]{#struct_0_17473_x5816_x1760809611}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x544042035}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x819867030}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1862420413}

[[R2 \--\> CMC: *message-type*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555410649}

[[R2 ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1802262610}[模块给]{style="font-size:9.0pt;font-family:宋体"}[CMC ]{lang="EN-US" style="font-size:9.0pt"}[模块发送]{style="font-size:9.0pt;
  font-family:宋体"}[ *[message-type ]{lang="EN-US"}*]{style="font-size:9.0pt"}[消息]{style="font-size:9.0pt;
  font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1338230027}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x1499780054}[：表示入局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x1564768056}[：表示出局端对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x1834868707}[：表示出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_RELEASE_COMPLETE]{lang="EN-US"}]{#struct_0_17473_x5816_555869401}[：表示出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送完成拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_x1248181657}[：表示出局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_489143654}[：表示出局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CHANNEL_READY]{lang="EN-US"}]{#struct_0_17473_x5816_x1642320536}[：表示出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送媒体通道准备就绪信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_779874510}[：表示出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[CMC \--\> R2: *message-type*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555803865}

[[CMC ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_308263137}[模块给]{style="font-size:9.0pt;font-family:宋体"}[R2]{lang="EN-US" style="font-size:9.0pt"}[模块发送]{style="font-size:9.0pt;
  font-family:宋体"}*[message-type]{lang="EN-US" style="font-size:9.0pt"}*[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x868817966}[ ]{lang="EN-US" style="font-size:9.0pt"}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_2006012419}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给出局端发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x142725580}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端发送拆线信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_555345110}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给入局端发送建立新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_x18833419}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给入局端发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_x726264066}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给入局端发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_1287269955}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给出]{lang="EN-US" style="font-family:宋体"}[(]{lang="EN-US"}[入]{lang="EN-US" style="font-family:宋体"}[)]{lang="EN-US"}[局端发送]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令]{lang="EN-US" style="font-family:宋体"}

[[R2 \--\> DRV: *command-type*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_717113210}

[[R2 ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555279574}[模块给驱动下发命令字]{style="font-size:9.0pt;font-family:宋体"}

[*[command-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_1140575664}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_INSTALL ]{lang="EN-US"}]{#struct_0_17473_x5816_x2074548900}[：表示给驱动下发安装呼叫准备工作的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_MFC_DETECT_ON ]{lang="EN-US"}]{#struct_0_17473_x5816_1611346721}[：表示给驱动下发打开检测]{lang="EN-US" style="font-family:宋体"}[MFC]{lang="EN-US"}[信令的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_TONE_GEN_ON ]{lang="EN-US"}]{#struct_0_17473_x5816_x435294597}[：表示给驱动下发打开播放提示音的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_RECEIVE_GAIN ]{lang="EN-US"}]{#struct_0_17473_x5816_555214038}[：表示给驱动下发设置输入增益的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_EC_ON ]{lang="EN-US"}]{#struct_0_17473_x5816_x1602087947}[：表示给驱动下发打开回波抵消的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_EC_OFF ]{lang="EN-US"}]{#struct_0_17473_x5816_1966538445}[：表示给驱动下发关闭回波抵消的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_TRANSMIT_GAIN ]{lang="EN-US"}]{#struct_0_17473_x5816_111586893}[：表示给驱动下发设置输出增益的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_DTMF_DETECT_OFF ]{lang="EN-US"}]{#struct_0_17473_x5816_555148502}[：表示给驱动下发关闭]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[信令检测的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_MFC_DETECT_OFF ]{lang="EN-US"}]{#struct_0_17473_x5816_x297349749}[：表示给驱动下发关闭]{lang="EN-US" style="font-family:宋体"}[MFC]{lang="EN-US"}[信令检测的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_UNINSTALL ]{lang="EN-US"}]{#struct_0_17473_x5816_x1821635499}[：表示给驱动下发卸载呼叫准备的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_CAS_LINESIG ]{lang="EN-US"}]{#struct_0_17473_x5816_x1703559748}[：表示给驱动下发各种线路信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_COM_TONE_GEN_OFF ]{lang="EN-US"}]{#struct_0_17473_x5816_555607254}[：表示给驱动下发关闭播放提示音的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_MFC_GEN_ON ]{lang="EN-US"}]{#struct_0_17473_x5816_x1844827438}[：表示给驱动下发打开接收]{lang="EN-US" style="font-family:宋体"}[MFC]{lang="EN-US"}[信令的开关]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_COM_MFC_GEN_OFF ]{lang="EN-US"}]{#struct_0_17473_x5816_x2010552207}[：表示给驱动下发关闭接收]{lang="EN-US" style="font-family:宋体"}[MFC]{lang="EN-US"}[信令的开关]{lang="EN-US" style="font-family:宋体"}

[[DRV \--\> R2: *event-type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1250773545}

[[驱动给]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_555541718}[ R2]{lang="EN-US" style="font-size:9.0pt"}[模块上报的事件]{style="font-size:9.0pt;font-family:宋体"}

[*[event-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_1046864971}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE_EVENT_COM_INSTALL_ACK ]{lang="EN-US"}]{#struct_0_17473_x5816_x1836093337}[：表示驱动给出局端上报安装呼叫准备结果的事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_EVENT_COM_DTMF_ACK ]{lang="EN-US"}]{#struct_0_17473_x5816_413366230}[：表示驱动给出局端上报接收到了]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[被叫号码的应答事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE_EVENT_E1T1_SUB_CAS_LINESIG ]{lang="EN-US"}]{#struct_0_17473_x5816_555476182}[：表示驱动上报的用户线路信令事件]{lang="EN-US" style="font-family:宋体"}

[[Set reg status to *stage-type* successfully.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_280731670}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x780206084}[ MFC]{lang="EN-US" style="font-size:9.0pt"}[方式下，把记发器]{style="font-size:9.0pt;font-family:宋体"}[REG]{lang="EN-US" style="font-size:9.0pt"}[的状态设置为]{style="font-size:9.0pt;font-family:
  宋体"}*[stage-type]{lang="EN-US" style="font-size:9.0pt"}*[阶段]{style="font-size:9.0pt;font-family:宋体"}

[*[stage-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_555410646}[ ]{lang="EN-US" style="font-size:9.0pt"}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_REG_STAGE_SEND_CALLEDNUMBER ]{lang="EN-US"}]{#struct_0_17473_x5816_1802262601}[：表示出局端发送被叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_REG_STAGE_SEND_CALLERNUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_x1338295562}[：表示出局端发送主叫号码]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_REG_STAGE_OVER_CALLERNUMBER ]{lang="EN-US"}]{#struct_0_17473_x5816_x376034358}[：表示出局端把主叫号码发送完毕]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_REG_STAGE_SEND_BILLINGCATEGORY]{lang="EN-US"}]{#struct_0_17473_x5816_555869398}[：表示出局端处于发送计费业务类别阶段]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_REG_STAGE_WAIT_CALLEDNUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_1053734649}[：表示入局端处于等待接收被叫号码阶段]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_REG_STAGE_WAIT_CALLERNUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_x704425400}[：表示入局端处于等待接收主叫号码阶段]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_REG_STAGE_WAIT_BILLINGCATEGORY]{lang="EN-US"}]{#struct_0_17473_x5816_555803862}[：表示入局端处于等待接收计费业务类别阶段]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[debugging voice r2 fsm]{lang="EN-US"}]{#struct_0_17473_x5816_308263142}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x542010707}[[字段]{style="font-size:10.0pt;font-family:黑体"}]{#struct_0_17473_x5816_x59513905}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1050938409}

[[The *event-type* event processed in *state-type* state.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x221394750}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x957469040}[ *[state-type ]{lang="EN-US"}*]{style="font-size:9.0pt"}[状态下，处理]{style="font-size:9.0pt;
  font-family:宋体"}*[event-type ]{lang="EN-US" style="font-size:9.0pt"}*[事件]{style="font-size:9.0pt;font-family:宋体"}

[[ *event-type* ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555345111}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_x18833418}[：表示新呼叫发起]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x726264067}[：表示安装新呼叫准备工作的应答事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_1287335491}[：表示回铃音事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_x844382571}[：表示建立通话连接事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_1878665150}[：表示通话拆线事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_ACCP_INFORMATION]{lang="EN-US"}]{#struct_0_17473_x5816_555279575}[：表示通话中收到]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[消息事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_DL_TKO_SEIZURE_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_1140575663}[：表示出局端的线路占用信令应答事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_DL_TKO_ANSWER]{lang="EN-US"}]{#struct_0_17473_x5816_x2074483364}[：表示出局端的线路接通回应事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_DL_TKO_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_195788955}[：表示出局端的线路拆线事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_DL_TKO_CLEAR_BACK]{lang="EN-US"}]{#struct_0_17473_x5816_906318921}[：表示出局端的后向主动拆线事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_DL_TKI_SEIZURE]{lang="EN-US"}]{#struct_0_17473_x5816_555214039}[：表示入局端的线路占用信令事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_DL_TKI_CLEAR_FORWARD]{lang="EN-US"}]{#struct_0_17473_x5816_x1602087948}[：表示入局端的线路前向拆线事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_REG_TKO_END_SUCCESS]{lang="EN-US"}]{#struct_0_17473_x5816_x406114550}[：表示出局端记发器拨号正确结束事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_REG_TKO_END_BUSY]{lang="EN-US"}]{#struct_0_17473_x5816_1104331592}[：表示出局端记发器因入局端线路忙，结束]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_REG_TKO_END_NULLNUMBER]{lang="EN-US"}]{#struct_0_17473_x5816_1315412129}[：表示出局端记发器因被叫号码为空号，错误结束]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_REG_TKI_END_SUCCESS]{lang="EN-US"}]{#struct_0_17473_x5816_555148503}[：表示入局端记发器收到完整被叫号码，正确结束]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_REG_TKI_END_NULLNUM]{lang="EN-US"}]{#struct_0_17473_x5816_x297349748}[：表示入局端记发器收到非法号码，错误终止]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_NOTIFY_REG_START]{lang="EN-US"}]{#struct_0_17473_x5816_x1821569963}[：表示发送启动记发器信令事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_NOTIFY_DTMF_START]{lang="EN-US"}]{#struct_0_17473_x5816_x721367338}[：表示发送启动]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[拨号事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_NO_RECEIVED_ANSWER]{lang="EN-US"}]{#struct_0_17473_x5816_555607255}[：表示出局端未收到入局端的接通回应事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_RECEIVED_ANSWER]{lang="EN-US"}]{#struct_0_17473_x5816_x1844827437}[：表示出局端收到了入局端的接通回应事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_RECEIVED_ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_1074561508}[：表示出局端收到了入局端的建立通话连接事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_NO_RECEIVED_ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_809091017}[：表示出局端未收到入局端的建立通话连接事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_RING_TIMEOUT]{lang="EN-US"}]{#struct_0_17473_x5816_1355445090}[：表示出局端接收回铃音超时事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R2_CTL_EVENT_DTMF_TKO_END]{lang="EN-US"}]{#struct_0_17473_x5816_555541719}[：表示出局端停止拨号]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R2_CTL_EVENT_DTMF_TKI_END]{lang="EN-US"}]{#struct_0_17473_x5816_1046864972}[：表示入局端停止收号]{lang="EN-US" style="font-family:宋体"}

[*[state-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1835896729}[ ]{lang="EN-US" style="font-size:9.0pt"}[取值上一栏已列举]{style="font-size:9.0pt;font-family:宋体"}

[[表1-14 ]{lang="EN-US"}[debugging voice r2 info]{lang="EN-US"}]{#struct_0_17473_x5816_x723789835}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x543005875}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1158879978}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_555476183}

[[Succeed in deleting R2 CCB.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_280731669}

[[删除]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1558446083}[呼叫控制块]{style="font-size:9.0pt;font-family:宋体"}[CCB]{lang="EN-US" style="font-size:9.0pt"}[成功]{style="font-size:9.0pt;
  font-family:宋体"}

[[Succeed in creating R2 CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1915185394}

[[创建]{style="font-size:9.0pt;font-family:
  宋体"}]{#struct_0_17473_x5816_21717712}[呼叫控制块]{style="font-size:9.0pt;font-family:宋体"}[CCB]{lang="EN-US" style="font-size:9.0pt"}[成功]{style="font-size:9.0pt;
  font-family:宋体"}

[[No call in current timeslot.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2060013489}

[[当前线路时隙上没有电话呼叫，即空闲状态]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_555410647}

[[Succeed in creating and initializing R2 CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1802262600}

[[成功创建并初始化呼叫控制块]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1338230026}[CCB]{lang="EN-US" style="font-size:
  9.0pt"}

[[Time slot blocked by local commands.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1229103301}

[[当前线路时隙，由本地配置的命令所阻塞]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1144745582}

[[Succeed in releasing the time slot.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_555869399}

[[成功释放时隙资源]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1053734650}

[ ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[debugging voice r2 timer]{lang="EN-US"}]{#struct_0_17473_x5816_x703966647}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x549223283}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1393875704}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1650636150}

[*[timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1381799639}[ timed out.]{lang="EN-US" style="font-size:9.0pt"}

[[定时器超时]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x168756603}

[*[timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_555803863}[ ]{lang="EN-US" style="font-size:9.0pt"}[取值为：]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CTL_DTMF_DELAY_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_308263143}[：延时]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[拨号定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CTL_RING_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_x59513906}[：播放回铃音定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DL_TAKE_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_1050938412}[：线路占用定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DL_TAKEACK_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_x221067069}[：线路占用应答定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DL_HANGUP_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_1375701975}[：线路挂起定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[REG_GROUP_I_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_2121429055}[：记发器前向]{lang="EN-US" style="font-family:宋体"}[ I ]{lang="EN-US"}[组信令定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[REG_GROUP_II_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_x1459273389}[：记发器前向]{lang="EN-US" style="font-family:宋体"}[ II ]{lang="EN-US"}[组信令定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[REG_GROUP_A_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_x1751687148}[：记发器后向]{lang="EN-US" style="font-family:宋体"}[ A ]{lang="EN-US"}[组信令定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[REG_GROUP_B_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_1656663145}[：记发器后向]{lang="EN-US" style="font-family:宋体"}[ B ]{lang="EN-US"}[组信令定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[REG_END_TIMER ]{lang="EN-US"}]{#struct_0_17473_x5816_x970864903}[：记发器拨号结束定时器]{lang="EN-US" style="font-family:宋体"}

[[Succeed in starting the timer *timer-type*. Timer ID = *timerID*, Timer length = *length* ms.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121363519}

[[启动定时器，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_530023564}[定时器类型为]{style="font-size:9.0pt;font-family:
  宋体"}[ *[timer-type]{lang="EN-US"}*]{style="font-size:9.0pt"}[，定时器标识为]{style="font-size:9.0pt;font-family:宋体"}[ *[timerID]{lang="EN-US"}*]{style="font-size:
  9.0pt"}*[，]{style="font-size:9.0pt;font-family:宋体"}*[定时器时长为]{style="font-size:
  9.0pt;font-family:宋体"}[ *[length]{lang="EN-US"}*[ ]{lang="EN-US"}]{style="font-size:9.0pt"}[毫秒。]{style="font-size:9.0pt;font-family:宋体"}*[timer-type ]{lang="EN-US" style="font-size:9.0pt"}*[取值上一栏已列举]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to start the timer *timer-type*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1295099349}

[[启动定时器失败，定时器类型为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_299540943}[ timer-type, timer-type ]{lang="EN-US" style="font-size:
  9.0pt"}[取值上一栏已列举]{style="font-size:9.0pt;
  font-family:宋体"}

[[Succeed in deleting the timer. TimerID = *timerID*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1694289088}

[[删除定时器，定时器的标识为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1390423989}[ *[timerID]{lang="EN-US"}*]{style="font-size:9.0pt"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17473_x5816_2121297983}

[[\# ]{lang="EN-US"}]{#struct_0_17473_x5816_1715909258}[主叫方采用]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式拨打被叫方电话]{style="font-family:宋体"}[2222]{lang="EN-US"}[。打开主叫侧]{style="font-family:宋体"}[R2]{lang="EN-US"}[事件类型的调试信息输出开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging vioce r2 event]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_17473_x5816_x549702595}

[[\*May 18 20:56:16:922 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_608708673}

[R2_EVENT\[D-Invalid\]: CMC \--\> R2: ACCP_SETUP.]{lang="EN-US"}

[*[// CMC]{lang="EN-US"}*]{#struct_0_17473_x5816_1252803366}*[向]{style="font-family:宋体"}[R2]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_SETUP]{lang="EN-US"}[消息]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[[\*May 18 20:56:16:924 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x851392962}

[R2_INFO\[D-6/0:1.0\]: Succeed in creating R2 CCB.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_761268472}*[创建]{style="font-family:宋体"}[R2]{lang="EN-US"}[控制块成功]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:925 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121232447}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_ACCP_SETUP event processed in R2_CTL_STATE_IDLE state.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_142610511}*[在]{style="font-family:宋体"}[R2_CTL_STATE_IDLE ]{lang="EN-US"}[空闲状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_ACCP_SETUP ]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:925 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1866082831}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE \_COM_INSTALL.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_753452771}*[给驱动下发安装新呼叫准备工作的命令字]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:926 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x653025985}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[CTL_VI_INSTALL_TIMER\]. Timer ID = 0x0, Timer length = 3000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_488876693}*[启动]{style="font-family:宋体"}[R2 ]{lang="EN-US"}[等待驱动安装新呼叫准备应答的定时器，]{style="font-family:宋体"}[timerID = 0]{lang="EN-US"}[，]{style="font-family:宋体"}[timerLen = 3 s]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:927 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_336677895}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_IDLE to R2_CTL_STATE_OUT_INIT.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121691199}*[模块的状态由]{style="font-family:宋体"}[R2_CTL_STATE_IDLE  ]{lang="EN-US"}[空闲状态变为]{style="font-family:宋体"}[R2_CTL_STATE_OUT_INIT ]{lang="EN-US"}[出局端初始化状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:932 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_113482805}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_VI_INSTALL_ACK event processed in R2_CTL_STATE_OUT_INIT state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_1159379182}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_INIT ]{lang="EN-US"}[出局端初始化状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_VI_INSTALL_ACK ]{lang="EN-US"}[收到驱动上报的安装结果的应答事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:932 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1742361961}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_2038675605}*[删除等待驱动上报]{style="font-family:宋体"}[ INSTALL_ACK]{lang="EN-US"}[事件的定时器，]{style="font-family:宋体"}[timerID = 0]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:933 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x44121643}

[R2_EVENT\[O-6/0:1.0\]: DRV \--\> R2: VOICE_EVENT_COM_INSTALL_ACK. The Result: SUCCESS.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x570665721}*[驱动给]{style="font-family:宋体"}[R2 ]{lang="EN-US"}[上报]{style="font-family:宋体"}[ INSTALL \_ACK ]{lang="EN-US"}[事件，结果：安装成功，新呼叫准备就绪]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:933 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121625663}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> CMC: ACCP_SETUP_ACK.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x228079150}*[给出局端的]{style="font-family:宋体"} [CMC ]{lang="EN-US"}[模块应答]{style="font-family:宋体"}[ ACCP_SETUP_ACK ]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:934 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1553340898}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_CTL_SEIZURE event processed in R2_DL_STATE_IDLE state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x770824918}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_IDLE ]{lang="EN-US"}[空闲状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_CTL_SEIZURE ]{lang="EN-US"}[线路占用事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:935 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1890331281}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE_CAS_LINESIG \[Seizure\].]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_1539990073}*[给驱动下发线路信令，信令为：]{style="font-family:宋体"}[Seizure]{lang="EN-US"}[占用信令]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:936 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2144867320}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[DL_TAKE_TIMER\]. Timer ID = 0x0, Timer length = 1000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_408153928}*[启动线路占用定时器，]{style="font-family:宋体"}[ timerID = 0]{lang="EN-US"}[，]{style="font-family:宋体"}[ timerLen = 1000 ms]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:936 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121560127}

[R2_FSM\[O-6/0:1.0\]: The state of DL module changes from R2_DL_STATE_IDLE to R2_DL_STATE_TAKE.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_1698899840}*[模块的状态由]{style="font-family:宋体"}[R2_DL_STATE_IDLE ]{lang="EN-US"}[线路空闲变为]{style="font-family:宋体"}[R2_DL_STATE_TAKE ]{lang="EN-US"}[线路占用状态]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*May 18 20:56:16:937 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1582023115}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_OUT_INIT to R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1575421176}*[模块的状态由]{style="font-family:宋体"}[R2_CTL_STATE_OUT_INIT ]{lang="EN-US"}[初始化状态变为]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK ]{lang="EN-US"}[等待线路占用应答状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:993 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1418912963}

[R2_EVENT\[O-6/0:1.0\]: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG \[1101\].]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_282860234}*[收到驱动上报的用户线路信令，信令值为：]{style="font-family:宋体"}[ 1101]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\*May 18 20:56:16:994 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x103608101}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_TAKE state.]{lang="EN-US"}

[*[// DL]{lang="EN-US"}*]{#struct_0_17473_x5816_x1685809540}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_TAKE ]{lang="EN-US"}[线路占用的状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_SIGNALFROMDRV ]{lang="EN-US"}[来自驱动上报的用户线路信令事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:995 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121494591}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_SEIZUREACKSIGNAL event processed in R2_DL_STATE_TAKE state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1411230352}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_TAKE ]{lang="EN-US"}[线路占用状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_SEIZUREACKSIGNAL ]{lang="EN-US"}[线路占用应答事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:995 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1869167754}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1133044024}*[删除线路占用定时器，]{style="font-family:宋体"}[timerID = 0]{lang="EN-US"}*

*[ ]{lang="EN-US" style="font-size:9.0pt"}*

[[\*May 18 20:56:16:996 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1016315215}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[DL_TAKEACK_TIMER\]. Timer ID = 0x0, Timer length = 60000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x794202179}*[启动]{style="font-family:宋体"}[DL_TAKEACK_TIMER ]{lang="EN-US"}[线路占用应答定时器，]{style="font-family:宋体"}[timerID = 0]{lang="EN-US"}[，]{style="font-family:宋体"}[timerLen = 60 s]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:996 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_91765831}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_DL_TKO_SEIZURE_ACK event processed in R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121953343}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK ]{lang="EN-US"}[等待线路占用应答状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_DL_TKO_SEIZURE_ACK ]{lang="EN-US"}[出局端收到线路占用应答的事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:16:997 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1666876387}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[CTL_DTMF_DELAY_TIMER\]. Timer ID = 0x1, Timer length = 50.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_908004973}*[启动]{style="font-family:宋体"}[CTL_DTMF_DELAY_TIMER ]{lang="EN-US"}[延时]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[拨号定时器，]{style="font-family:宋体"}[ timerID = 1]{lang="EN-US"}[，]{style="font-family:宋体"}[timerLen = 50 ms]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[\*May 18 20:56:16:998 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1266312382}

[R2_FSM\[O-6/0:1.0\]: The state of DL module changes from R2_DL_STATE_TAKE to R2_DL_STATE_TAKEACK.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1145160419}*[模块由]{style="font-family:宋体"}[R2_DL_STATE_TAKE ]{lang="EN-US"}[线路占用状态变为]{style="font-family:宋体"}[R2_DL_STATE_TAKEACK ]{lang="EN-US"}[线路占用应答状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:017 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x2017360180}

[R2_TIMER\[O-6/0:1.0\]: CTL_DTMF_DELAY_TIMER timed out.]{lang="EN-US"}

[*[// CTL_DTMF_DELAY_TIMER ]{lang="EN-US"}*]{#struct_0_17473_x5816_x492065107}*[延时]{style="font-family:
宋体"}[DTMF]{lang="EN-US"}[拨号定时器超时，超时后开始使用]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式发送被叫号码]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:017 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121887807}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x233918020}*[删除延时]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[拨号定时器，]{style="font-family:宋体"}[ timerID = 1]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:018 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1739425742}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_NOTIFY_DTMF_START event processed in R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1461334645}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK ]{lang="EN-US"}[出局端等待线路占用应答的状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_NOTIFY_DTMF_START ]{lang="EN-US"}[通知启动]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[模块事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:018 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x609833817}

[R2_FSM\[O-6/0:1.0\]: The R2_DTMF_EVENT_CTL_TKO_START event processed in R2_DTMF_STATE_IDLE state.]{lang="EN-US"}

[*[// DTMF ]{lang="EN-US"}*]{#struct_0_17473_x5816_14974283}*[模块在]{style="font-family:宋体"}[R2_DTMF_STATE_IDLE ]{lang="EN-US"}[空闲状态下，处理]{style="font-family:宋体"} [R2_DTMF_EVENT_CTL_TKO_START ]{lang="EN-US"}[出局端启动]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[模块的事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:019 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1411621908}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE_COM_DTMF_GEN. Dtmf: 2222]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1048670136}*[给驱动下发]{style="font-family:宋体"}[ DTMF ]{lang="EN-US"}[信号，也就是被叫号码]{style="font-family:宋体"}[ 2222]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:020 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121429056}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[DTMF_WAIT_TIMER\]. Timer ID = 0x1, Timer length = 10000.]{lang="EN-US"}

[\*May 18 20:56:17:020 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}

[R2_FSM\[O-6/0:1.0\]: The state of DTMF module changes from R2_DTMF_STATE_IDLE to R2_DTMF_STATE_WAIT.]{lang="EN-US"}

[*[// DTMF]{lang="EN-US"}*]{#struct_0_17473_x5816_x1459207853}*[模块由]{style="font-family:宋体"}[R2_DTMF_STATE_IDLE]{lang="EN-US"}[空闲状态变为]{style="font-family:宋体"}[R2_DTMF_STATE_WAIT]{lang="EN-US"}[等待]{style="font-family:宋体"}[ DTMF ]{lang="EN-US"}[消息的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:021 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1903838100}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK to R2_CTL_STATE_OUT_WAIT_DTMF_END.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_992274117}*[模块由]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_SEIZURE_ACK ]{lang="EN-US"}[等待线路占用应答的状态变为]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_DTMF_END ]{lang="EN-US"}[结束等待]{style="font-family:宋体"}[ DTMF]{lang="EN-US"}[消息]{style="font-family:宋体"}* *[的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:983 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_492750377}

[R2_EVENT\[O-6/0:1.0\]: DRV \--\> R2: VOICE_EVENT_COM_DTMF_ACK. Result = Success.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1454406870}*[驱动给]{style="font-family:宋体"}[ R2 ]{lang="EN-US"}[上报]{style="font-family:宋体"}[VOICE_EVENT_COM_DTMF_ACK ]{lang="EN-US"}[发送]{style="font-family:
宋体"}[DTMF ]{lang="EN-US"}[消息应答的事件，]{style="font-family:宋体"}* *[结果：成功发送被叫号码]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:983 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x278828824}

[R2_FSM\[O-6/0:1.0\]: The R2_DTMF_EVENT_DTMF_ACK event processed in R2_DTMF_STATE_WAIT state.]{lang="EN-US"}

[*[// DTMF ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121363520}*[模块在]{style="font-family:宋体"}[R2_DTMF_STATE_WAIT ]{lang="EN-US"}[等待]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[消息状态下，处理]{style="font-family:宋体"}[R2_DTMF_EVENT_DTMF_ACK ]{lang="EN-US"}[收到]{style="font-family:宋体"}[ DTMF_ACK]{lang="EN-US"}[的事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:984 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_530482319}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 18 20:56:17:984 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_DTMF_TKO_END event processed in R2_CTL_STATE_OUT_WAIT_DTMF_END state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x760111910}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_DTMF_END ]{lang="EN-US"}[结束等待]{style="font-family:
宋体"}[DTMF ]{lang="EN-US"}[消息的状态下，处理]{style="font-family:
宋体"}[R2_CTL_EVENT_DTMF_TKO_END ]{lang="EN-US"}[发送被叫号码结束的事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:985 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1501402458}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_NO_RECEIVED_ANSWER event processed in R2_CTL_STATE_OUT_WAIT_DTMF_END state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_2111322668}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_DTMF_END ]{lang="EN-US"}[结束等待]{style="font-family:
宋体"}[ DTMF ]{lang="EN-US"}[消息的状态下，处理]{style="font-family:
宋体"}[R2_CTL_EVENT_NO_RECEIVED_ANSWER ]{lang="EN-US"}[未收到入局端发送的]{style="font-family:宋体"}[ ANSWER ]{lang="EN-US"}[信号事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:985 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x208597303}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> CMC: ACCP_ALERTING.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x2048110828}*[向出局端]{style="font-family:宋体"}[ CMC ]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[ ACCP_ALERTING ]{lang="EN-US"}[播放回铃音消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:987 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121297984}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> CMC: ACCP_CHANNEL_READY.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_1716105866}*[给]{style="font-family:宋体"}[ CMC ]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[ACCP_CHANNEL_READY ]{lang="EN-US"}[语音通道准备就绪的消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:990 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1008901412}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_DTMF_END to R2_CTL_STATE_OUT_WAIT_ANSWER.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_624199753}*[模块由]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_DTMF_END ]{lang="EN-US"}[结束等待]{style="font-family:
宋体"}[DTMF ]{lang="EN-US"}[消息的状态变为]{style="font-family:
宋体"}[R2_CTL_STATE_OUT_WAIT_ANSWER ]{lang="EN-US"}[等待入局端发]{style="font-family:宋体"}[ ANSWER ]{lang="EN-US"}[的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:17:991 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x54992914}

[R2_FSM\[O-6/0:1.0\]: The state of DTMF module changes from R2_DTMF_STATE_WAIT to R2_DTMF_STATE_IDLE.]{lang="EN-US"}

[*[// DTMF ]{lang="EN-US"}*]{#struct_0_17473_x5816_1327704865}*[模块由]{style="font-family:宋体"}[R2_DTMF_STATE_WAIT ]{lang="EN-US"}[等待]{style="font-family:宋体"}[DTMF]{lang="EN-US"}[消息的状态变为]{style="font-family:宋体"}[R2_DTMF_STATE_IDLE ]{lang="EN-US"}[空闲状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:235 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x388865767}

[R2_EVENT\[O-6/0:1.0\]: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG \[0101\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121232448}*[驱动给]{style="font-family:宋体"}[ R2 ]{lang="EN-US"}[模块上报用户线路信令，信令值为：]{style="font-family:宋体"}[ 0101]{lang="EN-US"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:236 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_142020687}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_TAKEACK state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_486427373}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_TAKEACK ]{lang="EN-US"}[线路占用应答的状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_SIGNALFROMDRV ]{lang="EN-US"}[来自驱动上报的线路信令事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:236 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1948622047}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_ANSWERSIGNAL event processed in R2_DL_STATE_TAKEACK state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x581543334}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_TAKEACK ]{lang="EN-US"}[线路占用应答的状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_ANSWERSIGNAL ]{lang="EN-US"}[收到驱动上报来的]{style="font-family:
宋体"}[ANSWER ]{lang="EN-US"}[信令事件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:237 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1916194864}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x0.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 18 20:56:21:237 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_DL_TKO_ANSWER event processed in R2_CTL_STATE_OUT_WAIT_ANSWER state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1631594636}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_ANSWER ]{lang="EN-US"}[等待入局端发]{style="font-family:
宋体"}[ANSWER]{lang="EN-US"}[信号的状态下，处理]{style="font-family:
宋体"}[R2_CTL_EVENT_DL_TKO_ANSWER ]{lang="EN-US"}[来自]{style="font-family:宋体"}[DL]{lang="EN-US"}[模块透传的]{style="font-family:宋体"}[ ANSWER ]{lang="EN-US"}[信令事件]{style="font-family:宋体"}*

*[ ]{lang="EN-US" style="font-size:9.0pt"}*

[[\*May 18 20:56:21:238 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121691200}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> CMC: ACCP_CONNECT.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1460954052}*[给]{style="font-family:宋体"}[CMC ]{lang="EN-US"}[模块发送]{style="font-family:宋体"}[ ACCP_CONNECT]{lang="EN-US"}[建立通话连接的消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:239 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1108716209}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_OUT_WAIT_ANSWER to R2_CTL_STATE_ACTIVE.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_1111094966}*[模块由]{style="font-family:宋体"}[R2_CTL_STATE_OUT_WAIT_ANSWER ]{lang="EN-US"}[等待入局端发]{style="font-family:
宋体"}[ ANSWER ]{lang="EN-US"}[信号的状态变为]{style="font-family:
宋体"}[R2_CTL_STATE_ACTIVE ]{lang="EN-US"}[已激活的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:21:240 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x232925289}

[R2_FSM\[O-6/0:1.0\]: The state of DL module changes from R2_DL_STATE_TAKEACK to R2_DL_STATE_ANSWER.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_227777529}*[模块由]{style="font-family:宋体"}[R2_DL_STATE_TAKEACK ]{lang="EN-US"}[线路占用应答的状态变为]{style="font-family:宋体"}[R2_DL_STATE_ANSWER ]{lang="EN-US"}[收到入局端发的应答的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:862 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_565216815}

[R2_EVENT\[O-6/0:1.0\]: CMC \--\> R2: ACCP_RELEASE.]{lang="EN-US"}

[*[// CMC ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1556825920}*[给]{style="font-family:宋体"}[ R2 ]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_RELEASE ]{lang="EN-US"}[前向拆线信号]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:863 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121625664}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> CMC: ACCP_RELEASE_COMPLETE.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x228537902}*[给]{style="font-family:宋体"}[ CMC ]{lang="EN-US"}[回复]{style="font-family:宋体"}[ACCP_RELEASE_COMPLETE ]{lang="EN-US"}[前向拆线完成的信号]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:864 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1572441246}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_ACCP_RELEASE event processed in R2_CTL_STATE_ACTIVE state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_1641267171}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_ACTIVE ]{lang="EN-US"}[已激活的状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_ACCP_RELEASE ]{lang="EN-US"}[收到前线拆线信令的事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:864 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_455408915}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_CTL_TKO_RELEASE event processed in R2_DL_STATE_ANSWER state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_179716165}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_ANSWER ]{lang="EN-US"}[收到入局端的应答状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_CTL_TKO_RELEASE ]{lang="EN-US"}[出局端主动拆线的信令事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:865 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_370074613}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE_CAS_LINESIG \[ClearForward\].]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121560128}*[向驱动下发线路信令命令字，即前向拆线信令]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:865 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1697916800}

[R2_TIMER\[O-6/0:1.0\]: Succeed in starting the timer \[DL_END_TIMER\]. Timer ID = 0x0, Timer length = 10000.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 18 20:56:26:866 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}

[R2_FSM\[O-6/0:1.0\]: The state of DL module changes from R2_DL_STATE_ANSWER to R2_DL_STATE_END.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1427947333}*[模块由]{style="font-family:宋体"}[R2_DL_STATE_ANSWER ]{lang="EN-US"}[收到入局端应答的状态变为]{style="font-family:宋体"}[R2_DL_STATE_END ]{lang="EN-US"}[结束占用的状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:867 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1816072404}

[R2_FSM\[O-6/0:1.0\]: The state of CTL module changes from R2_CTL_STATE_ACTIVE to R2_CTL_STATE_RELEASE.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_1654397935}*[模块由]{style="font-family:宋体"}[R2_CTL_STATE_ACTIVE ]{lang="EN-US"}[已激活的状态变为]{style="font-family:宋体"}[R2_CTL_STATE_RELEASE ]{lang="EN-US"}[主动拆线状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:873 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x829229837}

[R2_EVENT\[O-6/0:1.0\]: DRV \--\> R2: VOICE_EVENT_E1T1_SUB_CAS_LINESIG \[1001\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x2126374362}*[驱动给]{style="font-family:宋体"}[ R2 ]{lang="EN-US"}[模块上报用户线路信令，信令值为：]{style="font-family:宋体"}[ 1001]{lang="EN-US"}[，]{style="font-family:宋体"}* *[表示前向拆线]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:874 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121494592}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_SIGNALFROMDRV event processed in R2_DL_STATE_END state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1411033744}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_END ]{lang="EN-US"}[线路结束被占用的状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_SIGNALFROMDRV ]{lang="EN-US"}[来自驱动上报的前向拆线信令事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:875 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x844125016}

[R2_FSM\[O-6/0:1.0\]: The R2_DL_EVENT_RELEASEGUARDSIGNAL event processed in R2_DL_STATE_END state.]{lang="EN-US"}

[*[// DL ]{lang="EN-US"}*]{#struct_0_17473_x5816_320254715}*[模块在]{style="font-family:宋体"}[R2_DL_STATE_END ]{lang="EN-US"}[线路结束被占用的状态下，处理]{style="font-family:宋体"}[R2_DL_EVENT_RELEASEGUARDSIGNAL ]{lang="EN-US"}[后向释放监控信令事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US"}

[[\*May 18 20:56:26:875 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1503164827}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE_CAS_LINESIG \[Idle\].]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_820246072}*[给驱动下发线路信令命令字，设置其状态为]{style="font-family:宋体"}[ Idle ]{lang="EN-US"}[空闲状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:876 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1528446221}

[R2_TIMER\[O-6/0:1.0\]: Succeed in deleting the timer. TimerID = 0x0.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*May 18 20:56:26:876 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}

[R2_FSM\[O-6/0:1.0\]: The R2_CTL_EVENT_DL_TKO_RELEASE event processed in R2_CTL_STATE_RELEASE state.]{lang="EN-US"}

[*[// CTL ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121953344}*[模块在]{style="font-family:宋体"}[R2_CTL_STATE_RELEASE ]{lang="EN-US"}[前向拆线的状态下，处理]{style="font-family:宋体"}[R2_CTL_EVENT_DL_TKO_RELEASE ]{lang="EN-US"}[收到出局端主动拆线信令的事件]{style="font-family:
宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:877 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1666548707}

[R2_EVENT\[O-6/0:1.0\]: R2 \--\> DRV: VOICE_COM_UNINSTALL.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121117264}*[给驱动下发卸载命令字，即卸载新呼叫所需的底层支撑部件]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:877 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1688777309}

[R2_INFO\[O-6/0:1.0\]: Succeed in freeing the time slot.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_250533089}*[模块释放线路时隙成功]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*May 18 20:56:26:878 2023 Sysname R2/7/R2_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1251469618}

[R2_INFO\[O-6/0:1.0\]: Succeed in deleting R2 CCB.]{lang="EN-US"}

[*[// R2 ]{lang="EN-US"}*]{#struct_0_17473_x5816_x242829763}*[模块删除控制块，释放资源]{style="font-family:宋体"}*

::: {#1284434459 .myid}
[]{#_Toc404794185}[]{#struct_0_17473_x5816_x234476733}

**语音用户线 \-- 语音用户线调试命令 \-- debugging voice iva**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17473_x5816_2121887808}

[**[debugging voice iva]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x233590340}

[**[undo debugging voice iva]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **info** \| **timer** }]{lang="EN-US"}]{#struct_0_17473_x5816_x1355095432}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x798892329}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17473_x5816_585055604}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17473_x5816_1492539604}

[[network-admin]{lang="EN-US"}]{#struct_0_17473_x5816_x179028329}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17473_x5816_2032885514}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1458880173}

[**[all]{lang="EN-US"}**]{#struct_0_17473_x5816_1889842810}[：表示]{style="font-family:宋体"}[IVA]{lang="EN-US"}[（]{style="font-family:宋体"}[ISDN Voice Adapter]{lang="EN-US"}[）]{style="font-family:宋体"}[所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17473_x5816_754683187}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17473_x5816_396533749}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的事件类消息调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17473_x5816_x1389855953}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的状态机类消息调试信息开关。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_17473_x5816_x1975756966}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的信息类消息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_17473_x5816_x1101602462}[：表示]{style="font-family:宋体"}[EM]{lang="EN-US"}[的定时器消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17473_x5816_x1198867087}

[**[debugging voice iva]{lang="EN-US"}**]{#struct_0_17473_x5816_2121363517}[命令用来打开]{style="font-family:宋体"}[IVA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice iva]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IVA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IVA]{lang="EN-US"}]{#struct_0_17473_x5816_530941068}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-16 ]{lang="EN-US"}[debugging voice iva error]{lang="EN-US"}]{#struct_0_17473_x5816_899814242}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x545403219}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1228109535}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x689543487}

[[Failed to send *message-type* to cmc.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_281399351}

[[IVA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1157667209}[向]{style="font-size:9.0pt;font-family:宋体"}[CMC ]{lang="EN-US" style="font-size:9.0pt"}[模块发送消息失败]{style="font-size:9.0pt;
  font-family:宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_2121297981}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP]{lang="EN-US"}]{#struct_0_17473_x5816_1715778186}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_x559699549}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_680862475}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_572512168}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[Failed to send *command-type* to driver.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x572745889}

[[IVA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121232445}[向驱动下发命令字失败]{style="font-size:9.0pt;font-family:宋体"}

[*[command-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_142741583}[命令字类型取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE \_COM_INSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_x1889217140}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[给驱动下发装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE\_ COM_UNINSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_x1031471396}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[给驱动下发去装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE \_COM_DTMF_GEN]{lang="EN-US"}]{#struct_0_17473_x5816_1713870946}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[通过]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式给驱动下发被叫号码]{lang="EN-US" style="font-family:宋体"}

[[Received *message-type* but failed to find the CCB.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121691197}

[[IVA]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_113351733}[收到了]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[消息，但是获取相应的呼叫控制块失败]{style="font-size:9.0pt;font-family:
  宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1004816730}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK ]{lang="EN-US"}]{#struct_0_17473_x5816_x1181299373}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[模块对网络侧发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_ALERTING ]{lang="EN-US"}]{#struct_0_17473_x5816_2092202466}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_1653170862}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送呼叫建立信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_2121625661}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送释放呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[Failed to send ISDN *message-type* message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x228210222}

[[IVA]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_46399668}[向]{style="font-size:9.0pt;font-family:宋体"}[ISDN]{lang="EN-US" style="font-size:9.0pt"}[发送消息失败]{style="font-size:9.0pt;font-family:
  宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1681843332}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SETUP_REQUEST]{lang="EN-US"}]{#struct_0_17473_x5816_2121560125}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送建立新呼叫的请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ALERTING_REQUEST ]{lang="EN-US"}]{#struct_0_17473_x5816_1698768768}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送振铃请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[CONNECT_REQUEST]{lang="EN-US"}]{#struct_0_17473_x5816_838841197}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫连接请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DISCONNECT_RESPOND]{lang="EN-US"}]{#struct_0_17473_x5816_1059325229}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送释放呼叫应答信令]{lang="EN-US" style="font-family:宋体"}

[[The subscriber-line channel D is down.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1997200943}

[[语音用户线]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_2121494589}[D]{lang="EN-US" style="font-size:9.0pt"}[通道关闭了]{style="font-size:9.0pt;font-family:宋体"}

[[The physical Channel D is down.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1410706065}

[[物理]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1878714132}[D]{lang="EN-US" style="font-size:9.0pt"}[通道关闭了]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to release B channel.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x2068608418}

[[释放]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_2121953341}[B]{lang="EN-US" style="font-size:9.0pt"}[通道失败]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get interface name by index.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1666745315}

[[通过接口索引获取接口名字失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x1822909840}

[[Failed to get physical status of interface by index.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121887805}

[[通过接口索引获取接口物理状态失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x233786948}

[[Failed to get physical interface type by index.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_632617340}

[[通过接口索引获取接口物理类型失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x16550965}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-17 ]{lang="EN-US"}[debugging voice iva event]{lang="EN-US"}]{#struct_0_17473_x5816_x1061097235}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x550350099}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_2121429054}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x1459338925}

[[ IVA \--\> CMC : *Message-type* message is sent to CMC Successfully.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_852077982}

[[IVA]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_240412374}[向]{style="font-size:9.0pt;font-family:宋体"}[CMC]{lang="EN-US" style="font-size:9.0pt"}[发送消息成功]{style="font-size:9.0pt;font-family:
  宋体"}

[*[Message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x310730135}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP ]{lang="EN-US"}]{#struct_0_17473_x5816_x1561341245}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送建立新呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_SETUP_ACK ]{lang="EN-US"}]{#struct_0_17473_x5816_1385288125}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块对]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_ALERTING ]{lang="EN-US"}]{#struct_0_17473_x5816_2121363518}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_CONNECT ]{lang="EN-US"}]{#struct_0_17473_x5816_529958028}[：表示网络侧给]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送通话连接信令]{lang="EN-US" style="font-family:宋体"}

[[IVA \--\> ISDN : *Message-type* message is sent to ISDN Successfully.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1422346246}

[[IVA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1617147191}[向]{style="font-size:9.0pt;font-family:宋体"}[ISDN]{lang="EN-US" style="font-size:9.0pt"}[发送消息成功]{style="font-size:9.0pt;
  font-family:宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1062767062}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SETUP_REQUEST]{lang="EN-US"}]{#struct_0_17473_x5816_2121297982}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送建立新呼叫的请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ALERTING_REQUEST ]{lang="EN-US"}]{#struct_0_17473_x5816_1715974794}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送振铃请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[CONNECT_REQUEST]{lang="EN-US"}]{#struct_0_17473_x5816_x1738418576}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫连接请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DISCONNECT_RESPOND]{lang="EN-US"}]{#struct_0_17473_x5816_x1210065974}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[模块向]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送释放呼叫应答信令]{lang="EN-US" style="font-family:宋体"}

[[\[*ifindex*\] IVA \--\> DRV: *Command-type* command is sent to DRV.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1915996666}

[[IVA]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_398322998}[向驱动下发命令字成功]{style="font-size:9.0pt;font-family:宋体"}

[*[command-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_2121232446}[命令字类型取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE \_COM_INSTALL ]{lang="EN-US"}]{#struct_0_17473_x5816_142676047}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[给驱动下发装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[VOICE\_ COM_UNINSTALL]{lang="EN-US"}]{#struct_0_17473_x5816_455947142}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[给驱动下发去装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的命令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VOICE \_COM_DTMF_GEN ]{lang="EN-US"}]{#struct_0_17473_x5816_x1601856520}[：表示]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[通过]{lang="EN-US" style="font-family:宋体"}[DTMF]{lang="EN-US"}[方式给驱动下发被叫号码]{lang="EN-US" style="font-family:宋体"}

[[CMC \--\> IVA : Received *message-type* message from CMC.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1056340618}

[[IVA]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121691198}[收到]{style="font-size:9.0pt;font-family:宋体"}[[CMC]{lang="EN-US" style="font-size:9.0pt"}]{.TableTextChar}[消息]{style="font-size:9.0pt;font-family:宋体"}

[*[message-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_113548341}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_SETUP_ACK ]{lang="EN-US"}]{#struct_0_17473_x5816_764119345}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[模块对网络侧发起新呼叫的应答信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ACCP_ALERTING ]{lang="EN-US"}]{#struct_0_17473_x5816_28816792}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送振铃信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_CONNECT]{lang="EN-US"}]{#struct_0_17473_x5816_2121625662}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送呼叫建立信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ACCP_RELEASE]{lang="EN-US"}]{#struct_0_17473_x5816_x228144686}[：表示]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[给网络侧发送释放呼叫信令]{lang="EN-US" style="font-family:宋体"}

[[ISDN \--\> IVA : Received *message-type* message from ISDN.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_1244474977}

[[IVA]{lang="EN-US"}]{#struct_0_17473_x5816_2055500003}[收到]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送的消息]{style="font-family:宋体"}

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_1513232563}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_SETUP_IND]{lang="EN-US"}]{#struct_0_17473_x5816_2121560126}[：表示]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[向]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[发送建立新呼叫的请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_CONN_IND ]{lang="EN-US"}]{#struct_0_17473_x5816_1698834304}[：表示]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[向]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[发送呼叫连接请求信令]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[IVA_DISC_IND]{lang="EN-US"}]{#struct_0_17473_x5816_x19518960}[：表示]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[向]{lang="EN-US" style="font-family:宋体"}[IVA]{lang="EN-US"}[发送释放呼叫请求信令]{lang="EN-US" style="font-family:宋体"}

[[DRV \--\> IVA : Received *message-type* message from driver, BchIfIndex= *ifindex.*]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1831007185}

[[IVA]{lang="EN-US"}]{#struct_0_17473_x5816_2121494590}[收到驱动发送的消息，并且]{style="font-family:宋体"}[B]{lang="EN-US"}[通道的索引是]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[*[message-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1411164816}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[INSTALL_BCH_ACK]{lang="EN-US"}]{#struct_0_17473_x5816_806778056}[：表示驱动装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道成功]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[INBAND_DTMF]{lang="EN-US"}]{#struct_0_17473_x5816_1366125900}[：表示驱动获取带外传输号码成功]{style="font-family:
  宋体"}

[[Succeeded in installing channel B.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121953342}

[[装配]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_1666941923}[B]{lang="EN-US" style="font-size:9.0pt"}[通道成功]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-18 ]{lang="EN-US"}[debugging voice iva fsm]{lang="EN-US"}]{#struct_0_17473_x5816_x1765357759}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x791107347}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x158462829}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_1747257685}

[[ Change state from \[*state-type*\] to \[*state-type*\], CallID=\[*callId*\].]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_2121887806}

[[呼叫状态改变，且对应的呼叫]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_17473_x5816_x233983556}[为]{style="font-family:宋体"}*[callId]{lang="EN-US"}*

[*[state-type ]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x1771743344}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_IDLE]{lang="EN-US"}]{#struct_0_17473_x5816_x1072040993}[：表示正处于空闲状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_INCONNECTBCH ]{lang="EN-US"}]{#struct_0_17473_x5816_x103236140}[：表示正处于装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的状态]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_TALK]{lang="EN-US"}]{#struct_0_17473_x5816_x881337870}[：表示正处于通话]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IVA_CMC_RELEASING]{lang="EN-US"}]{#struct_0_17473_x5816_2121429051}[：表示正处于]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[拆线状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US" style="font-family:宋体"}

[[表1-19 ]{lang="EN-US"}[debugging voice iva info]{lang="EN-US"}]{#struct_0_17473_x5816_x1459011245}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x792271059}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x365052535}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_x834074217}

[[ Succeeded in deleting CCB, CallID= *callId.*]{lang="EN-US"}]{#struct_0_17473_x5816_x1205596350}

[[删除]{style="font-family:宋体"}[CCB(]{lang="EN-US"}]{#struct_0_17473_x5816_x165312420}[呼叫控制块]{style="font-family:宋体"}[)]{lang="EN-US"}[成功，其所对应的]{style="font-family:宋体"}[CallID(]{lang="EN-US"}[呼叫标识]{style="font-family:宋体"}[)]{lang="EN-US"}[为]{style="font-family:宋体"}[callId]{lang="EN-US"}

[[Succeeded in creating CCB, CallID= *callId.*]{lang="EN-US"}]{#struct_0_17473_x5816_2121363515}

[[创建]{style="font-family:宋体"}[CCB(]{lang="EN-US"}]{#struct_0_17473_x5816_530809996}[呼叫控制块]{style="font-family:宋体"}[)]{lang="EN-US"}[成功，其所对应的]{style="font-family:宋体"}[CallID(]{lang="EN-US"}[呼叫标识]{style="font-family:宋体"}[)]{lang="EN-US"}[为]{style="font-family:宋体"}[callId]{lang="EN-US"}

[[Failed to find CCB by CmcId \[*cmcid*\].]{lang="EN-US"}]{#struct_0_17473_x5816_x1155978153}

[[通过]{style="font-family:宋体"}[CmcId(cmc]{lang="EN-US"}]{#struct_0_17473_x5816_2083104823}[全局标识符]{style="font-family:宋体"}[)cmcid]{lang="EN-US"}[查找]{style="font-family:宋体"}[CCB(]{lang="EN-US"}[呼叫控制块]{style="font-family:宋体"}[)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to find CCB by ifIndex \[*ifIndex*\].]{lang="EN-US"}]{#struct_0_17473_x5816_x438354694}

[[通过]{style="font-family:宋体"}[ifIndex(]{lang="EN-US"}]{#struct_0_17473_x5816_x1874128945}[接口索引]{style="font-family:宋体"}[)ifIndex]{lang="EN-US"}[查找]{style="font-family:宋体"}[CCB(]{lang="EN-US"}[呼叫控制块]{style="font-family:宋体"}[)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to find CCB by IsdnId \[*isdnid*\].]{lang="EN-US"}]{#struct_0_17473_x5816_2121297979}

[[通过]{style="font-family:宋体"}[IsdnId(Isdn]{lang="EN-US"}]{#struct_0_17473_x5816_1716302461}[全局标识符]{style="font-family:宋体"}[)isdnid]{lang="EN-US"}[查找]{style="font-family:宋体"}[CCB(]{lang="EN-US"}[呼叫控制块]{style="font-family:宋体"}[)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Received an unexpected message.]{lang="EN-US"}]{#struct_0_17473_x5816_525802515}

[[收到错误的信息]{style="font-family:宋体"}]{#struct_0_17473_x5816_x1262105343}

[[The called number does not exist.]{lang="EN-US"}]{#struct_0_17473_x5816_1282703120}

[[被叫号码不存在]{style="font-family:宋体"}]{#struct_0_17473_x5816_2121232443}

[[Received called number from ISDN.]{lang="EN-US"}]{#struct_0_17473_x5816_142348367}

[[收到]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_17473_x5816_x102854358}[发送的被叫号码]{style="font-family:宋体"}

[[Succeed in sending messages to ISDN.]{lang="EN-US"}]{#struct_0_17473_x5816_249676877}

[[向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_17473_x5816_x1628723398}[进程发送消息成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[debugging voice iva timer]{lang="EN-US"}]{#struct_0_17473_x5816_929969752}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x795429203}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_2121691195}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_17473_x5816_113220661}

[[ Succeed in starting the timer \[*timer-type*\].]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1014092762}

[[启动定时器成功]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x129621003}

[*[timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_x413698507}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[TIMER_INSTALLBCH]{lang="EN-US"}]{#struct_0_17473_x5816_288192439}[：表示等待装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_CMCALERTING]{lang="EN-US"}]{#struct_0_17473_x5816_2121625659}[：表示等待]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃消息的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_CONN_IND]{lang="EN-US"}]{#struct_0_17473_x5816_x228734507}[：表示等待]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫建立请求的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_DISC_CFM]{lang="EN-US"}]{#struct_0_17473_x5816_x318492913}[：表示等待]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫释放确认消息的定时器]{lang="EN-US" style="font-family:宋体"}

[[Succeed in deleting the timer \[%s\].TimerID: *timerid.*]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_195881318}

[[成功删除定时器，]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_328910400}[定时器标识为]{style="font-size:9.0pt;font-family:
  宋体"}*[timerid]{lang="EN-US" style="font-size:9.0pt"}*

[*[Timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_2078949693}[ timed out.]{lang="EN-US" style="font-size:9.0pt"}

[[定时器超时]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_2121560123}

[*[Timer-type]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_17473_x5816_1698637696}[取值为：]{style="font-size:9.0pt;font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_INSTALLBCH]{lang="EN-US"}]{#struct_0_17473_x5816_1575537934}[：表示等待装配]{lang="EN-US" style="font-family:宋体"}[B]{lang="EN-US"}[通道的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_CMCALERTING ]{lang="EN-US"}]{#struct_0_17473_x5816_1920039787}[：表示等待]{lang="EN-US" style="font-family:宋体"}[CMC]{lang="EN-US"}[发送振铃消息的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_CONN_IND]{lang="EN-US"}]{#struct_0_17473_x5816_x553890485}[：表示等待]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫建立请求的定时器]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[TIMER_DISC_CFM]{lang="EN-US"}]{#struct_0_17473_x5816_2121494587}[：表示等待]{lang="EN-US" style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送呼叫释放确认消息的定时器]{lang="EN-US" style="font-family:宋体"}

[[Failed to get timer length]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_17473_x5816_x1410837137}

[[获取定时器时长失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_17473_x5816_x729478628}

*[ ]{lang="EN-US" style="color:blue"}*

[[【举例】]{style="font-family:黑体"}]{#struct_0_17473_x5816_675784241}

[[\# ]{lang="EN-US"}]{#struct_0_17473_x5816_x796057764}[使用]{style="font-family:宋体"}[BSV]{lang="EN-US"}[语音用户线发起呼叫，主叫号码为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，被叫号码为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，打开被叫侧]{style="font-family:宋体"}[IVA debug]{lang="EN-US"}[开关，输出调试信息如下：]{style="font-family:宋体"}

[[\<Sysname\> debugging vioce iva all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_17473_x5816_1089509849}

[[\*Mar 26 04:32:39:829 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x494319986}

[IVA_Event: ISDN \--\> IVA : Received IVA_SETUP_IND message from ISDN.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_2121953339}*[收到]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[侧发送的呼叫建立请求消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1667269604}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000000]{lang="EN-US"}

[           Rate                   :0x00000010]{lang="EN-US"}

[           enStatusType    :0x0009]{lang="EN-US"}

[           ucStatusValue   :0x0000]{lang="EN-US"}

[           ucIsComplete    :0x0001]{lang="EN-US"}

[           CalledNum        :2000]{lang="EN-US"}

[           CallerNum         :1000]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Failed to find CCB by IsdnId \[0xffff0002\].]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:830 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Create CCB succeeded, CallID=0x0001ffff]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:831 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: \[0x000001e1\] IVA \--\> DRV: VOICE_COMMON_GET_BSV_RELATED_IF command is sent to driver.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_1005593552}*[向驱动下发]{style="font-family:宋体"}[VOICE_COMMON_GET_BSV_RELATED_IF]{lang="EN-US"}[命令获取]{style="font-family:
宋体"}[B]{lang="EN-US"}[通道索引]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:
9.0pt"}

[[\*Mar 26 04:32:39:831 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121887803}

[IVA_Event: \[0x00011a01\] IVA \--\> DRV: VOICE_COMMON_GET_BSV_RELATED_IF command is sent to driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:832 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: \[0x00011a09\] IVA \--\> DRV: VOICE_COM_INSTALL command is sent to driver.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x234180164}*[向驱动下发]{style="font-family:宋体"}[VOICE_COM_INSTALL]{lang="EN-US"}[命令装配]{style="font-family:宋体"}[B]{lang="EN-US"}[通道]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:832 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1104354806}

[IVA_Fsm: Change state from \[IVA_IDLE\] to \[IVA_INCONNECTBCH\], CallID=\[0x0001ffff\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_1853399433}*[改变呼叫状态，由空闲状态切换到装配]{style="font-family:宋体"}[B]{lang="EN-US"}[通道状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:833 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_156980596}

[IVA_Timer: Create timer TIMER_INSTALLBCH succeeded.]{lang="EN-US"}

[TimerID: 0 state:IVA_INCONNECTBCH, time length:60000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: DRV \--\> IVA : Received INSTALL_BCH_ACK message from driver, BchIfIndex=0x00011a09.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_244816336}*[收到驱动装配]{style="font-family:宋体"}[B]{lang="EN-US"}[通道成功的消息]{style="font-family:宋体"}*

[[\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121429052}

[IVA_Timer: Delete timer TIMER_INSTALLBCH success.]{lang="EN-US"}

[TimerID: 0 state:IVA_INCONNECTBCH]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:860 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: Install B channel succeeded.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:861 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> ISDN : IVA_CALLPROC_REQ message is sent to ISDN Successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x1458945709}*[向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送]{style="font-family:宋体"}[IVA_CALLPROC_REQ]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:861 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_419834530}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000000]{lang="EN-US"}

[           Rate                   :0x00000000]{lang="EN-US"}

[           enStatusType    :0x0000]{lang="EN-US"}

[           ucStatusValue   :0x0000]{lang="EN-US"}

[           ucIsComplete    :0x0000]{lang="EN-US"}

[           CalledNum        :]{lang="EN-US"}

[           CallerNum         :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:862 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Succeed in sending message to ISDN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:864 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> CMC : ACCP_SETUP message is sent to CMC successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_2121363516}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送呼叫建立请求消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_530875532}

[IVA_Timer: Create timer TIMER_CMCSETUPACK succeeded.]{lang="EN-US"}

[TimerID: 0 state:IVA_INCONNECTBCH, time length:10000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Fsm: Change state from \[IVA_INCONNECTBCH\] to \[IVA_INSETUP\], CallID=\[0x0001ffff\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: CMC \--\> IVA : Received ACCP_SETUP_ACK message from CMC.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x1072342378}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送呼叫建立请求应答消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:865 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1759277667}

[IVA_Timer: Delete timer TIMER_CMCSETUPACK successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_495214946}*[删除等待]{style="font-family:宋体"}[CMC]{lang="EN-US"}[呼叫请求应答消息的定时器]{style="font-family:宋体"}*

[[TimerID: 0 state:IVA_INSETUP]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_17473_x5816_1899446248}

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:866 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121297980}

[IVA_Event: IVA \--\> CMC : ACCP_CHANNEL_READY message is sent to CMC successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_1715843722}*[向]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ACCP_CHANNEL_READY]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:866 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_643212877}

[IVA_Timer: Create timer TIMER_CMCALERTING successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_INSETUP, time length:150000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: CMC \--\> IVA : Received ACCP_ALERTING message from CMC.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x1531405298}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[发送的振铃消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2124750653}

[IVA_Timer: Delete timer TIMER_CMCALERTING successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_INSETUP]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:892 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: \[0x00011a09\] IVA \--\> DRV: VOICE_COM_TONE_GEN_ON command is sent to driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:893 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> ISDN : IVA_ALERTING_REQ message is sent to ISDN successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x134600893}*[向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送振铃消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:39:893 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121232444}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000001]{lang="EN-US"}

[           Rate                  :0x00000000]{lang="EN-US"}

[           enStatusType    :0x0000]{lang="EN-US"}

[           ucStatusValue   :0x0000]{lang="EN-US"}

[           ucIsComplete    :0x0000]{lang="EN-US"}

[           CalledNum        :]{lang="EN-US"}

[           CallerNum         :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Succeed in sending message to ISDN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Fsm: Change state from \[IVA_INSETUP\] to \[IVA_INALERT\], CallID=\[0x0001ffff\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_142807119}*[改变呼叫状态，由呼叫建立状态切换到振铃状态]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Mar 26 04:32:39:894 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121691196}

[IVA_Timer: Create timer TIMER_CMCCONNECT successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_INALERT, time length:240000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:132 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: CMC \--\> IVA : Received ACCP_CHANNEL_READY_ACK message from CMC.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:561 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: CMC \--\> IVA : Received ACCP_CONNECT message from CMC.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_113417269}*[收到]{style="font-family:宋体"}[CMC]{lang="EN-US"}[的连接建立消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:42:561 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x1957495253}

[IVA_Timer: Delete timer TIMER_CMCCONNECT success.]{lang="EN-US"}

[TimerID: 0 state:IVA_INALERT]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: \[0x00011a09\] IVA \--\> DRV: VOICE_COM_TONE_GEN_OFF command is sent to driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> ISDN : IVA_CONN_REQ message is sent to ISDN successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_970962792}*[向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送连接建立请求消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121625660}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex        :0x00011a01]{lang="EN-US"}

[           IsdnID                        :0xffff0002]{lang="EN-US"}

[           ucCapability              :0x00000001]{lang="EN-US"}

[           Rate                          :0x00000000]{lang="EN-US"}

[           enStatusType           :0x0000]{lang="EN-US"}

[           ucStatusValue           :0x0000]{lang="EN-US"}

[           ucIsComplete           :0x0000]{lang="EN-US"}

[           CalledNum               :]{lang="EN-US"}

[           CallerNum                :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Succeed in sending message to ISDN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:562 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Timer: Create timer TIMER_CONN_CFM successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_INALERT, time length:6000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:589 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: ISDN \--\> IVA : Received IVA_CONN_CFM message from ISDN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:589 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000000]{lang="EN-US"}

[           Rate                   :0x00000000]{lang="EN-US"}

[           enStatusType    :0x0000]{lang="EN-US"}

[           ucStatusValue   :0x0000]{lang="EN-US"}

[           ucIsComplete    :0x0000]{lang="EN-US"}

[           CalledNum        :]{lang="EN-US"}

[           CallerNum         :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:590 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Timer: Delete timer TIMER_CONN_CFM successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_INALERT]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:42:590 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Fsm: Change state from \[IVA_INALERT\] to \[IVA_TALK\], CallID=\[0x0001ffff\]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_2121560124}*[改变呼叫状态，由振铃状态切换到通话状态]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:45:982 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_1698703232}

[IVA_Event: CMC \--\> IVA : Received ACCP_RELEASE message from CMC.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_12057207}*[收到被叫释放呼叫消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_x824175572}

[IVA_Event: \[0x00011a09\] IVA \--\> DRV: VOICE_COM_UNINSTALL command is sent to driver.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> ISDN : IVA_DISC_REQ message is sent to ISDN successfully.]{lang="EN-US"}

[*[// IVA]{lang="EN-US"}*]{#struct_0_17473_x5816_x589782273}*[向]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[发送释放呼叫请求消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:45:983 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121494588}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000001]{lang="EN-US"}

[           Rate                  :0x00000000]{lang="EN-US"}

[           enStatusType    :0x0001]{lang="EN-US"}

[           ucStatusValue   :0x0010]{lang="EN-US"}

[           ucIsComplete    :0x0000]{lang="EN-US"}

[           CalledNum        :]{lang="EN-US"}

[           CallerNum         :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Succeed in sending message to ISDN.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Fsm: Change state from \[IVA_TALK\] to \[IVA_CMC_RELEASING\], CallID=\[0x0001ffff\]]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:45:985 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Timer: Create timer TIMER_DISC_CFM successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_CMC_RELEASING, time length:30000ms.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:46:012 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: ISDN \--\> IVA : Received IVA_DISC_CFM message from ISDN.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17473_x5816_x1410640529}*[收到]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[释放呼叫确认消息]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:9.0pt"}

[[\*Mar 26 04:32:46:012 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}]{#struct_0_17473_x5816_2121953340}

[IVA_Event: ifDChannelIndex:0x000001e1]{lang="EN-US"}

[           ifBChannelIndex:0x00011a01]{lang="EN-US"}

[           IsdnID                :0xffff0002]{lang="EN-US"}

[           ucCapability       :0x00000000]{lang="EN-US"}

[           Rate                   :0x00000000]{lang="EN-US"}

[           enStatusType    :0x0001]{lang="EN-US"}

[           ucStatusValue   :0x0010]{lang="EN-US"}

[           ucIsComplete    :0x0000]{lang="EN-US"}

[           CalledNum         :]{lang="EN-US"}

[           CallerNum         :]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Event: IVA \--\> CMC : ACCP_RELEASE_COMPLETE message is sent to CMC Successfully.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Info: Delete CCB successfully, CallID=0x0001ffff.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 26 04:32:46:013 2027 Sysname IVA/7/IVA_DEBUG: ]{lang="EN-US"}

[IVA_Timer: Delete timer TIMER_DISC_CFM successfully.]{lang="EN-US"}

[TimerID: 0 state:IVA_CMC_RELEASING]{lang="EN-US"}

[ ]{lang="EN-US" style="color:blue"}

[ ]{lang="EN-US"}
