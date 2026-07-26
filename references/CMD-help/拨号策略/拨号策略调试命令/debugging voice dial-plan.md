::: {#954037304 .myid}
[]{#_Toc404794338}[]{#struct_0_71044_x1827_795074482}

**拨号策略 \-- 拨号策略调试命令 \-- debugging voice dial-plan**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_71044_x1827_914045016}

[**[debugging voice dial-plan ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_71044_x1827_1004822776}

[**[undo debugging voice dial-plan ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_71044_x1827_1544370609}

[[【视图】]{style="font-family:黑体"}]{#struct_0_71044_x1827_x681425928}

[[用户视图]{style="font-family:宋体"}]{#struct_0_71044_x1827_1772615806}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_71044_x1827_1897435797}

[[network-admin]{lang="EN-US"}]{#struct_0_71044_x1827_1508816385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_71044_x1827_x821818337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_71044_x1827_x1142118731}

[**[all]{lang="EN-US"}**]{#struct_0_71044_x1827_1520652463}[：表示拨号策略所有消息类型的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_71044_x1827_x922542899}[：表示拨号策略的错误类型的消息调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_71044_x1827_x647894408}[：表示拨号策略的事件类消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_71044_x1827_1235959653}

[**[debugging voice dial-plan]{lang="EN-US"}**]{#struct_0_71044_x1827_416629814}[命令用来打开]{style="font-family:
宋体"}[拨号策略]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging voice dial-plan]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[拨号策略]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，拨号策略调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_71044_x1827_1160944183}

[[表1-1 ]{lang="EN-US"}[debugging voice dial-plan error]{lang="EN-US"}]{#struct_0_71044_x1827_x1241635559}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1825915109}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_71044_x1827_x783566025}
:::

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_71044_x1827_x729076222}

[[Failed to allocate memory for *object*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_x77916353}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1068398231}*[object]{lang="EN-US" style="font-size:9.0pt"}*[分配内存失败。]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为对象名，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[e]{lang="EN-US"}[ntity]{lang="EN-US"}]{#struct_0_71044_x1827_x600102725}[：语音实体]{lang="EN-US" style="font-family:宋体"}[号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[regular expression]{lang="EN-US"}]{#struct_0_71044_x1827_x945158230}[：正则表达式]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to send *type* command.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1229174178}

[[拨号策略向驱动下发]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_838754648}*[type]{lang="EN-US" style="font-size:
  9.0pt"}*[命令失败。]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[为下发驱动的命令字类型，包括：]{style="font-size:
  9.0pt;font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_VOICE_STAR]{lang="EN-US"}]{#struct_0_71044_x1827_x647726620}[：]{style="font-family:宋体"}[开启语音功能命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_BUSY_TONE_DETECT_START]{lang="EN-US"}]{#struct_0_71044_x1827_x287091252}[：]{style="font-family:宋体"}[忙音检测命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_BUSY_TONE_DETECT_STOP]{lang="EN-US"}]{#struct_0_71044_x1827_1485486236}[：]{style="font-family:宋体"}[停止忙音检测命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_BUSY_TONE_PARAM_DOWN]{lang="EN-US"}]{#struct_0_71044_x1827_269049893}[：]{style="font-family:宋体"}[忙音检测数据命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_EC_PARAM_DOWN]{lang="EN-US"}]{#struct_0_71044_x1827_x975657004}[：]{style="font-family:
  宋体"}[回波抵消命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_DTMF_AMP  DTMF]{lang="EN-US"}]{#struct_0_71044_x1827_x2023470648}[：]{style="font-family:
  宋体"}[振幅命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_DTMF_TIME]{lang="EN-US"}]{#struct_0_71044_x1827_1994078225}[：]{style="font-family:宋体"}[时长命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_CPTONE]{lang="EN-US"}]{#struct_0_71044_x1827_x900090921}[：]{style="font-family:宋体"}[提示音命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_CPTONEAMP]{lang="EN-US"}]{#struct_0_71044_x1827_2128780630}[：]{style="font-family:宋体"}[提示音振幅命令字]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VOICE_CIOCTL_FXO_MONITORING]{lang="EN-US"}]{#struct_0_71044_x1827_x800446655}[：]{style="font-family:
  宋体"}[FXO]{lang="EN-US"}[语音用户线]{style="font-family:宋体"}[检测]{lang="EN-US" style="font-family:宋体"}

[[Failed to get *type* table when *condition*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_x41100645}

[[在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1652013802}*[condition]{lang="EN-US" style="font-size:9.0pt"}*[条件下获取]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[表单失败。]{style="font-size:9.0pt;
  font-family:宋体"}*[condition]{lang="EN-US" style="font-size:9.0pt"}*[为获取的时机。]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[为表单的类型，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[entity substitution]{lang="EN-US"}]{#struct_0_71044_x1827_x1094793409}[：]{style="font-family:宋体"}[语音实体号码变换]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[call information]{lang="EN-US"}]{#struct_0_71044_x1827_x1763779347}[：]{style="font-family:宋体"}[呼叫信息]{lang="EN-US" style="font-family:宋体"}

[[Failed to get *type* entity from *module*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x2063834971}

[[从]{style="font-family:宋体"}[module]{lang="EN-US"}]{#struct_0_71044_x1827_x1430012672}[获取]{style="font-family:宋体"}[type]{lang="EN-US"}[语音实体失败。]{style="font-family:宋体"}[module]{lang="EN-US"}[为模块名，]{style="font-family:宋体"}[type]{lang="EN-US"}[为实体类型]{style="font-family:宋体"}

[[Failed to create socket, errno is *number*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_328532126}

[[创建]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_562696689}[socket]{lang="EN-US" style="font-size:9.0pt"}[失败，错误码是]{style="font-size:9.0pt;font-family:宋体"}*[number]{lang="EN-US" style="font-size:9.0pt"}*

[*[number]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1160001685}[为错误码数值]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to send *type object*  to *module*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_x20002721}

[[向]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1472639410}*[module]{lang="EN-US" style="font-size:9.0pt"}*[发送]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[类型的]{style="font-size:9.0pt;
  font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[失败。]{style="font-size:9.0pt;font-family:宋体"}*[module]{lang="EN-US" style="font-size:9.0pt"}*[为模块名，]{style="font-size:9.0pt;
  font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[为消息类型，]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待发送的对象]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to create *object*  for *module*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x508277063}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x36155766}*[module]{lang="EN-US" style="font-size:9.0pt"}*[创建]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[失败。]{style="font-size:9.0pt;
  font-family:宋体"}*[module]{lang="EN-US" style="font-size:9.0pt"}*[为模块名，]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待删除的对象]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to set *object*  for *module*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_582373732}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x434458902}*[module]{lang="EN-US" style="font-size:9.0pt"}*[设置]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[失败。]{style="font-size:9.0pt;
  font-family:宋体"}*[module]{lang="EN-US" style="font-size:9.0pt"}*[为模块名，]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待删除的对象]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to delete *object*  for *module*. ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1003387252}[颠三倒四的]{style="font-size:9.0pt;font-family:宋体"}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_320128834}*[module]{lang="EN-US" style="font-size:9.0pt"}*[删除]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[失败。]{style="font-size:9.0pt;
  font-family:宋体"}*[module]{lang="EN-US" style="font-size:9.0pt"}*[为模块名，]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待删除的对象]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to add *object*  to *module*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1524711430}

[[为]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1339548515}*[module]{lang="EN-US" style="font-size:9.0pt"}*[增加]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[失败。]{style="font-size:9.0pt;
  font-family:宋体"}*[module]{lang="EN-US" style="font-size:9.0pt"}*[为模块名，]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待增加的对象]{style="font-size:9.0pt;
  font-family:宋体"}

[[Failed to flush TLV message.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x429541039}

[[TLV]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x485853741}[消息转线性内存失败]{style="font-size:9.0pt;font-family:宋体"}

[[Invalid *module* type.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x870985521}

[*[module]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1594908851}[类型无效]{style="font-size:9.0pt;font-family:宋体"}

[[Invalid *object*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1725496103}

[[无效的对象名]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_658065957}

[[The *object*  is empty.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1168517254}

[*[object]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1333101411}[为空]{style="font-size:9.0pt;font-family:宋体"}

[*[object]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_x788684702}[为对应的对象名]{style="font-size:9.0pt;font-family:宋体"}

[[The user number does not exist.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_2011895703}

[[被叫号码不存在]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_159412162}

[[The regular expression is incomplete.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1007674356}

[[正则式不完整]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_631109135}

[[Unknown voice module ID.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_777155330}

[[未知的语音模块]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_816156568}[Id]{lang="EN-US" style="font-size:9.0pt"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging voice dial-plan event]{lang="EN-US"}]{#struct_0_71044_x1827_x448482289}[令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1801605361}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_71044_x1827_x1563482080}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_71044_x1827_290403020}

[[ The number template already exists.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x101247127}

[[号码模版已存在]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71044_x1827_1572818575}

[[The number template does not exist.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1406671779}

[[号码模版不存在]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71044_x1827_373478542}

[[The list of number template is empty.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_393070006}

[[号码模版列表为空]{lang="EN-US" style="font-family:宋体"}]{#struct_0_71044_x1827_765004990}

[[Remove the bound codec group from this entity first.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1792197689}

[[请先移除当前实体下绑定的编解码组]{style="font-family:宋体"}]{#struct_0_71044_x1827_x1233133102}

[[DPL \--\> DRV: *command*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_900334180}

[[拨号策略下发]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1694086832}*[command]{lang="EN-US" style="font-size:9.0pt"}*[给驱动]{style="font-size:9.0pt;font-family:宋体"}

[*[command]{lang="EN-US"}*]{#struct_0_71044_x1827_x1264893467}[为对应的命令字，同上]{lang="EN-US" style="font-family:宋体"}

[[The current connection number(*number1*) of entity *index* has reached max(*number2*).]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1438301150}

[[语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1353270142}*[index]{lang="EN-US" style="font-size:9.0pt"}*[的当前连接数]{style="font-size:9.0pt;font-family:宋体"}*[number1]{lang="EN-US" style="font-size:9.0pt"}*[已达最大值]{style="font-size:9.0pt;
  font-family:宋体"}*[number2]{lang="EN-US" style="font-size:9.0pt"}*

[*[index]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_117854136}[为当前实体的序号]{style="font-size:9.0pt;font-family:宋体"}

[*[number1]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1322211576}[为当前的连接数]{style="font-size:9.0pt;font-family:宋体"}

[*[number2]{lang="EN-US"}*]{#struct_0_71044_x1827_x911365954}[为当前配置的最大连接数]{lang="EN-US" style="font-family:宋体"}

[[Entity *index* is denied by call permission.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1847799826}

[[由于配置呼叫限制功能，匹配语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1315724522}*[index]{lang="EN-US" style="font-size:9.0pt"}*[的呼叫被拒绝]{style="font-size:9.0pt;
  font-family:宋体"}

[*[index]{lang="EN-US"}*]{#struct_0_71044_x1827_x1822238926}[为当前实体的序号]{style="font-family:宋体"}

[[The maximum number(*number*) of entity tags has been reached. The rest of the entities will not be selected.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x265354081}

[[已取到语音实体序号的最大值]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_2099376983}*[number]{lang="EN-US" style="font-size:
  9.0pt"}*[，其余的语音实体不会被选中]{style="font-size:9.0pt;font-family:宋体"}

[*[number]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1541616839}[为语音实体序号的最大值]{style="font-size:9.0pt;font-family:宋体"}

[[No available entity has been found.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1550022672}

[[没有找到可用的语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x956333085}

[[Access service number *number* has been found.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1692701791}

[[已发现接入服务号码]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1915296841}*[number]{lang="EN-US" style="font-size:
  9.0pt"}*

[*[number]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_x1569176943}[为接入服务号码]{style="font-size:9.0pt;font-family:宋体"}

[[Get entity *index* successfully.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_46106199}

[[成功选中语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1220205304}*[index]{lang="EN-US" style="font-size:9.0pt"}*

[[Suitable substitution rule has been found. ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1514396154}

[[InputFormat: *format*  \--\> OutputFormat: *format*  ]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_x16519552}

[[已找到匹配的变换规则]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1119721530}[:]{lang="EN-US" style="font-size:9.0pt"}

[[输入格式]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1772550270}[: *format*  \>\>  ]{lang="EN-US" style="font-size:9.0pt"}[输出格式]{style="font-size:9.0pt;font-family:宋体"}[: *format*]{lang="EN-US" style="font-size:9.0pt"}

[*[format]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_x89246624}[为变换规则的格式]{style="font-size:9.0pt;font-family:宋体"}

[[The user number has been substituted successfully.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1316294495}

[[主被叫号码已被成功变换]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x17246262}

[[No suitable substitution rule has been found. The user number has not been substituted]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_742517687}

[[未找到合适的的变换规则。用户号码没有被变换]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1812476164}

[[The user number only matches the first part of the regular expression.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_723447253}

[[用户号码只匹配正则式的前半部分]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x600168261}

[[The current connected number is 0.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x986868300}

[[ ]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1163239574}[当前已连接的（呼叫）数目为]{style="font-size:9.0pt;font-family:宋体"}[0]{lang="EN-US" style="font-size:9.0pt"}

[[Failed to update the information of entity *index*.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_246490066}

[[更新语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x763148804}*[index]{lang="EN-US" style="font-size:9.0pt"}*[的信息失败]{style="font-size:9.0pt;font-family:宋体"}

[[External initialization failed in a switch-over between master and standby.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1422359528}

[[主备倒换期间外部初始化失败]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x475247240}

[[Receive *type* event from interface *name*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_2128715094}

[[从接口]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_761055590}*[name]{lang="EN-US" style="font-size:9.0pt"}*[收到]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[事件。]{style="font-size:9.0pt;
  font-family:宋体"}*[name]{lang="EN-US" style="font-size:9.0pt"}*[为接口名，]{style="font-size:9.0pt;font-family:宋体"}*[type]{lang="EN-US" style="font-size:9.0pt"}*[为事件类型，包括：]{style="font-size:9.0pt;
  font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IF_IFMSG_ACTIVE  ACTIVE]{lang="EN-US"}]{#struct_0_71044_x1827_743983340}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IF_IFMSG_DEACTIVE  DEACTIVE]{lang="EN-US"}]{#struct_0_71044_x1827_40071480}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IF_IFMSG_DELETE  DELETE]{lang="EN-US"}]{#struct_0_71044_x1827_995407969}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IF_IFMSG_UP  UP]{lang="EN-US"}]{#struct_0_71044_x1827_x978554147}[事件]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IF_IFMSG_DOWN  DOWN]{lang="EN-US"}]{#struct_0_71044_x1827_562631153}[事件]{lang="EN-US" style="font-family:宋体"}

[[Sending request for data synchronization to MPU.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1083611030}

[[向]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1492446152}[MPU]{lang="EN-US" style="font-size:9.0pt"}[发送数据同步请求]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to get *object*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_x1784921766}

[[无法获取]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1184049065}*[object]{lang="EN-US" style="font-size:9.0pt"}*[。]{style="font-size:9.0pt;font-family:宋体"}*[object]{lang="EN-US" style="font-size:9.0pt"}*[为待获取对象名]{style="font-size:9.0pt;
  font-family:宋体"}

[[There are entities to be matched for the call.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_403392315}

[[存在可匹配当前呼叫的语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x1003452788}

[[Entity *index* stop keepalive. detection.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_1666467848}[。]{style="font-size:9.0pt;font-family:宋体"}

[[语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_x611875968}*[index]{lang="EN-US" style="font-size:9.0pt"}*[停止保活探测]{style="font-size:9.0pt;font-family:宋体"}

[*[index]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_1148399855}[为当前实体的序号]{style="font-size:9.0pt;font-family:宋体"}

[[Entity *index* start keepalive. detection.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_377576809}

[[语音实体]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_71044_x1827_1725430567}*[index]{lang="EN-US" style="font-size:9.0pt"}*[开始保活探测]{style="font-size:9.0pt;font-family:宋体"}

[*[index]{lang="EN-US" style="font-size:
  9.0pt"}*]{#struct_0_71044_x1827_x1730530471}[为当前实体的序号]{style="font-size:9.0pt;font-family:宋体"}

[[Failed to push message by MPU.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_71044_x1827_2128514184}

[[MPU]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_71044_x1827_370824462}[推送数据失败]{style="font-size:9.0pt;font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_71044_x1827_1384770963}

[[\# ]{lang="EN-US"}]{#struct_0_71044_x1827_x1295812841}[配置语音实体号]{style="font-family:宋体"}[121]{lang="EN-US"}[、]{style="font-family:宋体"}[14]{lang="EN-US"}[，两者的号码模版分别为]{style="font-family:宋体"}[121]{lang="EN-US"}[、]{style="font-family:宋体"}[14]{lang="EN-US"}[。对于号码变换组]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置规则，将号码]{style="font-family:宋体"}[121]{lang="EN-US"}[变换为]{style="font-family:宋体"}[14]{lang="EN-US"}[。在拨号策略视图下配置全局号码变换规则，绑定号码变换组]{style="font-family:宋体"}[1]{lang="EN-US"}[，使用其对被叫号码进行变换，打开拨号策略模块的所有调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging voice dial-plan all]{lang="EN-US"}]{#struct_0_71044_x1827_x1145286520}

[\<Sysname\>\*Jan 24 10:05:24:679 2014 Sysname DPL/7/DPLDBG: ]{lang="EN-US"}

[DPL_EVENT: Number substitution configured under dial-plan view is enabled.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_71044_x1827_x1198922004}*[检测到语音用户线或者语音实体视图下有号码变换规则]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 24 10:05:24:679 2014 Sysname DPL/7/DPLDBG: ]{lang="EN-US"}]{#struct_0_71044_x1827_765052240}

[DPL_EVENT: Suitable substitution rule has been found.]{lang="EN-US"}

[           Input format: 121 \--\> output format: 14.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_71044_x1827_2134319569}*[应用规则，将输入的被叫号码]{style="font-family:宋体"}[121]{lang="EN-US"}[变换为]{style="font-family:宋体"}[14]{lang="EN-US"}*

*[ ]{lang="EN-US"}*

[[\*Jan 24 10:05:24:680 2014 Sysname DPL/7/DPLDBG: ]{lang="EN-US"}]{#struct_0_71044_x1827_159346626}

[DPL_EVENT: The user number has been substituted successfully.]{lang="EN-US"}

[           Original number is 121, substituted number is 14;]{lang="EN-US"}

[           Original number type is unknown(0x00), substituted number type is unknown(0x00);]{lang="EN-US"}

[           Original numbering plan is unknown(0x00), substituted numbering plan is unknown(0x00). ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_71044_x1827_364593500}*[号码变换详细信息输出]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Jan 24 10:05:24:693 2014 Sysname DPL/7/DPLDBG: ]{lang="EN-US"}]{#struct_0_71044_x1827_187882619}

[DPL_EVENT: Get entity 14 successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_71044_x1827_x955650136}*[号码]{style="font-family:宋体"}[14]{lang="EN-US"}[成功匹配到语音实体]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}
