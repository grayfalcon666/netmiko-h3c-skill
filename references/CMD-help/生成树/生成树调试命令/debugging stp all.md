::: {#463035767 .myid}
[]{#_Toc404784415}[]{#struct_0_36352_15676_406296200}

**生成树 \-- 生成树调试命令 \-- debugging stp all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_575637938}

[**[debugging stp]{lang="EN-US"}**[ **all**]{lang="EN-US"}]{#struct_0_36352_15676_689259636}

[**[undo debugging stp all]{lang="EN-US"}**]{#struct_0_36352_15676_x607575149}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_x954976179}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_x135448761}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_741967729}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_1478057739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_x1310163953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_784085094}

[[无]{style="font-family:宋体"}]{#struct_0_36352_15676_191310684}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_575703474}

[**[debugging stp all]{lang="EN-US"}**]{#struct_0_36352_15676_x382713444}[命令用来打开生成树的所有调试信息开关。]{style="font-family:宋体"}**[undo debugging stp all]{lang="EN-US"}**[命令用来关闭生成树的所有调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树的所有调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_x1576152978}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_1696914735}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_906963442}[打开生成树的]{style="font-family:宋体"}[所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp all]{lang="EN-US"}]{#struct_0_36352_15676_x1946336356}
:::

::: {#-91971325 .myid}
[]{#_Toc127096848}[]{#_Toc404784416}[]{#struct_0_36352_15676_1325256858}

**生成树 \-- 生成树调试命令 \-- debugging stp error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_1743866607}

[**[debugging stp]{lang="EN-US"}**[ **error**]{lang="EN-US"}]{#struct_0_36352_15676_473007915}

[**[undo debugging stp error]{lang="EN-US"}**]{#struct_0_36352_15676_x214093745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_575769010}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_x1183443758}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_x2093473304}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_x894783662}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_851560565}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1971553193}

[[无]{style="font-family:宋体"}]{#struct_0_36352_15676_x1103461595}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_35323343}

[]{#OLE_LINK1}[**[debugging stp]{lang="EN-US"}[ error]{lang="EN-US"}**]{#struct_0_36352_15676_721957551}[命令用来打开生成树错误调试信息开关。]{style="font-family:宋体"}**[undo debugging stp]{lang="EN-US"}[ error]{lang="EN-US"}**[命令用来关闭生成树错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树错误调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_x710719282}

[[表1-1 ]{lang="EN-US"}[debugging stp error]{lang="EN-US"}]{#struct_0_36352_15676_575834546}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1560423342}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_x578695902}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x33988463}

[[Failed to *String1* the STP *String2* configuration database]{lang="EN-US"}]{#struct_0_36352_15676_x419295060}

[[对]{lang="EN-US" style="font-family:宋体"}]{#struct_0_36352_15676_x2059128890}[STP]{lang="EN-US"}[配置数据库进行]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}[1]{lang="EN-US"}*[操作失败]{lang="EN-US" style="font-family:宋体"}

[*[String]{lang="EN-US"}*]{#struct_0_36352_15676_62768699}*[1]{lang="EN-US"}*[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[write]{lang="EN-US"}]{#struct_0_36352_15676_66978725}[：表示写]{lang="EN-US" style="font-family:宋体"}[操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[read]{lang="EN-US"}]{#struct_0_36352_15676_x1967846662}[：表示读操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_36352_15676_62834235}[：表示删除操作]{style="font-family:宋体"}

[*[String]{lang="EN-US"}*]{#struct_0_36352_15676_x1648954831}*[2]{lang="EN-US"}*[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[region]{lang="EN-US"}]{#struct_0_36352_15676_821099299}[：表示域配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[global]{lang="EN-US"}]{#struct_0_36352_15676_63686203}[：表示全局配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN ]{lang="EN-US"}]{#struct_0_36352_15676_1552040740}[I]{lang="EN-US"}[gnore]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN Ignore]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface]{lang="EN-US"}]{#struct_0_36352_15676_1931355412}[：表示接口配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[instance]{lang="EN-US"}]{#struct_0_36352_15676_63751739}[：表示实例配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[instance]{lang="EN-US"}]{#struct_0_36352_15676_x321087233}[-]{lang="EN-US"}[on]{lang="EN-US"}[-]{lang="EN-US"}[interface]{lang="EN-US"}[：表示接口实例配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN list]{lang="EN-US"}]{#struct_0_36352_15676_1535019994}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_36352_15676_63161914}[：表示]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN-on-interface]{lang="EN-US"}]{#struct_0_36352_15676_x816087065}[：表示接口]{lang="EN-US" style="font-family:
  宋体"}[VLAN]{lang="EN-US"}[配置]{lang="EN-US" style="font-family:宋体"}

[[Failed to move database(key *String*)]{lang="EN-US"}]{#struct_0_36352_15676_218980061}

[[移动]{lang="EN-US" style="font-family:宋体"}[key]{lang="EN-US"}]{#struct_0_36352_15676_575900082}[为]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的数据库失败*，*]{lang="EN-US" style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}*[PortName]{lang="EN-US"}*

[[Failed to *String* the global *DataType* database]{lang="EN-US"}]{#struct_0_36352_15676_x1027468274}

[[对全局]{style="font-family:宋体"}[DataType]{lang="EN-US"}]{#struct_0_36352_15676_x1679958974}[数据库进行]{style="font-family:宋体"}[String]{lang="EN-US"}[操作失败]{style="font-family:宋体"}

[[String]{lang="EN-US"}]{#struct_0_36352_15676_63096378}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[write]{lang="EN-US"}]{#struct_0_36352_15676_x1334325903}[：表示写]{lang="EN-US" style="font-family:宋体"}[操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[read]{lang="EN-US"}]{#struct_0_36352_15676_62899770}[：表示]{lang="EN-US" style="font-family:宋体"}[读操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_36352_15676_x910900056}[：表示]{lang="EN-US" style="font-family:宋体"}[删除操作]{style="font-family:宋体"}

[*[DataType]{lang="EN-US"}*]{#struct_0_36352_15676_62965306}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control]{lang="EN-US"}]{#struct_0_36352_15676_561530886}[：表示]{lang="EN-US" style="font-family:宋体"}[控制数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[run]{lang="EN-US"}]{#struct_0_36352_15676_62768698}[：表示运行数据]{style="font-family:宋体"}

[[Failed to *String* the *DataType* database on instance *InstanceID*]{lang="EN-US"}]{#struct_0_36352_15676_202592582}

[[对]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}]{#struct_0_36352_15676_x641742781}[的]{style="font-family:宋体"}*[DataType]{lang="EN-US"}*[数据库进行]{style="font-family:宋体"}*[String]{lang="EN-US"}*[操作失败]{style="font-family:宋体"}

[*[String]{lang="EN-US"}*]{#struct_0_36352_15676_62834234}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[write]{lang="EN-US"}]{#struct_0_36352_15676_575965618}[：表示写]{lang="EN-US" style="font-family:宋体"}[操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[read]{lang="EN-US"}]{#struct_0_36352_15676_63686202}[：表示]{lang="EN-US" style="font-family:宋体"}[读操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_36352_15676_63751738}[：表示]{lang="EN-US" style="font-family:宋体"}[删除操作]{style="font-family:宋体"}

[*[DataType]{lang="EN-US"}*]{#struct_0_36352_15676_2017564927}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[run]{lang="EN-US"}]{#struct_0_36352_15676_63161917}[：表示运行数据]{style="font-family:宋体"}

[[Failed to *String* the *DataType* database for port*PortID(PortName)*]{lang="EN-US"}]{#struct_0_36352_15676_195254568}

[[对端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_x400040593}[的]{style="font-family:宋体"}*[DataType]{lang="EN-US"}*[数据库进行]{style="font-family:宋体"}*[String]{lang="EN-US"}*[操作失败]{style="font-family:宋体"}

[*[String]{lang="EN-US"}*]{#struct_0_36352_15676_63030845}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[write]{lang="EN-US"}]{#struct_0_36352_15676_751497333}[：表示写]{lang="EN-US" style="font-family:宋体"}[操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[read]{lang="EN-US"}]{#struct_0_36352_15676_63096381}[：表示]{lang="EN-US" style="font-family:宋体"}[读操作]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_36352_15676_x755779558}[：表示]{lang="EN-US" style="font-family:宋体"}[删除操作]{style="font-family:宋体"}

[*[DataType]{lang="EN-US"}*]{#struct_0_36352_15676_62899773}[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control]{lang="EN-US"}]{#struct_0_36352_15676_1427752104}[：表示]{lang="EN-US" style="font-family:宋体"}[控制数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[run]{lang="EN-US"}]{#struct_0_36352_15676_62965309}[：表示运行数据]{style="font-family:宋体"}

[[Failed to open database(name= *String*)]{lang="EN-US"}]{#struct_0_36352_15676_x1128886605}

[[打开数据库]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_36352_15676_x528643657}[失败，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[eSTP]{lang="EN-US"}]{#struct_0_36352_15676_574982578}[：表示生效配置数据库]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lSTP]{lang="EN-US"}]{#struct_0_36352_15676_x1887841392}[：表示本地运行数据库]{style="font-family:宋体"}

[[Received a *String* BPDU with invalid length]{lang="EN-US"}]{#struct_0_36352_15676_308646691}

[[收到一个长度错误的]{style="font-family:宋体"}*[String]{lang="EN-US"}*]{#struct_0_36352_15676_473127081}[类型报文，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STP]{lang="EN-US"}]{#struct_0_36352_15676_x925433768}[：表示生成树]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSTP]{lang="EN-US"}]{#struct_0_36352_15676_575048114}[：表示快速生成树]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVST]{lang="EN-US"}]{#struct_0_36352_15676_63686205}[：表示]{lang="EN-US" style="font-family:宋体"}[每]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[生成树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MSTP]{lang="EN-US"}]{#struct_0_36352_15676_x820207623}[：表示多实例生成树]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCN]{lang="EN-US"}]{#struct_0_36352_15676_86543385}[：表示拓扑变化通知消息]{style="font-family:宋体"}

[[The protocol type ID is wrong]{lang="EN-US"}]{#struct_0_36352_15676_x521225482}

[[报文类型错误]{style="font-family:宋体"}]{#struct_0_36352_15676_x895966500}

[[The protocol version ID is wrong]{lang="EN-US"}]{#struct_0_36352_15676_575506867}

[[报文版本错误]{style="font-family:宋体"}]{#struct_0_36352_15676_x1932412701}

[[Port *PortID(PortName)* received an error BPDU with *String*]{lang="EN-US"}]{#struct_0_36352_15676_1830584791}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_x145079787}[收到错误原因为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的报文，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid BPDU length]{lang="EN-US"}]{#struct_0_36352_15676_575572403}[：表示错误的报文长度]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid ]{lang="EN-US"}]{#struct_0_36352_15676_x1457634748}[MSTI]{lang="EN-US"}[ ]{lang="EN-US"}[information]{lang="EN-US"}[：表示错误的多实例信息]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid RemainingHops of CIST]{lang="EN-US"}]{#struct_0_36352_15676_x709449047}[：表示]{lang="EN-US" style="font-family:宋体"}[CIST]{lang="EN-US"}[错误的剩余跳数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid IntRootPathCost of CIST]{lang="EN-US"}]{#struct_0_36352_15676_x216069416}[：表示]{lang="EN-US" style="font-family:宋体"}[CIST]{lang="EN-US"}[错误的内部根路径开销]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[retired root priority]{lang="EN-US"}]{#struct_0_36352_15676_575637939}[：表示过期的根优先级]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid Root]{lang="EN-US"}]{#struct_0_36352_15676_689259635}[：表示错误的总根]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid RegionRoot]{lang="EN-US"}]{#struct_0_36352_15676_x607575148}[：表示错误的域根]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid ExtRootPathCost]{lang="EN-US"}]{#struct_0_36352_15676_x955041715}[：表示错误的外部路径开销]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[retired ]{lang="EN-US"}]{#struct_0_36352_15676_575703475}[MSTI]{lang="EN-US"}[ root priority]{lang="EN-US"}[：表示过期的多实例根优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid RootPathCost]{lang="EN-US"}]{#struct_0_36352_15676_62965308}[：表示]{lang="EN-US" style="font-family:
  宋体"}[错误的根路径开销]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid RemainingHops of ]{lang="EN-US"}]{#struct_0_36352_15676_x2114828282}[MSTI ]{lang="EN-US"}*[InstanceID]{lang="EN-US"}*[：表示错误的]{lang="EN-US" style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[剩余跳数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid IntRootPathCost of ]{lang="EN-US"}]{#struct_0_36352_15676_62768700}[MSTI ]{lang="EN-US"}*[InstanceID]{lang="EN-US"}*[：表示错误的]{lang="EN-US" style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[内部根路径开销]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Excess MessageAge]{lang="EN-US"}]{#struct_0_36352_15676_62834236}[：表示]{lang="EN-US" style="font-family:
  宋体"}[M]{lang="EN-US"}[essage]{lang="EN-US"}[A]{lang="EN-US"}[ge]{lang="EN-US"}[值过大]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid HelloTime]{lang="EN-US"}]{#struct_0_36352_15676_x1297223995}[：表示]{style="font-family:宋体"}[HelloTime]{lang="EN-US"}[值无效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid FwdDelay]{lang="EN-US"}]{#struct_0_36352_15676_1476270908}[：表示]{style="font-family:宋体"}[FwdDelay]{lang="EN-US"}[值无效]{style="font-family:宋体"}

[[BPDU's length is less than TCN\'s length]{lang="EN-US"}]{#struct_0_36352_15676_x382713443}

[[BPDU]{lang="EN-US"}]{#struct_0_36352_15676_x1576087442}[报文长度有误]{style="font-family:宋体"}

[[Port *PortID(PortName)* failed to send packet]{lang="EN-US"}]{#struct_0_36352_15676_443435581}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_575769011}[发送报文失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1183443757}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x2140527471}[打开生成树错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp error]{lang="EN-US"}]{#struct_0_36352_15676_x1435694357}

[\*Mar 18 14:28:41:744 2010 Sysname STP/7/ERROR:Port2(GigabitEthernet1/0/1) received an error BPDU with invalid Root]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_2021258467}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到错误的]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文，错误原因是报文中的根信息有误]{style="font-family:宋体"}*

::: {#1250092364 .myid}
[]{#_Toc404784417}[]{#struct_0_36352_15676_x462435345}

**生成树 \-- 生成树调试命令 \-- debugging stp event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_2063820879}

[**[debugging stp]{lang="EN-US"}**[ **event** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_575834547}

[**[undo debugging stp]{lang="EN-US"}**[ **event** \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_x578695903}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_x34053999}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_x1872811349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_x103786247}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_1059904183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_2009813382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_1247846862}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_36352_15676_x1633056974}[：打开或关闭指定端口的生成树事件调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开或关闭全局事件调试开关，和所有端口的事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_575900083}

[**[debugging stp event]{lang="EN-US"}**]{#struct_0_36352_15676_x1027468273}[命令用来打开生成树事件调试信息开关。]{style="font-family:宋体"}**[undo debugging stp event]{lang="EN-US"}**[命令用来关闭生成树事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树事件调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_1048924381}

[[表1-2 ]{lang="EN-US"}[debugging stp event]{lang="EN-US"}]{#struct_0_36352_15676_x82350005}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1591574542}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_722600254}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x199162988}

[[Instance *InstanceID* enters PRS machine]{lang="EN-US"}]{#struct_0_36352_15676_x983548828}

[[全局事件调试信息：]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}]{#struct_0_36352_15676_1453563889}[进入]{style="font-family:宋体"}[PRS]{lang="EN-US"}[状态机]{style="font-family:宋体"}

[*[String]{lang="EN-US"}*[ event occured on port*PortID(PortName)*]{lang="EN-US"}]{#struct_0_36352_15676_575965619}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_195254569}[上发生了]{style="font-family:宋体"}*[String]{lang="EN-US"}*[事件，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADD VLAN]{lang="EN-US"}]{#struct_0_36352_15676_x400040592}[：表示端口加入]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[65535]{lang="EN-US"}[表示批量]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEL VLAN]{lang="EN-US"}]{#struct_0_36352_15676_751562869}[：表示端口从]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[中删除，]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[65535]{lang="EN-US"}[表示批量]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SPEED CHANGE]{lang="EN-US"}]{#struct_0_36352_15676_x1207726263}[：表示端口速率变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DUPLEX CHANGE]{lang="EN-US"}]{#struct_0_36352_15676_2131046911}[：表示端口双工模式变化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FAST LINK DOWN]{lang="EN-US"}]{#struct_0_36352_15676_574982579}[：表示端口快速]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LINK DOWN]{lang="EN-US"}]{#struct_0_36352_15676_x1887841391}[：表示端口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LINK UP]{lang="EN-US"}]{#struct_0_36352_15676_711931218}[：表示端口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEACTIVE]{lang="EN-US"}]{#struct_0_36352_15676_x772603376}[：表示接口去激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELETE]{lang="EN-US"}]{#struct_0_36352_15676_696088414}[：表示接口删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[JOIN AGG]{lang="EN-US"}]{#struct_0_36352_15676_x717026889}[：表示端口加入聚合组]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LEAVE AGG]{lang="EN-US"}]{#struct_0_36352_15676_575048115}[：表示端口退出聚合组]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_x820207622}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_86608921}[打开]{style="font-family:宋体"}[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的生成树]{style="font-family:宋体"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp event interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_36352_15676_1693134358}

[\*Mar 18 14:28:41:887 2010 Sysname STP/7/PEVT: LINK DOWN event occured on port2(GigabitEthernet1/0/1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x752276740}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发生了端口]{style="font-family:宋体"}[down]{lang="EN-US"}[事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x1725680064}[打开生成树全局事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp event]{lang="EN-US"}]{#struct_0_36352_15676_861257965}

[\*Sep 23 09:39:24:773 2010 Sysname STP/7/PEVT: DUPLEX CHANGE event occured on port2(GigabitEthernet1/0/1).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x2144907614}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发生了双工变化事件]{style="font-family:宋体"}*

[[\*Sep 23 09:39:24:777 2010 Sysname STP/7/PEVT: SPEED CHANGE event occured on port2(GigabitEthernet1/0/1).]{lang="EN-US"}]{#struct_0_36352_15676_575506864}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x1932412704}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发生了速率变化事件]{style="font-family:宋体"}*

[[\*Sep 23 09:39:24:783 2010 Sysname STP/7/PEVT: LINK UP event occured on port2(GigabitEthernet1/0/1).]{lang="EN-US"}]{#struct_0_36352_15676_x2061097978}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x853353377}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发生了链路]{style="font-family:宋体"}[up]{lang="EN-US"}[事件]{style="font-family:宋体"}*

::: {#1602152669 .myid}
[]{#_Toc127096846}[]{#_Toc404784418}[]{#struct_0_36352_15676_x578448290}

**生成树 \-- 生成树调试命令 \-- debugging stp fsm**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_87776687}

[**[debugging stp fsm]{lang="EN-US"}**[ \[ **instance** *instance-id* \| **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_1529774393}

[**[undo]{lang="EN-US"}**[ **debugging stp** **fsm** \[ **instance** *instance-id* \| **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_881877273}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1618397838}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_575572400}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1457634745}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_x756503214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_1144558743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_x2017007609}

[**[instance]{lang="EN-US"}**[ *instance-id*]{lang="EN-US"}]{#struct_0_36352_15676_2112474865}[：打开或关闭指定]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的生成树状态机调试信息开关，]{style="font-family:宋体"}*[instance-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[到设备支持的最大值（最大值与设备的型号有关，请以设备的实际情况为准），]{style="font-family:宋体"}[0]{lang="EN-US"}[表示]{style="font-family:宋体"}[CIST]{lang="EN-US"}[。如果未指定本参数，则打开或关闭所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[的生成树状态机调试信息开关。本参数在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下无效。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_36352_15676_1629311389}[：打开或关闭指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态机调试信息开关，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，则打开所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树状态机调试信息开关。本参数只在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下有效。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_36352_15676_1601751954}[：打开或关闭指定端口的生成树状态机调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树状态机调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1321887714}

[**[debugging stp fsm]{lang="EN-US"}**]{#struct_0_36352_15676_512852416}[命令用来打开生成树状态机调试信息开关。]{style="font-family:宋体"}**[undo debugging stp fsm]{lang="EN-US"}**[命令用来关闭生成树状态机调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树状态机调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_575637936}

[[表1-3 ]{lang="EN-US"}[debugging stp fsm]{lang="EN-US"}]{#struct_0_36352_15676_689259622}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1592851726}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_1348739991}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x1708761887}

[[Instance *InstanceID*'s port *PortID(PortName)* enters *String* state]{lang="EN-US"}]{#struct_0_36352_15676_400169903}

[[VLAN *VLANID*'s port *PortID(PortName)* enters *String* state]{lang="EN-US"}]{#struct_0_36352_15676_1629114781}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_x989583069}[在]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上的状态为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[PIM%DISABLED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%AGED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%UPDATE]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%CURRENT]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%RECEIVE]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%SUPERIOR_DESIGNATED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%REPEATED_DESIGNATED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%INFERIOR_DESIGNATED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%NOT_DESIGNATED]{lang="EN-US"}[、]{style="font-family:宋体"}[PIM%OTHER]{lang="EN-US"}[、]{style="font-family:宋体"}[PPM%CHECKING_RSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[PPM%SELECTING_STP]{lang="EN-US"}[、]{style="font-family:宋体"}[PPM%SENSING]{lang="EN-US"}[；]{style="font-family:宋体"}[PRT%BLOCK_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%BACKUP_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ALTERNATE_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ALTERNATE_PROPOSED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ALTERNATE_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_PROPOSED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_SYNCED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_RETIRED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_DISCARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_LEARN]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%MASTER_FORWARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_PROPOSE]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_SYNCED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_RETIRED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_DISCARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_LEARN]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DESIGNATED_FORWARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_PROPOSED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_AGREED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_SYNCED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_DISCARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_LEARN]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_FORWARD]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_REROOT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%ROOT_REROOTED]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%INIT_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DISABLE_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PRT%DISABLED_PORT]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%PERIODIC]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%CONFIG]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%RSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%MSTP_DOT1S]{lang="EN-US"}[、]{style="font-family:宋体"}[PTX%MSTP_LEGACY]{lang="EN-US"}[、]{style="font-family:宋体"}[PST%DISCARDING]{lang="EN-US"}[、]{style="font-family:宋体"}[PST%LEARNING]{lang="EN-US"}[、]{style="font-family:宋体"}[PST%FORWARDING]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%INACTIVE]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%LEARNINGT]{lang="EN-US"}[、]{style="font-family:宋体"}[CM%DETECTED]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%ACTIVE]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%NOTIFIED_TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%NOTIFIED_TC]{lang="EN-US"}[、]{style="font-family:宋体"}[TCM%PROPAGATING]{lang="EN-US"}[和]{style="font-family:宋体"}[TCM%ACKNOLEDGED]{lang="EN-US"}[。各字段]{style="font-family:宋体"}[%]{lang="EN-US"}[之前表示状态机名称，]{style="font-family:宋体"}[%]{lang="EN-US"}[之后表示具体状态]{style="font-family:宋体"}

[[Instance *InstanceID*'s port *PortID(PortName)* is selected as *String* role]{lang="EN-US"}]{#struct_0_36352_15676_1767821362}

[[VLAN *VLANID*'s port *PortID(PortName)* is selected as *String* role]{lang="EN-US"}]{#struct_0_36352_15676_1628983709}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_575703472}[在]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上的角色为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DESIGNATED]{lang="EN-US"}]{#struct_0_36352_15676_x382713438}[：表示指定端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROOT]{lang="EN-US"}]{#struct_0_36352_15676_x1575366539}[：表示根端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ALTERNATE]{lang="EN-US"}]{#struct_0_36352_15676_1093679478}[：表示替换端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BACKUP]{lang="EN-US"}]{#struct_0_36352_15676_2029600497}[：表示备份端口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MASTER]{lang="EN-US"}]{#struct_0_36352_15676_593045402}[：表示主端口]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1571409359}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_575769008}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，打开所有]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[端口的生成树状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp fsm]{lang="EN-US"}]{#struct_0_36352_15676_1155208394}

[\*Mar 18 14:28:41:739 2010 Sysname STP/7/FSMSTATE:Instance 0\'s port2(GigabitEthernet1/0/1) enters PTX%PERIODIC state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x296170974}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PTX]{lang="EN-US"}[状态机处于]{style="font-family:宋体"}[PERIODIC]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 18 14:28:41:739 2010 Sysname STP/7/FSMSTATE:Instance 0\'s port2(GigabitEthernet1/0/1) enters PTX%MSTP_DOT1S state.]{lang="EN-US"}]{#struct_0_36352_15676_481568157}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x1708884916}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[PTX]{lang="EN-US"}[状态机处于]{style="font-family:宋体"}[MSTP_DOT1S]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 18 14:28:41:741 2010 Sysname STP/7/FSMSTATE:Instance 2\'s port2(GigabitEthernet1/0/1) is selected as MASTER role]{lang="EN-US"}]{#struct_0_36352_15676_x1995461939}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x1322402871}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[MSTI ]{lang="EN-US"}[2]{lang="EN-US"}[中被选举为主端口]{style="font-family:
宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_1629245856}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[端口的生成树状态机调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp fsm]{lang="EN-US"}]{#struct_0_36352_15676_1629311392}

[\*Mar 18 14:28:41:741 2010 Sysname STP/7/MEXS:Slot=1;VLAN 2's port105(GigabitEthernet1/0/1) enters PTX%PERIODIC state.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_1699850388}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[2]{lang="EN-US"}[上处于]{style="font-family:
宋体"}[PTX]{lang="EN-US"}[状态机中的]{style="font-family:宋体"}[PERIODIC]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Mar 18 14:28:41:741 2010 Sysname STP/7/MEXS:Slot=1;VLAN 2's port105(GigabitEthernet1/0/1) is selected as MASTER role]{lang="EN-US"}]{#struct_0_36352_15676_1629114784}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_175530316}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[2]{lang="EN-US"}[上被指定为主端口]{style="font-family:
宋体"}*

::: {#-453020650 .myid}
[]{#_Toc404784419}[]{#struct_0_36352_15676_1672227285}[]{#_Toc127096847}[]{#_Toc148517517}[]{#_Toc148610733}[]{#_Toc148517518}[]{#_Toc148610734}[]{#_Toc148517521}[]{#_Toc148610737}[]{#_Toc148517522}[]{#_Toc148610738}[]{#_Toc148517523}[]{#_Toc148610739}[]{#_Toc148517524}[]{#_Toc148610740}[]{#_Toc148517525}[]{#_Toc148610741}[]{#_Toc148517526}[]{#_Toc148610742}[]{#_Toc148517527}[]{#_Toc148610743}[]{#_Toc148517528}[]{#_Toc148610744}[]{#_Toc148517529}[]{#_Toc148610745}[]{#_Toc148517530}[]{#_Toc148610746}[]{#_Toc148517531}[]{#_Toc148610747}[]{#_Toc148517532}[]{#_Toc148610748}[]{#_Toc148517534}[]{#_Toc148610750}[]{#_Toc148517538}[]{#_Toc148610754}[]{#_Toc147113358}[]{#_Toc148517540}[]{#_Toc148610756}[]{#_Toc147113359}[]{#_Toc148517541}[]{#_Toc148610757}[]{#_Toc147113360}[]{#_Toc148517542}[]{#_Toc148610758}[]{#_Toc147113361}[]{#_Toc148517543}[]{#_Toc148610759}[]{#_Toc147113362}[]{#_Toc148517544}[]{#_Toc148610760}[]{#_Toc147113363}[]{#_Toc148517545}[]{#_Toc148610761}[]{#_Toc147113364}[]{#_Toc148517546}[]{#_Toc148610762}[]{#_Toc147113365}[]{#_Toc148517547}[]{#_Toc148610763}[]{#_Toc146534346}[]{#_Toc147113367}[]{#_Toc148517549}[]{#_Toc148610765}[]{#_Toc146534347}[]{#_Toc147113368}[]{#_Toc148517550}[]{#_Toc148610766}[]{#_Toc146534348}[]{#_Toc147113369}[]{#_Toc148517551}[]{#_Toc148610767}[]{#_Toc146534349}[]{#_Toc147113370}[]{#_Toc148517552}[]{#_Toc148610768}[]{#_Toc146534350}[]{#_Toc147113371}[]{#_Toc148517553}[]{#_Toc148610769}[]{#_Toc146534351}[]{#_Toc147113372}[]{#_Toc148517554}[]{#_Toc148610770}[]{#_Toc146534352}[]{#_Toc147113373}[]{#_Toc148517555}[]{#_Toc148610771}[]{#_Toc146534353}[]{#_Toc147113374}[]{#_Toc148517556}[]{#_Toc148610772}[]{#_Toc146534354}[]{#_Toc147113375}[]{#_Toc148517557}[]{#_Toc148610773}[]{#_Toc146534355}[]{#_Toc147113376}[]{#_Toc148517558}[]{#_Toc148610774}[]{#_Toc146534356}[]{#_Toc147113377}[]{#_Toc148517559}[]{#_Toc148610775}[]{#_Toc146534357}[]{#_Toc147113378}[]{#_Toc148517560}[]{#_Toc148610776}[]{#_Toc146534367}[]{#_Toc147113388}[]{#_Toc148517570}[]{#_Toc148610786}[]{#_Toc146534368}[]{#_Toc147113389}[]{#_Toc148517571}[]{#_Toc148610787}[]{#_Toc146534369}[]{#_Toc147113390}[]{#_Toc148517572}[]{#_Toc148610788}[]{#_Toc146534370}[]{#_Toc147113391}[]{#_Toc148517573}[]{#_Toc148610789}[]{#_Toc146534375}[]{#_Toc147113396}[]{#_Toc148517578}[]{#_Toc148610794}[]{#_Toc146534377}[]{#_Toc147113398}[]{#_Toc148517580}[]{#_Toc148610796}[]{#_Toc146534380}[]{#_Toc147113401}[]{#_Toc148517583}[]{#_Toc148610799}[]{#_Toc146534381}[]{#_Toc147113402}[]{#_Toc148517584}[]{#_Toc148610800}

**生成树 \-- 生成树调试命令 \-- debugging stp packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_575834544}

[**[debugging stp]{lang="EN-US"}**[ **packet** \[ **receive** \| **send** \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **brief** \| **verbose** \]]{lang="EN-US"}]{#struct_0_36352_15676_x578695900}

[**[undo debugging stp]{lang="EN-US"}**[ **packet** \[ **receive** \| **send** \] \[ **vlan** *vlan-id* \] \[ **interface** *interface-type interface-number* \] \[ **brief** \| **verbose** \]]{lang="EN-US"}]{#struct_0_36352_15676_x34119535}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_2040705783}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_484628829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_947704806}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_862694845}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_673772396}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_x957322457}

[**[receive]{lang="EN-US"}**]{#struct_0_36352_15676_575900080}[：打开或关闭接收生成树报文的调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_36352_15676_x1027468276}[：打开或关闭发送生成树报文的调试信息开关。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_36352_15676_1629049248}[：打开或关闭指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树报文调试信息开关，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。如果未指定本参数，则打开所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的生成树报文调试信息开关。本参数只在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下有效。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_36352_15676_1452208908}[：打开或关闭指定端口的生成树报文调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树报文调试信息开关。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_36352_15676_1342229035}[：打开或关闭生成树报文的简要调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_36352_15676_1885756808}[：打开或关闭生成树报文的详细调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_x839491513}

[**[debugging stp packet]{lang="EN-US"}**]{#struct_0_36352_15676_1643671031}[命令用来打开生成树报文调试信息开关。]{style="font-family:宋体"}**[undo debugging stp packet]{lang="EN-US"}**[命令用来关闭生成树报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树报文调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_x2041595859}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_36352_15676_x843588514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_36352_15676_575965616}**[receive]{lang="EN-US"}**[和]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，则同时打开接收和发送生成树报文的调试信息开关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_36352_15676_195254578}**[brief]{lang="EN-US"}**[和]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**[参数，则打开生成树报文的简要调试信息开关。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging stp packet]{lang="EN-US"}]{#struct_0_36352_15676_1938611567}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1591994894}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_1010737208}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x1196787361}

[[Port *PortID(PortName)* sent *Type* packet(Length:*number*)]{lang="EN-US"}]{#struct_0_36352_15676_794975200}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_190529621}[发送了类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的报文，报文的长度为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[（单位为字节），]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[STP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[MSTP-dot1s]{lang="EN-US"}[和]{style="font-family:宋体"}[MSTP-legacy]{lang="EN-US"}

[[Port *PortID(PortName)* received *Type* packet(Length:*number*)]{lang="EN-US"}]{#struct_0_36352_15676_574982576}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_x1887841386}[收到了类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的报文，报文的长度为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[（单位为字节），]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[STP]{lang="EN-US"}[、]{style="font-family:宋体"}[RSTP]{lang="EN-US"}[、]{style="font-family:宋体"}[MSTP-dot1s]{lang="EN-US"}[和]{style="font-family:宋体"}[MSTP-legacy]{lang="EN-US"}

[[Port *PortID(PortName)* VLAN *VLANID* sent *Type* packet(Length:*number*)]{lang="EN-US"}]{#struct_0_36352_15676_1629245855}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_1629311391}[在]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上发送了类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的报文，报文的长度为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[（单位为字节），]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[STP]{lang="EN-US"}[和]{style="font-family:宋体"}[RSTP]{lang="EN-US"}

[[Port *PortID(PortName)* VLAN *VLANID* received *Type* packet(Length:*number*)]{lang="EN-US"}]{#struct_0_36352_15676_1629114783}

[[端口]{style="font-family:宋体"}*[PortID(PortName))]{lang="EN-US"}*]{#struct_0_36352_15676_1629180319}[在]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上收到了类型为]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的报文，报文的长度为]{style="font-family:宋体"}*[Number]{lang="EN-US"}*[（单位为字节），]{style="font-family:宋体"}*[Type]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[TCN]{lang="EN-US"}[、]{style="font-family:宋体"}[STP]{lang="EN-US"}[和]{style="font-family:宋体"}[RSTP]{lang="EN-US"}

[[ProtocolVersionID]{lang="EN-US"}]{#struct_0_36352_15676_x1660787313}

[[协议的版本号]{style="font-family:宋体"}]{#struct_0_36352_15676_685988966}

[[BPDUType]{lang="EN-US"}]{#struct_0_36352_15676_140196047}

[[BPDU]{lang="EN-US"}]{#struct_0_36352_15676_x810409274}[报文的类型]{style="font-family:宋体"}

[[CIST Root ID]{lang="EN-US"}]{#struct_0_36352_15676_x1500773665}

[[CIST]{lang="EN-US"}]{#struct_0_36352_15676_575048112}[根桥编号]{style="font-family:宋体"}

[[External RPC]{lang="EN-US"}]{#struct_0_36352_15676_x820207625}

[[外部根路径开销]{style="font-family:宋体"}]{#struct_0_36352_15676_86936601}

[[Reg Root ID]{lang="EN-US"}]{#struct_0_36352_15676_1610828215}

[[域根桥编号]{style="font-family:宋体"}]{#struct_0_36352_15676_308193525}

[[Internal RPC]{lang="EN-US"}]{#struct_0_36352_15676_575506865}

[[内部根路径开销]{style="font-family:宋体"}]{#struct_0_36352_15676_x1932412703}

[[CIST Bridge ID]{lang="EN-US"}]{#struct_0_36352_15676_x1301583091}

[[CIST]{lang="EN-US"}]{#struct_0_36352_15676_672015348}[桥编号]{style="font-family:宋体"}

[[CIST Port ID]{lang="EN-US"}]{#struct_0_36352_15676_1647277010}

[[CIST]{lang="EN-US"}]{#struct_0_36352_15676_575572401}[端口编号]{style="font-family:宋体"}

[[Root ID]{lang="EN-US"}]{#struct_0_36352_15676_x1457634746}

[[根桥编号]{style="font-family:宋体"}]{#struct_0_36352_15676_x1159787741}

[[Path Cost]{lang="EN-US"}]{#struct_0_36352_15676_x1513560218}

[[路径开销]{style="font-family:宋体"}]{#struct_0_36352_15676_x462931663}

[[Bridge ID]{lang="EN-US"}]{#struct_0_36352_15676_575637937}

[[桥编号]{style="font-family:宋体"}]{#struct_0_36352_15676_689259621}

[[Port ID]{lang="EN-US"}]{#struct_0_36352_15676_1348739992}

[[端口编号]{style="font-family:宋体"}]{#struct_0_36352_15676_x1708565279}

[[(Instance)Flags  ]{lang="EN-US"}]{#struct_0_36352_15676_124114763}[：]{style="font-family:宋体"} [(*InstanceID*)*Port-Role*\[*Flag*\]]{lang="EN-US"}

[[收发]{style="font-family:宋体"}[BPDU]{lang="EN-US"}]{#struct_0_36352_15676_575703473}[报文的端口在]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[上的端口角色为]{style="font-family:宋体"}*[Port-Role]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[FlagA]{lang="EN-US"}*[，端口的状态为]{style="font-family:宋体"}*[FlagB]{lang="EN-US"}*[，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[Port-Role]{lang="EN-US"}*]{#struct_0_36352_15676_x382713437}[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}[Mast]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Master]{lang="EN-US"}[端口）、]{lang="EN-US" style="font-family:宋体"}[Altn]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Alternate]{lang="EN-US"}[端口或]{lang="EN-US" style="font-family:宋体"}[Backup]{lang="EN-US"}[端口）、]{lang="EN-US" style="font-family:宋体"}[Root]{lang="EN-US"}[（表示根端口）和]{lang="EN-US" style="font-family:宋体"}[Desi]{lang="EN-US"}[（表示指定端口）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[FlagA]{lang="EN-US"}*]{#struct_0_36352_15676_x1576349579}[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}[Ta]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[TCA]{lang="EN-US"}[报文）、]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Proposal]{lang="EN-US"}[报文）、]{lang="EN-US" style="font-family:宋体"}[A]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Agreement]{lang="EN-US"}[报文）和]{lang="EN-US" style="font-family:宋体"}[Tc]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[报文）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[FlagB]{lang="EN-US"}*]{#struct_0_36352_15676_x928953909}[的具体取值包括：]{lang="EN-US" style="font-family:宋体"}[F]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Forwarding]{lang="EN-US"}[）和]{lang="EN-US" style="font-family:宋体"}[L]{lang="EN-US"}[（表示]{lang="EN-US" style="font-family:宋体"}[Learning]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}[，如果没有显示该值，则表示]{style="font-family:宋体"}[Discarding]{lang="EN-US"}

[[PKT]{lang="EN-US"}]{#struct_0_36352_15676_575769009}

[[报文调试信息：包括端口号、端口名称、报文出入方向是发送还是接收、报文类型、报文长度以及十六进制显示的全部报文内容]{style="font-family:宋体"}]{#struct_0_36352_15676_1155208395}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_x296105438}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_39224178}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，打开所有端口的接收生成树报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp packet receive]{lang="EN-US"}]{#struct_0_36352_15676_575834545}

[\*Mar 18 14:28:41:781 2010 Sysname STP/7/PKT:]{lang="EN-US"}

[Port2(GigabitEthernet1/0/1) received MSTP-legacy packet(Length: 103)]{lang="EN-US"}

[ProtocolVersionID: 03]{lang="EN-US"}

[BPDUType         : 02]{lang="EN-US"}

[CIST Root ID     : 32768.000f-e200-3700]{lang="EN-US"}

[External RPC     : 0]{lang="EN-US"}

[Reg Root ID      : 32768.000f-e200-3700]{lang="EN-US"}

[Internal RPC     : 0]{lang="EN-US"}

[CIST Bridge ID   : 32768.000f-e200-3700]{lang="EN-US"}

[CIST Port ID     : 128.2]{lang="EN-US"}

[(Instance)Flags  : (00)Desi\[  A  P  \]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x578695901}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到长度为]{style="font-family:宋体"}[103]{lang="EN-US"}[字节的生成树私有格式报文，并对报文进行解析得到如下信息：对端设备运行的生成树协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文类型为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}[CIST]{lang="EN-US"}[根桥编号为]{style="font-family:宋体"}[32768.000F-E200-3700]{lang="EN-US"}[，外部根路径开销为]{style="font-family:宋体"}[0]{lang="EN-US"}[，域根桥编号为]{style="font-family:宋体"}[32768.000F-E200-3700]{lang="EN-US"}[，内部根路径开销为]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[CIST]{lang="EN-US"}[桥编号为]{style="font-family:宋体"}[32768.000F-E200-3700]{lang="EN-US"}[，]{style="font-family:宋体"}[CIST]{lang="EN-US"}[端口编号为]{style="font-family:宋体"}[128.2]{lang="EN-US"}[，]{style="font-family:宋体"}[MSTI]{lang="EN-US"}[编号为]{style="font-family:宋体"}[00]{lang="EN-US"}[，且]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文是指定端口发送的]{style="font-family:宋体"}[Agreement]{lang="EN-US"}[和]{style="font-family:宋体"}[Proposal]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x34185071}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，打开所有端口的发送生成树报文的详细调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp packet send verbose]{lang="EN-US"}]{#struct_0_36352_15676_898699729}

[\*Mar 18 14:28:41:782 2010 Sysname STP/7/PKT:]{lang="EN-US"}

[Port2(GigabitEthernet1/0/1) sent MSTP-legacy Packet(Length: 103)]{lang="EN-US"}

[00 00 03 02 6c 80 00 00 e0 fc 00 00 00 00 00 00]{lang="EN-US"}

[00 80 00 00 e0 fc 00 00 00 81 81 00 00 14 00 02]{lang="EN-US"}

[00 0f 00 00 00 00 40 30 30 65 30 66 63 30 30 30]{lang="EN-US"}

[30 30 30 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="EN-US"}

[00 00 00 00 00 00 00 00 00 ac 36 17 7f 50 28 3c]{lang="EN-US"}

[d4 b8 38 21 d8 ab 26 de 62 80 00 00 e0 fc 00 00]{lang="EN-US"}

[00 00 00 00 00 14 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x1199837206}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送长度为]{style="font-family:宋体"}[103]{lang="EN-US"}[字节的生成树私有格式报文，]{style="font-family:宋体"}[103]{lang="EN-US"}[字节的十六进制报文内容全部显示]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_1628983714}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开所有端口的接收生成树报文的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp packet receive]{lang="EN-US"}]{#struct_0_36352_15676_1629049250}

[\*Mar 18 14:28:41:781 2010 Sysname STP/7/PKT:]{lang="EN-US"}

[Port386(GigabitEthernet1/0/1) VLAN 2 received RSTP-legacy packet(Length: 42)]{lang="EN-US"}

[ProtocolVersionID: 03]{lang="EN-US"}

[BPDUType         : 02]{lang="EN-US"}

[Flags            : Desi\[  P  \]]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_1628852642}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到长度为]{style="font-family:宋体"}[42]{lang="EN-US"}[字节的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文，并对报文进行解析得到如下信息：对端设备运行的生成树协议版本号为]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文类型为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[，且]{style="font-family:宋体"}[BPDU]{lang="EN-US"}[报文是指定端口发送的]{style="font-family:宋体"}[Proposal]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_1628918178}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开所有端口的发送生成树报文的详细调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp packet send verbose]{lang="EN-US"}]{#struct_0_36352_15676_x1456154731}

[\*Mar 18 14:28:41:782 2010 Sysname STP/7/PKT:]{lang="EN-US"}

[Port385(GigabitEthernet1/0/1) VLAN 2 sent RSTP Packet(Length: 42)]{lang="EN-US"}

[00 00 02 02 6c 80 00 00 e0 fc 00 00 00 00 00 00]{lang="EN-US"}

[00 80 00 00 e0 fc 00 00 00 81 81 00 00 14 00 02]{lang="EN-US"}

[00 0f 00 00 00 00 00 02 00 02]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_1629770146}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送长度为]{style="font-family:宋体"}[42]{lang="EN-US"}[字节的]{style="font-family:宋体"}[PVST]{lang="EN-US"}[报文，]{style="font-family:宋体"}[42]{lang="EN-US"}[字节的十六进制报文内容全部显示]{style="font-family:宋体"}*

::: {#-670748357 .myid}
[]{#_Toc404784420}[]{#struct_0_36352_15676_x669671530}[]{#_Toc144801805}[]{#_Toc143943785}[]{#_Toc148517586}[]{#_Toc148610802}[]{#_Toc148517595}[]{#_Toc148610811}[]{#_Toc148517596}[]{#_Toc148610812}

**生成树 \-- 生成树调试命令 \-- debugging stp roles**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_575900081}

[**[debugging stp roles]{lang="EN-US"}**]{#struct_0_36352_15676_x1027468275}

[**[undo debugging stp roles]{lang="EN-US"}**]{#struct_0_36352_15676_x113875033}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_1186345203}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_x559497572}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_1131922002}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_x2077295318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_859692303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_x269675122}

[[无]{style="font-family:宋体"}]{#struct_0_36352_15676_575965617}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_195254579}

[**[debugging stp roles]{lang="EN-US"}**]{#struct_0_36352_15676_1938611568}[命令用来打开生成树端口角色变化调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging stp** **roles**]{lang="EN-US"}[命令用来关闭生成树端口角色变化调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树端口角色变化调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_36352_15676_1010933816}

[[表1-5 ]{lang="EN-US"}[debugging stp roles]{lang="EN-US"}]{#struct_0_36352_15676_x373774802}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1581452046}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_1405146382}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x296350471}

[[Instance *InstanceID*'s port *PortID(PortName)* is the currently *String* port]{lang="EN-US"}]{#struct_0_36352_15676_432416203}

[[VLAN *VLANID*'s port *PortID(PortName)* is the current *String* port]{lang="EN-US"}]{#struct_0_36352_15676_1629311393}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_574982577}[在]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上的角色为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}[ALTERNATE]{lang="EN-US"}[、]{style="font-family:宋体"}[BACKUP]{lang="EN-US"}[、]{style="font-family:宋体"}[ROOT]{lang="EN-US"}[、]{style="font-family:宋体"}[DESIGNATED]{lang="EN-US"}[和]{style="font-family:宋体"}[MASTER]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1887841385}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x1257502786}[打开生成树端口角色变化调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp roles]{lang="EN-US"}]{#struct_0_36352_15676_1128324520}

[\*Mar 18 14:28:41:783 2010 Sysname STP/7/ROLES: slot=6;Instance 2\'s port2(GigabitEthernet1/0/1) is currently ROOT port.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x383426151}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[MSTI 2]{lang="EN-US"}[上的端口角色被更新为根端口]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_1628918177}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开生成树端口角色变化调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp roles]{lang="EN-US"}]{#struct_0_36352_15676_1629770145}

[\*Mar 18 14:28:41:783 2010 Sysname STP/7/UPDTROLES:Slot=1; The role of ports on VLAN 2 was updated\...]{lang="EN-US"}

[\*Mar 18 14:28:41:783 2010 Sysname STP/7/ROLES: Slot=1;VLAN 2\'s port2(GigabitEthernet1/0/1) is the current ROOT port.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_36352_15676_x1398459526}*[端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[上的端口角色被更新为根端口]{style="font-family:宋体"}*

::: {#-1092076175 .myid}
[]{#_Toc404784421}[]{#struct_0_36352_15676_1527918115}[]{#_Toc144801806}[]{#_Toc143943786}

**生成树 \-- 生成树调试命令 \-- debugging stp tc**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_36352_15676_x1724786801}

[**[debugging stp tc]{lang="EN-US"}**[ \[ **interface** *interface-type* i*nterface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_1881802779}

[**[undo debugging stp tc]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_36352_15676_x595096263}

[[【视图】]{style="font-family:黑体"}]{#struct_0_36352_15676_575048113}

[[用户视图]{style="font-family:宋体"}]{#struct_0_36352_15676_x820207624}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_36352_15676_87002137}

[[network-admin]{lang="EN-US"}]{#struct_0_36352_15676_1790419037}

[[mdc-admin]{lang="EN-US"}]{#struct_0_36352_15676_x416661832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_36352_15676_1317559873}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_36352_15676_1152136378}[：打开或关闭指定端口的生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开或关闭所有端口的生成树]{style="font-family:宋体"}[ TC]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_36352_15676_x518100653}

[**[debugging stp]{lang="EN-US"}**[ **tc**]{lang="EN-US"}]{#struct_0_36352_15676_517591572}[命令用来打开生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging stp** **tc**]{lang="EN-US"}[命令用来关闭生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}]{#struct_0_36352_15676_x578912053}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[debugging stp tc]{lang="EN-US"}]{#struct_0_36352_15676_575506862}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1584512206}[[字段]{style="font-family:黑体"}]{#struct_0_36352_15676_x1932412698}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_36352_15676_x91139685}

[[TC event *String* occurs on Instance *InstanceID*'s port *PortID(PortName)*]{lang="EN-US"}]{#struct_0_36352_15676_1479916407}

[[TC event *String* occurs on VLAN *VLANID*'s port *PortID(PortName*]{lang="EN-US"}]{#struct_0_36352_15676_x1099703037}

[[端口]{style="font-family:宋体"}*[PortID(PortName)]{lang="EN-US"}*]{#struct_0_36352_15676_238677890}[在]{style="font-family:宋体"}[MSTI *InstanceID*]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN *VLANID*]{lang="EN-US"}[上发生的]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件为]{style="font-family:宋体"}*[String]{lang="EN-US"}*[，]{style="font-family:宋体"}*[String]{lang="EN-US"}*[的具体取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiving TCN]{lang="EN-US"}]{#struct_0_36352_15676_x1383283206}[：表示接收]{lang="EN-US" style="font-family:宋体"}[TCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiving TCA]{lang="EN-US"}]{#struct_0_36352_15676_452684575}[：表示接收]{lang="EN-US" style="font-family:宋体"}[TCA]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Receiving TC]{lang="EN-US"}]{#struct_0_36352_15676_575572398}[：表示接收]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sending TCN]{lang="EN-US"}]{#struct_0_36352_15676_1698215642}[：表示发送]{lang="EN-US" style="font-family:宋体"}[TCN]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sending TC]{lang="EN-US"}]{#struct_0_36352_15676_x1561479485}[：表示发送]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sending TCA]{lang="EN-US"}]{#struct_0_36352_15676_x1703753280}[：表示发送]{lang="EN-US" style="font-family:宋体"}[TCA]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TcWhile Expiring]{lang="EN-US"}]{#struct_0_36352_15676_69800354}[：表示]{lang="EN-US" style="font-family:
  宋体"}[TC]{lang="EN-US"}[报文发送定时器超时]{lang="EN-US" style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_36352_15676_1610067415}

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x1987282496}[在]{style="font-family:宋体"}[MSTP]{lang="EN-US"}[模式下，打开所有端口的生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp tc]{lang="EN-US"}]{#struct_0_36352_15676_575637934}

[\*Mar 18 14:28:41:784 2010 Sysname STP/7/TC: TC event Sending TC occurs on Instance 1\'s port2(GigabitEthernet1/0/1).]{lang="EN-US"}

[*[// MSTI 1]{lang="EN-US"}*]{#struct_0_36352_15676_689259624}*[中的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发出了]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 18 14:28:41:784 2010 Sysname STP/7/TC: TC event Receiving TC occurs on Instance 1\'s port2(GigabitEthernet1/0/1).]{lang="EN-US"}]{#struct_0_36352_15676_1348739989}

[*[// MSTI 1]{lang="EN-US"}*]{#struct_0_36352_15676_x1708237600}*[中的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到了]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_36352_15676_x1099571966}[在]{style="font-family:宋体"}[PVST]{lang="EN-US"}[模式下，打开所有端口的生成树]{style="font-family:宋体"}[TC]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging stp tc]{lang="EN-US"}]{#struct_0_36352_15676_462264660}

[\*Mar 18 14:28:41:784 2010 Sysname STP/8/PORTMSTTC: Slot=1; TC event Sending TC occurs on VLAN 1\'s port2(GigabitEthernet1/0/1).]{lang="EN-US"}

[*[// VLAN 1]{lang="EN-US"}*]{#struct_0_36352_15676_x1099768574}*[的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发出了]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 18 14:28:41:784 2010 Sysname STP/8/PORTMSTTC: Slot=1; TC event Receiving TC occurs on VLAN 1\'s port2(GigabitEthernet1/0/1).]{lang="EN-US"}]{#struct_0_36352_15676_x1099703038}

[*[// VLAN 1]{lang="EN-US"}*]{#struct_0_36352_15676_x1064811568}*[的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到了]{style="font-family:宋体"}[TC]{lang="EN-US"}[报文]{style="font-family:宋体"}*
