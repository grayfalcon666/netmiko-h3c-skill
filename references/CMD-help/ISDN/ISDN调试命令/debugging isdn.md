::: {#-669030716 .myid}
[]{#_Toc404785032}[]{#struct_0_15329_14513_x2046020894}

**ISDN \-- ISDN调试命令 \-- debugging isdn**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_15329_14513_x1507958445}

[**[debugging isdn]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_15329_14513_2090368139}**[cc]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[q921]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[q931]{lang="EN-US"}**[ } \[ ]{lang="EN-US"}**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type]{lang="EN-US"}*[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo debugging isdn]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_15329_14513_1358840487}**[cc]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[q921]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[q931]{lang="EN-US"}**[ } \[ ]{lang="EN-US"}**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type]{lang="EN-US"}*[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}*[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15329_14513_486679569}

[[用户视图]{style="font-family:宋体"}]{#struct_0_15329_14513_1835501100}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15329_14513_1518641117}

[[network-admin]{lang="EN-US"}]{#struct_0_15329_14513_1283297352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15329_14513_x225913464}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15329_14513_708665224}

[**[cc]{lang="EN-US"}**]{#struct_0_15329_14513_2022011788}[：呼叫控制调试信息开关。]{style="font-family:宋体"}

[**[q921]{lang="EN-US"}**]{#struct_0_15329_14513_x172319758}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[的]{style="font-family:宋体"}[Q921]{lang="EN-US"}[数据链路层协议调试信息开关。]{style="font-family:宋体"}

[**[q931]{lang="EN-US"}**]{#struct_0_15329_14513_1358774951}[：]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[的]{style="font-family:宋体"}[Q931]{lang="EN-US"}[网络层协议调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_15329_14513_x1511894455}[：指定接口的调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_15329_14513_x1098978015}

[**[debugging isdn]{lang="EN-US"}**]{#struct_0_15329_14513_814752975}[命令用来打开]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[debugging isdn]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_15329_14513_x131893624}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[如果不指定接口，将打开所有]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_15329_14513_x921413708}[接口的调试信息开关。]{style="font-family:宋体"}

[]{#struct_0_15329_14513_1415143209}[]{#_Ref155675443}[]{#_Toc130718928}[表1-1 ]{lang="EN-US"}[debugging isdn cc]{lang="EN-US"}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_142601206}[[字段]{style="font-family:黑体"}]{#struct_0_15329_14513_x1708677323}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15329_14513_1632961463}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_1358316200}

[[ISDN]{lang="EN-US"}]{#struct_0_15329_14513_1660643730}[呼叫控制]{style="font-family:宋体"}

[[DVA]{lang="EN-US"}]{#struct_0_15329_14513_x1023626919}

[[语音拨号模块，]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_15329_14513_x1960984958}[承载语音业务时的上层应用（]{style="font-family:宋体"}[User]{lang="EN-US"}[）]{style="font-family:宋体"}

[[DDR]{lang="EN-US"}]{#struct_0_15329_14513_x1829306748}

[[数据拨号模块，]{style="font-family:宋体"}[ISDN]{lang="EN-US"}]{#struct_0_15329_14513_x1854637885}[承载数据业务时的上层应用（]{style="font-family:宋体"}[User]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ISDN_SETUP_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1466178588}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_1358250664}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[请求发出]{style="font-family:宋体"}[SETUP]{lang="EN-US"}[呼叫]{style="font-family:宋体"}

[[ISDN_CONN_REQ]{lang="EN-US"}]{#struct_0_15329_14513_98313557}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_1687207746}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[请求发送]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_DISC_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x721169016}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_x1911285178}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送拆链消息给对端]{style="font-family:宋体"}

[[ISDN_DISC_RES]{lang="EN-US"}]{#struct_0_15329_14513_1358185128}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_x1489838615}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送对之前拆链指示的回应]{style="font-family:宋体"}

[[ISDN_CALLPROC_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x170122710}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_2060512051}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送]{style="font-family:宋体"}[CALL-PROCEEDING]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_PROGRESS_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x231591769}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_x56201765}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送]{style="font-family:宋体"}[PROGRESS]{lang="EN-US"}[消息给对端]{style="font-family:宋体"}

[[ISDN_ALERTING_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1358119592}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_437605672}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送]{style="font-family:宋体"}[ALERTING]{lang="EN-US"}[消息给对端]{style="font-family:宋体"}

[[ISDN_INFORMATION_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1250174044}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_x1954058919}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送]{style="font-family:宋体"}[INFORMATION]{lang="EN-US"}[消息给对端]{style="font-family:宋体"}

[[ISDN_FACILITY_REQ]{lang="EN-US"}]{#struct_0_15329_14513_852824508}

[[USER]{lang="EN-US"}]{#struct_0_15329_14513_1358054056}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送]{style="font-family:宋体"}[FACILITY]{lang="EN-US"}[消息给对端]{style="font-family:宋体"}

[[ISDN_SETUP_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1080405336}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_2146415738}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收呼叫]{style="font-family:宋体"}

[[ISDN_CONN_IND]{lang="EN-US"}]{#struct_0_15329_14513_x929441269}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_1357988520}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[CONNECT]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_CONN_CFM]{lang="EN-US"}]{#struct_0_15329_14513_x1335703360}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x286870076}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[CONNECT-ACK]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_FACILITY_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1631566485}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_530125313}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[FACILITY]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_DISC_IND]{lang="EN-US"}]{#struct_0_15329_14513_1357922984}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x547996996}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的拆链消息]{style="font-family:宋体"}

[[ISDN_CALLPROC_IND]{lang="EN-US"}]{#struct_0_15329_14513_x42445289}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x936580459}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[CALL-PROCEEDING]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_PROGRESS_IND]{lang="EN-US"}]{#struct_0_15329_14513_1357857448}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x1256524848}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[PROGRESS]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[ISDN_ALERTING_IND]{lang="EN-US"}]{#struct_0_15329_14513_1027771724}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x12474340}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收到对端的]{style="font-family:宋体"}[ALERTING]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1358840488}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_486220817}[和]{style="font-family:宋体"}[Q931]{lang="EN-US"}[之间呼叫建立请求的原语]{style="font-family:宋体"}

[[CCL3_DL_ESTABLISH_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1356372538}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x1712309247}[通知]{style="font-family:宋体"}[Q931]{lang="EN-US"}[进行二层建链]{style="font-family:宋体"}

[[CCL3_DL_ESTABLISH_CONFIRM]{lang="EN-US"}]{#struct_0_15329_14513_1358774952}

[[二层报给]{style="font-family:宋体"}[Q931]{lang="EN-US"}]{#struct_0_15329_14513_x1511697847}[的消息，会给]{style="font-family:宋体"}[CC]{lang="EN-US"}[报这个消息]{style="font-family:宋体"}

[[CCL3_PROCEEDING_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x57158061}

[[发]{style="font-family:宋体"}[Call Proceeding]{lang="EN-US"}]{#struct_0_15329_14513_x1370567152}[消息给网络]{style="font-family:宋体"}

[[CCL3_ALERTING_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1708511122}

[[发]{style="font-family:宋体"}[Alerting]{lang="EN-US"}]{#struct_0_15329_14513_x800847518}[消息给网络]{style="font-family:宋体"}

[[CCL3_PROGRESS_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1113608118}

[[发]{style="font-family:宋体"}[Progress]{lang="EN-US"}]{#struct_0_15329_14513_x1370632688}[消息给网络]{style="font-family:宋体"}

[[CCL3_SETUP_RES]{lang="EN-US"}]{#struct_0_15329_14513_865448828}

[[发]{style="font-family:宋体"}[Connect]{lang="EN-US"}]{#struct_0_15329_14513_254665477}[消息给网络]{style="font-family:宋体"}

[[CCL3_SETUPACK_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1370698224}

[[发]{style="font-family:宋体"}[Setup Acknowledge]{lang="EN-US"}]{#struct_0_15329_14513_x62863546}[消息给网络]{style="font-family:宋体"}

[[CCL3_SETUPCOMP_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x212622390}

[[发]{style="font-family:宋体"}[Connect Acknowledge]{lang="EN-US"}]{#struct_0_15329_14513_x1848907344}[消息给网络]{style="font-family:宋体"}

[[CCL3_DISCONNECT_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1370763760}

[[发]{style="font-family:宋体"}[Disconnect]{lang="EN-US"}]{#struct_0_15329_14513_x1077012062}[消息给网络]{style="font-family:宋体"}

[[CCL3_RELEASE_REQ]{lang="EN-US"}]{#struct_0_15329_14513_709581014}

[[发]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_15329_14513_x1370829296}[消息给网络]{style="font-family:宋体"}

[[CCL3_RELEASECOM_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1823399223}

[[发]{style="font-family:宋体"}[Release Complete]{lang="EN-US"}]{#struct_0_15329_14513_x1124972124}[消息给网络]{style="font-family:宋体"}

[[CCL3_TIME_OUT_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1370894832}

[[收到网络]{style="font-family:宋体"}[timeout]{lang="EN-US"}]{#struct_0_15329_14513_367844870}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_IND]{lang="EN-US"}]{#struct_0_15329_14513_1725663280}

[[收到网络]{style="font-family:宋体"}[Setup]{lang="EN-US"}]{#struct_0_15329_14513_x1370960368}[消息]{style="font-family:宋体"}

[[CCL3_PROCEEDING_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1134641538}

[[收到网络]{style="font-family:宋体"}[Call Proceeding]{lang="EN-US"}]{#struct_0_15329_14513_x741793211}[消息]{style="font-family:宋体"}

[[CCL3_ALERTING_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1371025904}

[[收到网络]{style="font-family:宋体"}[Alerting]{lang="EN-US"}]{#struct_0_15329_14513_962792535}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_COMPLETE_ERR]{lang="EN-US"}]{#struct_0_15329_14513_x1985153790}

[[收到网络]{style="font-family:宋体"}[setup complete err]{lang="EN-US"}]{#struct_0_15329_14513_x1370042864}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_CONFIRM_ERR]{lang="EN-US"}]{#struct_0_15329_14513_1051998011}

[[收到网络]{style="font-family:宋体"}[setup confirm err]{lang="EN-US"}]{#struct_0_15329_14513_x1370108400}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_CONFIRM]{lang="EN-US"}]{#struct_0_15329_14513_1467558295}

[[收到网络]{style="font-family:宋体"}[setup confirm]{lang="EN-US"}]{#struct_0_15329_14513_x822694310}[消息]{style="font-family:宋体"}

[[CCL3_SETUP_COMPLETE]{lang="EN-US"}]{#struct_0_15329_14513_x1370567151}

[[收到网络]{style="font-family:宋体"}[setup complete]{lang="EN-US"}]{#struct_0_15329_14513_1020372233}[消息]{style="font-family:宋体"}

[[CCL3_DISCONNECT_IND]{lang="EN-US"}]{#struct_0_15329_14513_x62382788}

[[收到网络]{style="font-family:宋体"}[Disconnect]{lang="EN-US"}]{#struct_0_15329_14513_x1370632687}[消息]{style="font-family:宋体"}

[[CCL3_RELEASE_IND]{lang="EN-US"}]{#struct_0_15329_14513_818394661}

[[收到网络]{style="font-family:宋体"}[Release]{lang="EN-US"}]{#struct_0_15329_14513_x1370698223}[消息]{style="font-family:宋体"}

[[CCL3_RELEASE_CONFIRM]{lang="EN-US"}]{#struct_0_15329_14513_1503220395}

[[收到网络]{style="font-family:宋体"}[Release Complete]{lang="EN-US"}]{#struct_0_15329_14513_1589716004}[消息]{style="font-family:宋体"}

[[CCL3_RELEASE_CFM_ERR]{lang="EN-US"}]{#struct_0_15329_14513_x1370763759}

[[T308]{lang="EN-US"}]{#struct_0_15329_14513_845367775}[二次超时向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发该原语]{style="font-family:宋体"}

[[CCL3_SETUPACK_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1370829295}

[[收到网络]{style="font-family:宋体"}[Setup Acknowledge]{lang="EN-US"}]{#struct_0_15329_14513_905484132}[消息]{style="font-family:宋体"}

[[CCL3_PROGRESS_IND]{lang="EN-US"}]{#struct_0_15329_14513_x54931704}

[[收到网络]{style="font-family:宋体"}[Progress]{lang="EN-US"}]{#struct_0_15329_14513_x1370894831}[消息]{style="font-family:宋体"}

[[CCL3_RELEASECOM_IND]{lang="EN-US"}]{#struct_0_15329_14513_1933928811}

[[收到网络]{style="font-family:宋体"}[Release Complete]{lang="EN-US"}]{#struct_0_15329_14513_x1370960367}[消息]{style="font-family:宋体"}

[[CCL3_INFO_IND]{lang="EN-US"}]{#struct_0_15329_14513_881781097}

[[收到网络]{style="font-family:宋体"}[info]{lang="EN-US"}]{#struct_0_15329_14513_x1371025903}[消息]{style="font-family:宋体"}

[[PRIM_SETUP_CFM]{lang="EN-US"}]{#struct_0_15329_14513_x959521766}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_1514241489}[向]{style="font-family:宋体"}[USER]{lang="EN-US"}[指示接收呼叫确认]{style="font-family:宋体"}

[[CC\<-DDR]{lang="EN-US"}]{#struct_0_15329_14513_x1370042863}

[[DDR]{lang="EN-US"}]{#struct_0_15329_14513_1811512898}[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送原语]{style="font-family:宋体"}

[[CC-\>Q931]{lang="EN-US"}]{#struct_0_15329_14513_x1370108399}

[[CC]{lang="EN-US"}]{#struct_0_15329_14513_x1618145239}[向]{style="font-family:宋体"}[Q931]{lang="EN-US"}[发送原语]{style="font-family:宋体"}

[[CallID]{lang="EN-US"}]{#struct_0_15329_14513_x1370567154}

[[由]{style="font-family:宋体"}[CC]{lang="EN-US"}]{#struct_0_15329_14513_1423656760}[模块分配标识呼叫的唯一性的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号]{style="font-family:宋体"}

[[PortID]{lang="EN-US"}]{#struct_0_15329_14513_x1370632690}

[[端口]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_15329_14513_1221744724}[，即接口索引]{style="font-family:宋体"}

[[CES]{lang="EN-US"}]{#struct_0_15329_14513_x947035883}

[[连接点标识符]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370698226}

[[ServiceType]{lang="EN-US"}]{#struct_0_15329_14513_1099935868}

[[服务类型]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370763762}

[[Channel]{lang="EN-US"}]{#struct_0_15329_14513_2055155820}

[[通道编号]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370829298}

[[IsCompleted]{lang="EN-US"}]{#struct_0_15329_14513_952538299}

[[是否发送完全]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370894834}

[[SN_COM]{lang="EN-US"}]{#struct_0_15329_14513_1530644284}

[[发送完全信息单元]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370960370}

[[Cause]{lang="EN-US"}]{#struct_0_15329_14513_x1490937434}

[[原因值信息单元]{style="font-family:宋体"}]{#struct_0_15329_14513_x1371025906}

[[bearer]{lang="EN-US"}]{#struct_0_15329_14513_x200006879}

[[承载能力信息单元]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370042866}

[[chan_id]{lang="EN-US"}]{#struct_0_15329_14513_x2080169871}

[[通路标识信息单元]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370108402}

[[called_n]{lang="EN-US"}]{#struct_0_15329_14513_x1664609587}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370567153}

[[szCalledNumProperty]{lang="EN-US"}]{#struct_0_15329_14513_x142427181}

[[被叫号码（信息单元）属性字段]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370632689}

[[szCallingNumProperty]{lang="EN-US"}]{#struct_0_15329_14513_x700635113}

[[主叫号码（信息单元）属性字段]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370698225}

[[szCalledNum]{lang="EN-US"}]{#struct_0_15329_14513_x1628947487}

[[被叫号码（信息单元）号码信息]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370763761}

[[szCallingNum]{lang="EN-US"}]{#struct_0_15329_14513_489071879}

[[主叫号码（信息单元）号码信息]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370829297}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging isdn q931]{lang="EN-US"}]{#struct_0_15329_14513_x257315282}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_157856628}[[字段]{style="font-family:黑体"}]{#struct_0_15329_14513_494447401}

[[描述]{style="font-family:黑体"}]{#struct_0_15329_14513_1677155564}

[[DL_I_Data_Req]{lang="EN-US"}]{#struct_0_15329_14513_1865913022}

[[Q931]{lang="EN-US"}]{#struct_0_15329_14513_25800820}[向]{style="font-family:宋体"}[Q921]{lang="EN-US"}[发送报文请求]{style="font-family:宋体"}

[[DL_I_Data_Ind]{lang="IT"}]{#struct_0_15329_14513_x1370894833}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1198239071}[向]{style="font-family:宋体"}[Q931]{lang="EN-US"}[上送报文指示]{style="font-family:宋体"}

[[CES]{lang="EN-US"}]{#struct_0_15329_14513_x1583726106}

[[连接点标识符]{style="font-family:宋体"}]{#struct_0_15329_14513_1812164582}

[[SETUP]{lang="EN-US"}]{#struct_0_15329_14513_1115608938}

[[发给程控交换机的呼叫建立请求]{style="font-family:宋体"}]{#struct_0_15329_14513_x1643992648}

[[cr_length]{lang="EN-US"}]{#struct_0_15329_14513_x1370960369}

[[呼叫参考值长度]{style="font-family:宋体"}]{#struct_0_15329_14513_431442403}

[[cr]{lang="EN-US"}]{#struct_0_15329_14513_x1035287791}

[[呼叫参考值]{style="font-family:宋体"}]{#struct_0_15329_14513_275016116}

[[CS_XX]{lang="EN-US"}]{#struct_0_15329_14513_x850484339}

[[当前呼叫状态]{style="font-family:宋体"}]{#struct_0_15329_14513_336732190}

[[send_comp]{lang="EN-US"}]{#struct_0_15329_14513_x1371025905}

[[号码发送完全]{style="font-family:宋体"}]{#struct_0_15329_14513_x1766090820}

[[called_n]{lang="EN-US"}]{#struct_0_15329_14513_814229282}

[[被叫号码]{style="font-family:宋体"}]{#struct_0_15329_14513_528118893}

[[Call Reference]{lang="EN-US"}]{#struct_0_15329_14513_x1594637962}

[[呼叫参考值]{style="font-family:宋体"}]{#struct_0_15329_14513_x140514758}

[[CALL_PROC]{lang="EN-US"}]{#struct_0_15329_14513_x1370042865}

[[呼叫进行时]{style="font-family:宋体"}]{#struct_0_15329_14513_x1676885344}

[[ALERTING]{lang="EN-US"}]{#struct_0_15329_14513_466496843}

[[振铃原语]{style="font-family:宋体"}]{#struct_0_15329_14513_x866805590}

[[prog_ind]{lang="EN-US"}]{#struct_0_15329_14513_x1370108401}

[[呼叫进程指示]{style="font-family:宋体"}]{#struct_0_15329_14513_x1261325060}

[[CONN]{lang="EN-US"}]{#struct_0_15329_14513_1407856983}

[[Q931]{lang="EN-US"}]{#struct_0_15329_14513_1116736544}[呼叫连接请求消息]{style="font-family:宋体"}

[[CONNECT_ACK]{lang="EN-US"}]{#struct_0_15329_14513_x1370567156}

[[Q931]{lang="EN-US"}]{#struct_0_15329_14513_260857346}[呼叫连接应答消息]{style="font-family:宋体"}

[[date/time]{lang="EN-US"}]{#struct_0_15329_14513_1241162482}

[[日期]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15329_14513_1894210169}[时间]{style="font-family:宋体"}

[[Q931-\>Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1900586767}

[[Q931]{lang="EN-US"}]{#struct_0_15329_14513_x1370632692}[向]{style="font-family:宋体"}[Q921]{lang="EN-US"}[发送原语]{style="font-family:宋体"}

[[Q921-\>Q931]{lang="EN-US"}]{#struct_0_15329_14513_58945310}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_732091350}[向]{style="font-family:宋体"}[Q931]{lang="EN-US"}[发送原语]{style="font-family:宋体"}

[[T303]{lang="EN-US"}]{#struct_0_15329_14513_x14911212}

[[Q931 T303]{lang="EN-US"}]{#struct_0_15329_14513_x1370698228}[定时器]{style="font-family:宋体"}

[[T310]{lang="EN-US"}]{#struct_0_15329_14513_x2032232014}

[[Q931 T310]{lang="EN-US"}]{#struct_0_15329_14513_972745290}[定时器]{style="font-family:宋体"}

[[ISDN L3 timer T303 started]{lang="EN-US"}]{#struct_0_15329_14513_461126201}

[[Q931 T303]{lang="EN-US"}]{#struct_0_15329_14513_x1370763764}[定时器开始运行]{style="font-family:宋体"}

[[ISDN Layer 3 call state change]{lang="EN-US"}]{#struct_0_15329_14513_892356406}

[[Q931]{lang="EN-US"}]{#struct_0_15329_14513_x1817085258}[呼叫状态变化]{style="font-family:宋体"}

[[ISDN L3 timer T303 stopped]{lang="EN-US"}]{#struct_0_15329_14513_246514272}

[[Q931 T303]{lang="EN-US"}]{#struct_0_15329_14513_x1370829300}[定时器停止]{style="font-family:宋体"}

[[ISDN L3 timer T310 started]{lang="EN-US"}]{#struct_0_15329_14513_1308178834}

[[Q931 T310]{lang="EN-US"}]{#struct_0_15329_14513_x1907701598}[定时器开始运行]{style="font-family:宋体"}

[[ISDN L3 timer T310 stopped]{lang="EN-US"}]{#struct_0_15329_14513_x1370894836}

[[Q931 T310]{lang="EN-US"}]{#struct_0_15329_14513_x1601523598}[定时器停止]{style="font-family:宋体"}

[[INFORMATION]{lang="EN-US"}]{#struct_0_15329_14513_1214395725}

[[SPID]{lang="EN-US"}]{#struct_0_15329_14513_x1370960372}[自协商时发送的]{style="font-family:宋体"}[information]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Spid]{lang="EN-US"}]{#struct_0_15329_14513_1641230448}

[[消息中含有的]{style="font-family:宋体"}[SPID]{lang="EN-US"}]{#struct_0_15329_14513_x1517206501}[信息单元]{style="font-family:宋体"}

[[end_id]{lang="EN-US"}]{#struct_0_15329_14513_1349925205}

[[SPID]{lang="EN-US"}]{#struct_0_15329_14513_x1371025908}[协商完成时]{style="font-family:宋体"}[information]{lang="EN-US"}[消息中携带该信息单元（目前该信息单元没有实际用途）]{style="font-family:宋体"}

[[其它信息单元字段描述请参考]{style="font-family:宋体"}]{#struct_0_15329_14513_x1719036653}[[表]{style="font-family:宋体"}[1-1]{lang="EN-US"}](http://press.h3c.com/data/infoblade/Comware%20V5平台中文/1.1.05%20二层技术-广域网接入/1.1.05.09%20ISDN/ISDN%20Debug.htm#_Ref155675443)

[[-]{lang="EN-US"}]{#struct_0_15329_14513_x967149819}

[ ]{lang="EN-US"}

[]{#struct_0_15329_14513_80605317}[[表1-3 ]{lang="EN-US"}[debugging Isdn q921]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_184381110}[[字段]{style="font-family:黑体"}]{#struct_0_15329_14513_x1370042868}

[[描述]{style="font-family:黑体"}]{#struct_0_15329_14513_x561140097}

[[Net Tx]{lang="EN-US"}]{#struct_0_15329_14513_x1094836041}

[[网络侧发送报文]{style="font-family:宋体"}]{#struct_0_15329_14513_399389171}

[[Net Rx]{lang="EN-US"}]{#struct_0_15329_14513_x16721369}

[[网络侧接收报文]{style="font-family:宋体"}]{#struct_0_15329_14513_x1570472342}

[[User Tx]{lang="EN-US"}]{#struct_0_15329_14513_x1512042389}

[[用户侧发送报文]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370108404}

[[User Rx]{lang="EN-US"}]{#struct_0_15329_14513_x501810173}

[[用户侧接收报文]{style="font-family:宋体"}]{#struct_0_15329_14513_1693315556}

[[I]{lang="PT-BR"}]{#struct_0_15329_14513_1956624035}

[[信息帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x1038593440}

[[UI]{lang="PT-BR"}]{#struct_0_15329_14513_1934036390}

[[无编号信息帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370567155}

[[SABME]{lang="PT-BR"}]{#struct_0_15329_14513_x1305226595}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_257690823}[建链请求帧]{style="font-family:宋体"}

[[DISC]{lang="PT-BR"}]{#struct_0_15329_14513_242582115}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_589077239}[拆链请求帧]{style="font-family:宋体"}

[[UA]{lang="PT-BR"}]{#struct_0_15329_14513_x1370632691}

[[无编号确认帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x344339217}

[[REJ]{lang="PT-BR"}]{#struct_0_15329_14513_1764829793}

[[拒绝帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x700570993}

[[RR]{lang="PT-BR"}]{#struct_0_15329_14513_x391319223}

[[接收准备好帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x1370698227}

[[RNR]{lang="EN-US"}]{#struct_0_15329_14513_x466148073}

[[接收未准备好帧]{style="font-family:宋体"}]{#struct_0_15329_14513_x1222345756}

[[sapi]{lang="EN-US"}]{#struct_0_15329_14513_1266316778}

[[服务接入点标识号]{style="font-family:宋体"}]{#struct_0_15329_14513_1944719248}

[[tei]{lang="EN-US"}]{#struct_0_15329_14513_x1370763763}

[[终端端点标识符（]{style="font-family:宋体"}[TEI]{lang="EN-US"}]{#struct_0_15329_14513_x673727535}[）值]{style="font-family:宋体"}

[[ns]{lang="EN-US"}]{#struct_0_15329_14513_x275363419}

[[发送序号]{style="font-family:宋体"}]{#struct_0_15329_14513_283080378}

[[nr]{lang="EN-US"}]{#struct_0_15329_14513_x1370829299}

[[接收序号]{style="font-family:宋体"}]{#struct_0_15329_14513_x1776345056}

[[p]{lang="EN-US"}]{#struct_0_15329_14513_367648219}

[[询问比特位值]{style="font-family:宋体"}]{#struct_0_15329_14513_x527296969}

[[c/r]{lang="EN-US"}]{#struct_0_15329_14513_x1370894835}

[[命令]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15329_14513_x35439657}[响应比特位值]{style="font-family:宋体"}

[[p/f]{lang="EN-US"}]{#struct_0_15329_14513_x30787955}

[[询问]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15329_14513_670174036}[结束比特位值]{style="font-family:宋体"}

[[Len]{lang="EN-US"}]{#struct_0_15329_14513_x1370960371}

[[用户侧发送的报文长度和内容]{style="font-family:宋体"}]{#struct_0_15329_14513_75146507}

[[Status]{lang="EN-US"}]{#struct_0_15329_14513_x697174884}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x252446715}[状态]{style="font-family:宋体"}

[[TIMER_RECOVERY]{lang="EN-US"}]{#struct_0_15329_14513_x1371025907}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_1366077062}[状态机中的链路恢复状态]{style="font-family:宋体"}

[[MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}]{#struct_0_15329_14513_978813967}

[[多帧建链]{style="font-family:宋体"}]{#struct_0_15329_14513_x306748126}

[[Q921_DL_ESTABLISH_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x1370042867}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x514085930}[建链请求]{style="font-family:宋体"}

[[Q921_DL_DATA_REQ]{lang="EN-US"}]{#struct_0_15329_14513_1181233036}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1370108403}[需确认消息]{style="font-family:宋体"}[请求]{style="font-family:宋体"}

[[Q921_DL_RELEASE_REQ]{lang="EN-US"}]{#struct_0_15329_14513_x98525646}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_1238838648}[拆链请求]{style="font-family:宋体"}

[[Q921_DL_UNIT_DATA_REQ]{lang="EN-US"}]{#struct_0_15329_14513_945862895}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195516789}[未确认的消息]{style="font-family:宋体"}[请求]{style="font-family:宋体"}

[[Q921_DL_ESTABLISH_IND]{lang="EN-US"}]{#struct_0_15329_14513_x1653738322}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1207528339}[建链指示]{style="font-family:宋体"}

[[Q921_DL_ESTABLISH_CFM]{lang="EN-US"}]{#struct_0_15329_14513_195451253}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1338361033}[建链证实]{style="font-family:宋体"}

[[Q921_DL_DATA_IND]{lang="EN-US"}]{#struct_0_15329_14513_1302606295}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195385717}[需确认的消息指示]{style="font-family:宋体"}

[[Q921_DL_RELEASE_IND]{lang="EN-US"}]{#struct_0_15329_14513_1557656529}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1009096406}[拆链指示]{style="font-family:宋体"}

[[Q921_DL_RELEASE_CFM]{lang="EN-US"}]{#struct_0_15329_14513_195320181}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_1571205303}[拆链证实]{style="font-family:宋体"}

[[Q921_DL_UNIT_DATA_IND]{lang="EN-US"}]{#struct_0_15329_14513_2135593753}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195254645}[未确认的消息指示]{style="font-family:宋体"}

[[Q921_LAPD_DATA_REQ]{lang="EN-US"}]{#struct_0_15329_14513_783706313}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1355583443}[向物理层发送]{style="font-family:宋体"}[需确认的消息]{style="font-family:宋体"}[请求]{style="font-family:宋体"}

[[Q921_LAPD_DATA_IND]{lang="EN-US"}]{#struct_0_15329_14513_195189109}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1447055499}[收到物理层发送的]{style="font-family:宋体"}[需确认的消息指示]{style="font-family:宋体"}

[[Q921_LAPD_DEACTIVE_IND]{lang="EN-US"}]{#struct_0_15329_14513_52618336}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195123573}[收到去激活指示]{style="font-family:宋体"}

[[Q921_LAPD_ACTIVE_IND]{lang="EN-US"}]{#struct_0_15329_14513_2083315273}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x859066030}[收到激活指示]{style="font-family:宋体"}

[[Q921_LAPD_ACTIVING_IND]{lang="EN-US"}]{#struct_0_15329_14513_195058037}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1838668695}[收到激活中指示]{style="font-family:宋体"}

[[Q921_MDL_TEI_IND]{lang="EN-US"}]{#struct_0_15329_14513_196041077}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_85873477}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[分配指示]{style="font-family:宋体"}

[[Q921_MDL_REMOVE_IND]{lang="EN-US"}]{#struct_0_15329_14513_x710031792}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195975541}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[移除指示]{style="font-family:宋体"}

[[Q921_MDL_TEI_FAIL_IND]{lang="EN-US"}]{#struct_0_15329_14513_1133108650}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_2056763865}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[分配失败指示]{style="font-family:宋体"}

[[Q921_MDL_TEI_REQ]{lang="EN-US"}]{#struct_0_15329_14513_195516790}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_302576821}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[TEI]{lang="EN-US"}[分配请求]{style="font-family:宋体"}

[[Q921_MDL_ERROR_IND]{lang="EN-US"}]{#struct_0_15329_14513_195451254}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_x1338361036}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[错误]{style="font-family:宋体"}[指示]{style="font-family:宋体"}

[[Q921_MDL_UNIT_DATA_IND]{lang="EN-US"}]{#struct_0_15329_14513_543091408}

[[Q921]{lang="EN-US"}]{#struct_0_15329_14513_195385718}[与]{style="font-family:宋体"}[LME]{lang="EN-US"}[间的]{style="font-family:宋体"}[未确认消息指示]{style="font-family:宋体"}

[[其它信息单元字段描述请参考]{style="font-family:宋体"}]{#struct_0_15329_14513_1557656532}[[表]{style="font-family:宋体"}[1-1]{lang="EN-US"}](http://press.h3c.com/data/infoblade/Comware%20V5平台中文/1.1.05%20二层技术-广域网接入/1.1.05.09%20ISDN/ISDN%20Debug.htm#_Ref155675443)

[[-]{lang="EN-US"}]{#struct_0_15329_14513_195320182}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15329_14513_1571205302}

[[\# Router A]{lang="EN-US"}]{#struct_0_15329_14513_2135528217}[的配置如下：]{style="font-family:宋体"}

[[\<RouterA\> system-view]{lang="EN-US"}]{#struct_0_15329_14513_x1966166636}

[\[RouterA\] dialer-group 1 rule ip permit]{lang="EN-US"}

[\[RouterA\] interface Serial2/3/0:15]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] link-protocol ppp]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] ip address 3.1.1.19 255.255.255.0]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] dialer circular enable]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] dialer-group 1]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] dialer number 666]{lang="EN-US"}

[\[RouterA-Serial2/3/0:15\] return]{lang="EN-US"}

[[\# Router B]{lang="EN-US"}]{#struct_0_15329_14513_x1784294675}[的配置如下：]{style="font-family:宋体"}

[[\<RouterB\> system-view]{lang="EN-US"}]{#struct_0_15329_14513_195254646}

[\[RouterB\] interface Serial2/3/0:15]{lang="EN-US"}

[\[RouterB-Serial2/3/0:15\] link-protocol ppp]{lang="EN-US"}

[\[RouterB-Serial2/3/0:15\] ip address 3.1.31.1 255.255.255.0]{lang="EN-US"}

[\[RouterB-Serial2/3/0:15\] dialer circular enable]{lang="EN-US"}

[\[RouterB-Serial2/3/0:15\] dialer-group 1]{lang="EN-US"}

[\[RouterB-Serial2/3/0:15\] quit]{lang="EN-US"}

[\[RouterB\] dialer-group 1 rule ip permit]{lang="EN-US"}

[[\# Router A]{lang="EN-US"}]{#struct_0_15329_14513_783706310}[与]{style="font-family:宋体"}[Router B]{lang="EN-US"}[通过程控交换机相连。打开]{style="font-family:宋体"}[Router A]{lang="EN-US"}[的数据报文调试开关]{style="font-family:宋体"}**[debugging isdn cc]{lang="EN-US"}**[、]{style="font-family:宋体"}**[debugging isdn q921]{lang="EN-US"}**[和]{style="font-family:宋体"}**[debugging isdn q931]{lang="EN-US"}**[。从]{style="font-family:宋体"}[Router A ping Router B]{lang="EN-US"}[，调试信息分析如下：]{style="font-family:宋体"}

[[\<RouterA\> debugging isdn cc]{lang="EN-US"}]{#struct_0_15329_14513_x1355583440}

[\<RouterA\> debugging isdn q921]{lang="EN-US"}

[\<RouterA\> debugging isdn q931]{lang="EN-US"}

[\<RouterA\> ping -t 1 -i Dialer 1 -c 1 3.1.31.1]{lang="EN-US"}

[\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/CC: Serial2/3/0:15]{lang="EN-US"}

[  CC\<-DDR: ISDN_SETUP_REQ]{lang="EN-US"}

[  CallID=0xffff, PortID=0x11505, ServiceType=0x8, Channel=0x0, IsCompleted=0x1, Cause=0x00(No0), szCalledNumProperty=0x1 0x0 0x0, szCalledNum=4021]{lang="EN-US"}

[*[// DDR]{lang="EN-US"}*]{#struct_0_15329_14513_999564380}*[向]{style="font-family:宋体"}[CC]{lang="EN-US"}[发送请求，要求建立]{style="font-family:宋体"}[ISDN]{lang="EN-US"}[连接]{style="font-family:宋体"}*

[[\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/CC: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x508553150}

[  CC-\>Q931: CCL3_SETUP_REQ]{lang="EN-US"}

[  CallID=0xffff, PortID=0x1505, CES=0x1, \*SN_COM=a1, \*bearer= 04 02 88 90, \*chan_id= 18 03 a1 83 81, \*called_n= 70 05 80 34 30 32 31]{lang="EN-US"}

[*[// CC]{lang="EN-US"}*]{#struct_0_15329_14513_195189110}*[向]{style="font-family:宋体"}[Q931]{lang="EN-US"}[发送请求，要求网络层建立连接]{style="font-family:宋体"}*

[[\*Dec 17 03:45:59:986 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_509259630}

[  Q931-\>Q921: DL_I_Data_Req, CES=1]{lang="EN-US"}

[  cr_length=2, cr= 02 00 93, SETUP, \*send_comp=a1, \*bearer= 04 02 88 90, \*chan_id= 18 03 a1 83 81, \*called_n= 70 05 80 34 30 32 31]{lang="EN-US"}

[*[// Q931]{lang="EN-US"}*]{#struct_0_15329_14513_x1143918268}*[向]{style="font-family:宋体"}[Q921]{lang="EN-US"}[发送请求，要求建立链路层连接]{style="font-family:宋体"}*

[[\*Dec 17 03:45:59:987 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_293825132}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=26 00 01 90 90 08 02 00 93 05 A1 04 02 88 90 18 03 A1 83 81 70 05 80 34 30 32 31]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=0, I, ns=48, nr=48, p=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_1383044027}*[向对端发送]{style="font-family:宋体"}[I]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:45:59:988 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_747260384}

[  ISDN L3 timer T303 started, Call Reference=0x0093.]{lang="EN-US"}

[*[// Q931]{lang="EN-US"}*]{#struct_0_15329_14513_1090227954}*[启动定时器]{style="font-family:宋体"}*

[[\*Dec 17 03:45:59:988 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_195123574}

[  ISDN Layer 3 call state change: CS_NULL-\>CS_CALL_INITIATED]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:45:59:996 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=4 00 01 01 92]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=0, RR, nr=49, p/f=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_2083315280}*[收到]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:026 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x859262627}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=14 02 01 90 92 08 02 80 93 02 18 03 A9 83 8F]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=1, I, ns=48, nr=49, p=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_1318521007}*[收到对端发送的]{style="font-family:宋体"}[I]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x926117913}

[  Q921-\>Q931: DL_I_Data_Ind, CES=1]{lang="EN-US"}

[  cr_length=2, cr= 02 80 93, CALL_PROC, \*chan_id= 18 03 a9 83 8f]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x1656255429}*[将该]{style="font-family:宋体"}[I]{lang="EN-US"}[帧上送]{style="font-family:宋体"}[Q931]{lang="EN-US"}*

[[\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_195058038}

[  ISDN L3 timer T303 stopped, Call Reference=0x0093.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}

[  ISDN L3 timer T310 started, Call Reference=0x0093.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:027 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}

[  ISDN Layer 3 call state change: CS_CALL_INITIATED-\>CS_OUTGOING_CALL_PROCEEDING]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:028 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=4 02 01 01 92]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=1, RR, nr=49, p/f=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x1838668682}*[发送]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧应答]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:083 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x2040839043}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=13 02 01 92 92 08 02 80 93 01 1E 02 82 81]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=1, I, ns=49, nr=49, p=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x607380923}*[收到对端发送的]{style="font-family:宋体"}[I]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_196041078}

[  Q921-\>Q931: DL_I_Data_Ind, CES=1]{lang="EN-US"}

[  cr_length=2, cr= 02 80 93, ALERTING, \*prog_ind= 1e 02 82 81]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_85873488}*[将该]{style="font-family:宋体"}[I]{lang="EN-US"}[帧上送]{style="font-family:宋体"}[Q931]{lang="EN-US"}*

[[\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_57066407}

[  ISDN L3 timer T310 stopped, Call Reference=0x0093.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:084 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}

[  ISDN Layer 3 call state change: CS_OUTGOING_CALL_PROCEEDING-\>CS_CALL_DELIVERED]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:085 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=4 02 01 01 94]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=1, RR, nr=4A, p/f=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x973466705}*[发送]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:089 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x1517896159}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=21 02 01 94 92 08 02 80 93 07 1E 02 82 81 29 06 0C 05 12 0A 21 1C]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=1, I, ns=4A, nr=49, p=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_958840888}*[收到对端发送的]{style="font-family:宋体"}[I]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:090 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_195975542}

[  Q921-\>Q931: DL_I_Data_Ind, CES=1]{lang="EN-US"}

[  cr_length=2, cr= 02 80 93, CONN, \*prog_ind= 1e 02 82 81, \*date/time= 29 06 0c 05 12 0a 21 1c]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_1133108651}*[将该]{style="font-family:宋体"}[I]{lang="EN-US"}[帧上送]{style="font-family:宋体"}[Q931]{lang="EN-US"}*

[[\*Dec 17 03:46:00:090 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_2056829401}

[  ISDN Layer 3 call state change: CS_CALL_DELIVERED-\>CS_CONNECT_REQUEST]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:091 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}

[  Q931-\>Q921: DL_I_Data_Req, CES=1]{lang="EN-US"}

[  cr_length=2, cr= 02 00 93, CONNECT_ACK]{lang="EN-US"}

[*[// Q931]{lang="EN-US"}*]{#struct_0_15329_14513_x615168059}*[下发发送]{style="font-family:宋体"}[I]{lang="EN-US"}[帧的请求]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:092 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_2018473708}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=9 00 01 92 96 08 02 00 93 0F]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=0, I, ns=49, nr=4B, p=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_195516787}*[向对端发送]{style="font-family:宋体"}[I]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:00:092 2011 RouterA ISDN/7/Q931: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x1653738312}

[  ISDN Layer 3 call state change: CS_CONNECT_REQUEST-\>CS_ACTIVE]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 17 03:46:00:099 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=4 00 01 01 94]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=0, RR, nr=4A, p/f=0]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x1207462803}*[收到]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:10:346 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x2132405735}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Rx: Len=4 02 01 01 95]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=1, RR, nr=4A, p/f=1]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_109398196}*[收到]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:10:347 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_195451251}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=4 02 01 01 97]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=1, RR, nr=4B, p/f=1]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x1338361031}*[发送]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:20:483 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x1829561587}

[  CES=1, Status=MULTIPLE_FRAME_ESTABLISHED]{lang="EN-US"}

[  User Tx: Len=4 00 01 01 97]{lang="EN-US"}

[  User Tx: sapi=00, tei=00, c/r=0, RR, nr=4B, p/f=1]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_177536342}*[发送]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*

[[\*Dec 17 03:46:20:490 2011 RouterA ISDN/7/Q921: Serial2/3/0:15]{lang="EN-US"}]{#struct_0_15329_14513_x224417342}

[  CES=1, Status=TIMER_RECOVERY]{lang="EN-US"}

[  User Rx: Len=4 00 01 01 95]{lang="EN-US"}

[  User Rx: sapi=00, tei=00, c/r=0, RR, nr=4A, p/f=1]{lang="EN-US"}

[*[// Q921]{lang="EN-US"}*]{#struct_0_15329_14513_x1209692991}*[收到]{style="font-family:宋体"}[RR]{lang="EN-US"}[帧]{style="font-family:宋体"}*
