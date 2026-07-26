::: {#-222193438 .myid}
[]{#_Toc404795567}[]{#struct_0_58685_x2140_x1092536207}[]{#_Toc263087402}

**RPR \-- RPR调试命令 \-- debugging rpr error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x761378791}

[**[debugging]{lang="EN-US"}**[ **rpr** **error** \[ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x45974495}

[**[undo]{lang="EN-US"}**[ **debugging** **rpr** **error** \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x1035591619}

[[【视图】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x255861556}

[[用户视图]{style="font-family:宋体"}]{#struct_0_58685_x2140_17403253}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_58685_x2140_827577931}

[[network-admin]{lang="EN-US"}]{#struct_0_58685_x2140_336606489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x144171587}

[[【参数】]{style="font-family:黑体"}]{#struct_0_58685_x2140_741770590}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_58685_x2140_844646571}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x997064917}

[**[debugging]{lang="EN-US"}**[ **rpr** **error**]{lang="EN-US"}]{#struct_0_58685_x2140_x1891764308}[命令用来打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rpr** **error**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_58685_x2140_1274775509}[错误调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging rpr error]{lang="EN-US"}]{#struct_0_58685_x2140_x1297378697}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2145873625}[[字段]{style="font-family:黑体"}]{#struct_0_58685_x2140_1939520946}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_58685_x2140_2142180468}

[[On interface *interface*, at east/west, *string*.]{lang="EN-US"}]{#struct_0_58685_x2140_x1833552146}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_x932285480}[在东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向上收到错误报文，错误原因为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a control frame with invalid head content]{lang="EN-US"}]{#struct_0_58685_x2140_x477259038}[：收到无效帧头的控制帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TP frame with invalid west protection state and discard it]{lang="EN-US"}]{#struct_0_58685_x2140_x1865619353}[：收到带有无效的西向保护状态的]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧，]{lang="EN-US" style="font-family:宋体"}[将其]{style="font-family:宋体"}[丢弃]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TP frame with invalid east protection state and discard it]{lang="EN-US"}]{#struct_0_58685_x2140_x196405984}[：收到带有无效的东向保护状态的]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧，]{lang="EN-US" style="font-family:宋体"}[将其]{style="font-family:宋体"}[丢弃]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TP frame with invalid version]{lang="EN-US"}]{#struct_0_58685_x2140_373437005}[：收到带有无效版本号的]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TP frame with invalid FCS]{lang="EN-US"}]{#struct_0_58685_x2140_355470386}[：收到带有无效帧检查序列的]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TC frame with invalid version]{lang="EN-US"}]{#struct_0_58685_x2140_x895041818}[：收到带有无效版本号的]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TC frame with invalid FCS]{lang="EN-US"}]{#struct_0_58685_x2140_862433445}[：收到带有无效帧检查序列的]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an ATD frame with invalid version]{lang="EN-US"}]{#struct_0_58685_x2140_2016967522}[：收到带有无效版本号的]{lang="EN-US" style="font-family:宋体"}[ATD]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an ATD frame with invalid FCS]{lang="EN-US"}]{#struct_0_58685_x2140_x1208718348}[：收到带有无效帧检查序列的]{lang="EN-US" style="font-family:宋体"}[ATD]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an ATD frame with invalid Resv Rate property]{lang="EN-US"}]{#struct_0_58685_x2140_x1990117455}[：收到带有无效保留速率值的]{lang="EN-US" style="font-family:宋体"}[ATD]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an ATD frame with invalid Manage IP property]{lang="EN-US"}]{#struct_0_58685_x2140_776721532}[：收到带有无效]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{lang="EN-US" style="font-family:宋体"}[ATD]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an ATD frame from unknown station]{lang="EN-US"}]{#struct_0_58685_x2140_1885110540}[：收到来自未知站点的]{lang="EN-US" style="font-family:宋体"}[ATD]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TP frame with invalid length]{lang="EN-US"}]{#struct_0_58685_x2140_x2038794409}[：收到无效长度的]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a TC frame with invalid length]{lang="EN-US"}]{#struct_0_58685_x2140_x849552023}[：收到无效长度的]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a]{lang="EN-US"}]{#struct_0_58685_x2140_405874679}[n]{lang="EN-US"}[ echo request with invalid ]{lang="EN-US"}[FCS]{lang="EN-US"}[：收到带有无效校验和的]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[cho]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a]{lang="EN-US"}]{#struct_0_58685_x2140_x713272120}[n]{lang="EN-US"}[ echo response with invalid ]{lang="EN-US"}[FCS]{lang="EN-US"}[：收到带有无效校验和的]{lang="EN-US" style="font-family:宋体"}[E]{lang="EN-US"}[cho]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received an unexpected echo response]{lang="EN-US"}]{#struct_0_58685_x2140_x789362409}[：没有进行]{lang="EN-US" style="font-family:宋体"}[Echo]{lang="EN-US"}[操作却收到了]{lang="EN-US" style="font-family:宋体"}[Echo]{lang="EN-US"}[回应报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[received a control frame with invalid type]{lang="EN-US"}]{#struct_0_58685_x2140_1608997746}[：收到类型无效的控制帧]{lang="EN-US" style="font-family:宋体"}

[[On interface *interface*, *string*.]{lang="EN-US"}]{#struct_0_58685_x2140_1198489751}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_x1701298511}[在拓扑计算时发生错误，错误原因为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC duplicate error: ringlet ]{lang="EN-US"}]{#struct_0_58685_x2140_x13353700}*[ringlet_id]{lang="FR"}*[ hop ]{lang="EN-US"}*[hop_id]{lang="FR"}*[ duplicate with local station]{lang="EN-US"}[：子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id]{lang="FR"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id]{lang="FR"}*[跳的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与本站点重复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC duplicate error: ringlet ]{lang="EN-US"}]{#struct_0_58685_x2140_1720485027}*[ringlet_id1]{lang="FR"}*[ hop ]{lang="EN-US"}*[hop_id1]{lang="FR"}*[ duplicate with ringlet ]{lang="EN-US"}*[ringlet_id2]{lang="FR"}*[ hop ]{lang="EN-US"}*[hop_id2]{lang="FR"}*[：子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id1]{lang="FR"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id1]{lang="FR"}*[跳的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id2]{lang="FR"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id2]{lang="FR"}*[跳的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址重复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP duplicate error: ringlet ]{lang="EN-US"}]{#struct_0_58685_x2140_x1045244532}*[ringlet_id]{lang="FR"}*[ hop ]{lang="EN-US"}*[hop_id]{lang="FR"}*[ duplicate with local station]{lang="EN-US"}[：子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id]{lang="FR"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id]{lang="FR"}*[跳的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址与本站点重复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[IP duplicate error: ringlet *ringlet_id1* hop *hop_id1* duplicate with ringlet *ringlet_id2* hop *hop_id2*]{lang="EN-US"}]{#struct_0_58685_x2140_179742619}[：子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id1]{lang="EN-US"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id1]{lang="EN-US"}*[跳的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址与子环]{lang="EN-US" style="font-family:宋体"}*[ringlet_id2]{lang="EN-US"}*[第]{lang="EN-US" style="font-family:宋体"}*[hop_id2]{lang="EN-US"}*[跳的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址重复]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x29847522}

[[\# ]{lang="EN-US"}]{#struct_0_58685_x2140_x514489352}[两个站点组成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环网，且为闭环。在接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[异常调试信息开关，把两个站点的]{style="font-family:宋体"}[IP]{lang="EN-US"}[配置相同。]{style="font-family:宋体"}

[[\<Sysname\> debugging rpr error interface rpr-router1]{lang="EN-US"}]{#struct_0_58685_x2140_358744798}

[\*Apr  1 09:40:54:540 2014 ]{lang="NL"}[Sysname]{lang="EN-US"}[ RPR/7/ERROR: -MDC=1; On interface RPR-Router1, IP duplicate error: ringlet 1 hop 1 duplicate with local station.]{lang="NL"}

[*[// ]{lang="NL"}*]{#struct_0_58685_x2140_1893780796}*[接口]{style="font-family:宋体"}[RPR-Router1]{lang="NL"}[在拓扑计算时发生]{style="font-family:宋体"}[IP]{lang="NL"}[地址重复错误]{style="font-family:宋体"}[，]{style="font-family:宋体"}[子环]{style="font-family:宋体"}[1]{lang="NL"}[第一跳的]{style="font-family:宋体"}[IP]{lang="NL"}[地址与本站点重复]{style="font-family:宋体"}*

::: {#-1920618589 .myid}
[]{#_Toc404795568}[]{#struct_0_58685_x2140_x1373874107}[]{#_Toc263087403}

**RPR \-- RPR调试命令 \-- debugging rpr event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_58685_x2140_1282142695}

[**[debugging]{lang="EN-US"}**[ **rpr** **event** \[ **general** \| **ringlet-selection** \] \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_579702294}

[**[undo]{lang="EN-US"}**[ **debugging** **rpr** **event** \[ **general** \| **ringlet-selection** \] \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x2012455314}

[[【视图】]{style="font-family:黑体"}]{#struct_0_58685_x2140_623886081}

[[用户视图]{style="font-family:宋体"}]{#struct_0_58685_x2140_x1038223201}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1595931463}

[[network-admin]{lang="EN-US"}]{#struct_0_58685_x2140_1138455933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_58685_x2140_466406801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1631479313}

[**[general]{lang="EN-US"}**]{#struct_0_58685_x2140_987177171}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[通用事件调试信息开关，包括保护状态变化、错纤变化、接口]{style="font-family:宋体"}[up/down]{lang="EN-US"}[等。]{style="font-family:宋体"}

[**[ringlet-selection]{lang="EN-US"}**]{#struct_0_58685_x2140_28433940}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[选环表事件调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_58685_x2140_1524392265}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x28893894}

[**[debugging]{lang="EN-US"}**[ **rpr** **event**]{lang="EN-US"}]{#struct_0_58685_x2140_x1807376269}[命令用来打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rpr** **event**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_58685_x2140_1472042148}[事件调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-2 ]{lang="EN-US"}[debugging rpr event]{lang="EN-US"}]{#struct_0_58685_x2140_x1192646936}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2147179168}[[字段]{style="font-family:黑体"}]{#struct_0_58685_x2140_x333402203}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_58685_x2140_1956105161}

[[On interface *interface*, *string* ringlet selection table was updated.]{lang="EN-US"}]{#struct_0_58685_x2140_x1432887827}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_x2026636204}[上更新]{style="font-family:宋体"}*[string]{lang="EN-US"}*[选环表结束。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[default]{lang="EN-US"}]{#struct_0_58685_x2140_861727532}[：默认选环表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_58685_x2140_1536236419}[：动态选环表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[overall]{lang="EN-US"}]{#struct_0_58685_x2140_384576551}[：综合选环表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}[-learning]{lang="EN-US"}]{#struct_0_58685_x2140_x475603545}[：]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习选环表]{lang="EN-US" style="font-family:宋体"}

[[On interface *interface*, *string*]{lang="EN-US"}]{#struct_0_58685_x2140_2100197216}[.]{lang="NL"}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_x1564117800}[上发生了]{style="font-family:宋体"}*[string]{lang="EN-US"}*[事件。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_active]{lang="EN-US"}]{#struct_0_58685_x2140_1583290586}[：逻辑接口激活]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_deactive]{lang="EN-US"}]{#struct_0_58685_x2140_969635755}[：逻辑接口去激活]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_up]{lang="EN-US"}]{#struct_0_58685_x2140_937814901}[：逻辑接口]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_down]{lang="EN-US"}]{#struct_0_58685_x2140_x2119157378}[：逻辑接口]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notify linkstatus_up]{lang="EN-US"}]{#struct_0_58685_x2140_x1955446421}[：通知接口管理逻辑口链路]{lang="EN-US" style="font-family:
  宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[notify linkstatus_down]{lang="EN-US"}]{#struct_0_58685_x2140_17206645}[：通知接口管理逻辑口链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[On interface *interface*, at ]{lang="EN-US"}[east/west span, *string*]{lang="EN-US"}]{#struct_0_58685_x2140_x2001579595}[.]{lang="NL"}

[[在]{style="font-family:宋体"}]{#struct_0_58685_x2140_1939586482}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向段上]{style="font-family:宋体"}[发生了]{style="font-family:宋体"}*[string]{lang="EN-US"}*[事件。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[m]{lang="EN-US"}[istake cable is occurred]{lang="EN-US"}]{#struct_0_58685_x2140_1036987210}[：发生错纤]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[p]{lang="EN-US"}[rotection status is changed]{lang="EN-US"}]{#struct_0_58685_x2140_2047850020}[：保护状态改变]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MATE status is changed]{lang="EN-US"}]{#struct_0_58685_x2140_466564687}[：]{lang="EN-US" style="font-family:宋体"}[MATE]{lang="EN-US"}[口状态改变]{lang="EN-US" style="font-family:宋体"}

[[On interface *interface*, at ringlet *ringlet_id*(*port*), *string*]{lang="EN-US"}]{#struct_0_58685_x2140_1463483185}[.]{lang="NL"}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_373502541}[在环]{style="font-family:宋体"}*[ringlet_id]{lang="FR"}*[（物理接口为]{style="font-family:宋体"}*[port]{lang="FR"}*[）上发生]{style="font-family:宋体"}*[string]{lang="EN-US"}*[事件。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_active]{lang="EN-US"}]{#struct_0_58685_x2140_1155450258}[：物理]{lang="EN-US" style="font-family:
  宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_deactive]{lang="EN-US"}]{#struct_0_58685_x2140_1671505032}[：物理]{lang="EN-US" style="font-family:
  宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[去激活]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[interface_up]{lang="EN-US"}]{#struct_0_58685_x2140_x135818699}[：物理]{lang="EN-US" style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[链路]{lang="EN-US" style="font-family:
  宋体"}[up]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[interface_down]{lang="EN-US"}]{#struct_0_58685_x2140_x1212708874}[：物理]{lang="EN-US" style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[链路]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}

[[On interface *interface*,]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_58685_x2140_2024004147}[received ]{lang="FR"}[IPv4/IPv6]{lang="EN-US"}[ ]{lang="EN-US"}[address change event, ]{lang="FR"}[IPv4/IPv6]{lang="EN-US"}[ address is *address*]{lang="FR"}[.]{lang="NL"}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_776787068}[上]{style="font-family:宋体"}[收到]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址改变事件，]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址变为]{style="font-family:宋体"}*[address]{lang="FR"}*

[ ]{lang="FR"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1608369339}

[[\# ]{lang="EN-US"}]{#struct_0_58685_x2140_x571218567}[两个站点组成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环网，且为闭环。打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[事件开关，配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> debugging rpr event general]{lang="EN-US"}]{#struct_0_58685_x2140_1029135614}

[\*Apr  1 09:44:38:177 2014 ]{lang="NL"}[Sysname]{lang="EN-US"}[ RPR/7/EVENT: -MDC=1; On interface RPR-Router1, received IPv4 address change event, IPv4 address is 1.5.3.6.]{lang="NL"}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_58685_x2140_1372509681}*[在接口]{style="font-family:
宋体"}[RPR-Router1]{lang="EN-US"}[上发生]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址改变事件，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址变为]{style="font-family:宋体"}[1.5.3.6]{lang="EN-US"}*

::: {#44955378 .myid}
[]{#_Toc404795569}[]{#struct_0_58685_x2140_654383865}[]{#_Toc263087404}

**RPR \-- RPR调试命令 \-- debugging rpr fsm**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_58685_x2140_184011827}

[**[debugging]{lang="EN-US"}**[ **rpr** **fsm** \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x789296873}

[**[undo]{lang="EN-US"}**[ **debugging** **rpr** **fsm** \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_1964125560}

[[【视图】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x998991178}

[[用户视图]{style="font-family:宋体"}]{#struct_0_58685_x2140_333427178}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_58685_x2140_650352580}

[[network-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x757576538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x1171310904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x359766120}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_58685_x2140_499005196}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_58685_x2140_1671155465}

[**[debugging]{lang="EN-US"}**[ **rpr** **fsm**]{lang="EN-US"}]{#struct_0_58685_x2140_x29781986}[命令用来打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rpr** **fsm**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_58685_x2140_x1094382284}[状态机调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-3 ]{lang="EN-US"}[debugging rpr fsm]{lang="EN-US"}]{#struct_0_58685_x2140_x706540543}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2144045597}[[字段]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1580207802}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_58685_x2140_1054726776}

[[On interface *interface*, at ]{lang="EN-US"}[east/west span, *string* protection switch is current.]{lang="EN-US"}]{#struct_0_58685_x2140_x41916139}

[[在]{style="font-family:宋体"}]{#struct_0_58685_x2140_x2025562760}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向段上]{style="font-family:宋体"}[发生了]{style="font-family:宋体"}*[string]{lang="EN-US"}*[保护事件。]{style="font-family:宋体"}*[string]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TP_RCVD]{lang="EN-US"}]{#struct_0_58685_x2140_x628314515}[：收到]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR_EXP]{lang="EN-US"}]{#struct_0_58685_x2140_x608424279}[：]{lang="EN-US" style="font-family:宋体"}[WTR]{lang="EN-US"}[定时器溢出]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO_IDLE]{lang="EN-US"}]{#struct_0_58685_x2140_x1595865927}[：链路恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO_SD]{lang="EN-US"}]{#struct_0_58685_x2140_416292871}[：信号减弱]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AUTO_SF]{lang="EN-US"}]{#struct_0_58685_x2140_266836135}[：信号消失]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADMIN_IDLE]{lang="EN-US"}]{#struct_0_58685_x2140_x19154113}[：手动恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADMIN_MS]{lang="EN-US"}]{#struct_0_58685_x2140_x1192382102}[：手动保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADMIN_FS]{lang="EN-US"}]{#struct_0_58685_x2140_537853229}[：强制保护]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MATE_IDLE]{lang="EN-US"}]{#struct_0_58685_x2140_1731267991}[：]{lang="EN-US" style="font-family:宋体"}[MATE]{lang="EN-US"}[口恢复]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MATE_SF]{lang="EN-US"}]{#struct_0_58685_x2140_1433253764}[：]{lang="EN-US" style="font-family:宋体"}[MATE]{lang="EN-US"}[口]{lang="EN-US" style="font-family:宋体"}[SF]{lang="EN-US"}

[[On interface *interface*, *state* state machine is running.]{lang="EN-US"}]{#struct_0_58685_x2140_x1192581400}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_2089346656}[上]{style="font-family:宋体"}[正在运行]{style="font-family:宋体"}*[state]{lang="EN-US"}*[状态机。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topology validation]{lang="EN-US"}]{#struct_0_58685_x2140_670651263}[：]{lang="EN-US" style="font-family:
  宋体"}[TopologyValidation]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[On interface *interface*, at ]{lang="EN-US"}[east/west span, *state* state machine is running.]{lang="EN-US"}]{#struct_0_58685_x2140_x401204120}

[[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_x59981014}[的]{style="font-family:宋体"}[东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向段]{style="font-family:宋体"}[上]{style="font-family:宋体"}[正在运行]{style="font-family:宋体"}*[state]{lang="EN-US"}*[状态机。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[receive TP]{lang="EN-US"}]{#struct_0_58685_x2140_x1636030812}[：]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[eceiveT]{lang="EN-US"}[pF]{lang="EN-US"}[rame]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topology control]{lang="EN-US"}]{#struct_0_58685_x2140_x948494214}[：]{lang="EN-US" style="font-family:
  宋体"}[TopologyControl]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[parse ]{lang="EN-US"}]{#struct_0_58685_x2140_1536301955}[TP]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[ParseTpFrame]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[protection update]{lang="EN-US"}]{#struct_0_58685_x2140_x1135501147}[：]{lang="EN-US" style="font-family:
  宋体"}[ProtectionUpdate]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[secondary update]{lang="EN-US"}]{#struct_0_58685_x2140_x591568887}[：]{lang="EN-US" style="font-family:
  宋体"}[SecondaryUpdate]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[On interface *interface*, *state* state machine: in stage *stage*.]{lang="EN-US"}]{#struct_0_58685_x2140_1728807221}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_1119469118}[上]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[状态机正处于]{style="font-family:宋体"}*[stage]{lang="EN-US"}*[阶段。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[topology validation]{lang="EN-US"}]{#struct_0_58685_x2140_x1981991715}[：]{lang="EN-US" style="font-family:
  宋体"}[TopologyValidation]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[*[stage]{lang="EN-US"}*]{#struct_0_58685_x2140_1583356122}[包括：]{style="font-family:宋体"}[START]{lang="EN-US"}[、]{style="font-family:宋体"}[UNSTABLE]{lang="EN-US"}[、]{style="font-family:宋体"}[STABLE]{lang="EN-US"}[、]{style="font-family:宋体"}[VALID]{lang="EN-US"}[和]{style="font-family:宋体"}[INVALID]{lang="EN-US"}

[[On interface *interface*, at ]{lang="EN-US"}[east/west span, *state* state machine: in stage *stage*.]{lang="EN-US"}]{#struct_0_58685_x2140_1391878344}

[[在接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*]{#struct_0_58685_x2140_1429910225}[的]{style="font-family:宋体"}[东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向段]{style="font-family:宋体"}[上]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[状态机正处于]{style="font-family:宋体"}*[stage]{lang="EN-US"}*[阶段。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[parse tp]{lang="EN-US"}]{#struct_0_58685_x2140_1452815031}[：]{lang="EN-US" style="font-family:宋体"}[ParseTpFrame]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[protection update]{lang="EN-US"}]{#struct_0_58685_x2140_x585310973}[：]{lang="EN-US" style="font-family:
  宋体"}[ProtectionUpdate]{lang="EN-US"}[状态机]{lang="EN-US" style="font-family:宋体"}

[*[stage]{lang="EN-US"}*]{#struct_0_58685_x2140_17272181}[包括：]{style="font-family:宋体"}[START]{lang="EN-US"}[、]{style="font-family:宋体"}[ADMIN]{lang="EN-US"}[、]{style="font-family:宋体"}[MAIN]{lang="EN-US"}[、]{style="font-family:宋体"}[MARK]{lang="EN-US"}[、]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[、]{style="font-family:宋体"}[WTRC]{lang="EN-US"}[、]{style="font-family:宋体"}[CLEAR]{lang="EN-US"}[、]{style="font-family:宋体"}[CHECK]{lang="EN-US"}[、]{style="font-family:宋体"}[FINAL]{lang="EN-US"}[、]{style="font-family:宋体"}[NEXT]{lang="EN-US"}[、]{style="font-family:宋体"}[TEST]{lang="EN-US"}[、]{style="font-family:宋体"}[DIFF]{lang="EN-US"}[、]{style="font-family:宋体"}[EXEC]{lang="EN-US"}[、]{style="font-family:宋体"}[CC]{lang="EN-US"}[和]{style="font-family:宋体"}[NEAR]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1644705539}

[[\# ]{lang="EN-US"}]{#struct_0_58685_x2140_x1538215611}[两个站点组成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环网，为站点执行绑定操作。]{style="font-family:宋体"}

[[\<Sysname\> debugging rpr fsm]{lang="EN-US"}]{#struct_0_58685_x2140_x1539412154}

[\*Apr  1 09:52:11:783 2014 Sysname RPR/7/FSM: -MDC=1; On interface RPR-Router1, topology control state machine is running.]{lang="EN-US"}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_58685_x2140_x123685327}*[接口]{style="font-family:
宋体"}[RPR-Router1]{lang="EN-US"}[上正在运行]{style="font-family:
宋体"}[TopologyControl]{lang="EN-US"}[状态机]{style="font-family:宋体"}*

[[\*Apr  1 09:52:11:783 2014 Sysname RPR/7/FSM: -MDC=1; On interface RPR-Router1, protection update state machine is running.]{lang="EN-US"}]{#struct_0_58685_x2140_1974379463}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_58685_x2140_x1588061259}*[接口]{style="font-family:
宋体"}[RPR-Router1]{lang="EN-US"}[上正在运行]{style="font-family:
宋体"}[ProtectionUpdate]{lang="EN-US"}[状态机]{style="font-family:宋体"}*

::: {#-1232116447 .myid}
[]{#_Toc404795570}[]{#struct_0_58685_x2140_1047310001}

**RPR \-- RPR调试命令 \-- debugging rpr packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_58685_x2140_475284473}

[**[debugging]{lang="EN-US"}**[ **rpr** **packet** \[ \[ ]{lang="EN-US"}**[atd]{lang="EN-US"}**[ \| **echo-request** \| **echo-response** \| **tc** \| **tp** \] \[ **receive** \| **send** \] \| { **tc** \| **tp** } **burst-send** \] \[ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x557433798}

[**[undo]{lang="EN-US"}**[ **debugging** **rpr** **packet** \[ \[ ]{lang="EN-US"}**[atd]{lang="EN-US"}**[ \| **echo-request** \| **echo-response** \| **tc** \| **tp** \] \[ **receive** \| **send** \] \| { **tc** \| **tp** } **burst-send** \] \[ **interface** { **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_1939389874}

[[【视图】]{style="font-family:黑体"}]{#struct_0_58685_x2140_2121549178}

[[用户视图]{style="font-family:宋体"}]{#struct_0_58685_x2140_484786422}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1745069315}

[[network-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x1157036999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x10271689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x859317564}

[**[atd]{lang="PT-BR"}**]{#struct_0_58685_x2140_x2144812559}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文]{style="font-family:宋体"}[ATD]{lang="PT-BR"}[帧]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[echo-request]{lang="PT-BR"}**]{#struct_0_58685_x2140_1129772595}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RPR]{lang="PT-BR"}[报文]{style="font-family:宋体"}[Echo]{lang="PT-BR"}[请求报文]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[echo-response]{lang="PT-BR"}**]{#struct_0_58685_x2140_x803660626}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RPR]{lang="PT-BR"}[报文]{style="font-family:宋体"}[Echo]{lang="PT-BR"}[响应报文]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[tc]{lang="PT-BR"}**]{#struct_0_58685_x2140_1373106594}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RPR]{lang="PT-BR"}[报文]{style="font-family:宋体"}[TC]{lang="PT-BR"}[帧]{style="font-family:宋体"}[调试信息开关。]{style="font-family:宋体"}

[**[tp]{lang="EN-US"}**]{#struct_0_58685_x2140_x1769475965}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文]{style="font-family:宋体"}[TP]{lang="EN-US"}[帧调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_58685_x2140_373305933}[：表示接收的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_58685_x2140_77348052}[：表示发送的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[burst-send]{lang="EN-US"}**]{#struct_0_58685_x2140_x551895655}[：表示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[快发报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_58685_x2140_x681137150}[：显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文的摘要信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_58685_x2140_x375086542}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1519141575}

[**[debugging]{lang="EN-US"}**[ **rpr** **packet**]{lang="EN-US"}]{#struct_0_58685_x2140_x555268289}[命令用来打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rpr** **packet**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_58685_x2140_1769248438}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_58685_x2140_x974016716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何报文类型，表示所有类型的]{style="font-family:宋体"}]{#struct_0_58685_x2140_x1645363908}[RPR]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_58685_x2140_776590460}**[receive]{lang="EN-US"}**[或]{style="font-family:宋体"}**[send]{lang="EN-US"}**[参数，表示所有快发的、接收的和发送的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging rpr packet]{lang="EN-US"}]{#struct_0_58685_x2140_x1536356966}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2144877466}[[字段]{style="font-family:黑体"}]{#struct_0_58685_x2140_718920326}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_58685_x2140_1634724117}

[[On interface *interface*, at ]{lang="EN-US"}[east/west span, *packet* packet was received/sent/burst-sent. *string*]{lang="EN-US"}]{#struct_0_58685_x2140_600457804}

[[在]{style="font-family:宋体"}]{#struct_0_58685_x2140_332376692}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[的]{style="font-family:宋体"}[东向]{style="font-family:宋体"}[/]{lang="EN-US"}[西向段上，]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[类型的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[报文被接收]{style="font-family:宋体"}[/]{lang="EN-US"}[发送]{style="font-family:宋体"}[/]{lang="EN-US"}[快发，报文内容为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[。]{style="font-family:宋体"}*[packet]{lang="EN-US"}*[包括：]{style="font-family:宋体"}[TP]{lang="EN-US"}[、]{style="font-family:宋体"}[TC]{lang="EN-US"}[、]{style="font-family:宋体"}[ATD]{lang="EN-US"}[、]{style="font-family:宋体"}[ECHO REQUEST]{lang="EN-US"}[和]{style="font-family:宋体"}[ECHO RESPONSE]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x863157687}

[[\# ]{lang="EN-US"}]{#struct_0_58685_x2140_x1837346570}[两个站点组成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环网，且为闭环。为站点]{style="font-family:宋体"}[1]{lang="EN-US"}[配置站点名称。]{style="font-family:宋体"}

[[\<Sysname\>debugging rpr packet atd verbose]{lang="EN-US"}]{#struct_0_58685_x2140_x789493481}

[\*Apr  1 09:54:59:728 2014 Sysname RPR/7/PKT: -MDC=1; On interface RPR-Router1, at west span, ATD packet was sent.]{lang="EN-US"}

[ ttl:255  ri:0  fe:0  ft:1  sc:3  we:0  parity:0]{lang="EN-US"}

[ DA:ffff-ffff-ffff  SA:00e0-0100-0002]{lang="EN-US"}

[ ttlBase:255  ef:0  fi:0  ps:0  so:0  res:0]{lang="EN-US"}

[ controlType:1  controlVersion:0]{lang="EN-US"}

[ Ringlet0 weight: 1, ringlet1 weight: 1]{lang="EN-US"}

[ Ringlet0 reserveband: 0, ringlet1 reserveband: 0]{lang="EN-US"}

[ Station setting: mulitichoke-user 0;conversative 0;badfcs-user 0]{lang="EN-US"}

[ Station name: test]{lang="EN-US"}

[ Manage address: 1.5.3.6]{lang="EN-US"}

[ Ifindex: 450]{lang="EN-US"}

[ Secondary mac1: 0000-0000-0000 Secondary mac2: 0000-0000-0000]{lang="EN-US"}

[*[//]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_58685_x2140_73519190}*[在接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[的西向段上，发送的]{style="font-family:宋体"}[ATD]{lang="EN-US"}[报文的全部内容]{style="font-family:宋体"}*

::: {#941214550 .myid}
[]{#_Toc404795571}[]{#struct_0_58685_x2140_x1807989548}[]{#_Toc263087406}

**RPR \-- RPR调试命令 \-- debugging rpr timer**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_58685_x2140_388137563}

[**[debugging]{lang="EN-US"}**[ **rpr** **timer** \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_x637225579}

[**[undo]{lang="EN-US"}**[ **debugging** **rpr** **timer** \[ **interface** ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number* \]]{lang="EN-US"}]{#struct_0_58685_x2140_2072222436}

[[【视图】]{style="font-family:黑体"}]{#struct_0_58685_x2140_573510009}

[[用户视图]{style="font-family:宋体"}]{#struct_0_58685_x2140_1154614270}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x29978594}

[[network-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x172588011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_58685_x2140_x403939959}

[[【参数】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x567801033}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **rpr-bridge** \| **rpr-router** } *interface-number*]{lang="EN-US"}]{#struct_0_58685_x2140_x1866492315}[：]{style="font-family:
宋体"}[指定]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口的接口类型和编号。不同型号的设备支持的]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_58685_x2140_x1439503247}

[**[debugging]{lang="EN-US"}**[ **rpr** **timer**]{lang="EN-US"}]{#struct_0_58685_x2140_x339410071}[命令用来打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **rpr** **timer**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[RPR]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[表1-5 ]{lang="EN-US"}[debugging rpr timer]{lang="EN-US"}]{#struct_0_58685_x2140_x1992301928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2144449542}[[字段]{style="font-family:黑体"}]{#struct_0_58685_x2140_1245020243}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_58685_x2140_453198810}

[[On interface *interface*, *timer* timer *string*]{lang="EN-US"}[.]{lang="EN-US"}]{#struct_0_58685_x2140_x1596062535}

[[在]{style="font-family:宋体"}]{#struct_0_58685_x2140_x1666369748}[接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[上，]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[定时器发生了]{style="font-family:宋体"}*[string]{lang="EN-US"}*[动作]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[timer]{lang="EN-US"}*]{#struct_0_58685_x2140_1332465261}[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fast TP]{lang="EN-US"}]{#struct_0_58685_x2140_18664846}[：]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧快发定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Slow TP]{lang="EN-US"}]{#struct_0_58685_x2140_x1798171017}[：]{lang="EN-US" style="font-family:宋体"}[TP]{lang="EN-US"}[帧慢发定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fast]{lang="EN-US"}]{#struct_0_58685_x2140_x1769482718}[ ]{lang="EN-US"}[TC]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[帧快发定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Slow TC]{lang="EN-US"}]{#struct_0_58685_x2140_x2096779957}[：]{lang="EN-US" style="font-family:宋体"}[TC]{lang="EN-US"}[帧慢发定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATD]{lang="EN-US"}]{#struct_0_58685_x2140_x2098786870}[：]{style="font-family:宋体"}[ATD]{lang="EN-US"}[帧发送定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WTR]{lang="EN-US"}]{#struct_0_58685_x2140_x1192778008}[：]{lang="EN-US" style="font-family:宋体"}[WTR]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold]{lang="EN-US"}]{#struct_0_58685_x2140_787905055}[O]{lang="EN-US"}[ff]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[Hold]{lang="EN-US"}[O]{lang="EN-US"}[ff]{lang="EN-US"}[定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stability]{lang="EN-US"}]{#struct_0_58685_x2140_x514253948}[：稳定定时器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OAM]{lang="EN-US"}]{#struct_0_58685_x2140_2013164581}[：站点间连通性检测定时器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Report Defect]{lang="EN-US"}]{#struct_0_58685_x2140_x1746089289}[：缺陷检测定时器]{lang="EN-US" style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_58685_x2140_x1130517205}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[starts]{lang="EN-US"}]{#struct_0_58685_x2140_2131918346}[：启动]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[stops]{lang="EN-US"}]{#struct_0_58685_x2140_1536105347}[：停止]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[expires]{lang="EN-US"}]{#struct_0_58685_x2140_x1549545992}[：超时]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_58685_x2140_1752939494}

[[\# ]{lang="EN-US"}]{#struct_0_58685_x2140_970871853}[两个站点组成]{style="font-family:宋体"}[RPR]{lang="EN-US"}[环网，且为闭环。打开]{style="font-family:宋体"}[RPR]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging rpr timer]{lang="EN-US"}]{#struct_0_58685_x2140_2142889605}

[\*May 19 05:53:58:088 2014 Sysname RPR/7/TIMER: -MDC=1; On interface RPR-Router1, Report Defect timer expires.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_58685_x2140_1633701824}*[在接口]{style="font-family:宋体"}[RPR-Router1]{lang="EN-US"}[上，缺陷检测定时器超时]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
