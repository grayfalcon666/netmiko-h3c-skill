::: {#-2037482360 .myid}
[]{#_Toc404785132}[]{#struct_0_53807_x1404_x773627986}

**ATM \-- ATM调试命令 \-- debugging atm all**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1507609039}

[**[debugging atm all]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_53807_x1404_x662618855}

[**[undo debugging atm all]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_53807_x1404_854293682}

[[【视图】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x2061327643}

[[用户视图]{style="font-family:宋体"}]{#struct_0_53807_x1404_2099208320}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x1109350640}

[[network-admin]{lang="EN-US"}]{#struct_0_53807_x1404_x210258107}

[[mdc-admin]{lang="EN-US"}]{#struct_0_53807_x1404_x995330349}

[[【参数】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x1326504504}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_53807_x1404_2066253973}[：表示指定接口的调试信息开关。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x193551147}

[**[debugging atm all]{lang="EN-US"}**]{#struct_0_53807_x1404_x928009873}[命令用来打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging atm all]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，所有的]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_1178737124}[调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[如果不指定接口，则打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x95388753}[接口的所有调试信息开关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x1944534319}

[[\# ]{lang="EN-US"}]{#struct_0_53807_x1404_1091292595}[打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging atm all]{lang="EN-US"}]{#struct_0_53807_x1404_x210192571}
:::

::: {#-1864992396 .myid}
[]{#_Toc404785133}[]{#struct_0_53807_x1404_1007675615}

**ATM \-- ATM调试命令 \-- debugging atm error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_53807_x1404_639199918}

[**[debugging atm error]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_x1702157740}

[**[undo debugging atm error]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_609423704}

[[【视图】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x2018070651}

[[用户视图]{style="font-family:宋体"}]{#struct_0_53807_x1404_648958561}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x29515730}

[[network-admin]{lang="EN-US"}]{#struct_0_53807_x1404_957520445}

[[mdc-admin]{lang="EN-US"}]{#struct_0_53807_x1404_x471980735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1960116963}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_53807_x1404_x210127035}[：表示指定接口的调试信息开关。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x945797452}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_53807_x1404_519752295}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-1864992396#_Ref337389143)[[ ]{lang="EN-US" style="color:blue"}]{.underline}[[[[不同[接口[对应的]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}VCI[[的取值范围]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}]{lang="EN-US"}](?-1864992396#_Ref57541113)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[]{#struct_0_53807_x1404_x1575592227}[]{#_Toc95359221}[]{#_Toc85604331}[]{#_Toc81386710}[]{#_Toc74661833}[]{#_Toc72589796}[]{#_Toc72589523}[]{#_Toc72589008}[]{#_Toc65921178}[]{#_Toc65919126}[]{#_Toc65919101}[]{#_Toc65910735}[]{#_Toc65909980}[]{#_Toc60125190}[]{#_Toc60111189}[[表1-1 ]{lang="EN-US"}[不同接口对应的]{style="font-family:黑体"}[VCI]{lang="EN-US"}]{#_Ref57541113}[的取值范围]{style="font-family:黑体"}[]{#_Ref337389143}

[]{#table_struct_0_x1405243689}[[接口类型]{style="font-family:黑体"}]{#struct_0_53807_x1404_2104648226}
:::

[[VCI]{lang="EN-US"}]{#struct_0_53807_x1404_x254821247}[取值范围]{style="font-family:黑体"}

[[ATM ADSL]{lang="EN-US"}]{#struct_0_53807_x1404_1774812782}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_x608559812}

[[ATM ADSL2+]{lang="EN-US"}]{#struct_0_53807_x1404_x209537211}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_1478643477}

[[ATM G.SHDSL]{lang="EN-US"}]{#struct_0_53807_x1404_x1294554791}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_225194168}

[[ATM SHDSL_4WIRE]{lang="EN-US"}]{#struct_0_53807_x1404_2007081636}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_x1688368121}

[[ATM SHDSL_4WIRE_BIS]{lang="EN-US"}]{#struct_0_53807_x1404_x209471675}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_x457218558}

[[ATM SHDSL_8WIRE_BIS]{lang="EN-US"}]{#struct_0_53807_x1404_x1253927238}

[[\<0-255\>]{lang="EN-US"}]{#struct_0_53807_x1404_885558435}

[[ATM E1]{lang="EN-US"}]{#struct_0_53807_x1404_2042391524}

[[\<0-511\>]{lang="EN-US"}]{#struct_0_53807_x1404_x854021297}

[[ATM T1]{lang="EN-US"}]{#struct_0_53807_x1404_x1890353919}

[[\<0-511\>]{lang="EN-US"}]{#struct_0_53807_x1404_x210061502}

[[ATM E3]{lang="EN-US"}]{#struct_0_53807_x1404_x543597282}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_53807_x1404_x1716860369}

[[ATM T3]{lang="EN-US"}]{#struct_0_53807_x1404_x177088764}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_53807_x1404_1725127873}

[[ATM OC-3c/STM-1]{lang="EN-US"}]{#struct_0_53807_x1404_x113852630}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_53807_x1404_x209995966}

[[ATM OC-12c/STM-4]{lang="EN-US"}]{#struct_0_53807_x1404_1428240584}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_53807_x1404_1871066138}

[[ATM 25M]{lang="EN-US"}]{#struct_0_53807_x1404_x1965625174}

[[\<0-1023\>]{lang="EN-US"}]{#struct_0_53807_x1404_x1177438223}

[[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x209930430}[子接口]{style="font-family:宋体"}

[[与]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_734851526}[子接口所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[[PVC-group]{lang="EN-US"}]{#struct_0_53807_x1404_x45560862}

[[与]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}]{#struct_0_53807_x1404_x1566926943}[所属]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的取值范围相同]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x394682845}

[**[debugging atm error]{lang="EN-US"}**]{#struct_0_53807_x1404_786644277}[命令用来打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging atm error]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x209864894}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果不指定接口，则打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_1052623961}[接口的错误调试信息开关。如果不指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名或者]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对，则打开指定接口的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging atm error]{lang="EN-US"}]{#struct_0_53807_x1404_1669842680}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1376495611}[[字段]{style="font-family:黑体"}]{#struct_0_53807_x1404_1153907713}

[[描述]{style="font-family:黑体"}]{#struct_0_53807_x1404_1452143534}

[[Interface *interface-name* PVC *vpi/vci* : Failed to process InARP timeout event, as there is no InARP mapping.]{lang="EN-US"}]{#struct_0_53807_x1404_x2132621536}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x634737317}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[超时处理失败，没有]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : Failed to process InARP timeout event, as there is no InARP mapping.]{lang="EN-US"}]{#struct_0_53807_x1404_x1349090077}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x210323646}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[超时处理失败，没有]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : Sending InARP *type* packet failed, as the interface has no IP address.]{lang="EN-US"}]{#struct_0_53807_x1404_x123505553}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x1156537491}[：发送]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报文失败，接口未配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_x246702215}[：请求]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x1229772740}[：]{lang="EN-US" style="font-family:宋体"}[应答报文]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id*: Sending InARP *type* packet failed, as the interface has no IP address.]{lang="EN-US"}]{#struct_0_53807_x1404_1851313262}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x2029533343}[：发送]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报文失败，接口未配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_x210258110}[：请求]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x995002670}[：]{lang="EN-US" style="font-family:宋体"}[应答报文]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed due to packet protocol is error.]{lang="EN-US"}]{#struct_0_53807_x1404_607206408}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x1806177802}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文协议字段错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC PVC-group *id* : InARP packet parse failed due to packet protocol error.]{lang="EN-US"}]{#struct_0_53807_x1404_x588618612}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_1405460564}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文协议字段错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as the packet type is not reply or request.]{lang="EN-US"}]{#struct_0_53807_x1404_x210192574}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_1007872223}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文类型不是请求或应答报文]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : InARP packet parse failed, as the packet type is not reply or request.]{lang="EN-US"}]{#struct_0_53807_x1404_x518309458}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x1472134509}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文类型不是请求或应答报文]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed due to packet length field error.]{lang="EN-US"}]{#struct_0_53807_x1404_x2122697403}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_439122368}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文长度字段错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : InARP packet parse failed due to packet length field error.]{lang="EN-US"}]{#struct_0_53807_x1404_x210127038}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x946518348}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文长度字段错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as packet length is too long.]{lang="EN-US"}]{#struct_0_53807_x1404_x1236290037}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_1322760443}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文长度太长]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : InARP packet parse failed, as packet length is too long.]{lang="EN-US"}]{#struct_0_53807_x1404_x1672924285}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x209537214}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文长度太长]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : InARP packet parse failed, as packet destination IP address is 0.0.0.0.]{lang="EN-US"}]{#struct_0_53807_x1404_1478315797}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_1814270708}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}

[[Interface *interface-name* PVC-group *id* : InARP packet parse failed, as packet destination IP is 0.0.0.0.]{lang="EN-US"}]{#struct_0_53807_x1404_210503015}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x1775298706}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文解析失败，报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}

[[Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as there is no InARP mapping.]{lang="EN-US"}]{#struct_0_53807_x1404_x209471678}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x458070526}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，没有]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : Failed to process an InARP reply packet, as there is no InARP mapping.]{lang="EN-US"}]{#struct_0_53807_x1404_x1408765529}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_1325579481}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，没有]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as InARP mapping state is not ATM_INARP_STATE_SNDREQUEST.]{lang="EN-US"}]{#struct_0_53807_x1404_x307999560}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x210061501}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射的状态不为"发送请求等待应答"状态]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id*: Failed to process an InARP reply packet, as InARP mapping state is not ATM_INARP_STATE_SNDREQUEST.]{lang="EN-US"}]{#struct_0_53807_x1404_x543531746}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_216565197}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射的状态不为"发送请求等待应答"状态]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* : Failed to process an InARP reply packet, as packet destination IP is *ipaddress*, different from interface IP.]{lang="EN-US"}]{#struct_0_53807_x1404_x1435714517}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x209995965}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ipaddress]{lang="EN-US"}*[，与本端接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id* : Failed to process an InARP reply packet, as packet destination IP is *ipaddress*, different from interface IP.]{lang="EN-US"}]{#struct_0_53807_x1404_1428437192}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x108544312}[：处理]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答报文失败，报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ipaddress]{lang="EN-US"}*[，与本端接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[OAM ping reply error due to invalid ping index.]{lang="EN-US"}]{#struct_0_53807_x1404_624346032}

[[OAM]{lang="EN-US"}]{#struct_0_53807_x1404_1365452239}[回应报文错误，索引无效]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_x209930429}

[[接口]{lang="EN-US" style="font-family:宋体"}]{#struct_0_53807_x1404_734392773}[[interface-name]{lang="EN-US"}]{.TableTextChar}[ PVC ]{lang="EN-US"}[[vpi/vci]{lang="EN-US"}]{.TableTextChar}[不存在]{style="font-family:宋体"}

[[Dropped a packet on interface *interface-name* due to absence of the link control block.]{lang="EN-US"}]{#struct_0_53807_x1404_1160832053}

[[报文发送失败，链路控制块不存在]{style="font-family:宋体"}]{#struct_0_53807_x1404_x441631747}

[[Failed to send a packet, as the physical control block of interface *interface-name* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_x209864893}

[[报文发送失败，接口]{style="font-family:宋体"}]{#struct_0_53807_x1404_1052689497}[[interface-name]{lang="EN-US"}]{.TableTextChar}[物理控制块不存在]{style="font-family:宋体"}

[[Failed to send a packet, as the outbound EoA mapping is the same as inbound EoA mapping.]{lang="EN-US"}]{#struct_0_53807_x1404_1602049299}

[[报文发送失败，报文的出]{style="font-family:宋体"}]{#struct_0_53807_x1404_x210323645}[EoA]{lang="EN-US"}[映射和入]{style="font-family:宋体"}[EoA]{lang="EN-US"}[映射相同]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as PVC state is down.]{lang="EN-US"}]{#struct_0_53807_x1404_x123440017}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_5243223}[：报文接收失败，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to send a packet, as PVC state is down.]{lang="EN-US"}]{#struct_0_53807_x1404_x135151876}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x210258109}[：报文发送失败，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet due to packet de-encapsulation error.]{lang="EN-US"}]{#struct_0_53807_x1404_x994412845}

[[接口]{style="font-family:宋体"}[interface-name PVC vpi/vci]{lang="EN-US"}]{#struct_0_53807_x1404_1444035827}[：报文接收失败，去封装错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the packet is not an IP packet though IP transparent transmission is enabled.]{lang="EN-US"}]{#struct_0_53807_x1404_x210192573}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_1007544543}[：报文接收失败，接口使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}[透传但报文不是]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to send a packet due to packet encapsulation error.]{lang="EN-US"}]{#struct_0_53807_x1404_255325615}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x778347354}[：报文发送失败，封装错误]{style="font-family:宋体"}

[[Interface *interface-name* PVC-group *id*: Failed to send a packet, as PVC-group has no appropriate sub PVC available.]{lang="EN-US"}]{#struct_0_53807_x1404_x210127037}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC-group *id*]{lang="EN-US"}]{#struct_0_53807_x1404_x945928524}[：报文发送失败，]{style="font-family:宋体"}[PVC-group]{lang="EN-US"}[下没有合适的子]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to send a packet, as VPI *vpi-value* failed to get token.]{lang="EN-US"}]{#struct_0_53807_x1404_x718555511}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x209537213}[：报文发送失败，]{style="font-family:宋体"}[VPI *vpi-value*]{lang="EN-US"}[获取令牌失败]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as VPI *vpi-value* failed to get token.]{lang="EN-US"}]{#struct_0_53807_x1404_1478774549}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_633931542}[：报文接收失败，]{style="font-family:宋体"}[VPI *vpi-value*]{lang="EN-US"}[获取令牌失败]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as PPPoA mapping does not exist..]{lang="EN-US"}]{#struct_0_53807_x1404_x209471677}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x457087486}[：报文接收失败，]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射不存在]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as EoA mapping does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_x1215250080}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x2023179271}[：报文接收失败，]{style="font-family:宋体"}[EoA]{lang="EN-US"}[映射不存在]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as physical control block of interface *virtual-interface-name* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_1356022443}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_242170847}[：报文接收失败，接口]{style="font-family:宋体"}*[virtual-interface-name]{lang="EN-US"}*[的物理控制块不存在]{style="font-family:宋体"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the state of interface *virtual-interface-name* is down.]{lang="EN-US"}]{#struct_0_53807_x1404_1356087979}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x485034791}[：报文接收失败，接口]{style="font-family:宋体"}*[virtual-interface-name]{lang="EN-US"}*[的状态为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Interface *interface-name* PVC *vpi/vci*: Failed to receive a packet, as the packet is a multicast one.]{lang="EN-US"}]{#struct_0_53807_x1404_x124447127}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_1356153515}[：报文接收失败，报文是组播报文]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive a packet, as PVC *vpi/vci* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_x141179102}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_199764542}[：报文接收失败，]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to send an IP packet, as IPoA mapping for IP: *ipaddress* was not found.]{lang="EN-US"}]{#struct_0_53807_x1404_x282675654}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356219051}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文发送失败，未找到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ipaddress]{lang="EN-US"}*[对应的]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to change OAM state, as PVC *vpi/vci* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_x1734388333}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355760299}[：]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态改变失败，]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive OAM ping, as PVC *vpi/vci* does not exist.]{lang="EN-US"}]{#struct_0_53807_x1404_1547117737}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_25230512}[：接收]{style="font-family:宋体"}[OAM ping]{lang="EN-US"}[失败，]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[不存在]{style="font-family:宋体"}

[[Interface *interface-name*: Failed to receive a packet, as the network layer state of interface is down.]{lang="EN-US"}]{#struct_0_53807_x1404_1355825835}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1132471037}[：报文接收失败，接口网络层状态为]{style="font-family:宋体"}[down]{lang="EN-US"}

[[Interface *interface-name*: Failed to send a packet by IPoA mapping, as the packet type is unknown.]{lang="EN-US"}]{#struct_0_53807_x1404_960865546}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355891371}[：]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射发送报文失败，未知的报文类型]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_53807_x1404_749055859}

[[\# Router A]{lang="EN-US"}]{#struct_0_53807_x1404_x42296907}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口连接，其中一端配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，另一端不配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_53807_x1404_x2054153429}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_1933854822}

[\[Sysname\] interface atm 2/4/2]{lang="EN-US"}

[\[Sysname-ATM2/4/2\] pvc 10/33]{lang="EN-US"}

[\[Sysname-ATM2/4/2-pvc-10/33\] map ip inarp]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_53807_x1404_x2045689431}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_1355956907}

[\[Sysname\] interface atm 2/4/3]{lang="EN-US"}

[\[Sysname-ATM2/4/3\] pvc 10/33]{lang="EN-US"}

[\[Sysname-ATM2/4/3-pvc-10/33\] map ip inarp]{lang="EN-US"}

[\[Sysname-ATM2/4/3-pvc-10/33\] quit]{lang="EN-US"}

[\[Sysname-ATM2/4/3\] ip address 100.1.1.2 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_53807_x1404_x1898158008}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的错误调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging atm error]{lang="EN-US"}]{#struct_0_53807_x1404_x18403234}

[\*Dec 24 08:04:05:125 2012 Sysname ATM/7/ERROR: -MDC=1;]{lang="EN-US"}

[Interface ATM2/4/3 PVC 10/33: Sending InARP request packet failed, as the interface has no IP address.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_53807_x1404_x1167893812}*[由于没有找到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[InARP]{lang="EN-US"}[请求报文发送失败]{style="font-family:宋体"}*

::: {#1802670155 .myid}
[]{#_Toc404785134}[]{#struct_0_53807_x1404_x845573797}

**ATM \-- ATM调试命令 \-- debugging atm event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1074502813}

[**[debugging atm event]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_80354715}

[**[undo debugging atm event]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_1385075080}

[[【视图】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1356546731}

[[用户视图]{style="font-family:宋体"}]{#struct_0_53807_x1404_650668235}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1300372483}

[[network-admin]{lang="EN-US"}]{#struct_0_53807_x1404_1467562703}

[[mdc-admin]{lang="EN-US"}]{#struct_0_53807_x1404_1885944927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x2020587339}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_53807_x1404_136561685}[：表示指定接口的调试信息开关。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1528368935}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_53807_x1404_20437207}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-1864992396#_Ref337389143)[[ ]{lang="EN-US" style="color:blue"}]{.underline}[[[[不同[接口[对应的]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}VCI[[的取值范围]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}]{lang="EN-US"}](?-1864992396#_Ref57541113)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_53807_x1404_1877750713}

[**[debugging atm event]{lang="EN-US"}**]{#struct_0_53807_x1404_1356612267}[命令用来打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging atm event]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x142591085}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果不指定接口，则打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_1653310930}[接口的事件调试信息开关。如果不指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名或者]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对，则打开指定接口的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[[本命令将打开所有发生在]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_1242375472}[接口或者某条]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上的事件调试信息开关，可以用来跟踪系统的一些关键事件，在查找网络故障时，这些信息可能会有参考作用。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging atm event]{lang="EN-US"}]{#struct_0_53807_x1404_x1352669657}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1384667853}[[字段]{style="font-family:黑体"}]{#struct_0_53807_x1404_1859250596}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_53807_x1404_x230480566}

[[Received and dropped an InARP packet on interface *interface-name* PVC *vpi/vci*, as no local IP is configured.]{lang="EN-US"}]{#struct_0_53807_x1404_1890509465}

[[本端未配]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_53807_x1404_1356022444}[地址，丢弃收到的]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文，对应接口为]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，对应]{style="font-family:宋体"}[PVC]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*

[[InARP mapping on interface *interface-name* PVC *vpi/vci* timed out.]{lang="EN-US"}]{#struct_0_53807_x1404_241974239}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x455143610}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[的]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射超时]{style="font-family:宋体"}

[[The InARP mapping state on interface *interface-name* PVC *vpi/vci*  changed from *oldstate* to *newstate*.]{lang="EN-US"}]{#struct_0_53807_x1404_x1508076490}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1407601667}[下]{style="font-family:宋体"}[PVC *vpi/vci* ]{lang="EN-US"}[的]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射状态从]{style="font-family:宋体"}*[oldstate]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[oldstate]{lang="EN-US"}*[和]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATM_INARP_STATE_INIT]{lang="EN-US"}]{#struct_0_53807_x1404_x1212873945}[：初始化状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATM_INARP_STATE_SNDREQUEST]{lang="EN-US"}]{#struct_0_53807_x1404_x2056950382}[：已发送]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[请求]{style="font-family:宋体"}[报文、等待]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[应答]{style="font-family:宋体"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATM_INARP_STATE_RCVREPLY]{lang="EN-US"}]{#struct_0_53807_x1404_1356087980}[：]{lang="EN-US" style="font-family:宋体"}[已收到]{style="font-family:宋体"}[InARP]{lang="EN-US"}[应答]{style="font-family:宋体"}[报文状态]{lang="EN-US" style="font-family:宋体"}

[[Deleted the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci* because InARP mapping changed.]{lang="EN-US"}]{#struct_0_53807_x1404_x485624628}

[[删除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x2078271594}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的邻接表，因为]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射改变]{style="font-family:宋体"}

[[Refreshed the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci* because InARP mapping changed, the old IP is *oldip-address*]{lang="EN-US"}]{#struct_0_53807_x1404_x442555190}

[[刷新接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1620751207}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的邻接表，因为]{style="font-family:宋体"}[InARP]{lang="EN-US"}[映射改变，原]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[oldip-address]{lang="EN-US"}*

[[The kernel notified interface *interface-name* PVC *vpi/vci* to change to *newstate*.]{lang="EN-US"}]{#struct_0_53807_x1404_1356153516}

[[内核通知接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x141244638}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_1043021373}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_x54675338}[：关闭状态]{style="font-family:宋体"}

[[Received create-PVC *vpi/vci* event on interface *interface-name* from kernel.]{lang="EN-US"}]{#struct_0_53807_x1404_x806576931}

[[内核通知创建]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x1573987720}

[[Received delete-PVC *vpi/vci* event on interface *interface-name* from kernel.]{lang="EN-US"}]{#struct_0_53807_x1404_1356219052}

[[内核通知删除]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}]{#struct_0_53807_x1404_x1734453869}

[[Received OAM ping reply from kernel with ping index being *value*.]{lang="EN-US"}]{#struct_0_53807_x1404_1897789590}

[[收到]{style="font-family:宋体"}[OAM ping]{lang="EN-US"}]{#struct_0_53807_x1404_x775602478}[应答，对应索引为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Interface *interface-name* PVC *vpi/vci* received QoS bandwidth change event from kernel(OutputPcr: *pcrvalue*, OutputScr: *scrvalue*, ServiceType: *type*).]{lang="EN-US"}]{#struct_0_53807_x1404_x1773868039}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355760300}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[收到内核通知]{style="font-family:宋体"}[QoS]{lang="EN-US"}[带宽变化，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}*[pcrvalue]{lang="EN-US"}*[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的可承受速率为]{style="font-family:宋体"}*[scrvalue]{lang="EN-US"}*[，业务类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UBR]{lang="EN-US"}]{#struct_0_53807_x1404_x791075664}[：非确定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBR]{lang="EN-US"}]{#struct_0_53807_x1404_x1639349489}[：]{style="font-family:宋体"}[恒定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-RT]{lang="EN-US"}]{#struct_0_53807_x1404_x364457585}[：实时可变速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-NRT]{lang="EN-US"}]{#struct_0_53807_x1404_x476229239}[：非实时可变速率]{style="font-family:宋体"}

[[Received add-IP-address *ip-address* event on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_1355825836}

[[收到添加]{style="font-family:宋体"}]{#struct_0_53807_x1404_x1132667645}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[[ip-address]{lang="EN-US"}]{.TableTextChar}[事件]{style="font-family:宋体"}

[[Received delete-IP-address *ip-address* event on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_388562307}

[[收到删除]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_53807_x1404_1093728924}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[[PVC *vpi/vci* state changed to *newstate* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_1355891372}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_748990323}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_1559030333}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_x74504941}[：关闭状态]{style="font-family:宋体"}

[[PVC-group *id* state changed to *newstate* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_x885511715}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355956908}[下]{style="font-family:宋体"}[PVC-group *id*]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_x1898747832}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_952472457}[：关闭状态]{style="font-family:宋体"}

[[PVC *vpi/vci* state changed to *newstate* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_x8552653}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356546732}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[not shutdown]{lang="EN-US"}]{#struct_0_53807_x1404_650733771}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[shutdown]{lang="EN-US"}]{#struct_0_53807_x1404_951673747}[：关闭状态]{style="font-family:宋体"}

[[Network layer state changed to *newstate* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_53807_x1404_264214399}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356612268}[网络层状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_x141608045}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_x179325332}[：关闭状态]{style="font-family:宋体"}

[[OAM state changed to *newstate* on interface *interface-name* PVC *vpi/vci*.]{lang="EN-US"}]{#struct_0_53807_x1404_x467968014}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356022441}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[状态变为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_242301919}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_684015819}[：关闭状态]{style="font-family:宋体"}

[[Notified driver to create a mapping on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*, MapType: *type*, IP Address: *ip-address*)]{lang="EN-US"}]{#struct_0_53807_x1404_2076887759}

[[通知驱动在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356087977}[上创建映射，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，映射类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x485165863}[：]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INARP IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x2017555608}[：]{lang="EN-US" style="font-family:宋体"}[InARP IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEFAULT IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x2059908989}[：]{lang="EN-US" style="font-family:宋体"}[默认]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3 EoA]{lang="EN-US"}]{#struct_0_53807_x1404_1356153513}[：]{lang="EN-US" style="font-family:宋体"}[三层]{style="font-family:宋体"}[EoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x141572318}[：]{lang="EN-US" style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Notified driver to delete a mapping on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*, MapType: *type*, IP Address: *ip-address*)]{lang="EN-US"}]{#struct_0_53807_x1404_629811194}

[[通知驱动在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356219049}[上删除映射，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，映射类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x1733864044}[：]{lang="EN-US" style="font-family:宋体"}[静态]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INARP IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_x1225224355}[：]{lang="EN-US" style="font-family:宋体"}[InARP IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEFAULT IPoA]{lang="EN-US"}]{#struct_0_53807_x1404_1355760297}[：]{lang="EN-US" style="font-family:宋体"}[默认]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3 EoA]{lang="EN-US"}]{#struct_0_53807_x1404_1547773097}[：]{lang="EN-US" style="font-family:宋体"}[三层]{style="font-family:宋体"}[EoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPPoA]{lang="EN-US"}]{#struct_0_53807_x1404_1554763488}[：]{lang="EN-US" style="font-family:宋体"}[PPPoA]{lang="EN-US"}[映射]{style="font-family:宋体"}

[[Notified driver to send OAM AIS/RDI cell on interface *interface-name*, with *value* returned.]{lang="EN-US"}]{#struct_0_53807_x1404_1414579942}

[[通知驱动在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355825833}[上发送]{style="font-family:宋体"}[OAM AIS/RDI]{lang="EN-US"}[告警信元，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Notified driver to create a PVC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)]{lang="EN-US"}]{#struct_0_53807_x1404_x1132339965}

[[下驱动创建接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x172485853}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*

[[Notified driver to delete a PVC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)]{lang="EN-US"}]{#struct_0_53807_x1404_1355891369}

[[下驱动删除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_748531572}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*

[[Notified driver to clear PVC statistics on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext*)]{lang="EN-US"}]{#struct_0_53807_x1404_x1685216112}

[[下驱动清除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355956905}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*

[[Notified driver to change PVC state on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* *State: newstate*)]{lang="EN-US"}]{#struct_0_53807_x1404_x1898026936}

[[通知驱动改变接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1193675002}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，状态为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[。]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_1356546729}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_650143946}[：关闭状态]{style="font-family:宋体"}

[[Notified driver to change PVC physical state on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* *State: newstate*)]{lang="EN-US"}]{#struct_0_53807_x1404_1356612265}

[[通知驱动改变接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x142460013}[下]{style="font-family:宋体"}[PVC]{lang="EN-US"}[物理状态，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，状态为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[。]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_53807_x1404_x1056239283}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_53807_x1404_1356022442}[：关闭状态]{style="font-family:宋体"}

[[Notified driver to set service on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* ServiceType*: type* Output-pcr*: pcrvalue,* Output-scr*: scrvalue,* Output-mbs*: mbsvalue,* Cdvt_value*:  cdvtvalue* )]{lang="EN-US"}]{#struct_0_53807_x1404_242105311}

[[通知驱动设置接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1231455537}[下业务类型，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，业务类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的峰值速率为]{style="font-family:宋体"}*[pcrvalue]{lang="EN-US"}*[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的可承受速率为]{style="font-family:宋体"}*[scrvalue]{lang="EN-US"}*[，输出]{style="font-family:宋体"}[ATM]{lang="EN-US"}[信元的最大突发长度为]{style="font-family:宋体"}*[mbsvalue]{lang="EN-US"}*[，信元时延变化容限为]{style="font-family:宋体"}*[cdvtvalue]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UBR]{lang="EN-US"}]{#struct_0_53807_x1404_1356087978}[：非确定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBR]{lang="EN-US"}]{#struct_0_53807_x1404_x485100327}[：]{style="font-family:宋体"}[恒定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-RT]{lang="EN-US"}]{#struct_0_53807_x1404_1086080101}[：实时可变速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-NRT]{lang="EN-US"}]{#struct_0_53807_x1404_1356153514}[：非实时可变速率]{style="font-family:宋体"}

[[Notified driver to set transmit-priority on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* ServiceType: *type,* Transmit-Priority: * privalue*)]{lang="EN-US"}]{#struct_0_53807_x1404_x141113566}

[[通知驱动设置接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356219050}[下传输优先级，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，业务类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，传输优先级为]{style="font-family:宋体"}*[privalue]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UBR]{lang="EN-US"}]{#struct_0_53807_x1404_x1734322797}[：非确定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBR]{lang="EN-US"}]{#struct_0_53807_x1404_1387240516}[：]{style="font-family:宋体"}[恒定速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-RT]{lang="EN-US"}]{#struct_0_53807_x1404_1355760298}[：实时可变速率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VBR-NRT]{lang="EN-US"}]{#struct_0_53807_x1404_1547052201}[：非实时可变速率]{style="font-family:宋体"}

[[Notified driver to set OAM loopback on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* interval: *interval*, up-count: *up-count*, down-count: *down-count*, retry-interval: *retry-interval*)]{lang="EN-US"}]{#struct_0_53807_x1404_1355825834}

[[通知驱动设置接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1132536573}[下]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的发送以及重传检测，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，发送]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的间隔时间为]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[UP]{lang="EN-US"}[之前必须连续正确收到]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的数量为]{style="font-family:宋体"}*[up-count]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态转变为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[之前连续未收到的]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[信元的数量为]{style="font-family:宋体"}*[down-count]{lang="EN-US"}*[，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态改变前]{style="font-family:宋体"}[OAM F5 Loopback]{lang="EN-US"}[在进行重传验证时的信元发送间隔时间为]{style="font-family:宋体"}*[retry-interval]{lang="EN-US"}*

[[Notified driver to set OAM CC on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* CheckType: *type*)]{lang="EN-US"}]{#struct_0_53807_x1404_x852011131}

[[通知驱动设置接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1355891370}[下]{style="font-family:宋体"}[OAM]{lang="EN-US"}[连续性检测，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，启动方式类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sink]{lang="EN-US"}]{#struct_0_53807_x1404_749121395}[：]{style="font-family:宋体"}[作为接收端时启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[source]{lang="EN-US"}]{#struct_0_53807_x1404_1355956906}[：]{style="font-family:宋体"}[作为发送端时启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[both]{lang="EN-US"}]{#struct_0_53807_x1404_x1898092472}[：]{style="font-family:宋体"}[作为接收端和发送端时启动]{lang="EN-US" style="font-family:宋体"}

[[Notified driver to set OAM AIS/RDI cell detection parameters on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* up-count: *up-count*, down-count: *down-count*)]{lang="EN-US"}]{#struct_0_53807_x1404_x1903634968}

[[通知驱动修改接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356546730}[下]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元检测的相关参数，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，连续没有收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元秒数为]{style="font-family:宋体"}*[up-count]{lang="EN-US"}*[，连续收到]{style="font-family:宋体"}[AIS/RDI]{lang="EN-US"}[告警信元个数为]{style="font-family:宋体"}*[down-count]{lang="EN-US"}*

[[Notified driver to send OAM ping cell on interface *interface-name*, with *value* returned. (VPI: *vpi-value*, VCI: *vci-value*, DrvContext: *drvcontext,* PingIndex: *indexvalue*)]{lang="EN-US"}]{#struct_0_53807_x1404_650602699}

[[通知驱动在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356612266}[上发送]{style="font-family:宋体"}[OAM ping]{lang="EN-US"}[信元，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*[。下发数据如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[，驱动上下文为]{style="font-family:宋体"}*[drvcontext]{lang="EN-US"}*[，]{style="font-family:宋体"}[Ping]{lang="EN-US"}[索引为]{style="font-family:宋体"}*[indexvalue]{lang="EN-US"}*

[[Get OAM statistics on interface *interface-name* PVC *vpi/vci* from driver, with *value* returned.]{lang="EN-US"}]{#struct_0_53807_x1404_x142525549}

[[向驱动获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356022439}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[统计信息，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Get PVC statistics on interface *interface-name* PVC *vpi/vci* from driver, with *value* returned.]{lang="EN-US"}]{#struct_0_53807_x1404_242826204}

[[向驱动获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1452150863}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Refreshed the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci*, with *value* returned.]{lang="EN-US"}]{#struct_0_53807_x1404_1356087975}

[[刷新接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x485296935}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的邻接表，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Deleted the adjacent table of IP *ip-address* on interface *interface-name* PVC *vpi/vci*, with *value* returned.]{lang="EN-US"}]{#struct_0_53807_x1404_1356153511}

[[删除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x141441246}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的邻接表，返回]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Notified *event-type* event  on interface *interface-name* to module *module-id*.  (VPI: *vpi-value*, VCI: *vci-value*)]{lang="EN-US"}]{#struct_0_53807_x1404_x1728674323}

[[通知模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_53807_x1404_1356219047}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发生]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[事件，具体参数如下：]{style="font-family:宋体"}[VPI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vpi-value]{lang="EN-US"}*[，]{style="font-family:宋体"}[VCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[vci-value]{lang="EN-US"}*[。其中]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC_CREATE]{lang="EN-US"}]{#struct_0_53807_x1404_x1734781548}[：创建]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC_DELETE]{lang="EN-US"}]{#struct_0_53807_x1404_1355760295}[：删除]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[Notified *event-type* event  on interface *interface-name* PVC *vpi/vci* to module *module-id* . ]{lang="EN-US"}]{#struct_0_53807_x1404_1547904169}

[[通知模块]{style="font-family:宋体"}*[module-id]{lang="EN-US"}*]{#struct_0_53807_x1404_1355825831}[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[发生]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[事件，其中]{style="font-family:宋体"}*[event-type]{lang="EN-US"}*[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC_UP]{lang="EN-US"}]{#struct_0_53807_x1404_x1132208893}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC_DOWN]{lang="EN-US"}]{#struct_0_53807_x1404_x1604570647}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PVC_SPEEDCHANGE]{lang="EN-US"}]{#struct_0_53807_x1404_1355891367}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[带宽改变]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_53807_x1404_748662644}

[[\# Router A]{lang="EN-US"}]{#struct_0_53807_x1404_151668216}[和]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口连接，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_53807_x1404_x2072962138}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_x1427341911}

[\[Sysname\] interface atm 2/4/2]{lang="EN-US"}

[\[Sysname-ATM2/4/2\] pvc 10/33]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_53807_x1404_406988708}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_1355956903}

[\[Sysname\] interface atm 2/4/3]{lang="EN-US"}

[\[Sysname-ATM2/4/3\] pvc 10/33]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_53807_x1404_x1898420152}[打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging atm event]{lang="EN-US"}]{#struct_0_53807_x1404_499131538}

[[\# ]{lang="EN-US"}]{#struct_0_53807_x1404_2023792996}[将]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的]{style="font-family:宋体"}[PVC 10/33]{lang="EN-US"}[进行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[操作。]{style="font-family:宋体"}

[[\[Sysname-ATM0/2-pvc-10/33\] shutdown]{lang="EN-US"}]{#struct_0_53807_x1404_1794314349}

[\*Dec 24 09:36:30:715 2012 Sysname ATM/7/EVENT:]{lang="EN-US"}

[PVC 10/33 state changed to shutdown on interface ATM2/4/2.]{lang="EN-US"}

[*[// ATM2/4/2]{lang="EN-US"}*]{#struct_0_53807_x1404_x1103615169}*[的]{style="font-family:宋体"}[PVC 10/33]{lang="EN-US"}[状态为]{style="font-family:宋体"}[shutdown]{lang="EN-US"}*

::: {#-1588002991 .myid}
[]{#_Toc404785135}[]{#struct_0_53807_x1404_716174800}

**ATM \-- ATM调试命令 \-- debugging atm packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x1186229079}

[**[debugging atm packet]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_1356546727}

[**[undo debugging atm packet]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_53807_x1404_650537162}

[[【视图】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x132548002}

[[用户视图]{style="font-family:宋体"}]{#struct_0_53807_x1404_881624908}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x320843979}

[[network-admin]{lang="EN-US"}]{#struct_0_53807_x1404_x766091350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_53807_x1404_x61238025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_53807_x1404_959959638}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_53807_x1404_x108175521}[：表示指定接口的调试信息开关。支持]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口、]{style="font-family:宋体"}[ATM]{lang="EN-US"}[子接口。]{style="font-family:宋体"}

[*[pvc-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1356612263}[：]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名中不允许使用"]{style="font-family:宋体"}[/]{lang="EN-US"}["和"]{style="font-family:宋体"}[-]{lang="EN-US"}["，如"]{style="font-family:宋体"}[1/20]{lang="EN-US"}["、"]{style="font-family:宋体"}[a-b]{lang="EN-US"}["就不允许作为]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}

[*[vpi/vci]{lang="EN-US"}*]{#struct_0_53807_x1404_x142328941}[：]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[为]{style="font-family:宋体"}[VPI]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[为]{style="font-family:宋体"}[VCI]{lang="EN-US"}[值，取值范围与接口类型相关，请参见"]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-1864992396#_Ref337389143)[[ ]{lang="EN-US" style="color:blue"}]{.underline}[[[[不同[接口[对应的]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}VCI[[的取值范围]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}]{lang="EN-US"}](?-1864992396#_Ref57541113)["。]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[与]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[不能同时为]{style="font-family:宋体"}[0]{lang="EN-US"}[。通常，]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[取值]{style="font-family:宋体"}[0]{lang="EN-US"}[到]{style="font-family:宋体"}[31]{lang="EN-US"}[保留用于特定用途，建议用户不要使用。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_53807_x1404_117814729}

[**[debugging atm packet]{lang="EN-US"}**]{#struct_0_53807_x1404_1468562408}[命令用来打开]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}**[undo ]{lang="EN-US"}[debugging atm packet]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_125451359}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果不指定接口，则打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x202651994}[接口的报文调试信息开关。如果不指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名或者]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值对，则打开指定接口的所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[打开报文调试信息开关之后，就可以观察到]{style="font-family:宋体"}[ATM]{lang="EN-US"}]{#struct_0_53807_x1404_x1188141498}[接口或者]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上收发报文的具体信息，这对于系统排错具有很大的参考作用。对于接收的报文，显示所有接收报文的信息，它可以表明发送端是否正确封装了这些报文，这对于网络设备进行检测很有用处。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging atm packet]{lang="EN-US"}]{#struct_0_53807_x1404_1935614658}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1359624451}[[字段]{style="font-family:黑体"}]{#struct_0_53807_x1404_905396840}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_53807_x1404_1356022440}

[[Received a packet (length=*length*) on interface *interface-name* PVC *vpi/vci*.]{lang="EN-US"}]{#struct_0_53807_x1404_242236383}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_1518044302}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上接收到长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Sent a packet (length=*length*) on interface *interface-name* PVC *vpi/vci*.]{lang="EN-US"}]{#struct_0_53807_x1404_1660147600}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1036680215}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[报]{lang="EN-US" style="font-family:宋体"}[文]{style="font-family:宋体"}

[[Received an IP InARP *type* packet on interface *interface-name* PVC *vpi/vci* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).]{lang="EN-US"}]{#struct_0_53807_x1404_x1924819036}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x339997211}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上接收到长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报]{lang="EN-US" style="font-family:宋体"}[文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[target-ip]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_1356087976}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x485231399}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[[Received an IP InARP *type* packet on interface *interface-name* PVC-group *id* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).]{lang="EN-US"}]{#struct_0_53807_x1404_x485312294}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x2034345124}[下]{style="font-family:宋体"}[PVC-group *id*]{lang="EN-US"}[上接收到长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报]{lang="EN-US" style="font-family:宋体"}[文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[target-ip]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_1397002474}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x1674612868}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[[Sent an IP InARP *type* packet on interface *interface-name* PVC *vpi/vci* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).]{lang="EN-US"}]{#struct_0_53807_x1404_1356153512}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x141506782}[下]{style="font-family:宋体"}[PVC *vpi/vci*]{lang="EN-US"}[上发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报]{lang="EN-US" style="font-family:宋体"}[文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[target-ip]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_1844532629}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x856925701}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[[Sent an IP InARP *type* packet on interface *interface-name* PVC-group *id* (length=*length*, source IP=*source-ip*, target IP=*target-ip*).]{lang="EN-US"}]{#struct_0_53807_x1404_x80565273}

[[在接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_53807_x1404_x1088223125}[下]{style="font-family:宋体"}[PVC-group *id*]{lang="EN-US"}[上发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的]{style="font-family:宋体"}[InARP *type*]{lang="EN-US"}[报]{lang="EN-US" style="font-family:宋体"}[文，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[source-ip]{lang="EN-US"}*[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[target-ip]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[request]{lang="EN-US"}]{#struct_0_53807_x1404_1356219048}[：请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[reply]{lang="EN-US"}]{#struct_0_53807_x1404_x1733798508}[：应答报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_53807_x1404_x889039175}

[[\# Router A]{lang="EN-US"}]{#struct_0_53807_x1404_431035334}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口连接，两端配置好]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，具体配置如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router A]{lang="EN-US"}]{#struct_0_53807_x1404_x1526033874}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_x960429753}

[\[Sysname\] interface atm 2/4/2]{lang="EN-US"}

[\[Sysname-ATM2/4/2\] pvc 10/33]{lang="EN-US"}

[\[Sysname-ATM2/4/2-pvc-10/33\] map ip inarp 1]{lang="EN-US"}

[\[Sysname-ATM2/4/2-pvc-10/33\] quit]{lang="EN-US"}

[\[Sysname-ATM2/4/2\] ip address 10.10.10.11 255.255.255.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router B]{lang="EN-US"}]{#struct_0_53807_x1404_x1832914678}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_53807_x1404_1355760296}

[\[Sysname\] interface atm2/4/3]{lang="EN-US"}

[\[Sysname-ATM2/4/3\] pvc 10/33]{lang="EN-US"}

[\[Sysname-ATM2/4/3-pvc-10/33\] map ip inarp 1]{lang="EN-US"}

[\[Sysname-ATM2/4/3-pvc-10/33\] quit]{lang="EN-US"}

[\[Sysname-ATM2/4/3-pvc-10/33\] ip address 10.10.10.10 255.255.255.0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_53807_x1404_1547707561}[在]{style="font-family:宋体"}[Router A]{lang="EN-US"}[打开所有]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口的报文调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging atm packet]{lang="EN-US"}]{#struct_0_53807_x1404_414186599}

[\*Dec 24 09:45:46:236 2012 Sysname ATM/7/PACKET: -MDC=1;]{lang="EN-US"}

[Sent an IP InARP request packet on interface ATM2/4/2 PVC 10/33 (length=16, source IP =10.10.10.11, target IP=0.0.0.0).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_53807_x1404_286904211}*[发送了]{style="font-family:宋体"}[InARP]{lang="EN-US"}[请求报文，长度]{style="font-family:宋体"}[16]{lang="EN-US"}[，源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.10.11]{lang="EN-US"}[，目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}*

[ ]{lang="EN-US"}
